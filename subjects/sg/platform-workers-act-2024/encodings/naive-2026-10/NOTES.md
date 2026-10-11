# Platform Workers Act 2024 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** the Act as enacted, Act 30 of 2024 -- not a revised edition.

**Checks:** two case files, 85 assertions satisfied (35 in `pwa-cases-coverage.l4`, 50 in
`pwa-cpf-contributions-cases.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**21 of the 527 Singapore Acts** deposited here cite it, 10 to 14 times each for ss 3,
4 and 5: the CPF, Work Injury Compensation and Income Tax Acts extend to "platform
workers" through these definitions. This row encodes the definitions, the
association-rights guarantee, insolvency priority, and the strike ballot.

## What the Act turns out to say

### 1. Only delivery and ride-hail are covered

s 3(1) and First Schedule para 1: a "platform service" means **delivery service** or
**ride-hail service**, nothing else. A cleaner, tutor or handyman on a tightly
controlled app is outside the Act until the Schedule is amended. Taxi call-booking,
permitted car-pooling and licensed cross-border ride-hail are excluded from ride-hail.
Asserted.

### 2. Working through an app is presumed to be management control

s 6(1): management control needs algorithmic data use to decide eligibility, allocation
or pay, without routine human intervention, **and** a Second Schedule restriction
(service rules, no fare negotiation, no own clientele, limits on hours or tasks,
systematic incentives or penalties). But s 6(4): control is **presumed**, unless
disproved, wherever the worker must take tasks through the operator's app or
website. Almost every app platform starts presumed in. Asserted.

### 3. Employees are not platform workers

s 5(2): the worker's "agreement" excludes a contract of service. An employed rider is
an employee under the Employment Act, not a platform worker. s 5(1)(d): the worker
must be in Singapore when providing the service. Asserted.

### 4. Individual members can be fined for an unballoted strike

s 36: a registered platform work association needs a majority secret ballot of the
affected members before any strike. Members who take part in one without the ballot
commit an offence ($2,000 each) (s 36(3)), as well as the association and its executive
($3,000). Asserted.

### 5. Smaller things worth recording

- **s 7:** any term restricting a worker's right to join or organise a platform work
  association is void.
- **ss 16 to 18:** unpaid platform earnings rank first among platform claims in the
  operator's insolvency (capped by order), then work injury compensation, then CPF.
- **s 4(2):** subcontracting the service or the control does not stop the principal
  being the platform operator.

## CPF contributions on platform earnings (added 11 October 2026 for REQ-0267)

Module `pwa-cpf-contributions.l4`, cases `pwa-cpf-contributions-cases.l4`. The Act does this by
amendment: s 97 and the Fourth Schedule para 4 insert s 8A into the CPF Act, and para 19 inserts a
new CPF Fourth Schedule, "Platform worker contributions". The question's "Part 3" is Part 3 of
that inserted Schedule (Group A rates). Because the Schedule has since been amended by
notification (S 1026/2024, S 886/2025), it was read against the CPF Act deposit (version in force
from 1 July 2026) as well; the 40 Group A rate bands and the Group B table are identical in both.

1. **The answer to REQ-0267.** A worker born in 2006 is a Group A worker (para 5(a): born on or
   after 1 January 1995). In March 2027 para 16 applies ("each relevant month starting on or after
   1 January 2027"), band (a), 35 or below: the operator pays **26% of APE** to the Fund, of which
   it may deduct **15.5% of APE** from his earnings (s 8A(1), (2)); the operator's own share is
   10.5%. Rounding: the contribution to the nearest dollar, 50 cents up; the deduction with cents
   dropped (para 9(b), (c)).
2. **The figure turns on his vehicle.** The rates apply to "aggregate platform earnings", which are
   earnings less a fixed expenses deduction by mode of transport (paras 1 to 3): 60% for a car, 35%
   for a motorcycle, power-assisted bicycle or PMD, 20% on foot, by bicycle or public transport. On
   $2,900 the ledger does not say which, so all three are asserted:
   - motorcycle, power-assisted bicycle or PMD: APE $1,885; **operator pays $490, deducts $292**,
     bears $198;
   - car or van: APE $1,160; operator pays $302, deducts $179, bears $123;
   - on foot, bicycle or public transport: APE $2,320; operator pays $603, deducts $359, bears $244.
3. **Where this differs from the expectation.** The ledger assumed full employee-equivalent rates
   for a worker born after 1994. Not so in 2027: Group A rates are phased in by calendar year
   (paras 14 to 18), for band (a) 14%/10.5% in 2025, 20%/13% in 2026, **26%/15.5% in 2027**,
   32%/18% in 2028, and only from 1 January 2029 37%/20%, the employee rates. Even then they apply
   to APE, not gross earnings, so on $2,900 by motorcycle the 2029 contribution would be $697 (not
   37% of $2,900 = $1,073). Birth cohort decides the GROUP (A or B), not the rate step; the year
   decides the step.
4. **Group B** (born before 1995 and not opted in, para 8) pays a single, lower table (para 19:
   8% to 10.5% of APE above $750), and the whole contribution is recoverable from the worker; only
   rounding leaves the operator a dollar. A Group B worker may opt into Group A, irrevocably
   (para 4).
5. **Para 8 oddity.** The CPF deposit's para 8, as amended by S 886/2025, says Group B is a worker
   born before "1 January 2026" (the Act as enacted said 1995). Para 8 is "subject to paragraph 5",
   so a worker born in 1995 or later is still Group A; the amendment is recorded, not explained.
6. **Combined ceiling** (para 10, recast by S 1026/2024): no contribution on total APE in a year
   above the "applicable amount", $102,000 (First Schedule para 5(da)). Applied in the encoding by
   cutting down the month's APE (inference). The variants where the operator also pays wages, or is
   a related contributor (paras 10A to 10C), are not encoded.
7. **Provisional deduction** (para 13(1)(b)): the operator may deduct as if APE exceeded $750 and
   must refund any excess within 14 days after the month (para 13(3)). Encoded as the top
   recoverable rate on the APE (inference).
8. **Age band timing** (para 9(a)): read as in the CPF row, the age in completed years at the end of
   the previous month, "above 35" meaning 36 or more on that count. Inference; CPF Board practice
   may switch bands from the month after the birthday of the band's lower age. Irrelevant to
   REQ-0267, where he is 20 or 21.
9. **Not in the deposit:** regulations under CPF Act s 77(1), to which s 8A(1) is "subject" (they
   may confine the duty to citizens and permanent residents or make other exclusions); any
   Gazette notification of "excluded payments" from platform earnings; the commencement
   notification (the CPF deposit's own note gives "wef 15/12/2024"). The answer assumes Jun Hao is a
   citizen or permanent resident covered by s 8A, that the $2,900 is all platform earnings from one
   operator, and that none of it is excluded.

## What would need doing before this is worth anything

- **The regulations and orders** (prescribed classes, the earnings cap) were not
  retrieved.
- The consequential provisions in the Work Injury Compensation Act, which give platform
  workers insurance, are not followed here; the CPF contribution rules are (section above).
- **No case law** yet exists on most of this Act; none was searched.
