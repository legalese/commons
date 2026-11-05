# NOTES -- mlr4: regulations 65 to 110 and Schedules 1, 2, 3 and 3AZA of the Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (SI 2017/692)

Status (2026-11-05, checked): this file describes files that exist in this folder and have been run.
Modules, tests and seat layer pass `check.sh` on build 1.6.109 and on the main build 1.6.108 with the same counts (the output is at the end of this file); `srcrefs.py check --refs` and `--strict` report 0 problems on every module.
The coverage and marginal-reading tables are generated from the text and from the modules' own comments by a script, not typed; the fork register, the jural-relations table and the findings are judgement and were checked against the text lines they cite.
The text encoded is lines 2200 to 3054 of `uksi-2017-692.txt`, a converter-script rendering of the Regulations, not the official text.
The brief governs where it differs from PLAN.md; the differences are under `## Where this brief governs over PLAN.md`.

Files (all in this folder):
`mlr4-part8.l4` (regulations 65 to 74C), `mlr4-part9.l4` (75 to 92), `mlr4-part10.l4` (93 to 100), `mlr4-part11.l4` (101 to 110), `mlr4-schedules.l4` (Schedules 1, 2, 3 and 3AZA);
`mlr4-tests-part8.l4`, `mlr4-tests-part9.l4`, `mlr4-tests-part10.l4`, `mlr4-tests-part11.l4`, `mlr4-tests-schedules.l4`;
`mlr4-seat.l4` and `mlr4-cases-seat.l4` (the seat layer: a business that is a relevant person, and its compliance officer; every question is named "Under regulation N, ..." or "Under schedule N, ...", has `@export` and `@desc`, takes plain inputs and calls layer 1; there is no seat for an official);
`NOTES.md`, `PROGRESS.md`, and the supplied `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` and the read-only `mlr-core.l4`.
No `NEEDS-CORE.md`: nothing in the core had to be extended; a constructor this range needed lives under this part's own prefix.

## Coverage (mlr4)

Every non-blank line of lines 2200 to 3054 falls in some row below: 855 non-blank lines, 827 rows (one per section, subsection, paragraph, sub-paragraph, defined term, defined-term limb, schedule item and heading), checked by a script that fails if a line belongs to no row or an encoded row has no declaration citing it.
Each row has exactly one disposition.

| disposition | rows |
|---|---|
| encoded | 661 |
| fork (the row points at the fork-register entry) | 101 |
| inert, reason 1 (a heading; nothing else is inert) | 61 |
| repealed or blank in this text | 4 |
| total | 827 |

Fork rows by entry: F-101-OFFICER 1, F-3AZA-INCLUDING 1, F-3AZA-NUMBERS 3, F-69-1 5, F-69-2 1, F-72-1 1, F-77-4 1, F-77-79 2, F-86-FINE 8, F-ARRANGEMENTS 8, F-CHAPEAU 9, F-OFFICER 5, F-PERIOD 13, F-SCH3-36 5, F-SCH3-NUMBERS 41, F-WHEN 5.

**Audit counts.** Text units counted by the extractor: 827.
Rows in the table before the audit: 827; after: 827.
The audit found ten Schedule 2 rows (the items other than 1, 3 and 6) that no `@ref` reached, because the activities are constructors of the core's `Listed activity`; `sch 2 the activity is a listed activity` now cites them and a test exercises each.
A second audit found 70 constructors of this range's own tables (regulations 77(2), 81(1), 83(1), 102(1), 103(1), 110(5) and Schedule 3) that no test used; each now has an assertion.
All 364 decision functions are used by at least one assertion, and all 99 seat questions by at least one case.

**The four blank rows.** Lines 2249 (regulation 67(5)), 2265 (regulation 69(1)(b)(i)), 2462 (regulation 76(6)(a)) and 2650 (regulation 86(2)(a)) print a line of dots where a paragraph was omitted by amendment.
The text shows nothing to encode, and the surrounding paragraphs are encoded as printed.

**The inert rows.** All 61 are headings, inert for reason 1: 4 PARTs, 5 CHAPTERs, 2 SCHEDULEs, 50 regulation title lines (61 in all).
The headings of Schedules 1 and 2 are encoded rows instead, because the quotation each declaration cites begins at its heading line.
No row of this range is inert for reason 2 or 3; regulations 104A, 108, 109 and 110(1) look like machinery but have rules that bear on a person or a date, so they are encoded.

