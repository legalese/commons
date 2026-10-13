# FRAGMENT-G5: ss.30 to 40 of the Regulation of Engagement in Work on Refrigeration or Air-Conditioning Systems Law 5785-2025

Written by ENCODER G5, for the INTEGRATOR.
Scope: Chapter 5, Subchapters A and B (ss.30 to 40).
Modules: `g5-inspectors` (ss.30-32), `g5-senior-inspector` (ss.33-34), `g5-testing-bodies` (ss.35-36), `g5-test-conduct` (ss.37-38), `g5-withdrawal` (ss.39-40).
Tests: `g5-tests-inspectors`, `g5-tests-senior-inspector`, `g5-tests-testing-bodies`, `g5-tests-test-conduct`, `g5-tests-withdrawal`, `g5-tests-entry` (trap T30, imports two modules), `g5-tests-red` (assertions meant to fail, counted).
Status of every claim below: written after the last run of the check script in section 9, and checked against it; nothing here describes a planned state.
Each module imports only `prelude`, `daydate` (where it uses a date), `il-interpretation-time` (where it counts a period) and `domain`.
Import graph, acyclic: no rule module imports another G5 module, because I read ruling 1 as forbidding it; the lead has since said that intra-group imports are allowed, and I did not change the modules, so the wiring between them is by inputs (section 5) and the INTEGRATOR may compose them.
The tests import the modules they test: each `g5-tests-X` imports `g5-X`; `g5-tests-entry` imports `g5-inspectors` and `g5-test-conduct`; `g5-tests-red` imports all five rule modules.
No G5 module imports another group's module.
Hebrew in the quotation comments is copied by `srcrefs.py quote` from `inputs/law.wiki`; the English is mine.
I typed no Hebrew.
Sources checked: `law.wiki` lines 247 to 337 (ss.30 to 40), and the gazette page images of Sefer HaChukim 3349 pp.189 to 193 (the text layer is scrambled, so the images were read); every list and count in ss.30 to 40 (four powers in s.31, two conditions in s.32, seven definitions in s.33, six subsections in s.34, five conditions in s.35, five subsections in s.36, five powers and four conditions in s.37, three subsections in s.38, five grounds in s.39, three enactments in s.40) agrees between the two, and I found no difference in wording that bears on a rule.
Every non-blank line of those sections except the two headings (s.30 and Subchapter B) is quoted in a module beside the rule that carries it.

## 1. Coverage

74 rows of ss.30 to 40, in the Law's numbering: 69 encoded, 1 inert, 1 refused, 3 out-of-scope, 0 deferred.
The dispositions and modules are those of `phase1/slice-G5.md`; I changed none.
Row 36(a) stays `refused` because the section carries a named REFUSE (the regulations under s.60(1)(c) are not in the sources); its duty is encoded as well.
Row 33 is `inert`: the lead-in is quoted at the head of `§§ s 33` and introduces seven definitions that have their own rows.
Rows 40(1) to (3) are `out-of-scope`: the enactments' content is outside the sources; each is a constructor of the list in `Enactment on which section 40 equates testers and experts with State employees`, so the equation of s.40 is encoded.
A row with a rule on it that is an alternative reading says so in the rule column.

