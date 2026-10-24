# NOTES: Employment Insurance Regulations (SOR/96-332), piece er2: regulations 19 to 34

Piece er2 of the encoding of the Employment Insurance Act (S.C. 1996, c. 23) and the Employment Insurance Regulations (SOR/96-332): regulations 19 to 34, lines 340 to 539 of `SOR-96-332.txt` (5,198 words), written by the piece agent `er2` (Sonnet 5.5) on 2026-10-24 for the lead's merge.

**The text.** `SOR-96-332.txt` is an unofficial plain-text rendering, made by a converter script, of the Justice Laws consolidation of the Regulations current to 2026-09-30 and last amended 2026-04-01 (`../../registers/source-bundle/*.meta.json`). It is not the official text and nothing here is verified against the official text. The French version is equally authoritative and was not read; historical notes and footnotes are not in the rendering.

**Which instrument each rule comes from.** Every rule, type and quotation in the er2 files comes from the Regulations, regulations 19 to 34 (`src:N` is a line of `SOR-96-332.txt`). The Act appears only as a cross-reference: where a Regulation says "section 14 of the Act", "subsection 87(3) of the Act" and so on, the fact is an input (see Cross-references), and where it uses a term the Act defines in s 2(1) the core's rule is called (`s 2(1) employer`, `s 2(1) claimant`, `s 5(2)(b) employment of a person by a corporation they control`, and the helpers `s 2(1) the Sunday that begins the week containing`, `weeks as days`, `the last day of n days after d`, `Period of days`, `Reason for benefits`).

**Dates.** My range contains no enactment, assent, making or coming-into-force provision and no commencement rule, so no commencement date is carried and nothing is done about one. The dates the text itself fixes are substantive, not commencement, and are carried as values with an `@ref`: 26 June 1999 (reg 26.1(2)(b)), 1 August 1999 (reg 34(7)), 1 October and 31 March (reg 30(4)), 25 December (reg 28(b)(i)) and the years 1997, 1998, 1999 and 2000 (reg 34(6)). The text is one vintage, so no rule takes a rule date as input.

**Files** (all in this folder; `check.sh` runs every `.l4` here).

| file | what it holds |
| --- | --- |
| `er2-common.l4` | helpers that are not law: the later and the earlier of two days, the days two periods share, a period lying within another, the week containing a day |
| `er2-record-of-employment.l4` | regs 19 to 21: the record of employment and the hours and earnings it reports |
| `er2-allocation.l4` | regs 22 to 24.3: allocation of hours and insurable earnings, lay-off and separation earnings, a self-employed person's excluded earnings |
| `er2-claims.l4` | regs 25 to 28: week of benefits, the election, the claim and its time limit, periodic claims, claims for incapacitated and deceased persons, payments in advance |
| `er2-full-working-week.l4` | regs 29 to 32: the full working week (special cases, self-employed, employed), the self-employed person's week of unemployment, the working day |
| `er2-teachers.l4` | reg 33: teachers |
| `er2-family-supplement.l4` | reg 34: the family supplement, with both tables |
| `er2-tests-record-of-employment.l4`, `er2-tests-allocation.l4` (also tests `er2-common`), `er2-tests-claims.l4`, `er2-tests-full-working-week.l4`, `er2-tests-teachers.l4`, `er2-tests-family-supplement.l4` | hand-written expectations for each layer-1 module |
| `er2-seat.l4`, `er2-cases-seat.l4` | layer 2: 61 questions and 162 worked cases |
| `NOTES.md`, `PROGRESS.md` | this file; the working log |
| `check.sh`, `srcrefs.py`, `eia-core*.l4` | supplied by the lead, unchanged |

