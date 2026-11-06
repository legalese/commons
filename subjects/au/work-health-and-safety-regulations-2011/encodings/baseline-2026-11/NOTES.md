# Work Health and Safety Regulations 2011 (Cth), Chapter 8A — baseline encoding (crystalline silica and engineered stone)

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it: a case a regulation does not reach answers `NOTHING` or an explicit enumeration value ("the prohibition was not yet in force", "no notice is required for this work"), and the cases assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

This is the first encoding of the Regulations' own subject. The Work Health and Safety Act 2011's baseline (`subjects/au/work-health-and-safety-act-2011/encodings/baseline-2026-10/`) reads regs 12A, 22 to 24 and 699 for the Act's questions; it is untouched, and nothing here repeats it. It was written as part of a run of baselines on the law behind workplace injury and dust disease claims.

## Edition

Compilation No. 28, compilation date 25 March 2025, includes amendments up to F2025L00404 (register id **F2025C00381**, Federal Register of Legislation, retrieved 19 October 2026), as deposited at `../../registers/source-bundle/F2011L02664.txt`. The compilation carries the engineered stone prohibition and the crystalline silica substance duties inserted by the Work Health and Safety Amendment (Penalties and Engineered Stone and Crystalline Silica Substances) Regulations 2024 (F2024L00766).

