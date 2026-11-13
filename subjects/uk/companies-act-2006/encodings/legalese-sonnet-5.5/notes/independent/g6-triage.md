# triage.md: failed or refused assertions and gaps, review dst-rev-coa6 (coa28 18349-19081, coa29 19082-20016, coa30 20017-20928)

Format: scenario (number in ANSWERS.md; SEAT/EXTRA ids are the seat assertions and one extra probe written in tests-independent.l4) | file line of my assertion in `enc/tests-independent.l4` | provision (text line in `inputs/ukpga-2006-46.txt`) | my expected answer | what the encoding answered | verdict | reason.
Run: `l4-main-110 run tests-independent.l4` from `enc/`, `JL4_LIBRARY_PATH` unset: 689 assertions, 663 satisfied, 26 failed, 0 refused. Verdict words: ENCODER (encoding wrong), SCENARIO (my mistake), AMBIGUOUS (text reads both ways), GAP (no function for the scenario).

## Failed assertions (26)
26 | line 94 | s 1279(1), text 18427-18429 | expected JUST FALSE | encoding NOTHING | SCENARIO | "The shares to which section 1277 applies are shares (a) ... and (b) ...": "are", not "means", and no "only", so the family convention gives NOTHING for traded shares in which the institution has no interest; my FALSE read "are ... and" as a closed definition (the case would be AMBIGUOUS only if "are" is read as "means")
46 | line 113 | s 1282 new s176ZA(4), text 18489 | expected JUST FALSE | encoding NOTHING | SCENARIO | "all expenses properly incurred ..., including the remuneration of the liquidator": "including" leaves the class open under the convention; my FALSE relied on "properly incurred" and ignored "including"
49 | line 116 | s 1283, text 18504 | expected NOTHING | encoding JUST FALSE | ENCODER | "Where a commonhold association alters ... at a time when the land ... is commonhold land, the alteration ...": "where" is not a no-word of the convention and the rule is limited by its own wording, so a non-commonhold case is NOTHING; the encoding gives JUST FALSE here but NOTHING for the same kind of "where" in Sch 1A para 23 (EXTRA-1)
70 | line 145 | s 1291(2), text 18543 | expected JUST FALSE | encoding NOTHING | SCENARIO | the exclusion is for time "during which ... both Houses are adjourned for more than four days"; four days is outside that limit, so the family convention gives NOTHING; my FALSE was wrong
123 | line 193 | Sch 1 para 6(3), text 18654-18656 | expected NOTHING | encoding JUST FALSE | SCENARIO | "A person is treated as not interested in shares if and so long as he holds them" as bare, custodian or simple trustee: "if and so long as" is a no-word, so a trustee with active duties is JUST FALSE; I overlooked it
135 | line 211 | Sch 1A para 1, text 18669 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | para 1 speaks only of "an individual (X)": for a body corporate the text is silent (NOTHING, mine) or "must be met by an individual in order for the individual to be a person with significant control" is read as the whole test (JUST FALSE, encoding)
207 | line 285 | Sch 1B para 11, text 18901-18904 | expected NOTHING | encoding JUST FALSE | SCENARIO | "must by notice withdraw the restrictions notice if (a), (b) or (c)": "if" is a no-word of the convention, so none of (a)-(c) is JUST FALSE; I wrote NOTHING by mistake
227 | line 311 | Sch 1C para 7(3), text 18972 | expected NOTHING | encoding JUST FALSE | ENCODER | "where control has been acquired following a voluntary takeover bid to all the holders for all their holdings, the obligation ... no longer applies": a "where" limit; for a bid for some holdings only the text is outside it (NOTHING); the encoding gives JUST FALSE
238 | line 321 | Sch 1C para 9(2), text 18981-18983 | expected NOTHING | encoding JUST FALSE | ENCODER | cash "must be offered (a) ... where the consideration is not liquid listed securities, (b) at least ... where cash purchases carry 5% or more": a duty limited by "where"; with liquid securities and 4% the text does not say cash need not be offered (and para 9(4) lets the rules require cash in all cases); the encoding gives JUST FALSE
259 | line 342 | Sch 1C para 17(3), text 19042-19044 | expected NOTHING | encoding JUST FALSE | ENCODER | the general meeting must approve "any decision (a) not in the normal course of business and (b) ... may result in frustration": for a decision in the normal course the text is silent; the encoding gives JUST FALSE
262 | line 345 | Sch 1C para 18(3), text 19052 | expected NOTHING | encoding JUST FALSE | ENCODER | the opinion must be appended "where the board receives in good time a separate opinion": a "where" limit; for an opinion not received in good time the text is silent; the encoding gives JUST FALSE
274 | line 357 | Sch 1C para 21(1)-(3), text 19076-19081 | expected JUST TRUE | encoding NOTHING | SCENARIO | the text only removes the UK-regulated-market limit for the listed provisions (s1 does not apply); it does not say a foreign company with no such securities is a "company" there; the encoding's NOTHING is the safer reading, mine overreached
277 | line 421 | Sch 2 Pt 1(A), text 19086-19097 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | a person not on the table of "specified persons" (Lord Chancellor): the table is not closed with "only" (mine, NOTHING) versus the table being the whole specification for s948(3)(b), amendable only by order under s948(4) (encoding, JUST FALSE)
283 | line 427 | Sch 2 Pt 2(A) para 13, text 19136-19143 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | my scenario was about para 13's own list (SoS functions under the Pensions Act 1995 are not in it; para 20 gives the Pensions Regulator that Act); the API can only say "none of the descriptions"; same closed-table question as 277
287 | line 431 | Sch 2 Pt 2(A) para 25(m), text 19173-19176 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | CMA functions under Chapter 2 of Part 4 of the 2024 Act are not in para 25(m) (Part 3, Ch 1 of Part 4, Ch 2 of Part 5); same closed-table question as 277
292 | line 436 | Sch 2 Pt 2(A) para 52(1), text 19216 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | disciplinary proceedings about an architect: not among "lawyer, auditor, accountant, valuer or actuary"; same closed-table question as 277
306 | line 450 | Sch 2 Pt 2(E) para 4, text 19321 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | a summary that does enable a person to be identified: outside the words of para 4 (NOTHING, mine) versus not a specified description (JUST FALSE, encoding)
347 | line 485 | Sch 5 para 4(2), text 19451 | expected NOTHING | encoding JUST FALSE | ENCODER | "Where the company is unable to obtain an address falling within sub-paragraph (1), the document ... may be sent to the last address known": a "where" permission limited by its own wording; if the company can obtain an address the text is silent; the encoding gives JUST FALSE
403 | line 547 | Sch 8 "company" in Schedule 1C, text 19687 | expected "in Schedule 1C (see Chapter 1 of Part 28): paragraph 21 of Schedule 1C" among the provisions listed for "company" | encoding not listed (the lookup of "company" returns only the first three rows) | ENCODER | the row at text 19685 is dots; the five dash rows after it (19686-19690: Part 26, Schedule 1C, Part 26A, Chapter 3 of Part 28, the company communications provisions) are encoded as stand-alone expressions headed "— in ..." instead of scopes of "company", so the lookup misses them
460 | line 651 | Sch 10 para 3(6), text 20066-20069 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | "The persons within this sub-paragraph are (a) the recognised body, (b) any member, (c) any other person who appears to the Secretary of State to be affected": a list not closed with "only" gives NOTHING for a stranger not appearing affected (mine), but limb (c) is a catch-all test that can be read as making the list exhaustive (encoding, JUST FALSE). Evidence about consistency: the encoding itself gives NOTHING for the same shape of list in s1275(3A) and s1278(1)
547 | line 740 | Sch 11 para 3(1), text 20432-20434 | expected NOTHING | encoding JUST FALSE | SCENARIO | "A recognition order may be revoked ... if at any time it appears to him (a) ... or (b) ...": "if" is a no-word of the convention, so a ground outside (a)/(b) is JUST FALSE; I wrote NOTHING by mistake (same slip as 207)
571 | line 766 | Sch 2 Pt 1(A), text 19086-19097 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | the PRA is not on the Schedule 2 Part 1(A) table (it is on Schedule 11A, para 5A); the API can only say "none of the persons listed"; same closed-table question as 277
596 | line 793 | Sch 12 para 3(2)-(3), text 20677-20680 | expected NOTHING | encoding JUST FALSE | SCENARIO | my assertion asked the negative function "are not to be regarded as appropriate" for arrangements that meet the minimum; "not to be regarded as appropriate ... unless" gives JUST FALSE there, which the encoding says; the NOTHING I wanted belongs to the question "are they appropriate", which has no function
601 | line 800 | Sch 13 para 1(1), text 20692-20695 | expected NOTHING | encoding JUST FALSE | AMBIGUOUS | "has effect ... as follows: (a) paras 2 to 12 for an established body; (b) paras 2 and 6 to 11 for an existing body": para 4 for an existing body is not named; read as a closed allocation by body type (encoding, JUST FALSE) or as silence because the list does not end with "only" (mine, NOTHING)
SEAT29-37 | line 631 | Sch 8 "company" seat lookup, text 19682-19690 | expected eight rows under "company" (generally, Chapter 7 of Part 17, Chapter A1 of Part 25, Part 26, Schedule 1C, Part 26A, Chapter 3 of Part 28, the company communications provisions) | encoding only the first three | ENCODER | same defect as 403: the dots row at 19685 splits the "company" group
SEAT30-30 | line 856 | Sch 12 para 4 seat question "must I pay the costs ...", text 20682 | expected JUST TRUE (the duty applies whether or not I have paid) | encoding JUST FALSE (when I have not paid) | ENCODER | the seat question asks about the duty but answers whether it has been performed: with the arrangements within para 1 or 2, the auditor obliged to take part, and the arrangements providing that it pays, an unpaid auditor is told "no"

