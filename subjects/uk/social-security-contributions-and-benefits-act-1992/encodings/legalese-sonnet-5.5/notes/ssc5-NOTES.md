# NOTES -- part ssc5: Social Security Contributions and Benefits Act 1992, lines 2444-3094 (Parts VI to X, ss 112-150)

Source: `ukpga-1992-4.txt`, a plain-text rendering made by a converter script from legislation.gov.uk (point in time 2026-07-08, see `inputs/SOURCES.md`).
It is not the official text, and nothing here is "verified against the official text".
Binary: the stable `l4` 1.6.98; every module also runs on the main build 1.6.108 with the same four counts (`check.sh`, below).
Quotations and `@ref` locators were checked mechanically against the text: `srcrefs.py check --refs` and `--strict` both report 0 problems for every `ssc5-*.l4` file.

## Seat

The individual who works, is self-employed, or claims a benefit, statutory pay or Child Benefit in Great Britain.
Layer 2 is `ssc5-seat.l4` (51 questions, each `@export` with `@desc`, named "Under section N, ...", grouped under five `§` headings in the text's order) and `ssc5-cases-seat.l4` (146 cases).
Provisions that address only an official (the Secretary of State's duties to display a scheme, the appropriate officer's duty to have regard, powers to make regulations) are encoded in layer 1 for what they decide, and in layer 2 only for what they mean to the person: whether they may inspect a scheme, whether the matter must be considered in deciding their award.
There is no seat for an official.
Where a group of questions arises only in a situation the person may not be in (Crown or forces service, an accident outside Great Britain, the social fund, health in pregnancy grant, a child's death, the Christmas bonus), the comment under the `§` heading says so, so that a form can ask first.


## Files

| file | holds |
|---|---|
| `ssc5-logic.l4`, `ssc5-tests-logic.l4` | Kleene three-valued helpers over `MAYBE BOOLEAN` (`s 124(1) both hold`, `either holds`, `does not hold`, `is known to hold`, `holds or else nothing`, `all of these hold`) and the type `s 122(1) A definition` used by every definition record; 32 assertions |
| `ssc5-part6.l4`, `ssc5-tests-part6.l4` | Part VI, ss 112-122: employment protection entitlements, disqualification, Crown and forces service, the three seam functions for s 94(5) (S20), continental shelf operations (S25), "deferred" (S37, asks), tax year, tax week, week, qualifying earnings factor, and 62 records of how s 122(1) defines a term |
| `ssc5-part7.l4`, `ssc5-tests-part7.l4` | Part VII, ss 123-137: income-related benefits, income support (s 124), trade disputes (s 126), return to work (s 127), housing benefit (s 130), exclusions, applicable amount, income and capital, "couple" (S12) and the other s 137(1) terms |
| `ssc5-part8.l4`, `ssc5-tests-part8.l4` | Part VIII, ss 138-140 (the social fund), Part 8A, ss 140A-140B (health in pregnancy grant) |
| `ssc5-part9.l4`, `ssc5-tests-part9.l4` | Part IX, ss 141-147 (child benefit), including S18 and S33 |
| `ssc5-part10.l4`, `ssc5-tests-part10.l4` | Part X, ss 148-150 (Christmas bonus for pensioners) |
| `ssc5-seat.l4`, `ssc5-cases-seat.l4` | layer 2 |
| `NOTES.md`, `PROGRESS.md` | this file; the working log |

`NEEDS-CORE.md` is not written: no type or constructor was missing from the core that I could not do without.
Besides the enumerations that belong to one rule alone (kinds, matters and duties, each named by its section), five types stand where the core might have supplied one, all under the `ssc5` prefix: the four `Party` types `s 123 Party`, `s 127(c) Party`, `s 139 Party` and `s 140 Party` (a regulative rule, or a list of the persons a sum is recoverable from, needs a type of its own, and the core's `Authority` has `a social fund officer` but not "an authority granting housing benefit" or "an appropriate officer ... exercising functions of the Secretary of State"), and `s 138(4A) Reference` (the Scottish Ministers are not in the core's `Authority`; the substitution in s 138(4A) is encoded as the words it substitutes, in a `MAYBE STRING`).
If the lead wants the Scottish Ministers in the core, `Authority` is where they would go.


## Decision procedure (ssc5; applied uniformly, each rule licensed by the text named)

- P1. A grant or status that the text states with a trailing "if" (`is entitled ... if`, `shall be treated ... if`, `shall also be entitled ... if`): all conditions hold gives `JUST TRUE`; a failed "if" gives `JUST FALSE` (reading (a), marginal; listed below).
  It does not extend to a computation rule such as s 143(3) (a day of absence "shall be disregarded ... if it is due solely to"), which answers `NOTHING` when the "if" fails.
- P2. A relative-clause grant ("A person who ... shall be entitled", "A woman who satisfies ... is entitled"): the conditions hold gives `JUST TRUE`; otherwise `NOTHING` (reading (b), marginal).
- P3. A flat negative or an "unless" ("No person shall be entitled", "A woman is not entitled ... unless", "shall not be payable"): the triggering case gives `JUST FALSE`.
  What a function answers when the bar does not bite depends on what its name says.
  A function named for the bar's own condition (`s 134(1) ... barred ... by capital`, `s 134(2) ... excluded by another member's entitlement`, `s 140A(2) ... as far as subsection (2) goes`, `s 146(1) ... as the subsection requires`) tests that condition and answers both ways: `JUST TRUE` when the bar bites (or, for "as far as ... goes" and "as the subsection requires", when the "unless" is met), `JUST FALSE` otherwise.
  A function named for an effect that other provisions can also bring about (`s 113(1) the person is disqualified`, `s 134(4) the income-related benefit is not payable`, any "is entitled", "may ..." or "is payable") answers `JUST TRUE` where the text's own words say so and `NOTHING` where they do not.
  An "unless" or "except" that is triggered against a requirement or a deeming (s 143(2), s 139(5), the "unless the context otherwise requires" of ss 122(1) and 137(1)) is the text's no and gives `JUST FALSE`.
  A grant or status limited to a stated period or to "while" a state lasts (ss 113(1), 116(1), 127(b), 145A(1)) is not a flat negative: outside its limit it gives `NOTHING` (reading (b), listed below).
- P4. "means": the case matches gives `TRUE`, no match gives `JUST FALSE`. "is", "are", "includes", "has the meaning given by": a match gives `TRUE`, anything else `NOTHING`. "That is to say" (s 139(1)) and "shall be taken to consist of" (s 116(3)) are read as "means" (marginal, listed below).
- P5. A power to make regulations, orders, directions or rules is inert (reason 2), except where the section states its own limit or default (`s 122(6B)`, `s 140(4ZA)`, `s 148(3)(b)`), or another part's seam needs a function (ss 117, 119, 120).
- P6. A conditional that opens a provision ("Where a person has had a child living with him ...", "If a child dies ...", "Where regulations are made by the Scottish Ministers") only sets the scene: where the scene is absent the provision is silent and the answer is `NOTHING`.
- P7. Figures that regulations prescribe (rates, ages, amounts, periods, circumstances) are inputs. Figures the Act states in its own words are written in the code with the line quoted: £53.00 (s 126(7)), the multiple of 5p (s 126(4)), the multiple of 50p and the remainder of 25p (s 126(8)(b)), £10 (s 148(3)(b)), 16 (s 142(1), through the keel's s 173), more than 56 days in the 16 weeks (s 143(2)), 1 January 2011 and the 25th week (s 140A(2)), the 15 days (s 127(b)); the 6th week before and the 7th week after (s 126(2)) are written as 42 days before and 55 days after the start of a Sunday week, which is arithmetic on the text's figures and is commented where it is done.
- P8. A judgment the text hands to someone else becomes a plain input (the Secretary of State "accepts" a payment as analogous; the context "otherwise requires"; the amount "appears to the Secretary of State").


## Coverage (ssc5)

A unit is a non-blank line of `ukpga-1992-4.txt` between lines 2444 and 3094 inclusive: the converter puts one provision, one limb or one heading on a line.
Every unit has exactly one row below and exactly one disposition:

- **encoded**: the line is quoted in a layer-1 module by a `-- src:` comment, under a rule named in the last column; every such name is exercised by a test or a case.
- **fork**: encoded as above, under a reading recorded in the Fork register (the fork id is in the disposition).
- **inert 1**: not operative: a heading, a section number and title, or a lead-in whose words the rules below it already carry.
- **inert 2**: machinery: a power to make regulations, orders or rules, or a duty about who does so, that no case in this range turns on (rule P5).
- **repealed or blank**: a line of dots, or the title of a section whose whole body is a line of dots.

Rows in the table: before this run 0 (no table existed); after, 651, equal to the 651 units counted.
The table and the counts below are generated by `work/mkcov.py` from the `-- src:` quotations in the deposit and a list of manual dispositions; the script exits non-zero on any unit without a disposition, any name that is not defined, and any encoded name that no test exercises, and it exited 0 for this table.

Audit counts:

- Units (one per non-blank line of lines 2444-3094): 651; non-blank lines 651; lines that start no unit 0.
- encoded: 385
- fork: 21
- inert 1: 61
- inert 2: 126
- repealed or blank: 58
- Total dispositions: 651 (must equal units: yes)
- Encoded and fork rows whose L4 names are all exercised by a test or case: all; untested: []
- Fork rows by fork: fork F1 4, fork F2 3, fork F3 4, fork F4 1, fork F5 1, fork F6 2, fork F7 4, fork F8 2

| provision | lines | disposition | L4 name, or what the text shows |
|---|---|---|---|
| Part VI — Miscellaneous Provisions relating to Parts I to V | 2444 | inert 1 | a heading |
| Earnings | 2445 | inert 1 | a heading |
| s 112 | 2446 | inert 1 | section number and title |
| s 112(1) | 2447 | inert 2 | s 112(1): the Treasury's power to make regulations deeming employment protection entitlements earnings |
| s 112(1)(a) | 2448 | inert 2 | s 112(1): the Treasury's power to make regulations deeming employment protection entitlements earnings |
| s 112(1)(b) | 2449 | inert 2 | s 112(1): the Treasury's power to make regulations deeming employment protection entitlements earnings |
| s 112(2) | 2450 | encoded | `s 112(2) the sum is an employment protection entitlement` |
| s 112(2)(a) | 2451 | encoded | `s 112(2) the sum is an employment protection entitlement` |
| s 112(2)(b) | 2452 | encoded | `s 112(2) the sum is an employment protection entitlement` |
| s 112(2A) | 2453 | inert 2 | s 112(2A): who makes the regulations under subsection (2) |
| s 112(3) | 2454 | encoded | `s 112(3) Sum` |
| s 112(3)(a) | 2455 | encoded | `s 112(3) Sum` |
| s 112(3)(b) | 2456 | encoded | `s 112(3) Sum` |
| s 112(3)(c) | 2457 | encoded | `s 112(3) Sum` |
| Disqualification and suspension | 2458 | inert 1 | a heading |
| s 113 | 2459 | inert 1 | section number and title |
| s 113(1) | 2460 | encoded | `s 113(1) an increase of the benefit is payable in respect of the person as the beneficiary's wife, husband or civil partner for the period`; `s 113(1) the person is disqualified for receiving the benefit for the period` |
| s 113(1)(a) | 2461 | encoded | `s 113(1) an increase of the benefit is payable in respect of the person as the beneficiary's wife, husband or civil partner for the period`; `s 113(1) the person is disqualified for receiving the benefit for the period` |
| s 113(1)(b) | 2462 | encoded | `s 113(1) an increase of the benefit is payable in respect of the person as the beneficiary's wife, husband or civil partner for the period`; `s 113(1) the person is disqualified for receiving the benefit for the period` |
| s 113(2) | 2463 | inert 2 | s 113(2), (3): powers to make regulations (suspension during in-patient treatment; treating a person as entitled) |
| s 113(3) | 2464 | inert 2 | s 113(2), (3): powers to make regulations (suspension during in-patient treatment; treating a person as entitled) |
| Persons maintaining dependants etc. | 2465 | inert 1 | a heading |
| s 114 | 2466 | inert 1 | section number and title |
| s 114(1) | 2467 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(1)(a) | 2468 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(1)(b) | 2469 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(2) | 2470 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(2)(a) | 2471 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(2)(b) | 2472 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(2)(b) (unlabelled limb) | 2473 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(3) | 2474 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(3)(a) | 2475 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(3)(b) | 2476 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(3)(b) (unlabelled limb) | 2477 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| s 114(4) | 2478 | inert 2 | s 114: powers to make regulations on maintaining dependants and contributions, and the list of provisions they affect |
| Special cases | 2479 | inert 1 | a heading |
| s 115 | 2480 | inert 1 | section number and title |
| s 115(1) | 2481 | encoded | `s 115(1) Parts I to V and this Part apply to the person as if employed by a private person` |
| s 115(2) | 2482 | encoded | `s 115(1) Parts I to V and this Part apply to the person as if employed by a private person` |
| s 115(3) | 2483 | encoded | `s 115(3) the employment is employed earner's employment for the purposes of Part V` |
| s 115(4) | 2484 | inert 2 | s 115(4): excludes section 111 from the references to Parts I to V; section 111 is blank in this text, so the saving affects no one now |
| s 116 | 2485 | inert 1 | section number and title |
| s 116(1) | 2486 | encoded | `s 116(1) the person is treated as an employed earner in respect of membership of the forces` |
| s 116(1)(a) | 2487 | encoded | `s 116(1) the person is treated as an employed earner in respect of membership of the forces` |
| s 116(1)(b) | 2488 | encoded | `s 116(1) the person is treated as an employed earner in respect of membership of the forces` |
| s 116(2) | 2489 | inert 2 | s 116(2): power to make regulations modifying Parts I to V and this Part for the forces |
| s 116(2)(a) | 2490 | inert 2 | s 116(2): power to make regulations modifying Parts I to V and this Part for the forces |
| s 116(2)(b) | 2491 | inert 2 | s 116(2): power to make regulations modifying Parts I to V and this Part for the forces |
| s 116(3) | 2492 | encoded | `s 116(3) the establishment or organisation is part of Her Majesty's forces` |
| s 117 | 2493 | inert 1 | section number and title |
| s 117(1) | 2494 | encoded | `s 117 the accident falls within the exception` |
| s 117(2) | 2495 | inert 2 | s 117(2): what regulations under s 117(1) may in particular provide |
| s 117(2)(a) | 2496 | inert 2 | s 117(2): what regulations under s 117(1) may in particular provide |
| s 117(2)(b) | 2497 | inert 2 | s 117(2): what regulations under s 117(1) may in particular provide |
| s 117(2)(c) | 2498 | inert 2 | s 117(2): what regulations under s 117(1) may in particular provide |
| s 117(2)(d) | 2499 | inert 2 | s 117(2): what regulations under s 117(1) may in particular provide |
| s 117(2)(e) | 2500 | inert 2 | s 117(2): what regulations under s 117(1) may in particular provide |
| s 118 | 2501 | inert 1 | section number and title |
| s 118 (unlabelled limb) | 2502 | inert 2 | s 118: power to make regulations modifying Parts I, II, III and IV for women who are or have been married |
| s 118(a) | 2503 | inert 2 | s 118: power to make regulations modifying Parts I, II, III and IV for women who are or have been married |
| s 118(b) | 2504 | inert 2 | s 118: power to make regulations modifying Parts I, II, III and IV for women who are or have been married |
| s 118(c) | 2505 | inert 2 | s 118: power to make regulations modifying Parts I, II, III and IV for women who are or have been married |
| s 118(c) (unlabelled limb) | 2506 | inert 2 | s 118: power to make regulations modifying Parts I, II, III and IV for women who are or have been married |
| s 119 | 2507 | inert 1 | section number and title |
| s 119 (unlabelled limb) | 2508 | encoded | `s 119 the accident falls within the exception` |
| s 120 | 2509 | inert 1 | section number and title |
| s 120(1) | 2510 | encoded | `s 120 the accident falls within the exception` |
| s 120(2) | 2511 | encoded | `s 120(2) the employment is in connection with continental shelf operations` |
| s 120(3) | 2512 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(4) | 2513 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(4)(a) | 2514 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(4)(b) | 2515 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(5) | 2516 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(5)(a) | 2517 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(5)(b) | 2518 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(5)(c) | 2519 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(5)(d) | 2520 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 120(5)(e) | 2521 | inert 2 | s 120(3) to (5): regulations on continental shelf workers and certificates of liability met by another person |
| s 121 | 2522 | inert 1 | section number and title |
| s 121(1) | 2523 | inert 2 | s 121: power to make regulations on annulled marriages and polygamous marriages |
| s 121(1)(a) | 2524 | inert 2 | s 121: power to make regulations on annulled marriages and polygamous marriages |
| s 121(1)(aa) | 2525 | inert 2 | s 121: power to make regulations on annulled marriages and polygamous marriages |
| s 121(1)(b) | 2526 | inert 2 | s 121: power to make regulations on annulled marriages and polygamous marriages |
| s 121(2) | 2527 | inert 2 | s 121: power to make regulations on annulled marriages and polygamous marriages |
| s 121(2)(a) | 2528 | inert 2 | s 121: power to make regulations on annulled marriages and polygamous marriages |
| s 121(2)(b) | 2529 | inert 2 | s 121: power to make regulations on annulled marriages and polygamous marriages |
| Interpretation | 2530 | inert 1 | a heading |
| s 122 | 2531 | inert 1 | section number and title |
| s 122(1) | 2532 | encoded | `s 122(1) the defined meaning applies` |
| s 122(1) “additional Class 4 percentage” | 2533 | encoded | `s 122(1) additional Class 4 percentage` |
| s 122(1) “additional primary percentage” | 2534 | encoded | `s 122(1) additional primary percentage` |
| s 122(1) “adult disability payment” | 2535 | encoded | `s 122(1) adult disability payment` |
| s 122(1) “age-related secondary percentage” | 2536 | encoded | `s 122(1) age-related secondary percentage` |
| s 122(1) “Bank of England base rate” | 2537 | encoded | `s 122(1) Bank of England base rate` |
| s 122(1) “Bank of England base rate” (unlabelled limb) | 2538 | encoded | `s 122(1) Bank of England base rate` |
| s 122(1) “Bank of England base rate” (unlabelled limb) | 2539 | encoded | `s 122(1) Bank of England base rate` |
| s 122(1) “beneficiary” | 2540 | encoded | `s 122(1) beneficiary` |
| s 122(1) “benefit” | 2541 | encoded | `s 122(1) benefit` |
| s 122(1) “benefit” (unlabelled limb) | 2542 | encoded | `s 122(1) benefit` |
| s 122(1) “benefit” (unlabelled limb) | 2543 | encoded | `s 122(1) benefit` |
| s 122(1) “benefit” (unlabelled limb) | 2544 | encoded | `s 122(1) benefit` |
| s 122(1) “benefit” (unlabelled limb) | 2545 | encoded | `s 122(1) benefit` |
| s 122(1) “benefit” (unlabelled limb) | 2546 | encoded | `s 122(1) benefit` |
| s 122(1) “benefit” (unlabelled limb) | 2547 | encoded | `s 122(1) benefit` |
| s 122(1) “the benefits code” | 2548 | encoded | `s 122(1) the benefits code` |
| s 122(1) “child” | 2549 | encoded | `s 122(1) child` |
| s 122(1) “child disability payment” | 2550 | encoded | `s 122(1) child disability payment` |
| s 122(1) “claim” | 2551 | encoded | `s 122(1) claim` |
| s 122(1) “claimant” | 2552 | encoded | `s 122(1) claimant, other than for industrial injuries benefit` |
| s 122(1) “claimant” | 2553 | encoded | `s 122(1) claimant, for industrial injuries benefit` |
| s 122(1) “contract of service” | 2554 | encoded | `s 122(1) contract of service` |
| s 122(1) “contribution-based jobseeker’s allowance” | 2555 | encoded | `s 122(1) contribution-based jobseeker's allowance` |
| s 122(1) “current” | 2556 | encoded | `s 122(1) current` |
| s 122(1) “day of interruption of employment” | 2557 | encoded | `s 122(1) day of interruption of employment` |
| s 122(1) “deferred” | 2558 | encoded | `s 122(1) period of deferment`; `s 122(1) the pension is deferred` |
| s 122(1) “deferred” (unlabelled limb) | 2559 | encoded | `s 122(1) period of deferment`; `s 122(1) the pension is deferred` |
| s 122(1) “deferred” (unlabelled limb) | 2560 | encoded | `s 122(1) period of deferment`; `s 122(1) the pension is deferred` |
| s 122(1) “earner” | 2561 | encoded | `s 122(1) earner and earnings` |
| s 122(1) “employed earner” | 2562 | encoded | `s 122(1) employed earner` |
| s 122(1) “employment” | 2563 | encoded | `s 122(1) employment` |
| s 122(1) “the employment income Parts of ITEPA 2003” | 2564 | encoded | `s 122(1) the employment income Parts of ITEPA 2003` |
| s 122(1) “entitled” | 2565 | encoded | `s 122(1) entitled` |
| s 122(1) “entitled” (unlabelled limb) | 2566 | encoded | `s 122(1) entitled` |
| s 122(1) “entitled” (unlabelled limb) | 2567 | encoded | `s 122(1) entitled` |
| s 122(1) “entitled” (unlabelled limb) | 2568 | encoded | `s 122(1) entitled` |
| s 122(1) “entitled” [repealed or blank line] | 2569 | repealed or blank | a line of dots in the text: repealed or blank |
| s 122(1) “first appointed year” | 2570 | encoded | `s 122(1) first appointed year and second appointed year` |
| s 122(1) “the flat rate introduction year” | 2571 | encoded | `s 122(1) the flat rate introduction year` |
| s 122(1) “general earnings” | 2572 | encoded | `s 122(1) general earnings` |
| s 122(1) “industrial injuries benefit” | 2573 | encoded | `s 122(1) industrial injuries benefit` |
| s 122(1) “industrial injuries benefit” [repealed or blank line] | 2574 | repealed or blank | a line of dots in the text: repealed or blank |
| s 122(1) “the Inland Revenue” | 2575 | encoded | `s 122(1) the Inland Revenue` |
| s 122(1) “ITEPA 2003” | 2576 | encoded | `s 122(1) ITEPA 2003` |
| s 122(1) “late husband” | 2577 | encoded | `s 122(1) late husband` |
| s 122(1) “long-term benefit” | 2578 | encoded | `s 122(1) long-term benefit` |
| s 122(1) “loss of physical faculty” | 2579 | encoded | `s 122(1) loss of physical faculty` |
| s 122(1) “lower earnings limit” | 2580 | encoded | `s 122(1) lower earnings limit, upper earnings limit, primary threshold and secondary threshold` |
| s 122(1) “lower-paid employment as a minister of religion” | 2581 | encoded | `s 122(1) lower-paid employment as a minister of religion` |
| s 122(1) “lower-paid employment as a minister of religion” [repealed or blank line] | 2582 | repealed or blank | a line of dots in the text: repealed or blank |
| s 122(1) “main Class 4 percentage” | 2583 | encoded | `s 122(1) main Class 4 percentage` |
| s 122(1) “main primary percentage” | 2584 | encoded | `s 122(1) main primary percentage` |
| s 122(1) “medical examination” | 2585 | encoded | `s 122(1) medical examination` |
| s 122(1) “medical treatment” | 2586 | encoded | `s 122(1) medical treatment` |
| s 122(1) “the Northern Ireland Department” | 2587 | encoded | `s 122(1) the Northern Ireland Department` |
| s 122(1) “Old Cases payments” | 2588 | encoded | `s 122(1) Old Cases payments` |
| s 122(1) “PAYE settlement agreement” | 2589 | encoded | `s 122(1) PAYE settlement agreement` |
| s 122(1) “payments by way of occupational or personal pension” | 2590 | encoded | `s 122(1) payments by way of occupational or personal pension` |
| s 122(1) “payments by way of occupational or personal pension” (unlabelled limb) | 2591 | encoded | `s 122(1) payments by way of occupational or personal pension` |
| s 122(1) “payments by way of occupational or personal pension” (unlabelled limb) | 2592 | encoded | `s 122(1) payments by way of occupational or personal pension` |
| s 122(1) “payments by way of occupational or personal pension” (unlabelled limb) | 2593 | encoded | `s 122(1) payments by way of occupational or personal pension` |
| s 122(1) “payments by way of occupational or personal pension” (unlabelled limb) | 2594 | encoded | `s 122(1) payments by way of occupational or personal pension` |
| s 122(1) “payments by way of occupational or personal pension” (unlabelled limb) | 2595 | encoded | `s 122(1) payments by way of occupational or personal pension` |
| s 122(1) “pension age disability payment” | 2596 | encoded | `s 122(1) pension age disability payment` |
| s 122(1) “pensionable age” | 2597 | encoded | `s 122(1) pensionable age` |
| s 122(1) “pneumoconiosis” | 2598 | encoded | `s 122(1) pneumoconiosis` |
| s 122(1) “PPF periodic payments” | 2599 | encoded | `s 122(1) PPF periodic payments` |
| s 122(1) “PPF periodic payments” (unlabelled limb) | 2600 | encoded | `s 122(1) PPF periodic payments` |
| s 122(1) “PPF periodic payments” (unlabelled limb) | 2601 | encoded | `s 122(1) PPF periodic payments` |
| s 122(1) “prescribe” | 2602 | encoded | `s 122(1) prescribe` |
| s 122(1) “prescribe” [repealed or blank line] | 2603 | repealed or blank | a line of dots in the text: repealed or blank |
| s 122(1) “qualifying earnings factor” | 2604 | encoded | `s 122(1) the qualifying earnings factor in pounds` |
| s 122(1) “qualifying young person” | 2605 | encoded | `s 122(1) qualifying young person` |
| s 122(1) “Regulation (EC) No 1408/71” | 2606 | encoded | `s 122(1) Regulation (EC) No 1408/71` |
| s 122(1) “Regulation (EC) No 883/2004” | 2607 | encoded | `s 122(1) Regulation (EC) No 883/2004` |
| s 122(1) “relative” | 2608 | encoded | `s 122(1) relative` |
| s 122(1) “relevant accident” | 2609 | encoded | `s 122(1) relevant accident` |
| s 122(1) “relevant injury” | 2610 | encoded | `s 122(1) relevant injury` |
| s 122(1) “relevant loss of faculty” | 2611 | encoded | `s 122(1) relevant loss of faculty` |
| s 122(1) “relevant loss of faculty” [repealed or blank line] | 2612 | repealed or blank | a line of dots in the text: repealed or blank |
| s 122(1) “relevant loss of faculty” (unlabelled limb) | 2613 | encoded | `s 122(1) relevant loss of faculty` |
| s 122(1) “Scottish adult disability living allowance” | 2614 | encoded | `s 122(1) Scottish adult disability living allowance` |
| s 122(1) “secondary percentage” | 2615 | encoded | `s 122(1) secondary percentage` |
| s 122(1) “self-employed earner” | 2616 | encoded | `s 122(1) self-employed earner` |
| s 122(1) “short-term benefit” | 2617 | encoded | `s 122(1) short-term benefit` |
| s 122(1) “tax week” | 2618 | encoded | `s 122(1) the tax week containing the date` |
| s 122(1) “tax year” | 2619 | encoded | `s 122(1) the tax year containing the date`; `s 122(1) the tax year named by a pair of successive years` |
| s 122(1) “trade or business” | 2620 | encoded | `s 122(1) trade or business` |
| s 122(1) “trade union” | 2621 | encoded | `s 122(1) trade union` |
| s 122(1) “unit of additional pension” | 2622 | encoded | `s 122(1) unit of additional pension` |
| s 122(1) “the upper accrual point” | 2623 | encoded | s 122(1) "the upper accrual point" is 770: the core's constant `the upper accrual point` (ssc-core.l4), not defined again |
| s 122(1) “week” | 2624 | encoded | `s 122(1) the week containing the date` |
| s 122(1) “working life” | 2625 | encoded | `s 122(1) working life` |
| s 122(1A) | 2626 | repealed or blank | a line of dots in the text: repealed or blank |
| s 122(2) | 2627 | inert 2 | s 122(2), (3): powers to make regulations (meaning of employment; residing together) |
| s 122(3) | 2628 | inert 2 | s 122(2), (3): powers to make regulations (meaning of employment; residing together) |
| s 122(4) | 2629 | encoded | `s 122(4) the person is treated as entitled to the child benefit to which the spouse is entitled` |
| s 122(5) | 2630 | inert 2 | s 122(5): power to make regulations treating a person as entitled to child benefit |
| s 122(6) | 2631 | encoded | `s 122(6) the person is permanently incapable of self-support` |
| s 122(6A) | 2632 | inert 2 | s 122(6A): power to prescribe an equivalent of the upper accrual point (its limit in (6B) is encoded) |
| s 122(6B) | 2633 | encoded | `s 122(6B) the amount prescribed is one the power includes` |
| s 122(7) | 2634 | repealed or blank | a line of dots in the text: repealed or blank |
| s 122(8) | 2635 | repealed or blank | a line of dots in the text: repealed or blank |
| Part VII — Income-Related Benefits | 2636 | inert 1 | a heading |
| General | 2637 | inert 1 | a heading |
| s 123 | 2638 | inert 1 | section number and title |
| s 123(1) | 2639 | encoded | `s 123(1) the benefit is an income-related benefit` |
| s 123(1)(a) | 2640 | encoded | `s 123(1) the benefit is an income-related benefit` |
| s 123(1)(b) | 2641 | encoded | `s 123(1) the benefit is an income-related benefit` |
| s 123(1)(c) | 2642 | encoded | `s 123(1) the benefit is an income-related benefit` |
| s 123(1)(d) | 2643 | encoded | `s 123(1) the benefit is an income-related benefit` |
| s 123(1)(e) | 2644 | encoded | `s 123(1) the benefit is an income-related benefit` |
| s 123(2) | 2645 | encoded | `s 123(2) the Secretary of State's duty to make copies of the schemes available`; `s 123(2) the person may inspect a copy of the scheme without payment` |
| s 123(3) | 2646 | encoded | `s 123(3)(a) the authority must take steps so that the person becomes aware`; `s 123(3)(a) the housing benefit authority's duty to make persons aware`; `s 123(3)(b) the housing benefit authority's duty to make copies of its scheme available`; `s 123(3)(b) the person may inspect a copy of the housing benefit scheme without payment` |
| s 123(3)(a) | 2647 | encoded | `s 123(3)(a) the authority must take steps so that the person becomes aware`; `s 123(3)(a) the housing benefit authority's duty to make persons aware`; `s 123(3)(b) the housing benefit authority's duty to make copies of its scheme available`; `s 123(3)(b) the person may inspect a copy of the housing benefit scheme without payment` |
| s 123(3)(b) | 2648 | encoded | `s 123(3)(b) the housing benefit authority's duty to make copies of its scheme available`; `s 123(3)(b) the person may inspect a copy of the housing benefit scheme without payment` |
| s 123(4) | 2649 | encoded | `s 123(4)(a) the authority must take steps so that the person becomes aware`; `s 123(4)(a) the billing authority's duty to make persons aware`; `s 123(4)(b) the billing authority's duty to make copies of its scheme available`; `s 123(4)(b) the person may inspect a copy of the council tax benefit scheme without payment` |
| s 123(4)(a) | 2650 | encoded | `s 123(4)(a) the authority must take steps so that the person becomes aware`; `s 123(4)(a) the billing authority's duty to make persons aware`; `s 123(4)(b) the billing authority's duty to make copies of its scheme available`; `s 123(4)(b) the person may inspect a copy of the council tax benefit scheme without payment` |
| s 123(4)(b) | 2651 | encoded | `s 123(4)(b) the billing authority's duty to make copies of its scheme available`; `s 123(4)(b) the person may inspect a copy of the council tax benefit scheme without payment` |
| Income support | 2652 | inert 1 | a heading |
| s 124 | 2653 | inert 1 | section number and title |
| s 124(1) | 2654 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1)(a) | 2655 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1)(aa) | 2656 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1)(b) | 2657 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1)(c) | 2658 | encoded | `s 124(1) the person is entitled to income support`; `s 124(1)(c) the person satisfies paragraph (c)` |
| s 124(1)(d) | 2659 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1)(e) | 2660 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1)(f) | 2661 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1)(g) | 2662 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1)(h) | 2663 | encoded | `s 124(1) the person is entitled to income support` |
| s 124(1A) | 2664 | encoded | `s 124(1A) the person falls within a category prescribed under subsection (1)(e)` |
| s 124(1A)(a) | 2665 | encoded | `s 124(1A) the person falls within a category prescribed under subsection (1)(e)` |
| s 124(1A)(b) | 2666 | encoded | `s 124(1A) the person falls within a category prescribed under subsection (1)(e)` |
| s 124(1A)(b) (unlabelled limb) | 2667 | encoded | `s 124(1A) the person falls within a category prescribed under subsection (1)(e)` |
| s 124(1B) | 2668 | encoded | `s 124(1A) the person falls within a category prescribed under subsection (1)(e)` |
| s 124(2) | 2669 | repealed or blank | a line of dots in the text: repealed or blank |
| s 124(3) | 2670 | repealed or blank | a line of dots in the text: repealed or blank |
| s 124(4) | 2671 | encoded | `s 124(4) the amount of income support in pounds a week` |
| s 124(4)(a) | 2672 | encoded | `s 124(4) the amount of income support in pounds a week` |
| s 124(4)(b) | 2673 | encoded | `s 124(4) the amount of income support in pounds a week` |
| s 124(5) | 2674 | encoded | `s 124(5) the amount payable for the period in pounds` |
| s 124(6) | 2675 | encoded | `s 124(6) subsection (5) applies to the period` |
| s 124(6)(a) | 2676 | encoded | `s 124(6) subsection (5) applies to the period` |
| s 124(6)(b) | 2677 | encoded | `s 124(6) subsection (5) applies to the period` |
| s 124(7) | 2678 | encoded | `s 124(7) the allowance is an income-related employment and support allowance` |
| s 125 | 2679 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 125 [repealed or blank line] | 2680 | repealed or blank | a line of dots in the text: repealed or blank |
| s 126 | 2681 | inert 1 | section number and title |
| s 126(1) | 2682 | encoded | `s 126(1) section 126 applies to the person` |
| s 126(1)(a) | 2683 | encoded | `s 126(1) section 126 applies to the person` |
| s 126(1)(b) | 2684 | encoded | `s 126(1) section 126 applies to the person` |
| s 126(1)(b) (unlabelled limb) | 2685 | encoded | `s 126(1) section 126 applies to the person` |
| s 126(2) | 2686 | encoded | `s 126(2) the maternity period` |
| s 126(3) | 2687 | encoded | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(3)(a) | 2688 | encoded | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(3)(b) | 2689 | encoded | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(3)(c) | 2690 | encoded | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(3)(c)(i) | 2691 | encoded | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(3)(c)(ii) | 2692 | fork F6 | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(3)(d) | 2693 | encoded | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(3)(d)(i) | 2694 | encoded | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(3)(d)(ii) | 2695 | encoded | `s 126(3) the applicable amount to be used in pounds a week` |
| s 126(4) | 2696 | fork F6 | `s 126(4) the sum rounded down to a multiple of 5p` |
| s 126(5) | 2697 | encoded | `s 126(5)(a) the income taken into account in pounds` |
| s 126(5)(a) | 2698 | encoded | `s 126(5)(a) the income taken into account in pounds` |
| s 126(5)(a)(i) | 2699 | encoded | `s 126(5)(a) the income taken into account in pounds` |
| s 126(5)(a)(ii) | 2700 | encoded | `s 126(5)(a) the income taken into account in pounds` |
| s 126(5)(b) | 2701 | encoded | `s 126(5)(b) the weekly rate of income support payable in pounds` |
| s 126(5)(b)(i) | 2702 | encoded | `s 126(5)(b) the weekly rate of income support payable in pounds` |
| s 126(5)(b)(ii) | 2703 | encoded | `s 126(5)(b) the weekly rate of income support payable in pounds` |
| s 126(6) | 2704 | inert 2 | s 126(6): modifications of subsection (5) for a period of less than a week, as may be prescribed |
| s 126(7) | 2705 | encoded | `s 126(7) the relevant sum in pounds` |
| s 126(8) | 2706 | fork F7 | `s 126(8) the substituted sum in pounds` |
| s 126(8)(a) | 2707 | fork F7 | `s 126(8) the substituted sum in pounds` |
| s 126(8)(b) | 2708 | fork F7 | `s 126(8) the substituted sum in pounds` |
| s 126(8)(b) (unlabelled limb) | 2709 | fork F7 | `s 126(8) the substituted sum in pounds` |
| s 127 | 2710 | inert 1 | section number and title |
| s 127 (unlabelled limb) | 2711 | fork F1 | `s 127(a) section 126 applies to the person on the day`; `s 127(b) section 124(1) has effect with the substituted paragraph (c) on the day` |
| s 127(a) | 2712 | fork F1 | `s 127(a) section 126 applies to the person on the day`; `s 127(b) section 124(1) has effect with the substituted paragraph (c) on the day` |
| s 127(b) | 2713 | fork F1 | `s 127(b) section 124(1) has effect with the substituted paragraph (c) on the day` |
| s 127(b) (the paragraph substituted for s 124(1)(c)) | 2714 | fork F1 | `s 127(b) section 124(1) has effect with the substituted paragraph (c) on the day` |
| s 127(c) | 2715 | encoded | `s 127(c) the sum is recoverable in accordance with the regulations from the party` |
| Family credit | 2716 | inert 1 | a heading |
| s 128 | 2717 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 128 [repealed or blank line] | 2718 | repealed or blank | a line of dots in the text: repealed or blank |
| Disability working allowance | 2719 | inert 1 | a heading |
| s 129 | 2720 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 129 [repealed or blank line] | 2721 | repealed or blank | a line of dots in the text: repealed or blank |
| Housing benefit | 2722 | inert 1 | a heading |
| s 130 | 2723 | inert 1 | section number and title |
| s 130(1) | 2724 | encoded | `s 130(1) the person is entitled to housing benefit` |
| s 130(1)(a) | 2725 | encoded | `s 130(1) the person is entitled to housing benefit` |
| s 130(1)(b) | 2726 | encoded | `s 130(1) the person is entitled to housing benefit` |
| s 130(1)(c) | 2727 | encoded | `s 130(1) the person is entitled to housing benefit` |
| s 130(1)(c)(i) | 2728 | encoded | `s 130(1) the person is entitled to housing benefit` |
| s 130(1)(c)(ii) | 2729 | encoded | `s 130(1) the person is entitled to housing benefit` |
| s 130(2) | 2730 | encoded | `s 130(2) the payment is a payment in respect of a dwelling` |
| s 130(2)(a) | 2731 | encoded | `s 130(2) the payment is a payment in respect of a dwelling` |
| s 130(2)(b) | 2732 | encoded | `s 130(2) the payment is a payment in respect of a dwelling` |
| s 130(3) | 2733 | encoded | `s 130(3) the amount of housing benefit in pounds a week` |
| s 130(3)(a) | 2734 | encoded | `s 130(3) the amount of housing benefit in pounds a week` |
| s 130(3)(b) | 2735 | encoded | `s 130(3) the amount of housing benefit in pounds a week` |
| s 130(4) | 2736 | repealed or blank | a line of dots in the text: repealed or blank |
| s 130(5) | 2737 | repealed or blank | a line of dots in the text: repealed or blank |
| s 130A | 2738 | inert 1 | section number and title |
| s 130A(1) | 2739 | encoded | `s 130A(1) the appropriate maximum housing benefit in pounds` |
| s 130A(2) | 2740 | encoded | `s 130A(1) the appropriate maximum housing benefit in pounds` |
| s 130A(3) | 2741 | inert 2 | s 130A(3) to (6): what the regulations on the appropriate maximum housing benefit may include |
| s 130A(4) | 2742 | inert 2 | s 130A(3) to (6): what the regulations on the appropriate maximum housing benefit may include |
| s 130A(4)(a) | 2743 | inert 2 | s 130A(3) to (6): what the regulations on the appropriate maximum housing benefit may include |
| s 130A(4)(b) | 2744 | inert 2 | s 130A(3) to (6): what the regulations on the appropriate maximum housing benefit may include |
| s 130A(5) | 2745 | inert 2 | s 130A(3) to (6): what the regulations on the appropriate maximum housing benefit may include |
| s 130A(6) | 2746 | inert 2 | s 130A(3) to (6): what the regulations on the appropriate maximum housing benefit may include |
| s 130A(7) | 2747 | encoded | `s 130A(7) the determination is a rent officer determination` |
| s 130B | 2748 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 130B [repealed or blank line] | 2749 | repealed or blank | a line of dots in the text: repealed or blank |
| s 130C | 2750 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 130C [repealed or blank line] | 2751 | repealed or blank | a line of dots in the text: repealed or blank |
| s 130D | 2752 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 130D [repealed or blank line] | 2753 | repealed or blank | a line of dots in the text: repealed or blank |
| s 130E | 2754 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 130E [repealed or blank line] | 2755 | repealed or blank | a line of dots in the text: repealed or blank |
| s 130F | 2756 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 130F [repealed or blank line] | 2757 | repealed or blank | a line of dots in the text: repealed or blank |
| s 130G | 2758 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 130G [repealed or blank line] | 2759 | repealed or blank | a line of dots in the text: repealed or blank |
| Council tax benefit | 2760 | inert 1 | a heading |
| s 131 | 2761 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 131 [repealed or blank line] | 2762 | repealed or blank | a line of dots in the text: repealed or blank |
| s 132 | 2763 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 132 [repealed or blank line] | 2764 | repealed or blank | a line of dots in the text: repealed or blank |
| s 133 | 2765 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 133 [repealed or blank line] | 2766 | repealed or blank | a line of dots in the text: repealed or blank |
| General | 2767 | inert 1 | a heading |
| s 134 | 2768 | inert 1 | section number and title |
| s 134(1) | 2769 | encoded | `s 134(1) the person is barred from the income-related benefit by capital` |
| s 134(2) | 2770 | encoded | `s 134(2) the person's entitlement is excluded by another member's entitlement` |
| s 134(3) | 2771 | repealed or blank | a line of dots in the text: repealed or blank |
| s 134(4) | 2772 | encoded | `s 134(4) the income-related benefit is not payable` |
| s 135 | 2773 | inert 1 | section number and title |
| s 135(1) | 2774 | encoded | `s 135(1) the applicable amount in pounds` |
| s 135(2) | 2775 | encoded | `s 135(1) the applicable amount in pounds` |
| s 135(3) | 2776 | repealed or blank | a line of dots in the text: repealed or blank |
| s 135(4) | 2777 | repealed or blank | a line of dots in the text: repealed or blank |
| s 135(5) | 2778 | encoded | `s 135(5) the applicable amount includes an amount for being severely disabled` |
| s 135(6) | 2779 | inert 2 | s 135(6): power to make regulations on being or not being in a family |
| s 136 | 2780 | inert 1 | section number and title |
| s 136(1) | 2781 | encoded | `s 136(1) the amount treated as the claimant's in pounds` |
| s 136(2) | 2782 | inert 2 | s 136(2) to (5): powers and directions to regulations on income and capital |
| s 136(3) | 2783 | inert 2 | s 136(2) to (5): powers and directions to regulations on income and capital |
| s 136(4) | 2784 | inert 2 | s 136(2) to (5): powers and directions to regulations on income and capital |
| s 136(5) | 2785 | inert 2 | s 136(2) to (5): powers and directions to regulations on income and capital |
| s 136(5)(a) | 2786 | inert 2 | s 136(2) to (5): powers and directions to regulations on income and capital |
| s 136(5)(b) | 2787 | inert 2 | s 136(2) to (5): powers and directions to regulations on income and capital |
| s 136(5)(c) | 2788 | inert 2 | s 136(2) to (5): powers and directions to regulations on income and capital |
| s 136(5)(d) | 2789 | inert 2 | s 136(2) to (5): powers and directions to regulations on income and capital |
| s 136A | 2790 | inert 1 | section number and title |
| s 136A(1) | 2791 | encoded | `s 136A(1) subsections (2) and (3) apply to the benefit and the person` |
| s 136A(2) | 2792 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(3) | 2793 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(3)(a) | 2794 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(3)(b) | 2795 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(4) | 2796 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(4)(a) | 2797 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(4)(b) | 2798 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(4)(b)(i) | 2799 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(4)(b)(ii) | 2800 | inert 2 | s 136A(2) to (4): powers to make regulations on income and capital after the qualifying age |
| s 136A(5) | 2801 | encoded | `s 136A(5) how the term is defined` |
| s 136A(6) | 2802 | inert 2 | s 136A(6), (7): power to make regulations |
| s 136A(7) | 2803 | inert 2 | s 136A(6), (7): power to make regulations |
| s 137 | 2804 | inert 1 | section number and title |
| s 137(1) | 2805 | encoded | `s 137(1) the defined meaning applies` |
| s 137(1) “billing authority” | 2806 | encoded | `s 137(1) how the term is defined` |
| s 137(1) “child” | 2807 | encoded | `s 137(1) how the term is defined`; `s 137(1) the person is a child` |
| s 137(1) “couple” | 2808 | encoded | `s 137(1) how the term is defined`; `s 137(1) the two persons are a couple` |
| s 137(1) “couple” (unlabelled limb) | 2809 | fork F8 | `s 137(1) how the term is defined`; `s 137(1) the two persons are a couple` |
| s 137(1) “couple” (unlabelled limb) | 2810 | fork F8 | `s 137(1) how the term is defined`; `s 137(1) the two persons are a couple` |
| s 137(1) “couple” [repealed or blank line] | 2811 | repealed or blank | a line of dots in the text: repealed or blank |
| s 137(1) “couple” [repealed or blank line] | 2812 | repealed or blank | a line of dots in the text: repealed or blank |
| s 137(1) “dwelling” | 2813 | encoded | `s 137(1) how the term is defined`; `s 137(1) the accommodation is a dwelling` |
| s 137(1) “family” | 2814 | encoded | `s 137(1) how the term is defined`; `s 137(1) the persons are a family` |
| s 137(1) “family” (unlabelled limb) | 2815 | encoded | `s 137(1) how the term is defined`; `s 137(1) the persons are a family` |
| s 137(1) “family” (unlabelled limb) | 2816 | encoded | `s 137(1) how the term is defined`; `s 137(1) the persons are a family` |
| s 137(1) “family” (unlabelled limb) | 2817 | encoded | `s 137(1) how the term is defined`; `s 137(1) the persons are a family` |
| s 137(1) “income-based jobseeker’s allowance” | 2818 | encoded | `s 137(1) how the term is defined` |
| s 137(1) “industrial injuries scheme” | 2819 | encoded | `s 137(1) how the term is defined`; `s 137(1) the scheme is an industrial injuries scheme` |
| s 137(1) “industrial injuries scheme” [repealed or blank line] | 2820 | repealed or blank | a line of dots in the text: repealed or blank |
| s 137(1) “local authority” | 2821 | encoded | `s 137(1) how the term is defined`; `s 137(1) the body is a local authority in relation to Scotland` |
| s 137(1) “local authority” [repealed or blank line] | 2822 | repealed or blank | a line of dots in the text: repealed or blank |
| s 137(1) “local authority” [repealed or blank line] | 2823 | repealed or blank | a line of dots in the text: repealed or blank |
| s 137(1) “local authority” [repealed or blank line] | 2824 | repealed or blank | a line of dots in the text: repealed or blank |
| s 137(1) “pensionable age” | 2825 | encoded | `s 137(1) how the term is defined` |
| s 137(1) “prescribed” | 2826 | encoded | `s 137(1) how the term is defined` |
| s 137(1) “the qualifying age for state pension credit” | 2827 | encoded | `s 137(1) how the term is defined`; `s 137(1) the date the person attains the qualifying age for state pension credit`; `s 137(1) the person has attained the qualifying age for state pension credit` |
| s 137(1) “the qualifying age for state pension credit” (unlabelled limb) | 2828 | encoded | `s 137(1) how the term is defined`; `s 137(1) the date the person attains the qualifying age for state pension credit`; `s 137(1) the person has attained the qualifying age for state pension credit` |
| s 137(1) “the qualifying age for state pension credit” (unlabelled limb) | 2829 | encoded | `s 137(1) how the term is defined`; `s 137(1) the date the person attains the qualifying age for state pension credit`; `s 137(1) the person has attained the qualifying age for state pension credit` |
| s 137(1) “state pension credit” | 2830 | encoded | `s 137(1) how the term is defined` |
| s 137(1) “state pension credit” [repealed or blank line] | 2831 | repealed or blank | a line of dots in the text: repealed or blank |
| s 137(1) “war pension scheme” | 2832 | encoded | `s 137(1) the scheme is a war pension scheme` |
| s 137(1) “week” | 2833 | encoded | `s 137(1) the week in relation to council tax benefit containing the date` |
| s 137(1A) | 2834 | repealed or blank | a line of dots in the text: repealed or blank |
| s 137(2) | 2835 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(a) | 2836 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(b) | 2837 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(c) | 2838 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(d) | 2839 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(e) | 2840 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(f) | 2841 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(g) | 2842 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(h) | 2843 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(i) | 2844 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(j) | 2845 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(k) | 2846 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(l) | 2847 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| s 137(2)(m) | 2848 | inert 2 | s 137(2): powers to make regulations on residence, remunerative work, education, dwellings, households |
| Part VIII — The Social Fund | 2849 | inert 1 | a heading |
| s 138 | 2850 | inert 1 | section number and title |
| s 138(1) | 2851 | encoded | `s 138(1) the payment may be made out of the social fund` |
| s 138(1)(a) | 2852 | encoded | `s 138(1) the payment may be made out of the social fund` |
| s 138(1)(b) | 2853 | encoded | `s 138(1) the payment may be made out of the social fund` |
| s 138(1)(b)(i) | 2854 | encoded | `s 138(1) the payment may be made out of the social fund` |
| s 138(1)(b)(ii) | 2855 | encoded | `s 138(1) the payment may be made out of the social fund` |
| s 138(1)(b) (unlabelled limb) | 2856 | encoded | `s 138(1) the payment may be made out of the social fund` |
| s 138(2) | 2857 | encoded | `s 138(2) the heating payment may be made out of the social fund` |
| s 138(3) | 2858 | encoded | `s 138(3) the payment may be made to a third party` |
| s 138(4) | 2859 | encoded | `s 138(4) how the term is defined` |
| s 138(4A) | 2860 | encoded | `s 138(4A) the reference is read in Scotland as` |
| s 138(4A)(a) | 2861 | encoded | `s 138(4A) the reference is read in Scotland as` |
| s 138(4A)(b) | 2862 | encoded | `s 138(4A) the reference is read in Scotland as` |
| s 138(4A)(c) | 2863 | encoded | `s 138(4A) the reference is read in Scotland as` |
| s 138(4B) | 2864 | encoded | `s 138(4B)(a) sections 175(2) and (7) and 176 apply to the regulations` |
| s 138(4B)(a) | 2865 | encoded | `s 138(4B)(a) sections 175(2) and (7) and 176 apply to the regulations` |
| s 138(4B)(b) | 2866 | inert 2 | s 138(4B)(b), (4C): the negative procedure for Scottish regulations; the Order in Council power |
| s 138(4C) | 2867 | inert 2 | s 138(4B)(b), (4C): the negative procedure for Scottish regulations; the Order in Council power |
| s 138(5) | 2868 | inert 1 | s 138(5): lead-in words "In this Part--"; the three definitions that follow are encoded |
| s 138(5) “budgeting loan” | 2869 | encoded | `s 138(5) the payment is a budgeting loan` |
| s 138(5) “community care grant” | 2870 | encoded | `s 138(5) the payment is a community care grant` |
| s 138(5) “crisis loan” | 2871 | encoded | `s 138(5) the payment is a crisis loan` |
| s 138(5) “crisis loan” (unlabelled limb) | 2872 | encoded | `s 138(5) the payment meets a need or defrays an expense` |
| s 139 | 2873 | inert 1 | section number and title |
| s 139(1) | 2874 | encoded | `s 139(1) the person is an appropriate officer`; `s 139(1) the question of whether to award and how much is one for an appropriate officer` |
| s 139(2) | 2875 | encoded | `s 139(2) the person may determine that an award shall be payable in specified instalments at specified times` |
| s 139(3) | 2876 | repealed or blank | a line of dots in the text: repealed or blank |
| s 139(4) | 2877 | encoded | `s 139(4) the award is repayable on the notified terms`; `s 139(4) the duty to repay a crisis loan or budgeting loan on the notified terms` |
| s 139(5) | 2878 | encoded | `s 139(5) payment of the award is to be made to the applicant` |
| s 140 | 2879 | inert 1 | section number and title |
| s 140(1) | 2880 | encoded | `s 140(1) the appropriate officer's duty to have regard`; `s 140(1) the matter for a grant or a crisis loan`; `s 140(1) the officer must have regard to the matter` |
| s 140(1)(a) | 2881 | encoded | `s 140(1) the appropriate officer's duty to have regard`; `s 140(1) the matter for a grant or a crisis loan`; `s 140(1) the officer must have regard to the matter` |
| s 140(1)(b) | 2882 | encoded | `s 140(1) the appropriate officer's duty to have regard`; `s 140(1) the matter for a grant or a crisis loan`; `s 140(1) the officer must have regard to the matter` |
| s 140(1)(c) | 2883 | encoded | `s 140(1) the appropriate officer's duty to have regard`; `s 140(1) the matter for a grant or a crisis loan`; `s 140(1) the officer must have regard to the matter` |
| s 140(1)(d) | 2884 | encoded | `s 140(1) the appropriate officer's duty to have regard`; `s 140(1) the matter for a grant or a crisis loan`; `s 140(1) the officer must have regard to the matter` |
| s 140(1)(e) | 2885 | encoded | `s 140(1) the appropriate officer's duty to have regard`; `s 140(1) the matter for a grant or a crisis loan`; `s 140(1) the officer must have regard to the matter` |
| s 140(1A) | 2886 | fork F2 | `s 140(1A) the matter for a budgeting loan` |
| s 140(1A)(a) | 2887 | fork F2 | `s 140(1A) the matter for a budgeting loan` |
| s 140(1A)(b) | 2888 | fork F2 | `s 140(1A) the matter for a budgeting loan` |
| s 140(1A)(b) [repealed or blank line] | 2889 | repealed or blank | a line of dots in the text: repealed or blank |
| s 140(2) | 2890 | encoded | `s 140(2) the appropriate officer's duty to follow the general directions`; `s 140(2) the officer has done what the subsection requires` |
| s 140(3) | 2891 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4) | 2892 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(a) | 2893 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(aa) | 2894 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(b) | 2895 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(c) | 2896 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(d) | 2897 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(da) | 2898 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(e) | 2899 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(f) | 2900 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(f)(i) | 2901 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(f)(ii) | 2902 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4)(f) (unlabelled limb) | 2903 | inert 2 | s 140(3), (4): the Secretary of State's powers to issue directions and guidance |
| s 140(4ZA) | 2904 | encoded | `s 140(4ZA) the sum determined by applying the multiplier in pounds` |
| s 140(4ZB) | 2905 | encoded | `s 140(4ZB) how the term is defined` |
| s 140(5) | 2906 | encoded | `s 140(5) the officer must take account of the guidance of the officer nominated for the area` |
| Part 8A — Health in pregnancy grant | 2907 | inert 1 | a heading |
| s 140A | 2908 | inert 1 | section number and title |
| s 140A(1) | 2909 | encoded | `s 140A the woman is entitled to health in pregnancy grant`; `s 140A(1) the woman is entitled to payment of health in pregnancy grant` |
| s 140A(2) | 2910 | encoded | `s 140A the woman is entitled to health in pregnancy grant`; `s 140A(2) the woman is entitled to health in pregnancy grant as far as subsection (2) goes` |
| s 140A(3) | 2911 | encoded | `s 140A the woman is entitled to health in pregnancy grant`; `s 140A(3)(a) the woman is entitled to health in pregnancy grant as far as paragraph (a) goes`; `s 140A(3)(b) the woman is entitled to health in pregnancy grant as far as paragraph (b) goes` |
| s 140A(3)(a) | 2912 | encoded | `s 140A the woman is entitled to health in pregnancy grant`; `s 140A(3)(a) the woman is entitled to health in pregnancy grant as far as paragraph (a) goes`; `s 140A(3)(b) the woman is entitled to health in pregnancy grant as far as paragraph (b) goes` |
| s 140A(3)(b) | 2913 | encoded | `s 140A the woman is entitled to health in pregnancy grant`; `s 140A(3)(b) the woman is entitled to health in pregnancy grant as far as paragraph (b) goes` |
| s 140A(4) | 2914 | inert 2 | s 140A(4): power to prescribe when a woman is treated as being in Great Britain |
| s 140A(5) | 2915 | inert 1 | s 140A(5): lead-in words "In this section--"; the definitions that follow are encoded |
| s 140A(5) “health professional” | 2916 | encoded | `s 140A(5) how the term is defined` |
| s 140A(5) “prescribed” | 2917 | encoded | `s 140A(5) how the term is defined` |
| s 140A(5) “woman” | 2918 | encoded | `s 140A(5) how the term is defined`; `s 140A(5) the person is a woman` |
| s 140A(6) | 2919 | inert 2 | s 140A(6): the power to make regulations under s 140A is exercisable by the Treasury |
| s 140B | 2920 | inert 1 | section number and title |
| s 140B(1) | 2921 | encoded | `s 140B(1) the amount of health in pregnancy grant in pounds` |
| s 140B(2) | 2922 | inert 2 | s 140B(2): different amounts may be prescribed |
| Part IX — Child Benefit | 2923 | inert 1 | a heading |
| s 141 | 2924 | inert 1 | section number and title |
| s 141 (unlabelled limb) | 2925 | encoded | `s 141 the person is entitled to child benefit for the week` |
| s 142 | 2926 | inert 1 | section number and title |
| s 142(1) | 2927 | encoded | `s 142(1) the person is a child` |
| s 142(2) | 2928 | encoded | `s 142(2) the person is a qualifying young person` |
| s 142(2)(a) | 2929 | encoded | `s 142(2) the person is a qualifying young person` |
| s 142(2)(b) | 2930 | encoded | `s 142(2) the person is a qualifying young person` |
| s 143 | 2931 | inert 1 | section number and title |
| s 143(1) | 2932 | encoded | `s 143(1) the person is responsible for the child or qualifying young person in the week` |
| s 143(1)(a) | 2933 | encoded | `s 143(1) the person is responsible for the child or qualifying young person in the week`; `s 143(1)(a) the person is entitled for the week by virtue of paragraph (a)` |
| s 143(1)(b) | 2934 | fork F4 | `s 143(1) the person is responsible for the child or qualifying young person in the week`; `s 143(1)(b) the contributions are over and above those required for satisfying section 143(1)(b)`; `s 143(1)(b) the person is entitled for the week by virtue of paragraph (b)` |
| s 143(2) | 2935 | encoded | `s 143(2) the child or qualifying young person is treated as living with the person in the week` |
| s 143(3) | 2936 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(a) | 2937 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(b) | 2938 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c) | 2939 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(i) | 2940 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(ii) | 2941 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(iii) | 2942 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(iv) | 2943 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(v) | 2944 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(vi) | 2945 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(vii) | 2946 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(viii) | 2947 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(3)(c)(ix) | 2948 | encoded | `s 143(3) the day of absence is disregarded` |
| s 143(4) | 2949 | encoded | `s 143(4) the number of days that may be disregarded` |
| s 143(5) | 2950 | inert 2 | s 143(5): power to make regulations on contributing to cost and regular expenditure |
| s 143(5)(a) | 2951 | inert 2 | s 143(5): power to make regulations on contributing to cost and regular expenditure |
| s 143(5)(b) | 2952 | inert 2 | s 143(5): power to make regulations on contributing to cost and regular expenditure |
| s 143(5)(b) (unlabelled limb) | 2953 | inert 2 | s 143(5): power to make regulations on contributing to cost and regular expenditure |
| s 144 | 2954 | inert 1 | section number and title (the heading of s 144; its subsection (1) is a line of dots, subsections (2) and (3) are text) |
| s 144(1) | 2955 | repealed or blank | a line of dots in the text: repealed or blank |
| s 144(2) | 2956 | encoded | `s 144(2) entitlement to child benefit is excluded by Schedule 9` |
| s 144(3) | 2957 | encoded | `s 144(3) the person is the one entitled among those who would be entitled` |
| s 145 | 2958 | inert 1 | section number and title |
| s 145(1) | 2959 | encoded | `s 145(1) the weekly rate of child benefit in pounds` |
| s 145(2) | 2960 | inert 2 | s 145(2), (3): different rates may be prescribed; the day for new rates is set by order |
| s 145(3) | 2961 | inert 2 | s 145(2), (3): different rates may be prescribed; the day for new rates is set by order |
| s 145(4) | 2962 | encoded | `s 145(4) the rate prescribed may be lower than the rate it replaces` |
| s 145(5) | 2963 | repealed or blank | a line of dots in the text: repealed or blank |
| s 145(6) | 2964 | inert 2 | s 145(6), (7): variation and laying of an order |
| s 145(7) | 2965 | inert 2 | s 145(6), (7): variation and laying of an order |
| s 145A | 2966 | inert 1 | section number and title |
| s 145A(1) | 2967 | encoded | `s 145A(1) the person is entitled to child benefit for the week after the death` |
| s 145A(2) | 2968 | fork F3 | `s 145A(2) the other member of the couple is entitled to child benefit for the rest of the period` |
| s 145A(2)(a) | 2969 | fork F3 | `s 145A(2) the other member of the couple is entitled to child benefit for the rest of the period` |
| s 145A(2)(b) | 2970 | fork F3 | `s 145A(2) the other member of the couple is entitled to child benefit for the rest of the period` |
| s 145A(2)(b) (unlabelled limb) | 2971 | fork F3 | `s 145A(2) the other member of the couple is entitled to child benefit for the rest of the period` |
| s 145A(3) | 2972 | encoded | `s 145A(3) subsections (1) and (2) apply as if the person were the one who would have been entitled had the child been alive at the beginning of the week` |
| s 145A(4) | 2973 | encoded | `s 145A(4) section 77 applies with the omission of subsections (4) to (6)` |
| s 145A(5) | 2974 | inert 1 | s 145A(5): lead-in words "In this section--"; the definitions that follow are encoded |
| s 145A(5) “civil partnership” | 2975 | encoded | `s 145A(5) the two people are a civil partnership` |
| s 145A(5) “civil partnership” (unlabelled limb) | 2976 | encoded | `s 145A(5) the two people are a civil partnership` |
| s 145A(5) “civil partnership” (unlabelled limb) | 2977 | encoded | `s 145A(5) the two people are a civil partnership` |
| s 145A(5) “cohabiting couple” | 2978 | encoded | `s 145A(5) the two people are a cohabiting couple` |
| s 145A(5) “married couple” | 2979 | encoded | `s 145A(5) the two people are a married couple` |
| s 145A(5) “married couple” (unlabelled limb) | 2980 | encoded | `s 145A(5) the two people are a married couple` |
| s 145A(5) “married couple” (unlabelled limb) | 2981 | encoded | `s 145A(5) the two people are a married couple` |
| s 145A(5) “married couple” [repealed or blank line] | 2982 | repealed or blank | a line of dots in the text: repealed or blank |
| s 145A(6) | 2983 | repealed or blank | a line of dots in the text: repealed or blank |
| s 146 | 2984 | inert 1 | section number and title |
| s 146(1) | 2985 | encoded | `s 146(1) the child or qualifying young person is in Great Britain as the subsection requires` |
| s 146(2) | 2986 | encoded | `s 146(2) the person is in Great Britain as the subsection requires` |
| s 146(3) | 2987 | inert 2 | s 146(3): power to prescribe when a person is treated as being, or not being, in Great Britain |
| s 146A | 2988 | repealed or blank | title of a section whose body is a line of dots in this text |
| s 146A [repealed or blank line] | 2989 | repealed or blank | a line of dots in the text: repealed or blank |
| s 147 | 2990 | inert 1 | section number and title |
| s 147(1) | 2991 | inert 1 | s 147(1): lead-in words "In this Part of this Act--"; the definitions that follow are encoded |
| s 147(1) “prescribed” | 2992 | encoded | `s 147(1) how the term is defined` |
| s 147(1) “prescribed” [repealed or blank line] | 2993 | repealed or blank | a line of dots in the text: repealed or blank |
| s 147(1) “voluntary organisation” | 2994 | encoded | `s 147(1) the body is a voluntary organisation` |
| s 147(1) “week” | 2995 | encoded | `s 147(1) the week containing the date` |
| s 147(2) | 2996 | encoded | `s 147(2) the day on which a condition or fact in the week is judged` |
| s 147(3) | 2997 | encoded | `s 147(3) the person is within a reference in this Part to a parent, father or mother` |
| s 147(4) | 2998 | inert 2 | s 147(4), (5), (6)(a), (6)(b): powers to make regulations (residing together; polygamous marriages; modifications for voluntary organisations) |
| s 147(5) | 2999 | inert 2 | s 147(4), (5), (6)(a), (6)(b): powers to make regulations (residing together; polygamous marriages; modifications for voluntary organisations) |
| s 147(6) | 3000 | encoded | `s 147(6) this Part confers a right to child benefit on the body` |
| s 147(6)(a) | 3001 | inert 2 | s 147(4), (5), (6)(a), (6)(b): powers to make regulations (residing together; polygamous marriages; modifications for voluntary organisations) |
| s 147(6)(b) | 3002 | inert 2 | s 147(4), (5), (6)(a), (6)(b): powers to make regulations (residing together; polygamous marriages; modifications for voluntary organisations) |
| Part X — Christmas bonus for pensioners | 3003 | inert 1 | a heading |
| s 148 | 3004 | inert 1 | section number and title |
| s 148(1) | 3005 | encoded | `s 148(1) the person is entitled to payment under subsection (1)` |
| s 148(1)(a) | 3006 | encoded | `s 148(1) the person is entitled to payment under subsection (1)`; `s 148(1)(a) Place`; `s 148(1)(a) the place is one the paragraph names` |
| s 148(1)(b) | 3007 | encoded | `s 148(1) the person is entitled to payment under subsection (1)` |
| s 148(1)(b) (unlabelled limb) | 3008 | encoded | `s 148(1) the person is entitled to payment under subsection (1)` |
| s 148(2) | 3009 | encoded | `s 148(2) the member of the couple is also entitled to payment under subsection (2)` |
| s 148(2)(a) | 3010 | encoded | `s 148(2) the member of the couple is also entitled to payment under subsection (2)` |
| s 148(2)(b) | 3011 | encoded | `s 148(2) the member of the couple is also entitled to payment under subsection (2)` |
| s 148(2)(c) | 3012 | encoded | `s 148(2) the member of the couple is also entitled to payment under subsection (2)` |
| s 148(2)(c)(i) | 3013 | encoded | `s 148(2) the member of the couple is also entitled to payment under subsection (2)` |
| s 148(2)(c)(ii) | 3014 | encoded | `s 148(2) the member of the couple is also entitled to payment under subsection (2)` |
| s 148(2ZA) | 3015 | encoded | `s 148(2ZA) the provision to which the entitlement is subject` |
| s 148(2A) | 3016 | encoded | `s 148(2A) the age that paragraph (a) of subsection (2) reads` |
| s 148(3) | 3017 | encoded | `s 148(3)(a) who makes the payment` |
| s 148(3)(a) | 3018 | encoded | `s 148(3)(a) who makes the payment` |
| s 148(3)(b) | 3019 | fork F5 | `s 148(3)(b) the amount of the payment in pounds` |
| s 148(4) | 3020 | repealed or blank | a line of dots in the text: repealed or blank |
| s 148(5) | 3021 | encoded | `s 148(5) a further sum is payable in respect of the person` |
| s 149 | 3022 | inert 1 | section number and title |
| s 149(1) | 3023 | encoded | `s 149(1) the place is treated as part of the United Kingdom` |
| s 149(2) | 3024 | encoded | `s 149(2) the person is treated as entitled to a payment of the qualifying benefit` |
| s 149(2)(a) | 3025 | encoded | `s 149(2) the person is treated as entitled to a payment of the qualifying benefit` |
| s 149(2)(b) | 3026 | encoded | `s 149(2) the person is treated as entitled to a payment of the qualifying benefit` |
| s 149(3) | 3027 | encoded | `s 149(3) the person is treated as entitled to an increase in the payment of the qualifying benefit` |
| s 149(3)(a) | 3028 | encoded | `s 149(3) the person is treated as entitled to an increase in the payment of the qualifying benefit` |
| s 149(3)(b) | 3029 | encoded | `s 149(3) the person is treated as entitled to an increase in the payment of the qualifying benefit` |
| s 149(4) | 3030 | encoded | `s 149(4) the person is entitled to a payment of the war disablement pension` |
| s 149(5) | 3031 | encoded | `s 149(5) the sum is treated as benefit for the purposes of the enactment or instrument under which entitlement to the qualifying benefit arises` |
| s 149(6) | 3032 | encoded | `s 149(6) the payment and the right to receive it are disregarded` |
| s 149(6)(a) | 3033 | encoded | `s 149(6) the payment and the right to receive it are disregarded` |
| s 149(6)(b) | 3034 | encoded | `s 149(6) the payment and the right to receive it are disregarded` |
| s 149(6)(b) (unlabelled limb) | 3035 | encoded | `s 149(6) the payment and the right to receive it are disregarded` |
| s 150 | 3036 | inert 1 | section number and title |
| s 150(1) | 3037 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(a) | 3038 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(b) | 3039 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(ba) | 3040 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(bb) | 3041 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(bc) | 3042 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(bd) | 3043 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(c) | 3044 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(d) | 3045 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(e) | 3046 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(ea) | 3047 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(f) | 3048 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(g) | 3049 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(h) | 3050 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(i) | 3051 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(j) | 3052 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(k) | 3053 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(1)(l) | 3054 | encoded | `s 150(1) the payment is a qualifying benefit` |
| s 150(2) | 3055 | inert 1 | s 150(2): lead-in words "In this Part of this Act--"; the definitions that follow are encoded |
| s 150(2) “adult disability payment” | 3056 | encoded | `s 150(2) adult disability payment` |
| s 150(2) “armed forces independence payment” | 3057 | encoded | `s 150(2) armed forces independence payment` |
| s 150(2) “attendance allowance” | 3058 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3059 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3060 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3061 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3062 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3063 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3064 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3065 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3066 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “attendance allowance” (unlabelled limb) | 3067 | encoded | `s 150(2) the payment is an attendance allowance` |
| s 150(2) “carer support payment” | 3068 | encoded | `s 150(2) carer support payment` |
| s 150(2) “mobility supplement” | 3069 | encoded | `s 150(2) the supplement is a mobility supplement` |
| s 150(2) “pensionable age” | 3070 | encoded | `s 150(2) pensionable age` |
| s 150(2) “the qualifying age for state pension credit” | 3071 | encoded | `s 150(2) the date the person attains the qualifying age for state pension credit` |
| s 150(2) “the qualifying age for state pension credit” (unlabelled limb) | 3072 | encoded | `s 150(2) the date the person attains the qualifying age for state pension credit` |
| s 150(2) “the qualifying age for state pension credit” (unlabelled limb) | 3073 | encoded | `s 150(2) the date the person attains the qualifying age for state pension credit` |
| s 150(2) “qualifying employment and support allowance” | 3074 | encoded | `s 150(2) the allowance is a qualifying employment and support allowance` |
| s 150(2) “retirement pension” | 3075 | encoded | `s 150(2) the payment is a retirement pension` |
| s 150(2) “retirement pension” (unlabelled limb) | 3076 | encoded | `s 150(2) the payment is a retirement pension` |
| s 150(2) “retirement pension” (unlabelled limb) | 3077 | encoded | `s 150(2) the payment is a retirement pension` |
| s 150(2) “retirement pension” (unlabelled limb) | 3078 | encoded | `s 150(2) the payment is a retirement pension` |
| s 150(2) “state pension credit” | 3079 | encoded | `s 150(2) state pension credit` |
| s 150(2) “unemployability supplement or allowance” | 3080 | encoded | `s 150(2) the payment is an unemployability supplement or allowance` |
| s 150(2) “unemployability supplement or allowance” (unlabelled limb) | 3081 | encoded | `s 150(2) the payment is an unemployability supplement or allowance` |
| s 150(2) “unemployability supplement or allowance” (unlabelled limb) | 3082 | encoded | `s 150(2) the payment is an unemployability supplement or allowance` |
| s 150(2) “unemployability supplement or allowance” (unlabelled limb) | 3083 | encoded | `s 150(2) the payment is an unemployability supplement or allowance` |
| s 150(2) “unemployability supplement or allowance” (unlabelled limb) | 3084 | encoded | `s 150(2) the payment is an unemployability supplement or allowance` |
| s 150(2) “unemployability supplement or allowance” (unlabelled limb) | 3085 | encoded | `s 150(2) the payment is an unemployability supplement or allowance` |
| s 150(2) “unemployability supplement or allowance” (unlabelled limb) | 3086 | encoded | `s 150(2) the payment is an unemployability supplement or allowance` |
| s 150(2) “unemployability supplement or allowance” [repealed or blank line] | 3087 | repealed or blank | a line of dots in the text: repealed or blank |
| s 150(2) “war disablement pension” | 3088 | encoded | `s 150(2) the payment is a war disablement pension` |
| s 150(2) “war disablement pension” (unlabelled limb) | 3089 | encoded | `s 150(2) the payment is a war disablement pension` |
| s 150(2) “war disablement pension” (unlabelled limb) | 3090 | encoded | `s 150(2) the payment is a war disablement pension` |
| s 150(2) “war widow’s pension” | 3091 | encoded | `s 150(2) the payment is a war widow's pension` |
| s 150(2) “war widow’s pension” (unlabelled limb) | 3092 | encoded | `s 150(2) the payment is included because the Secretary of State accepts it as analogous` |
| s 150(3) | 3093 | encoded | `s 150(3) the two persons are a couple` |
| s 150(4) | 3094 | encoded | `s 150(4) the relevant week` |

