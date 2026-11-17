# triage.md for g1 (dst-rev-aia1)

Test file: `enc/tests-independent.l4`.
Run: 444 assertions, 422 satisfied, 22 failed, 0 refused, 20 gaps (gaps are `-- GAP` comment lines, not assertions).
Scenario tags in the file are `S<n>` for the numbered scenarios of ANSWERS.md and `Sseat<n>` for its seat-layer scenarios S1 to S40.
"File line" is the line of the assertion (or GAP comment) in `enc/tests-independent.l4`.
"l." is a line of the consolidated text.
Expected values are mine from ANSWERS.md and were never edited to match the encoding.
Verdict tally: ENCODER 0, SCENARIO 4, AMBIGUOUS 18, GAP 20.

## Failed assertions

| scen | file line | provision (text line) | expected | encoding | verdict and the readings |
| --- | --- | --- | --- | --- | --- |
| S11 | 76 | Art 2(8) (l.52) | JUST TRUE | NOTHING | AMBIGUOUS: "testing in real world conditions shall not be covered by that exclusion" restores the Regulation (Y), or only withdraws the exclusion and leaves application to other provisions (NOTHING). I restated the question to "does the Regulation apply". |
| S14 | 79 | Art 2(12) (l.56) | JUST TRUE | NOTHING | AMBIGUOUS, "unless" once met (one of the six case-by-case questions): open-source exclusion lost so the Regulation applies (Y), or exclusion lifted and application rests elsewhere (NOTHING). |
| S14b | 80 | Art 2(12) (l.56), system falls under Art 5 | JUST TRUE | NOTHING | AMBIGUOUS, same two readings as S14. |
| S69 | 170 | Art 4a(1) (l.159) | JUST FALSE | NOTHING | SCENARIO: "To the extent strictly necessary" limits the grant in its own words, so a case outside the limit is NOTHING under the Guide (limits a grant in its own wording). My N misapplied it. |
| S166 | 308 | Art 6(3) (l.228-233) | NOTHING | JUST TRUE | AMBIGUOUS: Annex III system with none of (a) to (d) but "no significant risk": the conditions are required so it stays high-risk (the encoding's Y), or the first subparagraph stands alone so the derogation applies (N). My NOTHING fits neither reading and is the weakest; left unedited. |
| S172b | 317 | Art 6(7) (l.238) | NOTHING | JUST FALSE | SCENARIO: "where there is concrete and reliable evidence" is a "where" condition and ruling (b) gives JUST FALSE when it fails; I applied ruling (b) at S214b and not here. The encoding follows ruling (b). |
| S181b | 331 | Annex I Section B item 21 (l.1698), asked 2026-07-26 | NOTHING | JUST FALSE | AMBIGUOUS, "listed in Schedule N": the Annex as in force on that date lists no such item (N), or the list is not closed with "only" (NOTHING). |
| S182b | 333 | Annex I (l.1671-1698), GDPR | NOTHING | JUST FALSE | AMBIGUOUS, "listed in Schedule N": same two readings as S181b. |
| S183 | 334 | Annex I item 20 (l.1696), manned aircraft | NOTHING | JUST FALSE | AMBIGUOUS: "in so far as" unmanned aircraft closes the item (N), or it is a scope limit with no "only" (NOTHING). ANSWERS.md 183 already flagged this one. |
| S200 | 371 | Art 16(e) (l.383), logs not under provider's control | JUST FALSE | NOTHING | AMBIGUOUS, duty whose "where" is unmet: "when" counts as "where" under ruling (b) and (c) so N, or the duty is simply not triggered (NOTHING). |
| S201a | 372 | Art 16(k) (l.389), request not reasoned | JUST FALSE | NOTHING | AMBIGUOUS, same: "upon" counts as "where" (N) or duty not triggered (NOTHING). |
| S210c | 390 | Art 19(1) (l.424), five months, other law provides otherwise | JUST TRUE | NOTHING | AMBIGUOUS, "unless" once met: the six-month floor is displaced so the keeping is compliant (Y), or the paragraph then says nothing about compliance (NOTHING). |
| S211 | 391 | Art 19(1) (l.424), logs not under control | JUST FALSE | NOTHING | SCENARIO: "to the extent such logs are under their control" limits the duty in its own words, so outside it the Guide gives NOTHING; my N contradicts my own S241a. |
| S214b | 396 | Art 20(2) (l.429), no Art 79(1) risk | JUST FALSE | NOTHING | AMBIGUOUS, duty whose "where" is unmet: ruling (b) gives N, or duty not triggered (NOTHING). |
| S215b | 398 | Art 21(1) (l.432), request not reasoned | JUST FALSE | NOTHING | AMBIGUOUS, same as S201a. |
| S216b | 400 | Art 21(2) (l.433), logs not under control | JUST FALSE | NOTHING | SCENARIO, same error as S211. |
| S223b | 412 | Art 23(2) (l.454), no reason to consider | NOTHING | JUST FALSE | AMBIGUOUS, prohibition whose "where" is unmet: bar limited in its own wording (NOTHING), or "where" fails so N under ruling (b). |
| S229b | 422 | Art 24(2) (l.463), no reason to consider | NOTHING | JUST FALSE | AMBIGUOUS, same as S223b. |
| S231b | 426 | Art 24(5) (l.466), request not reasoned | JUST FALSE | NOTHING | AMBIGUOUS, same as S201a. |
| S236a | 434 | Art 25(2) last subparagraph (l.481) | JUST FALSE | NOTHING | AMBIGUOUS: "This paragraph shall not apply in cases where the initial provider has clearly specified" is a flat negative (N), or an exception once met that leaves the duty untriggered (NOTHING). |
| S238b | 440 | Art 25(4) (l.487), free and open-source tool | JUST FALSE | NOTHING | AMBIGUOUS: "This paragraph shall not apply to third parties making accessible ... tools" is a flat negative (N), or an exception once met (NOTHING). |
| S245c | 454 | Art 26(6) (l.499), five months, other law provides otherwise | JUST TRUE | NOTHING | AMBIGUOUS, "unless" once met: same two readings as S210c. |

## Gaps (a scenario I could not ask of the encoding)

| scen | file line | provision (text line) | what I could not ask |
| --- | --- | --- | --- |
| S41c | 122 | Art 3(14a) (l.82) | "a company of 120 employees: NC" cannot be asked, SME status is an input. |
| S55 | 151 | Art 3(37) (l.124) | "is health data a special category? NC" cannot be asked, it is an input. |
| S56 | 152 | Art 3(52) (l.139) | "is customer scoring profiling? NC" cannot be asked, it is an input. |
| S90 | 177 | Art 10(5) deleted (l.305-306) | no function answers "may a provider process special categories under Article 10(5)" on a date. |
| S79b | 189 | Art 9(3) (l.276) | "a risk that cannot be mitigated is outside the system" cannot be asked, the sentence is one input. |
| S156 | 295 | Art 5(5) (l.209) | 30-day Member State deadline: day 30 in time, day 31 late, cannot be asserted, the duty has no deadline input. |
| S170 | 315 | Art 6(5) (l.236) | Commission guidelines deadline of 2 Feb 2026 exists only as a DEONTIC duty with no deadline input. |
| S184b | 336 | Annex II (l.1702-1718) | "tax fraud is not listed: NC", the function is BOOLEAN and has no NOTHING answer ("listed in Schedule N" is case by case). |
| S187c | 343 | Annex III 2 (l.1727) | "billing optimiser, not a safety component: NC", BOOLEAN function. |
| S188c | 346 | Annex III 3 (l.1728-1732) | "a timetabling system: NC", BOOLEAN function. |
| S189c | 349 | Annex III 4 (l.1733-1735) | "a payroll calculator with no decisions: NC", BOOLEAN function. |
| S190b | 351 | Annex III 5(a) (l.1737) | "private charity with no public mandate: NC", BOOLEAN function. |
| S193c | 358 | Annex III 6(a) (l.1742) | "private company with no law-enforcement mandate: NC", BOOLEAN function. |
| S196 | 365 | Annex III (l.1719-1754) | count of areas (8) and use cases (25) cannot be asked. |
| S208 | 387 | Art 18(1)(a) to (e) (l.415-419) | count of five documents cannot be asked, the function takes a record. |
| S220 | 406 | Art 22(3)(b) (l.441) | the 10-year retention by the authorised representative has no function with a date. |
| S248 | 461 | Art 26(10) (l.504) | 47, 48 and 49 hours cannot be asked, the 48-hour limit is one yes/no input. |
| S249 | 462 | Art 26(10) (l.504) | "initial identification: authorisation needed? N" cannot be asked, the function asks whether the deployer has requested one. |
| seat16 | 525 | Art 6(1) (l.219-221) | the P1 importer seat has only Article 5 questions, so "importer of a lift with an AI safety component" cannot be asked from that seat. |
| seat24 | 526 | Art 9 (l.270) | the P2 GPAI seat has only Article 4a questions, so "is a GPAI provider bound by Art 9" cannot be asked from that seat. |

## Notes for the reviewer

- Site-by-site inconsistency on an unmet "where": the encoding answers JUST FALSE at Art 6(7), Art 23(2) and Art 24(2), and NOTHING at Art 16(e), Art 16(k), Art 20(2), Art 21(1) and Art 24(5). Each is a case-by-case site, so I marked them AMBIGUOUS, but the literal words of ruling (b) and (c) ("when", "upon" count as "where"; unmet gives JUST FALSE) would make the NOTHING sites ENCODER findings if the reviewer rules that ruling (b) governs duties.
- I restated the question to fit the encoding's function in 11 assertions (comments say "question restated"); the restated question is the one a reviewer should check against the text, since it is mine and not the encoding's.
- 0 ENCODER findings does not show the encoding is right everywhere: 20 gaps are questions the encoding cannot answer, and 40 seat assertions plus 404 part assertions pass on facts I chose.
