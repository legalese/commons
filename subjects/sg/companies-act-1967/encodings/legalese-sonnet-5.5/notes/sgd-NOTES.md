# NOTES (sgd): the Companies Act 1967 (Singapore), Part 7, ss 210 to 215K

Part agent `sgd`.
Range: lines 20183-21697 of `inputs/CoA1967.txt` (Part 7: arrangements, reconstructions and amalgamations, ss 210 to 215K).
Status at the date of the last gate run recorded at the end of this file: layer 1, its tests, the seat layer and its cases are written and pass on both builds; the numbers are in "What check.sh prints".
This file is regenerated from `work/notes/*` by `work/mknotes.py` (`work/` is this part's scratch directory, `RUN/work`, beside the deposit and not part of it; `inputs/` is `RUN/inputs`); the coverage table, the fork register, the jural-relations rule column, the marginal-reading tables, the no-breach table and the seat table are generated from the deposited files and the text, never typed.

## Edition encoded

- The Companies Act 1967, 2020 Revised Edition, as the Singapore Statutes Online (SSO) informal consolidation "version in force from 6/5/2026 to 20/10/2026", retrieved 2026-10-09, carrying the amendments up to Act 24 of 2025.
- The file is `inputs/CoA1967.txt` (sha256 `ea9501a3e0829a46b396aa6cb5e7369fc8c1f4c2288ede5748cf3e62c6284303`, as `inputs/SOURCES.md` records it): a PDF turned into plain text by a converter script.
  It is a rendering, not the official text (SSO's terms, clause 8), and nothing in this encoding is "verified against the official text".
  Every line number in this folder is a line of that file as it is.
- A later consolidation may exist and was not read.
  The encoding is of this text only.
- Amendment marks (`[36/2014]`, `[Act 24 of 2025 wef 06/05/2026]`) and page furniture (`Informal Consolidation - version in force ...`, `2020 Ed. Companies Act 1967 <page>`) are not text and are not quoted as rules.
  The quotations in the layer-1 files are copied from the file by `work/gen.py` (the `-- src:` lines); none is typed.
  Where a provision runs across a page break, its two halves are two quotation runs.
- Nothing here suggests that the Singapore Government or the Attorney-General's Chambers endorses, checks or is associated with this work.

## The brief governs over PLAN.md

`inputs/PLAN.md` section 6 gives this part two instructions that this encoding does not follow to the letter, and the brief (`BRIEF.md`) governs where it differs:

1. **Group functions.** The plan row says the part takes "the group functions (including 5B)" and names `s 5B the corporation is a wholly owned subsidiary of the other corporation` and `s 5(1) ...`.
   Layer 1 calls neither.
   Section 215D asks whether the amalgamating companies are "a company and one or more of its wholly-owned subsidiaries" (215D(1)) or "two or more wholly-owned subsidiary companies of the same corporation" (215D(2)).
   The keel's `s 5B ...` function takes one subsidiary's members, listed by kind (`s 5B member`), and answers for that subsidiary; it does not answer a question about a set of amalgamating companies, and the plan itself says a part that needs "being a subsidiary" must also ask `s 5(1)`.
   So the fact is a plain `BOOLEAN` input named for the fact (`the amalgamating companies are a company and one or more of its wholly-owned subsidiaries`).
   This is a decision of this pass, assumed and not ruled; calling the keel from those two functions would be the change.
2. **"Associate".** The plan row points at `s 7(5)` for "associate" in the compulsory-acquisition provisions.
   The range contains no occurrence of "associate" (checked: `sed -n '20183,21697p' inputs/CoA1967.txt | grep -n -i associate` prints nothing).
   Section 215(9A) names its own persons (those accustomed to act on the transferee's directions, the transferee's spouse, parent, brother, sister, son, adopted son, stepson, daughter, adopted daughter or stepdaughter, those whose directions the transferee is accustomed to act on, and bodies corporate controlled by any of them), and layer 1 encodes those words; no keel function is called for it.

The keel functions layer 1 does call are `s 4(1) "officer" ...` and `s 4(1) "unit" ...` (`sg-definitions`), `s 4(1) "related corporation" the other corporation is a related corporation of the corporation` (`sg-groups`, the one-fact form), `Kind of resolution` and `Kind of meeting` (`sg-core`), and the `period:` functions of `sg-periods` (the keel's counting conventions P1 to P9, set out at the head of `sg-periods.l4`; every period in the range is counted through them, never by hand).

## Coverage (sgd)

One row per unit the script found in lines 20183-21697: a section, a subsection, a paragraph, a sub-paragraph, a defined term, a heading, or a line the text shows as repealed.
`work/units.py` finds the units from the text (their labels at the start of lines, the section numbers in the body, never the arrangement of sections at the head of the file), and `work/coverage.py` gives each exactly one disposition from what layer 1 does with it: its `@ref` blocks name the lines they cite, and each block carries the fork ids and the function names that the row shows.
The script then checks that the rows partition the range.

**Audit counts.**
- Lines in the range: 1515; non-blank lines: 1091; non-blank lines that fall in no row, or in more than one: 0.
- Units found by the script: 310 (19 headings, 17 sections, 101 subsections, 138 paragraphs, 24 sub-paragraphs, 6 repealeds, 5 defined terms); a row may hold two units, a section and its subsection (1), so there are 295 rows.
- Rows before the paragraph-level split: 124 (one row per distinct section or subsection key); rows after: 295.
- Dispositions: encoded 158, fork 112, inert 19, repealed or blank in this text 6.
  Every `encoded` and `fork` row names a layer-1 function (none is without one); a `fork` row also names its fork-register entries.
- Every `inert` row is reason 1 (not operative): the Part heading; the heading "Amalgamations", which stands over ss 215A to 215K; the marginal headings of ss 210, 211, 212, 215, 215AA, 215AB and 215B to 215K (s 215A has none); and the heading "Power of Court to restrain proceedings" inside s 210.
  No row is inert under reason 2 or 3, and no row is "out of scope" or "deferred".
- The six `repealed or blank` rows are ss 210(3A), 210(4A), 211A to 211J, 212(1A), 213 and 214, each as the text shows it.

The `seat` column is the number of the seat question (section "Seat layer (sgd)") that asks the rule.

| lines | unit | disposition | forks | layer-1 name | seat |
| --- | --- | --- | --- | --- | --- |
| 20183-20187 | Part 7 heading: "ARRANGEMENTS, RECONSTRUCTIONS AND AMALGAMATIONS" | inert (reason 1: not operative) |  |  |  |
| 20188-20190 | marginal heading of s 210: "Power to compromise with creditors, members and holders of units of shares" | inert (reason 1: not operative) |  |  |  |
| 20191-20193 | 210 ; 210(1) | fork | F-210-2 | `s 210(1) the Court may order a meeting to be summoned` | Q2 |
| 20194-20195 | 210(1)(a) | fork | F-210-2 | `s 210(1) the Court may order a meeting to be summoned` | Q2 |
| 20196-20197 | 210(1)(b) | fork | F-210-2 | `s 210(1) the Court may order a meeting to be summoned` | Q2 |
| 20198-20208 | 210(1)(c) | fork | F-210-2 | `s 210(1) the Court may order a meeting to be summoned` | Q2 |
| 20209-20210 | 210(2) | fork | F-210-1 | `s 210(2) the person is a person referred to in subsection (1)` | Q1 |
| 20211-20213 | 210(2)(a) | fork | F-210-1 | `s 210(2) the person is a person referred to in subsection (1)` | Q1 |
| 20214-20215 | 210(2)(b) | fork | F-210-1 | `s 210(2) the person is a person referred to in subsection (1)` | Q1 |
| 20216-20217 | 210(2)(b)(i) | fork | F-210-1 | `s 210(2) the person is a person referred to in subsection (1)` | Q1 |
| 20218-20222 | 210(2)(b)(ii) | fork | F-210-1 | `s 210(2) the person is a person referred to in subsection (1)` | Q1 |
| 20223-20227 | 210(3) | fork | F-210-5 | `s 210(3) the meeting may be adjourned` | Q3 |
| 20228-20229 | 210(3)(a) | fork | F-210-5 | `s 210(3) the meeting may be adjourned` | Q3 |
| 20230-20234 | 210(3)(b) | fork | F-210-5 | `s 210(3) the meeting may be adjourned` | Q3 |
| 20235-20241 | 210(3)(c) | fork | F-210-5 | `s 210(3) the meeting may be adjourned` | Q3 |
| 20242-20244 | 210(3AA) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20245-20248 | 210(3AA)(a) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20249-20250 | 210(3AA)(a)(i) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20251-20255 | 210(3AA)(a)(ii) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20256-20257 | 210(3AA)(a) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20258-20260 | 210(3AA)(b) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20261-20262 | 210(3AA)(b)(i) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20263-20267 | 210(3AA)(b)(ii) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20268-20271 | 210(3AA)(b) | encoded |  | `s 210(3AA) the compromise or arrangement is binding on the party` | Q5 |
| 20272-20274 | 210(3AB) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20275-20277 | 210(3AB)(a) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20278-20279 | 210(3AB)(a)(i) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20280-20287 | 210(3AB)(a)(ii) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20288-20291 | 210(3AB)(a) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20292-20295 | 210(3AB)(b) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20296-20297 | 210(3AB)(b)(i) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20298-20302 | 210(3AB)(b)(ii) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20303-20305 | 210(3AB)(b) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20306-20310 | 210(3AB)(c) | fork | F-210-6 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | Q4 |
| 20311-20312 | the text shows "(3A) [Deleted by Act 40 of 2018]" | repealed or blank in this text |  |  |  |
| 20313-20317 | 210(4) | fork | F-210-7 | `s 210(4) the Court may grant its approval subject to the alteration or condition` | Q6 |
| 20318-20319 | the text shows "(4A) [Deleted by Act 40 of 2018]" | repealed or blank in this text |  |  |  |
| 20320-20326 | 210(5) | fork | F-210-8 | `s 210(5) the order cannot yet have effect` (+1 more) | Q7, Q8 |
| 20327-20332 | 210(6) | fork | F-210-9 | `s 210(6) the company must annex a copy of the order to every copy of the constitution issued af...` (+1 more) | Q9 |
| 20333-20336 | 210(7) | fork | F-210-12 | `s 210(7) the Court may do it by order` | Q10 |
| 20337-20345 | 210(8) | encoded |  | `s 210(8)(a) the directors must instruct the accountants or solicitors named in the resolution t...` (+3 more) | Q11, Q12 |
| 20346-20351 | 210(8)(a) | encoded |  | `s 210(8)(a) a director must instruct the accountants or solicitors named in the resolution to r...` (+3 more) | Q11, Q12 |
| 20352-20359 | 210(8)(b) | encoded |  | `s 210(8)(b) the reports have been made available at least 7 days before the meeting` (+3 more) | Q11, Q12 |
| 20360-20364 | 210(9) | fork | F-210-10 | `s 210(9) the company is guilty of the offence` (+2 more) | Q13, Q14, Q15 |
| 20365-20366 | marginal heading before s 210(10): "Power of Court to restrain proceedings" | inert (reason 1: not operative) |  |  |  |
| 20367-20380 | 210(10) | fork | F-210-2 | `s 210(10) the Court may restrain further proceedings against the company` (+1 more) | Q16, Q17 |
| 20381-20395 | 210(10A) | fork | F-210-11 | `s 210(10A) the transfer to the Official Receiver is within the time the subsection allows` (+1 more) | Q18 |
| 20396-20397 | 210(10B) | encoded |  | `s 210(10B) how the Official Receiver must deal with what is received` (+2 more) | Q19 |
| 20398-20402 | 210(10B)(a) | encoded |  | `s 210(10B) how the Official Receiver must deal with what is received` (+2 more) | Q19 |
| 20403-20411 | 210(10B)(b) | encoded |  | `s 210(10B)(b) the Official Receiver must sell or dispose of the other consideration` (+2 more) | Q19 |
| 20412-20413 | 210(11) | encoded |  | `s 210(11) "arrangement" the thing is within the word arrangement` (+2 more) | Q20, Q21, Q22 |
| 20414-20418 | 210(11) "arrangement" | encoded |  | `s 210(11) "arrangement" the thing is within the word arrangement` (+2 more) | Q20, Q21, Q22 |
| 20419-20421 | 210(11) "company" | encoded |  | `s 210(11) "company" the body is a company` (+2 more) | Q20, Q21, Q22 |
| 20422-20426 | 210(11) "holder of units of shares" | encoded |  | `s 210(11) "holder of units of shares" the person is a holder of units of shares` (+2 more) | Q20, Q21, Q22 |
| 20427-20429 | marginal heading of s 211: "Information as to compromise with creditors, members and holders of units of shares of company" | inert (reason 1: not operative) |  |  |  |
| 20430-20432 | 211 ; 211(1) | encoded |  | `s 211(1) the notice carries what the subsection requires` | Q23 |
| 20433-20446 | 211(1)(a) | encoded |  | `s 211(1) the notice carries what the subsection requires` | Q23 |
| 20447-20455 | 211(1)(b) | encoded |  | `s 211(1) the notice carries what the subsection requires` | Q23 |
| 20456-20461 | 211(2) | encoded |  | `s 211(2) the statement gives what the subsection requires` | Q24 |
| 20462-20470 | 211(3) | encoded |  | `s 211(3) the company must furnish the person with a copy of the statement free of charge` | Q25 |
| 20471-20476 | 211(4) | encoded |  | `s 211(4) the director or trustee gave notice within 7 days of the receipt of the request` (+1 more) | Q26 |
| 20477-20482 | 211(5) | fork | F-211-1 | `s 211(5) the company is guilty of the offence` (+2 more) | Q27, Q30, Q31, Q32 |
| 20483-20489 | 211(6) | encoded |  | `s 211(6) the person is deemed to be an officer of the company for subsection (5)` | Q28 |
| 20490-20494 | 211(7) | fork | F-211-1 | `s 211(7) the section gives the person a defence` (+1 more) | Q29, Q31 |
| 20495-20496 | the text shows "211A. to 211J. [Repealed by Act 40 of 2018]" | repealed or blank in this text |  |  |  |
| 20497-20498 | marginal heading of s 212: "Approval of compromise or arrangement by Court" | inert (reason 1: not operative) |  |  |  |
| 20499-20512 | 212 ; 212(1) | fork | F-212-1 | `s 212(1) the Court may provide for the matter by its order` | Q33 |
| 20513-20516 | 212(1)(a) | fork | F-212-1 | `s 212(1) the Court may provide for the matter by its order` | Q33 |
| 20517-20522 | 212(1)(b) | fork | F-212-1 | `s 212(1) the Court may provide for the matter by its order` | Q33 |
| 20523-20526 | 212(1)(c) | fork | F-212-1 | `s 212(1) the Court may provide for the matter by its order` | Q33 |
| 20527-20532 | 212(1)(d) | fork | F-212-1 | `s 212(1) the Court may provide for the matter by its order` | Q33 |
| 20533-20536 | 212(1)(e) | fork | F-212-1 | `s 212(1) the Court may provide for the matter by its order` | Q33 |
| 20537-20542 | 212(1)(f) | fork | F-212-1 | `s 212(1) the Court may provide for the matter by its order` | Q33 |
| 20543-20544 | the text shows "(1A) [Deleted by Act 40 of 2018]" | repealed or blank in this text |  |  |  |
| 20545-20551 | 212(2) | encoded |  | `s 212(2) the property vests in the transferee company and the liabilities become its liabilitie...` (+1 more) | Q34, Q35 |
| 20552-20555 | 212(3) | fork | F-212-2 | `s 212(3) the lodgment was made within 7 days of the making of the order` (+5 more) | Q36, Q37, Q38, Q39, Q40 |
| 20556-20557 | 212(3)(a) | fork | F-212-2 | `s 212(3) the lodgment was made within 7 days of the making of the order` (+5 more) | Q36, Q37, Q38, Q39, Q40 |
| 20558-20566 | 212(3)(b) | fork | F-212-2 | `s 212(3) the lodgment was made within 7 days of the making of the order` (+5 more) | Q36, Q37, Q38, Q39, Q40 |
| 20567-20571 | 212(4) | encoded |  | `s 212(4) the vesting order cannot yet have effect in vesting the land` | Q41 |
| 20572-20573 | 212(5) | encoded |  | `s 212(5) "liabilities" the thing is within the word liabilities` (+1 more) | Q42, Q43 |
| 20574-20575 | 212(5) "liabilities" | encoded |  | `s 212(5) "liabilities" the thing is within the word liabilities` (+1 more) | Q42, Q43 |
| 20576-20581 | 212(5) "property" | encoded |  | `s 212(5) "property" the thing is within the word property` (+1 more) | Q42, Q43 |
| 20582-20587 | 212(6) | encoded |  | `s 212(6) "company" the body is a company` | Q44 |
| 20588-20589 | the text shows "213. [Repealed by S 675/2001]" | repealed or blank in this text |  |  |  |
| 20590-20591 | the text shows "214. [Repealed by S 675/2001]" | repealed or blank in this text |  |  |  |
| 20592-20594 | marginal heading of s 215: "Power to acquire shares of shareholders dissenting from scheme or contract approved by 90% majority" | inert (reason 1: not operative) |  |  |  |
| 20595-20621 | 215 ; 215(1) | fork | F-215-3, F-215-4, F-215-5, F-215-6, F-215-7 | `s 215(1) the last day of one month from the date on which the notice was given` (+6 more) | Q45, Q46, Q47, Q48, Q49, Q50, Q51 |
| 20622-20634 | 215(1A) | fork | F-215-7 | `s 215(1A) the dissenting shareholder is entitled to elect which of the terms the shareholder pr...` | Q52 |
| 20635-20642 | 215(1B) | encoded |  | `s 215(1B) the transferee has stated which of the terms is to apply on a failure to elect` (+1 more) | Q53 |
| 20643-20646 | 215(1C) | encoded |  | `s 215(1C)(a) the shares are to be disregarded` (+1 more) | Q54, Q56 |
| 20647-20652 | 215(1C)(a) | encoded |  | `s 215(1C)(a) the shares are to be disregarded` (+1 more) | Q54, Q56 |
| 20653-20657 | 215(1C)(b) | encoded |  | `s 215(1C)(b) the shares are to be disregarded` (+1 more) | Q54, Q56 |
| 20658-20659 | 215(1D) | encoded |  | `s 215(1D) the shares are relevant treasury shares` | Q55 |
| 20660-20662 | 215(1D)(a) | encoded |  | `s 215(1D) the shares are relevant treasury shares` | Q55 |
| 20663-20669 | 215(1D)(b) | encoded |  | `s 215(1D) the shares are relevant treasury shares` | Q55 |
| 20670-20675 | 215(1E) | encoded |  | `s 215(1E) the subsequent issue of shares affects the matter` | Q57 |
| 20676-20680 | 215(1E)(a) | encoded |  | `s 215(1E) the subsequent issue of shares affects the matter` | Q57 |
| 20681-20683 | 215(1E)(b) | encoded |  | `s 215(1E) the subsequent issue of shares affects the matter` | Q57 |
| 20684-20687 | 215(1E)(c) | encoded |  | `s 215(1E) the subsequent issue of shares affects the matter` | Q57 |
| 20688-20701 | 215(2) | fork | F-215-7, F-215-9 | `s 215(2) the transferor company must supply the dissenting shareholder with the written stateme...` (+2 more) | Q58, Q59 |
| 20702-20708 | 215(3) | fork | F-215-10, F-215-11, F-215-12, F-215-7, F-215-13 | `s 215(3) the shares transferred, together with the other shares held by the transferee, compris...` (+6 more) | Q60, Q62, Q63, Q64, Q65, Q66 |
| 20709-20716 | 215(3)(a) | fork | F-215-10, F-215-11, F-215-12, F-215-7, F-215-13 | `s 215(3)(a) the notice was given within one month from the date of the transfer` (+6 more) | Q60, Q62, Q63, Q64, Q65, Q66 |
| 20717-20733 | 215(3)(b) | fork | F-215-10, F-215-11, F-215-12, F-215-7, F-215-13 | `s 215(3) the transferee is entitled and bound to acquire the shares` (+6 more) | Q60, Q62, Q63, Q64, Q65, Q66 |
| 20734-20740 | 215(3A) | fork | F-215-10 | `s 215(3A) the number of the treasury shares treated as having been acquired by the transferee` | Q61 |
| 20741-20749 | 215(4) | fork | F-215-14 | `s 215(4) the first day on which the transferee must act` (+3 more) | Q67, Q68 |
| 20750-20754 | 215(4)(a) | fork | F-215-14 | `s 215(4) the transferee must transmit a copy of the notice and pay, allot or transfer the consi...` (+3 more) | Q67, Q68 |
| 20755-20764 | 215(4)(b) | fork | F-215-14 | `s 215(4) the transferor company must register the transferee as the holder of the shares` (+3 more) | Q67, Q68 |
| 20765-20772 | 215(5) | encoded |  | `s 215(5) the transferor company must hold the sums and other consideration in trust` (+2 more) | Q69 |
| 20773-20785 | 215(6) | encoded |  | `s 215(6) the transfer to the Official Receiver is within the time the subsection allows` (+1 more) | Q70 |
| 20786-20787 | 215(7) | encoded |  | `s 215(7) how the Official Receiver must deal with what is received under subsection (6)` (+2 more) | Q71 |
| 20788-20792 | 215(7)(a) | encoded |  | `s 215(7) how the Official Receiver must deal with what is received under subsection (6)` (+2 more) | Q71 |
| 20793-20801 | 215(7)(b) | encoded |  | `s 215(7)(b) the Official Receiver must sell or dispose of the other consideration` (+2 more) | Q71 |
| 20802-20808 | 215(8) | encoded |  | `s 215(8) the shareholder is a dissenting shareholder` | Q72 |
| 20809-20816 | 215(8A) | encoded |  | `s 215(8A) the shareholder is within the reference to a shareholder in subsection (8)` | Q73 |
| 20817-20821 | 215(8AA) | encoded |  | `s 215(8AA) the thing is within the word shares` | Q74 |
| 20822-20827 | 215(8AB) | encoded |  | `s 215(8AB) the person is within the word shareholders` | Q75 |
| 20828-20836 | 215(8AC) | encoded |  | `s 215(8AC) the records are within the register of members` | Q76 |
| 20837-20839 | 215(8B) | encoded |  | `s 215(8B) the definition of shares requires the securities to be treated that way` | Q77 |
| 20840-20843 | 215(8B)(a) | encoded |  | `s 215(8B) the definition of shares requires the securities to be treated that way` | Q77 |
| 20844-20852 | 215(8B)(b) | encoded |  | `s 215(8B) the definition of shares requires the securities to be treated that way` | Q77 |
| 20853-20854 | 215(9) | encoded |  | `s 215(9) the shares are to be treated as held or acquired by the transferee` | Q78 |
| 20855-20856 | 215(9)(a) | encoded |  | `s 215(9) the shares are to be treated as held or acquired by the transferee` | Q78 |
| 20857-20863 | 215(9)(b) | encoded |  | `s 215(9) the shares are to be treated as held or acquired by the transferee` | Q78 |
| 20864-20868 | 215(9A) | encoded |  | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | Q79 |
| 20869-20873 | 215(9A)(a) | encoded |  | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | Q79 |
| 20874-20877 | 215(9A)(b) | encoded |  | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | Q79 |
| 20878-20885 | 215(9A)(c) | encoded |  | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | Q79 |
| 20886-20893 | 215(9A)(d) | encoded |  | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | Q79 |
| 20894-20903 | 215(10) | encoded |  | `s 215(10) the shares are shares already held by the transferee within subsection (1)` | Q80 |
| 20904-20908 | 215(11) | encoded |  | `s 215(11) the transferee is to be treated as having acquired the shares by virtue of the approv...` | Q81 |
| 20909-20913 | 215(11)(a) | encoded |  | `s 215(11) the transferee is to be treated as having acquired the shares by virtue of the approv...` | Q81 |
| 20914-20922 | 215(11)(b) | encoded |  | `s 215(11) the transferee is to be treated as having acquired the shares by virtue of the approv...` | Q81 |
| 20923-20926 | 215(12) | encoded |  | `s 215(12) the body corporate is controlled by the transferee or the person` (+1 more) | Q82 |
| 20927-20936 | 215(12)(a) | encoded |  | `s 215(12)(a) the voting power reaches the lower of 50% and the prescribed percentage` (+1 more) | Q82 |
| 20937-20946 | 215(12)(b) | encoded |  | `s 215(12) the body corporate is controlled by the transferee or the person` (+1 more) | Q82 |
| 20947-20948 | marginal heading of s 215AA: "Joint offers" | inert (reason 1: not operative) |  |  |  |
| 20949-20955 | 215AA ; 215AA(1) | encoded |  | `s 215AA(1) section 215 is to be read subject to section 215AA` | Q83 |
| 20956-20958 | 215AA(2) | fork | F-215AA-1 | `s 215AA(2) the conditions for the exercise of the rights conferred by section 215(1) are satisf...` | Q84 |
| 20959-20963 | 215AA(2)(a) | fork | F-215AA-1 | `s 215AA(2) the conditions for the exercise of the rights conferred by section 215(1) are satisf...` | Q84 |
| 20964-20969 | 215AA(2)(b) | fork | F-215AA-1 | `s 215AA(2) the conditions for the exercise of the rights conferred by section 215(1) are satisf...` | Q84 |
| 20970-20972 | 215AA(3) | fork | F-215AA-1 | `s 215AA(3) the conditions for the exercise of the rights conferred by section 215(3) are satisf...` | Q85 |
| 20973-20977 | 215AA(3)(a) | fork | F-215AA-1 | `s 215AA(3) the conditions for the exercise of the rights conferred by section 215(3) are satisf...` | Q85 |
| 20978-20988 | 215AA(3)(b) | fork | F-215AA-1 | `s 215AA(3) the conditions for the exercise of the rights conferred by section 215(3) are satisf...` | Q85 |
| 20989-20994 | 215AA(4) | encoded |  | `s 215AA(4) how the joint transferees hold what section 215 gives the transferee` | Q86 |
| 20995-21000 | 215AA(5) | encoded |  | `s 215AA(5) the notice or document is complied with` | Q87 |
| 21001-21007 | 215AA(6) | encoded |  | `s 215AA(6) the notice is made as the subsection requires` (+1 more) | Q88 |
| 21008-21010 | marginal heading of s 215AB: "Effect of impossibility, etc., of communicating or accepting offer made under scheme or contract" | inert (reason 1: not operative) |  |  |  |
| 21011-21015 | 215AB ; 215AB(1) | fork | F-215AB-1 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made unde...` | Q89 |
| 21016-21018 | 215AB(1)(a) | fork | F-215AB-1 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made unde...` | Q89 |
| 21019-21020 | 215AB(1)(b) | fork | F-215AB-1 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made unde...` | Q89 |
| 21021-21023 | 215AB(1)(b)(i) | fork | F-215AB-1 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made unde...` | Q89 |
| 21024-21026 | 215AB(1)(b)(ii) | fork | F-215AB-1 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made unde...` | Q89 |
| 21027-21028 | 215AB(1)(c) | fork | F-215AB-1 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made unde...` | Q89 |
| 21029-21030 | 215AB(1)(c)(i) | fork | F-215AB-1 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made unde...` | Q89 |
| 21031-21041 | 215AB(1)(c)(ii) | fork | F-215AB-1 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made unde...` | Q89 |
| 21042-21049 | 215AB(2) | encoded |  | `s 215AB(2) the impossibility or difficulty of accepting the offer does not prevent it from bein...` | Q90 |
| 21050-21051 | 215AB(3) | encoded |  | `s 215AB(3)(a) it is to be inferred that the offer cannot be an offer made under a scheme or con...` (+1 more) | Q91, Q92 |
| 21052-21057 | 215AB(3)(a) | encoded |  | `s 215AB(3)(a) it is to be inferred that the offer cannot be an offer made under a scheme or con...` (+1 more) | Q91, Q92 |
| 21058-21065 | 215AB(3)(b) | encoded |  | `s 215AB(3)(b) it is to be inferred that the offer cannot be an offer made under a scheme or con...` (+1 more) | Q91, Q92 |
| 21066-21067 | heading of ss 215A to 215K: "Amalgamations" | inert (reason 1: not operative) |  |  |  |
| 21068-21073 | 215A | fork | F-215A-1 | `s 215A the companies may amalgamate and continue as one company` | Q93, Q94 |
| 21074-21075 | marginal heading of s 215B: "Amalgamation proposal" | inert (reason 1: not operative) |  |  |  |
| 21076-21078 | 215B ; 215B(1) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21079-21080 | 215B(1)(a) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21081-21082 | 215B(1)(b) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21083-21088 | 215B(1)(c) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21089-21095 | 215B(1)(ca) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21096-21098 | 215B(1)(d) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21099-21100 | 215B(1)(d)(i) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21101-21108 | 215B(1)(d)(ii) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21109-21110 | 215B(1)(e) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21111-21114 | 215B(1)(f) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21115-21119 | 215B(1)(g) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21120-21123 | 215B(1)(h) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21124-21129 | 215B(1)(i) | encoded |  | `s 215B(1) the amalgamation proposal contains what the subsection requires` | Q95 |
| 21130-21132 | 215B(2) | fork | F-215B-1 | `s 215B(2) the amalgamation proposal may specify the date` | Q96 |
| 21133-21139 | 215B(3) | encoded |  | `s 215B(3) the amalgamation proposal provides as the subsection requires` | Q97 |
| 21140-21143 | 215B(3)(a) | encoded |  | `s 215B(3) the amalgamation proposal provides as the subsection requires` | Q97 |
| 21144-21146 | 215B(3)(b) | encoded |  | `s 215B(3) the amalgamation proposal provides as the subsection requires` | Q97 |
| 21147-21149 | 215B(4) | encoded |  | `s 215B(4) the cancellation of the shares is deemed to be a reduction of share capital within th...` | Q98 |
| 21150-21152 | 215B(5) | fork | F-215B-2 | `s 215B(5) the name may be the name of the amalgamated company` | Q99 |
| 21153-21154 | 215B(5)(a) | fork | F-215B-2 | `s 215B(5) the name may be the name of the amalgamated company` | Q99 |
| 21155-21158 | 215B(5)(b) | fork | F-215B-2 | `s 215B(5) the name may be the name of the amalgamated company` | Q99 |
| 21159-21160 | marginal heading of s 215C: "Manner of approving amalgamation proposal" | inert (reason 1: not operative) |  |  |  |
| 21161-21162 | 215C ; 215C(1) | encoded |  | `s 215C(1) the amalgamation proposal has been approved as the subsection requires` | Q100 |
| 21163-21166 | 215C(1)(a) | encoded |  | `s 215C(1) the amalgamation proposal has been approved as the subsection requires` | Q100 |
| 21167-21174 | 215C(1)(b) | encoded |  | `s 215C(1) the amalgamation proposal has been approved as the subsection requires` | Q100 |
| 21175-21177 | 215C(2) | fork | F-215C-1 | `s 215C(2) the day is before the day of the general meeting` (+6 more) | Q101, Q102, Q103 |
| 21178-21180 | 215C(2)(a) | fork | F-215C-1 | `s 215C(2) the day is before the day of the general meeting` (+6 more) | Q101, Q102, Q103 |
| 21181-21183 | 215C(2)(b) | fork | F-215C-1 | `s 215C(2) the day is before the day of the general meeting` (+6 more) | Q101, Q102, Q103 |
| 21184-21189 | 215C(2)(c) | fork | F-215C-1 | `s 215C(2) the day is before the day of the general meeting` (+6 more) | Q101, Q102, Q103 |
| 21190-21193 | 215C(3) | encoded |  | `s 215C(3) the director must sign the declaration` (+2 more) | Q104, Q105 |
| 21194-21198 | 215C(3)(a) | encoded |  | `s 215C(3) the director must sign the declaration` (+2 more) | Q104, Q105 |
| 21199-21200 | 215C(3)(b) | encoded |  | `s 215C(3) the director must sign the declaration` (+2 more) | Q104, Q105 |
| 21201-21204 | 215C(4) | encoded |  | `s 215C(4) the board sent what the subsection requires to every member at least 21 days before t...` (+1 more) | Q106 |
| 21205-21206 | 215C(4)(a) | encoded |  | `s 215C(4) the board sent what the subsection requires to every member at least 21 days before t...` (+1 more) | Q106 |
| 21207-21209 | 215C(4)(b) | encoded |  | `s 215C(4) the board sent what the subsection requires to every member at least 21 days before t...` (+1 more) | Q106 |
| 21210-21212 | 215C(4)(c) | encoded |  | `s 215C(4) the board sent what the subsection requires to every member at least 21 days before t...` (+1 more) | Q106 |
| 21213-21218 | 215C(4)(d) | encoded |  | `s 215C(4) the board sent what the subsection requires to every member at least 21 days before t...` (+1 more) | Q106 |
| 21219-21222 | 215C(5) | encoded |  | `s 215C(5)(a) the directors sent the amalgamation proposal to every secured creditor at least 21...` (+3 more) | Q107, Q108 |
| 21223-21225 | 215C(5)(a) | encoded |  | `s 215C(5)(a) the directors sent the amalgamation proposal to every secured creditor at least 21...` (+3 more) | Q107, Q108 |
| 21226-21229 | 215C(5)(b) | encoded |  | `s 215C(5)(a) the directors sent the amalgamation proposal to every secured creditor at least 21...` (+3 more) | Q107, Q108 |
| 21230-21240 | 215C(5)(b)(i) | encoded |  | `s 215C(5)(a) the directors sent the amalgamation proposal to every secured creditor at least 21...` (+3 more) | Q107, Q108 |
| 21241-21245 | 215C(5)(b)(ii) | encoded |  | `s 215C(5)(a) the directors sent the amalgamation proposal to every secured creditor at least 21...` (+3 more) | Q107, Q108 |
| 21246-21248 | 215C(6) | fork | F-215C-2 | `s 215C(6) the director is guilty of the offence` | Q109 |
| 21249-21250 | marginal heading of s 215D: "Short form amalgamation" | inert (reason 1: not operative) |  |  |  |
| 21251-21260 | 215D ; 215D(1) | fork | F-215D-1 | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate wit...` | Q110, Q111 |
| 21261-21262 | 215D(1)(a) | fork | F-215D-1 | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate wit...` | Q110, Q111 |
| 21263-21267 | 215D(1)(a)(i) | fork | F-215D-1 | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate wit...` | Q110, Q111 |
| 21268-21285 | 215D(1)(a)(ii) | fork | F-215D-1 | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate wit...` | Q110, Q111 |
| 21286-21289 | 215D(1)(b) | fork | F-215D-1 | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate wit...` | Q110, Q111 |
| 21290-21295 | 215D(1)(c) | fork | F-215D-1 | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate wit...` | Q110, Q111 |
| 21296-21301 | 215D(1)(d) | fork | F-215D-1 | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate wit...` | Q110, Q111 |
| 21302-21308 | 215D(2) | fork | F-215D-1 | `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without ...` | Q112 |
| 21309-21311 | 215D(2)(a) | fork | F-215D-1 | `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without ...` | Q112 |
| 21312-21315 | 215D(2)(b) | fork | F-215D-1 | `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without ...` | Q112 |
| 21316-21320 | 215D(2)(c) | fork | F-215D-1 | `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without ...` | Q112 |
| 21321-21325 | 215D(2)(d) | fork | F-215D-1 | `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without ...` | Q112 |
| 21326-21335 | 215D(3) | encoded |  | `s 215D(3) the directors gave the written notice to every secured creditor at least 21 days befo...` (+1 more) | Q113 |
| 21336-21339 | 215D(4) | encoded |  | `s 215D(4) the resolution is deemed to be an amalgamation proposal that has been approved` | Q114 |
| 21340-21347 | 215D(5) | encoded |  | `s 215D(5) the board made the solvency statement in relation to the amalgamated company before t...` (+1 more) | Q115 |
| 21348-21351 | 215D(6) | encoded |  | `s 215D(6) the director must sign the declaration` (+2 more) | Q116, Q117 |
| 21352-21354 | 215D(6)(a) | encoded |  | `s 215D(6) the director must sign the declaration` (+2 more) | Q116, Q117 |
| 21355-21356 | 215D(6)(b) | encoded |  | `s 215D(6) the director must sign the declaration` (+2 more) | Q116, Q117 |
| 21357-21359 | 215D(7) | fork | F-215C-2 | `s 215D(7) the director is guilty of the offence` | Q118 |
| 21360-21362 | 215D(8) | encoded |  | `s 215D(8) the cancellation of the shares is deemed to be a reduction of share capital within th...` | Q119 |
| 21363-21364 | marginal heading of s 215E: "Registration of amalgamation" | inert (reason 1: not operative) |  |  |  |
| 21365-21369 | 215E ; 215E(1) | encoded |  | `s 215E(1) the documents filed with the Registrar are those the subsection requires` | Q120 |
| 21370-21371 | 215E(1)(a) | encoded |  | `s 215E(1) the documents filed with the Registrar are those the subsection requires` | Q120 |
| 21372-21374 | 215E(1)(aa) | encoded |  | `s 215E(1) the documents filed with the Registrar are those the subsection requires` | Q120 |
| 21375-21377 | 215E(1)(b) | encoded |  | `s 215E(1) the documents filed with the Registrar are those the subsection requires` | Q120 |
| 21378-21386 | 215E(1)(c) | encoded |  | `s 215E(1) the documents filed with the Registrar are those the subsection requires` | Q120 |
| 21387-21393 | 215E(1)(d) | encoded |  | `s 215E(1) the documents filed with the Registrar are those the subsection requires` | Q120 |
| 21394-21405 | 215E(1)(e) | encoded |  | `s 215E(1) the documents filed with the Registrar are those the subsection requires` | Q120 |
| 21406-21407 | 215E(2) | encoded |  | `s 215E(2)(a) section 19(1)(a) and (c) is deemed to have been complied with` (+1 more) | Q121, Q122 |
| 21408-21411 | 215E(2)(a) | encoded |  | `s 215E(2)(a) section 19(1)(a) and (c) is deemed to have been complied with` (+1 more) | Q121, Q122 |
| 21412-21418 | 215E(2)(b) | encoded |  | `s 215E(2)(a) section 19(1)(a) and (c) is deemed to have been complied with` (+1 more) | Q121, Q122 |
| 21419-21420 | marginal heading of s 215F: "Notice of amalgamation, etc." | inert (reason 1: not operative) |  |  |  |
| 21421-21423 | 215F ; 215F(1) | encoded |  | `s 215F(1) what the Registrar must issue on receiving the documents and fees` (+1 more) | Q123 |
| 21424-21431 | 215F(1)(a) | encoded |  | `s 215F(1) what the Registrar must issue on receiving the documents and fees` (+1 more) | Q123 |
| 21432-21436 | 215F(1)(b) | encoded |  | `s 215F(1) what the Registrar must issue on receiving the documents and fees` (+1 more) | Q123 |
| 21437-21444 | 215F(2) | encoded |  | `s 215F(2) the notice must be expressed to have effect on the date specified in the amalgamation...` | Q124 |
| 21445-21448 | 215F(3) | encoded |  | `s 215F(3) the Registrar must remove the amalgamating companies, other than the amalgamated comp...` (+1 more) | Q125 |
| 21449-21455 | 215F(4) | encoded |  | `s 215F(4) the Registrar must issue a certificate of confirmation of amalgamation to the amalgam...` (+1 more) | Q126 |
| 21456-21457 | marginal heading of s 215G: "Effect of amalgamations" | inert (reason 1: not operative) |  |  |  |
| 21458-21459 | 215G | encoded |  | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | Q127, Q128 |
| 21460-21461 | 215G(a) | encoded |  | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | Q127, Q128 |
| 21462-21464 | 215G(b) | encoded |  | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | Q127, Q128 |
| 21465-21468 | 215G(c) | encoded |  | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | Q127, Q128 |
| 21469-21473 | 215G(d) | encoded |  | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | Q127, Q128 |
| 21474-21480 | 215G(e) | encoded |  | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | Q127, Q128 |
| 21481-21484 | 215G(f) | encoded |  | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | Q127, Q128 |
| 21485-21488 | 215G(g) | encoded |  | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | Q127, Q128 |
| 21489-21490 | marginal heading of s 215H: "Power of Court in certain cases" | inert (reason 1: not operative) |  |  |  |
| 21491-21499 | 215H ; 215H(1) | fork | F-215H-1, F-215H-2 | `s 215H(1) the Court may make an order in relation to the amalgamation proposal` (+1 more) | Q129, Q130, Q131 |
| 21500-21502 | 215H(1)(a) | fork | F-215H-1, F-215H-2 | `s 215H(1) the Court may make an order in relation to the amalgamation proposal` (+1 more) | Q129, Q130, Q131 |
| 21503-21505 | 215H(1)(b) | fork | F-215H-1, F-215H-2 | `s 215H(1) the Court may make an order in relation to the amalgamation proposal` (+1 more) | Q129, Q130, Q131 |
| 21506-21509 | 215H(1)(c) | fork | F-215H-1, F-215H-2 | `s 215H(1) the Court may make an order in relation to the amalgamation proposal` (+1 more) | Q129, Q130, Q131 |
| 21510-21512 | 215H(2) | fork | F-215H-2 | `s 215H(2) the order may be made on the terms or conditions` | Q132 |
| 21513-21515 | marginal heading of s 215I: "Solvency statement in relation to amalgamating company and offence for making false statement" | inert (reason 1: not operative) |  |  |  |
| 21516-21520 | 215I ; 215I(1) | encoded |  | `s 215I(1) the statement has the content the subsection requires` (+1 more) | Q133, Q135 |
| 21521-21529 | 215I(1)(a) | encoded |  | `s 215I(1) the statement has the content the subsection requires` (+1 more) | Q133, Q135 |
| 21530-21535 | 215I(1)(b) | encoded |  | `s 215I(1) the statement has the content the subsection requires` (+1 more) | Q133, Q135 |
| 21536-21537 | 215I(2) | encoded |  | `s 215I(2) the statement is in the form the subsection requires` | Q134 |
| 21538-21541 | 215I(2)(a) | encoded |  | `s 215I(2) the statement is in the form the subsection requires` | Q134 |
| 21542-21550 | 215I(2)(b) | encoded |  | `s 215I(2) the statement is in the form the subsection requires` | Q134 |
| 21551-21554 | 215I(3) | encoded |  | `s 215I(3) the directors have formed the opinion as the subsection requires` (+1 more) | Q136 |
| 21555-21559 | 215I(4) | fork | F-215I-1 | `s 215I(4)(a) the board has had regard to what the paragraph requires` (+2 more) | Q137, Q138 |
| 21560-21561 | 215I(4)(a) | fork | F-215I-1 | `s 215I(4)(a) the board has had regard to what the paragraph requires` (+2 more) | Q137, Q138 |
| 21562-21565 | 215I(4)(a)(i) | fork | F-215I-1 | `s 215I(4)(a) the board has had regard to what the paragraph requires` (+2 more) | Q137, Q138 |
| 21566-21574 | 215I(4)(a)(ii) | fork | F-215I-1 | `s 215I(4)(a) the board has had regard to what the paragraph requires` (+2 more) | Q137, Q138 |
| 21575-21579 | 215I(4)(b) | fork | F-215I-1 | `s 215I(4)(a) the board has had regard to what the paragraph requires` (+2 more) | Q137, Q138 |
| 21580-21583 | 215I(5) | fork | F-215I-3 | `s 215I(5) the board may take the matter into account in valuing a contingent liability` | Q139 |
| 21584-21585 | 215I(5)(a) | fork | F-215I-3 | `s 215I(5) the board may take the matter into account in valuing a contingent liability` | Q139 |
| 21586-21589 | 215I(5)(b) | fork | F-215I-3 | `s 215I(5) the board may take the matter into account in valuing a contingent liability` | Q139 |
| 21590-21596 | 215I(6) | fork | F-215I-2 | `s 215I(6) the director is guilty of the offence this subsection creates` (+1 more) | Q140, Q141 |
| 21597-21599 | marginal heading of s 215J: "Solvency statement in relation to amalgamated company and offence for making false statement" | inert (reason 1: not operative) |  |  |  |
| 21600-21604 | 215J ; 215J(1) | encoded |  | `s 215J(1) the statement is a solvency statement in relation to the amalgamated company for the ...` | Q142 |
| 21605-21608 | 215J(1)(a) | encoded |  | `s 215J(1) the statement is a solvency statement in relation to the amalgamated company for the ...` | Q142 |
| 21609-21614 | 215J(1)(b) | encoded |  | `s 215J(1) the statement is a solvency statement in relation to the amalgamated company for the ...` | Q142 |
| 21615-21618 | 215J(2) | encoded |  | `s 215J(2) the directors have formed the opinion as the subsection requires` (+1 more) | Q143 |
| 21619-21627 | 215J(3) | fork | F-215I-1 | `s 215J(3)(a) the board has had regard to what the paragraph requires` (+2 more) | Q144, Q145 |
| 21628-21629 | 215J(3)(a) | fork | F-215I-1 | `s 215J(3)(a) the board has had regard to what the paragraph requires` (+2 more) | Q144, Q145 |
| 21630-21634 | 215J(3)(a)(i) | fork | F-215I-1 | `s 215J(3)(a) the board has had regard to what the paragraph requires` (+2 more) | Q144, Q145 |
| 21635-21640 | 215J(3)(a)(ii) | fork | F-215I-1 | `s 215J(3)(a) the board has had regard to what the paragraph requires` (+2 more) | Q144, Q145 |
| 21641-21645 | 215J(3)(b) | fork | F-215I-1 | `s 215J(3)(a) the board has had regard to what the paragraph requires` (+2 more) | Q144, Q145 |
| 21646-21649 | 215J(4) | fork | F-215I-3 | `s 215J(4) the board may take the matter into account in valuing a contingent liability` | Q146 |
| 21650-21651 | 215J(4)(a) | fork | F-215I-3 | `s 215J(4) the board may take the matter into account in valuing a contingent liability` | Q146 |
| 21652-21655 | 215J(4)(b) | fork | F-215I-3 | `s 215J(4) the board may take the matter into account in valuing a contingent liability` | Q146 |
| 21656-21662 | 215J(5) | fork | F-215I-2 | `s 215J(5) the director is guilty of the offence this subsection creates` (+1 more) | Q147, Q148 |
| 21663-21665 | marginal heading of s 215K: "Transfer of money or other consideration paid under terms of amalgamation to Official Receiver" | inert (reason 1: not operative) |  |  |  |
| 21666-21681 | 215K ; 215K(1) | encoded |  | `s 215K(1) the transfer to the Official Receiver is within the time the subsection allows` (+1 more) | Q149 |
| 21682-21683 | 215K(2) | encoded |  | `s 215K(2) how the Official Receiver must deal with what is received under subsection (1)` (+2 more) | Q150 |
| 21684-21688 | 215K(2)(a) | encoded |  | `s 215K(2) how the Official Receiver must deal with what is received under subsection (1)` (+2 more) | Q150 |
| 21689-21697 | 215K(2)(b) | encoded |  | `s 215K(2)(b) the Official Receiver must sell or dispose of the other consideration` (+2 more) | Q150 |

## Fork register (sgd)

42 forks: every ambiguity found in the range, the readings seen, the one taken, the text that licenses the choice, and the layer-1 rule that carries it.
The text column is quoted mechanically by `work/forks.py` from the line ranges it names (a quotation may start or end mid-sentence where the range does; it never crosses page furniture).
A coverage row of disposition `fork` names its fork ids; the layer-1 comment above each branch that rests on a fork names the id too.
Where a fork is a split site (an unmet element of an offence, or a "may" gated by "where" or an application) or relies on a ruling of the Guide, its "reading taken" cell ends by naming the line of `inputs/ENCODING-GUIDE.md` and quoting the Guide's own words; the rulings themselves are quoted whole under "Split sites (sgd)".
Nothing in the register was decided by looking at what another part did.

| id | provision | the ambiguity | readings seen | reading taken | text that licenses it | layer-1 rule |
| --- | --- | --- | --- | --- | --- | --- |
| F-210-1 | s 210(2) | Is the list of persons who may apply a closed list? | Closed: only the liquidator (company being wound up) and, in any other case, the company or a creditor, member or holder of units of shares; anyone else answers JUST FALSE. Open: anyone else is not covered (NOTHING). | Closed. The subsection states the list as a definition ("are"). | "(2) The persons referred to in subsection (1) are —" (line 20209); "(b) in any other case —" (line 20214) | `s 210(2) the person is a person referred to in subsection (1)` |
| F-210-2 | s 210(1) and s 210(10) | A "may" gated by "Where" and by an application: JUST FALSE (periods ruling (b)) or NOTHING (the "In short" line on grants)? | JUST FALSE where the "where" condition or the application is missing; NOTHING. | JUST FALSE (ruling (b) of 2026-11-05); counted in "Split sites (sgd)" and listed here for the maintainer. Split site (ii), two functions. Rule relied on: Guide line 93: “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”; for "on the application" by analogy to Guide line 94: “(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above”. The other reading (NOTHING) rests on the "In short" line on grants (Guide line 86) and is listed under Guide line 99: “do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon"”. | "210.—(1) Where a compromise or an arrangement is proposed" (line 20191); "the Court may, on the application in a summary way of any person referred to in subsection (2), order a meeting of the creditors, the" (lines 20201-20202); "(10) Where no order has been made or resolution passed for the winding up of a company and any such compromise or arrangement has been proposed between the company and its creditors or any class of such creditors, the Court may, in addition to any of its powers, on the application in a summary way of the company or of any member," (lines 20367-20371) | `s 210(1) the Court may order a meeting to be summoned`; `s 210(10) the Court may restrain further proceedings against the company` |
| F-210-3 | s 210(3) | How is "value" measured for members and holders of units of shares? | The text does not say (for creditors, the value of the claims). The figure is supplied as an input. | Input: the value held by those present and voting and by those in favour. | "three‑fourths in value of —" (line 20226); "present and voting either in person or by proxy at the meeting." (line 20238) | `s 210(3) vote` (four numbers) |
| F-210-4 | s 210(3) and (3AB)(b) | Is "three-fourths in value" a floor (at least) or a strict majority of the value above that fraction? | At least three-fourths; more than three-fourths. | At least three-fourths: exactly three-fourths is enough. | "adjournment is approved by a majority in number representing three‑fourths in value of —" (lines 20225-20226) | `s 210(3) those who voted in favour represent three-fourths in value of those present and voting` |
| F-210-5 | s 210(3) | A meeting "may be adjourned ... if" the resolution is approved by the majorities: what does a failed "if" answer? | JUST FALSE (the "if" says no); NOTHING (a grant limited by its own wording). | NOTHING (grant ruling of 2026-11-12, limit 1). Split-site rule relied on: Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”. | "(3) A meeting held pursuant to an order made under subsection (1) may be adjourned from time to time if the resolution for the adjournment is approved by a majority in number representing three‑fourths in value of —" (lines 20223-20226) | `s 210(3) the meeting may be adjourned` |
| F-210-6 | s 210(3AB)(a), (b) | "unless the Court orders otherwise": does a number the Court orders replace the majority in number, or add to it? | It replaces it in (a) and in (b) ("the majority in number referred to, or such number as the Court may order"); it is an extra requirement. | It replaces it. | "(a) unless the Court orders otherwise, a majority in number" (line 20275); "(b) the majority in number referred to, or such number as the Court may order, under paragraph (a) represents" (lines 20292-20293) | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` |
| F-210-7 | s 210(4) | "may grant its approval ... subject to such alterations or conditions as it thinks just": what is the case where the Court does not think the alteration or condition just? | JUST FALSE; NOTHING (a grant limited by the Court's own judgment). | NOTHING (grant ruling of 2026-11-12, limit 1); the Court's judgment is a conditional input. Split-site rule relied on: Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”. | "(4) The Court may grant its approval to a compromise or arrangement subject to such alterations or conditions as it thinks just." (lines 20313-20314) | `s 210(4) the Court may grant its approval subject to the alteration or condition` |
| F-210-8 | s 210(5) | The order takes effect "on and from the date of lodgment or such earlier date as the Court may determine and as may be specified in the order": what if the specified date is not earlier than the lodgment? | That date governs; it is not "such earlier date", so the text does not say (NOTHING). | NOTHING: only an earlier date counts as "such earlier date". | "(5) An order under subsection (3AB)(c) has no effect until a copy of the order is lodged with the Registrar, and upon being so lodged, the order takes effect on and from the date of lodgment or such earlier date as the Court may determine and as may be specified in the order." (lines 20320-20323) | `s 210(5) the date from which the order takes effect` |
| F-210-9 | s 210(6) | A copy of the constitution issued before the order was made. | Outside the duty (NOTHING); the duty does not apply (JUST FALSE). | NOTHING (scope limit, periods ruling (c)). | "(6) Subject to subsection (7), a copy of every order made under subsection (3AB)(c) must be annexed to every copy of the constitution of the company issued after the order has been made." (lines 20327-20329) | `s 210(6) a copy of the order must be annexed to the copy of the constitution` |
| F-210-10 | s 210(9) | The unmet element of an offence (no default): JUST FALSE or NOTHING? | JUST FALSE (the provision's own question, "is the company guilty?"); NOTHING. | JUST FALSE (Guide line 98; split site (i)). Split site (i). Rule relied on: Guide line 98: “keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question”. | "(9) Every company which makes default in complying with subsection (6) or (8) and every officer of the company who is in default shall be guilty of an offence and shall be liable on conviction to a fine not exceeding $2,000." (lines 20360-20363) | `s 210(9) the company is guilty of the offence`; `s 210(9) the officer is guilty of the offence` |
| F-210-11 | s 210(10A) | "may, after the expiration of 2 years and must before the expiration of 10 years": counting the end of each period. | After the last day of the 2 years and up to and including the last day of the 10 years (the keel conventions P1 to P9); the day the period "expires" is the last day of the period. | After the last day of the 2 years, up to and including the last day of the 10 years. A transfer outside it answers JUST FALSE (periods ruling (a)). | "holding the money or other consideration may, after the expiration of 2 years and must before the expiration of 10 years from the date on" (lines 20385-20387) | `s 210(10A) the transfer to the Official Receiver is within the time the subsection allows` |
| F-210-12 | s 210(7) | "The Court may, by order, exempt a company from compliance with the requirements of subsection (6) or determine the period during which the company must so comply": a grant naming two things and no other. | NOTHING for anything else the Court might do (the grant names two things without "only"); JUST FALSE (the Court may do nothing else). | NOTHING. Rule relied on: Guide line 87: “limits a grant or prohibition in its own wording and the case falls outside the limit”. | "(7) The Court may, by order, exempt a company from compliance with the requirements of subsection (6) or determine the period during which the company must so comply." (lines 20333-20335) | `s 210(7) the Court may do it by order` |
| F-211-1 | s 211(5) | The unmet element of the offence (no default). | JUST FALSE; NOTHING. | JUST FALSE (split site (i)). Split site (i). Rule relied on: Guide line 98: “keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question”. | "(5) Where default is made in complying with any requirement of this section, the company and every officer of the company who is in default shall be guilty of an offence and shall be liable on conviction to a fine not exceeding $5,000 or to imprisonment for a term not exceeding 12 months." (lines 20477-20481) | `s 211(5) the company is guilty of the offence` and the officer and liability functions |
| F-212-1 | s 212(1) | A "may" gated by "Where" (an application and what is shown to the Court). | JUST FALSE (ruling (b)); NOTHING. | JUST FALSE (periods ruling (b)). Split site (ii). Rule relied on: Guide line 93: “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”. Listed under Guide line 99: “do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon"”. | "212.—(1) Where an application is made to the Court under this Part or section 71 of the Insolvency, Restructuring and Dissolution Act 2018 for the approval of a compromise or arrangement and it is shown to the Court that the compromise or arrangement has been" (lines 20499-20502) | `s 212(1) the Court may provide for the matter by its order` |
| F-212-2 | s 212(3) | The unmet element of the offence (no default). | JUST FALSE; NOTHING. | JUST FALSE (split site (i)). Split site (i). Rule relied on: Guide line 98: “keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question”. | "(3) Where an order is made under this section, every company in relation to which the order is made must lodge within 7 days of the making of the order —" (lines 20552-20555) | `s 212(3) the company is guilty of the offence`; `s 212(3) the officer is guilty of the offence` |
| F-215-1 | s 215(1), (1C) | "disregarded" does not say on which side of the 90% fraction the shares are left out. | Out of the total (the denominator) and out of the approvals; out of the total only. | The shares are left out of the total; the caller states the number of the counted shares whose holders approved. | "(a) shares that are issued after the date of the offer are to be disregarded unless they have been issued pursuant to the exercise of an option or right attached to any convertible" (lines 20647-20649); "(b) relevant treasury shares that cease to be held as treasury shares after the date of the offer are to be disregarded." (lines 20653-20654) | `s 215(1) the total number of the shares the 90% is counted against` |
| F-215-2 | s 215(1) | The parenthesis "(other than shares already held at the date of the offer by the transferee ...)" stands in the class limb only. | Literal: it applies only where the scheme is for all the shares of a class; it applies to both limbs. | Literal reading (class limb only); a marginal reading for a lawyer. | "(excluding treasury shares) or of the shares of that class (other than shares already held at the date of the offer by the transferee, and excluding any shares in the transferor company held as treasury shares), the transferee may at any time within 2 months, after the offer" (lines 20602-20605) | `s 215(1) the number of shares already held by the transferee that are left out of the count` |
| F-215-3 | s 215(1) | "within 4 months after the making of the offer": where the window opens. | The day after the offer (the keel convention P2); the day of the offer. | The day after the offer. | "this section the transferee) has, within 4 months after the making of the offer in that behalf by the transferee, been approved as to the" (lines 20598-20599) | `s 215(1) the scheme or contract has been approved by the holders of the requisite number of the shares` |
| F-215-4 | s 215(1) | "the transferee may at any time within 2 months, after the offer has been so approved, give notice": a "may" gated by "Where" and by a period. | JUST FALSE (rulings (a) and (b)); NOTHING. | JUST FALSE; a shareholder who is not dissenting is outside the grant (NOTHING, ruling (c)). Split site (ii). Rule relied on: Guide line 93: “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”. Listed under Guide line 99: “do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon"”. | "has been so approved, give notice in the prescribed manner to any dissenting shareholder that it desires to acquire the dissenting shareholder’s shares; and when such a notice is given the" (lines 20606-20608) | `s 215(1) the transferee may give notice to the dissenting shareholder that it desires to acquire the shares` |
| F-215-5 | s 215(1), (1A), (4) | "14 days of a statement being supplied": what "supplied" is. | The day the statement is posted (subsection (2)); the day it is received. | The day it is posted. | "transferee is, unless on an application made by the dissenting shareholder within one month from the date on which the notice was given or within 14 days of a statement being supplied to a dissenting shareholder pursuant to subsection (2) (whichever is the later) the" (lines 20609-20612) | `s 215(1) the last day of the later of the one month and the 14 days` |
| F-215-6 | s 215(1) | "unless on an application made by the dissenting shareholder ... the Court thinks fit to order otherwise": the Court's power on a timely application. | JUST FALSE where there is no application or it is late ("on an application" counts as "where", ruling (c)); NOTHING where the Court does not think fit (grant ruling, limit 1). | As stated: JUST FALSE where there is none or it is late, NOTHING where the Court does not think fit. Split site (ii) for the missing or late application; the Court not thinking fit is limit 1 (Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”). Rule relied on: Guide line 94: “(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above” (applied to "on an application"). Listed under Guide line 99: “do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon"”. | "transferee is, unless on an application made by the dissenting shareholder within one month from the date on which the notice was given or within 14 days of a statement being supplied to a dissenting shareholder pursuant to subsection (2) (whichever is the later) the Court thinks fit to order otherwise, entitled and bound to acquire" (lines 20609-20613) | `s 215(1) the Court may order that the transferee is not entitled and bound to acquire the shares` |
| F-215-7 | s 215(1), (1A), (2), (3) | "entitled and bound" and "is entitled to elect" and "is entitled to require": an "entitled" function is a claim, not a power; the grant ruling does not settle it. | Leave the answers as they are and list them (limit 3 of the grant ruling); rename and re-answer them. | Left as they are and listed. An "unless" once met answers JUST FALSE case by case. Rule relied on: Guide line 99: “and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it)”. | "Court thinks fit to order otherwise, entitled and bound to acquire" (line 20613); "shares, the dissenting shareholder is entitled to require the transferor company by a written demand served on the transferor company," (lines 20690-20691); "respect to any shares, the transferee is entitled and bound to acquire" (line 20722) | `s 215(1) the transferee is entitled and bound to acquire the dissenting shareholder's shares`; `s 215(1A) ...`; `s 215(2) the dissenting shareholder is entitled to require ...`; `s 215(3) the transferee is entitled and bound to acquire the shares` |
| F-215-8 | s 215(1) | "the terms which were specified in the offer as being applicable to dissenting shareholders". | The terms subsection (1B) makes the offer state (those that apply where the shareholder fails to elect); some other terms. | Read with (1B). | "those shares on the terms which, under the scheme or contract the shares of the approving shareholders are to be transferred to the transferee or if the offer contained 2 or more alternative sets of terms upon the terms which were specified in the offer as being applicable to dissenting shareholders." (lines 20614-20618) | `s 215(1) the terms on which the transferee must acquire the dissenting shareholder's shares` |
| F-215-9 | s 215(2) | "the transferee is not entitled or bound to acquire the shares of the dissenting shareholders until 14 days after the posting of that statement": where no statement is demanded. | NOTHING (the subsection sets the bar by the posting); JUST FALSE. | NOTHING (a marginal reading for a lawyer). An "until" bar ends the day after the last of the 14 days (ruling (d) of 2026-11-05). Rule relied on: Guide line 94: “(d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X)”. | "the register of members, and the transferee is not entitled or bound to acquire the shares of the dissenting shareholders until 14 days after the posting of the statement of such names and addresses to the dissenting shareholder." (lines 20695-20698) | `s 215(2) the transferee is not yet entitled or bound to acquire the shares` |
| F-215-10 | s 215(3A) | "for the purpose of calculating whether 90% of the total number of shares are held by the transferee, shares held by the transferor company as treasury shares are to be treated as having been acquired by the transferee": does it apply where the 90% is measured against a class? | Only where measured against the total number of the shares; in both cases. | Only against the total. | "(3A) In subsection (3), for the purpose of calculating whether 90% of the total number of shares are held by the transferee, shares held by the transferor company as treasury shares are to be treated as having been acquired by the transferee." (lines 20734-20737) | `s 215(3A) the number of the treasury shares treated as having been acquired by the transferee` |
| F-215-11 | s 215(3)(a) | "(unless on a previous transfer pursuant to the scheme or contract it has already complied with this requirement)": an "unless" once met. | JUST FALSE (the text says no); NOTHING. | JUST FALSE, case by case. | "(a) the transferee must within one month from the date of the transfer (unless on a previous transfer pursuant to the scheme or contract it has already complied with this requirement) give notice of that fact in the prescribed" (lines 20709-20712) | `s 215(3)(a) the transferee must give notice of that fact to the holders of the remaining shares who have not assented` |
| F-215-12 | s 215(3)(b) | "any such holder may within 3 months from the giving of the notice to such holder require the transferee to acquire the shares": a "may" gated by "Where" and a period. | JUST FALSE (rulings (a), (b)); NOTHING. | JUST FALSE; a holder who has not assented but was not given the notice, or who did assent, is outside the grant (NOTHING, ruling (c)). Split site (ii). Rule relied on: Guide line 93: “(b) a "where ..." condition: when it fails the answer is `JUST FALSE`”. Listed under Guide line 99: “do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon"”. | "(b) any such holder may within 3 months from the giving of the notice to such holder require the transferee to acquire the shares in question," (lines 20717-20719) | `s 215(3)(b) the holder may require the transferee to acquire the shares in question` |
| F-215-13 | s 215(3) | Other terms agreed, and other terms ordered by the Court: which governs? | The agreed terms; the Court's terms; the text does not say. | NOTHING. | "respect to any shares, the transferee is entitled and bound to acquire those shares on the terms on which under the scheme or contract the shares of the approving shareholders were transferred to it, or on such" (lines 20722-20725); "other terms as are agreed or as the Court on the application of either the transferee or the shareholder thinks fit to order." (lines 20729-20730) | `s 215(3) the terms on which the transferee must acquire the shares` |
| F-215-14 | s 215(4) | "if an application to the Court by the dissenting shareholder is then pending": pending at what moment? | At the end of the later of the two periods; at any time after the notice. | At the end of the later period. | "must, after the expiration of one month after the date on which the notice has been given or, after 14 days after a statement has been supplied to a dissenting shareholder pursuant to subsection (2) or if an application to the Court by the dissenting shareholder is then pending, after that application has been disposed of —" (lines 20744-20748) | `s 215(4) the first day on which the transferee must act` |
| F-215AA-1 | s 215AA(2), (3) | The conditions are said to be satisfied in the way the paragraphs describe; the text does not say "only". | Where the acceptances were acquired separately, NOTHING; JUST FALSE. | NOTHING. | "(2) The conditions for the exercise of the rights conferred by section 215(1) are satisfied — (a) in the case of acquisitions of shares by virtue of acceptances of the offer — by the joint transferees acquiring or unconditionally contracting to acquire the necessary shares jointly; or (b) in other cases — by the joint transferees acquiring or unconditionally contracting to acquire the necessary shares either jointly or separately." (lines 20956-20966) | `s 215AA(2) the conditions for the exercise of the rights conferred by section 215(1) are satisfied` |
| F-215AB-1 | s 215AB(1), (3) | An offer not communicated to every holder when the conditions of (1) are not met. | JUST FALSE (the "if" says no); NOTHING because (3)(a) says it is not to be inferred that the offer cannot be an offer made under a scheme. | NOTHING. | "(3) It is not to be inferred — (a) that an offer which is not communicated to every holder of" (lines 21050-21052) | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made under a scheme or contract` |
| F-215A-1 | s 215A | "2 or more companies may amalgamate ... in accordance with sections 215B to 215G, where applicable": a grant limited by its own wording. | JUST FALSE; NOTHING. | NOTHING outside the grant (limit 1). Split-site rule relied on: Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”. | "215A. Without affecting section 212 and any other law relating to the merger or amalgamation of companies, 2 or more companies may amalgamate and continue as one company, which may be one of the amalgamating companies or a new company, in accordance with sections 215B to 215G, where applicable." (lines 21068-21072) | `s 215A the companies may amalgamate and continue as one company` |
| F-215B-1 | s 215B(2) | "An amalgamation proposal may specify the date ...": a grant limited by its own wording. | JUST FALSE; NOTHING. | NOTHING outside it (limit 1). Split-site rule relied on: Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”. | "(2) An amalgamation proposal may specify the date on which the amalgamation is intended to become effective." (lines 21130-21131) | `s 215B(2) the amalgamation proposal may specify the date` |
| F-215B-2 | s 215B(5) | "the name of the amalgamated company may be (a) the name of one of the amalgamating companies; or (b) a new name that has been reserved": any other name. | JUST FALSE; NOTHING. | NOTHING (limit 1). Split-site rule relied on: Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”. | "(5) For the purposes of subsection (1)(a), the name of the amalgamated company may be — (a) the name of one of the amalgamating companies; or (b) a new name that has been reserved under section 27(12B)." (lines 21150-21155) | `s 215B(5) the name may be the name of the amalgamated company` |
| F-215C-1 | s 215C(2) | "before the general meeting": a day or a moment. | Judged on days: an earlier day is before the meeting, a later day is not, and an act on the day of the meeting cannot be placed from a date alone (NOTHING); a time of day input. | Days. Trace deadlines use the day before the meeting. | "(2) The board of directors of each amalgamating company must, before the general meeting mentioned in subsection (1)(a) —" (lines 21175-21177) | `s 215C(2) the day is before the day of the general meeting` |
| F-215C-2 | s 215C(6), 215D(7) | "shall be guilty of an offence": no penalty is stated in either subsection. | State none; supply a general penalty from outside the sources. | State none: the general penalty provision is not among the sources. Split site (i) (the offence). Rule relied on: Guide line 98: “keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question”. | "(6) Any director who contravenes subsection (3) shall be guilty of an offence." (lines 21246-21247); "(7) Any director who contravenes subsection (6) shall be guilty of an offence." (lines 21357-21358) | `s 215C(6) the director is guilty of the offence`; `s 215D(7) the director is guilty of the offence` |
| F-215D-1 | s 215D(1), (2) | A "may" with an "if" gate that fails. | JUST FALSE; NOTHING. | NOTHING (limit 1). Split-site rule relied on: Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”. | "215D.—(1) A company (called in this subsection the amalgamating holding company) and one or more of its wholly‑owned subsidiaries (called in this subsection the amalgamating subsidiary company) may amalgamate and continue as one company, being the amalgamated holding company or the amalgamated subsidiary company, without complying with sections 215B and 215C if the members of each amalgamating company, by special resolution at a general meeting," (lines 21251-21257) | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate without complying with sections 215B and 215C` |
| F-215H-1 | s 215H(1) | "If the Court is satisfied ... it may, on the application of that person made at any time before the date on which the amalgamation becomes effective, make any order it thinks fit". | NOTHING when the Court is not satisfied or the person is not within the three; JUST FALSE where there is no application or it is out of time. | As stated (limit 1; ruling (c); periods ruling (a)). Split site (ii) for the missing or late application (Guide line 94: “(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above”, applied to "on the application"); the Court not satisfied is limit 1 (Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”). | "215H.—(1) If the Court is satisfied that giving effect to an amalgamation proposal would unfairly prejudice a member or creditor of an amalgamating company or a person to whom an amalgamating company is under an obligation, it may, on the application of that person made at any time before the date on which the amalgamation becomes effective, make any order it thinks fit in relation to the amalgamation proposal, and may, without limiting the generality of this subsection, make an order —" (lines 21491-21499) | `s 215H(1) the Court may make an order in relation to the amalgamation proposal` |
| F-215H-2 | s 215H(1), (2) | "make any order it thinks fit" and "on such terms or conditions as the Court thinks fit": a grant limited by the Court's own judgment. | JUST FALSE where the Court does not think fit; NOTHING. | NOTHING (limit 1): the Court's judgment is a conditional input. Split-site rule relied on: Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”. | "the amalgamation becomes effective, make any order it thinks fit in relation to the amalgamation proposal, and may, without limiting the" (lines 21496-21497); "(2) An order may be made under subsection (1) on such terms or conditions as the Court thinks fit." (lines 21510-21511) | `s 215H(1) the order is within the Court's power`; `s 215H(2) the order may be made on the terms or conditions` |
| F-215I-1 | s 215I(4)(b), 215J(3)(b) | "may rely on valuations of assets or estimates of liabilities that are reasonable in the circumstances": a grant whose limit is not met. | JUST FALSE; NOTHING. | NOTHING (limit 1). Split-site rule relied on: Guide line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed”. | "(b) may rely on valuations of assets or estimates of liabilities that are reasonable in the circumstances." (lines 21575-21576) | `s 215I(4)(b) the board may rely on the valuation or estimate`; `s 215J(3)(b) ...` |
| F-215I-2 | s 215I(6), 215J(5) | The unmet element of the offence (the director had reasonable grounds). | JUST FALSE; NOTHING. | JUST FALSE (split site (i)). Split site (i). Rule relied on: Guide line 98: “keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question”. | "(6) Any director of an amalgamating company who votes in favour of or otherwise causes a solvency statement under this section to be made without having reasonable grounds for the opinions expressed in it shall be guilty of an offence and shall be liable on conviction to a fine not exceeding $100,000 or to imprisonment for a term not exceeding 3 years or to both." (lines 21590-21595) | `s 215I(6) the director is guilty of the offence this subsection creates`; `s 215J(5) ...` |
| F-215I-3 | s 215I(5), 215J(4) | "may take into account (a) the likelihood of the contingency occurring; and (b) any claim ...": two matters listed without "only". | JUST FALSE for any other matter; NOTHING. | NOTHING: the list is not closed. Rule relied on: Guide line 87: “where the text lists without closing the list”. | "(5) In determining, for the purposes of subsection (4), the value of a contingent liability, the board of directors of the amalgamating company may take into account — (a) the likelihood of the contingency occurring; and (b) any claim the amalgamating company is entitled to make and can reasonably expect to be met to reduce or extinguish the contingent liability." (lines 21580-21588); "(4) In determining, for the purposes of subsection (3), the value of a contingent liability, the board of directors of each amalgamating company may take into account — (a) the likelihood of the contingency occurring; and (b) any claim the amalgamated company is entitled to make and can reasonably expect to be met to reduce or extinguish the contingent liability." (lines 21646-21654) | `s 215I(5) the board may take the matter into account in valuing a contingent liability`; `s 215J(4) ...` |

## Jural relations (sgd)

One row per provision (or run of provisions) that creates a Hohfeldian relation, in text order.
The second column names the holder of the right (claim), privilege (liberty), power or immunity; the third names the bearer of the correlative duty, no-right, liability or disability.
Each relation is written once, from one side, and only from what the text says: where the text names no holder or no bearer, the cell says so rather than supply one (the commonest case is a passive "must be sent" or "must be annexed").
Where a provision creates no such relation (a definition, a counting rule, a deeming rule, a timing rule) the cells say `none` and what it does.
The State's claim in an offence provision is the claim that the duty be performed together with the power to prosecute; it is written once, in the row for the offence.
The last column is generated: every layer-1 function whose name begins with the provision's own key, minus the date-arithmetic helpers (`the number of days from ...`, `the last day of ...`), so a name there is a name in the files.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | L4 rules |
| --- | --- | --- | --- |
| s 210(1) | the Court (power to order a meeting to be summoned); each person in subsection (2) (privilege to apply in a summary way) | the creditors, members or holders of units of shares of the company, or a class of them (liability to be summoned as the Court directs) | `s 210(1) the Court may order a meeting to be summoned` |
| s 210(2) | the liquidator, where the company is being wound up; otherwise the company, or any creditor, member or holder of units of shares of the company (privilege to apply) | any other person (no-right to apply under subsection (1)) | `s 210(2) the person is a person referred to in subsection (1)` |
| s 210(3) | the creditors, members or holders of units of shares present and voting, by a majority in number representing three-fourths in value (power to approve an adjournment) | no bearer named | `s 210(3) a majority in number of those present and voting voted in favour`; `s 210(3) those who voted in favour represent three-fourths in value of those present and voting`; `s 210(3) the meeting may be adjourned` |
| s 210(3AA) | the creditors, members or holders of units of shares who agree by the majorities of subsection (3AB), with the Court that approves (together, the power to bind) | the company, or the liquidator and contributories where the company is being wound up, and all the creditors, members or holders of units of shares of the class (liability to be bound) | `s 210(3AA) the compromise or arrangement is binding on the party` |
| s 210(3AB) | none: the three conditions of the power in subsection (3AA) (majority in number, three-fourths in value, order of the Court) | none | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` |
| s 210(4) | the Court (power to approve subject to alterations or conditions) | no bearer named; the parties to the compromise or arrangement are in fact subject to what the Court imposes | `s 210(4) the Court may grant its approval subject to the alteration or condition` |
| s 210(5) | none: a timing rule (no effect until a copy is lodged with the Registrar; effect from the date of lodgment or an earlier date the Court specifies) | none | `s 210(5) the order cannot yet have effect`; `s 210(5) the date from which the order takes effect` |
| s 210(6) | no holder named | the company (the duty is stated passively, of "every copy of the constitution of the company"; layer 1 reads it as the company's) | `s 210(6) a copy of the order must be annexed to the copy of the constitution`; `s 210(6) the company must annex a copy of the order to every copy of the constitution issued after the order` |
| s 210(7) | the Court (power to exempt the company or fix the period) | the company (liability to the exemption or period) | `s 210(7) the Court may do it by order` |
| s 210(8)(a) | the members of the company, by a resolution of a meeting (power to direct that a report be commissioned) | the directors (duty, once the resolution so directs, to instruct the accountants or solicitors named and to forward their reports) | `s 210(8)(a) the directors must instruct the accountants or solicitors named in the resolution to report`; `s 210(8)(a) a director must instruct the accountants or solicitors named in the resolution to report` |
| s 210(8)(b) | the shareholders, creditors and holders of units of shares of the company (privilege to inspect the reports at the registered office) | the directors (duty to make the reports available at least 7 days before the meeting) | `s 210(8)(b) the reports have been made available at least 7 days before the meeting`; `s 210(8)(b) a director must make the reports available at the registered office at least 7 days before the meeting` |
| s 210(9) | the State (claim that subsections (6) and (8) be obeyed; power to prosecute) | the company, and every officer of the company who is in default (duty; liability to a fine not exceeding $2,000) | `s 210(9) the company is guilty of the offence`; `s 210(9) the officer is guilty of the offence`; `s 210(9) the most the person may be sentenced to on conviction` |
| s 210(10) | the Court (power to restrain); the company, or any member, creditor or holder of units of shares of the company (privilege to apply) | a person suing the company (liability to be restrained except by the Court's permission and on its terms) | `s 210(10) the Court may restrain further proceedings against the company`; `s 210(10) further proceedings against the company may continue` |
| s 210(10A) | the person holding the money or other consideration (privilege to transfer it to the Official Receiver after 2 years); the person for whom it is held in trust (beneficiary of that trust) | the holder (duty to transfer before 10 years from receipt); the Official Receiver (liability to receive) | `s 210(10A) the transfer to the Official Receiver is within the time the subsection allows`; `s 210(10A) the holder must transfer the money or other consideration to the Official Receiver before the 10 years expire` |
| s 210(10B) | no holder named (the text points to section 197 of the Insolvency, Restructuring and Dissolution Act 2018, outside this range) | the Official Receiver (duty to deal with the moneys as if paid under that section, and to sell or dispose of other consideration and deal with the proceeds likewise) | `s 210(10B) how the Official Receiver must deal with what is received`; `s 210(10B)(a) the Official Receiver must deal with the moneys as if they were paid under section 197`; `s 210(10B)(b) the Official Receiver must sell or dispose of the other consideration` |
| s 210(11) | none: definitions of "arrangement", "company" and "holder of units of shares" | none | `s 210(11) "arrangement" the thing is within the word arrangement`; `s 210(11) "company" the body is a company`; `s 210(11) "holder of units of shares" the person is a holder of units of shares` |
| s 211(1) | every creditor, member or holder of units of shares to whom a notice is sent, or who is entitled to attend a meeting summoned by advertisement (claim to the statement, or to the notification of where to obtain it) | no bearer named (passive: "there must be sent"); subsection (5) makes the company and its officers in default liable | `s 211(1) the notice carries what the subsection requires` |
| s 211(2) | none named: a requirement on the content of the statement where the compromise affects the rights of debenture holders | none | `s 211(2) the statement gives what the subsection requires` |
| s 211(3) | every creditor, member or holder of units of shares entitled to attend who applies in the manner indicated (claim to a free copy) | the company (duty to furnish it) | `s 211(3) the company must furnish the person with a copy of the statement free of charge` |
| s 211(4) | the company (claim to notice of matters relating to the director or trustee) | each director and each trustee for debenture holders (duty to give notice within 7 days of a written request) | `s 211(4) the director or trustee gave notice within 7 days of the receipt of the request`; `s 211(4) a director or trustee for debenture holders must give notice within 7 days of the receipt of the request` |
| s 211(5) | the State (claim; power to prosecute) | the company, and every officer of the company who is in default (duty; liability to a fine not exceeding $5,000 or imprisonment not exceeding 12 months) | `s 211(5) the company is guilty of the offence`; `s 211(5) the officer is guilty of the offence`; `s 211(5) and (7) the person is liable under subsection (5)`; `s 211(5) the most the person may be sentenced to on conviction` |
| s 211(6) | none: a deeming rule (the liquidator and any trustee for debenture holders are officers for subsection (5)) | none | `s 211(6) the person is deemed to be an officer of the company for subsection (5)` |
| s 211(7) | a person who shows that the default was due to the refusal of another director or trustee to supply the necessary particulars (immunity from liability under subsection (5)) | the State (disability: cannot convict that person under subsection (5)) | `s 211(7) the section gives the person a defence` |
| s 212(1) | the Court (power to provide for the matters listed) | the transferor company, the transferee company and any persons who dissent (liability to the Court's order) | `s 212(1) the Court may provide for the matter by its order` |
| s 212(2) | the transferee company (the property vests in it and the liabilities become its liabilities by virtue of the order) | the transferor company (loses the property and liabilities); the holder of a charge that the order directs shall cease to have effect (disability) | `s 212(2) the property vests in the transferee company and the liabilities become its liabilities by virtue of the order`; `s 212(2) the particular property vests free from the charge` |
| s 212(3) | no holder named (the copies go to the Registrar and the appropriate authority); the State (claim on the offence; power to prosecute) | every company in relation to which the order is made (duty to lodge within 7 days); the company and every officer in default (liability to a fine not exceeding $2,000 and a default penalty) | `s 212(3) the lodgment was made within 7 days of the making of the order`; `s 212(3) the company has lodged what the subsection requires within 7 days of the making of the order`; `s 212(3) the company is guilty of the offence`; `s 212(3) the officer is guilty of the offence`; `s 212(3) the most the person may be sentenced to on conviction`; `s 212(3) the company must lodge within 7 days of the making of the order` |
| s 212(4) | none: a timing rule for a vesting order over land (no effect until the appropriate entries are made) | none | `s 212(4) the vesting order cannot yet have effect in vesting the land` |
| s 212(5), (6) | none: definitions of "liabilities", "property" and "company" | none | `s 212(5) "liabilities" the thing is within the word liabilities`; `s 212(5) "property" the thing is within the word property`; `s 212(6) "company" the body is a company` |
| s 215(1) | the transferee (power to give notice within 2 months of approval that it desires to acquire a dissenting shareholder's shares; claim to those shares on the terms); the dissenting shareholder (power to apply to the Court within the time to have the acquisition refused; claim to be bought out on the terms) | the dissenting shareholder (liability to be bought out, and duty to transfer); the transferee (duty to acquire, "entitled and bound") | `s 215(1) the scheme or contract involves the transfer of all of the shares or of all of the shares in a particular class`; `s 215(1) the number of shares already held by the transferee that are left out of the count`; `s 215(1) the total number of the shares the 90% is counted against`; `s 215(1) the scheme or contract has been approved by the holders of the requisite number of the shares`; `s 215(1) the transferee may give notice to the dissenting shareholder that it desires to acquire the shares`; `s 215(1) the dissenting shareholder's application to the Court is within the time subsection (1) allows`; `s 215(1) the Court may order that the transferee is not entitled and bound to acquire the shares`; `s 215(1) the transferee is entitled and bound to acquire the dissenting shareholder's shares`; `s 215(1) the terms on which the transferee must acquire the dissenting shareholder's shares` |
| s 215(1A) | the dissenting shareholder (power to elect, by the later of one month after the notice and 14 days after the statement, which alternative terms to take) | the transferee (liability to the election) | `s 215(1A) the dissenting shareholder is entitled to elect which of the terms the shareholder prefers` |
| s 215(1B) | the shareholders to whom alternative terms are offered (claim to be told which terms apply on a failure to elect) | the transferee (duty to state it in the offer) | `s 215(1B) the transferee has stated which of the terms is to apply on a failure to elect`; `s 215(1B) the transferee must state which of the alternative terms is to apply on a failure to elect` |
| s 215(1C), (1D) | none: a counting rule and a definition (which shares are disregarded in the 90% count; what "relevant treasury shares" means) | none | `s 215(1C)(a) the shares are to be disregarded`; `s 215(1D) the shares are relevant treasury shares`; `s 215(1C)(b) the shares are to be disregarded` |
| s 215(1E) | the transferee (immunity of the approval, of its right to give notice, and of the validity of any notice from being affected by a later issue under an option or right) | no bearer named | `s 215(1E) the subsequent issue of shares affects the matter` |
| s 215(2) | the dissenting shareholder (power to demand, by written demand within one month of the notice, a statement of the other dissenting shareholders' names and addresses; immunity from acquisition until 14 days after the statement is posted) | the transferor company (duty to supply the statement); the transferee (disability: not entitled or bound until then) | `s 215(2) the dissenting shareholder is entitled to require the transferor company to supply the statement`; `s 215(2) the transferee is not yet entitled or bound to acquire the shares`; `s 215(2) the transferor company must supply the dissenting shareholder with the written statement` |
| s 215(3) | the holders of the remaining shares who have not assented (claim to notice of the 90%; power to require the transferee to acquire their shares within 3 months); the transferee or the shareholder (power to apply to the Court for other terms) | the transferee (duty to give the notice within one month of the transfer; liability to be required to acquire, "entitled and bound") | `s 215(3) the number of shares held by the transferee after the transfer, the treasury shares treated as acquired`; `s 215(3) the shares transferred, together with the other shares held by the transferee, comprise or include 90%`; `s 215(3)(a) the transferee must give notice of that fact to the holders of the remaining shares who have not assented`; `s 215(3)(a) the notice was given within one month from the date of the transfer`; `s 215(3)(b) the holder may require the transferee to acquire the shares in question`; `s 215(3) the transferee is entitled and bound to acquire the shares`; `s 215(3) the terms on which the transferee must acquire the shares`; `s 215(3)(a) the transferee must give notice of the 90% within one month from the date of the transfer` |
| s 215(3A) | none: a counting rule (treasury shares of the transferor treated as acquired by the transferee) | none | `s 215(3A) the number of the treasury shares treated as having been acquired by the transferee` |
| s 215(4) | the transferee (claim to be registered as the holder); the transferor company (claim to the notice, the instrument of transfer and the consideration) | the transferee (duty, after the waiting period, to transmit the notice and instrument and to pay, allot or transfer the consideration); the transferor company (duty to register) | `s 215(4) the transferee must transmit a copy of the notice and pay, allot or transfer the consideration to the transferor company`; `s 215(4) the transferee must transmit the notice and pay, allot or transfer the consideration`; `s 215(4) the transferor company must register the transferee as the holder of the shares` |
| s 215(5) | the several persons entitled to the shares (beneficiaries of the trust) | the transferor company (duty to pay the sums into a separate bank account and to hold sums and other consideration in trust) | `s 215(5) the transferor company has paid the sums into a separate bank account`; `s 215(5) the transferor company must pay the sums received into a separate bank account`; `s 215(5) the transferor company must hold the sums and other consideration in trust` |
| s 215(6) | the company holding the money or other consideration in trust (privilege to transfer it to the Official Receiver after 2 years); the person for whom it is held | the holding company (duty to transfer before 10 years from receipt); the Official Receiver (liability to receive) | `s 215(6) the transfer to the Official Receiver is within the time the subsection allows`; `s 215(6) the company holding the money or other consideration must transfer it to the Official Receiver before the 10 years expire` |
| s 215(7) | no holder named (the text points to section 197 of the 2018 Act) | the Official Receiver (duty, as in section 210(10B)) | `s 215(7) how the Official Receiver must deal with what is received under subsection (6)`; `s 215(7)(a) the Official Receiver must deal with the moneys as if they were paid under section 197`; `s 215(7)(b) the Official Receiver must sell or dispose of the other consideration` |
| s 215(8) to (12) | none: definitions and deeming and counting rules ("dissenting shareholder", "shares", "shareholders", "register of members", the nominee, related-corporation and associated-person rules, shares already held, a later acquisition, control of a body corporate) | none | `s 215(8) the shareholder is a dissenting shareholder`; `s 215(8A) the shareholder is within the reference to a shareholder in subsection (8)`; `s 215(8AA) the thing is within the word shares`; `s 215(8AB) the person is within the word shareholders`; `s 215(8AC) the records are within the register of members`; `s 215(8B) the definition of shares requires the securities to be treated that way`; `s 215(9) the shares are to be treated as held or acquired by the transferee`; `s 215(12)(a) the voting power reaches the lower of 50% and the prescribed percentage`; `s 215(12) the body corporate is controlled by the transferee or the person`; `s 215(9A) the shares are also to be treated as held or acquired by the transferee`; `s 215(10) the shares are shares already held by the transferee within subsection (1)`; `s 215(11) the transferee is to be treated as having acquired the shares by virtue of the approval of the offer` |
| s 215AA(1) to (3) | none: when section 215 is read subject to section 215AA, and when the conditions for the rights in section 215(1) and (3) are satisfied by joint transferees | none | `s 215AA(1) section 215 is to be read subject to section 215AA`; `s 215AA(2) the conditions for the exercise of the rights conferred by section 215(1) are satisfied`; `s 215AA(3) the conditions for the exercise of the rights conferred by section 215(3) are satisfied` |
| s 215AA(4) | the joint transferees (the transferee's rights are joint rights) | the dissenting shareholders and holders of the remaining shares (as to the joint rights); the joint transferees (the transferee's obligations are joint and several) | `s 215AA(4) how the joint transferees hold what section 215 gives the transferee` |
| s 215AA(5) | none: a compliance rule (a notice or document given or sent by or to any one of the joint transferees is complied with) | none | `s 215AA(5) the notice or document is complied with` |
| s 215AA(6) | no holder named (the notices go to dissenting shareholders and to non-assenting holders under section 215(1) and (3)) | the joint transferees (duty to make the notice by all of them and, where one is a company, signed by a director of that company) | `s 215AA(6) the notice is made as the subsection requires`; `s 215AA(6) the joint transferees must make the notice by all of them, signed for each company by a director of that company` |
| s 215AB | none: when an offer that is not communicated, or is impossible or harder to accept, is still an offer made under a scheme or contract for section 215, and a non-inference rule | none | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made under a scheme or contract`; `s 215AB(2) the impossibility or difficulty of accepting the offer does not prevent it from being made under a scheme or contract`; `s 215AB(3)(a) it is to be inferred that the offer cannot be an offer made under a scheme or contract unless the requirements of subsection (1)(a), (b) and (c) are met`; `s 215AB(3)(b) it is to be inferred that the offer cannot be an offer made under a scheme or contract unless the reason is the reason mentioned in subsection (2)` |
| s 215A | two or more companies (power to amalgamate and continue as one company) | no bearer named | `s 215A the amalgamated company is one of the amalgamating companies or a new company`; `s 215A the companies may amalgamate and continue as one company` |
| s 215B(1) | no holder named: a requirement on the content of the amalgamation proposal | none | `s 215B(1) the amalgamation proposal contains what the subsection requires` |
| s 215B(2) | no holder named: the proposal may specify the intended effective date | none | `s 215B(2) the amalgamation proposal may specify the date` |
| s 215B(3) | no holder named: a requirement on the proposal where one amalgamating company's shares are held by or for another (cancel without payment; do not convert) | none | `s 215B(3) the amalgamation proposal provides as the subsection requires` |
| s 215B(4), (5) | none: a cancellation is not deemed a reduction of share capital; what the amalgamated company's name may be | none | `s 215B(4) the cancellation of the shares is deemed to be a reduction of share capital within the meaning of the Act`; `s 215B(5) the name may be the name of the amalgamated company` |
| s 215C(1) | the members of each amalgamating company, by special resolution at a general meeting; any other person whose approval a provision of the proposal would require (power to approve) | each amalgamating company (liability: the proposal cannot be effective without the approval) | `s 215C(1)(a) the resolution is a special resolution`; `s 215C(1)(a) the meeting is a general meeting`; `s 215C(1) the amalgamation proposal has been approved as the subsection requires` |
| s 215C(2) | no holder named | the board of directors of each amalgamating company (duty, before the general meeting, to resolve that the amalgamation is in the company's best interest and to make the two solvency statements) | `s 215C(2) the day is before the day of the general meeting`; `s 215C(2)(a) the board resolved before the general meeting that the amalgamation is in the best interest of the amalgamating company`; `s 215C(2)(b) the board made the solvency statement in relation to the amalgamating company before the general meeting`; `s 215C(2)(c) the board made the solvency statement in relation to the amalgamated company before the general meeting`; `s 215C(2)(a) the board must resolve before the general meeting that the amalgamation is in the best interest of the amalgamating company`; `s 215C(2)(b) the board must make the solvency statement in relation to the amalgamating company before the general meeting`; `s 215C(2)(c) the board must make the solvency statement in relation to the amalgamated company before the general meeting` |
| s 215C(3) | no holder named | every director who votes in favour (duty to sign a declaration of opinion and grounds) | `s 215C(3) the director must sign the declaration`; `s 215C(3) the declaration states what the subsection requires`; `s 215C(3) a director who votes in favour must sign the declaration` |
| s 215C(4) | every member of the amalgamating company (claim to the proposal, the declarations, the statement of the directors' interests and the further information, not less than 21 days before the meeting) | the board of directors of each amalgamating company (duty to send) | `s 215C(4) the board sent what the subsection requires to every member at least 21 days before the general meeting`; `s 215C(4) the board must send what the subsection requires to every member at least 21 days before the general meeting` |
| s 215C(5) | every secured creditor (claim to a copy of the proposal); any member or creditor (the notice must tell them of their privilege to inspect the proposal and their claim to a free copy upon request to an amalgamating company) | the directors of each amalgamating company (duty to send, and to cause the notice to be published, not less than 21 days before the meeting) | `s 215C(5)(a) the directors sent the amalgamation proposal to every secured creditor at least 21 days before the general meeting`; `s 215C(5)(b) the directors caused the notice to be published as the paragraph requires at least 21 days before the general meeting`; `s 215C(5)(a) a director must send the amalgamation proposal to every secured creditor at least 21 days before the general meeting`; `s 215C(5)(b) a director must cause the notice to be published at least 21 days before the general meeting` |
| s 215C(6) | the State (claim; power to prosecute) | a director who contravenes subsection (3) (liable as guilty of an offence; no penalty stated, finding 6) | `s 215C(6) the director is guilty of the offence` |
| s 215D(1), (2) | the amalgamating holding company and its wholly-owned subsidiaries, or two or more wholly-owned subsidiaries of the same corporation (privilege to amalgamate without complying with sections 215B and 215C, if their members so resolve by special resolution) | no bearer named | `s 215D(1)(a) the terms of paragraph (a) are in the resolution`; `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate without complying with sections 215B and 215C`; `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without complying with sections 215B and 215C` |
| s 215D(3) | every secured creditor of the amalgamating company (claim to written notice not less than 21 days before the meeting) | the directors of each amalgamating company (duty) | `s 215D(3) the directors gave the written notice to every secured creditor at least 21 days before the general meeting`; `s 215D(3) a director must give written notice to every secured creditor at least 21 days before the general meeting` |
| s 215D(4), (8) | none: deeming rules (the resolution is an approved amalgamation proposal; a cancellation is not a reduction of share capital) | none | `s 215D(4) the resolution is deemed to be an amalgamation proposal that has been approved`; `s 215D(8) the cancellation of the shares is deemed to be a reduction of share capital within the meaning of the Act` |
| s 215D(5) | no holder named | the board of directors of each amalgamating company (duty to make the solvency statement in relation to the amalgamated company before the meeting begins) | `s 215D(5) the board made the solvency statement in relation to the amalgamated company before the commencement of the general meeting`; `s 215D(5) the board must make the solvency statement in relation to the amalgamated company before the commencement of the general meeting` |
| s 215D(6) | no holder named | every director who votes in favour (duty to sign a declaration) | `s 215D(6) the director must sign the declaration`; `s 215D(6) the declaration states what the subsection requires`; `s 215D(6) a director who votes in favour must sign the declaration` |
| s 215D(7) | the State (claim; power to prosecute) | a director who contravenes subsection (6) (liable as guilty of an offence; no penalty stated, finding 6) | `s 215D(7) the director is guilty of the offence` |
| s 215E(1) | the Registrar (claim to the listed documents, in the prescribed form, with the prescribed fee) | no bearer named (finding 5) | `s 215E(1) the documents filed with the Registrar are those the subsection requires` |
| s 215E(2) | none: deeming rules for a new amalgamated company (section 19(1)(a) and (c) deemed complied with if and only if subsection (1) is; a proposed director counts as a person named in the constitution) | none | `s 215E(2)(a) section 19(1)(a) and (c) is deemed to have been complied with`; `s 215E(2)(b) the person is within the reference in section 19(2)(b) to a person named in the constitution as a director or the secretary` |
| s 215F(1), (2) | no holder named | the Registrar (duty, on receipt of the documents and fees, to issue a notice of amalgamation, with the notice of incorporation for a new company, expressed to take effect on the date the proposal specifies if that is not earlier than receipt) | `s 215F(1) what the Registrar must issue on receiving the documents and fees`; `s 215F(2) the notice must be expressed to have effect on the date specified in the amalgamation proposal`; `s 215F(1) the Registrar must issue the notice of amalgamation on receiving the documents and fees` |
| s 215F(3) | no holder named | the Registrar (duty to remove the other amalgamating companies from the register as soon as practicable after the effective date) | `s 215F(3) the Registrar must remove the amalgamating companies, other than the amalgamated company, from the register`; `s 215F(3) the Registrar must remove the amalgamating companies from the register` |
| s 215F(4) | the amalgamated company (claim to a certificate of confirmation, on application and payment of the prescribed fee) | the Registrar (duty to issue it) | `s 215F(4) the Registrar must issue a certificate of confirmation of amalgamation to the amalgamated company`; `s 215F(4) the Registrar must issue the certificate of confirmation of amalgamation` |
| s 215G | the amalgamated company (the property, rights and privileges vest in it; proceedings and judgments may be continued or enforced by it); the members (their shares and rights are converted as the proposal provides) | the amalgamated company (the liabilities and obligations become its own; proceedings and judgments may be continued or enforced against it) | `s 215G the effect is one the section lists`; `s 215G on the date shown in the notice of amalgamation the effect has taken place` |
| s 215H(1) | a member or creditor of an amalgamating company, or a person to whom it is under an obligation, who would be unfairly prejudiced (privilege to apply before the effective date); the Court (power to make any order it thinks fit) | the amalgamating company and its board of directors (liability to the order) | `s 215H(1) the person is one the subsection names`; `s 215H(1) the Court may make an order in relation to the amalgamation proposal`; `s 215H(1) the order is within the Court's power` |
| s 215H(2) | the Court (power to impose terms or conditions) | the parties to the order (liability) | `s 215H(2) the order may be made on the terms or conditions` |
| s 215I(1), (2) | none: what a solvency statement in relation to an amalgamating company is, and the form it must take | none | `s 215I(1) the statement has the content the subsection requires`; `s 215I(2) the statement is in the form the subsection requires`; `s 215I(1) the statement is a solvency statement in relation to the amalgamating company for the purposes of section 215C(2)(b)` |
| s 215I(3), (4)(a) | no holder named | the directors (duty to take all liabilities into account); the board (duty to have regard to the most recent financial statements and all other circumstances) | `s 215I(3) the directors have formed the opinion as the subsection requires`; `s 215I(4)(a) the board has had regard to what the paragraph requires`; `s 215I(3) a director must take into account all liabilities of the amalgamating company`; `s 215I(4)(a) the board must have regard to the most recent financial statements and all other circumstances` |
| s 215I(4)(b), (5) | the board (privilege to rely on reasonable valuations and estimates; to take the likelihood of a contingency and any claim into account) | no bearer named | `s 215I(4)(b) the board may rely on the valuation or estimate`; `s 215I(5) the board may take the matter into account in valuing a contingent liability` |
| s 215I(6) | the State (claim; power to prosecute) | a director who votes in favour of, or otherwise causes, a statement to be made without reasonable grounds (liable to a fine not exceeding $100,000 or imprisonment not exceeding 3 years or both) | `s 215I(6) the director is guilty of the offence this subsection creates`; `s 215I(6) the most the person may be sentenced to on conviction` |
| s 215J(1) | none: what a solvency statement in relation to the amalgamated company is (a written declaration by the board of each amalgamating company) | none | `s 215J(1) the statement is a solvency statement in relation to the amalgamated company for the purposes of sections 215C(2)(c) and 215D(5)` |
| s 215J(2), (3)(a) | no holder named | the directors (duty to take all liabilities of the amalgamated company into account); the board of each amalgamating company (duty to have regard to the financial statements and all other circumstances) | `s 215J(2) the directors have formed the opinion as the subsection requires`; `s 215J(3)(a) the board has had regard to what the paragraph requires`; `s 215J(2) a director must take into account all liabilities of the amalgamated company`; `s 215J(3)(a) the board must have regard to the most recent financial statements and all other circumstances` |
| s 215J(3)(b), (4) | the board of each amalgamating company (privilege to rely on reasonable valuations and estimates; to take the likelihood of a contingency and any claim into account) | no bearer named | `s 215J(3)(b) the board may rely on the valuation or estimate`; `s 215J(4) the board may take the matter into account in valuing a contingent liability` |
| s 215J(5) | the State (claim; power to prosecute) | a director who votes in favour of, or otherwise causes, a statement to be made without reasonable grounds (same penalty as section 215I(6)) | `s 215J(5) the director is guilty of the offence this subsection creates`; `s 215J(5) the most the person may be sentenced to on conviction` |
| s 215K(1) | the person holding money or other consideration in trust under an approved or deemed-approved proposal (privilege to transfer it to the Official Receiver after 2 years); the person for whom it is held | the holder (duty to transfer before 10 years from receipt); the Official Receiver (liability to receive) | `s 215K(1) the transfer to the Official Receiver is within the time the subsection allows`; `s 215K(1) the person holding the money or other consideration must transfer it to the Official Receiver before the 10 years expire` |
| s 215K(2) | no holder named (the text points to section 197 of the 2018 Act) | the Official Receiver (duty, as in section 210(10B)) | `s 215K(2) how the Official Receiver must deal with what is received under subsection (1)`; `s 215K(2)(a) the Official Receiver must deal with the moneys as if they were paid under section 197`; `s 215K(2)(b) the Official Receiver must sell or dispose of the other consideration` |
| headings; repealed ss 210(3A), 210(4A), 211A to 211J, 212(1A), 213, 214 | none: not operative, or shown as repealed or deleted | none | no rule |

## Marginal readings for a lawyer (sgd)

The brief names two readings that are for a lawyer to decide, not for this encoder, and says to take them as the status quo and list every branch that rests on one:

- **(a)** a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no;
- **(b)** a prohibition or grant limited by its own wording does not count as the text's no: outside the limit the answer is "not covered".

Both lists below are generated from the layer-1 files: every branch whose comment carries `marginal reading (a)`, and every `NOTHING-kind (limited by its own wording)` branch.

### Reading (a): a failed "if" answers JUST FALSE (19 branches)

The other reading: a failed "if" says nothing about the case (an "if A then B" does not itself say "if not A then not B"), so the branch would answer NOTHING.
Each row is a branch of one layer-1 function; `file:line` is where the branch and its `FALSE-kind` comment are.

| file:line | layer-1 function | the words the branch rests on |
| --- | --- | --- |
| sgd-compromise.l4:244 | `s 210(3AA) the compromise or arrangement is binding on the party` | If the conditions set out in subsection (3AB) are satisfied, a compromise or an arrangement is binding |
| sgd-compromise.l4:371 | `s 210(8)(a) the directors must instruct the accountants or solicitors named in the resolution to report` | Where any such compromise or arrangement ... has been proposed, the directors of the company must — (a) if a meeting of the members of the company... |
| sgd-compromise.l4:615 | `s 211(1) the notice carries what the subsection requires` | Where a meeting is summoned under section 210, there must |
| sgd-compromise.l4:640 | `s 211(2) the statement gives what the subsection requires` | Where the compromise or arrangement affects the rights of debenture holders, the statement must give the like explanation |
| sgd-compromise.l4:663 | `s 211(3) the company must furnish the person with a copy of the statement free of charge` | Where a notice given by advertisement includes a notification that copies of such a statement can be obtained, every creditor, member or holder of... |
| sgd-compromise.l4:854 | `s 212(2) the property vests in the transferee company and the liabilities become its liabilities by virtue of the order` | Where an order made under this section provides for the transfer of property or liabilities, then by virtue of the order that property is transferred |
| sgd-compromise.l4:863 | `s 212(2) the particular property vests free from the charge` | free in the case of any particular property if the order so directs, from any charge which is by virtue of the compromise or arrangement to cease t... |
| sgd-acquisition.l4:287 | `s 215(1B) the transferee has stated which of the terms is to apply on a failure to elect` | In offering alternative terms to the shareholders, the transferee must state |
| sgd-acquisition.l4:504 | `s 215(3)(a) the transferee must give notice of that fact to the holders of the remaining shares who have not assented` | Where ... comprise or include 90% ... then — (a) the transferee must |
| sgd-acquisition.l4:626 | `s 215(4) the transferee must transmit a copy of the notice and pay, allot or transfer the consideration to the transferor company` | Where a notice has been given by the transferee under subsection (1) and the Court has not, on an application made by the dissenting shareholder, o... |
| sgd-acquisition.l4:889 | `s 215(12) the body corporate is controlled by the transferee or the person` | a body corporate is controlled by a transferee or person mentioned in paragraph (a), (b) or (c) of subsection (9A) if — |
| sgd-acquisition.l4:994 | `s 215(11) the transferee is to be treated as having acquired the shares by virtue of the approval of the offer` | then, if — (a) the consideration ... does not at that time exceed the consideration specified in the terms of the offer; or (b) those terms are sub... |
| sgd-acquisition.l4:1124 | `s 215AA(5) the notice or document is complied with` | is complied with if the notice or document is given or sent by or to any of them |
| sgd-amalgamation.l4:165 | `s 215B(3) the amalgamation proposal provides as the subsection requires` | If shares of one of the amalgamating companies are held by or on behalf of another of the amalgamating companies, the amalgamation proposal |
| sgd-amalgamation.l4:349 | `s 215C(3) the director must sign the declaration` | Every director who votes in favour of the resolution and the making of the statements mentioned in subsection (2) must sign a declaration |
| sgd-amalgamation.l4:660 | `s 215D(6) the director must sign the declaration` | Every director who votes in favour of the making of the solvency statement mentioned in subsection (5) must sign a declaration |
| sgd-amalgamation.l4:880 | `s 215F(4) the Registrar must issue a certificate of confirmation of amalgamation to the amalgamated company` | Upon the application of the amalgamated company and payment of the prescribed fee, the Registrar must issue |
| sgd-amalgamation-solvency.l4:80 | `s 215I(2) the statement is in the form the subsection requires` | (a) if the amalgamating company is exempt from audit requirements under section 205B or 205C, must be in the form of a written declaration |
| sgd-amalgamation-solvency.l4:84 | `s 215I(2) the statement is in the form the subsection requires` | (b) if the amalgamating company is not such a company, must be in the form of a written declaration or must be accompanied by a report from its aud... |

### Reading (b): a grant, power or prohibition limited by its own wording answers NOTHING outside the limit (54 branches)

The other reading: outside the limit the text says no, so the branch would answer JUST FALSE.
| file:line | layer-1 function | the words the limit rests on |
| --- | --- | --- |
| sgd-compromise.l4:163 | `s 210(3) the meeting may be adjourned` | may be adjourned from time to time if the resolution for the adjournment is approved by a majority in number representing three-fourths in value |
| sgd-compromise.l4:247 | `s 210(3AA) the compromise or arrangement is binding on the party` | (a) in the case of a company in the course of being wound up, on the liquidator and contributories |
| sgd-compromise.l4:249 | `s 210(3AA) the compromise or arrangement is binding on the party` | (a) in the case of a company in the course of being wound up, on the liquidator and contributories of the company |
| sgd-compromise.l4:251 | `s 210(3AA) the compromise or arrangement is binding on the party` | (b) in the case of any other company, on the company and on all — |
| sgd-compromise.l4:270 | `s 210(4) the Court may grant its approval subject to the alteration or condition` | subject to such alterations or conditions as it thinks just |
| sgd-compromise.l4:302 | `s 210(5) the date from which the order takes effect` | on and from the date of lodgment or such earlier date as the Court may determine and as may be specified in the order |
| sgd-compromise.l4:324 | `s 210(6) a copy of the order must be annexed to the copy of the constitution` | to every copy of the constitution of the company issued after the order has been made |
| sgd-compromise.l4:347 | `s 210(7) the Court may do it by order` | may, by order, exempt a company from compliance with the requirements of subsection (6) or determine the period during which the company must so co... |
| sgd-compromise.l4:536 | `s 210(10B) how the Official Receiver must deal with what is received` | (a) deal with any moneys received under subsection (10A) ...; and (b) sell or dispose of any other consideration received under subsection (10A) |
| sgd-compromise.l4:834 | `s 212(1) the Court may provide for the matter by its order` | provide for all or any of the following matters: (a) ...; (f) ... |
| sgd-acquisition.l4:136 | `s 215(1) the transferee may give notice to the dissenting shareholder that it desires to acquire the shares` | give notice in the prescribed manner to any dissenting shareholder |
| sgd-acquisition.l4:204 | `s 215(1) the Court may order that the transferee is not entitled and bound to acquire the shares` | the Court thinks fit to order otherwise |
| sgd-acquisition.l4:310 | `s 215(1C)(a) the shares are to be disregarded` | shares that are issued after the date of the offer are to be disregarded |
| sgd-acquisition.l4:345 | `s 215(1C)(b) the shares are to be disregarded` | relevant treasury shares that cease to be held as treasury shares after the date of the offer are to be disregarded |
| sgd-acquisition.l4:372 | `s 215(1E) the subsequent issue of shares affects the matter` | does not affect — (a) such approval; (b) the transferee’s right to give a notice ...; or (c) the validity of any such notice |
| sgd-acquisition.l4:374 | `s 215(1E) the subsequent issue of shares affects the matter` | To avoid doubt, where the requisite percentage ... has been reached, any subsequent issue of shares pursuant to the exercise of an option or right... |
| sgd-acquisition.l4:553 | `s 215(3)(b) the holder may require the transferee to acquire the shares in question` | to the holders of the remaining shares ... who have not assented to the scheme or contract; and (b) any such holder may |
| sgd-acquisition.l4:721 | `s 215(7) how the Official Receiver must deal with what is received under subsection (6)` | (a) deal with any moneys received under subsection (6) ...; and (b) sell or dispose of any other consideration received under subsection (6) |
| sgd-acquisition.l4:813 | `s 215(8B) the definition of shares requires the securities to be treated that way` | Nothing in the definition ... is to be read as requiring any securities to be treated — (a) ...; or (b) ... |
| sgd-acquisition.l4:841 | `s 215(9) the shares are to be treated as held or acquired by the transferee` | by a related corporation of the transferee |
| sgd-acquisition.l4:845 | `s 215(9) the shares are to be treated as held or acquired by the transferee` | or by a nominee of that related corporation |
| sgd-acquisition.l4:846 | `s 215(9) the shares are to be treated as held or acquired by the transferee` | shares held or acquired — (a) by a nominee on behalf of the transferee; or (b) by a related corporation of the transferee or by a nominee of that r... |
| sgd-acquisition.l4:928 | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | in respect of an offer made on or after the date of commencement of section 10(a) of the Companies, Business Trusts and Other Bodies (Miscellaneous... |
| sgd-acquisition.l4:936 | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | by a body corporate that is controlled (within the meaning of subsection (12)) |
| sgd-acquisition.l4:937 | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | shares held or acquired — (a) ...; (b) ...; (c) ...; or (d) ... are also to be treated as held or acquired by the transferee |
| sgd-acquisition.l4:1042 | `s 215AA(2) the conditions for the exercise of the rights conferred by section 215(1) are satisfied` | (a) in the case of acquisitions of shares by virtue of acceptances of the offer — by the joint transferees acquiring or unconditionally contracting... |
| sgd-acquisition.l4:1046 | `s 215AA(2) the conditions for the exercise of the rights conferred by section 215(1) are satisfied` | (b) in other cases — by the joint transferees acquiring or unconditionally contracting to acquire the necessary shares either jointly or separately |
| sgd-acquisition.l4:1070 | `s 215AA(3) the conditions for the exercise of the rights conferred by section 215(3) are satisfied` | (a) in the case of acquisitions of shares by virtue of acceptances of the offer — by the joint transferees acquiring or unconditionally contracting... |
| sgd-acquisition.l4:1074 | `s 215AA(3) the conditions for the exercise of the rights conferred by section 215(3) are satisfied` | (b) in other cases — by the joint transferees acquiring or contracting (whether unconditionally or subject to conditions being met) to acquire the... |
| sgd-acquisition.l4:1183 | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made under a scheme or contract` | that does not prevent the offer from being an offer made under a scheme or contract for the purposes of section 215 if — |
| sgd-acquisition.l4:1221 | `s 215AB(3)(a) it is to be inferred that the offer cannot be an offer made under a scheme or contract unless the requirements of subsection (1)(a), (b) and (c) are met` | an offer which is not communicated to every holder of shares in the company |
| sgd-acquisition.l4:1229 | `s 215AB(3)(b) it is to be inferred that the offer cannot be an offer made under a scheme or contract unless the reason is the reason mentioned in subsection (2)` | an offer which is impossible, or more difficult, for certain persons to accept |
| sgd-amalgamation.l4:60 | `s 215A the companies may amalgamate and continue as one company` | 2 or more companies may amalgamate and continue as one company, which may be one of the amalgamating companies or a new company, in accordance with... |
| sgd-amalgamation.l4:146 | `s 215B(2) the amalgamation proposal may specify the date` | An amalgamation proposal may specify the date on which the amalgamation is intended to become effective |
| sgd-amalgamation.l4:179 | `s 215B(4) the cancellation of the shares is deemed to be a reduction of share capital within the meaning of the Act` | A cancellation of shares under this section |
| sgd-amalgamation.l4:201 | `s 215B(5) the name may be the name of the amalgamated company` | (b) a new name that has been reserved under section 27(12B) |
| sgd-amalgamation.l4:202 | `s 215B(5) the name may be the name of the amalgamated company` | the name of the amalgamated company may be — (a) the name of one of the amalgamating companies; or (b) a new name that has been reserved |
| sgd-amalgamation.l4:268 | `s 215C(2) the day is before the day of the general meeting` | before the general meeting |
| sgd-amalgamation.l4:564 | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate without complying with sections 215B and 215C` | may amalgamate and continue as one company ... without complying with sections 215B and 215C if the members of each amalgamating company, by specia... |
| sgd-amalgamation.l4:601 | `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without complying with sections 215B and 215C` | may amalgamate and continue as one company without complying with sections 215B and 215C if the members of each amalgamating company, by special re... |
| sgd-amalgamation.l4:629 | `s 215D(4) the resolution is deemed to be an amalgamation proposal that has been approved` | The resolution mentioned in subsection (1) or (2) (as the case may be) is deemed to be an amalgamation proposal that has been approved |
| sgd-amalgamation.l4:697 | `s 215D(8) the cancellation of the shares is deemed to be a reduction of share capital within the meaning of the Act` | A cancellation of shares under this section |
| sgd-amalgamation.l4:834 | `s 215F(1) what the Registrar must issue on receiving the documents and fees` | (a) if the amalgamated company is the same as one of the amalgamating companies ...; or (b) if the amalgamated company is a new company |
| sgd-amalgamation.l4:866 | `s 215F(3) the Registrar must remove the amalgamating companies, other than the amalgamated company, from the register` | as soon as practicable after the effective date of an amalgamation |
| sgd-amalgamation.l4:933 | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | On the date shown in a notice of amalgamation — (a) ...; (g) ... |
| sgd-amalgamation.l4:936 | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | On the date shown in a notice of amalgamation |
| sgd-amalgamation.l4:987 | `s 215H(1) the Court may make an order in relation to the amalgamation proposal` | a member or creditor of an amalgamating company or a person to whom an amalgamating company is under an obligation |
| sgd-amalgamation.l4:990 | `s 215H(1) the Court may make an order in relation to the amalgamation proposal` | If the Court is satisfied that giving effect to an amalgamation proposal would unfairly prejudice a member or creditor |
| sgd-amalgamation.l4:1021 | `s 215H(1) the order is within the Court's power` | make any order it thinks fit |
| sgd-amalgamation.l4:1023 | `s 215H(1) the order is within the Court's power` | make any order it thinks fit in relation to the amalgamation proposal |
| sgd-amalgamation.l4:1035 | `s 215H(2) the order may be made on the terms or conditions` | on such terms or conditions as the Court thinks fit |
| sgd-amalgamation.l4:1097 | `s 215K(2) how the Official Receiver must deal with what is received under subsection (1)` | (a) deal with any moneys received under subsection (1) ...; and (b) sell or dispose of any other consideration received under subsection (1) |
| sgd-amalgamation-solvency.l4:170 | `s 215I(4)(b) the board may rely on the valuation or estimate` | (b) may rely on valuations of assets or estimates of liabilities that are reasonable in the circumstances |
| sgd-amalgamation-solvency.l4:315 | `s 215J(3)(b) the board may rely on the valuation or estimate` | (b) may rely on valuations of assets or estimates of liabilities that are reasonable in the circumstances |


### Other readings that are marginal in this range

Each is also a fork-register entry, which has the text and the other readings.
The other reading is stated here so that a lawyer can overrule it without opening the register.

1. **s 215(1), the parenthesis "(other than shares already held at the date of the offer by the transferee ...)" (F-215-2).**
   Read literally, it stands in the class limb only ("or of the shares of that class (other than shares ...)"), so for a scheme for all the shares of the company the transferee's own shares stay in the count of the 90%.
   Other reading: it qualifies both limbs.
2. **s 215(1), (1C): which side of the 90% fraction the "disregarded" shares leave (F-215-1).**
   Taken: out of the total; the caller states the number of the counted shares whose holders approved.
   Other reading: out of the total and out of the approvals.
3. **s 215(2), the "until" bar where no statement is demanded (F-215-9).**
   Taken: `NOTHING`: the subsection sets the bar by the posting of the statement and says nothing of a case in which none is demanded.
   Other reading: `JUST FALSE` (no bar).
4. **s 215(6), "from the date on which the money or other consideration was received by the person" (finding 3).**
   Taken: "the person" is the company holding the money or consideration.
   Other reading: the person for whom it is held.
   The same words in ss 210(10A) and 215K(1) are unambiguous, because there "the person holding" is the subject.
5. **s 215C(2), "before the general meeting" (F-215C-1).**
   Taken: counted in days, so an act on an earlier day is before, an act on a later day is not, and an act on the day of the meeting cannot be placed from a date alone (`NOTHING`).
   Other reading: a moment, which would need the time of day of both the act and the start of the meeting.
6. **s 210(3), (3AB)(b), "three-fourths in value" (F-210-4).**
   Taken: at least three-fourths (exactly three-fourths is enough).
   Other reading: more than three-fourths.
7. **s 215(1), (1A), (4), "within 14 days of a statement being supplied" (F-215-5).**
   Taken: the day the statement is posted.
   Other reading: the day it is received.
8. **s 215(7), s 210(10B), s 215K(2): who has a claim against the Official Receiver.**
   The text says only that the Official Receiver "must deal with" the moneys "as if the moneys were paid to the Official Receiver under section 197 of the Insolvency, Restructuring and Dissolution Act 2018"; the encoding names the duty and no holder, and takes the outcome of that Act's section 197 as outside the sources.

### Reading a result: FALSE and NOTHING (sgd)

A function of this part answers one of three things.

- **`JUST TRUE`**: the case meets the words of the provision the function is named for.
- **`JUST FALSE`**: the text itself says no, in its own words.
  In this Part that is one of:
  - a `means` definition that the case does not meet ("company" in ss 210(11) and 212(6), "relevant treasury shares" in s 215(1D), "solvency statement" in ss 215I(1) and 215J(1));
  - a closed list the text states as a definition (who may apply under s 210(2));
  - a condition the text introduces with "if", or with "where", "when", "upon" or "on the application" (which the periods ruling counts the same way): the transferee's power in s 215(1) to give notice, for example, is stated for a scheme "approved ... by the holders of not less than 90%" within 4 months of the offer, so on facts without that approval the answer is "this section does not let the transferee give that notice on these facts", never "the transferee is forbidden";
  - a flat negative or a bar ("shall not be liable", "is not entitled or bound ... until 14 days after the posting");
  - a period the text itself fixes, missed ("within 7 days", "within one month", "before the expiration of 10 years");
  - an offence function's own question when an element is not met: "is the company guilty of the offence?" answers "this subsection makes the company guilty of nothing on these facts", never "the company has done nothing wrong";
  - a defence not shown: "this section gives no defence on these facts", never "no defence at all".
- **`NOTHING`**, "not covered": the text does not answer the case.
  In this Part that is one of:
  - a grant or power limited by its own wording, where the case is outside the limit or the "if" gate fails (the Court's approval "subject to such alterations or conditions as it thinks just"; the board "may rely on valuations ... that are reasonable in the circumstances"; the amalgamating companies' "may amalgamate ... without complying with sections 215B and 215C if" the members resolve it);
  - a list the text does not close ("may take into account (a) ... and (b) ...");
  - silence (a case the subsection does not speak to, such as no statement demanded under s 215(2), or a copy of the constitution issued before the order under s 210(6));
  - the text pointing outside the sources (the manner of a notice "prescribed", the prescribed form and fee, the value of a member's interest for the three-fourths test, the Court's judgment, and the winding-up outcomes of the Insolvency, Restructuring and Dissolution Act 2018).
  A caller must never turn `NOTHING` into `FALSE`: "not covered" is not "no".
- A **penalty function** (`s 210(9) the most the person may be sentenced to on conviction` and its four siblings) states the maximum fine, the longest imprisonment, whether the text allows both, and whether a default penalty also applies, for a person the offence function says is guilty; for anyone else the text states no penalty and it answers `NOTHING`.
  Sections 215C(6) and 215D(7) say "shall be guilty of an offence" and state no penalty, so there is no penalty function for them (finding 6).
- A **regulative rule** reads `FULFILLED`, `BREACH` or `RESIDUAL` in a trace.
  A duty with a time limit reads `BREACH` when the time is missed; a duty with no time limit never does, which is why those rules are listed under "Rules with no breach path (sgd)" and not given a deadline the text does not state.

## Seams (sgd)

A part cannot import another part (separate sandboxes until the merge), so a fact that another part's provision answers is an input named for the fact and its section; the seat asks the same fact under the same name.
Each row is a seam this part took, with its source as `inputs/PLAN.md` section 4 and `inputs/XREFS.md` give it.
"Plan" says whether PLAN section 4 already names the seam; the rows marked "not in the plan" are seams this pass found.

### Seams where this part asks (inputs taken)

| asking provision | answering provision or source | input, name and type | plan |
| --- | --- | --- | --- |
| s 215I(2)(a), (b) | ss 205B, 205C (sgc2) | `the amalgamating company is exempt from audit requirements under section 205B or 205C` BOOLEAN (PLAN section 4A gives `the company is exempt ...`; the subject is the amalgamating company here) | plan, A |
| s 215I(4)(a)(i) | s 201(2) and (5) (sgc1) | `the board had regard to the most recent financial statements of the amalgamating company that comply with section 201(2) and (5), as the case may be` BOOLEAN | plan, A (the keel's `s 7A(4)(a)(i)` takes the directors and "the company"; section 215I(4)(a) has the board and the amalgamating company, so the name differs) |
| s 215J(3)(a)(i) | s 201(2) and (5) (sgc1) | `the board had regard to the most recent financial statements of the amalgamating company and the other amalgamating companies that comply with section 201(2) and (5), as the case may be` BOOLEAN | not in the plan |
| ss 215B(5)(b), 215E(1)(d) | s 27(12B) (a later wave) | `the new name has been reserved under section 27(12B)`; `a copy of any notice or other documentary evidence that the name has been reserved under section 27(12B) is filed` BOOLEAN each | XREFS (s 27), not in the plan |
| s 215B(1)(ca) | s 173(1)(a) (sgb2) | `s 215B(1)(ca) the residential address and contact address of every director of the amalgamated company which is contained in the register of directors kept by the Registrar under section 173(1)(a) are stated` BOOLEAN | XREFS (s 173), not in the plan |
| ss 215E(2), 215F(1)(b) | s 19 (a later wave) | none taken: section 215E(2) only deems section 19(1)(a) and (c) complied with, and the notice of incorporation "under section 19(4)" is a name inside the Registrar's duty in section 215F(1) | XREFS (s 19), not in the plan |
| ss 210(11), 212(6) | the Insolvency, Restructuring and Dissolution Act 2018 (winding up) | `the corporation is liable to be wound up under the Insolvency, Restructuring and Dissolution Act 2018` BOOLEAN | brief ("take the outcome as an input") |
| ss 210(2)(a), 210(3AA)(a), 210(10) | the same Act | `the company is being wound up`; `the company is in the course of being wound up`; `no order has been made or resolution passed for the winding up of the company` BOOLEAN each | brief |
| s 212(1) | s 71 of the same Act | `an application is made to the Court under Part 7 or section 71 of the Insolvency, Restructuring and Dissolution Act 2018 for the approval of a compromise or arrangement` BOOLEAN | not in the plan |
| ss 210(10B), 215(7), 215K(2) | s 197 of the same Act | none taken as an input: the Official Receiver's duty is encoded as the text states it ("as if the moneys were paid ... under section 197"), with the treatment declared as a type (`s 210(10B) treatment`, `s 215(7) treatment`, `s 215K(2) treatment`) | not in the plan |
| ss 211(5), 212(3) | the default penalty (s 4(1) "default penalty", a later wave) | not an input: the penalty record `s 210(9) penalty` carries the flag `the person is also liable to a default penalty`, set from the text; no amount is encoded | plan, A (one BOOLEAN each for the s 4(1) terms) |
| s 215(9)(b) | s 6 (the keel) | `the corporation is deemed to be related to the transferee by virtue of section 6` BOOLEAN, with the keel's `s 4(1) "related corporation" the other corporation is a related corporation of the corporation` | plan, B |
| ss 215(1), 215E(1), 215F(4), 215(12)(a) | the regulations ("prescribed") | `the notice is given in the prescribed manner` (s 215(1)); `the documents are filed in the prescribed form with the particulars required in the form` and `the prescribed fee is paid` (s 215E(1)); `the prescribed fee has been paid` (s 215F(4)) BOOLEAN each; `s 215(12)(a) the percentage of the voting power prescribed, if any` MAYBE NUMBER; the notice of s 215(3)(a), which the text also requires "in the prescribed manner", is not asked for its manner (finding 9) | plan, A (prescribed terms) |
| s 215(9A) | s 10(a) of the Companies, Business Trusts and Other Bodies (Miscellaneous Amendments) Act 2023 (commencement) | `the offer was made on or after the date of commencement of section 10(a) of the Companies, Business Trusts and Other Bodies (Miscellaneous Amendments) Act 2023` BOOLEAN (finding 8) | not in the plan |
| s 215D(1), (2) | ss 5B and 5(1) (the keel's group functions) | `the amalgamating companies are a company and one or more of its wholly-owned subsidiaries`; `the amalgamating companies are two or more wholly-owned subsidiary companies of the same corporation` BOOLEAN each (see "The brief governs over PLAN.md") | plan names the keel functions; not called |
| s 210(3), (3AB)(b) | none (the text does not say how a member's "value" is measured) | the four numbers of `s 210(3) vote` (those present and voting, those in favour, and the value each holds) | fork F-210-3 |
| the Court's judgment: ss 210(4), 215(1), 215H(1), (2) | the Court | `the Court thinks fit ...`, `the Court is satisfied that ...` BOOLEAN (a conditional input: a judgment the text hands to the Court is never guessed) | brief |

The keel's `s 7A(1) the statement is a solvency statement` is not called: sections 215I and 215J each define their own "solvency statement" (for the amalgamating company and for the amalgamated company), with their own form and their own content, and the keel's `s 7A` is for other proposals.

### Seams where this part answers (other parts take the fact as an input)

`inputs/XREFS.md` lists the cites of this part's sections from other parts: s 210 (the keel at lines 1057 and 1058; sga1: 6630; sga2: 7454; sga3: 9105; a later wave: 15427; sgg: 24178), s 215 (sga3: 9223), and ss 215C and 215D (a later wave: 15419).
The text at those lines needs only the plain fact (a scheme of arrangement approved by the Court under s 210, an order made under s 210, a meeting ordered by the Court under s 210, a notice received under s 215, a general meeting of an amalgamating company mentioned in s 215C or 215D), which each of those parts takes as its own input.
Where this part states the same fact, the function is:

| the fact another part takes | this part's function |
| --- | --- |
| a compromise or arrangement approved by the Court under s 210; an order of the Court made under s 210 | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` (its condition (c) is the Court's order); `s 210(5) the order cannot yet have effect` |
| a meeting ordered by the Court under s 210 | `s 210(1) the Court may order a meeting to be summoned` |
| a notice received under s 215 | `s 215(1) the transferee may give notice to the dissenting shareholder that it desires to acquire the shares` |
| a general meeting of an amalgamating company mentioned in s 215C or 215D | `s 215C(1) the amalgamation proposal has been approved as the subsection requires`; `s 215D(1) ...` and `s 215D(2) ...` |

## Split sites (sgd)

The brief leaves two questions to be decided site by site and counted here, without harmonising with any other part:

- **(i)** an unmet element of an offence or a contravention: does the function answer `JUST FALSE` or `NOTHING`?
- **(ii)** a "may" gated by "where", "when", "upon", "on application" and the like: `JUST FALSE` (the periods ruling's rule (b)) or `NOTHING` (the grant ruling)?

### Site (i): an unmet element of an offence (answer taken: `JUST FALSE` at every site)

11 functions in 7 offence provisions, 14 branches.
Reason, from the Guide's own words (line 98): “keep `JUST FALSE` ... for a bar, a duty or the provision's own question”.
An offence function's own question is "is this person guilty of the offence?", and the text answers it only for a person whose conduct meets the elements; for anyone else it makes no one guilty, and the function says so (never that the person has done nothing wrong).
The other reading, `NOTHING`, treats the text as silent about a person who does not meet an element.

| layer-1 function | branches | fork line |
| --- | --- | --- |
| `s 210(9) the company is guilty of the offence` | 1 | F-210-10 |
| `s 210(9) the officer is guilty of the offence` | 2 | F-210-10 |
| `s 211(5) the company is guilty of the offence` | 1 | F-211-1 |
| `s 211(5) the officer is guilty of the offence` | 2 | F-211-1 |
| `s 211(5) and (7) the person is liable under subsection (5)` | 1 | F-211-1 |
| `s 212(3) the company is guilty of the offence` | 1 | F-212-2 |
| `s 212(3) the officer is guilty of the offence` | 2 | F-212-2 |
| `s 215C(6) the director is guilty of the offence` | 1 | F-215C-2 |
| `s 215D(7) the director is guilty of the offence` | 1 | F-215C-2 |
| `s 215I(6) the director is guilty of the offence this subsection creates` | 1 | F-215I-2 |
| `s 215J(5) the director is guilty of the offence this subsection creates` | 1 | F-215I-2 |

### Site (ii): a "may" gated by "where", "when", "upon" or an application (answer taken: `JUST FALSE` where the gate fails)

7 functions.
Reason, from the Guide's own words (line 93, rule (b)): “a "where ..." condition: when it fails the answer is `JUST FALSE`”, and (line 94, rule (c)) “"when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above”; "on an application" and "on the application" are read as "upon" (an extension this pass made; the brief's own list of gates names "on application").
The Guide's grant ruling (line 99, limit 3) says not to change but to list “a "may" function whose gate is "where", "when" or "upon"”: each is listed in the fork register for the maintainer or a lawyer, and here.
The other reading, `NOTHING`, rests on the "In short" line on grants (line 86).
Where one of these functions also has a branch for a limit in the text's own wording, that branch is named under limit 1 below.

| layer-1 function | the gate | fork line |
| --- | --- | --- |
| `s 210(1) the Court may order a meeting to be summoned` | "Where a compromise or an arrangement is proposed ..." and "on the application in a summary way of any person referred to in subsection (2)" | F-210-2 |
| `s 210(10) the Court may restrain further proceedings against the company` | "Where no order has been made or resolution passed for the winding up of a company and any such compromise or arrangement has been proposed ..." | F-210-2 |
| `s 212(1) the Court may provide for the matter by its order` | "Where an application is made to the Court ... and it is shown to the Court that ..." | F-212-1 |
| `s 215(1) the transferee may give notice to the dissenting shareholder that it desires to acquire the shares` | "Where a scheme or contract ... has ... been approved" | F-215-4 |
| `s 215(1) the Court may order that the transferee is not entitled and bound to acquire the shares` | "on an application made by the dissenting shareholder" | F-215-6 |
| `s 215(3)(b) the holder may require the transferee to acquire the shares in question` | "Where ... those shares ... comprise or include 90% ..., then ... (b) any such holder may" | F-215-12 |
| `s 215H(1) the Court may make an order in relation to the amalgamation proposal` | "on the application of that person made at any time before the date on which the amalgamation becomes effective" | F-215H-1 |

The four "entitled"-named functions, also listed under limit 3 (“an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it)”) and left as they are, all answer `JUST FALSE` where their "where" or "when" gate fails (fork F-215-7):
`s 215(1) the transferee is entitled and bound to acquire the dissenting shareholder's shares`, `s 215(1A) the dissenting shareholder is entitled to elect which of the terms the shareholder prefers`, `s 215(2) the dissenting shareholder is entitled to require the transferor company to supply the statement` and `s 215(3) the transferee is entitled and bound to acquire the shares`.
(`s 215(2) the transferee is not yet entitled or bound to acquire the shares` is a bar, not an entitlement: it follows the "until" ruling, line 94 rule (d).)

### The grant ruling's limit 1: `NOTHING` for a grant whose "if" gate or limit fails

Thirteen functions carry a limit-1 branch, each with its fork line (the Guide, line 97: “answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ... whose `if` gate failed”):

| layer-1 function | fork line |
| --- | --- |
| `s 210(3) the meeting may be adjourned` | F-210-5 |
| `s 210(4) the Court may grant its approval subject to the alteration or condition` | F-210-7 |
| `s 215A the companies may amalgamate and continue as one company` | F-215A-1 |
| `s 215B(2) the amalgamation proposal may specify the date` | F-215B-1 |
| `s 215B(5) the name may be the name of the amalgamated company` | F-215B-2 |
| `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate without complying with sections 215B and 215C` | F-215D-1 |
| `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without complying with sections 215B and 215C` | F-215D-1 |
| `s 215I(4)(b) the board may rely on the valuation or estimate` | F-215I-1 |
| `s 215J(3)(b) the board may rely on the valuation or estimate` | F-215I-1 |
| `s 215H(1) the order is within the Court's power` | F-215H-2 |
| `s 215H(2) the order may be made on the terms or conditions` | F-215H-2 |
| `s 215(1) the Court may order that the transferee is not entitled and bound to acquire the shares` (its branch where the Court does not think fit) | F-215-6 |
| `s 215H(1) the Court may make an order in relation to the amalgamation proposal` (its branches where the Court is not satisfied or the person is not within the three) | F-215H-1 |

Three grant-named functions answer `NOTHING` for a different reason (a grant that names things without "only", not a failed "if"), and have their own fork lines: `s 210(7) the Court may do it by order` (F-210-12), and `s 215I(5) ...` and `s 215J(4) ...` (F-215I-3, "list not closed").

### The rulings relied on, word for word

Recorded mechanically from `inputs/ENCODING-GUIDE.md` (section 5), with the line each is on:

> **Guide line 86.** In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
>
> **Guide line 87.** Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
>
> **Guide line 93.** **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
>
> **Guide line 94.** **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
>
> **Guide line 96.** **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The ruling sets three limits:
>
> **Guide line 97.** 1. answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed;
>
> **Guide line 98.** 2. keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question;
>
> **Guide line 99.** 3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it).

## Rules with no breach path (sgd)

> Added 2026-11-27 (decided by Claude, assumed, not ruled): this section was written before the pass recorded in `lest-without-deadline.md`, and it is no longer true of the rules listed below.
> Each of them now takes an input-length `WITHIN` and can reach `BREACH`, so read "no time limit", "no deadline" and "no breach path" of them as the position before that pass, here and wherever else these notes say so of them:
>
> - `s 210(10B)(a) the Official Receiver must deal with the moneys as if they were paid under section 197`
> - `s 210(10B)(b) the Official Receiver must sell or dispose of the other consideration`
> - `s 210(8)(a) a director must instruct the accountants or solicitors named in the resolution to report`
> - `s 211(3) the company must furnish the person with a copy of the statement free of charge`
> - `s 215F(1) the Registrar must issue the notice of amalgamation on receiving the documents and fees`
> - `s 215K(2)(a) the Official Receiver must deal with the moneys as if they were paid under section 197`
> - `s 215K(2)(b) the Official Receiver must sell or dispose of the other consideration`
> - `s 215C(3) a director who votes in favour must sign the declaration`
> - `s 215F(3) the Registrar must remove the amalgamating companies from the register`
> - `s 215F(4) the Registrar must issue the certificate of confirmation of amalgamation`
> - `s 215D(6) a director who votes in favour must sign the declaration`
> - `s 215(2) the transferor company must supply the dissenting shareholder with the written statement`
> - `s 215(4) the transferee must transmit the notice and pay, allot or transfer the consideration`
> - `s 215(4) the transferor company must register the transferee as the holder of the shares`
> - `s 215(5) the transferor company must pay the sums received into a separate bank account`
> - `s 215(7)(a) the Official Receiver must deal with the moneys as if they were paid under section 197`
> - `s 215(7)(b) the Official Receiver must sell or dispose of the other consideration`
>
> The other rules named in this section are unchanged.

40 regulative rules are encoded (every one has at least one `#TRACE`, and every trace carries an `-- EXPECT` line).
15 have a time limit in the text and each of them has a trace that reaches `BREACH` (25 `BREACH` traces in all, 43 `FULFILLED`, 27 `RESIDUAL`; 95 traces in the four tests files).
The other 25 are a `MUST` with no time limit: a late act still reads `FULFILLED`, so no trace can show them breached, and no deadline has been invented for them.
Where the text states a consequence for the default, the table names the offence function that encodes it; that function is tested on its own, not through the trace.

| provision | rule | time limit in the text | consequence the text states, and the function that encodes it |
| --- | --- | --- | --- |
| s 210(6) | `s 210(6) the company must annex a copy of the order to every copy of the constitution issued after the order` | none | `s 210(9)` offence functions: a fine not exceeding $2,000, for the company and every officer in default |
| s 210(8)(a) | `s 210(8)(a) a director must instruct the accountants or solicitors named in the resolution to report` | none | `s 210(9)` offence functions: a fine not exceeding $2,000, for the company and every officer in default |
| s 210(10B)(a) | `s 210(10B)(a) the Official Receiver must deal with the moneys as if they were paid under section 197` | none | none stated |
| s 210(10B)(b) | `s 210(10B)(b) the Official Receiver must sell or dispose of the other consideration` | none | none stated |
| s 211(3) | `s 211(3) the company must furnish the person with a copy of the statement free of charge` | none | `s 211(5)` offence functions: a fine not exceeding $5,000 or imprisonment not exceeding 12 months, for the company and every officer in default |
| s 215(1B) | `s 215(1B) the transferee must state which of the alternative terms is to apply on a failure to elect` | none | none stated |
| s 215(2) | `s 215(2) the transferor company must supply the dissenting shareholder with the written statement` | on a written demand; no period for supplying it | none stated |
| s 215(4) | `s 215(4) the transferee must transmit the notice and pay, allot or transfer the consideration` | a first day (after the waiting period) and no last day | none stated |
| s 215(4) | `s 215(4) the transferor company must register the transferee as the holder of the shares` | "thereupon" (after the transmission); no period | none stated |
| s 215(5) | `s 215(5) the transferor company must pay the sums received into a separate bank account` | a standing duty; no period | none stated |
| s 215(5) | `s 215(5) the transferor company must hold the sums and other consideration in trust` | a standing duty; no period | none stated |
| s 215(7)(a) | `s 215(7)(a) the Official Receiver must deal with the moneys as if they were paid under section 197` | none | none stated |
| s 215(7)(b) | `s 215(7)(b) the Official Receiver must sell or dispose of the other consideration` | none | none stated |
| s 215AA(6) | `s 215AA(6) the joint transferees must make the notice by all of them, signed for each company by a director of that company` | none | none stated |
| s 215C(3) | `s 215C(3) a director who votes in favour must sign the declaration` | none | `s 215C(6)` offence functions: guilty of an offence; no penalty stated (finding 6) |
| s 215D(6) | `s 215D(6) a director who votes in favour must sign the declaration` | none | `s 215D(7)` offence functions: guilty of an offence; no penalty stated (finding 6) |
| s 215F(1) | `s 215F(1) the Registrar must issue the notice of amalgamation on receiving the documents and fees` | upon receipt of the documents and fees; no period | none stated |
| s 215F(3) | `s 215F(3) the Registrar must remove the amalgamating companies from the register` | "as soon as practicable"; no number of days | none stated |
| s 215F(4) | `s 215F(4) the Registrar must issue the certificate of confirmation of amalgamation` | upon application and payment of the fee; no period | none stated |
| s 215K(2)(a) | `s 215K(2)(a) the Official Receiver must deal with the moneys as if they were paid under section 197` | none | none stated |
| s 215K(2)(b) | `s 215K(2)(b) the Official Receiver must sell or dispose of the other consideration` | none | none stated |
| s 215I(3) | `s 215I(3) a director must take into account all liabilities of the amalgamating company` | none | none stated |
| s 215I(4)(a) | `s 215I(4)(a) the board must have regard to the most recent financial statements and all other circumstances` | none | none stated |
| s 215J(2) | `s 215J(2) a director must take into account all liabilities of the amalgamated company` | none | none stated |
| s 215J(3)(a) | `s 215J(3)(a) the board must have regard to the most recent financial statements and all other circumstances` | none | none stated |

## What the text turns out to say (numbered findings)

Each finding is something the encoding had to decide because of what the text says or fails to say; line numbers are of `inputs/CoA1967.txt`.
Layer-1 comments cite these numbers (findings 1, 3 and 6).

1. **The rendering interleaves the labels of s 210(3AA) and (3AB).**
   In (3AA) the closing words of each limb are printed after its list of three kinds of person, under a repeated label: "(a) as the case may be; or" (line 20256) and "(b) as the case may be." (line 20268).
   In (3AB) the tails "(a) present and voting either in person or by proxy at the meeting or the adjourned meeting agrees to the compromise or arrangement;" (lines 20288-20290) and "(b) present and voting either in person or by proxy at the meeting or the adjourned meeting, as the case may be;" (lines 20303-20304) are printed after the lists they complete.
   They are read as the tails of limbs (a) and (b), not as new paragraphs; the only genuine third condition is "(c) the compromise or arrangement is approved by order of the Court" (lines 20306-20307).
   The coverage table gives each such line to the row of the paragraph it completes.

2. **s 215(1): the parenthesis "(other than shares already held at the date of the offer by the transferee ...)" stands in the class limb only** (lines 20601-20605; fork F-215-2).
   Read literally, for a scheme for all the shares of the company the transferee's own shares stay in the count.
   This is a marginal reading for a lawyer.

3. **s 215(6): "from the date on which the money or other consideration was received by the person" does not say which person** (lines 20773-20782).
   Section 215(6) has two persons in view, the company holding the money in trust and the person for whom it is held.
   The same words in ss 210(10A) (lines 20381-20392) and 215K(1) (lines 21666-21678) follow "the person holding the money or other consideration", so "the person" there can only be the holder.
   Layer 1 reads s 215(6) the same way: the date the company holding it received it.

4. **There is no "associate" in the range.**
   PLAN section 6 sends this part to `s 7(5)` for "associate" in the compulsory-acquisition provisions; section 215(9A) names its own persons instead (lines 20864-20890), and layer 1 encodes those words.

5. **s 215E(1) names no party who must file.**
   "The following documents must be filed with the Registrar, in the prescribed form ..., together with payment of the prescribed fee" (lines 21365-21368) is passive.
   The jural-relations table says "no bearer named", and layer 1 states what has been filed rather than who must file it.

6. **ss 215C(6) and 215D(7) say "shall be guilty of an offence" and state no penalty** (lines 21246-21247, 21357-21358).
   Of the five provisions that do state a penalty (ss 210(9), 211(5), 212(3), 215I(6) and 215J(5)), only s 212(3) mentions a "default penalty" (line 20565); no other provision of the range mentions one.
   The general penalty provision of the Act is not among the sources, so no penalty function is written for these two (they return no fine); a reader who wants the general penalty must supply it.

7. **s 215AB(1): a failed "if" answers `NOTHING`, not `JUST FALSE`, because s 215AB(3)(a) says so** (lines 21011-21014 and 21050-21056).
   Subsection (3)(a): "It is not to be inferred ... that an offer which is not communicated to every holder of shares in the company cannot be an offer made under a scheme or contract for the purposes of section 215 unless the requirements of subsection (1)(a), (b) and (c) are met".
   An unmet "if" in subsection (1) therefore does not make the offer a non-offer, and the function answers "not covered" (fork F-215AB-1).

8. **s 215(9A): the commencement date is in an amendment mark, which is not text.**
   The subsection speaks of "an offer made on or after the date of commencement of section 10(a) of the Companies, Business Trusts and Other Bodies (Miscellaneous Amendments) Act 2023" (lines 20864-20867); the date "wef 01/07/2023" appears only in the mark at line 20892.
   The encoding asks the fact as an input (`the offer was made on or after the date of commencement of section 10(a) ...`) and does not read the date from the mark.

9. **s 215(3)(a): the manner of the notice is not asked.**
   The text requires the transferee to "give notice of that fact in the prescribed manner" (lines 20709-20715).
   Section 215(1)'s power to give notice asks whether the notice is given in the prescribed manner (`the notice is given in the prescribed manner`, `NOTHING` where it is not, as the manner is outside the sources).
   The s 215(3)(a) functions test the time ("within one month from the date of the transfer"), whether the 90% was reached and whether the transferee had already complied, and the duty rule's action is the giving of the notice; none asks the manner.
   This is a gap, not a decision: a notice given in another manner reads as a notice given in time.

10. **ss 215I(1) and 215J(1) define two differently shaped statements.**
    Section 215I(1) says a solvency statement for the amalgamating company is "a statement by the board of directors ... that it has formed the opinion" in two respects, "being a statement which complies with subsection (2)", and subsection (2) lets a company that is not exempt from audit supply either a written declaration or a statement accompanied by the auditor's report (lines 21516-21547).
    Section 215J(1) says a solvency statement for the amalgamated company is "a written declaration by the board of directors of each amalgamating company" (lines 21600-21603), with no auditor's report alternative.
    The keel's `s 7A` solvency statement is not used for either.

11. **s 215D asks for two solvency assurances.**
    The resolution of s 215D(1) and (2) must contain the term that "the directors ... are satisfied that the amalgamated company will be able to pay its debts as they fall due" (lines 21290-21294, 21316-21319), and s 215D(5) separately requires the board to make a solvency statement under s 215J before the meeting begins (lines 21340-21344).
    Layer 1 encodes them as two separate conditions; the text does not say whether one satisfies the other.

12. **Duties of officials in the seat layer.**
    The brief says the seat is never for an official.
    Six seat questions are about a duty of an official (the Registrar's duties in ss 215F(1), (3) and (4); how the Official Receiver deals with what is transferred, ss 210(10B), 215(7) and 215K(2)); each is asked by the person who relies on the duty, never by the official, and names the duty from that person's side (see "Seat layer (sgd)").

## What the stable binary does not accept

The brief says the binary governs where the skills describe a construct it rejects.
Everything below was run on both builds, `1.6.110 (main, e51181d, 2026-11-11)` and `1.6.109 (main, 4c887e0, 2026-11-04)`, with the probe files in `work/probe/` (`bq_*.l4`, `br_*.l4`, `bs_refuse.l4`); the keel's own list is in `inputs/PLAN.md` section 5 and is not repeated.

**Loud (the binary says so).**
- `JUST (r's f)` is required: `JUST r's f` reads as `(JUST r)'s f` and gives `check/not-a-function` followed by `check/type-mismatch` (`bq_just.l4`).
- A bullet `•` in a `LIST` is `parse/syntax-error` (`bq_bullet.l4`); a list is written one element per line.
- `BECAUSE` after an expression is `parse/unexpected-BECAUSE` (`br_because.l4`); only `LEST BREACH ... BECAUSE` is used, as the brief says.

**Silent (a wrong answer, exit code 0).**
- `NOT a AND b` parses as `NOT (a AND b)`: with `a` and `b` both `FALSE` it answers `TRUE`, and an assertion that expects `FALSE` fails (`bq_not.l4`; the failure is reported only as `eval/assertion-failed`).
  A one-line scan of every `sgd-*.l4` file finds no `NOT x` that is not in parentheses and is directly followed by `AND` or `OR`.

**Where the brief and the binaries disagree (not followed; recorded so the lead can decide).**
The brief says `REFUSE`, `#ASSERT REFUSED` and `YMD` are not available on the stable binary.
Both builds above accepted them:
- `` `br r` MEANS REFUSE "because" `` checks without a message, and `#EVAL` of it prints "The model refuses to answer: because" with code `eval/refused` (`bs_refuse.l4`);
- `#ASSERT REFUSED` parses and runs (`br_assert.l4` reports `assertion failed: expected a refusal, but the expression produced a value`, which is the assertion working, not a parse error);
- `YMD 2020 1 1`, with `IMPORT daydate`, evaluates to `DATE OF 1, 1, 2020` (`bs_refuse.l4`).
This pass used none of them: a case outside the encoding is `NOTHING` or a named "not covered" constructor, asserted, and dates are written `Date day month year`.
Whether the "stable build" the brief means is a different build from these two `main` builds is not something this pass can tell.

## Seat layer (sgd)

`sgd-seat.l4` is the seat of an individual who is, or is about to become, a director, a company secretary or a member of a company, or who deals with one (a creditor, a holder of units of shares, a dissenting shareholder, the person holding money in trust, the directors of an amalgamating company).
It is never a seat for an official: the Court, the Registrar and the Official Receiver appear only as the person against whom a duty or power is asked, never as the asker.

- 150 questions and 317 inputs, generated by `work/seatgen.py` from `work/tpl/sgd-seat-*.l4t` (an input is defined once with `@@DESC`, so one fact has one name and one `@desc` wherever it is asked); `l4 check` is clean on both builds.
- Every question is `@export Under section N, <question>?` with a `GIVEN` input per fact, each with an `@desc` written as the question put to the person in plain words, and a body `DECIDE <title minus ?> IS <layer-1 call> WHERE <records built from the plain inputs>`.
  123 questions pass their inputs straight to one layer-1 rule; 27 build a record or a date from plain inputs first (their cases are written by hand).
- The `§` headings are in the text's order: ss 210, 211, 212, 215 (with 215(2), 215(3) and (3A), 215(4) to (7), 215(8) to (12)), 215AA, 215AB, 215A, 215B, 215C, 215D, 215E, 215F, 215G, 215H, 215I, 215J, 215K.
- Every question's name begins "Under section N," and names the same direction as the layer-1 function it calls (a "must" duty is asked as "must ...?", a power as "may ...?", an offence as "am I guilty ...?" or "is the company guilty ...?"); no question reverses the direction of its layer-1 function.
- Questions whose name and body differ in the subject they frame (the direction is the same):
  - ss 210(10B), 215(7) and 215K(2): the question asks "how is what has been transferred to the Official Receiver dealt with?" (framed on the thing dealt with), where the layer-1 function says how "the Official Receiver must deal with what is received" (the Official Receiver's duty).
  - s 215F(3): the question asks whether "the amalgamating companies other than the amalgamated company [are] to be removed from the register on the day I ask about" (framed on the companies), where the layer-1 function is the Registrar's duty to remove them.
  - s 210(9) penalty: the question says "what is the most I may be sentenced to on conviction as an officer in default?", where the layer-1 function is "the most the person may be sentenced to on conviction" for anyone the offence function says is guilty.
- `sgd-cases-seat.l4`: 597 assertions, all satisfied on both builds (597 satisfied, 0 failed on the run of 1.6.110, 597 satisfied, 0 failed on 1.6.109; check.sh).
  For a question that passes its inputs straight to one layer-1 rule, the cases are that rule's layer-1 tests restated through the question, each with the words that decide it beside it; for the other questions the cases are written by hand from the text.
  A mutation probe on a copy of the seat (the first two arguments of the call in the s 215(3)(b) question swapped) made 2 of the 597 assertions fail on 1.6.110, so the cases detect a wrong call and not only a wrong rule; the copy was deleted.
  Regenerating the file overwrites it: run `work/seatcases.py` and then `work/addtrailer.py`, which adds the closing "written = satisfied" line.

| # | question (the `@export` name) | layer-1 rules it calls | inputs | cases |
| --- | --- | --- | --- | --- |
| 1 | Under section 210(2), am I a person who may apply to the Court for a meeting to be summoned about a compromise or arrangement? | `s 210(2) the person is a person referred to in subsection (1)` | 2 | 8 |
| 2 | Under section 210(1), may the Court order a meeting of the creditors or members to be summoned about the compromise or arrangement proposed? | `s 210(1) the Court may order a meeting to be summoned` | 3 | 8 |
| 3 | Under section 210(3), may the meeting be adjourned on the vote that was taken? | `s 210(3) the meeting may be adjourned` | 4 | 5 |
| 4 | Under section 210(3AB), are the conditions for the compromise or arrangement to be binding satisfied? | `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | 7 | 6 |
| 5 | Under section 210(3AA), is the compromise or arrangement binding on me? | `s 210(3AA) the compromise or arrangement is binding on the party`; `s 210(3AB) the conditions for the compromise or arrangement to be binding are satisfied` | 9 | 8 |
| 6 | Under section 210(4), may the Court grant its approval subject to an alteration or condition? | `s 210(4) the Court may grant its approval subject to the alteration or condition` | 1 | 2 |
| 7 | Under section 210(5), is the Court's order unable yet to have effect because no copy has been lodged with the Registrar? | `s 210(5) the order cannot yet have effect` | 1 | 2 |
| 8 | Under section 210(5), from what date does the Court's order take effect? | `s 210(5) the date from which the order takes effect` | 4 | 6 |
| 9 | Under section 210(6), must a copy of the Court's order be annexed to the copy of the constitution that is being issued? | `s 210(6) a copy of the order must be annexed to the copy of the constitution` | 4 | 5 |
| 10 | Under section 210(7), may the Court do what the order does about annexing? | `s 210(7) the Court may do it by order` | 1 | 3 |
| 11 | Under section 210(8)(a), must the directors instruct the accountants or solicitors named in the resolution to report? | `s 210(8)(a) the directors must instruct the accountants or solicitors named in the resolution to report` | 2 | 3 |
| 12 | Under section 210(8)(b), were the reports made available at the registered office at least 7 days before the meeting? | `s 210(8)(b) the reports have been made available at least 7 days before the meeting` | 2 | 6 |
| 13 | Under section 210(9), is the company guilty of an offence for its default in annexing the order or in giving effect to the members' direction? | `s 210(9) the company is guilty of the offence` | 2 | 3 |
| 14 | Under section 210(9), am I guilty of an offence as an officer of the company in default? | `s 210(9) the officer is guilty of the offence` | 4 | 6 |
| 15 | Under section 210(9), what is the most I may be sentenced to on conviction as an officer in default? | `s 210(9) the most the person may be sentenced to on conviction`; `s 210(9) the officer is guilty of the offence` | 4 | 6 |
| 16 | Under section 210(10), may the Court restrain further proceedings against the company? | `s 210(10) the Court may restrain further proceedings against the company` | 3 | 4 |
| 17 | Under section 210(10), may further proceedings against the company continue? | `s 210(10) further proceedings against the company may continue` | 2 | 3 |
| 18 | Under section 210(10A), was what is held in trust for a person transferred to the Official Receiver within the time the subsection allows? | `s 210(10A) the transfer to the Official Receiver is within the time the subsection allows` | 3 | 7 |
| 19 | Under section 210(10B), how is what has been transferred to the Official Receiver dealt with? | `s 210(10B) how the Official Receiver must deal with what is received` | 2 | 3 |
| 20 | Under section 210(11), is the thing within the word "arrangement"? | `s 210(11) "arrangement" the thing is within the word arrangement` | 2 | 3 |
| 21 | Under section 210(11), is the body a "company" for the purposes of section 210? | `s 210(11) "company" the body is a company` | 1 | 2 |
| 22 | Under section 210(11), am I a "holder of units of shares"? | `s 210(11) "holder of units of shares" the person is a holder of units of shares` | 1 | 2 |
| 23 | Under section 211(1), does the notice carry what the subsection requires? | `s 211(1) the notice carries what the subsection requires` | 6 | 7 |
| 24 | Under section 211(2), does the statement give what the subsection requires about the trustee for the debenture holders? | `s 211(2) the statement gives what the subsection requires` | 2 | 3 |
| 25 | Under section 211(3), must the company furnish me with a copy of the statement free of charge? | `s 211(3) the company must furnish the person with a copy of the statement free of charge` | 3 | 4 |
| 26 | Under section 211(4), did the director or trustee give notice within 7 days of the receipt of the request? | `s 211(4) the director or trustee gave notice within 7 days of the receipt of the request` | 2 | 5 |
| 27 | Under section 211(5), is the company guilty of the offence? | `s 211(5) the company is guilty of the offence` | 1 | 2 |
| 28 | Under section 211(6), am I deemed to be an officer of the company for subsection (5)? | `s 211(6) the person is deemed to be an officer of the company for subsection (5)` | 2 | 3 |
| 29 | Under section 211(7), does the section give me a defence? | `s 211(7) the section gives the person a defence` | 1 | 2 |
| 30 | Under section 211(5), am I guilty of the offence as an officer in default? | `s 211(5) the officer is guilty of the offence` | 5 | 6 |
| 31 | Under section 211(5) and (7), am I liable under subsection (5)? | `s 211(5) and (7) the person is liable under subsection (5)`; `s 211(5) the officer is guilty of the offence` | 6 | 4 |
| 32 | Under section 211(5), what is the most I may be sentenced to on conviction? | `s 211(5) the most the person may be sentenced to on conviction`; `s 211(5) the officer is guilty of the offence` | 5 | 3 |
| 33 | Under section 212(1), may the Court provide for the matter by its order? | `s 212(1) the Court may provide for the matter by its order` | 4 | 7 |
| 34 | Under section 212(2), does the property vest in the transferee company, and do the liabilities become its liabilities, by virtue of the order? | `s 212(2) the property vests in the transferee company and the liabilities become its liabilities by virtue of the order` | 1 | 2 |
| 35 | Under section 212(2), does the particular property vest free from the charge? | `s 212(2) the particular property vests free from the charge` | 2 | 3 |
| 36 | Under section 212(3), was a copy of the order lodged with the Registrar within 7 days of the making of the order? | `s 212(3) the lodgment was made within 7 days of the making of the order` | 3 | 4 |
| 37 | Under section 212(3), has the company lodged what the subsection requires within 7 days of the making of the order? | `s 212(3) the company has lodged what the subsection requires within 7 days of the making of the order` | 6 | 6 |
| 38 | Under section 212(3), is the company guilty of the offence? | `s 212(3) the company is guilty of the offence` | 1 | 2 |
| 39 | Under section 212(3), am I guilty of the offence as an officer in default? | `s 212(3) the officer is guilty of the offence` | 3 | 4 |
| 40 | Under section 212(3), what is the most I may be sentenced to on conviction? | `s 212(3) the most the person may be sentenced to on conviction`; `s 212(3) the officer is guilty of the offence` | 3 | 3 |
| 41 | Under section 212(4), is the vesting order unable yet to have effect in vesting the land because the entries have not been made? | `s 212(4) the vesting order cannot yet have effect in vesting the land` | 1 | 2 |
| 42 | Under section 212(5), is the thing within the word "liabilities"? | `s 212(5) "liabilities" the thing is within the word liabilities` | 1 | 2 |
| 43 | Under section 212(5), is the thing within the word "property"? | `s 212(5) "property" the thing is within the word property` | 1 | 2 |
| 44 | Under section 212(6), is the body a "company" for the purposes of section 212? | `s 212(6) "company" the body is a company` | 1 | 2 |
| 45 | Under section 215(1), has the scheme or contract been approved by the holders of at least 90% of the shares within 4 months of the offer? | `s 215(1) the scheme or contract has been approved by the holders of the requisite number of the shares` | 9 | 9 |
| 46 | Under section 215(1), may the transferee give me notice that it desires to acquire my shares? | `s 215(1) the transferee may give notice to the dissenting shareholder that it desires to acquire the shares` | 5 | 8 |
| 47 | Under section 215(1), what is the last day on which I may apply to the Court? | `s 215(1) the last day of the later of the one month and the 14 days` | 3 | 3 |
| 48 | Under section 215(1), is my application to the Court within the time the subsection allows? | `s 215(1) the dissenting shareholder's application to the Court is within the time subsection (1) allows` | 4 | 4 |
| 49 | Under section 215(1), may the Court order that the transferee is not entitled and bound to acquire my shares? | `s 215(1) the Court may order that the transferee is not entitled and bound to acquire the shares` | 3 | 4 |
| 50 | Under section 215(1), is the transferee entitled and bound to acquire my shares? | `s 215(1) the transferee is entitled and bound to acquire the dissenting shareholder's shares` | 3 | 5 |
| 51 | Under section 215(1), on what terms must the transferee acquire my shares? | `s 215(1) the terms on which the transferee must acquire the dissenting shareholder's shares` | 2 | 4 |
| 52 | Under section 215(1A), am I entitled to elect which of the terms I prefer? | `s 215(1A) the dissenting shareholder is entitled to elect which of the terms the shareholder prefers` | 5 | 5 |
| 53 | Under section 215(1B), has the transferee stated which of the terms is to apply if I fail to elect in time? | `s 215(1B) the transferee has stated which of the terms is to apply on a failure to elect` | 2 | 3 |
| 54 | Under section 215(1C)(a), are the shares to be disregarded in counting the 90%? | `s 215(1C)(a) the shares are to be disregarded` | 2 | 3 |
| 55 | Under section 215(1D), are the shares relevant treasury shares? | `s 215(1D) the shares are relevant treasury shares` | 3 | 5 |
| 56 | Under section 215(1C)(b), are the shares to be disregarded because they have ceased to be held as treasury shares? | `s 215(1C)(b) the shares are to be disregarded` | 2 | 3 |
| 57 | Under section 215(1E), does a later issue of shares on the exercise of an option affect the approval, the transferee's right to give notice or the notice's validity? | `s 215(1E) the subsequent issue of shares affects the matter` | 3 | 6 |
| 58 | Under section 215(2), am I entitled to require the transferor company to supply the statement of the other dissenting shareholders? | `s 215(2) the dissenting shareholder is entitled to require the transferor company to supply the statement` | 3 | 4 |
| 59 | Under section 215(2), is the transferee not yet entitled or bound to acquire my shares because the statement has not been posted to me 14 days ago? | `s 215(2) the transferee is not yet entitled or bound to acquire the shares` | 5 | 6 |
| 60 | Under section 215(3), do the shares transferred, together with the other shares the transferee holds, comprise or include 90%? | `s 215(3) the shares transferred, together with the other shares held by the transferee, comprise or include 90%` | 5 | 4 |
| 61 | Under section 215(3A), how many treasury shares are treated as acquired by the transferee? | `s 215(3A) the number of the treasury shares treated as having been acquired by the transferee` | 5 | 2 |
| 62 | Under section 215(3)(a), must the transferee give notice of the 90% to the holders of the remaining shares who have not assented? | `s 215(3)(a) the transferee must give notice of that fact to the holders of the remaining shares who have not assented` | 2 | 3 |
| 63 | Under section 215(3)(a), was the notice of the 90% given within one month from the date of the transfer? | `s 215(3)(a) the notice was given within one month from the date of the transfer` | 2 | 4 |
| 64 | Under section 215(3)(b), may I require the transferee to acquire my shares? | `s 215(3)(b) the holder may require the transferee to acquire the shares in question` | 5 | 5 |
| 65 | Under section 215(3), is the transferee entitled and bound to acquire my shares? | `s 215(3) the transferee is entitled and bound to acquire the shares` | 1 | 2 |
| 66 | Under section 215(3), on what terms must the transferee acquire my shares? | `s 215(3) the terms on which the transferee must acquire the shares` | 2 | 4 |
| 67 | Under section 215(4), must the transferee transmit a copy of the notice and pay, allot or transfer the consideration to the transferor company? | `s 215(4) the transferee must transmit a copy of the notice and pay, allot or transfer the consideration to the transferor company` | 2 | 3 |
| 68 | Under section 215(4), on what day must the transferee first act? | `s 215(4) the first day on which the transferee must act` | 6 | 5 |
| 69 | Under section 215(5), has the transferor company paid the sums it received into a separate bank account? | `s 215(5) the transferor company has paid the sums into a separate bank account` | 2 | 4 |
| 70 | Under section 215(6), was what is held in trust transferred to the Official Receiver within the time the subsection allows? | `s 215(6) the transfer to the Official Receiver is within the time the subsection allows` | 3 | 5 |
| 71 | Under section 215(7), how is what has been transferred to the Official Receiver dealt with? | `s 215(7) how the Official Receiver must deal with what is received under subsection (6)` | 2 | 3 |
| 72 | Under section 215(8), am I a dissenting shareholder? | `s 215(8) the shareholder is a dissenting shareholder` | 2 | 3 |
| 73 | Under section 215(8A), am I within the reference to a shareholder in subsection (8)? | `s 215(8A) the shareholder is within the reference to a shareholder in subsection (8)` | 1 | 2 |
| 74 | Under section 215(8AA), is the thing within the word "shares"? | `s 215(8AA) the thing is within the word shares` | 2 | 3 |
| 75 | Under section 215(8AB), am I within the word "shareholders"? | `s 215(8AB) the person is within the word shareholders` | 2 | 4 |
| 76 | Under section 215(8AC), are the records within the "register of members"? | `s 215(8AC) the records are within the register of members` | 1 | 2 |
| 77 | Under section 215(8B), does the definition of shares require the securities to be treated that way? | `s 215(8B) the definition of shares requires the securities to be treated that way` | 1 | 3 |
| 78 | Under section 215(9), are the shares to be treated as held or acquired by the transferee? | `s 215(9) the shares are to be treated as held or acquired by the transferee` | 2 | 6 |
| 79 | Under section 215(9A), are the shares also to be treated as held or acquired by the transferee? | `s 215(9A) the shares are also to be treated as held or acquired by the transferee` | 6 | 7 |
| 80 | Under section 215(10), are the shares shares already held by the transferee at the date of the offer? | `s 215(10) the shares are shares already held by the transferee within subsection (1)` | 5 | 6 |
| 81 | Under section 215(11), is the transferee to be treated as having acquired the shares by virtue of the approval of the offer? | `s 215(11) the transferee is to be treated as having acquired the shares by virtue of the approval of the offer` | 5 | 5 |
| 82 | Under section 215(12), is the body corporate controlled by the transferee or the person? | `s 215(12) the body corporate is controlled by the transferee or the person` | 4 | 5 |
| 83 | Under section 215AA(1), is section 215 to be read subject to section 215AA for this offer? | `s 215AA(1) section 215 is to be read subject to section 215AA` | 2 | 4 |
| 84 | Under section 215AA(2), are the conditions for the exercise of the rights conferred by section 215(1) satisfied? | `s 215AA(2) the conditions for the exercise of the rights conferred by section 215(1) are satisfied` | 3 | 6 |
| 85 | Under section 215AA(3), are the conditions for the exercise of the rights conferred by section 215(3) satisfied? | `s 215AA(3) the conditions for the exercise of the rights conferred by section 215(3) are satisfied` | 3 | 4 |
| 86 | Under section 215AA(4), how do the joint transferees hold what section 215 gives the transferee? | `s 215AA(4) how the joint transferees hold what section 215 gives the transferee` | 1 | 2 |
| 87 | Under section 215AA(5), is the notice or document complied with when given by or to any of the joint transferees? | `s 215AA(5) the notice or document is complied with` | 2 | 3 |
| 88 | Under section 215AA(6), is the notice made as the subsection requires? | `s 215AA(6) the notice is made as the subsection requires` | 2 | 3 |
| 89 | Under section 215AB(1), does the non-communication of the offer to some holders leave it an offer made under a scheme or contract? | `s 215AB(1) the non-communication of the offer does not prevent it from being an offer made under a scheme or contract` | 6 | 6 |
| 90 | Under section 215AB(2), does the impossibility or difficulty of accepting the offer leave it an offer made under a scheme or contract? | `s 215AB(2) the impossibility or difficulty of accepting the offer does not prevent it from being made under a scheme or contract` | 2 | 3 |
| 91 | Under section 215AB(3)(a), is it to be inferred that the offer cannot be an offer made under a scheme or contract unless the requirements of subsection (1) are met? | `s 215AB(3)(a) it is to be inferred that the offer cannot be an offer made under a scheme or contract unless the requirements of subsection (1)(a), (b) and (c) are met` | 1 | 2 |
| 92 | Under section 215AB(3)(b), is it to be inferred that the offer cannot be an offer made under a scheme or contract unless the reason is the one in subsection (2)? | `s 215AB(3)(b) it is to be inferred that the offer cannot be an offer made under a scheme or contract unless the reason is the reason mentioned in subsection (2)` | 1 | 2 |
| 93 | Under section 215A, may the companies amalgamate and continue as one company? | `s 215A the companies may amalgamate and continue as one company` | 3 | 5 |
| 94 | Under section 215A, is the amalgamated company one of the amalgamating companies or a new company? | `s 215A the amalgamated company is one of the amalgamating companies or a new company` | 1 | 2 |
| 95 | Under section 215B(1), does the amalgamation proposal contain what the subsection requires? | `s 215B(1) the amalgamation proposal contains what the subsection requires` | 14 | 8 |
| 96 | Under section 215B(2), may the amalgamation proposal specify the date on which the amalgamation is intended to become effective? | `s 215B(2) the amalgamation proposal may specify the date` | 2 | 3 |
| 97 | Under section 215B(3), does the amalgamation proposal provide as the subsection requires for shares held by one amalgamating company in another? | `s 215B(3) the amalgamation proposal provides as the subsection requires` | 3 | 5 |
| 98 | Under section 215B(4), is the cancellation of the shares deemed to be a reduction of share capital within the meaning of the Act? | `s 215B(4) the cancellation of the shares is deemed to be a reduction of share capital within the meaning of the Act` | 1 | 2 |
| 99 | Under section 215B(5), may the name be the name of the amalgamated company? | `s 215B(5) the name may be the name of the amalgamated company` | 2 | 4 |
| 100 | Under section 215C(1), has the amalgamation proposal been approved as the subsection requires? | `s 215C(1) the amalgamation proposal has been approved as the subsection requires` | 5 | 6 |
| 101 | Under section 215C(2)(a), did the board resolve before the general meeting that the amalgamation is in the best interest of the amalgamating company? | `s 215C(2)(a) the board resolved before the general meeting that the amalgamation is in the best interest of the amalgamating company` | 3 | 4 |
| 102 | Under section 215C(2)(b), did the board make the solvency statement for the amalgamating company before the general meeting? | `s 215C(2)(b) the board made the solvency statement in relation to the amalgamating company before the general meeting` | 3 | 3 |
| 103 | Under section 215C(2)(c), did the board make the solvency statement for the amalgamated company before the general meeting? | `s 215C(2)(c) the board made the solvency statement in relation to the amalgamated company before the general meeting` | 3 | 3 |
| 104 | Under section 215C(3), must I, as a director who votes in favour, sign the declaration? | `s 215C(3) the director must sign the declaration` | 1 | 2 |
| 105 | Under section 215C(3), does the declaration state what the subsection requires? | `s 215C(3) the declaration states what the subsection requires` | 2 | 3 |
| 106 | Under section 215C(4), did the board send what the subsection requires to every member at least 21 days before the general meeting? | `s 215C(4) the board sent what the subsection requires to every member at least 21 days before the general meeting` | 6 | 8 |
| 107 | Under section 215C(5)(a), did the directors send the amalgamation proposal to every secured creditor at least 21 days before the general meeting? | `s 215C(5)(a) the directors sent the amalgamation proposal to every secured creditor at least 21 days before the general meeting` | 3 | 3 |
| 108 | Under section 215C(5)(b), did the directors cause the notice to be published as the paragraph requires at least 21 days before the general meeting? | `s 215C(5)(b) the directors caused the notice to be published as the paragraph requires at least 21 days before the general meeting` | 5 | 5 |
| 109 | Under section 215C(6), am I guilty of an offence for contravening section 215C(3)? | `s 215C(6) the director is guilty of the offence` | 1 | 2 |
| 110 | Under section 215D(1)(a), are the terms of paragraph (a) in the resolution? | `s 215D(1)(a) the terms of paragraph (a) are in the resolution` | 4 | 2 |
| 111 | Under section 215D(1), may a holding company and its wholly-owned subsidiaries amalgamate without complying with sections 215B and 215C? | `s 215D(1) the amalgamating holding company and its wholly-owned subsidiaries may amalgamate without complying with sections 215B and 215C` | 9 | 8 |
| 112 | Under section 215D(2), may wholly-owned subsidiary companies of the same corporation amalgamate without complying with sections 215B and 215C? | `s 215D(2) the wholly-owned subsidiary companies of the same corporation may amalgamate without complying with sections 215B and 215C` | 6 | 7 |
| 113 | Under section 215D(3), did the directors give the written notice to every secured creditor at least 21 days before the general meeting? | `s 215D(3) the directors gave the written notice to every secured creditor at least 21 days before the general meeting` | 3 | 3 |
| 114 | Under section 215D(4), is the resolution deemed to be an amalgamation proposal that has been approved? | `s 215D(4) the resolution is deemed to be an amalgamation proposal that has been approved` | 1 | 2 |
| 115 | Under section 215D(5), did the board make the solvency statement for the amalgamated company before the commencement of the general meeting? | `s 215D(5) the board made the solvency statement in relation to the amalgamated company before the commencement of the general meeting` | 3 | 4 |
| 116 | Under section 215D(6), must I, as a director who votes in favour, sign the declaration? | `s 215D(6) the director must sign the declaration` | 1 | 2 |
| 117 | Under section 215D(6), does the declaration state what the subsection requires? | `s 215D(6) the declaration states what the subsection requires` | 2 | 3 |
| 118 | Under section 215D(7), am I guilty of an offence for contravening section 215D(6)? | `s 215D(7) the director is guilty of the offence` | 1 | 2 |
| 119 | Under section 215D(8), is the cancellation of the shares deemed to be a reduction of share capital within the meaning of the Act? | `s 215D(8) the cancellation of the shares is deemed to be a reduction of share capital within the meaning of the Act` | 1 | 2 |
| 120 | Under section 215E(1), are the documents filed with the Registrar those the subsection requires? | `s 215E(1) the documents filed with the Registrar are those the subsection requires` | 9 | 8 |
| 121 | Under section 215E(2)(a), is section 19(1)(a) and (c) deemed to have been complied with? | `s 215E(2)(a) section 19(1)(a) and (c) is deemed to have been complied with` | 2 | 3 |
| 122 | Under section 215E(2)(b), is the person within the reference in section 19(2)(b) to a person named in the constitution as a director or the secretary? | `s 215E(2)(b) the person is within the reference in section 19(2)(b) to a person named in the constitution as a director or the secretary` | 2 | 3 |
| 123 | Under section 215F(1), what must the Registrar issue on receiving the documents and fees? | `s 215F(1) what the Registrar must issue on receiving the documents and fees` | 2 | 4 |
| 124 | Under section 215F(2), must the notice be expressed to have effect on the date specified in the amalgamation proposal? | `s 215F(2) the notice must be expressed to have effect on the date specified in the amalgamation proposal` | 3 | 4 |
| 125 | Under section 215F(3), are the amalgamating companies other than the amalgamated company to be removed from the register on the day I ask about? | `s 215F(3) the Registrar must remove the amalgamating companies, other than the amalgamated company, from the register` | 2 | 3 |
| 126 | Under section 215F(4), must the Registrar issue a certificate of confirmation of amalgamation to the amalgamated company? | `s 215F(4) the Registrar must issue a certificate of confirmation of amalgamation to the amalgamated company` | 2 | 3 |
| 127 | Under section 215G, is the effect one the section lists? | `s 215G the effect is one the section lists` | 1 | 2 |
| 128 | Under section 215G, has the effect taken place on the day I ask about? | `s 215G on the date shown in the notice of amalgamation the effect has taken place` | 3 | 6 |
| 129 | Under section 215H(1), am I a person the subsection names (a member or creditor of an amalgamating company, or a person to whom it is under an obligation)? | `s 215H(1) the person is one the subsection names` | 1 | 3 |
| 130 | Under section 215H(1), may the Court make an order in relation to the amalgamation proposal? | `s 215H(1) the Court may make an order in relation to the amalgamation proposal` | 5 | 8 |
| 131 | Under section 215H(1), is the order within the Court's power? | `s 215H(1) the order is within the Court's power` | 2 | 6 |
| 132 | Under section 215H(2), may the order be made on the terms or conditions? | `s 215H(2) the order may be made on the terms or conditions` | 1 | 2 |
| 133 | Under section 215I(1), does the statement have the content the subsection requires? | `s 215I(1) the statement has the content the subsection requires` | 5 | 4 |
| 134 | Under section 215I(2), is the statement in the form the subsection requires? | `s 215I(2) the statement is in the form the subsection requires` | 6 | 5 |
| 135 | Under section 215I(1), is the statement a solvency statement in relation to the amalgamating company for the purposes of section 215C(2)(b)? | `s 215I(1) the statement is a solvency statement in relation to the amalgamating company for the purposes of section 215C(2)(b)` | 6 | 4 |
| 136 | Under section 215I(3), have the directors formed the opinion as the subsection requires? | `s 215I(3) the directors have formed the opinion as the subsection requires` | 1 | 2 |
| 137 | Under section 215I(4)(a), has the board had regard to what the paragraph requires? | `s 215I(4)(a) the board has had regard to what the paragraph requires` | 2 | 3 |
| 138 | Under section 215I(4)(b), may the board rely on the valuation or estimate? | `s 215I(4)(b) the board may rely on the valuation or estimate` | 1 | 2 |
| 139 | Under section 215I(5), may the board take the matter into account in valuing a contingent liability? | `s 215I(5) the board may take the matter into account in valuing a contingent liability` | 2 | 3 |
| 140 | Under section 215I(6), am I guilty of the offence the subsection creates? | `s 215I(6) the director is guilty of the offence this subsection creates` | 3 | 4 |
| 141 | Under section 215I(6), what is the most I may be sentenced to on conviction? | `s 215I(6) the most the person may be sentenced to on conviction`; `s 215I(6) the director is guilty of the offence this subsection creates` | 3 | 4 |
| 142 | Under section 215J(1), is the statement a solvency statement in relation to the amalgamated company for the purposes of sections 215C(2)(c) and 215D(5)? | `s 215J(1) the statement is a solvency statement in relation to the amalgamated company for the purposes of sections 215C(2)(c) and 215D(5)` | 4 | 5 |
| 143 | Under section 215J(2), have the directors formed the opinion as the subsection requires? | `s 215J(2) the directors have formed the opinion as the subsection requires` | 1 | 2 |
| 144 | Under section 215J(3)(a), has the board had regard to what the paragraph requires? | `s 215J(3)(a) the board has had regard to what the paragraph requires` | 2 | 3 |
| 145 | Under section 215J(3)(b), may the board rely on the valuation or estimate? | `s 215J(3)(b) the board may rely on the valuation or estimate` | 1 | 2 |
| 146 | Under section 215J(4), may the board take the matter into account in valuing a contingent liability? | `s 215J(4) the board may take the matter into account in valuing a contingent liability` | 2 | 3 |
| 147 | Under section 215J(5), am I guilty of the offence the subsection creates? | `s 215J(5) the director is guilty of the offence this subsection creates` | 3 | 4 |
| 148 | Under section 215J(5), what is the most I may be sentenced to on conviction? | `s 215J(5) the most the person may be sentenced to on conviction`; `s 215J(5) the director is guilty of the offence this subsection creates` | 3 | 3 |
| 149 | Under section 215K(1), was what is held in trust transferred to the Official Receiver within the time the subsection allows? | `s 215K(1) the transfer to the Official Receiver is within the time the subsection allows` | 3 | 7 |
| 150 | Under section 215K(2), how is what has been transferred to the Official Receiver dealt with? | `s 215K(2) how the Official Receiver must deal with what is received under subsection (1)` | 2 | 3 |

## What check.sh prints

Run in the folder as `L4=<1.6.110 build> L4_MAIN=<1.6.109 build> ./check.sh`; the output is pasted unedited (`work/final-check.txt`).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sg-auditors.l4                                 0         0       0        0         0 |      0         0       0        0  same
sg-core.l4                                     0         0       0        0         0 |      0         0       0        0  same
sg-definitions.l4                              0         0       0        0         0 |      0         0       0        0  same
sg-groups.l4                                   0         0       0        0         0 |      0         0       0        0  same
sg-interests.l4                                0         0       0        0         0 |      0         0       0        0  same
sg-interpretation.l4                           0         0       0        0         0 |      0         0       0        0  same
sg-periods.l4                                  0         0       0        0         0 |      0         0       0        0  same
sg-solvency.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgd-acquisition.l4                             0         0       0        0         0 |      0         0       0        0  same
sgd-amalgamation-solvency.l4                   0         0       0        0         0 |      0         0       0        0  same
sgd-amalgamation.l4                            0         0       0        0         0 |      0         0       0        0  same
sgd-cases-seat.l4                              0       597       0        0         0 |      0       597       0        0  same
sgd-compromise.l4                              0         0       0        0         0 |      0         0       0        0  same
sgd-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgd-tests-acquisition.l4                       0       220       0        0         0 |      0       220       0        0  same
sgd-tests-amalgamation-solvency.l4             0        54       0        0         0 |      0        54       0        0  same
sgd-tests-amalgamation.l4                      0       199       0        0         0 |      0       199       0        0  same
sgd-tests-compromise.l4                        0       191       0        0         0 |      0       191       0        0  same
TOTAL (18 modules)                             0      1261       0        0           |      0      1261       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline it replaced: the same command on the folder as handed over (the eight keel modules and `check.sh`, no `sgd-` file), `work/baseline-check.txt`:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sg-auditors.l4                                 0         0       0        0         0 |      0         0       0        0  same
sg-core.l4                                     0         0       0        0         0 |      0         0       0        0  same
sg-definitions.l4                              0         0       0        0         0 |      0         0       0        0  same
sg-groups.l4                                   0         0       0        0         0 |      0         0       0        0  same
sg-interests.l4                                0         0       0        0         0 |      0         0       0        0  same
sg-interpretation.l4                           0         0       0        0         0 |      0         0       0        0  same
sg-periods.l4                                  0         0       0        0         0 |      0         0       0        0  same
sg-solvency.l4                                 0         0       0        0         0 |      0         0       0        0  same
TOTAL (8 modules)                              0         0       0        0           |      0         0       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The other gates, run on the final files (`work/final-gates.txt`):

```
srcrefs.py check --refs, sgd-*.l4:
srcrefs check: 1426 src: lines, 169 runs, 188 locators, 0 problems
srcrefs.py check --strict, sgd-*.l4:
srcrefs check: 1426 src: lines, 169 runs, 188 locators, 0 problems
kindcheck.py (quoted words of every FALSE-kind and NOTHING-kind comment against the text), layer 1:
kindcheck: 220 tagged comments, 258 fragments checked, 67 short quotations left to the eye, 0 problems
trace_compare.py (each #TRACE against its -- EXPECT), per tests file and build:
  sgd-tests-compromise.l4 on 1.6.110: traces: 26, matched: 26, problems: 0
  sgd-tests-compromise.l4 on 1.6.109: traces: 26, matched: 26, problems: 0
  sgd-tests-acquisition.l4 on 1.6.110: traces: 25, matched: 25, problems: 0
  sgd-tests-acquisition.l4 on 1.6.109: traces: 25, matched: 25, problems: 0
  sgd-tests-amalgamation.l4 on 1.6.110: traces: 36, matched: 36, problems: 0
  sgd-tests-amalgamation.l4 on 1.6.109: traces: 36, matched: 36, problems: 0
  sgd-tests-amalgamation-solvency.l4 on 1.6.110: traces: 8, matched: 8, problems: 0
  sgd-tests-amalgamation-solvency.l4 on 1.6.109: traces: 8, matched: 8, problems: 0
```

## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

No site of this part changed under it (2026S1bC): the functions of this part that stay Boolean after the protocol split already answered as the ruling reads, and its protocol-shaped functions keep limit 3 of the grant ruling until they are re-encoded.
