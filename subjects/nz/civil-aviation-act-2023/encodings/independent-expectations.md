# Independent expectations: Civil Aviation Act 2023, Part 5 subpart 3 (domestic carriage, delay)

Written from BRIEF.md and the source text (ss 269-283) before any `.l4` file was opened.
Expected values here are fixed; they are not to be changed after the encoding is opened.

## Readings taken where the Act is ambiguous or silent

- **R1 Contract governs, not the actual route** (s 270(1) "according to the contract between the parties"). A diversion outside NZ that was not agreed does not take the carriage out of the subpart.
- **R2 International carriage** (s 270(3)) is decided on the contract as well. A contract with departure and destination in NZ but an agreed stopping place abroad is international under (3)(b) and also fails (1)(b): both routes give "does not apply".
- **R3 s 272(a)** needs a *single flight* whose contracted departure and intended destination are the same. A return trip made of two flights (AKL-WLG, WLG-AKL) is not a single flight: the subpart applies.
- **R4 s 271**: in combined carriage the subpart applies only to the air part. A delay that occurred on the surface leg is outside the subpart; a delay on the air leg is inside it.
- **R5 Defences** (s 274(2), s 276) require the carrier to *prove* the matter. I treat the input as "proved". Any one proven defence → not liable.
- **R6 s 277 cap**: liability = min(damage proved, 10 × sum paid). With a special contract that sets a higher cap, the cap is that higher figure (still not more than damage proved: (1)(a) is the damage itself). A special contract cap *lower* than 10× is a term "limiting a carrier's liability" → unenforceable under s 278(2), so the 10× cap stands.
- **R7 s 279**: where intent or recklessness is proved, the s 277 limits do not apply; the carrier answers for the damage proved (nothing above damage proved can be "damage caused by delay").
- **R8 Sum paid = 0** (s 269: "contract includes an arrangement made without consideration"): literally 10 × 0 = 0, so the cap is 0. This is ambiguous (Parliament may not have meant free carriage to be uncompensable), but I take the literal reading.
- **R9 "2 years after" a date** (s 283(1), s 281(2)): the last day on which proceedings may be brought is the anniversary date two years on (arrival 10 March 2024 → last day 10 March 2026; filing on 11 March 2026 is out of time). Where the start date is 29 February and the anniversary year has no 29 February, the last day is 28 February (the period ends on the last day of that month). This follows the usual NZ calendar-year reckoning; an encoding that returns 1 March would be a defensible alternative but I expect 28 February.
- **R10 s 283(1)(b)**: if the aircraft did not arrive, the date is the *later* of the date it ought to have arrived and the date the carriage stopped. If it did arrive, the arrival date alone is used (the "later of" collapses to (a) because (b) is conditional on non-arrival).
- **R11 s 273**: with an actual carrier, the contracting carrier is liable for the whole carriage; the actual carrier only for the part it performs. If the delay was on a part the actual carrier did not perform, the actual carrier is not liable.
- **R12 s 275**: with successive carriers, "the contracting carrier who is liable is the successive carrier who performed or was to perform the carriage where the delay occurred".

## Not expressible as input/output tests (by nature)

- s 274(3), s 277(3) (other law, remoteness), s 280 (just and equitable orders), s 282 (inter-carrier arrangements), s 283(2)-(4) (court leave up to 6 years: discretionary). At most, an encoding might expose the 6-year outer limit; see T-12.
- s 269 presumption of authority (evidential).
- s 273(b) (special agreements not binding the actual carrier unless agreed) - only expressible if the encoding takes a per-carrier special-contract input.

## Goal 1: Application and carriers (ss 270-273, 275)