## Fork register (ssc5)

A fork is a place where the words allow two readings that give different answers on a case somebody could bring.
Each entry gives the lines, the readings seen, the one taken, the words that license it, and what changes if the other is right.
Two kinds of reading are not forks and are listed under "Marginal readings for a lawyer (ssc5)" instead: a failed "if" read as the text's no (a), and a grant or bar limited by its own wording read as not the text's no (b), because the brief fixes both as the status quo.
The fork ids F1 to F8 are the ones the coverage table cites in its "fork" rows (21 rows).

### F1. What the paragraph s 127(b) substitutes for s 124(1)(c) requires (lines 2713-2714; 2658)

- Words: s 124(1)(c) reads "(c) he is not engaged in remunerative work and, if he is a member of a couple, the other member is not so engaged; ...".
  Section 127(b) says that for 15 days from a return to work "section 124(1) above shall have effect in relation to him as if the following paragraph were substituted for paragraph (c)—" and the paragraph is "(c) in the case of a member of a couple, the other member is not engaged in remunerative work; and".
- Readings seen: (1) the substituted paragraph replaces the whole of (c), so for the 15 days the claimant's own work does not bar, and a claimant who is not a member of a couple satisfies it because it speaks only "in the case of a member of a couple"; (2) the claimant's own-work condition survives and the substitution only drops the partner's; (3) a claimant who is not in a couple fails the substituted paragraph because it "says nothing" of him.
- Taken: (1).
  Reading (2) would make the substitution change nothing for a single claimant, and reading (3) would leave nobody single entitled in the 15 days that the section exists to cover.
