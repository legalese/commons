# Independent expectations: Third Parties (Rights against Insurers) Act 2010

Written from BRIEF.md and the source text (revised, PIT 4 January 2024) only, before any `.l4` module was opened.

## Readings adopted

- **R1 (route, from the brief).** Route (a) in s 1(1) applies if the insured is a relevant person on or before the day the liability is incurred (event day <= liability day). Route (b) applies if the liability was incurred first (liability day < event day). On the same day, it is route (a).
- **R2 ((b)-only events).** A debt relief order (s 4(1)(d), 4(3)(ba)) and dying insolvent (s 5(1)) make the person a relevant person "for the purposes of section 1(1)(b) only". So if the liability is incurred on or after that event day (route (a) under R1), nothing transfers.
- **R3 (28 days).** "The period of 28 days beginning with the day of receipt" ends on receipt + 27 (the brief). No working-day roll.
- **R4 (s 10 and s 14).** The amount recoverable from the insurer under s 14(1) is the s 8 amount less the s 10 set-off. The set-off reduces what the insurer pays the third party, so the third party may enforce the remainder against the insured. (Ambiguity: one could argue the set-off is an amount "recoverable" in substance because it discharges the insured's own debt; the Act's words "amount recoverable from the insurer by virtue of the transfer" favour the net figure.)
- **R5 (s 14(6)-(7)).** Recoverable = net transferred amount, less the shortfall from the insurer's shortage of assets (only where the insurer is a relevant person, and, if the third party is FSCS-eligible, only if it made the claim), less the shortfall caused by a fund limit; then, where the third party is FSCS-eligible, plus the amount paid or due under the FSCS claim. Ambiguity: whether the FSCS amount is added on top or just caps the exclusion; I read (7)(b) as "treated as being able to recover from the insurer" that amount, so it is added back.
- **R6 (s 9(3)).** Not bound only if the condition "cannot be fulfilled because" the insured is a dead individual / dissolved body corporate / dissolved unincorporated non-partnership. Restoration after dissolution does not matter (s 9(8)(b)). A dissolved partnership that is an unincorporated body does not qualify.
- **R7 (s 9(4)).** A condition to notify the insurer of the existence of a claim is not an "information or assistance" condition, so s 9(3) does not relieve it; it binds.
- **R8 (s 9(5)-(6)).** Pay-to-be-paid condition does not bind, except for marine insurance where the liability is not for death or personal injury.
- **R9 (s 1(3)-(4)).** May enforce only if both existence and amount are established, by declaration/declarator, judgment/decree, arbitral award, or enforceable agreement. Proceedings may be brought before that.
- **R10 (Sch 3 para 3).** If the 1930 Act continues to apply (input flag), this Act's s 1 does not transfer.
- **R11 (s 15).** If the liability is itself an insurer's liability under a contract of insurance (reinsurance), no transfer.

## Scenarios

Dates below: E = event day, L = liability day.

