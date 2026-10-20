# Private Health Insurance Act 2007 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the
design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

One module, `phi-cover.l4`, holds the rules and the exported questions (each with
`@export` and `@desc`). One case file, `phi-cases-cover.l4`, is built by the
scratchpad generator `gen_private-health-insurance-act-2007_baseline.py`. Its
expected values were written by hand from the text.

There was no first-pass encoding of this Act to replace.

## Edition

Private Health Insurance Act 2007, Compilation No. 42, compilation date 19 September
2026, includes amendments up to Act No. 90, 2026 (Register id C2026C00412), as
deposited at `../../registers/source-bundle/C2007A00031.txt`.

Two instruments are not deposited:

- the Private Health Insurance (Lifetime Health Cover) Rules 2015;
- the Private Health Insurance (Incentives) Rules.

So everything they settle is an input:

- days of suspended cover;
- classes of people taken to have cover;
- the yearly rebate adjustment factor.

## Checks

- `phi-cases-cover.l4`: 50 assertions written, 50 satisfied, 0 errors, 0 warnings.
- `phi-cover.l4`: checks with no errors or warnings.
- Both were run with the stable `l4` from VS Code extension 1.6.98.

## Seat

**The person deciding on hospital cover.** That is the adult who asks when Lifetime
Health Cover loading starts and how much it will be. The same person asks what rebate
they get and whether an insurer can turn them away. Every duty in Part 2-3 and Part 3-2
falls on the private health insurer ("A private health insurer must increase ...",
"must not ... improperly discriminat[e]"). Each one is encoded as what it means for
that person: what their premium becomes, and what the insurer may not do to them.

The questions:

- `When is my base day`
- `Does lifetime health cover apply to me yet`
- `Do I have hospital cover`
- `What is my lifetime health cover age`
- `Must my premiums be increased for joining late`
- `What is my late-joiner loading in percent`
- `How many days without cover count against me`
- `How many years without cover`
- `What is my lifetime health cover loading`
- `How much is my loading in dollars`
- `How much is our joint loading in dollars`
- `Does the families table apply to me`
- `Which income tier am I in`
- `What is my rebate percentage`
- `How much is my share of the rebate`
- `May my insurer act on this`
- `Must the insurer offer hospital cover`

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The
  Lifetime Health Cover Rules and the Incentives Rules are not deposited, so their
  matters are inputs. The indexed tier thresholds are published figures, not
  legislated ones, so they are inputs too.
- **The actors the text names.** Followed: the adult, the spouse, dependent persons,
  the private health insurer, and the restricted access insurer.
- **A judgment handed to someone else, answered conditionally.** Nothing in scope
  turns on an official's opinion. Section 23-35 revocation, which does ("if the Chief
  Executive Medicare is satisfied"), is out of scope.
- **The Act's own definitions worked out from facts; borrowed terms asked as
  facts.**
  - Worked out from facts: lifetime health cover base day, lifetime health cover age,
    hospital cover, permitted days without hospital cover, years without hospital
    cover, tier 1 to tier 3 earner, family thresholds, and the share of the PHII
    benefit.
  - Asked as facts: "married", "child", "income for surcharge purposes",
    "applicable benefits arrangement", "gold card", "overseas", and the medicare
    eligibility day.
- **One case is the text's natural unit.** Followed: one adult and their hospital
  cover. Joint cover (s 37-20) is for two adults on one policy.
- **The Act's own terms, each with a plain gloss.** Followed in the comments.
- **Operative sections in; machinery out.** Followed. There are two departures, both
  because the deposit drops a formula:
  - **The ss 34-1(2) and 34-5(2) formulas are missing.** They are read as 2% of the
    base rate a year. This is an INFERENCE, kept in one place
    (`the loading per year, in percent`).
  - **The s 22-40(4) child increase and the s 22-45(4) indexation factor are
    missing.** They are inputs, as in the Medicare Levy Act baseline.

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| chloe c073 (1 April 2034), "Turns 31; hospital cover taken out before 1 July to avoid the loading" | `When is my base day`; `Does lifetime health cover apply to me yet`; `What is my late-joiner loading in percent`; `What is my lifetime health cover loading` | Chloe was born 14 March 2003, so her base day is 1 July 2034. On 1 April 2034 lifetime health cover does not yet apply to her (s 37-7). Her lifetime health cover age is 30. She holds cover on her base day, so her loading is 0. Had she waited until 1 August 2034, it would be 2% (age 31 on 1 July 2034). |

The scenario does not say whether Chloe was overseas on 1 July 2034. The cases assume
she was in Australia. In the Medicare Levy Act baseline her income is $71,500 (c048).
Under the assumed thresholds that puts her below the tier 1 threshold here as well,
and that is asserted.

## Why this scope

The Act is large, and most of it regulates insurers:

- their product rules;
- benefit and waiting-period requirements;
- health benefits funds;
- enforcement, the Ombudsman, review.

The seat, and Chloe's one event, need what a person deciding on hospital cover meets:

- when the loading starts and how big it is;
- how it ends;
- what rebate they get, by income tier;
- that the insurer must take them at the community rate.

Also covered: the tier definitions that the Medicare Levy Act baseline borrows
(ss 22-30 to 22-40). They use the same names (`Tier`, `a tier 1 earner`, ...) and
the same stand-in thresholds.

