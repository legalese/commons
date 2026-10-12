# International Finance Corporation Act 1968 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else (the skill was not loaded in this session, so the
conventions of the finished naive rows were followed). No pipeline, no coverage
table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/IFCA1968.txt`, incorporating "all amendments up to
and including 1 December 2021" and in operation from 31 December 2021. The body
carries no amendment annotations. The Legislative History (not part of the Act)
names the Statutes (Miscellaneous Amendments) Act 1991 (Act 11 of 1991, in force
30 November 1991) as the latest amending Act, followed by the 2013 Revised Edition.
The Schedule reproduces sections 2 to 9 and 11 of Article VI of the Agreement;
sections 1 and 10 are not in the deposit.

**Checks:** one case file, 49 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0178** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet.

The Act is eight sections, mostly about Government finance. What reaches a person
is in the Schedule, which s 7(1) gives the force of law "notwithstanding anything
to the contrary in any other written law". This row takes the Consolidated Fund
charge (s 4), the borrowing power (s 5), and Article VI sections 3, 4, 8, 9 and 11
with the s 7(1) proviso. Not encoded: acceptance of the Agreement (s 3), receipts
(s 6), the Minister's powers to amend the Schedule by Gazette notification and to
make rules (ss 7(2), 8), Article VI sections 2, 5, 6 and 7 (quoted in comments
only), and the Agreement itself beyond the Schedule, which is not deposited.

## What the Act turns out to say

### 1. The Corporation has no immunity from suit as such: only a venue rule and a bar on members

Article VI section 3 says actions may be brought against the Corporation "only in
a court of competent jurisdiction" in a member's territory where it has an office,
an agent for service, or has issued or guaranteed securities; and none may be
brought "by members or persons acting for or deriving claims from members". It
does not limit the kinds of claim. A supplier's price claim, an employee's wage
claim or a personal-injury claim may be brought on the same footing as a claim on
the Corporation's bonds, provided the venue condition is met. (By contrast, the
Asian Development Bank Schedule, as quoted in that subject's naive row, gives that
Bank immunity "from every form of legal process" outside borrowing, guarantees and
securities.) Whether section 11's waiver can relax the venue condition is not
settled by the text; this row assumes not. Asserted.

### 2. A Singapore citizen working for the Corporation can be taxed on the salary; a foreigner cannot

Section 9(b): no tax on salaries and emoluments paid to "Directors, Alternates,
officials or employees of the Corporation who are not local citizens, local
subjects, or other local nationals". The exemption turns on nationality alone;
there is no declaration by the member to make. Governors, though named in section
8, are not named in section 9(b). Asserted.

### 3. Personnel are immune for official acts, but experts and contractors are not personnel

Section 8 covers "Governors, Directors, Alternates, officers and employees": immune
from legal process for acts in their official capacity (s 8(i)); and, if not local
nationals, the immigration, alien-registration and national-service immunities of
comparable officials of other members (s 8(ii)). A consultant on a mission or a
contractor is not named. Section 8(i) has no waiver words of its own; section 11's
general waiver is applied to it. Asserted.

### 4. The Corporation's tax immunity stops at the price of goods and charges for services

Section 9(a) makes the Corporation, its income, operations and transactions immune
"from all taxation and from all customs duties", and from liability to collect or
pay any tax. The s 7(1) proviso cuts it back: no duty-free import for unrestricted
resale, no exemption from taxes that "form part of the price of goods sold", none
from taxes that are "no more than charges for services rendered". Reading a
withholding duty as "liability for the collection" of tax is an inference.
Asserted.

### 5. Bonds issued and bonds guaranteed are protected differently

A tax on a Corporation obligation is barred if it discriminates solely because of
the Corporation, or if its sole jurisdictional basis is, for an issued security,
the place or currency of issue or payment or the location of a Corporation office
(s 9(c)); for a guaranteed security, only the location of a Corporation office
(s 9(d)). Taxing the holder on residence is untouched. Asserted.

### 6. Property is safe from attachment before judgment and from executive seizure

Section 3 bars "seizure, attachment or execution before the delivery of final
judgment"; section 4 bars search, requisition, confiscation or expropriation "by
executive or legislative action". Section 11 lets the Corporation waive either; the
row models waiver as all-or-nothing, though the text allows waiver "to such extent
and upon such conditions as it may determine". Asserted.

### 7. Only two kinds of payment are charged on the Consolidated Fund by s 4, but s 5 borrowing covers any payment

s 4 charges subscriptions for shares (Article II section 3) and payments on
ceasing to be a member (Article V section 4). s 5 lets the Minister, with the
President's concurrence under Article 144(1)(b) of the Constitution, borrow to
provide sums "for making any payments to the Corporation". Asserted.

## What would need doing before this is worth anything

- The Agreement itself (Articles II, III and V, and sections 1 and 10 of Article
  VI) was not deposited, so the payments in s 4 and the cross-reference to
  Article III section 5 in section 6 cannot be followed.
- No Gazette notification amending the Schedule under s 7(2), and no rules under
  s 8, were searched for.
- No case law on the Corporation's immunities, or on how Singapore's Income Tax
  Act treats Corporation salaries, was consulted.
