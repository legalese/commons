# Asian Infrastructure Investment Bank Act 2015 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/AIIBA2015.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". Its legislative history lists only Act 24 of 2015 (commenced
22 August 2015) and the 2017 Revised Edition (Chapter 15A); no amending Act is
annotated. The arrangement of sections at the top of the deposit is one line out of
step with the body; the body's numbering (ss 1-9) is followed.

**Checks:** one module, one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0157** in `subjects/sg/requirements.jsonl`: Tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

The Act itself is short (nine sections) and mostly concerns the Government: ratification
(s 3), subscription (s 4), the Consolidated Fund (ss 5, 6). What reaches a person or
business is the Schedule — Chapter IX of the Agreement (Articles 44 to 52), given the
force of law by s 7(1) "despite anything to the contrary in any other law" — and the
limits s 7(2) puts on the tax exemption. This row encodes Articles 46, 47(1), 50(i), 51
and 52 with s 7(2), and the subscription limits in s 4. Not encoded: s 3, ss 5, 6,
s 7(3), s 8, s 9, Articles 44, 45, 47(2), 48, 49 and 50(ii), (iii).

## What the Act turns out to say

### 1. Most claims against the Bank cannot be brought at all

Article 46(1) gives the Bank "immunity from every form of legal process", except in
cases arising out of raising funds (borrowings or other means), guaranteeing
obligations, or buying, selling or underwriting securities. A supplier with an unpaid
invoice, an employee, a person injured on Bank premises or a person defamed has no
action in a Singapore court unless the Bank waives (Article 52). Even the excepted
claims lie only in a country where the Bank has an office, an agent for service, or
has issued or guaranteed securities. Asserted.

### 2. Anyone deriving a claim from a member is barred, even on a bond

Article 46(2): "no action shall be brought" by a member, its agencies, or any person
"directly or indirectly acting for or deriving claims from a member" — notwithstanding
para 1. A bondholder whose claim derives from a member government cannot sue on the
bond. Whether a waiver under Article 52 can lift this bar is not stated; the encoding
treats it as waivable (inference). Asserted.

### 3. The Bank's tax exemption has three holes Singapore wrote in

Article 51(1) exempts the Bank from "all taxation and from all customs duties" and from
any duty to withhold or collect tax. s 7(2) says Article 51 does not entitle the Bank to
import goods duty-free "without any restriction on their subsequent sale in Singapore",
nor exempt it from taxes that form part of the price of goods or services, nor from
charges that are "no more than charges for services rendered". So tax built into a price
and service charges are payable. That a resale restriction keeps an import within the
customs exemption is an inference. Asserted.

### 4. Pay from the Bank is tax-free unless Singapore deposited a declaration — and the deposit does not say whether it did

Article 51(2) bars any tax on "salaries, emoluments and expenses" paid by the Bank to
its directors, officers, employees, experts and consultants, except where a member
deposited, with its ratification, a declaration retaining the right to tax its own
citizens' or nationals' "salaries, and emoluments". Expenses are not in the retained
right. s 3, which describes Singapore's instrument of ratification, says nothing about
such a declaration, so it is an input here. Asserted.

### 5. A guarantee shields less than an issue

Article 51(3) bars a tax on a Bank-issued security whose sole jurisdictional basis is
the place or currency of issue or payment, or the location of a Bank office.
Article 51(4), for a security the Bank merely guarantees, names only the office
location. A tax on a guaranteed security based solely on where it is payable is not
barred by Article 51(4). Discriminatory taxes are barred for both. Asserted.

### 6. Seizure before judgment is never possible; execution after judgment is not barred by the text

Article 46(3) makes the Bank's property immune from "seizure, attachment or execution
before the delivery of final judgment". Article 47(1) bars taking "by executive or
legislative action" at any time. Neither in terms bars judicial execution of a final
judgment (inference). Asserted.

### 7. Officers' immunity is for official acts, and the Bank alone can waive it

Article 50(i): Governors, Directors, Alternates, the President, Vice-Presidents, officers,
employees, and experts and consultants on missions are immune from legal process for
acts in their official capacity, "except when the Bank waives the immunity". Asserted.

### 8. Singapore's subscription is capped twice

s 4(1)(a): up to US$250 million of the original authorised capital stock; s 4(2): the
total may not exceed US$500 million unless Parliament approves more by resolution.
Asserted.

### 9. The Companies Act 1967 does not reach the Bank or its securities

s 8: the Bank "is not to be treated as a corporation" under the Companies Act 1967, which
does not apply to it or to its issue of "shares, debentures, bonds, notes or other
securities". Not asserted.

### 10. The Schedule stops at Article 52(1)

The deposited Schedule is Chapter IX, Articles 44 to 52, and ends with paragraph 1 of
Article 52. Nothing else of the Agreement has the force of law under s 7(1).

## What would need doing before this is worth anything

- Find whether Singapore deposited an Article 51(2) declaration with its ratification.
- Check whether the Income Tax Act 1947, the Goods and Services Tax Act 1985 or the
  International Organisations (Immunities and Privileges) Act 1948 touch the Bank.
- Read the Agreement itself for the "special procedures" Article 46(2) refers to, and
  for whether Article 52 extends beyond paragraph 1.
- No case law on Article 46 immunities (in Singapore or on the parallel clauses of other
  development banks' charters) was searched.