### Goal 1: transfer of rights

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| T1 | Bankruptcy order (4(1)(f)) E 1 Mar 2024, L 1 Feb 2024, insured | transfers, route (b) | s 1(1)(b) "a person who is subject to such a liability becomes a relevant person" |
| T2 | Bankruptcy order E 1 Mar 2024, L 10 Mar 2024 | transfers, route (a) | s 1(1)(a) "a relevant person incurs a liability" |
| T3 | Bankruptcy order E = L = 1 Mar 2024 | transfers, route (a) | brief: same day is (a) |
| T4 | Compulsory winding-up (6(2)(f)) E 1 Jun 2024, L 31 May 2024 | transfers, route (b) | s 1(1)(b) |
| T5 | Administration (6(2)(b)) E = L | transfers, route (a) | s 1(1)(a) |
| T6 | DRO (4(1)(d)) E 1 Mar 2024, L 1 Feb 2024 | transfers (route (b)) | s 4(4) "for the purposes of section 1(1)(b) only" |
| T7 | DRO E 1 Mar 2024, L 2 Mar 2024 | no transfer | s 4(4) |
| T8 | DRO E = L = 1 Mar 2024 | no transfer (same day is route (a)) | s 4(4) + brief |
| T9 | NI DRO (4(3)(ba)) E 1 Mar 2024, L 2 Mar 2024 | no transfer | s 4(4) |
| T10 | NI DRO E 1 Mar 2024, L 28 Feb 2024 | transfers | s 4(4) |
| T11 | Died insolvent (s 5) E 10 Jan 2025, L 1 Jan 2025 | transfers | s 5(1) |
| T12 | Died insolvent E = L | no transfer | s 5(1) "for the purposes of section 1(1)(b) only" |
| T13 | Died insolvent E 10 Jan 2025, L 11 Jan 2025 | no transfer | s 5(1) |
| T14 | Dissolved body corporate (6A(1)), not restored, L before E | transfers | s 6A(1) |
| T15 | Dissolved body, since restored (6A(2)) | no transfer | s 6A(2) "treated as not having been dissolved" |
| T16 | Dissolved partnership that is not a body corporate | no transfer | s 6A(3) |
| T17 | Dissolved partnership that is a body corporate (LLP), not restored | transfers | s 6A(3) |
| T18 | Dissolved unincorporated non-partnership body, not restored | transfers | s 6A(1) |
| T19 | Sanctioned compromise (6(1)); liability transferred to another body by the sanctioning order | no transfer | s 6(5) |
| T20 | Sanctioned compromise, liability kept, third party bound | transfers | s 6(1), 6(6) |
| T21 | Sanctioned compromise, liability kept, third party not bound | no transfer | s 6(6) "only to a person on whom the compromise ... is binding" |
| T22 | Bankruptcy order, reinsurance liability (insurer's liability under a contract of insurance) | no transfer | s 15 |
| T23 | Bankruptcy order, 1930 Act case flag | no transfer under 2010 Act | Sch 3 para 3 |
| T24 | Bankruptcy order, not insured against the liability | no transfer | s 1(1)(a) "against which that person is insured" |
| T25 | Bankruptcy order, liability incurred voluntarily | transfers | s 16 |
| T26 | Scottish sequestration (4(2)(a)) E 1 Jan 2024, L 31 Dec 2023 | transfers, route (b) | s 1(1)(b) |
| T27 | Voluntary winding-up (6(2)(d)) E 29 Feb 2028, L 28 Feb 2028 | transfers route (b) | s 1(1)(b) |

### Goal 2: recovery and enforcement

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| R1 | Liability 100,000; insurer's liability to insured 150,000 | transferred 100,000 | s 8 "no rights are transferred ... in respect of the difference" |
| R2 | Liability 100,000; insurer 60,000 | transferred 60,000; enforceable vs insured 40,000 | s 8, s 14(1) |
| R3 | Liability = insurer = 50,000 | transferred 50,000; vs insured 0 | s 14(1) "only to the extent (if any)" |
| R4 | Liability 100,000; insurer 150,000; set-off 10,000 | from insurer 90,000; vs insured 10,000 | s 10(2), R4 |
| R5 | Liability 100,000; insurer 60,000; set-off 5,000 | from insurer 55,000; vs insured 45,000 | s 8, 10, 14 |
| R6 | Liability 100,000; insurer 100,000; set-off 0; insurer insolvent (relevant person) shortfall 30,000; no FSCS eligibility | recoverable 70,000; vs insured 30,000 | s 14(6)(a) |
| R7 | As R6 but insurer not a relevant person | recoverable 100,000; vs insured 0 | s 14(6)(a) "in a case where the insurer is a relevant person" |
| R8 | As R6 but FSCS-eligible, no claim made | recoverable 100,000; vs insured 0 | s 14(7)(a) "applies only if the third party has made such a claim" |
| R9 | As R6, FSCS-eligible, claim made, FSCS paid 20,000 | recoverable 90,000; vs insured 10,000 | s 14(7)(b) |
| R10 | As R6, FSCS-eligible, claim made, FSCS paid 30,000 | recoverable 100,000; vs insured 0 | s 14(7)(b) |
| R11 | Liability 100,000; insurer 100,000; fund-limit shortfall 25,000 | recoverable 75,000; vs insured 25,000 | s 14(6)(b) |
| R12 | Liability 100,000; insurer 100,000; fund limit 25,000 and FSCS-eligible, no claim | vs insured 25,000 | s 14(6)(b), (7)(a) only gates (6)(a) |
| R13 | Liability 80,000; insurer 50,000; set-off 10,000; fund shortfall 5,000 | recoverable 35,000; vs insured 45,000 | ss 8, 10, 14 |
| R14 | Existence established by judgment, amount established too | may enforce | s 1(3), (4)(b) |
| R15 | Existence established, amount not | may not enforce | s 1(4) "existence and amount are established" |
| R16 | Established by enforceable agreement (both) | may enforce | s 1(4)(d) |
| R17 | Established by arbitral award (both) | may enforce | s 1(4)(c) |
| R18 | Established by declaration under s 2 (both) | may enforce | s 1(4)(a) |
| R19 | Not established at all | may not enforce (may still sue) | s 1(3) |
| R20 | Info/assistance condition; insured a dead individual; cannot fulfil because dead | not bound | s 9(3)(a) |
| R21 | Info/assistance; body corporate dissolved | not bound | s 9(3)(b) |
| R22 | Info/assistance; body corporate dissolved then restored | not bound | s 9(8)(b) |
| R23 | Info/assistance; partnership (unincorporated) dissolved | bound | s 9(3)(c) "other than a partnership" |
| R24 | Info/assistance; unincorporated non-partnership dissolved | not bound | s 9(3)(c) |
| R25 | Info/assistance; individual alive and bankrupt | bound | s 9(3) |
| R26 | Notify-claim condition; insured dead individual | bound | s 9(4) |
| R27 | Prior discharge; non-marine | not bound | s 9(5) |
| R28 | Prior discharge; marine; personal injury | not bound | s 9(6) |
| R29 | Prior discharge; marine; property damage | bound | s 9(6) |
| R30 | Prior discharge; marine; death | not bound | s 9(6) |

### Goal 3: information and disclosure (Sch 1)

| # | Inputs | Expected | Act's words |
|---|---|---|---|
| I1 | A believes B incurred liability to A and B is relevant person | A may give para 1(1) notice to B | para 1(1) |
| I2 | A believes liability incurred, but not that B is a relevant person | no para 1(1) notice | para 1(1)(b) |
| I3 | A believes all of para 1(2)(a)-(d) | may give notice to C | para 1(2) |
| I4 | para 1(2): no belief in transfer (c) | no notice to C | para 1(2)(c) |
| I5 | Receipt 1 Mar 2024 | last day 28 Mar 2024 | para 2(1) |
| I6 | Receipt 2 Feb 2028 | last day 29 Feb 2028 | leap year |
| I7 | Receipt 3 Feb 2028 | last day 1 Mar 2028 | leap year |
| I8 | Receipt 2 Feb 2027 | last day 1 Mar 2027 | non-leap |
| I9 | Receipt 1 Feb 2027 | last day 28 Feb 2027 | |
| I10 | Receipt 15 Dec 2027 | last day 11 Jan 2028 | year end |
| I11 | Receipt 31 Jan 2028 | last day 27 Feb 2028 | month end |
| I12 | Receipt 4 Apr 2026 (Saturday) | last day 1 May 2026 (no working-day roll) | brief |
| I13 | Para 3: proceedings started, body corporate, dissolved, recipient officer before transfer | may require disclosure | para 3(1), (2)(a) |
| I14 | Para 3: proceedings not started | may not | para 3(1)(a) |
| I15 | Para 3: partnership body | may not | para 3(1)(b)(ii) |
| I16 | Para 3: body dissolved then restored | may (still dissolved) | para 3(6)(b) |
| I17 | Para 3: recipient was IP immediately before dissolution | may | para 3(2)(b)(i) |
| I18 | Para 3: recipient neither officer/employee nor IP/OR | may not | para 3(2) |
| I19 | Para 4(3) list: receipt 2 Feb 2028 | last day 29 Feb 2028 | para 4(3) |
| I20 | Para 4(3) list: receipt 31 Dec 2027 | last day 27 Jan 2028 | para 4(3) |
| I21 | Para 3: body not dissolved | may not | para 3(1)(c) |

Total: 27 + 30 + 21 = 78 rows (some may be dropped if the encoding has no input for them).

## Ambiguities noted

1. Same-day liability and event: settled by the brief (route (a)).
2. s 10/s 14 interaction (R4) and FSCS add-back (R5).
3. s 9(6) partial marine liabilities (part PI, part property): "to the extent" suggests a split; not tested.
4. s 21(4): paras 3 and 4 do not extend to Scotland. Not tested unless the encoding has a jurisdiction input.
5. Sch 1 para 1 "reasonably believes": the beliefs are inputs; I do not test their reasonableness.