| row | provision | disposition | module | rule(s) |
| --- | --- | --- | --- | --- |
| 30 | s.30 | encoded | `g5-inspectors` | container: see 30(a) to (c) |
| 30(a) | s.30(a) | encoded | `g5-inspectors` | `s 30(a) — the Minister shall authorise inspectors from among the employees of the Ministry` (MUST); `s 30(a) — the candidate is an employee of the Ministry` (limb "(a)" of the decision below); alternative `s 30(a), read as a power — ...` (MAY) |
| 30(b) | s.30(b) | encoded | `g5-inspectors` | `s 30(b) — the candidate may be authorised as an inspector` (exported; it also carries the employee test of s.30(a), so a non-employee is never answered TRUE); `s 30(b) — the Minister shall authorise as an inspector only a person who satisfies all three conditions` (SHANT) |
| 30(b)(1) | s.30(b)(1) | encoded | `g5-inspectors` | `s 30(b)(1) — the candidate was not convicted of an offence that makes him unfit, in the Minister's opinion`; alternative `s 30(b)(1), counting a conviction for a disciplinary offence too` |
| 30(b)(2) | s.30(b)(2) | encoded | `g5-inspectors` | `s 30(b)(2) — the candidate received suitable training, as the Minister directed` |
| 30(b)(3) | s.30(b)(3) | encoded | `g5-inspectors` | `s 30(b)(3) — the candidate meets the further conditions of eligibility the Minister directed` |
| 30(c) | s.30(c) | encoded | `g5-inspectors` | `s 30(c) — the Minister shall have notice of an inspector's authorisation published in Reshumot` (MUST), over `s 30(c) — notice of an inspector's authorisation shall be published in Reshumot by` publisher |
| 31 | s.31 | encoded | `g5-inspectors` | container: see 31(1) to (4) |
| 31(1) | s.31(1) | encoded | `g5-inspectors` | `s 31(1) — an inspector may require any person to give his name and address and to show identification` (MAY) |
| 31(2) | s.31(2) | encoded | `g5-inspectors` | `s 31(2) — an inspector may require a person concerned to give information or a document` (MAY); `s 31(2) — the demand is one the inspector may make`; `s 31(2) — the thing is a document, which includes computer output`; `the inspector's demand for a document under s.31(2) was lawfully made` (IP10); `s 31(2) — a person concerned shall give the information or document an inspector lawfully demanded` (MUST); `the violation committed under s.31(2), if any` (IP9); alternative `s 31(2), s 32 ignored — a document was demanded` |
| 31(3) | s.31(3) | encoded | `g5-inspectors` | `s 31(3) — an inspector may enter a place` (MAY); `s 31(3) — the inspector may enter the place` (exported); `s 31(3) — the inspector has reason to suppose that unlicensed or non-conforming work is done or engaged there`; `s 31(3) proviso — the place may be entered: it is not a dwelling, or a court order permits it, or the holder consented`; `s 31(3) proviso — an inspector shall not enter a dwelling without a court order or the holder's consent` (SHANT) |
| 31(4) | s.31(4) | encoded | `g5-inspectors` | `s 31(4) — an inspector may make measurements and tests`; `... may order measurements and tests kept for a period he directs`; `... may deal with measurements and tests in another way` (three MAY rules); period P22: `s 31(4) — the last day of the period for keeping directed on`, `s 31(4), s 10(c) applied — ...`, `s 31(4) — keeping is directed on` ... , `s 31(4), beginning the day after the direction — keeping is directed on` ... |
| 32 | s.32 | encoded | `g5-inspectors` | container: see 32(1), 32(2); the lead-in (on duty) and the whole gate are `s 32 — the inspector may use the powers` and the SHANT `s 32 — an inspector shall not use the powers unless he is performing his function, wears the badge and holds the certificate` |
| 32(1) | s.32(1) | encoded | `g5-inspectors` | `s 32(1) — the inspector visibly wears a badge identifying him and his function` |
| 32(2) | s.32(2) | encoded | `g5-inspectors` | `s 32(2) — the inspector holds a certificate signed by the Minister stating his function and powers`; `s 32(2) — the certificate, if it was demanded, was shown`; `s 32(2) — an inspector whose certificate is demanded shall show it` (MUST); alternative `s 32, reading A — ...` |
| 33 | s.33 | inert | `g5-senior-inspector` | quoted at `§§ s 33`; no rule: the lead-in introduces seven definitions that have their own rows |
| 33/def1 | s.33 def.1 | encoded | `g5-senior-inspector` | `s 33 def 1 — the test is an auxiliary test`; `s 33 def 1 — the performer is a tester or an expert` |
| 33/def2 | s.33 def.2 | encoded | `g5-senior-inspector` | `s 33 def 2 — the person is a tester` (exported) |
| 33/def3 | s.33 def.3 | encoded | `g5-senior-inspector` | `s 33 def 3 — the person is a family member of the subject`; `s 33 def 3 — the person is a relative of the subject` |
| 33/def4 | s.33 def.4 | encoded | `g5-senior-inspector` | `s 33 def 4 — the corporation is a testing body` |
| 33/def5 | s.33 def.5 | encoded | `g5-senior-inspector` | `s 33 def 5 — the person is an expert` (exported); alternative `s 33 def 5, an employee authorised only to test being a tester and not an expert — the person is an expert` |
| 33/def6 | s.33 def.6 | encoded | `g5-senior-inspector` | `s 33 def 6 — the subject is in a conflict of interest` (exported); `s 33 def 6 — the other person is a relative whose interest or role conflicts with the subject's function` |
| 33/def7 | s.33 def.7 | encoded | `g5-senior-inspector` | `s 33 def 7 — the list is a checklist` |
| 34 | s.34 | encoded | `g5-senior-inspector` | container: see 34(a) to (f) |
| 34(a) | s.34(a) | encoded | `g5-senior-inspector` | `s 34(a) — the Minister shall authorise a senior inspector from among the inspectors` (MUST); alternative `s 34(a), read as a power — ...` (MAY) |
| 34(b) | s.34(b) | encoded | `g5-senior-inspector` | `s 34(b) — the senior inspector may rely on auxiliary test findings and expert opinions` (MAY); `s 34(b) — the senior inspector may rely on the material` |
| 34(b)(1) | s.34(b)(1) | encoded | `g5-senior-inspector` | `s 34(b) — the material is findings by a tester, or findings or an opinion by an expert` (first arm of the CONSIDER) |
| 34(b)(2) | s.34(b)(2) | encoded | `g5-senior-inspector` | `s 34(b) — the material is findings by a tester, or findings or an opinion by an expert` (second and third arms); `s 34(b)(2) — the opinion was given by an expert` |
| 34(c) | s.34(c) | encoded | `g5-senior-inspector` | `s 34(c) — the Ministry shall engage a testing body or an expert to be relied on only in accordance with the Mandatory Tenders Law` (SHANT), over `s 34(c) — a testing body or an expert shall be engaged ..., the party engaging being` engager; `s 34(c) — the engagement is made in accordance with the Mandatory Tenders Law`; the last words (an expert may be employed by a testing body) are tested, not ruled: `g5-tests-senior-inspector` |
| 34(d) | s.34(d) | encoded | `g5-senior-inspector` | `s 34(d) — an engaged testing body shall report each auxiliary test and its findings to the senior inspector` (MUST); `s 34(d) — the report covers the auxiliary test and its findings and is signed by the manager` |
| 34(e) | s.34(e) | encoded | `g5-senior-inspector` | `s 34(e) — an engaged or employed expert shall report each auxiliary test and give his opinion on its results` (MUST); `s 34(e) — the expert is engaged in accordance with section 34(c) or employed by a testing body`; `s 34(e) — the report covers the auxiliary test, gives the opinion on its results and is signed by the expert` |
| 34(f) | s.34(f) | encoded | `g5-senior-inspector` | `s 34(f) — a tester shall act in accordance with the working rules the senior inspector directs` and the same for an expert (MUST); `s 34(f), s 36(d) — the party whose rule governs when the instrument of authorisation and the senior inspector's working rules conflict` (named REFUSE) |
| 35 | s.35 | encoded | `g5-testing-bodies` | `s 35 — the corporation may serve as a testing body` (exported) |
| 35(1) | s.35(1) | encoded | `g5-testing-bodies` | `s 35(1) — the corporation is incorporated and registered in Israel` |
| 35(2) | s.35(2) | encoded | `g5-testing-bodies` | `s 35(2) — the person was convicted of a disqualifying offence, or a criminal proceeding is pending on suspicion of one`; `s 35(2) — neither the corporation nor an officer or controller has a disqualifying conviction or pending proceeding`; alternatives for the proceeding (investigation counts) and for the offence (a disciplinary conviction counts) |
| 35(3) | s.35(3) | encoded | `g5-testing-bodies` | `s 35(3) — the corporation proved to the Minister's satisfaction that it employs testers in the fields and to the extent required`; alternative `s 35(3), strictly — ...` |
| 35(4) | s.35(4) | encoded | `g5-testing-bodies` | `s 35(4) — neither the corporation nor an officer or controller may be in a conflict of interest` |
| 35(5) | s.35(5) | encoded | `g5-testing-bodies` | `s 35(5) — the further conditions set in the tender or the terms of engagement, if any, are met` |
| 36 | s.36 | encoded | `g5-testing-bodies` | container: see 36(a) to (e) |
| 36(a) | s.36(a) | refused | `g5-testing-bodies` | `s 36(a) — the Minister shall authorise the person as a tester or an expert` (MUST); `s 36(a) — the person meets the conditions set by regulations under section 60(1)(c)` (named REFUSE when the caller does not say); `s 36 — the person may be authorised as a tester or an expert` (exported); `s 36 — the Minister must authorise the person as a tester or an expert`; alternative `s 36(a), read as a power — ...` (MAY) |
| 36(b) | s.36(b) | encoded | `g5-testing-bodies` | `s 36(b) — the person is barred from authorisation`; `s 36(b) — the Minister shall not authorise the person as a tester or an expert` (SHANT) |
| 36(b)(1) | s.36(b)(1) | encoded | `g5-testing-bodies` | `s 36(b)(1) — the person was convicted of a disqualifying offence, or a criminal proceeding is pending on suspicion of one` |
| 36(b)(2) | s.36(b)(2) | encoded | `g5-testing-bodies` | `s 36(b)(2) — the person may be in a conflict of interest, directly or indirectly` |
| 36(c) | s.36(c) | encoded | `g5-testing-bodies` | `s 36(c) — the Minister may refuse to authorise the person as a tester or an expert` (MAY); `s 36(c) — the Minister may refuse to authorise the person`; `s 36(c) — the Minister validly refused to authorise the person` |
| 36(d) | s.36(d) | encoded | `g5-testing-bodies` | `s 36(d) — the Minister may set conditions and instructions in the instrument of authorisation` (MAY); `s 36(d) — the Minister may change a condition or instruction he gave as to modes of action, after a written hearing` (MAY); alternative `s 36(d), reading B — ...` |
| 36(e) | s.36(e) | encoded | `g5-testing-bodies` | `s 36(e) — the last day of the authorisation`; `s 36(e) — the authorisation runs on the day` ... `under` ... (exported); period P23, alternatives `s 36(e), s 10(c) applied — ...` and `s 36(e), beginning the day after the grant — ...`; status with revocation and suspension in `g5-withdrawal`: `s 36(e), s 39 — the authorisation is in force on the day` |
| 37 | s.37 | encoded | `g5-test-conduct` | container: see 37(a), 37(b) |
| 37(a) | s.37(a) | encoded | `g5-test-conduct` | `s 37(a) — the purpose fits the capacity`; `s 37(a) — the tester or expert holds the power: ...`; `the party acting as` |
| 37(a)(1) | s.37(a)(1) | encoded | `g5-test-conduct` | `s 37(a)(1) — a tester or expert may enter a place` (MAY); `s 37(a)(1) — the tester or expert may enter the place` (exported); `s 37(a)(1) — the senior inspector has reason to suppose that unlicensed or non-conforming work is done or engaged there` |
| 37(a)(2) | s.37(a)(2) | encoded | `g5-test-conduct` | `s 37(a)(2) — a tester or expert may require a person doing work on a cooling system to give his name and address and to show identification` (MAY) |
| 37(a)(3) | s.37(a)(3) | encoded | `g5-test-conduct` | `s 37(a)(3) — a tester or expert may use a checklist` (MAY); `s 37(a)(3) — the senior inspector shall have the checklist published in Reshumot and on the Ministry website` (MUST), over `s 37(a)(3) — the checklist shall be published in Reshumot and on the Ministry website by` publisher; alternative `s 37(a)(3), publication read as a condition of use — ...` |
| 37(a)(4) | s.37(a)(4) | encoded | `g5-test-conduct` | `s 37(a)(4) — a tester or expert may receive from a person concerned the documents or information in the checklist` (MAY) |
| 37(a)(5) | s.37(a)(5) | encoded | `g5-test-conduct` | `s 37(a)(5) — a tester or expert may carry out tests on a cooling system` (MAY) |
| 37(b) | s.37(b) | encoded | `g5-test-conduct` | `s 37(b) — all the conditions of entry are met` (exported); `s 37(b) — a tester or expert shall not enter a place unless all the conditions are met` (SHANT) |
| 37(b)(1) | s.37(b)(1) | encoded | `g5-test-conduct` | `s 37(b)(1) — the tester or expert showed his instrument of authorisation to the holder of the place` |
| 37(b)(2) | s.37(b)(2) | encoded | `g5-test-conduct` | `s 37(b)(2) — the holder gave written consent to the entry, and it stands`; alternative `s 37(b)(2), withdrawal ignored — ...` |
| 37(b)(3) | s.37(b)(3) | encoded | `g5-test-conduct` | `s 37(b)(3) — before consenting the holder was told the purpose of the tests and of his rights to refuse and to withdraw consent` |
| 37(b)(4) | s.37(b)(4) | encoded | `g5-test-conduct` | `s 37(b)(4) — a dwelling is entered only at the holder's request and by prior arrangement` |
| 38 | s.38 | encoded | `g5-test-conduct` | container: see 38(a) to (c) |
| 38(a) | s.38(a) | encoded | `g5-test-conduct` | `s 38(a) — an engaged testing body shall secure the information` and `... an engaged expert shall secure the information` (MUST) over `s 38(a) — an engaged testing body or expert shall secure ..., the party bound being`; `s 38(a) — the measures secure the information: ...` |
| 38(b) | s.38(b) | encoded | `g5-test-conduct` | `s 38(b) — a testing body at the end of its engagement` and `s 38(b) — an expert at the end of his engagement` (MUST chain: hand over, destroy what remains, tell) over `s 38(b) — when the engagement ends ..., the party bound being` |
| 38(c) | s.38(c) | encoded | `g5-test-conduct` | `s 38(c) — a testing body shall not disclose or use the information`, `... a tester ...`, `... an expert ...`, `... an employee of a testing body who is not a tester ...` (SHANT) over `s 38(c) — the party shall not disclose or use information ..., the party bound being`; `s 38(c) — the disclosure or use is permitted` and its literal alternative |
| 39 | s.39 | encoded | `g5-withdrawal` | container: see 39(a), 39(b) |
| 39(a) | s.39(a) | encoded | `g5-withdrawal` | `s 39(a) — the Minister may revoke the authorisation of a tester or expert` and `... may suspend ... for a period he sets` (MAY); `s 39 — the Minister may revoke or suspend the authorisation` (exported); period P24: `s 39(a) — the last day of a suspension`, `s 39(a), s 10(c) applied — ...`, `s 39(a) — the authorisation is suspended on the day` ... |
| 39(a)(1) | s.39(a)(1) | encoded | `g5-withdrawal` | `s 39(a)(1), (4), (5) — a ground that the cure-first rule does not touch exists` (first limb) |
| 39(a)(2) | s.39(a)(2) | encoded | `g5-withdrawal` | `s 39(a)(2), (3) — a ground that the cure-first rule governs exists` (first limb) |
| 39(a)(3) | s.39(a)(3) | encoded | `g5-withdrawal` | `s 39(a)(2), (3) — a ground that the cure-first rule governs exists` (second limb) |
| 39(a)(4) | s.39(a)(4) | encoded | `g5-withdrawal` | `s 39(a)(1), (4), (5) — a ground that the cure-first rule does not touch exists` (second limb) |
| 39(a)(5) | s.39(a)(5) | encoded | `g5-withdrawal` | `s 39(a)(1), (4), (5) — a ground that the cure-first rule does not touch exists` (third limb) |
| 39(b) | s.39(b) | encoded | `g5-withdrawal` | `s 39(b) — the cure-first rule is satisfied`; `s 39(b) — a demand was made, the time directed for it has run out and it was not met`; `s 39(b) — the last day of the time directed for meeting a demand` (P25); `s 39(b) — the Minister shall not revoke the authorisation on a ground that a condition lapsed or was breached before the cure-first rule is satisfied` (SHANT); alternatives `s 39(b), s 10(c) not applied — ...` |
| 40 | s.40 | encoded | `g5-withdrawal` | `s 40 — the party has the status of a State employee for the enactment` (exported); `s 40 — the party is a tester or an expert`; `s 40 — the enactment is one of the three listed` |
| 40(1) | s.40(1) | out-of-scope | `g5-withdrawal` | constructor `the Public Service (Gifts) Law 1979` of `Enactment on which section 40 equates testers and experts with State employees`; the content of the enactment is outside the sources |
| 40(2) | s.40(2) | out-of-scope | `g5-withdrawal` | constructor `the provisions of the Penal Law about public servants`; content outside the sources |
| 40(3) | s.40(3) | out-of-scope | `g5-withdrawal` | constructor `the Public Service (Restrictions after Retirement) Law 1969`; content outside the sources |

