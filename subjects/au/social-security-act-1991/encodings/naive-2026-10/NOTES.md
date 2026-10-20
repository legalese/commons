# Social Security Act 1991 — naive encoding

**Method: naive.** Straight from the deposited text. The `writing-l4-rules`
skill was not available in this session, so the encoding follows the conventions
of the finished naive encodings instead. No pipeline, no coverage table, no
independent test pass, no human gate. NOT for public use.

**Edition:** Compilation No. 232, compilation date 1 July 2026, includes amendments
up to Act No. 17, 2025 (register id C2026C00336, in 6 volumes), deposited at
`../../registers/source-bundle/C2004A04121.txt`. The deposit's metadata warns that a
version in force from 20 September 2026 has no registered compilation yet, so
amendments commencing on or after that date may be missing.

**Checks:** one module (`ssa-payments.l4`) and one case file (`ssa-cases-payments.l4`):
49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This encoding answers **REQ-0005** in `subjects/au/requirements.jsonl` (priority 1). The
three Western Australian cradle-to-grave lives raise it 9 times:

- **chloe c079** (2037-05-02): Graham turns 67. He is refused the Age Pension on the
  assets test but granted the seniors health card.
- **chloe c093** (2070-03-14): Chloe turns 67 and is refused the Age Pension on assets.
- **daniel d083** (2063-04-09): Daniel turns 67. No Age Pension.
- **jake k095** (2073-08-30): Jake turns 67. He moves from the Disability Support
  Pension to the Age Pension.
- **jake k091** (2063-04-28): the Disability Support Pension on exactly 20 impairment
  points. **jake k093** (2065-05-01): a review that finds him still qualified.
- **jake k086** (2055-11-30): redundant at 49. What does JobSeeker require?
- **jake k092** (2063-05-15): Ruby, his daughter, gets Carer Allowance.
- **daniel d020** (2014-02-24): Youth Allowance refused on parental income.

The scope is those provisions and the definitions, conditions and exceptions needed to
answer them:

- pension age, s 23(5A)–(5D)
- 10 years qualifying Australian residence, s 7(5)
- the age pension, ss 43, 44 and the s 1064 income and assets tests (Modules A, E, G)
- the seniors health card, s 1061ZG and the s 1071 income test
- the disability support pension, ss 94 and 103(2)
- jobseeker payment, s 593, with the liquid assets waiting period, ss 14A and 598
- youth allowance age, ss 540 and 543–543B, and the parental income test in s 1067G
- carer allowance for a disabled adult, ss 954, 954A and 957A

The rest of a 6-volume Act is left out. That includes every payment rate and its
indexation, the supplements, deeming, the rules on what counts as income or as an asset,
the homeowner definition, financial hardship, the other jobseeker waiting periods,
employment pathway plans, independence for youth allowance, the maintenance income test,
carer allowance for children and its rate, and review and appeal (which sit in the
Administration Act, not deposited). The Impairment Tables and the Adult Disability
Assessment Tool are legislative instruments, also not deposited.

**Inputs.** The Act does not state the figures in force on any scenario date:
- maximum payment rates
- assets value limits and income free areas
- the seniors health card income limit
- the parental income free area (set by the Family Assistance Act)

These are inputs. The case file uses **illustrative** figures and says so. **The
scenarios give no asset or income figures for any of the lives.** The asset values in
the cases are invented to show the shape of each refusal the scenarios record.

## What the Act turns out to say

### 1. The deposit has lost four formulas, including the assets test taper

The `.txt` conversion dropped every formula typeset as an equation:

- **Point 1064-E10:** "A person's reduction for ordinary income is:" and nothing follows.
- **Table G-2:** column 3, the reduction for assets, is empty for all three family
  situations.
- **Point 1067G-F28:** the parental income test where siblings share parental income.
- **Section 598(2A):** the liquid assets waiting period formula. Only its terms
  survive.

So the deposit cannot say by how much assets above the limit cut a pension, which is the
question in c079, c093 and d083. The two pension tapers are inputs. Two shapes are
**inferences**:

- F27's result is taken from its surviving Note as (combined parental income − free
  area) / 130, "20 cents for each dollar of the excess" per fortnight.
- s 598's formula weeks are taken as (liquid assets − maximum reserve) / divisor, the
  only arrangement of its three defined terms that gives weeks.

Anyone re-encoding should take these formulas from the PDF. Asserted only through the
inputs and inferences above.

### 2. The dollar figures in Tables G-1, E-1 and B are pre-indexation base figures

Table G-1 prints assets value limits of **$250,000 and $450,000** for a single person
(homeowner and not) and **$187,500 and $287,500** for each member of a couple.
Section 1192(5C)–(5E) shows that these were the figures "immediately before" 1 July 2017,
and they have been indexed every year since. The seniors health card limits ($90,000;
$72,000) are likewise the base for indexation on 20 September 2023 (s 1192(5BB)). None of
them is the limit in force in 2037, 2063, 2070 or 2073. The encoding takes the limit in
force as an input. The cases use the base figures only as illustrations.

### 3. Nothing ends the Disability Support Pension at pension age; Jake has to claim

