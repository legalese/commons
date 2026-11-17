# NOTES: part P3 of the EU Artificial Intelligence Act encoding (lines 374 to 526 of the consolidated text: Section 3 heading and Articles 16 to 27)

Status header (2026-11-17).
How each kind of claim below was checked:
line numbers and quotations by `python3 -I srcrefs.py check --strict` over `P3-section-3.l4`, `P3-art-16.l4` to `P3-art-27.l4`, the test files and the seat files (278 quote lines, 158 runs, 231 locators, 0 problems);
assertion counts by `check.sh` with L4=1.6.110 and L4_MAIN=1.6.109 (45 modules, 1065 assertions satisfied, 0 failed, 0 refused, every module the same on both builds; 652 of the assertions are in the layer-1 test files and 413 in the seat case files);
trace outcomes by running every one of the 228 `#TRACE`s on both builds and comparing each with the `-- EXPECT` comment above it (`work/tracecheck.py`, outside the deposit): 228 match on both builds, none differs between builds;
the three probes in "What the stable binary does not accept" (`NOT a OR b`, `MAX`, a continued `#ASSERT`) were re-run on 2026-11-17 on both builds.
Everything else here is this part's reading of the text: assumed, not ruled by a lawyer.
The text is the Publications Office consolidated version of 27.7.2026, which says of itself that it "is meant purely as a documentation tool and has no legal effect" (line 2): it is a rendering, not the official text.
The as-enacted wording is quoted from `eu-ai-act-2024-1689.txt` (the base text, source id `eu-ai-act-2024-1689`), and the Omnibus from `eu-omnibus-2026-1744.txt`.
Assumed, not ruled: commencement is IN for this Regulation (the brief says so, as it does for the keel), so Chapter III Sections 1 to 3 apply from 2 December 2027 for a system high-risk under Article 6(2) with Annex III and from 2 August 2028 for a system under Article 6(1) with Annex I, and every function that states a duty, a power or a consequence takes `the date asked`.
The two readings of the text on either side of 27 July 2026 are the keel's `Omnibus Art 4 the version in force`; four passages of this range are marked `▼M1 REPLACED` and each has its own function per version plus a dispatcher: Art 17(2), Art 25(2), Art 25(4) and Art 27(4) with 27(5).

## What this part is

