# Work Health and Safety Act 2011 (Cth) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill, with a second seat layer for the person conducting the business or undertaking.
There is no REFUSE in it; work under a State or Territory WHS law answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0067` in `subjects/au/requirements.jsonl` (priority 2, the 20 topics: work injury and workplace safety). No scenario life raised it, so every case is hypothetical. There was no earlier encoding of this Act to keep.

## Edition

Compilation No. 16, compilation date 1 July 2024, includes amendments up to Act No. 120, 2023 (register id **C2024C00243**, Federal Register of Legislation, retrieved 13 October 2026), as deposited at `../../registers/source-bundle/C2011A00137.txt`.

Nothing else is brought in. The Work Health and Safety Regulations 2011 (which add to or exclude from the notifiable incidents, prescribe the default issue procedure, the HSR training, the transitional periods of licensees and the "prescribed purposes" of s 88) are not deposited; where an answer turns on them it is an input or a comment.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `whs-worker.l4` (the worker, 13 questions) | `whs-cases-worker.l4` | 44 written, 44 satisfied |
| `whs-seat-pcbu.l4` (the PCBU, 6 questions) | `whs-cases-pcbu.l4` | 24 written, 24 satisfied (8 mirror cases) |

`l4 run` on all four files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seats

**The worker (first seat, `whs-worker.l4`).** "I work for a Commonwealth employer. What safety duties are owed to me, may I stop unsafe work, and what are my duties as a worker?" A worker in the s 7 sense: an employee, contractor, labour hire worker, apprentice, volunteer or Defence Force member, carrying out work for a business or undertaking the Commonwealth Act covers (s 12). The duties the Act puts on the PCBU are encoded for what they mean to the worker: what it must ensure for me, when it must consult me, what it must do when I stop work.

**The person conducting the business or undertaking (second seat, `whs-seat-pcbu.l4`).** The PCBU is the Act's main duty holder, so it gets a seat: asked by the owner or manager of a non-Commonwealth licensee, a Commonwealth company or a public authority. The Commonwealth itself is a PCBU too (s 12(1)(a)); it gets no seat, being the government, but the answers are the same for it. The layer calls the rules in `whs-worker.l4` for the notifiable incident, consultation and the penalties, and adds the duties that are the PCBU's alone (ss 38, 39, 87). The two seats define no name twice. Mirror cases in `whs-cases-pcbu.l4` ask the worker file's facts from the PCBU's seat; the answers agree.

The 2026-10-18 defaults:

- **The Act alone.** The Regulations are not deposited.
- **The actors the text names:** the worker, the PCBU, its officers, the health and safety representative, Comcare (the regulator, s 4), inspectors, the court.
- **Judgments handed to others are answered conditionally.** Whether something was "reasonably practicable" (s 18) is the court's weighing and is never computed; the duties are stated "so far as is reasonably practicable". The worker's "reasonable concern" (s 84) is asked as a fact.
- **The Act's own definitions are worked out from facts:** worker (s 7), notifiable incident, serious injury or illness, dangerous incident (ss 35 to 37), discriminatory conduct and prohibited reason (ss 105, 106). Borrowed terms are asked as facts: public authority and Commonwealth company, non-Commonwealth licensee, the Maritime Industry OHS Act's vessels.
- **One case:** one worker, one business or undertaking, one matter or incident.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** Parts 8 to 14 (Comcare, inspectors, notices, enforceable undertakings, proceedings, review), Part 7 (entry permits), Schedules 1 to 3.

## Scope

**In:** ss 5(7)–(8), 7(1), (2A), 12(1)–(2), (4), (6), 12A, 17, 19, 28, 30A, 31–34, 35–37, 38(1)–(4), (7), 39, 47–49, 50, 80(1), 81(2), 82, 84, 85 (as an input), 86, 87, 88, 105, 106, 112, 113, 115(a), Schedule 4 cls 1–2 (before indexation).

**Out:** ss 20–27 (the duties of those who manage workplaces and fixtures, design, manufacture, import, supply and install plant, and officers' due diligence, except the officer's penalty column); s 29; s 46; Part 4 (authorisations); Part 5 Division 3 beyond s 50, Divisions 4 and 7; Part 6 Division 2 (criminal proceedings for discrimination, s 104 as an offence); Part 7; Parts 8 to 14; Schedule 4 cls 3–5 (civil penalty tiers, indexation, rounding).

## What the Act turns out to say

1. **The Commonwealth Act covers only Commonwealth work.** It applies to the Commonwealth, its public authorities and, in their transitional period, non-Commonwealth licensees (s 12(1), (4)), not to the ACT or NT administrations (s 12(2)), and not on vessels under the Maritime Industry OHS Act or offshore petroleum facilities (s 12A). Every other worker is under a State or Territory WHS law, which answers `not covered`. Asserted.
2. **"Worker" is wider than employee.** Contractors, labour hire workers, outworkers, apprentices, work experience students and volunteers are workers (s 7(1)), and Defence Force members are at work while performing their functions (s 7(2A)). A volunteer association with no employees is no PCBU (s 5(7)), so its volunteers are not its workers. Asserted.
3. **The PCBU's duty is "so far as is reasonably practicable", and the Act does not let the worker compute it.** Section 18 lists what is weighed; the encoding states the duties owed (s 19(1), (3), (4)) and leaves the weighing to the court. Asserted (the s 19 list).
4. **A worker may stop work only for an immediate or imminent hazard.** Section 84 needs "a reasonable concern" of "a serious risk ... emanating from an immediate or imminent exposure to a hazard"; a longer-term risk goes through the issue procedure (ss 81, 82), which does not take away the right to stop (s 82(3)). A worker who stops must tell the PCBU (unless an HSR directed it) and stay available for alternative work (s 86); continuity of engagement is kept unless the worker unreasonably refuses safe and appropriate alternative work (s 88), for purposes the Regulations prescribe. Asserted, mirrored (s 87).
5. **An unresolved issue goes to Comcare's inspector through the right party.** Where the worker is in a work group, the party is the HSR (s 80(1)(c)), so it is the HSR who asks (s 82(2)); otherwise the worker. Reasonable efforts must come first (s 82(1)). Asserted.
6. **A worker can commit a Category 1, 2 or 3 offence, but not industrial manslaughter.** Section 30A is limited to a PCBU or an officer. A worker is an individual "other than" a PCBU or officer, column 3 of Schedule 4 cl 1: Category 1 $1,500,000 or 15 years or both; Category 2 $209,000; Category 3 $70,000. Volunteers keep their s 28 duty and its offences (s 34(1)). Asserted.
7. **The penalties printed are not the penalties in force.** Schedule 4 cl 4 indexes every figure each year from 1 July 2024 by CPI numbers, and the formula is missing from the deposited text (lost in conversion: "calculated as follows: where:" with nothing between). The figures here are the printed ones, before indexation, and each answer says so. A formulas sidecar transcribed from the authorised rendering is needed before the indexed figures can be computed. Asserted as printed.
8. **A notifiable incident needs no injury.** A dangerous incident (s 37), such as a load falling from height near a worker, is notifiable even if nobody is hurt (s 35(c)); a PCBU must ensure Comcare is told "immediately" and "by the fastest possible means" (s 38(1), (2)) and keep a record for at least 5 years from the notice (s 38(7)); the site must be left undisturbed, except for the five things s 39(3) allows, until an inspector arrives or directs. The Regulations may add or exclude kinds; that is an input. Asserted, mirrored.
9. **The protection against punishment for raising safety is presumed, with a one-year limit.** Dismissal, detriment or refusal to engage for a s 106 reason (including stopping unsafe work, which is exercising a power under the Act) may be taken to court under s 112, within 1 year after the person knew or ought to have known (s 113(1)); the reason is presumed substantial unless the other side proves otherwise (s 113(2)); there is a defence of reasonable conduct done substantially to comply with the Act (s 113(3)); and no s 112 proceeding may be begun while another claim about the same matter is live (s 115(a)). Asserted.
10. **The Commonwealth as employer gets no seat, but is a PCBU.** The PCBU seat is worded for a licensee, company or public authority; the same answers hold for a Commonwealth department (s 12(1)(a), s 10). Not asserted (a finding about the seat).

## What would need doing before this is worth relying on

- **The Work Health and Safety Regulations 2011**: the incidents they add or exclude, the default issue resolution procedure, HSR training, the s 88 prescribed purposes, licensees' transitional periods.
- **Schedule 4 cl 4's formula**, transcribed from the authorised rendering into a `C2011A00137.formulas.md` sidecar, with the CPI numbers, so the indexed penalties can be computed.
- **Sections 20 to 27** (other duty holders, officers' due diligence) and **Part 7** (entry permits), if a case asks.
- **Wider sources.** No Comcare guidance, code of practice or decision was read.

## The Regulations brought in (added 2026-10-23, REQ-0093)

**Module:** `whs-regulations.l4`, beside `whs-worker.l4`, which it imports; cases in `whs-cases-regulations.l4` (20 assertions written, 20 satisfied; 2 `#TRACE` runs of the regulative rules, both FULFILLED; `l4 run` 0 errors, 0 warnings on both new files; `whs-cases-worker.l4` 44 of 44 and `whs-cases-pcbu.l4` 24 of 24 still pass). Seat: the worker, as before.