Brought in for the numbers: the printed penalty amounts of Schedule 4 cl 2 of the Work Health and Safety Act 2011 (C2024C00243, deposited in the Act's subject), before indexation under cl 4. The Act's encoding indexes them (`whs-penalty-indexation.l4`); it cannot be imported from this folder, so a worker who needs the indexed figure for a given year should run that module with the tier this encoding names.

The workplace exposure standard for respirable crystalline silica (reg 5, "exposure standard", a Safe Work Australia document of 16 December 2019) is not deposited; whether a result exceeded it is an input.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `silica-worker.l4` (the worker, 20 questions, 5 regulative rules) | `silica-cases-worker.l4` | 107 written, 107 satisfied; 6 `#TRACE` runs: 3 FULFILLED, 3 BREACHED by the business, each as the comment above it says |

`l4 run` on both files: 0 errors, 0 warnings (7 November 2026). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was worked out by hand from the text before the file was run.

## Seat

**The worker.** "I cut, fitted, removed or worked near engineered stone or other silica-bearing material for a business. Was my employer allowed to have me do it? Was my processing controlled? What did the business have to do because it was high risk? Must I be given health monitoring, what must it include, who may see my report, and how long must the records of my exposure and training be kept?"
A worker in the Act's s 7 sense, working for a business or undertaking the Commonwealth Act covers (the Commonwealth, Commonwealth authorities and non-Commonwealth licensees, Act s 12). Every duty in Chapter 8A is on the person conducting the business or undertaking; each is encoded for what it means to the worker.
These are the provisions a worker who later brings a silica disease claim meets: whether the work was lawful, whether it was controlled, and which records of exposure, training and health monitoring must exist and for how long.

No second seat is written. The business is the duty holder and could have one later, beside this module, calling the same rules.

The 2026-10-18 defaults:

- **The instrument alone, with what sets its numbers:** Chapter 8A and the regulations it points to (reg 50, Part 7.1 Division 6, Schedule 14 item 7, reg 689A(2), reg 698A); the Act's Schedule 4 cl 2 printed amounts.
- **The actors the text names:** the worker, the person conducting a business or undertaking, the regulator, the registered medical practitioner. The regulator gets no seat.
- **Judgments handed to others are asked as inputs, never decided:** "so far as is reasonably practicable" and "not reasonably practicable" (reg 529B), "reasonably likely to expose" (529A(1)(f)), "significant risk" (368), "reasonably believes" (529CD), "could not reasonably be expected to know" (529G(3)), "genuine research and analysis" (529E, 529F).
- **Own definitions worked out from facts:** CSS (529A(2)), engineered stone (529A(4), with reg 5's porcelain product and sintered stone), processing (529A(1)), controlled (529B), respiratory protective equipment (529B(3)). Borrowed terms (the AS/NZS standards, the exposure standard, "high risk construction work") are asked as facts.
- **One case:** one piece of work, one worker.
- **The text's terms with plain glosses** in the comments and `@desc`s.
- **Machinery out:** the regulator's exemption process (regs 689A(1), 689B to 689E), the acknowledgements of notices, review of decisions.

## Scope

**In.** Chapter 8A whole: regs 529A, 529B, 529C, 529CA (high-risk assessment, the (5) deeming), 529CB (silica risk control plan, the (3) safe work method statement alternative), 529CC (plan given to workers, stopping), 529CD (training and its record), 529CE (air monitoring, the 14-day report, health monitoring), 529D to 529F (the prohibition and its exceptions), 529G to 529J (notices to the regulator and keeping them). With them: reg 50(2) (the 30-year air monitoring record), regs 368, 370, 372, 374, 375, 376, 377, 378 (health monitoring, its report, its record, its confidentiality), Schedule 14 table 14.1 item 7 (the crystalline silica monitoring), reg 689A(2) (an exemption granted, as a fact), reg 698A (the pre-2024 contract transition), and the penalty tier for every offence encoded.

**Out, and why.**
- Regs 689A(1), 689B to 689E: how the regulator grants an exemption; the worker meets only its result, taken as an input.
- Reg 698B: whether reg 529D would acquire property otherwise than on just terms is a constitutional question for a court.
- Regs 529G(4), 529H(2), 529I(3): the regulator's acknowledgement of a notice.
- Reg 529CB(2) (what a plan must contain) and 529CD(4) (what training counts): content requirements the worker cannot test as facts; they are glossed in comments.
- Regs 369, 371, 373 are covered only through the penalty question; their content is glossed.
- The rest of the Regulations (asbestos in Chapter 8, the other hazardous chemicals, major hazard facilities, mines), the workplace exposure standard's figure, State and Territory WHS laws (which carry their own engineered stone bans; most stone workers are under them, not under this Commonwealth instrument), and compensation for silicosis (the Safety, Rehabilitation and Compensation Act 1988 and State schemes).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** (commencement of 529A to 529J other than 529CA to 529CE; `the engineered stone prohibition starts`): 1 July 2024. Endnote 3 gives F2024L00766 Sch 2 from 1 July 2024 and Sch 3 from 1 September 2024 but does not say which Schedule inserted which regulation. Other reading: some of these came in on 1 September 2024.
- **F2** (commencement of 529CA to 529CE; `the high-risk processing duties start`): 1 September 2024, on the reading that regs 529A to 529C were added by Sch 2 and substituted by Sch 3 (endnote 4 shows "ad" then "rs"), while 529CA to 529CE were added once, by Sch 3. Other reading: 1 July 2024.
- **F3** (reg 529C, `reg 529C was breached`): a flat negative with "unless": `JUST FALSE` once the processing is controlled, `JUST TRUE` when not; `NOTHING` before 1 July 2024 or where the task is not processing of a CSS (scope limit). Other reading: `JUST FALSE` where the task is not processing.
- **F4** (reg 698A(1)(a)(ii) and (b), (2)(b) and (c); `the State or Territory transition also covered it`): asked as one fact. Other reading: two facts (the place, and the State or Territory law's own transition). The answers do not differ, because both must hold.
- **F5** (reg 529CA(5), `the processing is high risk`): with no assessment made at all, `NOTHING`. Other reading: the (5) deeming ("unable to determine") reaches a business that never tried, giving `JUST TRUE`.
- **F6** (reg 529CE(b), `the last day to give the result to the regulator`): `NOTHING` (no deadline) where the result did not exceed the standard or was reported before 1 September 2024.
- **F7** (reg 529D, `what reg 529D says`): the answer is an enumeration naming the exception that applied, checked in the order 689A, 529E, 529F, 698A; where two apply, the first is named. Other reading: report every exception that applies.
- **F8** (periods of years, `the last day of a period of years beginning on`): a period of N years beginning on a day ends on the day before its Nth anniversary; a period "N years after" a day begins the next day (Acts Interpretation Act 1901 s 36(1)), so it ends on the anniversary. A 29 February anniversary in a common year is 1 March, so the period ends on 28 February. Other reading: clamp the anniversary to 28 February, which ends a period one day earlier.

The rulings of 2026-11-04 and 2026-11-05 recorded in `docs/ENCODING-GUIDE.md` §5 govern the `JUST FALSE` and `NOTHING` answers; F3, F5 and F6 are case-by-case sites under Meng's rule of 2026-11-05 ("decide case by case").

## What the Regulations turn out to say

1. **Commencement is not in the text.** The compilation's endnotes give two commencement dates for the 2024 amending regulations and do not say which regulation came in on which (F1, F2). The engineered stone prohibition is encoded from 1 July 2024 and the high-risk duties from 1 September 2024.
2. **A typo in the note to reg 529A(2):** "Engineered stone is a type of CCS." The defined abbreviation is CSS.
3. **Reg 529I(2) is garbled:** the notice is due "within the period of 30 days ending after the day the 12-month period ends". A period cannot both be "of 30 days" and "end after" a day. Encoded as 30 days after the last day of the 12-month period, the same as reg 529H(1)'s "within the period ending 30 days after the day the change occurs". Asserted (13 April 2026 for a last notice on 15 March 2025).
4. **Reg 698A reaches only Commonwealth work in a State or Territory with a transition of its own.** Paragraph (1)(a)(ii) requires the work to be done "in a place to which a corresponding WHS law applies", and (1)(b) that the corresponding law's own reg 529D would not apply because of its own 31 December 2024 cut-off. Read literally, Commonwealth work in a place where the State or Territory had no such transition gets no transition at all. Asserted.
5. **Manufacturing has no exception.** Regs 529E and 529F cover supplying, installing and processing; reg 698A covers installing, and supplying or processing for installation. Manufacturing engineered stone benchtops, panels or slabs is prohibited from 1 July 2024 unless the type is exempted under reg 689A, even for research. Asserted.
6. **Supplying or installing for research or sampling (reg 529E) need not be controlled; processing for the same purposes (reg 529F) must be.** Installing to repair or modify installed engineered stone is not within reg 529E (which names only research and sampling). Asserted.
7. **Resin decides two exclusions.** Engineered stone excludes porcelain products and sintered stone (529A(4)(b)(vi), (vii)), but reg 5 says neither term includes "a product that contains resin". A resin-bearing product sold as sintered stone or porcelain is therefore engineered stone if it otherwise meets (a). Asserted.
8. **Reg 529B(2) displaces subregulation (1) entirely.** Where none of the five engineering measures is reasonably practicable, a compliant respirator given and worn is enough; paragraph (1)(a) (control measures so far as is reasonably practicable) is not repeated. Asserted.
9. **A respirator that does not meet AS/NZS 1716:2012 and AS/NZS 1715:2009 is not "respiratory protective equipment"** (529B(3)), so processing relying on it is not controlled. Asserted.
10. **A business that makes no high-risk assessment is not caught by reg 529CA(5).** The deeming applies when the business "is unable to determine" whether the processing is high risk, not when it never assessed it (F5). Failing to assess is itself a tier E offence.
11. **The worker's health monitoring report may go to the regulator without consent only if it advises a work-caused disease or recommends remedial measures** (regs 376, 378(3)); to a new employer or an insurer only with the worker's written consent. Asserted.
12. **Records a silica disease claim may turn on last 30 years** (air monitoring, reg 50(2); health monitoring, reg 378(1)), **the training record 5 years after the worker leaves** (529CD(2)), and **an engineered stone notice 5 years from when it was given** (529J), which any person may ask to see. Asserted.
13. **Penalties are small beside the Act's.** The Chapter's offences are tier E ($8,400 for an individual, $42,000 for a body corporate, before indexation), tier G ($5,000 / $25,000) and tier I ($1,700 / $8,500). Asserted.

## What would need doing before this is worth relying on

- Confirm F1 and F2 against the 2024 amending regulations (F2024L00766), which are not deposited.
- Deposit the Safe Work Australia workplace exposure standard (2019) so the exceedance in reg 529CE(b) can be worked from a measured concentration.
- A second seat for the business, if wanted, beside this module.
- An independent test pass, and human review of the fork register.
- Links to the State and Territory engineered stone bans, which cover most stone workers, and to the compensation Acts a silica disease claim is brought under.