k095 says that at 67 "the Disability Support Pension gives way to the Age Pension". In
the Act, ss 94–103 set no upper age. Section 103(2) makes the DSP not payable only once
"another social security pension ... becomes payable", and Note 1 says another payment
"will generally not become payable to the person until the person claims it". So the
change is triggered by Jake's claim, not by his birthday. Asserted.

### 4. Jake's review is easier than his first claim

Under s 94(2)(aa), an impairment that is not "severe" (20 points under a single
Impairment Table, s 94(3B)) also needs active participation in a program of support. But
s 94(3A) switches (aa) off when a current recipient is reassessed on a s 63 notice,
unless the person is a reviewed 2008–2011 DSP starter.

Take 20 points split 10 + 10 across two Tables, with no program of support:
- on a first claim, the person is **not** qualified;
- on review (k093), the same person **is** qualified.

Jake's own 20 points "on a borderline table" are treated as all from one Table, so they
are severe and (aa) never applies to him. That is an inference from the scenario's
wording. The rating itself is a clinical input. Who decides a borderline case (k091) is a
question for the Tables and the Administration Act, neither deposited. Asserted.

### 5. Graham's refusal and his card come from the same facts

The Age Pension is refused when the assets reduced rate is nil. Module A Step 11 takes
the lower of the income reduced and assets reduced rates, and s 44 says a pension at a nil
rate is not payable. The seniors health card does not look at assets: s 1061ZG asks for
pension age, residence, presence in Australia, the income test, and that the person is
**not** receiving a pension. So a refusal on assets is close to a precondition for the
card.

The card's income test is strict. The couple's adjusted taxable incomes are added and
halved (1071-11). Income "equal to or exceeds" the limit fails (1071-1 Step 5). Asserted
for c079 with invented figures: the pension is refused and the card granted. The same
figures refuse Chloe (c093) and Daniel (d083), and Jake's modest assets give him the
pension (k095).

### 6. Pension age is 67 for all four lives, reached on the 67th birthday

The man's and woman's tables in s 23(5A) and (5D) both end at "On or after 1 January
1957 — 67 years". Graham (born 1970), Daniel (1996), Chloe (2003) and Jake (2006) all
reach pension age on their 67th birthdays, as the scenarios assume. A day earlier, Jake
has not. Asserted.

### 7. JobSeeker requires the mutual obligation, and unpaid redundancy pay delays it

Section 593(1)(b), by (1AC), requires that the person "satisfies the employment pathway
plan requirements" and is "willing to actively seek and to accept and undertake paid
work in Australia". The age band is 22 to pension age.

Section 14A(1)(c) counts "amounts due, and able to be paid, to the person by ... a former
employer" as liquid assets. So redundancy pay owed to Jake counts towards the waiting
period. For a single person without children:
- the maximum reserve is $5,000 and the divisor $500;
- the waiting period is capped at 13 weeks (s 598(2B));
- $20,000 gives 13 weeks and $8,000 gives 6.

Asserted, on the inferred formula in finding 1.

### 8. Carer Allowance turns on a score, not a payment rate the Act states

Under s 954, Jake must be a family member of Ruby (her parent, s 23(14)) and rated
under the Adult Disability Assessment Tool at **at least 30, on a professional
questionnaire score of at least 12**. Ruby must care for him daily in their shared
home. If they do not share a home, s 954A requires at least 20 hours a week of care for
bodily functions or sustaining life.

The income test is a flat **$250,000** on the couple's adjusted taxable incomes **added
together**, not halved as for the seniors health card (s 957A). What the carer "gets", the
rate, is outside this scope. Asserted.

### 9. Smaller things worth recording

- **s 7(5):** a single period of residence of exactly 10 years qualifies, but several
  periods totalling exactly 10 years do not. The aggregate must "exceed" 10 years, with
  one period of 5 or more. Asserted.
- **d020 is dated 2014,** but this compilation is the 2026 text. The encoding applies
  2026 law to Daniel's 2014 claim, which may not be the law he faced.
- **d020:** Daniel's sister Sofia (14 in 2014) is probably an FTB child of their parents.
  That is an inference. If so, F31 deems her to share parental income with Daniel, which
  sends him to the lost F28 formula, not F27. The encoding takes the F28 result as an
  input. Under Step 13, a nil rate caused by the parental reduction means youth allowance
  "is not payable". Asserted on a supplied figure.
- **Youth allowance age (s 543A(2AA)):** a 16- or 17-year-old in full-time *secondary*
  study does not meet the minimum age unless an exception applies. Daniel, at university,
  does. Asserted.

## What would need doing before this is worth anything

- Recover the four lost formulas (1064-E10, Table G-2, 1067G-F28, s 598(2A)) from the PDF
  and replace the inputs and inferences.
- Supply the indexed rates, limits and free areas for each scenario date. That means
  either the Act's indexation machinery (ss 1190–1194) or published figures.
- Encode what counts as an asset and as income: deeming, the principal home, superannuation
  before and after pension age. Without that, "refused on assets" is only a shape.
- The scenarios need asset and income figures for Graham, Chloe, Daniel and Jake before
  any outcome can be computed rather than illustrated.
- Encode the Social Security (Administration) Act 1999 (claims, reviews, employment
  pathway plans) and the Impairment Tables for k091 and k093.
- Use the 2014 compilation for d020.
