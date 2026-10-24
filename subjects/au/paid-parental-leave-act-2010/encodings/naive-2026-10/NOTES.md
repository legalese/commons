# Paid Parental Leave Act 2010 (Cth) — naive encoding

**Method: naive.** Written straight from the deposited text using the
`writing-l4-rules` conventions and nothing else. No pipeline, no coverage table,
no independent test pass, no human gate. Not for public use.

**Edition:** Compilation No. 48, compilation date 1 July 2026 (includes
amendments up to Act No. 57, 2025), register id C2026C00294, deposited at
`../../registers/source-bundle/C2010A00104.txt`.

**Checks:** one module (`ppl-leave.l4`) and one case file (`ppl-cases-leave.l4`):
55 assertions satisfied, 0 errors, 0 warnings.
Added 2026-10-24: `ppl-leave-formulas.l4` and `ppl-cases-leave-formulas.l4` (16 assertions): 71 satisfied in all, 0 errors, 0 warnings in every file.

## Why this Act, and why scoped

This encoding answers **REQ-0010** in `subjects/au/requirements.jsonl` (priority 1). The three
Western Australian cradle-to-grave lives raise it 7 times:

- Chloe **c061** (2030-08-22): unpaid leave begins and PPL is claimed. How many paid weeks, shared how, paid by whom?
- Chloe **c063** (2030-09-05): Liam's reserved weeks. What is reserved, and what may be transferred?
- Chloe **c071** (2033-04-12): Ella is born, and the same questions come up again.
- Jake **k052** (2033-01-22): is an unmarried mother eligible?
- Jake **k053** (2033-01-22): is a self-employed father eligible, married or not?
- Daniel **d040** (2030-02-02): Luca is born and PPL is shared.
- Daniel **d04c** (2034-04-14): Jarrah pays Chloe's PPL as paymaster. What must the employer do?

The scope is the provisions those events name, plus the definitions, conditions and
exceptions needed to answer them. The encoding covers the day counts and the reserved period
(ss 11D, 31AB, 31ABA), the cap on concurrent days (s 21), who may claim (s 54), what
a partner needs from the birth mother (ss 13, 15), eligibility (s 31AA(2)), the
work, income and residency tests (ss 31A, 32–37, 41, 45, 46), the claim window
(s 60), the instalment (s 65), the continuous flexible period and the employer
determination (ss 71A, 101), who pays and what the paymaster must do (ss 72–74, 84),
and the superannuation contribution (s 115C).

Everything the PPL rules prescribe is an INPUT or is left out. So are the national
minimum wage, the indexed income limits, the Social Security Act meanings ("partner",
"Australian resident", "income support payment"), adjusted taxable income and the SG
charge percentage. Adoption, special claims, stillbirth, COVID-19 claimants, review,
debts and penalties are not encoded.

## What the Act turns out to say

### 1. A child born in 2030 brings 26 weeks, not 24

Section 31ABA(1)(d) gives "130 flexible PPL days" for a child born on or after 1 July 2026.
That is 26 weeks of five week days. Chloe c061 expects `ppl_weeks: 24`, which is the
2025–26 figure (120 days, s 31ABA(1)(c)). Oliver (2030), Luca (2030), Ruby (2033)
and Ella (2033) are all born after 1 July 2026, so each has 130 days. The
deposit is the compilation in force on 1 July 2026, and nothing later was read.
Asserted.

### 2. Jarrah cannot be Chloe's paymaster in April 2034, at least not for Ella

d04c puts Jarrah as paymaster on 14 April 2034. Ella was born on 12 April 2033, and
Chloe joined Jarrah on 1 February 2034. Three things stand in the way:

- A continuous flexible period "ends on ... the day before the child's first birthday" (s 71A(e)(ii)). For Ella that is 11 April 2034, so no such period can start on 14 April.
- An employer determination needs the person "employed by the employer for at least 12 months immediately before" the expected date of birth (s 101(1)(c)).
- It also needs a continuous flexible period (s 101(1)(d)).

An election under s 109 with Chloe's consent lifts paras (b) and (c), but not (d) (s 101(2)).
Any of Ella's days that are still unpaid go to the Secretary, who pays them direct (s 84(2)).
Inference: unless d04c means a later child that the life does not name, the employer's
duties in ss 72–82 do not arise at Jarrah for this claim. Asserted (both with and without
the election).

### 3. The partner's weeks come through the birth mother

The "reserved weeks" are not a separate entitlement for the second parent. They work as a cap
on any claimant who "has a partner at the time ... [of] their first effective claim":
110 days for a child born on or after 1 July 2026, out of 130 (ss 31AB(3), 31ABA(2)). That
leaves 20 days, or four weeks, that no single partnered claimant can take. This matches c061's
`ppl_reserved_for_each_parent_weeks: 4`.

A claimant who is not the birth mother has two further hurdles:

- Unless she has already done so, the birth mother must satisfy the work test (s 13(2)(b)).
- Unless the PPL rules say otherwise, the claimant needs the birth mother's permission under s 15(1)(a), and is paid no more days than that permission names (s 13(2)(d)).

So on c063's question, what "may be transferred" is whatever the birth mother's permission
says. She may vary it or revoke it, but not for days that have already passed (s 15(4)–(7)).
Liam's four weeks depend on Chloe's permission, and on Chloe passing the work test. Asserted.

### 4. No marriage condition anywhere

Section 54(1) lists the people who may claim: the birth mother, an adoptive parent, "a parent ... [who] is not
the child's birth mother", and the partners of each. Section 31AA(2) adds residency, care, no
more than one hour of paid work, the work and income tests, and the waiting period. Neither
mentions marriage.

