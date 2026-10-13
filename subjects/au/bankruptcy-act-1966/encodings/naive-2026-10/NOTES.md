# Bankruptcy Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** Compilation No. 97, compilation date 21 May 2026 (includes amendments up
to Act No. 47, 2026), Federal Register of Legislation register id C2026C00215,
deposited at `../../registers/source-bundle/C1966A00033.txt`.

**Checks:** one module (`bda-debt-agreements.l4`), one case file
(`bda-cases-debt-agreements.l4`), 58 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0022** in `subjects/au/requirements.jsonl` (priority 1), raised
**3 times**, all by Jake Harding's life (`au/wa/cradle-to-grave-jake`, born
2006-08-30):

- **k065** (2037-04-20, aged 30): after debts of $41,000 and collectors (k064), a
  creditor's petition is threatened and a debt agreement proposed instead, "accepted
  by a majority of creditors in value". "Who may propose a debt agreement; who
  decides; what does it do to the debts?" (ss 185C, 185EC, 185H).
- **k066** (2037-06-01): "A five-year plan: $690 a month to the administrator" (Part IX
  Division 3).
- **k075** (2042-05-31): the agreement completes. "What stays on the National Personal
  Insolvency Index and the credit file, and for how long?" (s 185N, the Index).

This encoding takes those questions and what they need: who may give a proposal
(s 185C(1), (4), (5), with s 5 "insolvent"), how long payments may run
(s 185C(2AA)-(2AC)), the Official Receiver's gate (s 185E), the applicable deadline
(s 185), the creditors' vote and lapse (ss 185EC, 185G), when the agreement is made
(s 185H), what creditors may do during processing and while it is in force
(ss 185F, 185K), proportionate payment (s 185C(2)(d), (e)), arrears defaults and
termination (ss 185LB, 185LC, 185QA), extension by variation (s 185M(1D)-(1DB)), and
the end of the agreement and the release (ss 185N, 185NA, with s 153(2)).

Not encoded: the s 185C(4)(e) formula (missing from the deposit, see finding 4); every
amount set outside the Act (the threshold amount's Social Security Act rate, any
greater prescribed amount, the Minister's percentage and low income debtor amount),
which are inputs; the Index's contents and retention, which the Act leaves to
regulations; the credit file (Privacy Act 1988 Part IIIA, a separate subject);
statements of affairs and forms; cancellation of acceptance (s 185ED); voting on
variations and terminations; termination by the Court (s 185Q) and voiding
(ss 185T-185V) beyond comments; administrators' duties and registration; Part X; and
bankruptcy itself.

## What the Act turns out to say

### 1. Jake's five-year agreement is one the Act does not allow

The scenario gives Jake "Five years at $690 a month", from 2037-06-01 to completion on
2042-05-31. s 185C(2AA) forbids a proposal providing for payments after "3 years
beginning on the day the agreement is made", or 5 years only "if subsection (2AB)
applies". (2AB) needs an interest in a dwelling that is the debtor's principal place
of residence, and excepts "an interest under a lease (other than a long-term lease)".
In 2037 Jake rents a unit in Gosnells; he owns nothing until 2042. So the longest his
payments may run is to 2040-05-31, and the Official Receiver cannot accept a
five-year proposal for processing, because s 185E(2)(a) requires satisfaction that
(2AA) was complied with. The only route to five years is a later variation under
s 185M(1DB): an administrator's certificate of an unforeseen substantial change in
circumstances, and no increase in the total payments. (Whether the 2038 separation
would qualify is an inference left open.) Asserted.

### 2. Who proposes, who gates, who decides — and the decision is by value of replies

Only an insolvent debtor may give a proposal (s 185C(1)), and never jointly
(s 185C(2E)). The Official Receiver is the gate (s 185E): the s 185C conditions, the
14 days from signing (s 185E(2AA)), and a mandatory refusal if creditors' interests
"would be better served by not accepting" (s 185E(3)). The creditors decide: "a
majority in value of the creditors who reply before the applicable deadline"
(s 185EC(1)(b)). Creditors who do not reply do not count; the proposed administrator
and its related entities are disregarded (s 185EC(1A)); a secured creditor counts
only its shortfall (s 185EC(5)). If no one replies the proposal lapses (s 185G(b)).
The deadline is the 35th day after acceptance for processing, or the 42nd in December
(s 185). Asserted, on an illustrative split of Jake's $41,000; a tie is read as no
majority.

### 3. The agreement stops a creditor's petition and enforcement — and, on its words, wage deductions of any kind

While the agreement is in force and on the Index, a creditor cannot present or pursue
a creditor's petition, or enforce or sue for a provable debt (s 185K(1)); maintenance
and proceeds of crime liabilities may still be enforced (s 185K(2)). But
s 185K(3)(b) says, without limiting it to provable debts, that a person entitled
under any law "to retain or deduct money from money that is or will be owing or
payable to the debtor must not retain or deduct money". s 185F(1)(c) says the same
during processing. On its words that reaches the Registrar's deduction of child
support from Jake's wages in k072 (2039-01-15), while the scenario's agreement is
still running. The encoding follows the words; the Child Support (Registration and
Collection) Act 1988 may answer otherwise and was not read. Asserted.

### 4. The deposit is missing the s 185C(4)(e) formula

s 185C(4)(e) reads "the amount worked out using the following formula (expressed as a
percentage) exceeds the percentage determined in an instrument under subsection
(4B)", and the next line in the deposit is s 185C(4A). The formula (and the matching
one in s 185M(1E)) did not survive conversion. Whether it is exceeded is an input. It
does not bite on a home owner ((2AB) applies), or when the administrator certifies
under (4C). Asserted.

