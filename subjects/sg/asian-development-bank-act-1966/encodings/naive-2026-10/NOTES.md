# Asian Development Bank Act 1966 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else (the skill was not loadable in this session, so the
conventions of the finished naive rows were followed). No pipeline, no coverage
table, no independent test pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/ADBA1966.txt`, incorporating "all amendments up to
and including 1 December 2021" and in operation from 31 December 2021. The body
carries no amendment annotations. The Legislative History (not part of the Act)
names the Statutes (Miscellaneous Amendments) Act 1991 (Act 11 of 1991, in force
30 November 1991) as the latest amending Act, followed by the 2011 Revised Edition.
The deposit's arrangement of sections is out of step by one line; the body's
numbering is followed. Article 57 of the Schedule is shown only as a row of dots.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0156** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked
a sharper question yet.

The Act is short: eleven sections, mostly about Government finance. What reaches a
person is in the Schedule, which s 9(1) gives the force of law "notwithstanding
anything to the contrary in any other law". This row takes the subscription limits
(s 4), payment media (s 5(2)), s 10, and Articles 50, 51, 55, 56 and 58 with the
s 9(1) proviso. Not encoded: ratification (s 3), the Consolidated Fund charges and
loan powers (ss 5(1), 6–8), ss 9(2) and 11, and Articles 48, 49, 52–54 (quoted in
comments only).

## What the Act turns out to say

### 1. Most people cannot sue the Bank at all

Article 50(1) gives the Bank "immunity from every form of legal process", except in
cases arising from its powers to borrow, to guarantee obligations, or to buy, sell
or underwrite securities, and then only in a country where it has an office, an
agent for service, or has issued or guaranteed securities. A supplier owed the
price of goods, an employee claiming wages, or someone injured on its premises has
no action unless the Bank waives (Article 58). A bondholder does. Asserted (the
waiver route is an inference; see 6).

### 2. A member, or anyone deriving a claim from one, can never sue

Article 50(2): "notwithstanding" paragraph 1, no action may be brought by a member,
its agencies, or "any entity or person directly or indirectly acting for or
deriving claims from a member". Even a claim on the Bank's borrowing is barred to
them. Asserted, including with a waiver (inference: 50(2) is worded as a bar on
actions, not as an immunity the Bank can waive).

### 3. A Bank-guaranteed bond is less protected from tax than a Bank-issued one

Article 56(3) forbids a tax on a security the Bank **issues** whose sole
jurisdictional basis is the place or currency of issue or payment, or the location
of a Bank office. Article 56(4), for a security the Bank **guarantees**, names only
the location of a Bank office. So a tax based solely on where a guaranteed bond was
issued is not barred; the same tax on a Bank-issued bond is. Either is barred if it
discriminates solely because of the Bank. Asserted.

### 4. Governors are immune but not named in the salary exemption

Article 55 covers "Governors, Directors, alternates, officers and employees ...
including experts"; Article 56(2), on salaries paid by the Bank, names "Directors,
alternates, officers or employees ... including experts" and leaves Governors out.
The salary exemption also yields where the member declared on ratification that it
keeps the right to tax its own citizens. The deposit does not say whether Singapore
made that declaration; it is a parameter. Asserted.

### 5. The Bank's tax exemption is narrower in Singapore than in the Agreement

Article 56(1) exempts the Bank "from all taxation and from all customs duties" and
from any duty to withhold or collect tax. The s 9(1) proviso reads it down: no
duty-free import "without any restriction on their subsequent sale", no exemption
from taxes forming part of the price of goods sold, none from taxes that are "no
more than charges for services rendered". Asserted.

### 6. Officials are immune only for official acts, and only until the Bank waives

Article 55(i): immunity "with respect to acts performed by them in their official
capacity, except when the Bank waives the immunity". The immigration, alien
registration and national service immunities in (ii) go only to those who are "not
local citizens or nationals". Asserted.

### 7. Before final judgment the Bank's property cannot be touched; by the State, never

Article 50(3) bars seizure, attachment or execution "before the delivery of final
judgment against the Bank"; Article 51 bars any taking "by executive or legislative
action". Asserted.

### 8. The Government's stake has a ceiling Parliament controls

s 4(a) caps the original subscription at US$5 million; the proviso bars any increase
taking the total above US$10 million without a resolution of Parliament. Sums due
may be paid "in gold or United States dollars or in local currency" (s 5(2)). The
Companies Act 1967 does not apply to the Bank or its securities (s 10). Asserted.

## What would need doing before this is worth anything

- The Agreement itself (beyond the Schedule) and Article 57 were not deposited or
  read; whether Singapore deposited an Article 56(2) declaration is unknown.
- Whether waiver under Article 58 reaches the Article 50(2) bar, and whether waiver
  displaces the Article 50(1) venue condition, is left as an inference.
- "Taxes which form part of the price of goods sold" was not mapped to any specific
  Singapore tax.
- Any rules under s 11 or Schedule amendments under s 9(2) were not searched; no
  case law was searched.