- Where: `s 124(1)(c) the person satisfies paragraph (c)` (with the flag for the 15 days), `s 127(b) section 124(1) has effect with the substituted paragraph (c) on the day`; tested in `ssc5-tests-part7.l4`.
- If the other reading is right: a claimant who is working in the 15 days is `FALSE` on (c) under (2), and a single claimant is `FALSE` under (3).

### F2. Whether s 140(1A) lists the only matters for a budgeting loan (lines 2880-2888)

- Words: s 140(1): "an appropriate officer shall have regard, subject to subsection (2) below, to all the circumstances of the case and, in particular—" (a) to (e), for "a community care grant or a crisis loan".
  Section 140(1A) says that for "a budgeting loan" he "shall have regard to— (a) such of the applicant’s personal circumstances as are of a description specified in directions issued by the Secretary of State; and (b) the criteria specified in paragraphs (b), (d) and (e) of subsection (1) above;" and the next line is a line of dots.
- Readings seen: (1) the list in (1A) is exhaustive, so for a budgeting loan the other matters in (1) are not required (the officer may disregard them); (2) (1A) adds to the "all the circumstances" of (1), so every matter in (1) is also required.
- Taken: neither.
  A matter that (1A) lists answers `JUST TRUE`; a matter of (1) that (1A) does not list answers `NOTHING` (neither required nor excluded), so the encoding does not say which reading is right.
