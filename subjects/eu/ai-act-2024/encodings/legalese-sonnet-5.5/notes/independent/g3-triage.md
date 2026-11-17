# Triage: dst-rev-aia3 (Arts 72-113, P8 + P9 + keel Arts 111 and 113)

Test file: `enc/tests-independent.l4` (1065 lines).
Run from inside `enc/` with `JL4_LIBRARY_PATH` unset, binary `l4-main-110`, output kept in `work/final.out`.
Result read from the diagnostics: 494 assertions, 474 `eval/assertion-passed`, 20 `eval/assertion-failed`, 0 refused (no other diagnostic code).
"File line" is the line of my `#ASSERT` in `enc/tests-independent.l4`; for a GAP it is the line of the `-- GAP` comment.
"Text line" is the line of `inputs/eu-ai-act-2024-1689-consolidated-20260727.txt`.
Scenario numbers are the numbers of `ANSWERS.md` (X-series numbers are extras described at its end).

## Failed assertions (20)

ENCODER (9)

- ANSWERS 30, file line 119, Art 73(6) second subparagraph, text l.1137 ("shall not perform any investigation ... prior to informing the competent authorities"): expected JUST FALSE once the authorities are informed, encoder NOTHING; ENCODER (ruling (d) of the delegated-definitions paragraph: an "until"/"prior to" bar answers JUST TRUE before X and JUST FALSE after X; the encoder gets the "before" side right, seat SP8-5 passes, and gives NOTHING after).
- ANSWERS 95, file line 243, Art 75(1e) fourth sentence, text l.1183 ("If a notified body ... does not perform those tasks adequately, the Commission may withdraw the delegation"): expected JUST FALSE when the body performs adequately, encoder NOTHING; ENCODER (a "may" grant under "If" is the guide's worked example 1; it is a power, not a duty, so the six case-by-case questions do not cover it).
- ANSWERS 132 (local 132b), file line 319, Art 75b first sentence, text l.1221 ("If, during proceedings under Article 75a(2), the operator concerned offers commitments ... the AI Office may ... make those commitments binding"): expected JUST FALSE when commitments are offered outside such proceedings, encoder NOTHING; ENCODER (same reason as ANSWERS 95).
- ANSWERS 150, file line 349, Art 75c(8) first subparagraph, text l.1248 (five-year limitation period): expected JUST FALSE (power not barred) for an infringement of 2026-09-01 asked on 2030-01-01, encoder NOTHING; ENCODER (a period the text fixes in its own words, ruling (a), answers on both sides; the encoder answers JUST TRUE after the five years, ANSWERS 149 and 152 pass, and NOTHING inside them).
- X-151c, file line 957, Art 75c(8) first subparagraph, text l.1248: continuing infringement ceased 2029-01-01, asked 2033-06-01 (inside the five years): expected JUST FALSE, encoder NOTHING; ENCODER (same finding as ANSWERS 150, a twin I wrote after finding my arithmetic wrong in ANSWERS 151).
- X-153c, file line 959, Art 75c(8) second subparagraph, text l.1249 (limitation of the power to enforce, five years from the decision becoming final): final 2027-03-01, asked 2031-06-01: expected JUST FALSE, encoder NOTHING; ENCODER (same finding, twin of ANSWERS 153).
- ANSWERS 333 (local 320), file line 797, Art 111(1), text l.1620 with Art 113 default date l.1657: asked 2026-08-01, expected NOTHING (ANSWERS 333, gate), encoder JUST DATE 2030-12-31; ENCODER (the encoding's other substantive functions answer NOTHING before their gate, and its own seat question "does General apply" answers JUST FALSE on this date, yet the Art 111 date functions return a date without consulting the gate; the other reading, that a deadline date is a plain fact of the text, is noted and not preferred).
- ANSWERS 345 (local 326), file line 809, Art 111(2) second sentence, text l.1623 and l.1657: asked 2026-08-01, expected NOTHING, encoder JUST DATE 2030-08-02; ENCODER (same as ANSWERS 333).
- ANSWERS 351 (local 337), file line 831, Art 111(4), text l.1627 and l.1657: asked 2026-07-30 (Omnibus in force from 27 July, Art 111 applicable from 2 August), expected NOTHING, encoder JUST DATE 2026-12-02; ENCODER (same as ANSWERS 333; the ANSWERS entry states the date regime in terms).

SCENARIO (5, my own mistakes)

- ANSWERS 130, file line 313, Art 75a(7), text l.1217 ("may appoint ... experts ... from the Member State's competent authorities with the agreement of the authority concerned"): expected JUST FALSE without agreement, encoder NOTHING; SCENARIO (the proviso is a limit on a grant in the text's own wording with no "if", and the guide answers NOTHING for that; I filed it under the case-by-case questions but it is not one of the six, and I misapplied the guide).
- ANSWERS 151, file line 351, Art 75c(8), text l.1248: continuing infringement that ceased 2029-01-01, asked 2034-06-01, expected JUST FALSE, encoder JUST TRUE; SCENARIO (arithmetic: five years from 2029-01-01 end on 2034-01-01, so 2034-06-01 is after the period and the power IS barred; the encoder is right, and ANSWERS 152 already says barred from 2035).
- ANSWERS 153, file line 355, Art 75c(8) second subparagraph, text l.1249: decision final 2027-03-01, asked 2032-06-01, expected JUST FALSE, encoder JUST TRUE; SCENARIO (five years from 2027-03-01 end on 2032-03-01; 2032-06-01 is after it; the encoder is right).
- ANSWERS 231 (local 233), file line 567, Art 86(1), text l.1359 ("subject to a decision ... which produces legal effects or similarly significantly affects that person"): decision with no legal or similarly significant effect, expected JUST FALSE, encoder NOTHING; SCENARIO (the relative clause defines the class of persons entitled, a scope limit with no "only", so ruling (c) and the guide's "limits a grant in its own wording" give NOTHING; my ANSWERS 231 cited "which produces ... that" as if it were an "if", which is not among the words the guide lists, and it contradicts my own ANSWERS 232 and 233).
- X-285c, file line 925, Art 99(4)(da), text l.1483 (inserted by M1): asked 2026-07-27 for a non-compliance with Art 25(2) and (4), expected JUST TRUE, encoder NOTHING; SCENARIO (I took the date of the amendment as enough; probes show the encoder gates "is subject to administrative fines" on the date the infringed provision itself applies: NOTHING for Art 25(2),(4) and Art 16 until 2027-12-02 on the Annex III route, JUST TRUE for Art 50 from 2026-09-01; that is a defensible reading because an obligation that does not yet apply cannot be breached; one inconsistency to note: the sibling ceiling function is not gated that way, so ANSWERS 288 (Art 16, 2026-07-26, SMC, 15,000,000) passes while the "subject to fines" function answers NOTHING for the same facts).

AMBIGUOUS (6)

- ANSWERS 11, file line 75, Art 72(4), text l.1124 ("providers shall have a choice of integrating ... provided that it achieves an equivalent level of protection"): expected JUST FALSE when the integration gives no equivalent protection, encoder NOTHING; AMBIGUOUS (reading A: "provided that" is a plain variant of "as long as" and the guide answers JUST FALSE for it; reading B: it is a proviso limiting a grant in its own wording, for which the guide answers NOTHING; the guide's list of words does not include "provided").
- ANSWERS 50, file line 159, Art 74(3) second subparagraph, text l.1152 ("Member States may designate another relevant authority ... provided they ensure coordination"): expected JUST FALSE without coordination, encoder NOTHING; AMBIGUOUS (same two readings as ANSWERS 11).
- ANSWERS 91, file line 235, Art 75(1d), text l.1182 ("Before taking a decision that would have the effect of prohibiting or restricting ... the AI Office shall ... notify"): a decision without that effect, expected JUST FALSE, encoder NOTHING; AMBIGUOUS (one of the six case-by-case questions: a duty whose "where" or "before" condition is unmet; reading A: no duty arises, so NO; reading B: the text is silent, so NOTHING).
- ANSWERS 358 (local SP8-10), file line 981, seat `P8-seat-notified` "Under Article 78 ... does Notified bodies, GPAI, governance, penalties and Art 78 apply on the date asked", text l.1662 ("shall apply from 2 August 2025"): asked 2025-08-01, expected NOTHING (ANSWERS legend: NOTHING = not yet applicable on the date asked), encoder JUST FALSE; AMBIGUOUS (reading A: my legend, and the way the encoder answers the substantive gate assertions that pass (at least 23 assertions whose comment marks a date gate); reading B: ruling (a), "shall apply from" fixes a period in the text's own words, so before it the text itself says no, which is what the direct seat question returns; see the note below).
- ANSWERS 333 (local SK-6), file line 1031, seat `P0-seat-provider` "Under Article 111 ... does General apply on the date asked", text l.1657: asked 2026-08-01, expected NOTHING, encoder JUST FALSE; AMBIGUOUS (same as ANSWERS 358).
- ANSWERS 352 (local SK-8), file line 1035, seat `P0-seat-provider` "Under Article 1 ... does Chapter I apply on the date asked", text l.1660: asked 2025-02-01, expected NOTHING, encoder JUST FALSE; AMBIGUOUS (same as ANSWERS 358).

## GAP (26 comment lines covering 42 ANSWERS scenarios)

Each line: ANSWERS number, file line, provision and text line, my expected answer in ANSWERS.md, what the encoding offers.
All verdict GAP; "no function" means no layer-1 function takes the fact the scenario varies.

- ANSWERS 47, file line 1040, Art 74(2) second sentence, text l.1150: whether prohibited-practice reports also go to national competition authorities; no function carries the addressee.
- ANSWERS 54, file line 1041, Art 74(5), text l.1154: whether the Art 14(4) point (a) power may be exercised remotely; the function covers only points (d) and (j).
- ANSWERS 84, file line 1042, Art 75(1a), text l.1179: whether the report may go to the market surveillance authority under Art 73(1) instead; no function.
- ANSWERS 85, file line 1043, Art 75(1a) with Art 73(4), text l.1179: days for a death report to the AI Office; the Art 73 day functions have no AI Office input.
- ANSWERS 121, file line 1044, Art 75a(4)(e), text l.1210: sealing beyond the duration of the inspection; the function has no duration input.
- ANSWERS 140, file line 1045, Art 75c(4) with Art 99(4), text l.1232-1233 and l.1477: ceiling of an AI Office fine (30,000,000 at turnover EUR 1,000,000,000); no function gives that ceiling.
- ANSWERS 141, file line 1046, Art 75c(4)(b)(c), text l.1234-1235: failure to comply with a decision of Art 75a or a binding commitment; the conduct input covers the (a) infringement only.
- ANSWERS 166, file line 1047, Art 76(2), text l.1265: derogation from Art 60(4) point (a); the function has no point input.
- ANSWERS 8, file line 1048, Art 72(3), text l.1122: adoption on 2027-09-03 is late; the encoding returns the deadline date (asserted under ANSWERS 7), not a met-in-time verdict.
- ANSWERS 35, file line 1049, Art 73(7), text l.1138: guidance issued 2025-08-03 misses 2025-08-02; same pattern, deadline asserted under ANSWERS 34.
- ANSWERS 37, file line 1050, Art 73(8), text l.1139: measures on day 8; same pattern, deadline asserted under ANSWERS 36 and X-36c, X-36d.
- ANSWERS 101, file line 1051, Art 75(2a), text l.1193: told on 2027-01-16; same pattern, deadline asserted under ANSWERS 100 and X-100c, X-100d.
- ANSWERS 106, file line 1052, Art 75(3), text l.1195: supplied on day 31; same pattern, deadline asserted under ANSWERS 105 and X-105c.
- ANSWERS 117, file line 1053, Art 75a(3), text l.1203: a simple request need not indicate the right of review; covered by ANSWERS 116 (a complete simple request without that statement is JUST TRUE), no separate function.
- ANSWERS 143, file line 1054, Art 75c(4), text l.1236 with l.1488: ceiling 7,500,000 at turnover EUR 100,000,000; same as ANSWERS 140.
- ANSWERS 223, file line 1055, Art 83(1), text l.1338-1345: a finding outside the seven listed (instructions for use missing) cannot be put to the function.
- ANSWERS 262, file line 1056, Art 96(1)(g), text l.1444: guidelines published by 1 August 2027; the act is deontic only and exposes no deadline.
- ANSWERS 265-277, file line 1057, Art 97, text l.1452-1462: delegation of power (five-year periods, report nine months before the end, tacit extension, revocation, objection period); no module encodes Art 97.
- ANSWERS 278, file line 1058, Art 98, text l.1464-1467: committee procedure; no module encodes Art 98.
- ANSWERS 293 second half (shown as 293b), file line 1059, Art 99(4)(f), text l.1486: Art 33(2) is not named; the infringement type is the whole (f) wording, so Art 33(2) alone cannot be asked.
- ANSWERS 313, file line 1060, Art 101(1) with Art 99(6), text l.1526 and l.1489: whether the SME rule reaches an Art 101 fine; the Art 101 ceiling function has no SME input.
- ANSWERS 314-321, file line 1061, Arts 102 to 109 and the Annex I point of Art 110, text l.1539-1616: amendments of other Acts ("requirements of Chapter III Section 2 shall be taken into account"); no function, and the number of the added Annex point (68) is not exposed.
- ANSWERS 328, file line 1062, Art 112(5), text l.1642: AI Office evaluation by 2 August 2028; no date function for paragraph 5.
- ANSWERS 332, file line 1063, Art 112(13), text l.1653: assessment of enforcement by 2 August 2031 and the report to the European Economic and Social Committee; the function covers the proposal only.
- ANSWERS 295, file line 1064, Art 99(4) with Art 99(3), text l.1477 and l.1476: whether an Art 5 infringement is fined under Art 99(4); the function answers whether a non-compliance is subject to administrative fines, not under which paragraph, so NO cannot be put to it.
- ANSWERS 336, file line 1065, Art 111(1) opening words, text l.1620: Art 5 applies to Annex X components without the 2030 delay; no function for the "without prejudice to Article 5" clause.

## Counts by verdict

ENCODER 9, SCENARIO 5, AMBIGUOUS 6, GAP 26 comment lines (42 ANSWERS scenarios); 46 triage lines in all.

## Notes for the reader

1. Date gates are treated two ways, and my ANSWERS legend sides with one of them.
   At least 23 assertions (those whose comment marks a date gate) expect NOTHING before an application date and pass; the three direct seat questions ("does General / Chapter I / Art 78 group apply on the date asked") answer JUST FALSE before it.
   Ruling (a) ("a period the text fixes in its own words") can be read to give JUST FALSE for "shall apply from", which would contradict those; the family needs one ruling on "shall apply from <date>".
2. Thirteen keel assertions call `Art 113 the provision group applies`, which returns a plain `BOOLEAN`, so NOTHING cannot be expressed; I asserted FALSE where ANSWERS says NOTHING and said so in each comment ("plain BOOLEAN").
   They pass; they are not findings.
3. The X-series (60 labels, listed at the end of `ANSWERS.md`) and the seat assertions beyond S1-S30 were written after I had read function names and types from the `.l4` files, and after my first run of the P8 block; their expected values come from the text and the convention, but they are not blind in the way ANSWERS 1-369 are.
4. `ANSWERS.md` was changed twice during the work: scenario 33 was corrected before any run (it first said NOTHING for a notification not of type (c), which misapplied ruling (c); the test expects JUST FALSE as the corrected entry says), and scenario 315 had been garbled in writing and was rewritten (it now reads YES on both dates).
   No expected value of a failing assertion was changed after a run; ANSWERS 151 and 153 stay wrong as written, and the twins X-151c and X-153c carry the arithmetic done right.
5. The placement date of the test system is 2028-08-15 for the Annex III and Annex I contexts, so it is not after the date asked for any assertion dated 2028-09-01 or later; assertions dated 2026-09-01 on high-risk contexts (for example seat SP8-6, ANSWERS S4, the AI Office competence question) use that placement date although it is later than the date asked, which the encoding does not check.
6. To explain ANSWERS 151, 153, X-285c and the gate failures I ran extra `#EVAL` probes of the encoding's functions at boundary dates (scratch files under `work/enccopy/`, `probe1.l4` and `probe2.l4`); no encoding file, note or plan was opened.