**Instrument:** the Work Health and Safety Regulations 2011 (Cth), Compilation No. 28 (F2025C00381), already deposited at `subjects/au/work-health-and-safety-regulations-2011/` (retrieved 2026-10-19); no new fetch was needed.

**What the module computes:** whether an incident is notifiable with reg 699's prescribed serious illnesses worked out from the facts (it sets `whs-worker.l4`'s `the regulations exclude it, or add it` input instead of asking it); which issue resolution procedure applies and whether the resolution must be written and given to the worker (regs 22, 23), with the default procedure and the written-agreement duty as regulative rules (`PARTY ... MAY/MUST ... HENCE ... LEST`); whether continuity of engagement is kept for a named entitlement (s 88, reg 24); whether a named former Comcare licensee's transitional period is running on a day (s 12(6)(b), reg 12A).

14. **The Commonwealth Regulations only add to the notifiable list, and only illnesses.** Reg 699 adds work-related infections (care, blood and body substances, animals) and seven occupational zoonoses to s 36. Nothing is prescribed out of s 36, nothing into or out of s 37 (dangerous incidents), and no class of worker under s 7(1)(i). So `the regulations exclude it, or add it` is TRUE exactly when the Act's list misses the incident and the illness is one reg 699 names. Asserted.
15. **The end of the named licensees' transitional period is fixed by reference to another instrument's commencement, which the deposit dates only to a range.** Reg 12A ends the period for Hollard Insurance Partners, MLC Wealth and Vicinity Centres PM "on the day on which Part 2 of Schedule 1" to the 2022 psychosocial amendment Regulations commences. The compilation's endnotes record that Schedule 1 commenced as items 1 and 2 on 1 April 2023 and the remainder on 4 January 2023, without saying which items make up Part 2. The module answers "running" before 4 January 2023, "ended" from 1 April 2023, and "not known from the deposit" between. For any other licensee the Regulations prescribe no end day, so on the text its period is still running. Asserted.
16. **Reg 24 makes every engagement-related entitlement a prescribed purpose.** It lists seniority-based pay and promotion, superannuation, leave and notice of termination, but "including" introduces them: the purpose is "any benefit or entitlement associated with the worker's engagement". The only thing that defeats continuity is the s 88 condition (an unreasonable failure to do safe alternative work). Asserted.