## Gaps (94 scenarios with no function to ask them; 216 and 599 are half-gaps whose other half is asserted and satisfied)
1 | - | s1274(2) new s16(2)(l), 18354 | expected TRUE | encoding: no function | GAP | the matters list inserted by the amendment has no function
2 | - | s1274(2) new s16(2)(q), 18359 | expected TRUE | encoding: no function | GAP | same
12 | - | s1275(4), 18379-18380 | expected TRUE | encoding: no function | GAP | regulation-making permission: no function
15 | - | s1276(5), 18396 | expected TRUE | encoding: no function | GAP | amendment of s66(2) of the 2004 Act: no function
16 | - | s1277(1), 18399 | expected TRUE | encoding: no function | GAP | the Treasury's power to make regulations: no function
17 | - | s1277(1), 18399 | expected TRUE | encoding: no function | GAP | the Secretary of State's power: no function
23 | - | s1278(2)(b), 18424 | expected TRUE | encoding: no function | GAP | power to disapply by regulations: no function
31 | - | s1280(1)(b), 18443 | expected TRUE | encoding: no function | GAP | permission to require information about instructions: no function
32 | - | s1280(4)(b), 18449 | expected TRUE | encoding: no function | GAP | permission to require publication to the public: no function
47 | - | new Art 150ZA(3)(b), 18498-18500 | expected TRUE | encoding: no function | GAP | power to restrict by rules: no function
72 | - | s1291(2), 18543 | expected TRUE | encoding: no function | GAP | one House adjourned: the encoding's kinds of interval are dissolved/prorogued and both Houses adjourned only
75 | - | s1292(1)(c), 18551 | expected TRUE | encoding: no function | GAP | permission to make transitional provision: no function
83 | - | s1294(1)-(2)(a), 18567-18569 | expected TRUE | encoding: no function | GAP | power to amend an earlier enactment by order: no function
84 | - | s1294(2)(c), 18571 | expected TRUE | encoding: no function | GAP | same
85 | - | s1294(2), 18568-18571 | expected NOTHING | encoding: no function | GAP | same
88 | - | s1295, 18580 | expected TRUE | encoding: no function | GAP | the repeal by Schedule 16: no function in these modules
93 | - | s1298, 18597 | expected TRUE | encoding: no function | GAP | short title: not encoded
95 | - | s1300(1)(b), 18603-18605 | expected TRUE | encoding: no function | GAP | commencement: not encoded
96 | - | s1300(1)(b), 18603-18605 | expected TRUE | encoding: no function | GAP | commencement: not encoded
97 | - | s1300(1)(b), 18603; (2), 18608 | expected FALSE | encoding: no function | GAP | commencement: not encoded
98 | - | s1300(1)(c), 18606 | expected TRUE | encoding: no function | GAP | commencement: not encoded
99 | - | s1300(1)(c), 18606 | expected FALSE | encoding: no function | GAP | commencement: not encoded
100 | - | s1300(1)(d), 18607 | expected TRUE | encoding: no function | GAP | commencement: not encoded
101 | - | s1300(2), 18608 | expected TRUE | encoding: no function | GAP | commencement: not encoded
102 | - | s1300(1)(a), 18602 | expected FALSE | encoding: no function | GAP | commencement: not encoded
171 | - | para 26(2)(a), 18806 | expected TRUE | encoding: no function | GAP | the power to replace a percentage by regulations: no function
173 | - | para 26(2), 18805-18808 | expected NOTHING | encoding: no function | GAP | list of permitted purposes: no function
216 | - | para 14A(3), 18933-18936 | expected FALSE (summary only; no imprisonment: maximum imprisonment none) | encoding: no function | GAP | no function answers whether the offence is triable on indictment; the no-imprisonment half is asserted
231 | - | para 8(1), 18973 | expected FALSE | encoding: no function | GAP | no function asks whether a rules period of 5 months is permitted
232 | - | para 8(1), 18973 | expected FALSE | encoding: no function | GAP | same for 13 months
240 | - | para 9(4), 18987 | expected TRUE | encoding: no function | GAP | permission for the rules to require cash in all cases: no function
245 | - | para 12(4), 19000 | expected NOTHING | encoding: no function | GAP | the function takes only the listed items; an item outside the list (credit rating) cannot be asked
251 | - | para 13(2), 19023 | expected TRUE | encoding: no function | GAP | permission to extend the maximum acceptance period: no function
252 | - | para 14(2), 19025 | expected TRUE | encoding: no function | GAP | permission for a Panel derogation: no function
311 | - | Sch 3 para 1(2), new s444(4)(a), 19339 | expected value 24 months (2 years) | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
312 | - | para 1(2), s444(4)(b)(i), 19341 | expected value 12 months | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
313 | - | para 1(2), s444(4)(b)(ii), 19342 | expected value 6 months | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
314 | - | para 1(2), s444(4)(b)(i), 19341 | expected value 1/50 | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
315 | - | para 2(2), new s448(7A), 19346-19348 | expected FALSE (fine only; maximum imprisonment none) | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
316 | - | para 3(3), new s449(6A)(a), 19354 | expected value 24 months | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
317 | - | para 3(3), s449(6A)(b)(ii), 19357 | expected value 6 months | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
318 | - | para 4(1), new s450(3)(a), 19362 | expected value 84 months (seven years) | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
319 | - | para 4(1), s450(3)(b)(i), 19364 | expected value 12 months | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
320 | - | para 5(1), new s451(2)(a), 19370 | expected value 24 months | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
321 | - | para 6(3), new s453A(5A), 19379-19381 | expected FALSE (fine only) | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
322 | - | para 7(2), 19385-19388 | expected TRUE | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
323 | - | para 7(2), 19388 | expected FALSE | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
324 | - | para 7(3), new s455(2A)(b), 19392 | expected FALSE | encoding: no function | GAP | Schedule 3 (amendments of CA 1985 offences) is not encoded by any module
441 | - | Sch 9 Pt 1 para 3, 20002 | expected NOTHING (the paragraph is shown as omitted: ". . . . .") | encoding: no function | GAP | Schedule 9 is shown as omitted; no module
442 | - | Sch 9, 19997-19998 | expected TRUE (title only; no operative text remains) | encoding: no function | GAP | Schedule 9 is shown as omitted; no module
501 | - | para 10B, 20210 | expected NOTHING (the paragraph is omitted: ". . . . .") | encoding: no function | GAP | the paragraph is shown as omitted; no function
504 | - | para 12(3)(b)(v), 20237 | expected value 3 years | encoding: no function | GAP | no function returns the "up to three years" length
505 | - | para 12(3)(b), 20232-20241 | expected NOTHING | encoding: no function | GAP | the function takes the nine listed sanctions only; an unlisted sanction (imprisonment) cannot be asked
539 | - | Pt 3 paras 21-27, 20381-20399 | expected NOTHING (paragraph omitted) | encoding: no function | GAP | shown as omitted; no function
560 | - | para 8(4), 20493 | expected TRUE | encoding: no function | GAP | procedure for regulations under para 8: no function
584 | - | Pt 2 para 39, 20582-20592 | expected NOTHING | encoding: no function | GAP | the description enumeration has no "none of the descriptions" constructor, so a description outside para 39 cannot be asked
599 | - | para 6(1)-(2), 20687-20688 | expected TRUE | encoding: no function | GAP | the negative-procedure order: no function (para 6(1) is asserted)
603 | - | para 3(2), 20704 | expected TRUE | encoding: no function | GAP | minimum of eight members: no function
604 | - | para 3(2), 20704 | expected FALSE | encoding: no function | GAP | minimum of eight members: no function
618 | - | para 11(3)(c), 20766 | expected TRUE | encoding: no function | GAP | the provision that may be made on transfer: no function
619 | - | para 12(a), 20773-20774 | expected TRUE | encoding: no function | GAP | the power to provide compensation on revocation: no function
621 | - | Sch 14 para 1(2)(b), 20786 | expected TRUE | encoding: no function | GAP | not encoded
622 | - | para 1(3)(b), 20789 | expected TRUE | encoding: no function | GAP | not encoded
623 | - | Sch 15 para 3, new s73A(6) FSMA, 20796 | expected FALSE | encoding: no function | GAP | not encoded
624 | - | para 3, 20796 | expected TRUE | encoding: no function | GAP | not encoded
625 | - | para 6(2), new s91(1ZA)(c), 20808-20809 | expected TRUE | encoding: no function | GAP | not encoded
626 | - | para 6(3), new s91(1B)(a)(ii), 20814-20816 | expected TRUE | encoding: no function | GAP | not encoded
627 | - | para 6(3), new s91(1B)(b), 20815 | expected TRUE | encoding: no function | GAP | not encoded
628 | - | para 10(4), new s102A(6)(aa), 20834 | expected FALSE | encoding: no function | GAP | not encoded
629 | - | para 10(4), 20834 | expected TRUE | encoding: no function | GAP | not encoded
630 | - | para 10(4), 20834 | expected TRUE | encoding: no function | GAP | not encoded
631 | - | para 11(3), 20838 | expected TRUE | encoding: no function | GAP | not encoded
632 | - | Sch 16, Companies Act 1985, 20870 | expected TRUE | encoding: no function | GAP | not encoded
633 | - | Sch 16, CA 1985, 20870 | expected TRUE | encoding: no function | GAP | not encoded
634 | - | Sch 16, CA 1985, 20870 | expected NOTHING | encoding: no function | GAP | not encoded
635 | - | Sch 16, CA 1985, 20870 | expected TRUE | encoding: no function | GAP | not encoded
636 | - | Sch 16, CA 1985, 20870 | expected TRUE | encoding: no function | GAP | not encoded
637 | - | Sch 16, CA 1985, 20870 | expected NOTHING | encoding: no function | GAP | not encoded
638 | - | Sch 16, CA 1985, 20870 | expected TRUE | encoding: no function | GAP | not encoded
639 | - | Sch 16, CA 1985, 20870 | expected TRUE | encoding: no function | GAP | not encoded
640 | - | Sch 16, CA 1985, 20870 | expected NOTHING | encoding: no function | GAP | not encoded
641 | - | Sch 16, CA 1985, 20870 | expected TRUE | encoding: no function | GAP | not encoded
642 | - | Sch 16, CA 1985, 20870 | expected NOTHING | encoding: no function | GAP | not encoded
643 | - | Sch 16, Companies Act 1989, 20876, 20925 | expected TRUE | encoding: no function | GAP | not encoded
644 | - | Sch 16, Companies Act 1989, 20876, 20925 | expected NOTHING | encoding: no function | GAP | not encoded
645 | - | Sch 16, CA 1989, 20876 | expected NOTHING | encoding: no function | GAP | not encoded
646 | - | Sch 16, NI, 20899 | expected TRUE | encoding: no function | GAP | not encoded
647 | - | Sch 16, NI, 20901 | expected TRUE | encoding: no function | GAP | not encoded
648 | - | Sch 16, NI, 20920 | expected TRUE | encoding: no function | GAP | not encoded
649 | - | Sch 16, NI, 20908 | expected NOTHING | encoding: no function | GAP | not encoded
650 | - | Sch 16, NI, 20906 | expected TRUE | encoding: no function | GAP | not encoded
651 | - | Sch 16, 20899-20920 | expected NOTHING | encoding: no function | GAP | not encoded
652 | - | Sch 16, other repeals, 20924 | expected TRUE | encoding: no function | GAP | not encoded
653 | - | Sch 16, other repeals, 20927 | expected TRUE | encoding: no function | GAP | not encoded

