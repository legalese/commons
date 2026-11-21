# Triage, reader group 1 (keel, sga1, sga2, sga3, with their seat layers)

Run: `l4-main-110 run tests-independent.l4` from `enc/`, `JL4_LIBRARY_PATH` unset, diagnostics read (not the exit code).
Result: 623 assertions, 602 satisfied, 21 failed, 0 refused, 0 other diagnostics.
Scenarios written: 373 (334 from the text, S1 to S334, and 39 seat scenarios, S335 to S373, in the "Seat addendum" of ANSWERS.md).
Format of each line: scenario | file line of my assertion in `enc/tests-independent.l4` | provision (line of its text in `inputs/CoA1967.txt`) | my expected answer | what the encoding answered | verdict, with the reason.
"JUST FALSE" is the text's own no, "NOTHING" is not covered, as in the Guide.

## Failed assertions (21)

S103b | 160 | s 10(5) (text 2778) | JUST FALSE (a partner who is not a public accountant) | NOTHING | SCENARIO: the text gives the effect to partners "who are public accountants"; the Guide's scope-limit sentence gives NOTHING outside it; my ANSWERS S103 said NO.
S103c | 161 | s 10(5) (text 2778) | JUST FALSE (a public accountant who became a partner after the appointment) | NOTHING | SCENARIO: same reading, a limit on a deeming with no "only".
S104c | 164 | s 10(6) (text 2786) | JUST FALSE (a director of the corporation who does not practise) | NOTHING | SCENARIO: same reading as S103b.
S138c | 231 | s 63A(2) (text 6573) | JUST FALSE (a company not listed: the return must state the 50 largest members, so "need not" is no) | NOTHING | SCENARIO: the text only says a listed public company need not; the unlisted case is outside a scope limit with no "only".
S142c | 238 | s 63C (text 6649) | NOTHING (a public company) | JUST FALSE | SCENARIO: the section opens "Where a private company issues"; ruling (b) of the periods ruling gives JUST FALSE when a "where" fails, and I used rule (c). The encoding follows (b).
S165b | 285 | s 71(1)(d) (text 6915) | JUST FALSE (a subdivision that does not keep the paid proportion) | NOTHING | SCENARIO: "so however that" is a proviso on a grant, not "only if" or "unless"; a grant limited in its own wording gives NOTHING outside the limit.
S194b | 344 | Sixth Schedule Part 2 paragraph 2(1) (text 28778) | NOTHING (shares in a corporation that will not become a subsidiary) | JUST FALSE | SCENARIO: the paragraph opens "Where it is proposed to acquire shares in a corporation which ... will become a subsidiary"; ruling (b) gives JUST FALSE; I used rule (c).
S207b | 368 | s 76(3) (text 7379) | JUST FALSE (the relevant purpose was only incidental) | NOTHING | AMBIGUOUS: reading A, the Guide's "a condition the text introduces with if" gives JUST FALSE; reading B, "is taken to have given ... if (a) and (b)" is a deeming rule that adds cases and does not close the question, so NOTHING.
S210b | 373 | s 76(6) (text 7420) | NOTHING (no conviction) | JUST FALSE | AMBIGUOUS: a "may" gated by "Where a person is convicted ... and the Court is satisfied" is a named split site: JUST FALSE under ruling (b), NOTHING under the grant ruling.
S213b | 377 | s 76(8)(c) (text 7449) | JUST FALSE (a liability not incurred in good faith) | NOTHING | SCENARIO: the exception is limited by a relative clause ("that was incurred in good faith ..."), not by "if" or "unless"; the case outside the limit is simply not covered. My ANSWERS S213 called it an "if-style qualifier".
S217b | 386 | s 76(9)(a)(ii) (text 7553 and following) | JUST FALSE (the loan is not on ordinary commercial terms, so the exception does not apply) | NOTHING | AMBIGUOUS: reading A, a "where" gate on an exception fails, so JUST FALSE under ruling (b); reading B, the text never says such a loan IS prohibited, so NOTHING.
S242b | 429 | s 76(11) (text 7985) | NOTHING (the application is by a member, not the company) | JUST FALSE | AMBIGUOUS: a "may" gated by "Where, on application to the Court by a company"; named split site (ruling (b) against the grant ruling).
S245b | 436 | s 76A(2) (text 8130) | JUST FALSE (the company gives oral notice) | NOTHING | SCENARIO: "The company may ... avoid ... by giving written notice" is a grant limited by its own wording; an oral notice falls outside the limit, so NOTHING.
S247c | 440 | s 76A(6) (text 8199) | JUST FALSE (a certificate signed by one director only) | NOTHING | AMBIGUOUS: reading A, "If a certificate signed by not less than 2 directors, or by a director and a secretary" is an "if" condition, JUST FALSE; reading B, it describes the certificate inside a protective consequence and does not say that a certificate signed by one director leaves the person liable, so NOTHING.
S264b | 498 | s 76C(1) (text 8511) | JUST FALSE (the scheme was authorised only after the purchase) | NOTHING | SCENARIO: "may make ... if the purchase is made in accordance with an equal access scheme authorised in advance" is a grant with an "if" gate; the Guide gives NOTHING when the gate fails (I applied exactly this to S253 and then forgot it in S264).
S276b | 524 | s 76DA(1) (text 8810) | JUST FALSE (authorised by ordinary resolution only) | NOTHING | SCENARIO: the same grant "may ... if" gate as S264b.
S285c | 541 | s 76F(3) (text 8978) | NOTHING (a company secretary approves knowing the company is not solvent) | JUST FALSE | AMBIGUOUS: an unmet element of an offence is a named split site (the person is neither a director nor a chief executive officer): JUST FALSE or NOTHING.
S304b | 589 | s 77(1) (text 9246) | NOTHING (an option exercisable after 4 years only) | JUST FALSE | AMBIGUOUS: reading A, ruling (a): "after a period of 5 years has elapsed" is a period fixed in the text's own words, so outside it JUST FALSE; reading B, ruling (c): a scope limit with no "only", so NOTHING.
S311 | 604 | s 78A(1) with s 78A(3) (text 9304, 9320) | JUST FALSE (the constitution excludes the power: may the company use it?) | NOTHING | SCENARIO: (3) says the constitution "may exclude or restrict" the power, which is a permission to the constitution; the text never says in its own words that the company may not use the power, so NOTHING.
S314a | 610 | s 78B(2) (text 9375) | JUST FALSE (the reduction involves a return of cash: the company must meet the solvency requirements, so "need not" is no) | NOTHING | AMBIGUOUS: reading A, "the company need not meet the solvency requirements if the reduction does not involve any of the following" is an "if" condition that fails, JUST FALSE; reading B, "need not" is a permission to the company and its gate failing leaves the text silent, NOTHING.
S321 | 625 | s 78D(3) (text 9512) | JUST FALSE (a creditor with no admissible debt or claim) | NOTHING | SCENARIO: "Subsection (2) applies to a creditor of the company who ... is entitled to any debt or claim" is a scope statement with no "only"; the Guide gives NOTHING outside it.