- Where: `s 140(1A) the matter for a budgeting loan`, reached through `s 140(1) the officer must have regard to the matter`; tested in `ssc5-tests-part8.l4`.
- If a reading is chosen: (1) makes the unlisted matters `JUST FALSE`; (2) makes them `JUST TRUE`.

### F3. The "living with" words in s 145A(2)(a) (lines 2968-2971; 2975-2981)

- Words: s 145A(2) gives the other member of a couple the entitlement if the person entitled under (1) "was— (a) a member of a married couple or civil partnership and living with the person to whom he was married or who was his civil partner, or (b) a member of a cohabiting couple,".
  Subsection (5) defines "married couple" as "a man and a woman who are married to each other and are neither— separated under a court order, nor separated in circumstances in which the separation is likely to be permanent", and "civil partnership" in the same way.
- Readings seen: (1) "and living with the person to whom he was married or who was his civil partner" is a further condition of limb (a), on top of the definitions in (5), which exclude only a separation under a court order or likely to be permanent; (2) the words only restate the definitions and add nothing.
- Taken: (1).
  Limb (b) needs no extra condition, because a cohabiting couple are defined in (5) as people "living together as if they were a married couple or civil partners".
- Where: `s 145A(2) the other member of the couple is entitled to child benefit for the rest of the period`; tested in `ssc5-tests-part9.l4`.
- If the other reading is right: a spouse who was away for a reason that is neither a court order nor likely to be permanent (a spell in hospital, a posting) is within limb (a); under (1) that case answers `NOTHING` (a relative-clause grant, reading (b)).