**Reading the table.** `unit` is the structural unit (a defined term's limbs are their own rows); `lines` are lines of the raw text; the last column names up to three L4 declarations whose `@ref` locators reach the unit, with the number of further ones.
A unit under a fork also names the entry in the fork register.

| unit | lines | disposition | L4 name |
|---|---|---|---|
| PART 8 | 2200 | inert (reason 1: a heading) | no rule: a heading |
| reg 65 heading | 2201 | inert (reason 1: a heading) | no rule: a heading |
| reg 65(1) | 2202 | encoded | `reg 65(1) tribunal` |
| reg 65(1) “premises” | 2203 | encoded | `reg 65(1) tribunal`, `reg 65(1) the place is premises` |
| reg 65(1) “tribunal” | 2204 | encoded | `reg 65(1) tribunal`, `reg 65(1) the tribunal for the purposes of Part 8 is` (gap: the definition (line 2204) reads "the First-tier Tribunal or, where determined by or under Tribunal Procedure Rules, the Upper Tribunal", and the type `reg 65(1) tribunal` has those two constructors; the High Court appears in this range only in regulation 72 (lines 2346, 2350, 2352) and regulation 80(4) (line 2526), never as "the tribunal", so no constructor for it was added) |
| reg 65(2) | 2205 | encoded | `reg 65(2) person` |
| reg 65(2) “officer” | 2206 | fork F-OFFICER | `reg 65(2) person`, `reg 65(2) the person is an officer` |
| reg 65(2) “officer” limb | 2207 | fork F-OFFICER | `reg 65(2) person`, `reg 65(2) the person is an officer` |
| reg 65(2) “officer” limb | 2208 | fork F-OFFICER | `reg 65(2) person`, `reg 65(2) the person is an officer` |
| reg 65(2) “officer” limb | 2209 | fork F-OFFICER | `reg 65(2) person`, `reg 65(2) the person is an officer` |
| reg 65(2) “officer” limb | 2210 | fork F-OFFICER | `reg 65(2) person`, `reg 65(2) the person is an officer` |
| reg 65(2) “relevant officer” | 2211 | fork F-ARRANGEMENTS | `reg 65(2) person`, `reg 65(2) the person is a relevant officer` |
| reg 65(2) “relevant officer” limb | 2212 | fork F-ARRANGEMENTS | `reg 65(2) person`, `reg 65(2) the person is a relevant officer` |
| reg 65(2) “relevant officer” limb | 2213 | fork F-ARRANGEMENTS | `reg 65(2) person`, `reg 65(2) the person is a relevant officer` |
| reg 65(2) “relevant officer” limb | 2214 | fork F-ARRANGEMENTS | `reg 65(2) person`, `reg 65(2) the person is a relevant officer` |
| reg 65(3) | 2215 | encoded | `reg 65(3) the person is a connected person` |
| reg 66 heading | 2216 | inert (reason 1: a heading) | no rule: a heading |
| reg 66(1) | 2217 | encoded | `reg 66(1) what the notice requires`, `reg 66(1) the body is a supervisory authority`, `reg 66(1) the supervisory authority may require P` |
| reg 66(1)(a) | 2218 | encoded | `reg 66(1) what the notice requires`, `reg 66(1) the supervisory authority may require P` |
| reg 66(1)(b) | 2219 | encoded | `reg 66(1) what the notice requires`, `reg 66(1) the supervisory authority may require P` |
| reg 66(1)(c) | 2220 | encoded | `reg 66(1) what the notice requires`, `reg 66(1) the supervisory authority may require P` |
| reg 66(1A) | 2221 | encoded | `reg 66(1A) the power in paragraph (1) includes requiring the information` |
| reg 66(2) | 2222 | encoded | `reg 66(2)(a) the information or documents were provided or produced in time`, `reg 66 the person has failed to comply with a requirement of a notice given under regulation 66` |
| reg 66(2)(a) | 2223 | encoded | `reg 66(2)(a) the information or documents were provided or produced in time`, `reg 66(2)(a) P must provide the information or produce the documents`, `reg 66 the person has failed to comply with a requirement of a notice given under regulation 66` |
| reg 66(2)(b) | 2224 | encoded | `reg 66(2)(a) the information or documents were provided or produced in time`, `reg 66(2)(b) the information or documents were provided or produced at the specified place`, `reg 66 the person has failed to comply with a requirement of a notice given under regulation 66` |
| reg 66(3) | 2225 | encoded | `reg 66(3) what the officer requires`, `reg 66(3) the officer may require P`, `reg 66(3) P provided or produced without unreasonable delay (+1 more)` |
| reg 66(3)(a) | 2226 | encoded | `reg 66(3) what the officer requires`, `reg 66(3) the officer may require P`, `reg 66 the person has failed to comply with a requirement of a notice given under regulation 66` |
| reg 66(3)(b) | 2227 | encoded | `reg 66(3) what the officer requires`, `reg 66(3) the officer may require P`, `reg 66 the person has failed to comply with a requirement of a notice given under regulation 66` |
| reg 66(4) | 2228 | encoded | `reg 66(3) the officer may require P`, `reg 66(4) the powers in regulation 66 may be exercised`, `reg 66(4) and 67(1) the information or documents may be required under regulation 66` |
| reg 66(5) | 2229 | encoded | `reg 66(5) the duty to set out the reasons arises`, `reg 66(5) the notice complies with the requirement to set out the reasons` |
| reg 66(6) | 2230 | encoded | `reg 66(6)(a) the supervisory authority may require the information to be produced in legible form` |
| reg 66(6)(a) | 2231 | encoded | `reg 66(6)(a) the supervisory authority may require the information to be produced in legible form` |
| reg 66(6)(b) | 2232 | encoded | `reg 66(6)(a) the supervisory authority may require the information to be produced in legible form`, `reg 66(6)(b) the supervisory authority may require the information to be provided in the form` |
| reg 66(7) | 2233 | encoded | `reg 66(7) the production of the document affects a lien on it` |
| reg 66(8) | 2234 | encoded | `reg 66(8) the supervisory authority may exercise the power in relation to the third person` |
| reg 66(9) | 2235 | encoded | `reg 66(9) suspicious activity disclosure is given by` |
| reg 67 heading | 2236 | inert (reason 1: a heading) | no rule: a heading |
| reg 67(1) | 2237 | encoded | `reg 67(1) the supervisory authority may exercise the power in regulation 66 to meet the request`, `reg 66(4) and 67(1) the information or documents may be required under regulation 66` |
| reg 67(2) | 2238 | encoded | `reg 67(2) paragraph (2) applies to the request` |
| reg 67(2)(a) | 2239 | encoded | `reg 67(2) paragraph (2) applies to the request` |
| reg 67(2)(b) | 2240 | encoded | `reg 67(2) paragraph (2) applies to the request` |
| reg 67(2)(c) | 2241 | encoded | `reg 67(2) paragraph (2) applies to the request` |
| reg 67(3) | 2242 | encoded | `reg 67(3) matter`, `reg 67(3) the supervisory authority may take the matter into account` |
| reg 67(3)(a) | 2243 | encoded | `reg 67(3) matter`, `reg 67(3) the supervisory authority may take the matter into account` |
| reg 67(3)(b) | 2244 | encoded | `reg 67(3) matter`, `reg 67(3) the supervisory authority may take the matter into account` |
| reg 67(3)(c) | 2245 | encoded | `reg 67(3) matter`, `reg 67(3) the supervisory authority may take the matter into account` |
| reg 67(4) | 2246 | encoded | `reg 67(4) the supervisory authority may decide not to exercise its powers` |
| reg 67(4)(a) | 2247 | encoded | `reg 67(4) the supervisory authority may decide not to exercise its powers` |
| reg 67(4)(b) | 2248 | encoded | `reg 67(4) the supervisory authority may decide not to exercise its powers` |
| reg 67(5) | 2249 | repealed or blank in this text | the text shows the paragraph is shown as `. . . .` (omitted by amendment) |
| reg 67(6) | 2250 | encoded | `reg 67(6) the authority is a foreign authority` |
| reg 68 heading | 2251 | inert (reason 1: a heading) | no rule: a heading |
| reg 68(1) | 2252 | encoded | `reg 68(1) this regulation applies` |
| reg 68(1)(a) | 2253 | encoded | `reg 68(1) this regulation applies` |
| reg 68(1)(b) | 2254 | encoded | `reg 68(1) this regulation applies` |
| reg 68(2) | 2255 | fork F-CHAPEAU | `reg 68(2) the supervisory authority may request the assistance of the foreign authority` |
| reg 68(3) | 2256 | encoded | `reg 68(3) the use made of the information or documents is permitted` |
| reg 68(3)(a) | 2257 | encoded | `reg 68(3) the use made of the information or documents is permitted` |
| reg 68(3)(b) | 2258 | encoded | `reg 68(3) the use made of the information or documents is permitted` |
| reg 68(4) | 2259 | encoded | `reg 68(4) paragraph (3) applies` |
| reg 68(5) | 2260 | encoded | `reg 68(5) foreign authority is given by` |
| reg 69 heading | 2261 | inert (reason 1: a heading) | no rule: a heading |
| reg 69(1) | 2262 | fork F-69-1 | `reg 69(1) paragraph (2) applies` |
| reg 69(1)(a) | 2263 | fork F-69-1 | `reg 69(1) paragraph (2) applies` |
| reg 69(1)(b) | 2264 | fork F-69-1 | `reg 69(1) paragraph (2) applies` |
| reg 69(1)(b)(i) | 2265 | repealed or blank in this text | the text shows the sub-paragraph is shown as `. . . .` (omitted by amendment) |
| reg 69(1)(b)(ii) | 2266 | fork F-69-1 | `reg 69(1) paragraph (2) applies` |
| reg 69(1)(b)(iii) | 2267 | fork F-69-1 | `reg 69(1) paragraph (2) applies` |
| reg 69(2) | 2268 | fork F-69-2 F-CHAPEAU | `reg 69(2) power`, `reg 69(2) the officer may` |
| reg 69(2)(a) | 2269 | encoded | `reg 69(2) power`, `reg 69(2) the officer may` |
| reg 69(2)(b) | 2270 | encoded | `reg 69(2) power`, `reg 69(2) the officer may` |
| reg 69(2)(c) | 2271 | encoded | `reg 69(2) power`, `reg 69(2) the officer may` |
| reg 69(2)(d) | 2272 | encoded | `reg 69(2) power`, `reg 69(2) the officer may` |
| reg 69(2)(e) | 2273 | encoded | `reg 69(2) power`, `reg 69(2) the officer may` |
| reg 69(2)(f) | 2274 | encoded | `reg 69(2) power`, `reg 69(2) the officer may` |
| reg 69(3) | 2275 | fork F-CHAPEAU | `reg 69(3) the officer may take copies of, or make extracts from, the documents` |
| reg 69(4) | 2276 | encoded | `reg 69(4) the person is a duly authorised officer` |
| reg 69(4)(a) | 2277 | encoded | `reg 69(4) the person is a duly authorised officer` |
| reg 69(4)(b) | 2278 | encoded | `reg 69(4) the person is a duly authorised officer` |
| reg 70 heading | 2279 | inert (reason 1: a heading) | no rule: a heading |
| reg 70(1) | 2280 | encoded | `reg 70(1) the justice may issue a warrant` |
| reg 70(1)(a) | 2281 | encoded | `reg 70(1) the justice may issue a warrant` |
| reg 70(1)(b) | 2282 | encoded | `reg 70(1) the justice may issue a warrant` |
| reg 70(2) | 2283 | encoded | `reg 70(2) the application meets the requirements` |
| reg 70(2)(a) | 2284 | encoded | `reg 70(2) the application meets the requirements` |
| reg 70(2)(b) | 2285 | encoded | `reg 70(2) the application meets the requirements` |
| reg 70(2)(c) | 2286 | encoded | `reg 70(2) the application meets the requirements` |
| reg 70(2)(c)(i) | 2287 | encoded | `reg 70(2) the application meets the requirements` |
| reg 70(2)(c)(ii) | 2288 | encoded | `reg 70(2) the application meets the requirements` |
| reg 70(2)(d) | 2289 | encoded | `reg 70(2) the application meets the requirements` |
| reg 70(3) | 2290 | encoded | `reg 70(3) the first set of conditions is satisfied` |
| reg 70(3)(a) | 2291 | encoded | `reg 70(3) the first set of conditions is satisfied` |
| reg 70(3)(b) | 2292 | encoded | `reg 70(3) the first set of conditions is satisfied` |
| reg 70(3)(b)(i) | 2293 | encoded | `reg 70(3) the first set of conditions is satisfied` |
| reg 70(3)(b)(ii) | 2294 | encoded | `reg 70(3) the first set of conditions is satisfied` |
| reg 70(4) | 2295 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(4)(a) | 2296 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(4)(a)(i) | 2297 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(4)(a)(ii) | 2298 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(4)(a)(iii) | 2299 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(4)(b) | 2300 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(4)(c) | 2301 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(4)(c)(i) | 2302 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(4)(c)(ii) | 2303 | encoded | `reg 70(4) the second set of conditions is satisfied` |
| reg 70(5) | 2304 | encoded | `reg 70(5) the third set of conditions is satisfied` |
| reg 70(5)(a) | 2305 | encoded | `reg 70(5) the third set of conditions is satisfied` |
| reg 70(5)(b) | 2306 | encoded | `reg 70(5) the third set of conditions is satisfied` |
| reg 70(6) | 2307 | encoded | `reg 70(6) the fourth set of conditions is satisfied` |
| reg 70(6)(a) | 2308 | encoded | `reg 70(6) the fourth set of conditions is satisfied` |
| reg 70(6)(b) | 2309 | encoded | `reg 70(6) the fourth set of conditions is satisfied` |
| reg 70(7) | 2310 | encoded | `reg 70(7) authority`, `reg 70(7) the warrant authorises the executing officer` |
| reg 70(7)(a) | 2311 | encoded | `reg 70(7) authority`, `reg 70(7) the warrant authorises the executing officer` |
| reg 70(7)(b) | 2312 | encoded | `reg 70(7) authority`, `reg 70(7) the warrant authorises the executing officer` |
| reg 70(7)(c) | 2313 | encoded | `reg 70(7) authority`, `reg 70(7) the warrant authorises the executing officer` |
| reg 70(7)(d) | 2314 | encoded | `reg 70(7) authority`, `reg 70(7) the warrant authorises the executing officer` |
| reg 70(7)(e) | 2315 | encoded | `reg 70(7) authority`, `reg 70(7) the warrant authorises the executing officer` |
| reg 70(7)(f) | 2316 | encoded | `reg 70(7) authority`, `reg 70(7) the warrant authorises the executing officer` |
| reg 70(8) | 2317 | encoded | `reg 70(8) the warrant authorises the executing officer to take possession of the information in legible form` |
| reg 70(9) | 2318 | encoded | `reg 70(9) feature`, `reg 70(9) a warrant may have the feature` |
| reg 70(9)(a) | 2319 | encoded | `reg 70(9) feature`, `reg 70(9) a warrant may have the feature` |
| reg 70(9)(b) | 2320 | encoded | `reg 70(9) feature`, `reg 70(9) a warrant may have the feature` |
| reg 70(9)(c) | 2321 | encoded | `reg 70(9) feature`, `reg 70(9) a warrant may have the feature` |
| reg 70(10) | 2322 | encoded | `reg 70(10) the accompanying person may exercise the powers in paragraph (7)` |
| reg 70(11) | 2323 | encoded | `reg 70(11) sections 15(5) to (8) and 16(3) to (12) of the Police and Criminal Evidence Act 1984 apply to the warrant` |
| reg 70(12) | 2324 | encoded | `reg 70(12) Articles 17(5) to (8) and 18(3) to (12) of the Police and Criminal Evidence (Northern Ireland) Order 1989 apply to the warrant` |
| reg 70(13) | 2325 | encoded | `reg 70(13) the person is a justice` |
| reg 70(13) “duly authorised officer” | 2326 | encoded | `reg 70(13) the person is a justice`, `reg 70(13) the person is a duly authorised officer` |
| reg 70(13) “duly authorised officer” limb | 2327 | encoded | `reg 70(13) the person is a justice`, `reg 70(13) the person is a duly authorised officer` |
| reg 70(13) “duly authorised officer” limb | 2328 | encoded | `reg 70(13) the person is a justice`, `reg 70(13) the person is a duly authorised officer` |
| reg 70(13) “executing officer” | 2329 | encoded | `reg 70(13) the person is a justice`, `reg 70(13) the person is an executing officer` |
| reg 70(13) “executing officer” limb | 2330 | encoded | `reg 70(13) the person is a justice`, `reg 70(13) the person is an executing officer` |
| reg 70(13) “executing officer” limb | 2331 | encoded | `reg 70(13) the person is a justice`, `reg 70(13) the person is an executing officer` |
| reg 70(13) “justice” | 2332 | encoded | `reg 70(13) the person is a justice` |
| reg 70(13) “justice” limb | 2333 | encoded | `reg 70(13) the person is a justice` |
| reg 70(13) “justice” limb | 2334 | encoded | `reg 70(13) the person is a justice` |
| reg 70(13) “justice” limb | 2335 | encoded | `reg 70(13) the person is a justice` |
| reg 71 heading | 2336 | inert (reason 1: a heading) | no rule: a heading |
| reg 71(1) | 2337 | encoded | `reg 71(1) the seized material may be retained` |
| reg 71(2) | 2338 | encoded | `reg 71(2) the seized material may be retained until the proceedings are concluded` |
| reg 71(2)(a) | 2339 | encoded | `reg 71(2) the seized material may be retained until the proceedings are concluded` |
| reg 71(2)(b) | 2340-2341 | encoded | `reg 71(2) the seized material may be retained until the proceedings are concluded` |
| reg 71(3) | 2342 | encoded | `reg 71(3) court`, `reg 71(3) the person may apply for delivery to` |
| reg 71(4) | 2343 | encoded | `reg 71(4) the court may make such order as it thinks fit` |
| reg 71(5) | 2344 | encoded | `reg 71(5) the order affects the right to take legal proceedings against the person in possession for the recovery of the material` |
| reg 72 heading | 2345 | inert (reason 1: a heading) | no rule: a heading |
| reg 72(1) | 2346 | fork F-72-1 | `reg 72(1) the person may be required` |
| reg 72(2) | 2347 | encoded | `reg 72(2) providing the information breaches a restriction on the disclosure of information` |
| reg 72(3) | 2348 | encoded | `reg 72(3) civil liability arises in respect of the disclosure` |
| reg 72(4) | 2349 | encoded | `reg 72(4) the warrant confers the right to seize the material` |
| reg 72(5) | 2350 | encoded | `reg 72(5) the material is privileged material` |
| reg 72(6) | 2351 | encoded | `reg 72(6) court`, `reg 72(6)(a) the court whose proceedings are referred to in paragraphs (1) and (5)`, `reg 72(6)(b) the person is entitled to refuse on the grounds of confidentiality of communication` |
| reg 72(6)(a) | 2352 | encoded | `reg 72(6) court`, `reg 72(6)(a) the court whose proceedings are referred to in paragraphs (1) and (5)` |
| reg 72(6)(b) | 2353 | encoded | `reg 72(6) court`, `reg 72(6)(b) the person is entitled to refuse on the grounds of confidentiality of communication` |
| reg 72(6)(b)(i) | 2354 | encoded | `reg 72(6) court`, `reg 72(6)(b) the person is entitled to refuse on the grounds of confidentiality of communication` |
| reg 72(6)(b)(ii) | 2355 | encoded | `reg 72(6) court`, `reg 72(6)(b) the person is entitled to refuse on the grounds of confidentiality of communication` |
| reg 72(7) | 2356 | encoded | `reg 72(7) the material is excluded material` |
| reg 72(7)(a) | 2357 | encoded | `reg 72(7) the material is excluded material` |
| reg 72(7)(b) | 2358 | encoded | `reg 72(7) the material is excluded material` |
| reg 73 heading | 2359 | inert (reason 1: a heading) | no rule: a heading |
| reg 73(1) | 2360 | encoded | `reg 73(1) the statement may be used in evidence against the person in criminal proceedings`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(2) | 2361 | encoded | `reg 73(2) case`, `reg 73(2) paragraph (1) applies`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(2)(a) | 2362 | encoded | `reg 73(2) case`, `reg 73(2) paragraph (1) applies`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(2)(b) | 2363 | encoded | `reg 73(2) case`, `reg 73(2) paragraph (1) applies`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(2)(c) | 2364 | encoded | `reg 73(2) case`, `reg 73(2) paragraph (1) applies`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(2)(d) | 2365 | encoded | `reg 73(2) case`, `reg 73(2) paragraph (1) applies`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(2)(e) | 2366 | encoded | `reg 73(2) case`, `reg 73(2) paragraph (1) applies`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(2)(f) | 2367 | encoded | `reg 73(2) case`, `reg 73(2) paragraph (1) applies`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(3) | 2368 | encoded | `reg 73(3) the statement may be used by virtue of paragraph (2)(f)`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(3)(a) | 2369 | encoded | `reg 73(3) the statement may be used by virtue of paragraph (2)(f)`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 73(3)(b) | 2370-2371 | encoded | `reg 73(3) the statement may be used by virtue of paragraph (2)(f)`, `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` |
| reg 74 heading | 2372 | inert (reason 1: a heading) | no rule: a heading |
| reg 74(1) | 2373 | encoded | `reg 74(1) R may exercise powers under this Part` |
| reg 74(1)(a) | 2374 | encoded | `reg 74(1) R may exercise powers under this Part` |
| reg 74(1)(b) | 2375 | encoded | `reg 74(1) R may exercise powers under this Part` |
| reg 74(2) | 2376 | encoded | `reg 74(2)(a) anything done by R is treated as done by an officer of the FCA` |
| reg 74(2)(a) | 2377 | encoded | `reg 74(2)(a) anything done by R is treated as done by an officer of the FCA` |
| reg 74(2)(b) | 2378 | encoded | `reg 74(2)(a) anything done by R is treated as done by an officer of the FCA`, `reg 74(2)(b) anything done by R is treated as done by an officer of Revenue and Customs` |
| reg 74(3) | 2379 | encoded | `reg 74(3) paragraph (2) applies` |
| reg 74(4) | 2380 | encoded | `reg 74(4) R must not disclose the information`, `reg 74(4) party`, `reg 74(4) the prohibition on R` |
| reg 74(4)(a) | 2381 | encoded | `reg 74(4) R must not disclose the information`, `reg 74(4) party` |
| reg 74(4)(b) | 2382 | encoded | `reg 74(4) R must not disclose the information`, `reg 74(4) party` |
| reg 74A heading | 2383 | inert (reason 1: a heading) | no rule: a heading |
| reg 74A(1) | 2384 | encoded | `reg 74A(1) the cryptoasset business must provide the information to the FCA` |
| reg 74A(1)(a) | 2385 | encoded | `reg 74A(1) the cryptoasset business must provide the information to the FCA` |
| reg 74A(1)(b) | 2386 | encoded | `reg 74A(1) the cryptoasset business must provide the information to the FCA` |
| reg 74A(1)(c) | 2387 | encoded | `reg 74A(1) the cryptoasset business must provide the information to the FCA` |
| reg 74A(2) | 2388 | encoded | `reg 74A(2) the information was provided as the FCA directed` |
| reg 74B heading | 2389 | inert (reason 1: a heading) | no rule: a heading |
| reg 74B(1) | 2390 | encoded | `reg 74B(1) this regulation applies` |
| reg 74B(2) | 2391 | fork F-CHAPEAU | `reg 74B(2) step`, `reg 74B(2) the FCA may take the step` |
| reg 74B(2)(a) | 2392 | encoded | `reg 74B(2) step`, `reg 74B(2) the FCA may take the step` |
| reg 74B(2)(b) | 2393 | encoded | `reg 74B(2) step`, `reg 74B(2) the FCA may take the step`, `reg 74B(2)(b) the fee payable by the relevant person is` |
| reg 74B(3) | 2394 | fork F-WHEN | `reg 74B(3) requirement`, `reg 74B(3) the FCA may require` |
| reg 74B(3)(a) | 2395 | encoded | `reg 74B(3) requirement`, `reg 74B(3) the FCA may require` |
| reg 74B(3)(b) | 2396 | encoded | `reg 74B(3) requirement`, `reg 74B(3) the FCA may require` |
| reg 74B(4) | 2397 | encoded | `reg 74B(4) the FCA gave notice in writing of the appointment` |
| reg 74B(5) | 2398 | encoded | `reg 74B(5) the person is a skilled person` |
| reg 74B(5)(a) | 2399 | encoded | `reg 74B(5) the person is a skilled person` |
| reg 74B(5)(b) | 2400 | encoded | `reg 74B(5) the person is a skilled person` |
| reg 74B(6) | 2401 | encoded | `reg 74B(6) the person gave the skilled person the assistance` |
| reg 74C heading | 2402 | inert (reason 1: a heading) | no rule: a heading |
| reg 74C(1) | 2403 | encoded | `reg 74C(1) the FCA may exercise its powers of direction` |
| reg 74C(2) | 2404 | encoded | `reg 74C(2) time`, `reg 74C(2) a direction may be imposed at the time` |
| reg 74C(3) | 2405 | encoded | `reg 74C(3) purpose`, `reg 74C(3) a direction may be imposed for the purpose` |
| reg 74C(3)(a) | 2406 | encoded | `reg 74C(3) purpose`, `reg 74C(3) a direction may be imposed for the purpose` |
| reg 74C(3)(b) | 2407 | encoded | `reg 74C(3) purpose`, `reg 74C(3) a direction may be imposed for the purpose` |
| reg 74C(3)(c) | 2408 | encoded | `reg 74C(3) purpose`, `reg 74C(3) a direction may be imposed for the purpose` |
| reg 74C(4) | 2409 | encoded | `reg 74C(4) content`, `reg 74C(4) a direction may have the content` |
| reg 74C(5) | 2410 | encoded | `reg 74C(5) act`, `reg 74C(5) the FCA may on its own initiative` |
| reg 74C(5)(a) | 2411 | encoded | `reg 74C(5) act`, `reg 74C(5) the FCA may on its own initiative` |
| reg 74C(5)(b) | 2412 | encoded | `reg 74C(5) act`, `reg 74C(5) the FCA may on its own initiative` |
| reg 74C(5)(c) | 2413 | encoded | `reg 74C(5) act`, `reg 74C(5) the FCA may on its own initiative` |
| reg 74C(6) | 2414 | encoded | `reg 74C(6) act`, `reg 74C(6) the FCA may on the request of the cryptoasset business` |
| reg 74C(6)(a) | 2415 | encoded | `reg 74C(6) act`, `reg 74C(6) the FCA may on the request of the cryptoasset business` |
| reg 74C(6)(b) | 2416 | encoded | `reg 74C(6) act`, `reg 74C(6) the FCA may on the request of the cryptoasset business` |
| reg 74C(6)(c) | 2417 | encoded | `reg 74C(6) act`, `reg 74C(6) the FCA may on the request of the cryptoasset business` |
| reg 74C(7) | 2418 | encoded | `reg 74C(7) the FCA consulted the PRA as required` |
| reg 74C(7)(a) | 2419 | encoded | `reg 74C(7) the FCA consulted the PRA as required` |
| reg 74C(7)(b) | 2420 | encoded | `reg 74C(7) the FCA consulted the PRA as required` |
| reg 74C(8) | 2421 | encoded | `reg 74C(8) the direction may be expressed to expire at the end of the period`, `reg 74C(8) the expiry of the direction affects the FCA's power to impose a new direction` |
| reg 74C(9) | 2422 | encoded | `reg 74C(9) the duty to give the notice in writing arises`, `reg 74C(9) the FCA gave the notice in writing` |
| reg 74C(10) | 2423 | encoded | `reg 74C(10) the notice contains what it must` |
| reg 74C(10)(a) | 2424 | encoded | `reg 74C(10) the notice contains what it must` |
| reg 74C(10)(b) | 2425 | encoded | `reg 74C(10) the notice contains what it must` |
| reg 74C(10)(c) | 2426 | encoded | `reg 74C(10) the notice contains what it must` |
| reg 74C(10)(d) | 2427 | encoded | `reg 74C(10) the notice contains what it must` |
| reg 74C(10)(e) | 2428 | encoded | `reg 74C(10) the notice contains what it must` |
| reg 74C(11) | 2429 | encoded | `reg 74C(11) the FCA may extend the period` |
| reg 74C(12) | 2430 | encoded | `reg 74C(12) the duty to give notice of the decision not to rescind arises`, `reg 74C(12) the FCA gave the notice in writing of its decision not to rescind` |
| reg 74C(13) | 2431 | encoded | `reg 74C(13) the duty to give notice of the decision on the representations arises`, `reg 74C(13) the FCA gave the notice in writing of its decision on the representations` |
| reg 74C(13)(a) | 2432 | encoded | `reg 74C(13) the duty to give notice of the decision on the representations arises`, `reg 74C(13) the FCA gave the notice in writing of its decision on the representations` |
| reg 74C(13)(b) | 2433 | encoded | `reg 74C(13) the duty to give notice of the decision on the representations arises`, `reg 74C(13) the FCA gave the notice in writing of its decision on the representations` |
| reg 74C(13)(c) | 2434-2435 | encoded | `reg 74C(13) the duty to give notice of the decision on the representations arises`, `reg 74C(13) the FCA gave the notice in writing of its decision on the representations` |
| reg 74C(14) | 2436 | encoded | `reg 74C(14) the notice informs the cryptoasset business of its right to refer the matter` |
| reg 74C(15) | 2437 | encoded | `reg 74C(15) the notice complies with paragraph (10)` |
| reg 74C(16) | 2438 | encoded | `reg 74C(16) the duty to indicate the procedure on a reference arises`, `reg 74C(16) the notice gives an indication of the procedure on a reference` |
| reg 74C(17) | 2439 | encoded | `reg 74C(17) the duty to give the notice in writing of the direction imposed or varied on request arises`, `reg 74C(17) the FCA gave the notice in writing of the direction imposed or varied on request` |
| reg 74C(18) | 2440 | encoded | `reg 74C(18) the notice contains what it must` (gap: paragraph (18) lists three things the notice must do (give details of the direction, state the reasons, inform the business when the direction takes effect, lines 2441-2443) and does not mention a right to refer the matter, so no function asks whether the notice must state one) |
| reg 74C(18)(a) | 2441 | encoded | `reg 74C(18) the notice contains what it must` |
| reg 74C(18)(b) | 2442 | encoded | `reg 74C(18) the notice contains what it must` |
| reg 74C(18)(c) | 2443 | encoded | `reg 74C(18) the notice contains what it must` |
| reg 74C(19) | 2444 | encoded | `reg 74C(19) the duty to give the notice in writing of the rescission arises`, `reg 74C(19) the FCA gave the notice in writing of the rescission` |
| reg 74C(20) | 2445 | encoded | `reg 74C(20) the FCA may publish information about the notice` |
| reg 74C(21) | 2446 | encoded | `reg 74C(21) the duty to publish the fact of the rescission arises`, `reg 74C(21) the FCA published the fact of the rescission` |
| reg 74C(22) | 2447 | encoded | `reg 74C(22) the duty to publish the status of the appeal and its outcome arises`, `reg 74C(22) the FCA published the status of the appeal and its outcome` |
| PART 9 | 2448 | inert (reason 1: a heading) | no rule: a heading |
| CHAPTER 1 | 2449 | inert (reason 1: a heading) | no rule: a heading |
| reg 75 heading | 2450 | inert (reason 1: a heading) | no rule: a heading |
| reg 75 | 2451 | encoded | `reg 75 the requirement is a relevant requirement` |
| CHAPTER 2 | 2452 | inert (reason 1: a heading) | no rule: a heading |
| reg 76 heading | 2453 | inert (reason 1: a heading) | no rule: a heading |
| reg 76(1) | 2454 | encoded | `reg 76(1) paragraph (2) applies` |
| reg 76(2) | 2455 | fork F-CHAPEAU | `reg 76(2) measure`, `reg 76(2) the designated supervisory authority may` |
| reg 76(2)(a) | 2456 | encoded | `reg 76(2) measure`, `reg 76(2) the designated supervisory authority may` |
| reg 76(2)(b) | 2457 | encoded | `reg 76(2) measure`, `reg 76(2) the designated supervisory authority may` |
| reg 76(3) | 2458 | encoded | `reg 76(3) the designated supervisory authority may impose a penalty on the officer` |
| reg 76(4) | 2459 | encoded | `reg 76(4) the designated supervisory authority may impose a penalty on P`, `reg 76(4) the prohibition on the designated supervisory authority` |
| reg 76(5) | 2460 | encoded | `reg 76(5) the duty to consult the PRA arises`, `reg 76(5) the FCA consulted the PRA` |
| reg 76(6) | 2461 | encoded | `reg 76(6)(b) the guidance is guidance the authority must consider` |
| reg 76(6)(a) | 2462 | repealed or blank in this text | the text shows the paragraph (a) is shown as `. . . .` (omitted by amendment) |
| reg 76(6)(b) | 2463 | encoded | `reg 76(6)(b) the guidance is guidance the authority must consider` |
| reg 76(6)(b)(i) | 2464 | encoded | `reg 76(6)(b) the guidance is guidance the authority must consider` |
| reg 76(6)(b)(ii) | 2465 | encoded | `reg 76(6)(b) the guidance is guidance the authority must consider` |
| reg 76(7) | 2466 | encoded | `reg 76(7) the penalty is payable to` |
| reg 76(8) | 2467 | encoded | `reg 76(8)(b) the body is a designated supervisory authority` |
| reg 76(8)(a) | 2468 | encoded | `reg 76(8)(b) the body is a designated supervisory authority`, `reg 76(8)(a) the penalty or measure is appropriate` |
| reg 76(8)(b) | 2469 | encoded | `reg 76(8)(b) the body is a designated supervisory authority` |
| reg 77 heading | 2470 | inert (reason 1: a heading) | no rule: a heading |
| reg 77(1) | 2471 | encoded | `reg 77(1) paragraph (2) applies` |
| reg 77(1)(a) | 2472 | encoded | `reg 77(1) paragraph (2) applies` |
| reg 77(1)(b) | 2473 | encoded | `reg 77(1) paragraph (2) applies` |
| reg 77(1)(c) | 2474 | encoded | `reg 77(1) paragraph (2) applies` |
| reg 77(1)(d) | 2475 | encoded | `reg 77(1) paragraph (2) applies` |
| reg 77(1)(e) | 2476 | encoded | `reg 77(1) paragraph (2) applies` |
| reg 77(2) | 2477 | fork F-CHAPEAU F-77-79 | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` (gap: regulation 77 names the FCA (line 2471) and regulation 79 lets "a designated supervisory authority" exercise the powers in regulations 76, 77 and 78 (line 2512), which includes the Commissioners; the text gives both, and no input for the acting authority was added (fork F-77-79)) |
| reg 77(2)(a) | 2478 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(a)(i) | 2479 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(a)(ii) | 2480 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(a)(iii) | 2481 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(a)(iv) | 2482 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(a)(v) | 2483 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(b) | 2484 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(b)(i) | 2485 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(b)(ii) | 2486 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(b)(iii) | 2487 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(b)(iv) | 2488 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(2)(b)(v) | 2489 | encoded | `reg 77(2) measure`, `reg 77(2) the FCA may take the measure` |
| reg 77(3) | 2490 | encoded | `reg 77(3)(a) the thing is a permission`, `reg 77(3)(b) regulated activity is given by` |
| reg 77(3)(a) | 2491 | encoded | `reg 77(3)(a) the thing is a permission`, `reg 77(3)(b) regulated activity is given by` |
| reg 77(3)(b) | 2492 | encoded | `reg 77(3)(a) the thing is a permission`, `reg 77(3)(b) regulated activity is given by` |
| reg 77(4) | 2493 | fork F-77-4 | `reg 77(4) the period of the suspension, limitation or other restriction is permitted` (gap: the paragraph limits the period of a suspension, limitation or other restriction (in months); the function takes months only, and a cancellation is not given a period by the text (fork F-77-4)) |
| reg 77(5) | 2494 | encoded | `reg 77(5) the suspension may relate to the thing` |
| reg 77(6) | 2495 | encoded | `reg 77(6) the restriction may be imposed so as to require the person to take, or refrain from taking, specified action` |
| reg 77(7) | 2496 | encoded | `reg 77(7) step`, `reg 77(7) the FCA may` |
| reg 77(7)(a) | 2497 | encoded | `reg 77(7) step`, `reg 77(7) the FCA may` |
| reg 77(7)(b) | 2498 | encoded | `reg 77(7) step`, `reg 77(7) the FCA may` |
| reg 77(8) | 2499 | encoded | `reg 77(8) the period or limitation is appropriate` |
| reg 78 heading | 2500 | inert (reason 1: a heading) | no rule: a heading |
| reg 78(1) | 2501 | encoded | `reg 78(1) paragraph (2) applies` |
| reg 78(2) | 2502 | fork F-CHAPEAU | `reg 78(2) measure`, `reg 78(2) the designated supervisory authority may impose the measure` (gap: the two measures are listed as "one of the following measures"; no function asks whether a temporary and a permanent prohibition may be imposed together) |
| reg 78(2)(a) | 2503 | encoded | `reg 78(2) measure`, `reg 78(2) the designated supervisory authority may impose the measure` |
| reg 78(2)(b) | 2504 | encoded | `reg 78(2) measure`, `reg 78(2) the designated supervisory authority may impose the measure` |
| reg 78(3) | 2505 | encoded | `reg 78(3) the prohibition may be expressed to expire at the end of the period`, `reg 78(3) the expiry of the temporary prohibition affects the power to impose a new prohibition under paragraph (2)(a)` |
| reg 78(4) | 2506 | encoded | `reg 78(4) scope`, `reg 78(4) the prohibition may be expressed to be in` |
| reg 78(4)(a) | 2507 | encoded | `reg 78(4) scope`, `reg 78(4) the prohibition may be expressed to be in` |
| reg 78(4)(b) | 2508 | encoded | `reg 78(4) scope`, `reg 78(4) the prohibition may be expressed to be in` |
| reg 78(4)(c) | 2509 | encoded | `reg 78(4) scope`, `reg 78(4) the prohibition may be expressed to be in` |
| reg 78(5) | 2510 | encoded | `reg 78(5) the person took reasonable care` |
| reg 79 heading | 2511 | inert (reason 1: a heading) | no rule: a heading |
| reg 79 | 2512 | fork F-77-79 | `reg 79 the powers may be exercised in relation to the same contravention` |
| reg 80 heading | 2513 | inert (reason 1: a heading) | no rule: a heading |
| reg 80(1) | 2514 | encoded | `reg 80(1) the court may make an order restraining the contravention` |
| reg 80(1)(a) | 2515 | encoded | `reg 80(1) the court may make an order restraining the contravention` |
| reg 80(1)(b) | 2516-2517 | encoded | `reg 80(1) the court may make an order restraining the contravention` |
| reg 80(2) | 2518 | encoded | `reg 80(2) the court may make an order requiring the person to take steps to remedy the contravention` |
| reg 80(2)(a) | 2519 | encoded | `reg 80(2) the court may make an order requiring the person to take steps to remedy the contravention` |
| reg 80(2)(b) | 2520-2521 | encoded | `reg 80(2) the court may make an order requiring the person to take steps to remedy the contravention` |
| reg 80(3) | 2522 | encoded | `reg 80(3) the court may make an order restraining the person from disposing or otherwise dealing with the assets` |
| reg 80(3)(a) | 2523 | encoded | `reg 80(3) the court may make an order restraining the person from disposing or otherwise dealing with the assets` |
| reg 80(3)(b) | 2524-2525 | encoded | `reg 80(3) the court may make an order restraining the person from disposing or otherwise dealing with the assets` |
| reg 80(4) | 2526 | encoded | `reg 80(4) court`, `reg 80(4) the jurisdiction in this regulation is exercisable by` |
| reg 80(5) | 2527 | encoded | `reg 80(5) the steps are within paragraph (2)` |
| reg 81 heading | 2528 | inert (reason 1: a heading) | no rule: a heading |
| reg 81(1) | 2529 | fork F-WHEN | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1)(a) | 2530 | encoded | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1)(b) | 2531 | encoded | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1)(c) | 2532 | encoded | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1)(d) | 2533 | encoded | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1)(e) | 2534 | encoded | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1)(f) | 2535 | encoded | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1)(g) | 2536 | encoded | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1)(h) | 2537 | encoded | `reg 81(1) circumstance`, `reg 81(1) the FCA must take the circumstance into account` |
| reg 81(1A) | 2538 | fork F-WHEN | `reg 81(1A) the duty to check whether P has criminal convictions arises`, `reg 81(1A) the FCA checked whether P has criminal convictions` |
| reg 81(2) | 2539 | encoded | `reg 81(2) the duty to give P a warning notice arises`, `reg 81(2) the FCA gave P a warning notice` |
| reg 81(3) | 2540 | encoded | `reg 81(3) the duty to consult the PRA arises`, `reg 81(3) the FCA consulted the PRA` |
| reg 81(4) | 2541 | encoded | `reg 81(4) section 387 of FSMA applies to the notice` |
| reg 81(5) | 2542 | encoded | `reg 81(5) the warning notice contains what it must` |
| reg 81(5)(a) | 2543 | encoded | `reg 81(5) the warning notice contains what it must` |
| reg 81(5)(b) | 2544 | encoded | `reg 81(5) the warning notice contains what it must` |
| reg 81(5)(c) | 2545 | encoded | `reg 81(5) the warning notice contains what it must` |
| reg 81(5)(c)(i) | 2546 | encoded | `reg 81(5) the warning notice contains what it must` |
| reg 81(5)(c)(ii) | 2547 | encoded | `reg 81(5) the warning notice contains what it must` |
| reg 81(5)(d) | 2548 | encoded | `reg 81(5) the warning notice contains what it must` |
| reg 81(5)(e) | 2549 | encoded | `reg 81(5) the warning notice contains what it must` |
| reg 81(6) | 2550 | encoded | `reg 81(6) the duty to give P a decision notice arises`, `reg 81(6) the FCA gave P a decision notice without undue delay` |
| reg 81(7) | 2551 | encoded | `reg 81(7) the duty to set out the terms of the statement arises`, `reg 81(7) the decision notice sets out the terms of the statement` |
| reg 81(8) | 2552 | encoded | `reg 81(8) the duty to specify the amount of the penalty arises`, `reg 81(8) the decision notice specifies the amount of the penalty` |
| reg 81(9) | 2553 | encoded | `reg 81(9) the duty to include what paragraph (9) requires arises`, `reg 81(9) the decision notice contains what it must` |
| reg 81(9)(a) | 2554 | encoded | `reg 81(9) the duty to include what paragraph (9) requires arises`, `reg 81(9) the decision notice contains what it must` |
| reg 81(9)(b) | 2555 | encoded | `reg 81(9) the duty to include what paragraph (9) requires arises`, `reg 81(9) the decision notice contains what it must` |
| reg 81(10) | 2556 | encoded | `reg 81(10) the duty to state the date of the cancellation arises`, `reg 81(10) the decision notice states the date of the cancellation` |
| reg 81(11) | 2557 | encoded | `reg 81(11) the duty to set out the terms of the prohibition arises`, `reg 81(11) the decision notice sets out the terms of the prohibition` |
| reg 81(12) | 2558 | encoded | `reg 81(12) section 388 of FSMA applies to the notice` |
| reg 81(13) | 2559 | encoded | `reg 81(13)(a) the words substituted in section 388(1)(e)(i) of FSMA for “this Act”`, `reg 81(13)(b) the subsection is omitted for the purposes of paragraph (12)` |
| reg 81(13)(a) | 2560 | encoded | `reg 81(13)(a) the words substituted in section 388(1)(e)(i) of FSMA for “this Act”`, `reg 81(13)(b) the subsection is omitted for the purposes of paragraph (12)` |
| reg 81(13)(b) | 2561 | encoded | `reg 81(13)(a) the words substituted in section 388(1)(e)(i) of FSMA for “this Act”`, `reg 81(13)(b) the subsection is omitted for the purposes of paragraph (12)` |
| reg 82 heading | 2562 | inert (reason 1: a heading) | no rule: a heading |
| reg 82(1) | 2563 | encoded | `reg 82(1) section of FSMA`, `reg 82(1) the section of FSMA applies to the notice` |
| reg 82(2) | 2564 | encoded | `reg 82(2)(a) the final notice about a cancellation, suspension, limitation or other restriction contains what it must` |
| reg 82(2)(a) | 2565 | encoded | `reg 82(2)(a) the final notice about a cancellation, suspension, limitation or other restriction contains what it must` |
| reg 82(2)(a) [s 390(4) of FSMA as substituted] | 2566-2570 | encoded | `reg 82(2)(a) the final notice about a cancellation, suspension, limitation or other restriction contains what it must` |
| reg 82(2)(a) [s 390(4A) of FSMA as substituted] | 2571-2573 | encoded | `reg 82(2)(a) the final notice about a cancellation, suspension, limitation or other restriction contains what it must` |
| reg 82(2)(b) | 2574 | encoded | `reg 82(2)(a) the final notice about a cancellation, suspension, limitation or other restriction contains what it must`, `reg 82(2)(b) the subsection of section 390 of FSMA is omitted` |
| reg 82(3) | 2575 | encoded | `reg 82(3) section 392 of FSMA has effect as modified for the notice` |
| reg 82(3)(a) | 2576 | encoded | `reg 82(3) section 392 of FSMA has effect as modified for the notice` |
| reg 82(3)(b) | 2577 | encoded | `reg 82(3) section 392 of FSMA has effect as modified for the notice` |
| reg 83 heading | 2578 | inert (reason 1: a heading) | no rule: a heading |
| reg 83(1) | 2579 | fork F-WHEN | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1)(a) | 2580 | encoded | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1)(b) | 2581 | encoded | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1)(c) | 2582 | encoded | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1)(d) | 2583 | encoded | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1)(e) | 2584 | encoded | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1)(f) | 2585 | encoded | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1)(g) | 2586 | encoded | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1)(h) | 2587 | encoded | `reg 83(1) circumstance`, `reg 83(1) the Commissioners must take the circumstance into account` |
| reg 83(1A) | 2588 | fork F-WHEN | `reg 83(1A) the duty to check whether P has criminal convictions arises`, `reg 83(1A) the Commissioners checked whether P has criminal convictions` |
| reg 83(2) | 2589 | encoded | `reg 83(2) the duty to give P a notice arises`, `reg 83(2) the Commissioners gave P a notice` |
| reg 83(3) | 2590 | encoded | `reg 83(3) the notice contains what it must` |
| reg 83(3)(a) | 2591 | encoded | `reg 83(3) the notice contains what it must` |
| reg 83(3)(a)(i) | 2592 | encoded | `reg 83(3) the notice contains what it must` |
| reg 83(3)(a)(ii) | 2593 | encoded | `reg 83(3) the notice contains what it must` |
| reg 83(3)(a)(iii) | 2594 | encoded | `reg 83(3) the notice contains what it must` |
| reg 83(3)(b) | 2595 | encoded | `reg 83(3) the notice contains what it must` |
| reg 83(3)(c) | 2596 | encoded | `reg 83(3) the notice contains what it must` |
| reg 83(3)(d) | 2597 | encoded | `reg 83(3) the notice contains what it must` |
| reg 83(4) | 2598 | encoded | `reg 83(4) the notice about a penalty contains what it must` |
| reg 83(4)(a) | 2599 | encoded | `reg 83(4) the notice about a penalty contains what it must` |
| reg 83(4)(b) | 2600 | encoded | `reg 83(4) the notice about a penalty contains what it must` |
| reg 84 heading | 2601 | inert (reason 1: a heading) | no rule: a heading |
| reg 84(1) | 2602 | encoded | `reg 84(1) the FCA or a person to whom the warning notice is given or copied may publish it or any details concerning it`, `reg 84(1) FCA the prohibition on the FCA`, `reg 84(1) recipient the prohibition on a person to whom the notice is given or copied` |
| reg 84(2) | 2603 | encoded | `reg 84(2) the duty to publish information about the matter arises`, `reg 84(2) the FCA published information about the matter` |
| reg 84(3) | 2604 | encoded | `reg 84(3) the duty to publish the status of the appeal and its outcome arises`, `reg 84(3) the FCA published the status of the appeal and its outcome` |
| reg 84(4) | 2605 | encoded | `reg 84(4) the duty to publish the type and nature of the breach arises`, `reg 84(4) the FCA published the type and nature of the breach and the identity of the person` |
| reg 84(5) | 2606 | encoded | `reg 84(5) the information must be published in accordance with paragraph (6)` |
| reg 84(5)(a) | 2607 | encoded | `reg 84(5) the information must be published in accordance with paragraph (6)` |
| reg 84(5)(b) | 2608 | encoded | `reg 84(5) the information must be published in accordance with paragraph (6)` |
| reg 84(5)(c) | 2609 | encoded | `reg 84(5) the information must be published in accordance with paragraph (6)` |
| reg 84(6) | 2610 | encoded | `reg 84(6) the duty to defer the publication or publish it anonymously arises`, `reg 84(6) the FCA deferred or published anonymously` |
| reg 84(6)(a) | 2611 | encoded | `reg 84(6) the duty to defer the publication or publish it anonymously arises`, `reg 84(6) the FCA deferred or published anonymously` |
| reg 84(6)(b) | 2612 | encoded | `reg 84(6) the duty to defer the publication or publish it anonymously arises`, `reg 84(6) the FCA deferred or published anonymously` |
| reg 84(7) | 2613 | encoded | `reg 84(7) the FCA may make arrangements as to the publication of information` |
| reg 84(8) | 2614 | encoded | `reg 84(8) the FCA may make arrangements for the postponed publication of personal data` |
| reg 84(8)(a) | 2615 | encoded | `reg 84(8) the FCA may make arrangements for the postponed publication of personal data` |
| reg 84(8)(b) | 2616 | encoded | `reg 84(8) the FCA may make arrangements for the postponed publication of personal data` |
| reg 84(9) | 2617 | encoded | `reg 84(9) the information about the matter may be published` |
| reg 84(9)(a) | 2618 | encoded | `reg 84(9) the information about the matter may be published` |
| reg 84(9)(b) | 2619 | encoded | `reg 84(9) the information about the matter may be published` |
| reg 84(10) | 2620 | encoded | `reg 84(10) the duty to keep the information on the website arises`, `reg 84(10) the information remained on the website for long enough` |
| reg 84(11) | 2621 | encoded | `reg 84(11) personal data is given by` |
| reg 85 heading | 2622 | inert (reason 1: a heading) | no rule: a heading |
| reg 85(1) | 2623 | encoded | `reg 85(1) the duty to publish information about the matter arises`, `reg 85(1) the Commissioners published information about the matter` |
| reg 85(2) | 2624 | encoded | `reg 85(2) the duty to publish the status of the appeal and its outcome arises`, `reg 85(2) the Commissioners published the status of the appeal and its outcome` |
| reg 85(3) | 2625 | encoded | `reg 85(3) the duty to publish the type and nature of the breach arises`, `reg 85(3) the Commissioners published the type and nature of the breach and the identity of the person` |
| reg 85(4) | 2626 | encoded | `reg 85(4) the information must be published in accordance with paragraph (5)` |
| reg 85(4)(a) | 2627 | encoded | `reg 85(4) the information must be published in accordance with paragraph (5)` |
| reg 85(4)(b) | 2628 | encoded | `reg 85(4) the information must be published in accordance with paragraph (5)` |
| reg 85(4)(c) | 2629 | encoded | `reg 85(4) the information must be published in accordance with paragraph (5)` |
| reg 85(5) | 2630 | encoded | `reg 85(5) the duty to defer the publication or publish it anonymously arises`, `reg 85(5) the Commissioners deferred or published anonymously` |
| reg 85(5)(a) | 2631 | encoded | `reg 85(5) the duty to defer the publication or publish it anonymously arises`, `reg 85(5) the Commissioners deferred or published anonymously` |
| reg 85(5)(b) | 2632 | encoded | `reg 85(5) the duty to defer the publication or publish it anonymously arises`, `reg 85(5) the Commissioners deferred or published anonymously` |
| reg 85(6) | 2633 | encoded | `reg 85(6) the Commissioners may make arrangements as to the publication of information` |
| reg 85(7) | 2634 | encoded | `reg 85(7) the Commissioners may make arrangements for the postponed publication of personal data` |
| reg 85(7)(a) | 2635 | encoded | `reg 85(7) the Commissioners may make arrangements for the postponed publication of personal data` |
| reg 85(7)(b) | 2636 | encoded | `reg 85(7) the Commissioners may make arrangements for the postponed publication of personal data` |
| reg 85(8) | 2637 | encoded | `reg 85(8) the information about the matter may be published` |
| reg 85(8)(a) | 2638 | encoded | `reg 85(8) the information about the matter may be published` |
| reg 85(8)(b) | 2639 | encoded | `reg 85(8) the information about the matter may be published` |
| reg 85(9) | 2640 | encoded | `reg 85(9) the duty to keep the information on the website arises`, `reg 85(9) the information remained on the website for long enough` |
| reg 85(10) | 2641 | encoded | `reg 85(10) personal data is given by` |
| CHAPTER 3 | 2642 | inert (reason 1: a heading) | no rule: a heading |
| reg 86 heading | 2643 | inert (reason 1: a heading) | no rule: a heading |
| reg 86(1) | 2644 | encoded | `reg 86(1) the person is guilty of an offence`, `reg 86(1) the term of imprisonment is within the liability`, `reg 86(1) the fine is within the liability (+1 more)` |
| reg 86(1)(a) | 2645 | encoded | `reg 86(1) the person is guilty of an offence`, `reg 86(1) the term of imprisonment is within the liability`, `reg 86(1) the fine is within the liability` |
| reg 86(1)(a)(i) | 2646 | fork F-86-FINE | `reg 86(1) the person is guilty of an offence`, `reg 86(1) the term of imprisonment is within the liability`, `reg 86(1) the fine is within the liability` |
| reg 86(1)(a)(ii) | 2647 | encoded | `reg 86(1) the person is guilty of an offence`, `reg 86(1) the term of imprisonment is within the liability`, `reg 86(1) the fine is within the liability` |
| reg 86(1)(b) | 2648 | fork F-86-FINE | `reg 86(1) the person is guilty of an offence`, `reg 86(1) the term of imprisonment is within the liability`, `reg 86(1) the fine is within the liability` |
| reg 86(2) | 2649 | encoded | `reg 86(2)(b) the guidance is guidance the court must consider` |
| reg 86(2)(a) | 2650 | repealed or blank in this text | the text shows the paragraph (a) is shown as `. . . .` (omitted by amendment) |
| reg 86(2)(b) | 2651 | encoded | `reg 86(2)(b) the guidance is guidance the court must consider` |
| reg 86(2)(b)(i) | 2652 | encoded | `reg 86(2)(b) the guidance is guidance the court must consider` |
| reg 86(2)(b)(ii) | 2653 | encoded | `reg 86(2)(b) the guidance is guidance the court must consider` |
| reg 86(3) | 2654 | encoded | `reg 86(3) the person is guilty of an offence under this regulation`, `reg 86(1) and (3) the person is guilty of an offence under regulation 86` |
| reg 86(4) | 2655 | encoded | `reg 86(4) the person is liable to a sanction under Chapter 2 of this Part` |
| reg 87 heading | 2656 | inert (reason 1: a heading) | no rule: a heading |
| reg 87(1) | 2657 | encoded | `reg 87(1) this regulation applies` |
| reg 87(2) | 2658 | encoded | `reg 87(2)(a) P commits an offence by a disclosure likely to prejudice the investigation`, `reg 87(2) P commits an offence` |
| reg 87(2)(a) | 2659 | encoded | `reg 87(2)(a) P commits an offence by a disclosure likely to prejudice the investigation`, `reg 87(2) P commits an offence` |
| reg 87(2)(b) | 2660 | encoded | `reg 87(2)(a) P commits an offence by a disclosure likely to prejudice the investigation`, `reg 87(2) P commits an offence` |
| reg 87(3) | 2661 | encoded | `reg 87(3) case`, `reg 87(3) P commits an offence under paragraph (2)(a)`, `reg 87(2) P commits an offence` |
| reg 87(3)(a) | 2662 | encoded | `reg 87(3) case`, `reg 87(3) P commits an offence under paragraph (2)(a)`, `reg 87(2) P commits an offence` |
| reg 87(3)(b) | 2663 | encoded | `reg 87(3) case`, `reg 87(3) P commits an offence under paragraph (2)(a)`, `reg 87(2) P commits an offence` |
| reg 87(3)(c) | 2664 | encoded | `reg 87(3) case`, `reg 87(3) P commits an offence under paragraph (2)(a)`, `reg 87(2) P commits an offence` |
| reg 87(3)(d) | 2665 | encoded | `reg 87(3) case`, `reg 87(3) P commits an offence under paragraph (2)(a)`, `reg 87(2) P commits an offence` |
| reg 87(3)(e) | 2666 | encoded | `reg 87(3) case`, `reg 87(3) P commits an offence under paragraph (2)(a)`, `reg 87(2) P commits an offence` |
| reg 87(3)(f) | 2667 | encoded | `reg 87(3) case`, `reg 87(3) P commits an offence under paragraph (2)(a)`, `reg 87(2) P commits an offence` |
| reg 87(4) | 2668 | encoded | `reg 87(4) the conduct is criminal conduct` |
| reg 87(4)(a) | 2669 | encoded | `reg 87(4) the conduct is criminal conduct` |
| reg 87(4)(b) | 2670 | encoded | `reg 87(4) the conduct is criminal conduct` |
| reg 87(5) | 2671 | encoded | `reg 87(5) the person benefits from the conduct` |
| reg 87(6) | 2672 | encoded | `reg 87(6) the disclosure falls within this paragraph` |
| reg 87(6)(a) | 2673 | encoded | `reg 87(6) the disclosure falls within this paragraph` |
| reg 87(6)(b) | 2674 | encoded | `reg 87(6) the disclosure falls within this paragraph` |
| reg 87(7) | 2675 | encoded | `reg 87(7) the disclosure falls within paragraph (6)` |
| reg 87(8) | 2676 | encoded | `reg 87(8) P commits an offence under paragraph (2)(b)`, `reg 87(2) P commits an offence` |
| reg 87(8)(a) | 2677 | encoded | `reg 87(8) P commits an offence under paragraph (2)(b)`, `reg 87(2) P commits an offence` |
| reg 87(8)(b) | 2678 | encoded | `reg 87(8) P commits an offence under paragraph (2)(b)`, `reg 87(2) P commits an offence` |
| reg 87(9) | 2679 | encoded | `reg 87(9) the term of imprisonment is within the liability`, `reg 87(9) the fine is within the liability` |
| reg 87(9)(a) | 2680 | encoded | `reg 87(9) the term of imprisonment is within the liability`, `reg 87(9) the fine is within the liability` |
| reg 87(9)(a)(i) | 2681 | fork F-86-FINE | `reg 87(9) the term of imprisonment is within the liability`, `reg 87(9) the fine is within the liability` |
| reg 87(9)(a)(ii) | 2682 | encoded | `reg 87(9) the term of imprisonment is within the liability`, `reg 87(9) the fine is within the liability` |
| reg 87(9)(b) | 2683 | fork F-86-FINE | `reg 87(9) the term of imprisonment is within the liability`, `reg 87(9) the fine is within the liability` |
| reg 87(10) | 2684 | encoded | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “appropriate officer” | 2685 | encoded | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “appropriate officer” limb | 2686 | encoded | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “appropriate officer” limb | 2687 | encoded | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “appropriate officer” limb | 2688 | encoded | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “appropriate officer” limb | 2689 | encoded | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “relevant officer” | 2690 | fork F-ARRANGEMENTS | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “relevant officer” limb | 2691 | fork F-ARRANGEMENTS | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “relevant officer” limb | 2692 | fork F-ARRANGEMENTS | `reg 87(10) the person is a relevant officer` |
| reg 87(10) “relevant officer” limb | 2693 | fork F-ARRANGEMENTS | `reg 87(10) the person is a relevant officer` |
| reg 88 heading | 2694 | inert (reason 1: a heading) | no rule: a heading |
| reg 88(1) | 2695 | encoded | `reg 88(1) P commits an offence` |
| reg 88(1)(a) | 2696 | encoded | `reg 88(1) P commits an offence` |
| reg 88(1)(b) | 2697 | encoded | `reg 88(1) P commits an offence` |
| reg 88(2) | 2698 | encoded | `reg 88(2) the term of imprisonment is within the liability`, `reg 88(2) the fine is within the liability` |
| reg 88(2)(a) | 2699 | encoded | `reg 88(2) the term of imprisonment is within the liability`, `reg 88(2) the fine is within the liability` |
| reg 88(2)(a)(i) | 2700 | fork F-86-FINE | `reg 88(2) the term of imprisonment is within the liability`, `reg 88(2) the fine is within the liability` |
| reg 88(2)(a)(ii) | 2701 | encoded | `reg 88(2) the term of imprisonment is within the liability`, `reg 88(2) the fine is within the liability` |
| reg 88(2)(b) | 2702 | fork F-86-FINE | `reg 88(2) the term of imprisonment is within the liability`, `reg 88(2) the fine is within the liability` |
| reg 88(3) | 2703 | encoded | `reg 88(3) the person is guilty of an offence of disclosing information`, `reg 88(3) the term of imprisonment is within the liability`, `reg 88(3) the fine is within the liability` |
| reg 88(3)(a) | 2704 | encoded | `reg 88(3) the person is guilty of an offence of disclosing information`, `reg 88(3) the term of imprisonment is within the liability`, `reg 88(3) the fine is within the liability` |
| reg 88(3)(a)(i) | 2705 | fork F-86-FINE | `reg 88(3) the person is guilty of an offence of disclosing information`, `reg 88(3) the term of imprisonment is within the liability`, `reg 88(3) the fine is within the liability` |
| reg 88(3)(a)(ii) | 2706 | encoded | `reg 88(3) the person is guilty of an offence of disclosing information`, `reg 88(3) the term of imprisonment is within the liability`, `reg 88(3) the fine is within the liability` |
| reg 88(3)(b) | 2707 | fork F-86-FINE | `reg 88(3) the person is guilty of an offence of disclosing information`, `reg 88(3) the term of imprisonment is within the liability`, `reg 88(3) the fine is within the liability` |
| reg 88(4) | 2708 | encoded | `reg 88(4) the person has a defence` (note: when neither belief is proved the function answers JUST FALSE, meaning regulation 88(4) gives no defence on these facts; it does not say the person has no defence at all (ruled 2026-11-05 (b))) |
| reg 88(4)(a) | 2709 | encoded | `reg 88(4) the person has a defence` |
| reg 88(4)(b) | 2710 | encoded | `reg 88(4) the person has a defence` |
| reg 89 heading | 2711 | inert (reason 1: a heading) | no rule: a heading |
| reg 89(1) | 2712 | encoded | `reg 89(1) body`, `reg 89(1) the body may institute proceedings for an offence under these Regulations`, `reg 89(1) and (5) the body may institute proceedings` |
| reg 89(1)(a) | 2713 | encoded | `reg 89(1) body`, `reg 89(1) the body may institute proceedings for an offence under these Regulations`, `reg 89(1) and (5) the body may institute proceedings` |
| reg 89(1)(b) | 2714 | encoded | `reg 89(1) body`, `reg 89(1) the body may institute proceedings for an offence under these Regulations`, `reg 89(1) and (5) the body may institute proceedings` |
| reg 89(1)(c) | 2715 | encoded | `reg 89(1) body`, `reg 89(1) the body may institute proceedings for an offence under these Regulations`, `reg 89(1) and (5) the body may institute proceedings` |
| reg 89(1)(d) | 2716 | encoded | `reg 89(1) body`, `reg 89(1) the body may institute proceedings for an offence under these Regulations`, `reg 89(1) and (5) the body may institute proceedings` |
| reg 89(1)(e) | 2717 | encoded | `reg 89(1) body`, `reg 89(1) the body may institute proceedings for an offence under these Regulations`, `reg 89(1) and (5) the body may institute proceedings` |
| reg 89(2) | 2718 | encoded | `reg 89(2) the duty to bring the proceedings in the name of an officer of Revenue and Customs arises`, `reg 89(2) the proceedings were brought in the name of an officer of Revenue and Customs` |
| reg 89(3) | 2719 | encoded | `reg 89(3) the duty to report arises`, `reg 89(3) the local weights and measures authority reported as required` |
| reg 89(4) | 2720 | encoded | `reg 89(4) the matter is treated as an assigned matter` |
| reg 89(4)(a) | 2721 | encoded | `reg 89(4) the matter is treated as an assigned matter` |
| reg 89(4)(b) | 2722-2723 | encoded | `reg 89(4) the matter is treated as an assigned matter` |
| reg 89(5) | 2724 | encoded | `reg 89(5) paragraphs (1) and (3) extend to the place`, `reg 89(1) and (5) the body may institute proceedings` |
| reg 89(6) | 2725 | encoded | `reg 89(6) paragraph (4)(b) is read as referring to the Crown Office and Procurator Fiscal Service` |
| reg 90 heading | 2726 | inert (reason 1: a heading) | no rule: a heading |
| reg 90(1) | 2727 | encoded | `reg 90(1) proceedings may be taken before the appropriate court having jurisdiction where the person is` |
| reg 90(2) | 2728 | encoded | `reg 90(2) proceedings may be taken at any appropriate court in the United Kingdom` |
| reg 90(3) | 2729 | encoded | `reg 90(3) the offence may for all incidental purposes be treated as committed within the jurisdiction of the court` |
| reg 91 heading | 2730 | inert (reason 1: a heading) | no rule: a heading |
| reg 91(1) | 2731 | encoded | `reg 91(1) the proceedings were brought in the right name` |
| reg 91(1)(a) | 2732 | encoded | `reg 91(1) the proceedings were brought in the right name` |
| reg 91(1)(b) | 2733-2734 | encoded | `reg 91(1) the proceedings were brought in the right name` |
| reg 91(2) | 2735 | encoded | `reg 91(2) the fine is paid out of the funds of the partnership or association` |
| reg 91(2)(a) | 2736 | encoded | `reg 91(2) the fine is paid out of the funds of the partnership or association` |
| reg 91(2)(b) | 2737 | encoded | `reg 91(2) the fine is paid out of the funds of the partnership or association` |
| reg 91(3) | 2738 | encoded | `reg 91(3) the rules of court relating to the service of documents have effect as if the body were a body corporate` |
| reg 91(4) | 2739 | encoded | `reg 91(4)(a) section 33 of the Criminal Justice Act 1925 and Schedule 3 to the Magistrates' Courts Act 1980 apply as to a body corporate`, `reg 91(4)(b) section 18 of the Criminal Justice (Northern Ireland) Act 1945 and Schedule 4 to the Magistrates' Courts (Northern Ireland) Order 1981 apply as to a body corporate` |
| reg 91(4)(a) | 2740 | encoded | `reg 91(4)(a) section 33 of the Criminal Justice Act 1925 and Schedule 3 to the Magistrates' Courts Act 1980 apply as to a body corporate`, `reg 91(4)(b) section 18 of the Criminal Justice (Northern Ireland) Act 1945 and Schedule 4 to the Magistrates' Courts (Northern Ireland) Order 1981 apply as to a body corporate` |
| reg 91(4)(b) | 2741 | encoded | `reg 91(4)(a) section 33 of the Criminal Justice Act 1925 and Schedule 3 to the Magistrates' Courts Act 1980 apply as to a body corporate`, `reg 91(4)(b) section 18 of the Criminal Justice (Northern Ireland) Act 1945 and Schedule 4 to the Magistrates' Courts (Northern Ireland) Order 1981 apply as to a body corporate` |
| reg 92 heading | 2742 | inert (reason 1: a heading) | no rule: a heading |
| reg 92(1) | 2743 | encoded | `reg 92(1) the officer is guilty of the offence` |
| reg 92(1)(a) | 2744 | encoded | `reg 92(1) the officer is guilty of the offence` |
| reg 92(1)(b) | 2745-2746 | encoded | `reg 92(1) the officer is guilty of the offence` |
| reg 92(2) | 2747 | encoded | `reg 92(2) paragraph (1) applies to the member as if the member was a director` |
| reg 92(3) | 2748 | encoded | `reg 92(3) the officer is guilty of the offence committed by the partnership` |
| reg 92(3)(a) | 2749 | encoded | `reg 92(3) the officer is guilty of the offence committed by the partnership` |
| reg 92(3)(b) | 2750-2751 | encoded | `reg 92(3) the officer is guilty of the offence committed by the partnership` |
| reg 92(4) | 2752 | encoded | `reg 92(4) the officer is guilty of the offence committed by the unincorporated association` |
| reg 92(4)(a) | 2753 | encoded | `reg 92(4) the officer is guilty of the offence committed by the unincorporated association` |
| reg 92(4)(b) | 2754-2755 | encoded | `reg 92(4) the officer is guilty of the offence committed by the unincorporated association` |
| PART 10 | 2756 | inert (reason 1: a heading) | no rule: a heading |
| CHAPTER 1 | 2757 | inert (reason 1: a heading) | no rule: a heading |
| reg 93 heading | 2758 | inert (reason 1: a heading) | no rule: a heading |
| reg 93(1) | 2759 | encoded | `reg 93(1) a person may appeal to the Upper Tribunal` |
| reg 93(1)(a) | 2760 | encoded | `reg 93(1) a person may appeal to the Upper Tribunal` |
| reg 93(1)(b) | 2761 | encoded | `reg 93(1) a person may appeal to the Upper Tribunal` |
| reg 93(1)(c) | 2762 | encoded | `reg 93(1) a person may appeal to the Upper Tribunal` |
| reg 93(1)(ca) | 2763 | encoded | `reg 93(1) a person may appeal to the Upper Tribunal` |
| reg 93(1)(d) | 2764 | encoded | `reg 93(1) a person may appeal to the Upper Tribunal` |
| reg 93(1)(e) | 2765 | encoded | `reg 93(1) a person may appeal to the Upper Tribunal` |
| reg 93(1)(f) | 2766 | encoded | `reg 93(1) a person may appeal to the Upper Tribunal` |
| reg 93(2) | 2767 | encoded | `reg 93(2) Part 9 of FSMA applies to the appeal with the modifications in paragraph (3)` |
| reg 93(3) | 2768 | encoded | `reg 93(3)(a) the paragraph inserted after paragraph (o) of section 133(7A) of FSMA` |
| reg 93(3)(a) [new para (p) in s 133(7A) of FSMA] | 2769-2770 | encoded | `reg 93(3)(a) the paragraph inserted after paragraph (o) of section 133(7A) of FSMA` |
| reg 93(3)(b) | 2771 | encoded | `reg 93(3)(b) section 133A(1) the action specified in the decision notice may be taken`, `reg 93(3)(b) section 133A(1) the action specified in the decision notice is barred` |
| reg 93(3)(b) [s 133A(1) of FSMA as substituted] | 2772-2775 | encoded | `reg 93(3)(b) section 133A(1) the action specified in the decision notice may be taken`, `reg 93(3)(b) section 133A(1) the action specified in the decision notice is barred` (note: the section is also asked as a bar, `... is barred`: JUST TRUE inside the referral period and while the reference is pending, JUST FALSE once the bar has ended; neither function says the action may be taken (ruled 2026-11-05 (d))) |
| reg 93(3)(b) [s 133A(2) of FSMA as substituted] | 2776 | encoded | `reg 93(3)(b) section 133A(2) the Tribunal may make recommendations as to the FCA's regulating provisions or procedures` |
| CHAPTER 2 | 2777 | inert (reason 1: a heading) | no rule: a heading |
| reg 94 heading | 2778 | inert (reason 1: a heading) | no rule: a heading |
| reg 94(1) | 2779 | encoded | `reg 94(1) the duty to offer P a review arises`, `reg 94(1) the Commissioners offered P a review` |
| reg 94(2) | 2780 | encoded | `reg 94(2) the offer of a review was made by notice at the same time as the decision` |
| reg 94(3) | 2781 | encoded | `reg 94 applies to the notification` |
| reg 95 heading | 2782 | inert (reason 1: a heading) | no rule: a heading |
| reg 95(1) | 2783 | encoded | `reg 95(1) the duty to review the decision arises`, `reg 95(1) the Commissioners reviewed the decision` |
| reg 95(1)(a) | 2784 | encoded | `reg 95(1) the duty to review the decision arises`, `reg 95(1) the Commissioners reviewed the decision` |
| reg 95(1)(b) | 2785 | fork F-PERIOD | `reg 95(1) the duty to review the decision arises`, `reg 95(1) the Commissioners reviewed the decision` |
| reg 95(2) | 2786 | encoded | `reg 95(2) P may notify acceptance of the offer`, `reg 95(2) the prohibition on P` |
| reg 95(3) | 2787 | encoded | `reg 95(3) the Commissioners may review the decision`, `reg 95(3) the prohibition on the Commissioners` |
| reg 96 heading | 2788 | inert (reason 1: a heading) | no rule: a heading |
| reg 96(1) | 2789 | encoded | `reg 96(1) the Commissioners may notify P that the relevant period is extended` |
| reg 96(2) | 2790 | fork F-PERIOD | `reg 96(2) the relevant period is extended to the end of day` |
| reg 96(2)(a) | 2791 | fork F-PERIOD | `reg 96(2) the relevant period is extended to the end of day` |
| reg 96(2)(b) | 2792 | fork F-PERIOD | `reg 96(2) the relevant period is extended to the end of day` |
| reg 96(3) | 2793 | encoded | `reg 96(3) a further notice may be given` |
| reg 96(4) | 2794 | encoded | `reg 96(4) the relevant period ends on day` |
| reg 96(4)(a) | 2795 | encoded | `reg 96(4) the relevant period ends on day` |
| reg 96(4)(b) | 2796 | encoded | `reg 96(4) the relevant period ends on day` |
| reg 97 heading | 2797 | inert (reason 1: a heading) | no rule: a heading |
| reg 97(1) | 2798 | encoded | `reg 97(1) this regulation applies` |
| reg 97(1)(a) | 2799 | encoded | `reg 97(1) this regulation applies` |
| reg 97(1)(b) | 2800 | encoded | `reg 97(1) this regulation applies` |
| reg 97(2) | 2801 | encoded | `reg 97(2) the duty to review the decision out of time arises`, `reg 97(2) the Commissioners reviewed the decision out of time` |
| reg 97(2)(a) | 2802 | encoded | `reg 97(2) the duty to review the decision out of time arises`, `reg 97(2) the Commissioners reviewed the decision out of time` |
| reg 97(2)(b) | 2803 | encoded | `reg 97(2) the duty to review the decision out of time arises`, `reg 97(2) the Commissioners reviewed the decision out of time` |
| reg 97(2)(c) | 2804 | encoded | `reg 97(2) the duty to review the decision out of time arises`, `reg 97(2) the Commissioners reviewed the decision out of time` |
| reg 98 heading | 2805 | inert (reason 1: a heading) | no rule: a heading |
| reg 98(1) | 2806 | encoded | `reg 98(1) this regulation applies` |
| reg 98(2) | 2807 | fork F-CHAPEAU | `reg 98(2) the nature and extent of the review are for the Commissioners to judge` |
| reg 98(3) | 2808 | encoded | `reg 98(3) the duty to have regard to the steps taken before the review arises`, `reg 98(3) the Commissioners had regard to the steps taken before the review` |
| reg 98(3)(a) | 2809 | encoded | `reg 98(3) the duty to have regard to the steps taken before the review arises`, `reg 98(3) the Commissioners had regard to the steps taken before the review` |
| reg 98(3)(b) | 2810 | encoded | `reg 98(3) the duty to have regard to the steps taken before the review arises`, `reg 98(3) the Commissioners had regard to the steps taken before the review` |
| reg 98(4) | 2811 | encoded | `reg 98(4) the duty to take account of the representations arises`, `reg 98(4) the review took account of the representations` |
| reg 98(5) | 2812 | fork F-CHAPEAU | `reg 98(5) conclusion`, `reg 98(5) the review may conclude that the decision is` |
| reg 98(5)(a) | 2813 | encoded | `reg 98(5) conclusion`, `reg 98(5) the review may conclude that the decision is` |
| reg 98(5)(b) | 2814 | encoded | `reg 98(5) conclusion`, `reg 98(5) the review may conclude that the decision is` |
| reg 98(5)(c) | 2815 | encoded | `reg 98(5) conclusion`, `reg 98(5) the review may conclude that the decision is` |
| reg 98(6) | 2816 | fork F-PERIOD | `reg 98(6) the duty to give P notice of the conclusions and reasoning arises`, `reg 98(6) the Commissioners gave P notice of the conclusions and reasoning in time` |
| reg 98(6)(a) | 2817 | fork F-PERIOD | `reg 98(6) the duty to give P notice of the conclusions and reasoning arises`, `reg 98(6) the Commissioners gave P notice of the conclusions and reasoning in time` |
| reg 98(6)(b) | 2818 | fork F-PERIOD | `reg 98(6) the duty to give P notice of the conclusions and reasoning arises`, `reg 98(6) the Commissioners gave P notice of the conclusions and reasoning in time` |
| reg 98(7) | 2819 | encoded | `reg 98(7) the relevant date is day` |
| reg 98(7)(a) | 2820 | encoded | `reg 98(7) the relevant date is day` |
| reg 98(7)(b) | 2821 | encoded | `reg 98(7) the relevant date is day` |
| reg 98(8) | 2822 | encoded | `reg 98(8) the review is treated as having concluded that the decision is upheld` |
| reg 98(9) | 2823 | encoded | `reg 98(9) the duty to notify P of the conclusion treated as reached arises`, `reg 98(9) the Commissioners notified P of the conclusion treated as reached` |
| reg 99 heading | 2824 | inert (reason 1: a heading) | no rule: a heading |
| reg 99(1) | 2825 | encoded | `reg 99(1) a person may appeal to the tribunal in accordance with regulation 100` |
| reg 99(1)(a) | 2826 | encoded | `reg 99(1) a person may appeal to the tribunal in accordance with regulation 100` |
| reg 99(1)(b) | 2827 | encoded | `reg 99(1) a person may appeal to the tribunal in accordance with regulation 100` |
| reg 99(1)(c) | 2828 | encoded | `reg 99(1) a person may appeal to the tribunal in accordance with regulation 100` |
| reg 99(1)(d) | 2829 | encoded | `reg 99(1) a person may appeal to the tribunal in accordance with regulation 100` |
| reg 99(1)(e) | 2830 | encoded | `reg 99(1) a person may appeal to the tribunal in accordance with regulation 100` |
| reg 99(1)(f) | 2831 | encoded | `reg 99(1) a person may appeal to the tribunal in accordance with regulation 100` |
| reg 99(2) | 2832 | encoded | `reg 99(2) Part 5 of the Value Added Tax Act 1994 applies to the appeal` |
| reg 99(3) | 2833 | encoded | `reg 99(3) section of the Value Added Tax Act 1994`, `reg 99(3) the section is omitted` |
| reg 99(4) | 2834 | encoded | `reg 99(4) power`, `reg 99(4) the tribunal has the power to` |
| reg 99(4)(a) | 2835 | encoded | `reg 99(4) power`, `reg 99(4) the tribunal has the power to`, `reg 99(4)(a) the tribunal may reduce the penalty to the amount` |
| reg 99(4)(b) | 2836 | encoded | `reg 99(4) power`, `reg 99(4) the tribunal has the power to` |
| reg 99(5) | 2837 | encoded | `reg 99(5) tribunal is given by` |
| reg 100 heading | 2838 | inert (reason 1: a heading) | no rule: a heading |
| reg 100(1) | 2839 | fork F-PERIOD | `reg 100(1) the appeal was made in time` |
| reg 100(1)(a) | 2840 | fork F-PERIOD | `reg 100(1) the appeal was made in time` |
| reg 100(1)(b) | 2841 | fork F-PERIOD | `reg 100(1) the appeal was made in time` |
| reg 100(2) | 2842 | encoded | `reg 100(2) the appeal was made in time` |
| reg 100(2)(a) | 2843 | encoded | `reg 100(2) the appeal was made in time` |
| reg 100(2)(b) | 2844 | fork F-PERIOD | `reg 100(2) the appeal was made in time` |
| reg 100(3) | 2845 | encoded | `reg 100(3) the appeal was made in time` |
| reg 100(3)(a) | 2846 | encoded | `reg 100(3) the appeal was made in time` |
| reg 100(3)(a)(i) | 2847 | encoded | `reg 100(3) the appeal was made in time` |
| reg 100(3)(a)(ii) | 2848 | encoded | `reg 100(3) the appeal was made in time` |
| reg 100(3)(b) | 2849 | fork F-PERIOD | `reg 100(3) the appeal was made in time` |
| reg 100(3)(c) | 2850 | encoded | `reg 100(3) the appeal was made in time` |
| reg 100(4) | 2851 | fork F-PERIOD | `reg 100(4) the appeal may be made` |
| reg 100(5) | 2852 | encoded | `reg 100(5) the appeal may be made after the end of the period` |
| reg 100(6) | 2853 | encoded | `reg 100(6) the conclusion date is day` |
| PART 11 | 2854 | inert (reason 1: a heading) | no rule: a heading |
| reg 101 heading | 2855 | inert (reason 1: a heading) | no rule: a heading |
| reg 101 | 2856 | fork F-101-OFFICER | `reg 101 the charge or penalty is a debt due to` (gap: the paragraph is silent on interest on a penalty or charge that is not paid, and no function asks it) |
| reg 102 heading | 2857 | inert (reason 1: a heading) | no rule: a heading |
| reg 102(1) | 2858 | encoded | `reg 102(1) class`, `reg 102(1) the charge may be imposed on` |
| reg 102(1)(a) | 2859 | encoded | `reg 102(1) class`, `reg 102(1) the charge may be imposed on` |
| reg 102(1)(b) | 2860 | encoded | `reg 102(1) class`, `reg 102(1) the charge may be imposed on` |
| reg 102(1)(c) | 2861 | encoded | `reg 102(1) class`, `reg 102(1) the charge may be imposed on` |
| reg 102(1)(d) | 2862 | encoded | `reg 102(1) class`, `reg 102(1) the charge may be imposed on` |
| reg 102(1)(e) | 2863 | encoded | `reg 102(1) class`, `reg 102(1) the charge may be imposed on` |
| reg 102(2) | 2864 | encoded | `reg 102(2) the charge is permitted` |
| reg 102(3) | 2865 | encoded | `reg 102(3) a charge may be levied in respect of each of the premises` |
| reg 102(4) | 2866 | encoded | `reg 102(4) the FCA paid the penalties it received to the Treasury` (gap: paragraph (4) obliges the FCA to pay to the Treasury "amounts received ... by way of penalties imposed under Part 9"; the charges levied under paragraph (1) are not mentioned, so whether the FCA must pay them to the Treasury is not asked (the text is silent)) |
| reg 102(5) | 2867 | encoded | `reg 102(5) the Treasury may give directions to the FCA` |
| reg 102(6) | 2868 | encoded | `reg 102(6) content`, `reg 102(6) the directions may` |
| reg 102(6)(a) | 2869 | encoded | `reg 102(6) content`, `reg 102(6) the directions may` |
| reg 102(6)(b) | 2870 | encoded | `reg 102(6) content`, `reg 102(6) the directions may` |
| reg 102(7) | 2871 | encoded | `reg 102(7) the Treasury paid the sums into the Consolidated Fund` |
| reg 102(8) | 2872 | encoded | `reg 102(8) the expenses are expenses within paragraph (2)` |
| reg 102(8)(a) | 2873 | encoded | `reg 102(8) the expenses are expenses within paragraph (2)` |
| reg 102(8)(b) | 2874 | encoded | `reg 102(8) the expenses are expenses within paragraph (2)` |
| reg 103 heading | 2875 | inert (reason 1: a heading) | no rule: a heading |
| reg 103(1) | 2876 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(a) | 2877 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(b) | 2878 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(c) | 2879 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(d) | 2880 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(e) | 2881 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(f) | 2882 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(g) | 2883 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(h) | 2884 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(i) | 2885 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(j) | 2886 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(k) | 2887 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(l) | 2888 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(m) | 2889 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(n) | 2890 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(o) | 2891 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(p) | 2892 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(q) | 2893 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(r) | 2894 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(s) | 2895 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(t) | 2896 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(1)(u) | 2897 | encoded | `reg 103(1) body`, `reg 103(1) the duty to inform the NCA arises`, `reg 103(1) the body or person informed the NCA as required` |
| reg 103(2) | 2898 | encoded | `reg 103(2) the disclosure breaches a restriction on the disclosure of information` |
| reg 103(3) | 2899 | encoded | `reg 103(3) civil liability arises in respect of the disclosure` |
| reg 104 heading | 2900 | inert (reason 1: a heading) | no rule: a heading |
| reg 104(1) | 2901 | encoded | `reg 104(1) the NCA made arrangements to provide appropriate feedback` |
| reg 104(2) | 2902 | encoded | `reg 104(2) the feedback may be provided in the way` |
| reg 104(3) | 2903 | encoded | `reg 104(3) the feedback may be provided in the form` |
| reg 104(4) | 2904 | encoded | `reg 104(4) the disclosure is a suspicious activity disclosure` |
| reg 104(4)(a) | 2905 | encoded | `reg 104(4) the disclosure is a suspicious activity disclosure` |
| reg 104(4)(b) | 2906 | encoded | `reg 104(4) the disclosure is a suspicious activity disclosure` |
| reg 104A heading | 2907 | inert (reason 1: a heading) | no rule: a heading |
| reg 104A | 2908 | encoded | `reg 104A the provision in relation to the NCA as the United Kingdom's financial intelligence unit is made by` |
| reg 105 heading | 2909 | inert (reason 1: a heading) | no rule: a heading |
| reg 105(1) | 2910 | encoded | `reg 105(1) the Commissioners may disclose the information to the FCA` |
| reg 105(2) | 2911 | encoded | `reg 105(2) the FCA or a recipient must not disclose the information`, `reg 105(2) FCA the prohibition on the FCA`, `reg 105(2) recipient the prohibition on a person who receives the information from the FCA` |
| reg 105(2)(a) | 2912 | encoded | `reg 105(2) the FCA or a recipient must not disclose the information`, `reg 105(2) FCA the prohibition on the FCA`, `reg 105(2) recipient the prohibition on a person who receives the information from the FCA` |
| reg 105(2)(b) | 2913 | encoded | `reg 105(2) the FCA or a recipient must not disclose the information`, `reg 105(2) FCA the prohibition on the FCA`, `reg 105(2) recipient the prohibition on a person who receives the information from the FCA` |
| reg 105(2)(c) | 2914 | encoded | `reg 105(2) the FCA or a recipient must not disclose the information`, `reg 105(2) FCA the prohibition on the FCA`, `reg 105(2) recipient the prohibition on a person who receives the information from the FCA` |
| reg 105(2)(d) | 2915 | encoded | `reg 105(2) the FCA or a recipient must not disclose the information`, `reg 105(2) FCA the prohibition on the FCA`, `reg 105(2) recipient the prohibition on a person who receives the information from the FCA` |
| reg 106 heading | 2916 | inert (reason 1: a heading) | no rule: a heading |
| reg 106 | 2917-2919 | encoded | `reg 106 these Regulations authorise or require the disclosure` |
| reg 107 heading | 2920 | inert (reason 1: a heading) | no rule: a heading |
| reg 107 | 2921-2924 | encoded | `reg 107 place`, `reg 107 the transfer is treated as a transfer of funds within the United Kingdom` (note: Jersey and Guernsey both map to the one constructor `reg 107(a) the Channel Islands`, because the paragraph names "the Channel Islands" and the functions do not tell the two apart) |
| reg 108 heading | 2925 | inert (reason 1: a heading) | no rule: a heading |
| reg 108(1) | 2926 | encoded | `reg 108(1) the Treasury carried out a review and published a report` (gap: the text puts the duty on the Treasury and says nothing of who else may carry out the review, so the inputs ask only whether the Treasury did; "from time to time" fixes no interval, so no function asks whether the review was frequent enough) |
| reg 108(1)(a) | 2927 | encoded | `reg 108(1) the Treasury carried out a review and published a report` |
| reg 108(1)(b) | 2928 | encoded | `reg 108(1) the Treasury carried out a review and published a report` |
| reg 108(2) | 2929 | encoded | `reg 108(2) the first report was published in time` |
| reg 108(3) | 2930 | encoded | `reg 108(3) the subsequent report was published in time` |
| reg 108(4) | 2931 | encoded | `reg 108(4) the review had regard to how the instruments are implemented in other member States` |
| reg 108(4)(a) | 2932 | encoded | `reg 108(4) the review had regard to how the instruments are implemented in other member States` |
| reg 108(4)(b) | 2933 | encoded | `reg 108(4) the review had regard to how the instruments are implemented in other member States` |
| reg 108(4)(c) | 2934-2935 | encoded | `reg 108(4) the review had regard to how the instruments are implemented in other member States` |
| reg 108(5) | 2936 | encoded | `reg 108(5) the report sets out what it must` |
| reg 108(5)(a) | 2937 | encoded | `reg 108(5) the report sets out what it must` |
| reg 108(5)(b) | 2938 | encoded | `reg 108(5) the report sets out what it must` |
| reg 108(5)(c) | 2939 | encoded | `reg 108(5) the report sets out what it must` |
| reg 108(5)(d) | 2940 | encoded | `reg 108(5) the report sets out what it must` |
| reg 108(6) | 2941 | encoded | `reg 108(6) regulatory provision is given by` |
| reg 109 heading | 2942 | inert (reason 1: a heading) | no rule: a heading |
| reg 109 | 2943 | encoded | `reg 109 the amendments relating to these Regulations are made by` |
| reg 110 heading | 2944 | inert (reason 1: a heading) | no rule: a heading |
| reg 110(1) | 2945 | encoded | `reg 110(1) the instrument is revoked` |
| reg 110(2) | 2946 | encoded | `reg 110(2) the old regulations continue to have effect` |
| reg 110(3) | 2947 | encoded | `reg 110(3) a penalty or an offence under the relevant Part of these Regulations has effect` |
| reg 110(4) | 2948 | encoded | `reg 110(4) the conduct is taken to have begun on` |
| reg 110(5) | 2949 | encoded | `reg 110 instrument`, `reg 110(5) the instrument is one of the old money laundering regulations` |
| reg 110(5)(a) | 2950 | encoded | `reg 110 instrument`, `reg 110(5) the instrument is one of the old money laundering regulations` |
| reg 110(5)(b) | 2951 | encoded | `reg 110 instrument`, `reg 110(5) the instrument is one of the old money laundering regulations` |
| reg 110(5)(c) | 2952 | encoded | `reg 110 instrument`, `reg 110(5) the instrument is one of the old money laundering regulations` |
| reg 110(5)(d) | 2953 | encoded | `reg 110 instrument`, `reg 110(5) the instrument is one of the old money laundering regulations` |
| reg 110(5)(e) | 2954 | encoded | `reg 110 instrument`, `reg 110(5) the instrument is one of the old money laundering regulations` |
| reg 110(6) | 2955 | encoded | `reg 110 instrument`, `reg 110(6) the instrument is the old transfer of funds regulations` |
| SCHEDULE 1 | 2956 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2957 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2958 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2959 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2960 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2961 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2962 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2963 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2964 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2965 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2966 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2967 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2968 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2969 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2970 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2971 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2972 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2973 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2974 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2975 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2976 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2977 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| sch 1 item | 2978 | encoded | `sch 1 the body is a professional body listed in Schedule 1` |
| SCHEDULE 2 | 2979 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 chapeau | 2980 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2981 | encoded | `sch 2 item 1 the kind of credit is within lending` |
| sch 2 item | 2982 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2983 | encoded | `sch 2 item 3 the service is within payment services` |
| sch 2 item | 2984 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2985 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2986 | encoded | `sch 2 item 6 instrument`, `sch 2 item 6 the trading is within the item` |
| sch 2 item 6 limb a | 2987 | encoded | `sch 2 item 6 instrument`, `sch 2 item 6 the trading is within the item` |
| sch 2 item 6 limb b | 2988 | encoded | `sch 2 item 6 instrument`, `sch 2 item 6 the trading is within the item` |
| sch 2 item 6 limb c | 2989 | encoded | `sch 2 item 6 instrument`, `sch 2 item 6 the trading is within the item` |
| sch 2 item 6 limb d | 2990 | encoded | `sch 2 item 6 instrument`, `sch 2 item 6 the trading is within the item` |
| sch 2 item 6 limb e | 2991 | encoded | `sch 2 item 6 instrument`, `sch 2 item 6 the trading is within the item` |
| sch 2 item | 2992 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2993 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2994 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2995 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2996 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2997 | encoded | `sch 2 the activity is a listed activity` |
| sch 2 item | 2998 | encoded | `sch 2 the activity is a listed activity` |
| SCHEDULE 3 | 2999 | inert (reason 1: a heading) | no rule: a heading |
| sch 3 item | 3000 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3001 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3002 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3003 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3004 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3005 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3006 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3007 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3008 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3009 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3010 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3011 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3012 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3013 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3014 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3015 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3016 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3017 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3018 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3019 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3020 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3021 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3022 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3023 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3024 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3025 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3026 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3027 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3028 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3029 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3030 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3031 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3032 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3033 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3034 | fork F-SCH3-NUMBERS | `sch 3 paragraph`, `sch 3 the offence is a relevant offence` |
| sch 3 item | 3035 | fork F-SCH3-NUMBERS | `sch 3 para 36 the act is a relevant offence`, `sch 3 the offence is a relevant offence` |
| sch 3 item 36 limb a | 3036 | fork F-SCH3-NUMBERS F-SCH3-36 | `sch 3 para 36 the act is a relevant offence`, `sch 3 the offence is a relevant offence` |
| sch 3 item 36 limb b | 3037 | fork F-SCH3-NUMBERS F-SCH3-36 | `sch 3 para 36 the act is a relevant offence`, `sch 3 the offence is a relevant offence` |
| sch 3 item 36 limb (b)(i) | 3038 | fork F-SCH3-NUMBERS F-SCH3-36 | `sch 3 para 36 the act is a relevant offence`, `sch 3 the offence is a relevant offence` |
| sch 3 item 36 limb (b)(ii) | 3039 | fork F-SCH3-NUMBERS F-SCH3-36 | `sch 3 para 36 the act is a relevant offence`, `sch 3 the offence is a relevant offence` |
| sch 3 item 36 limb (b)(iii) | 3040 | fork F-SCH3-NUMBERS F-SCH3-36 | `sch 3 para 36 the act is a relevant offence`, `sch 3 the offence is a relevant offence` |
| SCHEDULE 3AZA | 3041 | inert (reason 1: a heading) | no rule: a heading |
| sch 3AZA para 1 | 3042-3043 | fork F-3AZA-NUMBERS F-3AZA-INCLUDING | `sch 3AZA para 1 a material discrepancy may arise in relation to the information`, `sch 3AZA the discrepancy is a material discrepancy` |
| sch 3AZA para 2 chapeau | 3044 | fork F-3AZA-NUMBERS | `sch 3AZA para 2 the discrepancy satisfies the condition` |
| sch 3AZA para 2 limb (a) | 3045 | encoded | `sch 3AZA para 2 the discrepancy satisfies the condition` |
| sch 3AZA para 2 limb (b) | 3046 | encoded | `sch 3AZA para 2 the discrepancy satisfies the condition` |
| sch 3AZA para 3 chapeau | 3047 | fork F-3AZA-NUMBERS | `sch 3AZA para 3 form`, `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` |
| sch 3AZA para 3 limb (a) | 3048 | encoded | `sch 3AZA para 3 form`, `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` |
| sch 3AZA para 3 limb (b) | 3049 | encoded | `sch 3AZA para 3 form`, `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` |
| sch 3AZA para 3 limb (c) | 3050 | encoded | `sch 3AZA para 3 form`, `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` |
| sch 3AZA para 3 limb (d) | 3051 | encoded | `sch 3AZA para 3 form`, `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` |
| sch 3AZA para 3 limb (e) | 3052 | encoded | `sch 3AZA para 3 form`, `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` |
| sch 3AZA para 3 limb (f) | 3053 | encoded | `sch 3AZA para 3 form`, `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` |
| sch 3AZA para 3 limb (g) | 3054 | encoded | `sch 3AZA para 3 form`, `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` |

## Fork register (mlr4)

Rulings of 2026-11-04 on the Commons guide and of 2026-11-05 on periods, "where" and scope limits, copied word for word from the briefs:

- **E1.** Do not look for, or propose, a language construct that gathers a legal effect "by name" from every section that gives it. Where several sections give the same legal effect, encode each section's answer on its own (option C). You may, by hand and in plain L4, write one function that gathers the routes to a legal effect where that helps a reader (option B as guidance for hand-gathering only); say in the fork register where you did. The Magna Carta pilot is not to be run.
- **N2.** A flat negative in the text ("shall not", "is not", "no person") counts as the text's no, so the answer is `JUST FALSE`, and where the text names who bears a prohibition, the prohibition (`SHANT`) is derived from that answer. Do not type the Hohfeld kind into the person-facing answer. Record the kinds in `NOTES.md` under `## Jural relations`.
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**How the 2026-11-05 ruling is applied (a design entry; no coverage row is marked as a fork on it, because it touches many rows).**
A `JUST FALSE` that rests on the ruling carries the tag `[ruled 2026-11-05 (a) period]` or `[ruled 2026-11-05 (b) where]` in the module, and the marginal-readings table counts them in two columns of their own.
The rule was applied across the range, not only at the sites a reviewer named.
Where a grant or a power has a "where" condition, a period, or a chapeau that says when the paragraph applies, the function now answers `JUST FALSE` outside it: regulations 66(3), 66(8), 68(2), 69(1), 69(2), 69(3), 70(8), 71(2), 71(4), 74B(1), 74B(2), 74B(3), 74C(20), 76(2), 76(3), 77(2), 78(2), 80(1) to (3), 81(1), 83(1), 84(5), 84(7), 85(4), 85(6), 88(4), 89(4), 92(1) to (4), 96(1), 98(2), 98(5), 98(8), 100(4), 100(5), 110(2) and Schedule 3 paragraph 28.
Each of those answered `NOTHING` in the case concerned before, except Schedule 3 paragraph 28, which had no constructor for the excluded offence; the tests say "was NOTHING" at each changed assertion, so the change is findable.

**Companion functions (design entry).**
A compliance function, such as `reg 95(1) the Commissioners reviewed the decision`, answers `JUST FALSE` when the duty applied and was not done, which means a breach.
It therefore cannot also say "the duty does not arise", because `JUST FALSE` would then read as a breach.
So each duty whose trigger is an "if", "where" or period the text states has a companion, `... the duty ... arises`, that answers `JUST TRUE` when the trigger is met and `JUST FALSE` when it is not (rulings (a) and (b)).
The compliance function keeps `NOTHING` where the duty does not arise, and its `NOTHING-kind` note says so and names the companion.
There are 41 companions: regulations 66(5), 74C(9), 74C(12), 74C(13), 74C(16), 74C(17), 74C(19), 74C(21), 74C(22), 76(5), 81(2), 81(3), 81(1A), 81(6) to (11), 83(1A), 83(2), 84(2) to (4), 84(6), 84(10), 85(1) to (3), 85(5), 85(9), 89(2), 89(3), 94(1), 95(1), 97(2), 98(3), 98(4), 98(6), 98(9) and 103(1).
The seat questions that asked whether a duty is met, where the person is really asking whether it applies, now sit on the companion (regulations 81(2), 81(6), 83(2), 95(1), 97(2)), and regulation 103(1) has both questions ("is my duty to inform the NCA triggered" and "must I inform the NCA").
**One deviation from the obvious assertion, F-95-1.**
An assertion that an acceptance on day 31 gives `JUST FALSE` under regulation 95(1)(b) belongs on the companion `reg 95(1) the duty to review the decision arises`, not on the compliance function `reg 95(1) the Commissioners reviewed the decision`.
The compliance function still answers `NOTHING` there, because `JUST FALSE` from it means the Commissioners breached the duty to review.
The same holds for every other duty in the list above.

**Polarity: where the ruling was not applied (design entry).**
Ruling (b), and the 2026-10-29 rule for an "if", turn an unmet condition into `JUST FALSE` when the question is "may X" or "does the duty arise", because `JUST FALSE` then reads as "no".
They were not applied to a rule whose own answer inside the condition is already `JUST FALSE` (a flat negative): there, an unmet condition answering `JUST FALSE` too would make the text's no apply everywhere, including to cases the text is silent on.
The flat negatives under a "where": regulations 72(3) ("Where a disclosure is made in good faith ... no civil liability arises"), 84(1) (a warning notice given under regulation 81(2)), 86(4) (a person convicted), 95(2) ("P may not notify acceptance of the offer where P has already appealed"), 103(3) (a disclosure in good faith) and 110(3) (where the old regulations continue to have effect).
The other flat negatives, mostly under an "if": regulations 74C(8) and 78(3) (a direction or prohibition that expires "does not affect" the power to impose a new one), 84(9) and 85(8) ("must not be published if"), 86(3) ("is not guilty ... if"), 87(3) ("does not commit an offence ... if"), 89(5) (the places to which paragraphs (1) and (3) do not extend) and 95(3).
For regulation 72(3), `JUST FALSE` on "civil liability arises" for a disclosure not made in good faith would say there is no liability, which the text does not say; outside the condition the function answers `NOTHING`.
The substituted section 133A(1) of FSMA in regulation 93(3)(b) bounds a prohibition by a period (the action must not be taken during the referral period): outside the period, `JUST FALSE` on "the action may be taken" would repeat the prohibition where the text gives no permission and none is withheld, so it answers `NOTHING`.
The timing functions of regulation 100(2) and (3) are `JUST FALSE` for an appeal that is early or late inside the case they are for (a review under regulation 95, or one requested under regulation 97) and `NOTHING` outside that case: a scope limit, ruling (c).

**How the delegated-definitions ruling of 2026-11-05 is applied (design entry).**
(a) No site in this range fits.
Schedules 1 and 2 are closed lists that already answer `JUST FALSE` for a body or activity outside them ("The activities ... are"; Schedule 1 is the table of "Professional Bodies").
Schedule 3 is a bare list: the sentence that refers to it is regulation 26(14), outside this range, and it says "The offences listed in Schedule 3 are relevant offences for the purposes of this regulation", which makes the listed offences relevant and does not hand the definition to the list; so `sch 3 the offence is a relevant offence` keeps `NOTHING` for an offence in no paragraph.
(b) One site: regulation 88(4) ("It is a defence ... to prove that they reasonably believed"): when the person is charged under paragraph (3) and proves neither belief, `reg 88(4) the person has a defence` answers `JUST FALSE`, meaning regulation 88(4) gives no defence on these facts; a person not so charged is outside the provision and gets `NOTHING`.
The seat question is worded "does regulation 88(4) give me a defence on these facts".
(c) The five sites are F-WHEN below; regulation 89(3), which says "whenever", already had a companion; no "upon" occurs in the range.
(d) One site: the substituted section 133A(1) in regulation 93(3)(b) ("must not be taken ... until the reference, and any appeal ..., has been finally disposed of"): the function `... may be taken` is kept (`JUST FALSE` while barred, `NOTHING` afterwards, because the section never says the action may be taken), and a twin `reg 93(3)(b) section 133A(1) the action specified in the decision notice is barred` answers `JUST TRUE` while the bar lasts and `JUST FALSE` once it has ended.
Other "until" wording was left alone: regulation 71(2) ("may be retained until the proceedings are concluded") is a grant with an end, answered `JUST FALSE` after it under the periods ruling; regulations 100(2)(a) and 100(3)(a)(ii) ("may not be made until the conclusion date") are asked as "was the appeal made in time", which is `JUST FALSE` both before the conclusion date and after the window, and never says an appeal has been made; regulations 84(6)(a) and 85(5)(a) ("defer ... until paragraph (5) ceases to apply") are options of a duty, not a bar.

**How the sweep of 2026-11-05 was done.**
Every line of the range (2200-3054) that contains "where" or "when" (60 lines) or a period word, such as "within", "until", "not later than", "N days", "beginning with", "without delay" (58 lines), was read and put in one bucket: flipped to `JUST FALSE` outside the condition or period; given a companion (a duty with a trigger); polarity (above); scope limit (ruling (c): regulations 66(1), 74C(14), 74C(15), 74C(18), 100(2), 100(3)); a "when" or "before" opener (F-WHEN); a function that returns a number or a date, which cannot say `JUST FALSE` (regulations 96(2), 98(7), 110(4) and the fee in 74B(2)(b)); or not a condition at all (a "where" or "when" inside a definition's limb, a list of what a notice must say, or narrative such as "state where documents might be found").
The sweep found six duties that had a trigger and no companion (regulations 84(6), 85(5), 98(3), 98(4), 98(6) and 98(9)); they now have one.
A second sweep took every function that has an "applies" or "arises" answer of another provision as an input and checked what it answers when that input is `JUST FALSE`: it found regulations 69(2) and 69(3), which answered `NOTHING` when regulation 69(1) ("Paragraph (2) applies where") was `JUST FALSE` and now answer `JUST FALSE`.
The rest either answer `JUST FALSE` already (68(2), 74B(2), 76(2), 77(2), 78(2), 87(2)(a), 98(2), 98(5), 98(8), and the companions), are duties whose companion carries the `JUST FALSE` (84(6), 85(5), 97(2), 98(3), 98(4), 98(6), 98(9)), are flat negatives (110(3)), or were left on purpose (67(1), see F-CHAPEAU; `sch 3AZA`, see F-3AZA-INCLUDING).

**Where option B (hand-gathering) was used.**
Five functions gather the routes to one legal effect by hand, in plain L4, so that a reader finds the effect in one place.
Three of them (86, 87 and 89) take the per-section answers as inputs and combine them; two (regulation 73, and regulations 66(4) and 67(1)) restate their sections' conditions over the raw facts.
Every per-section function is also written and tested on its own (option C), so no answer depends on the gathered function:
`reg 73 the statement is protected from use in evidence against the person in criminal proceedings` (regulation 73(1) with the cases in (2) and the exception in (3));
`reg 86(1) and (3) the person is guilty of an offence under regulation 86` (86(1) with the defence in 86(3));
`reg 87(2) P commits an offence` (87(2)(a), (3), (2)(b) and (8));
`reg 89(1) and (5) the body may institute proceedings` (89(1) with the extent in 89(5));
`reg 66(4) and 67(1) the information or documents may be required under regulation 66`.
Nothing in the language gathers by name.

**Forks taken.**
A fork is a place where the text can be read two or more ways with different outcomes.
Each row of the coverage table that rests on a fork says `fork` and names the entry below.
The first column of each entry is the identifier used in the L4 comments.

| id | where | the readings | the one taken, and the text that licenses each |
|---|---|---|---|
| F-OFFICER | reg 65(2) "officer", lines 2206-2210 | (1) The line "a relevant officer;" (2210) is a fourth limb of "officer", so an officer of a local weights and measures authority, or of the Department for the Economy, acting under arrangements, is an officer. (2) The "or" at the end of line 2208 closes the list at three limbs, line 2210 is stray, and a relevant officer is an officer only where another provision says so. | (1). Licence for (1): the rendering prints the limbs of "officer" without their letters, "relevant officer" is defined on the very next line (2211), and the same list in regulation 87(10) (lines 2685-2689) has "a relevant officer" as its fourth limb, after an "or" at line 2688. (Regulation 74(1) also uses the term, which fits either reading.) Licence for (2): the "or" at 2208. The outcome differs for a local-authority officer exercising a power the Regulations give to "an officer" (regulation 66(3) is one). |
| F-ARRANGEMENTS | reg 65(2) "relevant officer", lines 2211-2214; reg 87(10) "relevant officer", lines 2690-2693 | (1) "acting pursuant to arrangements made with the FCA or with the Commissioners for the purposes of these Regulations" qualifies both limbs (Great Britain and Northern Ireland). (2) It qualifies only the Northern Ireland limb, because the comma after "Department for the Economy" in 65(2) (line 2213) attaches it there. | (1). Licence: the line is flush with the list, after the last limb, with no letter of its own, in both definitions; in 87(10) line 2692 ends in a semicolon, which would be odd if the tail qualified only that limb. Licence for (2): the comma at 2213. The outcome differs for a Great Britain officer who acts without arrangements. |
| F-PERIOD | every period counted in days: regs 95(1)(b), 96(2), 98(6), 100(1), 100(2)(b), 100(3)(b), 100(4) | (1) The anchor date is day 0 and "30 days from the date" ends on day 30; "a period of 30 days beginning with the date" counts the anchor as day 1 and ends on day 29. (2) Both phrases end on the same day, whichever convention is chosen for the anchor. | (1). Licence: "from" excludes the day it names, "beginning with" includes it. The text states no counting rule and the Interpretation Act 1978 module is unusable on main (see `## Dependencies`), so the convention is this row's, written at the head of `mlr4-part10.l4`. Every period is a NUMBER of days after the anchor, which is the keel's convention (main has no date-plus-days function). The outcome differs by one day at every deadline. Since the ruling of 2026-11-05 (a), a case outside the period answers `JUST FALSE`: regulations 95(1)(b) (through the companion `reg 95(1) the duty to review the decision arises`, see F-95-1), 96(1), 98(8) and 100(4). |
| F-72-1 | reg 72(1), line 2346 | (1) "except that a lawyer may be required to provide the full name and address of the lawyer's client" excepts only the privilege limb. (2) It excepts both limbs, so a lawyer can be required to give the client's name and address even of excluded material. | (1). Licence: the exception is attached to the sentence's last clause and speaks of "the lawyer's client", which is the privilege setting; "excluded material" is defined in regulation 72(7) (lines 2356-2358) as personal records held in confidence or under a secrecy obligation, which the definition does not tie to a client. The outcome differs for a lawyer holding excluded material. |
| F-86-FINE | regs 86(1)(a)(i) and (b), 87(9)(a)(i) and (b), 88(2)(a)(i) and (b), 88(3)(a)(i) and (b); lines 2646, 2648, 2681, 2683, 2700, 2702, 2705, 2707 | (1) "to a fine" with no figure states no ceiling, so whether a particular fine is within the liability is not answered (NOTHING). (2) A fine in England and Wales, and on indictment, is unlimited, so any fine is within the liability (JUST TRUE). | (1). Licence: the paragraphs for Scotland and Northern Ireland say "not exceeding the statutory maximum", so the text knows how to state a ceiling and does not state one here; the text states no maximum for England and Wales or on indictment. The functions answer JUST FALSE only where the text states the ceiling (Scotland and Northern Ireland, summary conviction). |
| F-101-OFFICER | reg 101, line 2856 | (1) A penalty imposed under regulation 76(3) on an officer is not a "charge or penalty imposed on a relevant person or on a payment service provider", so regulation 101 does not make it a debt (NOTHING). (2) Regulation 101 reaches every penalty the FCA or the Commissioners impose under these Regulations, so an officer's penalty is a debt due to the body that imposed it. | (1). Licence: the words "imposed on a relevant person or on a payment service provider" name the two classes, and an officer is neither. Licence for (2): "under these Regulations" and "respectively". |
| F-SCH3-NUMBERS | Schedule 3, lines 3000-3040 | (1) The rendering prints the 36 paragraphs without numbers; numbering them by position makes line 3000 paragraph 1 and line 3035 ("An act which—") paragraph 36. (2) Some other numbering. | (1). Licence: the cross-reference inside paragraph 36, "any of paragraphs 1 to 34" (line 3037), is consistent with the positional count: 1 to 34 are the offences, 35 (line 3034) is aiding and abetting, 36 is the act abroad.  |
| F-3AZA-NUMBERS | Schedule 3AZA, lines 3042-3054 | (1) Lines 3042-3043 are one paragraph 1, line 3044 with its limbs is paragraph 2 and line 3047 with its limbs is paragraph 3. (2) Lines 3042 and 3043 are paragraphs 1 and 2, so the condition is in paragraph 3 and the forms in paragraph 4. | (1). Licence: line 3043 itself refers to "the condition in paragraph 2" and "a form listed in paragraph 3", and the lines that state those are 3044 and 3047; under (2) both references would point one paragraph too early. |
| F-3AZA-INCLUDING | Schedule 3AZA paragraph 1 (line 3043) | (1) A discrepancy "which satisfies the condition in paragraph 2, including one which is in a form listed in paragraph 3" is material when it meets the condition; a listed form that does not meet the condition is neither said to be material nor said not to be (NOTHING). (2) A listed form is material whether or not it meets the condition. (3) A listed form must also meet the condition. | (1). Licence: "including" marks the listed forms as examples inside the class defined by the condition, not as a second route in. The outcome differs for a listed form (a difference in name, say) that the condition does not reach. Reviewer expected JUST FALSE for a listed form that does not meet the condition (reading (3)); open question. |
| F-69-1 | reg 69(1), lines 2262-2267 | (1) "Paragraph (2) applies where a duly authorised officer ... has reasonable grounds to believe that—" makes the whole where clause the condition: if any limb is missing (the officer lacks grounds, is not a duly authorised officer, or is not acting for a supervisory authority in relation to P), paragraph (2) does not apply and the answer is `JUST FALSE`. (2) Only the grounds are the condition; the officer's status is taken as given, and a case lacking it is silent (`NOTHING`). | (1). Licence: ruling (b), "where" works like "if", and the text puts the officer in the same clause as the grounds. `NOTHING` is kept only where every limb the caller can state holds and an answer another provision gives (regulation 69(4), "duly authorised officer"; regulation 8, "relevant person") is not in. The outcome differs for an officer who is not duly authorised: `JUST FALSE` under (1), `NOTHING` under (2). |
| F-69-2 | reg 69(2), line 2268 | (1) "The officer may, on producing evidence of the officer's authority, at any reasonable time" is a limit on the grant, no "only", so an officer who has not produced evidence, or who comes at an unreasonable time, is outside the grant: `NOTHING` (when paragraph (1) does not apply the answer is `JUST FALSE`, F-CHAPEAU). (2) The same words are a "where"-like condition on the power, so without evidence the answer is `JUST FALSE`. | (1). Licence: "on producing" is a time-and-manner limit on a grant, which ruling (c) leaves at `NOTHING`. Reviewer expected JUST FALSE; open question. |
| F-CHAPEAU | regs 68(2), 69(2), 69(3), 74B(2), 76(2), 77(2), 78(2), 98(2), 98(5) | (1) A paragraph that follows a chapeau saying when the regulation or paragraph "applies if" or "applies where" is governed by it, so when the chapeau fails (the earlier paragraph answers `JUST FALSE`) the grant in the later paragraph is `JUST FALSE`. (2) The chapeau governs only the paragraph that holds it; the grant is silent outside it (`NOTHING`). | (1) for the nine listed. For 69(2) and 69(3) the chapeau is regulation 69(1), "Paragraph (2) applies where": when it answers `JUST FALSE`, "may the officer enter the premises" and "may the officer take copies" are `JUST FALSE` too; the officer's evidence of authority and the reasonable time stay `NOTHING` (F-69-2). Licence: "This regulation applies if" (68(1), 98(1)), "This regulation applies where" (74B(1)), "Paragraph (2) applies if" (76(1), 77(1), 78(1)) name the paragraph that carries the grant. Where the earlier paragraph's answer is not in, the function answers `NOTHING`. NOT extended: regulation 98(7) (it returns a date, not a yes or no) and regulation 67(1) (67(2) says "This paragraph applies if", so 67(1) reads as a scope limit). Regulation 74B(3) is F-WHEN. |
| F-77-4 | reg 77(4), line 2493 | (1) "may not exceed 12 months" is a cap, not a grant: above 12 months `JUST FALSE`, at or below it `NOTHING` (regulation 77(2) is the grant). (2) A period of 12 months or less is permitted (`JUST TRUE`), and the cap is the only limit. A cancellation, which has no period, is not asked: the function takes a number of months. | (1). Licence: the paragraph limits the period of a "suspension, limitation or other restriction" and says nothing of a cancellation (regulation 77(2)(a)(i) lists "cancel or suspend" together). Reviewer expected JUST FALSE; open question. |
| F-77-79 | reg 77 (line 2471) and reg 79 (line 2512) | (1) Regulation 77 gives the powers to the FCA and regulation 79 lets "a designated supervisory authority" exercise the powers in regulations 76, 77 and 78 in relation to the same contravention, so the Commissioners and the other authorities may act under 77 through 79. (2) Regulation 77 is the FCA's alone. | (1) is what the text says, but no input names the acting authority: each function answers for the power as the regulation words it, and `reg 79 the powers may be exercised in relation to the same contravention` answers regulation 79 on its own (option C). Which authority acts is not asked. |
| F-SCH3-36 | Schedule 3 paragraph 36, lines 3035-3040 | (1) The paragraph is a list entry in Schedule 3 ("An act which ... would have constituted an offence under any of paragraphs 1 to 34"): an act that fails the test is not covered here (`NOTHING`). (2) The paragraph is a definition of what is a relevant offence abroad, so an act failing the test is not a relevant offence (`JUST FALSE`). | (1). Licence: Schedule 3 is a list, regulation 26(14) (line 761) says "The offences listed in Schedule 3 are relevant offences" with no "only", and the paragraph has no "means". Reviewer expected JUST FALSE; open question. |
| F-WHEN | regs 74B(3) (line 2394), 81(1) (line 2529), 81(1A) (line 2538), 83(1) (line 2579), 83(1A) (line 2588) | (1) A paragraph that opens "When acting under paragraph (2)(a)", "When determining the type of sanction ... including where appropriate" or "Before imposing a sanction" is limited to that case by a word of time, not "where" or "if", so outside the case the text is silent (`NOTHING`, ruling (c)). (2) "When" and "before" count as "where" (ruling of 2026-11-05 (c)), so outside the case the answer is `JUST FALSE`. | (2). Ruled 2026-11-05 (typed 06:04:54.553Z). 74B(3), 81(1) and 83(1) answer `JUST FALSE` in the function itself (a grant, and a "must take into account"); in 81(1) and 83(1) the "where appropriate" is a second "where", so a circumstance that is not appropriate also answers `JUST FALSE`. 81(1A) and 83(1A) are duties ("Before X, a person must ..." works like "when X"): each has a companion, `reg 81(1A) the duty to check whether P has criminal convictions arises` and `reg 83(1A) ...`, that is `JUST TRUE` when the sanction is imposed and `JUST FALSE` when it is not, and the compliance function keeps `NOTHING` there. Tagged `[ruled 2026-11-05 (b) where (read from "when")]` or `(read from "before")` and counted in the ruled (b) column of the marginal table. |

**A name-only fork (no outcome in this range differs).**
F-SCH2-NUMBERS: Schedule 2 prints thirteen items without numbers (lines 2981-2998; the five instruments under the trading item are its sub-items).
The three rules that need an item number are named `sch 2 item 1`, `sch 2 item 3` and `sch 2 item 6`, by position.
Regulation 10 cites points of Schedule 2 up to 15 (the keel's fork F4 records that); nothing in regulations 65 to 110 turns on a point number, so no row of this range is a fork on it.

## Jural relations (mlr4)

The Hohfeld kinds live here and nowhere in the person-facing answers (ruling N2).
Each row names the holder, the kind, the other party and the provision's L4 function.
"Power / liability" means the holder can change the other party's position by acting, and the other party is exposed to it.
"Duty / claim" means the bearer must do (or must not do) something and the other party may demand it.
"Privilege / no-claim" means the holder may do it and the other party cannot complain.
"Immunity / disability" means the other party cannot change the holder's position.
A row for a provision that only defines, lists or points creates no relation and says so.
In the last column, `reg 77(4)` to `reg 77(8)` means the functions whose names start with those labels, and `...` stands for the rest of a name.

| provision | holder | kind | other party | what | L4 |
|---|---|---|---|---|---|
| 65 | none | definition | | premises, tribunal, officer, relevant officer, connected person (a pointer to Schedule 5) | `reg 65(1) the place is premises`, `reg 65(2) the person is an officer`, `reg 65(3) the person is a connected person` |
| 66(1), (3) | supervisory authority; an officer authorised in writing | power | P (a relevant person, payment service provider or connected person) | to require information, documents or attendance by notice | `reg 66(1) the supervisory authority may require P`, `reg 66(3) the officer may require P` |
| 66(2), (3) | P | duty | the supervisory authority or officer | to provide or produce within the period and at the place, or without unreasonable delay | `reg 66(2)(a) P must provide the information or produce the documents`, `reg 66(3) P provided or produced without unreasonable delay` |
| 66(5) | the supervisory authority or officer | duty | P | to set out the reasons, unless not permitted to disclose them | `reg 66(5) the notice complies with the requirement to set out the reasons` |
| 66(6) | the supervisory authority | power | P | to require legible form and the form of provision | `reg 66(6)(a) ...`, `reg 66(6)(b) ...` |
| 66(7) | the holder of a lien | immunity | the supervisory authority | production does not affect a lien | `reg 66(7) the production of the document affects a lien on it` |
| 66(8) | the supervisory authority | power | a third person who holds the document | to exercise the power against the third person | `reg 66(8) the supervisory authority may exercise the power in relation to the third person` |
| 67(1), (3), (4) | supervisory authority | power / privilege | a foreign authority | to exercise the reg 66 power on a request; to weigh the matters in (3); to insist on undertakings | `reg 67(1) ...`, `reg 67(3) ...`, `reg 67(4) ...` |
| 68(2) | supervisory authority | privilege | a foreign authority | to request assistance | `reg 68(2) the supervisory authority may request the assistance of the foreign authority` |
| 68(3), (4) | the supervisory authority | disability, lifted by the foreign authority's consent | the foreign authority | the material may only be used for the purpose provided or for proceedings | `reg 68(3) the use made of the information or documents is permitted`, `reg 68(4) paragraph (3) applies` |
| 69 | a duly authorised officer | power | P (the relevant person or provider) | to enter and inspect premises, observe business, inspect and copy documents | `reg 69(1) paragraph (2) applies`, `reg 69(2) the officer may`, `reg 69(3) ...` |
| 70(1), (7) to (10) | a justice; the executing officer | power | the occupier of the premises | to issue a warrant; to enter, search, seize, take possession, require explanations | `reg 70(1) the justice may issue a warrant`, `reg 70(7) the warrant authorises the executing officer` |
| 71(1), (2) | the authority holding seized material | privilege | the owner | to retain it while necessary, and until the proceedings conclude | `reg 71(1) ...`, `reg 71(2) ...` |
| 71(3), (4) | the owner of seized material | power | the court | to apply for delivery to a court; the court may order as it thinks fit | `reg 71(3) the person may apply for delivery to`, `reg 71(4) ...` |
| 72(1), (4) | P | immunity | the supervisory authority and officers | cannot be required to produce excluded material or privileged information (a lawyer must give the client's name and address); a warrant gives no right to seize privileged or excluded material | `reg 72(1) the person may be required`, `reg 72(4) the warrant confers the right to seize the material` |
| 72(2), (3) | a person who provides information in accordance with the regulations | immunity | any person bound by a restriction on disclosure | no breach of a restriction; no civil liability if in good faith | `reg 72(2) ...`, `reg 72(3) civil liability arises in respect of the disclosure` |
| 73 | P | immunity | the prosecution | a statement made on a requirement under regulation 66(1)(c), 69(2)(e), 70(7)(e) or 74B(6) cannot be used in evidence against P in criminal proceedings, save in the cases in (2) | `reg 73(1) ...`, `reg 73(2) paragraph (1) applies`, `reg 73 the statement is protected ...` |
| 74(1) to (3) | a relevant officer | power / liability | the FCA or the Commissioners | may exercise powers only under arrangements; acts are treated as the FCA's or the Commissioners' | `reg 74(1) R may exercise powers under this Part`, `reg 74(2)(a) ...` |
| 74(4) | R | duty (a prohibition) | the FCA or the Commissioners | not to disclose the information except to the named recipients, with approval or under a duty | `reg 74(4) R must not disclose the information`, `reg 74(4) the prohibition on R` |
| 74A | a cryptoasset business | duty | the FCA | to provide the information the FCA directs, at the times, in the form and verified as directed | `reg 74A(1) ...`, `reg 74A(2) ...` |
| 74B | the FCA | power | a relevant person that is a cryptoasset business | to require a skilled person's report, to appoint one and recover the fee; to require reports and assistance | `reg 74B(2) the FCA may take the step`, `reg 74B(2)(b) the fee payable by the relevant person is`, `reg 74B(3) the FCA may require` |
| 74B(6) | the relevant person, connected persons | duty | the skilled person | to give all assistance required | `reg 74B(6) the person gave the skilled person the assistance` |
| 74C(1) to (6) | the FCA | power / liability | a cryptoasset business | to impose, vary and rescind directions, on its own initiative or on request | `reg 74C(1)` to `reg 74C(6)` |
| 74C(7) to (22) | the FCA | duty | a cryptoasset business; the PRA | to consult the PRA, to give written notices of a stated content, to publish the fact of a rescission and the status of an appeal; the business has a claim to notice, to make representations and to refer to the Upper Tribunal | `reg 74C(7)` to `reg 74C(22)` |
| 75 | none | definition / pointer | | "relevant requirement" is given by Schedule 6 | `reg 75 the requirement is a relevant requirement` |
| 76(1), (2) | a designated supervisory authority | power / liability | P | to impose a penalty or publish a censuring statement | `reg 76(1) paragraph (2) applies`, `reg 76(2) the designated supervisory authority may` |
| 76(3) | a designated supervisory authority | power / liability | an officer who was knowingly concerned | to impose a penalty | `reg 76(3) the designated supervisory authority may impose a penalty on the officer` |
| 76(4) | P | immunity | the authority | no penalty if the authority is satisfied P took all reasonable steps and exercised all due diligence | `reg 76(4) the designated supervisory authority may impose a penalty on P`, `reg 76(4) the prohibition on the designated supervisory authority` |
| 76(5), (6) | the FCA; the authority | duty | the PRA; P | to consult the PRA before a penalty on a PRA-authorised person; to consider whether P followed guidance | `reg 76(5) the FCA consulted the PRA`, `reg 76(6) the authority considered whether P followed the guidance` |
| 76(7) | the imposing authority | claim | P | the penalty is payable to it | `reg 76(7) the penalty is payable to` |
| 77 | the FCA | power / liability | a relevant person or payment service provider | to cancel, suspend or limit permissions and registrations; to restrict | `reg 77(1) paragraph (2) applies`, `reg 77(2) the FCA may take the measure`, `reg 77(4)` to `reg 77(8)` |
| 78 | a designated supervisory authority | power / liability | an officer | to prohibit management roles, temporarily or permanently | `reg 78(1) paragraph (2) applies`, `reg 78(2) ...` |
| 78(5) | a relevant person or payment service provider | duty | the supervisory authority | to take reasonable care that an individual under a prohibition is not given, and does not continue in, a management role | `reg 78(5) the person took reasonable care` |
| 79 | a designated supervisory authority | power | P | to exercise any one or more of the powers in regulations 76, 77 and 78 for the same contravention | `reg 79` |
| 80 | a designated supervisory authority | power (to apply); the court has power to order | P or any person | injunction, remedial steps, restraint of assets | `reg 80(1)` to `reg 80(5)` |
| 81 | the FCA | duty | P | to take into account the listed circumstances, check convictions, give a warning notice, consult the PRA, give a decision notice without undue delay; the notices contain what the section lists | `reg 81(1)` to `reg 81(13)` |
| 82 | the FCA | duty | P | FSMA procedure applies as modified; final notices contain what the section lists | `reg 82(1)` to `reg 82(3)` |
| 83 | the Commissioners | duty | P | to take into account the listed circumstances, check convictions, give notice of the decision with the stated content | `reg 83(1)` to `reg 83(4)` |
| 84(1) | the FCA; any person to whom the warning notice is given or copied | duty (a prohibition) | P | not to publish the warning notice or details of it | `reg 84(1) ...`, `reg 84(1) FCA the prohibition on the FCA`, `reg 84(1) recipient the prohibition on a person to whom the notice is given or copied` |
| 84(2) to (10) | the FCA | duty, with privileges to defer, anonymise or refrain | P; the public | to publish information about the matter, and the appeal's status and outcome; to keep it for five years | `reg 84(2)` to `reg 84(10)` |
| 85 | the Commissioners | duty, with privileges | P; the public | the same, for the Commissioners | `reg 85(1)` to `reg 85(9)` |
| 86 | P | duty (not to contravene a relevant requirement), with liability | the Crown | offence, with the stated imprisonment and fine; defence of reasonable steps; no double sanction | `reg 86(1)` to `reg 86(4)`, `reg 86(1) and (3) ...` |
| 87 | P | duty (a prohibition) | the Crown | not to prejudice an investigation or falsify or destroy documents, with defences | `reg 87(1)` to `reg 87(10)` |
| 88 | P | duty (a prohibition) | the Crown | not to give false or misleading information; not to disclose information in contravention; defence of reasonable belief | `reg 88(1)` to `reg 88(4)` |
| 89, 90 | the Commissioners (by order), a local weights and measures authority, the Department for the Economy, the Director of Public Prosecutions, the Director of Public Prosecutions for Northern Ireland | power (to institute proceedings) | the accused | who may prosecute (regulation 89(1)), and where (regulation 90) | `reg 89(1)` to `reg 89(6)`, `reg 90(1)` to `reg 90(3)` |
| 91 | none | procedure | partnerships and unincorporated associations | proceedings are brought in the name of the partnership or association | `reg 91(1)` to `reg 91(4)(b)` |
| 92 | the officer of a body | liability | the Crown | the officer is guilty where the offence was committed with consent, connivance or neglect | `reg 92(1)` to `reg 92(4)` |
| 93 | a person subject to an FCA decision | power | the Upper Tribunal | to appeal | `reg 93(1)` to `reg 93(3)(b) section 133A(2) ...` |
| 94 | the Commissioners | power | P | to offer a review by notice at the time of the decision | `reg 94(1)`, `reg 94(2)` |
| 95 | P; the Commissioners | power (to accept); duty (to review); duty (a prohibition) once P has appealed | each other | accept within 30 days; the Commissioners must review; P may not accept (95(2)) and the Commissioners must not review (95(3)) once P has appealed | `reg 95(1)` to `reg 95(3)`, `reg 95(2) the prohibition on P`, `reg 95(3) the prohibition on the Commissioners` |
| 96 | the Commissioners | power | P | to extend the relevant period by notice, more than once | `reg 96(1)` to `reg 96(4)` |
| 97 | P; the Commissioners | power (to request); duty (to review out of time) | each other | review out of time if there is a reasonable excuse and no unreasonable delay | `reg 97(1)`, `reg 97(2)` |
| 98 | the Commissioners | duty | P | to review, have regard to the earlier steps and representations, and give notice of conclusions within 45 days; if not, the decision is treated as upheld | `reg 98(1)` to `reg 98(9)` |
| 99 | a person subject to a Commissioners' decision; the tribunal | power (to appeal); power (to quash, vary, substitute, reduce) | each other | appeal in accordance with regulation 100 | `reg 99(1)` to `reg 99(5)` |
| 100 | the person appealing | power and disability (time limits) | the tribunal | when an appeal may and may not be made, and with permission | `reg 100(1)` to `reg 100(6)` |
| 101 | the FCA; the Commissioners | claim | P | a charge or penalty is a debt, recoverable accordingly | `reg 101 the charge or penalty is a debt due to` |
| 102 | the FCA; the Commissioners | power; duty | the classes listed; the Treasury | to levy charges (up to the cost of functions); the FCA pays penalties to the Treasury; the Treasury may direct and pays into the Consolidated Fund | `reg 102(1)` to `reg 102(8)` |
| 103 | the bodies listed; any person | privilege / immunity | the NCA; the person bound by a restriction | disclosure to the NCA is not a breach of a restriction and gives no civil liability if in good faith | `reg 103(1)` to `reg 103(3)` |
| 104 | the NCA | duty | those who make suspicious activity disclosures | to make arrangements for appropriate feedback at least once a year | `reg 104(1)` to `reg 104(4)`, `reg 104A` |
| 105 | the Commissioners; the FCA and any recipient | power; duty (a prohibition) | the FCA; the person identifiable | to disclose to the FCA; the FCA and recipients not to disclose, save for four purposes | `reg 105(1)`, `reg 105(2) ...` |
| 106 | none | limit on every disclosure power | | these Regulations do not authorise or require a disclosure in contravention of the data protection legislation, or one prohibited by Parts 1 to 3 or 5 to 7 of the Investigatory Powers Act 2016 | `reg 106` |
| 107 | none | deeming | | a transfer is treated as within the United Kingdom | `reg 107` |
| 108 | the Treasury | duty | none named | to review the regulatory provision and publish a report: the first before 26th June 2022, later ones at intervals not exceeding 5 years | `reg 108(1)` to `reg 108(6)` |
| 109 | none | pointer | | transitional provision is in Schedule 7 | `reg 109` |
| 110 | none | revocation and saving | | the old money laundering and transfer of funds regulations are revoked; they continue for conduct before the commencement date | `reg 110(1)` to `reg 110(6)` |
| Schedules 1, 2, 3, 3AZA | none | lists and definitions | | the professional bodies, the listed activities, the relevant offences, the material discrepancies | `sch 1 ...`, `sch 2 ...`, `sch 3 ...`, `sch 3AZA ...` |

## Marginal readings for a lawyer (mlr4)

These are the readings the brief marks "for a lawyer, not for the encoder to decide".
They are the status quo of this row, not a finding about the law.

- **(a)** A failed "if", "only if", "unless" or "except" condition, an "is" or "means" definition and a flat negative count as the text's no (`JUST FALSE`), clause by clause, within the provision that holds them.
  The other reading: "if A then B" does not itself say "if not A then not B", so a failed condition is silence and the answer outside the case is `NOTHING`.
  A sentence that starts with "If X, Y may" is treated the same way: outside X the answer is `JUST FALSE`, except where Y is itself a flat negative ("must not be published if", "is not guilty if"), which keeps `NOTHING` outside the case it names (see "Polarity" in the fork register).
- **(c)** A "must" that has not been done is the text's no.
  The other reading: an unperformed duty is a breach, not a "no", and the function should answer `NOTHING` until a deadline or breach is shown.
  Every deadline function (regulations 66(2)(a), 95(1), 98(6) and 100(1) to (3)) rests on this reading for its late branches.
- **(b)** A grant or prohibition limited by its own wording, where the limit is a scope and the text has no "only", is not the text's no: outside the limit the function answers `NOTHING`.
  The other reading: a stated limit is itself a negative ("only if the tribunal gives permission"), so outside it the answer is `JUST FALSE`.
  Most of the `NOTHING` branches in this row rest on (b).
  A stated period and a "where" condition used to rest on (b) as well; they are ruled (below) and no longer do.

**Rulings of 2026-11-05 (Meng: "i agree with your lean: no for a and b; nothing for c.")** are not marginal readings: they are decided, and they have columns of their own in the table.

- **Ruled (a), a period.** Where the text fixes a period in its own words ("within", "not later than", "begins from ... until", "30 days after"), outside the period the answer is `JUST FALSE`.
- **Ruled (b), "where".** A "where" condition that is not met answers `JUST FALSE`, like "if".
- **Ruled (c), a scope limit with no "only".** Outside the scope the answer is `NOTHING`.

- **Ruled, "when", "upon", "whenever", "before".** They count as "where", so an unmet one answers `JUST FALSE`.
- **Ruled, a defence.** "It is a defence ... to prove that X" with X not proved answers `JUST FALSE`, worded "this regulation gives no defence on these facts".
- **Ruled, a bar.** "Must not ... until X" is encoded as the bar: `JUST TRUE` before X, `JUST FALSE` after X, and never a claim that the thing has happened.

The letters of the rulings are not the letters of the marginal readings above: the last three columns of the table are the ruled (a), the ruled (b) with its "when" and "before" readings, and the defence and bar rulings.

The table lists every function that has at least one branch resting on a marginal reading, with the number of branches under each.
A blank cell means none.
It is generated from the `-- FALSE-kind ... [marginal (a)|(c)]`, `[ruled 2026-11-05 (a) period]` and `[ruled 2026-11-05 (b) where]` tags and the `-- NOTHING-kind (limited by its own wording)` comments in the modules, so the comments are the record and this table is a count of them.

| module | function | (a) failed condition, definition or flat negative = no | (c) unperformed must = no | (b) limit in its own wording = NOTHING | ruled 2026-11-05 (a): period the text fixes = no outside it | ruled 2026-11-05 (b): unmet "where" or "when" = no | ruled 2026-11-05: unproved defence, or a bar that has ended = no |
|---|---|---|---|---|---|---|---|
| mlr4-part8 | `reg 65(3) the person is a connected person` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 66(1) the supervisory authority may require P` |  |  | 3 |  |  |  |
| mlr4-part8 | `reg 66(2)(a) the information or documents were provided or produced in time` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 66(2)(b) the information or documents were provided or produced at the specified place` |  | 1 |  |  |  |  |
| mlr4-part8 | `reg 66(3) the officer may require P` | 2 |  |  |  |  |  |
| mlr4-part8 | `reg 66(3) P provided or produced without unreasonable delay` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 66(4) the powers in regulation 66 may be exercised` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 66(5) the duty to set out the reasons arises` |  |  |  |  | 1 |  |
| mlr4-part8 | `reg 66(5) the notice complies with the requirement to set out the reasons` |  | 1 |  |  |  |  |
| mlr4-part8 | `reg 66(6)(a) the supervisory authority may require the information to be produced in legible form` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 66(6)(b) the supervisory authority may require the information to be provided in the form` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 66(7) the production of the document affects a lien on it` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 66(8) the supervisory authority may exercise the power in relation to the third person` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 67(1) the supervisory authority may exercise the power in regulation 66 to meet the request` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 67(2) paragraph (2) applies to the request` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 67(4) the supervisory authority may decide not to exercise its powers` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 66(4) and 67(1) the information or documents may be required under regulation 66` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 68(1) this regulation applies` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 68(2) the supervisory authority may request the assistance of the foreign authority` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 68(3) the use made of the information or documents is permitted` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 68(4) paragraph (3) applies` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 69(1) paragraph (2) applies` |  |  |  |  | 1 |  |
| mlr4-part8 | `reg 69(2) the officer may` |  |  | 1 |  | 1 |  |
| mlr4-part8 | `reg 69(3) the officer may take copies of, or make extracts from, the documents` |  |  | 1 |  | 1 |  |
| mlr4-part8 | `reg 70(1) the justice may issue a warrant` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 70(2) the application meets the requirements` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 70(3) the first set of conditions is satisfied` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 70(4) the second set of conditions is satisfied` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 70(5) the third set of conditions is satisfied` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 70(6) the fourth set of conditions is satisfied` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 70(7) the warrant authorises the executing officer` |  |  | 2 |  |  |  |
| mlr4-part8 | `reg 70(8) the warrant authorises the executing officer to take possession of the information in legible form` |  |  | 1 |  | 1 |  |
| mlr4-part8 | `reg 70(9) a warrant may have the feature` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 70(10) the accompanying person may exercise the powers in paragraph (7)` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 70(11) sections 15(5) to (8) and 16(3) to (12) of the Police and Criminal Evidence Act 1984 apply to the warrant` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 70(12) Articles 17(5) to (8) and 18(3) to (12) of the Police and Criminal Evidence (Northern Ireland) Order 1989 apply to the warrant` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 71(1) the seized material may be retained` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 71(2) the seized material may be retained until the proceedings are concluded` | 1 |  |  | 1 |  |  |
| mlr4-part8 | `reg 71(3) the person may apply for delivery to` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 71(4) the court may make such order as it thinks fit` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 71(5) the order affects the right to take legal proceedings against the person in possession for the recovery of the material` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 72(5) the material is privileged material` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 72(6)(b) the person is entitled to refuse on the grounds of confidentiality of communication` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 72(1) the person may be required` | 2 |  | 1 |  |  |  |
| mlr4-part8 | `reg 72(2) providing the information breaches a restriction on the disclosure of information` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 72(3) civil liability arises in respect of the disclosure` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 72(4) the warrant confers the right to seize the material` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 73(1) the statement may be used in evidence against the person in criminal proceedings` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 73(2) paragraph (1) applies` | 6 |  |  |  |  |  |
| mlr4-part8 | `reg 73(3) the statement may be used by virtue of paragraph (2)(f)` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 73 the statement is protected from use in evidence against the person in criminal proceedings` | 2 |  | 1 |  |  |  |
| mlr4-part8 | `reg 74(1) R may exercise powers under this Part` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74(2)(a) anything done by R is treated as done by an officer of the FCA` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74(2)(b) anything done by R is treated as done by an officer of Revenue and Customs` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74(3) paragraph (2) applies` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74(4) R must not disclose the information` | 2 |  | 1 |  |  |  |
| mlr4-part8 | `reg 74A(1) the cryptoasset business must provide the information to the FCA` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 74A(2) the information was provided as the FCA directed` |  | 1 |  |  |  |  |
| mlr4-part8 | `reg 74B(1) this regulation applies` |  |  |  |  | 1 |  |
| mlr4-part8 | `reg 74B(2) the FCA may take the step` |  |  | 1 |  | 1 |  |
| mlr4-part8 | `reg 74B(2)(b) the fee payable by the relevant person is` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 74B(3) the FCA may require` |  |  |  |  | 1 |  |
| mlr4-part8 | `reg 74B(4) the FCA gave notice in writing of the appointment` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74B(5) the person is a skilled person` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74B(6) the person gave the skilled person the assistance` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(1) the FCA may exercise its powers of direction` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 74C(5) the FCA may on its own initiative` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 74C(6) the FCA may on the request of the cryptoasset business` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 74C(7) the FCA consulted the PRA as required` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(8) the direction may be expressed to expire at the end of the period` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 74C(8) the expiry of the direction affects the FCA's power to impose a new direction` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 74C(9) the duty to give the notice in writing arises` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74C(9) the FCA gave the notice in writing` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(10) the notice contains what it must` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(11) the FCA may extend the period` |  |  | 1 |  |  |  |
| mlr4-part8 | `reg 74C(12) the duty to give notice of the decision not to rescind arises` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74C(12) the FCA gave the notice in writing of its decision not to rescind` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(13) the duty to give notice of the decision on the representations arises` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74C(13) the FCA gave the notice in writing of its decision on the representations` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(14) the notice informs the cryptoasset business of its right to refer the matter` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(15) the notice complies with paragraph (10)` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(16) the duty to indicate the procedure on a reference arises` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74C(16) the notice gives an indication of the procedure on a reference` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(17) the duty to give the notice in writing of the direction imposed or varied on request arises` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74C(17) the FCA gave the notice in writing of the direction imposed or varied on request` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(18) the notice contains what it must` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(19) the duty to give the notice in writing of the rescission arises` | 1 |  |  |  |  |  |
| mlr4-part8 | `reg 74C(19) the FCA gave the notice in writing of the rescission` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(20) the FCA may publish information about the notice` | 1 |  | 1 |  |  |  |
| mlr4-part8 | `reg 74C(21) the duty to publish the fact of the rescission arises` |  |  |  |  | 1 |  |
| mlr4-part8 | `reg 74C(21) the FCA published the fact of the rescission` |  | 1 | 1 |  |  |  |
| mlr4-part8 | `reg 74C(22) the duty to publish the status of the appeal and its outcome arises` |  |  |  |  | 1 |  |
| mlr4-part8 | `reg 74C(22) the FCA published the status of the appeal and its outcome` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 75 the requirement is a relevant requirement` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 76(1) paragraph (2) applies` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 76(2) the designated supervisory authority may` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 76(3) the designated supervisory authority may impose a penalty on the officer` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 76(4) the designated supervisory authority may impose a penalty on P` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 76(5) the duty to consult the PRA arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 76(5) the FCA consulted the PRA` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 76(6)(b) the guidance is guidance the authority must consider` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 76(6) the authority considered whether P followed the guidance` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 76(7) the penalty is payable to` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 77(1) paragraph (2) applies` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 77(2) the FCA may take the measure` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 77(3)(a) the thing is a permission` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 77(4) the period of the suspension, limitation or other restriction is permitted` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 77(5) the suspension may relate to the thing` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 77(7) the FCA may` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 78(1) paragraph (2) applies` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 78(2) the designated supervisory authority may impose the measure` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 78(3) the prohibition may be expressed to expire at the end of the period` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 78(3) the expiry of the temporary prohibition affects the power to impose a new prohibition under paragraph (2)(a)` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 78(4) the prohibition may be expressed to be in` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 78(5) the person took reasonable care` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 79 the powers may be exercised in relation to the same contravention` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 80(1) the court may make an order restraining the contravention` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 80(2) the court may make an order requiring the person to take steps to remedy the contravention` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 80(3) the court may make an order restraining the person from disposing or otherwise dealing with the assets` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 81(1) the FCA must take the circumstance into account` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 81(1A) the duty to check whether P has criminal convictions arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 81(1A) the FCA checked whether P has criminal convictions` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(2) the duty to give P a warning notice arises` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 81(2) the FCA gave P a warning notice` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(3) the duty to consult the PRA arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 81(3) the FCA consulted the PRA` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(5) the warning notice contains what it must` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(6) the duty to give P a decision notice arises` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 81(6) the FCA gave P a decision notice without undue delay` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(7) the duty to set out the terms of the statement arises` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 81(7) the decision notice sets out the terms of the statement` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(8) the duty to specify the amount of the penalty arises` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 81(8) the decision notice specifies the amount of the penalty` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(9) the duty to include what paragraph (9) requires arises` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 81(9) the decision notice contains what it must` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(10) the duty to state the date of the cancellation arises` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 81(10) the decision notice states the date of the cancellation` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 81(11) the duty to set out the terms of the prohibition arises` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 81(11) the decision notice sets out the terms of the prohibition` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 82(1) the section of FSMA applies to the notice` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 82(2)(a) the final notice about a cancellation, suspension, limitation or other restriction contains what it must` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 82(2)(a) the final notice about a prohibition contains what it must` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 83(1) the Commissioners must take the circumstance into account` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 83(1A) the duty to check whether P has criminal convictions arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 83(1A) the Commissioners checked whether P has criminal convictions` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 83(2) the duty to give P a notice arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 83(2) the Commissioners gave P a notice` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 83(3) the notice contains what it must` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 83(4) the notice about a penalty contains what it must` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 84(1) the FCA or a person to whom the warning notice is given or copied may publish it or any details concerning it` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 84(2) the duty to publish information about the matter arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 84(2) the FCA published information about the matter` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 84(3) the duty to publish the status of the appeal and its outcome arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 84(3) the FCA published the status of the appeal and its outcome` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 84(4) the duty to publish the type and nature of the breach arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 84(4) the FCA published the type and nature of the breach and the identity of the person` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 84(5) the information must be published in accordance with paragraph (6)` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 84(6) the duty to defer the publication or publish it anonymously arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 84(6) the FCA deferred or published anonymously` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 84(7) the FCA may make arrangements as to the publication of information` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 84(8) the FCA may make arrangements for the postponed publication of personal data` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 84(9) the information about the matter may be published` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 84(10) the duty to keep the information on the website arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 84(10) the information remained on the website for long enough` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 85(1) the duty to publish information about the matter arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 85(1) the Commissioners published information about the matter` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 85(2) the duty to publish the status of the appeal and its outcome arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 85(2) the Commissioners published the status of the appeal and its outcome` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 85(3) the duty to publish the type and nature of the breach arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 85(3) the Commissioners published the type and nature of the breach and the identity of the person` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 85(4) the information must be published in accordance with paragraph (5)` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 85(5) the duty to defer the publication or publish it anonymously arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 85(5) the Commissioners deferred or published anonymously` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 85(6) the Commissioners may make arrangements as to the publication of information` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 85(7) the Commissioners may make arrangements for the postponed publication of personal data` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 85(8) the information about the matter may be published` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 85(9) the duty to keep the information on the website arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 85(9) the information remained on the website for long enough` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 86(1) the person is guilty of an offence` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 86(1) the term of imprisonment is within the liability` | 2 |  |  |  |  |  |
| mlr4-part9 | `reg 86(1) the fine is within the liability` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 86(2)(b) the guidance is guidance the court must consider` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 86(2) the court decided whether the person followed the guidance` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 86(3) the person is guilty of an offence under this regulation` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 86(1) and (3) the person is guilty of an offence under regulation 86` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 86(4) the person is liable to a sanction under Chapter 2 of this Part` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 87(1) this regulation applies` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 87(2)(a) P commits an offence by a disclosure likely to prejudice the investigation` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 87(2)(b) P commits an offence by falsifying, concealing or destroying documents` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 87(4) the conduct is criminal conduct` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 87(5) the person benefits from the conduct` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 87(6) the disclosure falls within this paragraph` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 87(7) the disclosure falls within paragraph (6)` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 87(3) P commits an offence under paragraph (2)(a)` | 6 |  | 2 |  |  |  |
| mlr4-part9 | `reg 87(8) P commits an offence under paragraph (2)(b)` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 87(2) P commits an offence` | 2 |  |  |  |  |  |
| mlr4-part9 | `reg 87(9) the term of imprisonment is within the liability` | 2 |  |  |  |  |  |
| mlr4-part9 | `reg 87(9) the fine is within the liability` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 88(1) P commits an offence` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 88(2) the term of imprisonment is within the liability` | 2 |  |  |  |  |  |
| mlr4-part9 | `reg 88(2) the fine is within the liability` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 88(3) the person is guilty of an offence of disclosing information` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 88(3) the term of imprisonment is within the liability` | 2 |  |  |  |  |  |
| mlr4-part9 | `reg 88(3) the fine is within the liability` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 88(4) the person has a defence` |  |  | 1 |  |  | 1 |
| mlr4-part9 | `reg 89(1) the body may institute proceedings for an offence under these Regulations` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 89(5) paragraphs (1) and (3) extend to the place` | 1 |  | 1 |  |  |  |
| mlr4-part9 | `reg 89(1) and (5) the body may institute proceedings` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 89(2) the duty to bring the proceedings in the name of an officer of Revenue and Customs arises` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 89(2) the proceedings were brought in the name of an officer of Revenue and Customs` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 89(3) the duty to report arises` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 89(3) the local weights and measures authority reported as required` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 89(4) the matter is treated as an assigned matter` |  |  |  |  | 1 |  |
| mlr4-part9 | `reg 89(6) paragraph (4)(b) is read as referring to the Crown Office and Procurator Fiscal Service` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 90(1) proceedings may be taken before the appropriate court having jurisdiction where the person is` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 90(2) proceedings may be taken at any appropriate court in the United Kingdom` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 90(3) the offence may for all incidental purposes be treated as committed within the jurisdiction of the court` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 91(1) the proceedings were brought in the right name` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 91(2) the fine is paid out of the funds of the partnership or association` |  | 1 | 1 |  |  |  |
| mlr4-part9 | `reg 91(3) the rules of court relating to the service of documents have effect as if the body were a body corporate` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 91(4)(a) section 33 of the Criminal Justice Act 1925 and Schedule 3 to the Magistrates' Courts Act 1980 apply as to a body corporate` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 91(4)(b) section 18 of the Criminal Justice (Northern Ireland) Act 1945 and Schedule 4 to the Magistrates' Courts (Northern Ireland) Order 1981 apply as to a body corporate` |  |  | 1 |  |  |  |
| mlr4-part9 | `reg 92(1) the officer is guilty of the offence` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 92(2) paragraph (1) applies to the member as if the member was a director` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 92(3) the officer is guilty of the offence committed by the partnership` | 1 |  |  |  |  |  |
| mlr4-part9 | `reg 92(4) the officer is guilty of the offence committed by the unincorporated association` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 93(1) a person may appeal to the Upper Tribunal` |  |  | 1 |  |  |  |
| mlr4-part10 | `reg 93(3)(b) section 133A(1) the action specified in the decision notice may be taken` | 1 |  | 1 |  |  |  |
| mlr4-part10 | `reg 93(3)(b) section 133A(1) the action specified in the decision notice is barred` |  |  | 1 |  |  | 1 |
| mlr4-part10 | `reg 93(3)(b) section 133A(2) the Tribunal may make recommendations as to the FCA's regulating provisions or procedures` |  |  | 1 |  |  |  |
| mlr4-part10 | `reg 94(1) the duty to offer P a review arises` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 94(1) the Commissioners offered P a review` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 94(2) the offer of a review was made by notice at the same time as the decision` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 94 applies to the notification` | 1 |  | 1 |  |  |  |
| mlr4-part10 | `reg 95(1) the duty to review the decision arises` |  |  |  | 1 |  |  |
| mlr4-part10 | `reg 95(1) the Commissioners reviewed the decision` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 95(2) P may notify acceptance of the offer` | 1 |  | 1 |  |  |  |
| mlr4-part10 | `reg 95(3) the Commissioners may review the decision` | 1 |  | 1 |  |  |  |
| mlr4-part10 | `reg 96(1) the Commissioners may notify P that the relevant period is extended` |  |  |  | 1 |  |  |
| mlr4-part10 | `reg 96(2) the relevant period is extended to the end of day` |  |  | 1 |  |  |  |
| mlr4-part10 | `reg 96(3) a further notice may be given` |  |  | 1 |  |  |  |
| mlr4-part10 | `reg 97(1) this regulation applies` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 97(2) the duty to review the decision out of time arises` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 97(2) the Commissioners reviewed the decision out of time` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 98(1) this regulation applies` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 98(2) the nature and extent of the review are for the Commissioners to judge` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 98(3) the duty to have regard to the steps taken before the review arises` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 98(3) the Commissioners had regard to the steps taken before the review` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 98(4) the duty to take account of the representations arises` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 98(4) the review took account of the representations` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 98(5) the review may conclude that the decision is` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 98(7) the relevant date is day` |  |  | 1 |  |  |  |
| mlr4-part10 | `reg 98(6) the duty to give P notice of the conclusions and reasoning arises` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 98(6) the Commissioners gave P notice of the conclusions and reasoning in time` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 98(8) the review is treated as having concluded that the decision is upheld` |  |  |  | 1 | 1 |  |
| mlr4-part10 | `reg 98(9) the duty to notify P of the conclusion treated as reached arises` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 98(9) the Commissioners notified P of the conclusion treated as reached` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 99(1) a person may appeal to the tribunal in accordance with regulation 100` | 1 |  |  |  |  |  |
| mlr4-part10 | `reg 99(4) the tribunal has the power to` |  |  | 1 |  |  |  |
| mlr4-part10 | `reg 99(4)(a) the tribunal may reduce the penalty to the amount` |  |  | 1 |  |  |  |
| mlr4-part10 | `reg 100(6) the conclusion date is day` |  |  | 1 |  |  |  |
| mlr4-part10 | `reg 100(1) the appeal was made in time` |  | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 100(2) the appeal was made in time` | 1 | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 100(3) the appeal was made in time` | 3 | 1 | 1 |  |  |  |
| mlr4-part10 | `reg 100(4) the appeal may be made` |  |  |  | 1 |  |  |
| mlr4-part10 | `reg 100(5) the appeal may be made after the end of the period` | 1 |  |  |  |  |  |
| mlr4-part11 | `reg 101 the charge or penalty is a debt due to` |  |  | 1 |  |  |  |
| mlr4-part11 | `reg 102(1) the charge may be imposed on` |  |  | 1 |  |  |  |
| mlr4-part11 | `reg 102(2) the charge is permitted` | 1 |  | 1 |  |  |  |
| mlr4-part11 | `reg 102(4) the FCA paid the penalties it received to the Treasury` |  | 1 | 1 |  |  |  |
| mlr4-part11 | `reg 102(5) the Treasury may give directions to the FCA` |  |  | 1 |  |  |  |
| mlr4-part11 | `reg 102(6) the directions may` |  |  | 1 |  |  |  |
| mlr4-part11 | `reg 102(7) the Treasury paid the sums into the Consolidated Fund` |  | 1 | 1 |  |  |  |
| mlr4-part11 | `reg 103(1) the duty to inform the NCA arises` | 1 |  |  |  |  |  |
| mlr4-part11 | `reg 103(1) the body or person informed the NCA as required` |  | 1 | 1 |  |  |  |
| mlr4-part11 | `reg 103(2) the disclosure breaches a restriction on the disclosure of information` | 1 |  | 1 |  |  |  |
| mlr4-part11 | `reg 103(3) civil liability arises in respect of the disclosure` | 1 |  | 1 |  |  |  |
| mlr4-part11 | `reg 104(4) the disclosure is a suspicious activity disclosure` | 1 |  |  |  |  |  |
| mlr4-part11 | `reg 104(1) the NCA made arrangements to provide appropriate feedback` |  | 1 | 1 |  |  |  |
| mlr4-part11 | `reg 104(2) the feedback may be provided in the way` |  |  | 1 |  |  |  |
| mlr4-part11 | `reg 104(3) the feedback may be provided in the form` |  |  | 1 |  |  |  |
| mlr4-part11 | `reg 105(1) the Commissioners may disclose the information to the FCA` | 1 |  |  |  |  |  |
| mlr4-part11 | `reg 105(2) the FCA or a recipient must not disclose the information` | 1 |  | 1 |  |  |  |
| mlr4-part11 | `reg 106 these Regulations authorise or require the disclosure` | 1 |  | 1 |  |  |  |
| mlr4-part11 | `reg 107 the transfer is treated as a transfer of funds within the United Kingdom` |  |  | 1 |  |  |  |
| mlr4-part11 | `reg 108(1) the Treasury carried out a review and published a report` |  | 1 | 1 |  |  |  |
| mlr4-part11 | `reg 108(2) the first report was published in time` |  | 1 |  |  |  |  |
| mlr4-part11 | `reg 108(3) the subsequent report was published in time` |  | 1 | 1 |  |  |  |
| mlr4-part11 | `reg 108(4) the review had regard to how the instruments are implemented in other member States` |  | 1 | 1 |  |  |  |
| mlr4-part11 | `reg 108(5) the report sets out what it must` |  | 1 | 1 |  |  |  |
| mlr4-part11 | `reg 110(5) the instrument is one of the old money laundering regulations` | 2 |  |  |  |  |  |
| mlr4-part11 | `reg 110(6) the instrument is the old transfer of funds regulations` | 1 |  |  |  |  |  |
| mlr4-part11 | `reg 110(1) the instrument is revoked` |  |  | 1 |  |  |  |
| mlr4-part11 | `reg 110(2) the old regulations continue to have effect` |  |  |  |  | 1 |  |
| mlr4-part11 | `reg 110(3) a penalty or an offence under the relevant Part of these Regulations has effect` | 1 |  | 1 |  |  |  |
| mlr4-part11 | `reg 110(4) the conduct is taken to have begun on` |  |  | 1 |  |  |  |
| mlr4-schedules | `sch 1 the body is a professional body listed in Schedule 1` | 1 |  |  |  |  |  |
| mlr4-schedules | `sch 2 the activity is a listed activity` | 1 |  |  |  |  |  |
| mlr4-schedules | `sch 2 item 3 the service is within payment services` | 1 |  |  |  |  |  |
| mlr4-schedules | `sch 2 item 6 the trading is within the item` |  |  | 1 |  |  |  |
| mlr4-schedules | `sch 3 para 36 the act is a relevant offence` |  |  | 2 |  |  |  |
| mlr4-schedules | `sch 3 the offence is a relevant offence` | 1 |  |  |  |  |  |
| mlr4-schedules | `sch 3AZA para 1 a material discrepancy may arise in relation to the information` |  |  | 1 |  |  |  |
| mlr4-schedules | `sch 3AZA para 2 the discrepancy satisfies the condition` | 1 |  |  |  |  |  |
| mlr4-schedules | `sch 3AZA para 3 the discrepancy is in a form listed in paragraph 3` | 1 |  |  |  |  |  |
| mlr4-schedules | `sch 3AZA the discrepancy is a material discrepancy` | 1 |  | 1 |  |  |  |

### Reading a result: FALSE and NOTHING (mlr4)

**A "no" in this row** is `JUST FALSE`, or a bearer's prohibition derived from it.
It is given only where the Regulations say no in their own words.
Eight kinds of words count: a flat negative ("may not be required", "must not impose", "does not affect", "is not guilty", "do not authorise or require"); a definition that says "means" or "is"; a closed list ("The activities ... are"); an "if", "only if", "unless" or "except" condition that fails (marginal reading (a), below); a period the text fixes in its own words, with the case outside it (ruled 2026-11-05 (a), tag `[ruled 2026-11-05 (a) period]`); and a "where", "when", "upon" or "whenever" condition that is not met (ruled 2026-11-05 (b) and (c), tag `[ruled 2026-11-05 (b) where]`, or `(read from "when")` or `(read from "before")` for those openers); an unproved defence ("it is a defence ... to prove that X", tag `[ruled 2026-11-05 (b) defence]`, meaning "this regulation gives no defence on these facts" and never "no defence at all"); and a bar that has ended ("must not ... until X", tag `[ruled 2026-11-05 (d) bar]`).
So `JUST FALSE` on `reg 76(4) the designated supervisory authority may impose a penalty on P` means "regulation 76(4) forbids this penalty".
It does not mean "the authority has no power in general".

**"Not covered" in this row** is `NOTHING`.
It is given where the Regulations list without closing the list ("inter alia", "including", a power list without "only"), leave a term undefined, are silent, point to a body or instrument that is not among the sources (Schedules 5 and 6, the Companies Act, the Proceeds of Crime Act, FSMA), or limit a grant or prohibition by a scope with no "only" ("in a case where the Commissioners are required to undertake a review under regulation 95", "if the tribunal gives permission": ruled 2026-11-05 (c)) and the facts fall outside the scope.
A stated period and a "where" condition are no longer in this list: since the ruling of 2026-11-05 they give `JUST FALSE` outside them, except where the rule's own answer inside the condition is already `JUST FALSE` (see "Polarity" in the fork register).
A `NOTHING` is also given for a duty that does not arise: the compliance function answers `NOTHING` there and its note names the companion function (`... the duty ... arises`) that says whether the duty arises.
Each branch says which of the six reasons it is, in a `-- NOTHING-kind (...)` comment.
A caller must never read `NOTHING` as no: on a question about a deadline, `NOTHING` means the Regulations do not say whether the act was in time.

**What the person sees.** The seat layer returns the same `MAYBE BOOLEAN`.
"I am not sure" in a seat question becomes `NOTHING` going in, so a rule that cannot answer without that fact answers `NOTHING` coming out, and the seat never turns a missing fact into a no.

## Seams (mlr4)

A seam is an answer that another section gives and this section reads (or the reverse).
Each one is an input of type `MAYBE BOOLEAN` (or `BOOLEAN` for a plain fact), marked in the module with `-- SEAM S-n (asking|answering)`.
The names are those of PLAN.md section 5.
A caller who has no answer passes `NOTHING`, and the rule answers `NOTHING` where it cannot answer without it.

| id | direction | where in this range | input or output |
|---|---|---|---|
| S-K2 | asking | Schedule 3AZA paragraph 1 | `reg 5 and 6 the individual is a beneficial owner of the customer`, `MAYBE BOOLEAN` |
| S-K3 | asking | reg 66(1) | `reg 7(1) the supervisory authorities of the relevant person`, `MAYBE (LIST OF Authority)` |
| S-K4 | asking | regs 76(3), 78(1), 92(1), (3), (4) (an "officer" outside Part 8) | `reg 3(1) the person is an officer of the entity`, `MAYBE BOOLEAN` |
| S-8 | asking | regs 66(1) and 69(1) | `reg 8 the person is a relevant person`, `MAYBE BOOLEAN` |
| S-12 | answering | reg 66 | `reg 66 the person has failed to comply with a requirement of a notice given under regulation 66`, `BOOLEAN` (a fact built from the four ways to fail) |
| S-16 | asking | reg 65(3) | `sch 5 the person is a connected person of the relevant person`, `MAYBE BOOLEAN` |
| S-17 | asking | reg 75 | `sch 6 the provision is a relevant requirement`, `MAYBE BOOLEAN` |
| S-19 | asking | regs 93(1) and 99(1) | four `BOOLEAN` facts: `reg 25(2) the decision is a direction`, `reg 59(1) the decision refuses to register an applicant`, `reg 60 the decision suspends or cancels a registration`, `reg 58 the decision is that a person is not a fit and proper person, other than one required by regulation 58(3)` |
| S-5 | answering | Schedule 3 | `sch 3 the offence is a relevant offence`, `MAYBE BOOLEAN` |
| S-6 | answering | Schedule 3AZA | `sch 3AZA the discrepancy is a material discrepancy`, `MAYBE BOOLEAN` |

Seams the plan lacks: none found in this range.
Seam S-K1 (a business relationship), which the plan's entry for this part lists, is not asked: no line of this range speaks of a business relationship.
The plan lists S-K2 and S-K3 together for the beneficial owner of Schedule 3AZA; only S-K2 is asked there, and S-K3 is asked by regulation 66(1).
Where the plan says the core answers the ask (PLAN.md section 5.3), the rules take the core's types as given: `Authority`, `Professional body` and `Listed activity` serve Schedules 1 and 2 and regulations 66(1), 76(7) and 101, `Kind of relevant person` serves regulations 74A to 74C, and `Part of the United Kingdom` serves regulations 71(3), 86 to 88 and 89.

## Dependencies

None staged: `inputs/DEPENDENCIES.md` says "None".
The Interpretation Act 1978 row has an unstable target (it uses `REFUSE`), so a main build cannot read it and it was not copied.
Taken as a convention of this row, to fill from that Act's module later: the counting of a period in days from an anchor date (regulations 66(2), 95(1)(b), 96(2), 98(6), 100(1) to (4); see fork F-PERIOD), and a "month" or a "year" in a limit (regulations 77(4), 86(1), 87(9), 88(2), 88(3), 84(10), 108(3)), which the caller states as a number of months or years.
The Proceeds of Crime Act 2002 Part 7 and the Terrorism Act 2000 Part 3 are being encoded in other rows and are not staged: regulation 104(4) takes "made under Part 3 of the Terrorism Act 2000" and "made under Part 7 of the Proceeds of Crime Act 2002" as inputs.

## Unstable dialect

I looked at time (the fixed dates in regulations 108(2) and 110(2), and the deadlines counted from events in regulations 95 to 100), at rule versions (none: the text is one consolidated version) and at workarounds, and found no shape that earns a second encoding: the dates compare as dates on main, and the only workaround is the day-count convention of F-PERIOD, for which `references/dialects.md` lists no unstable difference.
No second encoding was written.

## What the text turns out to say (findings)

1. **Regulation 83(1A) names a power the Commissioners do not have.**
   It requires the Commissioners to check for convictions "Before imposing a sanction on P under regulation 76, 77 or 78" (line 2588), while regulation 83(1) says "under regulation 76 or 78" (line 2579) and regulation 77 is the FCA's power.
   Encoded as written: the input is "the Commissioners impose a sanction on P under regulation 76, 77 or 78"; for the Commissioners the 77 limb can never apply.
   (`reg 83(1A) the Commissioners checked whether P has criminal convictions`.)
2. **Regulation 66(5) does not oblige a notice to attend to give reasons.**
   It requires reasons where a supervisory authority or officer "requires information to be provided or documents to be produced" (line 2229).
   A notice under 66(1)(c), to attend and answer questions, is outside the words: the companion `reg 66(5) the duty to set out the reasons arises` answers `JUST FALSE` for it ("Where ... requires information to be provided or documents to be produced", ruled 2026-11-05 (b)), and the compliance function `reg 66(5) the notice complies with the requirement to set out the reasons` answers `NOTHING`, its note naming the companion.
3. **The "all reasonable steps" bar in regulation 76(4) protects P, not the officer penalised under 76(3).**
   Paragraph (4) forbids a penalty "on P" (line 2459); an officer penalised under (3) is "that person" (line 2458).
   The function answers `NOTHING` for an officer's penalty.
4. **Regulation 101 does not reach an officer's penalty** (fork F-101-OFFICER): the debt is for a charge or penalty "imposed on a relevant person or on a payment service provider" (line 2856), and an officer is neither.
5. **Under the counting of F-PERIOD, limb (a) of regulation 100(1) never decides an appeal where the offer of a review was made with the decision.**
   The offer is to be made at the same time as the decision (regulation 94(2), line 2780), so the relevant period of regulation 96 (30 days from the date) ends on day 30 at the earliest, while limb (a) (30 days beginning with the date) ends on day 29.
   If the counting were the other way, the two would end on the same day.
   The tests cover days 29, 30 and 31 of both limbs.
6. **A deemed-upheld review has no stated end to the appeal window until the Commissioners give the regulation 98(9) notice.**
   Regulation 100(4) lets an appeal be made "to the date 30 days after the conclusion date" (line 2851), and regulation 100(6) defines the conclusion date as "the date of the notice notifying the conclusions of the review" (line 2853); in a regulation 98(8) case the only such notice is the one regulation 98(9) requires (line 2823).
   The function takes the conclusion date as an input, so the question cannot be asked until the notice has been given.
7. **Regulation 95(2) ("P may not notify acceptance") and regulation 95(3) ("the Commissioners must not review") are two prohibitions on two bearers for one fact.**
   Both are `JUST FALSE` answers once P has appealed, and the prohibition is derived for each bearer (ruling N2): `reg 95(2) the prohibition on P` and `reg 95(3) the prohibition on the Commissioners`.
   Reading P's "may not" as a prohibition rather than only as an ineffective act is assumed, not ruled; the other reading drops the derived rule for P and keeps the decision function.
8. **Regulations 84(9) and 85(8) print a garbled cross-reference.**
   Lines 2617 and 2637 read "in accordance with paragraph under paragraph (6)" and "(5)".
   The quotation is kept as printed; the rules read the reference as paragraph (6) and (5), which are the paragraphs that deal with deferred or anonymous publication.
9. **Regulations 108(2) and 110(2) turn on fixed dates.**
    The functions compare a date they are given with 26th June 2022 and with the commencement date; they do not know today's date, so "was the first report in time" is answered for the date the caller states.
10. **Regulation 65(2) and regulation 87(10) define "relevant officer" in the same words** (lines 2211-2214 and 2690-2693), and 65(2) begins "Unless otherwise defined in this Part".
    Each is encoded under its own regulation (option C), as a separate function with its own tests.
11. **Schedule 1 does not name the Royal Institution of Chartered Surveyors or the Chartered Insurance Institute.**
    The 22 professional bodies printed at lines 2957-2978 are the whole list in this text, and `sch 1 the body is a professional body listed in Schedule 1` answers for exactly those; no body was added.
12. **Jersey and Guernsey are not told apart in regulation 107.**
    Paragraph (a) of regulation 107 says "the Channel Islands" (line 2922), so both map to the one constructor `reg 107(a) the Channel Islands`.
13. **Stated gaps.**
    Where the text gives nothing to encode, the coverage row says so in brackets rather than a function inventing an answer: regulations 65(1) "tribunal" (the High Court), 74C(18), 77(2) with 79, 77(4), 78(2), 101, 102(4), 107 and 108(1).

## What the main binary does not accept

Measured on build 1.6.109 and 1.6.108; every item below was met while writing this row.

- **Loud** (an error, so it teaches):
  `REFUSE` and `#ASSERT REFUSED` do not exist, so "not covered" is `NOTHING` or a constructor, asserted.
  A constructor with `HAS` fields cannot share a line with its name in a `DECLARE`: put the constructor on its own lines.
  `NOT` must be parenthesised.
  An `#ASSERT` must be on one line.
  There are no sets, no `YMD`, no `TYPICALLY` and no section-level `GIVEN`.
  There is no function that adds days to a date, so every period is a number of days after an anchor date (the keel's convention).
- **Silent** (exit code 0, wrong or unchecked answer if you do not look):
  A `DEONTIC` value can be asserted only with `EQUALS FULFILLED`.
  A breach is checked with `#TRACE`, which prints the outcome and never an assertion line, so `check.sh` cannot see it.
  The fourteen traces in this row (two each for regulations 66(2)(a), 74(4), 76(4), 95(2) and 95(3), and one for each bearer in regulations 84(1) and 105(2)) were run on both builds and the outcomes compared by reading them: on 1.6.109 and on 1.6.108 nine end in BREACH (a forbidden act, or a late one), one in FULFILLED (regulation 66(2)(a), performed on the last day) and four stay open (a wait with nothing done), and the two builds agree trace by trace.
  Every prohibition is therefore also a decision function that is asserted, and the regulative rule only restates it.
  `BECAUSE` is accepted only after `LEST BREACH BY`.
  `EQUALS JUST TRUE` on a `MAYBE BOOLEAN` input turns a missing fact (`NOTHING`) into a false one; the rules that read such an input use an explicit `NOTHING` branch.

## Where this brief governs over PLAN.md

- The brief requires the seat layer (two files) and the coverage, fork, jural-relation and marginal-reading sections; PLAN.md has no seat.
  The brief governs.
- My own first reading (written in PROGRESS.md before any L4) pre-registered regulations 104A, 108, 109 and 110(1) as machinery.
  The brief allows `inert` for machinery only as a reason of its own (reason 2) and says "addresses an official" and "refers to another Act" are not reasons; each of those regulations has a rule that bears on a person or a date, so each is encoded: 104A and 109 as pointers that return the schedule they name, 108 as the Treasury's review duty with its dates, 110(1) as a revocation.
  No row of this range is `inert` for reason 2; the 61 inert rows are headings (reason 1).
- PLAN.md section 5.2 gives S-19 as four facts; regulation 93(1) uses three of them and regulation 99(1) uses all four, because regulation 99(1)(b) is the only head that names regulation 58.
  The seat question for regulation 99(1) carries the exception in the person's own words: "Is the decision ... other than a decision that regulation 58(3) required the Commissioners to make (because you were convicted of a criminal offence listed in Schedule 3)?", and the cases include a person whose decision regulation 58(3) required, who is answered `JUST FALSE`.
  The plan's input names are used unchanged.

## Statement about the text

The text encoded is a converter-script rendering of the Regulations (lines 2200 to 3054 of `uksi-2017-692.txt`), not the official text.
Nothing here is verified against the official text, and a rendering fault (the unnumbered Schedules, the unlettered limbs, the garbled cross-references of finding 8) is recorded as a fork or a finding, not corrected.

## What check.sh prints

Before this part's files, the supplied `check.sh` printed one module: `mlr-core.l4`, 0 errors, 0 satisfied, 0 failed, 0 refused (the baseline it replaced).
After, run as `L4=<main 1.6.109> L4_MAIN=<main 1.6.108> ./check.sh` in this folder:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
mlr-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
mlr4-cases-seat.l4                             0       290       0        0         0 |      0       290       0        0  same
mlr4-part10.l4                                 0         0       0        0         0 |      0         0       0        0  same
mlr4-part11.l4                                 0         0       0        0         0 |      0         0       0        0  same
mlr4-part8.l4                                  0         0       0        0         0 |      0         0       0        0  same
mlr4-part9.l4                                  0         0       0        0         0 |      0         0       0        0  same
mlr4-schedules.l4                              0         0       0        0         0 |      0         0       0        0  same
mlr4-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
mlr4-tests-part10.l4                           0       192       0        0         0 |      0       192       0        0  same
mlr4-tests-part11.l4                           0       139       0        0         0 |      0       139       0        0  same
mlr4-tests-part8.l4                            0       445       0        0         0 |      0       445       0        0  same
mlr4-tests-part9.l4                            0       565       0        0         0 |      0       565       0        0  same
mlr4-tests-schedules.l4                        0       103       0        0         0 |      0       103       0        0  same
TOTAL (13 modules)                             0      1734       0        0           |      0      1734       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`check.sh` counts error diagnostics and assertion lines; it does not see a `#TRACE` outcome.
The fourteen traces were compared by hand between the two builds (see "What the main binary does not accept").
`srcrefs.py check --refs` and `--strict ../../../inputs/uksi-2017-692.txt` were run on every module of this part and report 0 problems.
