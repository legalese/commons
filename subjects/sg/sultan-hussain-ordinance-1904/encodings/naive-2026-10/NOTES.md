# Sultan Hussain Ordinance 1904 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/SHO1904.txt`. The deposit says it incorporates all
amendments up to and including 1 December 2021. The latest amending Act in its
Legislative History is Act 23 of 1999 (in force 21 July 1999). After it come
G.N. No. S 61/2000, which appointed 1 March 2000 "for purposes of section 4A", and
the 2000 Revised Edition.

**Checks:** one case file, 41 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0252** in `subjects/sg/requirements.jsonl`: Tier 4 of the
remaining Singapore Acts, ordered by how much they touch everyday life. The
requirement asks what the Act decides for a person or business it applies to. No
scenario has asked a sharper question yet. The Act has four sections, so all of the
operative text is encoded: s 2 (the Kampong Glam land), s 3 (the annuity scheme) and
s 4 (non-assignability). The regulations made under s 3 were not retrieved, so the
proportions and the amount of any commuted gratuity are not known here.

## What the Act turns out to say

### 1. The beneficiaries are a closed class, and the scheme ends in 2030

s 3(2): the annuity "shall be paid only to members of the family ... who before
4 May 1999 were receiving an annuity under the Ordinance". A descendant born later, or
a family member who was never on the earlier annuity, can never qualify. s 3(1) sets
the scheme at "30 years from 1 March 2000". When those 30 years run out, or the last
qualifying person dies or commutes, the Ordinance has nobody left to pay. The
encoding reads the period as ending before 1 March 2030; the text gives no end date,
so that boundary is an inference. Asserted.

### 2. The cut-off date is the day the amending Bill was first read

The Legislative History gives 4 May 1999 as the First Reading of Bill 15/1999, which
became Act 23 of 1999. So the class was fixed on the day the Bill was introduced in
Parliament, not when it came into force (21 July 1999). That date link comes from the
history, which is "not part of the Ordinance". The encoding reads "before" strictly:
someone first paid on 4 May 1999 does not qualify. Asserted.

### 3. The $350,000 figure is ambiguous on the face of the text

s 3(1) reads "a scheme for the payment of an annuity to the family ... a sum of
$350,000 for a period of 30 years". The sentence is ungrammatical. It does not say
whether $350,000 is paid each year or once over the 30 years. The encoding records only
the figure and draws nothing from it. Asserted (the figure only).

### 4. The sums cannot be assigned or taken by creditors, whatever the debt

s 4: the sums "shall not be assignable or transferable or liable to be attached,
sequestrated or levied upon for or in respect of any debt or claim". The text makes no
exception for any kind of creditor. Two questions stay open: whether the protection
covers money once it is paid out, and whether it covers a commuted gratuity paid to an
estate, which is not obviously "the family". Asserted for each of the five dealings.

### 5. Most of the scheme lives in regulations the Act only permits

s 3(3) lets regulations divide the annuity, give an annuitant the option of a commuted
gratuity "in lieu of the annuity", and pay a commuted gratuity to an annuitant's estate
on death. The encoding assumes the regulations use all three powers. It also infers
that someone who has already commuted leaves nothing further for their estate under
(c), because they are no longer "a person to whom annuity is payable". Asserted, with
both inferences labelled.

### 6. The land question was settled before the Ordinance, in the preamble

s 2 says the Kampong Glam land, "having reverted to the State", is to be administered
by the Collector of Land Revenue like other State land. The reason appears only in the
preamble: the Court of Appeal's judgment of 23 December 1897 that the land was Crown
land, occupied "without legal right or title". The Ordinance gives the family money,
not land. Asserted (s 2 only).

## What would need doing before this is worth anything

- Retrieve the regulations made under s 3: the proportions, how the commuted gratuity
  is calculated, and whether $350,000 is an annual figure.
- The text does not define "member of the family". Find out who was on the pre-1999
  annuity and on what terms; the deposit no longer contains those provisions.
- Check whether s 4 protects money after it is paid, and whether it reaches an estate's
  gratuity.
- No case law or parliamentary debate (Bill 15/1999) was read.
