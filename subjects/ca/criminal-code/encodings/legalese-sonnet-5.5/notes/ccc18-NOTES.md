# NOTES.md -- part ccc18 of the Criminal Code (Canada), R.S.C., 1985, c. C-46: lines 10275-10956, sections 490.02 to 492.2

Status (first written 2026-11-13 by part agent `ccc18`, model Sonnet 5.5, on the local clock; last write 05:17; the lead dates the weekly-limit stop 2026-11-12T21:20Z; resumed and finished 2026-11-16 on the lead's message): the layer-1 modules, their tests, the seat layer and its cases exist and run clean on the stable binary 1.6.110 (main, e51181d, 2026-11-11), compared by `check.sh` with 1.6.109 (main, 4c887e0, 2026-11-04); every count below was printed by a command run in the resumed session (2026-11-16); the findings and fork rows that describe the text were written in the first session and not re-derived.
The text is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation (current to 2026-09-30); it is not the official text, and nothing here is claimed verified against the official text.
The French version is equally authoritative and is not among the sources; the quote lines are whole lines of the text.
The target is the stable `l4` (the brief's "main").
Where PLAN.md and the brief differ, the brief governs: PLAN.md section 1 says a part receives only `ccc-core`, while the brief says layer 1 imports `ccc-core` and `ccc-definitions`.
This part imports `ccc-core` only and takes every section 2 and 2.1 answer as a MAYBE BOOLEAN input named `s 2 <term>: ...` (PLAN.md section 4), so the swap at the merge is mechanical; `ccc-definitions` is not imported by any ccc18 module.

## What is encoded and what is not

Every provision of lines 10275-10956 (57 sections from 490.02 to 492.2: the Sex Offender Information Registration Act orders and obligations, ss 490.02 to 490.07; forfeiture of offence-related property, ss 490.1 to 490.9; forfeiture of weapons and ammunition, s 491; restitution of property obtained by crime, s 491.1; photographic evidence, s 491.2; seizure of explosives, s 492; tracking device and transmission data recorder warrants, ss 492.1 and 492.2) has a row in the coverage table and one disposition.
Nothing is `out-of-scope` or `deferred`.
Layer 1 is eight modules (`ccc18-soira-notice`, `-soira-foreign`, `-soira-itoa`, `-soira-offences`, `-soira-additional`, `ccc18-forfeiture`, `ccc18-weapons-evidence`, `ccc18-tracking`), each with a tests module `ccc18-tests-<name>.l4`; layer 2 is `ccc18-seat.l4` and `ccc18-cases-seat.l4`.
A decision function answers a MAYBE BOOLEAN (or a MAYBE of a type); a duty on a named party is also a regulative rule (`PARTY ... MUST/MAY ...`), traced in the tests.
The L4 files were written by Python generators kept in `../work/` (not shipped): every quote line and every `@ref` locator is read from the text by `gen.py`, never typed (`srcrefs.py check --strict` reports 0 problems on every module).

## Seat (ccc18)

The seat is a person who is, or may be, accused of an offence under the Criminal Code (the accused), asking on facts they can state whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply at each stage from arrest through trial, sentence and appeal, and what follows from a conviction (assumed, not ruled: Singapore's Penal Code is the model, per the maintainer's instruction of 2026-11-09, but this is a plain seat layer; no charge-generator contract).
In this range the person is asked: whether they can be served with a registration notice and when their obligation begins and ends; whether and when they may apply to be exempted from it or have it terminated; what they must tell a police service and by when; whether failing to comply, giving false information or breaching a restraint order is an offence and the most they can be punished; what property can be forfeited, whether they may get it back, and whether the court must or may order forfeiture; what evidence may be received against them without notice; and whether a warrant to track them or their communications is valid.
There is never a seat for an official: provisions that address only an official are asked for what they mean to the person (what may be done to them, what they must be given, and by when).
The seat layer has 58 questions under 8 `§` headings in the text's order, each named "Under section N, ..." with `@export`, and an `@desc` on every input worded as the person would be asked; each calls layer-1 functions (the table shows the first it calls; questions 1, 3, 5, 11, 33 and 34 compose several (computed by script)) and restates no rule.
`ccc18-cases-seat.l4` carries 171 assertions.
A seam input a person cannot state (an answer of the keel or another part, typed MAYBE BOOLEAN in layer 1) is asked as the person's own fact, a yes or no, and wrapped in `JUST`: that is their fact, not a conversion of NOTHING to FALSE (Seams, below).

### The seat questions (ccc18)

Each row: number, the question as named (the `DECIDE` name, which the cases call), what the answer is, and the layer-1 function it calls.
Section groups are in the text's order.


**§ Sex offender registration: a notice served on you for an earlier conviction (sections 490.02 to 490.029)**

| # | question | answer | calls |
| --- | --- | --- | --- |
| 1 | `Under section 490.02, may the Attorney General or minister of justice serve me with a notice` | MAYBE BOOLEAN | `s 490.02 the notice may be served, subject to subsection (2)` |
| 2 | `Under section 490.021(1), was my notice served within one year after the day the Sex Offender Information Registration Act came into force` | MAYBE BOOLEAN | `s 490.021(1) the notice is served within one year after the day on which the Sex Offender Information Registration Act comes into force` |
| 3 | `Under section 490.021, is the way my notice was served one the section allows` | MAYBE BOOLEAN | `s 490.021 the manner of service is one the section allows` |
| 4 | `Under section 490.022(1), on what day does my obligation to comply with the Sex Offender Information Registration Act begin` | DATE | `s 490.022(1) the day on which the obligation under section 490.019 begins` |
| 5 | `Under section 490.022, when does my obligation end, or does it apply for life` | MAYBE `s 490.022(3) end of the obligation` | `s 490.022 the obligation ends, or applies for life` |
| 6 | `Under section 490.023(1), may I apply for an exemption order` | MAYBE BOOLEAN | `s 490.023(1) the person may apply for an exemption order` |
| 7 | `Under section 490.023(2), must the court make an exemption order` | MAYBE BOOLEAN | `s 490.023(2) the court shall make an exemption order` |
| 8 | `Under section 490.026(2), may I apply for a termination order now, the period since my sentence having elapsed` | MAYBE BOOLEAN | `s 490.026(2) the person may apply for a termination order, the period since sentence having elapsed` |
| 9 | `Under section 490.026(5), may I apply again for a termination order` | MAYBE BOOLEAN | `s 490.026(5) the person may apply again for a termination order` |
| 10 | `Under section 490.027(1), must the court make an order terminating my obligation` | MAYBE BOOLEAN | `s 490.027(1) the court shall make an order terminating the obligation` |

**§ Sex offender registration: a conviction outside Canada (sections 490.02901 to 490.02911)**

| # | question | answer | calls |
| --- | --- | --- | --- |
| 11 | `Under section 490.02902, may the Attorney General or minister of justice serve me with a notice in Form 54` | MAYBE BOOLEAN | `s 490.02902 the notice in Form 54 may be served, subject to subsection (2)` |
| 12 | `Under section 490.02903(1), is the way my notice in Form 54 was served the one the subsection requires` | MAYBE BOOLEAN | `s 490.02903(1) the manner of service is the one the subsection requires` |
| 13 | `Under section 490.02904(3), if subsection (2) does not apply, when does my obligation under section 490.02901 end, or does it apply for life` | MAYBE `s 490.022(3) end of the obligation` | `s 490.02904(3) the obligation, if subsection (2) does not apply, ends or applies for life` |
| 14 | `Under section 490.02905(1), may I apply for an exemption order from a notice in Form 54` | MAYBE BOOLEAN | `s 490.02905(1) the person may apply for an exemption order` |
| 15 | `Under section 490.02908(2), may I apply for a termination order of the Form 54 obligation, the period since my sentence having elapsed` | MAYBE BOOLEAN | `s 490.02908(2) the person may apply for a termination order, the period since sentence having elapsed` |
| 16 | `Under section 490.02911(1), must I advise a police service after I arrive in Canada` | MAYBE BOOLEAN | `s 490.02911(1) the person must advise a police service` |
| 17 | `Under section 490.02911(1), did I advise a police service within seven days after the day I arrived in Canada` | MAYBE BOOLEAN | `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada` |
| 18 | `Under section 490.02911(2), must I advise a police service of a change in address` | MAYBE BOOLEAN | `s 490.02911(2) the person must advise a police service of a change in address` |
| 19 | `Under section 490.02911(2), did I advise a police service of the change in address within seven days after the change` | MAYBE BOOLEAN | `s 490.02911(2) the person advised a police service of the change in address within seven days after the day on which the change was made` |

**§ Sex offender registration: a transfer to Canada under the International Transfer of Offenders Act (sections 490.029111 to 490.02915)**

| # | question | answer | calls |
| --- | --- | --- | --- |
| 20 | `Under section 490.029111(1), may I apply for an exemption order after my transfer to Canada` | MAYBE BOOLEAN | `s 490.029111(1) the person may apply for an exemption order` |
| 21 | `Under section 490.02912(2), may I apply for a termination order of the section 36.1 obligation, the period since my sentence having elapsed` | MAYBE BOOLEAN | `s 490.02912(2) the person may apply for a termination order, the period since sentence having elapsed` |
| 22 | `Under section 490.02915(2), must the Review Board cause a copy of the Form 1 to be given to me` | MAYBE BOOLEAN | `s 490.02915(2) the Review Board must cause a copy of the Form 1 to be given to the person` |

**§ Offences about the registration orders and obligations, and the warrant (sections 490.03 to 490.03121)**

| # | question | answer | calls |
| --- | --- | --- | --- |
| 23 | `Under section 490.031(1), am I guilty of an offence for failing to comply with an order or obligation` | MAYBE BOOLEAN | `s 490.031(1) the person is guilty of an offence` |
| 24 | `Under section 490.031(1), what is the most I can be punished on conviction on indictment` | Punishment | `s 490.031(1)(a) the punishment on conviction on indictment` |
| 25 | `Under section 490.031(1), what is the most I can be punished on summary conviction` | Punishment | `s 490.031(1)(b) the punishment on summary conviction` |
| 26 | `Under section 490.031(5), is a certificate barred from being received in evidence against me` | MAYBE BOOLEAN | `s 490.031(5) the certificate is not to be received in evidence` |
| 27 | `Under section 490.0311, am I guilty of an offence for knowingly giving false or misleading information` | MAYBE BOOLEAN | `s 490.0311 the person is guilty of an offence` |
| 28 | `Under section 490.0312, am I guilty of an offence for failing to advise a police service` | MAYBE BOOLEAN | `s 490.0312 the person is guilty of an offence` |
| 29 | `Under section 490.03121(1), may a justice issue a warrant in Form 6.4 to arrest me` | MAYBE BOOLEAN | `s 490.03121(1) the justice may issue a warrant in Form 6.4 to arrest the person` |
| 30 | `Under section 490.03121(5), is a charge barred for a contravention I remedied after the warrant was issued` | MAYBE BOOLEAN | `s 490.03121(5) no charge shall be laid against the person in respect of the contravention` |

**§ Additional orders for earlier orders and obligations (sections 490.04 to 490.07)**

| # | question | answer | calls |
| --- | --- | --- | --- |
| 31 | `Under section 490.04(1), may I apply to a court for an exemption order` | MAYBE BOOLEAN | `s 490.04(1) the person may apply to a court for an exemption order` |
| 32 | `Under section 490.04(4), is the court barred from making an exemption order` | MAYBE BOOLEAN | `s 490.04(4) the court shall not make an exemption order` |

**§ Forfeiture of offence-related property, restraint orders and management orders (sections 490.1 to 490.9)**

| # | question | answer | calls |
| --- | --- | --- | --- |
| 33 | `Under section 490.1(1), must the court order my property forfeited, subject to sections 490.3 to 490.41` | MAYBE BOOLEAN | `s 490.1(1) the court shall order the property forfeited, subject to sections 490.3 to 490.41` |
| 34 | `Under section 490.2(2), must a judge order the property forfeited because the accused has died or absconded, subject to sections 490.3 to 490.41` | MAYBE BOOLEAN | `s 490.2(2) the judge shall order the property forfeited, subject to sections 490.3 to 490.41` |
| 35 | `Under section 490.3, may the court set aside a transfer of the property` | MAYBE BOOLEAN | `s 490.3 the court may set aside the conveyance or transfer` |
| 36 | `Under section 490.4(3), may the court order that the property be returned to me` | MAYBE BOOLEAN | `s 490.4(3) the court may order that the property be returned to the person` |
| 37 | `Under section 490.41(3), may the court decide not to order the forfeiture because it would be disproportionate` | MAYBE BOOLEAN | `s 490.41(3) (decision) the court may decide not to order the forfeiture of the property or part of the property` |
| 38 | `Under section 490.5(1), may I apply for an order that my interest in the forfeited property is not affected` | MAYBE BOOLEAN | `s 490.5(1) the person may apply for an order under subsection (4)` |
| 39 | `Under section 490.5(4), may the judge declare that my interest is not affected by the forfeiture` | MAYBE BOOLEAN | `s 490.5(4) the judge may make an order declaring that the interest of the applicant is not affected by the forfeiture` |
| 40 | `Under section 490.7, is the property barred from being disposed of until thirty days have expired` | MAYBE BOOLEAN | `s 490.7 the property shall not be disposed of or otherwise dealt with` |
| 41 | `Under section 490.8(3), may a judge make a restraint order prohibiting me from dealing with the property` | MAYBE BOOLEAN | `s 490.8(3) the judge may make a restraint order` |
| 42 | `Under section 490.8(9), am I guilty of an offence for breaching a restraint order` | MAYBE BOOLEAN | `s 490.8(9) the person is guilty of an offence` |
| 43 | `Under section 490.8(9), what is the most I can be punished on conviction on indictment for breaching a restraint order` | Punishment | `s 490.8(9)(a) the punishment on conviction on indictment` |
| 44 | `Under section 490.8(9), what is the most I can be punished on summary conviction for breaching a restraint order` | Punishment | `s 490.8(9)(b) the punishment on summary conviction` |

**§ Forfeiture of weapons, restitution of property obtained by crime, photographic evidence and explosives (sections 491 to 492)**

| # | question | answer | calls |
| --- | --- | --- | --- |
| 45 | `Under section 491(1), is a thing seized from me forfeited to Her Majesty` | MAYBE BOOLEAN | `s 491(1) the thing is forfeited to Her Majesty` |
| 46 | `Under section 491(2), what order must the court make for me as the lawful owner of a seized thing` | `s 491(2) order` | `s 491(2) the order the court shall make` |
| 47 | `Under section 491.1(2), what order must the court make about property obtained by crime` | MAYBE `s 491.1(2) order` | `s 491.1(2) the order the court shall make` |
| 48 | `Under section 491.1(3), is an order for return or forfeiture of the property barred` | MAYBE BOOLEAN | `s 491.1(3) an order shall not be made under subsection (2)` |
| 49 | `Under section 491.2(5), is the photograph, certificate, affidavit or solemn declaration barred from being received in evidence against me` | MAYBE BOOLEAN | `s 491.2(5) the photograph, certificate, affidavit or solemn declaration shall not be received in evidence` |
| 50 | `Under section 492(1), may the person executing a warrant seize my explosive substance` | MAYBE BOOLEAN | `s 492(1) the person may seize the thing` |
| 51 | `Under section 492(2), is the thing seized forfeited on my conviction` | MAYBE BOOLEAN | `s 492(2) the thing is forfeited and shall be dealt with as the court directs` |

**§ Tracking device and transmission data warrants (sections 492.1 and 492.2)**

| # | question | answer | calls |
| --- | --- | --- | --- |
| 52 | `Under section 492.1(1), may a justice or judge issue a warrant to track a transaction or a thing of mine` | MAYBE BOOLEAN | `s 492.1(1) the justice or judge may issue a warrant for a tracking device` |
| 53 | `Under section 492.1(2), may a justice or judge issue a warrant to track me as an individual` | MAYBE BOOLEAN | `s 492.1(2) the justice or judge may issue a warrant for a tracking device, for an individual` |
| 54 | `Under section 492.1(5), is a tracking device warrant valid for the period it specifies because that period ends within 60 days` | MAYBE BOOLEAN | `s 492.1(5) the warrant is valid for the period specified in it` |
| 55 | `Under section 492.1(6), is a tracking device warrant valid for up to one year for an organized crime or terrorism offence` | MAYBE BOOLEAN | `s 492.1(6) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| 56 | `Under section 492.2(1), may a justice or judge issue a warrant for a transmission data recorder on my communications` | MAYBE BOOLEAN | `s 492.2(1) the justice or judge may issue a warrant for a transmission data recorder` |
| 57 | `Under section 492.2(3), is a transmission data recorder warrant barred because its purpose is to obtain tracking data` | MAYBE BOOLEAN | `s 492.2(3) no warrant shall be issued under this section` |
| 58 | `Under section 492.2(4), is a transmission data recorder warrant valid for the period it specifies because that period ends within 60 days` | MAYBE BOOLEAN | `s 492.2(4) the warrant is valid for the period specified in it` |

### Seat audit of 2026-11-12 (the first direction audit and the second pass; ccc18)

Written 2026-11-16 (the instruction is dated 2026-11-12).
The first direction audit (done on 2026-11-13, when the seat layer was written) read each question's name beside the name of the function it calls and found no mismatch of direction or of subject.
The second pass of 2026-11-12 (`seat-audit-second-pass.md`, done in the resumed session on 2026-11-16) read every question's name and `@export` text against the BODY of the layer-1 function it calls (its branches and its inputs), not against its own title, by the four tests of the tightened rule (a different limb, route or scope; a premise or consequence the function does not compute; a wrong polarity or modal; a different type of answer).
It found three mismatches of route that the first audit had missed.

- **Seat questions read: 58.
  Mismatched and retitled: 3 (direction 0, subject or route 3).
  Read and left: 55.**
- Direction (a question titled "may" over a bar, or the reverse): none.
  The bars are titled as bars (questions 26, 30, 32, 40, 48, 49, 57); the powers as powers; the duties as duties; the offences as offences.
- Retitled, each by the one route its function answers (the `@export` text and the `DECIDE` name changed together; the cases call the new name and each restated assertion carries `-- RECONCILED 2026-11-12: was <the original assertion>`; 8 assertions restated, answers unchanged):
  - question 13: `Under section 490.02904(3), if subsection (2) does not apply, when does my obligation under section 490.02901 end, or does it apply for life`
    - export text: Under section 490.02904(3), if subsection (2) does not apply (no exemption order has been made), when does my obligation under section 490.02901 end, or does it apply for life (by the maximum term in Canadian law for the equivalent offence)?
  - question 54: `Under section 492.1(5), is a tracking device warrant valid for the period it specifies because that period ends within 60 days`
    - export text: Under section 492.1(5), is a tracking device warrant valid for the period specified in it because that period ends no more than 60 days after the day it was issued (a longer period is for subsection (6))?
  - question 58: `Under section 492.2(4), is a transmission data recorder warrant valid for the period it specifies because that period ends within 60 days`
    - export text: Under section 492.2(4), is a transmission data recorder warrant valid for the period specified in it because that period ends no more than 60 days after the day it was issued (a longer period is for subsection (5))?
- The function and its answer are unchanged in each case: the question now asks what the function answers.
  Negating an answer was not used anywhere.
- Read and left (one line of reason each; "premise is an input" means the title repeats the text's own "if" words and the function tests them as separate inputs, so a failed premise answers what the function says, never the opposite):

| # | verdict | reason |
| --- | --- | --- |
| 1 | left | power titled as a power over `s 490.02 ... may be served, subject to subsection (2)`; both limbs, (1) and (2), are composed in the body |
| 2 | left | restates the function's own name (the one-year window after commencement) |
| 3 | left | restates the function's own name; the cases of subsections (2) to (4) are in the body |
| 4 | left | asks a day and the function returns the day (a DATE, as the title says) |
| 5 | left | asks end-or-life and the function composes subsections (2) and (3), as the title says |
| 6 | left | power over power; the window and the 490.012 limb are both computed, and the title names the window |
| 7 | left | duty over `the court shall make`; the premise "if it is satisfied" is the function's own input (the text's words) |
| 8 | left | power over power; the period limb is named in the title as in the function's name, and the answer is JUST TRUE or NOTHING (never JUST FALSE) |
| 9 | left | power over power; "after my application was refused" is the function's first input and a missing refusal answers NOTHING |
| 10 | left | duty over `shall make`; the premises are the function's inputs |
| 11 | left | power over power; subsections (1) and (2) are composed |
| 12 | left | restates the function's own name |
| 13 | RETITLED | the body answers subsection (3) only, which applies "if subsection (2) does not apply" (the obligation ends earlier on the day an exemption order is made); the title asked when the obligation ends, so the end date (or "for life") in the answer could be read as the end although an exemption order may end it sooner |
| 14 | left | power over power; the window, the service and the court are all computed |
| 15 | left | power over power; same shape as 8 |
| 16 | left | duty over duty; "within seven days" is the duty's own period in the text (the timing test is the next question) |
| 17 | left | restates the function's own name |
| 18 | left | duty over duty; "if they are in Canada" is the function's input |
| 19 | left | restates the function's own name |
| 20 | left | power over power; the window is computed |
| 21 | left | power over power; same shape as 8 |
| 22 | left | duty over duty; "when it discharges me" is tested by the function's two discharge inputs |
| 23 | left | offence over offence; the elements in the title are the function's inputs, and an unmet element answers NOTHING, not JUST FALSE |
| 24 | left | asks the most (a Punishment record) and the function returns the record |
| 25 | left | same as 24 |
| 26 | left | bar titled as a bar; JUST TRUE = barred |
| 27 | left | offence over offence (same as 23) |
| 28 | left | offence over offence (same as 23) |
| 29 | left | power over power; JUST FALSE never arises (NOTHING when not satisfied) |
| 30 | left | bar titled as a bar |
| 31 | left | power over power; paragraphs (a) and (b) are both computed |
| 32 | left | bar titled as a bar; the "application under paragraph (1)(a)" is the function's first input |
| 33 | left | duty over `shall`; "subject to sections 490.3 to 490.41" is carried by the function; "after my conviction" is an input that also takes a discharge under section 730 |
| 34 | left | duty over duty; "subject to" is carried by the function |
| 35 | left | power over power; the "unless" limb is in the body and the title does not claim to ignore it |
| 36 | left | power over power; the premises in the title are inputs, and the exclusion answers JUST FALSE, not a grant |
| 37 | left | power over power; premise is the function's input |
| 38 | left | power over power; window, exclusion and notice are all computed |
| 39 | left | power over power (a may-where function, listed in F18) |
| 40 | left | bar titled as a bar; the "until thirty days" limb is the one the title names |
| 41 | left | power over power |
| 42 | left | offence over offence |
| 43 | left | asks the most; the function returns the record |
| 44 | left | asks the most; the title says the paragraph states no penalty and the record says so |
| 45 | left | asks subsection (1) as named; "subject to subsection (2)" is the next question (46), and JUST FALSE means "not forfeited by (1)", which (2) cannot undo |
| 46 | left | asks the order and the function returns the order (a constructor, with a "no order required" value) |
| 47 | left | asks the order and the function returns the order |
| 48 | left | bar titled as a bar |
| 49 | left | bar titled as a bar |
| 50 | left | power over power |
| 51 | left | forfeiture over forfeiture; "if I am convicted" is the function's input |
| 52 | left | power over power |
| 53 | left | power over power |
| 54 | RETITLED | the body tests the 60-day route of subsection (5), which is "subject to subsection (6)"; the title asked whether the warrant is valid, so JUST FALSE could be read as "not valid" although subsection (6) may allow a year |
| 55 | left | asks the one-year route of subsection (6) and says so ("up to one year"); the body answers that route |
| 56 | left | power over power |
| 57 | left | bar titled as a bar; "because its purpose is to obtain tracking data" is the function's input |
| 58 | RETITLED | same as 54: the 60-day route of subsection (4), subject to subsection (5) |

## Coverage (ccc18)

Built by `work/units.py` from the text itself (one row per section, subsection, paragraph, subparagraph, defined term, group heading and repealed marker of lines 10275-10956) and mapped to the modules by `work/mknotes.py`; every row has exactly one disposition.

**Audit counts.**
Text units counted by an independent recount (a second code path in `mknotes.py` reading the same lines): 57 section lines, 212 subsection lines (2 of them repealed), 195 paragraph lines, 13 subparagraph lines, 12 defined terms, 8 group headings; 673 non-blank lines and 15662 words in the range (the brief says 15,662 words: it matches).
Rows in the table before the audit: 497; after: 497 (the audit found no unit missing and removed none).
Non-blank lines in no row: 0.

**Dispositions.** encoded: 342; fork: 142; inert: 11 (reason 1, headings: 8; reason 2, machinery: 3, the three rows of s 490.032, the regulation-making power); repealed or blank in this text: 2 (490.03(4) and 490.1(1.1)); total 497.
There is no `out-of-scope` row and no `deferred` row.
A parent row (a section, or a subsection with paragraphs) reads `fork` when any unit below it does; the forks are named in the Fork register.

Layer 1 holds 486 units: 274 decision functions, 85 regulative rules (87 traced), 127 declarations of types.

| row | lines | disposition | L4 name |
| --- | --- | --- | --- |
| s 490.02 | 10275-10287 | encoded | its rows below (5 units, module ccc18-soira-notice) |
| s 490.02(1) | 10276-10280 | encoded | `s 490.02(1) the Attorney General or minister of justice may serve the person with a notice`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(1)(a) | 10277-10277 | encoded | `s 490.02(1) the Attorney General or minister of justice may serve the person with a notice`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(1)(b) | 10278-10280 | encoded | `s 490.02(1) the Attorney General or minister of justice may serve the person with a notice`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(1)(b)(i) | 10279-10279 | encoded | `s 490.02(1) the Attorney General or minister of justice may serve the person with a notice`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(1)(b)(ii) | 10280-10280 | encoded | `s 490.02(1) the Attorney General or minister of justice may serve the person with a notice`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(2) | 10281-10285 | encoded | `s 490.02(2) a notice shall not be served on the person`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(2)(a) | 10283-10283 | encoded | `s 490.02(2) a notice shall not be served on the person`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(2)(b) | 10284-10284 | encoded | `s 490.02(2) a notice shall not be served on the person`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(2)(c) | 10285-10285 | encoded | `s 490.02(2) a notice shall not be served on the person`; `s 490.02 the notice may be served, subject to subsection (2)` |
| s 490.02(3) | 10286-10287 | encoded | `s 490.02(3) the reference is to the provision as it read from time to time before the day on which the subsection comes into force` |
| s 490.021 | 10288-10302 | fork (F3, F5) | its rows below (14 units, module ccc18-soira-notice) |
| s 490.021(1) | 10289-10289 | fork (F3) | `s 490.021(1) one year after the day`; `s 490.021(1) the notice is served within one year after the day on which the Sex Offender Information Registration Act comes into force`; `s 490.021 the manner of service is one the section allows` |
| s 490.021(2) | 10290-10291 | fork (F5) | `s 490.021(2) the notice may be served by registered mail at the person's last known address`; `s 490.021 the manner of service is one the section allows` |
| s 490.021(3) | 10292-10293 | fork (F5) | `s 490.021(3) the notice may be served by registered mail at the person's last known address, the person not being in compliance with the Ontario Act`; `s 490.021 the manner of service is one the section allows` |
| s 490.021(4) | 10294-10295 | fork (F5) | `s 490.021(4) the notice may be served by registered mail at the person's last known address, the person having failed to comply`; `s 490.021(4) the notice is served within one year after the day on which the person failed to comply`; `s 490.021 the manner of service is one the section allows` |
| s 490.021(5) | 10296-10300 | encoded | `s 490.021(5) the affidavit is evidence of the service and the notice` |
| s 490.021(5)(a) | 10298-10298 | encoded | `s 490.021(5) the affidavit is evidence of the service and the notice` |
| s 490.021(5)(b) | 10299-10299 | encoded | `s 490.021(5) the affidavit is evidence of the service and the notice` |
| s 490.021(5)(c) | 10300-10300 | encoded | `s 490.021(5) the affidavit is evidence of the service and the notice` |
| s 490.021(6) | 10301-10302 | encoded | `s 490.021(6) the person who served the notice must send a copy of the affidavit and the notice`; `s 490.021(6) the duty of the person who served the notice, without delay` |
| s 490.022 | 10303-10319 | encoded | its rows below (13 units, module ccc18-soira-notice) |
| s 490.022(1) | 10304-10306 | encoded | `s 490.022(1) the day on which the obligation under section 490.019 begins` |
| s 490.022(1)(a) | 10305-10305 | encoded | `s 490.022(1) the day on which the obligation under section 490.019 begins` |
| s 490.022(1)(b) | 10306-10306 | encoded | `s 490.022(1) the day on which the obligation under section 490.019 begins` |
| s 490.022(2) | 10307-10311 | encoded | `s 490.022(2) the earliest day on which the obligation ends`; `s 490.022 the obligation ends, or applies for life` |
| s 490.022(2)(a) | 10309-10309 | encoded | `s 490.022(2) the earliest day on which the obligation ends`; `s 490.022 the obligation ends, or applies for life` |
| s 490.022(2)(b) | 10310-10310 | encoded | `s 490.022(2) the earliest day on which the obligation ends`; `s 490.022 the obligation ends, or applies for life` |
| s 490.022(2)(c) | 10311-10311 | encoded | `s 490.022(2) the earliest day on which the obligation ends`; `s 490.022 the obligation ends, or applies for life` |
| s 490.022(3) | 10312-10317 | encoded | `s 490.022(3) the band of the maximum term of imprisonment`; `s 490.022(3) the day a number of years after the day`; `s 490.022(3) the obligation, if none of paragraphs (2)(a) to (c) applies earlier, ends or applies for life` (+1 more in the same unit) |
| s 490.022(3)(a) | 10314-10314 | encoded | `s 490.022(3) the band of the maximum term of imprisonment`; `s 490.022(3) the day a number of years after the day`; `s 490.022(3) the obligation, if none of paragraphs (2)(a) to (c) applies earlier, ends or applies for life` (+1 more in the same unit) |
| s 490.022(3)(b) | 10315-10315 | encoded | `s 490.022(3) the band of the maximum term of imprisonment`; `s 490.022(3) the day a number of years after the day`; `s 490.022(3) the obligation, if none of paragraphs (2)(a) to (c) applies earlier, ends or applies for life` (+1 more in the same unit) |
| s 490.022(3)(c) | 10316-10316 | encoded | `s 490.022(3) the band of the maximum term of imprisonment`; `s 490.022(3) the day a number of years after the day`; `s 490.022(3) the obligation, if none of paragraphs (2)(a) to (c) applies earlier, ends or applies for life` (+1 more in the same unit) |
| s 490.022(3)(d) | 10317-10317 | encoded | `s 490.022(3) the band of the maximum term of imprisonment`; `s 490.022(3) the day a number of years after the day`; `s 490.022(3) the obligation, if none of paragraphs (2)(a) to (c) applies earlier, ends or applies for life` (+1 more in the same unit) |
| s 490.022(4) | 10318-10319 | encoded | `s 490.022(4) the reference is to the definition as it read from time to time before the day on which the subsection comes into force` |
| s 490.023 | 10320-10331 | encoded | its rows below (13 units, module ccc18-soira-notice) |
| s 490.023(1) | 10321-10321 | encoded | `s 490.023(1) the person may apply for an exemption order` |
| s 490.023(1.1) | 10322-10325 | encoded | `s 490.023(1.1) the application shall be made to a court of criminal jurisdiction` |
| s 490.023(1.1)(a) | 10324-10324 | encoded | `s 490.023(1.1) the application shall be made to a court of criminal jurisdiction` |
| s 490.023(1.1)(b) | 10325-10325 | encoded | `s 490.023(1.1) the application shall be made to a court of criminal jurisdiction` |
| s 490.023(2) | 10326-10327 | encoded | `s 490.023(2) the court shall make an exemption order`; `s 490.023(2) the duty of the court` |
| s 490.023(3) | 10328-10329 | encoded | `s 490.023(3) the court shall give reasons for its decision`; `s 490.023(3) the duty of the court` |
| s 490.023(4) | 10330-10331 | encoded | `s 490.023(4) the court shall also make an order for removal of the information from the database`; `s 490.023(4) the duty of the court` |
| s 490.024 | 10332-10335 | fork (F5) | its rows below (10 units, module ccc18-soira-notice) |
| s 490.024(1) | 10333-10333 | fork (F5) | `s 490.024(1) the appeal court may do it`; `s 490.024(1) the appeal may be brought` |
| s 490.024(2) | 10334-10335 | encoded | `s 490.024(2) the appeal court shall also make an order for removal of the information from the database`; `s 490.024(2) the duty of a court of appeal` |
| s 490.025 | 10336-10337 | encoded | `s 490.025 the court shall cause the notification and the information to be given`; `s 490.025 the duty of the court to cause the Commissioner and the Attorney General to be notified`; `s 490.025 the duty of the court to cause the person to be informed of the sections` |
| s 490.026 | 10338-10354 | fork (F5, F18) | its rows below (10 units, module ccc18-soira-notice) |
| s 490.026(1) | 10339-10339 | encoded | `s 490.026(1) the person may apply for a termination order` |
| s 490.026(2) | 10340-10344 | fork (F5) | `s 490.026(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.026(2)(a) | 10342-10342 | fork (F5) | `s 490.026(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.026(2)(b) | 10343-10343 | fork (F5) | `s 490.026(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.026(2)(c) | 10344-10344 | fork (F5) | `s 490.026(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.026(3) | 10345-10346 | fork (F5) | `s 490.026(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` |
| s 490.026(4) | 10347-10348 | fork (F18) | `s 490.026(4) the person may apply for a termination order, despite subsections (2) and (3)` |
| s 490.026(5) | 10349-10350 | fork (F5, F18) | `s 490.026(5) the person may apply again for a termination order` |
| s 490.026(6) | 10351-10354 | encoded | `s 490.026(6) the application shall be made to a court of criminal jurisdiction` |
| s 490.026(6)(a) | 10353-10353 | encoded | `s 490.026(6) the application shall be made to a court of criminal jurisdiction` |
| s 490.026(6)(b) | 10354-10354 | encoded | `s 490.026(6) the application shall be made to a court of criminal jurisdiction` |
| s 490.027 | 10355-10371 | encoded | its rows below (11 units, module ccc18-soira-notice) |
| s 490.027(1) | 10356-10358 | encoded | `s 490.027(1) the court shall make an order terminating the obligation`; `s 490.027(1) the duty of the court` |
| s 490.027(1)(a) | 10357-10357 | encoded | `s 490.027(1) the court shall make an order terminating the obligation`; `s 490.027(1) the duty of the court` |
| s 490.027(1)(b) | 10358-10358 | encoded | `s 490.027(1) the court shall make an order terminating the obligation`; `s 490.027(1) the duty of the court` |
| s 490.027(1.1) | 10359-10367 | encoded | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(1.1)(a) | 10361-10361 | encoded | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(1.1)(b) | 10362-10362 | encoded | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(1.1)(c) | 10363-10363 | encoded | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(1.1)(d) | 10364-10364 | encoded | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(1.1)(e) | 10365-10365 | encoded | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(1.1)(f) | 10366-10366 | encoded | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(1.1)(g) | 10367-10367 | encoded | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(2) | 10368-10369 | encoded | `s 490.027(2) the court shall give reasons for its decision`; `s 490.027(2) the duty of the court` |
| s 490.027(3) | 10370-10371 | encoded | `s 490.027(3) the court shall cause the notification to be given`; `s 490.027(3) the duty of the court` |
| s 490.028 | 10372-10373 | encoded | `s 490.028 an application for one order is deemed to be an application for both` |
| s 490.029 | 10374-10377 | fork (F5) | its rows below (8 units, module ccc18-soira-notice) |
| s 490.029(1) | 10375-10375 | fork (F5) | `s 490.029(1) the appeal court may do it`; `s 490.029(1) the appeal may be brought` |
| s 490.029(2) | 10376-10377 | encoded | `s 490.029(2) the appeal court shall cause the notification to be given`; `s 490.029(2) the duty of a court of appeal` |
| group heading: Notice and Obligation to Comply with the Sex Offender Information Registration Act — Convictions Outside Canada | 10379-10379 | inert (reason 1: a heading) |  |
| s 490.02901 | 10380-10381 | encoded | `s 490.02901 the person shall comply with the Sex Offender Information Registration Act`; `s 490.02901 the duty of the offender to comply` |
| s 490.02902 | 10382-10385 | encoded | its rows below (3 units, module ccc18-soira-foreign) |
| s 490.02902(1) | 10383-10383 | encoded | `s 490.02902(1) the Attorney General or minister of justice may serve the person with a notice in Form 54` |
| s 490.02902(2) | 10384-10385 | encoded | `s 490.02902(2) a notice shall not be served on the person`; `s 490.02902 the notice in Form 54 may be served, subject to subsection (2)` |
| s 490.02903 | 10386-10394 | encoded | its rows below (7 units, module ccc18-soira-foreign) |
| s 490.02903(1) | 10387-10387 | encoded | `s 490.02903(1) the manner of service is the one the subsection requires` |
| s 490.02903(2) | 10388-10392 | encoded | `s 490.02903(2) the affidavit is evidence of the service and the notice` |
| s 490.02903(2)(a) | 10390-10390 | encoded | `s 490.02903(2) the affidavit is evidence of the service and the notice` |
| s 490.02903(2)(b) | 10391-10391 | encoded | `s 490.02903(2) the affidavit is evidence of the service and the notice` |
| s 490.02903(2)(c) | 10392-10392 | encoded | `s 490.02903(2) the affidavit is evidence of the service and the notice` |
| s 490.02903(3) | 10393-10394 | encoded | `s 490.02903(3) the person who served the notice must send a copy of the affidavit and the notice`; `s 490.02903(3) the duty of the person who served the notice` |
| s 490.02904 | 10395-10404 | encoded | its rows below (6 units, module ccc18-soira-foreign) |
| s 490.02904(1) | 10396-10396 | encoded | `s 490.02904(1) the day on which the obligation under section 490.02901 begins` |
| s 490.02904(2) | 10397-10398 | encoded | `s 490.02904(2) the day on which the obligation ends` |
| s 490.02904(3) | 10399-10404 | encoded | `s 490.02904(3) the obligation, if subsection (2) does not apply, ends or applies for life` |
| s 490.02904(3)(a) | 10401-10401 | encoded | `s 490.02904(3) the obligation, if subsection (2) does not apply, ends or applies for life` |
| s 490.02904(3)(b) | 10402-10402 | encoded | `s 490.02904(3) the obligation, if subsection (2) does not apply, ends or applies for life` |
| s 490.02904(3)(c) | 10403-10403 | encoded | `s 490.02904(3) the obligation, if subsection (2) does not apply, ends or applies for life` |
| s 490.02904(3)(d) | 10404-10404 | encoded | `s 490.02904(3) the obligation, if subsection (2) does not apply, ends or applies for life` |
| s 490.02905 | 10405-10429 | encoded | its rows below (18 units, module ccc18-soira-foreign) |
| s 490.02905(1) | 10406-10406 | encoded | `s 490.02905(1) the person may apply for an exemption order` |
| s 490.02905(2) | 10407-10412 | encoded | `s 490.02905(2) the court shall make an exemption order`; `s 490.02905(2) the duty of the court` |
| s 490.02905(2)(a) | 10409-10409 | encoded | `s 490.02905(2) the court shall make an exemption order`; `s 490.02905(2) the duty of the court` |
| s 490.02905(2)(b) | 10410-10410 | encoded | `s 490.02905(2) the court shall make an exemption order`; `s 490.02905(2) the duty of the court` |
| s 490.02905(2)(c) | 10411-10411 | encoded | `s 490.02905(2) the court shall make an exemption order`; `s 490.02905(2) the duty of the court` |
| s 490.02905(2)(d) | 10412-10412 | encoded | `s 490.02905(2) the court shall make an exemption order`; `s 490.02905(2) the duty of the court` |
| s 490.02905(2.1) | 10413-10421 | encoded | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.1)(a) | 10415-10415 | encoded | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.1)(b) | 10416-10416 | encoded | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.1)(c) | 10417-10417 | encoded | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.1)(d) | 10418-10418 | encoded | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.1)(e) | 10419-10419 | encoded | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.1)(f) | 10420-10420 | encoded | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.1)(g) | 10421-10421 | encoded | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.2) | 10422-10423 | encoded | `s 490.02905(2.2) the court shall order that the notice be corrected`; `s 490.02905(2.2) the duty of the court` |
| s 490.02905(3) | 10424-10425 | encoded | `s 490.02905(3) the court shall give reasons for its decision`; `s 490.02905(3) the duty of the court` |
| s 490.02905(4) | 10426-10427 | encoded | `s 490.02905(4) the court shall also make an order for removal of the information from the database`; `s 490.02905(4) the duty of the court` |
| s 490.02905(5) | 10428-10429 | encoded | `s 490.02905(5) the court shall cause the notification to be given`; `s 490.02905(5) the duty of the court` |
| s 490.029051 | 10430-10441 | fork (F5) | its rows below (16 units, module ccc18-soira-foreign) |
| s 490.029051(1) | 10431-10433 | fork (F5) | `s 490.029051(1) the person may apply for a variation order` |
| s 490.029051(1)(a) | 10432-10432 | fork (F5) | `s 490.029051(1) the person may apply for a variation order` |
| s 490.029051(1)(b) | 10433-10433 | fork (F5) | `s 490.029051(1) the person may apply for a variation order` |
| s 490.029051(2) | 10434-10435 | encoded | `s 490.029051(2) the court shall make the variation order`; `s 490.029051(2) the duty of the court` |
| s 490.029051(3) | 10436-10437 | encoded | `s 490.029051(3) the duration of the obligation set out in the variation order`; `s 490.029051(3) the duty of the court to set out the duration` |
| s 490.029051(4) | 10438-10439 | encoded | `s 490.029051(4) the court shall give reasons for its decision`; `s 490.029051(4) the duty of the court` |
| s 490.029051(5) | 10440-10441 | encoded | `s 490.029051(5) the court shall cause the notification to be given`; `s 490.029051(5) the duty of the court` |
| s 490.02906 | 10442-10447 | fork (F5) | its rows below (10 units, module ccc18-soira-foreign) |
| s 490.02906(1) | 10443-10445 | fork (F5) | `s 490.02906(1) the appeal court may do it`; `s 490.02906(1) the appeal may be brought` |
| s 490.02906(1)(a) | 10444-10444 | fork (F5) | `s 490.02906(1) the appeal court may do it`; `s 490.02906(1) the appeal may be brought` |
| s 490.02906(1)(b) | 10445-10445 | fork (F5) | `s 490.02906(1) the appeal court may do it`; `s 490.02906(1) the appeal may be brought` |
| s 490.02906(2) | 10446-10447 | encoded | `s 490.02906(2) the appeal court shall also make an order for removal of the information from the database`; `s 490.02906(2) the duty of a court of appeal` |
| s 490.02907 | 10448-10451 | encoded | its rows below (10 units, module ccc18-soira-foreign) |
| s 490.02907(1) | 10449-10449 | encoded | `s 490.02907(1) the appeal court shall cause the notification and the information to be given`; `s 490.02907(1) the duty of the appeal court to cause the Commissioner and the Attorney General to be notified`; `s 490.02907(1) the duty of the appeal court to cause the person to be informed of the sections` |
| s 490.02907(2) | 10450-10451 | encoded | `s 490.02907(2) the appeal court shall cause the notification to be given`; `s 490.02907(2) the duty of a court of appeal` |
| s 490.02908 | 10452-10462 | fork (F5) | its rows below (7 units, module ccc18-soira-foreign) |
| s 490.02908(1) | 10453-10453 | encoded | `s 490.02908(1) the person may apply for a termination order` |
| s 490.02908(2) | 10454-10458 | fork (F5) | `s 490.02908(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02908(2)(a) | 10456-10456 | fork (F5) | `s 490.02908(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02908(2)(b) | 10457-10457 | fork (F5) | `s 490.02908(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02908(2)(c) | 10458-10458 | fork (F5) | `s 490.02908(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02908(3) | 10459-10460 | fork (F5) | `s 490.02908(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` |
| s 490.02908(4) | 10461-10462 | fork (F5) | `s 490.02908(4) the person may apply again for a termination order` |
| s 490.02909 | 10463-10479 | fork (F5) | its rows below (12 units, module ccc18-soira-foreign) |
| s 490.02909(1) | 10464-10466 | encoded | `s 490.02909(1) the court shall make an order terminating the obligation`; `s 490.02909(1) the duty of the court` |
| s 490.02909(1)(a) | 10465-10465 | encoded | `s 490.02909(1) the court shall make an order terminating the obligation`; `s 490.02909(1) the duty of the court` |
| s 490.02909(1)(b) | 10466-10466 | encoded | `s 490.02909(1) the court shall make an order terminating the obligation`; `s 490.02909(1) the duty of the court` |
| s 490.02909(1.1) | 10467-10475 | encoded | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(1.1)(a) | 10469-10469 | encoded | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(1.1)(b) | 10470-10470 | encoded | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(1.1)(c) | 10471-10471 | encoded | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(1.1)(d) | 10472-10472 | encoded | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(1.1)(e) | 10473-10473 | encoded | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(1.1)(f) | 10474-10474 | encoded | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(1.1)(g) | 10475-10475 | encoded | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(2) | 10476-10477 | encoded | `s 490.02909(2) the court shall give reasons for its decision`; `s 490.02909(2) the duty of the court` |
| s 490.02909(3) | 10478-10479 | encoded | `s 490.02909(3) the court shall cause the notification to be given`; `s 490.02909(3) the duty of the court` |
| s 490.0291 | 10480-10483 | fork (F5) | its rows below (10 units, module ccc18-soira-foreign) |
| s 490.0291(1) | 10481-10481 | fork (F5) | `s 490.0291(1) the appeal court may do it`; `s 490.0291(1) the appeal may be brought` |
| s 490.0291(2) | 10482-10483 | encoded | `s 490.0291(2) the appeal court shall cause the notification to be given`; `s 490.0291(2) the duty of a court of appeal` |
| s 490.02911 | 10484-10500 | encoded | its rows below (18 units, module ccc18-soira-foreign) |
| s 490.02911(1) | 10485-10492 | encoded | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada`; `s 490.02911(1) the advice covers what the subsection lists` (+1 more in the same unit) |
| s 490.02911(1)(a) | 10486-10486 | encoded | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada`; `s 490.02911(1) the advice covers what the subsection lists` (+1 more in the same unit) |
| s 490.02911(1)(b) | 10487-10492 | encoded | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada`; `s 490.02911(1) the advice covers what the subsection lists` (+1 more in the same unit) |
| s 490.02911(1)(b)(i) | 10488-10488 | encoded | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada`; `s 490.02911(1) the advice covers what the subsection lists` (+1 more in the same unit) |
| s 490.02911(1)(b)(ii) | 10489-10489 | encoded | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada`; `s 490.02911(1) the advice covers what the subsection lists` (+1 more in the same unit) |
| s 490.02911(1)(b)(iii) | 10490-10490 | encoded | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada`; `s 490.02911(1) the advice covers what the subsection lists` (+1 more in the same unit) |
| s 490.02911(1)(b)(iv) | 10491-10491 | encoded | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada`; `s 490.02911(1) the advice covers what the subsection lists` (+1 more in the same unit) |
| s 490.02911(1)(b)(v) | 10492-10492 | encoded | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada`; `s 490.02911(1) the advice covers what the subsection lists` (+1 more in the same unit) |
| s 490.02911(1.1) | 10493-10494 | encoded | `s 490.02911(1.1) the person is required to advise the police service again` |
| s 490.02911(2) | 10495-10496 | encoded | `s 490.02911(2) the person must advise a police service of a change in address`; `s 490.02911(2) the person advised a police service of the change in address within seven days after the day on which the change was made`; `s 490.02911(2) the duty of the offender to advise a police service of a change in address within seven days` |
| s 490.02911(3) | 10497-10498 | encoded | `s 490.02911(3) the police service shall cause the Attorney General or minister of justice to be provided with the information`; `s 490.02911(3) the duty of a police service` |
| s 490.02911(4) | 10499-10500 | encoded | `s 490.02911(4) the day on which the obligation under subsection (2) ends` |
| group heading: International Transfer of Offenders Act | 10502-10502 | inert (reason 1: a heading) |  |
| s 490.029111 | 10503-10521 | encoded | its rows below (12 units, module ccc18-soira-itoa) |
| s 490.029111(1) | 10504-10504 | encoded | `s 490.029111(1) the person may apply for an exemption order` |
| s 490.029111(2) | 10505-10508 | encoded | `s 490.029111(2) the court shall make an exemption order`; `s 490.029111(2) the duty of the court` |
| s 490.029111(2)(a) | 10507-10507 | encoded | `s 490.029111(2) the court shall make an exemption order`; `s 490.029111(2) the duty of the court` |
| s 490.029111(2)(b) | 10508-10508 | encoded | `s 490.029111(2) the court shall make an exemption order`; `s 490.029111(2) the duty of the court` |
| s 490.029111(3) | 10509-10517 | encoded | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(3)(a) | 10511-10511 | encoded | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(3)(b) | 10512-10512 | encoded | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(3)(c) | 10513-10513 | encoded | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(3)(d) | 10514-10514 | encoded | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(3)(e) | 10515-10515 | encoded | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(3)(f) | 10516-10516 | encoded | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(3)(g) | 10517-10517 | encoded | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(4) | 10518-10519 | encoded | `s 490.029111(4) the court shall give reasons for its decision`; `s 490.029111(4) the duty of the court` |
| s 490.029111(5) | 10520-10521 | encoded | `s 490.029111(5) the court shall also make an order for removal of the information from the database`; `s 490.029111(5) the duty of the court` |
| s 490.029112 | 10522-10533 | fork (F5) | its rows below (16 units, module ccc18-soira-itoa) |
| s 490.029112(1) | 10523-10525 | fork (F5) | `s 490.029112(1) the person may apply for a variation order` |
| s 490.029112(1)(a) | 10524-10524 | fork (F5) | `s 490.029112(1) the person may apply for a variation order` |
| s 490.029112(1)(b) | 10525-10525 | fork (F5) | `s 490.029112(1) the person may apply for a variation order` |
| s 490.029112(2) | 10526-10527 | encoded | `s 490.029112(2) the court shall make the variation order`; `s 490.029112(2) the duty of the court` |
| s 490.029112(3) | 10528-10529 | encoded | `s 490.029112(3) the duration of the obligation set out in the variation order`; `s 490.029112(3) the duty of the court to set out the duration` |
| s 490.029112(4) | 10530-10531 | encoded | `s 490.029112(4) the court shall give reasons for its decision`; `s 490.029112(4) the duty of the court` |
| s 490.029112(5) | 10532-10533 | encoded | `s 490.029112(5) the court shall cause the notification to be given`; `s 490.029112(5) the duty of the court` |
| s 490.029113 | 10534-10539 | fork (F5) | its rows below (10 units, module ccc18-soira-itoa) |
| s 490.029113(1) | 10535-10537 | fork (F5) | `s 490.029113(1) the appeal court may do it`; `s 490.029113(1) the appeal may be brought` |
| s 490.029113(1)(a) | 10536-10536 | fork (F5) | `s 490.029113(1) the appeal court may do it`; `s 490.029113(1) the appeal may be brought` |
| s 490.029113(1)(b) | 10537-10537 | fork (F5) | `s 490.029113(1) the appeal court may do it`; `s 490.029113(1) the appeal may be brought` |
| s 490.029113(2) | 10538-10539 | encoded | `s 490.029113(2) the appeal court shall also make an order for removal of the information from the database`; `s 490.029113(2) the duty of a court of appeal` |
| s 490.029114 | 10540-10543 | encoded | its rows below (10 units, module ccc18-soira-itoa) |
| s 490.029114(1) | 10541-10541 | encoded | `s 490.029114(1) the appeal court shall cause the notification and the information to be given`; `s 490.029114(1) the duty of the appeal court to cause the Commissioner and the Attorney General to be notified`; `s 490.029114(1) the duty of the appeal court to cause the person to be informed of the sections` |
| s 490.029114(2) | 10542-10543 | encoded | `s 490.029114(2) the appeal court shall cause the notification to be given`; `s 490.029114(2) the duty of a court of appeal` |
| s 490.02912 | 10544-10556 | fork (F5, F18) | its rows below (8 units, module ccc18-soira-itoa) |
| s 490.02912(1) | 10545-10545 | encoded | `s 490.02912(1) the person may apply for a termination order` |
| s 490.02912(2) | 10546-10550 | fork (F5) | `s 490.02912(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02912(2)(a) | 10548-10548 | fork (F5) | `s 490.02912(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02912(2)(b) | 10549-10549 | fork (F5) | `s 490.02912(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02912(2)(c) | 10550-10550 | fork (F5) | `s 490.02912(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02912(3) | 10551-10552 | fork (F5) | `s 490.02912(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` |
| s 490.02912(3.1) | 10553-10554 | fork (F18) | `s 490.02912(3.1) the person may apply for a termination order, despite subsections (2) and (3)` |
| s 490.02912(4) | 10555-10556 | fork (F5) | `s 490.02912(4) the person may apply again for a termination order` |
| s 490.02913 | 10557-10573 | fork (F5) | its rows below (12 units, module ccc18-soira-itoa) |
| s 490.02913(1) | 10558-10560 | encoded | `s 490.02913(1) the court shall make an order terminating the obligation`; `s 490.02913(1) the duty of the court` |
| s 490.02913(1)(a) | 10559-10559 | encoded | `s 490.02913(1) the court shall make an order terminating the obligation`; `s 490.02913(1) the duty of the court` |
| s 490.02913(1)(b) | 10560-10560 | encoded | `s 490.02913(1) the court shall make an order terminating the obligation`; `s 490.02913(1) the duty of the court` |
| s 490.02913(1.1) | 10561-10569 | encoded | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(1.1)(a) | 10563-10563 | encoded | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(1.1)(b) | 10564-10564 | encoded | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(1.1)(c) | 10565-10565 | encoded | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(1.1)(d) | 10566-10566 | encoded | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(1.1)(e) | 10567-10567 | encoded | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(1.1)(f) | 10568-10568 | encoded | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(1.1)(g) | 10569-10569 | encoded | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(2) | 10570-10571 | encoded | `s 490.02913(2) the court shall give reasons for its decision`; `s 490.02913(2) the duty of the court` |
| s 490.02913(3) | 10572-10573 | encoded | `s 490.02913(3) the court shall cause the notification to be given`; `s 490.02913(3) the duty of the court` |
| s 490.02914 | 10574-10577 | fork (F5) | its rows below (10 units, module ccc18-soira-itoa) |
| s 490.02914(1) | 10575-10575 | fork (F5) | `s 490.02914(1) the appeal court may do it`; `s 490.02914(1) the appeal may be brought` |
| s 490.02914(2) | 10576-10577 | encoded | `s 490.02914(2) the appeal court shall cause the notification to be given`; `s 490.02914(2) the duty of a court of appeal` |
| s 490.02915 | 10578-10583 | encoded | its rows below (10 units, module ccc18-soira-itoa) |
| s 490.02915(1) | 10579-10579 | encoded | `s 490.02915(1) the person in charge of the place must give the person a copy of the Form 1`; `s 490.02915(1) the copy was given not earlier than 10 days before the release or discharge`; `s 490.02915(1) the duty of the person in charge of the place to give a copy of the Form 1` |
| s 490.02915(2) | 10580-10583 | encoded | `s 490.02915(2) the Review Board must cause a copy of the Form 1 to be given to the person`; `s 490.02915(2) the duty of the Review Board to cause a copy of the Form 1 to be given` |
| s 490.02915(2)(a) | 10582-10582 | encoded | `s 490.02915(2) the Review Board must cause a copy of the Form 1 to be given to the person`; `s 490.02915(2) the duty of the Review Board to cause a copy of the Form 1 to be given` |
| s 490.02915(2)(b) | 10583-10583 | encoded | `s 490.02915(2) the Review Board must cause a copy of the Form 1 to be given to the person`; `s 490.02915(2) the duty of the Review Board to cause a copy of the Form 1 to be given` |
| group heading: Disclosure of Information | 10585-10585 | inert (reason 1: a heading) |  |
| s 490.03 | 10586-10594 | fork (F5) | its rows below (9 units, module ccc18-soira-offences) |
| s 490.03(1) | 10587-10589 | encoded | `s 490.03(1) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the registered information`; `s 490.03(1)(a) the duty of the Commissioner to disclose to the prosecutor`; `s 490.03(1)(b) the duty of the Commissioner to disclose to the Attorney General` |
| s 490.03(1)(a) | 10588-10588 | encoded | `s 490.03(1) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the registered information`; `s 490.03(1)(a) the duty of the Commissioner to disclose to the prosecutor`; `s 490.03(1)(b) the duty of the Commissioner to disclose to the Attorney General` |
| s 490.03(1)(b) | 10589-10589 | encoded | `s 490.03(1) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the registered information`; `s 490.03(1)(a) the duty of the Commissioner to disclose to the prosecutor`; `s 490.03(1)(b) the duty of the Commissioner to disclose to the Attorney General` |
| s 490.03(2) | 10590-10591 | encoded | `s 490.03(2) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the information to the prosecutor or Attorney General`; `s 490.03(2) the duty of the Commissioner to disclose to the prosecutor or Attorney General` |
| s 490.03(3) | 10592-10593 | fork (F5) | `s 490.03(3) the prosecutor or the Attorney General may disclose the information to the presiding court` |
| s 490.03(4) | 10594-10594 | repealed or blank in this text (the text shows [Repealed]) |  |
| group heading: Offences | 10596-10596 | inert (reason 1: a heading) |  |
| s 490.031 | 10597-10608 | fork (F5, F9) | its rows below (8 units, module ccc18-soira-offences) |
| s 490.031(1) | 10598-10600 | encoded | `s 490.031(1) the person is guilty of an offence`; `s 490.031(1) the class of the offence`; `s 490.031(1)(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.031(1)(a) | 10599-10599 | encoded | `s 490.031(1) the person is guilty of an offence`; `s 490.031(1) the class of the offence`; `s 490.031(1)(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.031(1)(b) | 10600-10600 | encoded | `s 490.031(1) the person is guilty of an offence`; `s 490.031(1) the class of the offence`; `s 490.031(1)(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.031(2) | 10601-10602 | fork (F9) | `s 490.031(2) a lawful command is a reasonable excuse` |
| s 490.031(3) | 10603-10604 | encoded | `s 490.031(3) the certificate is evidence of the statements contained in it without proof of the signature or official character` |
| s 490.031(4) | 10605-10606 | fork (F5) | `s 490.031(4) the sex offender may require the attendance of the person who signed the certificate for cross-examination` |
| s 490.031(5) | 10607-10608 | encoded | `s 490.031(5) the certificate is not to be received in evidence` |
| s 490.0311 | 10609-10612 | encoded | `s 490.0311 the person is guilty of an offence`; `s 490.0311 the class of the offence`; `s 490.0311(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.0311(a) | 10611-10611 | encoded | `s 490.0311 the person is guilty of an offence`; `s 490.0311 the class of the offence`; `s 490.0311(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.0311(b) | 10612-10612 | encoded | `s 490.0311 the person is guilty of an offence`; `s 490.0311 the class of the offence`; `s 490.0311(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.0312 | 10613-10614 | encoded | `s 490.0312 the person is guilty of an offence`; `s 490.0312 the class of the offence`; `s 490.0312 the punishment on summary conviction` |
| group heading: Warrant | 10616-10616 | inert (reason 1: a heading) |  |
| s 490.03121 | 10617-10626 | fork (F5) | its rows below (9 units, module ccc18-soira-offences) |
| s 490.03121(1) | 10618-10618 | fork (F5) | `s 490.03121(1) the justice may issue a warrant in Form 6.4 to arrest the person`; `s 490.03121(1) the power of the justice to issue the warrant` |
| s 490.03121(2) | 10619-10620 | encoded | `s 490.03121(2) the warrant shall contain the condition`; `s 490.03121(2) the duty of the justice to put the conditions in the warrant` |
| s 490.03121(3) | 10621-10622 | fork (F5) | `s 490.03121(3) the warrant may be executed there` |
| s 490.03121(4) | 10623-10624 | encoded | `s 490.03121(4) the warrant remains in force` |
| s 490.03121(5) | 10625-10626 | encoded | `s 490.03121(5) no charge shall be laid against the person in respect of the contravention` |
| group heading: Regulations | 10628-10628 | inert (reason 1: a heading) |  |
| s 490.032 | 10629-10632 | inert (reason 2: machinery: the Governor in Council's power to make regulations about the content of Form 53 and Form 54) |  |
| s 490.032(a) | 10631-10631 | inert (reason 2: machinery: the Governor in Council's power to make regulations about the content of Form 53 and Form 54) |  |
| s 490.032(b) | 10632-10632 | inert (reason 2: machinery: the Governor in Council's power to make regulations about the content of Form 53 and Form 54) |  |
| group heading: Additional Orders | 10634-10634 | inert (reason 1: a heading) |  |
| s 490.04 | 10635-10667 | fork (F5) | its rows below (17 units, module ccc18-soira-additional) |
| s 490.04(1) | 10636-10638 | fork (F5) | `s 490.04(1) the person may apply to a court for an exemption order` |
| s 490.04(1)(a) | 10637-10637 | fork (F5) | `s 490.04(1) the person may apply to a court for an exemption order` |
| s 490.04(1)(b) | 10638-10638 | fork (F5) | `s 490.04(1) the person may apply to a court for an exemption order` |
| s 490.04(2) | 10639-10640 | encoded | `s 490.04(2) the person is not permitted to apply under paragraph (1)(b)` |
| s 490.04(3) | 10641-10644 | encoded | `s 490.04(3) the court to which the application shall be made` |
| s 490.04(3)(a) | 10643-10643 | encoded | `s 490.04(3) the court to which the application shall be made` |
| s 490.04(3)(b) | 10644-10644 | encoded | `s 490.04(3) the court to which the application shall be made` |
| s 490.04(4) | 10645-10650 | encoded | `s 490.04(4) the court shall not make an exemption order`; `s 490.04 the court shall make an exemption order, subject to subsection (4)` |
| s 490.04(4)(a) | 10647-10647 | encoded | `s 490.04(4) the court shall not make an exemption order`; `s 490.04 the court shall make an exemption order, subject to subsection (4)` |
| s 490.04(4)(b) | 10648-10650 | encoded | `s 490.04(4) the court shall not make an exemption order`; `s 490.04 the court shall make an exemption order, subject to subsection (4)` |
| s 490.04(4)(b)(i) | 10649-10649 | encoded | `s 490.04(4) the court shall not make an exemption order`; `s 490.04 the court shall make an exemption order, subject to subsection (4)` |
| s 490.04(4)(b)(ii) | 10650-10650 | encoded | `s 490.04(4) the court shall not make an exemption order`; `s 490.04 the court shall make an exemption order, subject to subsection (4)` |
| s 490.04(5) | 10651-10654 | encoded | `s 490.04(5) the court shall make an exemption order`; `s 490.04(5) the duty of the court`; `s 490.04 the court shall make an exemption order, subject to subsection (4)` |
| s 490.04(5)(a) | 10653-10653 | encoded | `s 490.04(5) the court shall make an exemption order`; `s 490.04(5) the duty of the court`; `s 490.04 the court shall make an exemption order, subject to subsection (4)` |
| s 490.04(5)(b) | 10654-10654 | encoded | `s 490.04(5) the court shall make an exemption order`; `s 490.04(5) the duty of the court`; `s 490.04 the court shall make an exemption order, subject to subsection (4)` |
| s 490.04(6) | 10655-10663 | encoded | `s 490.04(6) the court shall consider the factor` |
| s 490.04(6)(a) | 10657-10657 | encoded | `s 490.04(6) the court shall consider the factor` |
| s 490.04(6)(b) | 10658-10658 | encoded | `s 490.04(6) the court shall consider the factor` |
| s 490.04(6)(c) | 10659-10659 | encoded | `s 490.04(6) the court shall consider the factor` |
| s 490.04(6)(d) | 10660-10660 | encoded | `s 490.04(6) the court shall consider the factor` |
| s 490.04(6)(e) | 10661-10661 | encoded | `s 490.04(6) the court shall consider the factor` |
| s 490.04(6)(f) | 10662-10662 | encoded | `s 490.04(6) the court shall consider the factor` |
| s 490.04(6)(g) | 10663-10663 | encoded | `s 490.04(6) the court shall consider the factor` |
| s 490.04(7) | 10664-10665 | encoded | `s 490.04(7) the court shall give reasons for its decision`; `s 490.04(7) the duty of the court` |
| s 490.04(8) | 10666-10667 | encoded | `s 490.04(8) the court shall also make an order for removal of the information from the database`; `s 490.04(8) the duty of the court` |
| s 490.05 | 10668-10691 | fork (F5) | its rows below (20 units, module ccc18-soira-additional) |
| s 490.05(1) | 10669-10673 | fork (F5) | `s 490.05(1) the person may apply to a court for a variation order` |
| s 490.05(1)(a) | 10670-10670 | fork (F5) | `s 490.05(1) the person may apply to a court for a variation order` |
| s 490.05(1)(b) | 10671-10671 | fork (F5) | `s 490.05(1) the person may apply to a court for a variation order` |
| s 490.05(1)(c) | 10672-10672 | fork (F5) | `s 490.05(1) the person may apply to a court for a variation order` |
| s 490.05(1)(d) | 10673-10673 | fork (F5) | `s 490.05(1) the person may apply to a court for a variation order` |
| s 490.05(2) | 10674-10675 | encoded | `s 490.05(2) the person is not permitted to apply under paragraph (1)(c) or (d)` |
| s 490.05(3) | 10676-10679 | encoded | `s 490.05(3) the court to which the application shall be made` |
| s 490.05(3)(a) | 10678-10678 | encoded | `s 490.05(3) the court to which the application shall be made` |
| s 490.05(3)(b) | 10679-10679 | encoded | `s 490.05(3) the court to which the application shall be made` |
| s 490.05(4) | 10680-10681 | encoded | `s 490.05(4) the court shall make the variation order`; `s 490.05(4) the duty of the court` |
| s 490.05(5) | 10682-10687 | encoded | `s 490.05(5) the duration set out in the variation order`; `s 490.05(5) the duty of the court to set out the duration` |
| s 490.05(5)(a) | 10684-10684 | encoded | `s 490.05(5) the duration set out in the variation order`; `s 490.05(5) the duty of the court to set out the duration` |
| s 490.05(5)(b) | 10685-10685 | encoded | `s 490.05(5) the duration set out in the variation order`; `s 490.05(5) the duty of the court to set out the duration` |
| s 490.05(5)(c) | 10686-10686 | encoded | `s 490.05(5) the duration set out in the variation order`; `s 490.05(5) the duty of the court to set out the duration` |
| s 490.05(5)(d) | 10687-10687 | encoded | `s 490.05(5) the duration set out in the variation order`; `s 490.05(5) the duty of the court to set out the duration` |
| s 490.05(6) | 10688-10689 | encoded | `s 490.05(6) the court shall give reasons for its decision`; `s 490.05(6) the duty of the court` |
| s 490.05(7) | 10690-10691 | encoded | `s 490.05(7) the court shall cause the notification to be given`; `s 490.05(7) the duty of the court` |
| s 490.06 | 10692-10697 | fork (F5) | its rows below (10 units, module ccc18-soira-additional) |
| s 490.06(1) | 10693-10695 | fork (F5) | `s 490.06(1) the appeal court may do it`; `s 490.06(1) the appeal may be brought` |
| s 490.06(1)(a) | 10694-10694 | fork (F5) | `s 490.06(1) the appeal court may do it`; `s 490.06(1) the appeal may be brought` |
| s 490.06(1)(b) | 10695-10695 | fork (F5) | `s 490.06(1) the appeal court may do it`; `s 490.06(1) the appeal may be brought` |
| s 490.06(2) | 10696-10697 | encoded | `s 490.06(2) the appeal court shall also make an order for removal of the information from the database`; `s 490.06(2) the duty of a court of appeal` |
| s 490.07 | 10698-10701 | encoded | its rows below (10 units, module ccc18-soira-additional) |
| s 490.07(1) | 10699-10699 | encoded | `s 490.07(1) the appeal court shall cause the notification and the information to be given`; `s 490.07(1) the duty of the appeal court to cause the Commissioner and the Attorney General to be notified`; `s 490.07(1) the duty of the appeal court to cause the person to be informed of the sections` |
| s 490.07(2) | 10700-10701 | encoded | `s 490.07(2) the appeal court shall cause the notification to be given`; `s 490.07(2) the duty of a court of appeal` |
| group heading: Forfeiture of Offence-related Property | 10703-10703 | inert (reason 1: a heading) |  |
| s 490.1 | 10704-10714 | fork (F5, F10) | its rows below (10 units, module ccc18-forfeiture) |
| s 490.1(1) | 10705-10707 | fork (F10) | `s 490.1(1) the court shall order the property forfeited`; `s 490.1(1) the Crown in whose right the property is forfeited`; `s 490.1(1) the court shall order the property forfeited, subject to sections 490.3 to 490.41` (+1 more in the same unit) |
| s 490.1(1)(a) | 10706-10706 | fork (F10) | `s 490.1(1) the court shall order the property forfeited`; `s 490.1(1) the Crown in whose right the property is forfeited`; `s 490.1(1) the court shall order the property forfeited, subject to sections 490.3 to 490.41` (+1 more in the same unit) |
| s 490.1(1)(b) | 10707-10707 | fork (F10) | `s 490.1(1) the court shall order the property forfeited`; `s 490.1(1) the Crown in whose right the property is forfeited`; `s 490.1(1) the court shall order the property forfeited, subject to sections 490.3 to 490.41` (+1 more in the same unit) |
| s 490.1(1.1) | 10708-10708 | repealed or blank in this text (the text shows [Repealed]) |  |
| s 490.1(2) | 10709-10710 | fork (F5) | `s 490.1(2) the court may make an order of forfeiture under subsection (1) of property not shown to be related to the offence` |
| s 490.1(2.1) | 10711-10712 | fork (F5) | `s 490.1(2.1) an order may be issued in respect of property situated outside Canada` |
| s 490.1(3) | 10713-10714 | fork (F5) | `s 490.1(3) the appeal may be brought` |
| s 490.2 | 10715-10735 | fork (F5, F10) | its rows below (11 units, module ccc18-forfeiture) |
| s 490.2(1) | 10716-10716 | fork (F5) | `s 490.2(1) the Attorney General may make an application to a judge for an order of forfeiture` |
| s 490.2(2) | 10717-10721 | fork (F10) | `s 490.2(2) the judge shall order the property forfeited`; `s 490.2(2) the duty of the judge to order the forfeiture`; `s 490.2(2) the judge shall order the property forfeited, subject to sections 490.3 to 490.41` |
| s 490.2(2)(a) | 10719-10719 | fork (F10) | `s 490.2(2) the judge shall order the property forfeited`; `s 490.2(2) the duty of the judge to order the forfeiture`; `s 490.2(2) the judge shall order the property forfeited, subject to sections 490.3 to 490.41` |
| s 490.2(2)(b) | 10720-10720 | fork (F10) | `s 490.2(2) the judge shall order the property forfeited`; `s 490.2(2) the duty of the judge to order the forfeiture`; `s 490.2(2) the judge shall order the property forfeited, subject to sections 490.3 to 490.41` |
| s 490.2(2)(c) | 10721-10721 | fork (F10) | `s 490.2(2) the judge shall order the property forfeited`; `s 490.2(2) the duty of the judge to order the forfeiture`; `s 490.2(2) the judge shall order the property forfeited, subject to sections 490.3 to 490.41` |
| s 490.2(3) | 10722-10727 | encoded | `s 490.2(3) the day on which the accused is deemed to have absconded` |
| s 490.2(3)(a) | 10724-10724 | encoded | `s 490.2(3) the day on which the accused is deemed to have absconded` |
| s 490.2(3)(b) | 10725-10725 | encoded | `s 490.2(3) the day on which the accused is deemed to have absconded` |
| s 490.2(3)(c) | 10726-10727 | encoded | `s 490.2(3) the day on which the accused is deemed to have absconded` |
| s 490.2(4) | 10728-10731 | encoded | `s 490.2(4) the Crown in whose right the judge shall order the property forfeited` |
| s 490.2(4)(a) | 10730-10730 | encoded | `s 490.2(4) the Crown in whose right the judge shall order the property forfeited` |
| s 490.2(4)(b) | 10731-10731 | encoded | `s 490.2(4) the Crown in whose right the judge shall order the property forfeited` |
| s 490.2(4.1) | 10732-10733 | fork (F5) | `s 490.2(4.1) an order may be issued in respect of property situated outside Canada` |
| s 490.2(5) | 10734-10735 | encoded | `s 490.2(5) judge` |
| s 490.2(5) "judge" | 10735-10735 | encoded | `s 490.2(5) judge` |
| s 490.3 | 10736-10737 | encoded | `s 490.3 the court may set aside the conveyance or transfer` |
| s 490.4 | 10738-10746 | fork (F5, F11) | its rows below (7 units, module ccc18-forfeiture) |
| s 490.4(1) | 10739-10739 | fork (F5) | `s 490.4(1) the court shall require notice to be given to the person`; `s 490.4(1) the duty of the court`; `s 490.4(1) (hearing) the court may hear the person` |
| s 490.4(2) | 10740-10744 | encoded | `s 490.4(2) the notice is as the subsection requires` |
| s 490.4(2)(a) | 10742-10742 | encoded | `s 490.4(2) the notice is as the subsection requires` |
| s 490.4(2)(b) | 10743-10743 | encoded | `s 490.4(2) the notice is as the subsection requires` |
| s 490.4(2)(c) | 10744-10744 | encoded | `s 490.4(2) the notice is as the subsection requires` |
| s 490.4(3) | 10745-10746 | fork (F5, F11) | `s 490.4(3) the court may order that the property be returned to the person` |
| s 490.41 | 10747-10759 | fork (F5, F11) | its rows below (9 units, module ccc18-forfeiture) |
| s 490.41(1) | 10748-10748 | fork (F5) | `s 490.41(1) the court shall require notice to be given to the person, and may hear them`; `s 490.41(1) the duty of the court to require notice to the member of the immediate family` |
| s 490.41(2) | 10749-10753 | encoded | `s 490.41(2) the notice is as the subsection requires` |
| s 490.41(2)(a) | 10751-10751 | encoded | `s 490.41(2) the notice is as the subsection requires` |
| s 490.41(2)(b) | 10752-10752 | encoded | `s 490.41(2) the notice is as the subsection requires` |
| s 490.41(2)(c) | 10753-10753 | encoded | `s 490.41(2) the notice is as the subsection requires` |
| s 490.41(3) | 10754-10755 | fork (F5) | `s 490.41(3) (decision) the court may decide not to order the forfeiture of the property or part of the property`; `s 490.41(3) (restraint order) the court may revoke a restraint order made in respect of the property or part of it` |
| s 490.41(4) | 10756-10759 | encoded | `s 490.41(4) the court shall also consider the matter` |
| s 490.41(4)(a) | 10758-10758 | encoded | `s 490.41(4) the court shall also consider the matter` |
| s 490.41(4)(b) | 10759-10759 | encoded | `s 490.41(4) the court shall also consider the matter` |
| s 490.5 | 10760-10780 | fork (F5, F11, F12, F18) | its rows below (14 units, module ccc18-forfeiture) |
| s 490.5(1) | 10761-10765 | fork (F11) | `s 490.5(1) the person may apply for an order under subsection (4)` |
| s 490.5(1)(a) | 10762-10762 | fork (F11) | `s 490.5(1) the person may apply for an order under subsection (4)` |
| s 490.5(1)(b) | 10763-10763 | fork (F11) | `s 490.5(1) the person may apply for an order under subsection (4)` |
| s 490.5(1)(c) | 10764-10765 | fork (F11) | `s 490.5(1) the person may apply for an order under subsection (4)` |
| s 490.5(2) | 10766-10767 | encoded | `s 490.5(2) the day fixed is not less than thirty days after the date of the filing`; `s 490.5(2) the duty of the judge to fix the day` |
| s 490.5(3) | 10768-10769 | fork (F12) | `s 490.5(3) the notice was served at least fifteen days before the day fixed for the hearing`; `s 490.5(3) the duty of the applicant to serve the notice` |
| s 490.5(4) | 10770-10774 | fork (F18) | `s 490.5(4) the judge may make an order declaring that the interest of the applicant is not affected by the forfeiture` |
| s 490.5(4)(a) | 10772-10772 | fork (F18) | `s 490.5(4) the judge may make an order declaring that the interest of the applicant is not affected by the forfeiture` |
| s 490.5(4)(b) | 10773-10774 | fork (F18) | `s 490.5(4) the judge may make an order declaring that the interest of the applicant is not affected by the forfeiture` |
| s 490.5(5) | 10775-10776 | fork (F5) | `s 490.5(5) the appeal may be brought` |
| s 490.5(6) | 10777-10780 | encoded | `s 490.5(6) the Attorney General shall direct that the property be returned or the amount paid`; `s 490.5(6) the duty of the Attorney General to direct the return or the payment` |
| s 490.5(6)(a) | 10779-10779 | encoded | `s 490.5(6) the Attorney General shall direct that the property be returned or the amount paid`; `s 490.5(6) the duty of the Attorney General to direct the return or the payment` |
| s 490.5(6)(b) | 10780-10780 | encoded | `s 490.5(6) the Attorney General shall direct that the property be returned or the amount paid`; `s 490.5(6) the duty of the Attorney General to direct the return or the payment` |
| s 490.6 | 10781-10782 | fork (F5) | `s 490.6 the person may appeal from the order` |
| s 490.7 | 10783-10787 | fork (F12) | `s 490.7 the operation of the order is suspended`; `s 490.7 the property shall not be disposed of or otherwise dealt with` |
| s 490.7(a) | 10785-10785 | fork (F12) | `s 490.7 the operation of the order is suspended`; `s 490.7 the property shall not be disposed of or otherwise dealt with` |
| s 490.7(b) | 10786-10787 | fork (F12) | `s 490.7 the operation of the order is suspended`; `s 490.7 the property shall not be disposed of or otherwise dealt with` |
| s 490.8 | 10788-10814 | fork (F5) | its rows below (13 units, module ccc18-forfeiture) |
| s 490.8(1) | 10789-10789 | fork (F5) | `s 490.8(1) the Attorney General may apply for a restraint order` |
| s 490.8(2) | 10790-10794 | encoded | `s 490.8(2) the application is in the form the subsection requires` |
| s 490.8(2)(a) | 10792-10792 | encoded | `s 490.8(2) the application is in the form the subsection requires` |
| s 490.8(2)(b) | 10793-10793 | encoded | `s 490.8(2) the application is in the form the subsection requires` |
| s 490.8(2)(c) | 10794-10794 | encoded | `s 490.8(2) the application is in the form the subsection requires` |
| s 490.8(3) | 10795-10796 | fork (F5) | `s 490.8(3) the judge may make a restraint order` |
| s 490.8(3.1) | 10797-10798 | fork (F5) | `s 490.8(3.1) a restraint order may be issued in respect of property situated outside Canada` |
| s 490.8(4) | 10799-10800 | fork (F5) | `s 490.8(4) the restraint order may be subject to the condition` |
| s 490.8(5) | 10801-10802 | encoded | `s 490.8(5) the restraint order is made as the subsection requires` |
| s 490.8(6) | 10803-10804 | encoded | `s 490.8(6) the copy of the restraint order is served as the subsection requires` |
| s 490.8(7) | 10805-10806 | encoded | `s 490.8(7) the copy of the restraint order is registered as the subsection requires` |
| s 490.8(8) | 10807-10810 | encoded | `s 490.8(8) the restraint order remains in effect` |
| s 490.8(8)(a) | 10809-10809 | encoded | `s 490.8(8) the restraint order remains in effect` |
| s 490.8(8)(b) | 10810-10810 | encoded | `s 490.8(8) the restraint order remains in effect` |
| s 490.8(9) | 10811-10814 | encoded | `s 490.8(9) the person is guilty of an offence`; `s 490.8(9) the class of the offence`; `s 490.8(9)(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.8(9)(a) | 10813-10813 | encoded | `s 490.8(9) the person is guilty of an offence`; `s 490.8(9) the class of the offence`; `s 490.8(9)(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.8(9)(b) | 10814-10814 | encoded | `s 490.8(9) the person is guilty of an offence`; `s 490.8(9) the class of the offence`; `s 490.8(9)(a) the punishment on conviction on indictment` (+1 more in the same unit) |
| s 490.81 | 10815-10846 | fork (F5, F11, F18) | its rows below (25 units, module ccc18-forfeiture) |
| s 490.81(1) | 10816-10818 | fork (F5, F11, F18) | `s 490.81(1) the judge or justice may appoint a person to manage the property and require its possessor to give possession` |
| s 490.81(1)(a) | 10817-10817 | fork (F5, F11, F18) | `s 490.81(1) the judge or justice may appoint a person to manage the property and require its possessor to give possession` |
| s 490.81(1)(b) | 10818-10818 | fork (F5, F11, F18) | `s 490.81(1) the judge or justice may appoint a person to manage the property and require its possessor to give possession` |
| s 490.81(2) | 10819-10820 | encoded | `s 490.81(2) the judge or justice shall appoint the Minister of Public Works and Government Services`; `s 490.81(2) the duty of a judge` |
| s 490.81(3) | 10821-10825 | encoded | `s 490.81(3) the power to manage or otherwise deal with property includes the power` |
| s 490.81(3)(a) | 10823-10823 | encoded | `s 490.81(3) the power to manage or otherwise deal with property includes the power` |
| s 490.81(3)(b) | 10824-10824 | encoded | `s 490.81(3) the power to manage or otherwise deal with property includes the power` |
| s 490.81(3)(c) | 10825-10825 | encoded | `s 490.81(3) the power to manage or otherwise deal with property includes the power` |
| s 490.81(4) | 10826-10827 | encoded | `s 490.81(4) the person appointed to manage property shall apply to a court for a destruction order`; `s 490.81(4) the duty of a person appointed to manage property` |
| s 490.81(5) | 10828-10829 | encoded | `s 490.81(5) the court shall require notice to be given`; `s 490.81(5) the duty of the court` |
| s 490.81(6) | 10830-10833 | encoded | `s 490.81(6) the notice is as the subsection requires` |
| s 490.81(6)(a) | 10832-10832 | encoded | `s 490.81(6) the notice is as the subsection requires` |
| s 490.81(6)(b) | 10833-10833 | encoded | `s 490.81(6) the notice is as the subsection requires` |
| s 490.81(7) | 10834-10835 | encoded | `s 490.81(7) the court shall order that the property be destroyed`; `s 490.81(7) the duty of the court` |
| s 490.81(7.1) | 10836-10840 | encoded | `s 490.81(7.1) the court shall order the property forfeited to Her Majesty`; `s 490.81(7.1) the duty of the court to order the forfeiture` |
| s 490.81(7.1)(a) | 10838-10838 | encoded | `s 490.81(7.1) the court shall order the property forfeited to Her Majesty`; `s 490.81(7.1) the duty of the court to order the forfeiture` |
| s 490.81(7.1)(b) | 10839-10839 | encoded | `s 490.81(7.1) the court shall order the property forfeited to Her Majesty`; `s 490.81(7.1) the duty of the court to order the forfeiture` |
| s 490.81(7.1)(c) | 10840-10840 | encoded | `s 490.81(7.1) the court shall order the property forfeited to Her Majesty`; `s 490.81(7.1) the duty of the court to order the forfeiture` |
| s 490.81(8) | 10841-10842 | encoded | `s 490.81(8) the management order ceases to have effect` |
| s 490.81(8.1) | 10843-10844 | encoded | `s 490.81(8.1) the management order applies to the net proceeds of the sale` |
| s 490.81(9) | 10845-10846 | encoded | `s 490.81(9) the Attorney General may apply to the judge or justice` |
| s 490.9 | 10847-10850 | fork (F18) | its rows below (4 units, module ccc18-forfeiture) |
| s 490.9(1) | 10848-10848 | encoded | `s 490.9(1) sections 489.1 and 490 apply to the property` |
| s 490.9(2) | 10849-10850 | fork (F18) | `s 490.9(2) (recognizance) the judge or justice may require the applicant to enter into a recognizance`; `s 490.9(2) (deposit) the judge or justice may require the applicant to deposit a sum of money or other valuable security` |
| s 491 | 10851-10859 | fork (F18) | its rows below (11 units, module ccc18-forfeiture, ccc18-weapons-evidence) |
| s 491(1) | 10852-10855 | encoded | `s 491(1) the thing is forfeited to Her Majesty` |
| s 491(1)(a) | 10853-10853 | encoded | `s 491(1) the thing is forfeited to Her Majesty` |
| s 491(1)(b) | 10854-10855 | encoded | `s 491(1) the thing is forfeited to Her Majesty` |
| s 491(2) | 10856-10857 | encoded | `s 491(2) the order the court shall make`; `s 491(2) the duty of the court to order the return or payment` |
| s 491(3) | 10858-10859 | encoded | `s 491(3) the person to whom the proceeds of the sale shall be paid` |
| s 491.1 | 10860-10878 | encoded | its rows below (12 units, module ccc18-weapons-evidence) |
| s 491.1(1) | 10861-10864 | encoded | `s 491.1(1) the court shall make an order under subsection (2) in respect of the property`; `s 491.1(1) the duty of the court to make an order in respect of the property`; `s 491.1(1) (section 490) section 490 does not apply in respect of the property` |
| s 491.1(1)(a) | 10862-10862 | encoded | `s 491.1(1) the court shall make an order under subsection (2) in respect of the property`; `s 491.1(1) the duty of the court to make an order in respect of the property`; `s 491.1(1) (section 490) section 490 does not apply in respect of the property` |
| s 491.1(1)(b) | 10863-10864 | encoded | `s 491.1(1) the court shall make an order under subsection (2) in respect of the property`; `s 491.1(1) the duty of the court to make an order in respect of the property`; `s 491.1(1) (section 490) section 490 does not apply in respect of the property` |
| s 491.1(2) | 10865-10868 | encoded | `s 491.1(2) the order the court shall make` |
| s 491.1(2)(a) | 10867-10867 | encoded | `s 491.1(2) the order the court shall make` |
| s 491.1(2)(b) | 10868-10868 | encoded | `s 491.1(2) the order the court shall make` |
| s 491.1(3) | 10869-10876 | encoded | `s 491.1(3) an order shall not be made under subsection (2)` |
| s 491.1(3)(a) | 10871-10871 | encoded | `s 491.1(3) an order shall not be made under subsection (2)` |
| s 491.1(3)(b) | 10872-10876 | encoded | `s 491.1(3) an order shall not be made under subsection (2)` |
| s 491.1(3)(b)(i) | 10873-10873 | encoded | `s 491.1(3) an order shall not be made under subsection (2)` |
| s 491.1(3)(b)(ii) | 10874-10874 | encoded | `s 491.1(3) an order shall not be made under subsection (2)` |
| s 491.1(3)(b)(iii) | 10875-10875 | encoded | `s 491.1(3) an order shall not be made under subsection (2)` |
| s 491.1(3)(b)(iv) | 10876-10876 | encoded | `s 491.1(3) an order shall not be made under subsection (2)` |
| s 491.1(4) | 10877-10878 | encoded | `s 491.1(4) the peace officers shall execute the order`; `s 491.1(4) the duty of a peace officer` |
| s 491.2 | 10879-10898 | fork (F5, F18) | its rows below (15 units, module ccc18-weapons-evidence) |
| s 491.2(1) | 10880-10880 | fork (F18) | `s 491.2(1) the person may take and retain a photograph of the property` |
| s 491.2(2) | 10881-10882 | encoded | `s 491.2(2) the photograph is admissible in evidence`; `s 491.2(2) the photograph has the same probative force as the property would have had if it had been proved in the ordinary way` |
| s 491.2(3) | 10883-10888 | encoded | `s 491.2(3) the certificate is admissible in evidence`; `s 491.2(3) the certificate is evidence of the statements contained in it without proof of the signature of the person appearing to have signed it` |
| s 491.2(3)(a) | 10885-10885 | encoded | `s 491.2(3) the certificate is admissible in evidence`; `s 491.2(3) the certificate is evidence of the statements contained in it without proof of the signature of the person appearing to have signed it` |
| s 491.2(3)(b) | 10886-10886 | encoded | `s 491.2(3) the certificate is admissible in evidence`; `s 491.2(3) the certificate is evidence of the statements contained in it without proof of the signature of the person appearing to have signed it` |
| s 491.2(3)(c) | 10887-10888 | encoded | `s 491.2(3) the certificate is admissible in evidence`; `s 491.2(3) the certificate is evidence of the statements contained in it without proof of the signature of the person appearing to have signed it` |
| s 491.2(4) | 10889-10890 | encoded | `s 491.2(4) the affidavit or solemn declaration is admissible in evidence`; `s 491.2(4) the affidavit or solemn declaration is evidence of the statements contained in it without proof of the signature or official character` |
| s 491.2(5) | 10891-10892 | encoded | `s 491.2(5) the photograph, certificate, affidavit or solemn declaration shall not be received in evidence` |
| s 491.2(6) | 10893-10894 | fork (F5) | `s 491.2(6) the court may require the person who appears to have signed to appear for examination or cross-examination` |
| s 491.2(7) | 10895-10896 | fork (F18) | `s 491.2(7) the court may order the property to be produced in court or made available for examination` |
| s 491.2(8) | 10897-10898 | encoded | `s 491.2(8) photograph` |
| s 491.2(8) "photograph" | 10898-10898 | encoded | `s 491.2(8) photograph` |
| s 492 | 10899-10904 | fork (F5) | its rows below (8 units, module ccc18-weapons-evidence) |
| s 492(1) | 10900-10900 | fork (F5) | `s 492(1) the person may seize the thing`; `s 492(1) the duty of the person who executes the warrant to remove and detain what they seize`; `s 492(1) the thing shall be detained` |
| s 492(2) | 10901-10902 | encoded | `s 492(2) the thing is forfeited and shall be dealt with as the court directs` |
| s 492(3) | 10903-10904 | encoded | `s 492(3) the proceeds of the sale shall be paid to the Attorney General` |
| s 492.1 | 10905-10930 | fork (F3, F5, F18) | its rows below (23 units, module ccc18-tracking, ccc18-weapons-evidence) |
| s 492.1(1) | 10906-10906 | fork (F5) | `s 492.1(1) the justice or judge may issue a warrant for a tracking device`; `s 492.1(1) the power of the justice or judge to issue the warrant` |
| s 492.1(2) | 10907-10908 | fork (F5) | `s 492.1(2) the justice or judge may issue a warrant for a tracking device, for an individual`; `s 492.1(2) the power of the justice or judge to issue the warrant` |
| s 492.1(3) | 10909-10910 | fork (F5) | `s 492.1(3) the warrant authorizes the act` |
| s 492.1(4) | 10911-10912 | fork (F5) | `s 492.1(4) the warrant may contain the condition` |
| s 492.1(5) | 10913-10914 | fork (F3) | `s 492.1(5) the day a number of days after the day`; `s 492.1(6) one year after the day`; `s 492.1(5) the warrant is valid for the period specified in it` |
| s 492.1(6) | 10915-10919 | encoded | `s 492.1(6) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.1(6)(a) | 10917-10917 | encoded | `s 492.1(6) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.1(6)(b) | 10918-10918 | encoded | `s 492.1(6) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.1(6)(c) | 10919-10919 | encoded | `s 492.1(6) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.1(6.1) | 10920-10921 | fork (F5) | `s 492.1(6.1) (place) the warrant may be executed at the place`; `s 492.1(6.1) (officer) the officer who executes the warrant has the authority the subsection requires` |
| s 492.1(7) | 10922-10923 | fork (F18) | `s 492.1(7) the justice or judge may authorize the covert removal of the tracking device after the expiry of the warrant`; `s 492.1(7) the authorization is valid for the period specified in it` |
| s 492.1(8) | 10924-10930 | fork (F18) | its rows below (7 units, module ccc18-tracking) |
| s 492.1(8) "data" | 10926-10926 | encoded | `s 492.1(8) "data" data` |
| s 492.1(8) "judge" | 10927-10927 | encoded | `s 492.1(8) "judge"` |
| s 492.1(8) "public officer" | 10928-10928 | encoded | `s 492.1(8) "public officer"` |
| s 492.1(8) "tracking data" | 10929-10929 | encoded | `s 492.1(8) "tracking data" tracking data` |
| s 492.1(8) "tracking device" | 10930-10930 | encoded | `s 492.1(8) "tracking device"` |
| s 492.2 | 10931-10955 | fork (F5) | its rows below (17 units, module ccc18-tracking) |
| s 492.2(1) | 10932-10932 | fork (F5) | `s 492.2(1) the justice or judge may issue a warrant for a transmission data recorder`; `s 492.2(1) the power of the justice or judge to issue the warrant` |
| s 492.2(2) | 10933-10934 | fork (F5) | `s 492.2(2) the warrant authorizes the act` |
| s 492.2(3) | 10935-10936 | encoded | `s 492.2(3) no warrant shall be issued under this section` |
| s 492.2(4) | 10937-10938 | encoded | `s 492.2(4) the warrant is valid for the period specified in it` |
| s 492.2(5) | 10939-10943 | encoded | `s 492.2(5) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.2(5)(a) | 10941-10941 | encoded | `s 492.2(5) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.2(5)(b) | 10942-10942 | encoded | `s 492.2(5) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.2(5)(c) | 10943-10943 | encoded | `s 492.2(5) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.2(5.1) | 10944-10945 | fork (F5) | `s 492.2(5.1) (place) the warrant may be executed at the place`; `s 492.2(5.1) (officer) the officer who executes the warrant has the authority the subsection requires` |
| s 492.2(6) | 10946-10955 | fork (F5) | its rows below (7 units, module ccc18-tracking) |
| s 492.2(6) "data" | 10948-10948 | encoded | `s 492.2(6) "data" data` |
| s 492.2(6) "judge" | 10949-10949 | encoded | `s 492.2(6) "judge"` |
| s 492.2(6) "public officer" | 10950-10950 | encoded | `s 492.2(6) "public officer"` |
| s 492.2(6) "transmission data" | 10951-10954 | encoded | `s 492.2(6) "transmission data"` |
| s 492.2(6) "transmission data" para (a) | 10952-10952 | encoded | `s 492.2(6) "transmission data"` |
| s 492.2(6) "transmission data" para (b) | 10953-10953 | encoded | `s 492.2(6) "transmission data"` |
| s 492.2(6) "transmission data" para (c) | 10954-10954 | encoded | `s 492.2(6) "transmission data"` |
| s 492.2(6) "transmission data recorder" | 10955-10955 | encoded | `s 492.2(6) "transmission data recorder"` |

## Fork register (ccc18)

Every site where the text can be read two ways with different outcomes: the provision, the readings, the one taken, and the text that licenses each.
A coverage row marked `fork (Fn)` points here.
Where a ruling governs, its wording is repeated at the end of this section.

- **F1 -- Bearers of duties that the core's `Party` lacks.**
  - Text: The person who served the notice (490.021(6), 490.02903(3)); a police service (490.02911(3)); the Commissioner of the Royal Canadian Mounted Police or a person authorized by the Commissioner (490.03); the person in charge of the place of custody (490.02915(1)); the applicant (490.5(3)); a person appointed to manage property (490.81(4)); the person who executes the warrant (492(1)).
  - Taken: A one-constructor local type `s <label> party` for each such rule, recorded in NEEDS-CORE.md for the lead to hoist.
    No bearer is invented: each is the text's own words.
  - Other reading: Using the nearest core constructor (`a public officer`, `a peace officer`, `the keeper of a prison`) would name a bearer the text does not.
- **F2 -- "it", "a court" and "the appeal court" as parties.**
  - Text: 490.025 and 490.02907(1) say "it" for a court that refuses an exemption order or an appeal court that quashes one; 490.024(2) and kin say "the appeal court", which this range does not define.
  - Taken: "it" and "a court" are the core's `the court` ("the court the provision in question names"); "the appeal court" is the core's `a court of appeal`.
  - Other reading: "appeal court" is defined elsewhere (ss 673, 812, 829 for their Parts); if a Part-scoped definition differs from s 2 "court of appeal", the actor constructor changes.
- **F3 -- Counting the day, and dates that roll.**
  - Text: "within one year after the day on which the Sex Offender Information Registration Act comes into force" (490.021(1)) and "after the day of their transfer to Canada" (490.029111(1), 490.029112(1)); "within one year after they are served" and "within thirty days after the forfeiture" (490.023(1), 490.02905(1), 490.029051(1), 490.5(1)); "six month period beginning on the day on which the warrant was issued" (490.2(3)).
  - Taken: After "the day" of another event or Act, the day itself is not "after" it (tests: the day itself answers JUST FALSE).
    After an event the person is served with or an order made, the same day is in time.
    One year after is the same date a year later; the last day of a six-month period beginning on a day is the day before the same date six months later.
    The `Date` constructor rolls an impossible date forward, so a 29 February anniversary becomes 1 March and a period beginning on 31 August is taken to end on 2 March (30 February rolls forward); no test asserts these two edges.
  - Other reading: The Interpretation Act is not among the sources.
    The other reading counts the day itself, or ends the one-year period the day before the anniversary, or clamps a month-end to the last day of the month (28 February).
- **F4 -- "has elapsed" counts to the anniversary day.**
  - Text: 490.026(2), (3), (5); 490.02908(2) to (4); 490.02912(2) to (4): "if the following period has elapsed since they were sentenced".
  - Taken: The period has elapsed on the anniversary day itself (sentenced 1 June 2005: five years have elapsed on 1 June 2010; tests assert 31 May 2010 as not yet).
  - Other reading: Elapsed only at the end of the anniversary day, so from the next day.
- **F5 -- "may ... if [a condition]": NOTHING or JUST FALSE.**
  - Text: Every function NAMED for a grant or a power ("may", "is permitted to", "power", "authorizes") whose gate is introduced by "if" or is a named complement (a relative clause, a listed object, a scope): 19 functions with an "if" gate and 37 with a named-complement gate, and three of the functions kept JUST FALSE for a closed gate that also carry an "if" gate (490.4(3), 490.029051(1), 490.029112(1)); each is named in the sweep subsection (class A1, A2 and K), and the coverage rows over them read `fork (F5)`.
  - Taken: NOTHING (brief, ruling of 2026-11-12 (1)): the text grants a power "if" the gate holds and does not say the power is lacking otherwise.
    All of them were written as NOTHING in the first pass; the sweep of 2026-11-12 changed none in this direction.
  - Other reading: JUST FALSE by the periods ruling of 2026-11-05 (a)/(b) (a failed condition is the text's no, read clause by clause: the status quo of marginal reading (a)); the brief's ruling (1) of 2026-11-12 chose NOTHING for a grant, and a lawyer may overrule.
- **F6 -- "within seven days after the day on which they arrive in Canada".**
  - Text: 490.02911(1) and (2).
  - Taken: Advising on the day of arrival, or of the change, is in time (the window runs from that day to the seventh day after it); the rule is traced in days from day 0 with `WITHIN 7`, so an act on day 7 is in time and `WAITUNTIL 8` breaches.
  - Other reading: The seven days start the day after arrival, so advising on the day itself is "before" the period; or the last day is the sixth day after.
- **F7 -- Overlap of 490.022(3)(a), (c) and (d), and of 490.02904(3)(a) to (d).**
  - Text: (a) "if the offence was prosecuted summarily or if the maximum term ... is two or five years"; (c) "if the maximum term ... is life"; (d) "applies for life if ... more than one offence ... and if more than one of those offences is listed in the notice".
  - Taken: (d) first (it is the only way the multi-offence rule can bite); then (a) (so a summarily prosecuted offence with a life maximum ends after 10 years: tested); then (b), then (c).
  - Other reading: (c) before (a), so a life maximum prosecuted summarily is for life; or (a) to (c) before (d), so (d) never overrides a shorter term.
- **F8 -- Judgments the text hands to the court or a judge, and the lists of what the court shall consider.**
  - Text: "if it is satisfied that the person has established that ..." (490.023(2), 490.027(1), 490.02905(2), 490.029051(2), 490.02909(1), 490.029111(2), 490.029112(2), 490.02913(1), 490.04(5), 490.05(4)); "where the judge is satisfied" (490.2(2), 490.5(4)); the factors of 490.027(1.1), 490.02905(2.1), 490.02909(1.1), 490.029111(3), 490.02913(1.1), 490.04(6).
  - Taken: Each satisfaction is a BOOLEAN input, never computed from the facts; the (a) to (g) factors are a table of what the court "shall consider" (paragraph (g), "any other factors that the court considers relevant", is itself in the list and takes the court's relevance as an input), not a test that decides the order.
  - Other reading: None open in the text: the grounds are the court's to find.
    A reviewer who wanted the court's reasoning encoded would need a model of the factors' weights, which the text does not give.
- **F9 -- "For greater certainty, ... is a reasonable excuse if" (490.031(2)).**
  - Text: 490.031(2): "a lawful command that prevents a person from complying with an order or obligation is a reasonable excuse if, at the time, the person is subject to the Code of Service Discipline".
  - Taken: NOTHING when the person is not subject to the Code of Service Discipline: the clause declares a case "for greater certainty" and does not say that a lawful command is never otherwise a reasonable excuse.
  - Other reading: JUST FALSE by marginal reading (a) (a failed "if" counts as the text's no).
- **F10 -- "Subject to sections 490.3 to 490.41".**
  - Text: 490.1(1) and 490.2(2).
  - Taken: The orders of 490.4(3) (return to an innocent owner) and 490.41(3) (non-forfeiture for disproportion) prevail: the composite functions answer JUST FALSE when either is made.
    490.3 (setting aside a transfer) and the notice duties of 490.4(1) and 490.41(1) are separate functions and do not change the answer.
  - Other reading: "Subject to" read as a procedural precondition only (notice first), leaving the forfeiture duty intact until the order is made.
- **F11 -- "other than X" read as an exclusion.**
  - Text: 490.4(3) ("other than a person who was charged"); 490.5(1) ("other than (a) ... (b) ... (c)"); 490.81(1) ("other than a controlled substance ... or cannabis").
  - Taken: JUST FALSE for the excluded case (the maintainer's rule of 2026-11-05: decide case by case; the exclusion is in the text's own words).
  - Other reading: NOTHING: the clause limits a grant and says nothing of the excluded person.
- **F12 -- "at least fifteen days before" and "until thirty days have expired".**
  - Text: 490.5(2), (3) and 490.7.
  - Taken: 490.5(3) is a decision function over dates (service at least 15 days before the hearing) and a rule traced with `WITHIN 15` from an assumed day 0; 490.7 bars disposal through the thirtieth day after the order, so the thirty-first day is free.
  - Other reading: Thirty days "have expired" at the start of the thirtieth day; a rule with a real deadline anchor (`OF THE DEADLINE`) would need a build the stable binary lacks.
- **F13 -- "direct that (a) ... or (b) ..." (490.5(6)).**
  - Text: 490.5(6)(a) return the property or (b) pay an amount equal to the value of the interest.
  - Taken: One action constructor naming both alternatives: the text gives the Attorney General no rule for choosing.
  - Other reading: Two actions joined by `ROR`.
- **F14 -- Penalty sections that state no penalty.**
  - Text: 490.0312 ("an offence punishable on summary conviction") and 490.8(9)(b).
  - Taken: The `Punishment` record has `no imprisonment is stated` and `no fine is stated`; the general penalty for an offence punishable on summary conviction is in another part (s 787), not among the sources.
  - Other reading: Importing the maximum from s 787 would answer from memory.
- **F15 -- An offence whose element is unmet answers NOTHING.**
  - Text: 490.031(1) ("without reasonable excuse"), 490.0311 ("knowingly"), 490.0312, 490.8(9).
  - Taken: NOTHING (brief: a prohibition limited by its own wording, "without", answers NOTHING outside the limit), so a person with a reasonable excuse is told the section does not say they are guilty, not that they are innocent.
  - Other reading: JUST FALSE for an unmet element (the offence is defined by its elements).
- **F16 -- The day of deemed absconding (490.2(3)).**
  - Text: "the accused is deemed to have so absconded on the last day of that six month period".
  - Taken: A warrant issued on 1 January 2020 gives 30 June 2020 (the period begins on the day of issue).
  - Other reading: The last day is the same date six months later (1 July 2020).
- **F17 -- Proceedings and offences named by section number.**
  - Text: 490.03(1) (the proceedings of sections 490.012, 490.016, 490.023, ...), 491.1(3)(a), 491.2(1), 492.1(6)(a), 492.2(5)(a).
  - Taken: Tested against the core's `Provision of the Code` (rule R1): no input from another part.
    490.03(1)(b)'s appeal limb is a separate BOOLEAN.
    467.11 to 467.13 are tested as a range of the decimal.
  - Other reading: Asking each proceeding as a yes or no.
- **F18 -- "may" with a gate of the where/when/upon kind: listed, not decided.**
  - Text: 10 functions named for a power whose gate, tested by the function as an input of its own, is introduced by "where" or by an equivalent: 6 with a gate of that kind alone (class W: 490.5(4), 490.9(2) recognizance, 490.9(2) deposit and 491.2(7), on "where"; 490.026(4) and 490.02912(3.1), on "once") and 4 with it beside an "if" or a named complement (class WM: 490.026(5), "once"; 490.81(1), "on application" and "in the case of"; 491.2(1), "before"; 492.1(7), "on ex parte application" and "after the expiry").
    "On such an application", "in the case of" and "after ..." are in the instruction's list of equivalents (assumed, not ruled); "once" and "before" are NOT in it: they are this part's own reading of "when" and "after", and they decide 490.026(4) and 490.02912(3.1) (the only two answers this pass changed) and the two WM functions 490.026(5) and 491.2(1).
    Where-kind frames that a function does not test as an input of its own, so that no answer of theirs can arise, are not listed: 490.3 ("before ordering"), 490.4(1) and 490.41(1) ("before making an order", inside one composite input), 490.5(1) ("Where any offence-related property is forfeited") and 490.8(3) ("Where an application ... is made").
  - Taken: Class W answers JUST FALSE where the gate fails, as ruling (b) of the periods ruling and ruling (c) of the 2026-11-05 delegated ruling give ("when", "upon" and "whenever" count as "where"), and carries `[may-where]`.
    Class WM answers NOTHING because the function has a second gate whose failure the guide answers NOTHING, and one answer is possible.
    490.026(4) and 490.02912(3.1) answered NOTHING until the resumed pass of 2026-11-16 and now answer JUST FALSE; the lead may overrule those two changes, and the two assertions that carry them are restated in place.
  - Other reading: NOTHING for class W (the guide's line on grants: a grant limited by its own wording and the case outside the limit); JUST FALSE for the where-kind limb of class WM; NOTHING again for 490.026(4) and 490.02912(3.1) if "once" is not read as "when".
    A question for the maintainer or a lawyer, not one to settle by sweep (the lead's instruction of 2026-11-12).
- **F19 -- "entitled"-named functions: listed, not decided.**
  - Text: No function of this range has "entitled" in its name (count: 0; checked by `work/sweep.py` over every layer-1 name).
    Several texts say "lawfully entitled to possession" (490.4(3)) or "entitled" in a defined sense; those words sit inside an input's name, not in a function's.
  - Taken: Nothing to decide here.
  - Other reading: If a later edit names a function "entitled", an entitlement is a claim, not a power, and the guide does not settle it: list it here.

### Name-test sweep of 2026-11-12

Written 2026-11-16 (the instruction is dated 2026-11-12).
Every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised/authorized" was found by `work/sweep.py` (91 functions; the lists below name every one, nothing was selected by tag).
Each was classified by the words that open its gate in the text (printed beside the A1 and A2 names; quoted for the others), counting a gate only if the function tests it as an input of its own, and the classification was cross-checked against the code by the same script (a function classified as answering NOTHING must contain no JUST FALSE branch, a where-kind function must carry `[may-where]` and a JUST FALSE branch, and so on: 0 disagreements).
Each function is counted once: where-kind first, then kept JUST FALSE, then NOTHING under F5.
**"once" and "before" are this part's own extension of the instruction's list of equivalents** (which names "in the case of", "so long as", "while", "on payment", "on such an application", "after ..." and "on ..."); the two answers this pass changed rest on it, so the lead can overrule them (F18).
The class W and WM rows are listed here and in the fork register only, as the instruction says, and are not repeated in the Marginal readings table.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| **0** in this pass (56 functions answer NOTHING under F5; every one was written so in the first pass, on the brief's ruling, and none answered JUST FALSE for a failed "if") | **16** | **10** (6 alone, 4 beside an "if" or a named complement) | **0** |

What this pass changed in the code, apart from the flips (none): two functions that answered NOTHING on a gate introduced by "once" now answer JUST FALSE, listed (class W): `s 490.026(4)` and `s 490.02912(3.1)` ("once" read as "when", which is this part's own extension of the instruction's list of equivalents (assumed, not ruled), so the lead can overrule both; the two assertions that expected NOTHING are restated in place with `-- RECONCILED 2026-11-12`; no other function and no seat question calls either).
The four functions of class WM keep NOTHING.
Outside the sweep: "it is lawful, scoped: **0**; it is lawful, unscoped and retitled: **0**" (no function of this range is named "it is lawful ..."; `s 490.031(2) a lawful command is a reasonable excuse` is scoped and is not a grant: it answers NOTHING by F9).

**Listed: "may" with a where/when/upon-kind gate, class W: answers JUST FALSE, `[may-where]`, fork F18 (6)**

- `s 490.026(4) the person may apply for a termination order, despite subsections (2) and (3)` (soira-notice:605); gate: "once they receive a pardon, once a record suspension is ordered or once they are absolutely discharged"; gate "once", which is not in the instruction's list of equivalents: this part's own reading of "when" (assumed, not ruled); changed in the resumed pass of 2026-11-16 from NOTHING to JUST FALSE
- `s 490.02912(3.1) the person may apply for a termination order, despite subsections (2) and (3)` (soira-itoa:420); gate: "once they are absolutely discharged under paragraph 672.54(a)"; gate "once", which is not in the instruction's list of equivalents: this part's own reading of "when" (assumed, not ruled); changed in the resumed pass of 2026-11-16 from NOTHING to JUST FALSE
- `s 490.5(4) the judge may make an order declaring that the interest of the applicant is not affected by the forfeiture` (forfeiture:473); gate: "Where, on the hearing of an application made under subsection (1), the judge is satisfied"
- `s 490.9(2) (recognizance) the judge or justice may require the applicant to enter into a recognizance` (forfeiture:933); gate: "Where, pursuant to subsection (1), an order is made ... the judge or justice making the order may require"
- `s 490.9(2) (deposit) the judge or justice may require the applicant to deposit a sum of money or other valuable security` (forfeiture:944); gate: "where the judge or justice considers it appropriate"
- `s 491.2(7) the court may order the property to be produced in court or made available for examination` (weapons-evidence:354); gate: "where the court is satisfied that the interests of justice so require"

**Listed: "may" with a where/when/upon-kind gate beside another gate, class WM: answers NOTHING, fork F18 (4)**

- `s 490.026(5) the person may apply again for a termination order` (soira-notice:620); gate: "may apply again if five years have elapsed ..." (if) and "They may also apply again once they receive a pardon or once a record suspension is ordered" (once); "they may not apply again if" (closed); "once" is this part's own reading of "when" (not in the instruction's list); the "if" limb gives NOTHING, the "once" limb would give JUST FALSE; one answer is possible, so NOTHING
- `s 490.81(1) the judge or justice may appoint a person to manage the property and require its possessor to give possession` (forfeiture:726); gate: "on application of the Attorney General or of any other person with the written consent of the Attorney General, a judge or justice in the case of ..." (on application; in the case of), "if he or she is of the opinion that the circumstances so require" (if), and "other than a controlled substance" (closed: JUST FALSE, F11); the exclusion answers JUST FALSE; the application, the case and the opinion answer NOTHING
- `s 491.2(1) the person may take and retain a photograph of the property` (weapons-evidence:229); gate: "Before any property ... is returned or ordered to be returned, forfeited or otherwise dealt with" (before) with the listed offences and the peace officer (named complements); "before" is this part's own reading of "after ..." (not in the instruction's list); one answer is possible, so NOTHING
- `s 492.1(7) the justice or judge may authorize the covert removal of the tracking device after the expiry of the warrant` (tracking:169); gate: "On ex parte application supported by an affidavit" (on) and "after the expiry of the warrant" (after), with the named judge and the conditions "that the justice or judge considers advisable"; four inputs: two where-kind, two named complements; one answer is possible, so NOTHING

**Listed: "entitled" (0).**
No function name contains "entitled".

**Kept JUST FALSE, class K (16)**, in three named sub-rows so that none is folded silently into "closed by the text":

- closed by "only if", "unless", "shall not" or "may not": 9
  - `s 490.02(1) the Attorney General or minister of justice may serve the person with a notice` (soira-notice:40); gate: "may serve a person with a notice only if"
  - `s 490.02 the notice may be served, subject to subsection (2)` (soira-notice:83); gate: "A notice shall not be served on a person"
  - `s 490.026(1) the person may apply for a termination order` (soira-notice:553); gate: "unless they are also subject to an obligation under section 490.02901"
  - `s 490.02902(1) the Attorney General or minister of justice may serve the person with a notice in Form 54` (soira-foreign:50); gate: "may serve a person with a notice in Form 54 only if"
  - `s 490.02902 the notice in Form 54 may be served, subject to subsection (2)` (soira-foreign:72); gate: "The notice shall not be served on a person who has been acquitted"
  - `s 490.02908(1) the person may apply for a termination order` (soira-foreign:576); gate: "unless they are also subject to another obligation"
  - `s 490.02912(1) the person may apply for a termination order` (soira-itoa:373); gate: "unless they are also subject to an obligation under section 490.019 or 490.02901"
  - `s 490.3 the court may set aside the conveyance or transfer` (forfeiture:223); gate: "unless the conveyance or transfer was for valuable consideration to a person acting in good faith"
  - `s 490.81(9) the Attorney General may apply to the judge or justice` (forfeiture:909); gate: "but may not apply to vary an appointment made under subsection (2)"
- closed by "other than" (fork F11: read as an exclusion): 2
  - `s 490.4(3) the court may order that the property be returned to the person` (forfeiture:285); gate: "other than a person who was charged ..." (exclusion, F11); the "if the court is satisfied" gate answers NOTHING (F5)
  - `s 490.5(1) the person may apply for an order under subsection (4)` (forfeiture:405); gate: "other than (a) ... (b) ... (c)" (exclusion, F11) and "within thirty days after the forfeiture" (a period)
- a period the text fixes in its own words (periods ruling (a)): 5
  - `s 490.023(1) the person may apply for an exemption order` (soira-notice:366); gate: "within one year after they are served with a notice" (a period)
  - `s 490.02905(1) the person may apply for an exemption order` (soira-foreign:179); gate: "within one year after they are served" (a period); "A person who is served with a notice" answers NOTHING
  - `s 490.029051(1) the person may apply for a variation order` (soira-foreign:350); gate: "within one year after they are served" (a period); the "if" gate of paragraphs (a) and (b) answers NOTHING (F5)
  - `s 490.029111(1) the person may apply for an exemption order` (soira-itoa:25); gate: "within one year after the day of their transfer to Canada" (a period)
  - `s 490.029112(1) the person may apply for a variation order` (soira-itoa:151); gate: "within one year after the day of their transfer to Canada" (a period); the "if" gate of paragraphs (a) and (b) answers NOTHING (F5)

**Answers NOTHING under F5, gate introduced by "if", class A1 (19)**

- `s 490.021(2) the notice may be served by registered mail at the person's last known address` (soira-notice:131); opens: "...e, or of any conditions set under this Act or under Part III of the National Defence Act, that relate to residence, the notice may"
- `s 490.021(3) the notice may be served by registered mail at the person's last known address, the person not being in compliance with the Ontario Act` (soira-notice:143); opens: "...th section 3 of the Ontario Act on the day on which the Sex Offender Information Registration Act comes into force, the notice may"
- `s 490.021(4) the notice may be served by registered mail at the person's last known address, the person having failed to comply` (soira-notice:155); opens: "...ct within one year after that day, the notice shall be served within one year after the day on which they failed to comply and may"
- `s 490.026(2) the person may apply for a termination order, the period since sentence having elapsed` (soira-notice:572); opens: "Time for application (2) A person may"
- `s 490.026(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` (soira-notice:592); opens: "More than one offence (3) If more than one offence is listed in the notice, the person may"
- `s 490.02908(2) the person may apply for a termination order, the period since sentence having elapsed` (soira-foreign:593); opens: "Time for application — one offence (2) The person may"
- `s 490.02908(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` (soira-foreign:612); opens: "...cation — more than one offence (3) If more than one offence is listed in the notice served under section 490.02903, the person may"
- `s 490.02908(4) the person may apply again for a termination order` (soira-foreign:625); opens: "Re-application (4) A person whose application is refused may"
- `s 490.02912(2) the person may apply for a termination order, the period since sentence having elapsed` (soira-itoa:390); opens: "Time for application — one offence (2) The person may"
- `s 490.02912(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` (soira-itoa:409); opens: "...opy of the Form 1 that was delivered under subparagraph 8(4)(a)(ii) of the International Transfer of Offenders Act, the person may"
- `s 490.02912(4) the person may apply again for a termination order` (soira-itoa:431); opens: "Re-application (4) A person whose application is refused may"
- `s 490.03(3) the prosecutor or the Attorney General may disclose the information to the presiding court` (soira-offences:99); opens: "Disclosure in proceedings (3) The prosecutor or the Attorney General may"
- `s 490.03121(1) the justice may issue a warrant in Form 6.4 to arrest the person` (soira-offences:255); opens: "...o believe that a person has contravened any of sections 4 to 5.1 of the Sex Offender Information Registration Act, the justice may"
- `s 490.1(2) the court may make an order of forfeiture under subsection (1) of property not shown to be related to the offence` (forfeiture:74); opens: "...or discharged, but the court is satisfied, beyond a reasonable doubt, that the property is offence-related property, the court may"
- `s 490.2(1) the Attorney General may make an application to a judge for an order of forfeiture` (forfeiture:115); opens: "...aid in respect of an indictable offence under this Act or the Corruption of Foreign Public Officials Act, the Attorney General may"
- `s 490.41(1) the court shall require notice to be given to the person, and may hear them` (forfeiture:301); opens: "...se, before making an order of forfeiture, a court shall require that notice in accordance with subsection (2) be given to, and may"
- `s 490.41(3) (decision) the court may decide not to order the forfeiture of the property or part of the property` (forfeiture:340); opens: "...commission of the offence and the criminal record, if any, of the person charged with or convicted of the offence, as the case may"
- `s 490.41(3) (restraint order) the court may revoke a restraint order made in respect of the property or part of it` (forfeiture:350); opens: "...commission of the offence and the criminal record, if any, of the person charged with or convicted of the offence, as the case may"
- `s 490.8(3) the judge may make a restraint order` (forfeiture:589); opens: "Restraint order (3) Where an application for a restraint order is made to a judge under subsection (1), the judge may"

**Answers NOTHING under F5, gate a named complement, a scope or a relative clause, class A2 (37)**

- `s 490.024(1) the appeal may be brought` (soira-notice:465); opens: "Appeal 490.024 (1) The Attorney General or the person who applied for an exemption order may"
- `s 490.024(1) the appeal court may do it` (soira-notice:482); opens: "490.024 (1) The Attorney General or the person who applied for an exemption order may"
- `s 490.029(1) the appeal may be brought` (soira-notice:778); opens: "Appeal 490.029 (1) The Attorney General or the person who applied for a termination order may"
- `s 490.029(1) the appeal court may do it` (soira-notice:795); opens: "490.029 (1) The Attorney General or the person who applied for a termination order may"
- `s 490.02906(1) the appeal may be brought` (soira-foreign:466); opens: "Appeal 490.02906 (1) The Attorney General or the person who applied for an exemption order or a variation order may"
- `s 490.02906(1) the appeal court may do it` (soira-foreign:486); opens: "490.02906 (1) The Attorney General or the person who applied for an exemption order or a variation order may"
- `s 490.0291(1) the appeal may be brought` (soira-foreign:750); opens: "Appeal 490.0291 (1) The Attorney General or the person who applied for a termination order may"
- `s 490.0291(1) the appeal court may do it` (soira-foreign:767); opens: "490.0291 (1) The Attorney General or the person who applied for a termination order may"
- `s 490.029113(1) the appeal may be brought` (soira-itoa:263); opens: "Appeal 490.029113 (1) The Attorney General or the person who applied for an exemption order or a variation order may"
- `s 490.029113(1) the appeal court may do it` (soira-itoa:283); opens: "490.029113 (1) The Attorney General or the person who applied for an exemption order or a variation order may"
- `s 490.02914(1) the appeal may be brought` (soira-itoa:556); opens: "Appeal 490.02914 (1) The Attorney General or the person who applied for a termination order may"
- `s 490.02914(1) the appeal court may do it` (soira-itoa:573); opens: "490.02914 (1) The Attorney General or the person who applied for a termination order may"
- `s 490.031(4) the sex offender may require the attendance of the person who signed the certificate for cross-examination` (soira-offences:171); opens: "Attendance and cross-examina­tion (4) The sex offender named in the certificate may"
- `s 490.03121(3) the warrant may be executed there` (soira-offences:294); opens: "Execution of warrant (3) The warrant may"
- `s 490.04(1) the person may apply to a court for an exemption order` (soira-additional:24); opens: "Additional Orders Application for exemption order 490.04 (1) A person may"
- `s 490.05(1) the person may apply to a court for a variation order` (soira-additional:222); opens: "Application for variation order 490.05 (1) A person may"
- `s 490.06(1) the appeal may be brought` (soira-additional:385); opens: "Appeal 490.06 (1) The Attorney General or the person who applied for an exemption order or a variation order may"
- `s 490.06(1) the appeal court may do it` (soira-additional:405); opens: "490.06 (1) The Attorney General or the person who applied for an exemption order or a variation order may"
- `s 490.1(2.1) an order may be issued in respect of property situated outside Canada` (forfeiture:84); opens: "Property outside Canada (2.1) An order may"
- `s 490.1(3) the appeal may be brought` (forfeiture:102); opens: "...convicted of an indictable offence under this Act or the Corruption of Foreign Public Officials Act, or the Attorney General, may"
- `s 490.2(4.1) an order may be issued in respect of property situated outside Canada` (forfeiture:197); opens: "Property outside Canada (4.1) An order may"
- `s 490.4(1) (hearing) the court may hear the person` (forfeiture:257); opens: "...1) or 490.2(2) in relation to any property, a court shall require notice in accordance with subsection (2) to be given to, and may"
- `s 490.5(5) the appeal may be brought` (forfeiture:491); opens: "Appeal from order made under subsection (4) (5) An applicant or the Attorney General may"
- `s 490.6 the person may appeal from the order` (forfeiture:528); opens: "...ders under subsection 490.2(2) 490.6 Any person who, in their opinion, is aggrieved by an order made under subsection 490.2(2) may"
- `s 490.8(1) the Attorney General may apply for a restraint order` (forfeiture:563); opens: "Application for restraint order 490.8 (1) The Attorney General may"
- `s 490.8(3.1) a restraint order may be issued in respect of property situated outside Canada` (forfeiture:599); opens: "Property outside Canada (3.1) A restraint order may"
- `s 490.8(4) the restraint order may be subject to the condition` (forfeiture:610); opens: "Conditions (4) A restraint order made by a judge under this section may"
- `s 491.2(6) the court may require the person who appears to have signed to appear for examination or cross-examination` (weapons-evidence:342); opens: "Attendance for examination (6) Notwithstanding subsection (3) or (4), the court may"
- `s 492(1) the person may seize the thing` (weapons-evidence:395); opens: "Seizure of explosives 492 (1) Every person who executes a warrant issued under section 487 may"
- `s 492.1(1) the justice or judge may issue a warrant for a tracking device` (tracking:39); opens: "...more transactions or the location or movement of a thing, including a vehicle, will assist in the investigation of the offence may"
- `s 492.1(2) the justice or judge may issue a warrant for a tracking device, for an individual` (tracking:62); opens: "...ying the location of a thing that is usually carried or worn by the individual will assist in the investigation of the offence may"
- `s 492.1(3) the warrant authorizes the act` (tracking:91); opens: "Scope of warrant (3) The warrant authorizes"
- `s 492.1(4) the warrant may contain the condition` (tracking:103); opens: "Conditions (4) A warrant may"
- `s 492.1(6.1) (place) the warrant may be executed at the place` (tracking:146); opens: "Execution in Canada (6.1) A warrant issued under this section may"
- `s 492.2(1) the justice or judge may issue a warrant for a transmission data recorder` (tracking:259); opens: "...mmitted against this or any other Act of Parliament and that transmission data will assist in the investigation of the offence may"
- `s 492.2(2) the warrant authorizes the act` (tracking:287); opens: "Scope of warrant (2) The warrant authorizes"
- `s 492.2(5.1) (place) the warrant may be executed at the place` (tracking:342); opens: "Execution in Canada (5.1) A warrant issued under subsection (1) may"

**Outside the sweep, with the reason (9)**

- `s 490.03(1) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the registered information` (soira-offences:33): a duty ("shall, on request, disclose"): the name matches only "authorized by the Commissioner"
- `s 490.03(2) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the information to the prosecutor or Attorney General` (soira-offences:78): a duty ("shall, on request, disclose"): the name matches only "authorized by the Commissioner"
- `s 490.03121(1) the power of the justice to issue the warrant` (soira-offences:264): a DEONTIC rule: gives no MAYBE answer
- `s 490.04(2) the person is not permitted to apply under paragraph (1)(b)` (soira-additional:36): a bar ("is not permitted to apply ... if"), answered by the rule for a prohibition limited by its own wording: NOTHING outside it
- `s 490.05(2) the person is not permitted to apply under paragraph (1)(c) or (d)` (soira-additional:236): a bar ("is not permitted to apply ... if"), answered by the rule for a prohibition limited by its own wording: NOTHING outside it
- `s 490.81(3) the power to manage or otherwise deal with property includes the power` (forfeiture:771): "includes": a list that is not closed, NOTHING by the rule for "includes"
- `s 492.1(1) the power of the justice or judge to issue the warrant` (tracking:46): a DEONTIC rule: gives no MAYBE answer
- `s 492.1(2) the power of the justice or judge to issue the warrant` (tracking:69): a DEONTIC rule: gives no MAYBE answer
- `s 492.2(1) the power of the justice or judge to issue the warrant` (tracking:266): a DEONTIC rule: gives no MAYBE answer

Every number above is the length of a list printed beside it: 6 + 4 + 16 + 19 + 37 + 9 = 91 functions matched.

### Rulings, word for word (ccc18)

Copied by script from BRIEF.md (lines 24 and 113-117); the wording is not edited.

**A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails (ruling of 2026-11-12, three limits).** A layer-1 function NAMED for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an "if" gate failed reads as "may not", a grant turned into a bar. The guide's "In short" sentence gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". (1) Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading. (2) Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question. (3) Do NOT decide two groups by yourself; list them in the fork register with a count and leave the answer as the guide's rulings give it: "may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer), and "entitled"-named functions (a claim, not a power).

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Jural relations (ccc18)

One row per provision that creates a relation, in Hohfeld's pairs: the party holding the right (claim), privilege (liberty), power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it.
A provision that creates no relation (a definition, a counting rule, a rule of reading, a repealed subsection, machinery) is listed once as `none`.
The table covers every section and subsection row of the range (checked by script: no section or subsection row is missing).

| section | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | L4 rule |
| --- | --- | --- | --- |
| s 490.02(1) | Attorney General or minister of justice: power to serve a Form 53 notice (only if ...) | the person convicted or found not criminally responsible: liability to be served | `s 490.02(1) the Attorney General or minister of justice may serve the person with a notice` |
| s 490.02(2) | the person: immunity from service in the three cases | Attorney General or minister of justice: disability | `s 490.02(2) a notice shall not be served on the person` |
| s 490.02(3) | none (a rule of reading: references to earlier versions) | none | `s 490.02(3) the reference is to the provision as it read from time to time before the day on which the subsection comes into force` |
| s 490.021(1) | the person: claim that the notice is served personally within one year | the Attorney General (the unnamed server, taken from s 490.02(1)): duty | `s 490.021(1) one year after the day`; `s 490.021(1) the notice is served within one year after the day on which the Sex Offender Information Registration Act comes into force` |
| s 490.021(2) | Attorney General: privilege to serve by registered mail on a person unlawfully at large or in breach of a residence term | that person: no-right to personal service | `s 490.021(2) the notice may be served by registered mail at the person's last known address` |
| s 490.021(3) | Attorney General: privilege to serve by registered mail on a person not in compliance with the Ontario Act | that person: no-right to personal service | `s 490.021(3) the notice may be served by registered mail at the person's last known address, the person not being in compliance with the Ontario Act` |
| s 490.021(4) | Attorney General: privilege to serve by registered mail, within one year after the failure | that person: no-right to personal service | `s 490.021(4) the notice may be served by registered mail at the person's last known address, the person having failed to comply`; `s 490.021(4) the notice is served within one year after the day on which the person failed to comply` |
| s 490.021(5) | the server: privilege to prove service by affidavit | the person served: no-right to demand other proof | `s 490.021(5) the affidavit is evidence of the service and the notice` |
| s 490.021(6) | Attorney General or minister of justice: claim to a copy of the affidavit and notice, without delay | the person who served the notice: duty | `s 490.021(6) the person who served the notice must send a copy of the affidavit and the notice`; `s 490.021(6) the duty of the person who served the notice, without delay` |
| s 490.022(1) | none (a counting rule: when the obligation under section 490.019 begins; the obligation itself is s 490.019) | none | `s 490.022(1) the day on which the obligation under section 490.019 begins` |
| s 490.022(2) | none (a counting rule: the earliest day on which the obligation ends) | none | `s 490.022(2) the earliest day on which the obligation ends` |
| s 490.022(3) | none (a counting rule: it ends 10 or 20 years after sentence, or applies for life) | none | `s 490.022(3) the band of the maximum term of imprisonment`; `s 490.022(3) the day a number of years after the day` (+1) |
| s 490.022(4) | none (a rule of reading: the definition designated offence as it read before the subsection came into force) | none | `s 490.022(4) the reference is to the definition as it read from time to time before the day on which the subsection comes into force` |
| s 490.023(1) | the person: power to apply for an exemption order within one year | court of criminal jurisdiction: liability | `s 490.023(1) the person may apply for an exemption order` |
| s 490.023(1.1) | none (a rule of jurisdiction) | none | `s 490.023(1.1) the application shall be made to a court of criminal jurisdiction` |
| s 490.023(2) | the person: claim to an exemption order if the court is satisfied | the court: duty | `s 490.023(2) the court shall make an exemption order`; `s 490.023(2) the duty of the court` |
| s 490.023(3) | the person: claim to reasons | the court: duty | `s 490.023(3) the court shall give reasons for its decision`; `s 490.023(3) the duty of the court` |
| s 490.023(4) | the person: claim to removal of the information from the database | the court: duty (to order); Royal Canadian Mounted Police: liability to the order | `s 490.023(4) the court shall also make an order for removal of the information from the database`; `s 490.023(4) the duty of the court` |
| s 490.024(1) | the Attorney General and the person who applied: power to appeal on a question of law or mixed law and fact | the other party and the appeal court: liability | `s 490.024(1) the appeal may be brought`; `s 490.024(1) the appeal court may do it` |
| s 490.024(2) | the person: claim to removal of the information (on appeal) | the appeal court: duty | `s 490.024(2) the appeal court shall also make an order for removal of the information from the database`; `s 490.024(2) the duty of a court of appeal` |
| s 490.025 | the person who applied: claim to be informed of the sections; the Commissioner and the Attorney General: claim to notification | the court (or appeal court): duty | `s 490.025 the court shall cause the notification and the information to be given`; `s 490.025 the duty of the court to cause the Commissioner and the Attorney General to be notified` (+1) |
| s 490.026(1) | the person subject to the obligation: power to apply for a termination order, unless a later obligation or order | the court: liability | `s 490.026(1) the person may apply for a termination order` |
| s 490.026(2) | the person: power to apply once the period since sentence has elapsed | the court: liability | `s 490.026(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.026(3) | the person: power to apply once 20 years have elapsed (several offences) | the court: liability | `s 490.026(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` |
| s 490.026(4) | the person: power to apply on a pardon, record suspension or absolute discharge | the court: liability | `s 490.026(4) the person may apply for a termination order, despite subsections (2) and (3)` |
| s 490.026(5) | the person: power to apply again after five years, a pardon or a record suspension; disability if they became subject to another obligation or order | the court: liability | `s 490.026(5) the person may apply again for a termination order` |
| s 490.026(6) | none (a rule of jurisdiction) | none | `s 490.026(6) the application shall be made to a court of criminal jurisdiction` |
| s 490.027(1) | the person: claim to a termination order if the court is satisfied | the court: duty | `s 490.027(1) the court shall make an order terminating the obligation`; `s 490.027(1) the duty of the court` |
| s 490.027(1.1) | the person: claim to the court's consideration of the factors | the court: duty | `s 490.027(1.1) the court shall consider the factor` |
| s 490.027(2) | the person: claim to reasons | the court: duty | `s 490.027(2) the court shall give reasons for its decision`; `s 490.027(2) the duty of the court` |
| s 490.027(3) | Commissioner and Attorney General: claim to notification | the court: duty | `s 490.027(3) the court shall cause the notification to be given`; `s 490.027(3) the duty of the court` |
| s 490.028 | the person: power (an application for one order counts for both) | the court: liability | `s 490.028 an application for one order is deemed to be an application for both` |
| s 490.029(1) | the Attorney General and the person who applied: power to appeal | the other party and the appeal court: liability | `s 490.029(1) the appeal may be brought`; `s 490.029(1) the appeal court may do it` |
| s 490.029(2) | Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.029(2) the appeal court shall cause the notification to be given`; `s 490.029(2) the duty of a court of appeal` |
| s 490.02901 | Her Majesty (the public): claim to compliance with the Act | the person served with a Form 54 notice: duty (unless an exemption order is made) | `s 490.02901 the person shall comply with the Sex Offender Information Registration Act`; `s 490.02901 the duty of the offender to comply` |
| s 490.02902(1) | Attorney General or minister of justice: power to serve a Form 54 notice (only if ...) | the person: liability | `s 490.02902(1) the Attorney General or minister of justice may serve the person with a notice in Form 54` |
| s 490.02902(2) | the person: immunity from service | Attorney General or minister of justice: disability | `s 490.02902(2) a notice shall not be served on the person`; `s 490.02902 the notice in Form 54 may be served, subject to subsection (2)` |
| s 490.02903(1) | the person: claim to personal service | the Attorney General: duty | `s 490.02903(1) the manner of service is the one the subsection requires` |
| s 490.02903(2) | the server: privilege to prove service by affidavit | the person served: no-right | `s 490.02903(2) the affidavit is evidence of the service and the notice` |
| s 490.02903(3) | Attorney General or minister of justice: claim to a copy, without delay | the person who served the notice: duty | `s 490.02903(3) the person who served the notice must send a copy of the affidavit and the notice`; `s 490.02903(3) the duty of the person who served the notice` |
| s 490.02904(1) | none (a counting rule: the obligation begins on the day the person is served) | none | `s 490.02904(1) the day on which the obligation under section 490.02901 begins` |
| s 490.02904(2) | none (a counting rule: the obligation ends on the day an exemption order is made) | none | `s 490.02904(2) the day on which the obligation ends` |
| s 490.02904(3) | none (a counting rule: it ends 10 or 20 years after sentence, or applies for life) | none | `s 490.02904(3) the obligation, if subsection (2) does not apply, ends or applies for life` |
| s 490.02905(1) | the person: power to apply for an exemption order within one year | court of criminal jurisdiction: liability | `s 490.02905(1) the person may apply for an exemption order` |
| s 490.02905(2) | the person: claim to an exemption order on any of four grounds | the court: duty | `s 490.02905(2) the court shall make an exemption order`; `s 490.02905(2) the duty of the court` |
| s 490.02905(2.1) | the person: claim to the court's consideration of the factors (grounds (c) and (d)) | the court: duty | `s 490.02905(2.1) the court shall consider the factor` |
| s 490.02905(2.2) | the Attorney General: claim to a corrected notice | the court: duty; the person: liability to the correction | `s 490.02905(2.2) the court shall order that the notice be corrected`; `s 490.02905(2.2) the duty of the court` |
| s 490.02905(3) | the person: claim to reasons | the court: duty | `s 490.02905(3) the court shall give reasons for its decision`; `s 490.02905(3) the duty of the court` |
| s 490.02905(4) | the person: claim to removal of the information | the court: duty | `s 490.02905(4) the court shall also make an order for removal of the information from the database`; `s 490.02905(4) the duty of the court` |
| s 490.02905(5) | Commissioner and Attorney General: claim to notification | the court: duty | `s 490.02905(5) the court shall cause the notification to be given`; `s 490.02905(5) the duty of the court` |
| s 490.029051(1) | the person: power to apply for a variation order within one year | court of criminal jurisdiction: liability | `s 490.029051(1) the person may apply for a variation order` |
| s 490.029051(2) | the person: claim to a variation order | the court: duty | `s 490.029051(2) the court shall make the variation order`; `s 490.029051(2) the duty of the court` |
| s 490.029051(3) | the person: claim to a duration set by paragraphs 490.02904(3)(a) and (b) | the court: duty | `s 490.029051(3) the duration of the obligation set out in the variation order`; `s 490.029051(3) the duty of the court to set out the duration` |
| s 490.029051(4) | the person: claim to reasons | the court: duty | `s 490.029051(4) the court shall give reasons for its decision`; `s 490.029051(4) the duty of the court` |
| s 490.029051(5) | Commissioner and Attorney General: claim to notification | the court: duty | `s 490.029051(5) the court shall cause the notification to be given`; `s 490.029051(5) the duty of the court` |
| s 490.02906(1) | the Attorney General and the person who applied: power to appeal | the other party and the appeal court: liability | `s 490.02906(1) the appeal may be brought`; `s 490.02906(1) the appeal court may do it` |
| s 490.02906(2) | the person: claim to removal of the information | the appeal court: duty | `s 490.02906(2) the appeal court shall also make an order for removal of the information from the database`; `s 490.02906(2) the duty of a court of appeal` |
| s 490.02907(1) | the person who applied: claim to be informed; Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.02907(1) the appeal court shall cause the notification and the information to be given`; `s 490.02907(1) the duty of the appeal court to cause the Commissioner and the Attorney General to be notified` (+1) |
| s 490.02907(2) | Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.02907(2) the appeal court shall cause the notification to be given`; `s 490.02907(2) the duty of a court of appeal` |
| s 490.02908(1) | the person subject to the obligation: power to apply for a termination order, unless a later obligation or order | court of criminal jurisdiction: liability | `s 490.02908(1) the person may apply for a termination order` |
| s 490.02908(2) | the person: power to apply once the period since sentence has elapsed | the court: liability | `s 490.02908(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02908(3) | the person: power to apply once 20 years have elapsed (several offences) | the court: liability | `s 490.02908(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` |
| s 490.02908(4) | the person: power to apply again after five years | the court: liability | `s 490.02908(4) the person may apply again for a termination order` |
| s 490.02909(1) | the person: claim to a termination order if the court is satisfied | the court: duty | `s 490.02909(1) the court shall make an order terminating the obligation`; `s 490.02909(1) the duty of the court` |
| s 490.02909(1.1) | the person: claim to the court's consideration of the factors | the court: duty | `s 490.02909(1.1) the court shall consider the factor` |
| s 490.02909(2) | the person: claim to reasons | the court: duty | `s 490.02909(2) the court shall give reasons for its decision`; `s 490.02909(2) the duty of the court` |
| s 490.02909(3) | Commissioner and Attorney General: claim to notification | the court: duty | `s 490.02909(3) the court shall cause the notification to be given`; `s 490.02909(3) the duty of the court` |
| s 490.0291(1) | the Attorney General and the person who applied: power to appeal | the other party and the appeal court: liability | `s 490.0291(1) the appeal may be brought`; `s 490.0291(1) the appeal court may do it` |
| s 490.0291(2) | Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.0291(2) the appeal court shall cause the notification to be given`; `s 490.0291(2) the duty of a court of appeal` |
| s 490.02911(1) | a police service: claim to be advised within seven days of arrival | the person convicted abroad: duty | `s 490.02911(1) the person must advise a police service`; `s 490.02911(1) the person advised a police service within seven days after the day on which they arrived in Canada` (+2) |
| s 490.02911(1.1) | the person: immunity from advising again unless later convicted abroad | a police service: disability | `s 490.02911(1.1) the person is required to advise the police service again` |
| s 490.02911(2) | a police service: claim to be advised of a change in address within seven days | the person in Canada: duty | `s 490.02911(2) the person must advise a police service of a change in address`; `s 490.02911(2) the person advised a police service of the change in address within seven days after the day on which the change was made` (+1) |
| s 490.02911(3) | Attorney General or minister of justice: claim to the information | the police service: duty | `s 490.02911(3) the police service shall cause the Attorney General or minister of justice to be provided with the information`; `s 490.02911(3) the duty of a police service` |
| s 490.02911(4) | none (a counting rule: when the duty of subsection (2) ends) | none | `s 490.02911(4) the day on which the obligation under subsection (2) ends` |
| s 490.029111(1) | the person subject to a section 36.1 obligation: power to apply for an exemption order within one year of transfer | court of criminal jurisdiction: liability | `s 490.029111(1) the person may apply for an exemption order` |
| s 490.029111(2) | the person: claim to an exemption order on either ground | the court: duty | `s 490.029111(2) the court shall make an exemption order`; `s 490.029111(2) the duty of the court` |
| s 490.029111(3) | the person: claim to the court's consideration of the factors | the court: duty | `s 490.029111(3) the court shall consider the factor` |
| s 490.029111(4) | the person: claim to reasons | the court: duty | `s 490.029111(4) the court shall give reasons for its decision`; `s 490.029111(4) the duty of the court` |
| s 490.029111(5) | the person: claim to removal of the information | the court: duty | `s 490.029111(5) the court shall also make an order for removal of the information from the database`; `s 490.029111(5) the duty of the court` |
| s 490.029112(1) | the person: power to apply for a variation order within one year of transfer | court of criminal jurisdiction: liability | `s 490.029112(1) the person may apply for a variation order` |
| s 490.029112(2) | the person: claim to a variation order | the court: duty | `s 490.029112(2) the court shall make the variation order`; `s 490.029112(2) the duty of the court` |
| s 490.029112(3) | the person: claim to a duration set under section 36.2 of the International Transfer of Offenders Act | the court: duty | `s 490.029112(3) the duration of the obligation set out in the variation order`; `s 490.029112(3) the duty of the court to set out the duration` |
| s 490.029112(4) | the person: claim to reasons | the court: duty | `s 490.029112(4) the court shall give reasons for its decision`; `s 490.029112(4) the duty of the court` |
| s 490.029112(5) | Commissioner and Attorney General: claim to notification | the court: duty | `s 490.029112(5) the court shall cause the notification to be given`; `s 490.029112(5) the duty of the court` |
| s 490.029113(1) | the Attorney General and the person who applied: power to appeal | the other party and the appeal court: liability | `s 490.029113(1) the appeal may be brought`; `s 490.029113(1) the appeal court may do it` |
| s 490.029113(2) | the person: claim to removal of the information | the appeal court: duty | `s 490.029113(2) the appeal court shall also make an order for removal of the information from the database`; `s 490.029113(2) the duty of a court of appeal` |
| s 490.029114(1) | the person who applied: claim to be informed; Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.029114(1) the appeal court shall cause the notification and the information to be given`; `s 490.029114(1) the duty of the appeal court to cause the Commissioner and the Attorney General to be notified` (+1) |
| s 490.029114(2) | Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.029114(2) the appeal court shall cause the notification to be given`; `s 490.029114(2) the duty of a court of appeal` |
| s 490.02912(1) | the person subject to a section 36.1 obligation: power to apply for a termination order, unless a later obligation or order | court of criminal jurisdiction: liability | `s 490.02912(1) the person may apply for a termination order` |
| s 490.02912(2) | the person: power to apply once the period since sentence has elapsed | the court: liability | `s 490.02912(2) the person may apply for a termination order, the period since sentence having elapsed` |
| s 490.02912(3) | the person: power to apply once 20 years have elapsed (several offences) | the court: liability | `s 490.02912(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` |
| s 490.02912(3.1) | the person: power to apply once absolutely discharged | the court: liability | `s 490.02912(3.1) the person may apply for a termination order, despite subsections (2) and (3)` |
| s 490.02912(4) | the person: power to apply again after five years | the court: liability | `s 490.02912(4) the person may apply again for a termination order` |
| s 490.02913(1) | the person: claim to a termination order if the court is satisfied | the court: duty | `s 490.02913(1) the court shall make an order terminating the obligation`; `s 490.02913(1) the duty of the court` |
| s 490.02913(1.1) | the person: claim to the court's consideration of the factors | the court: duty | `s 490.02913(1.1) the court shall consider the factor` |
| s 490.02913(2) | the person: claim to reasons | the court: duty | `s 490.02913(2) the court shall give reasons for its decision`; `s 490.02913(2) the duty of the court` |
| s 490.02913(3) | Commissioner and Attorney General: claim to notification | the court: duty | `s 490.02913(3) the court shall cause the notification to be given`; `s 490.02913(3) the duty of the court` |
| s 490.02914(1) | the Attorney General and the person who applied: power to appeal | the other party and the appeal court: liability | `s 490.02914(1) the appeal may be brought`; `s 490.02914(1) the appeal court may do it` |
| s 490.02914(2) | Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.02914(2) the appeal court shall cause the notification to be given`; `s 490.02914(2) the duty of a court of appeal` |
| s 490.02915(1) | the person subject to a section 36.1 obligation: claim to a copy of the Form 1, not earlier than 10 days before release | the person in charge of the place: duty | `s 490.02915(1) the person in charge of the place must give the person a copy of the Form 1`; `s 490.02915(1) the copy was given not earlier than 10 days before the release or discharge` (+1) |
| s 490.02915(2) | the person discharged: claim to a copy of the Form 1 | the Review Board: duty | `s 490.02915(2) the Review Board must cause a copy of the Form 1 to be given to the person`; `s 490.02915(2) the duty of the Review Board to cause a copy of the Form 1 to be given` |
| s 490.03(1) | the prosecutor and the Attorney General: claim to disclosure of the registered information on request; the person registered: liability to disclosure | the Commissioner or a person authorized: duty | `s 490.03(1) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the registered information`; `s 490.03(1)(a) the duty of the Commissioner to disclose to the prosecutor` (+1) |
| s 490.03(2) | the prosecutor and the Attorney General: claim to the information where the person discloses the fact of registration | the Commissioner: duty; the person: liability | `s 490.03(2) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the information to the prosecutor or Attorney General`; `s 490.03(2) the duty of the Commissioner to disclose to the prosecutor or Attorney General` |
| s 490.03(3) | the prosecutor and the Attorney General: privilege to disclose to the presiding court | the person: no-right | `s 490.03(3) the prosecutor or the Attorney General may disclose the information to the presiding court` |
| s 490.031(1) | Her Majesty: claim to compliance, and power to prosecute | the person subject to an order or obligation: duty and liability to the penalty | `s 490.031(1) the person is guilty of an offence`; `s 490.031(1) the class of the offence` (+2) |
| s 490.031(2) | the person subject to the Code of Service Discipline: privilege (a lawful command is a reasonable excuse) | Her Majesty: no-right | `s 490.031(2) a lawful command is a reasonable excuse` |
| s 490.031(3) | the prosecution: privilege to prove failure to report by certificate | the person: no-right to proof of the signature | `s 490.031(3) the certificate is evidence of the statements contained in it without proof of the signature or official character` |
| s 490.031(4) | the sex offender: power, with leave, to require the signer's attendance for cross-examination | the signer and the court: liability | `s 490.031(4) the sex offender may require the attendance of the person who signed the certificate for cross-examination` |
| s 490.031(5) | the person: immunity (no certificate received without a copy and notice before trial) | the party producing it: disability | `s 490.031(5) the certificate is not to be received in evidence` |
| s 490.0311 | Her Majesty: claim to true information, and power to prosecute | the person: duty and liability to the penalty | `s 490.0311 the person is guilty of an offence`; `s 490.0311 the class of the offence` (+2) |
| s 490.0312 | Her Majesty: claim to advice of the police service, and power to prosecute | the person: duty and liability to the penalty | `s 490.0312 the person is guilty of an offence`; `s 490.0312 the class of the offence` (+1) |
| s 490.03121(1) | a justice: power to issue a warrant to arrest; a peace officer: power to arrest under it | the person: liability | `s 490.03121(1) the justice may issue a warrant in Form 6.4 to arrest the person`; `s 490.03121(1) the power of the justice to issue the warrant` |
| s 490.03121(2) | the person: claim to conditions that make the arrest reasonable | the justice: duty | `s 490.03121(2) the warrant shall contain the condition`; `s 490.03121(2) the duty of the justice to put the conditions in the warrant` |
| s 490.03121(3) | a peace officer: privilege to execute the warrant anywhere in Canada | the person: no-right | `s 490.03121(3) the warrant may be executed there` |
| s 490.03121(4) | none (how long the warrant remains in force) | none | `s 490.03121(4) the warrant remains in force` |
| s 490.03121(5) | the person: immunity from a charge for a contravention they remedied after the warrant | the prosecutor: disability | `s 490.03121(5) no charge shall be laid against the person in respect of the contravention` |
| s 490.04(1) | the person: power to apply to a court for an exemption order | the court: liability | `s 490.04(1) the person may apply to a court for an exemption order` |
| s 490.04(2) | the person: disability (not permitted to apply under (1)(b) after an application for the same obligation) | the court: immunity | `s 490.04(2) the person is not permitted to apply under paragraph (1)(b)` |
| s 490.04(3) | none (a rule of jurisdiction) | none | `s 490.04(3) the court to which the application shall be made` |
| s 490.04(4) | the person: disability (no exemption order in the cases listed) | the court: disability | `s 490.04(4) the court shall not make an exemption order` |
| s 490.04(5) | the person: claim to an exemption order, subject to (4) | the court: duty | `s 490.04(5) the court shall make an exemption order`; `s 490.04(5) the duty of the court` |
| s 490.04(6) | the person: claim to the court's consideration of the factors | the court: duty | `s 490.04(6) the court shall consider the factor` |
| s 490.04(7) | the person: claim to reasons | the court: duty | `s 490.04(7) the court shall give reasons for its decision`; `s 490.04(7) the duty of the court` |
| s 490.04(8) | the person: claim to removal of the information | the court: duty | `s 490.04(8) the court shall also make an order for removal of the information from the database`; `s 490.04(8) the duty of the court` |
| s 490.05(1) | the person: power to apply for a variation order | the court: liability | `s 490.05(1) the person may apply to a court for a variation order` |
| s 490.05(2) | the person: disability (not permitted to apply under (1)(c) or (d) after an application for the same obligation) | the court: immunity | `s 490.05(2) the person is not permitted to apply under paragraph (1)(c) or (d)` |
| s 490.05(3) | none (a rule of jurisdiction) | none | `s 490.05(3) the court to which the application shall be made` |
| s 490.05(4) | the person: claim to a variation order | the court: duty | `s 490.05(4) the court shall make the variation order`; `s 490.05(4) the duty of the court` |
| s 490.05(5) | the person: claim to a duration set by the stated provisions | the court: duty | `s 490.05(5) the duration set out in the variation order`; `s 490.05(5) the duty of the court to set out the duration` |
| s 490.05(6) | the person: claim to reasons | the court: duty | `s 490.05(6) the court shall give reasons for its decision`; `s 490.05(6) the duty of the court` |
| s 490.05(7) | Commissioner and Attorney General: claim to notification | the court: duty | `s 490.05(7) the court shall cause the notification to be given`; `s 490.05(7) the duty of the court` |
| s 490.06(1) | the Attorney General and the person who applied: power to appeal | the other party and the appeal court: liability | `s 490.06(1) the appeal may be brought`; `s 490.06(1) the appeal court may do it` |
| s 490.06(2) | the person: claim to removal of the information | the appeal court: duty | `s 490.06(2) the appeal court shall also make an order for removal of the information from the database`; `s 490.06(2) the duty of a court of appeal` |
| s 490.07(1) | the person who applied: claim to be informed; Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.07(1) the appeal court shall cause the notification and the information to be given`; `s 490.07(1) the duty of the appeal court to cause the Commissioner and the Attorney General to be notified` (+1) |
| s 490.07(2) | Commissioner and Attorney General: claim to notification | the appeal court: duty | `s 490.07(2) the appeal court shall cause the notification to be given`; `s 490.07(2) the duty of a court of appeal` |
| s 490.1(1) | Her Majesty (in right of the province or of Canada): claim to forfeiture | the court: duty; the owner of offence-related property: liability | `s 490.1(1) the court shall order the property forfeited`; `s 490.1(1) the Crown in whose right the property is forfeited` (+2) |
| s 490.1(1.1) | none (repealed) | none | n/a |
| s 490.1(2) | the court: power to order forfeiture of property not shown related to the offence | the owner: liability | `s 490.1(2) the court may make an order of forfeiture under subsection (1) of property not shown to be related to the offence` |
| s 490.1(2.1) | none (scope: property outside Canada) | none | `s 490.1(2.1) an order may be issued in respect of property situated outside Canada` |
| s 490.1(3) | the convicted person and the Attorney General: power to appeal as a sentence appeal | the court of appeal: liability | `s 490.1(3) the appeal may be brought` |
| s 490.2(1) | the Attorney General: power to apply for in rem forfeiture | the judge: liability; the owner: liability | `s 490.2(1) the Attorney General may make an application to a judge for an order of forfeiture` |
| s 490.2(2) | Her Majesty: claim to forfeiture where the accused has died or absconded | the judge: duty; the owner: liability | `s 490.2(2) the judge shall order the property forfeited`; `s 490.2(2) the duty of the judge to order the forfeiture` (+1) |
| s 490.2(3) | none (a deeming rule: when an accused is deemed to have absconded) | none | `s 490.2(3) the day on which the accused is deemed to have absconded` |
| s 490.2(4) | Her Majesty in right of the province or of Canada: claim to the property | the judge: duty | `s 490.2(4) the Crown in whose right the judge shall order the property forfeited` |
| s 490.2(4.1) | none (scope: property outside Canada) | none | `s 490.2(4.1) an order may be issued in respect of property situated outside Canada` |
| s 490.2(5) | none (a definition of judge) | none | `s 490.2(5) judge` |
| s 490.3 | the court: power to set aside a transfer; a transferee for valuable consideration in good faith: immunity | the transferee otherwise: liability | `s 490.3 the court may set aside the conveyance or transfer` |
| s 490.4(1) | a person with a valid interest: claim to notice and privilege to be heard | the court: duty | `s 490.4(1) the court shall require notice to be given to the person`; `s 490.4(1) the duty of the court` (+1) |
| s 490.4(2) | a person with a valid interest: claim to notice of the stated content | the court: duty | `s 490.4(2) the notice is as the subsection requires` |
| s 490.4(3) | the court: power to return property to a lawful owner who appears innocent | Her Majesty: liability; the excluded persons: no-right | `s 490.4(3) the court may order that the property be returned to the person` |
| s 490.41(1) | a member of the immediate family who resides in the dwelling-house: claim to notice and privilege to be heard | the court: duty | `s 490.41(1) the court shall require notice to be given to the person, and may hear them`; `s 490.41(1) the duty of the court to require notice to the member of the immediate family` |
| s 490.41(2) | a member of the immediate family: claim to notice of the stated content | the court: duty | `s 490.41(2) the notice is as the subsection requires` |
| s 490.41(3) | the person charged or convicted: privilege (the court may decide not to forfeit, or revoke a restraint order) | the court: power; Her Majesty: liability | `s 490.41(3) (decision) the court may decide not to order the forfeiture of the property or part of the property`; `s 490.41(3) (restraint order) the court may revoke a restraint order made in respect of the property or part of it` |
| s 490.41(4) | a member of the immediate family: claim to the court's consideration of the impact and of their innocence | the court: duty | `s 490.41(4) the court shall also consider the matter` |
| s 490.5(1) | a person claiming an interest: power to apply within thirty days | the judge: liability | `s 490.5(1) the person may apply for an order under subsection (4)` |
| s 490.5(2) | the applicant: claim to a hearing not less than thirty days after filing | the judge: duty | `s 490.5(2) the day fixed is not less than thirty days after the date of the filing`; `s 490.5(2) the duty of the judge to fix the day` |
| s 490.5(3) | the Attorney General: claim to notice at least fifteen days before the hearing | the applicant: duty | `s 490.5(3) the notice was served at least fifteen days before the day fixed for the hearing`; `s 490.5(3) the duty of the applicant to serve the notice` |
| s 490.5(4) | the applicant: power-claim (the judge may declare their interest not affected) | the judge: power; Her Majesty: liability | `s 490.5(4) the judge may make an order declaring that the interest of the applicant is not affected by the forfeiture` |
| s 490.5(5) | the applicant and the Attorney General: power to appeal | the other party and the court of appeal: liability | `s 490.5(5) the appeal may be brought` |
| s 490.5(6) | the applicant: claim to the return of the property or payment of its value | the Attorney General: duty | `s 490.5(6) the Attorney General shall direct that the property be returned or the amount paid`; `s 490.5(6) the duty of the Attorney General to direct the return or the payment` |
| s 490.6 | a person aggrieved by an order under 490.2(2): power to appeal | the court: liability | `s 490.6 the person may appeal from the order` |
| s 490.7 | the person claiming the property: immunity from disposal pending applications and appeals, and for thirty days | the Attorney General and others: disability | `s 490.7 the operation of the order is suspended`; `s 490.7 the property shall not be disposed of or otherwise dealt with` |
| s 490.8(1) | the Attorney General: power to apply for a restraint order | the owner: liability | `s 490.8(1) the Attorney General may apply for a restraint order` |
| s 490.8(2) | the judge: claim to the stated form of application | the Attorney General: duty | `s 490.8(2) the application is in the form the subsection requires` |
| s 490.8(3) | the judge: power to make a restraint order | the person in possession: liability | `s 490.8(3) the judge may make a restraint order` |
| s 490.8(3.1) | none (scope: property outside Canada) | none | `s 490.8(3.1) a restraint order may be issued in respect of property situated outside Canada` |
| s 490.8(4) | the judge: power to attach reasonable conditions | the person served: liability | `s 490.8(4) the restraint order may be subject to the condition` |
| s 490.8(5) | the person served: claim to a restraint order in writing | the judge: duty | `s 490.8(5) the restraint order is made as the subsection requires` |
| s 490.8(6) | the person to whom the order is addressed: claim to service of a copy | the Attorney General: duty | `s 490.8(6) the copy of the restraint order is served as the subsection requires` |
| s 490.8(7) | third parties: claim to registration of the order against the property | the Attorney General: duty | `s 490.8(7) the copy of the restraint order is registered as the subsection requires` |
| s 490.8(8) | none (how long a restraint order remains in effect) | none | `s 490.8(8) the restraint order remains in effect` |
| s 490.8(9) | Her Majesty: claim to compliance, and power to prosecute | the person served: duty and liability to the penalty | `s 490.8(9) the person is guilty of an offence`; `s 490.8(9) the class of the offence` (+2) |
| s 490.81(1) | the Attorney General (or another person with consent): power to apply; the judge or justice: power to appoint a manager and require possession to be given | the possessor of the property: liability | `s 490.81(1) the judge or justice may appoint a person to manage the property and require its possessor to give possession` |
| s 490.81(2) | the Attorney General of Canada: claim that the Minister of Public Works and Government Services be appointed | the judge or justice: duty | `s 490.81(2) the judge or justice shall appoint the Minister of Public Works and Government Services`; `s 490.81(2) the duty of a judge` |
| s 490.81(3) | none (what the power to manage includes) | none | `s 490.81(3) the power to manage or otherwise deal with property includes the power` |
| s 490.81(4) | the court: claim that the manager apply before destroying property | the person appointed: duty | `s 490.81(4) the person appointed to manage property shall apply to a court for a destruction order`; `s 490.81(4) the duty of a person appointed to manage property` |
| s 490.81(5) | a person with a valid interest: claim to notice and privilege to be heard | the court: duty | `s 490.81(5) the court shall require notice to be given`; `s 490.81(5) the duty of the court` |
| s 490.81(6) | a person with a valid interest: claim to notice of the stated content | the court: duty | `s 490.81(6) the notice is as the subsection requires` |
| s 490.81(7) | the manager: claim to a destruction order | the court: duty | `s 490.81(7) the court shall order that the property be destroyed`; `s 490.81(7) the duty of the court` |
| s 490.81(7.1) | the manager: claim to a forfeiture order | the court: duty | `s 490.81(7.1) the court shall order the property forfeited to Her Majesty`; `s 490.81(7.1) the duty of the court to order the forfeiture` |
| s 490.81(8) | none (when a management order ceases) | none | `s 490.81(8) the management order ceases to have effect` |
| s 490.81(8.1) | none (the order applies to the net proceeds) | none | `s 490.81(8.1) the management order applies to the net proceeds of the sale` |
| s 490.81(9) | the Attorney General: power to apply to cancel or vary a condition (not an appointment) | the judge or justice: liability | `s 490.81(9) the Attorney General may apply to the judge or justice` |
| s 490.9(1) | none (sections 489.1 and 490 apply) | none | `s 490.9(1) sections 489.1 and 490 apply to the property` |
| s 490.9(2) | the judge or justice: power to require a recognizance or a deposit | the applicant for the return: liability | `s 490.9(2) (recognizance) the judge or justice may require the applicant to enter into a recognizance`; `s 490.9(2) (deposit) the judge or justice may require the applicant to deposit a sum of money or other valuable security` |
| s 491(1) | Her Majesty: claim to forfeiture of a seized thing | the person from whom it was seized: liability; the Attorney General: power to direct disposal | `s 491(1) the thing is forfeited to Her Majesty` |
| s 491(2) | the lawful owner who was not a party: claim to return, the proceeds or the value | the court: duty | `s 491(2) the order the court shall make`; `s 491(2) the duty of the court to order the return or payment` |
| s 491(3) | the Attorney General or the lawful owner: claim to the proceeds of sale | the seller: duty | `s 491(3) the person to whom the proceeds of the sale shall be paid` |
| s 491.1(1) | none (the circumstances; section 490 does not apply) | the court: duty to make an order under (2) | `s 491.1(1) the court shall make an order under subsection (2) in respect of the property`; `s 491.1(1) the duty of the court to make an order in respect of the property` (+1) |
| s 491.1(2) | the lawful owner: claim to return; Her Majesty: claim to forfeiture where the owner is not known | the court: duty | `s 491.1(2) the order the court shall make` |
| s 491.1(3) | the persons listed: immunity from an order | the court: disability | `s 491.1(3) an order shall not be made under subsection (2)` |
| s 491.1(4) | the court: power to direct execution | peace officers: duty | `s 491.1(4) the peace officers shall execute the order`; `s 491.1(4) the duty of a peace officer` |
| s 491.2(1) | a peace officer or person under their direction: privilege to take and retain a photograph | the owner of the property: no-right | `s 491.2(1) the person may take and retain a photograph of the property` |
| s 491.2(2) | the prosecution: claim that a certified photograph is admissible and has the property's probative force | the accused: no-right | `s 491.2(2) the photograph is admissible in evidence`; `s 491.2(2) the photograph has the same probative force as the property would have had if it had been proved in the ordinary way` |
| s 491.2(3) | the prosecution: claim that the certificate is admissible | the accused: no-right | `s 491.2(3) the certificate is admissible in evidence`; `s 491.2(3) the certificate is evidence of the statements contained in it without proof of the signature of the person appearing to have signed it` |
| s 491.2(4) | the prosecution: claim that the affidavit or declaration is admissible | the accused: no-right | `s 491.2(4) the affidavit or solemn declaration is admissible in evidence`; `s 491.2(4) the affidavit or solemn declaration is evidence of the statements contained in it without proof of the signature or official character` |
| s 491.2(5) | the accused: immunity (no receipt in evidence without a copy and reasonable notice) | the prosecutor: disability | `s 491.2(5) the photograph, certificate, affidavit or solemn declaration shall not be received in evidence` |
| s 491.2(6) | the court: power to require the signer to appear for examination | the signer: liability | `s 491.2(6) the court may require the person who appears to have signed to appear for examination or cross-examination` |
| s 491.2(7) | the court: power to order the property produced | the party holding it: liability | `s 491.2(7) the court may order the property to be produced in court or made available for examination` |
| s 491.2(8) | none (a definition of photograph) | none | `s 491.2(8) photograph` |
| s 492(1) | the person executing a warrant: power to seize an explosive substance; the judge of a superior court: power to order delivery | the owner or possessor: liability | `s 492(1) the person may seize the thing`; `s 492(1) the duty of the person who executes the warrant to remove and detain what they seize` (+1) |
| s 492(2) | Her Majesty: claim to the forfeited thing | the convicted accused: liability | `s 492(2) the thing is forfeited and shall be dealt with as the court directs` |
| s 492(3) | the Attorney General: claim to the proceeds of sale | the seller: duty | `s 492(3) the proceeds of the sale shall be paid to the Attorney General` |
| s 492.1(1) | a justice or judge: power to issue a tracking warrant (suspicion) | the person tracked: liability | `s 492.1(1) the justice or judge may issue a warrant for a tracking device`; `s 492.1(1) the power of the justice or judge to issue the warrant` |
| s 492.1(2) | a justice or judge: power to issue a tracking warrant for an individual (belief) | the person tracked: liability | `s 492.1(2) the justice or judge may issue a warrant for a tracking device, for an individual`; `s 492.1(2) the power of the justice or judge to issue the warrant` |
| s 492.1(3) | a peace officer or public officer: privilege to install, use and remove the device, covertly | the person tracked: no-right | `s 492.1(3) the warrant authorizes the act` |
| s 492.1(4) | the justice or judge: power to attach conditions, including to protect a person's interests | the person tracked: liability; the officer: liability | `s 492.1(4) the warrant may contain the condition` |
| s 492.1(5) | none (a counting rule: validity up to 60 days) | none | `s 492.1(5) the day a number of days after the day`; `s 492.1(6) one year after the day` (+1) |
| s 492.1(6) | none (a counting rule: validity up to one year for the listed offences) | none | `s 492.1(6) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.1(6.1) | a peace officer or public officer: privilege to execute anywhere in Canada, with authority there | the person tracked: no-right | `s 492.1(6.1) (place) the warrant may be executed at the place`; `s 492.1(6.1) (officer) the officer who executes the warrant has the authority the subsection requires` |
| s 492.1(7) | the justice or judge: power to authorize covert removal after expiry (up to 90 days) | the person tracked: liability | `s 492.1(7) the justice or judge may authorize the covert removal of the tracking device after the expiry of the warrant`; `s 492.1(7) the authorization is valid for the period specified in it` |
| s 492.1(8) | none (definitions: data, judge, public officer, tracking data, tracking device) | none | `s 492.1(8) "data" data`; `s 492.1(8) "judge"` (+3) |
| s 492.2(1) | a justice or judge: power to issue a transmission data recorder warrant | the person whose communications are recorded: liability | `s 492.2(1) the justice or judge may issue a warrant for a transmission data recorder`; `s 492.2(1) the power of the justice or judge to issue the warrant` |
| s 492.2(2) | a peace officer or public officer: privilege to install, use and remove the recorder, covertly | the person: no-right | `s 492.2(2) the warrant authorizes the act` |
| s 492.2(3) | the person: immunity (no warrant for the purpose of obtaining tracking data) | the justice or judge: disability | `s 492.2(3) no warrant shall be issued under this section` |
| s 492.2(4) | none (a counting rule: validity up to 60 days) | none | `s 492.2(4) the warrant is valid for the period specified in it` |
| s 492.2(5) | none (a counting rule: validity up to one year for the listed offences) | none | `s 492.2(5) the warrant is valid for the period specified in it, for organized crime and terrorism offences` |
| s 492.2(5.1) | a peace officer or public officer: privilege to execute anywhere in Canada, with authority there | the person: no-right | `s 492.2(5.1) (place) the warrant may be executed at the place`; `s 492.2(5.1) (officer) the officer who executes the warrant has the authority the subsection requires` |
| s 492.2(6) | none (definitions: data, judge, public officer, transmission data, transmission data recorder) | none | `s 492.2(6) "data" data`; `s 492.2(6) "judge"` (+3) |
| s 490.032 | none (machinery: the Governor in Council's power to make regulations about the content of Form 53 and Form 54) | none | n/a |
| s 490.03(4) | none (repealed) | none | n/a |

## Marginal readings for a lawyer (ccc18)

Every branch of layer 1 that rests on one of the two readings the brief leaves to a lawyer, with the other reading.
(a): a failed "if", "where" or "when" counts as the text's no, clause by clause, within the provision that holds it, and a flat negative counts as the text saying no. (b): a prohibition or grant limited by its own wording does not.
Generated from the branch tags of the modules (`[marginal (a)]`, `[may-where]`, `NOTHING-kind (limited by its own wording)`), cross-checked against the sweep: 211 branches in 189 functions (66 tagged (a), 145 (b); the 6 `[may-where]` branches of the ten listed functions are in F18, not here).

- Reading (a), JUST FALSE taken (tag `[marginal (a)]`).
  Other reading: NOTHING ("if A then B" does not itself say "if not A then not B").
- Reading (b), NOTHING taken (the text limits a grant or a prohibition in its own wording and the case is outside the limit).
  Other reading: JUST FALSE.
  For a function named for a power whose gate is an "if" or a named complement this is fork F5, by the brief's ruling of 2026-11-12 (1).
- `[may-where]`, JUST FALSE taken (a "may" function whose gate is of the where/when/upon kind: ruling (b) of the periods ruling).
  Other reading: NOTHING, the guide's line on grants (fork F18; class W of the sweep).
  The four class-WM functions are in reading (b) with NOTHING, and name the same other reading.

| function | module:line | rests on | answer taken | other reading |
| --- | --- | --- | --- | --- |
| `s 490.02(2) a notice shall not be served on the person` | soira-notice:61 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.021(2) the notice may be served by registered mail at the person's last known address` | soira-notice:131 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.021(3) the notice may be served by registered mail at the person's last known address, the person not being in compliance with the Ontario Act` | soira-notice:143 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.021(4) the notice may be served by registered mail at the person's last known address, the person having failed to comply` | soira-notice:155 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.021(5) the affidavit is evidence of the service and the notice` | soira-notice:212 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.021(6) the person who served the notice must send a copy of the affidavit and the notice` | soira-notice:229 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.022(2) the earliest day on which the obligation ends` | soira-notice:273 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.023(1) the person may apply for an exemption order` | soira-notice:366 | (b) x1 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.023(1.1) the application shall be made to a court of criminal jurisdiction` | soira-notice:384 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.023(2) the court shall make an exemption order` | soira-notice:398 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.023(3) the court shall give reasons for its decision` | soira-notice:418 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.023(4) the court shall also make an order for removal of the information from the database` | soira-notice:438 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.024(1) the appeal may be brought` | soira-notice:465 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.024(1) the appeal court may do it` | soira-notice:482 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.024(2) the appeal court shall also make an order for removal of the information from the database` | soira-notice:498 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.025 the court shall cause the notification and the information to be given` | soira-notice:519 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.026(1) the person may apply for a termination order` | soira-notice:553 | (b) x1 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.026(2) the person may apply for a termination order, the period since sentence having elapsed` | soira-notice:572 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.026(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` | soira-notice:592 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.026(6) the application shall be made to a court of criminal jurisdiction` | soira-notice:638 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.027(1) the court shall make an order terminating the obligation` | soira-notice:657 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.027(1.1) the court shall consider the factor` | soira-notice:696 | (a) x1, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.027(2) the court shall give reasons for its decision` | soira-notice:717 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.027(3) the court shall cause the notification to be given` | soira-notice:737 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.028 an application for one order is deemed to be an application for both` | soira-notice:757 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.029(1) the appeal may be brought` | soira-notice:778 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.029(1) the appeal court may do it` | soira-notice:795 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.029(2) the appeal court shall cause the notification to be given` | soira-notice:811 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02901 the person shall comply with the Sex Offender Information Registration Act` | soira-foreign:25 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02902(2) a notice shall not be served on the person` | soira-foreign:63 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02903(2) the affidavit is evidence of the service and the notice` | soira-foreign:99 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02903(3) the person who served the notice must send a copy of the affidavit and the notice` | soira-foreign:116 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02904(2) the day on which the obligation ends` | soira-foreign:142 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02905(1) the person may apply for an exemption order` | soira-foreign:179 | (b) x2 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.02905(2) the court shall make an exemption order` | soira-foreign:202 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02905(2.1) the court shall consider the factor` | soira-foreign:243 | (a) x1, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.02905(2.2) the court shall order that the notice be corrected` | soira-foreign:264 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02905(3) the court shall give reasons for its decision` | soira-foreign:284 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02905(4) the court shall also make an order for removal of the information from the database` | soira-foreign:304 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02905(5) the court shall cause the notification to be given` | soira-foreign:324 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.029051(1) the person may apply for a variation order` | soira-foreign:350 | (b) x2 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.029051(2) the court shall make the variation order` | soira-foreign:369 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.029051(3) the duration of the obligation set out in the variation order` | soira-foreign:389 | (b) x2 | NOTHING | JUST FALSE |
| `s 490.029051(4) the court shall give reasons for its decision` | soira-foreign:417 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.029051(5) the court shall cause the notification to be given` | soira-foreign:437 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02906(1) the appeal may be brought` | soira-foreign:466 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02906(1) the appeal court may do it` | soira-foreign:486 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02906(2) the appeal court shall also make an order for removal of the information from the database` | soira-foreign:503 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02907(1) the appeal court shall cause the notification and the information to be given` | soira-foreign:522 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02907(2) the appeal court shall cause the notification to be given` | soira-foreign:555 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02908(1) the person may apply for a termination order` | soira-foreign:576 | (b) x1 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.02908(2) the person may apply for a termination order, the period since sentence having elapsed` | soira-foreign:593 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02908(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` | soira-foreign:612 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02908(4) the person may apply again for a termination order` | soira-foreign:625 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02909(1) the court shall make an order terminating the obligation` | soira-foreign:643 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02909(1.1) the court shall consider the factor` | soira-foreign:682 | (a) x1, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.02909(2) the court shall give reasons for its decision` | soira-foreign:703 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02909(3) the court shall cause the notification to be given` | soira-foreign:723 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.0291(1) the appeal may be brought` | soira-foreign:750 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.0291(1) the appeal court may do it` | soira-foreign:767 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.0291(2) the appeal court shall cause the notification to be given` | soira-foreign:783 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02911(1) the person must advise a police service` | soira-foreign:810 | (a) x1, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.02911(2) the person must advise a police service of a change in address` | soira-foreign:881 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02911(3) the police service shall cause the Attorney General or minister of justice to be provided with the information` | soira-foreign:916 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02911(4) the day on which the obligation under subsection (2) ends` | soira-foreign:934 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.029111(1) the person may apply for an exemption order` | soira-itoa:25 | (b) x2 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.029111(2) the court shall make an exemption order` | soira-itoa:45 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.029111(3) the court shall consider the factor` | soira-itoa:84 | (a) x1, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.029111(4) the court shall give reasons for its decision` | soira-itoa:105 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.029111(5) the court shall also make an order for removal of the information from the database` | soira-itoa:125 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.029112(1) the person may apply for a variation order` | soira-itoa:151 | (b) x2 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.029112(2) the court shall make the variation order` | soira-itoa:171 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.029112(3) the duration of the obligation set out in the variation order` | soira-itoa:190 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.029112(4) the court shall give reasons for its decision` | soira-itoa:214 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.029112(5) the court shall cause the notification to be given` | soira-itoa:234 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.029113(1) the appeal may be brought` | soira-itoa:263 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.029113(1) the appeal court may do it` | soira-itoa:283 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.029113(2) the appeal court shall also make an order for removal of the information from the database` | soira-itoa:300 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.029114(1) the appeal court shall cause the notification and the information to be given` | soira-itoa:319 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.029114(2) the appeal court shall cause the notification to be given` | soira-itoa:352 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02912(1) the person may apply for a termination order` | soira-itoa:373 | (b) x1 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.02912(2) the person may apply for a termination order, the period since sentence having elapsed` | soira-itoa:390 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02912(3) the person may apply for a termination order, 20 years having elapsed since the most recent offence` | soira-itoa:409 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02912(4) the person may apply again for a termination order` | soira-itoa:431 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02913(1) the court shall make an order terminating the obligation` | soira-itoa:449 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02913(1.1) the court shall consider the factor` | soira-itoa:488 | (a) x1, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.02913(2) the court shall give reasons for its decision` | soira-itoa:509 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02913(3) the court shall cause the notification to be given` | soira-itoa:529 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02914(1) the appeal may be brought` | soira-itoa:556 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02914(1) the appeal court may do it` | soira-itoa:573 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.02914(2) the appeal court shall cause the notification to be given` | soira-itoa:589 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.02915(1) the person in charge of the place must give the person a copy of the Form 1` | soira-itoa:609 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.02915(2) the Review Board must cause a copy of the Form 1 to be given to the person` | soira-itoa:644 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.03(1) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the registered information` | soira-offences:33 | (a) x2, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.03(2) the Commissioner or a person authorized by the Commissioner shall, on request, disclose the information to the prosecutor or Attorney General` | soira-offences:78 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.03(3) the prosecutor or the Attorney General may disclose the information to the presiding court` | soira-offences:99 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.031(1) the person is guilty of an offence` | soira-offences:114 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.031(2) a lawful command is a reasonable excuse` | soira-offences:148 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.031(3) the certificate is evidence of the statements contained in it without proof of the signature or official character` | soira-offences:160 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.031(4) the sex offender may require the attendance of the person who signed the certificate for cross-examination` | soira-offences:171 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.0311 the person is guilty of an offence` | soira-offences:195 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.0312 the person is guilty of an offence` | soira-offences:229 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.03121(1) the justice may issue a warrant in Form 6.4 to arrest the person` | soira-offences:255 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.03121(2) the warrant shall contain the condition` | soira-offences:274 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.03121(3) the warrant may be executed there` | soira-offences:294 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.03121(5) no charge shall be laid against the person in respect of the contravention` | soira-offences:316 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.04(1) the person may apply to a court for an exemption order` | soira-additional:24 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.04(2) the person is not permitted to apply under paragraph (1)(b)` | soira-additional:36 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.04(4) the court shall not make an exemption order` | soira-additional:73 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.04(5) the court shall make an exemption order` | soira-additional:92 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.04(6) the court shall consider the factor` | soira-additional:150 | (a) x1, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.04(7) the court shall give reasons for its decision` | soira-additional:171 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.04(8) the court shall also make an order for removal of the information from the database` | soira-additional:191 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.05(1) the person may apply to a court for a variation order` | soira-additional:222 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.05(2) the person is not permitted to apply under paragraph (1)(c) or (d)` | soira-additional:236 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.05(4) the court shall make the variation order` | soira-additional:267 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.05(5) the duration set out in the variation order` | soira-additional:301 | (b) x2 | NOTHING | JUST FALSE |
| `s 490.05(6) the court shall give reasons for its decision` | soira-additional:336 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.05(7) the court shall cause the notification to be given` | soira-additional:356 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.06(1) the appeal may be brought` | soira-additional:385 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.06(1) the appeal court may do it` | soira-additional:405 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.06(2) the appeal court shall also make an order for removal of the information from the database` | soira-additional:422 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.07(1) the appeal court shall cause the notification and the information to be given` | soira-additional:441 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.07(2) the appeal court shall cause the notification to be given` | soira-additional:474 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.1(1) the court shall order the property forfeited` | forfeiture:31 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.1(2) the court may make an order of forfeiture under subsection (1) of property not shown to be related to the offence` | forfeiture:74 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.1(2.1) an order may be issued in respect of property situated outside Canada` | forfeiture:84 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.1(3) the appeal may be brought` | forfeiture:102 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.2(1) the Attorney General may make an application to a judge for an order of forfeiture` | forfeiture:115 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.2(2) the judge shall order the property forfeited` | forfeiture:130 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.2(3) the day on which the accused is deemed to have absconded` | forfeiture:175 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.2(4.1) an order may be issued in respect of property situated outside Canada` | forfeiture:197 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.3 the court may set aside the conveyance or transfer` | forfeiture:223 | (b) x1 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.4(1) the court shall require notice to be given to the person` | forfeiture:240 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.4(1) (hearing) the court may hear the person` | forfeiture:257 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.4(3) the court may order that the property be returned to the person` | forfeiture:285 | (b) x1 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.41(1) the court shall require notice to be given to the person, and may hear them` | forfeiture:301 | (b) x2 (F5) | NOTHING | JUST FALSE |
| `s 490.41(3) (decision) the court may decide not to order the forfeiture of the property or part of the property` | forfeiture:340 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.41(3) (restraint order) the court may revoke a restraint order made in respect of the property or part of it` | forfeiture:350 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.41(4) the court shall also consider the matter` | forfeiture:370 | (a) x2, (b) x1 | JUST FALSE / NOTHING | NOTHING / JUST FALSE |
| `s 490.5(1) the person may apply for an order under subsection (4)` | forfeiture:405 | (b) x1 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.5(5) the appeal may be brought` | forfeiture:491 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.5(6) the Attorney General shall direct that the property be returned or the amount paid` | forfeiture:508 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.6 the person may appeal from the order` | forfeiture:528 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.7 the operation of the order is suspended` | forfeiture:542 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.8(1) the Attorney General may apply for a restraint order` | forfeiture:563 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.8(3) the judge may make a restraint order` | forfeiture:589 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.8(3.1) a restraint order may be issued in respect of property situated outside Canada` | forfeiture:599 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.8(4) the restraint order may be subject to the condition` | forfeiture:610 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 490.8(9) the person is guilty of an offence` | forfeiture:668 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.81(2) the judge or justice shall appoint the Minister of Public Works and Government Services` | forfeiture:744 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.81(4) the person appointed to manage property shall apply to a court for a destruction order` | forfeiture:787 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.81(5) the court shall require notice to be given` | forfeiture:807 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.81(7) the court shall order that the property be destroyed` | forfeiture:840 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.81(7.1) the court shall order the property forfeited to Her Majesty` | forfeiture:868 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.81(8) the management order ceases to have effect` | forfeiture:888 | (a) x1 | JUST FALSE | NOTHING |
| `s 490.81(8.1) the management order applies to the net proceeds of the sale` | forfeiture:898 | (b) x1 | NOTHING | JUST FALSE |
| `s 490.81(9) the Attorney General may apply to the judge or justice` | forfeiture:909 | (b) x1 (F5, one limb) | NOTHING | JUST FALSE |
| `s 490.9(1) sections 489.1 and 490 apply to the property` | forfeiture:923 | (b) x1 | NOTHING | JUST FALSE |
| `s 491(1) the thing is forfeited to Her Majesty` | weapons-evidence:39 | (a) x2 | JUST FALSE | NOTHING |
| `s 491(2) the order the court shall make` | weapons-evidence:68 | (a) x1 | JUST FALSE | NOTHING |
| `s 491(3) the person to whom the proceeds of the sale shall be paid` | weapons-evidence:98 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.1(1) the court shall make an order under subsection (2) in respect of the property` | weapons-evidence:122 | (a) x1 | JUST FALSE | NOTHING |
| `s 491.1(1) (section 490) section 490 does not apply in respect of the property` | weapons-evidence:147 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.1(2) the order the court shall make` | weapons-evidence:165 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.1(3) an order shall not be made under subsection (2)` | weapons-evidence:188 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.1(4) the peace officers shall execute the order` | weapons-evidence:207 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.2(2) the photograph is admissible in evidence` | weapons-evidence:246 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.2(2) the photograph has the same probative force as the property would have had if it had been proved in the ordinary way` | weapons-evidence:257 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.2(3) the certificate is admissible in evidence` | weapons-evidence:275 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.2(3) the certificate is evidence of the statements contained in it without proof of the signature of the person appearing to have signed it` | weapons-evidence:290 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.2(4) the affidavit or solemn declaration is admissible in evidence` | weapons-evidence:304 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.2(4) the affidavit or solemn declaration is evidence of the statements contained in it without proof of the signature or official character` | weapons-evidence:315 | (b) x1 | NOTHING | JUST FALSE |
| `s 491.2(6) the court may require the person who appears to have signed to appear for examination or cross-examination` | weapons-evidence:342 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 492(1) the person may seize the thing` | weapons-evidence:395 | (b) x2 (F5) | NOTHING | JUST FALSE |
| `s 492(1) the thing shall be detained` | weapons-evidence:420 | (b) x1 | NOTHING | JUST FALSE |
| `s 492(2) the thing is forfeited and shall be dealt with as the court directs` | weapons-evidence:432 | (a) x1 | JUST FALSE | NOTHING |
| `s 492(3) the proceeds of the sale shall be paid to the Attorney General` | weapons-evidence:442 | (a) x1 | JUST FALSE | NOTHING |
| `s 492.1(1) the justice or judge may issue a warrant for a tracking device` | tracking:39 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 492.1(2) the justice or judge may issue a warrant for a tracking device, for an individual` | tracking:62 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 492.1(3) the warrant authorizes the act` | tracking:91 | (b) x2 (F5) | NOTHING | JUST FALSE |
| `s 492.1(4) the warrant may contain the condition` | tracking:103 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 492.1(6) the warrant is valid for the period specified in it, for organized crime and terrorism offences` | tracking:131 | (b) x1 | NOTHING | JUST FALSE |
| `s 492.1(6.1) (place) the warrant may be executed at the place` | tracking:146 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 492.2(1) the justice or judge may issue a warrant for a transmission data recorder` | tracking:259 | (b) x1 (F5) | NOTHING | JUST FALSE |
| `s 492.2(2) the warrant authorizes the act` | tracking:287 | (b) x2 (F5) | NOTHING | JUST FALSE |
| `s 492.2(3) no warrant shall be issued under this section` | tracking:299 | (b) x1 | NOTHING | JUST FALSE |
| `s 492.2(5) the warrant is valid for the period specified in it, for organized crime and terrorism offences` | tracking:327 | (b) x1 | NOTHING | JUST FALSE |
| `s 492.2(5.1) (place) the warrant may be executed at the place` | tracking:342 | (b) x1 (F5) | NOTHING | JUST FALSE |

### Reading a result: FALSE and NOTHING (ccc18)

Every decision function here answers a MAYBE BOOLEAN (a few answer a MAYBE of a type, a date, or a total type that has its own "the text says no" constructor), and so does every seat question.
- `JUST TRUE`: on the facts given the text says yes: the power is open to the person, the duty arises, the bar applies, the offence is made out.
- `JUST FALSE`, a "no": the text says no in its own words.
  In this range that means: a gate the text closes ("only if", "unless", "until", "as long as"); a flat negative ("shall not", "may not", "is not to be received"); a period fixed in words that the facts miss ("within one year after", "within thirty days after", "not less than thirty days", "at least fifteen days before"); a definition that says "means" and the case is outside it; and a duty or a flat statement whose "if", "where" or "when" fails (marginal reading (a)).
  Every such branch carries `-- FALSE-kind (the text says no in its own words): "<the words>"`, and `work/lint.py` checks that each quoted passage occurs in the text.
- `NOTHING`, "not covered": the text grants a power "if" a gate holds and the gate fails (F5); an offence's element is unmet (F15); a bar is not engaged; the provision is limited to a case the facts are outside ("A person who is subject to an obligation ... may apply"; "the following acts"); a list that "includes" is not closed; a term is defined in another part or Act and its answer is an input that came back NOTHING; or the text is silent.
  Every such branch carries `-- NOTHING-kind (<why>)`.
- A caller must never turn `NOTHING` into `FALSE`.
  In particular a person told NOTHING about a power to apply has not been told they may not apply; and a person who answers NOTHING on "am I guilty of an offence" has been told that the section does not say so, not that they are innocent.
- A bar answers `JUST TRUE` when it applies and `JUST FALSE` where the text lifts it in its own words ("unless the prosecutor has ... given a copy"); where the bar is limited to named cases and the facts are outside them it answers NOTHING.
- A function named for a power ("may") whose gate is of the where/when/upon kind answers `JUST FALSE` where the gate fails, carries `[may-where]`, and is listed in F18 with the other reading, NOTHING; where the gate is an "if" or a named complement it answers `NOTHING` (F5).
- `REFUSE` does not exist on the stable binary: "not covered" is `NOTHING` or a constructor, asserted.

## Seams (ccc18)

A seam is an answer another part (or the keel) computes, taken as a MAYBE BOOLEAN input named for what is asked (PLAN.md rule R4); `NOTHING` from the other part flows through and is never turned into `FALSE`.
The row of this part in PLAN.md section 6 names one seam; the table gives every one the modules take, and marks those the plan lacks (found while writing: the plan's row lists `490.012` only).

| input | modules | in PLAN.md's row for ccc18 |
| --- | --- | --- |
| `the person was convicted of, or found not criminally responsible on account of mental disorder for, an offence referred to in paragraph (a), (c), (c.1), (d) or (e) of the definition designated offence in subsection 490.011(1), by s 490.011(1) designated offence` | soira-notice | no: a seam the plan lacks |
| `s 490.012 an order to comply with the Sex Offender Information Registration Act is in force` | soira-notice | yes (ccc17: ss 490.011, 490.012, 490.019) |
| `s 490.019 the person is subject to an obligation to comply with the Sex Offender Information Registration Act` | soira-notice | no: a seam the plan lacks |
| `s 2 offence-related property: the property is offence-related property` | forfeiture | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `the person is a judge as defined in section 552, by s 552 judge` | forfeiture | no: a seam the plan lacks |
| `s 2 dwelling-house: all or part of the offence-related property is a dwelling-house` | forfeiture | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2 dwelling-house: all or part of the property that would otherwise be forfeited is a dwelling-house` | forfeiture | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2 weapon: the thing is a weapon` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2.1 imitation firearm: the thing is a imitation firearm` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2.1 prohibited device: the thing is a prohibited device` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2.1 firearm part: the thing is a firearm part` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2.1 ammunition: the thing is a ammunition` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2.1 prohibited ammunition: the thing is a prohibited ammunition` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2 explosive substance: the thing is a explosive substance` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2 firearm: the thing is a firearm` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2.1 cross-bow: the thing is a cross-bow` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2.1 prohibited weapon: the thing is a prohibited weapon` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2.1 restricted weapon: the thing is a restricted weapon` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `s 2 explosive substance: the thing is an explosive substance` | weapons-evidence | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `(c) the warrant relates to a terrorism offence, by s 2 terrorism offence` | tracking | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `the person is a judge of a superior court of criminal jurisdiction, by s 2 superior court of criminal jurisdiction` | tracking | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `the person is a public officer, by s 2 public officer` | tracking | a section 2 or 2.1 term: PLAN.md section 4 names it |
| `it is a computer program within the meaning of subsection 342.1(2), by s 342.1(2) computer program` | tracking | no: a seam the plan lacks |

Answers borrowed from other Acts or from provisions outside this range, asked as plain inputs because the text of this range does not decide them (Findings 3 and 4): the table lists the inputs whose names carry such a borrowing.

| input | type | modules |
| --- | --- | --- |
| `(b)(i) their name appears in connection with the offence, immediately before the Sex Offender Information Registration Act comes into force, in the sex offender regist...` | BOOLEAN | soira-notice |
| `(a) they have been finally acquitted of, or have received a free pardon granted under Her Majesty’s royal prerogative of mercy or under section 748 for, every offence ...` | BOOLEAN | soira-notice |
| `(b) an application has been made for an order under subsection 490.012(3) of this Act or subsection 227.01(3) of the National Defence Act in relation to any offence in...` | BOOLEAN | soira-notice |
| `(c) they are referred to in paragraph (1)(b) and they have provided proof of a pardon in accordance with subsection 9(1) of the Ontario Act` | BOOLEAN | soira-notice |
| `the person is in breach of any terms of their sentence or discharge, or of any conditions set under this Act or under Part III of the National Defence Act, that relate...` | BOOLEAN | soira-notice |
| `the person is not in compliance with section 3 of the Ontario Act on the day on which the Sex Offender Information Registration Act comes into force` | BOOLEAN | soira-notice |
| `the person is in compliance with section 3 and subsection 7(2) of the Ontario Act on the day on which the Sex Offender Information Registration Act comes into force` | BOOLEAN | soira-notice |
| `the person fails to comply with subsection 3(1) or 7(2) of the Ontario Act within one year after that day` | BOOLEAN | soira-notice |
| `(d) at any time the person was convicted of, or found not criminally responsible on account of mental disorder for, more than one offence referred to in paragraph (a),...` | BOOLEAN | soira-notice |
| `the day on which they were served with a notice under section 490.021 of this Act or section 227.08 of the National Defence Act` | DATE | soira-notice |
| `(b) the application relates to an obligation under section 227.06 of the National Defence Act` | BOOLEAN | soira-notice |
| `(b) the Chief Military Judge does not have jurisdiction to receive the application under subsection 227.1(2) of that Act` | BOOLEAN | soira-notice |
| `they are also subject to an obligation under section 490.02901, under section 227.06 of the National Defence Act or under section 36.1 of the International Transfer of...` | BOOLEAN | soira-notice |
| `after the previous application was made, they become subject to an obligation under section 490.02901, under section 227.06 of the National Defence Act or under sectio...` | BOOLEAN | soira-notice |
| `(b) the Chief Military Judge does not have jurisdiction to receive the application under subsection 227.12(6) of that Act` | BOOLEAN | soira-notice |
| `a person is eligible to apply for both an exemption order under section 490.023 and a termination order under section 490.026 within one year after they are served wit...` | BOOLEAN | soira-notice |
| `the offence is a service offence as defined in subsection 2(1) of the National Defence Act` | BOOLEAN | soira-foreign |
| `they are also subject to another obligation under section 490.02901, or to an obligation under section 490.019, under section 227.06 of the National Defence Act or und...` | BOOLEAN | soira-foreign |
| `they are subject to an obligation under section 36.1 of the International Transfer of Offenders Act` | BOOLEAN | soira-itoa |
| `(a) the obligation applies for life under subsection 36.2(3) of that Act` | BOOLEAN | soira-itoa |
| `they are also subject to an obligation under section 490.019 or 490.02901 or under section 227.06 of the National Defence Act, or to an order under section 490.012 or ...` | BOOLEAN | soira-itoa |
| `more than one offence is listed in the copy of the Form 1 that was delivered under subparagraph 8(4)(a)(ii) of the International Transfer of Offenders Act` | BOOLEAN | soira-itoa |
| `the person fails to comply with an order made under section 490.012 or under section 227.01 of the National Defence Act or with an obligation under section 490.019 or ...` | BOOLEAN | soira-offences |
| `at the time, the person is subject to the Code of Service Discipline within the meaning of subsection 2(1) of the National Defence Act` | BOOLEAN | soira-offences |
| `(b) the person is subject to an obligation under section 490.02901, or under section 36.1 of the International Transfer of Offenders Act, that began before the day on ...` | BOOLEAN | soira-additional |
| `(b)(i) before or after the order under section 490.012 was made, the person was convicted of a primary offence, or of an offence under section 130 of the National Defe...` | BOOLEAN | soira-additional |
| `(a) the person is subject to an order made under section 490.012 that applies for life under subsection 490.013(2.1), as it read from time to time before the day on wh...` | BOOLEAN | soira-additional |
| `(d) the person is subject to an obligation under section 36.1 of the International Transfer of Offenders Act that applies for life under subsection 36.2(3) of that Act` | BOOLEAN | soira-additional |
| `the property is a controlled substance within the meaning of the Controlled Drugs and Substances Act or cannabis as defined in subsection 2(1) of the Cannabis Act` | BOOLEAN | forfeiture |

## Findings: what the text turns out to say (ccc18)

1. **Four parallel registration regimes.**
   The Sex Offender Information Registration Act obligation is created four ways in this range, each with its own application, order, appeal and notice sections: a Form 53 notice for earlier convictions (490.02 to 490.029), a Form 54 notice for convictions outside Canada (490.02901 to 490.02911), persons transferred to Canada (490.029111 to 490.02915), and "additional orders" for orders and obligations that began before the amendments (490.04 to 490.07).
   The duration tables (two or five years: 10; 10 or 14: 20; life) and the waiting-period tables (five, 10, 20 years) recur in 490.022(3), 490.02904(3), 490.026(2), 490.02908(2), 490.02912(2); each is encoded where the text states it, over a shared band type declared in `ccc18-soira-notice`.
2. **The factors list is the same seven items six times** (490.027(1.1), 490.02905(2.1), 490.02909(1.1), 490.029111(3), 490.02913(1.1), 490.04(6)); only 490.04(6)(a) differs ("of the order or obligation"), and 490.02905(2.1) applies only to a decision under paragraph (2)(c) or (d).
   Encoded as a table with a gate, tested for each item.
3. **Borrowed durations.**
   490.029112(3) and 490.05(5)(a) and (d) fix the duration of a variation order by applying provisions of another Act (paragraphs 36.2(2)(a) and (b) of the International Transfer of Offenders Act) or of a section outside this range (490.013(2)); their answers are inputs.
4. **Days the text leaves to commencement.**
   490.021(1) turns on the day the Sex Offender Information Registration Act comes into force, and 490.04(1), 490.04(2) and 490.05(1) on "the day on which this paragraph [or subsection] comes into force"; the text states none of them, so each is asked as a fact (a date for 490.021(1); whether the order or obligation began before that day for the others).
   490.02902(1) states its date (15 April 2011) and the code uses it.
5. **Two penalty paragraphs state no penalty.**
   490.0312 ("an offence punishable on summary conviction") and 490.8(9)(b); the core's `no imprisonment is stated` and `no fine is stated` are used (F14).
6. **The two lists in section 491(1) differ.**
   Limb (a) (used in the commission of an offence) lists a weapon, an imitation firearm, a prohibited device, a firearm part, ammunition, prohibited ammunition and an explosive substance; limb (b) (an offence that involves the thing) lists a firearm, a cross-bow, a prohibited weapon, a restricted weapon, a prohibited device, a firearm part, ammunition, prohibited ammunition and an explosive substance.
   A weapon used in an offence is forfeited under (a); a weapon merely involved is not under (b); the tests assert both sides (and one assertion first written with the wrong list failed and led to a fix of the code, not of the expectation).
7. **A subject-to chain.**
   490.1(1) and 490.2(2) are "subject to sections 490.3 to 490.41", and 490.41(3) is "subject to an order made under subsection 490.4(3)"; encoded as composites that answer JUST FALSE when the later order is made (F10).
8. **"Her Majesty" and "Queen's Privy Council" remain in a text current to 2026-09-30.**
   The constructor names say "Her Majesty" as the text does; the French equivalents in parentheses after the defined terms of 492.1(8) and 492.2(6) are quoted inside the quote lines and not encoded.
9. **Two repealed subsections** are shown as `[Repealed]` (490.03(4) and 490.1(1.1)); and 490.032 (regulations) is machinery.
10. **Passive duties name no bearer.**
    490.021(1) (served within one year), 490.8(5) to (7) (writing, service, registration of a restraint order), 491(3) and 492(3) (proceeds paid to the Attorney General), 490.81(6): encoded as decision functions only, with no regulative rule, because no actor is named (the brief: never invent an actor).
11. **A deliberate bug found and fixed in the generator.**
    `NOT a OR b` parses as `NOT (a OR b)` on the stable binary: the first generated appeal function mis-read it (assertion failure); fixed by parenthesising, as the brief's section 5 warns.

12. **A short route over a long rule.**
    492.1(5) and 492.2(4) are the 60-day periods of validity "subject to" subsections (6) and (5), which allow a year for organized crime and terrorism warrants; the seat questions that ask them (54, 58) now say which route they answer, so that a JUST FALSE is not read as "not valid" (Seat audit, above).
13. **Two "once" permissions.**
    490.026(4) and 490.02912(3.1) let a person apply "once" a pardon, a record suspension or an absolute discharge occurs; they are gated by an event, not by an "if", and the name-test sweep lists them with the where-kind functions (F18).

## What the stable binary does not accept, and traps met (ccc18)

- **A DEONTIC value cannot be compared in `#ASSERT`.**
  The 85 regulative rules are exercised with `#TRACE` (87 traces; the outcome is printed, never asserted): 85 end FULFILLED and 2 (the `WAITUNTIL 8` traces of 490.02911(1) and (2)) end `DEONTIC BREACHED`, each as its comment says; the two builds 1.6.110 and 1.6.109 print identical results for all 1163 evaluations of every tests module (1076 assertions and 87 trace outcomes), compared by `work/trace_cmp.py` with `JL4_LIBRARY_PATH` unset on both sides and after asserting that both runs produced evaluations, because `check.sh` does not see traces.
  So that every duty is also asserted, each is encoded a second time as a decision function over the facts that fix when the duty arises.
- Avoided, following `writing-l4-rules/references/dialects.md` (measured there on build 98 and not re-measured here): `AFTER`, `WITHIN ... OF THE DEADLINE`, `EVERY`, `REFUSE`, `BECAUSE` other than `LEST BREACH ... BECAUSE`, a `LEST` after `MAY`, a section `GIVEN`, `TYPICALLY`, sets, `BREACH BY LIST`, an input named in an action.
  The "at least fifteen days before" deadline of 490.5(3) is therefore a `WITHIN 15` from an assumed day 0 (F12).
  Only constructs that ran on both 1.6.110 and 1.6.109 are in the deposit.
- A record built with `OF` needs commas between its arguments (`Length of time OF 7, 0, 0, FALSE`); without them the stable binary reports `unexpected (`.
- `Date 0 7 2020` rolls back to 30 June 2020 (probed on 1.6.110); used for the last day of a six-month period (490.2(3)).

## What check.sh prints (ccc18)

Run on 2026-11-16 as `L4=<scratchpad>/bin/l4-main-110 L4_MAIN=<scratchpad>/bin/l4-main-109 ./check.sh` (1.6.110, sha256 9c7656f7...16c7; 1.6.109, sha256 eeb12f1e...73cb; both restored byte for byte), exit 0.
Before the resumed pass: `TOTAL (21 modules) 0 1247 0 0 | 0 1247 0 0`.
After: `TOTAL (21 modules) 0 1247 0 0 | 0 1247 0 0`.
(The assertion count is unchanged: the pass changed expectations in place and added none.)

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc18-cases-seat.l4                            0       171       0        0         0 |      0       171       0        0  same
ccc18-forfeiture.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc18-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-additional.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-foreign.l4                         0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-itoa.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-notice.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc18-soira-offences.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc18-tests-forfeiture.l4                      0       198       0        0         0 |      0       198       0        0  same
ccc18-tests-soira-additional.l4                0        87       0        0         0 |      0        87       0        0  same
ccc18-tests-soira-foreign.l4                   0       174       0        0         0 |      0       174       0        0  same
ccc18-tests-soira-itoa.l4                      0       119       0        0         0 |      0       119       0        0  same
ccc18-tests-soira-notice.l4                    0       190       0        0         0 |      0       190       0        0  same
ccc18-tests-soira-offences.l4                  0        69       0        0         0 |      0        69       0        0  same
ccc18-tests-tracking.l4                        0       119       0        0         0 |      0       119       0        0  same
ccc18-tests-weapons-evidence.l4                0       120       0        0         0 |      0       120       0        0  same
ccc18-tracking.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc18-weapons-evidence.l4                      0         0       0        0         0 |      0         0       0        0  same
TOTAL (21 modules)                             0      1247       0        0           |      0      1247       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)

```

Assertions per tests module: soira-notice 190; soira-foreign 174; soira-itoa 119; soira-offences 69; soira-additional 87; forfeiture 198; weapons-evidence 120; tracking 119; seat cases 171.
Other checks of the last run: `lint: 8 modules, 146 FALSE-kind answers, 175 NOTHING-kind answers, 66 marginal-(a) tags, 0 problems`; `srcrefs.py check --refs` and `--strict` over all 18 files `ccc18-*.l4` (including the seat files, which carry no quote lines): `srcrefs check: 753 src: lines, 249 runs, 486 locators, 0 problems`; the hygiene check `l4 check FILE | grep "end of the file|follows code"` finds nothing.