Left out:

- s 22-25 (the 65-and-over percentage after the older person leaves the policy).
- s 22-45 indexation worked out year by year, and the s 22-15(5A) adjustment worked
  out year by year. The results are inputs.
- Division 23 registration, Division 40 notices and records.
- s 45-1 excess levels. They are encoded in the Medicare Levy Act baseline, s 3(5).
- Parts 3-3 and 3-4, except s 102-1. That means benefit requirements, waiting periods,
  portability and transfer certificates.
- Chapters 4 to 6, and machinery.
- Norfolk Island (ss 34-25(4A), (4B), 34-30(1)(a)). A person with it gets
  `Not covered by this encoding`.
- The day that s 34-25(2) preserves. A base day on or before 30 June 2010 is answered
  `My base day on or before 30 June 2010 stands`, because the old day is not worked
  out.

## What the Act turns out to say

1. **The base day is the 1 July *after* turning 31, not after turning 30.** Section
   31-1 says people are encouraged to take out cover "by the time they turn 30", but
   s 34-25(1) sets the base day at "the 1 July after the person turns 31". Someone
   whose 31st birthday is 1 July waits a full year. Asserted (Chloe: 1 July 2034;
   born 1 July 1995: 1 July 2027).
2. **The loading measures age on the 1 July before cover is taken out.** Under
   s 34-1(2), "lifetime health cover age" is "the adult's age on the 1 July before the
   day on which the adult took out the hospital cover". Cover taken out on 1 July
   itself is measured from the year before. Asserted.
3. **The deposit drops the loading formulas.** Sections 34-1(2) and 34-5(2) read
   "worked out as follows:" and then nothing. The encoding infers 2% of the base rate
   a year, which fits the deposit's defined terms and the s 37-15 cap. Every loading
   percentage asserted depends on this inference. Asserted, as an inference.
4. **The 70% cap.** Section 37-15: "any increase under this Part" may not exceed
   "70% of the base rate". Asserted: 72% capped at 70%, and $1,400 on a $2,000 base
   rate.
5. **Non-citizens and returning travellers get a later base day.** For a non-citizen,
   the base day is the later of the 1 July after turning 31 and the first anniversary
   of the medicare eligibility day (s 34-25(3)). For someone overseas on that day, it
   is the first anniversary of their first return of 90 days or more (ss 34-25(4),
   34-30(2)). Asserted.
6. **Permitted days.** After first dropping cover, these days do not count: suspended
   days, days in an absence overseas of more than a year, and "the first 1,094 days"
   of the rest (s 34-20). Every 365 counted days, rounded up, is a year without cover
   (s 34-5(2)). Asserted (2,000 days less 100 suspended, 400 overseas and 1,094 leaves
   406 days, which is 2 years).
7. **The loading ends after 10 years of loaded cover, but can come back.** Under
   s 34-10(1), the loading ends after 10 years of loaded cover. Under s 34-10(3) it
   restarts if cover later lapses with days that are not all permitted. The text does
   not say at what level it restarts. The encoding infers the same percentages.
   Asserted.
8. **People born on or before 1 July 1934 pay no loading** (s 37-1). Asserted.
9. **Joint cover halves the base for each adult** (s 37-20). A 14% loading on one
   partner of a $4,000 couple policy adds $280. Asserted.
10. **No rebate on the loading.** Under s 22-15(6), the rebate percentages apply to
    the premium less the Division 34 increase. Asserted.
11. **Rebate tiers.** The rebate is 30%, 35% or 40% by the age of the oldest person
    insured. It is reduced by 10 points for a tier 1 earner and 20 for a tier 2
    earner, and is nil for a tier 3 earner (s 22-15). The reductions are themselves
    adjusted each 1 April under s 22-15(5A). The Act states only the unadjusted
    figures; the adjusted ones come from the undeposited Incentives Rules. Asserted.
12. **The families table here differs from the Medicare Levy Act's.** Section
    22-30(1)(b) brings in a person who "contributes in a substantial way to the
    maintenance of" a dependent child or sibling. The Medicare Levy Act s 3A(3)
    replaces that with having any dependant. The tables then double the singles
    thresholds (s 22-40). Asserted.
13. **Community rating forbids pricing or refusing by health, claims, occupation or
    risky pastimes.** It allows the lifetime health cover loading, the exclusions of
    restricted access insurers, employer-group discounts, closing products and pilot
    projects (ss 55-5, 55-10, 55-15). But a policy may not be cancelled because the
    person's employment ends (s 55-5(5)). Asserted.
14. **An insurer that sells extras must also sell hospital cover** (s 102-1). Asserted.

## What would need doing before this is worth anything

- Retrieve the authoritative text of the ss 34-1(2), 34-5(2), 22-40(4) and 22-45(4)
  formulas. Confirm or replace the 2% inference.
- Deposit the Private Health Insurance (Lifetime Health Cover) Rules 2015, for
  suspension days, Rules classes and the s 34-20(2) exclusions. Deposit the Incentives
  Rules, for the adjustment factor.
- Deposit the indexed tier thresholds and adjusted rebate percentages for each year.
- Encode s 22-25, the Norfolk Island rules, and the pre-2010 base day.
- An independent test pass and a human gate.
