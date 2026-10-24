# Telecommunications (Consumer Protection and Service Standards) Act 1999 — customer baseline

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; the one question that can reach a gap answers `not covered`, and a test asserts it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0076` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep. No scenario raised it; every case is hypothetical.

## Edition

**Compilation No. 45**, compilation date 31 October 2025, includes amendments up to Act No. 50, 2025, as deposited at `../../registers/source-bundle/C2004A00441.txt`.

No instrument is brought in. The Act hands most of the detail a customer wants to instruments that are not deposited: the ACMA's customer service guarantee standard and scale of damages (ss 115, 117), the Minister's USO performance standards and benchmarks (ss 12EB–12EE), the s 9(2D) and s 9(3) determinations, any s 8J declaration or s 12A determination, the ACMA's s 147 emergency call services determination, and the regulations under ss 6(1)(c) and 9E. Each is asked as a fact where a question needs it.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `tcpss-customer.l4` | `tcpss-cases-customer.l4` | 49 written, 49 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The phone customer**: a residential customer, a small business or a charity, and an end-user of a carriage service. The questions are the customer's: "Am I entitled to a phone line, from whom, with what equipment?", "Must my provider offer untimed local calls, and can it switch me to timed?", "My connection or repair was late: am I owed damages, how much, and by when must it decide and pay, or I sue?", "Can I be made to waive the guarantee?", "Must my provider be in the Ombudsman scheme, and can the Ombudsman take my complaint?".

Provisions addressed to the Minister (ss 8J, 9(2D), 9(3), 12A), the ACMA (ss 115, 117, 120, 129–131) or the provider (ss 104, 105, 116, 117A, 128) are encoded as what they mean for the customer.

The 2026-10-18 defaults:

- **The Act alone.** No instrument is deposited; each is asked as a fact (for the guarantee, whether the standard was breached and what the scale sets).
- **The actors the text names:** the customer (and end-user), the carriage service provider, the carrier, the primary universal service provider (Telstra under s 12D), the Minister, the ACMA, the Telecommunications Industry Ombudsman.
- **Judgments handed to others are answered conditionally:** the Minister's determinations and declaration, the ACMA's exemption or direction, and the ACMA standard's periods (as "your provider contravened a standard").
- **The Act's own definitions are worked out from facts:** eligible local call (s 106), eligible customer (s 110), eligible carriage service provider (s 127), the equipment that comes with a standard telephone service (ss 6, 9E). Standard zone (s 108) and the applicable zone (s 109) are asked as facts, because they turn on how Telecom charged calls before 1 July 1991 and on providers' notices to the ACMA. Borrowed terms from the Telecommunications Act 1997 (carrier, carriage service provider, residential customer, public mobile telecommunications service) are asked as facts.
- **One case:** one customer and one service.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** Part 2's contracts, grants and levy (ss 13–74), the Regional Broadband Scheme (Part 4), the Ombudsman scheme's reviews and register, the RTIRC (Part 9B), s 160.

## Scope

**In:** ss 6(1)(a)–(b), 9(1)(a), (2), (2AAA), (2C), (2E), (4), (6), 9E(1), 12A (as a fact), 12C, 12D(1); Part 3 ss 104, 105, 106, 108–110 (zones as facts); Part 5 ss 114, 115(2), 116, 117(3), 117A(1), (3)–(5), 120, 120A; Part 6 ss 127, 128(1), (4)–(7), 129–131 (as facts).

**Out:** payphones (ss 9(1)(b), 9C, 12ED–12EI; the location and removal rules are not deposited); ss 6(1)(c), 9E(1)(c)–(d), 9E(2) (regulations); s 107 (customers outside standard zones: the regulations' scheme); s 112 (pre-1997 contracts); ss 12EB–12EE (the Minister's USO standards: not deposited); Part 5 Division 3 (wholesale), ss 117B–117F, 118, 118A, 119; Part 8 (emergency call services: the duties are in the ACMA's determination, not deposited); Part 9 (price control).

## What the Act turns out to say

1. **The Act does not guarantee broadband.** The universal service obligation in s 9 is about standard telephone services and payphones. A standard telephone service is voice telephony (or an equivalent for a person with a disability), plus any purpose the regulations declare, such as data (s 6(1)(c), (3)); none is deposited. Broadband for premises is the statutory infrastructure provider regime in Part 19 of the Telecommunications Act 1997, which this Act mentions only for the Ombudsman (s 128(5A)) and the ACMA's choices (ss 129–131). The ledger question's "broadband under the universal service guarantee" is therefore answered as not this Act; REQ-0092 names Part 19. Not asserted.
2. **The obligation is to supply on request, and the Minister can switch it off.** Section 9(2) makes the obligation one to supply "on request". It does not arise for a request that fails the Minister's s 9(2D) requirements, in circumstances the Minister excludes under s 9(3), or at all after a s 8J declaration of satisfactory alternative contractual arrangements survives disallowance (s 9(2AAA)). Asserted.
3. **Telstra is the provider by default.** Section 12D(1) deems the Minister to have determined Telstra the primary universal service provider for all of Australia except areas where another provider is determined; where two or more are determined, each bears the obligation and any one may discharge it (s 12C(2)). Asserted.
4. **The equipment is a basic handset, or what disability law requires, and the customer may hire it.** Unless the regulations prescribe other equipment, supply includes "a telephone handset that does not have switching functions" (s 9E(1)(b)), or other equipment the Disability Discrimination Act 1992 requires; the customer must be given the option of hiring it (s 9(6)) and may decline it (s 9(4)). Asserted.
5. **Untimed local calls depend on a 1991 map.** The customer must be in a standard zone (an area Telecom charged untimed before 1 July 1991, s 108), and the call must be of a kind a general carrier supplied untimed before 20 September 1996, or be on a service supplied under the universal service obligation (s 106). For a business the call must also be a voice call; for a household or charity it need not (s 106(1)–(2)). A call involving a mobile or satellite service that is not a universal service is never an eligible local call. Asserted.
6. **Once chosen, untimed charging sticks until the customer consents in writing to something else** (s 105(1)(b), (d)(ii)); a customer who did not choose it may ask for it by written notice at any time, effective from "the earliest practicable period" after the provider receives it (s 105(1)(c)–(d)). That period is not a date the Act fixes, so it is answered in words. Asserted.
7. **The guarantee's damages are a fixed scale, not proof of loss, and are reduced by any other credit for the same event.** The amount is "equal to the relevant amount specified in the scale" (s 116(2)), at most $25,000 a category (s 117(3)), and "damages includes punitive damages" (s 114). A credit or payment under another right arising out of the same event reduces it, not below zero (s 116(3)). The customer may sue within 2 years (s 116(6)); a breach is not an offence (s 122). Asserted, on hypothetical scale amounts.
8. **The provider has 14 days to decide and 14 weeks to pay.** From when it first has reason to believe it is likely to be liable, the provider must decide within 14 days whether to accept liability (s 117A(1)); it must then pay or credit, or notify a refusal in writing, within 14 weeks after the decision (s 117A(3)–(5)). Asserted.
9. **A universal service phone line's guarantee cannot be waived; any other service's can, and a provider may insist on it.** Section 120(7) bars a waiver for a standard telephone service supplied under the USO; s 120A lets a provider supply any other service on condition of a waiver, which must follow the ACMA's rules and form and cannot be in the standard form of agreement (s 120(3)–(6)). The waiver instrument is not deposited. Asserted.
10. **Every carrier, and every provider of a home or small-business phone, a mobile or internet access, must be in the Ombudsman scheme** unless exempted (ss 127, 128(1), 129); the scheme must deal with complaints about carriage services, including billing, but not about the level of prices or content (s 128(4)–(6)); and the provider may not charge the end-user for a complaint (s 128(4A)). Asserted.

## What would need doing before this is worth relying on

- **The customer service guarantee standard and scale of damages** (REQ-0090), so the periods and amounts are computed rather than asked.
- **The emergency call services determination** (REQ-0091): the Act states free access to Triple Zero only as an objective (s 147(2)(a)).
- **Part 19 of the Telecommunications Act 1997** for broadband (REQ-0092).
- **The Minister's USO instruments** (ss 9(2D), 9(3), 12EB–12EE) and any s 8J declaration, and the regulations under ss 6 and 9E.
- **A register of standard zones** and providers' nominated areas, so a customer can be told whether their calls are eligible local calls.
- **Case law and the Ombudsman's practice** were not read.

## The customer service guarantee Standard brought in (added 2026-10-23, REQ-0090)

**Module:** `tcpss-csg-standard.l4`, beside `tcpss-customer.l4`, which it imports; cases in `tcpss-cases-csg-standard.l4` (39 assertions written, 39 satisfied; 3 `#TRACE` runs: the connection duty met (FULFILLED), a repair 3 days late (BREACH), the oral-waiver statement in time (FULFILLED); `l4 run` 0 errors, 0 warnings; `tcpss-cases-customer.l4` still 49 of 49). Seat: the phone customer.

