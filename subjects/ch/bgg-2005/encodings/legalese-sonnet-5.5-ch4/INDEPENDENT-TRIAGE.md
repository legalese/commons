# Independent test author's pass on chapter 4: the lead's note

**What this file is.** A separate agent read the chapter 4 text (and chapter 3 as context) and wrote the answers it expected before it opened the encoding (`INDEPENDENT-ANSWERS.md`), then wrote `bgg4-tests-independent.l4` and its own triage (below, unchanged).
As returned, it had 277 assertions: 259 satisfied and 18 failed; 6 scenarios could not be asked at all (gaps).

**What was done with the 18 failures.** Four were findings against the encoding, one was the reader's own scenario, and thirteen were readings the text allows both ways.
- The main finding was real: the Art 109(1) seam to chapter 3 never derived Art 74, and the seat question had no input to state it, so every civil appeal that turns on the value limit answered `NOTHING`.
  The encoder derived Art 74 in the seam, added seven inputs to the seat question, and recorded the answers and the corrected fork F26 (see "Independent reader (blind test), repairs" in `NOTES.md`).
- The Art 107(1) and Art 107(3) findings were repaired (new forks F33 and F34, with the other readings kept); the encoder's reasons are in the same section.
- The thirteen readings (the six case-by-case questions of the Guide's ruling of 2026-11-05, the grants ruling of 2026-11-12, and the encoder's forks F3, F24, F27 and F32) were NOT repaired.
  The reader's file was restated to the encoder's answer, each line carrying a `RECONCILED` comment that names both readings; they are listed in the triage as `AMBIGUOUS` and in the encoder's fork register.
  These are the places a lawyer should look first.
- Lines that call the Art 109(1) seat question were updated by the lead for its seven new inputs, and the two that call Art 107(1) for its removed input; the facts of those scenarios are unchanged, and each carries an `UPDATED` comment.

**Not covered by any test.** Six scenarios the reader wrote could not be asked of the encoding: which authority an appeal was filed with (Art 100(1)), the part of a decision not challenged (Art 103(2)), whether an award within the claims breaches Art 107(1), whether a full discussion is a short statement of reasons (Art 108(3), Art 109(3)), and a value-limit field in the seat's records (the repair above covers it through the Art 109(1) question only).

---

The reader's own triage follows, unchanged.

# Triage: BGG chapter 4 (Art 90 to 112), independent test pass

Run: `l4-main-110 run tests-independent.l4` from `enc/`, `JL4_LIBRARY_PATH` unset, diagnostics read: 277 assertions, 259 satisfied, 18 failed (`assertion failed`, Error), 0 refused (no `assertion refused`), no parse or type error.
Every failure has the encoding answering `NOTHING` where I expected `JUST TRUE` or `JUST FALSE` (I re-ran each failing expression as `#EVAL` in a scratch file, since deleted, to read the answer).
Line numbers are lines of `enc/tests-independent.l4`.
Verdict counts: ENCODER 4, SCENARIO 1, AMBIGUOUS 13, GAP 6.

Format: scenario | line | provision | my expected | encoding answered | verdict, then the reason.

## Failed assertions

