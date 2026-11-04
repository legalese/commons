# SEAMS (snap1)

Status 2026-11-04. Made by `work/tools/make_notes.py` (the ASKS table is read from the modules); the ANSWERS list is written by hand and checked against the modules named in it.
A seam is a place where my ranges meet another part's or the core's. An input named for the answering function is typed as that function's result; a determination of the Secretary is `MAYBE BOOLEAN`, and `NOTHING` passes through.

## ASKS

What I take as inputs, named for the function that answers it. The answering part, or the merge, supplies the function; until then the caller states the answer.

| input (named for the answering function) | type | read by |
| --- | --- | --- |
| `s 2012(j) the household includes an elderly or disabled member` | MAYBE BOOLEAN | `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross mon...`; `s 2014(c)(2) the household is ineligible because its gross income exceeds the poverty l...`; `s 2014(e)(5)(A) the household is entitled to the excess medical expense deduction`; `s 2014(e)(6)(B) the maximum excess shelter expense deduction on the date`; `s 2014(e)(6)(C)(iv)(I) the standard utility allowance must be made available to the hou...`; `s 2014(g)(1) the resource limit for the household`; `s 2014(g)(1)(A) the household is ineligible because its resources exceed the limit`; `s 2014(k)(4)(A) the energy assistance payment is considered money payable directly to t...`; `s 2014(k)(4)(B) the energy assistance expense is considered an out-of-pocket expense in...` |
| `s 2012(k) the establishment is one described in paragraphs (3), (4) and (9) of section 2012(k)` | BOOLEAN | `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits` |
| `s 2012(k) the group living arrangement is one referred to in section 2012(k)` | BOOLEAN | `s 2018(i)(1)(B) the Secretary may review the program or arrangement`; `s 2018(i)(1)(C) the facility, program or arrangement must submit the information` |
| `s 2012(k)(3) the facility is one referred to in section 2012(k)(3)` | BOOLEAN | `s 2018(i)(1)(A) the Secretary must review the facility`; `s 2018(i)(1)(C) the facility, program or arrangement must submit the information` |
| `s 2012(l) every member of the household is a homeless individual` | MAYBE BOOLEAN | `s 2014(e)(6)(D) the household is entitled to the homeless shelter deduction` |
| `s 2012(m)(4) the individual or group may constitute a household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit`; `s 2014(a) the household is eligible because each member receives general assistance` |
| `s 2012(o)(4) the seller is a private nonprofit cooperative food purchasing venture or an agricultural producer marketing directly to consumers` | BOOLEAN | `s 2019 the retail food store is authorized to redeem the members' food benefits before ...` |
| `s 2015 a provision of section 2015 applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives general assistance` |
| `s 2015(b) the exception in subsection (b) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit` |
| `s 2015(c)(1) the household is required to submit monthly reports of its income and household circumstances` | MAYBE BOOLEAN | `s 2014(f)(2) the basis on which the household's income is calculated` |
| `s 2015(c)(1)(A) the household is specified in clause (i), (ii) or (iii) of section 2015(c)(1)(A)` | MAYBE BOOLEAN | `s 2014(f)(2) the basis on which the household's income is calculated` |
| `s 2015(d)(2) the exception in subsection (d)(2) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit` |
| `s 2015(f)(2)(B) the individual is an alien as described in section 2015(f)(2)(B)` | MAYBE BOOLEAN | `s 2014(i)(1) the income and resources of the sponsor are deemed to be the income and re...` |
| `s 2015(g) the exception in subsection (g) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit` |
| `s 2015(r) the exception in subsection (r) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives a listed benefit` |
| `s 2016(h)(3)(B) the EBT service the store provides is adequate EBT service as described in section 2016(h)(3)(B)` | MAYBE BOOLEAN | `s 2018(g) the approved retail food store has not provided the adequate EBT service` |
| `s 2017 the maximum monthly allotment for the household size, in dollars` | NUMBER | `s 2014(h)(3)(A) the value of the food replaced` |
| `s 2020(e)(25) the Secretary determines that the participation of the private establishment is required to meet a documented need` | BOOLEAN | `s 2018(h) permitted under section 2018(h)`; `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits` |
| `s 2021(a) the retail food store or wholesale food concern has been disqualified under section 2021(a)` | BOOLEAN | `s 2018(b)(2)(A) the buyer or transferee may accept or redeem benefits` |
| `s 2025(e)(1) section 2025(e)(1) applies to the household` | MAYBE BOOLEAN | `s 2014(a) the household is eligible because each member receives general assistance` |

Two asks are not sections:

- **The regulations in force as of June 1, 1982** (section 2014(g)(2)(A)): the input `the regulations in force as of June 1, 1982 include the resource in financial resources` (`MAYBE BOOLEAN`), read by `s 2014(g)(2)(A) the resource is included in financial resources by the regulations in force as of June 1, 1982`. The instrument is not among the sources.
- **The payment error rate** (section 2013(a)(2)): "the meaning given the term in section 2025(c)(2)" is taken as the inputs `the payment error rate of the State for the fiscal year ...` (`MAYBE NUMBER`), one per fiscal year the rule reads.