**How the layer-1 modules were made.** Each module was written as a template in which a marker line stands for a run of quotation lines; a small script expanded each marker with `srcrefs.py quote`, so every `-- src:N | ...` line is copied from the raw file and never typed. The two tables of reg 34 were emitted by the same script from lines 522 to 527 and 536 to 538 (a ruler comment names the columns once; each band's printed heading closes its line; the script stops if a band does not begin one dollar above the end of the one before). The templates and the script are scratch and are not part of the deposit; the `.l4` files are.

**Two layers.** Layer 1 follows the text's own structure, one module per group of regulations, each rule cited with `@ref` and `src:` locators. Layer 2 is `er2-seat.l4`, which imports layer 1 and calls its rules; it restates no rule. A "deadline" is a DATE-valued rule and "in time" a BOOLEAN over it (`check.sh` cannot count a `#TRACE`, so no DEONTIC rule is used); the duty itself is the relation named in Jural relations.

## Seat

**The seat** is the person who has lost work, or cannot work because of sickness, pregnancy, caring for a child or a family member, or who is self-employed or a fisher, asking whether they qualify for Employment Insurance benefits, how many hours or weeks they need, how much they would receive and for how long, and what they must do or tell the Commission (the brief's seat for this piece, as the keel states it).

**Why this seat for regulations 19 to 34.** The regulations of this range are mostly about what happens to that person's claim: the record of employment that proves their hours and earnings and the deadlines on the employer who owes it (regs 19 to 21), how those hours and earnings are spread over their qualifying period, pay periods and weeks (regs 22 to 24.3), when they are paid a "week of benefits", the election they make, when their claim must be made, when they are excused from making it every period and what they must then tell the Commission (regs 25 to 26.1), who may claim for them if they are incapacitated or have died (reg 27), when they may be paid early (reg 28), whether they count as having worked a full working week (regs 29 to 32), how teachers are treated in school holidays (reg 33), and the family supplement that raises their rate (reg 34).

**Officials have no seat.** The Commission appears only as the party that is owed a duty or holds a power over the person; its duties (to authorize payment, to work out hours and earnings from a trustee's records, to allocate hours and earnings) are asked as what the person is owed, and its powers (to pay in advance, to end an exemption) as what the person is exposed to. The employer's duties (regs 19 to 21) are asked from the employee's side: "By what date must my employer give me my paper record of employment?". The person who acts for an incapacitated claimant, the executor or administrator and the successor of reg 27 are asked in their own voice ("As the executor ... will the Commission authorize payment to me?"), because the text gives them the claim; a further seat for the employer, or for the family left behind, is not written (the brief asks for one thin layer).

**Rules that have no question of their own.** Every layer-1 rule is reached by some question, but some only inside a larger one: reg 19(1) (inside the first question of the record of employment); regs 22(1)(a), 22(1)(b) and 22(2) (inside "How many hours of my job count within my qualifying period"); the predicates of reg 23(1)(b), (1.1), (2), (3) and (4) and the arrangement of (1) (inside "Which rule of regulation 23 allocates this payment of mine"; the arithmetic of (a)(i), (a)(ii) and "proportionately", the day counts of (3) and (4), (1)(d) and (5) have their own questions); reg 24.1 and 24.3 (own questions); regs 26.1(2)(a), (b), (c), (d) and 26.1(3) (inside "Am I excused from making periodic claims on this day"; (d)(ii), (d)(iii) and the period of eligibility have their own); reg 27(3) (inside the executor's question) and 27(4), (5), (6) (inside the successor's); reg 28(b)(i) (inside the payment-in-advance question); regs 30(1), (2), (4) (inside the combined reg 30 question; (3) and (5) have their own); regs 31(1), (2), (3) (inside "How many hours, days or shifts make a full working week for me"); reg 34(4), (6) and (7) (inside "By how much is my rate of weekly benefits increased"; the month of (3), the table of (5) and the percentage of (6) also have their own). The rules with no seat question at all are the two repealed stubs.

**Plain inputs.** Every question takes one plain input per fact the person can state, each with an `@desc` worded as that person would be asked; records, periods and optional facts are built inside the question. The inputs that a person cannot know without the law (the maximum weekly insurable earnings, the period fixed by section 22(2) and its siblings, whether there is an interruption of earnings) are asked as facts and said to be decided elsewhere.

## Jural relations

One row per provision that creates a relation. Hohfeld's correlatives: claim / duty, privilege / no-right, power / liability, immunity / disability. "none" lists, once, the provisions that are definitions, counting rules or deemings. The rule column names the layer-1 rule that encodes the relation, once, with a neutral name.

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | section | rule |
| --- | --- | --- | --- | --- |
| claim to a record of employment | the insured person (claim); the Commission (claim) | the employer (duty) | reg 19(2) | `reg 19(2) a record of employment must be completed in respect of the person` |
| claim to the employee's copy within five days | the insured person (claim) | the employer (duty) | reg 19(3)(a) | `reg 19(3)(a) the last day for delivering the employee's copy ...`, `... delivered in time` |
| claim to the Commission's copy within the same time | the Commission (claim) | the employer (duty) | reg 19(3)(b) | `reg 19(3)(b) the Commission's copy was sent in time` |
| claim that the employer keeps its copy | the Commission (claim, through s 87(3) of the Act) | the employer (duty) | reg 19(3)(c), 19(3.1)(b) | `reg 19(3)(c) ...`, `reg 19(3.1)(b) ...` |
| claim to the electronic record within the time limit | the Commission (claim) | the employer (duty) | reg 19(3.1)(a) | `reg 19(3.1)(a) the last day for sending the electronic record of employment to the Commission`, `... sent in time` |
| claim to a mailed copy, or to retention of it, where delivery failed | the insured person (claim) | the employer (duty) | reg 19(4) | `reg 19(4) what the employer must do with the employee's copy`, `reg 19(4)(b) ...` |
| power to give a statement of hours and earnings | the person who becomes a claimant (power) | the Commission (liability: it must take the statement into account) | reg 19(5) | `reg 19(5) the person may provide a statement ...` |
| claim that hours and earnings be determined from the trustee's records | the insured person (claim) | the Commission (duty) | reg 19(6) | `reg 19(6) the hours of insurable employment and insurable earnings are determined from ...` |
| claim that the record reports the hours and earnings the Act determines | the insured person and the Commission (claim) | the employer (duty) | regs 20, 21 | `reg 20 ...`, `reg 21 ...` |
| claim that hours be allocated as stated unless evidence is given; power to give evidence | the claimant (claim); the claimant and the employer (power to give evidence) | the Commission (duty; liability to the evidence) | reg 22(1) | `reg 22(1)(a), (b) ...`, `reg 22 the hours of insurable employment counted within ...` |
| claim that earnings be allocated to the week as stated unless evidence is given | the claimant (claim); the claimant and the employer (power to give evidence) | the Commission (duty; liability to the evidence) | reg 24 | `reg 24 the insurable earnings allocated to the week` |
| privilege to estimate the earnings of a running pay period | the employer (privilege) | the claimant and the Commission (no-right to a different figure) | reg 23(5) | `reg 23(5) the employer may estimate ...` |
| power to elect between Part I and Part VII.1, in writing to the Commission | the person (power) | the Commission (liability); the person (duty to elect in the form) | reg 25.1 | `reg 25.1 the election ... is made as required` |
| duty to claim within three weeks (one week after a gap), and the claim's loss if late | the Commission (claim) | the claimant (duty; liability to lose the week) | reg 26(1), (2) | `reg 26 the last day for making the claim ...`, `... made in time` |
| immunity from periodic claims | the claimant (immunity) | the Commission (disability: it cannot require them) | reg 26.1(2) | `reg 26.1 the claimant is not required to make periodic claims on the day` |
| duty to notify as soon as possible and at the end of the period | the Commission (claim) | the claimant (duty) | reg 26.1(2)(d)(ii), (iii) | `reg 26.1(2)(d)(ii) ...`, `reg 26.1(2)(d)(iii) ...` |
| power to end the immunity by becoming aware of a failed condition | the Commission (power) | the claimant (liability) | reg 26.1(3) | `reg 26.1(3) section 26.1 still applies to the claim on the day` |
| claim that payment be authorized to the person acting for an incapacitated claimant | the person acting (claim) | the Commission (duty) | reg 27(1) | `reg 27(1) payment of the benefits must be authorized ...` |
| claim that payment be authorized to the legal representative of a deceased claimant | the legal representative (claim) | the Commission (duty) | reg 27(2), (3) | `reg 27(2) ...`, `reg 27(3) legal representative` |
| power of a successor to claim; benefits payable to them | the person entitled to succeed (power; then claim) | the Commission (liability; then duty) | reg 27(4) | `reg 27(4) the person may make a claim ...`, `reg 27(4) the benefits are payable to ...` |
| duty to make the claim on the form with the declaration and undertaking, and to submit the will and releases | the Commission (claim) | the applicant (duty) | reg 27(5), (6) | `reg 27(5) ...`, `reg 27(6) ...` |
| power to pay in advance of the customary time | the Commission (power) | the claimant (liability; no claim to early payment) | reg 28 | `reg 28 the Commission may pay benefits for the week of unemployment in advance of the customary time` |
| teacher's loss of the right to benefits in a non-teaching period | the Commission (privilege not to pay) | the claimant (no-right) | reg 33(2) | `reg 33(2) the claimant is not entitled to receive benefits for the week of unemployment` |
| ceiling on the benefits while qualifying on other work | the Commission (privilege to pay no more) | the claimant (no-right to more) | reg 33(3) | `reg 33(3) the amount of benefits payable for the week of unemployment` |
| claim to a family supplement on the rate of weekly benefits | the claimant (claim) | the Commission (duty) | reg 34(3) | `reg 34 the amount by which the rate of weekly benefits for the week is increased` |
| bar on a second increase for the same family | the Commission (privilege) | the claimant (no-right) | reg 34(4) | `reg 34(4) the claimant's rate of weekly benefits for the week shall not be increased` |
| none | (definitions, counting rules, deemings and standards) | | regs 19(1), 22(2), 23(1) to (4), 24.1, 24.2, 24.3, 25(1), 25(2), 26.1(1), 29, 30, 30.1, 30.2, 31, 32, 33(1), 34(1), 34(2), 34(5) to (7) | the corresponding rules; reg 24.3, reg 25 and regs 29 to 31 decide what counts, not who owes whom |

## Coverage table

One row per provision in lines 340 to 539 of the Regulations' raw file: every heading, every section, and every subsection or paragraph. Dispositions: `encoded`, `inert`, `repealed or blank in this text`, `fork` (the reading taken is in the Fork register, F-numbers below).

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Heading "Information Relating to Employment History" | src:340 | inert | - | A division title over regulation 19 (the first heading of the range, over the record of employment, the hours and earnings reported and their allocation) (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| Heading "Record of Employment" | src:342 | inert | - | A division title over regulation 19 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 19(1) | src:343 | encoded | `er2-record-of-employment` `reg 19(1) employer for the purposes of subsections (2) to (4)` | Calls the core's `s 2(1) employer` and adds the bankrupt employer and the trustee of one. |
| reg 19(2) | src:344 | encoded | `er2-record-of-employment` `reg 19(2) a record of employment must be completed in respect of the person` | The employer owes the record; the facts about insurable employment and the interruption of earnings are inputs (core s 5; piece er1 reg 14). |
| reg 19(3) lead-in | src:345 | encoded | `er2-record-of-employment` the `reg 19(3)(a)`, `(b)`, `(c)` rules | "Subject to subsection (4)": the delivery duty gives way to the step reg 19(4) names, which has its own rule; no rule combines the two. |
| reg 19(3)(a) | src:346-348 | encoded | `er2-record-of-employment` `reg 19(3)(a) the last day for delivering the employee's copy to the insured person`; `reg 19(3)(a) the employee's copy was delivered in time` | Five days after the later of the two days; the last day counts (keel F4). |
| reg 19(3)(b) | src:349 | encoded | `er2-record-of-employment` `reg 19(3)(b) the Commission's copy was sent in time` | The same time limit as (a), by the text's own words. |
| reg 19(3)(c) | src:350 | encoded | `er2-record-of-employment` `reg 19(3)(c) the employer's copy has been kept and retained` | Keeping it "in accordance with subsection 87(3) of the Act" is an input (piece ei3). |
| reg 19(3.1) lead-in | src:351 | encoded | `er2-record-of-employment` the `reg 19(3.1)(a)`, `(b)` rules | The electronic form; the text of s 2(3) of the Act makes "in electronic form" an ordinary form of the record. |
| reg 19(3.1)(a) | src:352-354 | encoded | `er2-record-of-employment` `reg 19(3.1)(a) the last day for sending the electronic record of employment to the Commission`; `... was sent in time` | The earlier of two days; limb (ii) is a candidate only with 13 or fewer pay periods a year (13 itself counts). Asserted. |
| reg 19(3.1)(b) | src:355 | encoded | `er2-record-of-employment` `reg 19(3.1)(b) the electronic record of employment has been kept and retained` | An input, as for (3)(c). |
| reg 19(4) lead-in | src:356 | encoded | `er2-record-of-employment` `reg 19(4) what the employer must do with the employee's copy` | The condition is "for reasons beyond the employer's control ... unable to deliver ... within the time limit": an input. |
| reg 19(4)(a) | src:357 | encoded | `er2-record-of-employment` the same rule, constructor `er2 mail the copy to the insured person` |  |
| reg 19(4)(b) | src:358-361 | encoded | `er2-record-of-employment` the same rule, constructor `er2 retain the copy ...`; `reg 19(4)(b) the day on which the employer may stop retaining the copy` | The earliest of three events; 52 weeks is 364 days. Asserted. |
| reg 19(5) | src:362 | fork | `er2-record-of-employment` `reg 19(5) the person may provide a statement of their hours of insurable employment and insurable earnings` | F1: How far "because the employer's records are destroyed or lost" reaches; read as attached to the last alternative only. |
| reg 19(6) | src:363 | fork | `er2-record-of-employment` `reg 19(6) the hours of insurable employment and insurable earnings are determined from the payroll and personnel records of the bankrupt employer` | F2: "has not provided a record of employment to an insured person or to the Commission": read as to either of them. |
| Heading "Hours of Insurable Employment for Record of Employment" | src:365 | inert | - | A division title over regulation 20 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 20 | src:366 | encoded | `er2-record-of-employment` `reg 20 the hours reported are the hours determined under Part I` | The determination is Part I's (pieces ei1, ei2, er1, er3): an input. |
| Heading "Insurable Earnings" | src:368 | inert | - | A division title over regulation 21 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 21 | src:369 | encoded | `er2-record-of-employment` `reg 21 the insurable earnings reported are the insurable earnings determined and allocated` | The allocation is regulation 23; the determination is Parts III and IV (piece ei3): an input. |
| Heading "Allocation of Hours of Insurable Employment to the Qualifying Period" | src:371 | inert | - | A division title over regulation 22 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 22(1) lead-in | src:372 | fork | `er2-allocation` `reg 22(1) a period of employment falls partially within the claimant's qualifying period` | F17: Which period is tested for "partially within" (the period of employment), and what "52 weeks or less" counts (364 days). |
| reg 22(1)(a) | src:373 | fork | `er2-allocation` `reg 22(1)(a) the period over which the total number of hours worked is allocated` | F17: The whole period of employment if 364 days or fewer, otherwise the period the record covers. Asserted at 364 and 365 days. |
| reg 22(1)(b) | src:374 | encoded | `er2-allocation` `reg 22(1)(a), (b) the hours allocated to the qualifying period, before any fraction of an hour is counted`; `reg 22 the hours of insurable employment counted within the claimant's qualifying period` | Hours per day times the days shared with the qualifying period; evidence of the hours actually worked governs ("unless"). Asserted. |
| reg 22(2) | src:375 | fork | `er2-allocation` `reg 22(2) a fraction of an hour counted as a whole hour` | F3: CEILING; applied to the allocation, not to hours given by evidence. |
| Heading "Allocation of Insurable Earnings" | src:377 | inert | - | A division title over regulation 23 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 23(1) lead-in | src:378 | fork | `er2-allocation` `reg 23 the method of allocating insurable earnings` | F5: The text does not rank subsections (1), (2) and (3); the order taken is (2), (3), (1.1), (1), then (4). |
| reg 23(1)(a) lead-in | src:379 | encoded | `er2-allocation` `reg 23(1) the method of allocating a payment under paragraphs (a) to (c)` | Pay "in respect of a pay period" other than paragraph (b) remuneration. |
| reg 23(1)(a)(i) | src:380 | encoded | `er2-allocation` method constructor `er2 to the pay period in proportion to the hours worked during each day of the period`; `reg 23(1)(a)(i) the part of the remuneration allocated to a day in proportion to the hours worked` |  |
| reg 23(1)(a)(ii) | src:381 | encoded | `er2-allocation` method constructor `er2 to the period of leave at the rate at which the period was compensated`; `reg 23(1)(a)(ii) the part of the remuneration allocated to a period of leave at the rate at which it was compensated` |  |
| reg 23(1)(a)(iii) | src:382 | encoded | `er2-allocation` method constructor `er2 proportionately over the whole period of leave`; `reg 23 the part of an amount allocated proportionately to a stretch of days` |  |
| reg 23(1)(b) | src:383 | fork | `er2-allocation` `reg 23(1)(b) the remuneration is one of the items listed in paragraph (b)` | F4: "not paid in respect of a pay period" read as qualifying only wages in lieu of notice and vacation pay. |
| reg 23(1)(c) | src:384 | encoded | `er2-allocation` `reg 23(1) the method of allocating a payment under paragraphs (a) to (c)` (the not-paid-in-respect arm) | Same method as (b): over the pay period in which it is paid. |
| reg 23(1)(d) | src:385 | encoded | `er2-allocation` `reg 23(1)(d) the unpaid remuneration is allocated as if it had actually been paid in the normal course of business` | Decided by s 2(2) of the Insurable Earnings and Collection of Premiums Regulations (not deposited): an input. |
| reg 23(1.1) | src:386 | encoded | `er2-allocation` `reg 23(1.1) the remuneration referred to in paragraph (1)(b) is allocated over the last pay period for which regular pay is paid` | Moves only paragraph (b) payments, not paragraph (c). Asserted. |
| reg 23(2) | src:387 | fork | `er2-allocation` `reg 23(2) the insurable earnings are allocated over the term of the contract` | F5: Taken before (1) and (3) because it applies "regardless of the basis on which they are paid". |
| reg 23(3) | src:388 | fork | `er2-allocation` `reg 23(3) the insurable earnings are allocated over the shorter of the period of employment and the last 52 weeks`; `reg 23(3) the number of days over which the insurable earnings are allocated` | F5: F5 for the ranking; F18 for the unpaid-leave weeks, which are subtracted from the days of the base. |
| reg 23(4) | src:389 | encoded | `er2-allocation` `reg 23(4) none of subsections (1) to (3) applies to the insurable earnings`; `reg 23(4) the number of days over which the insurable earnings are allocated` | The residual rule. |
| reg 23(5) | src:390 | encoded | `er2-allocation` `reg 23(5) the employer may estimate the insurable earnings for the pay period` | An employer's privilege (Hohfeld), asked in the seat as what the person may expect. |
| reg 24 | src:391 | fork | `er2-allocation` `reg 24 the insurable earnings allocated to the week` | F19: The earnings (less lay-off and separation pay) are spread evenly over the days of the period of employment and the week takes the days it shares; evidence governs. |
| reg 24.1 lead-in | src:392 | encoded | `er2-allocation` `reg 24.1 the insurable earnings paid or payable by reason of lay-off or separation that are counted` | The lesser of (a) and (b). |
| reg 24.1(a) | src:393 | encoded | `er2-allocation` the same rule, first argument |  |
| reg 24.1(b) and the formula | src:394-397 | encoded | `er2-allocation` the same rule, `A TIMES 0.18` | A is the earnings in the calculation period without the lay-off pay: an input (piece ei1). Asserted at the equal case. |
| reg 24.2 | src:398 | repealed or blank in this text | - | [Repealed, SOR/2013-45, s. 3]; kept as a labelled stub `regulation 24.2 - repealed, and therefore not encoded`. |
| Heading "Exclusion of Certain Insurable Earnings in the Calculation of the Rate of Weekly Benefits of a Self-employed Person" | src:400 | inert | - | A division title over regulation 24.3 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 24.3 lead-in | src:401 | encoded | `er2-allocation` `reg 24.3 the insurable earnings are not taken into account in the rate of weekly benefits of a self-employed person` | Paragraphs (a) and (b) are alternatives. |
| reg 24.3(a) | src:402 | encoded | `er2-allocation` the same rule, first two arguments | The meanings of paragraphs 29(b.1) and (c) of the Act (piece ei2) are inputs. |
| reg 24.3(b) | src:403 | encoded | `er2-allocation` the same rule, `earned before the beginning of a prior benefit period` | In the qualifying period and strictly before the first day of the prior benefit period; none, no exclusion. Asserted. |
| Heading "Week of Benefits" | src:405 | inert | - | A division title over regulation 25 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 25(1) | src:406 | fork | `er2-claims` `reg 25(1) the number of weeks of benefits that the claimant is considered to have been paid` | F6: FLOOR of the total percentage over 100: 150 is one week. |
| reg 25(2) | src:407 | fork | `er2-claims` `reg 25(2) the percentage of benefits paid for a week` | F20: The quotient is multiplied by 100 so that a full week is 100, as (1) reads. |
| Heading "Election to Receive Benefits Payable Under Part I or VII.1 of the Act" | src:409 | inert | - | A division title over regulation 25.1 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 25.1 | src:410 | encoded | `er2-claims` `reg 25.1 the election referred to in subsection 152.09(1) of the Act is made as required` | "In writing" is not "on paper" (s 2(3) of the Act). |
| Heading "Claim for Benefits" | src:412 | inert | - | A division title over regulation 26 and 26.1 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 26(1) | src:413 | encoded | `er2-claims` `reg 26 the last day for making the claim for a week of unemployment`; `reg 26 the claim for a week of unemployment is made in time` | Three weeks after the Saturday that ends the week claimed; the last day counts (keel F4). Asserted. |
| reg 26(2) | src:414 | fork | `er2-claims` the same rule, the 4-week arm | F21: Four or more consecutive weeks without a claim, counted back from this claim; then one week. Asserted at 3 and 4. |
| reg 26.1(1) lead-in | src:415 | encoded | `er2-claims` the rules for the two definitions below | A definition for this section only; the rules are named `reg 26.1(1) ...`. |
| reg 26.1(1) "condition of entitlement to benefits" | src:416 | encoded | `er2-claims` `reg 26.1(1) condition of entitlement to benefits` | Subsection 49(1) of the Act is piece ei2: the fact that it is one is an input. |
| reg 26.1(1) "period of eligibility" lead-in | src:417 | encoded | `er2-claims` `reg 26.1(1) the period of eligibility` | NOTHING for benefits the definition does not name (regular, sickness). Asserted. |
| reg 26.1(1) "period of eligibility" (a) lead-in | src:418 | fork | `er2-claims` the same rule, the first arm | F7: The waiting period "added" to the period is added at its end. |
| reg 26.1(1) "period of eligibility" (a)(i) to (v) | src:419-423 | encoded | `er2-claims` the same rule: the period fixed by whichever of ss 22(2), 23(2), 23.1(4), 23.2(3), 23.3(3) applies is one input | One period input, because each reason has exactly one of the five sections (piece ei1 decides which). |
| reg 26.1(1) "period of eligibility" (b) | src:424 | encoded | `er2-claims` the same rule, the apprenticeship arm |  |
| reg 26.1(1) "period of eligibility" (c) | src:425 | encoded | `er2-claims` the same rule, the work-sharing arm |  |
| reg 26.1(2) lead-in | src:426 | encoded | `er2-claims` `reg 26.1 the claimant is not required to make periodic claims on the day` | All four conditions together, and subsection (3). |
| reg 26.1(2)(a) | src:427 | encoded | `er2-claims` `reg 26.1(2)(a) the claim is an initial claim or one to which subsection 26(2) applies` |  |
| reg 26.1(2)(b) | src:428 | encoded | `er2-claims` `reg 26.1(2)(b) the claimant's period of eligibility ends after June 26, 1999` | 26 June 1999 itself is not "after". Asserted. |
| reg 26.1(2)(c) lead-in | src:429 | encoded | `er2-claims` `reg 26.1(2)(c) the claimant makes a claim for every week of unemployment in the period of eligibility, for a reason in (i), under section 25 or under section 24` |  |
| reg 26.1(2)(c)(i) | src:430 | encoded | `er2-claims` `reg 26.1(2)(c)(i) the benefits are for a reason set out in paragraph 12(3)(a), (b), (d), (e) or (f) of the Act` | Sickness (paragraph 12(3)(c)) is not in the list: finding 1. Asserted. |
| reg 26.1(2)(c)(ii) | src:431 | encoded | `er2-claims` the (c) rule, the apprenticeship input |  |
| reg 26.1(2)(c)(iii) | src:432 | encoded | `er2-claims` the (c) rule, the work-sharing input |  |
| reg 26.1(2)(d) lead-in | src:433 | encoded | `er2-claims` `reg 26.1(2)(d) the claimant completes the Commission's form stating (i), (ii) and (iii)` |  |
| reg 26.1(2)(d)(i) | src:434 | encoded | `er2-claims` the (d) rule, second input |  |
| reg 26.1(2)(d)(ii) | src:435 | encoded | `er2-claims` the (d) rule, third input; `reg 26.1(2)(d)(ii) the claimant must notify the Commission as soon as possible` | The claimant's undertaking, stated as the duty it creates. |
| reg 26.1(2)(d)(iii) | src:436 | encoded | `er2-claims` the (d) rule, fourth input; `reg 26.1(2)(d)(iii) the day at the end of the period of eligibility on which the claimant must notify the Commission` |  |
| reg 26.1(3) | src:437 | fork | `er2-claims` `reg 26.1(3) section 26.1 still applies to the claim on the day` | F8: The section stops applying on the day the Commission becomes aware; it still applies the day before. Asserted. |
| Heading "Persons with Mental Disabilities, Incapacitated Persons and Deceased Persons" | src:439 | inert | - | A division title over regulation 27 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 27(1) | src:440 | encoded | `er2-claims` `reg 27(1) payment of the benefits must be authorized to the person acting on behalf of the claimant` | Whether the person meets Parts I, VII.1 or VIII is an input. |
| reg 27(2) | src:441 | encoded | `er2-claims` `reg 27(2) payment of the benefits must be authorized to the legal representative of the deceased person` |  |
| reg 27(3) | src:442 | encoded | `er2-claims` `reg 27(3) legal representative` | The executor or the administrator. |
| reg 27(4) lead-in | src:443 | fork | `er2-claims` `reg 27(4) the person may make a claim for benefits notwithstanding subsection (2)`; `reg 27(4) the benefits are payable to the person entitled to succeed to the property of the deceased person` | F9: The "where the total value of the estate" clause conditions the benefits being payable, not the right to claim. |
| reg 27(4)(a) | src:444 | encoded | `er2-claims` `reg 27(4) the total value of the estate of the deceased person is not sufficient to warrant obtaining a grant`, intestate arm |  |
| reg 27(4)(b) | src:445 | encoded | `er2-claims` the same rule, testate arm |  |
| reg 27(5) lead-in | src:446 | encoded | `er2-claims` `reg 27(5) the claim for benefits is made on the form and includes the declaration and the undertaking` |  |
| reg 27(5)(a) | src:447 | encoded | `er2-claims` the (5) rule, second input |  |
| reg 27(5)(b) | src:448 | encoded | `er2-claims` the (5) rule, third input |  |
| reg 27(6) lead-in | src:449 | encoded | `er2-claims` `reg 27(6) the applicant submits the copy of the will, if one exists, and the release signed by all other persons entitled to succeed` |  |
| reg 27(6)(a) | src:450 | encoded | `er2-claims` the (6) rule, the will limb | Required only if a will exists. |
| reg 27(6)(b) | src:451 | encoded | `er2-claims` the (6) rule, the release limb | Required only if there are other persons entitled to succeed. |
| Heading "Payments in Advance" | src:453 | inert | - | A division title over regulation 28 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 28 lead-in | src:454 | encoded | `er2-claims` `reg 28 the Commission may pay benefits for the week of unemployment in advance of the customary time` | A power of the Commission: the rule says when it has the power, not that it uses it. |
| reg 28(a) | src:455 | encoded | `er2-claims` the reg 28 rule, first input |  |
| reg 28(b) lead-in | src:456 | encoded | `er2-claims` the reg 28 rule, second and third inputs |  |
| reg 28(b)(i) | src:457 | fork | `er2-claims` `reg 28(b)(i) the week is the week in which Christmas Day falls or the week that precedes it` | F22: Weeks run Sunday to Saturday; Christmas Day is 25 December of the year in which the week's Sunday falls. Asserted for 2025, 2026, 2027. |
| reg 28(b)(ii) | src:458 | encoded | `er2-claims` the reg 28 rule, third input |  |
| reg 28(c) | src:459 | encoded | `er2-claims` the reg 28 rule, fourth input |  |
| Heading "Employed Person Working a Full Working Week - Special Cases" | src:461 | inert | - | A division title over regulation 29 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 29(1) lead-in | src:462 | encoded | `er2-full-working-week` `reg 29(1) the claimant is considered to have worked a full working week during each week in the two-week period` |  |
| reg 29(1)(a) | src:463 | encoded | `er2-full-working-week` the reg 29(1) rule, first input |  |
| reg 29(1)(b) | src:464 | encoded | `er2-full-working-week` the reg 29(1) rule, second input |  |
| reg 29(1)(c) | src:465 | encoded | `er2-full-working-week` the reg 29(1) rule, "not less than twice the maximum weekly insurable earnings" | The maximum weekly insurable earnings is section 14(1.1) of the Act (piece ei1): an input. 1500 against 750 is enough; 1499.99 is not. Asserted. |
| reg 29(2) lead-in | src:466 | encoded | `er2-full-working-week` `reg 29(2) the claimant employed in farming or horticulture is considered to have worked a full working week` | "Notwithstanding section 31". |
| reg 29(2)(a) | src:467 | encoded | `er2-full-working-week` the reg 29(2) rule, days |  |
| reg 29(2)(b) | src:468 | encoded | `er2-full-working-week` the reg 29(2) rule, hours |  |
| reg 29(3) | src:469 | encoded | `er2-full-working-week` `reg 29(3) the claimant is regarded as having worked a full working week despite a holiday` |  |
| reg 29(4) | src:470 | encoded | `er2-full-working-week` `reg 29(4) the week is a full working week for the insured person` | Only a week that falls wholly in the period counts. Asserted. |
| Heading "Self-employed Person Working a Full Working Week" | src:472 | inert | - | A division title over regulation 30 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 30(1) | src:473 | fork | `er2-full-working-week` `reg 30(1) the claimant's work in the week is of a kind that is considered a full working week, before subsections (2) and (4)`; `reg 30 whether the claimant is considered to have worked a full working week in the week` | F10: "Subject to subsections (2) and (4)": those two prevail; how regulation 30 sits beside 29 and 31 is not stated. |
| reg 30(2) | src:474 | encoded | `er2-full-working-week` `reg 30(2) the claimant is not regarded as working a full working week in respect of that employment or engagement` | The "minor extent" standard is a judgment: an input. |
| reg 30(3) lead-in | src:475 | encoded | `er2-full-working-week` `reg 30(3) the circumstances to be considered in determining whether employment or engagement is of a minor extent` | A list of what is considered, not a computation. |
| reg 30(3)(a) to (f) | src:476-481 | encoded | `er2-full-working-week` the six constructors of `er2 Circumstance considered in judging whether employment is of a minor extent` | Asserted: six, in order. |
| reg 30(4) lead-in | src:482 | encoded | `er2-full-working-week` `reg 30(4) the claimant employed in farming is not considered to have worked a full working week in the week` |  |
| reg 30(4)(a) | src:483 | encoded | `er2-full-working-week` the reg 30(4) rule, "did not work" input | What the claimant "proves" is an input. |
| reg 30(4)(b) | src:484 | encoded | `er2-full-working-week` the reg 30(4) rule, "minor extent" input; `reg 30(4) the period that begins with the week in which October 1st falls ...` |  |
| reg 30(5) lead-in | src:485 | encoded | `er2-full-working-week` `reg 30(5) self-employed person` |  |
| reg 30(5)(a) | src:486 | encoded | `er2-full-working-week` the reg 30(5) rule, first limb |  |
| reg 30(5)(b) | src:487 | encoded | `er2-full-working-week` the reg 30(5) rule, second limb, calling the core's `s 5(2)(b) employment of a person by a corporation they control` | 40% exactly is not more than 40%. Asserted. |
| Heading "Week of Unemployment - Self-employed Person" | src:489 | inert | - | A division title over regulation 30.1 and 30.2 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 30.1 | src:490 | encoded | `er2-full-working-week` `reg 30.1 the week is a week of unemployment for a self-employed person` | "by more than 40%": exactly 40% is not enough. Asserted. |
| reg 30.2 lead-in | src:491 | fork | `er2-full-working-week` `reg 30.2 the self-employed person is deemed to be not working` | F11: "not engaged in (a) ...; and (b) ...": engaged in neither. |
| reg 30.2(a) | src:492 | fork | `er2-full-working-week` the reg 30.2 rule, first input | F11: As above. |
| reg 30.2(b) | src:493 | fork | `er2-full-working-week` the reg 30.2 rule, second input | F11: As above. |
| Heading "Employed Persons Working a Full Working Week" | src:495 | inert | - | A division title over regulation 31 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 31(1) | src:496 | encoded | `er2-full-working-week` `reg 31(1) the number of hours, days or shifts in a full working week` | NOTHING for a claimant referred to in section 29 or 30. |
| reg 31(2) | src:497 | fork | `er2-full-working-week` `reg 31(2) the number of hours, days or shifts that makes a full working week for a part-time claimant`; `reg 31 the claimant has worked a full working week` | F12: "has worked the number": at least the number. |
| reg 31(3) | src:498 | encoded | `er2-full-working-week` `reg 31(3) the number of days in a full working week for a claimant remunerated on a piece, mileage or other unit rate`; `reg 31 the number of hours, days or shifts that makes a full working week for the claimant` |  |
| Heading "Working Day" | src:500 | inert | - | A division title over regulation 32 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 32 | src:501 | encoded | `er2-full-working-week` `reg 32 working day` | A public holiday on a weekday is still a working day. Asserted. |
| Heading "Additional Conditions and Terms in Relation to Teachers" | src:503 | inert | - | A division title over regulation 33 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 33(1) lead-in | src:504 | encoded | `er2-teachers` the two `reg 33(1) ...` rules | Definitions for this section only. |
| reg 33(1) "non-teaching period" | src:505 | encoded | `er2-teachers` `reg 33(1) non-teaching period` | "a significant number of people" is a judgment: an input. |
| reg 33(1) "teaching" | src:506 | encoded | `er2-teachers` `reg 33(1) teaching` | A technical or vocational school counts at any level. |
| reg 33(2) lead-in | src:507 | encoded | `er2-teachers` `reg 33(2) the claimant is not entitled to receive benefits for the week of unemployment`; `reg 33(2) the benefits are payable under section 22, 23, 23.1, 23.2 or 23.3 of the Act` | Section 21 (sickness) is not excepted: finding 2. Asserted. |
| reg 33(2)(a) | src:508 | encoded | `er2-teachers` the reg 33(2) rule, fourth input |  |
| reg 33(2)(b) | src:509 | encoded | `er2-teachers` the reg 33(2) rule, fifth input |  |
| reg 33(2)(c) | src:510 | encoded | `er2-teachers` the reg 33(2) rule, sixth input |  |
| reg 33(3) | src:511 | fork | `er2-teachers` `reg 33(3) the amount of benefits payable for the week of unemployment` | F23: "limited to": the lesser of the two amounts; the limit cannot raise the benefit. |
| Heading "Family Supplement - Rate Increase" | src:513 | inert | - | A division title over regulation 34 (the brief's "pure citation or title"): it states no fact and creates no relation (phrasebook 9.4). The words are kept as the `§` heading of the module that encodes the regulation. |
| reg 34(1) | src:514 | encoded | `er2-family-supplement` `reg 34(1) cohabitating spouse or common-law partner` | Section 122.6 of the Income Tax Act is not deposited: the fact is an input. The core's `s 2(1) common-law partner` is the Act's own meaning and is not used. |
| reg 34(2) | src:515 | encoded | `er2-family-supplement` `reg 34(2) the Canada child benefit is deemed to be an overpayment under Subdivision a.1 of Division E of Part I of the Income Tax Act` | A deeming "for the purposes of this section" that depends on the Income Tax Act (not deposited); the rule says only that a Canada child benefit counts. |
| reg 34(2.1) | src:516 | repealed or blank in this text | - | [Repealed, SOR/99-290, s. 1]; kept as a labelled stub `regulation 34(2.1) - repealed, and therefore not encoded`. |
| reg 34(3) | src:517 | fork | `er2-family-supplement` `reg 34(3) the claimant's rate of weekly benefits for the week is to be increased by a family supplement`; `reg 34(3) the month preceding the Sunday of the week` | F24: "the month preceding the Sunday of the week": the calendar month before the month in which that Sunday falls. Asserted for January, February and a leap February. |
| reg 34(4) | src:518 | encoded | `er2-family-supplement` `reg 34(4) the claimant's rate of weekly benefits for the week shall not be increased` |  |
| reg 34(5) lead-in | src:519 | fork | `er2-family-supplement` `reg 34(5) the table row for the family income`; `reg 34(5) the family supplement` | F13: The bands have no room for cents and stop at $25,921: both are "not covered" (NOTHING). Asserted. |
| reg 34(5) table, header rows | src:520-522 | fork | `er2-family-supplement` the ladder in `reg 34(5) the table row for a family income in whole dollars` | F13: Emitted from the raw file by script; each band starts one dollar above the end of the one before (the script checks it). |
| reg 34(5) table, rows for 1, 2 and 3 children | src:523-525 | encoded | `er2-family-supplement` fields `er2 supplement for one child`, `... two children`, `... three children` | Asserted at the band edges. |
| reg 34(5) table, top-up for each additional child | src:526 | encoded | `er2-family-supplement` field `er2 top-up for each additional child` | From the fourth child. Asserted. |
| reg 34(5) table, age supplement for each child under 7 | src:527 | encoded | `er2-family-supplement` field `er2 age supplement for each child under 7 years old` | Asserted. |
| reg 34(6) lead-in | src:528 | fork | `er2-family-supplement` `reg 34(6) the family supplement after the ceiling` | F14: Section 6(2) of the Act (rounding) is about "this Part" and is not applied to the ceiling. |
| reg 34(6)(a) | src:529 | encoded | `er2-family-supplement` `reg 34(6) the percentage of the claimant's weekly insurable earnings that the family supplement shall not exceed`, 1997 | 10%. |
| reg 34(6)(b) | src:530 | encoded | `er2-family-supplement` the same rule, 1998 | 15%. |
| reg 34(6)(c) | src:531 | encoded | `er2-family-supplement` the same rule, 1999 | 20%. |
| reg 34(6)(d) | src:532 | encoded | `er2-family-supplement` the same rule, 2000 or later | 25%; NOTHING for a benefit period established before 1997. |
| reg 34(7) lead-in | src:533 | fork | `er2-family-supplement` `reg 34(7) the additional amount for the week` | F15: Whether (5) "results in a reduction" is a comparison with rules this text does not give: an input. F16: the addition is made after the ceiling of (6). |
| reg 34(7) table, header rows | src:534-536 | fork | `er2-family-supplement` the ladder in `reg 34(7) the table row for a family income in whole dollars` | F13: Same bands as the first table, emitted from the raw file by script. |
| reg 34(7) table, 12 to 15 years old | src:537 | encoded | `er2-family-supplement` field `er2 additional amount for a child 12 to 15 years old` | Asserted. |
| reg 34(7) table, 16 and 17 years | src:538 | encoded | `er2-family-supplement` field `er2 additional amount for a child 16 or 17 years old` | Asserted. |

Counts: 156 rows over 23 regulations (19, 20, 21, 22, 23, 24, 24.1, 24.2, 24.3, 25, 25.1, 26, 26.1, 27, 28, 29, 30, 30.1, 30.2, 31, 32, 33, 34) and 19 headings: 106 encoded, 29 fork, 19 inert (all of them headings), 2 repealed or blank in this text.

## Fork register

Every ambiguity met in regulations 19 to 34, the readings seen, the one taken (each can be reversed in the one rule named) and the text that licenses each. Forks F1 to F12 and F17 to F24 are readings of words; F13 to F16 concern the figures of reg 34. Entries are "assumed, not ruled".

| id | provision | readings seen | reading taken | text that licenses each |
| --- | --- | --- | --- | --- |
| F1 | reg 19(5) (src:362) | (i) "because the employer's records are destroyed or lost" governs only "is unable to provide information"; (ii) it governs "is not available" too | (i): four alternatives, the employer's unavailability standing alone | "the employer is not available or is unable to provide information respecting the record ... because the employer's records are destroyed or lost": the nearest verb takes the clause; an employer unavailable *because its records are lost* would make no sense |
| F2 | reg 19(6) (src:363) | "has not provided a record of employment to an insured person or to the Commission" means (i) has provided neither; (ii) has failed to provide to at least one | (ii) | reg 19(5) (src:362) uses "has failed to deliver ... to an insured person or to the Commission" for the same two recipients, and the two subsections mirror each other |
| F3 | reg 22(2) (src:375) | the whole-hour rule applies (i) only to the allocation of (1); (ii) also to hours given by evidence | (i) | "Where the allocation referred to in subsection (1) results in a number of hours that contains a fraction": where evidence is provided there is no allocation |
| F4 | reg 23(1)(b) (src:383) | "not paid in respect of a pay period" qualifies (i) only "wages in lieu of notice and vacation pay"; (ii) every item of the list | (i) | "overtime pay, shift premiums, ..., separation payments, and wages in lieu of notice and vacation pay not paid in respect of a pay period": the last "and" ties the qualifier to the last two items; under (ii) an overtime payment paid in respect of a pay period would fall into (a), which says "other than the remuneration referred to in paragraph (b)" |
| F5 | reg 23 (src:378-389) | subsections (1), (2) and (3) can all apply to one payment and the text ranks none of them | (2), then (3), then (1.1), then (1), then (4) | (2): "regardless of the basis on which they are paid"; (3): the more specific class; (1.1) says it moves "the remuneration referred to in paragraph (1)(b)"; (4): "to which none of subsections (1) to (3) apply". Where (2) and (3) both apply, (2) is taken because "the basis" includes commission |
| F6 | reg 25(1) (src:406) | "when the total of the percentages ... equals 100": (i) one week for each 100 reached (150 is one); (ii) only an exact 100 counts | (i) | "a claimant is considered to have been paid a week of benefits when the total ... equals 100" applied again for each further 100 |
| F7 | reg 26.1(1) (src:418) | "to which is added the waiting period": added (i) at the end of the period; (ii) at its start | (i) | the text gives no place; only the end date matters, to (2)(b) |
| F8 | reg 26.1(3) (src:437) | "shall cease to apply ... as of the date on which the Commission becomes aware": the section (i) no longer applies on that day; (ii) applies through that day | (i) | "as of the date" |
| F9 | reg 27(4) (src:443) | the "where the total value of the estate ... is not sufficient to warrant obtaining ..." clause conditions (i) the benefits being payable; (ii) the making of the claim | (i) | "may make a claim ..., which benefits are payable to the person where": "which benefits" points at payability |
| F10 | regs 29, 30, 31 (src:462-498) | when more than one of the three could describe a claimant, which prevails | each regulation is its own rule; regulation 30 answers `JUST FALSE` where (2) or (4) bars it and `NOTHING` where (1) does not describe the work; regulation 31 answers `NOTHING` for a claimant "referred to in section 29 or 30" | reg 30(1) "Subject to subsections (2) and (4)"; reg 29(2) "Notwithstanding section 31"; reg 31(1), (3) "other than a claimant referred to in section 29 or 30" |
| F11 | reg 30.2 (src:491-493) | "not engaged in (a) ...; and (b) ...": (i) engaged in neither; (ii) not engaged in both | (i) | the two paragraphs are items in a list of things the person "is not engaged in" |
| F12 | reg 31 (src:496-497) | "has worked the number": (i) at least; (ii) exactly | (i) | a person who works more than the full week has worked a full working week |
| F13 | reg 34(5), (7) (src:522, 536) | the bands "$20,921 to $21,250", "$21,251 to $21,500" ...: (i) an income with cents between $21,250 and $21,251 is in no band (not covered); (ii) it belongs to the next band up; (iii) it is rounded | (i); an income above $25,921 is also not covered; the question asks family income in whole dollars | the bands as printed; "Where the source does not answer, return an explicit not-covered value" |
| F14 | reg 34(6) (src:528) | the ceiling is (i) a percentage not rounded; (ii) rounded to the nearest dollar under s 6(2) of the Act | (i) | s 6(2) (Act, src:146) speaks of "a reference in this Part" (Part I of the Act); regulation 34 is not in that Part |
| F15 | reg 34(7) (src:533) | "results in a reduction of the amount of the family supplement payable": reduction compared with (i) what was payable before 1 August 1999 under rules this text does not give; (ii) something computed from the table | (i): the reduction is an input | the text names no comparison amount |
| F16 | reg 34(7) (src:533) | the addition is made (i) after the ceiling of (6); (ii) inside it | (i) | "the amount of the family supplement so calculated will be increased": the increase follows the calculation, including (6) |
| F17 | reg 22(1) (src:372-374) | (i) "partially within" is tested on the period of employment, and the total is allocated over the period of employment if it is 52 weeks or less and over the period the record covers if longer; (ii) the test is on the period the record covers; "52 weeks" is 364 days | (i), 364 days | "a period of employment falls partially within a claimant's qualifying period"; "if that period is 52 weeks or less, or over the period of employment covered by the record of employment if that period is more than 52 weeks"; "week" is seven days (Act s 2(1), src:50) |
| F18 | reg 23(3) (src:388) | "excluding weeks for which the insured person is on unpaid leave": the weeks are removed (i) from the days over which the earnings are allocated; (ii) from the earnings as well | (i) | "allocated proportionately over the shorter of the period of employment and the last 52 weeks, as applicable, excluding weeks ..." |
| F19 | reg 24 (src:391) | the earnings are spread (i) evenly over the days of the period of employment, the week taking the days it shares; (ii) over the weeks | (i) | "proportionately over that period of employment, on the basis that the claimant earned the same amount of insurable earnings for each of the seven days of each week" |
| F20 | reg 25(2) (src:407) | the "percentage" is (i) the quotient times 100; (ii) the bare quotient | (i) | reg 25(1) compares the total with 100 |
| F21 | reg 26(2) (src:414) | "has not made a claim for four or more consecutive weeks": (i) the weeks immediately before this claim; (ii) any such stretch earlier | (i) | "the first claim for benefits after that period" |
| F22 | reg 28(b)(i) (src:457) | the week in which Christmas Day falls: the Sunday-to-Saturday week (s 2(1) "week") containing 25 December of (i) the year in which the week's Sunday falls | (i) | s 2(1) "week" (Act, src:50): seven days beginning on Sunday |
| F23 | reg 33(3) (src:511) | "limited to the amount that is payable in respect of the employment in that other occupation": (i) a ceiling (the lesser of the two); (ii) a replacement (that amount even if larger) | (i) | "limited to" |
| F24 | reg 34(3) (src:517) | "the month preceding the Sunday of the week": (i) the calendar month before the month in which that Sunday falls; (ii) the 30 days before the Sunday | (i) | "month" |

**Where I looked and found no further fork.** Regulation 19(3)(a), (b) and (3.1)(a) (the counting of "not later than five days after" is the keel's F4); regulation 19(4)(b) (the earliest of three events; 52 weeks as 364 days); regulation 24.1 (the lesser of two figures, 18%); regulation 26 (three weeks, one week: counted from the Saturday that ends the week, F4); regulation 26.1(2)(c)(i) (the list is closed and omits sickness); regulations 27(1) to (3), 28, 29, 30(5), 32 and 33(1), (2) (read word for word). Judgments the text hands to a decision-maker are inputs and not forks: "such a minor extent that a person would not normally rely on ... as a principal means of livelihood" (reg 30(2)), "a significant number of people" (reg 33(1)), "for reasons beyond the employer's control" (reg 19(4)).

## Cross-references out of my ranges

A fact decided outside lines 340 to 539 of the Regulations is a plain input, named for the fact, with a comment `-- out of range: ...` where it is used. Terms of the Act's s 2(1) are the keel's rules, called by name (marked "keel").

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| reg 19(1) | s 2(1) "employer", s 5(1)(e) | keel | called: `s 2(1) employer` |
| reg 19(2) | s 5 insurable employment | keel | BOOLEAN `the person is employed by the employer in insurable employment` |
| reg 19(2) | "interruption of earnings", s 2(1); reg 14 | er1 | BOOLEAN `the person has an interruption of earnings` |
| reg 19(3)(c), 19(3.1)(b) | s 87(3) of the Act | ei3 | BOOLEANs `... in accordance with subsection 87(3) of the Act` |
| reg 19(3.1)(a) | reg 1(1) "pay period" | er1 | DATE `the last day of the pay period ...`; NUMBER of pay periods a year |
| reg 19(5) | s 2(1) "claimant" | keel | called: `s 2(1) claimant` |
| reg 20 | Part I of the Act and its regulations | ei1, ei2, er1, er3 | NUMBER `the number of hours ... determined pursuant to Part I` |
| reg 21 | Parts III and IV of the Act; the Insurable Earnings and Collection of Premiums Regulations | ei3; not deposited | NUMBER `the insurable earnings determined ... and allocated` (the allocation is regulation 23 of this piece) |
| reg 22 | s 8 "qualifying period" | ei1 | `Period of days` `the claimant's qualifying period` |
| reg 22, 24 | s 14 "calculation period" | ei1 | periods and amounts as inputs |
| reg 23(1)(d) | s 2(2) of the Insurable Earnings and Collection of Premiums Regulations | not deposited | BOOLEAN `the remuneration remains unpaid for reasons described in subsection 2(2) ...` |
| reg 23(3) | s 12(3) of the Act | keel | NUMBER of weeks of unpaid leave for a reason in subsection 12(3) |
| reg 24.1 | paragraph 14(3)(b) of the Act and the "calculation period" | ei1 | NUMBER `the claimant's insurable earnings during the calculation period, not including ...` |
| reg 24.3 | paragraphs 29(b.1) and (c) of the Act | ei2 | BOOLEANs `... lost because of their misconduct`, `... voluntarily left without just cause` |
| reg 24.3 | paragraph 152.16(1)(b), and the prior benefit period of Part I or Part VIII | ei5, ei1, ei4 | MAYBE DATE `the first day of a prior benefit period ...` |
| reg 25 | s 145 of the Act; the rate of weekly benefits (s 14) | ei4; ei1 | `er2 Week of benefits paid` record (NUMBERs of dollars) |
| reg 25.1 | subsection 152.09(1) of the Act | ei5 | BOOLEANs `the election is made to the Commission`, `... in writing` |
| reg 26.1(1) | subsection 49(1) of the Act | ei2 | BOOLEAN |
| reg 26.1(1) | subsections 22(2), 23(2), 23.1(4), 23.2(3), 23.3(3) of the Act | ei1 | `Period of days` `the period fixed for the benefits by the section of the Act that applies` |
| reg 26.1(1) | section 13 of the Act (waiting period) | ei1 | NUMBER `the number of days of the waiting period that have not already been served` |
| reg 26.1(1), (2)(c) | sections 24 and 25(1)(a) of the Act | ei2 | BOOLEANs `... under section 25 ... apprenticeship`, `... under section 24 ... work-sharing` |
| reg 26.1(1), (2)(c) | paragraph 12(3) of the Act | keel | `Reason for benefits` |
| reg 26.1(2)(d) | sections 19, 22, 23, 23.1, 23.2, 23.3 of the Act (deductible earnings) | ei1 | BOOLEANs |
| reg 27 | Parts I, VII.1 and VIII of the Act | ei1, ei2, ei5, ei4 | BOOLEANs `... meets the requirements of Part I, VII.1 or VIII` |
| reg 28(b)(ii) | paragraph 25(1)(a) of the Act | ei2 | BOOLEAN |
| reg 29(1)(c) | subsection 14(1.1) "maximum weekly insurable earnings" | ei1 | NUMBER `the maximum weekly insurable earnings` |
| reg 30(5)(b) | paragraph 5(2)(b) of the Act | keel | called: `s 5(2)(b) employment of a person by a corporation they control` |
| reg 30.1 | Part VII.1 of the Act | ei5 | none (a rule about the week) |
| reg 30.2 | subsection 152.03(4) of the Act | ei5 | none |
| reg 32 | sections 18 and 152.19 of the Act | ei1, ei5 | none (the rule is the working day) |
| reg 33(2) | sections 22, 23, 23.1, 23.2, 23.3 of the Act | ei1 | `Reason for benefits` (the keel's) |
| reg 33(2), (3) | the qualifying period; the amount payable for other work | ei1 | BOOLEAN/NUMBERs |
| reg 34(1) | section 122.6 of the Income Tax Act | not deposited | BOOLEAN `the person is a cohabitating spouse or common-law partner ...` |
| reg 34(2) | Subdivision a.1 of Division E of Part I of the Income Tax Act | not deposited | BOOLEAN `the payment is a Canada child benefit` |
| reg 34(3) | sections 16 and 152.17 of the Act | ei1, ei5 | BOOLEAN `the claimant establishes, in the manner directed by the Commission ...` |
| reg 34(6) | weekly insurable earnings, subsection 14(2) of the Act; the benefit period established (s 10) | ei1 | NUMBER; DATE |

## Needs from the core

Nothing here blocks the merge; the lead may decide to promote:

1. **`the maximum weekly insurable earnings`** (Act s 14(1.1), piece ei1): a shared NUMBER name. It is an input of reg 29(1)(c) here and of reg 6.1 (piece er1).
2. **A rule giving the section of the Act that pays each `Reason for benefits`** (sickness s 21, pregnancy s 22, a new-born or adopted child s 23, a family member s 23.1, a critically ill child s 23.2, a critically ill adult s 23.3, regular benefits none). `er2-claims` (`reg 26.1(2)(c)(i)`) and `er2-teachers` (`reg 33(2)`) each match the same five reasons by hand; the two regulations are different provisions, so the duplication is kept, but one core rule would show the match once.
3. **The helpers of `er2-common`** (`er2 the later of two days`, `er2 the earlier of two days`, `er2 the number of days two periods have in common`, `er2 a period lies wholly within another`, `er2 the week containing the day`), if other pieces need them. They are arithmetic on days and carry no `@ref`.

## What the text turns out to say

1. Regulation 26.1(2)(c)(i) lists paragraphs 12(3)(a), (b), (d), (e) and (f) of the Act and leaves out (c), a prescribed illness, injury or quarantine: a claimant on sickness benefits is never excused from making periodic claims, however complete the form. Asserted.
2. Regulation 33(2) excepts benefits "payable under section 22, 23, 23.1, 23.2 or 23.3" and not section 21: a teacher on sickness benefits for a week in a non-teaching period is barred, unless the contract has terminated, the teaching was casual or substitute, or they qualify on other work. Asserted.
3. Regulation 19(3.1)(a)(ii) (15 days after the first day of the interruption) is a candidate only when the pay cycle has 13 or fewer pay periods a year; exactly 13 counts; with 14 or more only limb (i), five days after the pay period ends, applies. Asserted.
4. After four or more consecutive weeks without a claim the first claim after them has one week, not three: a claim made a fortnight after the week has ended (13 days after its Saturday) is in time under reg 26(1) and late under reg 26(2). Asserted.
5. Regulation 26.1(2)(b) needs the period of eligibility to end *after* 26 June 1999: a period ending on 26 June 1999 does not qualify. Asserted.
6. Regulation 29(1)(c) is met at exactly twice the maximum weekly insurable earnings ("not less than"): 1,500 against 750 is enough, 1,499.99 is not. Asserted.
7. Regulation 30.1 needs a reduction of *more than* 40% of the normal level: exactly 40% does not make a week of unemployment. Asserted.
8. Regulation 30(5)(b), through paragraph 5(2)(b) of the Act, needs control of *more than* 40% of the voting shares: exactly 40% does not make someone a self-employed person. Asserted.
9. Regulation 32 leaves out only Saturday and Sunday: a public holiday on a weekday is a working day. Asserted.
10. Regulation 34(5): for more than three children the amount is the three-child amount plus the top-up for each child after the third, plus the age supplement for each child under 7. At $23,000 four children is 48.60 + 17.40 = 66.00, and with two under 7, 71.20. Asserted.
11. The tables of regulation 34 leave gaps: there is no band for an income with cents between two whole-dollar bands, and none above $25,921. Both are "not covered" and return NOTHING. Asserted.
12. Regulation 34(6) gives a ceiling of 10%, 15%, 20% and 25% of the weekly insurable earnings for benefit periods established in 1997, 1998, 1999 and 2000 or later; for one established before 1997 the text gives none. Asserted.
13. Regulation 23(1.1) moves only the paragraph (b) payments to the last regular pay period, not paragraph (c) ones. Asserted.
14. Vacation pay and wages in lieu of notice are paragraph (b) items only when not paid in respect of a pay period (fork F4): vacation pay for a period of leave in a pay period is paragraph (a)(ii). Asserted.
15. Regulation 22: 100 hours over a 90-day job with 35 days in the qualifying period is 38.9 hours, counted as 39; evidence of the hours actually worked replaces the allocation. Asserted.
16. Regulation 19(4)(b): the employer keeps an undeliverable copy until the earliest of the Commission's request, the person's request and 52 weeks (364 days) after completion. Asserted.
17. Regulation 25(1): payments of 100% and 50% of the weekly rate make one week of benefits (fork F6), not one and a half. Asserted.
18. Regulation 24.1 counts the lesser of the lay-off or separation pay and 18% of the other earnings; at the equal case it is that amount. Asserted.
19. Regulation 27(4): benefits are payable to the successor only if the estate is too small to warrant a grant *and* the claim meets both (5) and (6): the form, the declaration and the undertaking; the will, if any, and the releases of all others. Asserted.
20. Regulation 28(b)(i): Christmas week is the Sunday-to-Saturday week containing 25 December and the week before it; a week two weeks before or after is not. Asserted for 2025, 2026 and 2027.
21. Regulations 24.2 and 34(2.1) are repealed. Asserted (the stubs return the repeal note).
22. The text does not rank regulations 29, 30 and 31 beyond its own "subject to" and "notwithstanding" (fork F10); the encoding therefore answers each regulation separately.
23. Regulation 34(3) reads the Canada child benefit of the month before the month of the week's Sunday: a week with Sunday 1 March looks to February, a week with Sunday 4 January to December. Asserted.

## What the stable binary does not accept

Binary: `l4 1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`. Measured by this piece (a failing test or a diagnostic, each reproduced in this session):

- **`(NOT (x) OR y)` is read as `NOT (x OR y)`** even with the operand bracketed: `((NOT (a)) OR b)` is the safe spelling. Found by a failing test of reg 27(6) (a will that exists and a copy submitted came out false). Every `NOT` that meets `AND` or `OR` in these files is wrapped as `(NOT (x))`. Silent: exit 0, a wrong answer.
- **`JUST 25%` is `(JUST 25)%`** and fails with "The argument of '%' is expected to be of type NUMBER but is here of type MAYBE OF NUMBER": write `JUST (25%)`. Loud.
- **A record built with `OF` and passed as an argument must be bracketed or named**: `` f `Period of days` OF a, b `` gives "unexpected OF"; write `` f (`Period of days` OF a, b) ``. Loud.
- **`GIVETH A MAYBE (`Period of days`)`** is accepted with the type name bracketed.
- Nothing else in the keel's list was hit: no `REFUSE`, `BECAUSE`, section `GIVEN`, `TYPICALLY`, `WAIT UNTIL` or `YMD` redefinition is used; `YMD` is the core's.

## What check.sh prints

Run as `L4=<l4 1.6.98> L4_TARGET=unstable ./check.sh` in this folder (the binary is the stable `main` build itself, so the main-versus-unstable comparison is skipped and says so):

```
check.sh: the target is unstable, so the main check was skipped.
module                                    errors satisfied  failed  refused  expected
eia-core-insurable-employment.l4               0         0       0        0         0
eia-core-interpretation.l4                     0         0       0        0         0
eia-core-maximum-earnings.l4                   0         0       0        0         0
eia-core.l4                                    0         0       0        0         0
er2-allocation.l4                              0         0       0        0         0
er2-cases-seat.l4                              0       162       0        0         0
er2-claims.l4                                  0         0       0        0         0
er2-common.l4                                  0         0       0        0         0
er2-family-supplement.l4                       0         0       0        0         0
er2-full-working-week.l4                       0         0       0        0         0
er2-record-of-employment.l4                    0         0       0        0         0
er2-seat.l4                                    0         0       0        0         0
er2-teachers.l4                                0         0       0        0         0
er2-tests-allocation.l4                        0       118       0        0         0
er2-tests-claims.l4                            0       129       0        0         0
er2-tests-family-supplement.l4                 0        64       0        0         0
er2-tests-full-working-week.l4                 0        95       0        0         0
er2-tests-record-of-employment.l4              0        58       0        0         0
er2-tests-teachers.l4                          0        34       0        0         0
TOTAL (19 modules)                             0       660       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

`python3 -I srcrefs.py check --refs <the Regulations' raw file> er2-*.l4` prints:

```
srcrefs check: 163 src: lines, 71 runs, 131 locators, 0 problems
```

`l4 check` on every `er2-*.l4` prints no warning and no error, and no "follows code on its line" or "end of the file" note. Every case and test file ends with assertions written equal to assertions satisfied (`grep -c '^#ASSERT'` gives the same count as the satisfied column). No assertion is meant to fail.

## Before this is worth relying on

1. **A person who knows Canadian EI law reads each module against the official text.** This was written from a converter's plain-text rendering; nothing is verified against the official English or French text, and the French was not read.
2. **The 24 forks above are readings taken so that work could go on**; the likeliest to matter to a real answer are F5 (which allocation rule governs), F13 and F16 (the family supplement tables and ceiling), F6 (weeks of benefits) and F9 (who is paid for a deceased claimant).
3. **The two tables of regulation 34 were emitted by script from the raw file**, and a one-off check compared all 147 cells of the generated ladders (21 bands by 5 rows, and 21 by 2) and both header rows with the raw lines; the hand-written tests assert cells from the first, second, third, ninth and last bands of the first table and the first two of the second. The raw file is a converter's rendering, so check the tables against the official ones before use. The family income, the number of children and their ages are inputs; "family income" is itself the Income Tax Act's concept (not deposited).
4. **Facts decided outside the range are inputs**: the maximum weekly insurable earnings, the periods of ss 22(2), 23(2), 23.1(4), 23.2(3), 23.3(3), whether there is an interruption of earnings, the rate of weekly benefits. A caller who supplies them wrongly gets wrong answers; the pieces that own them (ei1, ei2, er1) should be joined at the merge.
5. **Judgments are inputs**, never computed: "such a minor extent that a person would not normally rely on ...", "a significant number of people", "for reasons beyond the employer's control".
6. **The Income Tax Act (s 122.6, Subdivision a.1 of Division E of Part I) and the Insurable Earnings and Collection of Premiums Regulations (s 2(2)) are not deposited**; regulations 23(1)(d) and 34(1), (2) depend on them as plain inputs.
7. **No independent test pass was run** (the brief gives none for this piece): the expectations were written by the encoder, from the text, before each run, which is the weaker check. An independent reader should decide the answers to the 61 seat questions from the text and compare.
8. **The seat has one voice**: the claimant (and, for regulation 27, the person who acts for or succeeds a claimant). An employer's seat, over the same modules, is not written.