Layer 1 is the law: `P3-section-3.l4` (the gate every provision passes through) and `P3-art-16.l4` to `P3-art-27.l4`, each with a test file (`P3-tests-section-3.l4`, `P3-tests-art-16.l4`, `P3-tests-art-17.l4`, `P3-tests-art-18-19.l4`, `P3-tests-art-20-21.l4`, `P3-tests-art-22.l4` to `P3-tests-art-27.l4`).
Layer 2 is the thin seat layer: `P3-seat-<slug>.l4` and `P3-cases-seat-<slug>.l4` for eight seats.
The keel (`aia-core`, `aia-timeline`, `aia-annex-x`, `aia-definitions`, `aia-scope`) is read-only and untouched.
`P3-section-3.l4` is infrastructure and not a provision: it takes the keel's answers for Article 113 with Article 111(2), Article 2(2) and Article 2(13) and says, for one Article of this range, whether it applies to the AI system on the date asked.
A shut gate (before the date of application, or a saved legacy system) gives `NOTHING`; Article 2(2) cutting the Article off gives `JUST FALSE`; Article 2(13) allowing the requirement to be limited gives `NOTHING` (the extent is for delegated acts outside the sources); an open gate gives the provision's own answer.
Every decision function of Articles 16 to 27 takes `the date asked`, `the AI system` (the keel's record) and `the circumstances` (`Section 3 circumstances`: the Section B flag and the two Article 2(13) facts) before its own facts.
The party's role is assumed by the function: the seat asks the role once, in a question of its own.

## Coverage (P3)

One row per line of the text in the part's range (374 to 526, 153 non-blank lines), so every provision, paragraph, point and subparagraph has a row with exactly one disposition.
Dispositions: `encoded` (a rule, function or table in layer 1 with a test, citing the provision with `@ref`), `fork` (the row points at the fork entry below and at the function that carries the answer taken), `inert` with a reason number (1 not operative; 2 machinery; 3 repealed or blank).
There is no `out-of-scope` and no `deferred` row.
The rows were made by reading the `-- src:N` quote lines of each module (which `srcrefs.py` checks against the text), so a row names the functions whose quotation covers the line.
Function names are shortened to 58 characters here; the modules hold the full names.

| lines | provision | disposition | where | note |
| --- | --- | --- | --- | --- |
| 374-375 | Section 3 heading | inert (1) |  | a heading: not operative |
| 376 | Article 16 heading | inert (1) |  | a heading: not operative |
| 377 | Article 16 title | inert (1) |  | a heading: not operative |
| 378 | Art 16 lead-in | fork | P3-art-16: `Art 16(a) the provider has ensured that the high-risk AI s...`, `Art 16(a) the provider's duty to ensure that the high-risk...` | see F-bare-shall; tests in P3-tests-art-16 |
| 379 | Art 16(a) | fork | P3-art-16: `Art 16(a) the provider has ensured that the high-risk AI s...`, `Art 16(a) the provider's duty to ensure that the high-risk...` | see F-bare-shall; tests in P3-tests-art-16 |
| 380 | Art 16(b) | fork | P3-art-16: `Art 16(b) the provider has indicated its name, registered...`, `Art 16(b) the provider's duty to indicate its name, regist...` | see F-bare-shall; tests in P3-tests-art-16 |
| 381 | Art 16(c) | fork | P3-art-16: `Art 16(c) the provider has a quality management system in...`, `Art 16(c) the provider's duty to have a quality management...` | see F-bare-shall; tests in P3-tests-art-16 |
| 382 | Art 16(d) | fork | P3-art-16: `Art 16(d) the provider keeps the documentation referred to...`, `Art 16(d) the provider's duty to keep the documentation re...` | see F-bare-shall; tests in P3-tests-art-16 |
| 383 | Art 16(e) | fork | P3-art-16: `Art 16(e) the provider keeps the logs automatically genera...`, `Art 16(e) the provider's duty to keep the logs automatical...` | see F-bare-shall, F-when-upon; tests in P3-tests-art-16 |
| 384 | Art 16(f) | fork | P3-art-16: `Art 16(f) the provider has ensured that the high-risk AI s...`, `Art 16(f) the provider's duty to ensure that the high-risk...` | see F-bare-shall, F-prior-to; tests in P3-tests-art-16 |
| 385 | Art 16(g) | fork | P3-art-16: `Art 16(g) the provider has drawn up an EU declaration of c...`, `Art 16(g) the provider's duty to draw up an EU declaration...` | see F-bare-shall; tests in P3-tests-art-16 |
| 386 | Art 16(h) | fork | P3-art-16: `Art 16(h) the provider has affixed the CE marking`, `Art 16(h) the provider's duty to affix the CE marking` | see F-bare-shall; tests in P3-tests-art-16 |
| 387 | Art 16(i) | fork | P3-art-16: `Art 16(i) the provider has complied with the registration...`, `Art 16(i) the provider's duty to comply with the registrat...` | see F-bare-shall; tests in P3-tests-art-16 |
| 388 | Art 16(j) | fork | P3-art-16: `Art 16(j) the provider has taken the necessary corrective...`, `Art 16(j) the provider's duty to take the necessary correc...` | see F-bare-shall; tests in P3-tests-art-16 |
| 389 | Art 16(k) | fork | P3-art-16: `Art 16(k) the provider has demonstrated the conformity of...`, `Art 16(k) the provider's duty to demonstrate the conformit...` | see F-bare-shall, F-when-upon; tests in P3-tests-art-16 |
| 390 | Art 16(l) | fork | P3-art-16: `Art 16(l) the provider has ensured that the high-risk AI s...`, `Art 16(l) the provider's duty to ensure that the high-risk...` | see F-bare-shall; tests in P3-tests-art-16 |
| 391 | Article 17 heading | inert (1) |  | a heading: not operative |
| 392 | Article 17 title | inert (1) |  | a heading: not operative |
| 393 | Art 17(1) | encoded | P3-art-17: `Art 17(1) the provider has put in place a quality manageme...`, `Art 17(1) the provider's duty to put a quality management...` (+1) | tests in P3-tests-art-17 |
| 394 | Art 17(1)(a) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 395 | Art 17(1)(b) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 396 | Art 17(1)(c) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 397 | Art 17(1)(d) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 398 | Art 17(1)(e) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 399 | Art 17(1)(f) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 400 | Art 17(1)(g) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 401 | Art 17(1)(h) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 402 | Art 17(1)(i) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 403 | Art 17(1)(j) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 404 | Art 17(1)(k) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 405 | Art 17(1)(l) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 406 | Art 17(1)(m) | encoded | P3-art-17: `Art 17(1) the quality management system includes at least...` | tests in P3-tests-art-17 |
| 407 | ▼M1 REPLACED | inert (1) |  | a marker of the consolidation: it says which text follows (the replaced text is quoted in the version functions) |
| 408 | Art 17(2) | fork | P3-art-17: `Art 17(2) as amended the provider has met paragraph 2`, `Art 17(2) the provider has met paragraph 2` (+2) | see F-17-2; tests in P3-tests-art-17; version dispatch (as enacted, as amended) |
| 409 | ▼B | inert (1) |  | a marker of the consolidation: it says which text follows (the replaced text is quoted in the version functions) |
| 410 | Art 17(3) | fork | P3-art-17: `Art 17(3) the provider may include the aspects listed in p...`, `Art 17(3) the provider's permission to include the aspects...` | see F-17-3; tests in P3-tests-art-17 |
| 411 | Art 17(4) | encoded | P3-art-17: `Art 17(4) the harmonised standards referred to in Article...`, `Art 17(4) the obligation to put in place a quality managem...` | tests in P3-tests-art-17 |
| 412 | Article 18 heading | inert (1) |  | a heading: not operative |
| 413 | Article 18 title | inert (1) |  | a heading: not operative |
| 414 | Art 18(1) | fork | P3-art-18: `Art 18(1) the last day of the period for keeping the docum...`, `Art 18(1) the period for keeping the documentation runs on...` (+2) | see F-18-1; tests in P3-tests-art-18-19 |
| 415 | Art 18(1)(a) | fork | P3-art-18: `Art 18(1) the documents listed in points (a) to (e) are ke...` | see F-18-1; tests in P3-tests-art-18-19 |
| 416 | Art 18(1)(b) | fork | P3-art-18: `Art 18(1) the documents listed in points (a) to (e) are ke...` | see F-18-1; tests in P3-tests-art-18-19 |
| 417 | Art 18(1)(c) | fork | P3-art-18: `Art 18(1) the documents listed in points (a) to (e) are ke...` | see F-18-1; tests in P3-tests-art-18-19 |
| 418 | Art 18(1)(d) | fork | P3-art-18: `Art 18(1) the documents listed in points (a) to (e) are ke...` | see F-18-1; tests in P3-tests-art-18-19 |
| 419 | Art 18(1)(e) | fork | P3-art-18: `Art 18(1) the documents listed in points (a) to (e) are ke...` | see F-18-1; tests in P3-tests-art-18-19 |
| 420 | Art 18(2) | encoded | P3-art-18: `Art 18(2) the Member State is to determine the conditions...`, `Art 18(2) the Member State's duty to determine the conditi...` | tests in P3-tests-art-18-19 |
| 421 | Art 18(3) | encoded | P3-art-18: `Art 18(3) the provider that is a financial institution has...`, `Art 18(3) the provider's duty to maintain the technical do...` | tests in P3-tests-art-18-19 |
| 422 | Article 19 heading | inert (1) |  | a heading: not operative |
| 423 | Article 19 title | inert (1) |  | a heading: not operative |
| 424 | Art 19(1) | encoded | P3-art-19: `Art 19(1) the provider keeps the logs referred to in Artic...`, `Art 19(1) the provider's duty to keep the logs for at leas...` | tests in P3-tests-art-18-19 |
| 425 | Art 19(2) | encoded | P3-art-19: `Art 19(2) the provider that is a financial institution has...`, `Art 19(2) the provider's duty to maintain the logs as part...` | tests in P3-tests-art-18-19 |
| 426 | Article 20 heading | inert (1) |  | a heading: not operative |
| 427 | Article 20 title | inert (1) |  | a heading: not operative |
| 428 | Art 20(1) | fork | P3-art-20: `Art 20(1) the provider has informed the distributors and,...`, `Art 20(1) the provider has taken the necessary corrective...` (+2) | see F-immediately; tests in P3-tests-art-20-21 |
| 429 | Art 20(2) | fork | P3-art-20: `Art 20(2) the provider has informed the market surveillanc...`, `Art 20(2) the provider has investigated the causes of the...` (+2) | see F-immediately; tests in P3-tests-art-20-21 |
| 430 | Article 21 heading | inert (1) |  | a heading: not operative |
| 431 | Article 21 title | inert (1) |  | a heading: not operative |
| 432 | Art 21(1) | fork | P3-art-21: `Art 21(1) the provider has provided the competent authorit...`, `Art 21(1) the provider's duty to provide the competent aut...` | see F-when-upon; tests in P3-tests-art-20-21 |
| 433 | Art 21(2) | fork | P3-art-21: `Art 21(2) the provider has given the requesting competent...`, `Art 21(2) the provider's duty to give the requesting compe...` | see F-when-upon; tests in P3-tests-art-20-21 |
| 434 | Art 21(3) | encoded | P3-art-21: `Art 21(3) the competent authority's duty to treat the info...`, `Art 21(3) the information obtained by a competent authorit...` | tests in P3-tests-art-20-21 |
| 435 | Article 22 heading | inert (1) |  | a heading: not operative |
| 436 | Article 22 title | inert (1) |  | a heading: not operative |
| 437 | Art 22(1) | fork | P3-art-22: `Art 22(1) the provider established in a third country has...`, `Art 22(1) the provider's duty to appoint an authorised rep...` | see F-prior-to; tests in P3-tests-art-22 |
| 438 | Art 22(2) | encoded | P3-art-22: `Art 22(2) the provider has enabled its authorised represen...`, `Art 22(2) the provider's duty to enable its authorised rep...` | tests in P3-tests-art-22 |
| 439 | Art 22(3) | encoded | P3-art-22: `Art 22(3) the authorised representative has provided a cop...`, `Art 22(3) the authorised representative performs the tasks...` (+3) | tests in P3-tests-art-22 |
| 440 | Art 22(3)(a) | encoded | P3-art-22: `Art 22(3) the mandate empowers the authorised representati...` | tests in P3-tests-art-22 |
| 441 | Art 22(3)(b) | encoded | P3-art-22: `Art 22(3) the mandate empowers the authorised representati...` | tests in P3-tests-art-22 |
| 442 | Art 22(3)(c) | encoded | P3-art-22: `Art 22(3) the mandate empowers the authorised representati...` | tests in P3-tests-art-22 |
| 443 | Art 22(3)(d) | encoded | P3-art-22: `Art 22(3) the mandate empowers the authorised representati...` | tests in P3-tests-art-22 |
| 444 | Art 22(3)(e) | encoded | P3-art-22: `Art 22(3) the mandate empowers the authorised representati...` | tests in P3-tests-art-22 |
| 445 | Art 22(3) continued | encoded | P3-art-22: `Art 22(3) the mandate empowers the authorised representati...` | tests in P3-tests-art-22 |
| 446 | Art 22(4) | fork | P3-art-22: `Art 22(4) the authorised representative has informed the r...`, `Art 22(4) the authorised representative has terminated the...` (+1) | see F-immediately; tests in P3-tests-art-22 |
| 447 | Article 23 heading | inert (1) |  | a heading: not operative |
| 448 | Article 23 title | inert (1) |  | a heading: not operative |
| 449 | Art 23(1) | fork | P3-art-23: `Art 23(1) the importer has verified, before placing the sy...`, `Art 23(1) the importer's duty to verify the matters in poi...` | see F-prior-to; tests in P3-tests-art-23 |
| 450 | Art 23(1)(a) | fork | P3-art-23: `Art 23(1) the importer has verified, before placing the sy...`, `Art 23(1) the importer's duty to verify the matters in poi...` | see F-prior-to; tests in P3-tests-art-23 |
| 451 | Art 23(1)(b) | fork | P3-art-23: `Art 23(1) the importer has verified, before placing the sy...`, `Art 23(1) the importer's duty to verify the matters in poi...` | see F-prior-to; tests in P3-tests-art-23 |
| 452 | Art 23(1)(c) | fork | P3-art-23: `Art 23(1) the importer has verified, before placing the sy...`, `Art 23(1) the importer's duty to verify the matters in poi...` | see F-prior-to; tests in P3-tests-art-23 |
| 453 | Art 23(1)(d) | fork | P3-art-23: `Art 23(1) the importer has verified, before placing the sy...`, `Art 23(1) the importer's duty to verify the matters in poi...` | see F-prior-to; tests in P3-tests-art-23 |
| 454 | Art 23(2) | fork | P3-art-23: `Art 23(2) the importer has informed the provider, the auth...`, `Art 23(2) the importer is barred from placing the high-ris...` (+2) | see F-when-upon; tests in P3-tests-art-23 |
| 455 | Art 23(3) | fork | P3-art-23: `Art 23(3) the importer has indicated its name, registered...`, `Art 23(3) the importer's duty to indicate its name, regist...` | see F-23-3-places; tests in P3-tests-art-23 |
| 456 | Art 23(4) | encoded | P3-art-23: `Art 23(4) the importer has ensured that the storage or tra...`, `Art 23(4) the importer's duty to ensure that the storage o...` | tests in P3-tests-art-23 |
| 457 | Art 23(5) | fork | P3-art-23: `Art 23(5) the importer keeps the copies for the period`, `Art 23(5) the importer's duty to keep the copies for the p...` (+1) | see F-18-1; tests in P3-tests-art-23 |
| 458 | Art 23(6) | encoded | P3-art-23: `Art 23(6) the importer has ensured that the technical docu...`, `Art 23(6) the importer has provided the relevant competent...` (+2) | tests in P3-tests-art-23 |
| 459 | Art 23(7) | encoded | P3-art-23: `Art 23(7) the importer has cooperated with the relevant co...`, `Art 23(7) the importer's duty to cooperate with the releva...` | tests in P3-tests-art-23 |
| 460 | Article 24 heading | inert (1) |  | a heading: not operative |
| 461 | Article 24 title | inert (1) |  | a heading: not operative |
| 462 | Art 24(1) | fork | P3-art-24: `Art 24(1) the distributor has verified, before making the...`, `Art 24(1) the distributor's duty to verify the matters lis...` | see F-prior-to, F-24-as-applicable; tests in P3-tests-art-24 |
| 463 | Art 24(2) | fork | P3-art-24: `Art 24(2) the distributor has informed the provider or the...`, `Art 24(2) the distributor is barred from making the high-r...` (+2) | see F-when-upon, F-24-as-applicable; tests in P3-tests-art-24 |
| 464 | Art 24(3) | encoded | P3-art-24: `Art 24(3) the distributor has ensured that the storage or...`, `Art 24(3) the distributor's duty to ensure that the storag...` | tests in P3-tests-art-24 |
| 465 | Art 24(4) | fork | P3-art-24: `Art 24(4) the distributor has immediately informed the pro...`, `Art 24(4) the distributor has taken the corrective actions...` (+2) | see F-immediately, F-24-as-applicable; tests in P3-tests-art-24 |
| 466 | Art 24(5) | encoded | P3-art-24: `Art 24(5) the distributor has provided the relevant compet...`, `Art 24(5) the distributor's duty to provide the relevant c...` | tests in P3-tests-art-24 |
| 467 | Art 24(6) | encoded | P3-art-24: `Art 24(6) the distributor has cooperated with the relevant...`, `Art 24(6) the distributor's duty to cooperate with the rel...` | tests in P3-tests-art-24 |
| 468 | Article 25 heading | inert (1) |  | a heading: not operative |
| 469 | Article 25 title | inert (1) |  | a heading: not operative |
| 470 | Art 25(1) | fork | P3-art-25: `Art 25(1) the party is considered to be the provider of th...`, `Art 25(1)(a) the party puts its name or trademark on a hig...` | see F-25-1-closed; tests in P3-tests-art-25 |
| 471 | Art 25(1)(a) | fork | P3-art-25: `Art 25(1)(a) the party puts its name or trademark on a hig...` | see F-25-1-closed; tests in P3-tests-art-25 |
| 472 | Art 25(1)(b) | fork | P3-art-25: `Art 25(1)(a) the party puts its name or trademark on a hig...`, `Art 25(1)(b) the party makes a substantial modification th...` | see F-25-1-closed; tests in P3-tests-art-25 |
| 473 | Art 25(1)(c) | fork | P3-art-25: `Art 25(1)(a) the party puts its name or trademark on a hig...`, `Art 25(1)(c) the party modifies the intended purpose so th...` | see F-25-1-closed; tests in P3-tests-art-25 |
| 474 | ▼M1 REPLACED | inert (1) |  | a marker of the consolidation: it says which text follows (the replaced text is quoted in the version functions) |
| 475 | Art 25(2) | fork | P3-art-25: `Art 25(2) the initial provider has cooperated with the new...`, `Art 25(2) the initial provider is no longer considered to...` | see F-when-upon; tests in P3-tests-art-25; version dispatch (as enacted, as amended) |
| 476 | Art 25(2) continued | fork | P3-art-25: `Art 25(2) as amended the initial provider has cooperated`, `Art 25(2) as enacted the initial provider has cooperated` (+3) | see F-when-upon; tests in P3-tests-art-25; version dispatch (as enacted, as amended) |
| 477 | Art 25(2) continued | fork | P3-art-25: `Art 25(2) as amended the initial provider has cooperated`, `Art 25(2) as amended the initial provider's duty to carry...` (+2) | see F-when-upon; tests in P3-tests-art-25; version dispatch (as enacted, as amended) |
| 478 | Art 25(2)(a) | fork | P3-art-25: `Art 25(2) as amended the initial provider has cooperated`, `Art 25(2) as amended the initial provider's duty to carry...` (+2) | see F-when-upon; tests in P3-tests-art-25; version dispatch (as enacted, as amended) |
| 479 | Art 25(2)(b) | fork | P3-art-25: `Art 25(2) as amended the initial provider has cooperated`, `Art 25(2) as amended the initial provider's duty to carry...` (+2) | see F-when-upon; tests in P3-tests-art-25; version dispatch (as enacted, as amended) |
| 480 | Art 25(2)(c) | fork | P3-art-25: `Art 25(2) as amended the initial provider has cooperated`, `Art 25(2) as amended the initial provider's duty to carry...` (+2) | see F-when-upon; tests in P3-tests-art-25; version dispatch (as enacted, as amended) |
| 481 | Art 25(2) continued | fork | P3-art-25: `Art 25(2) the initial provider has cooperated with the new...`, `Art 25(2) the initial provider is no longer considered to...` | see F-when-upon; tests in P3-tests-art-25; version dispatch (as enacted, as amended) |
| 482 | ▼B | inert (1) |  | a marker of the consolidation: it says which text follows (the replaced text is quoted in the version functions) |
| 483 | Art 25(3) | fork | P3-art-25: `Art 25(3) the product manufacturer is considered to be the...` | see F-25-1-closed; tests in P3-tests-art-25 |
| 484 | Art 25(3)(a) | fork | P3-art-25: `Art 25(3) the product manufacturer is considered to be the...` | see F-25-1-closed; tests in P3-tests-art-25 |
| 485 | Art 25(3)(b) | fork | P3-art-25: `Art 25(3) the product manufacturer is considered to be the...` | see F-25-1-closed; tests in P3-tests-art-25 |
| 486 | ▼M1 REPLACED | inert (1) |  | a marker of the consolidation: it says which text follows (the replaced text is quoted in the version functions) |
| 487 | Art 25(4) | encoded | P3-art-25: `Art 25(4) as amended the item is one the paragraph names`, `Art 25(4) as enacted the item is one the paragraph names` (+5) | tests in P3-tests-art-25; version dispatch (as enacted, as amended) |
| 488 | ▼B | inert (1) |  | a marker of the consolidation: it says which text follows (the replaced text is quoted in the version functions) |
| 489 | Art 25(4) continued | encoded | P3-art-25: `Art 25(4) the AI Office has met the requirements for the v...`, `Art 25(4) the AI Office's permission to develop and recomm...` | tests in P3-tests-art-25 |
| 490 | Art 25(5) | encoded | P3-art-25: `Art 25(5) the need to observe and protect intellectual pro...` | tests in P3-tests-art-25 |
| 491 | Article 26 heading | inert (1) |  | a heading: not operative |
| 492 | Article 26 title | inert (1) |  | a heading: not operative |
| 493 | Art 26(1) | encoded | P3-art-26: `Art 26(1) the deployer has taken appropriate technical and...`, `Art 26(1) the deployer's duty to take appropriate technica...` | tests in P3-tests-art-26 |
| 494 | Art 26(2) | encoded | P3-art-26: `Art 26(2) the deployer has assigned human oversight to nat...`, `Art 26(2) the deployer's duty to assign human oversight to...` | tests in P3-tests-art-26 |
| 495 | Art 26(3) | encoded | P3-art-26: `Art 26(3) the obligations are without prejudice to other d...` | tests in P3-tests-art-26 |
| 496 | Art 26(4) | encoded | P3-art-26: `Art 26(4) the deployer has ensured that the input data is...`, `Art 26(4) the deployer's duty to ensure that the input dat...` | tests in P3-tests-art-26 |
| 497 | Art 26(5) | fork | P3-art-26: `Art 26(5) Article 73 applies mutatis mutandis to the deplo...`, `Art 26(5) the deployer has informed first the provider, an...` (+10) | see F-undue-delay, F-immediately; tests in P3-tests-art-26 |
| 498 | Art 26(5) continued | fork | P3-art-26: `Art 26(5) the monitoring obligation is deemed to be fulfil...` | see F-26-5-deeming; tests in P3-tests-art-26 |
| 499 | Art 26(6) | encoded | P3-art-26: `Art 26(6) the deployer keeps the logs for an appropriate p...`, `Art 26(6) the deployer's duty to keep the logs for at leas...` | tests in P3-tests-art-26 |
| 500 | Art 26(6) continued | encoded | P3-art-26: `Art 26(6) the deployer that is a financial institution has...`, `Art 26(6) the deployer's duty to maintain the logs as part...` | tests in P3-tests-art-26 |
| 501 | Art 26(7) | fork | P3-art-26: `Art 26(7) the deployer that is an employer has informed th...`, `Art 26(7) the deployer's duty to inform the workers' repre...` | see F-prior-to; tests in P3-tests-art-26 |
| 502 | Art 26(8) | encoded | P3-art-26: `Art 26(8) the deployer has informed the provider or the di...`, `Art 26(8) the deployer is barred from using the system` (+4) | tests in P3-tests-art-26 |
| 503 | Art 26(9) | encoded | P3-art-26: `Art 26(9) the deployer has used the information provided u...`, `Art 26(9) the deployer's duty to use the information provi...` | tests in P3-tests-art-26 |
| 504 | Art 26(10) | fork | P3-art-26: `Art 26(10) the deployer has limited each use to what is st...`, `Art 26(10) the deployer has requested an authorisation for...` (+2) | see F-26-10-ex-ante, F-undue-delay; tests in P3-tests-art-26 |
| 505 | Art 26(10) continued | fork | P3-art-26: `Art 26(10) the deployer has stopped the use and deleted th...`, `Art 26(10) the deployer's duty to stop the use immediately...` | see F-immediately; tests in P3-tests-art-26 |
| 506 | Art 26(10) continued | encoded | P3-art-26: `Art 26(10) the decision may not be taken`, `Art 26(10) the deployer's duty not to use the system in an...` (+1) | tests in P3-tests-art-26 |
| 507 | Art 26(10) continued | encoded | P3-art-26: `Art 26(10) the paragraph is without prejudice to the data...` | tests in P3-tests-art-26 |
| 508 | Art 26(10) continued | encoded | P3-art-26: `Art 26(10) the deployer has documented each use in the rel...`, `Art 26(10) the deployer has made each use available to the...` (+2) | tests in P3-tests-art-26 |
| 509 | Art 26(10) continued | fork | P3-art-26: `Art 26(10) the deployer has submitted the annual report on...`, `Art 26(10) the deployer's duty to submit the annual report...` (+1) | see F-annual; tests in P3-tests-art-26 |
| 510 | Art 26(10) continued | encoded | P3-art-26: `Art 26(10) the Member State may introduce the law` | tests in P3-tests-art-26 |
| 511 | Art 26(11) | encoded | P3-art-26: `Art 26(11) Article 13 of Directive (EU) 2016/680 applies`, `Art 26(11) the deployer has informed the natural persons t...` (+1) | tests in P3-tests-art-26 |
| 512 | Art 26(12) | encoded | P3-art-26: `Art 26(12) the deployer has cooperated with the relevant c...`, `Art 26(12) the deployer's duty to cooperate with the relev...` | tests in P3-tests-art-26 |
| 513 | Article 27 heading | inert (1) |  | a heading: not operative |
| 514 | Article 27 title | inert (1) |  | a heading: not operative |
| 515 | Art 27(1) | fork | P3-art-27: `Art 27(1) the deployer has performed the assessment of the...`, `Art 27(1) the deployer is required to perform an assessmen...` (+1) | see F-prior-to; tests in P3-tests-art-27 |
| 516 | Art 27(1)(a) | encoded | P3-art-27: `Art 27(1) the deployer has performed the assessment of the...`, `Art 27(1) the deployer is required to perform an assessmen...` (+1) | tests in P3-tests-art-27 |
| 517 | Art 27(1)(b) | encoded | P3-art-27: `Art 27(1) the deployer has performed the assessment of the...`, `Art 27(1) the deployer is required to perform an assessmen...` (+1) | tests in P3-tests-art-27 |
| 518 | Art 27(1)(c) | encoded | P3-art-27: `Art 27(1) the deployer has performed the assessment of the...`, `Art 27(1) the deployer is required to perform an assessmen...` (+1) | tests in P3-tests-art-27 |
| 519 | Art 27(1)(d) | encoded | P3-art-27: `Art 27(1) the deployer has performed the assessment of the...`, `Art 27(1) the deployer is required to perform an assessmen...` (+1) | tests in P3-tests-art-27 |
| 520 | Art 27(1)(e) | encoded | P3-art-27: `Art 27(1) the deployer has performed the assessment of the...`, `Art 27(1) the deployer is required to perform an assessmen...` (+1) | tests in P3-tests-art-27 |
| 521 | Art 27(1)(f) | encoded | P3-art-27: `Art 27(1) the deployer has performed the assessment of the...`, `Art 27(1) the deployer is required to perform an assessmen...` (+1) | tests in P3-tests-art-27 |
| 522 | Art 27(2) | encoded | P3-art-27: `Art 27(2) the deployer has taken the necessary steps to up...`, `Art 27(2) the deployer may rely on a previous assessment` (+2) | tests in P3-tests-art-27 |
| 523 | Art 27(3) | encoded | P3-art-27: `Art 27(3) the deployer has notified the market surveillanc...`, `Art 27(3) the deployer's duty to notify the market surveil...` (+1) | tests in P3-tests-art-27 |
| 524 | ▼M1 REPLACED | inert (1) |  | a marker of the consolidation: it says which text follows (the replaced text is quoted in the version functions) |
| 525 | Art 27(4) | fork | P3-art-27: `Art 27(4) as amended the deployer may include cross-refere...`, `Art 27(4) the assessment stands as paragraph 4 provides` (+2) | see F-27-4-meaning; tests in P3-tests-art-27; version dispatch (as enacted, as amended) |
| 526 | Art 27(5) | encoded | P3-art-27: `Art 27(5) as amended the AI Office has developed the templ...`, `Art 27(5) the AI Office has developed the template` (+1) | tests in P3-tests-art-27; version dispatch (as enacted, as amended) |

Totals: 60 encoded, 60 fork, 32 inert (1) (152 rows for 153 non-blank lines; consecutive lines with the same provision, forks and functions share a row).
The 7 marker lines (`▼M1 REPLACED` and `▼B`) and the 26 heading lines (33 lines, 32 rows) are the only `inert` rows, all reason 1.
No row is `repealed or blank`: the consolidated text shows the replaced paragraphs as `▼M1 REPLACED` followed by the amended text.

## Fork register (P3)

Each entry: the site, the readings and the text that licenses each, the answer taken, the rule that carries it.
The answers taken are this part's, assumed, not ruled; a human reviewer may overrule any of them.
The Guide's rulings govern what they cover (the periods ruling of 2026-11-05, the delegated-definitions ruling of 2026-11-05, the grant ruling of 2026-11-12); where this part departs from the plain reading of a ruling the entry says so.
Each entry at a split site has an **Authority** line: the line of `inputs/ENCODING-GUIDE.md` (section 5, "Rulings on negatives and legal effects"; line numbers are the file's) that the answer taken relies on, in the Guide's own words.
A build step checks that every Guide quotation below occurs in that file.
The grant ruling of 2026-11-12 is not in the Guide copy among the inputs and the lead's brief is not an input file either, so it is cited as a paraphrase of the brief, marked as such, and not as a quotation: a function named for a grant or a power ("may") answers `NOTHING` when an "if" gate fails, with a fork line.

- **F-when-upon** (a convention; sites below).
  A function named for the performance of a duty ("has kept", "has provided", "has informed") answers `NOTHING` when the duty's own trigger is absent: "upon a reasoned request" (Art 16(k), 21(1), 21(2), 22(3) copy, 23(6), 24(5)), "when under their control" (Art 16(e)), "to the extent such logs are under their control" (Art 19(1)), "where relevant" (Art 26(5)), "to the extent the deployer exercises control over the input data" (Art 26(4)), "where applicable" (Art 26(9)), "while ... under their responsibility" (Art 23(4), 24(3)) and the rest of this kind.
  A function named for an effect or a bar ("is barred", "is no longer a provider", "applies mutatis mutandis") answers `JUST FALSE` when the "Where", "When" or "If" of its own sentence fails and `JUST FALSE` once an "until" is reached: Art 23(2), Art 24(2), Art 25(2) first and last subparagraphs, Art 26(8).
  The other reading for the performance functions: `JUST FALSE`, because rule (b) of the periods ruling and item (c) of the delegated-definitions ruling (both 2026-11-05) say a failed "where", "when" or "upon" gives `JUST FALSE`.
  Why this part takes `NOTHING` there: line 95 lists "a duty whose "if" or "where" is unmet" among the questions the rulings leave open, so it is decided on the text's own words; a function that asks whether a duty was performed, with the duty never triggered, would answer "no, it was not performed" when the text never made it due, which the text does not say in its own words.
  Authority, performance functions (a duty whose "where", "if" or "upon" is unmet): `ENCODING-GUIDE.md` line 95 (the maintainer, typed 2026-11-05T10:25:24Z): six questions "the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment", among them "a duty whose "if" or "where" is unmet"; "Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover."
  This entry is that fork line.
  Authority, effect and bar functions (the "Where", "When" or "If" of the sentence that gives the effect or the bar fails): line 93, rule (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; line 94, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above".
  Authority, an "until" bar (Art 23(2), Art 24(2)): line 94, item (d): ""the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X)".
  Authority, a scope limit with no "only" (the role in Art 26(8): "such deployers" are the public authorities and Union bodies): line 93, rule (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`".
  Carried by the `NOTHING-kind (limited by its own wording)` branches of the functions named above (72 branches of that kind in this part).
- **F-bare-shall** (Art 16 chapeau with points (a) to (l); every plain "shall" of Articles 17 to 27 that has no condition of its own).
  A duty that applies and whose act is not done answers `JUST FALSE`.
  The other reading: `NOTHING`, because the text does not say what follows.
  The keel took the same reading for Art 4(1) (its F-4-1).
  Carried by `Art 16(a) the provider has ensured ...` to `Art 16(l)` and by the matching functions of Articles 17 to 27.
  Authority: line 95 names "a bare "must" not done" among the questions the rulings leave open ("decided site by site, at encoding time, on the text's own words and the encoder's best judgment"); this entry is the fork line it asks for.
- **F-prior-to** (Art 16(f) conformity assessment before placing, 22(1), 23(1), 24(1), 26(7), 27(1)).
  "Before placing", "prior to making available", "before putting into service or using", "prior to deploying" are read as an inclusive deadline: the act is timely on the day itself.
  The date is the placement date in the `AI system` record (importer, authorised representative, Art 16(f)) or a date the distributor or deployer states.
  The other reading: a strict "before", so the day itself is late.
  Carried by the `WITHIN` of the rules `Art 16(f) ...`, `Art 22(1) ...`, `Art 23(1) ...`, `Art 24(1) ...`, `Art 26(7) ...`, `Art 27(1) ...`.
- **F-immediately** (Art 20(1), 20(2), 22(4), 24(4), 26(5), 26(10) rejected authorisation).
  "Immediately" and "with immediate effect" are read as the same day on a clock of whole days (`WITHIN 0`).
  The other reading: no deadline is stated, so a late act reads `FULFILLED`.
  Carried by the `WITHIN 0` clauses of the rules named.
- **F-undue-delay** (Art 26(5), 26(10) first subparagraph).
  "Without undue delay" has no number, so no deadline is encoded and no trace can show a breach of it.
  The other reading: a fixed number of days chosen by the encoder, which the text does not give.
  Art 26(10)'s "no later than 48 hours" is a number and is encoded (F-26-10-ex-ante).
- **F-17-2** (`Art 17(2) as amended the provider has met paragraph 2`).
  The Omnibus adds "in particular, if the provider is an SME, including a start-up, or an SMC" to the first sentence.
  Reading taken: an emphasis on the small provider and not a different standard, so both versions answer alike and no SME fact is an input.
  The other reading: the SME facts change the proportion required, which would need an input and a test the text does not give.
  The four assertions of `P3-tests-art-17.l4` that put the two versions side by side show the choice.
- **F-17-3** (`Art 17(3) the provider may include the aspects ...`).
  A power ("may include") limited in its own wording to providers "that are subject to obligations regarding quality management systems or an equivalent function under relevant sectoral Union law": a provider outside that limit answers `NOTHING`.
  The other reading: `JUST FALSE`.
  Authority: line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" (the answer is `NOTHING`).
  The limit is a relative clause and not a condition introduced by "if", "where", "when" or "upon", so line 93 rule (b) and line 94 item (c) are not engaged.
- **F-18-1** (`Art 18(1)`, `Art 23(5)`).
  The 10 years run from the placement on the market or putting into service ("a period ending 10 years after"); the last day is the tenth anniversary (`add years`).
  The period itself is a function (`Art 18(1) the period for keeping the documentation runs on the date asked`): `JUST TRUE` inside, `JUST FALSE` after the last day, `NOTHING` before the placement (the text gives the period no start).
  The "keeps" functions (`Art 18(1) the provider keeps the documents ...`, `Art 23(5) the importer keeps the copies for the period`) answer `JUST FALSE` after the last day and `NOTHING` before the placement.
  Read `JUST FALSE` after the period as "the duty is not on", not as "the documents are not kept".
  The other reading after the period: `NOTHING` (the duty to keep has ended, so nothing is asked); the other reading before the placement: `JUST FALSE` (outside the period).
  Authority, after the last day: line 93, rule (a): "a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`".
  The text fixes the end ("a period ending 10 years after", "for a period of 10 years after").
  Before the placement: no Guide line names a period that has an end and no start; the nearest is line 87, "is silent" (the text names the end of the period and gives it no start), so this site fits none of them closely and is listed under Marginal readings (11).
- **F-23-3-places** (`Art 23(3) the importer has indicated its name ...`).
  "Where applicable" qualifies the places of the indication (the system, its packaging, its accompanying documentation): one input says the indication is made at each place where it applies.
  The other reading: one input per place, so a missing indication at one place is separately visible.
- **F-24-as-applicable** (`Art 24(2)`, `Art 24(4)`).
  In 24(2) "the provider or the importer, as applicable": the importer where there is one, otherwise the provider.
  In 24(4) "the provider or importer" has no "as applicable": informing either meets the limb.
  The other reading for 24(2): both are informed.
- **F-25-1-closed** (`Art 25(1)`, `Art 25(3)`).
  "In any of the following circumstances" and "under either of the following circumstances" are not closed with "only", so a party meeting none of them answers `NOTHING`, not "not a provider".
  The other reading: `JUST FALSE`.
  Authority: line 87: "where the text lists without closing the list" (the answer is `NOTHING`).
- **F-26-5-deeming** (`Art 26(5) the monitoring obligation is deemed to be fulfilled`).
  The deeming reaches "the monitoring obligation set out in the first subparagraph", read as the duty to monitor and not the duty to inform providers.
  The other reading: it covers both duties of the first subparagraph.
- **F-26-10-ex-ante** (`Art 26(10) the deployer has requested an authorisation`).
  "Ex ante, or without undue delay and no later than 48 hours after the use": the 48 hours are counted from the start of the use, and an ex ante request is at hour 0.
  The other reading: 48 hours from the identification of the suspect.
- **F-annual** (`Art 26(10) the deployer has submitted the annual report`).
  "Annual" names a period and no start: the report is due within 365 days of the date asked.
  The other reading: a calendar year.
- **F-27-4-meaning** (`Art 27(4)`).
  The dispatcher answers "the assessment stands as paragraph 4 provides": as enacted that is a duty to complement the data protection impact assessment (`JUST TRUE` when it does, `JUST FALSE` when it does not, `NOTHING` where no obligation is already met through it); as amended it is a permission to cross-refer (`JUST TRUE` when both limbs hold, `NOTHING` when either fails: the grant ruling of 2026-11-12).
  The other reading: the same word for both versions.
  Authority, as amended (a grant gated by "If" and "when conducting"): the grant ruling of 2026-11-12 as the lead's brief states it (a paraphrase, see the head of this register: a grant answers `NOTHING` when an "if" gate fails) and line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit".
  Read literally, line 86 ("a condition the text introduces with "if"") and line 94 item (c) ("when" counts as "where") would give `JUST FALSE`; this part follows the grant ruling (Marginal readings 12).
  Authority, as enacted ("If ... shall complement"; the "If" unmet answers `NOTHING`): line 95, "a duty whose "if" or "where" is unmet" (decided site by site), and this entry is the fork line.
- **F-gate-2-13** (`Section 3 gate`).
  Where Art 2(13) lets the requirement or obligation be limited ("may be limited, where and to the extent that"), the gate answers `NOTHING` for the provision: which obligations and to what extent is for delegated acts under Article 97, outside the sources.
  The keel's own site (F-2-13) answers `JUST FALSE` when a condition of the "may" fails; this gate uses only the keel's `JUST TRUE` and so asks nothing the keel answers differently.
  The other reading: the provision applies in full until the Commission acts.
  Art 2(13) names Articles 9 to 15 and 17 to 25 (consolidated line 58), so Articles 16, 26 and 27 are never limited by it.
  Authority: line 87: "points outside the sources" (the delegated acts under Article 97) gives `NOTHING`.
  This arm answers `NOTHING` when the keel says the requirement may be limited; where a condition of the keel's "may" fails the keel answers `JUST FALSE` (its fork F-2-13, line 93 rule (b)) and this gate then lets the provision answer, so the two do not conflict.
- **F-bars** (`Art 26(10) the use is barred as untargeted`, `Art 26(10) the decision may not be taken`).
  The third subparagraph says "In no case shall such high-risk AI system ... be used for law enforcement purposes in an untargeted way, without any link to a criminal offence, a criminal proceeding, a genuine and present or genuine and foreseeable threat of a criminal offence, or the search for a specific missing person", and "no decision that produces an adverse legal effect on a person may be taken by the law enforcement authorities based solely on the output of such post-remote biometric identification systems".
  Each prohibition limits itself in its own wording ("without any link", "solely"): a use with a link, or a decision that rests on more than the output, falls outside the limit and answers `NOTHING`; the elements of scope (law enforcement purposes; an adverse legal effect; taken by the authorities) answer `NOTHING` when they fail.
  The other reading: `JUST FALSE` for the limit, "without any link" read like "unless there is a link" and "solely" like "only".
  Authority: line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" (the answer is `NOTHING`).
  Neither limit is introduced by "if", "where", "when" or "upon", and neither is a list closed with "only", so line 86 and line 93 rule (b) are not engaged.
  This differs from Art 23(2), Art 24(2) and Art 26(8), whose bars begin with "Where" or "When" (F-when-upon).
- **F-may-limited** (`Art 26(10) the Member State may introduce the law`, `Art 27(2) the deployer may rely on a previous assessment`, `Art 27(3)` for the words "may be exempt").
  A grant limited in its own wording ("in accordance with Union law"; "in similar cases"; "In the case referred to in Article 46(1)") answers `NOTHING` when the case falls outside the limit.
  In Art 27(3) the caller states that the deployer is in the Article 46(1) case and exempt: the duty to notify then answers `NOTHING` ("may be exempt" is a grant and not a statement that the duty is off); where it is not exempt the duty answers as a bare "shall" (F-bare-shall).
  The other reading: `JUST FALSE`.
  Authority: line 87: "limits a grant or prohibition in its own wording and the case falls outside the limit" (the answer is `NOTHING`).
  None of the three limits is introduced by "if", "where", "when" or "upon", so line 93 rule (b) and line 94 item (c) are not engaged.
  Art 26(10)'s "The reports may be aggregated to cover more than one deployment" has no limit and no gate: it answers `JUST TRUE` once the Article applies (not a split site).

### Reading a result: FALSE and NOTHING (P3)

In this part a `JUST FALSE` is the text's own "no": a flat "shall" whose act is not done (the bare duties of Articles 16 to 27), a bar whose "Where" or "When" has failed or whose "until" has been reached (Articles 23(2), 24(2), 26(8)), a period the text fixes once it has ended (Articles 18(1), 23(5)), an exception the text names ("with the exception of" in 17(4) and 27(1)), a requirement the text states and the facts miss ("at least six months", "appropriate to the intended purpose", the six points of 27(1)), and Art 2(2)'s "only ... shall apply" for a system cut off from Articles 16 to 27.
A `NOTHING` is "not covered": the provision does not yet apply on the date asked (the gate is shut), Art 2(13) may limit it, the provision limits itself in its own words (a trigger, a scope or a role the case lacks: 72 branches), the list is not closed (4 branches: Art 25(1), 25(3), 25(4)'s list of supplied items, 27(1)'s list of bodies), the text is silent (9), or it points outside the sources (3: the delegated acts under Article 97 in the gate, and other Union or national law on the keeping of logs in Art 19(1) and Art 26(6)).
No branch uses "includes" or an undefined term as its reason.
A caller never turns `NOTHING` into `FALSE`.
There are 104 `FALSE-kind` tags and 91 `NOTHING-kind` tags in layer 1 (counted by grep over `P3-section-3.l4` and `P3-art-16.l4` to `P3-art-27.l4`); each no-branch carries its quoted words and each not-covered branch its reason.
A decision function returns `MAYBE BOOLEAN` throughout; the seat questions return it unchanged (the role and applicability questions of the seats wrap a keel `BOOLEAN` in `JUST`).

## Jural relations (P3)

One row per provision that creates a relation; a provision that creates none is `none`.
The party holding the right, privilege, power or immunity is in the third column, the bearer of the correlative in the fourth.
The competent authorities are named as holders where the text says "shall" to a private party and names no other beneficiary; the text names none, so this is the encoder's reading of who may enforce.

| provision | relation | holder | bearer | L4 rule |
| --- | --- | --- | --- | --- |
| Art 16 chapeau, (a) to (l) | duty | the national competent authorities (claim) | the provider | `Art 16(a) the provider's duty ...` to `Art 16(l) ...` |
| Art 16(k) | power and duty | a national competent authority (power to request) | the provider (duty to demonstrate on request) | `Art 16(k) the provider's duty to demonstrate ...` |
| Art 17(1), (2) | duty | the competent authorities (claim) | the provider | `Art 17(1) ...`, two `Art 17(2) ...` rules |
| Art 17(3) | privilege | a provider subject to sectoral quality management obligations | the authorities (no-right) | `Art 17(3) the provider's permission ...` |
| Art 17(4) | immunity | a provider that is a financial institution, from the aspects other than (g), (h), (i) | the authorities (disability) | `Art 17(4) ...` functions (decision functions only) |
| Art 18(1) | duty | the national competent authorities (claim) | the provider | `Art 18(1) the provider's duty to keep ...` |
| Art 18(2) | duty | the national competent authorities (claim, that the documents stay available) | the Member State | `Art 18(2) the Member State's duty ...` |
| Art 18(3), 19(2) | duty | the financial supervisory authorities (claim) | a provider that is a financial institution | `Art 18(3) ...`, `Art 19(2) ...` |
| Art 19(1) | duty | the competent authorities (claim) | the provider | `Art 19(1) the provider's duty to keep the logs ...` |
| Art 20(1), (2) | duty | the distributors, deployers, authorised representative, importers, market surveillance authorities and notified body (claim to be informed) | the provider | four `Art 20 ...` rules |
| Art 21(1), (2) | power and duty | a competent authority (power to request) | the provider | `Art 21(1) ...`, `Art 21(2) ...` |
| Art 21(3) | duty | the provider (claim that what it supplies is treated in confidence) | the competent authority | `Art 21(3) the competent authority's duty ...` |
| Art 22(1) | duty | the authorities (claim) | a provider established in a third country | `Art 22(1) ...` |
| Art 22(2) | duty | the authorised representative (claim to be enabled) | the provider | `Art 22(2) ...` |
| Art 22(3) | duty | the provider (claim to performance of the mandate), the authorities (claim to the copy) | the authorised representative | two `Art 22(3) ...` rules |
| Art 22(3) last subparagraph | power | the competent authorities (to address the representative) | the provider (liability) | `Art 22(3) the mandate empowers ...` (decision function) |
| Art 22(4) | duty | the provider and the authorities | the authorised representative | `Art 22(4) ...` |
| Art 23(1), (3), (4), (5), (6), (7) | duty | the competent authorities (claim) | the importer | the `Art 23 ...` rules |
| Art 23(2) | duty (a bar, then a duty to inform) | the authorities, the provider and the representative (claim) | the importer | two `Art 23(2) ...` rules |
| Art 24(1), (3), (4), (5), (6) | duty | the competent authorities (claim) | the distributor | the `Art 24 ...` rules |
| Art 24(2) | duty (a bar, then a duty to inform) | the authorities, the provider and the importer (claim) | the distributor | two `Art 24(2) ...` rules |
| Art 25(1), (3) | liability | the authorities (to hold the party to the provider's obligations) | the distributor, importer, deployer or other third party; the product manufacturer | `Art 25(1) ...`, `Art 25(3) ...` (decision functions) |
| Art 25(2) | immunity, and duty | the initial provider (immunity from being a provider of that system); the new providers (claim to cooperation) | the authorities (disability); the initial provider (duty) | `Art 25(2) ...` (two rules) |
| Art 25(4) | duty, mutual | each of the provider and the third party (claim to the written agreement) | the other | `Art 25(4) the provider's duty ...`, `Art 25(4) the third party's duty ...` |
| Art 25(4) second subparagraph | privilege | the AI Office (to develop and recommend model terms) | providers and third parties (no-right) | `Art 25(4) the AI Office's permission ...` |
| Art 25(5) | immunity | the holders of intellectual property rights, confidential business information and trade secrets | the provider (disability under paragraphs 2 and 3) | `Art 25(5) ...` (decision function) |
| Art 26(1), (2), (4), (5), (6), (9), (12) | duty | the competent authorities (claim) | the deployer | the `Art 26 ...` rules |
| Art 26(3) | none (a saving clause: other obligations and the freedom to organise resources are untouched) | | | `Art 26(3) ...` (decision function) |
| Art 26(7) | duty | the workers' representatives and the affected workers (claim to be informed) | the deployer that is an employer | `Art 26(7) ...` |
| Art 26(8) | duty and bar | the authorities (claim) | a deployer that is a public authority or Union body | three `Art 26(8) ...` rules |
| Art 26(10) | power and duty | the judicial or administrative authority (power to authorise); the market surveillance and data protection authorities (claim) | the law enforcement deployer | the `Art 26(10) ...` rules |
| Art 26(10) third subparagraph | immunity | a person (from an adverse decision based solely on the output) | the law enforcement authorities (disability) | `Art 26(10) the decision may not be taken` (decision function) |
| Art 26(11) | duty | the natural persons (claim to be informed) | the deployer | `Art 26(11) ...` |
| Art 27(1), (2), (3) | duty | the authorities (claim) | the deployer (a public body, a private entity providing public services, or a deployer of the Annex III points 5(b) and (c) systems) | the `Art 27 ...` rules |
| Art 27(4) | duty as enacted; privilege as amended | the authorities; the deployer | the deployer; the authorities (no-right) | `Art 27(4) the deployer's duty or permission ...` |
| Art 27(5) | duty | the deployers (claim to a template) | the AI Office | `Art 27(5) the AI Office's duty ...` |

## Marginal readings for a lawyer (P3)

Each branch that rests on reading (a), a failed "if" or "where" counts as the text's no (and a flat negative counts as the text saying no), or reading (b), a prohibition or grant limited by its own wording does not.
For each, the other reading is stated; the Guide line each rests on is in the fork register.

1. Every bare "shall" of Articles 16 to 27 not done answers `JUST FALSE` (reading (a); fork F-bare-shall). Other reading: `NOTHING`.
2. Art 2(2): a provision of Articles 16 to 27 cut off for a Section B system answers `JUST FALSE` (reading (a): "only Article 6(1), Article 60a and Articles 102 to 112 shall apply"). Other reading: `NOTHING`.
3. Art 23(2) and Art 24(2): a bar whose "Where" fails, or whose "until" is reached, answers `JUST FALSE` (reading (a): line 93 rule (b), line 94 items (c) and (d); fork F-when-upon). Other reading: `NOTHING`.
4. Art 25(2): "Where the circumstances referred to in paragraph 1 occur" failing, or the carve-out "This paragraph shall not apply", answers `JUST FALSE` for the effect ("no longer considered to be a provider") (reading (a)). Other reading: `NOTHING`. The duty to cooperate answers `NOTHING` in the same cases (reading (b); fork F-when-upon).
5. Art 17(4) with an aspect that is (g), (h) or (i), and Art 27(1) for a system intended for the area of point 2 of Annex III: the named exception answers `JUST FALSE` (reading (a)). Other reading: `NOTHING`.
6. Art 26(8) second sentence: the "When" that has not happened answers `JUST FALSE` (reading (a): line 94 item (c) with line 93 rule (b)); the role itself answers `NOTHING` (line 93 rule (c)). Other reading: `NOTHING` for the "When".
7. Art 26(10) third subparagraph (untargeted use; decision based solely on the output): every element that fails answers `NOTHING`, including the limit itself ("without any link", "solely") (reading (b); fork F-bars). Other reading: `JUST FALSE` for the limit, "without any link" read like "unless there is a link" and "solely" like "only".
8. Art 19(1), Art 26(6): fewer than six months, or a period not appropriate to the intended purpose, answers `JUST FALSE` (the text states the requirement). Other reading: `NOTHING`, because "at least" names a floor and not an end.
9. Every "has met" function whose trigger is absent answers `NOTHING` (reading (b); fork F-when-upon, authority line 95). Other reading: `JUST FALSE` (reading (a): line 93 rule (b), line 94 item (c)).
10. Art 18(1), Art 23(5): after the last day of the ten years the "keeps" functions answer `JUST FALSE` (line 93 rule (a); fork F-18-1) and this reads "the duty is not on", not "the documents are not kept", so a caller who asks "do I keep them?" after the period gets `JUST FALSE` whether or not it still does. Other reading: `NOTHING`, the duty having ended.
11. Art 18(1), Art 23(5), the period function of Art 18(1): before the placement the answer is `NOTHING` because the text names the end of the period and gives it no start (line 87, "is silent"; fork F-18-1). This site fits no Guide line that names a period with no start. Other reading: `JUST FALSE` (outside the period, line 93 rule (a)).
12. Art 17(3), Art 26(10) Member State, Art 27(2) may rely, Art 27(3) may be exempt, Art 27(4) as amended: a grant limited by its own wording answers `NOTHING` when the case falls outside the limit (reading (b); line 87; fork F-17-3, F-may-limited, F-27-4-meaning). For Art 27(4) as amended the limit is introduced by "If" and "when", where line 86 and line 94 item (c) read literally give `JUST FALSE`: the answer rests on the grant ruling of 2026-11-12 as the brief states it, which is not in the Guide copy, and this site is the one a lawyer should check first. Other reading: `JUST FALSE`.
13. Art 2(13) in the gate: when the keel says the requirement may be limited, the gate answers `NOTHING` because the extent is for delegated acts outside the sources (line 87, "points outside the sources"; fork F-gate-2-13). Other reading: the Article applies in full until the Commission acts.
14. Art 25(1) and Art 25(3): a party meeting none of the listed circumstances answers `NOTHING` (reading (b); line 87, "where the text lists without closing the list"; fork F-25-1-closed). Other reading: `JUST FALSE`.
15. Art 25(4): an item that is not on the paragraph's list (before 27 July 2026 an AI model is not on it) answers `NOTHING` because the list is not closed; the free and open-source carve-out answers `NOTHING` (reading (b)). Other reading: `JUST FALSE`.
16. Art 17(2): the SME wording the Omnibus adds is read as emphasis and not as a different standard, so both versions answer alike (fork F-17-2). Other reading: the SME facts change the proportion required.

## Seams (P3)

PLAN.md section 4 gives this part's row as "takes S1, S6, S8, S14, S15".
A part cannot import another part, so a provision that needs another part's answer takes it as an input named for the section it comes from; the lead wires it at the merge.
Nothing in section 4 has Articles 16 to 27 as the answering provision, so this part provides no seam input; what other parts must ask of Article 25 is in "Seats (P3)".

| seam | taken or provided | input or call | how it is wired here |
| --- | --- | --- | --- |
| S1 | taken | `the route by which the AI system is high-risk` (`Route to high-risk`) | Asked by every seat question, put in the keel's `AI system` record (`route`) in the question's `WHERE`; `Section 3 gate` reads `the AI system`'s `route` for `Art 113 the provision group applies`, `Art 2(2)` and `Art 2(13)`; `Route neither` has no date, so the gate is shut and the answer is `NOTHING` |
| S2 | taken (not in this part's row; the roles come from the keel) | none: the keel's `Art 3(3)` to `Art 3(7)` and `Art 3(63)`, `Art 2(1)(e)`, `Art 2(1)(g)` | Called by the role and applicability questions of each seat (`P3-seat-<slug>.l4`); a layer-1 function assumes its party's role and does not re-ask it |
| S6 | taken | `the conformity assessment procedure of Article 43 has been completed`, `the EU declaration of conformity of Article 47 has been drawn up`, `the AI system has been registered under Article 49` (each `BOOLEAN`), and for Article 48 `the CE marking of Article 48 has been affixed to the high-risk AI system` with two siblings of this part's own (`it is not possible to affix the CE marking to the high-risk AI system`, `the CE marking of Article 48 has been affixed on its packaging or its accompanying documentation`) | Plain inputs of `Art 16(f)`, `Art 16(g)`, `Art 16(h)` and `Art 16(i)` in `P3-art-16.l4`; Article 49 is also an input of `Art 26(8)` (the registration obligations) |
| S8 | taken | `the high-risk AI system complies with the requirements set out in Chapter III, Section 2` (`BOOLEAN`) | Plain input of `Art 16(a)` in `P3-art-16.l4`; the other inputs that speak of Section 2 (`Art 16(k)`, `Art 21(1)`, `Art 23(4)`, `Art 23(6)`, `Art 24(2)` to `24(5)`) state what the party has ensured, demonstrated, provided or considers, and are not S8's answer |
| S13 | taken | `the date asked`, `the date the AI system was placed on the market or put into service`, `the AI system has been significantly changed in its design since the date of application of Chapter III` | An input of every decision function and of every seat question, with the exact `@desc` of PLAN.md section 8; the other two sit in the `AI system` record; `Section 3 gate` passes them to `Art 113 the provision group applies` |
| S14 | taken | the `Article reference` of the provision and the inputs of `Art 2(2) the provision applies to the high-risk AI system under Article 6(1) with Section B products` | `Section 3 gate` in `P3-section-3.l4`: `JUST FALSE` from the keel gives `Section 3 cut off by Article 2(2)`, which every decision function turns into `JUST FALSE`; `NOTHING` lets the part answer on its own provision; the Section B flag is in `Section 3 circumstances`, built in each seat question, with the two Art 2(13) facts |
| S15 | taken | `Art 2(13) the application of the requirement or obligation may be limited`, with the `Article reference` | `Section 3 gate`: `JUST TRUE` from the keel gives `Section 3 may be limited under Article 2(13)` (`NOTHING`, fork F-gate-2-13); any other answer lets the part answer; Articles 16, 26 and 27 are not named in Art 2(13) |

Seams not in PLAN.md section 4, taken as plain `BOOLEAN` inputs named for the section or the other instrument they come from (the lead wires or leaves them):
- Article 79(1), "presents a risk within the meaning of Article 79(1)" (Art 20, 23, 24, 26).
  PLAN.md's S11 is a different input, asked by Articles 80 to 83.
- Articles 9, 40, 72 and 73 (Art 17(1) and (4)); Articles 11 and 12(1) (Art 18, 19, 21, 23); Article 13 (Art 26(9), 27); Article 44 (Art 20(2)); Article 46(1) (Art 27(3)); Article 71 (Art 26(8)); Article 6 (Art 25(1)(b)); Article 35 of Regulation (EU) 2016/679 and Article 27 of Directive (EU) 2016/680 (Art 26(9), 27(4)).
- S12 (SME and SMC) is not taken: the SME wording the Omnibus adds to Art 17(2) is read as emphasis (fork F-17-2).
- The serious incident of Art 26(5) is a plain input (`the deployer has identified a serious incident`); this part does not call the keel's `Art 3(49)` that S10 names for Article 73.
- S3, S4, S5, S7, S9 and S16 are not used by this part.

## Split sites (P3)

Line numbers below are those of the modules in this folder; the Guide lines are the file's lines of `inputs/ENCODING-GUIDE.md`, quoted in the fork register.

(i) An unmet element of an infringement: 5 sites, all prohibitions, because Articles 16 to 27 name no infringement and no penalty (the penalties are in another part).
- `Art 23(2) the importer is barred from placing the high-risk AI system on the market` at `P3-art-23.l4:88` answers `JUST FALSE` when the "Where" fails and when the "until" is reached: line 93 rule (b), line 94 items (c) and (d); fork F-when-upon.
- `Art 24(2) the distributor is barred from making the high-risk AI system available on the market` at `P3-art-24.l4:78` answers the same: line 93 rule (b), line 94 items (c) and (d); fork F-when-upon.
- `Art 26(8) the deployer is barred from using the system` at `P3-art-26.l4:629` answers `NOTHING` when the deployer is not a public authority or Union body (line 93 rule (c)) and `JUST FALSE` when the "When" has not happened (line 94 item (c), line 93 rule (b)); fork F-when-upon.
- `Art 26(10) the decision may not be taken` at `P3-art-26.l4:922` answers `NOTHING` when no adverse decision is taken by the authorities and `NOTHING` when the decision rests on more than the output (line 87); fork F-bars.
- `Art 26(10) the use is barred as untargeted` at `P3-art-26.l4:879` answers `NOTHING` when the system is not used for law enforcement and `NOTHING` when a link to an offence, a proceeding, a threat or a missing person exists (line 87); fork F-bars.
The sites split by what introduces the unmet element: a "Where", "When" or "until" gives `JUST FALSE`, a limit in the prohibition's own wording gives `NOTHING`.

(ii) A "may" gated by "where", "when", "upon", "on application" or "with the consent of": 6 sites, each answering `NOTHING` when the gate fails, when the case falls outside the limit, or (Art 27(3)) when the exemption is the case:
- `Art 17(3) the provider may include the aspects listed in paragraph 1 as part of the quality management systems pursuant to sectoral Union law` at `P3-art-17.l4:163` (fork F-17-3; line 87),
- `Art 26(10) the Member State may introduce the law` at `P3-art-26.l4:1084` (fork F-may-limited; line 87),
- `Art 27(2) the deployer may rely on a previous assessment` at `P3-art-27.l4:175` (fork F-may-limited; line 87),
- `Art 27(3) the deployer has notified the market surveillance authority of the results` at `P3-art-27.l4:238` for the words "may be exempt" (fork F-may-limited; line 87),
- `Art 27(4) as amended the deployer may include cross-references to the data protection impact assessment or relevant parts of it` at `P3-art-27.l4:296` (fork F-27-4-meaning; the brief's grant ruling of 2026-11-12 and line 87),
- the gate's Art 2(13) arm at `P3-section-3.l4:69` (fork F-gate-2-13; line 87, "points outside the sources").
The keel's one site, Art 2(13), answers `JUST FALSE` when a condition fails (its F-2-13, line 93 rule (b)); this part's gate uses only its `JUST TRUE` and does not repeat that answer.
Art 17(3), Art 26(10) Member State, Art 27(2) and Art 27(3) are limited by their own wording and not gated by "where", "when" or "upon"; they are counted here because the Guide's grant line (87) is the line they rest on.
No answer was changed to match another part.

## Rules with no breach path (P3)

Each is a `MUST` or `MAY` with no time limit (no `WITHIN`) in a rule whose consequence arm cannot fire: a late act reads `FULFILLED`, and a missed act leaves the trace `RESIDUAL`.
The `LEST BREACH` arm written on these rules is for form and is unreachable; no deadline and no consequence the text does not state was added.
There are 61 such rules (of 84 regulative rules in layer 1):
- `Art 16(a) the provider's duty to ensure that the high-risk AI system is compliant with the requirements set out in Section 2` (MUST)
- `Art 16(b) the provider's duty to indicate its name, registered trade name or registered trade mark and its contact address` (MUST)
- `Art 16(c) the provider's duty to have a quality management system in place` (MUST)
- `Art 16(d) the provider's duty to keep the documentation referred to in Article 18` (MUST)
- `Art 16(e) the provider's duty to keep the logs automatically generated by its high-risk AI system` (MUST)
- `Art 16(g) the provider's duty to draw up an EU declaration of conformity` (MUST)
- `Art 16(h) the provider's duty to affix the CE marking` (MUST)
- `Art 16(i) the provider's duty to comply with the registration obligations referred to in Article 49(1)` (MUST)
- `Art 16(j) the provider's duty to take the necessary corrective actions and provide information as required in Article 20` (MUST)
- `Art 16(k) the provider's duty to demonstrate the conformity of the high-risk AI system upon a reasoned request` (MUST)
- `Art 16(l) the provider's duty to ensure that the high-risk AI system complies with accessibility requirements` (MUST)
- `Art 17(1) the provider's duty to put a quality management system in place` (MUST)
- `Art 17(2) the provider's duty to implement the aspects proportionately to the size of its organisation` (MUST)
- `Art 17(2) the provider's duty to respect the degree of rigour and the level of protection` (MUST)
- `Art 17(3) the provider's permission to include the aspects as part of the quality management systems pursuant to sectoral Union law` (MAY)
- `Art 18(3) the provider's duty to maintain the technical documentation as part of the documentation kept under financial services law` (MUST)
- `Art 18(2) the Member State's duty to determine the conditions` (MUST)
- `Art 19(2) the provider's duty to maintain the logs as part of the documentation kept under financial services law` (MUST)
- `Art 20(1) the provider's duty to inform the distributors and, where applicable, the deployers, the authorised representative and importers` (MUST)
- `Art 21(1) the provider's duty to provide the competent authority the information and documentation upon a reasoned request` (MUST)
- `Art 21(2) the provider's duty to give the requesting competent authority access to the automatically generated logs` (MUST)
- `Art 21(3) the competent authority's duty to treat the information obtained in accordance with Article 78` (MUST)
- `Art 22(2) the provider's duty to enable its authorised representative to perform the tasks specified in the mandate` (MUST)
- `Art 22(3) the authorised representative's duty to perform the tasks specified in the mandate` (MUST)
- `Art 22(3) the authorised representative's duty to provide a copy of the mandate to the market surveillance authorities upon request` (MUST)
- `Art 23(2) the importer's duty to inform the provider, the authorised representative and the market surveillance authorities of the risk` (MUST)
- `Art 23(3) the importer's duty to indicate its name, registered trade name or registered trade mark, and its address` (MUST)
- `Art 23(4) the importer's duty to ensure that the storage or transport conditions do not jeopardise compliance with Section 2` (MUST)
- `Art 23(6) the importer's duty to provide the relevant competent authorities the necessary information and documentation upon a reasoned request` (MUST)
- `Art 23(6) the importer's duty to ensure that the technical documentation can be made available to the competent authorities` (MUST)
- `Art 23(7) the importer's duty to cooperate with the relevant competent authorities` (MUST)
- `Art 24(2) the distributor's duty to inform the provider or the importer, as applicable, of the risk` (MUST)
- `Art 24(3) the distributor's duty to ensure that the storage or transport conditions do not jeopardise compliance with Section 2` (MUST)
- `Art 24(4) the distributor's duty to take the corrective actions or ensure that they are taken` (MUST)
- `Art 24(5) the distributor's duty to provide the relevant competent authority the information and documentation upon a reasoned request` (MUST)
- `Art 24(6) the distributor's duty to cooperate with the relevant competent authorities` (MUST)
- `Art 25(2) the initial provider's duty to cooperate closely with the new providers` (MUST)
- `Art 25(2) as amended the initial provider's duty to carry out the particular obligations of points (a) to (c) where relevant` (MUST)
- `Art 25(4) the provider's duty to specify by written agreement` (MUST)
- `Art 25(4) the third party's duty to specify by written agreement` (MUST)
- `Art 25(4) the AI Office's permission to develop and recommend voluntary model terms and its duties once it does` (MAY/MUST)
- `Art 26(1) the deployer's duty to take appropriate technical and organisational measures to use the system in accordance with the instructions for use` (MUST)
- `Art 26(2) the deployer's duty to assign human oversight to natural persons who have the necessary competence, training, authority and support` (MUST)
- `Art 26(4) the deployer's duty to ensure that the input data is relevant and sufficiently representative` (MUST)
- `Art 26(5) the deployer's duty to monitor the operation of the high-risk AI system on the basis of the instructions for use` (MUST)
- `Art 26(5) the deployer's duty to inform providers in accordance with Article 72 where relevant` (MUST)
- `Art 26(5) the deployer's duty to inform the provider or distributor and the relevant market surveillance authority of the risk` (MUST)
- `Art 26(5) the deployer's duty to suspend the use of the system` (MUST)
- `Art 26(6) the deployer's duty to maintain the logs as part of the documentation kept under financial service law` (MUST)
- `Art 26(8) the deployer's duty to comply with the registration obligations referred to in Article 49` (MUST)
- `Art 26(8) the deployer's duty to inform the provider or the distributor that the system has not been registered` (MUST)
- `Art 26(9) the deployer's duty to use the information provided under Article 13 to comply with its obligation to carry out a data protection impact assessment` (MUST)
- `Art 26(10) the deployer's duty to limit each use to what is strictly necessary for the investigation of a specific criminal offence` (MUST)
- `Art 26(10) the deployer's duty to document each use in the relevant police file` (MUST)
- `Art 26(10) the deployer's duty to make each use available to the relevant market surveillance authority and the national data protection authority upon request` (MUST)
- `Art 26(11) the deployer's duty to inform the natural persons that they are subject to the use of the high-risk AI system` (MUST)
- `Art 26(12) the deployer's duty to cooperate with the relevant competent authorities` (MUST)
- `Art 27(2) the deployer's duty to take the necessary steps to update the information` (MUST)
- `Art 27(3) the deployer's duty to notify the market surveillance authority of the results` (MUST)
- `Art 27(4) the deployer's duty or permission concerning the data protection impact assessment` (MAY/MUST)
- `Art 27(5) the AI Office's duty to develop the template` (MUST)

Rules that do reach `BREACH`, each with a trace on both builds (23 rules): the prohibitions `SHANT` (Art 18(1), 19(1), 23(2), 23(5), 24(2), 26(6), 26(8), 26(10) untargeted use) and the duties with a time limit (Art 16(f), 20(1) corrective actions, 20(2) two rules, 22(1), 22(4), 23(1), 24(1), 24(4) informing, 26(5) inform first, 26(7), 26(10) request, stop and annual report, 27(1)).
The rules of the four versioned passages (Art 25(2), Art 25(4) provider and third party, Art 27(4), Art 27(5)) are traced only for dates on or after 2 December 2027, because the gate is shut before it and that date is later than 27 July 2026: their as-enacted arms cannot be reached through the gate and have no trace.
The as-enacted decision functions are tested directly (`Art 17(2) as enacted ...`, `Art 25(2) as enacted ...`, `Art 25(4) as enacted ...`, `Art 27(4) as enacted ...`, `Art 27(5) as enacted ...`), and a test compares each pair where the answer is meant to be the same.

## Versions (P3)

`inputs/AMENDMENTS.md` lists four `▼M1` passages of the consolidated text between lines 374 and 526 (rows "408-408", "475-481", "487-487" and "525-526"; the marker lines are 407, 409, 474, 482, 486, 488 and 524).
All four are `REPLACED`; `inputs/AMENDMENTS.md` lists no `INSERTED` or `DELETED` passage and no other `▼M1` passage between lines 374 and 526.
Each passage has an as-enacted function, an as-amended function and a dispatcher that calls the one in force on `the date asked` (`Omnibus Art 4 the version in force`, boundary 27 July 2026); both versions are encoded, and the test files compare the two.

| provision | what the Omnibus changed | encoded | why |
| --- | --- | --- | --- |
| Art 17(2) (consolidated line 408; base line 926) | adds "in particular, if the provider is an SME, including a start-up, or an SMC" to the first sentence | both versions (`Art 17(2) as enacted the provider has met paragraph 2`, `Art 17(2) as amended ...`, dispatcher `Art 17(2) the provider has met paragraph 2`) | The text is replaced, so the amended text is encoded and the enacted text kept for dates before 27 July 2026; the two answer alike (fork F-17-2: the addition is read as emphasis) |
| Art 25(2) (lines 475 to 481; base line 1008) | adds the subparagraph "In particular, the obligation laid down in the second subparagraph shall include, where relevant for the purposes specified therein, the following: (a) ... (b) ... (c)"; the carve-out gains "to cooperate with the new providers and" (enacted: "does not fall under the obligation to hand over the documentation"); the second sentence's "regarding the compliance with" becomes "with regard to compliance with" | both versions (`Art 25(2) as enacted the initial provider has cooperated`, `Art 25(2) as amended the initial provider has cooperated`, `Art 25(2) as amended the initial provider's duty to carry out the particular obligations of points (a) to (c) where relevant`, dispatchers); the first subparagraph ("no longer considered to be a provider") and the words of the carve-out common to both versions are one function for both | The points (a) to (c) exist only in the amended text, so only the amended version has a function for them; the enacted version has no such function |
| Art 25(4) (line 487; base line 1014) | adds "AI model" to the items the third party supplies ("an AI system, AI model, tools, services, components, or processes") | both versions (`Art 25(4) as enacted the item is one the paragraph names`, `Art 25(4) as amended ...`, dispatcher); the carve-out "other than general-purpose AI models" has the same words in both | The list of items is the only change, and an AI model is on the list from 27 July 2026; the paragraph that follows (the AI Office's voluntary model terms, line 489) comes after `▼B` and is unversioned |
| Art 27(4) (line 525; base line 1056) and Art 27(5) (line 526; base line 1057) | 27(4): the duty "the fundamental rights impact assessment ... shall complement that data protection impact assessment" becomes a permission "the deployer may, when conducting the fundamental rights impact assessment ..., include cross-references ... or include relevant parts thereof"; 27(5): adds the second sentence "This template shall, where relevant, give deployers the possibility to include cross-references ..." | both versions (`Art 27(4) as enacted the assessment complies with paragraph 4`, `Art 27(4) as amended the deployer may include cross-references ...`, `Art 27(5) as enacted the AI Office has developed the template`, `Art 27(5) as amended ...`, dispatchers) | A duty becoming a permission is a change of kind, so the dispatcher `Art 27(4) the assessment stands as paragraph 4 provides` answers different things before and after 27 July 2026 (fork F-27-4-meaning) |

Chapter III Sections 1 to 3 apply from 2 December 2027 (Annex III route) or 2 August 2028 (Annex I route), after the Omnibus, so a rule that goes through the gate reads the amended text on every date where the gate is open; the enacted functions are reached only by calling them directly, which the tests do.

## What the stable binary does not accept

Met while writing this part (1.6.110, checked also on 1.6.109):

- `NOT a OR b` is read as `NOT (a OR b)`: with `a` TRUE and `b` TRUE it gives FALSE, and with `a` FALSE and `b` TRUE it gives FALSE; write `(NOT a) OR b`. No error is printed: two assertions of Art 18 failed before this was seen, so it is a silent wrong answer on a bare `NOT ... OR ...` and the exit code is 0.
- `MAX` is not defined (`check/unknown-identifier`): an IF-based deadline replaces it.
- An `#ASSERT` continued on a second line is a parse error (`parse/unexpected-identifier`): every `#ASSERT` here is one line.
- A `MAY` with a `LEST` is listed in the brief as degrading on main; the only `MAY` rules of this part have a `HENCE` and no `LEST` that can fire, and their traces agree on both builds.
- Listed in the brief and not exercised: no `REFUSE`; `AFTER ... WITHIN` is rejected; `WAIT UNTIL` is spelled `WAITUNTIL` (used on 69 lines of the test files); no sets, `TYPICALLY`, section `GIVEN`, opaque `DECLARE`; `Date day month year` only, never `YMD`; an input named in a `MUST` action degrades on main.
- Worked on both builds: `add months` and `add years` from `daydate` (an anniversary that does not exist is clamped: 29 February 2028 plus 10 years is 28 February 2038, asserted in `P3-tests-art-18-19.l4`); a `MAYBE DATE` `GIVEN` input (`JUST (Date ...)` or `NOTHING`); a nested `HENCE (IF ... THEN ... ELSE FULFILLED)`; a computed `WITHIN (Day x) MINUS (Day y)` with inclusive deadlines; chained `HENCE` of a second `MUST`; `CONSIDER gate WHEN ... THEN ... OTHERWISE ...` returning `MAYBE BOOLEAN`; an hours clock (Art 26(10), 48 hours, counted from hour 0) with `WITHIN` in hours.
- A `#TRACE` outcome that differs between the builds is invisible to `check.sh` (it prints no assertion line): all 228 traces were compared by hand.

## Seats (P3)

Eight seats, each in `P3-seat-<slug>.l4` with its cases in `P3-cases-seat-<slug>.l4`; 128 questions in all and 413 cases, every question with `@export` and `@desc`.
Every question names the question its body answers, in the same direction, as "Under Article N, as <role phrase>, ...", N being the Article of the provision asked about; the role and applicability questions use N = 16, the first Article of this part's range, so no other part writes the same name.
The seats are the parties this range addresses by a duty, a power or a status: the provider, the deployer, the importer, the distributor, the authorised representative, the product manufacturer, the provider of a general-purpose AI model, and the affected person.
A seat module imports layer 1 and the keel and restates no rule; the first questions of every seat (two, and three for the gpai seat) are the applicability question (`Art 113 the provision group applies` with `Chapter III Sections 1 to 3`, `JUST TRUE` or `JUST FALSE`) and the role question or questions (the keel's `Art 3(3)`, `3(4)`, `3(5)`, `3(6)`, `3(7)`, `3(63)`, `Art 2(1)(e)`, `Art 2(1)(g)`), the other questions each call one decision function.

| seat | questions | cases | what it asks |
| --- | --- | --- | --- |
| provider | 39 | 117 | Art 16 (a) to (l), 17, 18, 19, 20, 21, 22 (1), (2), 25(2) as the initial provider, 25(4), 25(5) |
| deployer | 44 | 132 | Art 25(1), Art 26 (1) to (12), Art 27 (1) to (5) |
| importer | 12 | 42 | Art 23 (1) to (7), Art 25(1) |
| distributor | 11 | 40 | Art 24 (1) to (6), Art 25(1) |
| rep | 7 | 26 | Art 22 (3), (4) |
| manufacturer | 3 | 12 | Art 25(3) |
| gpai | 4 | 18 | Art 25(4) as the supplier of an AI model |
| person | 8 | 26 | Art 26(7), (10), (11), Art 27(1) |

Seat audit (second pass): 128 questions read, 0 retitled (direction 0, subject 0).
Each question's name and `@export` text (the same words, the `@export` ending in `?`) were read against the function its body calls: the 111 duty, power, bar and effect questions against the layer-1 function, and the 17 applicability and role questions against the keel's `Art 113`, `Art 3(N)` and `Art 2(1)` functions.
A direction mismatch would be a permission or yes ("may I", "does X apply to me", "have I met") over a function that returns the bar, the exception or the opposite, or the reverse; none was found: the bar questions ask "am I barred" or "is ... barred" of functions named "is barred" or "may not be taken", the power questions ask "may" of functions named "may", and the deeming, applicability and exemption questions ask "is ... deemed" or "does ... apply" of functions that say the same.
A subject mismatch would be "must I" over "have I", or the authority over a provider's duty; none was found: the questions about the AI Office, a Member State and a competent authority (Art 18(2), 21(3), 25(4), 26(10), 27(5)) are asked of functions whose subject is that official, and the person seat asks what the deployer did, of functions whose subject is the deployer.
The Article number of each title was also compared with the Article of its function: all 128 agree.
The seat files `P3-seat-<slug>.l4` are unchanged by the audit; five case lines (three in `P3-cases-seat-deployer.l4`, two in `P3-cases-seat-person.l4`) were restated with `-- RECONCILED 2026-11-17` because layer 1's answer for the two Article 26(10) bars changed (fork F-bars).

Every one of the 102 decision functions of layer 1 that return `MAYBE BOOLEAN` after the gate is asked from at least one seat; the helper functions, the version functions below the dispatchers and the regulative rules are not asked (the rules are read through the traces).
The shared inputs have the same name and the same `@desc` in every question: `the date asked`, `the route by which the AI system is high-risk`, `the date the AI system was placed on the market or put into service`, `the AI system has been significantly changed in its design since the date of application of Chapter III` (the four of PLAN.md section 8), and three of this part's own, which build the `Section 3 circumstances` record inside the question: `the AI system is related to products covered by the Union harmonisation legislation listed in Section B of Annex I`, `Union harmonisation legislation listed in Section A of Annex I lays down requirements or obligations providing an equivalent or higher level of protection`, `limiting the requirement or obligation does not reduce the overall level of protection provided for by this Regulation` (Art 2(2) and Art 2(13); their `@desc` say "answer no if you do not know").
Records are built in a `WHERE` from plain answers: `AI system` and `Section 3 circumstances` in every question, and the record a function expects (for example `Art 25(1) what the party has done`, `Art 27(1) the assessment`) where it has one.
The role the seat holds is a constant of its questions where a function asks it (the importer, distributor and deployer seats pass TRUE for "the party is a distributor, importer, deployer or other third-party" in `Art 25(1)`; the manufacturer seat passes TRUE for "the party is the product manufacturer"; the gpai seat passes `Supplied AI model` and TRUE for "the item is a general-purpose AI model").

**Inputs outside the PLAN's plain list** (a yes/no, a date, a number, or one of the keel's own choices): two of this part's own choices and one text input.
`Art 25(4) supplied item` is an enumeration of this part (`Supplied AI system`, `Supplied AI model`, `Supplied tool`, `Supplied service`, `Supplied component`, `Supplied process`, `Supplied something else`) asked by the provider seat; the gpai seat fixes it.
`the aspect of paragraph 1, by its letter` (Art 17(4)) is a `STRING`: the letter of the point of Article 17(1) (a to m).
`the paragraph` (Art 25(5), Art 26(3)) is a `NUMBER`.
The keel's `Place of a party` (Art 22(1) and the role questions of the importer and authorised representative, and of the person) and `Route to high-risk` are keel choices.
A different design would turn the letter into thirteen yes/no questions; the text names the aspects by letter and the function's `NOTHING` for a letter that is not on the list is part of the answer.

**Mirror cases** (`-- MIRROR` in the case files; the same facts asked from two or more seats, the answers agree):
M1 Art 26(11) informing the natural persons (deployer and person); M2 Art 26(10) decision based solely on the output (deployer and person); M3 Art 26(7) workers' representatives (deployer and person); M4 Art 27(1) whether the assessment is required (deployer and person); M5 Art 26(10) untargeted use (deployer and person); M6 Art 25(4) written agreement for a supplied AI model (provider and gpai); M7 Art 25(1) a party that is not the provider (importer, distributor and deployer); M8 Art 25(1) and Art 25(2): a party becoming the provider and the initial provider ceasing to be one on the same circumstances (deployer and provider); M9 the CE marking, affixed by the provider (Art 16(h)) and verified by the importer (Art 23(1)) and the distributor (Art 24(1)): present gives `JUST TRUE` and absent `JUST FALSE` from each; M10 the tasks of the mandate, enabled by the provider (Art 22(2)) and performed by the authorised representative (Art 22(3)); M11 a party other than the provider puts its name or trademark on the system, or has none of the circumstances: the importer (Art 25(1)) and the product manufacturer (Art 25(3)) answer alike (`JUST TRUE`, or `NOTHING` by F-25-1-closed).
A fact only one seat can state (the deployer knows what it did; the person asks what the deployer did) is mirrored only where both can state it.
The answers of M8 agree on the positive case only: where the circumstances do not occur, `Art 25(1)` answers `NOTHING` (F-25-1-closed) and `Art 25(2)` answers `JUST FALSE` (reading (a), rule (b)), so a negative M8 case would disagree; this is the one asymmetry between two functions of the same part and it follows from the answers taken, not from a choice of questions.

**The notified body has no seat.**
The text of lines 374 to 526 names the notified body on seven lines (403, 417, 418, 429, 441, 446 and 457) and on none of them imposes a duty on it or grants it a power: it is the recipient of information (Art 20(2), Art 22(4)), the issuer of certificates and decisions that others keep or verify (Art 18(1)(c) and (d), Art 22(3)(b), Art 23(5)), and one party the provider's quality management system handles communication with (Art 17(1)(j)).
The notified body's own obligations are in Section 4 of Chapter III (Articles 28 to 39, from line 528), outside this range.
The questions this range raises about a notified body are asked from the seat that holds the duty: the provider (Art 20(2) informing the notified body), the authorised representative (Art 22(4)) and the importer (Art 23(5) keeping the certificate).
The AI Office, a Member State and a competent authority are officials and not seats either; what the text requires of them (Art 18(2), Art 21(3), Art 25(4) second subparagraph, Art 26(10) last subparagraph, Art 27(5)) is asked from the seat that relies on it.

**What other parts must ask of Article 25.**
No function of this part calls another part, and a seat answers a question, not a chain.
A party that is a distributor, an importer, a deployer or another third party is a provider of the high-risk AI system for the Regulation's obligations only if `Art 25(1)` (or, for a product manufacturer, `Art 25(3)`) answers `JUST TRUE`; a part that addresses "the provider" (the obligations of Articles 43 to 49, 72, 73 and the rest) must ask a non-provider caller the Article 25 question first and then ask its provider questions from the provider seat.
An answer of `NOTHING` from `Art 25(1)` is not "not a provider" (F-25-1-closed): the list of circumstances is not closed, so a caller whose facts fall outside (a) to (c) is outside this part's answer and may be a provider by another route (the keel's `Art 3(3)`).
When `Art 25(2)` answers `JUST TRUE`, the initial provider is no longer a provider of that specific AI system and stops being the seat for it; the new provider takes the seat.
Chapter III Sections 1 to 3 apply only from 2 December 2027, after the Omnibus, so every date on which a seat question can answer `JUST TRUE` or `JUST FALSE` reads the amended text (Art 25(4) lists AI models among the supplied items); the as-enacted list is reached only through the direct as-enacted functions.

## Files

Layer 1: `P3-section-3.l4`, `P3-art-16.l4` to `P3-art-27.l4`; tests: `P3-tests-section-3.l4` (27 assertions), `P3-tests-art-16.l4` (49, 24 traces), `P3-tests-art-17.l4` (59, 8), `P3-tests-art-18-19.l4` (49, 18), `P3-tests-art-20-21.l4` (44, 24), `P3-tests-art-22.l4` (42, 17), `P3-tests-art-23.l4` (54, 25), `P3-tests-art-24.l4` (45, 19), `P3-tests-art-25.l4` (99, 16), `P3-tests-art-26.l4` (122, 55), `P3-tests-art-27.l4` (62, 22).
Layer 2: `P3-seat-person.l4`, `P3-seat-provider.l4`, `P3-seat-deployer.l4`, `P3-seat-importer.l4`, `P3-seat-distributor.l4`, `P3-seat-rep.l4`, `P3-seat-manufacturer.l4`, `P3-seat-gpai.l4` and the matching `P3-cases-seat-<slug>.l4`.
`PROGRESS.md` is a working log, not a claim about the text.
