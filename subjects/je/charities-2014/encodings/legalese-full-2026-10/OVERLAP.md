# Overlap table: the blind hunt, the surveyor's traps and the encoders' contradiction passes

Written 2026-10-27 by the overlap reader.
It compares three independent lists of contradictions, gaps and ambiguities in the Charities (Jersey) Law 2014, vintage from 2 October 2026.
It decides nothing about the Law itself: where a cell says a doubtful match was "settled" against the Law's text, it means settled for the purpose of matching, not that either reading is right.

## 0. What was compared, and how to read the tables

**Set H** is the blind hunt, `work/hunt/CONTRADICTIONS.md`: 55 findings H1 to H55, each argued with a discriminating case, plus a section of checks that came out clean, a list of provisions "read in full and found clean", and a list of what the sources do not let the hunter check.
By the hunt's own severity: 8 "blocks a decision" (BD, H1 to H8), 40 "changes an outcome" (CO, H9 to H48), 7 "cosmetic" (C, H49 to H55).
The hunter saw the Law, the PDF text layer, the BRIEF's cleanroom rules and vintage facts, and the amending instruments in `inputs/amending/` as they stood then (the hunt says eight; the directory now holds ten files, adding R&O.29/2021 and R&O.136/2019, see section 6).

**Set S** is the surveyor's first read, `phase1/PLAN.md` section (f): traps T1 to T30.
Only the traps are counted.
The PLAN's forks in section (g), its section 9 and its section (d) raise some of the same points; I name them only as "outside the traps" and never count them.

**Set E** is section 6 of each of `deposit/FRAGMENT-G1.md` to `FRAGMENT-G9.md`: 118 counted items (G1 16, G2 10, G3 9, G4 14, G5 12, G6 13, G7 16, G8 18, G9 10).
The heading differs by group: G4's is section 7 ("Contradictions and other findings in the source"), G6's is written "(6)", the others are section 6.
I cite items as `G<n>:<id>` using each author's own ids:

- G1, G2 and G7 number their items C1, C2 and so on; G4 has two sub-lists, C1 to C7 and D1 to D7, and I count both.
  G4 files D1 to D7 under "Gaps and asymmetries (not contradictions)"; they are counted and marked G in Table C.
- G3, G5, G8 and G9 number their items 1, 2, 3 and so on.
- G6's items are unnumbered bullets; I number them 1 to 13 in the order they appear (G6:1 is "Article 19(9)(c) and Article 20(1)(c) against Articles 11(4) and 11(5)", G6:13 is "Article 15(3)(b) against Article 33(2)(a)").
- Three numbered entries say that nothing was found and are not counted: G3:10 (cross-references checked), G5:13 (no fault found), G7:C17 (chain of "Minister" substitutions checked and consistent).
- Five counted items are about the survey, the BRIEF, the sources or the assignment rather than the Law (G2:C9, G7:C14, G7:C15, G7:C16, G9:7); they stay in the totals and carry an N in Table C.
- Other parts of the FRAGMENTs (the fork registers, the open questions, "what the sources do not answer") are not part of set E.
  Where an encoder raised a point only there, I say "outside §6"; those notes are never counted.

**Labels.**

- **M** means the item concerns the same provision(s) and the same discriminating question, or the same stated defect, as the hunt finding.
  For a finding that bundles several limbs, M requires the limb the hunt builds its case on, or the limb its heading names first, and the cell names the limb covered.
- **P** means overlap in provisions but a different aspect: the item states a neighbouring or consequential question, or reproduces a limb the hunt names without building a case on it.
  A P is not a match.
- **near** means the same provision with a different question; it is shown in brackets and never counted.
- A row's **status** is computed from the M labels only (strict): `both` (M in S and in E), `S-only` (M in S, none in E), `E-only` (M in E, none in S), `partial` (no M in either, at least one P), `hunt-only` (no M and no P).
  "With H" is understood in every status: the list agrees with the hunt on that finding.
- A trap or item can be M for more than one finding (T10 for H1 and H3; T15 for H11 and H25) and a finding can have several M items; counts of findings and counts of items are therefore separate.

**Strict, lenient and limb-sensitive counts.**
The tables are strict.
Section 1.1 also gives a lenient figure (every P counted as a match) and the effect of demoting the eight matches that cover only one named limb of a bundled finding.

