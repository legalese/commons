# Water Industry Act 1991: expectations written by an independent tester

These were written from BRIEF.md and the source text in `../registers/source-bundle/ukpga-1991-56.txt` only (ss 45-51, 61-63A, 106, 144-144B and Schedule 4A). No `.l4` file was opened before this file was saved.

Calendar facts used (2026 unless stated). 1 Jan 2026 is a Thursday. Easter Sunday is 5 Apr 2026, so Good Friday is Fri 3 Apr. The bank holidays in England and Wales are 1 Jan, 6 Apr (Easter Monday), 4 May, 25 May, 31 Aug and 28 Dec (the substitute for Boxing Day). Christmas Day, Fri 25 Dec 2026, is disregarded by s 144(7)(b) itself. 2028 is a leap year.

"WD+2(d)" means the second working day after day d (the brief's day-level reading of "two working days").

## Goal 1: Connections

The rules for this goal are ss 45(1)-(2), 47(1)-(3), 48(1), 51(1)-(3) and (6), and 106(3)-(4).

| # | Facts | Expected | Source |
|---|---|---|---|
| C1 | Premises are an existing building, the supply is for domestic purposes, the main is an ordinary distribution main, no conditions were imposed, and the pipe is laid | duty to connect arises: TRUE | s 45(1)(a), (2)(a)-(b) |
| C2 | As C1 but the premises are land on which someone proposes to erect a building | TRUE | s 45(1)(b) "premises on which any person is proposing to erect any building" |
| C3 | As C1 but the main is a trunk main | FALSE | s 45(2)(a) "neither a trunk main nor..." |
| C4 | As C1 but the main is used solely for non-domestic supply | FALSE | s 45(2)(a) "...nor a water main which is or is to be used solely for the purpose of supplying water otherwise than for domestic purposes" |
| C5 | As C1 but the supply is not for domestic purposes | FALSE | s 45(1) "for the purpose of providing a supply of water for domestic purposes" |
| C6 | As C1 but a condition was imposed and has not been satisfied | FALSE | s 45(2)(b) "such conditions ... have been satisfied" |
| C7 | As C1 but the customer's part of the service pipe was not laid when the notice was served and still has not been laid | FALSE (the duty has not yet arisen) | s 51(3) "shall not arise by virtue of that notice until the person serving the notice ... has ... laid" |
| C8 | Connection notice served Sun 1 Feb 2026. Condition counter-notice on 14 Feb | in time: TRUE | s 47(3) "before the end of the period of fourteen days beginning with the day after the service": the period is 2 Feb to 15 Feb |
| C9 | Same notice. Counter-notice on 15 Feb (service + 14) | TRUE | as above |
| C10 | Same notice. Counter-notice on 16 Feb | FALSE | as above |
| C11 | Notice served 20 Feb 2026 (not a leap year). Last day for a counter-notice | 6 Mar 2026 | s 47(3) |
| C12 | Notice served 20 Feb 2028 (leap year). Last day for a counter-notice | 5 Mar 2028 | s 47(3) |
| C13 | Notice served 2 Mar 2026, no pipe-laid notice, no conditions. Relevant day | 3 Mar 2026 | s 51(6) "the day after whichever is the latest of" (a) the notice |
| C14 | As C13, with the pipe already laid. Last day to connect | 16 Mar 2026 (3 Mar + 13) | s 51(1)(b) "before the end of the period of fourteen days beginning with the relevant day" |
| C15 | Notice served 2 Mar 2026, conditions satisfied 10 Mar 2026, pipe laid. Relevant day, then last day | 11 Mar 2026, then 24 Mar 2026 | s 51(6)(c), (1)(b) |
| C16 | Notice served 20 Feb 2026, pipe-laid notice 28 Feb 2026, no conditions, pipe not laid when the notice was served. Relevant day, then presumed last day | 1 Mar 2026, then 21 Mar 2026 (R + 20) | s 51(6)(b), (2) "the period of twenty-one days beginning with the relevant day" |
| C17 | Notice served 28 Feb 2028 (leap year), pipe laid. Relevant day, then last day | 29 Feb 2028, then 13 Mar 2028 | s 51(6), (1)(b) |
| C18 | Notice served 31 Dec 2026, pipe laid. Relevant day, then last day | 1 Jan 2027, then 14 Jan 2027 | s 51(6), (1)(b) |
| C19 | Deposit of £100.30 at a rate of 1% for each 50p for each three months, held 1 Jan 2026 to 15 Aug 2026 | 200 complete 50p sums and 2 complete three-month periods, so £100 x 1% x 2 = £2.00 | s 48(1) "on every sum of 50p so deposited for every three months during which it remains in the hands of the undertaker" |
| C20 | £100.00 deposited 1 Jan 2026 and repaid 31 Mar 2026 | £0 (three months from 1 Jan run to 1 Apr) | s 48(1) |
| C21 | £100.00 deposited 1 Jan 2026 and repaid 1 Apr 2026 | £1.00 (one complete period) | s 48(1) |
| C22 | £0.40 deposited for a year | £0 (no complete 50p sum) | s 48(1) "every sum of 50p" |
| C23 | Sewerage undertaker receives a s 106(3) notice on 10 Feb 2026. Last day it can refuse | 3 Mar 2026 (10 Feb + 21) | s 106(4) "At any time within twenty-one days after a sewerage undertaker receives a notice" |
| C24 | As C23. Refusal on 3 Mar, on 4 Mar, and on 10 Feb (the day of receipt) | TRUE, FALSE, TRUE | s 106(4) |
| C25 | Notice received 10 Feb 2028 (leap year). Last day to refuse | 2 Mar 2028 | s 106(4) |

## Goal 2: Disconnection for non-payment

The rules for this goal are s 61(1), (1ZA), (1A), (2)-(3), s 63(3), s 63A(1) and Schedule 4A.

| # | Facts | Expected | Source |
|---|---|---|---|
| D1 | A private dwelling-house occupied as someone's only or principal home | protected (Schedule 4A): TRUE | Sch 4A para 1(1) |
| D2 | A dwelling that is a holiday home, nobody's only or principal home | FALSE | para 1(1) "occupied by a person as his only or principal home" |
| D3 | A hospital; a school; a prison; police premises | TRUE each | Sch 4A paras 4, 11, 15, 16 |
| D4 | A shop or office | FALSE | not listed |
| D5 | An HMO in which someone has their only or principal home / in which nobody does | TRUE / FALSE | para 2(1) |
| D6 | Notice requiring payment served Mon 2 Mar 2026. Last day to pay in time; earliest cut-off day | 9 Mar 2026; 10 Mar 2026 | s 61(1ZA)(b) "before the end of the period of seven days beginning with the day after he is served" |
| D7 | Notice served 23 Feb 2026. Earliest cut-off day | 3 Mar 2026 | s 61(1ZA)(b) |
| D8 | Notice served 23 Feb 2028 (leap year). Earliest cut-off day | 2 Mar 2028 | s 61(1ZA)(b) |
| D9 | Notice served 28 Dec 2026. Earliest cut-off day | 5 Jan 2027 | s 61(1ZA)(b) |
| D10 | Shop, notice 2 Mar 2026, not paid, no counter-notice, cut off 9 Mar / 10 Mar / 11 Mar | lawful FALSE / TRUE / TRUE | s 61(1), (1ZA) |
| D11 | As D10, cut off on 9 Mar: is it an offence? | TRUE | s 63(3)(a) "in a case in which it has no power to do so" |
| D12 | As D10, cut off on 10 Mar: offence? | FALSE | s 63(3)(a) |
| D13 | Shop, notice 2 Mar, paid 9 Mar, cut off 12 Mar | lawful FALSE; offence TRUE | s 61(1ZA)(b) payment was in time |
| D14 | Shop, notice 2 Mar, paid late on 11 Mar, cut off 12 Mar | lawful FALSE: by the cut-off day nothing is still due, so the occupier no longer "is liable ... to pay charges due" under (1ZA)(a). Low confidence: on the brief's reading, (1ZA)(b) is met by the late payment alone | s 61(1ZA)(a) present tense |
| D15 | Principal-home dwelling, notice 2 Mar, not paid, cut off 20 Mar | lawful FALSE; offence TRUE | s 61(1A), s 63(3)(a) |
| D16 | Shop, counter-notice disputing liability on 5 Mar, no judgment and no settlement agreement in breach, cut off 20 Mar | lawful FALSE; offence TRUE | s 61(2) |
| D17 | As D16 but a judgment for the charges is enforceable | lawful TRUE | s 61(2), (3)(a) |
| D18 | As D16 but the occupier is in breach of a settlement agreement made since the counter-notice | lawful TRUE | s 61(3)(b) |
| D19 | Counter-notice on 9 Mar (the last day of the seven) | it takes effect, so a cut-off on 20 Mar is unlawful | s 61(2)(b) "within the period of seven days" |
| D20 | Counter-notice on 10 Mar (too late), cut off 20 Mar | it has no effect, so the cut-off is lawful | s 61(2)(b) |
| D21 | Counter-notice on 2 Mar, the day the notice itself was served | Literally the period is 3-9 Mar, so the counter-notice is not "within" it and the cut-off is lawful. Low confidence: a purposive reading would let it count | s 61(2)(b) |
| D22 | Limiting device on a principal-home dwelling, used to enforce payment | offence TRUE | s 63A(1) |
| D23 | Limiting device on a shop, used to enforce payment | FALSE | s 63A(1) "premises specified in Schedule 4A" |
| D24 | Limiting device on a principal-home dwelling, not used to enforce payment | FALSE | s 63A(1) "with the intention of enforcing payment" |

## Goal 3: Charges

The rules for this goal are s 144(2)-(7), s 144A(1)-(3) and (5)-(7), and s 144B(1)-(3).

| # | Facts | Expected | Source |
|---|---|---|---|
| H1 | Informed the undertaker Fri 16 Oct 2026; ceased to occupy Tue 20 Oct 2026 (WD+2 = 20 Oct) | informed in time, so not liable after leaving | s 144(3)(a) "at least two working days before" |
| H2 | Informed Fri 16 Oct; ceased Mon 19 Oct | late, so can still be charged | s 144(3)(a) |
| H3 | Informed Thu 2 Apr 2026 (Easter); ceased Tue 7 Apr / Wed 8 Apr | late / in time. Good Friday 3 Apr and Easter Monday 6 Apr are disregarded, so WD+2 = 8 Apr | s 144(7) |
| H4 | Informed Wed 1 Apr 2026; ceased Tue 7 Apr | in time (WD+2 = 7 Apr) | s 144(7) |
| H5 | Informed Thu 24 Dec 2026; ceased Tue 29 Dec / Wed 30 Dec | late / in time. 25 Dec, the weekend and 28 Dec are disregarded | s 144(7)(b) |
| H6 | Informed Fri 22 May 2026; ceased Wed 27 May / Tue 26 May | in time / late (25 May is a bank holiday) | s 144(7) |
| H7 | Informed Fri 28 Aug 2026; ceased Wed 2 Sep | in time (31 Aug is a bank holiday) | s 144(7) |
| H8 | Informed Wed 31 Dec 2025; ceased Mon 5 Jan 2026 / Fri 2 Jan 2026 | in time / late (1 Jan is a bank holiday) | s 144(7) |
| H9 | Informed Sat 17 Oct 2026; ceased Tue 20 Oct | **Differs from the brief.** The 48 hours, after disregarding Saturday and Sunday, run from 00:00 Mon 19 Oct to 24:00 Tue 20 Oct. Any time on 20 Oct is less than 48 hours, so the occupier is late and can still be charged. The brief's day rule (cease on or after WD+2 = 20 Oct) gives "in time" | s 144(3)(a), (7) "a period of forty-eight hours calculated after disregarding any time falling on a Saturday or Sunday" |
| H10 | Informed Sat 17 Oct; ceased Wed 21 Oct | in time | as above |
| H11 | Charges unmeasured (not fixed by volume); informed late | cannot be charged after leaving | s 144(2) "fixed ... by reference to volume" |
| H12 | Ceased 10 Jul 2026, informed 9 Jul (late), meter normally read 30 Sep, no new occupier. Last day of liability | 6 Aug 2026 (9 Jul + 28) | s 144(4)(a), (3)(b) |
| H13 | As H12 but a new occupier informs the undertaker on 20 Jul | 20 Jul 2026 | s 144(4)(c) "whichever ... first occurs" |
| H14 | As H12 but the meter is normally read on 1 Aug | 1 Aug 2026 | s 144(4)(b) |
| H15 | Ceased 10 Jul 2026, informed after leaving on 15 Jul, no other events | 12 Aug 2026 | s 144(4)(a) "or at any time after" |
| H16 | Ceased 30 Jan 2026, informed 31 Jan 2026 | 28 Feb 2026 | s 144(4)(a) |
| H17 | Ceased 31 Jan 2028, informed 1 Feb 2028 | 29 Feb 2028 (leap year) | s 144(4)(a) |
| H18 | Never informed; ceased 10 Jul; meter normally read 1 Jul (before leaving) and 30 Sep | 30 Sep 2026. The 1 Jul reading came before he ceased, so it does not count | s 144(4) "first occurs after he ceases to occupy" |
| H19 | s 62 notice served Mon 19 Oct 2026, expiring the same day | no longer liable after Wed 21 Oct 2026 | s 144(6) "the later of (a) the expiry ... (b) the end of the period of two working days beginning with the service" |
| H20 | s 62 notice served Thu 2 Apr 2026, expiring 3 Apr | 8 Apr 2026 | s 144(6)(b), (7) |
| H21 | s 62 notice served Thu 2 Apr 2026, expiring 30 Apr | 30 Apr 2026 | s 144(6)(a) is later |
| H22 | s 62 notice served Thu 24 Dec 2026, expiring 24 Dec | 30 Dec 2026 | s 144(6)(b), (7) |
| M1 | Someone has their home there and charges are unmeasured | may require charging by volume: TRUE | s 144A(1) |
| M2 | Nobody has their home there / charges are already measured | FALSE / FALSE | s 144A(1)(a), (b) |
| M3 | Notice given; volume charging is practicable at reasonable expense | must give effect: TRUE | s 144A(2) |
| M4 | Not reasonably practicable / unreasonable expense | FALSE / FALSE | s 144A(3)(a), (b) |
| M5 | Measured charging began 15 Mar 2026. Last day to revoke | 14 Mar 2027 | s 144A(5) "twelve months beginning with the day" |
| M6 | Began 1 Mar 2027 | 29 Feb 2028 | s 144A(5) |
| M7 | Began 29 Feb 2028 | 28 Feb 2029 | s 144A(5); there is no 29 Feb 2029 |
| M8 | Began 1 Jan 2026 | 31 Dec 2026 | s 144A(5) |
| M9 | The giver had no previous notice and is still the consumer; revokes on 14 Mar 2027 (measured from 15 Mar 2026) / on 15 Mar 2027 | TRUE / FALSE | s 144A(5), (6) |
| M10 | The giver had a previous notice | cannot revoke | s 144A(6)(a) |
| M11 | The giver has ceased to be the consumer; neither the giver nor the new consumer had a previous notice; the occupiers remain | can revoke | s 144A(7) |
| M12 | As M11 but an earlier occupier has left | cannot revoke | s 144A(7)(c) |
| B1 | Home, previously unmeasured, no notice, no consent, no change of occupation | may not move to metered charges | s 144B(2) |
| B2 | Measured charges notice given and not revoked | may | s 144B(2)(a)(i) |
| B3 | Consent given and not revoked | may | s 144B(2)(a)(ii) |
| B4 | Notice given but later revoked | may not | s 144B(2)(a)(i) "which has not been revoked" |
| B5 | Change of occupation, no charges yet demanded from the new consumer | may | s 144B(2)(b) |
| B6 | Change of occupation, but charges already demanded | may not | s 144B(2)(b) |
| B7 | "Change" in which one earlier occupier stays on | may not; this is not a change of occupation | s 144B(3) |
| B8 | Nobody has their home there | the restriction does not apply, so it may | s 144B(1)(a) |