### F4. "Over and above those required" for s 143(1)(b), seam S18 (line 2934; asked at 1772, 2167, 5430)

- Words: s 143(1)(b): "he is contributing to the cost of providing for the child or qualifying young person at a weekly rate which is not less than the weekly rate of child benefit payable in respect of the child or qualifying young person for that week."
  The asking sections (ss 56, 77, Schedule 7) say "except in prescribed cases, the contributions are over and above those required for the purpose of satisfying section 143(1)(b)".
- Readings seen: (1) the contributions are over and above what (b) requires when their weekly rate is strictly greater than the weekly rate of child benefit payable for that child and week; (2) the comparison is made across everything the person contributes for all the children for whom (b) is being relied on, so a per-child comparison is not enough.
- Taken: (1), because (b) itself fixes what is "required" as that weekly rate.
- Where: `s 143(1)(b) the contributions are over and above those required for satisfying section 143(1)(b)`; the two rates are inputs; tested in `ssc5-tests-part9.l4`.
- If the other reading is right: the lead passes an aggregate rate instead of the per-child one; the function body does not change.

### F5. "£10 or such larger sum" when an order names less (line 3019)

- Words: s 148(3)(b): a payment "is to be of £10 or such larger sum as the Secretary of State may by order specify."
- Readings seen: (1) no order, or an order naming exactly £10, leaves the payment at £10; an order naming a larger sum sets the payment; an order naming less than £10 is not "a larger sum" and the text does not say what the payment is then; (2) whatever the order names is the payment; (3) £10 is a floor, so an order naming less is ignored and the payment is £10.
- Taken: (1), so an order naming less than £10 answers `NOTHING`.
- Where: `s 148(3)(b) the amount of the payment in pounds`; tested in `ssc5-tests-part10.l4` at 10.01, 10 and 9.
- If the other reading is right: under (2) the answer for 9 is 9; under (3) it is 10.

### F6. Which sum s 126(4) rounds in s 126(3)(c)(ii) (lines 2692, 2696)

- Words: s 126(3)(c)(ii): where the applicable amount "includes other amounts, the portion of it which is included in respect of them shall be reduced to one-half and any further portion of it which is included in respect of the member of the couple to whom this section applies shall be disregarded".
  Section 126(4): "Where a reduction under subsection (3)(c) above would not produce a sum which is a multiple of 5p, the reduction shall be to the nearest lower sum which is such a multiple."
- Readings seen: (1) the halved portion (the sum the portion is "reduced to") is rounded down to a multiple of 5p; (2) the whole applicable amount that results is rounded down; (3) the amount taken off is the sum rounded, which would round the result up.
- Taken: (1).
  In (c)(i) the whole amount is the sum reduced to one half, so (1) and (2) agree there; (3) is excluded because the text says the reduction is "to" a lower sum, not "by".
- Where: `s 126(3) the applicable amount to be used in pounds a week`, `s 126(4) the sum rounded down to a multiple of 5p`; tested in `ssc5-tests-part7.l4`.
- If the other reading is right: (1) and (2) differ in (c)(ii) only when the portions that are not halved are not multiples of 5p.

### F7. What "the remainder" is in s 126(8)(b) (lines 2706-2709)

- Words: if the increased sum "is not a multiple of 50p, disregarding the remainder if it is 25p and, if it is not, rounding it up or down to the nearest 50p".
- Readings seen: (1) the remainder is the excess over the largest multiple of 50p not above the sum, so a sum ending .25 or .75 has a remainder of 25p and is rounded down to the multiple below, and any other remainder rounds to the nearest 50p; (2) the remainder is the pence over the pound, so only a sum ending .25 has a remainder of 25p, and a sum ending .75 has a remainder of 75p, is "not" 25p, and must round to the nearest 50p, which is a tie the text does not resolve.
- Taken: (1), because "a multiple of 50p" is the unit the sentence has just named.
- Where: `s 126(8) the substituted sum in pounds`; tested in `ssc5-tests-part7.l4`.
- If the other reading is right: sums ending .75 have no answer under the words (`NOTHING`); every other sum is unchanged.

### F8. Spouses who are not in the same household: "couple" in s 137(1) (lines 2808-2810)

- Words: "“couple” means— two people who are married to, or civil partners of, each other and are members of the same household; or two people who are not married to, or civil partners of, each other but are living together as if they were a married couple or civil partners otherwise than in prescribed circumstances;".
- Readings seen: (1) the definition is closed ("means"), so spouses or civil partners who are not members of the same household fall under neither limb and are not a couple; (2) spouses who live apart but still act as a couple are within limb two.
- Taken: (1), because limb two begins "two people who are not married to, or civil partners of, each other".
  The "prescribed circumstances" qualify limb two only, by their place in the sentence; whether they apply is an input.
- Where: `s 137(1) the two persons are a couple` (seam S12); tested in `ssc5-tests-part7.l4` (married but not one household; married, apart, but living together as if married).
- If the other reading is right: the two cases above answer `JUST TRUE`, not `JUST FALSE`.

## Jural relations (ssc5)

One row per provision, or group of provisions, in the range; a provision that creates no relation (a definition, a counting rule, a heading) is listed as `none`.
Holder is the party with the right, privilege, power or immunity; bearer is the party with the correlative duty, no-right, liability or disability.
Parties are only those the text names: where it names none, the cell says "the section names none" (finding 3).
Each relation is stated once, neutrally, and the last column names the layer-1 rule that carries it.