**Doubtful matches settled against the Law.**
I settled four against `inputs/charities-jersey-law-2014-2026-10-02.txt`: H3 against G4:C2 (src:319-328: 11(5) reads "If not so satisfied", and the two read it in opposite ways while asking the same question), H17 against T25 (src:541-553 and 566-570: T25 states the consequence for a 2(1)(h) body but not H17's question whether a trust falls in (a) or (j), so P and not M), H21 against T23 and G8:9 (src:635: they read the two purposes of 26(10), H21 asks what falls outside them, so P), and H12 against G1:C16 (src:476 and 490: the same question put to 18(4)(a) instead of 19(1)(g), so P).
Matching was done by reading each candidate's text, not titles.
My judgement of M against P is the least certain part of this file; each cell names the limb or the case so a reader can overrule it.

**How the counts were made.**
All counts in section 1 were recomputed by script (`work/overlap/snap/verify_overlap.py`).
The script derives each row's status in Table A from the M and P labels in its S and E cells and checks it against the status column; it then recomputes the tables of 1.1, the trap groups of 1.2 and the per-group figures of 1.3 from Tables A, B and C.
It also checks that every one of the 118 items is either an M item of Table A or a row of Table C, and that the 12 partial rows of Table C are exactly the items Table A cites with a P.

**G2 and G7 were being edited while I worked.**
The G2 and G7 results of the second read are in section 6.

## 1. Counts

All counts are strict: only plain M labels count as matches.
The lenient figure and the limb-sensitive figure are given once, in 1.1.

### 1.1 The 55 hunt findings

| | blocks a decision (8) | changes an outcome (40) | cosmetic (7) | all (55) |
| --- | --- | --- | --- | --- |
| matched by S | 4 | 13 | 4 | 21 |
| matched by E | 4 | 17 | 6 | 27 |
| matched by S or E | 4 | 18 | 6 | **28** |
| matched by both S and E | 4 | 12 | 4 | 20 |
| S only (with H) | 0 | 1 | 0 | 1 |
| E only (with H) | 0 | 5 | 2 | 7 |
| partial only | 0 | 8 | 0 | 8 |
| hunt-only (no M, no P) | 4 | 14 | 1 | **19** |

The five exclusive groups add up: both 20, S-only 1, E-only 7, partial 8 and hunt-only 19 give 55.

**Which findings are in which group.**

- both (20): H1 H2 H3 H4 H9 H11 H13 H14 H19 H25 H26 H29 H32 H33 H34 H41 H49 H53 H54 H55.
- S-only (1): H40, confirmed by the surveyor and the hunt but by no encoder §6 item (G7's fork F7.1 asks the 9.30 a.m. question, outside §6).
- E-only (7): H10 H15 H18 H44 H46 H51 H52, confirmed by an encoder and the hunt but not by a trap.
- partial only (8): H12 H17 H20 H21 H24 H42 H43 H48.
- hunt-only (19): H5 H6 H7 H8 H16 H22 H23 H27 H28 H30 H31 H35 H36 H37 H38 H39 H45 H47 H50.

**Lenient reading** (every P counted as a match).
S matches 27, E matches 33, S or E 36, both 24, S-only 3, E-only 9, partial 0, hunt-only 19.
Four rows move to both (H12, H18, H20, H21), two to S-only (H17, H42), three to E-only (H24, H43, H48).

**Limb-sensitive reading** (the eight matches that cover only one named limb of a bundled finding are demoted to P: H3, H4, H13, H33, H53, H54 among the both rows, H15 and H46 among the E-only rows).
Both falls to 14, E-only to 5, partial rises to 16; S-only stays 1 and hunt-only 19.
H49 is not demoted: E covers both its limbs.

### 1.2 The 30 surveyor traps

| group | traps | count |
| --- | --- | --- |
| matched (M) to a numbered hunt finding | T1 T3 T4 T5 T6 T7 T9 T10 T11 T12 T13 T14 T15 T16 T20 T24 T26 T28 T30 | 19 |
| partial only (P) | T2 T8 T22 T23 T25 | 5 |
| not found by the hunt | T17 T18 T19 T21 T27 | 5 |
| not a claim of defect in the Law | T29 | 1 |

The 19 matched traps cover 21 hunt findings (T10 covers H1 and H3; T15 covers H11 and H25).
Lenient: 24 of 30 traps (the 5 partial ones counted).
So the hunt missed 5 traps outright and overlaps with 5 more only partially.
The hunt's own record explains four of the five misses: T17, T18, T19 and T27 sit on provisions the hunt lists as read and found clean (Sch 1 4(1)-(11); 13(5)-(13); 18(1)-(4); 6(1)-(4) and 28(1)-(2)).
T21 is on Sch 1 3(4)(c), which the hunt cites in H39 for a different question.
T29 is a statement about the sources, and the hunt's list of what it could not check names the same three instruments.
Of the five partials, T8 matches one half of a two-part trap and T2 is a correction to the BRIEF; T22 (H42), T23 (H20, H21) and T25 (H17) stand on the same provisions as the finding named but ask a different question.

### 1.3 The 118 encoder items

| group | section | items | not counted | M (matched to a finding) | P only | no relation | of the no-relation: labelled N / X / G / unlabelled | the hunt's clean list, over the 78 rows of Table C: listed / partly / not listed / n/a |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G1 | 6 | 16 | 0 | 7 | 1 | 8 | 1 / 4 / 0 / 3 | 3 / 2 / 4 / 0 |
| G2 | 6 | 10 | 0 | 1 | 1 | 8 | 2 / 2 / 0 / 4 | 5 / 3 / 0 / 1 |
| G3 | 6 | 9 | 1 (item 10) | 5 | 1 | 3 | 0 / 0 / 0 / 3 | 2 / 2 / 0 / 0 |
| G4 | 7 | 14 | 0 | 3 | 1 | 10 | 0 / 0 / 7 / 3 | 4 / 7 / 0 / 0 |
| G5 | 6 | 12 | 1 (item 13) | 5 | 2 | 5 | 1 / 2 / 0 / 2 | 4 / 1 / 2 / 0 |
| G6 | (6) | 13 | 0 | 8 | 0 | 5 | 0 / 0 / 0 / 5 | 3 / 2 / 0 / 0 |
| G7 | 6 | 16 | 1 (C17) | 6 | 3 | 7 | 2 / 2 / 0 / 3 | 3 / 1 / 3 / 3 |
| G8 | 6 | 18 | 0 | 4 | 1 | 13 | 1 / 2 / 0 / 10 | 6 / 5 / 3 / 0 |
| G9 | 6 | 10 | 0 | 1 | 2 | 7 | 3 / 1 / 0 / 3 | 5 / 2 / 1 / 1 |
| all | | 118 | 3 | 40 | 12 | 66 | 10 / 13 / 7 / 36 | 35 / 25 / 13 / 5 |

Items matched to a numbered hunt finding: G1:C3 C7 C8 C9 C11 C12 C13; G2:C8; G3:2 3 4 6 9; G4:C1 C2 C7; G5:3 4 9 10 11; G6:1 2 4 5 6 7 11 13; G7:C1 C5 C6 C7 C9 C12; G8:2 5 8 10; G9:1.
Items that are P only: G1:C16; G2:C10; G3:1; G4:C4; G5:2 6; G7:C3 C13 C14; G8:9; G9:2 7.

In the last column the clean list is the hunt's section "Provisions read in full and found clean"; the figures count the 78 rows of Table C (the 66 no-relation rows and the 12 P-only rows), each in exactly one of the four classes.
Of the 66 items with no relation to any hunt finding, 30 are labelled by their own authors: 10 as not a defect of the Law (N), 13 as a slip, redundancy or point with no case (X), 7 as a gap listed apart from the contradictions (G).
That leaves 36 unlabelled, substantive items the hunt did not raise.
Sixteen of those 36 are on provisions the hunt lists as read and found clean: G1:C4, G1:C14, G2:C3, G2:C4, G3:7, G3:8, G5:1, G6:8, G6:9, G6:10, G7:C2, G8:14, G8:15, G8:16, G9:3, G9:5.
The five items about the survey, the BRIEF or the assignment (G2:C9, G7:C14, G7:C15, G7:C16, G9:7) have no clean-list entry (n/a above); three of them are among the 66 and two (G7:C14, G9:7) among the P-only rows.

## 2. Table A: the 55 hunt findings

Severity: BD blocks a decision, CO changes an outcome, C cosmetic (the hunt's own labels; its "narrow", "of the maximum" and "fiscal" qualifiers are not shown).
A parenthesis after an M names the limb of a bundled finding that the match covers.
Rows whose status is `partial` have no plain M in either list.
"Outside the traps" and "outside §6" name points raised in the PLAN's forks or sections, or in an encoder's forks or open questions, which the counts do not use.

| hunt id | provisions | sev | one line | S match | E match | status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | 11(4)-(5), 19(9)(c), (e)(i) | BD | For an unfit governor the Commissioner "must register" (11(4)), "must not grant" (19(9)(c)) and must tell the applicant it "will be refused" on a ground 11(5) lacks | M: T10 (case A) | M: G4:C1, G6:1 | both |
| H2 | 19(9)(e)(i), 27(4), 28(3) | BD | The mandatory required steps notice to remove a governor is invalid for an organized religious charity | M: T11 | M: G6:2, G8:8 (near: G8:7, on 27(4) against 27(2)) | both |
| H3 | 11(4)-(5), 19(6), 11(8)(a)(i), 15(3), 33(1)-(2) | BD | The duties to register or refuse arise only once the applicant complies; an incomplete application gets no decision and no appeal | M: T10 (case B; the application limb, the 15(3) deregistration limb is H-only) | M: G4:C2 (same limb; settled against src:319-328: G4:C2 reads 11(5) as not conditioned on compliance and the hunt reads it as continuing 11(4), the question is the same); P: G4:C4 (19(6)) | both |
| H4 | 13(7)-(8), 8(3)(j), Art 1 "annual return", 19(4) | BD | The annual return has no due date and no defined year | M: T24 (the year limb; the due-date limb is H-only, outside the traps: PLAN section 9 item 5) | M: G5:10 (the year limb) | both |
| H5 | 9(2), 13(5), 13(6)(g) | BD | No route from the restricted section back to the general section | none | none (outside §6: G3 §7 question 8) | hunt-only |
| H6 | 19(9)(b), (d), (e), 19(10)-(11), 20(1)(a)-(b) | BD | A governor the court finds fit (application dismissed) has no permission to act, and commits an offence by acting | none | none | hunt-only |
| H7 | 16(2), 17(2)(c) | BD | Deregistering an entity that no longer exists needs written notice to a person who may not exist | none (near: T15, on the 16(1) and 16(2) pair) | none (near: G6:3; outside §6: G6 §7 question 4) | hunt-only |
| H8 | 19(11), 20(6), 21(9), 23(7), 26(10), 29(1); 21(10), 23(6), 26(7) | BD | Six offences carry "a fine" and three "level 3"; the Law states no amount | none (outside the traps: PLAN section 9 item 6, as a gap in the sources) | none (outside §6: G6 §8 item 5 and G8 §8 item 1, likewise as a gap in the sources) | hunt-only |
| H9 | Art 1 "Minister", 5(2)(a), (c) | CO | "Minister" is defined as one office, but 5(2)(a) says "a Minister" | M: T4 | M: G1:C13 | both |
| H10 | 13(2)-(3), 5(1)(a)(ii), 6(5) | CO | Adding a purely ancillary purpose is void under 13(2) but lawful under 5(1)(a)(ii) | none | M: G5:3 | E-only |
| H11 | 17(2)-(3), 17(5)-(9), 13(1) | CO | Retrospective deregistration: the property acquired, and the amendments made, in the gap | M: T15 (cases B and C) | M: G6:5; P: G5:6 (the 13(2) amendments limb) | both |
| H12 | 19(1)(g), 2(10)(b) | CO | Is an unspent dishonesty conviction unconnected with any charity a reportable matter | P: T8 (the same "in relation to" question asked of 2(10)(b) itself; PLAN F1.2 lists 19(1)(g), outside the traps) | P: G1:C16 (the same question through 18(4)(a): src:476 against src:490) | partial |
| H13 | 19(2)-(3), (8), (10)-(11), (13); 2(10)(a) | CO | The governor who reports commits an offence by acting; the one who conceals commits none | M: T9 (the asymmetry; the 19(3) application-stage gap is H-only) | M: G6:7 (same) | both |
| H14 | 33(1)-(3), 15(3)(b), 12(3)-(4), 19(9)(e)(ii), 9(2), 9(7), 10(5), 13(11)(b) | CO | Decisions that bind a charity or governor and that no one but the Attorney General can appeal | M: T12 | M: G6:13 (15(3)(b)), G8:5 (9(7) with 33(1)(b); 15(3)(b)); P: G3:1 ("the applicant" in Art 9, the premise of the 33(1)(b) case) | both |
| H15 | 33(5), 12(1) | CO | A registered charity cannot appeal the registration of a confusingly named rival, and the ground is the Commissioner's own opinion | none | M: G8:2 (the exclusion limb; the "opinion" limb is H-only; near: G8:13, G4:C3) | E-only |
| H16 | 21(1)-(6), 23(1)-(2), 2(1)(i) | CO | Part 6 binds only "entities": an individual or partnership may call itself a charity | none | none | hunt-only |
| H17 | 2(1)(a), (j), 2(3)(a), 21(3), 21(5), 22 | CO | A foreign-law trust within the Royal Court's jurisdiction is a "Jersey entity", which cancels its excepted-foreign-charity status | P: T25 (the same consequence for a 2(1)(h) body; T25 does not ask the (a) against (j) question and calls the text clear; settled against src:541-553 and 566-570) | none | partial |
| H18 | 2(1)(ba), 2(1)(j), 2(2), 2(3)(a), 39(1) | CO | Does the inserted (ba) fall inside "(a) to (h)", and could an Order under 2(2) have that effect | P: T5 (names 2(3)(a) as read around (ba) and asks no question; PLAN F1.1 asks it, outside the traps) | M: G1:C9; P: G7:C3 (the 39(1) limb) | E-only |
| H19 | 2(5)(e), 2(1)(g), (h), 8(4)(a), 2(10)(a)(ii) | CO | "Constitutional Law" has no case for bodies incorporated "under, but not by" an enactment | M: T6 | M: G1:C3, G3:3 | both |
| H20 | 26(1)-(2), 27(3), 4(1)(c) | CO | The information power cannot reach the cases the Commissioner most needs it for | P: T23 (the same single-purpose premise; asks about applicants, not deregistered or unregistered entities) | P: G8:9 (same; near: G8:1) | partial |
| H21 | 26(10)-(11), 13(6)-(7), 15(2), 9(4), 19(2), 19(5) | CO | Knowing falsehoods in returns, reports and declarations fall outside the false-information offence | P: T23 (the same two purposes of 26(10), seen from the other side; settled against src:635) | P: G8:9 | partial |
| H22 | 29(1) | CO | Restricted information: whose consent is needed | none | none (outside §6: G8 fork F8.11) | hunt-only |
| H23 | 4(3)(c), 29(1), 31, 4(1)(e) | CO | The Commissioner may assist foreign regulators, but disclosing to them may be an offence | none | none (near: G8:11, on 31(b), (c); outside §6: G2 fork F2.8 asks whether 4(3)(c) assistance needs a Commissioner function) | hunt-only |
| H24 | 29(1)-(2), 19(2)-(4), Sch 2 para 4(3)(g), 31 | CO | Article 29 binds every recipient, charities, governors and the tribunal included, with gateways only for officials | none | P: G9:7 (29(1) binds "a person who receives", the Commissioner included; a correction to the survey) | partial |
| H25 | 17(2)(c), 17(4), 16(1) | CO | "The notice under Article 16(1)": there are two | M: T15 (case D) | M: G6:4 | both |
| H26 | endnote tables; R&O.17/2018 | CO | The commencement table uses the pre-renumbering Article numbers without saying so | M: T1 (P: T2, the composition of the remainder) | M: G7:C6 (P: G7:C14, the same composition point, from the BRIEF) | both |
| H27 | 23(3)(c), 23(1), (6) | CO | "Wholly or mainly managed or controlled in or from within Jersey" | none | none | hunt-only |
| H28 | 22(2)(a)(i), 22(3)(a) | CO | "The jurisdiction under whose law it is established" for a charity of one part of the UK managed from another | none | none (near: G7:C10, on 22(3)(b)) | hunt-only |
| H29 | 10(4)-(5), 8(5), 10(3)(c) | CO | The safety exception cannot protect historic-section entries | M: T16 | M: G3:4 | both |
| H30 | 8(5)(b), 9(1)(a), 10(3)(c) | CO | Historic section: is the name of a charity that moved into the restricted section published | none | none (near: G3:7, on 9(1)(a); outside §6: G3 fork F3.11) | hunt-only |
| H31 | Art 1 "donation", "solicit"; 9(3); 14(3)(a)(ii); 24(1) | CO | "Donation" and "solicit" are defined only by an Order that may not exist and was made for another purpose | none | none (outside §6: G3 §7 questions 9 and 13 and §8 item 1 take the Order's content as an input) | hunt-only |
| H32 | 37(1), 21(9)-(10), 23(6)-(7), 2(1)(a), (b), (i) | CO | Offences "by an entity" that is not a body corporate have no one to bear them | M: T26 | M: G7:C9 | both |
| H33 | 8(6), 17(1)(a), 26(5), 20(5), 11(2)(e)(ii) | CO | Retention and other periods with no stated start | M: T14 (the two 10-year retention limbs; the 26(5), 20(5), 11(2)(e)(ii) limbs are H-only) | M: G3:6, G6:6 (the same retention limbs); near: G6:5 (17(1)(a) under a retrospective date) | both |
| H34 | 11(2)(e)(ii), 13(9)(b) | CO | An application must carry a payments statement only if an Order "applies to the registered charity", which an applicant is not | M: T28 | M: G4:C7, G5:9 (near: G4:C5) | both |
| H35 | 12(6), 13(6)(b) | CO | The power to require a change of name arises only from the charity's own report | none | none (near: G4:D7, on the wording of 13(6)(b)) | hunt-only |
| H36 | Sch 1 para 3(4)(b); Sch 2 para 2(4)(b) | CO | A sitting States member may be appointed; only "becoming" a member ends the appointment | none | none | hunt-only |
| H37 | 35(1), 33, Sch 2 para 4(3)(h) | CO | Can the Commissioner appeal from the tribunal: who is a "party" | none | none (near: G8:4, on 35(1) against 34(1)) | hunt-only |
| H38 | 36(2)(a), 33(5) | CO | No time limit for appeals unless an Order makes one; "the time of the appeal" | none (near: T12, which notes the two dates of 33(5)) | none (near: G8:3, G8:12; outside §6: G8 fork F8.6 asks from when a limit runs, not that none exists) | hunt-only |
| H39 | Sch 1 para 3(1)(a), 3(4)(c), 4(5), 4(3)(c) | CO | When a resigning Commissioner stops being Commissioner, and whether acting service counts toward 12 years | none (near: T21; PLAN F9.3 and F9.11 ask both limbs, outside the traps) | none (near: G9:9; G9 forks F9.3 and F9.11 ask both limbs, outside §6) | hunt-only |
| H40 | Art 1 "Minister"; R&O.10/2024; R&O.40/2019 | CO | Who "the Minister" is changes in the middle of 27 February 2024 | M: T3 | none (G7:C17 records the chain as consistent; G7 fork F7.1 asks the 9.30 a.m. question, outside §6) | S-only |
| H41 | 21(2)(b)(ii), 21(4)(b)(ii), 21(6)(b)(ii), 23(2)(b)(ii) | CO | "Or other advantage" is in one false-reference offence and not in its three siblings | M: T13 (second limb) | M: G7:C5 | both |
| H42 | Sch 1 para 2(4)(a), 4(7); L.1/2017 Art 20 | CO | Schedule 1 is made "subject to Article 20(1)" of the Dormant Bank Accounts Law, which is not the provision about the Commissioner's pay | P: T22 (the same provisions; asks when the words exist and takes the 20(1) Order as an input) | none (near: G7:C16, on the same L.1/2017 date) | partial |
| H43 | 7(1), 5(5) | CO | The public benefit rules bind only the Commissioner, the tribunal and the court | none | P: G2:C10 (the same two provisions name the Commissioner but not its staff; the hunt's case is a Comptroller or a trustee, G2:C10's is a staff determination; added to G2 §6 at 02:19 on 27 October); near: G2:C2 on 7(1), G4:D1 on 5(5) | partial |
| H44 | 14(1)(b), 14(2) | CO | Orders "to remedy the misconduct" where the ground is not misconduct | none | M: G5:4 | E-only |
| H45 | 8(4)(c), 11(4)(d), 13(6)(a) | CO | "One of the governors": which one | none | none (outside §6: G3 §4 request 3 and §5.3 return every governor's address) | hunt-only |
| H46 | 13(4)(b), 13(5)(b), 13(11)(b), 12(3)-(5), 33(2)(e) | CO | Approvals and permissions the Law assumes but gives no procedure or criteria for | none (near: T12, which lists 13(5)(b) and 13(11)(b) among the decisions with no appeal) | M: G5:11 (the 13(4)(b) and 33(2)(e) limb, which carries the hunt's case); P: G5:2 (the 13(5)(b) limb); near: G5:5 (13(11)(b)) | E-only |
| H47 | Sch 2 para 1(1), 4(1)-(3); 34(3)(b) | CO | Tribunal: no duty to keep four members, no quorum, costs in two places | none | none (outside §6: G9 §1 row Sch2 4(3)(e) and §3 answer the quorum question with a named refusal) | hunt-only |
| H48 | 38, 26(1), 27(2) | CO | "Further provision as to the service of any notice" with no first provision | none (outside the traps: PLAN F7.7) | P: G7:C13 (the same Art 38 gap, asking which date and not whether service happened) | partial |
| H49 | 2(10)(b), 22(1); commencement of Art 22 | C | "Excepted foreign charity (within the meaning of Article 22)" is defined for Art 21 only, and Art 22 was not in force when misconduct first mattered | M: T30 (the commencement limb) | M: G1:C8, G7:C1 (the cross-reference limb); G6:11, G7:C7 (the commencement limb) | both |
| H50 | Art 1 "register", "registered charity"; 8(5); 21(1) | C | The verb "register" makes a deregistered entity "registered" | none | none (near: G1:C11) | hunt-only |
| H51 | R&O.40/2019 Sch 2 para 1(e) | C | The instrument amends "Article 1(1)", which does not exist | none | M: G7:C12 | E-only |
| H52 | Endnote [4]; Art 31(a)-(c) | C | The endnote corrects "for purpose of" in 31(c) only | none | M: G8:10 | E-only |
| H53 | Sch 2 heading; Sch 1 para 4(12); endnote [3] marker | C | Names and references that do not match | M: T20 (the Sch 2 heading limb) | M: G1:C12, G9:1 (the Sch 2 heading limb); P: G9:2 (the Sch 1 4(12) limb) | both |
| H54 | "historic section", "charity", "supervisory body", "resident", "Jersey charity", "the applicant" | C | Terms used but not defined | M: T7 ("historic section", the first-named term) | M: G1:C11, G3:9 ("historic section"), G2:C8 ("charity" in 4(2), the only term the hunt gives a case for); P: G3:1 ("the applicant") | both |
| H55 | 8(3)(a)(i)-(ii), 2(1)(ba) | C | The register's status note does not mention (ba) | M: T5 | M: G1:C7, G3:2 (P: G7:C3, the 39(1) limb) | both |

Row count: 55 (8 BD, 40 CO, 7 C).

## 3. Table B: the 11 surveyor traps with no full match in the hunt

"Relation to H" is `not found`, `not a defect claim`, or `partial` (P to the finding named; near is shown in brackets and not counted).
"The hunt's clean list" is what the hunt's section "Provisions read in full and found clean" or its other sections say about the same provisions.
"E also" names the encoder items (§6 only) that raised the same point, so the table shows whether the miss was shared.

| trap | gist | relation to H | the hunt's clean list | E also |
| --- | --- | --- | --- | --- |
| T2 | The 2019 "remainder" is Part 6 and the original Article 41, not original 44(2) and (3); the BRIEF's wording is wrong (a correction to the BRIEF, not a defect of the Law) | partial: H26 (its Why states the composition of the remainder; it does not mention the BRIEF or ask whether "44" covers (2) and (3)) | nothing | G7:C14 |
| T8 | "Misconduct" is defined twice and refers to itself (2(10), 18(4)(c)); and does "in relation to" govern every limb of 2(10)(b) | partial: H12 (the "in relation to" half, reached through 19(1)(g)); the self-reference half is not found | 2(10)(a) and 18(1)-(4) are listed as clean; 2(10)(b) is not | G6:9 (the self-reference), G1:C16 (the "in relation to" half through 18(4)(a)) |
| T17 | Sch 1 4(3)(b) reserves "whether to refuse" under 15(3), not the grant | not found | Schedule 1 paras 4(1)-(11) are listed as clean | G9:3; G6:13 (second case); near: G2:C10 (staff acting under Sch 1 4(3)) |
| T18 | "Any Order under paragraph (7), (8) or (9)" in 13(10) names a paragraph that confers no Order | not found | 13(5)-(13) are listed as clean, apart from H4, H34, H46 | G5:1 |
| T19 | The standard of care in 18(2) binds only governors of 2(1)(i) bodies | not found | 18(1)-(4) are listed as clean | none in §6 (G6 fork F6.7, outside §6) |
| T21 | Re-appointment and the 12-year cap (Sch 1 3(4)(c)) | not found (near: H39, which asks whether acting service counts toward the 12 years) | Sch 1 3(2)-(3) are listed as clean; 3(4)(c) is cited by H39 | G9:9 |
| T22 | The two Dormant Bank Accounts openings of Schedule 1 exist only from 16 December 2019 | partial: H42 (the same provisions; H42 asks whether the cross-reference to 20(1) is the right paragraph) | nothing on the vintage; the hunt checked that L.1/2017 Art 30(3) inserts the two phrases | G7:C16 (the date rests on the Table alone) |
| T23 | The power to demand information serves one purpose; the offence of false information serves two | partial: H20 and H21 (the same two clauses, each asking a different question) | 26(3)-(9) and 26(11) are listed as clean; 26(1), (2) and (10) are not | G8:9 |
| T25 | A body incorporated under, but not by, a UK Act extended to Jersey is a Jersey entity (2(1)(h), 2(3)(a)) and so cannot use the excepted-foreign-charity exemption of 21(5) | partial: H17 (the same consequence for a trust within 2(1)(a); H17's discriminating question is whether such a trust falls in (a) or (j), which T25 does not ask and answers "the text is clear, if odd") | 2(3)(b) is listed as clean; 2(3)(a), Art 21 and 22(3) are not | none in §6 (G7:C10 repeats the last sentence of T25, the 22(3)(b) redundancy) |
| T27 | A philosophical-belief purpose is "analogous to" religion for 6(1)(p), but 28(1)(a) asks about 6(1)(c) | not found | 6(1)-(4) and 28(1)-(2) are listed as clean | G2:C4 |
| T29 | Three vintages are only partly shown by the sources (R&O.29/2021, R&O.136/2019, the Act appointing 16 December 2019) | not a defect claim: a statement about the sources; the hunt's section "What the sources do not let me check" lists the same three | n/a | G7:C15, G7:C16 (G7 says R&O.29/2021 and R&O.136/2019 are now among the inputs) |

Row count: 11 (5 partial, 5 not found, 1 not a defect claim).

## 4. Table C: the 78 encoder items with no full match in the hunt

"Relation" is `none` (near is shown in brackets and not counted) or `partial` (P to the finding named).
"S" names the surveyor trap, if any, that raised the same point.
"Self-label" marks items whose author says: N, not a defect of the Law (a tension, observation, consistent overlap, a defect of an amending instrument, or a correction to the survey, the BRIEF or the assignment); X, a slip, redundancy or point with no case or no effect; G, a gap or asymmetry listed apart from the contradictions.
"Hunt's clean list" says whether the provisions the item turns on appear in the hunt's section "Provisions read in full and found clean": `listed`, `partly` (some of them), `not listed`, or `n/a` (the item is about the BRIEF, the survey, the sources or the assignment).
The clean list is the hunt's own record of what it read and found nothing further in; it is not exclusive of the findings (it lists 13(3), cited by H10, for example), so `listed` means only that the hunt wrote nothing about the point.

| item | gist | relation | S | self-label | hunt's clean list |
| --- | --- | --- | --- | --- | --- |
| G1:C1 | 2(10)(b) "in relation a registered charity": a "to" is missing, in the consolidated text and the PDF alike | none | T8 (quotes the missing "to" in passing) | X | not listed |
| G1:C2 | 2(10)(b)(vi) says "clauses (i) to (v)"; the Law has no other name for that level and says "sub-paragraphs" only for the lettered level, so it is not shown to be a slip | none | none | X | not listed |
| G1:C4 | 2(1)(g) overlaps (c) and (d) as written, against 8(3)(a)(i)'s "the sub-paragraph" | none (near: T5, on overlapping kinds) | none | - | listed |
| G1:C5 | 2(1)(j) "an entity that is substantially similar to an entity" uses "entity" for the thing defined | none | none | X | not listed |
| G1:C6 | 2(1)(b) is "without prejudice to" (a) and (i) excludes only "the trustees of a trust": a fidéicommis may be within (a) and (b) | none | none | - | partly |
| G1:C10 | Art 1 defines "council member" and nothing uses the term | none | none | X | listed |
| G1:C14 | 17(9)(a) and 14(1)(a) against Art 1 "for the time being": is the charity's standing read when the conduct occurred or when asked | none | none | - | listed |
| G1:C15 | L.13/2019 Schedule 3 is headed "(Article 29(2))" while the Article saying "Schedule 3 has effect" is 28(2) | none | none | N | not listed |
| G1:C16 | 18(4)(a) "an offence, mentioned in Article 2(10)" can be read without the connection to a charity | partial (H12) | T8 | - | partly |
| G2:C1 | 4(4) "so far appears" for "so far as appears" | none | none | X | listed |
| G2:C2 | 5(1)(b) ("provides", or for an applicant "provides or intends to provide") against 7(1), which has no limit to applicants | none (near: H43, on 7(1)) | none | - | partly |
| G2:C3 | 5(6) says "guidance" where 5(4), (5) say "the guidance"; 11(6)(b) extends 5(6)-(8) to other guidance | none | none | - | listed |
| G2:C4 | 6(2)(f) puts a philosophical-belief purpose within (p) by analogy with (c); 28(1)(a) asks about 6(1)(c) | none | T27 | - | listed |
| G2:C5 | 11(4)(a) "or will do so on registration": which limbs of the charity test may be prospective | none | none | - | partly |
| G2:C6 | 7(4) has a comma before its verb | none | none | X | listed |
| G2:C7 | 4(1)(d), 5(4) and 7(4) are three provisions about the same guidance; they agree | none | none | N | listed |
| G2:C9 | The assignment gives the copy to the Minister as "4(7)"; the Law's Article is 5(7) | none | none | N | n/a |
| G2:C10 | Sch 1 4(3) lets staff exercise any function of the Commissioner; 7(1) and the second limb of 5(5) name the Commissioner but not staff, so a staff determination escapes 7(3)(b) (added to G2 §6 at 02:19 on 27 October, with its fork F2.13) | partial (H43) | T17 (near, same paragraph 4(3)) | - | partly |
| G3:1 | "The applicant" in 9(2)(a), (b) against the 9(2) lead-in, which lets a general-section charity request entry | partial (H54, the "applicant" limb; H14, the premise of its 33(1)(b) case) | T12 (near, on 9(7)) | - | partly |
| G3:5 | 8(3)(k) notes a notice served on the charity or on a governor; 8(6)(c) retains a copy of a notice served on the charity only | none (near: H33, on 8(6)) | none | - | partly |
| G3:7 | 9(1)(a) withholds a restricted-section charity's name, but 9(1)(b) makes public 8(3)(k), whose copy of a notice names it | none (near: H30) | none | - | listed |
| G3:8 | 12(5) has the Commissioner enter "the new or alternative registered name"; 8(3)(l) lists only "the previous registered name" | none | none | - | listed |
| G4:C3 | 12(1) defines "undesirable" "for the purpose of Article 11(4)(e)", but 12(7)(b)(ii) and 33(5)(b) use it elsewhere | none (near: H15, on 33(5)(b)) | none | - | partly |
| G4:C4 | "Complete" in 19(6) is not "includes what 11(2) requires" | partial (H3, which cites 19(6)) | T10 (case B) | - | listed |
| G4:C5 | 11(2)(e)(ii) cites an Order under 13(9)(b), 8(3)(m) one under 13(9)(c) | none (near: H34) | none | - | partly |
| G4:C6 | 2(4)(g) constitution "in whatever form" against 11(4)(b) "a written document" | none | none | - | partly |
| G4:D1 | 11(6)(c), (d) and 5(5): the two guidance regimes are parallel but not identical | none (near: H43, on 5(5)) | none | G | listed |
| G4:D2 | 11(2)(e)(iv) "prescribed by the Minister by Order" with no power to make it; 11(3)(a) lets the States add to the same list | none | none | G | partly |
| G4:D3 | 12(1)(a) compares a name with any other registered charity's, including a restricted-section charity whose name is not public | none | none | G | listed |
| G4:D4 | Nothing says an applicant must be told of a refusal under Art 11 | none (near: H3) | none | G | partly |
| G4:D5 | Whether a re-registered entity receives a new number or its old one (12(2)(b), 17(1)(b)) | none | none (near: T14, on 17(1)(b)) | G | partly |
| G4:D6 | An entity already registered or deregistered may apply (11(1)); the Law neither permits nor forbids it | none | none | G | listed |
| G4:D7 | 13(6)(b) speaks of "refusing to accept the name", which Arts 11 and 12 do not call any decision; 12(6) cross-refers | none (near: H35) | none | G | partly |
| G5:1 | 13(10) names "any Order under paragraph (7), (8) or (9)"; paragraph (8) creates no Order | none | T18 | - | listed |
| G5:2 | 13(5)(b) presupposes a permission that no provision confers | partial (H46, the 13(5)(b) limb) | T12 (near, which lists 13(5)(b)) | - | not listed (excluded for H46) |
| G5:5 | 13(11)(a) "a statement" against 13(11)(b) "that statement" and 13(9)(b) "current intentions" | none (near: H46, on 13(11)(b)) | none | - | partly |
| G5:6 | 13(1) with 17(3): amendments made in the interval of a retrospective deregistration are not struck by 13(2) | partial (H11, the 13(2) limb) | T15 (case C) | - | not listed |
| G5:7 | 14(3)(b) "(whether a specified or indefinite period)" lacks "for" | none | none | X | listed |
| G5:8 | 14(1) says "the powers set out in paragraph (2)" though the listed orders are in (3); 17(9) says "set out in Article 14" | none | none | X | listed |
| G5:12 | 14(3)(a)(i) lets the court forbid a registered charity to hold itself out as a charity, while an Order under Art 25 may require it to say it is one | none | none | N | listed |
| G6:3 | 16(1) (a power after a preliminary notice) beside 16(2) (a duty with no notice) for an entity that has ceased to exist and fails the charity test | none (near: H7, on 16(2)) | T15 | - | partly |
| G6:8 | 19(4) "when notified by the charity": nothing requires the charity to notify | none | none | - | listed |
| G6:9 | 18(4)(c) makes one governor's misconduct depend on another's, and Art 1 reads "misconduct" by 18(4) | none | T8 | - | listed |
| G6:10 | 17(9) lends the Art 14 powers but not to the Commissioner, whom 14(1) names | none (near: H11, whose case cites 17(9)) | none | - | listed |
| G6:12 | The heading of Art 20 ("fitness of governor") against paragraphs (3)-(6), which concern "a person" | none | none | - | partly |
| G7:C2 | 24(3)(a) lets Regulations adapt any of Arts 21-23, whose offences carry imprisonment; 24(4) caps the penalty at "no greater than a fine" | none | none | - | listed |
| G7:C3 | 2(2) lets an Order add sub-paragraphs; 39(1) bars an amendment of the Law from an Order's ancillary provisions | partial (H18 and H55, the 39(1) limb) | none | - | listed |
| G7:C4 | 21(1) and 21(2) (with 21(7)) are both made out by one untrue statement to a donor; likewise 21(3)/(4), (5)/(6), 23(1)/(2) | none (near: H41, the other limb of T13) | T13 (first limb) | - | not listed |
| G7:C8 | Part 8 is brought into force in two stages and Part 9 in three (the second read of G7 adds the spent original Article 41), so "Part 8 is in force" has no single day | none (near: H26) | none | - | partly |
| G7:C10 | 22(3)(b) "is not a registered charity" repeats the opening words of 21(5) and (6) | none (near: H28, on 22(3)(a)) | T25 (last sentence) | X | not listed |
| G7:C11 | 42(a) reads "by reference the test itself" (no "to") | none | none | X | listed |
| G7:C13 | "Giving of the notice" (17(4), 36(2)(b)) against "served" (Art 1, 8(3)(k), 26, 27) against "service" (38) | partial (H48) | none (outside the traps: PLAN F7.7) | - | not listed |
| G7:C14 | The BRIEF's account of the 2019 remainder against R&O.17/2018 Art 2 | partial (H26, the composition of the remainder) | T2 | N | n/a |
| G7:C15 | The survey took the 2 March 2021 text of "Minister" as inferred; R&O.29/2021 is now among the inputs | none | T29 | N | n/a |
| G7:C16 | L.1/2017's date of 16 December 2019 still rests on the Table alone | none (near: H42) | T29, T22 | N | n/a |
| G8:1 | 26(4)(a) "the registered charity" (a charity registered now) against 26(2), which reaches a formerly registered entity | none (near: H20, on 26(2)) | none | - | partly |
| G8:3 | 33(5): two groupings of "at both the time of the application and the time of the appeal - (a) or (b)" | none (near: H38) | T12 (near, "needs two dates") | - | not listed |
| G8:4 | 34(1) and 35(1) state the ground of two appeals differently | none (near: H37, on 35(1)) | none | - | partly |
| G8:6 | 33(2)(a) "to deregister the charity" against 15(3)(a): a deregistration on the charity's own application | none (near: H14, on 33(2)(a)) | none | - | not listed |
| G8:7 | 27(4) names notices under (1)(c) and (d); 27(2) lets any notice require steps; 28(3) voids a removal requirement without that limit | none (near: H2) | none | - | partly |
| G8:9 | 26(1)'s demand has one purpose, 26(10)'s offence has two, and applicants are not within 26(2) | partial (H20 and H21) | T23 | - | not listed |
| G8:11 | 31(b), (c) permit disclosure to the Comptroller and the JFSC for "any" function, while 30(1), (2) oblige it only for tax and NPO functions | none (near: H23 and H24, on Art 31) | none | N | listed |
| G8:12 | 36(2)(b) and 11(8)(a)(ii) both let the Minister make an Order about notice of decisions | none (near: H38, on 36(2)) | none | - | partly |
| G8:13 | 33(5)(b) "the registered name of the applicant" at the time of the application: 12(2)(a) gives a registered name only on registration | none (near: H15 and H38, on 33(5)) | none | - | partly |
| G8:14 | 27(1)(d) "unfit to be a governor" against 20(4) "unfit to be concerned in the management" | none | none | - | listed |
| G8:15 | 28(1) "categorized" against 28(2)(a) "status" | none | none | - | listed |
| G8:16 | 26(9) excepts "proceedings under paragraph (7)", although a statement made in compliance cannot itself be the contravention | none | none | - | listed |
| G8:17 | 31(d) lists "the Attorney General, the Bailiff or the court"; the Bailiff presides over the court | none | none | X | listed |
| G8:18 | 27(2) "in Commissioner's opinion" lacks "the" | none | none | X | listed |
| G9:2 | Sch 1 4(12) says "paragraph (11)" for a sub-paragraph | partial (H53, the 4(12) limb) | none | X | not listed |
| G9:3 | Sch 1 4(3)(b) reserves "whether to refuse" under 15(3), not the grant | none | T17 | - | listed |
| G9:4 | Sch 1 4(3)(a) "the decision under Article 11" against Art 9, which decides entry in the restricted section, and 33(1)(b) | none (near: H14) | T17 (near, same paragraph) | - | partly |
| G9:5 | Sch 2 3(2) "at least one member of staff" against "the responsible officer" in 3(3)-(5) | none | none | - | listed |
| G9:6 | Sch 2 says "vacates that position" and "resigns from office"; Sch 1 says "office" | none | none | N | listed |
| G9:7 | 29(1) binds "a person who receives" information, which includes the Commissioner (the survey said not) | partial (H24) | none | N | n/a |
| G9:8 | Independence (Sch 1 2(2)) against the Minister's powers of appointment, termination and direction | none | none | N | listed |
| G9:9 | A period of "not more than 6 years" that cannot be completed because 12 years of service are reached first | none (near: H39) | T21 | N | partly |
| G9:10 | Sch 2 1(8) "as Minister sees fit" lacks "the" | none | none | X | listed |

Row count: 78 (66 with no relation to any hunt finding, 12 partial).
The 12 partial rows are G1:C16, G2:C10, G3:1, G4:C4, G5:2, G5:6, G7:C3, G7:C13, G7:C14, G8:9, G9:2, G9:7.

## 5. The eight "blocks a decision" findings

The hunt's severity "blocks a decision" means the Law gives no answer, or gives two commands that cannot both be obeyed.

| id | what the hunt says blocks the decision | found by S (trap) | found by E (§6 item) | status |
| --- | --- | --- | --- | --- |
| H1 | the Commissioner must register an applicant whose governor is unfit (11(4)), must not grant (19(9)(c)), and must say it will be refused (19(9)(e)(i)) | T10 (case A) | G4:C1, G6:1 | both |
| H2 | the mandatory notice to remove a governor is invalid for an organized religious charity (19(9)(e)(i) against 28(3)) | T11 | G6:2, G8:8 | both |
| H3 | the duties to register or refuse arise only once the applicant complies, so an incomplete application gets no decision and no appeal | T10 (case B) | G4:C2 (P: G4:C4) | both, on the application limb only |
| H4 | the annual return has no due date and no defined year | T24 | G5:10 | both, on the year limb only |
| H5 | no route from the restricted section back to the general section | none | none | hunt-only |
| H6 | a governor the court finds fit has no permission and commits an offence by acting | none | none | hunt-only |
| H7 | deregistering an entity that no longer exists needs notice to a person who may not exist | none | none | hunt-only |
| H8 | six offences carry "a fine" and three "level 3"; the Law states no amount | none | none | hunt-only |

Four of the eight (H1 to H4) were found by the surveyor and by at least one encoder; four (H5 to H8) by neither list as counted.
For H3 the matched limb is the application for registration; the deregistration limb has two parts: no duty to decide when 15(2) is not complied with, which is in neither list (the PLAN's fork F6.1 and G6's fork F6.1 ask it, outside the traps and outside §6), and the missing appeal against a refusal to deregister, which S and E raise and which is matched under H14 (T12, G6:13, G8:5).
For H4 the due-date limb is in neither list; PLAN section 9 item 5 names the annual return's due date as something the sources do not answer (outside the traps).
H5, H7 and H8 are raised outside the counted sets, and H6 is raised in none of the places I searched (the PLAN and all nine FRAGMENTs, by keyword): H5 by G3 §7 question 8, H7 by G6 §7 question 4, H8 by PLAN section 9 item 6, G6 §8 item 5 and G8 §8 item 1 (each files the missing maximum as a gap in the sources).
See section 6 for the effect of admitting them.

## 6. Notes the lead may want

**Disagreements, as against omissions.**
The hunt lists provisions it "read in full and found clean".
Against that list, four of the five traps the hunt did not find (T17, T18, T19, T27) are points on provisions the hunt records as clean, and 16 of the 36 unlabelled, substantive encoder items with no relation to a hunt finding are too (listed in 1.3).
I have not judged who is right; the readings are in the three documents.
The list is not exclusive of the hunt's own findings (it lists 13(3) and 5(1), which H10 cites), so a "clean" entry shows only that the hunt wrote nothing about the point.

**A matched point read in opposite ways.**
H3 and G4:C2 ask the same question about 11(4) and 11(5) and read 11(5) oppositely: the hunt reads "If not so satisfied" as continuing the condition of 11(4), G4:C2 reads it as the whole condition of the duty to refuse.
T10 case B reads like the hunt ("neither duty arises").

**The hunt had fewer instruments than the encoders.**
The hunt says it read eight instruments in `inputs/amending/`; the directory now holds ten, adding `RO-029-2021.txt` and `RO-136-2019.txt` (both written at 13:25:43 on 14 October, 77 seconds after `CONTRADICTIONS.md` was last written at 13:24:26).
The hunt's H9 and its list of what it could not check say R&O.29/2021 and R&O.136/2019 are not in the sources, which was true of its inputs; G7:C15 says both are now among the inputs.
T29 and G7:C16 concern the third item of that list, the Act appointing 16 December 2019, which is still not among the sources.

**Four cosmetic hunt findings are matched by both other lists.**
The hunt rates H49, H53, H54 and H55 cosmetic; each is matched by both S and E.
For H49 the hunt gives a case (a conviction in August 2018 for fraud against a UK charity) but concludes that the result does not change, because the 2(10)(b) limb on foreign equivalents "very probably catches it anyway"; T30, G6:11 and G7:C7 present a conviction on 1 July 2018 of an offence in relation to an excepted foreign charity as a case that matters.

**Text checks agree.**
The hunt's word-for-word diff of the consolidated text against the PDF text layer found only heading capitals and endnote markers.
G1 (1,950 tokens), G3 (Articles 8 to 10), G4 (1,354 words) and G7 (Articles 21 to 25 and 37 to 43) report the same comparison on their Articles with the same result; no list reports a transcription difference.

**Items from outside the counted sets that would change a status if admitted.**
These are points the PLAN's forks or sections, or an encoder's forks or open questions, raise and which ask the hunt's question.
I read each only as far as the lines cited, and the lead said not to rely on G2's and G7's forks, so treat the G2 and G7 pointers as possibly moved.

| finding | where it is raised outside the counted sets | status now | status if admitted |
| --- | --- | --- | --- |
| H5 | G3 §7 question 8 (is a charity ever moved from the restricted section back to the general section) | hunt-only | E-only |
| H7 | G6 §7 question 4 (to whom is the written notice given if nobody purports to be a governor) | hunt-only | E-only |
| H8 | PLAN section 9 item 6; G6 §8 item 5; G8 §8 item 1 (each: the Law states no maximum for "a fine"; filed as a gap in the sources) | hunt-only | both |
| H22 | G8 fork F8.11 (which consents 29(1) requires) | hunt-only | E-only |
| H30 | G3 fork F3.11 (8(5)(b): the case of a charity moved to the restricted section and then deregistered) | hunt-only | E-only |
| H39 | PLAN F9.3 and F9.11; G9 forks F9.3 and F9.11 (both limbs: when a resignation takes effect; whether designated-person service counts toward 12 years) | hunt-only | both |
| H12 | PLAN F1.2; G1 fork F1.2 (the "in relation to" question, naming 19(1)(g)) | partial | both |
| H18 | PLAN F1.1; G1 fork F1.1 (does "(a) to (h)" reach (ba)) | E-only | both |
| H40 | G7 fork F7.1 (the 9.30 a.m. question) | S-only | both |

Admitting all nine would give both 25, S-only 0, E-only 10, partial 7, hunt-only 13.
Points that touch a finding without asking its question, and would change no status: H3 deregistration limb (PLAN F6.1, G6 F6.1); H4 due date (PLAN section 9 item 5); H23 (G2 fork F2.8, which asks whether 4(3)(c) assistance needs a Commissioner function); H31 (G3 §7 questions 9 and 13 take the Order's content as an input); H33 other limbs (PLAN F8.1, F6.14, F4.1; G8 F8.1, G6 F6.14, G4 F4.1); H38 (G8 fork F8.6, from when a limit runs); H42 (PLAN F9.9); H45 (G3 §4 request 3 and §5.3, whose rule returns every governor's address); H47 (G9 answers the quorum question with a named refusal); H48 (PLAN F7.7 and G7 F7.7, which date of service).

**G2 and G7: the second read.**
I snapshotted both files at 01:57 on 27 October (first read; G2 and G7 had last been written at 23:37 and 23:40 on 26 October) and compared them again at 02:19 and at the end.

- G2 changed at 02:19:43 on 27 October.
  Its section 6 gained one item, C10 (Schedule 1 paragraph 4(3) against 7(1) and 5(5): a staff determination escapes 7(3)(b); registered as fork F2.13), and C1 to C9 are unchanged.
  I added C10 to the tables at once: it is P for H43, which moves H43 from hunt-only to partial and the G2 count from 9 to 10.
  G2 also gained a section 11, "Changes after independent testing", which is not part of set E.
- G7 changed at 02:10:05 on 27 October (a new section 10, "Changes after independent testing", and edits to sections 0 to 5 and 7 to 9).
  Its section 6 is item for item the same except C8, which now says Part 8 has two stages and Part 9 three (it adds the spent original Article 41); it is the same point, its row in Table C is updated, and no count moves.
- The other seven FRAGMENTs were last written between 23:32 and 23:56 on 26 October and have not changed since my first read.

Snapshots of the first and the latest section 6 of G2 and G7 are kept in `work/overlap/snap/` (`G2-sec6-first.txt`, `G2-sec6-now.txt`, `G7-sec6-first-full.txt`, `G7-sec6-now.txt`).
I did not open the independent test authors' directories or the integrator's; G7's own "Peeked" section says G7 opened some of their files, and I read only G7's text about it.