## Counts by verdict word
ENCODER 9, SCENARIO 8, AMBIGUOUS 9, GAP 94 (total 120 lines)

## Notes that are not findings (read with the table)
1. "where" is treated inconsistently by the encoding. It gives NOTHING for the "where" limit in Sch 1A para 23 (EXTRA-1 passes) and for the "applies to a document ... to a person as" openings of Sch 5 paras 10 and 11 and the "In determining ..." opening of Sch 2 Pt 3 para 2 (read in the module comments, not re-asserted), and JUST FALSE for a "where" limit in s1283, Sch 1C paras 7(3), 9(2), 17(3), 18(3) and Sch 5 para 4(2). By the stated convention ("where" is not one of the no-words) all of these are NOTHING.
2. Scenarios 382 (Sch 6 para 7) and 395 (Sch 7 para 8) PASS, but I now think my expected JUST FALSE for "limb (a) met, limb (b) not met" was wrong: the paragraphs say "shall be treated as held by the person providing the security (a) where ... and (b) where ...", a "where" grant limited by its own wording, so the convention gives NOTHING. The encoding answers JUST FALSE for them and NOTHING for the identical words in Sch 1A para 23 (EXTRA-1). I did not change the expected values.
3. Several scenarios (for example 41, 43, 224, 388, 389) are asserted through a function that asks the converse question ("is barred", "cannot be regarded", "assets available after excluding the s176A(2)(a) amount"); the comment on each says how the scenario was mapped.
4. The seat assertions (SEAT28-1 to SEAT28-50, SEAT29-1 to SEAT29-37, SEAT30-1 to SEAT30-40) have expected values written from the text before their run, and are not in ANSWERS.md, which was frozen when the modules were opened. Two of them failed (SEAT29-37, SEAT30-30).
5. Date arithmetic checked beyond the assertions (probes not kept): "one month beginning with" 31 Jan 2025 ends 28 Feb 2025; 31 Mar ends 30 Apr; 30 Jan 2024 ends 29 Feb 2024; "three months beginning with" 31 Jan 2025 ends 30 Apr 2025 (first day after: 1 May); all as the text reads.