1. #165 | 227 | Art 109(1) with Art 74 | JUST TRUE | NOTHING | ENCODER. A CHF 20,000 sales dispute (threshold CHF 30,000, Art 74(1)(b)) with no question of fundamental importance: Art 109(1) names "Art. 74 und 83-85", so the three-judge non-entry rule reaches it. The seam derives only Art 84(1), 84a and 85 (its own fork F26 says Art 74 is "NOT derived here ... the person states the condition in the chapter 4 question") but the seat question has no input to state it, so `Art 109(1) the condition on which the appeal is admissible, by chapters 3` returns `on neither of these conditions` for every civil case. The layer-1 function answers `JUST TRUE` when handed the condition (I probed it), so the gap is in the seam and the seat.
2. #W22 | 326 | Art 109(1) with Art 74, from the seat | JUST TRUE | NOTHING | ENCODER. Same cause as #165, in the person's words: "my CHF 20,000 sales dispute raises no question of fundamental importance".
3. #150b | 204 | Art 107(3), first and second sentence | JUST TRUE | NOTHING | ENCODER (minor). In an extradition appeal where the asylum application already has a final decision, the exception of the second sentence does not apply, so the Court is held to the 15 days. The function "Art 107(3) the Court is bound by the period of 15 days" answers `JUST FALSE` for the exception and `NOTHING` for everything else, so it never says "held". The layer-1 within-period function agrees with me (#150a passes). Arguable: the seat question has no "the Court considers the appeal inadmissible" input.
4. #139b | 290 | Art 107(1) | JUST FALSE | NOTHING | ENCODER (minor; added after reading the API, see ANSWERS.md section X). "May the Court go beyond the claims I made?" is answered NO by the text in every case (flat negative). The function answers `NOTHING` when the decision the Court would give does not go beyond the claims, so a person who asks the standing question gets "not covered" unless they say the decision would exceed.
5. #168 | 230 | Art 109(1) with Art 74(2)(b) | JUST FALSE | NOTHING | SCENARIO. My facts were a labour case at CHF 14,999 admissible only because a federal statute provides a single cantonal instance; the seat question cannot state that premise (no input for Art 74(2)(b), and none for employment or tenancy), so the assertion as written asks something else. My expected value also rested on ruling (b) where NOTHING is as defensible. I list the missing premise as the finding: see #165.
6. #167 | 229 | Art 109(1) with Art 74(1)(a) | JUST FALSE | NOTHING | AMBIGUOUS. Labour case at CHF 15,000: the threshold is met ("mindestens"), so the appeal is admissible whatever the question and Art 109(1) does not reach it. Two readings: a failed "wenn die Beschwerde nur unter einer dieser Bedingungen zulässig ist" is `JUST FALSE` (periods ruling (b)); the competence rule is a scope limit with no "only" and so `NOTHING` (ruling (c)). The seat cannot say "labour case" either (same seam gap as #165).
7. #W23 | 327 | Art 109(1), from the seat | JUST FALSE | NOTHING | AMBIGUOUS. Same as #167 in the person's words (CHF 15,000 employment dispute).
8. #172 | 234 | Art 109(1) with Art 85(1)(a) | JUST FALSE | NOTHING | AMBIGUOUS. State liability at CHF 30,000, admissible whatever the question: ruling (b) against ruling (c), as #167.
9. #173b | 236 | Art 109(1) with Art 85(1)(b) | JUST FALSE | NOTHING | AMBIGUOUS. Public-law employment at CHF 15,000: as #172.
10. #176 | 239 | Art 109(2)(a) | JUST FALSE | NOTHING | AMBIGUOUS. Manifestly unfounded appeal, two of three judges agree: "bei Einstimmigkeit" read as a "where" condition that fails (ruling (b)) against a competence grant whose gate failed (grants ruling, `NOTHING`).
11. #180 | 243 | Art 109(2)(b) | JUST FALSE | NOTHING | AMBIGUOUS. Same as #176 for upholding a manifestly well-founded appeal.
12. #24 | 49 | Art 93(3) | JUST FALSE | NOTHING | AMBIGUOUS. Interim decision that does not affect the content of the final decision: "soweit sie sich auf dessen Inhalt auswirken" read as "as long as" (NO) against a grant limited by its own wording (NOTHING). The encoding documents this as its fork F3.
13. #95 | 138 | Art 102(1) | JUST FALSE | NOTHING | AMBIGUOUS. Service not necessary: a duty whose "soweit erforderlich" is unmet, one of the six case-by-case questions.
14. #184 | 250 | Art 110 | JUST FALSE | NOTHING | AMBIGUOUS. The last cantonal court reviews the facts only for arbitrariness: a bare duty ("gewährleisten sie") not done; the encoding answers NOTHING (its fork F27), I answered NO.
15. #186 | 252 | Art 110 | JUST FALSE | NOTHING | AMBIGUOUS. Only an administrative authority reviewed the facts freely: as #184.
16. #188 | 256 | Art 111(1) | JUST FALSE | NOTHING | AMBIGUOUS. A person entitled to appeal could not take part as a party: "has the canton let the person" NO against NOTHING: a bare "muss" not done.
17. #195 | 263 | Art 111(3) | JUST FALSE | NOTHING | AMBIGUOUS. The immediate lower court cannot examine the fact-finding complaints: a bare "muss ... können" not done.
18. #207 | 277 | Art 112(2) | JUST FALSE | NOTHING | AMBIGUOUS. Neither federal nor cantonal law provides for notification without reasons: "Sofern" condition failed (ruling (b)) against the grants ruling (limb 3 says list it in the fork register); the encoding lists it as fork F24.

## Gaps: scenarios with no function to ask them

19. #89 | none | Art 100(1) | NOTHING (filed in time but with the cantonal court; the text has no forwarding rule) | no function | GAP. No input says which authority the appeal was filed with.
20. #113 | none | Art 103(2) | NO for the part of the decision not challenged ("im Umfang der Begehren") | no function | GAP. The encoding takes the extent of the claims as a yes or no (its fork F16) and has no input for the part not challenged.
21. #139 | none | Art 107(1) | NO (an award within the claims does not breach Art 107(1)) | no function | GAP. There is no "does it breach" function; the seat asks only whether the Court may go beyond (see #139b above).
22. #164b | none | Art 108(3) | NO (a full discussion of the merits is not a short statement of the ground) | no function | GAP. No input says what the reasons contain; the function answers YES for any decision of paragraph 1.
23. #182c | none | Art 109(3) | NO (a full extensive reasoning is not summary) | no function | GAP. As #164b.
24. #W21 | none | seat, seam to Art 74 | YES at CHF 15,000 employment and CHF 30,000 other, NO below | no function | GAP. The seat's three records (civil, criminal, public law) carry Art 72 or 78 or 82 and Art 76 or 81 or 89 but no value-limit field; the value limit is a chapter 3 subject and I asked it only from the seat.

## What passed and is worth a reader's trust (not a finding)

The count of every period and its edge days (30, 10, 5, 3, 15 days, the one month, the 30 days of Art 101 and Art 112(2)), the days-not-running input, the more specific five days over ten for bill-of-exchange enforcement, the Art 100(5) start-day cap, the "until" bar of Art 112(2) (barred before, lifted after, not "may be enforced"), the NOTHING answers for every silent case I wrote (ordinary cantonal law, new legal arguments, dismissed appeals, other authorities, the Federal Council's determination), and the seat's wiring to chapter 3 (R1 to R3, W25) all agree with my answers.
