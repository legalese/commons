# Contradiction hunt: Charities (Jersey) Law 2014, vintage from 2 October 2026

Blind hunt by the HUNTER, 2026-10-14.
Read: `inputs/charities-jersey-law-2014-2026-10-02.txt` (cited as `src:N`), the official PDF text layer (cited as `pdf:N`), the eight instruments in `inputs/amending/` (cited by instrument and text-layer line), `SOURCE-LICENSE.md`, and `BRIEF.md` for the cleanroom rules and vintage facts only.
No encoding, plan, survey or skill was opened.

Every quotation below was inserted by `work/hunt/render.py` from the source files, which fails if a quoted phrase does not occur verbatim on the cited line; nothing was retyped.
Contains States Assembly information licensed under the Open States Assembly Licence – Jersey v1.0.

**How to read a finding.**
Each one gives the provisions, the type (from the assignment's list), the words, why it is a problem, a minimal discriminating case on which the readings part company, a severity, and a confidence.
Severity is one of: **blocks a decision** (the Law gives no answer, or two commands that cannot both be obeyed), **changes an outcome** (two workable readings give different results), **cosmetic** (no case found where the result changes).
Confidence is in the *defect*, not in which reading a court would take; where a court would very likely take one reading, the finding says so.
Findings are ordered by severity, then by how much turns on them.
Facts that depend on an enactment outside the sources (Trusts (Jersey) Law 1984, Interpretation (Jersey) Law 1954, and so on) are marked as inputs.

## Summary table

| # | provisions | type | severity | confidence |
| --- | --- | --- | --- | --- |
| H1 | 11(4)-(5) v 19(9)(c), (e)(i) | contradiction | blocks a decision | high |
| H2 | 19(9)(e)(i) v 28(3), 27(4) | contradiction | blocks a decision | high |
| H3 | 11(4)-(5), 19(6), 11(8), 15(3), 33 | scope gap; power without a procedure | blocks a decision | high |
| H4 | 13(7)-(8), 8(3)(j), Art 1 "annual return" | temporal problem; duty without a time | blocks a decision | high |
| H5 | 9(2), 13(5), 13(6)(g) | scope gap; power without a procedure | blocks a decision | high |
| H6 | 19(9)(b), (d), (e), 19(10)-(11), 20(1)(a) | scope gap | blocks a decision | medium |
| H7 | 16(2), 17(2)(c) | power without a procedure | blocks a decision (narrow) | high |
| H8 | 19(11), 20(6), 21(9), 23(7), 26(10), 29(1); 21(10), 23(6), 26(7) | offence without a stated maximum | blocks a decision (of the maximum) | high |
| H9 | Art 1 "Minister" v 5(2)(a), (c) | definition problem | changes an outcome | high |
| H10 | 13(2)-(3) v 5(1)(a)(ii), 6(5) | contradiction | changes an outcome | medium-high |
| H11 | 17(3) v 17(5)-(9), 13(1) | temporal problem; scope gap | changes an outcome | medium-high |
| H12 | 19(1)(g) with 2(10)(b) | connective ambiguity | changes an outcome | high |
| H13 | 19(2), (3), (8), (10)-(11), (13) | duty without a sanction; sanction asymmetry | changes an outcome | high |
| H14 | 33(1)-(3) v 15(3)(b), 12(3)-(4), 19(9)(e)(ii), 9(2), 9(7) | scope gap (one item a connective ambiguity) | changes an outcome | high (one item medium) |
| H15 | 33(5) v 12(1) | scope gap; definition problem | changes an outcome | medium-high |
| H16 | 21(1)-(6), 23(1)-(2) v 2(1)(i) | scope gap | changes an outcome | high |
| H17 | 2(1)(a), (j), 2(3)(a), 21(3), 21(5), 22 | definition problem (covers twice) | changes an outcome | medium |
| H18 | 2(1)(ba) (R&O.56/2025) v ranges in 2(1)(j), 2(3)(a); 2(2), 39(1) | temporal problem; amendment does not fit the text | changes an outcome | medium |
| H19 | 2(5)(e) v 2(1)(g), (h); 8(4)(a); 2(10)(a)(ii) | definition problem (under-inclusive) | changes an outcome | medium-high |
| H20 | 26(1)-(2) v 27(3); 4(1)(c) | scope gap; function without a power | changes an outcome | high / medium |
| H21 | 26(10)-(11) | scope gap | changes an outcome | high |
| H22 | 29(1) | connective ambiguity | changes an outcome | high |
| H23 | 29, 31 v 4(3)(c) | contradiction / scope gap | changes an outcome | medium |
| H24 | 29(1) v 19(2)-(4), Sch 2 para 4(3)(g), 31 | scope gap (over-inclusive) | changes an outcome | medium |
| H25 | 17(2)(c), 17(4) v 16(1) | wrong cross-reference (ambiguous target) | changes an outcome | medium |
| H26 | Table of Legislation History v Table of Renumbered Provisions; R&O.17/2018 | temporal problem; renumbering | changes an outcome | high |
| H27 | 23(3)(c) | connective ambiguity | changes an outcome | medium-high |
| H28 | 22(2)(a)(i), 22(3)(a) | connective ambiguity | changes an outcome | medium |
| H29 | 10(4)-(5) v 8(5), 10(3)(c) | scope gap | changes an outcome | high |
| H30 | 8(5)(b) v 9(1)(a) | connective / temporal ambiguity | changes an outcome | medium |
| H31 | Art 1 "donation", "solicit"; 9(3); 14(3)(a)(ii); 24(1) | definition problem; temporal problem | changes an outcome | medium |
| H32 | 37 v 21(9)-(10), 23(6)-(7) and 2(1)(a), (b), (i) | scope gap (sanction without a bearer) | changes an outcome | medium |
| H33 | 8(6), 17(1)(a), 26(5), 20(5), 11(2)(e)(ii) | temporal problem | changes an outcome | high |
| H34 | 11(2)(e)(ii) v 13(9)(b) | definition problem | changes an outcome | medium |
| H35 | 12(6) v 13(6)(b) | scope gap | changes an outcome | medium |
| H36 | Sch 1 para 3(4)(b); Sch 2 para 2(4)(b) | scope gap | changes an outcome | high |
| H37 | 35(1) | used but undefined ("party") | changes an outcome | medium-low |
| H38 | 36(2), 33(5) | temporal problem; power without a default | changes an outcome | medium |
| H39 | Sch 1 para 3(1)(a), 3(4)(c), 4(5) | temporal problem | changes an outcome | medium |
| H40 | Art 1 "Minister" vintages; R&O.10/2024, R&O.40/2019 | temporal problem | changes an outcome (narrow) | high |
| H41 | 21(2)(b)(ii) v 21(4)(b)(ii), 21(6)(b)(ii), 23(2)(b)(ii) | inconsistency between parallel provisions | changes an outcome | medium |
| H42 | Sch 1 para 2(4)(a), 4(7) v L.1/2017 Art 20 | wrong cross-reference | changes an outcome | medium-low |
| H43 | 7(1) v 5(5) | scope gap | changes an outcome | medium |
| H44 | 14(1)(b) v 14(2) | connective ambiguity | changes an outcome | low |
| H45 | 8(4)(c) | definition problem (indeterminate) | changes an outcome | medium |
| H46 | 13(4)(b), 13(5)(b), 13(11)(b), 12(3)-(5) | power without a procedure | changes an outcome | medium |
| H47 | Sch 2 paras 1(1), 4(1)-(3); 34(3)(b) | scope gap | changes an outcome | low |
| H48 | 38 | power without a procedure | changes an outcome | low |
| H49 | 2(10)(b) v 22(1); commencement of Art 22 | cross-reference; temporal problem | cosmetic (probably) | high on text, low on effect |
| H50 | Art 1 "register" (verb) v "registered charity", "deregistration", 8(5) | definition problem | cosmetic | medium |
| H51 | R&O.40/2019 Sch 2 para 1(e) | amendment does not fit the text | cosmetic | high |
| H52 | Endnote [4] v Art 31(a), (b) | consolidated text v endnote | cosmetic | high |
| H53 | Sch 2 heading; Sch 1 para 4(12); endnote [3] marker | wrong name / reference | cosmetic | high |
| H54 | undefined terms: "historic section", "charity", "supervisory body", "resident", "Jersey charity", "the applicant" | used but undefined | cosmetic | high |
| H55 | 8(3)(a)(i)-(ii) v 2(1)(ba) | amendment does not fit the text | cosmetic | high |

---

## Blocks a decision

### H1. The Commissioner must register an applicant whose governor has been found unfit, and must not

**Provisions:** Art 11(4)-(5) (src:319-328); Art 19(9)(c) and (e)(i) (src:502, src:504-505); Art 11(7) (src:334).
**Type:** contradiction.

**Words:**
> src:319 | (4) If the applicant complies with paragraph (2), with any Regulations under paragraph (3), and with Article 19(5), the Commissioner must register the applicant as a charity if satisfied that –
>
> src:327 | (f) no other ground for refusal, prescribed under paragraph (7), applies or should be applied.
>
> src:328 | (5) If not so satisfied, the Commissioner must refuse to register the applicant.
>
> src:502 | (c) must not, in the case of an application for registration, grant that application until the issue has been determined and any resulting order or notice complied with;
>
> src:505 | (i) notify the entity that the application will be refused unless the governor is removed, or in the case of a registered charity serve a required steps notice requiring the charity to suspend or remove the governor, or
>

**Why it is a problem.**
Article 11(4) is mandatory ("must register") once the applicant complies with 11(2), (3) and 19(5) and the Commissioner is satisfied of (a)-(f).
An unfit governor is none of (a)-(e), and is (f) only if Regulations under 11(7) prescribe it; no such Regulations are in the sources.
Article 11(5) allows refusal only "If not so satisfied", that is, of 11(4)(a)-(f).
Article 19(9)(c) forbids granting until the governor issue is determined "and any resulting order or notice complied with", and 19(9)(e)(i) tells the Commissioner to notify that the application "will be refused unless the governor is removed", a refusal for which Article 11 supplies no ground.
So the same facts produce "must register" (11(4)), "must not grant" (19(9)(c)) and "will be refused" (19(9)(e)(i)).
If the Commissioner obeys 19(9)(c) by doing nothing, there is no "decision ... to refuse" for the applicant to appeal under 33(1)(a).

**Discriminating case.**
Applicant A, a Jersey company, meets the charity test, has a written constitution, a principal address and an acceptable name; no Regulations under 11(7) exist.
Its governor G reports being an undischarged bankrupt (19(1)(e)).
The Commissioner does not go to court, determines that G is unfit, and notifies A under 19(9)(e)(i); A declines to remove G.
Reading 11(4): A must be registered.
Reading 19(9)(c)/(e)(i): A must not be registered, and refusal is threatened on a ground 11(5) does not contain.
(A court application under 19(9)(b) would avoid the conflict, because 20(1)(c) lets the court order that the entity must not be registered; the Commissioner's own route has no such power.)

**Severity:** blocks a decision.
**Confidence:** high that the text conflicts.

### H2. A mandatory required steps notice that the Law makes invalid (organized religious charities)

**Provisions:** Art 19(9)(e)(i) (src:504-505); Art 27(4) (src:650); Art 28(3) (src:662).
**Type:** contradiction.

**Words:**
> src:504 | (e) must, if the issue is not to be determined by the court under sub-paragraph (b), on determining the issue –
>
> src:505 | (i) notify the entity that the application will be refused unless the governor is removed, or in the case of a registered charity serve a required steps notice requiring the charity to suspend or remove the governor, or
>
> src:650 | (4) If the notice is served by virtue of paragraph (1)(c) or (d), the steps required may include (subject to Article 28) the suspension, removal or replacement of the governor referred to in that paragraph.
>
> src:662 | (3) A required steps notice served on an organized religious charity, or on a governor of such a charity, is invalid to the extent that it purports to impose a requirement to suspend, remove or replace a governor of that charity.
>

**Why it is a problem.**
Once the Commissioner keeps the fitness issue (no court application) and finds the governor unfit, 19(9)(e) leaves exactly two options, and (ii) (permission) is excluded by the finding; so the Commissioner "must" serve a required steps notice "requiring the charity to suspend or remove the governor".
Article 19(9)(e) is not made subject to Article 28, although 27(4) is ("subject to Article 28").
For an organized religious charity, 28(3) makes that very requirement invalid.
The Law therefore commands an act that it also nullifies, and 16(1)(c) (deregistration for failing to comply with a required steps notice) cannot rest on the invalid requirement.

**Discriminating case.**
Governor G of registered charity R, which an Order under 28(1) categorizes as an organized religious charity, reports an unspent conviction for a dishonesty offence (19(1)(g)).
The Commissioner determines G unfit without going to court.
Reading 19(9)(e)(i): the Commissioner must serve a notice requiring R to remove G, and R's failure to comply is a deregistration ground.
Reading 28(3): the requirement is invalid, R has nothing to comply with, and G is merely barred from acting by 19(10).
The court route (19(9)(b), 20(1)(d)) is not restricted by 28(3), so the outcome also depends on which route the Commissioner chose.

**Severity:** blocks a decision.
**Confidence:** high.

### H3. Applications (and applications to deregister) that the Commissioner need never decide

**Provisions:** Art 11(4)-(5) (src:319, src:328); Art 19(6) (src:496); Art 11(8)(a)(i) (src:339); Art 15(3) (src:432); Art 33(1)(a), 33(2)(a) (src:691, src:694).
**Type:** scope gap; power without a procedure.

**Words:**
“If the applicant complies with paragraph (2), with any Regulations under paragraph (3), and with Article 19(5), the Commissioner must register” (src:319)
> src:328 | (5) If not so satisfied, the Commissioner must refuse to register the applicant.
>
> src:496 | (6) An application for registration is not complete if the entity has not complied with paragraph (5).
>
> src:339 | (i) the period within which the Commissioner must make a decision on an application,
>
> src:432 | (3) If the entity complies with paragraph (2) the Commissioner must –
>
> src:691 | (a) to refuse to register the applicant; or
>

**Why it is a problem.**
Both the duty to register (11(4)) and the duty to refuse (11(5), "If not so satisfied") arise only after the applicant "complies with paragraph (2)".
Where the Commissioner considers the applicant has not complied (for example, an item of 11(2) the Commissioner thinks missing or inadequate, or a missing 19(5) statement that makes the application "not complete"), there is no duty to decide either way, no time limit unless an Order under 11(8)(a)(i) sets one (none is in the sources), no deemed refusal, and so no "decision ... to refuse" that 33(1)(a) lets the applicant appeal.
Article 15(3) has the same shape for applications to deregister: the duty arises only "If the entity complies with paragraph (2)", and a refusal to deregister is not appealable by the charity at all (33(2)(a) covers only a decision "to deregister").

**Discriminating case.**
Applicant A files everything except details of its "most recent, if any, financial accounts" (11(2)(e)(i)), saying it has none; the Commissioner thinks it has.
Two years pass with no decision.
Can A appeal? Under 33(1)(a), only against a decision to refuse, which does not exist; only the Attorney General (33(4), "any decision") might act, and there is still no decision.
Contrast: had the Commissioner refused, A could appeal.

**Severity:** blocks a decision.
**Confidence:** high on the text; whether an Order under 11(8)(a)(i) fills the gap is not in the sources.

### H4. The annual return has no due date and no defined year

**Provisions:** Art 13(7)-(8) (src:392-393); Art 8(3)(j) (src:234); Art 1 "annual return" (src:8); Art 19(4) (src:494).
**Type:** temporal problem; duty without a time.

**Words:**
> src:392 | (7) A registered charity must send an annual return to the Commissioner, containing information as to any matter falling within paragraph (6) arising during the year to which the return relates, and as to any other matter prescribed by the Minister by Order for this purpose.
>
> src:393 | (8) An Order under paragraph (7) may also make provision as to the format and timing of the annual return, the consequences of lateness, and the content of any entries to be made on the register in respect of the annual return.
>
> src:234 | (j) whether the registered charity has or has not sent its annual return for the most recent year;
>
> src:8 | “annual return” means a return sent under Article 13(7);
>

**Why it is a problem.**
The duty to send an annual return has no deadline in the Law: timing is left to an Order under 13(8) ("may also make provision as to ... timing"), and none is in the sources.
"The year to which the return relates" is not defined: calendar year, the charity's financial year, and the year from registration are all available.
Yet the Commissioner must record, for every charity, "whether the registered charity has or has not sent its annual return for the most recent year" (8(3)(j)), a fact the Law gives no way to compute.
The definition in Article 1 adds a small circularity: a return becomes an "annual return" only once "sent under Article 13(7)", which is the thing 13(7) requires.

**Discriminating case.**
Charity C is registered on 1 October 2018 and has sent nothing by 1 March 2020.
Is C in breach of 13(7) (and so, through 2(10)(a)(i), guilty of misconduct)?
Calendar-year reading: a return for 2018 (three months) and for 2019 are due, but by when?
Registration-year reading: a return for the year to 30 September 2019 is due, by when?
What does 8(3)(j) record for C on 1 March 2020? Without an Order, the Law cannot say.

**Severity:** blocks a decision.
**Confidence:** high on the text; the content of any Order under 13(7)-(8) is an input.

### H5. No way to move a charity from the restricted section to the general section

**Provisions:** Art 9(2) (src:260); Art 13(5) (src:380-382); Art 13(6)(g) (src:390); Art 9(7)(b) (src:286).
**Type:** scope gap; power without a procedure.

**Words:**
> src:260 | (2) An applicant for registration, or a charity registered in the general section of the register, may request entry in the restricted section of the register if –
>
> src:380 | (5) A registered charity must, while it is entered in the restricted section of the register, ensure –
>
> src:390 | (g) if the charity is entered in the restricted section, a proposal to change how or whether the charity meets a condition prescribed under Article 9(2); and
>

**Why it is a problem.**
Article 9(2) lets an applicant, or a charity in the general section, ask to enter the restricted section.
Nothing lets a restricted-section charity ask to move to the general section, and nothing empowers the Commissioner to move it.
A restricted-section charity must "ensure" it keeps meeting its condition (13(5)), and must report a proposal to change how or whether it meets it (13(6)(g)), but the Law says nothing about what follows the report.

**Discriminating case.**
Charity R, registered in the restricted section on the funding condition that it does not solicit donations from the general public, decides to launch a public appeal and reports this under 13(6)(g).
Can the Commissioner transfer R to the general section? The Law confers no such power.
R's only lawful routes are to abandon the appeal, or to deregister (Art 15) and reapply, which triggers 17(5)-(8) and locks its existing property to its "preserved charitable purposes"; if it launches the appeal, it breaches 13(5) (misconduct), exposing it to a required steps notice and deregistration.

**Severity:** blocks a decision.
**Confidence:** high.

### H6. A governor the court finds fit is left with no permission and no route to one

**Provisions:** Art 19(9)(b), (d), (e) (src:501, src:503-504); Art 19(10)-(11) (src:507-510); Art 20(1)(a)-(b) (src:514-516).
**Type:** scope gap.

**Words:**
> src:501 | (b) may apply to the court to determine that issue under Article 20;
>
> src:503 | (d) may, in the case of a registered charity, by written notice to the charity, permit, either unconditionally or subject to any condition appearing to the Commissioner to be necessary, the governor to act as a governor until that issue is determined or the notice is withdrawn;
>
> src:504 | (e) must, if the issue is not to be determined by the court under sub-paragraph (b), on determining the issue –
>
> src:507 | (10) A person must not act as a governor of a registered charity at any time after reporting a reportable matter, unless the governor –
>
> src:508 | (a) is permitted to do so by the Commissioner under paragraph (9)(d) or (e)(ii), or by the court under Article 20; and
>
> src:510 | (11) A person who without reasonable excuse contravenes paragraph (10) commits an offence and is liable to imprisonment for one year and to a fine.
>
> src:515 | (a) an order dismissing the application;
>
> src:516 | (b) an order giving permission for the governor to act as a governor despite a reportable matter;
>

**Why it is a problem.**
After reporting, a governor may act only if "permitted ... by the Commissioner under paragraph (9)(d) or (e)(ii), or by the court under Article 20".
Interim permission under (9)(d) lasts only "until that issue is determined".
Final permission under (9)(e)(ii) is available only "if the issue is not to be determined by the court".
When the Commissioner applies to the court and the court simply dismisses the application (20(1)(a)), nobody has given permission (only 20(1)(b) is a permission), the interim permission has lapsed, and the Commissioner's (e)(ii) power is switched off.
A governor the court has found fit therefore commits an offence (19(11), one year and a fine) by acting.

**Discriminating case.**
G reports a 2019 conviction under this Law, now spent (reportable "whether or not spent", 19(1)(f)).
The Commissioner gives interim permission under 19(9)(d) and applies to the court; the court dismisses the application as unnecessary, making no 20(1)(b) order.
G chairs the next board meeting.
Literal reading: offence under 19(11), and no one can now give G permission except by a fresh court application.
Purposive reading: dismissal implies permission; no offence.

**Severity:** blocks a decision (how G may lawfully act again).
**Confidence:** medium; a court would probably read permission into a dismissal, but nothing in the text says so.

### H7. Deregistering an entity that no longer exists requires notice to a person who may not exist

**Provisions:** Art 16(2) (src:441); Art 17(2)(c) (src:449).
**Type:** power without a procedure.

**Words:**
> src:441 | (2) If the Commissioner is satisfied that an entity that is registered as a charity no longer exists, the Commissioner must, by written notice to any person purporting to be a governor of the entity or to be responsible for the winding up of the affairs of the entity, deregister the entity.
>
> src:449 | (c) specifies that date in the notice under Article 16(1) or (2); and
>

**Why it is a problem.**
The duty to deregister an entity that no longer exists is to be performed "by written notice to any person purporting to be a governor of the entity or to be responsible for the winding up", and a retrospective date must be specified "in the notice".
Where no such person exists, the duty cannot be performed and the register keeps a dead entity as a "registered charity" (Art 1, src:34) with no end.

**Discriminating case.**
The sole trustee of a registered charitable trust dies; no successor is appointed; nobody purports to be a governor or to wind it up.
The Commissioner is satisfied that the entity no longer exists.
16(2): "must ... deregister" by notice to nobody; the entity stays registered, and 8(3)(j) keeps recording missing annual returns.

**Severity:** blocks a decision (narrow).
**Confidence:** high.

### H8. Offences whose maximum fine the Law does not state

**Provisions:** Art 19(11) (src:510); 20(6) (src:529); 21(9) (src:563); 23(7) (src:593); 26(10) (src:635); 29(1) (src:667); level 3 fines: 21(10) (src:564), 23(6) (src:592), 26(7) (src:632).
**Type:** offence without a stated maximum.

**Words:**
“is liable to imprisonment for one year and to a fine” (src:510)
“is liable to imprisonment for 2 years and to a fine” (src:529)
“is liable to imprisonment for a term of 2 years and a fine” (src:667)
“is liable to a fine of level 3 on the standard scale” (src:564)

**Why it is a problem.**
Six offences carry "a fine" with no ceiling and three carry "level 3 on the standard scale", whose amount the Law does not state.
The conventional Jersey reading, that an unqualified "fine" is unlimited, comes from enactments that are not in the sources (the Interpretation (Jersey) Law 1954 and the standard scale legislation).
The question "what is the maximum penalty?" cannot be answered from this Law.

**Discriminating case.**
An encoder or a defendant asks the maximum fine for an unauthorised disclosure under 29(1): the Law says "a fine" and nothing more.
The same question for an unregistered entity calling itself a "charity" (21(10)) yields "level 3", whose amount is an input.

**Severity:** blocks a decision (of the maximum; liability is unaffected).
**Confidence:** high that the maximum is not stated; that it is unlimited is the likely reading, from outside the sources.

---

## Changes an outcome

### H9. "Minister" is defined as one named Minister, but Article 5(2)(a) says "a Minister"

**Provisions:** Art 1 "Minister" (src:26) and its opening words (src:7); Art 5(2)-(3) (src:150-155).
**Type:** definition problem (defined term used in an incompatible sense).

**Words:**
> src:7 | In this Law, unless the context otherwise requires –
>
> src:26 | “Minister” means the Chief Minister;
>
> src:150 | (2) An entity that otherwise meets the charity test, nevertheless does not meet that test, despite paragraph (1), if its constitution expressly permits its activities to be directed or otherwise controlled by, or any of its governors to be –
>
> src:151 | (a) a Minister;
>
> src:152 | (b) a member of the States Assembly; or
>
> src:153 | (c) any equivalent of such a person in another jurisdiction,
>
> src:154 | acting in that capacity.
>

**Why it is a problem.**
On the defined meaning, "a Minister" in 5(2)(a) is the Chief Minister alone; from 31 May 2019, and again from 27 February 2024 until 2 October 2026, it would be the Minister for External Relations alone (“Minister” there is substituted “Minister for External Relations” –” (R&O.40/2019 l.189); “In each provision in the following table, for “Chief Minister” there is substituted” (R&O.10/2024 l.263)); and from 2 March 2021 to 12 April 2023, apparently the Minister for External Relations and Financial Services (R&O.29/2021 is not in the sources, but R&O.28/2023 presupposes it: “for “Minister for External Relations and” (R&O.28/2023 l.177)).
That reading is absurd, but it is what the definition says unless "the context otherwise requires", and it matters because a Minister acting as a Minister is not "a member of the States Assembly ... acting in that capacity" (5(2)(b)).
5(2)(c) ("any equivalent of such a person in another jurisdiction") also moves: the equivalent of a head of government, or of any minister.
In the same Article, 5(3) uses "The Minister" in the defined sense, so the context does not clearly require a different sense two lines earlier.

**Discriminating case.**
Trust T's constitution lets the Minister for Health and Social Services, acting as Minister, appoint two of its trustees.
Defined-term reading: 5(2)(a) is not engaged (that Minister is not the Chief Minister), 5(2)(b) is not engaged (the Minister acts as Minister, not as a member), so T meets the charity test.
Ordinary reading ("any Minister"): T fails the charity test unless an Order under 5(3) disapplies 5(2).

**Severity:** changes an outcome.
**Confidence:** high that the text is ambiguous; a court would very likely take the ordinary reading.

### H10. Adding a purely ancillary purpose: void under 13(2), lawful under 5(1)(a)(ii)

**Provisions:** Art 13(2)-(3) (src:373-376); Art 5(1)(a) (src:146-148); Art 6(5) (src:201).
**Type:** contradiction.

**Words:**
> src:373 | (2) Any provision of the entity’s constitution or constitutional Law is of no effect to the extent that it purports to permit an amendment of the purposes of the entity to include a purpose that is not charitable.
>
> src:374 | (3) Any provision of the entity’s constitution or constitutional Law that purports to permit an amendment of the purposes of the entity to add or substitute a different charitable purpose, is to be read as being subject to the entity –
>
> src:147 | (i) charitable purposes, or
>
> src:148 | (ii) purposes that are purely ancillary or incidental to any of its charitable purposes; and
>
“is neither a charitable purpose nor a purpose ancillary or incidental to a charitable purpose” (src:201)

**Why it is a problem.**
The charity test admits purposes "purely ancillary or incidental" to charitable purposes, and 6(5) shows the Law treats such a purpose as something other than a charitable purpose.
13(2) makes void any power to add "a purpose that is not charitable"; an ancillary purpose is not a charitable purpose, so its addition is void, although the same purpose would pass the test on a first application.
If instead "not charitable" means "outside 5(1)(a)", the ancillary purpose falls outside 13(3) too (13(3) covers only "a different charitable purpose"), so it can be added with no approval at all.

**Discriminating case.**
Registered charity C, a company relieving poverty, resolves under its articles to add the object "to operate a café, purely ancillary to its charitable purposes".
Reading 1: the amendment is of no effect (13(2)).
Reading 2: it is valid and needs no Commissioner approval.
Reading 3 (purposive): it is valid only with approval under 13(3).

**Severity:** changes an outcome.
**Confidence:** medium-high.

### H11. Retrospective deregistration and the property acquired in the gap

**Provisions:** Art 17(2)-(3) (src:446-451); 17(5)-(9) (src:453-459); 13(1) (src:372).
**Type:** temporal problem; scope gap.

**Words:**
> src:451 | (3) The termination takes effect from the past date specified under paragraph (2)(c) for all purposes, including the purposes of any enactment relating to taxation, but subject to paragraph (4).
>
> src:453 | (5) Paragraphs (6) to (11) apply, after a charity is deregistered, if and so long as there remains any property of the charity that was acquired before it was deregistered (the “remaining property”).
>
“The entity must continue to apply the remaining property for the purposes that were its registered charitable purposes immediately before deregistration” (src:454)
> src:372 | (1) Paragraphs (2) to (4) apply while an entity is registered as a charity, and only cease to apply if the entity is deregistered.
>

**Why it is a problem.**
A retrospective deregistration "takes effect from the past date ... for all purposes".
"Remaining property" is property "acquired before it was deregistered"; on the "for all purposes" reading, property acquired between the past date and the notice was acquired after deregistration and escapes 17(6)-(9) entirely.
13(1) has the same seam: 13(2)-(4) apply "while an entity is registered", so a retrospective date also retroactively lifts 13(2)'s voiding of non-charitable amendments made in the gap.
17(4) protects acts from becoming offences, but nothing protects property or constitutional amendments.

**Discriminating case.**
On 1 June 2026 the Commissioner deregisters C under 16(1)(a), specifying under 17(2)(c) that the grounds existed since 1 January 2026 and that the deregistration takes effect from then.
On 1 March 2026 C received a donation of £100,000, given because C was registered.
Reading A ("for all purposes"): the £100,000 is not remaining property; C may apply it to any purpose its constitution allows, and the court's 17(9) powers do not reach it.
Reading B (deregistered on 1 June for 17(5)): it is remaining property, locked to the preserved charitable purposes.

**Severity:** changes an outcome.
**Confidence:** medium-high.

### H12. Is every unspent dishonesty conviction a reportable matter, or only one connected with a charity?

**Provisions:** Art 19(1)(g) (src:490); Art 2(10)(b) (src:111-117).
**Type:** connective ambiguity.

**Words:**
> src:490 | (g) has an unspent conviction for an offence falling within Article 2(10)(b); or
>
> src:111 | (b) the commission by any person, in relation a registered charity or to an excepted foreign charity (within the meaning of Article 22) or to an entity equivalent to a registered charity under the law of a jurisdiction other than Jersey, of an offence –
>
> src:116 | (v) under any other enactment or under customary law, being an offence involving deception or dishonesty, or
>

**Why it is a problem.**
2(10)(b) defines misconduct as the commission of an offence of the listed kinds "in relation [to] a registered charity" or a foreign equivalent.
19(1)(g) borrows "an offence falling within Article 2(10)(b)": it is unclear whether the borrowed description includes the "in relation to a registered charity" condition, or only the list of kinds (i)-(vi).

**Discriminating case.**
G, a governor of registered charity C, has an unspent conviction for shoplifting, an offence "involving ... dishonesty" (2(10)(b)(v)) unconnected with any charity.
Reading A (kinds only): it is a reportable matter; G must report it (19(2)), may not act afterwards without permission (19(10)), and failure to report is misconduct.
Reading B (with the charity connection): not reportable; G carries on.

**Severity:** changes an outcome.
**Confidence:** high that both readings are open.

### H13. The governor who reports commits an offence by acting; the governor who hides commits none

**Provisions:** Art 19(2)-(3) (src:492-493); 19(8) (src:498); 19(10)-(11) (src:507, src:510); 19(13) (src:512); 2(10)(a) (src:106).
**Type:** duty without a sanction; sanction asymmetry.

**Words:**
> src:492 | (2) A governor of an entity applying for registration, or of a registered charity, must report any reportable matter promptly to that entity or charity and to the Commissioner.
>
> src:493 | (3) A governor of an entity applying for registration must, if there is no reportable matter in relation to that governor, provide to the entity a declaration to that effect before the application is made.
>
> src:498 | (8) A person must not act as a governor of a registered charity at any time when the person is in breach of paragraph (2) or (4).
>
> src:507 | (10) A person must not act as a governor of a registered charity at any time after reporting a reportable matter, unless the governor –
>
> src:510 | (11) A person who without reasonable excuse contravenes paragraph (10) commits an offence and is liable to imprisonment for one year and to a fine.
>
> src:512 | (13) If at any time the Commissioner suspects that a governor of a registered charity may have breached paragraph (2), the Commissioner may, without prejudice to any other of his or her powers, apply to the court to determine whether the governor is a fit and proper person to be a governor.
>
> src:106 | (a) a contravention, by a registered charity or by any of its governors, of a provision –
>

**Why it is a problem.**
The criminal sanction (19(11)) attaches only to 19(10), which applies "after reporting".
A governor who does not report breaches 19(2) and 19(8), neither of which carries an offence; the only consequence is misconduct, a required steps notice, or a court application.
So the Law punishes compliance more heavily than concealment.
At the application stage the gap is wider: a governor of an applicant who gives the entity a false declaration under 19(3) commits no misconduct (2(10)(a) reaches only a registered charity and its governors), probably no 26(10) offence (the declaration goes to the entity, not the Commissioner), and 19(13) reaches only governors "of a registered charity".

**Discriminating case.**
G1 and G2, governors of charity C, are both made bankrupt in the same week.
G1 reports to C and the Commissioner and goes on acting while the Commissioner makes inquiries, with no interim permission under 19(9)(d): offence under 19(11), one year and a fine, unless G1 has a "reasonable excuse".
G2 reports nothing and goes on acting: breach of 19(2) and 19(8), no offence.

**Severity:** changes an outcome.
**Confidence:** high.

### H14. Decisions with no appeal for the person affected

**Provisions:** Art 33(1)-(3) (src:690-699); Art 15(3)(b) (src:434); Art 9(2), 9(5), 9(7) (src:260, src:273-279, src:284-286); 12(3)-(4) (src:362-363); 19(9)(e)(ii) (src:506); 10(5) (src:297); 13(11)(b) (src:403).
**Type:** scope gap (one item a connective ambiguity).

**Words:**
> src:690 | (1) An applicant for registration may appeal against a decision of the Commissioner –
>
> src:692 | (b) to refuse to register the applicant in the restricted section of the register.
>
> src:693 | (2) A registered charity may appeal against a decision of the Commissioner –
>
> src:694 | (a) to deregister the charity;
>
> src:695 | (b) to refuse permission, under Article 12(4), for the charity to change its registered name or add an alternative registered name;
>
> src:699 | (3) A person on whom the Commissioner serves a notice under Article 26 or a required steps notice may appeal against the decision of the Commissioner to impose a requirement contained in the notice.
>
> src:434 | (b) refuse to deregister the entity on grounds relating to the proposals mentioned in paragraph (2).
>
> src:273 | (5) A request under paragraph (2) must be accompanied by a statement of the applicant’s intention, in the event of refusal of the request, being –
>
> src:277 | (b) in the case of a charity registered in the general section of the register –
>

**Why it is a problem.**
Article 33 lists the appealable decisions, and several decisions that bind a charity or a governor are not on the list:
a refusal to deregister on the charity's own application (15(3)(b); 33(2)(a) covers only a decision "to deregister");
a refusal of a name change on any ground other than "under Article 12(4)" (12(3)-(5) give no other criteria, so the Commissioner may have a residual discretion whose exercise 33(2)(b) does not reach);
conditions and time limits placed on a governor's permission (19(9)(e)(ii)), refusals under 13(11)(b), and designations under 10(5).
Only the Attorney General (33(4)) can appeal those.
One more is a two-reading case rather than a plain gap: a refusal to move a general-section charity into the restricted section.
Article 9 calls such a charity "the applicant" (9(2)(a)-(b), 9(5)), but 33(1)(b) gives the appeal to "An applicant for registration", which a charity already registered is not.
A further wrinkle: 33(2) gives the right to appeal a deregistration to "A registered charity", which the entity no longer is once deregistered (and, after a retrospective deregistration, was not "for all purposes" from the past date, 17(3)).

**Discriminating case.**
Charity C applies to deregister (Art 15), supplies everything requested under 15(2), and the Commissioner refuses under 15(3)(b) on grounds relating to C's proposals for its remaining property.
C cannot appeal: 33(2)(a) covers a decision "to deregister", not a refusal to; only the Attorney General may (33(4)).
Had the Commissioner instead deregistered C against its will, C could appeal.
For the restricted-section item: general-section charity C2 asks to enter the restricted section because its staff are at risk, and is refused; reading "applicant" in 33(1) as in Article 9, C2 may appeal under 33(1)(b); reading "applicant for registration" strictly, it may not.

**Severity:** changes an outcome.
**Confidence:** high for the 15(3)(b), 12(3)-(4), 19(9)(e)(ii), 13(11)(b) and 10(5) items; medium for the restricted-section item.

### H15. A registered charity cannot appeal the registration of a confusingly named rival, and the ground is the Commissioner's own opinion

**Provisions:** Art 33(5) (src:701-703); 12(1) (src:354-355).
**Type:** scope gap; definition problem.

**Words:**
> src:701 | (5) A person, other than an applicant for registration, a registered charity, or the Attorney General, may appeal against a decision of the Commissioner to register an applicant, on the ground that, at both the time of the application and the time of the appeal –
>
> src:703 | (b) if the appellant has an interest in the registered name of the applicant, that name was undesirable under Article 12(1).
>
> src:354 | (1) For the purpose of Article 11(4)(e), the name of an entity is undesirable as the registered name of a charity if, in the opinion of the Commissioner, the name –
>
> src:355 | (a) is the same as, or too similar to, the name of any other registered charity;
>

**Why it is a problem.**
The person most likely to have "an interest in the registered name" of a new charity is an existing registered charity with a similar name (12(1)(a)), and 33(5) excludes "a registered charity" from appealing.
If "a registered charity" means the charity whose registration is in issue, the exclusion merely stops it appealing its own registration; if it means any registered charity, the 12(1)(a) case is unappealable except by the Attorney General.
Separately, 33(5)(b) requires that the name "was undesirable under Article 12(1)", and 12(1) makes undesirability a matter of "the opinion of the Commissioner"; by registering the name, the Commissioner held the opposite opinion, so the ground fails on its own words unless the tribunal forms its own opinion (34(3)(a) suggests it can).

**Discriminating case.**
Registered charity A is "Jersey Hospice Care"; the Commissioner registers B as "Jersey Hospice Cares".
Reading 1: A has no right of appeal.
Reading 2: A may appeal under 33(5)(b).

**Severity:** changes an outcome.
**Confidence:** medium-high.

### H16. Part 6 regulates only "entities": an individual or a partnership may call itself a charity

**Provisions:** Art 21(1)-(6) (src:533-560); 23(1)-(2) (src:578-585); Art 2(1)(i) (src:64).
**Type:** scope gap.

**Words:**
> src:533 | (1) An entity that is not a registered charity –
>
> src:536 | (2) A person must not refer to an entity, that is not a registered charity, as being registered by the Commissioner, if the person –
>
> src:541 | (3) A Jersey entity that is not a registered charity –
>
> src:551 | (5) An entity that is not a registered charity and is neither a Jersey entity nor an excepted foreign charity (within the meaning of Article 22) –
>
> src:578 | (1) Unless an entity meets all of the conditions in paragraph (3), that entity –
>
> src:64 | (i) the persons, taken together, who constitute for the time being an unincorporated body or association of persons, other than a partnership and other than the trustees of a trust;
>

**Why it is a problem.**
Every prohibition in Articles 21 and 23 is framed around "an entity", either as the speaker or as the thing referred to.
An individual is not within any limb of 2(1), and a partnership is expressly excluded from 2(1)(i).
So an individual or a partnership that describes itself as "a charity", "a Jersey charity" or "registered by the Commissioner" commits no offence under this Law, and nor does anyone who describes it so.

**Discriminating case.**
X, an individual, collects cash in St Helier with a bucket marked "Registered Jersey charity".
21(1), 21(2), 23(1), 23(2): not engaged (X is not an entity).
If the same bucket were held for an unregistered unincorporated club (2(1)(i)), the club commits an offence under 21(10) and 23(6), and X under 21(9) and 23(7) if the knowledge and intent elements are met.

**Severity:** changes an outcome.
**Confidence:** high on the text; the gap may be deliberate (general fraud law), but nothing says so.

### H17. A foreign-law trust within the Royal Court's jurisdiction is a "Jersey entity", which cancels its excepted-foreign-charity status

**Provisions:** Art 1 "trust" (src:46); 2(1)(a), (j) (src:49, src:65); 2(3)(a) (src:68); 8(3)(a)(i) (src:224); 21(3), 21(5) (src:541, src:551); 22(1) (src:566).
**Type:** definition problem (covers twice).

**Words:**
> src:46 | “trust” means a trust over which the court has jurisdiction under Article 5 of the Trusts (Jersey) Law 1984.
>
> src:49 | (a) the person or persons, taken together, who are the trustees of a trust;
>
> src:65 | (j) an entity that is substantially similar to an entity mentioned in any of sub-paragraphs (a) to (h), but is established under the law of a jurisdiction other than Jersey.[2]
>
> src:68 | (a) it falls within any of sub-paragraphs (a) to (h) of paragraph (1); or
>
> src:224 | (i) the sub-paragraph of the definition “entity” in Article 2(1) within which the entity falls (including, in the case of an entity falling within one of sub-paragraphs (f) to (j) of that definition, whether it also falls within sub-paragraph (a)), and
>
> src:541 | (3) A Jersey entity that is not a registered charity –
>
> src:551 | (5) An entity that is not a registered charity and is neither a Jersey entity nor an excepted foreign charity (within the meaning of Article 22) –
>

**Why it is a problem.**
"Trust" requires only that the Royal Court has jurisdiction under Article 5 of the Trusts (Jersey) Law 1984, not that Jersey law governs it, so the trustees of a foreign-law trust can fall within both 2(1)(a) and 2(1)(j); 8(3)(a)(i) shows the Law expects such overlaps.
2(3)(a) makes anything within (a) a "Jersey entity", and 21(3) then forbids it to call itself a "charity" anywhere, whereas the excepted-foreign-charity exemption in 21(5) applies only to an entity that is "neither a Jersey entity nor an excepted foreign charity".

**Discriminating case.**
An English charitable trust, registered in England and managed from London, has a Jersey trust company as one of its trustees, so that (an input) the Royal Court has jurisdiction over it under Article 5 of the 1984 Law.
It is not registered in Jersey and runs an appeal in a Jersey newspaper describing itself as "a charity".
Reading A (2(1)(a) applies): it is a Jersey entity, so the appeal is an offence (21(3), 21(10)), and the excepted-foreign-charity exemption cannot help.
Reading B ((j) governs foreign-law trusts): it is not a Jersey entity, is an excepted foreign charity, and may do so.

**Severity:** changes an outcome.
**Confidence:** medium; it turns on the reach of Article 5 of the 1984 Law, which is an input.

### H18. Sub-paragraph (ba), inserted in 2025 by Order, and the ranges "(a) to (h)"

**Provisions:** Art 2(1)(ba) (src:51-54), inserted by R&O.56/2025; 2(1)(j) (src:65); 2(2) (src:66); 2(3)(a) (src:68); 21(3), 21(5) (src:541, src:551); 11(4)(c) (src:322-324); 39(1) (src:736).
**Type:** temporal problem; amendment does not fit the text.

**Words:**
> src:51 | (ba) a body corporate that –
>
> src:53 | (ii) is established under the law of Jersey; and
>
> src:54 | (iii) does not fall within any of sub-paragraphs (c) to (h);
>
> src:66 | (2) The Minister may by Order add sub-paragraphs to paragraph (1).
>
> src:68 | (a) it falls within any of sub-paragraphs (a) to (h) of paragraph (1); or
>
> src:736 | (1) An Order or Regulations under this Law may contain such transitional, consequential, incidental, supplementary or savings provisions, other than an amendment of this Law, as appear to the Minister or the States (as the case may be) to be necessary or expedient for the purposes of the Order or Regulations.
>
“after paragraph (1)(b) there is inserted –” (R&O.56/2025 l.18)

**Why it is a problem.**
The ranges "(a) to (h)" in 2(1)(j) and 2(3)(a) were enacted in 2014, before (ba) existed.
On the positional reading, inserting (ba) after (b) silently extends both ranges, so an Order made under 2(2) (a power only to "add sub-paragraphs to paragraph (1)") changed who is a "Jersey entity" in paragraph (3), something 2(2) does not authorise and 39(1) forbids an Order to do by consequential amendment ("other than an amendment of this Law").
On the enacted-text reading, (ba) bodies are entities but not Jersey entities, although (ba)(ii) requires them to be "established under the law of Jersey".

**Discriminating case.**
A Jersey NPO body corporate within (ba), not registered, writes to UK donors describing itself as "a charity" in connection with its UK work.
Positional reading: it is a Jersey entity, so 21(3) applies wherever it speaks: offence (21(10)); it could also register without substantial Jersey activity (11(4)(c)(i)).
Enacted-text reading: only 21(5) applies, and only "in connection with any of its activities in Jersey": no offence; registration needs substantial Jersey activity (11(4)(c)(ii)).
Before 16 October 2025 the same body was within no limb of 2(1) at all (unless as a trustee, under (a)).

**Severity:** changes an outcome.
**Confidence:** medium; the positional reading is conventional, but it gives an Order an effect its enabling power does not cover.

### H19. "Constitutional Law" misses bodies incorporated under (not by) an enactment

**Provisions:** Art 2(5)(e) (src:85); 2(1)(e), (g), (h) (src:57-63); 8(4)(a) (src:240); 2(10)(a)(ii), (b)(i) (src:108, src:112).
**Type:** definition problem (under-inclusive).

**Words:**
> src:85 | (e) in relation to an entity that is a body incorporated by (but not under) any other Law, that Law.
>
> src:62 | (g) a body incorporated under, but not by, any enactment other than the Companies (Jersey) Law 1991;
>
> src:63 | (h) a body incorporated under, but not by, an Act of the United Kingdom Parliament or Order in Council, as such Act or Order is extended to or applicable in Jersey;
>
> src:240 | (a) if the registered charity is a company, foundation, or other entity required by its constitutional Law to have a registered office or business address in Jersey, the address of that registered office or that business address;
>
> src:108 | (ii) of the constitution of the registered charity, or of the constitutional Law of the charity,
>

**Why it is a problem.**
2(5)(e) gives a constitutional Law only to a body "incorporated by (but not under)" a Law; 2(1)(g) and (h) describe bodies "incorporated under, but not by" an enactment, the mirror image.
So (g) and (h) bodies, and (ba) and (j) bodies, have no constitutional Law, though their incorporating enactments may require them to keep a registered office in Jersey (an input).
That moves the principal address (8(4)(a) applies only to an entity "required by its constitutional Law to have a registered office"), and narrows misconduct (2(10)(a)(ii), (b)(i)) and the overrides in 13(2)-(3), 17(7) and 18(3).

**Discriminating case.**
Charity L is a body incorporated under, but not by, a Jersey enactment that (an input) requires it to keep a registered office in Jersey; its work is run from a governor's home.
Literal reading: no constitutional Law, so 8(4)(a) does not apply, 8(4)(b) does not apply (private dwelling house), and its principal address is a governor's address (8(4)(c)).
Purposive reading: its incorporating enactment is its constitutional Law, so its principal address is its registered office.

**Severity:** changes an outcome.
**Confidence:** medium-high on the text; whether "by"/"under" is a slip is not provable from the sources.

### H20. The power to demand information cannot reach the cases the Commissioner most needs it for

**Provisions:** Art 26(1)-(2) (src:618-623); 27(3) (src:647-649); 4(1)(c) (src:127); 26(7) (src:632).
**Type:** scope gap; function without a power.

**Words:**
> src:619 | (a) to provide to the Commissioner, at such time and place as may be specified in the notice, any information or document of a specified description that the Commissioner reasonably requires for the purpose of determining whether to serve a required steps notice; or
>
> src:622 | (a) a registered charity or an entity that was formerly a registered charity; and
>
> src:647 | (3) The relevant persons for the purpose of paragraph (2) are –
>
> src:648 | (a) the registered charity; and
>
> src:649 | (b) the governors of the registered charity.
>
> src:127 | (c) to seek to enforce the requirements of Part 6 as to use of terms restricted by or under that Part;
>

**Why it is a problem.**
The only purpose for which information may be demanded is "determining whether to serve a required steps notice", and such a notice can be served only on a registered charity and its governors.
26(2)(a) names "an entity that was formerly a registered charity", but a demand to a deregistered entity about its own conduct (for example its use of remaining property under 17(6)) serves no lawful purpose under 26(1), so failure to answer it is arguably no offence under 26(7).
And the Commissioner's function "to seek to enforce the requirements of Part 6" comes with no information power at all over unregistered entities, the only ones Part 6 restrains.

**Discriminating case.**
1. Deregistered entity D holds remaining property; the Commissioner suspects it is being spent on non-charitable purposes and serves a 26(1) notice for D's accounts; D refuses.
Reading A (no required steps notice can follow, so the demand is outside 26(1)): no offence.
Reading B (the information might bear on a notice to some current charity): offence.
2. Unregistered Jersey entity E describes itself as a "charity"; the Commissioner cannot require E to produce anything (E is not within 26(2)).

**Severity:** changes an outcome.
**Confidence:** high for case 2; medium for case 1.

### H21. Knowingly false annual returns, reports and declarations are not covered by the false-information offence

**Provisions:** Art 26(10)-(11) (src:635-638); 13(6)-(7) (src:383, src:392); 15(2) (src:431); 9(4) (src:270-272); 19(2), 19(5) (src:492, src:495).
**Type:** scope gap.

**Words:**
> src:635 | (10) A person commits an offence, and is liable to imprisonment for a term of 2 years and to a fine, if the person provides information to the Commissioner, knowing that it is false in a material particular and intending it to be used by the Commissioner for the purpose of an application for registration or for the purpose of determining whether to serve a required steps notice.
>
> src:495 | (5) The entity must state in its application, and the registered charity must state in its annual return, that it has declarations from all of its governors who have not made a report under paragraph (2).
>

**Why it is a problem.**
The offence requires an intention that the information be used "for the purpose of an application for registration or for the purpose of determining whether to serve a required steps notice".
Information in an annual return, a 13(6) report, a request to enter the restricted section by a charity already registered, an application to deregister, or a governor's 19(2) report is given for none of those purposes on its face.

**Discriminating case.**
Charity C states in its annual return that it holds declarations from all its governors (19(5)), knowing it does not.
Reading A (the purposes are limited as written): no offence; misconduct only.
Reading B (an annual return is always potential material for a required steps notice): offence, two years and a fine.
The identical false statement in an application for registration is plainly an offence.

**Severity:** changes an outcome.
**Confidence:** high.

### H22. Restricted information: whose consent is needed?

**Provisions:** Art 29(1) (src:664-667).
**Type:** connective ambiguity.

**Words:**
> src:664 | (1) Subject to paragraph (2) and to Articles 30 and 31, a person who receives information relating to the business or other affairs of any person –
>
> src:666 | (b) directly or indirectly from a person who has so received it,
>
> src:667 | commits an offence and is liable to imprisonment for a term of 2 years and a fine if he or she discloses the information without the consent of the person to whom it relates and (where sub-paragraph (b) applies) the person from whom it was received.
>

**Why it is a problem.**
"Without the consent of the person to whom it relates and ... the person from whom it was received" can mean that both consents are needed (missing either is an offence) or that the offence needs both to be missing (either consent suffices).

**Discriminating case.**
H, a governor of charity C, received information about C's affairs from the Commissioner under this Law and passes it to journalist J; J publishes it with C's consent but without H's.
Reading A (both consents needed): J commits an offence (two years and a fine).
Reading B (either suffices): no offence.

**Severity:** changes an outcome.
**Confidence:** high that both readings are open.

### H23. The Commissioner may assist foreign regulators, but disclosing information to them may be an offence

**Provisions:** Art 4(3)(c) (src:136); Art 29(1) (src:664-667); Art 31(a)-(f) (src:676-682); Art 4(1)(e) (src:129).
**Type:** contradiction / scope gap.

**Words:**
> src:136 | (c) assist a body in any jurisdiction other than Jersey, that is equivalent to the Commissioner, or to the Attorney General, the court, the Comptroller or the JFSC, in the performance of that body’s functions under the law of that jurisdiction.
>
> src:676 | Article 29 does not preclude the disclosure of information –
>
> src:677 | (a) by or on behalf of the Commissioner, for purpose of enabling the Commissioner to discharge any of his or her functions;
>
> src:129 | (e) to assist other persons (including the Attorney General, the court, the Bailiff, the Comptroller and the JFSC) to discharge, in relation to registered charities and entities with charitable purposes, any function of such a person under any enactment or law, particularly by giving information about registered charities and other entities under Part 7;
>

**Why it is a problem.**
4(3)(c) empowers the Commissioner to assist a foreign equivalent body "in the performance of that body's functions", and Article 31 has no gateway for disclosure to a foreign body.
The only candidate is 31(a), disclosure "for purpose of enabling the Commissioner to discharge any of his or her functions"; but 4(3)(c) is listed as a power, not among the functions in 4(1), and the assistance serves the foreign body's functions, not the Commissioner's.
Contrast 4(1)(e), which makes assisting Jersey bodies a function "particularly by giving information ... under Part 7".

**Discriminating case.**
The Charity Commission for England and Wales asks the Jersey Commissioner for documents obtained under Article 26 about a person who is a governor in Jersey and a trustee in England.
Reading A (assisting under 4(3)(c) is a Commissioner function within 31(a)): lawful disclosure.
Reading B (31(a) covers only 4(1) functions): the officer who discloses commits an offence under 29(1).

**Severity:** changes an outcome.
**Confidence:** medium.

### H24. Article 29 binds every recipient, including charities, governors and the tribunal, with gateways only for officials

**Provisions:** Art 29(1)-(2) (src:664-671); 19(2)-(4) (src:492-494); 31 (src:676-682); Sch 2 para 4(3)(g) (src:858).
**Type:** scope gap (over-inclusive).

**Words:**
> src:665 | (a) under or for the purposes of this Law; or
>
> src:858 | (g) the publication of reports of the tribunal’s decisions;
>
> src:680 | (d) to the Attorney General, the Bailiff or the court for the purpose of enabling them to discharge any of their functions in relation to charities, whether under this Law, a constitutional Law, the customary law, or any other law;
>

**Why it is a problem.**
Anyone who receives information "under or for the purposes of this Law" is bound: a charity receiving a governor's 19(2) report or 19(3)-(4) declaration, its other governors, the tribunal and its staff.
The gateways in Article 31 are for the Commissioner, the Comptroller, the JFSC, the Attorney General, the Bailiff, the court, investigations, and Regulations; there is none for a charity's ordinary governance, and none for the tribunal (31(d) names "the court", and the tribunal is not the court; Sch 2 para 4(3)(g) lets Regulations provide for publishing decisions but is not itself an exception to 29).

**Discriminating case.**
Governor H reports H's bankruptcy to charity C under 19(2); C's chair tells C's bank, which asks for its governors' insolvency status, without H's consent.
Literal reading: offence under 29(1) by the chair.
Narrow reading (29 aims at official information): no offence.
Likewise, the tribunal publishing a reasoned decision that names a governor's reportable matter, absent Regulations under 31(f).

**Severity:** changes an outcome.
**Confidence:** medium.

### H25. "The notice under Article 16(1)": there are two

**Provisions:** Art 16(1) (src:436); 17(2)(c) (src:449); 17(4) (src:452).
**Type:** wrong cross-reference (ambiguous target).

**Words:**
> src:436 | (1) The Commissioner may, by written notice to an entity that is registered as a charity, deregister the entity if satisfied, after giving the entity written notice specifying reasons and inviting objections within a reasonable time specified in the notice, that it is proportionate to do so on the ground that –
>
> src:449 | (c) specifies that date in the notice under Article 16(1) or (2); and
>
> src:452 | (4) An act, that occurred before the date of the giving of the notice under Article 16(1) or (2) is not rendered an offence merely by virtue of the operation of paragraph (3).
>

**Why it is a problem.**
16(1) involves a preliminary notice "specifying reasons and inviting objections" and the "written notice" by which the entity is deregistered.
17(2)(c) and 17(4) refer to "the notice under Article 16(1)" as if there were one.
The cut-off date for 17(4)'s protection against retrospective offences depends on which.

**Discriminating case.**
Preliminary notice 1 March; deregistration notice 1 May, retrospective to 1 January.
On 15 April the entity tells donors it is "a charity" (21(3)).
Reading A (the preliminary notice): the 15 April act is after "the date of the giving of the notice", so 17(4) does not protect it, and by 17(3) the entity was unregistered on 15 April: offence under 21(10).
Reading B (the deregistration notice): protected; no offence.

**Severity:** changes an outcome.
**Confidence:** medium.

### H26. The commencement table uses the pre-renumbering article numbers without saying so

**Provisions:** Endnotes, Table of Legislation History (src:876-880) and Table of Renumbered Provisions (src:914-928); R&O.17/2018 (RO17 l.11, l.29-31); current Art 41-43 (src:742-753).
**Type:** temporal problem; renumbering.

**Words:**
> src:876 | Parts 1 to 3, Articles 32, 38, 39, 40, 42, 43 and 44 and
>
> src:878 | Parts 4, 5, 7, 8 (other than Article 32), Article 37 in
>
> src:880 | Remainder in force 1 January 2019 (R&O.17/2018).
>
“force by Article 44(2) of that Law or Article 1 of this Act, come into force on” (R&O.17/2018 l.30)

**Why it is a problem.**
The 2014 list names "Articles 32, 38, 39, 40, 42, 43 and 44", and the current Law has no Article 44, so the list must be in the original numbering; but the table does not say so, and read in current numbering it gives a different answer for current Article 41.
On the original numbering (confirmed by R&O.17/2018's reference to "Article 44(2)"), original 42, 43 and 44(1) are today's 41, 42 and 43, all in force on 21 November 2014, and the "Remainder" (1 January 2019) is Part 6 plus the original Article 41 ("spent, omitted"), whose text is not in the sources (R&O.17/2018's heading for the remainder reads “relating to taxation and to use of” (R&O.17/2018 l.27)).

**Discriminating case.**
The States make Regulations in 2016 under current Article 41(2) (sharing of information with the Commissioner).
Current-numbering reading: Article 41 is not in the 2014 list, so it was in the "Remainder" and the 2016 Regulations had no power behind them.
Original-numbering reading: original Article 42 (now 41) was in force from 21 November 2014; the Regulations are valid.

**Severity:** changes an outcome.
**Confidence:** high that the original numbering is meant; the table is still wrong for a reader who takes it at face value.

### H27. "Wholly or mainly managed or controlled in or from within Jersey"

**Provisions:** Art 23(3)(c) (src:589); 23(1), (6) (src:578, src:592).
**Type:** connective ambiguity.

**Words:**
> src:589 | (c) is wholly or mainly managed or controlled in or from within Jersey.
>
> src:592 | (6) An entity that contravenes paragraph (1) commits an offence and is liable to a fine of level 3 on the standard scale.
>

**Why it is a problem.**
The condition can be met by management alone or control alone, or it can require both (or the place of control to be decisive).
Contrast 22(3)(a), which speaks only of where an entity is "managed".

**Discriminating case.**
Jersey foundation F, a registered charity, has a council resident in London that takes all decisions there; all day-to-day administration is done by staff in Jersey.
Reading A (either suffices): F may call itself a "Jersey charity".
Reading B (control must be in Jersey too): F commits a strict-liability offence (23(6)) if it does.

**Severity:** changes an outcome.
**Confidence:** medium-high.

### H28. "The jurisdiction under the law of which it is established" for a charity in one part of the UK managed from another

**Provisions:** Art 22(2)(a)(i) (src:569); 22(3)(a) (src:573).
**Type:** connective ambiguity.

**Words:**
> src:569 | (i) of the United Kingdom, or of any jurisdiction that is part of the United Kingdom, or
>
> src:573 | (a) is managed wholly or mainly from the jurisdiction under the law of which it is established; and
>

**Why it is a problem.**
22(2)(a)(i) treats the United Kingdom and its parts alike, but 22(3)(a) asks whether the entity is managed from "the jurisdiction under the law of which it is established", which for a Scottish charity is Scotland and for an English one is England (and Wales).

**Discriminating case.**
A charity established under Scots law and registered in Scotland is managed from London; it is not registered in Jersey and describes itself as a "charity" when fundraising in Jersey.
Reading A (Scotland): not managed from there, so not excepted: offence under 21(5) and 21(10).
Reading B (the United Kingdom): excepted; no offence.

**Severity:** changes an outcome.
**Confidence:** medium.

### H29. The safety exception cannot protect historic-section entries

**Provisions:** Art 10(4)-(5) (src:296-297); 10(3)(c) (src:295); 8(5) (src:243-248).
**Type:** scope gap.

**Words:**
> src:296 | (4) Paragraph (5) applies if the Commissioner considers, in relation to a particular registered charity, that the safety or security of any person, property or premises would be significantly put at risk by public access to a matter entered on any section of the register in respect of that charity.
>
> src:297 | (5) The Commissioner may designate that matter as not being a public part of the register, in relation to that registered charity.
>
> src:243 | (5) The Commissioner must enter in the historic section, in relation to any formerly registered charity that has been deregistered –
>

**Why it is a problem.**
10(4) speaks of "any section of the register", but the power is exercisable only "in relation to a particular registered charity", and the historic section is about entities that are no longer registered charities (Art 1, src:34).
So a matter in the historic section (former name, reason for deregistration, dates) must be published on the website (10(1), 10(3)(c)) even where publication would put a person at risk.

**Discriminating case.**
A deregistered domestic-abuse refuge's historic entry shows its name and that it was deregistered for failing to comply with a required steps notice, with the reason for the notice (8(5)(c)).
The Commissioner considers that access would significantly put staff at risk.
Reading A (literal): no power to withhold.
Reading B ("any section" carries the power over to former charities): may withhold.

**Severity:** changes an outcome.
**Confidence:** high.

### H30. Historic section: is the name of a charity that moved into the restricted section published?

**Provisions:** Art 8(5)(b) (src:245); 9(1)(a) (src:256); 10(3)(c) (src:295).
**Type:** connective / temporal ambiguity.

**Words:**
> src:245 | (b) if the entity was registered in the general section, the name under which the entity was registered immediately before deregistration, and any names under which it was previously so registered;
>
> src:256 | (a) the registration number (but not the registered name) of the charity;
>

**Why it is a problem.**
"If the entity was registered in the general section" can mean at any time, or immediately before deregistration.
On the first reading, the historic section must publish "the name under which the entity was registered immediately before deregistration", which for an entity then in the restricted section is the name 9(1)(a) kept private.

**Discriminating case.**
Charity C is in the general section from 2018 to 2021, moves to the restricted section in 2021, and is deregistered in 2026.
Reading A (at any time): its 2026 name goes into the public historic section.
Reading B (immediately before deregistration): no name is entered.

**Severity:** changes an outcome.
**Confidence:** medium.

### H31. "Donation" and "solicit" are defined only by an Order that may not exist, made for another purpose

**Provisions:** Art 1 "donation", "solicit" (src:17, src:44); 9(2)(a), 9(3) (src:261, src:263-269); 14(3)(a)(ii) (src:414); 24(1) (src:595).
**Type:** definition problem; temporal problem.

**Words:**
> src:17 | “donation” is to be construed in accordance with the Order made under Article 9(3)(b)(ii);
>
> src:44 | “solicit” is to be construed in accordance with the Order made under Article 9(3)(b)(i);
>
> src:263 | (3) The Order –
>
> src:265 | (b) must specify, for the purpose of paragraph (2)(a) –
>
> src:268 | (iii) if the Order does not prescribe a description of persons, what constitutes the general public for the purpose of the Order; and
>
> src:269 | (c) may make provision under sub-paragraph (b) by reference to the exercise of discretion by the Commissioner, or in any other manner.
>
> src:414 | (ii) soliciting donations from the public, as specified in the order, or
>

**Why it is a problem.**
Article 1 imports the meanings Law-wide from "the Order made under Article 9(3)(b)", but 9(3)(b) asks that Order to specify them only "for the purpose of paragraph (2)(a)", and 9(3)(c) lets it do so "by reference to the exercise of discretion by the Commissioner".
Until such an Order exists (none is in the sources), "donation" and "solicit" have no statutory meaning; once one exists, the reach of a court order under 14(3)(a)(ii), and of any offence created by Regulations under 24, may depend on the Commissioner's discretion.
"The Order" in 9(3) is also singular where 9(2)(a) and (b) each contemplate an Order; an Order made only under 9(2)(b) need not define the terms at all.
"The general public" is defined only "for the purpose of the Order", but 24(1) uses it too.

**Discriminating case.**
The Royal Court orders charity C under 14(3)(a)(ii) not to solicit donations from the public; C then asks the public for "suggested membership fees".
With no 9(3)(b) Order: the Law cannot say whether that is soliciting a donation.
With an Order defining both by the Commissioner's discretion: the answer is whatever the Commissioner decides.

**Severity:** changes an outcome.
**Confidence:** medium.

### H32. Offences "by an entity" that is not a body corporate have no one to bear them

**Provisions:** Art 37(1) (src:728-731); 21(9)-(10) (src:563-564); 23(6)-(7) (src:592-593); 2(1)(a), (b), (i) (src:49-50, src:64).
**Type:** scope gap (sanction without a bearer).

**Words:**
> src:728 | (1) If an offence under this Law, committed by a limited liability partnership, a separate limited partnership or a body corporate is proved to have been committed with the consent or connivance of –
>
> src:564 | (10) An entity, that contravenes paragraph (1), (3) or (5), commits an offence and is liable to a fine of level 3 on the standard scale.
>
> src:49 | (a) the person or persons, taken together, who are the trustees of a trust;
>

**Why it is a problem.**
Part 6 makes "an entity" liable to a fine (21(10), 23(6)) and to imprisonment (21(9), 23(7)), and an entity can be "the person or persons, taken together, who are the trustees of a trust" or the members of an unincorporated association.
Article 37 attributes offences only for limited liability partnerships, separate limited partnerships and bodies corporate; nothing says which of the persons "taken together" is convicted, fined or imprisoned.

**Discriminating case.**
An unregistered unincorporated sports club (a Jersey entity under 2(3)(b)) calls itself a "charity" on its website.
Who is guilty under 21(10): every member, the committee, or only whoever published the page?
For a company in the same position, the company is guilty and consenting directors are too (37(1)).

**Severity:** changes an outcome.
**Confidence:** medium; Jersey's general criminal law (not in the sources) may supply an answer.

### H33. Retention and other periods with no stated start

**Provisions:** Art 8(6) (src:249); 17(1)(a) (src:444); 26(5) (src:628-630); 20(5) (src:528); 11(2)(e)(ii) (src:310).
**Type:** temporal problem.

**Words:**
> src:249 | (6) The Commissioner must retain for 10 years, in respect of each registered charity, a copy of –
>
> src:444 | (a) must retain the information registered in respect of that entity for 10 years; and
>
> src:628 | (5) A document, copy or extract retained or taken under paragraph (4)(a) may be retained for whichever is the longer of –
>
> src:629 | (a) a period of one year; and
>
> src:528 | (5) A disqualification order is to be for such period, not exceeding 15 years, as the court directs.
>

**Why it is a problem.**
8(6) says how long ("10 years") but not from when: from receipt of each document, or from the charity's deregistration (read with 17(1)(a))?
17(1)(a) requires retention of "the information registered in respect of that entity for 10 years" after deregistration, which may or may not include the historic-section entry made under 8(5), for which no period is given.
26(5) does not say when the "period of one year" starts (when the document is taken, or when copies are made); 20(5) does not say whether the 15 years run from the order or from some earlier date; 11(2)(e)(ii) does not say whether "the 12 months preceding the application" includes the day of application.

**Discriminating case.**
Charity C registered in 2018 is still registered in 2029.
Reading A (from receipt): the Commissioner may destroy C's 2018 constitution in 2029.
Reading B (10 years after the charity leaves the register): must keep it.

**Severity:** changes an outcome.
**Confidence:** high that the start is unstated.

### H34. An application must include a payments statement only if an Order "applies to the registered charity"

**Provisions:** Art 11(2)(e)(ii) (src:310); 13(9)(b) (src:396).
**Type:** definition problem.

**Words:**
> src:310 | (ii) any payment made to any governor of the entity in the 12 months preceding the application, and if an Order under Article 13(9)(b) applies to the registered charity, a draft of the proposed statement under that Order,
>
> src:396 | (b) require a registered charity to provide to the Commissioner a statement of its current intentions as to making any payments of such a prescribed description in future;
>

**Why it is a problem.**
An applicant is not yet a registered charity, and an Order under 13(9)(b) can only "require a registered charity" to do something, so on its words it never "applies to" an applicant.
Read literally, the requirement for a draft statement on an application can never be triggered.

**Discriminating case.**
An Order under 13(9)(b) applies to registered charities with annual income above a threshold; applicant A is above it and files no draft statement.
Literal reading: A has complied with 11(2), so the Commissioner must register A if the other conditions are met (11(4)).
Purposive reading: A has not complied; 11(4) is not triggered.

**Severity:** changes an outcome.
**Confidence:** medium.

### H35. The power to require a change of name arises only from the charity's own report

**Provisions:** Art 12(6) (src:365); 13(6)(b) (src:385).
**Type:** scope gap.

**Words:**
> src:365 | (6) If a registered charity reports a matter relating to its registered name under Article 13(6)(b), the Commissioner may require the charity to apply to change its registered name under paragraph (3).
>

**Why it is a problem.**
If the charity does not report, the Commissioner cannot use 12(6) however clearly the name has become undesirable; the only route is a required steps notice for the failure to report, which has a different appeal route (33(3), not 33(2)(c)) and different consequences.

**Discriminating case.**
"X Cancer Research" stops funding research; it does not report; the Commissioner learns of it from the press.
12(6) is not available; a required steps notice under 27(1)(a) is.
Had the charity reported, 12(6) would apply and the charity's appeal would lie under 33(2)(c).

**Severity:** changes an outcome.
**Confidence:** medium.

### H36. Sitting States members may be appointed Commissioner or tribunal member; only "becoming" a member ends the appointment

**Provisions:** Sch 1 para 3(4)(b) (src:791); Sch 2 para 2(4)(b) (src:837).
**Type:** scope gap.

**Words:**
> src:791 | (b) the person becomes a member of the States; or
>
> src:837 | (b) the person becomes a member of the States; or
>

**Why it is a problem.**
The incompatibility bites only on a person who "becomes" a member of the States after appointment; a person who is already a member when appointed never "becomes" one, and nothing else forbids the appointment.

**Discriminating case.**
The Minister appoints a sitting States member as Commissioner.
Literal reading: the appointment stands for its full term.
Purposive reading: it expires at once, or was never valid.
A Commissioner first elected to the States a year into the term loses office at once on either reading.

**Severity:** changes an outcome.
**Confidence:** high on the text.

### H37. Can the Commissioner appeal from the tribunal?

**Provisions:** Art 35(1) (src:714); 33 (src:689-703); Sch 2 para 4(3)(h) (src:859).
**Type:** used but undefined ("party").

**Words:**
> src:714 | (1) A party to an appeal to the tribunal, or the Attorney General, may appeal from the decision of the tribunal to the court on the ground that the decision was unreasonable having regard to all the circumstances of the case.
>
> src:859 | (h) duties of the Commissioner in relation to an appeal;
>

**Why it is a problem.**
The Law never says who the parties to an appeal are; it names the appellants in Article 33 and speaks of "duties of the Commissioner in relation to an appeal", not of the Commissioner as respondent.

**Discriminating case.**
The tribunal substitutes "register" for the Commissioner's refusal; the Commissioner wants the Royal Court to review it.
Reading A (the Commissioner is a party): may appeal under 35(1).
Reading B (not a party): only the Attorney General may.

**Severity:** changes an outcome.
**Confidence:** medium-low; the ordinary reading makes the decision-maker a party, but the Law does not.

### H38. No time limit for appeals unless an Order makes one

**Provisions:** Art 36(2)(a) (src:721); 33(5) (src:701).
**Type:** temporal problem; power without a default.

**Words:**
> src:721 | (a) prescribe time limits within which appeals to the tribunal or court are to be brought; and
>
“at both the time of the application and the time of the appeal” (src:701)

**Why it is a problem.**
Without an Order (none is in the sources), an appeal to the tribunal or the court can be brought at any time, including a third party's appeal against a registration years later; and "the time of the appeal" in 33(5) can be the time it is brought or the time it is heard.

**Discriminating case.**
In 2030 a third party appeals against a 2019 registration.
No Order: in time; and the applicant's position "at ... the time of the appeal" is measured at lodging or at hearing, giving different answers if the charity changed its purposes in between.

**Severity:** changes an outcome.
**Confidence:** medium.

### H39. When does a resigning Commissioner stop being Commissioner, and does acting service count?

**Provisions:** Sch 1 para 3(1)(a) (src:779-780); 3(4)(c) (src:792); 4(5) (src:801-804); 4(3)(c) (src:799).
**Type:** temporal problem.

**Words:**
> src:779 | (1) A person ceases to be appointed as the Commissioner if –
>
> src:780 | (a) he or she resigns from office by giving not less than 3 months’ notice in writing to the Minister;
>
> src:792 | (c) the person completes 12 years (whether consecutive or in aggregate) of service as Commissioner.
>
> src:801 | (5) A relevant person designated under sub-paragraph (4) is to be treated as the Commissioner for the purposes of this Law, if –
>

**Why it is a problem.**
"Resigns ... by giving not less than 3 months' notice" does not say whether office ends when the notice is given or when it expires.
3(4)(c) counts "service as Commissioner" but does not say whether time as a "relevant person ... treated as the Commissioner" (4(5)) counts.

**Discriminating case.**
The Commissioner gives notice on 1 January 2027 resigning with effect from 1 April 2027 and on 15 February 2027 deregisters a charity, a decision only the Commissioner may take (Sch 1 para 4(3)(c)).
Reading A (office ends when notice is given): the deregistration was made by someone no longer in office.
Reading B (office ends when notice expires): valid.

**Severity:** changes an outcome.
**Confidence:** medium.

### H40. Who "the Minister" is can change in the middle of a day

**Provisions:** Art 1 "Minister" (src:26); R&O.10/2024 (RO10 l.46, l.263, l.273); R&O.40/2019 (RO40 l.188-189, l.195).
**Type:** temporal problem.

**Words:**
“9.30 a.m. 27th February 2024” (R&O.10/2024 l.46)
“for “Chief Minister” there is substituted” (R&O.10/2024 l.263)
“Charities (Jersey) Law 2014” (R&O.10/2024 l.273)

**Why it is a problem.**
R&O.10/2024 changed the meaning of "Minister" (from the Chief Minister to the Minister for External Relations) at 9.30 a.m. on 27 February 2024, so a vintage keyed only by date cannot say who "the Minister" was on that day.
R&O.40/2019 was made and in force on the same day (“31st May 2019” (R&O.40/2019 l.49); “Coming into force” (R&O.40/2019 l.50)), with no time stated; whether it ran from the start of the day depends on the Interpretation (Jersey) Law 1954, which is not in the sources.

**Discriminating case.**
An Order under this Law signed by the Chief Minister on 27 February 2024: valid if signed at 9.00 a.m., made by the wrong Minister if signed at 10.00 a.m.

**Severity:** changes an outcome (narrow).
**Confidence:** high on the text.

### H41. "Or other advantage" appears in one false-reference offence and not in its three siblings

**Provisions:** Art 21(2)(b)(ii) (src:540); 21(4)(b)(ii) (src:550); 21(6)(b)(ii) (src:560); 23(2)(b)(ii) (src:585).
**Type:** inconsistency between parallel provisions.

**Words:**
> src:540 | (ii) to give to the entity any property or financial or other advantage.
>
> src:550 | (ii) to give any property or financial advantage to the entity.
>
> src:560 | (ii) to give any property or financial advantage to the entity.
>
> src:585 | (ii) to give any property or financial advantage to the entity.
>

**Why it is a problem.**
Only 21(2) reaches an intent to obtain a non-financial "other advantage"; the "charity" and "Jersey charity" offences reach only property or financial advantage.

**Discriminating case.**
P, knowing Jersey entity E is unregistered, tells volunteers that E is "a charity" so that they will work for it unpaid.
21(4): no offence (unpaid work is not "property or financial advantage").
Had P said E was "registered by the Commissioner": offence under 21(2).

**Severity:** changes an outcome.
**Confidence:** medium that the difference is unintended.

### H42. Schedule 1 is made "subject to Article 20(1)" of the Dormant Bank Accounts Law, which is not the provision about the Commissioner

**Provisions:** Sch 1 para 2(4)(a) (src:776), 4(7) (src:806); L.1/2017 Art 20(1), 20(2)(a), 30(3) (L1 l.637, l.642, l.904-908).
**Type:** wrong cross-reference.

**Words:**
> src:776 | (a) subject to Article 20(1) of the Dormant Bank Accounts (Jersey) Law 2017, the remuneration or other payment for services of the Commissioner, due under the terms of his or her appointment, must be paid out of the annual income of the States; and
>
“The Minister must by Order, having consulted the Minister for Treasury” (L.1/2017 l.637)
“to defray the cost of the remuneration or other payment for the” (L.1/2017 l.642)
“words “subject to Article 20(1) of the Dormant Bank Accounts” (L.1/2017 l.905)

**Why it is a problem.**
In the Dormant Bank Accounts Law as enacted (the only version in the sources), Article 20(1) is the power to make an Order setting distribution policy; the provision that lets Fund money "defray the cost of the remuneration" of the Commissioner is Article 20(2)(a).
The Charities Law text matches what L.1/2017 inserted, so this is a defect of the amending Law, not of the consolidation.
Article 20 may since have been amended by Regulations (its paragraph (8)); no later version is in the sources.

**Discriminating case.**
No Order has been made under Article 20(1) of the 2017 Law.
Reading A (only an Order under 20(1) displaces the rule): the Commissioner's pay must come from the annual income of the States.
Reading B (the reference means Article 20, including 20(2)(a)): it may be paid from the Fund.

**Severity:** changes an outcome (fiscal).
**Confidence:** medium-low.

### H43. The public benefit rules bind only the Commissioner, the tribunal and the court

**Provisions:** Art 7(1) (src:203); 5(5) (src:157).
**Type:** scope gap.

**Words:**
> src:203 | (1) Paragraphs (2) and (3) apply to the Commissioner, the tribunal and the court when determining the question of whether an entity provides or intends to provide public benefit, for the purpose of Article 5(1)(b).
>
“Any person, in determining whether an entity meets the charity test, must have regard to the guidance” (src:157)

**Why it is a problem.**
5(5) contemplates that "Any person" may determine whether an entity meets the charity test (and 42(a) contemplates the test being applied under the Trusts and Foundations Laws), but 7(2)-(3), including the ban on presuming public benefit, bind only three named bodies.

**Discriminating case.**
The Comptroller, or a trustee applying the test under an enactment amended under Article 42(a), decides whether a religious trust meets the test.
Reading A: may presume that advancing religion is for the public benefit (7(3)(a) does not bind them).
Reading B (7 states the meaning of 5(1)(b) for everyone): may not.

**Severity:** changes an outcome.
**Confidence:** medium.

### H44. Court orders "to remedy the misconduct" where the ground is not misconduct

**Provisions:** Art 14(1)(b) (src:409); 14(2) (src:410).
**Type:** connective ambiguity.

**Words:**
> src:410 | (2) The court may make any order that the court sees fit to remedy the misconduct, protect the property and secure its proper application.
>

**Why it is a problem.**
14(1)(b) lets the court act without any misconduct (to protect property), but 14(2) describes the orders it may make with three conjoined aims, the first of which presupposes misconduct.

**Discriminating case.**
On an application under 14(1)(b) alone, may the court appoint a manager (14(3)(b))?
Reading A ("and" means the aims that apply): yes.
Reading B (all three aims): no order is possible, because there is no misconduct to remedy.

**Severity:** changes an outcome.
**Confidence:** low; reading A is almost certainly right.

### H45. "One of the governors": which one?

**Provisions:** Art 8(4)(c) (src:242); 11(4)(d) (src:325); 13(6)(a) (src:384).
**Type:** definition problem (indeterminate).

**Words:**
> src:242 | (c) if neither sub-paragraph (a) nor (b) applies, the address in Jersey of one of the governors of the charity.
>

**Why it is a problem.**
Where neither 8(4)(a) nor (b) applies, the principal address is "the address in Jersey of one of the governors", but nothing says which governor, or who chooses.
Whether a governor's move is "a change in a matter about which information is entered on the register" (13(6)(a)) depends on which governor's address it is.

**Discriminating case.**
Charity C has three governors in Jersey and no premises other than their homes.
Governor 2 moves house.
If governor 2's address is the principal address, C must report the move (13(6)(a)); if governor 1's is, it need not.

**Severity:** changes an outcome.
**Confidence:** medium.

### H46. Approvals and permissions the Law requires but gives no procedure or criteria for

**Provisions:** Art 13(4)(b) (src:379); 13(5)(b) (src:382); 13(11)(b) (src:403); 12(3)-(5) (src:362-364); 33(2)(e) (src:698).
**Type:** power without a procedure.

**Words:**
> src:379 | (b) if it requests the Commissioner’s approval of a proposed amendment to that statement, provide evidence, to the satisfaction of the Commissioner, of a reason justifying that request.
>
> src:382 | (b) if, before it ceased to meet that condition, the Commissioner gave prior permission for it to remain entered in the restricted section on the basis of a different condition prescribed under that Article, that it meets that condition as specified in that permission.
>
> src:403 | (b) may apply to the Commissioner, with reasons, for permission to amend that statement.
>
> src:698 | (e) to refuse to approve an amendment, proposed under Article 13(4)(b), to the charity’s registered public benefit statement.
>

**Why it is a problem.**
The Law assumes the Commissioner can approve an amendment of the registered public benefit statement (and 33(2)(e) gives an appeal against a refusal "proposed under Article 13(4)(b)"), can give "prior permission" to switch restricted-section conditions, and can permit an amended payments statement, but says nothing about how such requests are made, the criteria, any time limit, or how the register is then amended.
13(4)(b) itself only imposes an evidential burden on a request; it does not create the request.

**Discriminating case.**
Charity C asks for approval to amend its registered public benefit statement and hears nothing for a year.
Is there a decision to appeal under 33(2)(e)? Is C bound by its old statement (13(4)(a)) in the meantime? The Law does not say.

**Severity:** changes an outcome.
**Confidence:** medium.

### H47. Tribunal: no duty to keep the minimum membership, no quorum, and costs in two places

**Provisions:** Sch 2 para 1(1) (src:816); para 4(1)-(3) (src:846-861); Art 34(3)(b) (src:711); contrast Sch 1 para 1(7) (src:764).
**Type:** scope gap.

**Words:**
> src:816 | (1) The Minister must appoint as members of the tribunal at least 4, and no more than 8, persons appearing to the Minister to be suitable for the position and to have appropriate experience to safeguard the interests of the public and the charitable sector in Jersey.
>
> src:764 | (7) The Minister must take all reasonable steps to ensure that at all times the office of the Commissioner is filled.
>
> src:711 | (b) award costs if satisfied that the appeal was vexatious or otherwise grossly unreasonable;
>
> src:857 | (f) the award of costs, and the creation of offences in relation to the tribunal, carrying a penalty not exceeding imprisonment for a term of 2 years and a fine;
>

**Why it is a problem.**
The Minister must appoint "at least 4" members, but, unlike the Commissioner's office (Sch 1 para 1(7)), there is no duty to keep the tribunal filled, and no quorum unless Regulations make one; a sitting of one member presiding over itself is not excluded.
34(3)(b) allows costs only for vexatious or grossly unreasonable appeals, while Regulations under Sch 2 para 4(3)(f) may provide for "the award of costs" generally.

**Discriminating case.**
Resignations leave two members; one sits alone and decides an appeal.
Reading A: valid (the tribunal regulates its own procedure, para 4(2)).
Reading B: invalid (the tribunal is not properly constituted below four).

**Severity:** changes an outcome.
**Confidence:** low.

### H48. "Further provision as to the service of any notice", with no first provision

**Provisions:** Art 38 (src:734); 26(1) (src:618); 27(2) (src:646).
**Type:** power without a procedure.

**Words:**
> src:734 | The Minister may by Order make further provision as to the service of any notice under this Law.
>

**Why it is a problem.**
Notices must be "served" (26(1), 27(2)), but the Law contains no rule on service for an Order to add to; absent an Order and outside rules (the Interpretation (Jersey) Law 1954, not in the sources), whether a notice left at a principal address that is a governor's home has been served is not decided here.

**Discriminating case.**
A required steps notice is posted to a charity's principal address and never read; the charity is deregistered for non-compliance (16(1)(c)).
Whether the notice was "served" decides whether the deregistration ground exists.

**Severity:** changes an outcome.
**Confidence:** low; outside rules very probably answer it.

---

## Cosmetic

### H49. Misconduct cites "excepted foreign charity (within the meaning of Article 22)", but Article 22 defines it only for Article 21, and was not in force when misconduct first mattered

**Provisions:** Art 2(10)(b) (src:111); 22(1) (src:566); commencement (src:876-880).
**Type:** cross-reference; temporal problem.

**Words:**
“or to an excepted foreign charity (within the meaning of Article 22)” (src:111)
> src:566 | (1) For the purpose of Article 21, an entity is an excepted foreign charity if it meets both the condition in paragraph (2) and the condition in paragraph (3).
>

**Why it is a problem.**
22(1) limits the definition "For the purpose of Article 21"; and Article 22 (Part 6) came into force on 1 January 2019, while misconduct was operative from 1 May 2018 through Parts 4, 5 and 7.

**Discriminating case.**
In August 2018 a governor is convicted of fraud against a UK registered charity.
The 2(10)(b) limb "an entity equivalent to a registered charity under the law of a jurisdiction other than Jersey" very probably catches it anyway, so no case was found where the result changes.

**Severity:** cosmetic (probably).
**Confidence:** high on the text, low on any effect.

### H50. The verb "register" makes a deregistered entity "registered"

**Provisions:** Art 1 "register", "registered charity" (src:32, src:34); 8(5) (src:243); 21(1) (src:533-535).
**Type:** definition problem.

**Words:**
> src:32 | “register” means the register kept by the Commissioner under Article 8, or (as a verb) to enter an entity on that register, and “registration” and “deregistration” are to be construed accordingly;
>
> src:34 | “registered charity” means an entity entered for the time being in the general section or the restricted section of the register;
>

**Why it is a problem.**
"To enter an entity on that register" includes entering it in the historic section, so a deregistered entity is, on the words, "registered" again; "registered charity" avoids this only because it is defined by section.

**Discriminating case.**
A deregistered entity truthfully says it is "on the Commissioner's register (historic section)".
21(1) forbids an entity that is not a registered charity to refer to itself "as being registered by the Commissioner" on either reading, so no case was found where the result changes.

**Severity:** cosmetic.
**Confidence:** medium.

### H51. R&O.40/2019 amends "Article 1(1)", which does not exist

**Provisions:** R&O.40/2019 Sch 2 para 1(e) (RO40 l.188-189, l.195); Art 1 (src:6-7).
**Type:** amendment does not fit the text.

**Words:**
“Article 1(1) of the Charities (Jersey) Law 2014” (R&O.40/2019 l.195)
> src:7 | In this Law, unless the context otherwise requires –
>

**Why it is a problem.**
Article 1 of the Charities Law is a single unnumbered paragraph; the instrument's target is misdescribed (unlike R&O.28/2023, R&O.10/2024 and R&O.102/2026, which say "1" or "Article 1").
The substitution evidently took effect (the vintage chain depends on it), so nothing changes.

**Discriminating case.** None found.

**Severity:** cosmetic.
**Confidence:** high.

### H52. Endnote [4] corrects "for purpose of" in Article 31(c), and the same slip remains in (a) and (b)

**Provisions:** Art 31(a)-(c) (src:677-679); endnote [4] (src:939-941).
**Type:** consolidated text v endnote.

**Words:**
> src:677 | (a) by or on behalf of the Commissioner, for purpose of enabling the Commissioner to discharge any of his or her functions;
>
> src:678 | (b) to the Comptroller for purpose of enabling the Comptroller to discharge any of his or her functions;
>
> src:679 | (c) to the JFSC for the purpose of enabling the JFSC to discharge any of its functions;
>
“in sub-paragraph (c),” (src:940)

**Why it is a problem.**
The editorial change was applied to (c) only; (a) and (b) still read "for purpose of".
No difference in meaning.

**Discriminating case.** None found.

**Severity:** cosmetic.
**Confidence:** high.

### H53. Names and references that do not match

**Provisions:** Sch 2 heading (src:814) v Art 1 "tribunal" (src:45) and Art 32 (src:686); Sch 1 para 4(12) (src:811); endnote [3] marker (src:491) v endnote text (src:937).
**Type:** wrong name / reference.

**Words:**
> src:814 | Charity Commission tribunal
>
> src:45 | “tribunal” means the Charity Tribunal established by Article 32;
>
“Directions under paragraph (11)” (src:811)
> src:491 | (h) falls within any other description that may be prescribed by the Minister by Order.[3]
>
> src:937 | [3] Article 19(1) editorial change, in sub-paragraph (e), “law or
>

**Why it is a problem.**
Schedule 2 is headed "Charity Commission tribunal", a body that does not exist; the tribunal is the "Charity Tribunal".
Schedule 1 elsewhere calls its own subdivisions "sub-paragraph" (for example src:765, src:781, src:801), but para 4(12) says "paragraph (11)".
Endnote [3] concerns 19(1)(e), but its marker sits at the end of 19(1)(h).

**Discriminating case.** None found.

**Severity:** cosmetic.
**Confidence:** high.

### H54. Terms used but not defined

**Provisions:** "historic section" (src:221, src:243, src:295); "charity" alone (src:132, src:680, src:739); "supervisory body" (src:747); "resident" (src:71); "Jersey charity" (src:413, before Art 23); "the applicant" in Art 9 (src:261-262, src:273).
**Type:** used but undefined.

**Words:**
> src:20 | “general section” means the section of the register that is to be distinguished from the restricted and historic sections under Article 8(2);
>
> src:43 | “restricted section” means the section of the register that is to be distinguished from the general and historic sections under Article 8(2);
>
> src:132 | (2) The Commissioner may do anything (other than acting as a governor of a charity or of an entity with charitable purposes) that is calculated to facilitate, or is conducive or incidental to, the performance of any of his or her functions.
>
> src:747 | (2) The States may by Regulations amend any relevant enactment, to make such provision as the States consider necessary or expedient to enable any supervisory body, the JFSC and the Comptroller to disclose information to the Commissioner for the purposes of this Law.
>
> src:261 | (a) the applicant meets the funding condition, prescribed by the Minister by Order for this purpose, as to refraining from soliciting donations from the general public or from any prescribed description of persons; or
>

**Why it is a problem.**
Article 1 defines the general and restricted sections but not the historic section.
"A charity" in 4(2) (the Commissioner may not act as "a governor of a charity") could mean a registered charity or any charity anywhere.
"Supervisory body" in 41(2) is undefined (presumably as in the Proceeds of Crime (Supervisory Bodies) Law, an input).
Article 9 uses "the applicant" both for an applicant for registration and for a registered charity making a request (9(2), 9(5)), which is what makes 33(1)(b) a two-reading case (H14).

**Discriminating case.**
4(2): the Commissioner, as a corporation sole, agrees to act as a trustee of an English charitable trust; lawful if "a charity" means a Jersey registered charity, unlawful if it means any charity.
No case found for the others.

**Severity:** cosmetic.
**Confidence:** high.

### H55. The register's status note does not mention (ba)

**Provisions:** Art 8(3)(a)(i)-(ii) (src:224-225); 2(1)(ba) (src:51-54).
**Type:** amendment does not fit the text.

**Words:**
> src:225 | (ii) in the case of an entity falling within one of sub-paragraphs (e), (g), (h) or (j) of that definition, details of the enactment, Act of the States, Royal Charter, Act of the United Kingdom Parliament, Order in Council or foreign law, by virtue of which it falls within that sub-paragraph;
>

**Why it is a problem.**
8(3)(a)(ii) requires details of the law under which an entity was established for (e), (g), (h) and (j), but not for (ba), which also turns on being "established under the law of Jersey"; and 8(3)(a)(i)'s note on overlap with (a) covers "(f) to (j)" only.
An Order under 2(2) could not have made the consequential amendment (39(1)).

**Discriminating case.** None found beyond what the register shows.

**Severity:** cosmetic.
**Confidence:** high.

---

## Checks that came out clean

**HTML-derived text against the PDF text layer.**
A word-level diff (`work/hunt/pdfdiff.py`, output in `work/hunt/pdfdiff.out`), after normalising curly quotes and dashes, dropping the PDF's running heads and the endnote markers, found the two texts word-for-word identical from the long title to the end of Schedule 2; the only differences are heading capitals ("PART 1" for "Part 1") and the glued endnote markers.
The endnotes (legislation history, renumbering table, endnote references) also match.

**Amending instruments against the consolidated text.**
L.13/2019 Sch 3 para 1 substitutes "Revenue Administration (Jersey) Law 2019" for "Income Tax (Jersey) Law 1961" in "Comptroller": matches src:12.
L.1/2017 Art 30(3) inserts the two "subject to Article 20(1)" phrases: matches src:776 and src:806 (but see H42 on the target).
R&O.40/2019 (Chief Minister to Minister for External Relations, 31 May 2019), R&O.28/2023 (Minister for External Relations and Financial Services to Chief Minister, 12 April 2023, made 5 April, in force 7 days later), R&O.10/2024 (Chief Minister to Minister for External Relations, 9.30 a.m. 27 February 2024) and R&O.102/2026 (Minister for External Relations to Chief Minister, made 25 September 2026, in force 7 days later, 2 October 2026) form a consistent chain ending in src:26, except that R&O.28/2023 presupposes a text ("Minister for External Relations and Financial Services") that only R&O.29/2021 could have produced, and R&O.29/2021 is not in the sources.
R&O.56/2025, made 9 October 2025 by the Minister for External Relations (the Minister under the definition then in force), in force 7 days later (16 October 2025), inserts (ba) exactly as src:51-54.
R&O.17/2018 commences Parts 4, 5, 7, 8 (other than Article 32) and Article 37 on 1 May 2018 and the remainder on 1 January 2019, as the endnote says.

**Cross-references.**
A regex count finds 83 references of the form "Article N…" to this Law in the body (and 14 more to other enactments); each was checked by hand against its target, as was every internal "paragraph"/"sub-paragraph" reference read in passing.
All resolve to an existing provision with the content the reference assumes, except those reported above (H25, H34, H42, H49, H53); none uses a pre-renumbering number (the body never refers to Articles 41-44).

**Provisions read in full and found clean** (nothing reported against them beyond the findings that cite them):
Art 1 (other definitions); 2(1)(b)-(i), 2(2), 2(3)(b), 2(4), 2(6)-(9), 2(10)(a); 3; 4(1)(a)-(b), (d)-(g), 4(2) apart from H54, 4(4); 5(1), 5(3)-(8); 6(1)-(4); 7(2)-(4); 8(1)-(3) apart from H4, H45, H55, 8(4)(a)-(b) apart from H19; 9(1), 9(4)-(7); 10(1)-(3); 11(1), 11(3), 11(4)(a)-(f) apart from H1, 11(5)-(11); 12(1)-(5), 12(7); 13(3), 13(5)-(13) apart from H4, H34, H46; 14(1), 14(3)-(6); 15(1)-(2); 16(1)(a)-(d); 17(6)-(11) apart from H11; 18(1)-(4); 19(1)(a)-(f), (h), 19(4)-(7), 19(12); 20(1)-(5); 22(1)-(2), 22(4)-(5) apart from H28, H49; 23(1)-(2), (4)-(7) apart from H27, H41; 24; 25; 26(3)-(9), 26(11); 27(1)-(5); 28(1)-(2); 30; 31(b)-(f); 32; 34; 35(2)-(4); 36(1), 36(3)-(4); 37(2); 39; 40; 41; 42; 43; Schedule 1 paras 1, 2, 3(2)-(3), 4(1)-(11); Schedule 2 paras 1(2)-(8), 2(1)-(3), 3.

## What the sources do not let me check

- The text of the original Article 41 and of original Article 44(2)-(3) (spent, omitted).
- R&O.29/2021 (2 March 2021) and R&O.136/2019 (commencement of L.13/2019), and the Act appointing 16 December 2019 for L.1/2017: none is in the sources.
- Any Order or Regulations made under the Law (9(2)-(3), 11(7)-(8), 13(7)-(10), 22, 24, 27(5), 28, 31(f), 36(2), 38, Sch 2 para 4(3)); several findings (H3, H4, H8, H31, H38, H48) would be narrowed or closed by them.
- The external enactments the Law leans on (Trusts (Jersey) Law 1984 Art 2(b) and Art 5, the Interpretation (Jersey) Law 1954, the standard scale of fines, the Non-Profit Organizations (Jersey) Law 2008, the Employment of States of Jersey Employees (Jersey) Law 2005 Arts 15 and 17): treated as inputs.