Differences from the plan's names (PLAN.md section 4):

- `s 2012(j) the household includes an elderly or disabled member` for the plan's per-member `s 2012(j) the member is an elderly or disabled member`: section 2014 asks about a household.
- `s 2012(l) every member of the household is a homeless individual` for the plan's `s 2012(l) the individual is a homeless individual`: section 2014(e)(6)(D) asks about "all members".
- `s 2015(b)`, `s 2015(d)(2)`, `s 2015(g)` and `s 2015(r)` are four inputs, not one: the second sentence of section 2014(a) names those four subsections of section 2015 and the third names "sections 2015" as a whole (`s 2015`) and `s 2025(e)(1)`.

## ANSWERS

What I give to others. Each is a function of mine that the plan, or my reading of the text, says another part asks.

1. **Section 2018(h), for the core's section 2012(k)(3), (4) and (9)** (PLAN.md group B, `permitted under section 2018(h)`, `BOOLEAN`): `s 2018(h) permitted under section 2018(h)`. Inputs: `s 2020(e)(25) the Secretary determines that the participation of the private establishment is required to meet a documented need` (`BOOLEAN`) and `s 2018(h)(2)(A) the operation of the private establishment may continue without the determination of need` (`MAYBE BOOLEAN`). It answers `TRUE` unless the text says no (`NOTHING` becomes `TRUE`, never `FALSE`); the finer `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits` returns the three values.
2. **The Secretary's finding that a tribal organization is capable, for section 2012(s)** (PLAN.md group B, `MAYBE BOOLEAN`): `s 2013(b)(2)(B) the tribal organization is capable of effectively and efficiently administering the distribution`. It passes the finding through (the finding is its input); `s 2013(b)(2) the party that administers the distribution` uses it. Section 2020(d) is asked the same question and is snap4's.
3. **The poverty line, for section 2012(m)(3)** (PLAN.md group B, `NUMBER`): `s 2014(c)(1) the poverty line for the household` (fiscal year, area, household size). It returns `MAYBE NUMBER`: `NOTHING` where the tables hold no row (fiscal year other than 2027, size 0). The core multiplies the line by 1.65; the merge must decide what a missing line means, since `NOTHING` cannot be turned into a number.
4. **Income of the others, excluding the spouse, for section 2012(m)(3)** (PLAN.md group B, `NUMBER`): `s 2014(d) household income`, over the list of the others' counted monthly amounts and the reduction of paragraph (9). The caller builds the list with `s 2014(d) the monthly amount of the item that counts as income`.

Offered to the parts that cite section 2014 (PLAN.md group C, from references only, lists sections 2015, 2016, 2017, 2020, 2026, 2027, 2031 and 2035) as separate functions, not one large rule:

- income: `s 2014(d) household income`, `s 2014(d) the monthly amount of the item that counts as income`, and the exclusions `s 2014(d)(1)` to `s 2014(d)(19)`;
- deductions and net income: `s 2014(e)(1) the standard deduction for the household`, `s 2014(e)(2)(B) the earned income deduction`, `s 2014(e)(3)(A) the dependent care deduction`, `s 2014(e)(4)(A) the child support deduction`, `s 2014(e)(5)(A) the excess medical expense deduction`, `s 2014(e)(6) the excess shelter expense deduction`, `s 2014(e) the household's income after the deductions other than the shelter deduction`, `s 2014(e) the household's net income`;
- the limits: `s 2014(c)(1) the poverty line for the household` (USDA Table 1), `s 2014(c)(2) the gross monthly income limit for the household` (USDA Table 2, the published whole-dollar figure), `s 2014(c) the USDA's Table 3 limit for the household` (USDA Table 3, for the core's `s 2012(m)(3)`); `s 2014(c)(2) the household is ineligible because its gross income exceeds the gross monthly income limit`;
- eligibility: `s 2014(a) the household is eligible because each member receives a listed benefit`, `s 2014(a) the household is eligible because each member receives general assistance`, `s 2014(c) the household is ineligible on income`, `s 2014(g)(1)(A) the household is ineligible because its resources exceed the limit`, `s 2014(j) the member is considered to have satisfied the resource limitations of subsection (g)`;
- the basis of calculation: `s 2014(f)(2) the basis on which the household's income is calculated`;
- sponsored aliens: `s 2014(i)(1) ...`, `s 2014(i)(2)(A) ...`, `s 2014(i)(2)(B) ...`, `s 2014(i)(2)(D) ...`;
- section 2013 and 2018: `s 2013(b)(3) the individual is not eligible to participate in the supplemental nutrition assistance program` (a disqualification from the reservation program bars SNAP), `s 2018(b)(2)(A) the buyer or transferee may accept or redeem benefits`.