## Gaps (10)

S282 | none | s 76E(3) (text 8916) | YES, the authority for a market purchase may be unconditional | no function asks it (the nearest, `s 76E(3) the authority for a market purchase states the particulars the subsection requires`, asks about the particulars) | GAP.
S269c | none (S269a and S269b are at 510 and 511) | s 76D(2A) (text 8611) | NO, class consent is not required when the purchase covers all the shares in the class | no function asks "is consent required" (`s 76D(2A) the company has obtained the consent the subsection requires` asks whether it was obtained) | GAP.
S318b | none (S318a is at 618) | s 78B(6) (text 9432) | YES, the requirement under (4)(b) ceases if the resolution is revoked | not asked: the last-day function takes a revocation date, but the text names no day for the end, so no value can be written for it | GAP.
S319c | none (S319b is at 620) | s 78B(5) (text 9425) | NOTHING for the maximum penalty (the section states none) | there is no penalty function to ask | GAP.
S332d | none (S332a to S332c are at 648 to 650) | s 78J (text 9859) | NOTHING for the maximum penalty (the section states none) | there is no penalty function to ask | GAP.
S195 | 345 | Sixth Schedule Part 1 (text 28738) | 2 financial years of dividends for a company that has existed for 2 years | no function counts the years; I asserted only that the dividend matter must be stated | GAP for the number.
S99 | 150 | s 10(1) (text 2739) | NO, an accounting entity acting as auditor is not prohibited | no function asks "is it prohibited"; I asserted the nearest ("may consent or act") with the answer NOTHING, which passes | GAP: the exact question is not askable; the nearest passes.
S101b | 153 | s 10(3) (text 2755) | NO, with prior consent the appointment is not prohibited | no function asks "is it prohibited"; I asserted the nearest ("may appoint") with NOTHING, which passes | GAP: same.
S143b | 241 | s 64(2) (text 6671) | YES, the constitution may provide that a member may not vote while calls are unpaid | no function asks "may the constitution provide"; I asserted the effect (the member is not entitled to vote) with JUST TRUE, which passes | GAP: the exact question is not askable; the nearest passes.
S168 | 290 | s 71(1A) (text 6932) | NOTHING (is lodging required?) | no function asks "is lodging required"; I asserted the grant ("may lodge") with JUST TRUE, which passes | GAP: same.

## A scenario of mine that passes but was wrong as written (1)

S256a | 472 | s 76B(3) and (3A) (text 8324, 8344) | my ANSWERS S256 said the 20 percent cap does not apply after a reduction under s 78B (reading the "unless" in (3)(a)) | the assertion I could write is on (3A): the total is the total as altered, 800, and it passes | SCENARIO: (3A) says "despite subsection (3)(a) and (b)", so the cap still applies, to the altered total; my original answer was wrong and the passing assertion tests the corrected reading, not the one in ANSWERS.md.

## Tally

ENCODER 0, SCENARIO 14 (13 failed assertions, plus S256a which passes), AMBIGUOUS 8 (all failed), GAP 10; 32 triage lines in all.
The 21 failed assertions are 13 SCENARIO and 8 AMBIGUOUS.
Each failure sits where the answer rested on the Guide's convention for "no" against "not said"; none is a disagreement about what the text says.
Seat layer: all 47 seat assertions (13 keel, 11 sga1, 10 sga2 and 13 sga3, covering the 39 seat scenarios S335 to S373), each with the facts a person in the seat would state, were satisfied.
Periods: no failed assertion concerns a period count; the period assertions on the encoding's conventions P1 to P9 (last day in time, the day after late) all passed, so there is no AMBIGUOUS verdict for a differing count.