### 5. The Act does not say what stays on the Index, or for how long

k075 asks what stays on the National Personal Insolvency Index after completion. The
Act defines the Index as "the Index of that name established under the regulations"
(s 5) and leaves its contents, extracts and inspection to regulations
(s 315(2)(a)-(c)). On completion the Act requires a certificate to the debtor
(s 185N(3)) and the administrator's notice to the Official Receiver within 5 business
days (s 185N(5)), and nothing more. The scenario's "five years" is Privacy Act and
regulation territory. Not asserted (nothing to assert).

### 6. Completion releases the provable debts — but not all of them

s 185NA(1) releases the debtor from the provable debts a discharge from bankruptcy
would have released, taken at the moment acceptance for processing was recorded. By
s 153(2) that excludes fraud debts and maintenance liabilities; by s 185NA(3) it does
not release a co-debtor or guarantor; and it ceases if the agreement is declared void
(s 185NA(2)). Anything left over from property dealt with under the agreement is the
debtor's (s 185N(2), the Rhea example). Asserted.

### 7. The threshold is not $150,000 in the Act

The scenario supplies "indexed; about $150,000 in unsecured debts". The Act's
threshold amount is "7 times" a rate in the Social Security Act 1991 (point 1064-B1,
column 3, item 2, Table B), and the unsecured-debt limit is that amount or any
greater amount prescribed (s 185C(4)(b)); divisible property may not exceed twice it,
and likely after tax income not three-quarters of it (s 185C(4)(c), (d)). All are
inputs. On the scenario's figure Jake's $41,000 is well inside. Asserted.

### 8. Two arrears tests

A 3-month arrears default (s 185LB(3)) needs arrears throughout the period exceeding
"$300, or 20% of the total of all of the due payments ... whichever is higher"; at $690
a month, one missed payment held for three months is enough. It obliges the
administrator to tell the creditors. A designated 6-month arrears default
(s 185LC(3)) obliges the administrator to tell the Official Receiver, who, if
satisfied, "must declare in writing that the agreement is terminated" (s 185QA).
Asserted.

## What would need doing before this is worth anything

- The s 185C(4)(e) and s 185M(1E) formulas must be recovered from the published
  compilation; the deposit has lost them.
- The Bankruptcy Regulations (the Index, the indexed amounts) and the Minister's
  instruments under s 185C(4B) and (2AD) were not retrieved.
- s 82 (provable debts) was not read beyond the s 153 note; the treatment of
  maintenance and proceeds of crime liabilities as provable for the proceedings
  limbs is an assumption.
- The interaction of s 185K(3)(b) with child support collection (finding 3) needs the
  Child Support (Registration and Collection) Act 1988.
- No case law on "majority in value", "insolvent" or s 185K was searched.