Jake can claim under s 54(1)(c) as Ruby's parent, whether or not he counts as Tahlia's
"partner". Partner status matters only to the 110-day cap (s 31AB(3)) and to the income
test (s 37(3)). "Partner" takes its Social Security Act meaning, which is an INPUT here
because that Act was not read. The test fixtures carry a `married to the other parent` flag that no
rule reads: Tahlia is eligible either way. Asserted.

### 5. A self-employed father passes the work test on his own business, but must stop working

Section 35(3) counts as paid work "work for the purposes of a business that is carried on for
profit" by the person or an entity the person controls. Under s 35(2), work as an employee of
the person's own company does not count under s 35(1), but the company's business still counts
under s 35(3).

The catch is s 31AA(2)(c): on each paid day the claimant may perform "no more than one hour
of paid work". A sole trader who does three hours of work on a day is not eligible for
that day. Jake has no employer, so no employer determination is made and the Secretary pays
him (s 84(2)). Asserted.

### 6. Both parents at once: 20 days

For a child born on or after 1 July 2025, s 21 stops the Secretary determining a further
day paid to two people once 20 such days have been determined (10 before then). If Liam's four
weeks from 5 September 2030 run alongside Chloe's (an inference from c063's date), they reach
the limit exactly. The PPL rules may exclude
some days from the count (s 21(2)). Asserted.

### 7. The income test has three doors

Section 37 is satisfied if any one of these holds:

- The claimant's own adjusted taxable income is within the individual limit.
- With no partner, the claimant's own income is within the *family* limit.
- With a partner, the combined income is within the family limit.

So a single claimant earning more than the individual limit can still pass. The Act states
only $150,000 (individual, before 1 July 2021) and $350,000 (family, 2023–24). Both are indexed
to CPI after that, so they are INPUTS (ss 41–44). The cases use hypothetical limits.
Asserted.

### 8. Superannuation on PPL

Section 115C: the contribution is "the base contribution ... multiplied by the SG charge percentage",
plus a nominal interest amount set by the rules. The base is the funding amounts paid to the
employer and the instalments the Secretary paid in the income year. The Commissioner of
Taxation pays it, usually in the following income year (s 4 guide). c061's note says "from July
2025". Whatever fixes that date (inference: an application provision in an amending Act)
was not read. Asserted for the formula only, on hypothetical figures.

### 9. Luca's mother and the waiting period (not asserted for her)

Section 31A(1)(b) applies a newly arrived resident's waiting period to someone who "becomes the
holder of a permanent visa". It ends after 104 weeks *in Australia* (s 31A(2)–(4)). Daniel's
life gives Priya a permanent visa in 2027 and a year in London. Whether the 104 weeks were
complete by Luca's birth on 2 February 2030 depends on dates and visa classes the life does not
state. The rule is encoded, and her case is left open.

### 10. What the paymaster must do

The employer must pay the instalment on the usual payday if the instalment is payable, an employer
determination is in force, and the employer "has been paid enough to fund the instalment"
(ss 72(1), 73). It pays only for days in the continuous flexible period (s 72(1A)). Payment must
be in money: cash, cheque or EFT to the person's account (s 74). Section 99A says the duty is
"in addition to any other obligation". Asserted.

The text also requires a record of payment by the end of the next working day (s 80),
records kept for 7 years (s 81), notice of listed events (s 82) and a response to the
determination within 14 days (s 103). Those were read but not encoded. Section 99 says a
period of unpaid leave does not become paid leave because PPL is received. Not asserted.

### 11. The indexed limits, computed from the recovered formula (2026-10-24)

`ppl-leave-formulas.l4` IMPORTs `ppl-leave.l4`, leaves it unchanged, and works out the limits finding 7 takes as inputs. It uses the same arithmetic as the baseline's `ppl-formulas.l4`, and its case file has the same cases:

- **The s 43 indexation factor**, from the formula: the reference December quarter's CPI over the base December quarter's, to 3 places, raised by 0.001 when the fourth place is more than 4, and never below 1.
- **The income limits in force on a day** (ss 41-44): $150,000 (individual) or $350,000 (family) indexed every 1 July from 1 July 2021 or 1 July 2024. The input is a list of December-quarter CPI numbers from December 2007. Each indexation's base quarter is the highest earlier December quarter (s 43(1)). A day after the last CPI number supplied answers `NOTHING`. So does a day before the limit starts.
- **The present value of an unpaid debt** (s 198(6)), for a part-payment agreement under s 198(4)-(5).

The CPI numbers in the cases are illustrative, not the published series, and the settlement interest rate is the Minister's (both inputs). s 44 does not say which way an amount ending in exactly 50 cents goes; it is rounded up (an inference). No computed value disagrees with an existing assertion; the existing questions that take "the indexed amount in force" are unchanged.

## What would need doing before this is worth anything

- The PPL rules (made by the Minister under s 298) were not deposited. They prescribe exceptional
  circumstances, the s 13(2)(d) and s 31AB(3)(d) carve-outs, what counts as paid work and paid
  leave, and the nominal interest method.
- The Social Security Act meanings of "partner", "Australian resident" and "income support
  payment" decide several of the inputs here.
- The scenario's 24 weeks (c061) and d04c's paymaster event should be checked against the text
  above before the lives are replayed.
- Whether a concurrent day counts once or twice toward the child's 130 days (s 31AB(2)) is left
  to the input. A reading of the PPL rules or the departmental guide would settle it.
- Instalment periods and paydays (s 64), PPL funding amounts beyond s 73, employer notices
  (ss 82, 102–105), review and debts are not encoded.