**Instrument:** the Telecommunications (Customer Service Guarantee) Standard 2023, Compilation No. 1 (F2026C00929, compilation date 19 August 2026), deposited at `subjects/au/telecommunications-customer-service-guarantee-standard-2023/` with `parent_act` this Act. It is one instrument made under ss 115, 117 and 120 together: the performance standards (Part 2), the exemptions (Part 3), the scale of damages (Part 4 and Schedule 2) and the waiver rules (Part 5).

**What the module computes:** the guaranteed connection period (s 11, Schedule 1) and repair period (ss 14, 15) in business days; whether a delay is a contravention, after arrangements (ss 12, 17), interim service (Schedule 2 item 101(2)) and the exemptions (ss 10, 21–24, 31); the scale amount for the delay (Schedule 2 items 201–204) and for a missed appointment (ss 19, 20, item 205); the damages owed, through the Act's own `How much guarantee damages must my provider pay` (s 116(2)–(3)) and liability through `Am I owed damages under the customer service guarantee` (s 116(1)); when a waiver takes effect (ss 33, 34); which Standard governs by date (s 39). The provider's duties (ss 11(3), 14(5), 19(5), 26(2)(b), 34(7)) are written as regulative rules with their business-day deadlines.

17. **The scale is a two-step daily rate in business days.** For a late connection or repair: $14.52 a business day (residential or charity) or $24.20 (business) for the first 5 business days, then $48.40 a day for everyone. A single late call-handling feature attracts half: $7.26 or $12.10, then $24.20. A missed appointment is $14.52 or $24.20, but only on a day for which no delay damages are payable. The amounts are far under the s 117(3) ceiling of $25,000. Asserted.
18. **The periods are business days, counted from receipt, and depend on the ABS's urban centres and localities.** Connection: 2 business days for an in-place connection, 5 in an urban centre of 10 000 or more, 10 for 2 501–9 999, 15 elsewhere, and 20 wherever the site is not close to a facility with capacity. Repair: by the end of the first full business day in a large urban centre, 2 in smaller centres and localities over 200, 3 elsewhere, 1 anywhere if no plant work or visit is needed. A request after 5 pm counts from the next business day (s 6(2)). The module takes counts of business days from the customer and never converts calendar dates. Asserted.
19. **An exemption for circumstances beyond the provider's control is lost if the customer is not told in time.** Section 25(2) makes the s 24 exemption "taken never to have applied" unless the provider gives the s 26 statement (within 10 business days, or 14 weeks for access or legal obstacles) or the s 27 general notice. Asserted (a storm-damage repair 3 days late is a contravention worth $43.56 without the notice).
20. **An oral waiver does not bite for 5 business days.** A written waiver takes effect on the day of consent; an oral one 5 business days later unless withdrawn, and the provider must send a written statement within 3 business days (s 34(7), (8)). A universal service line still cannot be waived (s 33; Act s 120(7)). Asserted.
21. **Contraventions that began before 31 August 2023 are under the 2011 Standard** (s 39), which is not deposited; the module says so rather than applying the 2023 figures.