| id | inputs | expected | provision |
|---|---|---|---|
| A-01 | departure Auckland (NZ), destination Christchurch (NZ), no stopping place abroad, by air, not single-flight-return, not excluded | applies = TRUE | s 270(1)(a),(b) "the place of departure and the place of destination are both in New Zealand; and there is no agreed stopping place outside New Zealand" |
| A-02 | departure NZ, destination Australia | applies = FALSE | s 270(1)(a); also s 270(3)(a) "within the territories of 2 countries" |
| A-03 | departure Australia, destination NZ | applies = FALSE | s 270(1)(a) |
| A-04 | departure NZ, destination NZ, agreed stopping place in Australia (Rarotonga, etc.) | applies = FALSE | s 270(1)(b); s 270(3)(b) "agreed stopping place within the territory of another country" |
| A-05 | departure NZ, destination NZ, no agreed foreign stop, but aircraft actually diverted to Australia | applies = TRUE | s 270(1) "according to the contract" (R1) |
| A-06 | domestic contract on an aircraft that is simultaneously carrying international passengers (e.g. AKL-CHC leg of a SYD-AKL-CHC flight) | applies = TRUE | s 270(2) "applies even if the aircraft ... is at the same time engaged in the international carriage" |
| A-07 | departure and destination both in Australia, no NZ involvement | applies = FALSE | s 270(1)(a) |
| A-08 | single flight, departure = destination (scenic flight Queenstown-Queenstown) | applies = FALSE | s 272(a) "single flight ... place of departure and the intended place of destination are the same" |
| A-09 | return trip AKL-WLG-AKL on two flights, departure = final destination | applies = TRUE | s 272(a) needs "a single flight" (R3) |
| A-10 | otherwise domestic flight of a type excluded by regulations | applies = FALSE | s 272(b) |
| A-11 | domestic, but single-flight return AND excluded by regulations | applies = FALSE | s 272 |
| A-12 | combined carriage (air + bus), domestic, delay on air leg | applies to the delay = TRUE | s 271 "applies only to the carriage by air" |
| A-13 | combined carriage (air + ferry), domestic, delay on ferry leg | applies to the delay = FALSE | s 271 (R4) |
| A-14 | single contracting carrier, no actual carrier, no successive carriers, delay occurred | liable carrier = the contracting carrier | s 269 "contracting carrier"; s 274(1) |
| A-15 | contracting carrier X, actual carrier Y performs the whole carriage, delay on Y's flight | X liable = TRUE, Y liable = TRUE | s 273(a)(i),(ii) |
| A-16 | contracting X, actual Y performs leg 2 only, delay on leg 2 | X liable TRUE, Y liable TRUE | s 273(a) |
| A-17 | contracting X, actual Y performs leg 2 only, delay on leg 1 (performed by X) | X liable TRUE, Y liable FALSE | s 273(a)(ii) "solely in respect of the carriage that the actual carrier performs" (R11) |
| A-18 | successive carriers A (leg 1) and B (leg 2), single operation, delay on leg 2 | liable contracting carrier = B (not A) | s 275 "the successive carrier who performed or was to perform the carriage where the delay occurred" |
| A-19 | successive carriers A, B, delay on leg 1 | liable = A | s 275 |
| A-20 | successive carriers A, B, C, delay on leg 3 that C "was to perform" (never flown) | liable = C | s 275 "or was to perform" |
| A-21 | international contract (NZ-Australia) with an actual carrier | applies = FALSE (no carrier question arises under this subpart) | s 270(1) |

## Goal 2: Liability and its limit (ss 274, 276-279)

Default for this goal: domestic carriage, delay caused damage, no defence proved, no s 276 measures, no intent/recklessness, no special contract.

| id | inputs | expected | provision |
|---|---|---|---|
| L-01 | no defence, no measures | liable = TRUE | s 274(1) "A carrier is liable ... for damage caused by delay" |
| L-02 | delay proved to arise from meteorological conditions | liable = FALSE | s 274(2)(a)(i) |
| L-03 | delay from complying with ATC instructions | liable = FALSE | s 274(2)(a)(ii) |
| L-04 | delay from obeying orders of a lawful authority | liable = FALSE | s 274(2)(a)(iii) |
| L-05 | delay made necessary by force majeure | liable = FALSE | s 274(2)(b) |
| L-06 | delay necessary to save or attempt to save life | liable = FALSE | s 274(2)(c) |
| L-07 | delay from crew shortage / mechanical fault (no listed cause) | liable = TRUE | s 274(1); none of (2) |
| L-08 | carrier took all necessary measures to avoid the damage | liable = FALSE | s 276(a) |
| L-09 | not possible for carrier to take those measures | liable = FALSE | s 276(b) |
| L-10 | carrier's agent (ground handler) took all necessary measures | liable = FALSE | s 276(a) "or the carrier's servants or agents" (only if encoding separates; else same input as L-08) |
| L-11 | weather cause + all measures taken | liable = FALSE | s 274(2), s 276 |
| L-12 | carriage not domestic (NZ-Sydney), no defence | liable under this subpart = FALSE / not applicable | s 270 |
| C-01 | damage 500, sum paid 200 | limit = 500 (10×200 = 2000) | s 277(1) "lesser of ... damage proved ... and ... 10 times the sum paid" |
| C-02 | damage 3000, sum paid 200 | 2000 | s 277(1)(b) |
| C-03 | damage 2000, sum paid 200 | 2000 (equal) | s 277(1) |
| C-04 | damage 1500, sum paid 99.50 | 995 | s 277(1)(b) |
| C-05 | damage 0, sum paid 200 | 0 | s 277(1)(a) |
| C-06 | damage 400, sum paid 0 (free carriage) | 0 | s 277(1)(b), s 269 "contract includes an arrangement made without consideration" (R8, ambiguous) |
| C-07 | damage 5000, sum paid 200, special contract cap 4000 | 4000 | s 277(2) "may, by special contract, increase the amount" |
| C-08 | damage 3000, sum paid 200, special contract cap 4000 | 3000 | s 277(1)(a), (2) (R6) |
| C-09 | damage 5000, sum paid 200, special contract cap 1000 (lower than 10×) | 2000 | s 278(2) "limiting a carrier's liability ... is unenforceable" (R6) |
| C-10 | damage 5000, sum paid 200, contract term excluding all delay liability | 2000 (term ignored) | s 278(1),(2) |
| C-11 | damage 5000, sum paid 200, intent to cause damage proved | 5000 | s 279(a) "limits ... do not apply" |
| C-12 | damage 5000, sum paid 200, recklessness proved | 5000 | s 279(b) |
| C-13 | damage 1000, sum paid 200, recklessness proved | 1000 | s 279; s 277(1)(a) (R7) |
| C-14 | damage 9000, sum paid 200, special cap 4000 AND recklessness | 9000 | s 279 |
| C-15 | weather defence proved, damage 500, sum 200 | amount payable = 0 / not liable | s 274(2)(a)(i) |
| C-16 | term in contract offering a stricter duty (e.g. liability even for weather delays) | term enforceable: liable = TRUE despite weather | s 278(4)(a) "imposes a stricter duty" |
| C-17 | term offering a more advantageous remedy (fixed 1000 regardless of damage) | enforceable | s 278(4)(b) (likely not expressible as a number beyond C-07) |
| C-18 | special contract raising limit agreed by contracting carrier only; claim against actual carrier; damage 5000, sum 200, cap 4000 | actual carrier's limit = 2000 | s 273(b) "does not affect the actual carrier unless agreed to by the actual carrier" |

