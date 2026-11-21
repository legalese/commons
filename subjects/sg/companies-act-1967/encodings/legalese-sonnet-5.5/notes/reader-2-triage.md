# Triage: independent tests for ss145-173I, ss199-204 and the Twelfth Schedule (reader group 2)

Run: `l4-main-110 run tests-independent.l4` from `enc/`, JL4_LIBRARY_PATH unset.
Result: 640 assertions, 608 satisfied, 32 failed, 0 refused; 14 GAP scenarios. "L" is the line of my assertion in `enc/tests-independent.l4`; "l." is the line in `inputs/CoA1967.txt`. "Silent-Sn" is the silent-case list in ANSWERS.md, kept apart from main scenario Sn.
Format: scenario | assertion line | provision (text line) | my expected | encoding answered | verdict.

## Failed assertions (32)

1. S6 | L47 | s145(2) (l.11601) | JUST FALSE (a person of 18 with capacity is not barred) | NOTHING | SCENARIO: "No person other than X may be a director" limits the bar to persons outside X, so for a person inside X the Guide gives NOTHING; my value was wrong.
2. S10 | L51 | s145(5) (l.11634) | JUST FALSE (a resident director remains, so no breach) | NOTHING | SCENARIO: "any purported resignation ... in breach of this subsection is invalid" limits itself to breach; outside the limit the Guide gives NOTHING.
3. S26 | L67 | s145(10)(a) (l.11711) | NOTHING (the person is not a member) | JUST FALSE | AMBIGUOUS: unmet element of a contravention: NOTHING (limited in its own wording) against JUST FALSE (an element the text requires is missing).
4. S82b | L131 | s149A(3) (l.12215) | JUST FALSE (proves (a) only; "and") | NOTHING | ENCODER: the subsection is a defence ("if such person proves ... that (a) ... and (b)") and ruling (b) of 2026-11-05 gives JUST FALSE when X is not proved; the encoder's reading (a prohibition limited in its own wording gives NOTHING) is the other side, so this is the weakest ENCODER call.
5. S118b | L181 | s155(8) (l.12589) | JUST TRUE (offence committed on 15 May 1984, so account is taken) | NOTHING | SCENARIO: "No account is to be taken ... of any offence committed before 15 May 1984" is a flat negative limited in its own wording; outside the limit the Guide gives NOTHING.
6. S126b | L192 | s155A(3A) (l.12676) | JUST FALSE (no Registrar application pending) | NOTHING | AMBIGUOUS: "cannot be made if ..." with the "if" unmet: JUST FALSE (a condition introduced with "if") against NOTHING (a bar limited in its own wording).
7. S128b | L196 | s155B(1) (l.12703) | NOTHING (a former director, not "at the time the order is made" a director) | JUST FALSE | AMBIGUOUS: a "may" gated by "Where ... / who, at the time ..., is": grant ruling NOTHING against periods ruling (b) JUST FALSE.
8. S158b | L251 | s157B (l.13229) | NOTHING (a company with two directors) | JUST FALSE | AMBIGUOUS: a "may" gated by "Where a company only has one director": grant ruling NOTHING against periods ruling (b) JUST FALSE.
9. S165b | L261 | s160(2) (l.13328) | NOTHING (application by a creditor) | JUST FALSE | AMBIGUOUS: a "may" gated by "on the application of any member": grant ruling NOTHING against JUST FALSE.
10. S170 | L270 | s161(1) (l.13358) | JUST FALSE (prior approval given, so the bar does not apply) | NOTHING | AMBIGUOUS: "without the prior approval" is an "unless" once met (a case-by-case question): JUST FALSE against a bar limited in its own wording (NOTHING).
11. S175a | L280 | s161(7) (l.13404) | JUST FALSE (proceedings on the second anniversary are in time, P4) | NOTHING | AMBIGUOUS: a period fixed in the text's own words (periods ruling (a) and the "until" bar of (d) point to JUST FALSE before the bar bites) against a bar limited in its own wording (NOTHING); I lean to the first.
12. S183b | L294 | s162(3) and (4) (l.13463) | JUST FALSE ((3)(a) transaction without the (4) conditions) | NOTHING | AMBIGUOUS: "Subject to subsection (4)" unmet means the exception fails, JUST FALSE, against "nothing in this section applies to any transaction ... that is (a)" limited in its own wording (NOTHING); the encoding's own s162(4) function answers JUST FALSE on these facts.
13. S184 | L295 | s162(3)(b) (l.13482) | JUST FALSE (a second home transaction outstanding) | NOTHING | AMBIGUOUS: "except that not more than one ... may be outstanding" once met (a case-by-case question).
14. S186b | L298 | s162(3) (l.13463) | JUST FALSE (no exception made out) | NOTHING | SCENARIO: the list of exceptions is not closed with "only", so the Guide gives NOTHING; my value was wrong.
15. S194b | L308 | s162(10) (l.13563) | JUST TRUE (approval before the transaction counts as prior approval) | NOTHING | SCENARIO: "does not include any approval ... given after" is a flat negative limited in its own wording; outside it the Guide gives NOTHING.
16. S215b | L344 | s163A(4) (l.13943) | NOTHING (an application for relief under another section) | JUST FALSE | AMBIGUOUS: "The reference ... is to an application under section 76A(13) or 391" read as a closed definition (JUST FALSE) against not closed with "only" or "means" (NOTHING).
17. S226c | L368 | s164(15)(a)(ii) (l.14176) | NOTHING (a child aged 18) | JUST FALSE | AMBIGUOUS: "deemed ... if ... a child of less than 18" is both a scope limit with no "only" (periods ruling (c), NOTHING) and a condition introduced with "if" (JUST FALSE).
18. S229c | L373 | s164A(1) (l.14220) | NOTHING (9% of members and 4.9% of shares) | JUST FALSE | AMBIGUOUS: a duty whose "if" is unmet (a case-by-case question).
19. S240b | L390 | s165(10) (l.14385) | JUST FALSE (director of a listed company, second limb not met) | NOTHING | SCENARIO: "does not apply to a person (a) ... and (b) ..." is a flat negative limited in its own wording; outside it the Guide gives NOTHING.
20. S251b | L402 | s168(5)(a) (l.14500) | JUST FALSE (agreement made on 1 January 1967) | NOTHING | SCENARIO: "does not include (a) any payment under an agreement entered into before 1 January 1967" limits itself; outside the limit NOTHING.
21. S253b | L404 | s168(5)(d) (l.14514) | JUST FALSE (pension above 3 years' emoluments) | NOTHING | SCENARIO: same reading as S251b.
22. S252b | L669 | s168(5)(c) (l.14507) | JUST FALSE (not a bona fide payment of damages) | NOTHING | SCENARIO: same reading as S251b (added in the second pass, written before it was run).
23. S288b | L447 | s173(14) (l.14906) | NOTHING (sent to an address not in the register) | JUST FALSE | SCENARIO: "is sufficiently served if ..." is an "if" condition and the Guide's worked example 1 gives JUST FALSE when it is unmet; my value contradicts it.
24. S326b | L502 | s201(11) (l.18058) | NOTHING (not a subsidiary at the year end) | JUST FALSE | AMBIGUOUS: a duty ("must state") whose "Where" is unmet: periods ruling (b) JUST FALSE against scope limit (c) NOTHING.
25. S331c | L513 | s201(17) (l.18140) | NOTHING (a banking corporation) | JUST FALSE | AMBIGUOUS: "(other than a banking corporation)" (a case-by-case question).
26. S332 | L514 | s201(18) (l.18158) | JUST FALSE (modifications determined by the MAS, so not "as they stand") | NOTHING | AMBIGUOUS: provisions apply "with such modifications and exceptions as are determined" by the MAS: not-as-they-stand (JUST FALSE) against the text being silent on the modified case (NOTHING).
27. S333b | L516 | s201(22) (l.18195) | JUST TRUE (year ended 1 July 2015) | NOTHING | SCENARIO: "does not apply ... in respect of any financial year which ended before 1 July 2015" is a flat negative limited in its own wording; outside it NOTHING.
28. S341b | L531 | s201A(6) (l.18311) | JUST TRUE (year ended 3 January 2016) | NOTHING | SCENARIO: "does not apply ... ended before 3 January 2016", same reading as S333b.
29. S377 | L601 | s204(1A) (l.19023) | `s 204 penalty` OF 10000, 24, TRUE, FALSE (I expected "or both") | `s 204 penalty` OF 10000, 24, FALSE, FALSE | SCENARIO: the text reads "a fine not exceeding $10,000 or to imprisonment for a term not exceeding 2 years" with no "or to both" (l.19021-19025); my value was wrong.
30. silent-S5 | L652 | s162(1)(a) and s162(8) (l.13417-13421, l.13549) | NOTHING (a person who is neither a director of the company nor of a related company, relationship "another person") | JUST FALSE | AMBIGUOUS: "(called ... a relevant director)" is a closed label and both director facts are false (JUST FALSE) against s162(8) "includes", an open list (NOTHING). My better question on the same case, silent-S5b (the restricted-transaction function, JUST FALSE), is satisfied.
31. silent-S10 | L653 | s204(1) (l.18995) | NOTHING (a person who is not a director fails to comply with s201(2)) | JUST FALSE | AMBIGUOUS: unmet element of an offence: "If any director of a company fails to comply" (an "if", JUST FALSE) against an offence limited in its own wording to directors (NOTHING).
32. S285a | L683 | s173(7)(c) (l.14854) | JUST FALSE (an auditor with no identification) | NOTHING | AMBIGUOUS: "identification, if any" is a duty whose "if" is unmet (a case-by-case question): JUST FALSE against NOTHING.

## GAP: scenarios that cannot be asked (14)

None of these has an assertion; each was checked against the signatures of the module named.

33. S47 | no assertion | s147(1) (l.11893) | FALSE ("obliged to obtain": a director already qualified) | not asked | GAP: the only function that reaches the duty is deontic; the non-deontic ones ask the last day and whether the director obtained the qualification in time, not whether the duty exists.
34. S102 | no assertion | s153 (l.12388) | NOTHING (repealed) | not asked | GAP: a coverage row only, no function.
35. S168 | no assertion | ss160A to 160D (l.13347) | NOTHING (repealed) | not asked | GAP: a coverage row only, no function.
36. S241 | no assertion | ss166 and 167 (l.14399) | NOTHING (repealed) | not asked | GAP: a coverage row only, no function.
37. S248 | no assertion | s168(2) (l.14458) | TRUE (the director must take reasonable steps to secure the particulars) | not asked | GAP: the duty is expressed only by a deontic function.
38. S258 | no assertion | s170 (l.14552) | NOTHING (repealed) | not asked | GAP: a coverage row only, no function.
39. S267 | no assertion | s171(2) (l.14618) | TRUE until 28 December 1968, FALSE from 30 December 1968 (a corporation acting as secretary may continue for 12 months) | not asked | GAP: the encoding records the row as inert, a comment with no function.
40. S282 | no assertion | s173(1) (l.14761) | TRUE (the Registrar must keep the registers) | not asked | GAP: deontic function only.
41. S318 | no assertion | ss200 and 200A (l.17924) | NOTHING (repealed) | not asked | GAP: a coverage row only, no function.
42. S348 | no assertion | s201B(2)(b) (l.18417) | TRUE for a spouse of an executive director, NOTHING for a nephew | not asked | GAP: the s201B(2) function takes only counts of members within (a), (b) or (c), so the kind of relative cannot be stated.
43. S356 | no assertion | s202(4) (l.18571) | TRUE (the Registrar must give the directors an opportunity of being heard) | not asked | GAP: the only s202(4) function asks whether an order has ended; the hearing duty has no function.
44. silent-S1 | no assertion | s145 (l.11596) | NOTHING (a duty to have a director who is a citizen of Singapore) | not asked | GAP: the s145 functions speak of ordinary residence only and take no citizenship fact.
45. silent-S6 | no assertion | s164 (l.13978) | NOTHING (a register of a company secretary's holdings) | not asked | GAP: the s164 functions take director and chief executive kinds only.
46. silent-S11 | no assertion | s173(1) (l.14761) | NOTHING (a Registrar's register of shareholders) | not asked | GAP: the register kinds are directors, chief executive officers, secretaries and auditors, and the duty function is deontic.