## 1A. A defect found after the first deposit, and its repair

An independent test author found, and the lead verified, that the exported `s 30(b) — the candidate may be authorised as an inspector` answered TRUE for a person who is not an employee of the Ministry if he met s.30(b)(1) to (3).
Cause: s.30(a) draws inspectors "from among the employees of the Ministry" (and s.2 defines an inspector as such an employee), but the field `an employee of the Ministry` was read only in the guards of the s.30(a) MUST and MAY; the decision and the SHANT of s.30(b) never read it, so authorising a non-employee was neither a performance of s.30(a) nor a breach of anything.
Repair, in `g5-inspectors`: a new decision `s 30(a) — the candidate is an employee of the Ministry`, read as limb "(a)" of `s 30(b) — the candidate may be authorised as an inspector`; the SHANT `s 30(b) — the Minister shall authorise as an inspector only a person who satisfies all three conditions` is guarded by that decision, so it now catches a non-employee, and its breach reason says so.
The comment above the decision says why (b) alone does not carry the employee test: (a) says who the inspectors are drawn from, (b) which of them.
No exported name or signature changed (the function keeps its name and its single parameter, `candidate`); the text of its `@export` description and of its parameter `@desc` changed to say that a non-employee is never answered TRUE.
The old reading is nowhere kept as a default; the only other readers of the field are the MUST and MAY guards of s.30(a), which are unchanged.
New tests in `g5-tests-inspectors`: the employee decision (employee TRUE, non-employee FALSE); the s.30(b) decision TRUE for an employee who meets all three conditions and FALSE for a non-employee who meets them; the three limbs (b)(1) to (3) answered TRUE for that non-employee, to show that it is only the employee limb that bars him; the existing FALSE assertions for an employee failing each of (b)(1), (2) and (3); and the trace `s 30(b) — the Minister shall authorise as an inspector only ...` with `the authorisation of a non-employee`, which ends in a breach by the Minister.
Two mutations (dropping the employee limb from the decision, and making the employee decision always TRUE) are caught by those tests.

## 2. Forks

Each fork gives the readings, the one taken, the text that licenses each, and the callable alternative with its test.
"Assumed, not ruled" applies to every choice below: the owner has not ruled on any of them.
The tests named are in the tests module of the same section; the numbered assertions are in `g5-tests-red`, which asserts, of the reading taken, the answer the other reading gives, so that each fails.

### 2.1 Forks on who does what