## Goal 3: Time limits (ss 281(2), 283)

| id | inputs | expected last day to bring | provision |
|---|---|---|---|
| T-01 | arrived 10 March 2024 | 10 March 2026 | s 283(1)(a) "2 years after ... the date on which the aircraft arrived" (R9) |
| T-02 | arrived 10 March 2024, action filed 10 March 2026 | in time = TRUE | s 283(1) "must not be brought ... later than 2 years after" |
| T-03 | arrived 10 March 2024, action filed 11 March 2026 | in time = FALSE | s 283(1) |
| T-04 | arrived 29 February 2024 | 28 February 2026 | s 283(1)(a) (R9, ambiguous: alternative 1 March 2026) |
| T-05 | arrived 29 February 2024, filed 1 March 2026 | in time = FALSE | s 283(1) (R9) |
| T-06 | arrived 28 February 2026 | 28 February 2028 | s 283(1)(a) |
| T-07 | arrived 29 February 2028 | 28 February 2030 | R9 |
| T-08 | arrived 31 December 2025 | 31 December 2027 | s 283(1)(a) |
| T-09 | not arrived; ought to have arrived 5 June 2025; carriage stopped 3 June 2025 | 5 June 2027 | s 283(1)(b) "later of" (R10) |
| T-10 | not arrived; ought 5 June 2025; stopped 20 July 2025 | 20 July 2027 | s 283(1)(b)(ii) |
| T-11 | not arrived; ought 29 February 2024; stopped 29 February 2024 | 28 February 2026 | s 283(1)(b), R9 |
| T-12 | arrived 10 March 2024, filed 1 June 2027 without leave | in time = FALSE (leave under s 283(2) up to 6 years is discretionary) | s 283(1),(2) |
| T-13 | arrived 1 January 2024 but delay of 3 days (ought 29 December 2023) | 1 January 2026 (arrival only; (b) not engaged) | s 283(1)(a),(b) "if the aircraft did not arrive" (R10) |
| T-14 | contribution: judgment against person A on 15 August 2025 | last day 15 August 2027 | s 281(2) "not later than 2 years after the time when judgment is obtained against person A" |
| T-15 | contribution: judgment 29 February 2024 | 28 February 2026 | s 281(2), R9 |
| T-16 | contribution: judgment 15 August 2025, filed 16 August 2027 | in time = FALSE | s 281(2) |
| T-17 | contribution: judgment 15 August 2025, filed 15 August 2027 | in time = TRUE | s 281(2) |

## Top-level goal

| id | inputs | expected | provision |
|---|---|---|---|
| G-01 | A-01 contract, single carrier, delay from mechanical fault, damage 500, sum 200, arrived 10 March 2024 | applies TRUE, liable TRUE, max 500, last day 10 March 2026 | ss 270, 274, 277, 283 |
| G-02 | same, but damage 5000 | max 2000 | s 277(1)(b) |
| G-03 | same as G-01 but departure NZ, destination Fiji | applies FALSE (other answers not engaged) | s 270 |
| G-04 | same as G-01 but weather cause | liable FALSE, max 0 | s 274(2)(a)(i) |
| G-05 | successive carriers A/B, delay on B's leg, damage 5000, sum 200, reckless | liable carrier B, max 5000 | ss 275, 279 |

## Added after opening the rule modules: scenarios not expressible in the encoding

(No expected value above was changed.)

- A-21: no separate actual-carrier/international interplay; covered only through the top-level goal (most payable 0).
- L-12: the liability function takes no carriage; covered through the top-level goal (G-03).
- C-16, C-17 (s 278(4) stricter duty / more advantageous remedy): no input for a term favouring the passenger; not expressible.
- C-18 (s 273(b) special contract not binding the actual carrier): no per-carrier special-contract input; not expressible.
- L-09/L-10: s 276(a) and (b), and carrier vs servant/agent, share one input; tested with the same input.
- A-05, A-06, A-09, A-12: the distinction (actual diversion, simultaneous international carriage, two-flight return, combined carriage) is not an input; tested by setting the flags the contract determines.
- T-16, T-17: no "contribution in time" function; tested by comparing the filing date with the last day returned.