| provision(s) | lines | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | relation | L4 rule |
|---|---|---|---|---|---|
| s 112, s 113, s 114, s 115, s 116, s 117, s 118, s 119, s 120, s 121, s 122, s 123, s 124, s 126, s 127, s 130, s 130A, s 134, s 135, s 136, s 136A, s 137, s 138, s 139, s 140, s 140A, s 140B, s 141, s 142, s 143, s 144, s 145, s 145A, s 146, s 147, s 148, s 149, s 150 | 2446-3036 | none | none | none (the section's number and title) | none encoded |
| s 112(1), s 112(2A) | 2447-2453 | the Treasury, with the concurrence of the Secretary of State | the persons whose employment protection entitlements are deemed earnings | power / liability (regulations; inert 2) | none encoded |
| s 112(2), s 112(3) | 2450-2454 | none | none | none (a definition) | `s 112(2) the sum is an employment protection entitlement`; `s 112(3) Sum` |
| s 113(1) | 2460-2460 | the Secretary of State or other paying authority (the section names none) | the person absent from Great Britain or in legal custody | immunity / disability (disqualified for the period; no increase payable) | `s 113(1) an increase of the benefit is payable in respect of the person as the beneficiary's wife, husband or civil partner for the period`; `s 113(1) the person is disqualified for receiving the benefit for the period` |
| s 113(2), s 113(3) | 2463-2464 | the maker of the regulations (the text says "Regulations may") | the persons receiving in-patient treatment, or who would be entitled but for a provision | power / liability (regulations; inert 2) | none encoded |
| s 114 | 2467-2478 | the maker of the regulations (the text says "Regulations may") | beneficiaries and the persons they maintain | power / liability (regulations; inert 2) | none encoded |
| s 115(1), s 115(3) | 2481-2483 | none | none | none (an applying rule and a treating rule; no new relation) | `s 115(1) Parts I to V and this Part apply to the person as if employed by a private person`; `s 115(3) the employment is employed earner's employment for the purposes of Part V` |
| s 115(2), s 115(4) | 2482-2484 | none | none | none (an exception to s 115(1); a reference rule) | `s 115(1) Parts I to V and this Part apply to the person as if employed by a private person` |
| s 116(1), s 116(3) | 2486-2492 | none | none | none (a treating rule; a definition) | `s 116(1) the person is treated as an employed earner in respect of membership of the forces`; `s 116(3) the establishment or organisation is part of Her Majesty's forces` |
| s 116(2) | 2489-2489 | the Treasury, with the concurrence of the Secretary of State | persons who are or have been members of the forces | power / liability (regulations; inert 2) | none encoded |
| s 117(1), s 117(2), s 118, s 119 | 2494-2495 | the Treasury, with the concurrence of the Secretary of State | persons employed on board ships, married women and widows, persons outside Great Britain | power / liability (regulations; inert 2); the seam functions for s 94(5) are none | `s 117 the accident falls within the exception` |
| s 120(1), s 120(3), s 120(4), s 120(5) | 2510-2516 | the Treasury, with the concurrence of the Secretary of State (s 120(4): the Treasury) | continental shelf workers and prescribed persons | power / liability (regulations; inert 2) | `s 120 the accident falls within the exception` |
| s 120(2) | 2511-2511 | none | none | none (a definition) | `s 120(2) the employment is in connection with continental shelf operations` |
| s 121 | 2523-2527 | the Treasury, with the concurrence of the Secretary of State | persons in annulled or polygamous marriages | power / liability (regulations; inert 2) | none encoded |
| s 122(1) | 2532-2625 | none | none | none (the Act's defined terms) | `s 122(1) Bank of England base rate`; `s 122(1) ITEPA 2003`; `s 122(1) Old Cases payments`; `s 122(1) PAYE settlement agreement`; `s 122(1) PPF periodic payments`; `s 122(1) Regulation (EC) No 1408/71` ... |
| s 122(2), s 122(3), s 122(5), s 122(6A) | 2627-2632 | the Treasury (s 122(5): the maker of regulations) | persons to whom the regulations apply | power / liability (regulations; inert 2) | none encoded |
| s 122(4) | 2629-2629 | the person residing with a spouse who is entitled to child benefit | the payer of child benefit (the section names none) | claim / duty (a deeming of entitlement) | `s 122(4) the person is treated as entitled to the child benefit to which the spouse is entitled` |
| s 122(6) | 2631-2631 | none | none | none (a definition) | `s 122(6) the person is permanently incapable of self-support` |
| s 122(6B) | 2633-2633 | the Treasury | persons earning otherwise than weekly | power / liability (the power's reach) | `s 122(6B) the amount prescribed is one the power includes` |
| s 123(1) | 2639-2639 | none | none | none (names the benefits) | `s 123(1) the benefit is an income-related benefit` |
| s 123(2) | 2645-2645 | any person (to inspect the schemes) | the Secretary of State | claim / duty | `s 123(2) the Secretary of State's duty to make copies of the schemes available`; `s 123(2) the person may inspect a copy of the scheme without payment` |
| s 123(3) | 2646-2646 | persons who may be entitled to housing benefit | every authority granting housing benefit | claim / duty | `s 123(3)(a) the authority must take steps so that the person becomes aware`; `s 123(3)(a) the housing benefit authority's duty to make persons aware`; `s 123(3)(b) the housing benefit authority's duty to make copies of its scheme available`; `s 123(3)(b) the person may inspect a copy of the housing benefit scheme without payment` |
| s 123(4) | 2649-2649 | persons who may be entitled to council tax benefit | every billing authority or, in Scotland, local authority | claim / duty | `s 123(4)(a) the authority must take steps so that the person becomes aware`; `s 123(4)(a) the billing authority's duty to make persons aware`; `s 123(4)(b) the billing authority's duty to make copies of its scheme available`; `s 123(4)(b) the person may inspect a copy of the council tax benefit scheme without payment` |
| s 124(1) | 2654-2654 | the person in Great Britain who meets paragraphs (a) to (h) | the payer of income support (the section names none) | claim / duty | `s 124(1) the person is entitled to income support` |
| s 124(1A), s 124(1B), s 124(5), s 124(6), s 124(7) | 2664-2678 | none | none | none (a counting rule, a definition) | `s 124(1A) the person falls within a category prescribed under subsection (1)(e)`; `s 124(5) the amount payable for the period in pounds`; `s 124(6) subsection (5) applies to the period`; `s 124(7) the allowance is an income-related employment and support allowance` |
| s 124(4) | 2671-2671 | the person entitled to income support | the payer of income support (the section names none) | claim / duty (the amount) | `s 124(4) the amount of income support in pounds a week` |
| s 126 | 2682-2706 | none | none | none (reduces the claim under s 124; it creates no new relation) | `s 126(1) section 126 applies to the person`; `s 126(2) the maternity period`; `s 126(3) the applicable amount to be used in pounds a week`; `s 126(4) the sum rounded down to a multiple of 5p`; `s 126(5)(a) the income taken into account in pounds`; `s 126(7) the relevant sum in pounds` ... |
| s 130(1), s 130(3) | 2724-2733 | the person liable to make payments in respect of a dwelling | the payer of housing benefit (the section names none) | claim / duty | `s 130(1) the person is entitled to housing benefit`; `s 130(3) the amount of housing benefit in pounds a week` |
| s 130(2) | 2730-2730 | none | none | none (a definition) | `s 130(2) the payment is a payment in respect of a dwelling` |
| s 130A | 2739-2747 | none | none | none (the maximum; the regulations' powers are inert 2) | `s 130A(1) the appropriate maximum housing benefit in pounds`; `s 130A(7) the determination is a rent officer determination` |
| s 134(1), s 134(2), s 134(4) | 2769-2772 | the payer of the income-related benefit (the section names none) | the person whose capital exceeds the limit, the family member, the claimant of a small amount | immunity / disability | `s 134(1) the person is barred from the income-related benefit by capital`; `s 134(2) the person's entitlement is excluded by another member's entitlement`; `s 134(4) the income-related benefit is not payable` |
| s 135, s 136, s 136A, s 137 | 2774-2835 | none | none | none (rules of calculation, definitions; the regulations' powers are inert 2) | `s 135(1) the applicable amount in pounds`; `s 135(5) the applicable amount includes an amount for being severely disabled`; `s 136(1) the amount treated as the claimant's in pounds`; `s 136A(1) subsections (2) and (3) apply to the benefit and the person`; `s 136A(5) how the term is defined`; `s 137(1) how the term is defined` ... |
| s 138(1), s 138(2), s 138(3) | 2851-2858 | the Secretary of State (the Scottish Ministers in Scotland, s 138(4A)) | applicants for social fund payments | privilege / no-right ("may be made") | `s 138(1) the payment may be made out of the social fund`; `s 138(2) the heating payment may be made out of the social fund`; `s 138(3) the payment may be made to a third party` |
| s 138(4), s 138(4A), s 138(4B), s 138(4C), s 138(5) | 2859-2871 | none | none | none (definitions, substitutions, procedure) | `s 138(4) how the term is defined`; `s 138(4A) the reference is read in Scotland as`; `s 138(4B)(a) sections 175(2) and (7) and 176 apply to the regulations`; `s 138(5) the payment is a budgeting loan`; `s 138(5) the payment is a community care grant`; `s 138(5) the payment is a crisis loan` |
| s 139(1), s 139(2) | 2874-2875 | the appropriate officer | the applicant | power / liability (to determine; to order instalments) | `s 139(1) the person is an appropriate officer`; `s 139(1) the question of whether to award and how much is one for an appropriate officer`; `s 139(2) the person may determine that an award shall be payable in specified instalments at specified times` |
| s 139(4) | 2877-2877 | the Secretary of State | the person by or on behalf of whom the application for a crisis loan or budgeting loan was made | claim / duty (to repay on the notified terms) | `s 139(4) the award is repayable on the notified terms`; `s 139(4) the duty to repay a crisis loan or budgeting loan on the notified terms` |
| s 139(5) | 2878-2878 | the applicant | the payer of the award | claim / duty (payment to the applicant unless the officer determines otherwise) | `s 139(5) payment of the award is to be made to the applicant` |
| s 140(1), s 140(1A), s 140(2), s 140(5) | 2880-2906 | the applicant | the appropriate officer | claim / duty (to have regard; to follow directions) | `s 140(1) the appropriate officer's duty to have regard`; `s 140(1) the matter for a grant or a crisis loan`; `s 140(1) the officer must have regard to the matter`; `s 140(1A) the matter for a budgeting loan`; `s 140(2) the appropriate officer's duty to follow the general directions`; `s 140(2) the officer has done what the subsection requires` ... |
| s 140(3), s 140(4) | 2891-2892 | the Secretary of State | appropriate officers | power / liability (directions and guidance; inert 2) | none encoded |
| s 140(4ZA) | 2904-2904 | the Secretary of State | appropriate officers | power / liability (a multiplier in a direction) | `s 140(4ZA) the sum determined by applying the multiplier in pounds` |
| s 140(4ZB) | 2905-2905 | none | none | none (a definition) | `s 140(4ZB) how the term is defined` |
| s 140A(1) | 2909-2909 | the woman who satisfies the prescribed conditions | the payer of the grant (the section names none) | claim / duty | `s 140A the woman is entitled to health in pregnancy grant`; `s 140A(1) the woman is entitled to payment of health in pregnancy grant` |
| s 140A(2), s 140A(3) | 2910-2911 | the payer of the grant (the section names none) | the woman who lacks the stated qualification | immunity / disability | `s 140A the woman is entitled to health in pregnancy grant`; `s 140A(2) the woman is entitled to health in pregnancy grant as far as subsection (2) goes`; `s 140A(3)(a) the woman is entitled to health in pregnancy grant as far as paragraph (a) goes`; `s 140A(3)(b) the woman is entitled to health in pregnancy grant as far as paragraph (b) goes` |
| s 140A(4), s 140A(6) | 2914-2919 | the Treasury | women claiming the grant | power / liability (regulations; inert 2) | none encoded |
| s 140A(5) | 2915-2918 | none | none | none (definitions) | `s 140A(5) how the term is defined`; `s 140A(5) the person is a woman` |
| s 140B(1) | 2921-2921 | none | none | none (the amount is prescribed) | `s 140B(1) the amount of health in pregnancy grant in pounds` |
| s 140B(2) | 2922-2922 | the Treasury | women claiming the grant | power / liability (regulations; inert 2) | none encoded |
| s 142, s 143(1), s 143(2), s 143(3), s 143(4) | 2927-2949 | none | none | none (definitions and counting rules) | `s 142(1) the person is a child`; `s 142(2) the person is a qualifying young person`; `s 143(1) the person is responsible for the child or qualifying young person in the week`; `s 143(2) the child or qualifying young person is treated as living with the person in the week`; `s 143(3) the day of absence is disregarded`; `s 143(4) the number of days that may be disregarded` |
| s 143(5) | 2950-2950 | the maker of the regulations (the text says "Regulations may") | persons claiming to be responsible | power / liability (regulations; inert 2) | none encoded |
| s 144(2), s 144(3) | 2956-2957 | the payer of child benefit (the section names none) | the persons excluded; all but one of those who would be entitled | immunity / disability | `s 144(2) entitlement to child benefit is excluded by Schedule 9`; `s 144(3) the person is the one entitled among those who would be entitled` |
| s 145(1) | 2959-2959 | none | none | none (the rate is prescribed) | `s 145(1) the weekly rate of child benefit in pounds` |
| s 145(2), s 145(3), s 145(6), s 145(7) | 2960-2965 | the maker of the regulations; the Secretary of State (orders) | persons receiving child benefit | power / liability (regulations and orders; inert 2) | none encoded |
| s 145(4) | 2962-2962 | persons receiving child benefit | the maker of the regulations | immunity / disability (no lower rate may replace a rate) | `s 145(4) the rate prescribed may be lower than the rate it replaces` |
| s 145A(1), s 145A(2) | 2967-2968 | the person entitled for the week of the death; the other member of the couple | the payer of child benefit (the section names none) | claim / duty | `s 145A(1) the person is entitled to child benefit for the week after the death`; `s 145A(2) the other member of the couple is entitled to child benefit for the rest of the period` |
| s 145A(3), s 145A(4), s 145A(5) | 2972-2979 | none | none | none (treating rules; definitions) | `s 145A(3) subsections (1) and (2) apply as if the person were the one who would have been entitled had the child been alive at the beginning of the week`; `s 145A(4) section 77 applies with the omission of subsections (4) to (6)`; `s 145A(5) the two people are a civil partnership`; `s 145A(5) the two people are a cohabiting couple`; `s 145A(5) the two people are a married couple` |
| s 146(1), s 146(2) | 2985-2986 | the payer of child benefit (the section names none) | the claimant or the child not in Great Britain | immunity / disability | `s 146(1) the child or qualifying young person is in Great Britain as the subsection requires`; `s 146(2) the person is in Great Britain as the subsection requires` |
| s 146(3) | 2987-2987 | the maker of the regulations (the text says "Circumstances may be prescribed") | persons claiming child benefit | power / liability (regulations; inert 2) | none encoded |
| s 147(1), s 147(2), s 147(3) | 2991-2997 | none | none | none (definitions and counting rules) | `s 147(1) how the term is defined`; `s 147(1) the body is a voluntary organisation`; `s 147(1) the week containing the date`; `s 147(2) the day on which a condition or fact in the week is judged`; `s 147(3) the person is within a reference in this Part to a parent, father or mother` |
| s 147(4), s 147(5) | 2998-2999 | the maker of the regulations (the text says "Regulations may") | persons claiming child benefit | power / liability (regulations; inert 2) | none encoded |
| s 147(6) | 3000-3000 | the payer of child benefit (the section names none); the Secretary of State (modifying regulations) | bodies corporate; voluntary organisations | immunity / disability; power / liability (inert 2) | `s 147(6) this Part confers a right to child benefit on the body` |
| s 148(1), s 148(2) | 3005-3009 | the person (and the member of a couple) entitled to the Christmas bonus | the Secretary of State (s 148(3)(a)) | claim / duty | `s 148(1) the person is entitled to payment under subsection (1)`; `s 148(2) the member of the couple is also entitled to payment under subsection (2)` |
| s 148(2ZA), s 148(2A) | 3015-3016 | none | none | none (a substitution) | `s 148(2A) the age that paragraph (a) of subsection (2) reads`; `s 148(2ZA) the provision to which the entitlement is subject` |
| s 148(3) | 3017-3017 | the person entitled | the Secretary of State | claim / duty (who pays; at least 10 pounds) | `s 148(3)(a) who makes the payment` |
| s 148(5) | 3021-3021 | the Secretary of State | the person entitled (against a second claim) | immunity / disability (only one sum) | `s 148(5) a further sum is payable in respect of the person` |
| s 149(1), s 149(2), s 149(3), s 149(4), s 149(5) | 3023-3031 | none | none | none (treating rules) | `s 149(1) the place is treated as part of the United Kingdom`; `s 149(2) the person is treated as entitled to a payment of the qualifying benefit`; `s 149(3) the person is treated as entitled to an increase in the payment of the qualifying benefit`; `s 149(4) the person is entitled to a payment of the war disablement pension`; `s 149(5) the sum is treated as benefit for the purposes of the enactment or instrument under which entitlement to the qualifying benefit arises` |
| s 149(6) | 3032-3032 | the payee | those assessing income tax or a person's means | immunity / disability (the payment is disregarded) | `s 149(6) the payment and the right to receive it are disregarded` |
| s 150 | 3037-3094 | none | none | none (definitions, a couple, the relevant week) | `s 150(1) the payment is a qualifying benefit`; `s 150(2) adult disability payment`; `s 150(2) armed forces independence payment`; `s 150(2) carer support payment`; `s 150(2) pensionable age`; `s 150(2) state pension credit` ... |

## Marginal readings for a lawyer (ssc5)

The brief fixes two readings as the status quo and asks for every branch that rests on one: (a) a failed "if" counts as the text's no, within the provision that holds the "if"; (b) a prohibition or grant limited by its own wording does not.
I add (c), two places where I read a phrase as a closed definition.
The tables are generated from the `FALSE-kind` and `NOTHING-kind` comments in the layer-1 modules by `work/mkmarg.py` and list the file and line of every branch: 7 for (a), 77 for (b), 2 for (c).
Flat negatives ("No person shall be entitled", "shall not be payable", "do not apply") count as the text saying no and are not listed.

### Reading a result: FALSE and NOTHING (ssc5)

Every rule that can answer "no" or "the text does not say" answers `MAYBE BOOLEAN` (or `MAYBE NUMBER`, `MAYBE DATE`, `MAYBE STRING`).
`JUST TRUE` is the text saying yes in its own words: a person "is entitled", a sum "shall be", a definition "means" and the case matches.
`JUST FALSE` is the text saying no in its own words, and each such branch carries `-- FALSE-kind (the text says no in its own words): "<the words>"`:
a "means" definition and the case does not match; a flat negative ("No person shall be entitled", "shall not be payable", "do not apply"); an "unless" or "only if" that is not met; and, on one marginal reading (a) below, the failed "if" of a grant.
`NOTHING` is "the text does not answer", and each such branch carries `-- NOTHING-kind (<why>)` with one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
In this Act the commonest reasons are "points outside the text" (the amount, the age, the circumstances or the rate is "as may be prescribed", or the section is "subject to" regulations) and "limited by its own wording" (a grant is "for a prescribed period", "in a week", "who is responsible", and the case is outside the limit).
A caller must never turn `NOTHING` into `FALSE`; the helpers in `ssc5-logic.l4` carry `NOTHING` through.
The one helper that discards a known answer is `s 124(1) holds or else nothing`, which turns `JUST FALSE` into `NOTHING` (never the other way); it is used wherever a relative-clause grant or a "treated as" rule has no "no" of its own, in the seven rules `s 122(4)`, `s 124(1A)`, `s 126(1)`, `s 139(2)`, `s 140A(1)`, `s 145A(2)` and `s 148(2)` (reading (b), listed below).
`s 148(2)` is the example that was written wrongly first: a person whose place of residence the paragraph does not name is `NOTHING`, and a first version collapsed that to `FALSE` through `is known to hold`; the tests for that rule assert both cases.
The layer-1 modules carry 61 `FALSE-kind` comments and 117 `NOTHING-kind` comments; by reason the `NOTHING-kind` comments are: limited by its own wording 77, points outside the text 19, silent 15, list not closed 3, includes 2, undefined term 1.

### (a) A failed "if" counts as the text's no (7 branches)

The text says "X is entitled if C" or "shall be treated as X if C"; it does not say "and not otherwise".
Taken: a failed "if" is `JUST FALSE`.
It does not extend to a computation rule such as s 143(3) (a day of absence is disregarded "if" it is due solely to ...), which answers `NOTHING` when the "if" fails.

| function | where | the words of the "if" | the other reading |
|---|---|---|---|
| `s 124(1) the person is entitled to income support` | ssc5-part7.l4:208 | "A person in Great Britain is entitled to income support if" | a failed "if" is silent: NOTHING |
| `s 130(1) the person is entitled to housing benefit` | ssc5-part7.l4:603 | "A person is entitled to housing benefit if" | a failed "if" is silent: NOTHING |
| `s 134(1) the person is barred from the income-related benefit by capital` | ssc5-part7.l4:660 | "No person shall be entitled to an income-related benefit if his capital or a prescribed part of it exceeds the prescribed amount" | a failed "if" is silent: NOTHING |
| `s 143(1) the person is responsible for the child or qualifying young person in the week` | ssc5-part9.l4:148 | "a person shall be treated as responsible for a child or qualifying young person in any week if" | a failed "if" is silent: NOTHING |
| `s 148(2) the member of the couple is also entitled to payment under subsection (2)` | ssc5-part10.l4:160 | "shall also be entitled to payment under this subsection in respect of that year if" | a failed "if" is silent: NOTHING |
| `s 149(2) the person is treated as entitled to a payment of the qualifying benefit` | ssc5-part10.l4:228 | "shall be treated ... as entitled to a payment of a qualifying benefit if he would be so entitled" | a failed "if" is silent: NOTHING |
| `s 149(3) the person is treated as entitled to an increase in the payment of the qualifying benefit` | ssc5-part10.l4:241 | "shall be treated ... as entitled in respect of the other member of the couple to an increase ... if he would be so entitled" | a failed "if" is silent: NOTHING |

### (b) A grant or bar limited by its own wording is not the text's no (77 branches)

The text grants something to "a person who ...", for "a prescribed period", "in a week", "at all reasonable hours", or bars something only in a stated case, and the case before us falls outside the stated limit.
Taken: the answer is `NOTHING` (the text does not answer), never `JUST FALSE`.
Where a rule here uses `s 124(1) holds or else nothing` for a relative-clause grant, a known `JUST FALSE` among the conditions becomes `NOTHING` on this reading.

| function | where | the limit in the text | the other reading |
|---|---|---|---|
| `s 113(1) the person is disqualified for receiving the benefit for the period` | ssc5-part6.l4:80 | "for any period during which the person (a) is absent from Great Britain; or (b) is undergoing imprisonment or detention in legal custody" | the limit is the text's no: JUST FALSE |
| `s 113(1) an increase of the benefit is payable in respect of the person as the beneficiary's wife, husband or civil partner for the period` | ssc5-part6.l4:97 | the bar is not triggered | the limit is the text's no: JUST FALSE |
| `s 115(1) Parts I to V and this Part apply to the person as if employed by a private person` | ssc5-part6.l4:113 | "persons employed by or under the Crown" | the limit is the text's no: JUST FALSE |
| `s 115(3) the employment is employed earner's employment for the purposes of Part V` | ssc5-part6.l4:123 | the subsection speaks only of those two employments | the limit is the text's no: JUST FALSE |
| `s 116(1) the person is treated as an employed earner in respect of membership of the forces` | ssc5-part6.l4:143 | "a person who is serving as a member of Her Majesty's forces shall, while he is so serving" | the limit is the text's no: JUST FALSE |
| `s 116(1) the person is treated as an employed earner in respect of membership of the forces` | ssc5-part6.l4:150 | the subsection lists the purposes | the limit is the text's no: JUST FALSE |
| `s 116(3) the establishment or organisation is part of Her Majesty's forces` | ssc5-part6.l4:165 | the text limits what may be prescribed to ones "in which persons serve under the control of the Defence Council" and does not say what follows if regulations go beyond that | the limit is the text's no: JUST FALSE |
| `s 122(1) the pension is deferred` | ssc5-part6.l4:244 | "in relation to a Category A or Category B retirement pension" and "in relation to a shared additional pension" | the limit is the text's no: JUST FALSE |
| `s 122(1) the tax year named by a pair of successive years` | ssc5-part6.l4:266 | "a pair of successive years" | the limit is the text's no: JUST FALSE |
| `s 122(4) the person is treated as entitled to the child benefit to which the spouse is entitled` | ssc5-part6.l4:829 | "A person who is residing with his spouse" | the limit is the text's no: JUST FALSE |
| `s 123(2) the person may inspect a copy of the scheme without payment` | ssc5-part7.l4:63 | "at local offices of the Department for Work and Pensions at all reasonable hours" | the limit is the text's no: JUST FALSE |
| `s 123(3)(a) the authority must take steps so that the person becomes aware` | ssc5-part7.l4:83 | "Every authority granting housing benefit ... persons who may be entitled to housing benefit from the authority" | the limit is the text's no: JUST FALSE |
| `s 123(3)(b) the person may inspect a copy of the housing benefit scheme without payment` | ssc5-part7.l4:106 | "at their principal office at all reasonable hours" | the limit is the text's no: JUST FALSE |
| `s 123(4)(a) the authority must take steps so that the person becomes aware` | ssc5-part7.l4:126 | "in respect of council tax payable to the authority" | the limit is the text's no: JUST FALSE |
| `s 123(4)(b) the person may inspect a copy of the council tax benefit scheme without payment` | ssc5-part7.l4:149 | "at its principal office at all reasonable hours" | the limit is the text's no: JUST FALSE |
| `s 124(1A) the person falls within a category prescribed under subsection (1)(e)` | ssc5-part7.l4:256 | "Subsection (1A) does not apply if regulations ... are in force" | the limit is the text's no: JUST FALSE |
| `s 124(1A) the person falls within a category prescribed under subsection (1)(e)` | ssc5-part7.l4:260 | "a person who— (a) is not a member of a couple, and (b) is responsible for, and a member of the same household as, a child under the age of 5" | the limit is the text's no: JUST FALSE |
| `s 124(4) the amount of income support in pounds a week` | ssc5-part7.l4:286 | "where a person is entitled to income support" | the limit is the text's no: JUST FALSE |
| `s 124(5) the amount payable for the period in pounds` | ssc5-part7.l4:296 | "for a period to which this subsection applies" | the limit is the text's no: JUST FALSE |
| `s 124(6) subsection (5) applies to the period` | ssc5-part7.l4:311 | "a period of less than a week" | the limit is the text's no: JUST FALSE |
| `s 126(1) section 126 applies to the person` | ssc5-part7.l4:358 | "a person ... (a) who is prevented ... or (b) who would be so prevented" | the limit is the text's no: JUST FALSE |
| `s 127(b) section 124(1) has effect with the substituted paragraph (c) on the day` | ssc5-part7.l4:519 | "until the end of the period of 15 days beginning with that day" | the limit is the text's no: JUST FALSE |
| `s 127(c) the sum is recoverable in accordance with the regulations from the party` | ssc5-part7.l4:543 | "where the person to whom it was paid is a member of a couple" | the limit is the text's no: JUST FALSE |
| `s 127(c) the sum is recoverable in accordance with the regulations from the party` | ssc5-part7.l4:544 | "any sum paid by way of income support for that period of 15 days" | the limit is the text's no: JUST FALSE |
| `s 130(3) the amount of housing benefit in pounds a week` | ssc5-part7.l4:643 | "Where a person is entitled to housing benefit" | the limit is the text's no: JUST FALSE |
| `s 134(4) the income-related benefit is not payable` | ssc5-part7.l4:681 | "Where the amount ... would be less than a prescribed amount" | the limit is the text's no: JUST FALSE |
| `s 135(5) the applicable amount includes an amount for being severely disabled` | ssc5-part7.l4:698 | "the applicable amount for a severely disabled person shall include" | the limit is the text's no: JUST FALSE |
| `s 136(1) the amount treated as the claimant's in pounds` | ssc5-part7.l4:711 | "Where a person claiming an income-related benefit is a member of a family ... except in prescribed circumstances" | the limit is the text's no: JUST FALSE |
| `s 136A(1) subsections (2) and (3) apply to the benefit and the person` | ssc5-part7.l4:729 | "in relation to housing benefit and council tax benefit" | the limit is the text's no: JUST FALSE |
| `s 136A(1) subsections (2) and (3) apply to the benefit and the person` | ssc5-part7.l4:730 | "in the case of any person who has attained the qualifying age for state pension credit" | the limit is the text's no: JUST FALSE |
| `s 138(1) the payment may be made out of the social fund` | ssc5-part8.l4:45 | "payments of prescribed amounts ... in prescribed circumstances" | the limit is the text's no: JUST FALSE |
| `s 138(1) the payment may be made out of the social fund` | ssc5-part8.l4:47 | "payments of prescribed amounts ... in prescribed circumstances" | the limit is the text's no: JUST FALSE |
| `s 138(1) the payment may be made out of the social fund` | ssc5-part8.l4:49 | "in accordance with directions given or guidance issued by the Secretary of State" | the limit is the text's no: JUST FALSE |
| `s 138(1) the payment may be made out of the social fund` | ssc5-part8.l4:51 | same | the limit is the text's no: JUST FALSE |
| `s 138(1) the payment may be made out of the social fund` | ssc5-part8.l4:53 | same | the limit is the text's no: JUST FALSE |
| `s 138(2) the heating payment may be made out of the social fund` | ssc5-part8.l4:71 | "of a prescribed amount ... to prescribed descriptions of persons, in prescribed circumstances to meet expenses for heating which appear to the Secretary of State" | the limit is the text's no: JUST FALSE |
| `s 138(3) the payment may be made to a third party` | ssc5-part8.l4:82 | "with a view to the third party providing, or arranging for the provision of, goods or services for the applicant" | the limit is the text's no: JUST FALSE |
| `s 138(3) the payment may be made to a third party` | ssc5-part8.l4:84 | same | the limit is the text's no: JUST FALSE |
| `s 138(3) the payment may be made to a third party` | ssc5-part8.l4:86 | same | the limit is the text's no: JUST FALSE |
| `s 138(3) the payment may be made to a third party` | ssc5-part8.l4:87 | "such as is mentioned in subsection (1)(b)" | the limit is the text's no: JUST FALSE |
| `s 138(3) the payment may be made to a third party` | ssc5-part8.l4:88 | "such as is mentioned in subsection (1)(b)" | the limit is the text's no: JUST FALSE |
| `s 138(3) the payment may be made to a third party` | ssc5-part8.l4:89 | "such as is mentioned in subsection (1)(b)" | the limit is the text's no: JUST FALSE |
| `s 138(4A) the reference is read in Scotland as` | ssc5-part8.l4:124 | "This section has effect in or as regards Scotland as if" | the limit is the text's no: JUST FALSE |
| `s 138(4B)(a) sections 175(2) and (7) and 176 apply to the regulations` | ssc5-part8.l4:135 | "Where regulations are made by the Scottish Ministers under this section" | the limit is the text's no: JUST FALSE |
| `s 139(1) the question of whether to award and how much is one for an appropriate officer` | ssc5-part8.l4:223 | "a payment mentioned in section 138(1)(b)" | the limit is the text's no: JUST FALSE |
| `s 139(1) the question of whether to award and how much is one for an appropriate officer` | ssc5-part8.l4:224 | "a payment mentioned in section 138(1)(b)" | the limit is the text's no: JUST FALSE |
| `s 139(1) the question of whether to award and how much is one for an appropriate officer` | ssc5-part8.l4:225 | "a payment mentioned in section 138(1)(b)" | the limit is the text's no: JUST FALSE |
| `s 139(2) the person may determine that an award shall be payable in specified instalments at specified times` | ssc5-part8.l4:233 | "An appropriate officer may determine" | the limit is the text's no: JUST FALSE |
| `s 139(4) the award is repayable on the notified terms` | ssc5-part8.l4:259 | "upon such terms and conditions as before the award is paid the Secretary of State notifies" | the limit is the text's no: JUST FALSE |
| `s 139(4) the award is repayable on the notified terms` | ssc5-part8.l4:261 | same | the limit is the text's no: JUST FALSE |
| `s 139(4) the award is repayable on the notified terms` | ssc5-part8.l4:262 | "An award of a crisis loan or a budgeting loan" | the limit is the text's no: JUST FALSE |
| `s 139(4) the award is repayable on the notified terms` | ssc5-part8.l4:263 | same | the limit is the text's no: JUST FALSE |
| `s 139(4) the award is repayable on the notified terms` | ssc5-part8.l4:264 | same | the limit is the text's no: JUST FALSE |
| `s 139(4) the award is repayable on the notified terms` | ssc5-part8.l4:265 | same | the limit is the text's no: JUST FALSE |
| `s 140(1) the officer must have regard to the matter` | ssc5-part8.l4:312 | the duty is stated for community care grants, crisis loans and budgeting loans | the limit is the text's no: JUST FALSE |
| `s 140(1) the officer must have regard to the matter` | ssc5-part8.l4:313 | same | the limit is the text's no: JUST FALSE |
| `s 140(1) the officer must have regard to the matter` | ssc5-part8.l4:314 | same | the limit is the text's no: JUST FALSE |
| `s 140(1) the matter for a grant or a crisis loan` | ssc5-part8.l4:332 | "where the payment is repayable" | the limit is the text's no: JUST FALSE |
| `s 140(1A) the matter for a budgeting loan` | ssc5-part8.l4:349 | "the criteria specified in paragraphs (b), (d) and (e)", and (d) is for "where the payment is repayable" | the limit is the text's no: JUST FALSE |
| `s 140(1A) the matter for a budgeting loan` | ssc5-part8.l4:351 | "(b), (d) and (e)" are the criteria named | the limit is the text's no: JUST FALSE |
| `s 140(1A) the matter for a budgeting loan` | ssc5-part8.l4:352 | same | the limit is the text's no: JUST FALSE |
| `s 140(1A) the matter for a budgeting loan` | ssc5-part8.l4:353 | subsection (1A) lists the matters and does not say "all the circumstances" | the limit is the text's no: JUST FALSE |
| `s 140A(1) the woman is entitled to payment of health in pregnancy grant` | ssc5-part8.l4:474 | "A woman who satisfies prescribed conditions" | the limit is the text's no: JUST FALSE |
| `s 143(3) the day of absence is disregarded` | ssc5-part9.l4:81 | "in such circumstances as may be prescribed" | the limit is the text's no: JUST FALSE |
| `s 143(3) the day of absence is disregarded` | ssc5-part9.l4:83 | "if it is due solely to the fact that" | the limit is the text's no: JUST FALSE |
| `s 143(2) the child or qualifying young person is treated as living with the person in the week` | ssc5-part9.l4:115 | "Where a person has had a child or qualifying young person living with him at some time before a particular week" | the limit is the text's no: JUST FALSE |
| `s 144(3) the person is the one entitled among those who would be entitled` | ssc5-part9.l4:182 | "Where ... two or more persons would be entitled" | the limit is the text's no: JUST FALSE |
| `s 141 the person is entitled to child benefit for the week` | ssc5-part9.l4:241 | "A person who is responsible for one or more children or qualifying young persons" | the limit is the text's no: JUST FALSE |
| `s 145A(1) the person is entitled to child benefit for the week after the death` | ssc5-part9.l4:276 | "for a prescribed period following that week" | the limit is the text's no: JUST FALSE |
| `s 145A(2) the other member of the couple is entitled to child benefit for the rest of the period` | ssc5-part9.l4:343 | "If the person entitled to child benefit under subsection (1) dies before the end of that prescribed period" | the limit is the text's no: JUST FALSE |
| `s 145A(3) subsections (1) and (2) apply as if the person were the one who would have been entitled had the child been alive at the beginning of the week` | ssc5-part9.l4:352 | "If a child dies before the end of the week in which he is born" | the limit is the text's no: JUST FALSE |
| `s 145A(4) section 77 applies with the omission of subsections (4) to (6)` | ssc5-part9.l4:361 | "Where a person is entitled to child benefit ... under this section" | the limit is the text's no: JUST FALSE |
| `s 148(1) the person is entitled to payment under subsection (1)` | ssc5-part10.l4:103 | "Any person who in any year ... shall ... be entitled" | the limit is the text's no: JUST FALSE |
| `s 148(2) the member of the couple is also entitled to payment under subsection (2)` | ssc5-part10.l4:158 | "any person who is a member of a couple and is entitled to a payment under subsection (1)" | the limit is the text's no: JUST FALSE |
| `s 148(3)(b) the amount of the payment in pounds` | ssc5-part10.l4:198 | "£10 or such larger sum as the Secretary of State may by order specify" | the limit is the text's no: JUST FALSE |
| `s 149(4) the person is entitled to a payment of the war disablement pension` | ssc5-part10.l4:252 | the subsection only takes a person NOT to be entitled; it does not say when a person is | the limit is the text's no: JUST FALSE |
| `s 149(6) the payment and the right to receive it are disregarded` | ssc5-part10.l4:282 | "shall be disregarded for all purposes of income tax and for the purposes of any enactment or instrument under which regard is had to a person's means" | the limit is the text's no: JUST FALSE |

### (c) Two phrases read as "means" (2 branches)

"That is to say" (s 139(1)) and "shall be taken to consist of" (s 116(3)) are read as a closed definition, so a case outside the list is `JUST FALSE`.

| function | where | the words | the other reading |
|---|---|---|---|
| `s 116(3) the establishment or organisation is part of Her Majesty's forces` | ssc5-part6.l4:161 | "shall be taken to consist of such establishments and organisations as may be prescribed" | the words are a gloss, not a closed definition: NOTHING outside the list |
| `s 139(1) the person is an appropriate officer` | ssc5-part8.l4:210 | "that is to say, an officer of the Secretary of State who, acting under his authority, is exercising functions of the Secretary of State in relation to payments so mentioned" | the words are a gloss, not a closed definition: NOTHING outside the list |

## Seams (ssc5)

Names are those PLAN.md section 5 gives (S-numbers) or section 3 (K-numbers).
At the merge the lead replaces an input by a call to the answering function; the arguments of each answering function are listed so the call can be wired.

### Answered by ssc5 (other parts ask)

| seam | asking section | answering function (type) | arguments |
| --- | --- | --- | --- |
| S12 | ssc3 s 45AA | `s 137(1) the two persons are a couple` (`MAYBE BOOLEAN`) | a core `Couple`; whether the circumstances are ones prescribed to take the pair out of limb two |
| S18 | ssc3 s 56; ssc4 s 77; ssc9 Schedule 7 | `s 143(1)(b) the contributions are over and above those required for satisfying section 143(1)(b)` (`MAYBE BOOLEAN`) | the weekly rate of the contributions; the weekly rate of child benefit payable for the child and week (fork F4) |
| S20 | ssc4 s 94(5) | `s 117 the accident falls within the exception`, `s 119 the accident falls within the exception`, `s 120 the accident falls within the exception` (`MAYBE BOOLEAN` each) | s 117: employed on board a ship, vessel, hovercraft or aircraft; regulations under s 117(1) apply the provision. s 119: outside Great Britain at a prescribed time or in prescribed circumstances; regulations under s 119 apply it. s 120: the s 120(2) answer; prescribed employment; regulations under s 120(1) apply it |
| S25 | ssc6 s 162; ssc7 ss 171ZZ3, 171ZZ13 | `s 120(2) the employment is in connection with continental shelf operations` (`BOOLEAN`) | the employment is in connection with activities; the activities would fall within s 11(2) of the Petroleum Act 1998 if paragraphs (a) and (d) of s 11(8) were omitted |
| S33 | ssc9 Schedule 10 | `s 143(1)(a) the person is entitled for the week by virtue of paragraph (a)`, `s 143(1)(b) the person is entitled for the week by virtue of paragraph (b)` (`BOOLEAN` each) | (a): the child is living with the person in the week; the `s 143(2)` answer. (b): the weekly rate of the person's contribution; the weekly rate of child benefit payable |

### Asked by ssc5 as plain inputs (other parts answer)

| seam | asked in | input (type) |
| --- | --- | --- |
| S37 | `s 122(1) the pension is deferred` | `s 55(3) the pension is deferred` (`MAYBE BOOLEAN`); `s 55C(3) the shared additional pension is deferred` (`MAYBE BOOLEAN`) |
| K2 | `s 124(1) the person is entitled to income support` | `s 173(a) the person is over 16` (`MAYBE BOOLEAN`) |
| K2 | `s 126(1) section 126 applies to the person` ("other than a child") | `s 173(a) the person is under 16` (`MAYBE BOOLEAN`) |
| K2 | `s 124(1A) the person falls within a category prescribed under subsection (1)(e)` | `s 173(a) the person is under 5` (`MAYBE BOOLEAN`); the person it asks about is the child |
| K2 | `s 137(1) the person is a child` and `s 142(1) the person is a child` | `s 173(a) the person is under 16` (`MAYBE BOOLEAN`) |
| K2, departure from the pattern | s 142(2) "qualifying young person" | `s 173(a) the person is under the age prescribed under subsection (2)(a)` (`MAYBE BOOLEAN`): regulations prescribe the age, so no number can be written in the name and the lead must supply the age when wiring the call |

K1 (`s 172(a)`, Great Britain includes the place) is not taken.
Sections 124(1), 140A and 146 ask whether the person or the child is in Great Britain as a plain fact that the person states, so the territorial waters rule is the lead's to wire in at that fact if wanted.
K3 is followed: each of `ssc5-part6.l4`, `ssc5-part7.l4`, `ssc5-part8.l4` and `ssc5-part10.l4`, the files that use a short name from s 174, says in a comment near its head which Act each short name means.

### Seams the plan lacks (found by reading; PLAN.md lists them only in its appendix of pattern matches, "ssc5 -> ssc9: 144->Sch 10, 144->Sch 9", sentences not read)

| asked in | input (type) | why |
| --- | --- | --- |
| `s 144(2) entitlement to child benefit is excluded by Schedule 9`, line 2956 | `sch 9 the exclusion from entitlement to child benefit applies` (`MAYBE BOOLEAN`) | "Schedule 9 to this Act shall have effect for excluding entitlement to child benefit": the Schedule decides, and `JUST TRUE` is the text's own "excluding" |
| `s 144(3) the person is the one entitled among those who would be entitled`, line 2957; and `s 141 the person is entitled to child benefit for the week` | `sch 10 the person is the one entitled under the priority rules` (`MAYBE BOOLEAN`) | "two or more persons would be entitled ... one of them only shall be entitled" and the Schedule says which; the count of persons who would be entitled is a plain number input |

Other cross-references from this range into other parts (PLAN.md lists them in the same appendix: ss 114, 115, 122, 137, 145A, 149, 150 pointing at ssc1, ssc2, ssc3, ssc4, ssc6, ssc8 and ssc9 provisions) are not seam inputs.
The definition records of ss 122(1) and 150(2) name what a term points at in their text field and call nothing there, and where a rule here depends on another benefit (ss 148 and 149, the qualifying benefit) the entitlement is a plain fact stated in the asking function's own words.

## Findings: what the text turns out to say (ssc5)

Each finding was checked against the text file or the deposit when it was written; the check is named.

1. **Thirteen sections in this range are only a heading and a line of dots in this text**: ss 125, 128, 129, 130B, 130C, 130D, 130E, 130F, 130G, 131, 132, 133 and 146A, and a further sixteen subsections (122(1A), 122(7), 122(8), 124(2), 124(3), 130(4), 130(5), 134(3), 135(3), 135(4), 137(1A), 139(3), 144(1), 145(5), 145A(6), 148(4)) are lines of dots.
   The coverage table marks each "repealed or blank" and encodes nothing for it.
   (Check: the table's "repealed or blank" rows, 58, and the rule in `work/mkcov.py` that a section title followed by a line of dots is blank; s 144 is not blank, only its subsection (1).)
   One consequence: s 131 (council tax benefit) is blank, but s 123(1)(e) (line 2644), s 123(4) (lines 2650-2651), s 136A and the "week" definition in s 137(1) (line 2833) still speak of council tax benefit, and are encoded for what they say.
2. **Sections 117, 119 and 120 do not themselves except any accident from the bar in s 94(5).**
   Section 94(5) (line 2288) reads "Subject to sections 117, 119 and 120 below, industrial injuries benefit shall not be payable in respect of an accident happening while the earner is outside Great Britain."
   Each of those sections is a power to make regulations (lines 2494, 2508 and 2510), so the three functions for seam S20 answer `JUST TRUE` only where regulations apply the provision to the accident, and `NOTHING` otherwise (`NOTHING-kind (points outside the text)`).
   A caller must not read `NOTHING` there as "the bar applies".
3. **The text names no payer in ss 113(1), 122(4), 124(1), 124(4), 130, 134, 140A, 141, 144(2) and (3), 145A, 146 and 147(6)**, and no creditor in s 127(c) ("recoverable in accordance with the regulations").
   The jural table says "the section names none" in the holder or bearer cell where that is so, and invents no authority; the core's `Authority` is not used for them.
   (Check: `grep 'names none' work/jural.tsv`, 14 rows besides the comment line.)
4. **The converter dropped some lettering.**
   Seventy-two lines are cited in the coverage table as "(unlabelled limb)" because the text gives them no letter or number: they are mostly the limbs of the definitions in s 122(1), s 137(1), s 145A(5) and s 150(2), which the table cites by the defined term and the line.
   In s 127 two lines begin "(c)": line 2714 is the paragraph that s 127(b) substitutes for s 124(1)(c), and line 2715 is s 127(c); the table labels line 2714 "s 127(b) (the paragraph substituted for s 124(1)(c))".
5. **"Pensionable age" is borrowed.**
   Sections 122(1) (line 2597) and 137(1) (line 2825) give it "the meaning given by the rules in paragraph 1 of Schedule 4 to the Pensions Act 1995", which is not in the sources.
   A woman's date of attaining it is the core's `Person` field `date of attaining pensionable age`; a man's "qualifying age for state pension credit" is the pensionable age of "a woman born on the same day as the man" (line 2829), so the date that woman attains it is an input the person states.
6. **"Week" has three meanings in this range**: seven days beginning with Sunday (s 122(1), line 2624), beginning with Monday in relation to council tax benefit (s 137(1), line 2833), and beginning with Monday for Part IX (s 147(1), line 2995).
   Each has its own function (`s 122(1) the week containing the date`, `s 137(1) the week in relation to council tax benefit containing the date`, `s 147(1) the week containing the date`), distinguished by `(Day date) MODULO 7`, which is 0 for a Sunday and 1 for a Monday on the stable binary.
7. **The rate of child benefit is not in this text.**
   Section 145(1) says "such weekly rate as may be prescribed", so `s 145(1) the weekly rate of child benefit in pounds` answers `NOTHING` unless the person gives a rate, and s 145(4) ("No rate prescribed in place of a rate previously in force shall be lower than the rate that it replaces") is encoded as a bar on a lower rate, not as a rate.
   The same holds for every amount that regulations or orders prescribe (the applicable amount in s 124 and the portions of it in s 126(3) are two): they are inputs.
   The only figures the Act states are listed in rule P7 of the decision procedure above.
8. **Section 141 grants entitlement to a person "who is responsible", and the bars sit elsewhere in the Part**: presence in Great Britain (s 146), exclusion by Schedule 9 (s 144(2)) and priority among several entitled persons by Schedule 10 (s 144(3)).
   `s 141 the person is entitled to child benefit for the week` answers `JUST FALSE` when a bar bites, `JUST TRUE` when no bar bites and the person is responsible, and `NOTHING` when responsibility is not established or a bar's answer is not known.
   The reason `NOTHING` and not `JUST FALSE` for a person who is not responsible: the text says who is entitled ("a person who is responsible"), not that others are not.
9. **The definitions of s 122(1) and the other definition sections are records, not yes-or-no tests.**
   Most of them point at another provision, at regulations, or at another Act, so a function that answered "is this a benefit" would invent a test the text does not give.
   The type `s 122(1) A definition` says which way the Act defines a term (a definition by "means", a definition by "includes", a construction by reference to another provision, a meaning borrowed from another Act or instrument, a plain statement of what the term is, or blank in this text) and what it points at or says.
   There are 62 of these records in `ssc5-part6.l4` and 12 more in parts 7 to 10.
   The 62 are tested for their way, checked against the line of the text, and for their text as a regression guard only, because the stable binary has no string length or non-emptiness test.

## Changes after the independent review (ssc5)

An independent reviewer ran its own 1,041 assertions against the merged encoding; seven fell in this range (ssc5 lines 2444-3094).
Each was judged against the text and against the brief's lists of grounds for `JUST FALSE` and for `NOTHING`, not against the reviewer's concession.
Function names, argument lists and exported types are unchanged.

| id | provision | verdict | what the branch does now |
| --- | --- | --- | --- |
| S361 | s 126(2), line 2686 | reviewer's slip | unchanged: 24 May 2026 is the start of the 6th week before the week beginning Sunday 5 July 2026 (the 5th is 31 May) |
| S377b | s 137(1) "dwelling", line 2813 | reviewer's slip | unchanged: "means" gives `JUST FALSE` for a business office |
| S364b | s 127(a), line 2712 | `NOTHING` (silent) | unchanged: the day before the return day is not decided by s 127(a), which fixes when s 126 stops applying, not when it began; s 126(1) and the period's start decide the earlier days, and the function is not given them |
| S364d | s 127(b), line 2713 | `NOTHING` (limited by its own wording) | unchanged: a stated period of 15 days limits the effect, which the brief lists under `NOTHING`; "until" also appears in the brief's list for `JUST FALSE`, and the branch is one of the grants limited to a period or to "while" a state lasts (ss 113(1), 116(1), 145A(1)) that all answer `NOTHING` outside the limit; listed under (b) |
| S368a | s 134(1), line 2769 | defect | now `JUST FALSE` when the capital does not exceed the prescribed amount: the function is named for the bar's own condition and so tests it |
| S385a | s 140A(2), line 2910 | defect | now `JUST TRUE` when the "unless" is met: the function is named "as far as subsection (2) goes", like `s 146(1)` and `s 146(2)`, which already answered both ways |
| S356b | s 122(6B), line 2633 | `NOTHING` (includes) | unchanged: "includes power to prescribe an amount which exceeds by not more than £1" does not say that a larger amount is outside the power |

Sibling branches of the same shape, changed in the same pass so that the encoding agrees with itself (rule P3):

- `s 134(2)`: now `JUST FALSE` when no other member is entitled or the circumstances are prescribed ones ("Except in prescribed circumstances").
- `s 140A(3)(a)` and `s 140A(3)(b)`: now `JUST TRUE` when the "unless" is met.
- `s 139(5)`, `s 122(1)` and `s 137(1)` "the defined meaning applies": now `JUST FALSE` when the "unless" is triggered ("unless the appropriate officer determines otherwise", "unless the context otherwise requires"), as `s 143(2)` and `s 126(1)` already answered.

The composite `s 140A the woman is entitled to health in pregnancy grant` is unchanged: a bar that answers `JUST TRUE` and a bar that answers `NOTHING` both leave the answer to `s 140A(1)`.
`s 134(4)` and `s 113(1)` are unchanged: their names state an effect (not payable, disqualified) that other provisions can also bring about, so outside the text's own words they answer `NOTHING`.

## What the stable binary does not accept (ssc5)

The binary is the stable `l4` 1.6.98.
Rows marked "probed" were run on 1.6.98 with one- or few-line files at the end of this run (positive control: `(Day (Date 5 1 2026)) MODULO 7` with `IMPORT daydate` answers 1, a Monday); rows marked "keel" are the keel's own probes in `KEEL-NOTES.md` that I did not repeat.

| construct | what 1.6.98 does | source |
| --- | --- | --- |
| `REFUSE` | check error, "I could not find a definition for the identifier" | probed |
| `#ASSERT REFUSED f 0` | the same error, on `REFUSED` | probed; keel |
| `... ELSE NOTHING BECAUSE "no"` | parse error at `BECAUSE`; `BECAUSE` is accepted only in `LEST BREACH BY p BECAUSE "..."`, which these modules use | probed |
| `YMD 2020 1 1` | check error, "I could not find a definition for the identifier"; use `Date day month year` | probed; keel |
| `STRLEN "abc"` | the same error; so a string's length or non-emptiness cannot be tested, and the text field of a definition record is guarded by an equality test only | probed |
| `SET 1 2`, `setFromList (LIST 1, 2)` and the other set functions | the same error | probed (`SET`); keel (`setFromList`) |
| record update `z WITH a IS 5` on a variable `z` | type error, "You are trying to apply z (predefined) of type P"; the main build 1.6.108 gives the same error; the constructor form `P WITH a IS 5, b IS 2` is accepted | probed on both builds |
| `7.5 MODULO 2` | runtime error, "Expected an Integer but got the fractional number"; so `MODULO` is used on whole numbers only (`(Day date) MODULO 7`) | probed |
| `TYPICALLY 3` on a `GIVEN` | parse error at the next token | probed; keel (on a record field) |
| a `GIVEN` at section level, after a `§` line | not usable: my probe could not tell the construct from a mistake in its own syntax, so this row rests on the keel | keel, not re-probed |
| `NOT x AND FALSE` | accepted, and means `NOT (x AND FALSE)`; every `NOT` in these modules is bracketed | probed; keel |
| `JUST p's a` | read as `JUST p` applied to `'s a`: type error; write `JUST (p's a)` | probed |
| a second line on an `#ASSERT` | parse error at the next line's first word; each `#ASSERT` is on one line | probed; the brief |
| a `#TRACE` outcome inside `#ASSERT`, as `#ASSERT (r AT 0 WITH PARTY ... DOES ... AT 0) EQUALS FULFILLED` | parse error at `AT`; `#TRACE` is a directive that prints, not an expression, so the outcome of a regulative rule is not asserted; each of the eight (ss 123(2), 123(3)(a), 123(3)(b), 123(4)(a), 123(4)(b), 139(4), 140(1), 140(2)) is run with `#TRACE` and has a decision-function twin whose answers are asserted | probed |
| `Date 31 2 2026` | accepted, and answers 3 March 2026: `Date` rolls an impossible date forward and does not refuse it | probed |

Where a skill describes one of these as available, the binary governed and the rule was written another way.

## What check.sh prints (ssc5)

Run from the deposit folder with the stable binary as `L4` and the main build as `L4_MAIN`; it exited 0.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc5-cases-seat.l4                             0       146       0        0         0 |      0       146       0        0  same
ssc5-logic.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-part10.l4                                 0         0       0        0         0 |      0         0       0        0  same
ssc5-part6.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-part7.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-part8.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-part9.l4                                  0         0       0        0         0 |      0         0       0        0  same
ssc5-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc5-tests-logic.l4                            0        32       0        0         0 |      0        32       0        0  same
ssc5-tests-part10.l4                           0       102       0        0         0 |      0       102       0        0  same
ssc5-tests-part6.l4                            0       249       0        0         0 |      0       249       0        0  same
ssc5-tests-part7.l4                            0       220       0        0         0 |      0       220       0        0  same
ssc5-tests-part8.l4                            0       155       0        0         0 |      0       155       0        0  same
ssc5-tests-part9.l4                            0       134       0        0         0 |      0       134       0        0  same
TOTAL (15 modules)                             0      1038       0        0           |      0      1038       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Baseline numbers it replaced: I did not capture a run before writing the modules.
Inferred, not measured: the sandbox held only `ssc-core.l4`, so the baseline was one module with 0 errors and 0 assertions, which is the `ssc-core.l4` row above (unchanged).
Now: 15 modules, 0 errors, 1038 assertions satisfied, 0 failed, 0 refused, and the main build gives the same four counts on every module.

The quotation gate, run when this file was generated, with the text file as the source:

- `srcrefs.py check --refs`: srcrefs check: 475 src: lines, 232 runs, 232 locators, 0 problems
- `srcrefs.py check --strict`: srcrefs check: 475 src: lines, 232 runs, 232 locators, 0 problems

Both gates cover every `ssc5-*.l4` file, tests and seat included.
`check.sh` and the gates were last run after the last edit to any `.l4` file in the deposit.
