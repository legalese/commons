# Environmental Public Health Act 1987 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (amendments to Act 5 of
2023, in force 1 July 2023).

**Checks:** two case files, 75 assertions satisfied (littering 34, cleaning wages 41), 0 errors, 0 warnings.

## Why this Act, and why scoped

**14 of the 527 Singapore Acts** deposited here cite it. This row takes the Part 3
public cleansing offences: littering, spitting, high-rise litter, spillage from
vehicles, illegal dumping, penalties and corrective work orders. Refuse collection,
industrial waste, waste collector licensing, pneumatic waste systems, food
establishments and hawkers, and nuisances are not encoded.

## What the Act turns out to say

### 1. Litter from a flat is presumed to be the tenants' or the owners'

s 17A (in force 1 July 2023): litter proved to have come from a residential flat is
presumed to have been thrown by **every tenant** if the whole flat was leased, otherwise
by **every owner**. The presumption is rebutted by proving any of:
- someone else did it
- the presumed offender was absent
- the presumed offender named the person they reasonably believe did it within 14 days
  of being asked

A landlord whose whole flat is let is not presumed. Asserted.

### 2. A dumping vehicle can be forfeited without anyone being convicted

s 20(6): on proof that a seized vehicle was used for illegal dumping, the court "is to"
forfeit it "even though no person may have been convicted". s 20(8): if there is no
prosecution, it is forfeited 3 months after seizure unless claimed. A second dumping
conviction carries a **mandatory** prison term of 1 to 12 months (s 21(1)(a)).
Asserted.

### 3. Corrective work orders are the default for littering

s 21A: on a s 17 or s 19 conviction of anyone aged 16 or over, the court "is to" make
a corrective work order "unless it has special reasons for not so doing", if satisfied
it is expedient. The order is capped at 12 hours in total (s 21A(2)) and 3 hours a day
(s 21B(3)). Asserted.

### 4. Smaller things worth recording

- **s 17(1)(g):** spitting and expelling nasal mucus in public are offences.
  **(1)(c):** so is drying anything in a public place.
- **s 17(7), 19(5), 20(4):** a vehicle or flat owner asked to identify the culprit cannot
  refuse on grounds of self-incrimination.
- **s 19(3)(a):** spillage from a vehicle is deemed the driver's offence unless the real
  culprit can be identified.
- **s 21(1)(c):** fines rise from $2,000 to $4,000 to $10,000 on the first, second and
  third convictions.
- **s 21(8):** cleaning costs can be recovered from an offender's employer.

## What would need doing before this is worth anything

- The composition (fixed-penalty) regime under s 108 is how most littering is dealt with
  in practice. It was not read.
- Part 4 (hawker and food establishment licensing) would be the natural next scope.
- No case law was searched.

## Cleaning wages (added 12 October 2026 for REQ-0275)

Module `epha-cleaning-wages.l4`, cases `epha-cases-cleaning-wages.l4` (41 assertions). Raised by the Jun Hao scenario,
event j088 (Jun Hao scenario, 2056): the lowest monthly basic wage a licensed cleaning business may pay a general cleaner
in February 2056, and where it is written.

1. **The Act does not contain the figure.** It is in an order of the Commissioner for Labour under **s 80H(2)(a)**, which
   "must, by order, specify ... the minimum amount of basic wage and the date that minimum amount takes effect", with
   different amounts for different classes of cleaners (s 80H(3)). The order binds the employer through a licence condition
   under **s 80H(1)(b)**, which exists only if regulations under s 111 prescribe it. Neither the order nor the regulations
   were deposited, so the amount, its effective date and whether the condition is prescribed are all inputs. The cases use
   made-up figures ($3,000 then $3,200 from 1 July 2055) and say so; they are not the 2056 order.
2. **The ledger named the wrong section.** s 31AA is the progressive wage condition for the **waste collection** industry
   (and s 23A for waste disposal). The cleaning industry's is s 80H, in Part 9A ("General Cleaning Industry"). Asserted.
3. **The floor protects resident cleaners only.** s 80H(1)(b) covers "every cleaner who is a citizen or permanent resident of
   Singapore". The question does not say whether the cleaner is one; for a foreign cleaner the Act sets no basic-wage floor
   (the encoding returns 0, meaning "none under this Act"). The Employment Act 1968 and the contract were not read.
4. **"General cleaner" is not a term of the Act.** It would be a class in the Commissioner's order (s 80H(3)); the Act's own
   term is "cleaner" (s 2), which covers anyone engaged to clean, or to supervise cleaning, for someone other than the
   employer, full-time, part-time or casual, and anyone the Minister gazettes as a cleaner.
5. **The effective date can be postponed** by the Director-General's written notice for cleaners working under a cleaning
   contract made before that date (s 80H(7)). Whether any such notice covers February 2056 is a fact outside the Act.
6. **A lower collective-agreement wage does not reduce the floor** (s 80H(6)). That the higher of the two is owed when the
   agreement pays more is an inference, labelled as one in the module.
7. **Sanctions.** Breaking the condition can lead to revocation or suspension of up to 6 months (s 80J(1)(k), (2)(a)) and a
   financial penalty of up to $5,000 (s 80K(1)), but for the basic-wage condition only after the Director-General has
   consulted the Commissioner for Labour (ss 80J(4), 80K(2)), and after a hearing window of 3 to 14 days (s 80J(3)).
   Carrying on a cleaning business unlicensed: up to $10,000 or 12 months or both, plus $1,000 a day continuing (s 80D(2));
   engaging an unlicensed cleaning business for one's own premises: up to $10,000, plus $1,000 a day, with a no-knowledge
   defence (s 80E). Asserted.
8. **Text problems in the deposit.** s 80D(3)(b) is garbled in the .txt (a stray "(b) the person, having -- (i) to achieve a
   stated result ... (ii) to supply ... plant or equipment" before the real (b)); it was read as one paragraph. The deposit's
   footer says "version in force from 1/7/2026", later than the edition line at the top of these notes, which predates
   this addition.

**Needs, for a full answer:** the Commissioner for Labour's basic-wage order under s 80H(2) in force in February 2056
(with its class for general cleaners), the regulations under s 111 prescribing the licence conditions (the cleaning
business licensing regulations), any Director-General postponement notice under s 80H(7), and the cleaner's residency.
