# Triage: SFA 2001, keel (ss 1-4B) and sfad (Part 13 Div 1 Subdivisions 3-5), independent reader group 1

Run: `l4-main-110 run tests-independent.l4` from `enc/`, `JL4_LIBRARY_PATH` unset.
Scenarios written 544 (numbers 1-544 in `ANSWERS.md`): 531 `#ASSERT` lines (514 satisfied, 17 failed, 0 refused), 9 `#TRACE` duty scenarios (535-543; each result matched the expected value in `ANSWERS.md`), 4 gaps.
Verdicts: ENCODER 2, SCENARIO 6, AMBIGUOUS 9, GAP 4 (21 lines).
Failing assertions were left failing; no expected value was changed to match the encoding.

How the answers were written, so a reader can weigh them.
Scenarios 1-438 were written in `ANSWERS.md` before any `.l4` file was opened.
Scenarios 439-534 and 544 were written after I had opened the modules for exported names and signatures (439-441 and 544 after seeing a failure, 442-470 after reading the seat's names, 471-534 after the first full run); their expected values still come from the text, but they are not blind.
Scenarios 535-543 were written after one probe showed that `#TRACE` works on a duty.
The heading or first paragraph of each batch in `ANSWERS.md` says so.
While diagnosing failures I read the function bodies and the encoder's inline FORK and MARGINAL-READING comments for the 17 failing functions; I opened no NOTES, PROGRESS or plan file.

Format: scenario | assertion line in `enc/tests-independent.l4` | provision (text line in `inputs/SFA2001.txt`) | my expected | encoding answered | verdict, with the reason.

## ENCODER (2)

- 160 | line 187 | s 4(10)(f) (3977-3980), "for the purposes of Part 7, an interest in a ... derivatives contract ... cash settlement only" | NOTHING | JUST FALSE | ENCODER. The limb is confined by its own words to Part 7 and has no "only" closing the scope, so for a provision other than Part 7 the answer is NOTHING (scope limit, ruling (c); Guide: "a scope limit with no only answers NOTHING"). The encoder's own comment records NOTHING as the other reading.
- 393 | line 416 | s 276(7)(a) (44540-44543), "Subsections (1), (3) and (4) do not apply where the securities ... are (a) ... of the same class as other securities ... listed" | JUST FALSE | NOTHING | ENCODER, a close call. The only gate is a "where" condition, and ruling (b) says a failed "where" answers JUST FALSE. The encoder read "where" as the limit of an exemption (its fork note s276-7 records JUST FALSE as the other reading), which the grant and prohibition sentence of the Guide supports; I weigh ruling (b) as the more specific, but a reader who prefers the other sentence should treat this as AMBIGUOUS.

## SCENARIO (6), my mistakes

- 13 | line 40 | s 2(1) "business rules" (1831-1845) | JUST TRUE | JUST FALSE | SCENARIO. I answered Y for by-laws that govern an approved exchange and its members (limb (a)) alone; the text joins (a) and (b) with "and" (1843-1845), so both are needed and the encoding is right. Re-ask 439 (both limbs) passes.
- 89 | line 116 | s 2(1) "representative" (a)(ii) (2993-2998) | JUST TRUE | JUST FALSE | SCENARIO. My inputs said an officer of a corporation performs the activity but left the input "the person carries out for the principal the activity" FALSE, so they contradicted each other; the encoding needs both. Re-ask 544 with both set passes.
- 135 | line 162 | s 3(3)(a) (3751-3758) | JUST TRUE | NOTHING | SCENARIO. I asked the s 3(3) function, which is not the question I meant (is the person associated under s 3(1)). Re-ask 440, asked of s 3(1), passes.
- 136 | line 163 | s 3(3)(d) (3770-3773) | JUST TRUE | NOTHING | SCENARIO. Same mistake as 135. Re-ask 441 passes.
- 292 | line 317 | s 271(2)(b)(i) (42621-42624), release agreed by 74% against the three-fourths majority | JUST FALSE | NOTHING | SCENARIO. "Subsection (1) does not invalidate (a) ... or (b) ..." is a flat negative that reaches only the saved cases; a 74% agreement is outside both limbs and the text is silent about it (Guide: a limit in the text's own wording and the case falls outside it answers NOTHING). The encoding is right. This differs from 393 because 271(2) has no "if" or "where" gate over the whole.
- 368 | line 391 | s 275(1A) (44210-44213), person acquires as nominee, not as principal | JUST FALSE | NOTHING | SCENARIO. "To a person who acquires ... as principal" is a scope limit on the exemption with no "only" (ruling (c)); a nominee is outside the scope and the text says nothing about them. The encoding is right.

## AMBIGUOUS (9)

- 162 | line 189 | s 4 as a whole (3783-3994), a person with none of the listed routes to an interest | NOTHING | JUST FALSE | AMBIGUOUS. Reading 1 (mine): s 4 lists ways a person has an interest and never closes the list with "only", so silence, NOTHING. Reading 2 (encoder): each route is an "if" and with no route holding the text's own answer is no, JUST FALSE.
- 230 | line 256 | s 266(2) (42107-42113), the trustee has formed no such opinion | NOTHING | JUST FALSE | AMBIGUOUS, split site ("may" gated by "where"). Reading 1 (mine, grant ruling): a power whose gate failed answers NOTHING. Reading 2 (encoder, ruling (b)): a failed "where" answers JUST FALSE.
- 402 | line 425 | s 277(1AB) (44686-44703), the listed entity has not guaranteed the subsidiary | NOTHING | JUST FALSE | AMBIGUOUS, same split site as 230 (the Authority "may" declare, "where" the guarantee exists).
- 256 | line 281 | s 268(10)(b) (42345-42352), annual accounts, trustee has not consented | JUST FALSE | NOTHING | AMBIGUOUS, case-by-case ("a duty whose if is unmet"). Reading 1 (mine): "need not be audited ... if the trustee has consented" is an "if" condition, so unmet answers JUST FALSE. Reading 2 (encoder): the dispensation is a grant and its gate failed, so NOTHING.
- 290 | line 315 | s 271(1) (42605-42611), a clause that exempts the trustee only where the trustee shows the required care | JUST FALSE | NOTHING | AMBIGUOUS. Reading 1 (mine, ruling (b)): "void insofar as ... where the trustee fails to show the care", the "where" fails, so not void, JUST FALSE. Reading 2 (encoder): "insofar as" limits a prohibition in its own wording and the case falls outside the limit, NOTHING.
- 389 | line 412 | s 276(3) (44459-44461), the holding corporation is itself an accredited investor | JUST FALSE | NOTHING | AMBIGUOUS, case-by-case ("(other than X)"). Reading 1 (mine): the carve-out takes the corporation outside the bar, so the bar answers no. Reading 2 (encoder): the text is silent about a carved-out corporation, NOTHING.
- 263 | line 288 | s 268A(2) (42401-42404), report period ended 30 June 2026, lodged 31 August 2026 | JUST TRUE | JUST FALSE | AMBIGUOUS, period count. Mine: "not later than 2 months after the end of that period" ends 31 August (the end of the month, because 30 June is the last day of June). Encoding: ends 30 August (same day of the month, P4). My own header convention in `ANSWERS.md` ("N months after D ends on the same day of the month") gives 30 August, so my scenario was not consistent with my own header; I keep the verdict AMBIGUOUS because the end-of-month reading is a recognised alternative.
- 351 | line 375 | s 273(5) (44044-44057), declaration 1 March 2026, offer 1 September 2026 ("for a period of 6 months from the date") | JUST TRUE | JUST FALSE | AMBIGUOUS, period count. Mine: the 6 months run through 1 September. Encoding: through 31 August (the date counts as day 1, P10); checked by `#EVAL` with offers on 31 August (JUST TRUE) and 1 September (JUST FALSE). The same words "6 months from the date of the initial acquisition" in s 276(1) are counted through 1 September by the encoding (my 383 and 384 pass), so the encoding counts the same phrase two ways.
- 398 | line 421 | s 277(1A) (44679-44682), statement lodged 1 March 2026, offer 1 September 2026 ("within a period of 6 months from the date") | JUST TRUE | JUST FALSE | AMBIGUOUS, period count. Same two counts as 351: mine through 1 September, encoding through 31 August (checked by `#EVAL`).

## GAP (4)

- 197 | no assertion | s 261(1A) (41840-41841) | NOTHING | no function asks whether s 268A is disapplied for a prescribed entity | GAP.
- 234 | no assertion | s 266(1) (42083-42100) | NOTHING | no function gives a penalty for a trustee's breach of s 266(1); the text states none | GAP.
- 299 | no assertion | s 272(1) (42649-42650), "(other than section 257)" | N | no function asks whether s 257 still applies to an offer exempt under s 272 | GAP.
- 356 | no assertion | s 273(8A) (44079-44084) | NOTHING | no function takes the offer's paragraph, so an advertisement of an offer under paragraph (i) cannot be asked | GAP.

## Not covered by assertions

Duties other than ss 268(4)(a), 268(4)(b), 268(6)(a) and 268(6)(b) were not run as traces (ss 261(1C), 265A(1), 266(3)(b), 266(4), 268(9), 268(11), 268A, 269(2), 270, 273(8A)); the four that were run take the allowed days as an input, so the month arithmetic of s 268(6) is left to the caller (92 days and 151 days in my traces 540-543).
