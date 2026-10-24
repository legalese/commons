# Seafarers Rehabilitation and Compensation Act 1992 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill, with a second seat layer for the employer.
There is no REFUSE in it; employment the Act does not reach answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0069` in `subjects/au/requirements.jsonl` (priority 2, the 20 topics: work injury and workplace safety). No scenario life raised it, so every case is hypothetical. There was no earlier encoding of this Act to keep.

## Edition

Compilation No. 34, compilation date 21 February 2025, includes amendments up to Act No. 14, 2025 (register id **C2025C00116**, Federal Register of Legislation, retrieved 13 October 2026), as deposited at `../../registers/source-bundle/C2004A04525.txt`.

The formulas the deposit lost are taken from the sidecar `../../registers/source-bundle/C2004A04525.formulas.md` (transcribed 2026-10-24 from the authorised Word rendering of the same compilation, each checked against its equation image), used by `sea-formulas.l4` (added 2026-10-24).

Nothing else is brought in. The approved Guide, the Minister's travel rate, and the Seafarers Regulations are not deposited. The CPI- and WPI-indexed amounts (ss 23, 23A) and AWOTE are inputs, each `@desc` giving the compilation's printed figure.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `sea-employee.l4` (the seafarer, 11 questions) | `sea-cases-employee.l4` | 55 written, 55 satisfied |
| `sea-seat-employer.l4` (the employer, 5 questions) | `sea-cases-employer.l4` | 15 written, 15 satisfied (9 mirror cases) |
| `sea-formulas.l4` (the seafarer, 5 questions, imports `sea-employee`) | `sea-cases-formulas.l4` | 26 written, 26 satisfied |

`l4 run` on all six files: 0 errors, 0 warnings (2026-10-23; again 2026-10-24 with the formulas module, the 70 earlier assertions unchanged and still satisfied). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seats

**The employee (first seat, `sea-employee.l4`):** a seafarer employed on a prescribed ship, a trainee, or a seafarer registering at a Seafarers Engagement Centre. "I was injured as a seafarer on a ship the Act covers. Am I covered, and what compensation do I get?" For compensation on death the question is the dependant's.

**The employer (second seat, `sea-seat-employer.l4`).** Under this Act the employer, not a government body, is liable to pay compensation "in full" (s 25) and determines the claim (s 24), within time limits (ss 72, 73, 73A, 79), and must be insured (s 93). It is the other party the text puts duties and liabilities on, so it has a seat. The layer calls the employee module's rules for the time limits, the weekly amount and permanent impairment, and adds insurance and the reconsideration time limit. The two seats define no name twice; mirror cases agree.

The 2026-10-18 defaults:

- **The Act alone.** Indexed amounts, AWOTE and the approved Guide's percentages are inputs.
- **The actors the text names:** the employee, the employer, the master of the ship, dependants, the Seafarers Safety, Rehabilitation and Compensation Authority, Comcare officers and industry panels, the ART.
- **Judgments handed to others are answered conditionally:** material contribution to a disease, what the employee can earn in suitable employment (s 32), serious and wilful misconduct, the degree of impairment, whether a late notice is excused.
- **The Act's own definitions are worked out from facts:** employee and seafarer (ss 3, 4), injury and disease (s 3), the s 9 circumstances, the s 31(5) percentages and minimum earnings, dependant. Borrowed terms are asked as facts: prescribed ship (Navigation Act), trading, financial or foreign corporation, pension age, the shipping registers.
- **One case:** one employee, one employment, one injury.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** Parts 6 onwards (insurance beyond s 93, the Fund, the Authority), levies.

## Scope

**Added 2026-10-24 (`sea-formulas.l4`):** s 13(1)–(6) (normal weekly earnings), s 28(6A) (the travel amount), s 31(2) (the first 45 weeks in dollars, in a dollar question covering every week), s 41 (non-economic loss), ss 23(4)–(6), 23A(2)–(4) (one year's indexation of an amount). The **Out** list below is as written on 2026-10-23; ss 13, the s 28 travel amount, the s 31(2) amount and s 41 have left it.

**In:** ss 3 (injury, disease, seafarer), 4(1), 9(2), (3), (4), 19(1), (1AA), (2)–(4), 20, 20A, 26, 28(2), (6), (7) (eligibility), 29(2)–(4), 31(2) as a band, (4)–(11), (14) (as an input), 38, 39(3)–(9), 62, 63, 72, 73, 73A, 76 (reviewable decision), 78(2), (3), 79(1), (2), (6), 88(1), (2), 93(1), (1A), (2).

**Out:** ss 5, 7, 10 (diseases presumed for maritime work), 11, 13 (normal weekly earnings: its formula is lost), 27, 28 amounts, 29(5), 30, 31(2) amount (formula lost), 31(12), (13) (asked as a count), 32–37, 40(1)–(3), 40(4) (in a comment), 41 (formula lost), 42–47, Part 3 (rehabilitation), Part 4 (common law), ss 64–71, 74, 75, 79(3) (medical examination extension), 80–87, 89 onwards.

## What the Act turns out to say

1. **The deposit has lost several formulas.** Sections 13 (normal weekly earnings), 23A(3), 28(6A)(b), 31(2) and 41(2) read "the formula: where:" with nothing between. Unlike the Comcare Act, s 31(5) states the later weeks' amounts in words, so they are computed; the first 45 weeks are answered as a band, not an amount. A `C2004A04525.formulas.md` sidecar is needed (raised in the ledger). Asserted (the band).
2. **The employer pays, and must decide quickly or be taken to refuse.** The employer determines liability (s 24) within 12 days for incapacity, property and medical claims (or 12 days after receiving what it asked for), 60 days for death and 30 days for permanent impairment (extended by the days a request for information was outstanding), or a period the Authority allows; otherwise the claim is taken to be disallowed at the end of the period (ss 72(5), 73(6), 73A(6)). Asserted from both seats.
3. **Journeys between home and work are covered, unlike under the Comcare Act.** Section 9(2)(e)(i) treats an injury while travelling between residence and work as arising out of employment, unless the route or an interruption substantially increased the risk (s 9(3)). Asserted.
4. **A disease needs only a "material degree" of contribution**, lower than the SRC Act's "significant degree"; the exclusion is narrower too: reasonable disciplinary action, or failure to get a promotion, transfer or benefit (s 3), not all reasonable administrative action. Asserted.
5. **A seafarer's first 45 weeks start when they are put ashore.** For a seafarer, the s 31(2) weeks are "the first 45 weeks ... after the date on which the seafarer is left on shore at, or returned to, his or her home port" (s 31(3)); the input counts weeks that way. Not asserted (an input's meaning).
6. **After 45 weeks the step-down is 75% to 100% of normal weekly earnings, with a cap and a floor.** The percentage turns on hours employed as a share of normal weekly hours, boundaries in the lower band (s 31(5)); any work as a seafarer in the week counts as 100% (s 31(6)); the amount is cut to 150% of AWOTE (s 31(7)); and an amount for a week of no employment is raised to the minimum earnings, the lesser of $254.46 plus $62.99 for a dependent prescribed person and $31.50 per dependent prescribed child, and 90% of normal weekly earnings (s 31(8)–(11), as printed in this compilation and indexed by CPI under s 23). Asserted.
7. **Weekly compensation stops at pension age, or after 52 weeks for an injury in the year before it**, half the SRC Act's 2 years and 104 weeks (s 38(1), (2)). Asserted.
8. **Permanent impairment has one threshold and no separate hearing rule.** Nothing below 10% except the loss of a finger, toe, taste or smell (s 39(7), (8)); no binaural hearing threshold as in the SRC Act. The maximum printed is $100,778.56, CPI-indexed. Asserted.
9. **Only the claimant may go to the ART, and only after reconsideration.** A reviewable decision is one under s 78 (s 76); the request must be made within 30 days after the determination came to the claimant's notice (s 78(3)); the employer must reconsider within 60 days, extended by outstanding requests, or is taken to have disallowed the claim (s 79). Asserted from both seats.
10. **The employer must be insured every day for its full liability**, through an authorised insurer, an approved P&I club in the International Group, or an approved employers' mutual; a strict liability offence of 50 penalty units (s 93). Asserted.
11. **The Act's coverage turns on the ship's trade or the employer's character.** A prescribed ship in overseas, interstate or territory trade, or coastal trading under a general licence (s 19(1), (1AA)), or any employment by a trading, financial or foreign corporation (s 19(2)–(4)); not a ship on the Australian International Shipping Register, not a Comcare employee (s 20), not exempt employment (s 20A). Asserted.

12. **The formulas are now in, from the sidecar (2026-10-24).** Finding 1 is answered for ss 23A(3), 28(6A)(b), 31(2) and 41(2): `sea-formulas.l4` gives the first 45 weeks as "Normal weekly earnings − Earnings in suitable employment", the private-car travel amount, and non-economic loss in dollars, and a dollar question for any week that takes the s 31(5) amount from `sea-employee.l4` after the first 45. The one earlier case with a dollar amount for the same facts (the low earner after 45 weeks, $360) is reproduced by the new question: no disagreement. Asserted.
13. **Section 13 never had a formula.** Finding 1 and the ledger entry (REQ-0105) list s 13 among the provisions whose formula was lost; the deposit and the authorised rendering both state normal weekly earnings in words: the weekly salary under the contract immediately before the injury (a seafarer, s 13(1), or anyone else, (4)), the salary that would have applied after training (a trainee, (2)), or the amount an industrial instrument specifies (a Seafarers Engagement Centre, (3)), increased by the percentage of an age, service or increment rise (5) and moved with the class's rates (6). The sidecar has no s 13 entry because there was no image. Encoded from the words. Asserted.
14. **The first 45 weeks are uncapped and have no floor.** The s 31(7) cap at 150% of AWOTE and the s 31(8) minimum earnings both act on an amount "worked out under subsection (5)", which is the later weeks only; in the first 45 a high earner gets normal weekly earnings less earnings in suitable employment in full, and a low earner gets no top-up. Asserted.
15. **The s 41(2) figure is printed in the formula itself.** The formula reads $18,895.98, a figure already indexed (s 23 lists s 41(2) as a relevant amount); the module takes the figure in force as an input, the compilation's figure standing in. A negative s 31(2) result is read as nil (an INFERENCE). Asserted.
16. **"Calculated to 3 decimal places" is read as truncation**, completing a round-half-up with the 0.001 rule of ss 23(6) and 23A(4); substitution only for a factor greater than one, on the last substituted amount. No index numbers are deposited, so the amounts in force remain inputs. Asserted.

## What would need doing before this is worth relying on

- **The indexed amounts** in force for the year asked: the ABS December-quarter CPI and WPI index numbers deposited, so `sea-formulas.l4`'s indexation question can produce them; and the Minister's rate per kilometre.
- **Section 10** (diseases presumed for maritime employment) and the Minister's instrument, and **Part 3** (rehabilitation).
- **Wider sources.** No Authority guidance, decision or case law was read.