**F-DUTY (ss.30(a), 34(a), 36(a)): "the Minister will authorise" is a duty or a power.**
Reading taken: a duty to authorise (MUST).
Text for it: the verb is in the future tense, where this Subchapter says "may" for discretion (ss.36(c), 36(d), 39(a)); s.36(c) allows a refusal "even if the conditions of (a) are met", which presupposes that otherwise he must authorise; the slice glosses ss.30(a) and 34(a) as "must".
Text for the other: authorising inspectors is an appointment, and ruling 2 of the brief lists "to appoint" among powers (MAY).
Alternatives, callable: `s 30(a), read as a power — ...`, `s 34(a), read as a power — ...`, `s 36(a), read as a power — ...`.
Tests: traces in `g5-tests-inspectors`, `g5-tests-senior-inspector`, `g5-tests-testing-bodies`.
Effect: none is a breach either way, since no time is stated; the duty reading leaves an open obligation, the power reading a standing permission.

**F-ACTOR (ss.30(c), 34(c), 37(a)(3)): the text names no actor.**
Section 30(c) says notice "will be published" in Reshumot, s.34(c) that an engagement "will be made under" the Mandatory Tenders Law, and s.37(a)(3) that the checklist "will be published" in Reshumot and on the Ministry website.
Inferred and taken: the Minister (s.30(c), who made the authorisation), the Ministry (s.34(c), the State acting through the Minister's office), the senior inspector (s.37(a)(3), who sets the checklist under s.33 def.7).
Alternatives, callable: each rule takes the party, so `s 30(c) — notice ... by` publisher, `s 37(a)(3) — the checklist shall be published ... by` publisher and `s 34(c) — a testing body or an expert shall be engaged ..., the party engaging being` engager are the other inference.
Tests: a trace with `the Ministry` as publisher and one with `the Minister` as engager.
Publication has no stated consequence: nothing in ss.30 to 32 makes it a condition of the authorisation's effect, and none is added (see F-PUBLISH for the checklist).

**F-COMPLY (s.31(2) with Third Schedule item (7)): is there a duty to comply with a demand.**
Section 31(2) says only that the inspector may "require"; item (7) prices "not giving a document on an inspector's demand under s.31(2)".
Reading taken: a duty on `a person` to give what was lawfully demanded, arising only on a demand the inspector could lawfully make, with no time limit because the text states none.
The other reading: no duty beyond the sanction; there is no callable alternative because the duty is a MUST on top of the rest, which needs none of it.

**F-REASON (s.31(3), s.37(a)(1)): whose belief, and what it depends on.**
The inspector's "reason to suppose" (s.31(3)) and the senior inspector's (s.37(a)(1)) are different belief-holders, each an input per limb (the worker; the engager).
The truth of the suspicion is not asked, so the licence status of the people there (integration points IP1, IP4) is not consumed by this group.
No alternative: it would need facts that other groups decide.

### 2.2 Forks on the conditions

**F-OFFENCE (ss.30(b)(1), 35(2), 36(b)(1)): "offence" is bare.**
Sections 6(a)(3), 21 and 23 say "criminal offence" or "disciplinary offence" (lines 87, 180, 190 of `law.wiki`); these three say only "offence".
Reading taken: a criminal offence only.
Alternatives, callable: `s 30(b)(1), counting a conviction for a disciplinary offence too` and `s 35(2), counting a conviction for a disciplinary offence too — ...` (s.36(b)(1) calls the s.35(2) function).
Tests: `a disciplinary convict the Minister finds unfit` in `g5-tests-inspectors`, `a disqualifying disciplinary conviction` in `g5-tests-testing-bodies`; red assertion 3.

**F-PROCEEDING (ss.35(2), 36(b)(1)): a "criminal proceeding on suspicion of an offence".**
Reading taken: a pending indictment, the domain's `charged with a criminal offence and no final judgment yet`.
The other reading: a criminal investigation counts, because the text says "on suspicion".
Alternatives, callable: `s 35(2), a criminal investigation counting as a proceeding — ...`, at person level and for the whole corporation.
Tests: `an investigation for a disqualifying offence` and `a corporation with an officer under investigation` in `g5-tests-testing-bodies`; red assertion 8.
Nouns request: the domain's `Record of offences` has no field for it.

**F-JUDGE (s.35(2)): whose judgement is "unfit".**
Sections 30(b)(1) and 36(b)(1) say "in the Minister's opinion"; s.35(2) does not.
Taken: the Minister's, an input (`a conviction is for an offence that makes the person unfit`).
There is no different function for another judge, only another supplier of the input, so no alternative is callable; it is an open question for an expert (section 7).

**F-NONE-DIRECTED (ss.30(b)(3), 35(5)): "as the Minister directed", "if set".**
The input is a `MAYBE BOOLEAN`: `NOTHING` is "none directed or set", which leaves nothing to meet, so the limb holds; `JUST` says whether what was directed or set is met.
Section 35(5) names the absent case ("if set"); s.30(b)(3) does not, and is read the same way.
The other reading (no direction means the condition is unmet) is the input `JUST FALSE`.
Tests: the three states in both sections.

**F-DEMAND (s.32(2)): the certificate "which he will show on demand".**
Reading B, taken: the showing is part of limb (2), so an inspector whose certificate was demanded and not shown does not meet it and may not use his powers.
Reading A: limb (2) is satisfied by holding the certificate, and showing it on demand is a separate duty.
Text for B: "on demand" is a relative clause inside condition (2), and the conditions are introduced by "both of these"; the purpose of the certificate is to let the person inspected verify the authority.
Text for A: the verb is a future-tense command ("will show"), which reads as a duty rather than as a condition.
Both readings keep the duty to show (`s 32(2) — an inspector whose certificate is demanded shall show it`, a MUST).
Alternative, callable: `s 32, reading A — ...`.
Tests: `g5-tests-inspectors`, section `s 32`; red assertion 1.
B is taken partly because it narrows liability under the financial sanction of item (7).

**F-ITEM7 (s.31(2) with s.32 and Third Schedule item (7)): is a demand by an inspector who fails s.32 a demand "given under s.31(2)".**
Reading taken: no; the demand counts for item (7) only if the inspector could lawfully make it, s.32 included.
Reading 2: any demand by an authorised inspector for a document that serves the Law counts; s.32 is a separate prohibition on the inspector.
Alternative, callable: `s 31(2), s 32 ignored — a document was demanded`.
Tests: `g5-tests-inspectors`, section `s 31(2) and Third Schedule item (7)`; red assertion 2.
Item (7) says "document", not "information": a demand for information alone is lawful and binds, and is not item (7)'s (tested).

**F-WITHDRAW (s.37(b)(2), (3)): consent the occupier withdrew.**
Section 37(b)(3) gives the occupier a right to withdraw consent until the tests begin.
Reading taken: a consent withdrawn before the tests began no longer stands.
The other reading: the consent was "given", which is all (b)(2) asks.
Alternatives, callable: `s 37(b)(2), withdrawal ignored — ...`, `s 37(b), withdrawal ignored — ...`, `s 37(a)(1), withdrawal ignored — ...`.
Tests: `g5-tests-test-conduct`; red assertion 12.

**F-PUBLISH (s.37(a)(3)): is publication of the checklist a condition of using it.**
Reading taken: no, a duty only (the second clause is a free-standing command, and the consequence of not publishing is unstated).
The other reading: an unpublished checklist cannot be used.
Alternative, callable: `s 37(a)(3), publication read as a condition of use — ...`.
Tests: `g5-tests-test-conduct`; red assertion 13.

**F-CHANGE (s.36(d)): the scope of the power to change.**
The power to set covers "modes of action and work procedures", the power to change only what he gave "as to modes of action", and only after a written hearing; setting needs no hearing.
Reading A, taken: the change power is narrower than the setting power.
Reading B: it covers both kinds.
Alternatives, callable: `s 36(d), reading B — ...` (a function and a rule).
Tests: `g5-tests-testing-bodies`; red assertion 9.

**F-GROUNDS (s.39(a), (b)): which grounds are "under (a)(2) or (3)".**
Reading taken: section 39(b) bars only a revocation or suspension resting on (a)(2) or (3); where (a)(1), (4) or (5) also exists the Minister can act under it without a demand.
The other reading: the cure-first rule applies whenever (a)(2) or (3) is among the grounds present.
Alternative, callable: `s 39, the cure-first rule applying whenever (a)(2) or (3) exists — ...`.
Discriminating case: a lapsed condition and a poor professional level, no demand.
Tests: `g5-tests-withdrawal`; red assertion 19.

**F-OVERLAP (s.33 defs 2 and 5): a tester who is also an expert.**
See contradiction C1 in section 6.
Reading taken: the definitions literally, so an employee authorised only to test is both a tester and an expert.
Alternative, callable: `s 33 def 5, an employee authorised only to test being a tester and not an expert — ...`.
Tests: `g5-tests-senior-inspector`; red assertion 6.

**F-LOOP (s.35(3), s.33 defs 2 and 4): the circularity.**
See contradiction C2.
Reading taken: "testers" in s.35(3) are persons who hold the s.36 authorisation to test, whatever their employer's status.
Alternative, callable: `s 35(3), strictly — ...`, which no corporation that is not yet a testing body can meet.
Tests: `g5-tests-testing-bodies`; red assertion 7.

**F-DISCLOSE (s.38(c) with ss.34(d), (e), 38(b)): the exception "except to carry out the act".**
See contradiction C3.
Reading taken: a disclosure the Law itself orders (the reports of s.34(d) and (e), the hand-over of s.38(b)) is not caught.
Alternative, callable: `s 38(c), literally — the disclosure or use is permitted`.
Tests: `g5-tests-test-conduct`; red assertion 18.

**F-OVERLAP-RULES (s.34(f) with s.36(d)): two sources of operating rules.**
See contradiction C4.
The sources do not say which prevails, so the answer is a named refusal: `s 34(f), s 36(d) — the party whose rule governs when the instrument of authorisation and the senior inspector's working rules conflict`.
Test: `#ASSERT REFUSED ... BECAUSE` in `g5-tests-senior-inspector`.

**F-COMMENCE (s.63(a), integration point IP2): the powers are used only where the Law has commenced for the work.**
The commencement of the Law is "for the work on a system", by refrigerant, so the powers "to supervise implementation of the Law's provisions" are read as used only for work the Law has reached.
The input is a field on `An inspector at work` and on `Tester or expert at work`: `the Law has commenced for the work on the system being supervised` and `... being tested`; G7's function sets it.
The authorising of inspectors, senior inspectors, testing bodies and testers is not tied to it.
There is no separate alternative: with the field TRUE the powers are independent of commencement.
Tests: `g5-tests-inspectors`, section `s 63(a) and IP2`; `g5-tests-test-conduct`.

### 2.3 Forks on periods

IL s.10 below is the Interpretation Law, s.10; "(c)" is its subsection (c), not the Law's own s.10(c).
Kinds met in this group: D (a deadline for doing something) once, V (a period of validity or duration) three times, X (a length an official fixes) four times; kinds C and W are not met in ss.30 to 40.
In each the length is an official's, so it is an input, stated as a number of days, months or years counted from a day, or as a last day.
A last day is a date, not a counted period, so IL s.10(c) never moves it.
Counted days go through IL s.10(a), counted months and years through IL s.10(b), from the module `il-interpretation-time`; no module of mine adds days or months to a date.

| id | period | provision | kind | IL s.10(c) | alternative, callable | tests |
| --- | --- | --- | --- | --- | --- | --- |
| F-P22 | the period an inspector directs for keeping measurements and tests | s.31(4) | X, read as V (a duration) | not applied | `s 31(4), s 10(c) applied — the last day of the period for keeping directed on` | `g5-tests-inspectors` section `s 31(4) -- the period ...`; red 4 |
| F-P23 | the period of an authorisation of a tester or expert | s.36(e) | X, V | not applied | `s 36(e), s 10(c) applied — the last day of the authorisation` | `g5-tests-testing-bodies` section `s 36(e)`; red 10 |
| F-P24 | the period of a suspension | s.39(a) | X, V | not applied | `s 39(a), s 10(c) applied — the last day of a suspension` | `g5-tests-withdrawal` section `s 39(a) -- the period of a suspension`; red 14 |
| F-P25 | the time the Minister directs for meeting a demand | s.39(b) | X, D | applied | `s 39(b), s 10(c) not applied — ...` (a function for each of the three steps and the whole decision) | `g5-tests-withdrawal`; red 16 |

Reasons: a period of validity or a duration is not a time for doing something, and IL s.10(c) moves the end of a time for doing something (the brief's ruling 4); a cure period is a deadline for the person to act, so (c) is applied.
The discriminating cases: a nominal last day that falls on a rest day (30 days from Thursday 2026-01-01 ends on Saturday 2026-01-31; with that day a rest day the (c) reading ends on Sunday 2026-02-01, or on 2026-02-02 if 1 February is a rest day too; and a cure period of 14 days from Monday 2026-03-02 ends on Monday 2026-03-16, which if a rest day moves the last day to 17 March, so the Minister may act from 18 March, against 17 March without (c)).
The calendars in the tests are illustrations and say nothing about any calendar.
The calendar is an input in every exported function (`Calendar of rest days`, passed through `days of rest, recess or holiday listed in`).

**F-START (P22, P23, P24): is the day the period runs from a day of the period.**
Reading taken: yes; IL s.10(a) leaves the first day out of the COUNT ("that day is not counted"), not out of the period, so an authorisation granted on a day is in force on that day, a suspension begun on a day suspends that day, and a retention directed on a day covers it.
The other reading: the period begins the day after.
This departs from the vendored module `il-interpretation-time`: its own fork F6 takes "the first day of every period is the day after D", and its `s 10 — the date x is inside a period of ... from/after d` functions start at d+1.
So G5's "in force on the day it was granted" will disagree with any group that answers the same shape through the module's `is inside` functions.
G5 does not call those functions for these three periods because the question is when a status begins, which IL s.10 does not speak to; the module's function for the last day (`s 10(a) — the last day of ...`, `s 10 — ... months from the day`) is called, and agrees.
Alternatives, callable: `s 31(4), beginning the day after the direction — ...`, `s 36(e), beginning the day after the grant — ...`, `s 39(a), beginning the day after — ...`; they start at the module's own `s 10 — the first day of a period counted from or after an event on`.
Tests and red assertions 5, 11, 15.

**F-STATUS-DAY (the status equation of ss.36(e) and 39): the day of a revocation, the day a suspension begins.**
The Law states no status rule; `s 36(e), s 39 — the authorisation is in force on the day` is the one the two sections imply, and is mine.
Reading taken: not in force on the day of a revocation or from the day a suspension begins.
Alternative, callable: `s 36(e), s 39, a revocation or suspension taking effect the day after it is made — ...`.
Test and red assertion 17.

**What I did not model.**
Periods counted backwards: none is met in ss.30 to 40.
A period with no end ("keeps for a period he directs" with no period stated): the input is required; there is no default.
For s.36(e) an instrument that fixes no period is a named refusal, `the instrument of authorisation fixes no period, and s 36(e) gives no default`.

## 3. Answer table: headline scenarios

Every row was decided from the Hebrew before the encoding was run; the module and test file are the evidence.

| scenario | answer | section | evidence |
| --- | --- | --- | --- |
| Inspector, authorised, on duty, badge worn, certificate held and not demanded, demands from a person concerned a document that serves the Law, and the document is not given | a lawful demand; the violation of item (7) is made | ss.31(2), 32, Third Schedule (7) | `g5-tests-inspectors` |
| The same, but the inspector wears no badge | not lawful; no item (7) violation (reading taken); a document demanded on the alternative | ss.31(2), 32 | `g5-tests-inspectors`; red 2 |
| The same, but the certificate was demanded and not shown | not lawful on reading B; lawful on reading A | s.32(2) | `g5-tests-inspectors`; red 1 |
| The same, but what was demanded is information, not a document | a lawful demand and a duty to comply, but not item (7)'s | ss.31(2), Third Schedule (7) | `g5-tests-inspectors` |
| Inspector enters a workshop where he has reason to suppose unlicensed work; no consent, no court order | may enter | s.31(3) | `g5-tests-inspectors` |
| A tester or expert enters the same place with no written consent | may not | s.37(b)(2) | `g5-tests-entry` |
| Inspector enters a dwelling on a court order alone | may enter | s.31(3) proviso | `g5-tests-entry` |
| A tester or expert enters a dwelling on a court order alone | may not: no court-order route | s.37(b) | `g5-tests-entry` |
| Inspector enters a dwelling on the holder's consent in no particular form | may enter | s.31(3) proviso | `g5-tests-entry` |
| A tester or expert enters a dwelling with oral consent, or with written consent but no request from the holder | may not | s.37(b)(2), (4) | `g5-tests-entry`, `g5-tests-test-conduct` |
| Candidate employee convicted of an offence the Minister finds unfit | may not be authorised as an inspector | s.30(b)(1) | `g5-tests-inspectors` |
| Candidate who is not an employee of the Ministry but meets s.30(b)(1) to (3) | may not be authorised as an inspector; authorising him is a breach by the Minister | ss.30(a), (b) | `g5-tests-inspectors` |
| Candidate with only a pending indictment | may be authorised as an inspector (no pending-proceedings limb) | s.30(b)(1) | `g5-tests-inspectors` |
| Corporation incorporated and registered in Israel, clean, proved, no conflict, no further tender conditions | may serve as a testing body | s.35 | `g5-tests-testing-bodies` |
| The same with an officer convicted, or a controller facing a proceeding | may not | s.35(2) | `g5-tests-testing-bodies` |
| The same with an officer under criminal investigation only | may serve (taken); may not on the broader reading | s.35(2) | `g5-tests-testing-bodies`; red 8 |
| Person with a disqualifying conviction, regulations of s.60(1)(c) not stated by the caller | may not be authorised (FALSE, answered before the regulations are asked) | s.36(b) | `g5-tests-testing-bodies` |
| Clean person, regulations not stated | refused: no regulations under s.60(1)(c) are in the sources | s.36(a) | `g5-tests-testing-bodies` |
| Clean person, regulations stated as met, no refusal | may be authorised, and the Minister must | s.36(a) | `g5-tests-testing-bodies` |
| The Minister refused without reasons, or without a written hearing, or without finding unfitting circumstances | not a refusal under s.36(c); the duty to authorise stands | s.36(c) | `g5-tests-testing-bodies` |
| A change to a work-procedures condition after a hearing | not allowed (reading A); allowed (B) | s.36(d) | `g5-tests-testing-bodies`; red 9 |
| Authorisation granted Thursday 2026-01-01 for 30 days | last day 2026-01-31; in force on 2026-01-01 and 2026-01-31, not on 2025-12-31 or 2026-02-01 | s.36(e) | `g5-tests-testing-bodies` |
| One month from 2025-01-31, one year from 2024-02-29 | last day 2025-02-28 in both | s.36(e), IL s.10(b) | `g5-tests-testing-bodies` |
| Revocation for a lapsed condition (a)(2) with no demand | may not | s.39(b) | `g5-tests-withdrawal` |
| The same with a demand on Monday 2026-03-02 for 14 days, not met | last day 2026-03-16; may not act on 2026-03-16, may from 2026-03-17 | s.39(b) | `g5-tests-withdrawal` |
| The same with Monday 2026-03-16 a rest day | may act from 2026-03-18 (taken, IL s.10(c) applied); from 2026-03-17 without it | s.39(b), IL s.10(c) | `g5-tests-withdrawal`; red 16 |
| A lapsed condition that cannot be met, no demand | may act (hearing given) | s.39(b) | `g5-tests-withdrawal` |
| A lapsed condition and a poor professional level, no demand | may act under (a)(5) (taken); may not on the stricter reading | s.39(a)(5), (b) | `g5-tests-withdrawal`; red 19 |
| Suspension begun 2026-01-01 for 30 days | suspended 2026-01-01 to 2026-01-31 | s.39(a) | `g5-tests-withdrawal` |
| A tester, an expert, a testing body: State-employee status for the Gifts Law, the Penal Law's provisions on public servants, the Retirement Restrictions Law | tester and expert: yes, for the three; testing body: no; any other enactment: no | s.40 | `g5-tests-withdrawal` |

## 4. Nouns requests, for the INTEGRATOR

Each noun below was missing from `domain.l4` and is stood in for locally, as the brief's ruling 6 says.

1. Domain `Party`: a constructor `an employee of a testing body` (s.38(c), "its employees, including a tester"). Stand-in: `a person`, guarded by a boolean saying the person is such an employee, in `s 38(c) — an employee of a testing body who is not a tester shall not disclose or use the information`.
2. Domain `Record of offences`: a field `a criminal proceeding or investigation is under way on suspicion of an offence` (ss.35(2), 36(b)(1), "criminal proceeding on suspicion"). Stand-in: the field `a criminal investigation on suspicion of an offence is under way` of the local `Standing as to offences (ss 35 and 36)`, read only by the broader reading.
3. A shared noun for "a period as an official states it": a number of days, months or years, or a last day. G5 declares three copies with module-specific constructor names because the modules may not import each other: `Period an inspector directs for keeping measurements and tests`, `Period fixed in an instrument of authorisation`, `Period fixed by the Minister`.
4. A shared noun for an authorisation under s.36 and its facts (`Person who may be a tester or an expert`, `Instrument of authorisation under section 36(e)`, `Authorisation of a tester or an expert as recorded`), which G4 may also need for the Council.
5. A shared noun for the standing of a person as to offences, with the Minister's judgement (`Standing as to offences (ss 35 and 36)`, `Candidate for authorisation as an inspector`).

## 5. Inputs consumed and functions exported, for wiring

### 5.1 Integration points

| id | what | how this group takes or gives it |
| --- | --- | --- |
| IP1 | a licence is in force | not consumed: s.31(3) asks for the inspector's reason to suppose (an input per limb), not for the truth of it |
| IP2 | the Law has commenced for the work on the system | fields `the Law has commenced for the work on the system being supervised` (`An inspector at work`) and `... being tested` (`Tester or expert at work`) |
| IP4 | work on a cooling system; the place | not consumed, for the same reason as IP1 |
| IP9 | a violation of a listed provision occurred | export `the violation committed under s.31(2), if any`, returning a `MAYBE Violation` for item (7) |
| IP10 | an inspector's demand for a document under s.31(2) was lawfully made | export `the inspector's demand for a document under s.31(2) was lawfully made`; G6's input `a document was demanded under s.31(2)` is wired to it (the function's name differs so as not to clash with that input) |
| IP14 | no order or regulation changes a Schedule; no regulation under ss.46, 60(1), 60(2) | stated here for s.36(a) only: the input `meets the conditions set by regulations under section 60(1)(c), if the caller says` is a `MAYBE`, and `NOTHING` is a named refusal; the Minister's directions (ss.30(b)(2), (3), 35(5), 36(d), the checklist, the working rules) are inputs and no content is assumed |
| IP15 | days of rest, recess and holiday | `Calendar of rest days` is a parameter of every exported function that counts a period and of its (c) alternative |

### 5.2 Wiring inside G5

| from | to |
| --- | --- |
| `s 35 — the corporation may serve as a testing body` (`g5-testing-bodies`) | field `meets the conditions of section 35` of `Corporation under section 33` (`g5-senior-inspector`) |
| `s 33 def 6 — the subject is in a conflict of interest` (`g5-senior-inspector`) | the judgement `may be in a conflict of interest, directly or indirectly` of ss.35(4), 36(b)(2) (`g5-testing-bodies`); s.35(4) and s.36(b)(2) say "may be", a likelihood, so def.6 informs the input and does not replace it |
| `s 36(e), s 39 — the authorisation is in force on the day` (`g5-withdrawal`) | field `holds an authorisation under section 36 that is in force` of `Tester or expert at work` (`g5-test-conduct`); and the s.36 authorisation facts of `Person who may be a tester or an expert` (`g5-senior-inspector`) |
| `s 36(e) — the last day of the authorisation` (`g5-testing-bodies`) | field `the last day of the period fixed in the instrument` of `Authorisation of a tester or an expert as recorded` (`g5-withdrawal`) |
| the fact that an engagement was made under the Mandatory Tenders Law | fields `made in accordance with the Mandatory Tenders Law` (`g5-senior-inspector`) and `made in accordance with section 34(c)` (`g5-test-conduct`): one source, two fields |
| `s 33 def 2 — the person is a tester` and `def 5 — ... an expert` | the capacity of `Tester or expert at work` and the performer of an auxiliary test |
| G4's s.29(a) definitions of "family member" and "relative" of a Council member | not imported: s.33 def.3 carries them with the subject changed, and `g5-senior-inspector` has its own copies under other names |

### 5.3 Exported functions (`@export`)

`s 30(b) — the candidate may be authorised as an inspector` (candidate).
`the inspector may use the power` (the inspector at work, the power).
`s 31(3) — the inspector may enter the place` (the inspector, the place).
`the inspector's demand for a document under s.31(2) was lawfully made` (the inspector, the demand).
`the violation committed under s.31(2), if any` (the inspector, the demand, the violator, a reference, the day of the act, whether the document was not given).
`s 33 def 2 — the person is a tester`, `s 33 def 5 — the person is an expert`, `s 33 def 6 — the subject is in a conflict of interest`.
`s 35 — the corporation may serve as a testing body` (the corporation).
`s 36 — the person may be authorised as a tester or an expert` (the person; a refusal unless the caller states whether the regulations' conditions are met).
`s 36(e) — the authorisation runs on the day` (the day, the instrument).
`s 37(b) — all the conditions of entry are met` (the entry).
`s 37(a)(1) — the tester or expert may enter the place` (the tester or expert, the entry).
`s 39 — the Minister may revoke or suspend the authorisation` (the case, the decision day, the calendar).
`s 36(e), s 39 — the authorisation is in force on the day` (the day, the authorisation as recorded).
`s 40 — the party has the status of a State employee for the enactment` (the party, the enactment).
The names differ from the slice's suggestions: `the entry is permitted` became the two s.31(3) and s.37(a)(1) functions above, and `a document was demanded under s.31(2)` became the IP10 function above.
The regulative rules are not exported; each is named for its section and its party (`s 31(1) — an inspector may require ...`, `s 36(b) — the Minister shall not authorise ...`).

## 6. Contradictions and inconsistencies in the source

Found in a separate pass after encoding, reading ss.30 to 40 against each other, against the definitions of s.2 and s.29(a), and against Third Schedule item (7).
Each gives the provisions, the case that discriminates, and the callable readings.

**C1. Tester and expert overlap (s.33 defs 2 and 5).**
A tester is an employee of a testing body authorised under s.36 to do auxiliary tests (def.2); an expert is an employee of a testing body, or an engaged person, authorised under s.36 "to do auxiliary tests or to give expert opinions, as the case may be" (def.5).
Discriminating case: an employee authorised only to test is both; so s.34(e), which binds "an expert employed by a testing body" to report and give an opinion, binds every such tester to give an opinion too.
Callable: the literal `s 33 def 5 — the person is an expert`, and `s 33 def 5, an employee authorised only to test being a tester and not an expert — ...`.

**C2. The testing body that cannot exist (s.35(3), s.33 defs 2 and 4).**
A testing body must have proved that it employs "testers" (s.35(3)); a tester is an employee "of a testing body" (def.2); a testing body is a corporation that meets s.35 (def.4).
Discriminating case: a corporation that is not yet a testing body employs no tester by the definitions, so cannot meet s.35(3), so can never become one.
Callable: `s 35(3), strictly — ...` (always FALSE for a corporation not yet a testing body) against `s 35(3) — ...` (taken).

**C3. The confidentiality exception against the Law's own disclosures (s.38(c), ss.34(d), (e), 38(b)).**
Section 38(c) forbids disclosing or using information obtained in an act under the engagement "except to carry out the act".
Section 34(d) and (e) order reports of each test to the senior inspector, and s.38(b) orders the whole hand-over of the information at the end, which are disclosures of that information and are not, in terms, carrying out the act.
Discriminating case: the hand-over at the end of an engagement.
Callable: `s 38(c) — the disclosure or use is permitted` (a required disclosure is permitted) against `s 38(c), literally — ...`.

**C4. Two sources of working rules, no priority (s.34(f), s.36(d)).**
The senior inspector directs "working rules" for testers and experts (s.34(f)); the Minister gives "conditions and instructions as to modes of action and work procedures" in the instrument of authorisation (s.36(d)).
Discriminating case: an instrument condition and a working rule that conflict.
The Law is silent: `s 34(f), s 36(d) — the party whose rule governs ...` is a named refusal.

**C5. The power to set against the power to change (s.36(d)).**
The Minister may set conditions "as to modes of action and work procedures", but may change only what he gave "as to modes of action", and only after a written hearing.
Discriminating case: a change to a work-procedures condition after a hearing.
Callable: reading A (taken) against `s 36(d), reading B — ...`.

**C6. Three standards of fitness (ss.30(b)(1), 35(2), 36(b)(1)).**
The judge is the Minister in ss.30(b)(1) and 36(b)(1) and unstated in s.35(2); only ss.35(2) and 36(b)(1) have a pending-proceedings limb; the word "offence" is bare in all three (F-OFFENCE).
Discriminating case: a person with an indictment pending for a serious offence may be authorised as an inspector (s.30(b)(1)) and may not be authorised as a tester or expert (s.36(b)(1)).
Both outcomes are asserted: `a candidate with a pending indictment` in `g5-tests-inspectors`, `an applicant under a pending proceeding` in `g5-tests-testing-bodies`.

**C7. Information against document (s.31(2), Third Schedule item (7)).**
Section 31(2) covers information or a document; item (7) prices only a document.
Discriminating case: a person who refuses to give oral information to an inspector who lawfully demanded it breaks s.31(2) and commits no listed violation.
Section 31(1) (name and address) and s.31(3) (entry) are not priced at all.
Callable: not a reading difference; `s 31(2) — the thing is a document, which includes computer output` separates the two, and the tests assert both.

**C8. Entry by an inspector against entry by a tester or expert (ss.31(3), 37(a)(1), 37(b)).**
The belief is the inspector's in s.31(3) and the senior inspector's in s.37(a)(1); an inspector needs no consent for a place that is not a dwelling, and for a dwelling needs a court order or the holder's consent in no form; a tester or expert needs written consent after an explanation, shows his instrument, and for a dwelling enters only at the holder's request by prior arrangement, with no court-order route (trap T30).
A tester or expert also has no identification duty for his other powers, where s.32 asks an inspector for a badge and a certificate for all of his.
Tests: `g5-tests-entry` (ten assertions).

**C9. The expert employed by a testing body (ss.34(e), 38(a), 38(c)).**
Section 34(e) binds an expert "engaged under (c) or employed by a testing body"; s.38(a) binds only a body or expert "with whom an engagement was made under (c)"; s.38(c) binds "an expert" with no such qualifier.
Discriminating case: an expert employed by an engaged testing body, with no engagement of his own: s.34(e) binds him, s.38(a) does not, s.38(c) does.
Tests: `g5-tests-senior-inspector` (`an expert employed by a testing body, not himself engaged`), `g5-tests-test-conduct` (the s.38(a) engagement not made, and s.38(c)).

**C10. Redundancy in s.37(b).**
For a dwelling, (b)(2) already requires the holder's written consent and (b)(4) requires his request and prior arrangement; the request implies the consent.
Not a contradiction: all four limbs are required ("all of these"), and the tests treat them as independent.

**C11. Reasons for refusal, none for revocation (ss.36(c), 39).**
The Minister must give reasons for refusing to authorise (s.36(c)) and must hear the person in writing, but s.39(a) requires only the written hearing before revoking or suspending.
Observation; the encoding requires no reasons for revocation.

**C12. "Family member" of a corporation (s.33 def.3).**
Section 33 carries s.29(a)'s definitions over "with the necessary changes" to a tester, an expert, a testing body and its officers and controllers.
A corporation has no spouse or parent, so for a testing body the definitions can only work through its officers and controllers.
`s 33 def 3 — ... of the subject` is one function for any subject; the subject's identity is the caller's.

**C13. A circular pointer (s.33 def.7, s.37(a)(3)).**
"Checklist" is defined as a list set "as stated in s.37(a)(3)", which uses the defined term.
Harmless: the two agree.

## 7. Open questions for a domain expert

1. Is s.30(a)'s "will authorise" a duty, as taken, or a power (F-DUTY)?
2. Does s.32(2)'s "which he will show on demand" condition the use of the powers, as taken, or only add a duty (F-DEMAND)?
3. Is a demand made by an inspector who lacks the badge or the certificate a demand "under s.31(2)" for item (7) (F-ITEM7)?
4. Does "offence" in ss.30(b)(1), 35(2) and 36(b)(1) include a disciplinary offence (F-OFFENCE)?
5. Does "criminal proceeding on suspicion" in ss.35(2) and 36(b)(1) include an investigation (F-PROCEEDING), and whose judgement is "unfit" in s.35(2) (F-JUDGE)?
6. Does withdrawal of consent under s.37(b)(3) end the consent for s.37(b)(2) (F-WITHDRAW)?
7. Does an unpublished checklist bind (F-PUBLISH), and who must publish it, and notice of an inspector's authorisation (F-ACTOR)?
8. Which prevails, the Minister's instrument or the senior inspector's working rules (C4)?
9. Is the power to change conditions in s.36(d) confined to modes of action (C5)?
10. Is an employee authorised only to test an expert as well (C1), and how can a first testing body arise (C2)?
11. May the hand-over at the end of an engagement be made under s.38(c) (C3)?
12. Does the cure-first rule of s.39(b) apply when a ground other than (a)(2) or (3) is also present (F-GROUNDS)?
13. Does s.10(c) of the Interpretation Law move the end of a period an official fixes: a suspension, an authorisation, a keeping period, a cure period (F-P22 to F-P25)?
14. Do authorisations, revocations and suspensions take effect on the day made or the day after (F-START, F-STATUS-DAY)?
15. Is there a duty to comply with a demand for information under s.31(2) beyond the sanction of item (7), and when must compliance be made (F-COMPLY)?

## 8. What the sources do not answer

Each of these is an input or a named refusal in the encoding; none gets a default.

1. The regulations under s.60(1)(c): the conditions for testers and experts (education, experience, specialisation, training). A named refusal unless the caller states whether a person meets them.
2. The Mandatory Tenders Law: whether an engagement was made under it is an input.
3. The Securities Law's "interested party" and the Computers Law's "output": inputs (`a corporation in which ... is an interested party`; `computer output as defined in the Computers Law`).
4. The Minister's directions: the training and further conditions of s.30(b)(2), (3), the conditions and instructions of s.36(d), the period of an authorisation (s.36(e)), the Minister's opinions of fitness and his finding of unfitting circumstances.
5. Time limits: for compliance with a demand under s.31(2); for the reports of s.34(d), (e); for the three steps of s.38(b); for the publication of notice of an authorisation and of the checklist.
6. Who must keep measurements and tests that an inspector orders kept (s.31(4)), and what follows from failing to keep them.
7. What happens when an authorisation's period ends: nothing in the sources provides for renewal or extension.
8. The effect of non-publication of an inspector's authorisation or of the checklist.
9. Which prevails when the instrument and the working rules conflict (C4).
10. The days of rest, recess and holiday for any year; the identity of the Minister's opinions; the content of the enactments of s.40.
11. How a family member or relative of a corporation is defined (C12).
12. Whether s.10(c) of the Interpretation Law reaches a period an official fixes (section 2.3).

## 9. What the check script prints

`work/g5/check.sh` is the skill's `assets/check.sh` with the glob changed to `g5-*.l4`, the count expected for `g5-tests-red.l4` set to 19, and five extra checks appended (the first line of each module is `@lang en`, `l4 run` prints no Warning and no stray `@ref`, `srcrefs.py check --refs` over every module, the sha256 of the time module, and `tracecheck.py`).
`tracecheck.py` compares the result of each `#TRACE` with the `-- EXPECT:` comment above it, because a DEONTIC cannot be compared in `#ASSERT` and so check.sh counts nothing for a trace.
`mut.py` applies one change at a time to a scratch copy of the modules and requires some test to notice; the mutations tried and their results are in section 10.

```text
module                                    errors satisfied  failed  refused  expected
g5-inspectors.l4                               0         0       0        0         0
g5-senior-inspector.l4                         0         0       0        0         0
g5-test-conduct.l4                             0         0       0        0         0
g5-testing-bodies.l4                           0         0       0        0         0
g5-tests-entry.l4                              0        10       0        0         0
g5-tests-inspectors.l4                         0       145       0        0         0
g5-tests-red.l4                               19         0      19        0        19
g5-tests-senior-inspector.l4                   0        82       0        0         0
g5-tests-test-conduct.l4                       0        84       0        0         0
g5-tests-testing-bodies.l4                     0       125       0        0         0
g5-tests-withdrawal.l4                         0        98       0        0         0
g5-withdrawal.l4                               0         0       0        0         0
TOTAL (12 modules)                            19       544      19        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)

extra checks (ENCODER G5)
  all g5 modules start with '@lang en' and have ASCII filenames
  l4 run: no Warning on any g5 module; no stray @ref
  srcrefs check: 88 src: lines, 54 runs, 193 locators, 0 problems
  il-interpretation-time.l4 sha256 matches the brief
  tracecheck g5-tests-inspectors.l4: 51 traces, 0 mismatches
  tracecheck g5-tests-senior-inspector.l4: 23 traces, 0 mismatches
  tracecheck g5-tests-test-conduct.l4: 39 traces, 0 mismatches
  tracecheck g5-tests-testing-bodies.l4: 21 traces, 0 mismatches
  tracecheck g5-tests-withdrawal.l4: 11 traces, 0 mismatches
```

One `#TRACE` expectation (`s 30(a)` read as a power, then waiting) was first written wrongly: a permission (`MAY`) with no `WITHIN` is never spent, so waiting leaves it STANDING and not FULFILLED.
That was a correction of my expectation of L4's semantics, not of a legal expectation; the trace checker caught it, and no expectation about what the Law says was changed to fit the code.
The 19 failed assertions of `g5-tests-red.l4` are expected: each asserts, of the reading taken, the answer of a reading that section 2 rejected.
No assertion refused and none was left unevaluated.
No module prints a Warning.

## 10. Mutation testing of the tests

Run against the modules as deposited, after the last change to them, and run again with a harness that treats a run killed by a signal as invalid and repeats it (another session on this machine killed processes by pattern during the work; no run of the final mutation pass was invalid).
71 changes were applied, each alone to a scratch copy: flipping an `AND` to `OR`, dropping a limb, negating a guard, shifting a day by one, counting months as 30 days, swapping a party or a power in a guard, negating the commencement limb (IP2) of the two holds-the-power rules, and replacing a named refusal with a default.
All 71 were caught by the tests, and the two later mutations of the employee limb (section 1A) were caught as well (an assertion failed, or a trace gave a different result).
Earlier runs of 74 changes had one equivalent mutant (it rewrote a limb of s.37(b)(4) to the same truth table; the corrected mutation is among the 71) and four changes whose target text was not found (two were re-expressed and are among the 71).
An earlier run had one survivor: a guard in the s.31(4) rule that checked a different power than the rule's own, because the fixture inspector held all six powers; tests for an inspector who holds only the power, and one who holds every power but it, were added.
The scratch copies were deleted.
I killed no process by pattern; background runs were started and awaited by their own shell.
