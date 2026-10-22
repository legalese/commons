# Notes: the Universal Credit Regulations 2013 (S.I. 2013/376), Schedules 1 to 5 and 5A (piece uc3, lines 1821-2721)

Written by the piece agent `uc3`.
**The source is a plain-text rendering, not the official text.**
`../../registers/source-bundle/uksi-2013-376.txt` was made by a converter script from the revised text on legislation.gov.uk (version 2026-07-16).
It is not marked up and it is not the official text; nothing in this encoding has been verified against the official text.
Every `-- src:N | ...` line in the modules copies line N of that file, mechanically, with `srcrefs.py quote`.
The deposit's metadata lists 12 outstanding effects and 4 prospective unapplied effects; the text may carry wording that is not yet, or no longer, in force without marking it.

**What is encoded.**
Lines 1821-2721: Schedule 1 (meaning of payments in respect of accommodation), Schedule 2 (liable or not liable), Schedule 3 (occupying or not occupying), Schedule 4 (housing costs element for renters), Schedule 5 (housing costs element for owner-occupiers) and Schedule 5A (further circumstances of a "pre-2026 claimant").
The brief's one-line description says "Schedules 1 to 5", but the line range it gives reaches Schedule 5A (lines 2696-2721), no other piece's range holds it (uc4 begins at line 2722), and the keel's notes name Schedule 5A as uc3's; it is encoded here and has its own rows.
Target dialect: the stable build 1.6.98 (`main`).
Modules are layer 1 (the law, objectively, one module per Schedule or natural group of paragraphs); `uc3-seat.l4` is layer 2.

**Dates.**
The range contains no provision that makes the Regulations or fixes when they come into force; the title block and regulation 1 are uc1's, and nothing here is a commencement rule.
The one date the text fixes in this range is 6th April 2026, which Schedule 5A uses as the day by which circumstances are tested; it is carried as a named value with an `@ref` in `uc3-sch5a-pre-2026-claimant.l4`.
No commencement date is taken from an order.

## Seat

The seat is "a person who claims or receives Universal Credit, alone or as one of a couple, asking whether they are entitled to it, how much, and what they must do or tell the Secretary of State."
In this range the person asks about the housing costs element.
55 questions are exported from `uc3-seat.l4`, grouped under a heading per Schedule and in the order of the text.
Each takes plain answers (yes or no, a number, a nation of Great Britain, or one of the modules' own named choices), builds the layer-1 records in its `WHERE` block, and calls the layer-1 rules; none restates a rule.
A date arrives as a year, a month and a day.
A list is built from a count or from a few named entries.
An input a rule does not read is given a placeholder with a comment saying so.

| # | question (with the provision it answers) | inputs | answer |
| --- | --- | --- | --- |
| 1 | Does what I pay for my home count as rent for the housing costs element (Sch 1 paras 2, 3, 3A, 3B)? | 53 | yes or no |
| 2 | Is what I pay a service charge payment for the housing costs element (Sch 1 paras 7, 8)? | 25 | yes or no |
| 3 | Am I liable to make the payments, or treated as liable (Sch 2 paras 1 to 4)? | 15 | yes or no |
| 4 | Am I treated as not liable to make the payments (Sch 2 paras 5 to 8)? | 40 | yes or no |
| 5 | What amount of an increase because of arrears am I treated as not liable for (Sch 2 para 9)? | 41 | a number |
| 6 | Am I treated as not liable because my liability was contrived (Sch 2 para 10)? | 41 | yes or no |
| 7 | Is the accommodation I normally live in treated as my home (Sch 3 para 1)? | 2 | yes or no |
| 8 | Is my croft land treated as part of my home (Sch 3 para 2)? | 3 | yes or no |
| 9 | Which home am I treated as normally occupying while my home is being repaired (Sch 3 para 3)? | 4 | Accommodation treated as normally occupied under paragraph 3 |
| 10 | Am I treated as occupying both my dwellings as one home (Sch 3 para 4)? | 10 | yes or no |
| 11 | Am I treated as occupying both my old and new home while my new home is adapted for a disabled person (Sch 3 para 5)? | 19 | yes or no |
| 12 | Which home am I treated as normally occupying after leaving because of fear of violence (Sch 3 para 6)? | 13 | Accommodation treated as normally occupied under paragraph 6 |
| 13 | Am I treated as having lived in my home before I moved in, because it was adapted for a disabled person (Sch 3 para 7)? | 18 | yes or no |
| 14 | Am I treated as having lived in my home before I moved in, after a stay in hospital or a care home (Sch 3 para 8)? | 18 | yes or no |
| 15 | Am I treated as no longer living in my home because of a long temporary absence (Sch 3 para 9)? | 11 | yes or no |
| 16 | Do I get no housing costs element because I am a 16 or 17 year old care leaver (Sch 4 para 4)? | 2 | yes or no |
| 17 | Is what I pay taken into account for my housing costs element (Sch 4 para 6)? | 4 | yes or no |
| 18 | What is the monthly equivalent of what I pay (Sch 4 para 7)? | 4 | a number |
| 19 | Is this person a member of my extended benefit unit (Sch 4 para 9)? | 13 | yes or no |
| 20 | How many bedrooms am I entitled to (Sch 4 paras 10 to 12)? | 39 | a number |
| 21 | Is my temporarily absent child or qualifying young person still counted in my extended benefit unit (Sch 4 para 11)? | 12 | yes or no |
| 22 | Am I still counted as a renter while I am temporarily away (Sch 4 para 11)? | 2 | yes or no |
| 23 | Is my temporarily absent non-dependant still counted in my extended benefit unit (Sch 4 para 11)? | 15 | yes or no |
| 24 | Is my absent non-dependant no longer counted in my extended benefit unit because of a long absence (Sch 4 para 11)? | 10 | yes or no |
| 25 | What housing cost contribution is deducted for a non-dependant (Sch 4 paras 13 to 16)? | 39 | a number |
| 26 | Under which Part of Schedule 4 is my housing costs element worked out if I am housed in two dwellings (Sch 4 para 17)? | 11 | Part of Schedule 4 under which the housing costs element is calculated |
| 27 | How many bedrooms count if I am housed in two dwellings (Sch 4 para 17)? | 2 | a number |
| 28 | What is the monthly total of what I pay for my two dwellings (Sch 4 para 17)? | 10 | a number |
| 29 | What is my housing costs element while I am treated as occupying my new and old home (Sch 4 para 18)? | 4 | a number |
| 30 | What is my housing costs element while I am treated as occupying both my home and the place I fled to (Sch 4 para 19)? | 6 | a number |
| 31 | Is my landlord not a provider of social housing, so that Part 4 of Schedule 4 applies to me (Sch 4 para 20)? | 7 | yes or no |
| 32 | What is my housing costs element if I rent privately (Sch 4 paras 22 to 25)? | 23 | a number |
| 33 | What is my cap rent (Sch 4 para 25)? | 8 | a number |
| 34 | How many bedrooms am I entitled to in the private rented sector (Sch 4 para 26)? | 39 | a number |
| 35 | What category of accommodation am I entitled to in the private rented sector (Sch 4 para 27)? | 40 | Category of accommodation |
| 36 | Am I a specified renter (Sch 4 para 28)? | 62 | yes or no |
| 37 | Am I an excepted person for the shared accommodation category (Sch 4 para 29)? | 59 | yes or no |
| 38 | Is my landlord a provider of social housing, so that Part 5 of Schedule 4 applies to me (Sch 4 para 30)? | 7 | yes or no |
| 39 | What is my housing costs element if I rent from a social landlord (Sch 4 paras 31 to 36)? | 33 | a number |
| 40 | Will a deduction be made because I have more bedrooms than I am entitled to (Sch 4 para 36)? | 10 | yes or no |
| 41 | How much will be deducted because I have more bedrooms than I am entitled to (Sch 4 para 36)? | 11 | a number |
| 42 | Am I an owner-occupier for the housing costs element (Sch 5 para 1)? | 2 | yes or no |
| 43 | Am I a joint owner-occupier for the housing costs element (Sch 5 para 1)? | 2 | yes or no |
| 44 | Is what I pay a relevant payment for the housing costs element of an owner-occupier (Sch 5 para 3)? | 23 | yes or no |
| 45 | Do I get no housing costs element as an owner-occupier for an assessment period because someone has earned income (Sch 5 para 4)? | 3 | yes or no |
| 46 | Can an amount under Schedule 4 still be included for me despite earned income because of shared ownership (Sch 5 para 4)? | 1 | yes or no |
| 47 | Have I got past the qualifying period for the housing costs element as an owner-occupier (Sch 5 para 5)? | 4 | yes or no |
| 48 | How many assessment periods do my days of jobseeker's allowance or employment and support allowance count as (Sch 5 para 6)? | 11 | a number |
| 49 | Does paragraph 7 carry my assessment periods forward after my partner and I stop being a couple (Sch 5 para 7)? | 5 | yes or no |
| 50 | How many assessment periods are carried forward to my further award after my partner and I stop being a couple (Sch 5 para 7)? | 5 | a number |
| 51 | What is my housing costs element as an owner-occupier (Sch 5 paras 9 and 13)? | 13 | a number |
| 52 | Is what I pay as an owner-occupier taken into account for my housing costs element (Sch 5 para 8)? | 8 | yes or no |
| 53 | What is the monthly amount of my service charge as an owner-occupier (Sch 5 para 13)? | 4 | a number |
| 54 | Is this period a service charge free period for me (Sch 5 para 13)? | 1 | yes or no |
| 55 | Am I a pre-2026 claimant for the LCWRA element (Sch 5A)? | 13 | yes or no |

**This range puts no duty on the claimant.**
Schedules 1 to 5A say what counts as rent and as a service charge, who is treated as liable, when a home is treated as occupied, how many bedrooms a renter is entitled to, what the amount is, and who is a "pre-2026 claimant".
They are the conditions of a claim and the way an amount is worked out.
The duties to claim, to report changes and to give evidence are elsewhere in the Regulations (other pieces), so the third limb of the seat sentence ("what they must do or tell the Secretary of State") is answered "nothing, in these Schedules".
The one place the claimant is asked to supply something is Schedule 4 paragraph 29(9B) and paragraph 36(6), where evidence from a person acting in an official capacity is a condition; those are inputs, not duties.

**Limits the seat adds to the layer-1 rules** (design choices, not the text; each is also said in the question's comment):

1. Schedule 2 paragraph 6: one holder per person, the person's own combined holding with associates; a parent undertaking's holdings are not asked (placeholders 0 and FALSE).
2. Schedule 4 paragraph 29(4): the renter's stays in hostels are one stay (the months are added).
3. Schedule 4 paragraph 12: the seat asks about one person who has an overnight carer, one foster carer or adopter and one joint renter who cannot share a bedroom; the layer-1 rules take any number.
4. The amount questions (Schedule 4 paragraphs 7, 17 to 19, 22 to 25, 31 to 36; Schedule 5 paragraphs 8, 9, 13) take "I meet the payment, liability and occupation conditions" as an answer and build an ordinary home in England, with rent, or a service charge payment taken to meet paragraph 8 of Schedule 1; the Schedule 1 to 3 questions are where those are tested.
5. Schedule 4 Part 5 takes one rent (with the tenant incentive scheme, commodity and rent officer facts) and one service charge (with a commodity amount, but no tenant incentive scheme reduction and no rent officer determination); Schedule 5 takes two service charges.
6. The housing cost contributions are asked one non-dependant at a time (Schedule 4 paragraphs 13 to 16) and the sum is given to the amount questions as a number.
7. Schedule 5 paragraph 5: the qualifying period is asked as the number of assessment periods in a row, not counting this one, that count (cut off at 9: nothing in paragraph 5 depends on a longer run); a period that does not count restarts the count (paragraph 5(3)), so only the run since the last gap is asked.
8. Schedule 5A: each "on a day before (or on or after) 6th April 2026" is a yes or no, and the layer-1 rules are given the stand-in day 5th April 2026 or 6th April 2026; the real day is never needed because the Schedule compares each day with that date only.
9. Dates: months are counted as fork U3-F8 says.

The source is a plain-text rendering, not the official text.
Nothing here says "verified against the official text".
The range has no commencement provision; the only date the text fixes is 6th April 2026 (Schedule 5A), carried as a named value.

## Jural relations

Hohfeld's terms, as I read the text.
Most provisions here are definitions or counting rules and carry no relation of their own; they decide whether the condition of a claim is met.
The claim itself (the housing costs element) comes from regulations 25 and 26 (uc1), outside this range.

| provision | relation | holder of the claim, power or privilege | against whom (duty, liability or no-right) | note |
| --- | --- | --- | --- | --- |
| Sch 1 (all) | none | | | definitions that sort payments into rent and service charge payments |
| Sch 2 paras 1 to 4, 5 to 9 | none | | | deeming rules: whether the claimant "is liable"; they settle a condition of the claim in reg 25(5) |
| Sch 2 para 10 | power / liability | the Secretary of State (power, by being satisfied the liability was contrived) | the claimant (liability to be treated as not liable) | a judgement the encoding carries as an input |
| Sch 3 (all) | none | | | which accommodation the claimant is treated as occupying; para 1(3) is an all-the-circumstances judgement (fork U3-F21) |
| Sch 4 para 4 | no-right / privilege | the Secretary of State (privilege not to include the element) | the 16 or 17 year old care leaver (no-right) | "section 11(1) of the Act does not apply" |
| Sch 4 paras 6, 7, 8 to 12, 26 to 29 | none | | | which payments count, in what monthly form, and how many bedrooms |
| Sch 4 paras 13, 14 | none | | | a calculation rule; the renter's claim is to the amount after deduction (the row below) |
| Sch 4 paras 22, 33; Sch 5 paras 9, 13 | claim / duty (read in) | the renter or owner-occupier (claim to the amount) | the Secretary of State (duty to include the amount worked out as the Schedule says) | stated in the passive ("is to be calculated as follows"); no party is named, so the claim and the duty are read in, not stated |
| Sch 4 paras 24(5), 35(5) | power / liability | the Secretary of State (power to allocate or to determine S in the manner considered appropriate) | the renter | where the shared-liability formula would be unreasonable |
| Sch 4 para 32(2) to (4) | power / liability | the Secretary of State (power to apply to a rent officer, and to disregard the lower amount if not appropriate) | the renter (liability to have the lower amount used) | no landlord relation is stated, and none is invented |
| Sch 4 para 36 | none | | | a calculation rule (the amount of the under-occupation deduction); excluded by 36(5) and 36(6) |
| Sch 5 para 5(1) | no-right / privilege | the Secretary of State (privilege not to include the element until the qualifying period has ended) | the owner-occupier (no-right until then) | |
| Sch 5 para 6(2) | power / liability | the decision-maker ("may be treated": the text names no one) | the owner-occupier | carried as an input, not decided |
| Sch 5 para 7 | none | | | carrying assessment periods forward |
| Sch 5A para 1 | none | | | a status ("pre-2026 claimant") that feeds regulation 27 (uc1) |
| Sch 5A para 2(2) | power / liability | the decision-maker (the decision "may be made" on a revision, a supersession or an appeal) | the claimant | no rule reads the route, so the encoding carries it inertly |

## Coverage table

Lines 1821-2721 are covered exactly once: 341 rows, checked by a script that expands every line range and counts each of the 901 lines.
By disposition: encoded 203, inert 75, repealed or blank in this text 20, fork 43.
The section index lists 87 paragraph headings in this range; each opens a row or sits inside one, so 87 headings against 341 rows is the finer grain, not a gap.
A row marked `fork` is encoded under a reading the text does not settle; its note names the fork (`U3-F..`) in the register below.
A row marked `inert` says in its note what the lines are (a title, a pure citation, a definition no rule reads).
Layer 2 (`uc3-seat.l4`) adds no coverage rows of its own: every question calls rules the rows already name.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Sch 1 title and "General" heading | 1821-1822 | inert | — | title |
| Sch 1 para 1 heading and "In this Schedule—" | 1823-1824 | inert | — | title |
| Sch 1 para 1 "approved premises" | 1825 | inert | — | pure citation (Offender Management Act 2007 s13); a stated input in uc3-sch1-payments where a rule reads it |
| Sch 1 para 1 "care home" (a), (aa), (b), (c) | 1826-1830 | encoded | uc3-sch1-interpretation: `Sch 1 para 1 — care home`, `Sch 1 para 1 — care home, limbs (a), (aa) and (b)` | limb (a) shows dots after "in England" (line 1827); encoded as printed |
| Sch 1 para 1 "exempt accommodation" | 1831 | inert | — | pure citation (Housing Benefit and Council Tax Benefit (Consequential Provisions) Regulations 2006 Sch 3 para 4(10)); a stated input where read |
| Sch 1 para 1 "housing association" | 1832 | inert | — | pure citation (Housing Associations Act 1985 s1(1)); a stated input where read |
| Sch 1 para 1 "independent hospital" (a), (b), (c) | 1833-1836 | encoded | uc3-sch1-interpretation: `Sch 1 para 1 — independent hospital` | the Acts are stated inputs per nation |
| Sch 1 para 1 "registered charity" | 1837 | encoded | uc3-sch1-interpretation: `Sch 1 para 1 — registered charity` | |
| Sch 1 para 1 "shared ownership tenancy" | 1838 | inert | — | pure citation of reg 26(6) (piece uc1); a stated input where read |
| Sch 1 para 1 "tent" | 1839 | encoded | uc3-sch1-interpretation: `Sch 1 para 1 — tent` | |
| Sch 1 para 1, line between "tent" and "voluntary organisation" | 1840 | repealed or blank in this text | — | the text shows `...` |
| Sch 1 para 1 "voluntary organisation" | 1841 | encoded | uc3-sch1-interpretation: `Sch 1 para 1 — voluntary organisation` | "public authority" is a stated input; "local authority" is the keel's reg 2 rule |
| Sch 1 "Rent payments" sub-heading and para 2 heading | 1842-1843 | inert | — | title |
| Sch 1 para 2 lead-in and (a)-(d) | 1844-1848 | encoded | uc3-sch1-payments: `Sch 1 para 2 — a rent payment`, `Sch 1 para 2 — a payment of a description in paragraph 2(a) to (e)` | |
| Sch 1 para 2(e)(i), (ii) | 1849-1851 | encoded | uc3-sch1-payments: `Sch 1 para 2(e) — a contribution towards almshouses` | "exempt charity within Schedule 3 to the Charities Act 2011" and "housing association" are stated inputs |
| Sch 1 para 3 heading and lead-in | 1852-1853 | encoded | uc3-sch1-payments: `Sch 1 para 3 — a payment is excluded from being a rent payment` | |
| Sch 1 para 3(a) | 1854 | encoded | uc3-sch1-payments: field `ground rent` | |
| Sch 1 para 3(b) | 1855 | encoded | uc3-sch1-payments: `Sch 1 para 3 — a payment is excluded from being a rent payment` (limbs `Sch 1 para 1 — tent`, field `the payment is in respect of the site on which a tent stands`) | |
| Sch 1 para 3(c) | 1856 | encoded | uc3-sch1-payments: field `approved premises` of `Accommodation in the Schedule 1 tests` | |
| Sch 1 para 3(d) | 1857 | encoded | uc3-sch1-payments: limb `Sch 1 para 1 — care home` | |
| Sch 1 para 3(e) | 1858 | repealed or blank in this text | — | dots |
| Sch 1 para 3(f) | 1859 | encoded | uc3-sch1-payments: field `owner-occupier payment within the meaning of Schedule 1 of the Loans for Mortgage Regulations 2017` | a stated input; that instrument is not among the inputs |
| Sch 1 para 3(g) | 1860 | fork | uc3-sch1-payments: limb `Sch 1 para 8(7) — the payment is treated as a service charge payment for the purposes of paragraph 3(g)` | U3-F3: read with para 8(7): a payment failing only the para 8 conditions is still excluded from being a rent payment |
| Sch 1 para 3(h) | 1861 | encoded | uc3-sch1-payments: limb `Sch 1 para 3A(1) — accommodation specified in paragraph 3A` | |
| Sch 1 para 3(i) | 1862 | encoded | uc3-sch1-payments: limb `Sch 1 para 3B(1) — temporary accommodation` | |
| Sch 1 para 3A heading and (1) | 1863-1864 | encoded | uc3-sch1-payments: `Sch 1 para 3A(1) — accommodation specified in paragraph 3A` | |
| Sch 1 para 3A(2) | 1865 | encoded | uc3-sch1-payments: `Sch 1 para 3A(2) — exempt accommodation` | a stated input |
| Sch 1 para 3A(3)(a)-(c) | 1866-1869 | encoded | uc3-sch1-payments: `Sch 1 para 3A(3) — accommodation provided by a relevant body for care, support or supervision` | |
| Sch 1 para 3A(4)(a), (b) | 1870-1872 | encoded | uc3-sch1-payments: `Sch 1 para 3A(4) — accommodation for a person who has left home as a result of domestic violence` | reg 98 "domestic violence" is uc4's: stated inputs |
| Sch 1 para 3A(5)(a), (b) | 1873-1875 | fork | uc3-sch1-payments: `Sch 1 para 3A(5) — a building that would be a hostel but for local authority ownership, where care is received` | U3-F14: "would be a hostel but for being owned or managed by a local authority" read as: not a hostel by Sch 4 para 29(10), but a hostel if a local authority counted as a provider of social housing |
| Sch 1 para 3A(6) "domestic violence" | 1876-1877 | inert | — | pure citation of reg 98 (uc4) |
| Sch 1 para 3A(6) "relevant body" (a)-(d) | 1878-1882 | encoded | uc3-sch1-payments: `Sch 1 para 3A(6) — relevant body` | |
| Sch 1 para 3B heading and (1) | 1883-1884 | fork | uc3-sch1-payments: `Sch 1 para 3B(1) — temporary accommodation` | U3-F4: "paragraph (3)(i)" read as paragraph 3(i) |
| Sch 1 para 3B(2)(a)-(c) | 1885-1890 | encoded | uc3-sch1-payments: `Sch 1 para 3B(2) — Case 1` | |
| Sch 1 para 3B(3)(a)-(c) | 1891-1896 | encoded | uc3-sch1-payments: `Sch 1 para 3B(3) — Case 2` | |
| Sch 1 para 3B(4) | 1897 | encoded | uc3-sch1-payments: `Sch 1 para 3B(1) — temporary accommodation` | the rule does not read the renter's liability for service charges; a test shows the answer is unchanged |
| Sch 1 para 3B(5) | 1898 | inert | — | pure citation of Sch 4 para 2; the rule uses `Sch 4 para 2 — provider of social housing` |
| Sch 1 "Owner-occupier payments" sub-heading | 1899 | inert | — | title |
| Sch 1 para 4 heading and dots | 1900-1901 | repealed or blank in this text | — | dots |
| Sch 1 para 5 heading and dots | 1902-1903 | repealed or blank in this text | — | dots |
| Sch 1 para 6 heading and dots | 1904-1905 | repealed or blank in this text | — | dots |
| Sch 1 "Service charge payments" sub-heading and para 7 heading | 1906-1907 | inert | — | title |
| Sch 1 para 7(1)(a)-(c) | 1908-1911 | encoded | uc3-sch1-payments: `Sch 1 para 7(1) — a service charge payment`, `Sch 1 para 7(1)(c) — in any case to which paragraph 8 applies, the payments meet all of its conditions` | |
| Sch 1 para 7(2)(a), (b) | 1912-1914 | encoded | uc3-sch1-payments: `Sch 1 para 7(2) — the payment falls within sub-paragraph (2)` | |
| Sch 1 para 7(3)(a), (b) | 1915-1921 | encoded | uc3-sch1-payments: `Sch 1 para 7(3) — the payment is excluded by sub-paragraph (3)`, `Sch 1 para 7(3)(b) — the occupant is in a tent, approved premises, a care home or exempt accommodation` | |
| Sch 1 para 7(4)(a)-(c) | 1922-1925 | encoded | uc3-sch1-payments: the three fields of `Payment that may be a service charge payment` that no rule reads | a test shows the answer unchanged when they change |
| Sch 1 para 8 heading and 8(1)(a), (b) | 1926-1929 | encoded | uc3-sch1-payments: field `the calculation is made under Part 5 of Schedule 4 or under Schedule 5`; `Sch 1 para 7(1)(c) — ...` | |
| Sch 1 para 8(2) | 1930 | encoded | uc3-sch1-payments: `Sch 1 para 8(2) — all four conditions are met` | |
| Sch 1 para 8(3) | 1931 | encoded | uc3-sch1-payments: `Sch 1 para 8(3) — the first condition` | |
| Sch 1 para 8(4) lead-in, Categories A-D | 1932-1944 | fork | uc3-sch1-payments: `Sch 1 para 8(4) — the second condition` and the four category rules | U3-F13: "to the extent that" and "only where": the payment under test is the part that fits |
| Sch 1 para 8(5) | 1945 | encoded | uc3-sch1-payments: `Sch 1 para 8(5) — the third condition` | |
| Sch 1 para 8(6)(a)-(c) | 1946-1949 | fork | uc3-sch1-payments: `Sch 1 para 8(6) — the fourth condition` | U3-F13 |
| Sch 1 para 8(7) | 1950 | fork | uc3-sch1-payments: `Sch 1 para 8(7) — the payment is treated as a service charge payment for the purposes of paragraph 3(g)` | U3-F3: cites para 4(2), which is dots in this text |
| Sch 2 title and Part 1 heading | 1951-1952 | inert | — | title |
| Sch 2 para 1 heading and 1(1)(a), (b) | 1953-1956 | encoded | uc3-sch2-liability: `Sch 2 para 1 — the claimant is treated as liable because of the person who is liable` | reg 4 "responsible for" is uc1's |
| Sch 2 para 1(2) | 1957 | encoded | uc3-sch2-liability: the same rule (its third input `claiming as a single person by virtue of regulation 3(4)`) | reg 3(4) is uc1's |
| Sch 2 para 2 heading and 2(1), (2)(a)-(d) | 1958-1964 | encoded | uc3-sch2-liability: `Sch 2 para 2 — the claimant is treated as liable because the person who is liable has failed to pay` | (c) and (d) are judgements and are stated inputs |
| Sch 2 para 2(3) | 1965 | fork | uc3-sch2-liability: the description of the input `it is otherwise reasonable in all the circumstances to treat the claimant as liable to make the payments` | U3-F16: a permission about how a judgement is reached, not a condition; quoted beside the input |
| Sch 2 para 3 heading and (a), (b) | 1966-1969 | encoded | uc3-sch2-liability: `Sch 2 para 3 — the claimant is treated as liable although the liability is waived for repair work` | |
| Sch 2 para 4 heading and 4(1) | 1970-1971 | encoded | uc3-sch2-liability: `Sch 2 para 4 — the claimant is treated as liable for the whole of a rent free period` | |
| Sch 2 para 4(2) | 1972 | inert | — | pure citation of Sch 4 para 7(4); the rule uses `Sch 4 para 7(4) — a rent free period` |
| Sch 2 Part 2 heading | 1973 | inert | — | title |
| Sch 2 para 5 heading and 5(1)(a)-(c)(iii) | 1974-1983 | encoded | uc3-sch2-liability: `Sch 2 para 5 — the claimant is treated as not liable (close relative)`, `Sch 2 para 5(1) — the liability is owed to a person who lives in the accommodation and is within paragraph 5(1)(a) to (c)` | "close relative" is the keel's reg 2 rule |
| Sch 2 para 5(2) | 1984 | encoded | uc3-sch2-liability: `Sch 2 para 5 — the claimant is treated as not liable (close relative)`, second limb | |
| Sch 2 para 6 heading and 6(1)(a)-(d) | 1985-1990 | encoded | uc3-sch2-liability: `Sch 2 para 6(1) — the owners or directors of the company include a listed person` | |
| Sch 2 para 6(2)(a), (b) | 1991-1993 | encoded | uc3-sch2-liability: `Sch 2 para 6 — the claimant is treated as not liable (company)`, second limb | "the same company" and "another company" are one test (the company's owners or directors include a listed person) |
| Sch 2 para 6(3) | 1994 | encoded | uc3-sch2-liability: `Sch 2 para 6(1) — the person is an owner or director of the company` | |
| Sch 2 para 6(4)(a)-(h) | 1995-2003 | encoded | uc3-sch2-liability: `Sch 2 para 6(4) — A has a material interest in C` and the four percentage rules and the influence rule | the 10% figure is the text's |
| Sch 2 para 6(5)(a)-(c) | 2004-2007 | fork | uc3-sch2-liability: `Sch 2 para 6(5) — the holder counts as A or one of A's associates` and the `taken together` rules | U3-F18: only the combined holding is computed, because every limb of 6(4) is monotone in the holding |
| Sch 2 para 6(6)(a)-(g) | 2008-2015 | encoded | uc3-sch2-liability: `Sch 2 para 6(6) — associate` | |
| Sch 2 para 6(7) "settlement" | 2016 | encoded | uc3-sch2-liability: field `trustee of a settlement under which A has a life interest in possession (in Scotland a life interest)` | the definition is carried in the field's wording; "settlement" is not computed |
| Sch 2 para 6(8) "parent undertaking" | 2017-2018 | inert | — | pure citation (Financial Services and Markets Act 2000 s420) |
| Sch 2 para 6(8) "shares", "voting power" | 2019-2025 | fork | uc3-sch2-liability: the percentage fields of `Holder of an interest in a company` | U3-F17: the definitions fix what is measured, not how; the percentages are stated inputs |
| Sch 2 para 7 heading and 7(1)(a)-(d) | 2026-2031 | encoded | uc3-sch2-liability: `Sch 2 para 7(1) — the trustees or beneficiaries include a listed person` | |
| Sch 2 para 7(2)(a), (b) | 2032-2034 | encoded | uc3-sch2-liability: `Sch 2 para 7 — the claimant is treated as not liable (trust)`, second limb | |
| Sch 2 para 8 heading and 8(1) | 2035-2036 | encoded | uc3-sch2-liability: `Sch 2 para 8 — the claimant is treated as not liable (household)`, first limb | |
| Sch 2 para 8(2) | 2037 | encoded | uc3-sch2-liability: the same rule, service charge limb | |
| Sch 2 para 8(3)(a), (b) | 2038-2040 | encoded | uc3-sch2-liability: the same rule, second service charge limb | |
| Sch 2 para 9 heading and 9(1)(a), (b) | 2041-2047 | encoded | uc3-sch2-liability: `Sch 2 para 9 — the amount for which the claimant is treated as not liable because of arrears` | |
| Sch 2 para 9(2) | 2048 | encoded | uc3-sch2-liability: the same rule (nil when paragraphs 5 to 8 apply) | |
| Sch 2 para 10 heading and 10(1) | 2049-2050 | encoded | uc3-sch2-liability: `Sch 2 para 10 — the claimant is treated as not liable because the liability was contrived` | the Secretary of State's satisfaction is a stated input |
| Sch 2 para 10(2) | 2051 | encoded | uc3-sch2-liability: the same rule | |
| Sch 3 title and Part 1 heading | 2052-2053 | inert | — | title |
| Sch 3 para 1 heading and 1(1) | 2054-2055 | encoded | uc3-sch3-occupation: `Sch 3 para 1 — the claimant is treated as occupying the accommodation as their home` | |
| Sch 3 para 1(2) | 2056 | encoded | uc3-sch3-occupation: `Sch 3 para 1 — the claimant is treated as occupying the accommodation as their home` (the one-dwelling limit) | "subject to the following provisions of this Part": paragraph 4 treats two dwellings as one accommodation |
| Sch 3 para 1(3) | 2057 | fork | uc3-sch3-occupation: field `the accommodation is the accommodation which the claimant normally occupies as their home` of `Accommodation the claimant may occupy as their home` | U3-F21: an all-the-circumstances judgement, carried as the input |
| Sch 3 para 1(4)(a), (b) "Dwelling" | 2058-2060 | inert | — | pure citation (Local Government Finance Act 1992 Part 1 and Part 2); `number of dwellings the accommodation comprises` is a stated input |
| Sch 3 para 2 heading and 2(1) | 2061-2062 | encoded | uc3-sch3-occupation: `Sch 3 para 2 — the croft land is treated as included in the accommodation` | |
| Sch 3 para 2(2) "Croft" | 2063 | inert | — | pure citation (Crofters (Scotland) Act 1993 s3(1)); a stated input |
| Sch 3 para 3 heading, 3(1)(a)-(c) and the words after it | 2064-2069 | encoded | uc3-sch3-occupation: `Sch 3 para 3(1)(a) and (b) — the claimant moved out for essential repairs and intends to return`, `Sch 3 para 3 — the accommodation the claimant is treated as normally occupying` | the payment and liability conditions are reg 25(5) (uc1): stated inputs |
| Sch 3 para 3(2)(a), (b) | 2070-2072 | encoded | uc3-sch3-occupation: `Sch 3 para 3 — the accommodation the claimant is treated as normally occupying` (both conditions met: the general rule) | |
| Sch 3 para 4 heading and 4(1)(a)-(c) | 2073-2077 | encoded | uc3-sch3-occupation: `Sch 3 para 4 — both dwellings are treated as the single accommodation the claimant normally occupies as their home` | "irrelevant whether the liability is to the same or a different person": the rule does not read the creditor |
| Sch 3 para 4(2) | 2078 | encoded | uc3-sch3-occupation: the same rule | |
| Sch 3 para 4(3) | 2079 | inert | — | pure citation of Sch 4 para 2; the rule uses `Sch 4 para 2 — provider of social housing` |
| Sch 3 para 5 heading, 5(1)(a), (b) | 2080-2083 | encoded | uc3-sch3-occupation: `Sch 3 para 5(1) — sub-paragraph (2) applies` | |
| Sch 3 para 5(2)(a), (b) | 2084-2086 | encoded | uc3-sch3-occupation: `Sch 3 para 5(2) — conditions for being treated as occupying both` | |
| Sch 3 para 5(3)(a), (b) | 2087-2096 | encoded | uc3-sch3-occupation: `Sch 3 para 5(3) — a person is specified`; uc3-disability-payments: `Sch 3 para 5(3)(b) — a person in receipt of one of the listed payments` | |
| Sch 3 para 5(4) | 2097 | fork | uc3-sch3-occupation: `Sch 3 para 5 — the claimant is treated as occupying both the new and the old accommodation` | U3-F19: the month starts on the first day the claimant is treated as occupying both (an input); counted by the periods module (U3-F8) |
| Sch 3 para 6 heading, 6(1)(a)-(c) | 2098-2102 | encoded | uc3-sch3-occupation: `Sch 3 para 6(1) — this paragraph applies` | |
| Sch 3 para 6(2)(a), (b) | 2103-2105 | encoded | uc3-sch3-occupation: `Sch 3 para 6(2) — the claimant is treated as normally occupying both` | |
| Sch 3 para 6(3) | 2106 | encoded | uc3-sch3-occupation: `Sch 3 para 6(3) — the accommodation the claimant is treated as normally occupying where one only meets the conditions` | |
| Sch 3 para 6(4) | 2107 | fork | uc3-sch3-occupation: `Sch 3 para 6(2) — the claimant is treated as normally occupying both` (its twelve-month limb) | U3-F19; after 12 months neither para 6(2) nor para 6(3) treats the claimant as occupying both, and the text does not say what then applies (U3-F20) |
| Sch 3 para 7 heading, 7(1)(a)-(c) | 2108-2112 | fork | uc3-sch3-occupation: `Sch 3 para 7 — the claimant is treated as having occupied the accommodation before moving in` | U3-F19 |
| Sch 3 para 7(2) | 2113 | encoded | uc3-sch3-occupation: field `the relevant person` of `Move that was delayed by adaptations to accommodation`, tested by `Sch 3 para 5(3) — a person is specified` | |
| Sch 3 para 7(3) | 2114 | fork | uc3-sch3-occupation: the same rule (its one-month limb) | U3-F19 |
| Sch 3 para 8 heading, 8(1)(a), (b) | 2115-2118 | encoded | uc3-sch3-occupation: `Sch 3 para 8(1)(b) — the liability arose while the claimant (or both joint claimants) were patients or in a care home` | |
| Sch 3 para 8(2) | 2119 | fork | uc3-sch3-occupation: `Sch 3 para 8 — the claimant is treated as having occupied the accommodation before moving in` (its one-month limb) | U3-F19 |
| Sch 3 para 8(3) "care home", "patient" | 2120-2122 | encoded | uc3-sch3-occupation: `Sch 3 para 8(1)(b) — the person was a patient or accommodated in a care home` | "care home" is Sch 1 para 1: `Sch 1 para 1 — care home` |
| Sch 3 Part 2 heading | 2123 | inert | — | title |
| Sch 3 para 9 heading and 9(1) | 2124-2125 | fork | uc3-sch3-occupation: `Sch 3 para 9 — the claimant is treated as no longer occupying the accommodation` | U3-F8: "exceeds, or is expected to exceed, 6 months" |
| Sch 3 para 9(2) | 2126 | encoded | uc3-sch3-occupation: the same rule (a claimant within paragraph 3 is never treated as no longer occupying) | |
| Sch 3 para 9(3) | 2127 | encoded | uc3-sch3-occupation: the same rule (12 months for a claimant within paragraph 6) | |
| Sch 4 title and Part 1 heading | 2128-2129 | inert | — | title |
| Sch 4 para 1 heading; para 1(1) | 2130-2131 | encoded | uc3-sch4-interpretation: `Sch 4 para 1(2) — a claimant is a renter` | whether reg 26(2) applies is a stated input (reg 26 is uc1's) |
| Sch 4 para 1(2) "renters", "joint renters" | 2132 | encoded | uc3-sch4-interpretation: `Sch 4 para 1(2) — a claimant is a renter`, `Sch 4 para 1(2) — a joint renter` | |
| Sch 4 para 1(3) | 2133 | inert | — | machinery: says where the exception to s11(1) is |
| Sch 4 para 1(4)(a)-(c) | 2134-2137 | encoded | uc3-sch4-interpretation: type `Part of Schedule 4 under which the housing costs element is calculated` | the answer type of the rules in paragraphs 17, 20 and 30; (a) is paragraph 5's signpost (Part 3 applies to both) |
| Sch 4 para 2 heading and "In this Schedule—" | 2138-2139 | inert | — | title |
| Sch 4 para 2 "domestic violence" | 2140 | inert | — | pure citation of reg 98(4) (piece uc4) |
| Sch 4 para 2 "exempt accommodation" | 2141 | inert | — | pure citation (as Sch 1 para 1) |
| Sch 4 para 2 "extended benefit unit" | 2142 | inert | — | pure citation of para 9; encoded at `Sch 4 para 9(1) — a person is a member of the renter's extended benefit unit` in uc3-sch4-bedrooms |
| Sch 4 para 2 "Housing Act functions" | 2143 | inert | — | pure citation (Housing Act 1996 s122) |
| Sch 4 para 2 "housing cost contribution" | 2144 | inert | — | pure citation of para 13 |
| Sch 4 para 2 "joint renter" | 2145 | inert | — | pure citation of para 1(2); encoded at `Sch 4 para 1(2) — a joint renter` |
| Sch 4 para 2 "listed persons" (a)-(c) | 2146-2149 | encoded | uc3-sch4-interpretation: `Sch 4 para 2 — a listed person` | reg 4 "responsible for" is a stated input (uc1) |
| Sch 4 para 2 "member of the armed forces" | 2150 | inert | — | pure citation (Armed Forces Act 2006 s374); a stated input where read (para 11(5)(d), para 16(2)(j)) |
| Sch 4 para 2 "non-dependant" | 2151 | inert | — | pure citation of para 9(2) |
| Sch 4 para 2 "provider of social housing" (a)-(d) | 2152-2156 | encoded | uc3-sch4-interpretation: `Sch 4 para 2 — provider of social housing` | registration and "social housing" (HRA 2008 ss68-77) are stated inputs |
| Sch 4 para 2 "registered social landlord" (a), (b) | 2157-2159 | encoded | uc3-sch4-interpretation: `Sch 4 para 2 — registered social landlord` | |
| Sch 4 para 2 "relative" | 2160 | inert | — | pure citation (Family Law Act 1996 s63(1)); a stated input in para 29(9B) |
| Sch 4 para 2 "relevant payments" | 2161 | inert | — | pure citation of para 3 |
| Sch 4 para 2 "the Rent Officers Order 2013" | 2162 | inert | — | pure citation (Rent Officers (Universal Credit Functions) Order 2013) |
| Sch 4 para 2 "renter" | 2163 | inert | — | pure citation of para 1(2) |
| Sch 4 para 2 "renter who requires overnight care" | 2164 | inert | — | pure citation of para 12(3) to (5); encoded at `Sch 4 para 12(3) — a person satisfies the overnight care condition` |
| Sch 4 para 2 "shared accommodation" | 2165 | inert | — | pure citation of para 27 |
| Sch 4 para 2 "social housing" | 2166 | inert | — | pure citation (Housing and Regeneration Act 2008 ss68-77) |
| Sch 4 para 3 heading and 3(1)(a), (b) | 2167-2170 | encoded | uc3-sch4-payments: `Sch 4 para 3 — the payment is a relevant payment` | |
| Sch 4 para 3(2) | 2171 | encoded | uc3-sch4-payments: limb `Sch 1 para 2 — a rent payment` | |
| Sch 4 para 3(3)(a), (b) | 2172-2174 | encoded | uc3-sch4-payments: limb `Sch 1 para 7(1) — a service charge payment` | in Part 4 the para 8 conditions do not apply (Sch 1 para 8(1)), which the payment record's field `the calculation is made under Part 5 of Schedule 4 or under Schedule 5` carries |
| Sch 4 Part 2 heading | 2175 | inert | — | title |
| Sch 4 para 4 heading and text | 2176-2177 | encoded | uc3-sch4-interpretation: `Sch 4 para 4 — the renter gets no housing costs element as a 16 or 17 year old care leaver` | "any renter" asked of one renter at a time (fork U3-F7); "care leaver" is reg 8 (uc1) |
| Sch 4 para 4A heading and dots | 2178-2179 | repealed or blank in this text | — | dots |
| Sch 4 para 4B heading and dots | 2180-2181 | repealed or blank in this text | — | dots |
| Sch 4 para 4C heading and dots | 2182-2183 | repealed or blank in this text | — | dots |
| Sch 4 Part 3 heading | 2184 | inert | — | title |
| Sch 4 para 5 heading and text | 2185-2186 | inert | — | machinery: says that Part 3 applies to Parts 4 and 5 |
| Sch 4 "Payments taken into account" sub-heading and para 6 heading | 2187-2188 | inert | — | title |
| Sch 4 para 6(1) | 2189 | encoded | uc3-sch4-payments: `Sch 4 para 6(1) — the renter meets the payment, liability and occupation conditions` | the three conditions are reg 25(5) (piece uc1): stated inputs |
| Sch 4 para 6(2) | 2190 | fork | uc3-sch4-payments: `Sch 4 para 6 — the liability is brought into account` | U3-F13: "to the extent that" read as the amount entered being the amount that meets the conditions |
| Sch 4 para 6(3) | 2191 | encoded | uc3-sch4-payments: `Sch 4 para 6 — the liability is brought into account` | |
| Sch 4 para 7 heading and 7(1) | 2192-2193 | encoded | uc3-sch4-payments: `Sch 4 para 6 — the monthly amount of a liability taken into account`, `Sch 4 para 6 — the monthly amount of all the relevant payments taken into account` | |
| Sch 4 para 7(2)(a)-(d) | 2194-2199 | encoded | uc3-sch4-payments: `Sch 4 para 7 — the monthly equivalent of a liability` (the keel's `core — the monthly equivalent of a payment`) | "so for example": only the listed intervals are handled |
| Sch 4 para 7(3) | 2200 | encoded | uc3-sch4-payments: `Sch 4 para 7 — the monthly equivalent of a liability` | |
| Sch 4 para 7(3A)(a)-(c) and the lines after them | 2201-2205 | fork | uc3-sch4-payments: field `total number of the relevant payments which the renter is liable to make in that 12 month period` | U3-F1: the formulas are missing from this text, so the number of payments is a stated input |
| Sch 4 para 7(4) | 2206 | encoded | uc3-sch4-payments: `Sch 4 para 7(4) — a rent free period` | |
| Sch 4 Part 3 "Room allocation" sub-heading | 2207 | inert | — | title |
| Sch 4 para 8 heading and 8(1) | 2208-2209 | encoded | uc3-sch4-bedrooms: `Sch 4 para 10 — the number of bedrooms to which a renter is entitled`, `Sch 4 para 27(1) — the category of accommodation to which a renter is entitled under Part 4` | the category is a function of bedrooms (and shared accommodation), as paras 9-12 and 26-29 decide |
| Sch 4 para 8(2)(a), (b) | 2210-2212 | inert | — | machinery: says which paragraphs apply to which Part; Part 4 uses para 26 and 27, Part 5 does not |
| Sch 4 para 9 heading and 9(1)(a)-(c) | 2213-2217 | encoded | uc3-sch4-bedrooms: `Sch 4 para 9(1) — a person is a member of the renter's extended benefit unit` | |
| Sch 4 para 9(2)(a)-(g) | 2218-2225 | encoded | uc3-sch4-bedrooms: `Sch 4 para 9(2) — a person is a non-dependant`, `Sch 4 para 9(2) — the descriptions that take a person out of being a non-dependant` | |
| Sch 4 para 9(3) "foster child" | 2226 | encoded | uc3-sch4-bedrooms: `Sch 4 para 9(3) — foster child` | uses the keel's reg 2 foster parent rule |
| Sch 4 para 10 heading and 10(1)(a)-(f) | 2227-2234 | fork | uc3-sch4-bedrooms: `Sch 4 para 10(1) — the bedrooms before any additional bedroom` | U3-F9: "sex" is two groups; "the renter (or joint renters)" is one bedroom, which para 12(6A) confirms |
| Sch 4 para 10(2) | 2235 | fork | uc3-sch4-bedrooms: `Sch 4 para 10(2) — the fewest bedrooms for children of four kinds`, `Sch 4 para 10(2) — the fewest bedrooms for a group of children` | U3-F6: the fewest is computed exhaustively over four kinds of child |
| Sch 4 para 10(3)(a)-(c) | 2236-2239 | encoded | uc3-sch4-bedrooms: `Sch 4 para 10 — the number of bedrooms to which a renter is entitled`, `Sch 4 para 26 — the number of bedrooms to which a renter is entitled under Part 4` | |
| Sch 4 para 11 heading and 11(1) | 2240-2241 | encoded | uc3-sch4-bedrooms: `Sch 4 para 11(2) — a temporarily absent child or qualifying young person is included`, `Sch 4 para 11(3) — a temporarily absent renter is included`, `Sch 4 para 11(4) — a temporarily absent non-dependant is included` | the three rules are the three cases of sub-paragraphs (2) to (4) |
| Sch 4 para 11(2)(a) | 2242-2243 | fork | uc3-sch4-bedrooms: `Sch 4 para 11(2)(a) — looked after by a local authority` | U3-F8: how a month is counted from a day |
| Sch 4 para 11(2)(b)(i), (ii) | 2244-2246 | fork | uc3-sch4-bedrooms: `Sch 4 para 11(2)(b) — a prisoner` | U3-F8 |
| Sch 4 para 11(2)(c) | 2247 | encoded | uc3-sch4-bedrooms: `Sch 4 para 11(2)(c) — before responsibility ceases under regulation 4(7)` | reg 4(7) is uc1's |
| Sch 4 para 11(3)(a), (b) | 2248-2250 | encoded | uc3-sch4-bedrooms: `Sch 4 para 11(3) — a temporarily absent renter is included` | reg 11 and reg 19(2) are uc1's |
| Sch 4 para 11(4)(a), (b) | 2251-2253 | encoded | uc3-sch4-bedrooms: `Sch 4 para 11(4) — a temporarily absent non-dependant is included` | |
| Sch 4 para 11(5)(a) | 2254-2255 | fork | uc3-sch4-bedrooms: `Sch 4 para 11(5)(a) — the first month of an absence from Great Britain, and a further month` | U3-F8 |
| Sch 4 para 11(5)(b) | 2256 | fork | uc3-sch4-bedrooms: `Sch 4 para 11(5)(b) — the first 6 months of an absence for treatment` | U3-F8 |
| Sch 4 para 11(5)(c) | 2257 | fork | uc3-sch4-bedrooms: `Sch 4 para 11(5)(c) — the first 6 months as a prisoner` | U3-F8 |
| Sch 4 para 11(5)(d) | 2258 | encoded | uc3-sch4-bedrooms: `Sch 4 para 11(5)(d) — a son or daughter in the armed forces away on operations` | |
| Sch 4 para 11(6) | 2259 | fork | uc3-sch4-bedrooms: `Sch 4 para 11(6) — an absent non-dependant is not treated as a member of the extended benefit unit` | U3-F8: "exceeds, or is expected to exceed, 6 months" |
| Sch 4 para 12 heading and 12(A1)(a)-(c) | 2260-2264 | encoded | uc3-sch4-bedrooms: `Sch 4 para 12(A1) — the additional bedroom for the overnight care condition`, `Sch 4 para 12(A1) — one or more of the persons listed satisfies the overnight care condition` | |
| Sch 4 para 12(1) lead-in | 2265 | encoded | uc3-sch4-bedrooms: `Sch 4 para 12 — the additional bedrooms` | the lead-in "(1) A renter is entitled to an additional bedroom if they satisfy any of the following conditions" is carried by the sum in para 12(8) and (9) |
| Sch 4 para 12(1)(a) | 2266 | repealed or blank in this text | — | dots |
| Sch 4 para 12(1)(b), (c), (d) | 2267-2269 | encoded | uc3-sch4-bedrooms: `Sch 4 para 12 — the additional bedrooms` | (b) the foster parent condition, (c) the disabled child condition, (d) the disabled person condition: each is its own rule and each adds one additional bedroom in para 12(9) |
| Sch 4 para 12(2) | 2270 | encoded | uc3-sch4-bedrooms: `Sch 4 para 12 — the additional bedrooms` | "subject to (8) and (9)": the sum follows (8) and (9) |
| Sch 4 para 12(3)(a)-(c) | 2271-2281 | encoded | uc3-sch4-bedrooms: `Sch 4 para 12(3) — a person satisfies the overnight care condition`; uc3-disability-payments: `Sch 3 para 5(3)(b) — a person in receipt of one of the listed payments` | |
| Sch 4 para 12(4)(a), (b) | 2282-2284 | encoded | uc3-sch4-bedrooms: `Sch 4 para 12(4) — a renter satisfies the foster parent condition` | "adopter" is reg 89(3)(a) (uc4), a stated input |
| Sch 4 para 12(5) | 2285 | fork | uc3-sch4-bedrooms: `Sch 4 para 12(5) — a person who would be a foster parent but for having no child placed` | U3-F8: 12 months counted by the periods module |
| Sch 4 para 12(6)(a), (b) | 2286-2290 | fork | uc3-sch4-bedrooms: `Sch 4 para 12(6) — the renter satisfies the disabled child condition`, `Sch 4 para 12(6)(a) and (b) — a child in receipt of a listed care component who cannot share a room`; uc3-disability-payments: `Sch 4 para 12(6)(a) — a child in receipt of one of the listed care components` | U3-F11: "would be expected to share" is read as "needs a further bedroom to have their own" |
| Sch 4 para 12(6A)(a), (b) | 2291-2300 | encoded | uc3-sch4-bedrooms: `Sch 4 para 12(6A) — a renter satisfies the disabled person condition` | |
| Sch 4 para 12(7) | 2301 | repealed or blank in this text | — | dots |
| Sch 4 para 12(8) | 2302 | fork | uc3-sch4-bedrooms: `Sch 4 para 12(8) — the additional bedrooms for the disabled child condition` | U3-F11 |
| Sch 4 para 12(9)(a)-(d) | 2303-2307 | fork | uc3-sch4-bedrooms: `Sch 4 para 12 — the additional bedrooms`, `Sch 4 para 12(9)(b) — the additional bedroom for the foster parent condition`, `Sch 4 para 12(9)(d) — the additional bedroom for the disabled person condition` | U3-F11: (9)(c) and (8) are read as the one amount |
| Sch 4 "Housing cost contributions" sub-heading and para 13 heading | 2308-2309 | inert | — | title |
| Sch 4 para 13(1) | 2310 | encoded | uc3-sch4-contributions: `Sch 4 para 13 — the number of housing cost contributions to be deducted` | the non-dependants are paragraph 9's (uc3-sch4-bedrooms) |
| Sch 4 para 13(2) | 2311 | encoded | uc3-sch4-contributions: the same rule, through `Sch 4 para 15(1) — no deduction is made because of the renter` and `Sch 4 para 16(2) — the sub-paragraph applies to the non-dependant` | |
| Sch 4 para 13(3) | 2312 | encoded | uc3-sch4-contributions: `Sch 4 para 13 — the sum of the housing cost contributions` | |
| Sch 4 para 14 heading and 14(1) | 2313-2314 | encoded | uc3-sch4-contributions: `Sch 4 para 14(1) — the amount of each housing cost contribution` | £96.55 |
| Sch 4 para 14(2) | 2315 | encoded | uc3-sch4-contributions: `Sch 4 para 14(2) and (3)(a) — the amount after the housing cost contributions are deducted` | the callers (Parts 4 and 5) apply it last |
| Sch 4 para 14(3)(a) | 2316-2317 | encoded | uc3-sch4-contributions: `Sch 4 para 14(2) and (3)(a) — the amount after the housing cost contributions are deducted` | |
| Sch 4 para 14(3)(b) | 2318 | encoded | uc3-sch4-contributions: `Sch 4 para 14(3)(b) — the further reduction of the award for housing cost contributions` | nil by construction |
| Sch 4 para 15 heading and 15(1)(a), (b) | 2319-2322 | encoded | uc3-sch4-contributions: `Sch 4 para 15(1) — no deduction is made because of the renter` | |
| Sch 4 para 15(2)(a)-(e) | 2323-2339 | encoded | uc3-sch4-contributions: `Sch 4 para 15(2) — the sub-paragraph applies to the person`; uc3-disability-payments: `Sch 3 para 5(3)(b) — a person in receipt of one of the listed payments`, `Sch 4 para 15(2)(e) — a person entitled to one of the listed payments but not receiving it` | "blind" is the keel's reg 2 rule; limb (a) shows dots before "blind" |
| Sch 4 para 16 heading and 16(1) | 2340-2341 | encoded | uc3-sch4-contributions: `Sch 4 para 13 — the number of housing cost contributions to be deducted` | |
| Sch 4 para 16(2)(a)-(i) | 2342-2362 | encoded | uc3-sch4-contributions: `Sch 4 para 16(2) — the sub-paragraph applies to the non-dependant`; uc3-disability-payments: `Sch 4 para 16(2)(c) to (ea) — a person in receipt of one of the listed payments` | (f) is the same six as para 15(2)(e); "prisoner" is the keel's reg 2 rule |
| Sch 4 para 16(2)(j)(i), (ii) | 2363-2365 | encoded | uc3-sch4-contributions: `Sch 4 para 16(2)(j) — a member of the armed forces away on operations` | |
| Sch 4 "Calculations involving more than one accommodation" sub-heading and para 17 heading | 2366-2367 | inert | — | title |
| Sch 4 para 17(1) | 2368 | encoded | uc3-sch4-two-accommodations: type `Renter treated as occupying a single accommodation` | the record is only built where `Sch 3 para 4 — both dwellings are treated as the single accommodation the claimant normally occupies as their home` holds |
| Sch 4 para 17(2)(a), (b) | 2369-2371 | encoded | uc3-sch4-two-accommodations: `Sch 4 para 17(2)(a) — the monthly amount of all the relevant payments in respect of accommodation A and accommodation B`, `Sch 4 para 17(2)(b) — the total number of bedrooms in accommodation A and accommodation B taken together` | |
| Sch 4 para 17(3) | 2372 | encoded | uc3-sch4-two-accommodations: `Sch 4 para 17(3) and (4) — the Part under which the single calculation is made` | "liability to make rent payments in respect of A and B is to a provider of social housing" read as: both landlords are providers (if only one is, the case is "any other case") |
| Sch 4 para 17(4) | 2373 | encoded | uc3-sch4-two-accommodations: the same rule | |
| Sch 4 para 18 heading and 18(1) | 2374-2375 | encoded | uc3-sch4-two-accommodations: `Sch 4 para 18(1) — sub-paragraph (2) applies` | the occupation condition is Sch 3 para 5: `Sch 3 para 5 — the claimant is treated as occupying both the new and the old accommodation` |
| Sch 4 para 18(2), Steps 1 to 3 | 2376-2384 | encoded | uc3-sch4-two-accommodations: `Sch 4 para 18(2) — the amount of the renter's housing costs element` | the amounts of step 1 are inputs: they come from Part 4 or Part 5 |
| Sch 4 para 18(3) | 2385 | inert | — | pure citation of Sch 3 para 5 |
| Sch 4 para 19 heading and 19(1) | 2386-2387 | encoded | uc3-sch4-two-accommodations: `Sch 4 para 19(1) — sub-paragraph (2) applies` | the occupation condition is Sch 3 para 6(2): `Sch 3 para 6(2) — the claimant is treated as normally occupying both` |
| Sch 4 para 19(2), Steps 1 to 3 | 2388-2398 | encoded | uc3-sch4-two-accommodations: `Sch 4 para 19(2) — the amount of the renter's housing costs element`, type `Accommodation the renter normally occupies as their home` | |
| Sch 4 para 19(3) | 2399 | inert | — | pure citation of Sch 3 para 6 |
| Sch 4 Part 4 heading | 2400 | inert | — | title |
| Sch 4 para 20 heading and 20(1) | 2401-2402 | encoded | uc3-sch4-private-sector: `Sch 4 para 20 — Part 4 applies to the renter` | |
| Sch 4 para 20(2) | 2403 | encoded | uc3-sch4-private-sector: the same rule (it does not read the field `the renter is also liable to make service charge payments`) | a test shows the answer unchanged |
| Sch 4 para 21 heading and dots | 2404-2405 | repealed or blank in this text | — | dots |
| Sch 4 "The calculation of the housing costs element under this Part" sub-heading | 2406 | inert | — | title |
| Sch 4 para 22 heading, lead-in, Step 1 | 2407-2413 | encoded | uc3-sch4-private-sector: `Sch 4 para 22 — step 1, the lower of core rent and cap rent` | |
| Sch 4 para 22 Step 2 | 2414-2416 | encoded | uc3-sch4-private-sector: `Sch 4 para 22 — the amount of the renter's housing costs element under Part 4` | uses uc3-sch4-contributions: `Sch 4 para 14(2) and (3)(a) — ...` |
| Sch 4 para 23 heading, lead-in, Steps 1 to 3 | 2417-2425 | encoded | uc3-sch4-private-sector: `Sch 4 para 23 — core rent` | uses uc3-sch4-payments: `Sch 4 para 6 — the monthly amount of all the relevant payments taken into account` |
| Sch 4 para 24 heading and 24(1) | 2426-2427 | encoded | uc3-sch4-private-sector: type `Joint liability for relevant payments` | |
| Sch 4 para 24(2) Steps 1 to 4 | 2428-2437 | encoded | uc3-sch4-private-sector: `Sch 4 para 24(2) — the total monthly amount of the relevant payments for which the renter and others are liable`, `Sch 4 para 24 — core rent for joint tenants` | |
| Sch 4 para 24(3) | 2438 | encoded | uc3-sch4-private-sector: `Sch 4 para 24 — core rent for joint tenants` (no other persons liable) | |
| Sch 4 para 24(4) | 2439-2444 | encoded | uc3-sch4-private-sector: `Sch 4 para 24(4) — the allocated amount by the formula` | the formula is shown as `[formula: ( (A)/(B) ) x C]` in this text |
| Sch 4 para 24(5) | 2445 | encoded | uc3-sch4-private-sector: `Sch 4 para 24 — core rent for joint tenants` (the Secretary of State limb) | the Secretary of State's satisfaction and the amount allocated are stated inputs |
| Sch 4 para 25 heading, 25(1) Steps 1 and 2 | 2446-2452 | encoded | uc3-sch4-private-sector: `Sch 4 para 25 — cap rent`; the category is `Sch 4 para 27(1) — the category of accommodation to which a renter is entitled under Part 4` in uc3-sch4-bedrooms | |
| Sch 4 para 25(2)(a), (b) | 2453-2455 | encoded | uc3-sch4-private-sector: `Sch 4 para 25 — cap rent` (field `local housing allowance which applies at the relevant time to the broad rental market area and the category of accommodation`) | a rent officer's figure under the Rent Officers Order 2013 (not among the inputs): a stated input |
| Sch 4 para 25(3)(a)-(c) | 2456-2459 | encoded | uc3-sch4-private-sector: `Sch 4 para 25(3) — the maximum allowable amount is determined under sub-paragraph (4)` | |
| Sch 4 para 25(4)(a)-(c) | 2460-2463 | fork | uc3-sch4-private-sector: `Sch 4 para 25(4) — the accommodation by reference to which the maximum allowable amount is determined` | U3-F5: the rule depends on history (what was chosen at the first calculation), so that choice is an input; a tie is resolved in favour of accommodation A (but a tie never reaches (4): sub-paragraph (3)(b) needs the amounts to differ) |
| Sch 4 para 25(5) "broad rental market area", "local housing allowance" | 2464-2466 | inert | — | pure citation (Rent Officers Order 2013 articles 3 and 4) |
| Sch 4 para 25(5) "relevant time" | 2467 | encoded | uc3-sch4-private-sector: the wording of the field `local housing allowance which applies at the relevant time to the broad rental market area and the category of accommodation` | the figure is supplied for the day the element is calculated |
| Sch 4 "Further provisions about size criteria for cases to which this Part applies" sub-heading | 2468 | inert | — | title |
| Sch 4 para 26 heading and text | 2469-2470 | encoded | uc3-sch4-bedrooms: `Sch 4 para 26 — the number of bedrooms to which a renter is entitled under Part 4` | |
| Sch 4 para 27 heading and 27(1) | 2471-2472 | encoded | uc3-sch4-bedrooms: `Sch 4 para 27(1) — the category of accommodation to which a renter is entitled under Part 4` | |
| Sch 4 para 27(2) | 2473 | encoded | uc3-sch4-bedrooms: `Category of accommodation` (constructor `shared accommodation`) | the category itself (Rent Officers Order 2013 Sch 1 para 1(a)) is not among the inputs |
| Sch 4 para 28 heading and 28(1) | 2474-2475 | encoded | uc3-sch4-bedrooms: `Sch 4 para 28(1) — a specified renter` | |
| Sch 4 para 28(2)(a), (b) | 2476-2478 | encoded | uc3-sch4-bedrooms: `Sch 4 para 28(2) — the first condition` | |
| Sch 4 para 28(3) | 2479 | encoded | uc3-sch4-bedrooms: `Sch 4 para 28(1) — a specified renter` | reg 4 "responsible for" is uc1's |
| Sch 4 para 28(4) | 2480 | encoded | uc3-sch4-bedrooms: `Sch 4 para 28(1) — a specified renter` | |
| Sch 4 para 29 heading and 29(1) | 2481-2482 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(1) — an excepted person` | there is no sub-paragraph (3) in this text |
| Sch 4 para 29(2) | 2483 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(2) — E is at least 18 but under 25 and was a care leaver` | reg 8 is uc1's |
| Sch 4 para 29(4)(a), (b) | 2484-2486 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(4) — E is at least 16 but under 35 and has lived in hostels and accepted services` | |
| Sch 4 para 29(5)(a)-(d) | 2487-2493 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(5) — E is under 35 and in receipt of a listed payment`; uc3-disability-payments: `Sch 4 para 29(5) — a person in receipt of one of the listed payments` | this six omits pension age disability payment, and para 16(2)'s six omits child disability payment |
| Sch 4 para 29(6) | 2494 | fork | uc3-sch4-bedrooms: `Sch 4 para 29(6) — in England and Wales, E is under 35 and subject to active multi-agency management` | U3-F12: "in relation to England and Wales" read as the nation E's accommodation is in |
| Sch 4 para 29(7) | 2495 | fork | uc3-sch4-bedrooms: `Sch 4 para 29(7) — in Scotland, E is under 35 and subject to active multi-agency risk management` | U3-F12 |
| Sch 4 para 29(8)(a), (b) | 2496-2498 | fork | uc3-sch4-bedrooms: `Sch 4 para 29(8) — in Scotland, E is under 35 and section 10(1)(b) or (d) is not fully in force` | U3-F12 |
| Sch 4 para 29(9)(a), (b) | 2499-2501 | fork | uc3-sch4-bedrooms: `Sch 4 para 29(9) — in Scotland, E is under 35 and section 10(1)(e) is not fully in force` | U3-F12 |
| Sch 4 para 29(9A) | 2502 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(9A) — E is under 35 and satisfies the foster parent condition` | |
| Sch 4 para 29(9B)(a), (b)(i), (ii) | 2503-2507 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(9B) — E is under 35 and has had domestic violence inflicted or threatened, with evidence` | |
| Sch 4 para 29(9C) | 2508 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(9C) — E is under 35 and has been the subject of a positive conclusive grounds determination` | |
| Sch 4 para 29(10) "the 2005 Act" | 2509-2510 | inert | — | pure citation (Management of Offenders etc. (Scotland) Act 2005) |
| Sch 4 para 29(10) "care home", "registered charity", "voluntary organisation" | 2511 | inert | — | pure citation of Schedule 1; used through the Schedule 1 rules |
| Sch 4 para 29(10) "competent authority" | 2512 | inert | — | pure citation (Trafficking Convention); a stated input in para 29(9C) |
| Sch 4 para 29(10) "compulsory labour", "forced labour", "servitude", "slavery" | 2513 | inert | — | pure citation (Article 4 of the European Convention on Human Rights) |
| Sch 4 para 29(10) "hostel" (a)-(c) | 2514-2520 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(10) — hostel` and its limbs | |
| Sch 4 para 29(10) "hostel for homeless people" | 2521 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(10) — hostel for homeless people` | |
| Sch 4 para 29(10) "person acting in an official capacity" | 2522 | encoded | uc3-sch4-bedrooms: `Sch 4 para 29(10) — person acting in an official capacity` | reg 98(4) terms are stated inputs (uc4) |
| Sch 4 para 29(10) "positive conclusive grounds determination relating to modern slavery" | 2523 | encoded | uc3-sch4-bedrooms: field `a competent authority has determined that the renter is a victim of trafficking in human beings, slavery, servitude or forced or compulsory labour` of `Renter who may be an excepted person` | |
| Sch 4 para 29(10) "the Trafficking Convention", "trafficking in human beings" | 2524-2525 | inert | — | pure citation (Council of Europe Convention on Action against Trafficking in Human Beings) |
| Sch 4 Part 5 heading | 2526 | inert | — | title |
| Sch 4 para 30 heading and 30(1) | 2527-2528 | encoded | uc3-sch4-social-sector: `Sch 4 para 30 — Part 5 applies to the renter` | |
| Sch 4 para 30(2) | 2529 | encoded | uc3-sch4-social-sector: the same rule (it does not read the field `the renter is also liable to make service charge payments`) | a test shows the answer unchanged |
| Sch 4 "Amount taken into account as the relevant payment" sub-heading | 2530 | inert | — | title |
| Sch 4 para 31 heading, lead-in, (a), (b) | 2531-2534 | fork | uc3-sch4-social-sector: `Sch 4 para 31 — the amount of the payment after the deduction for a commodity` | U3-F23: the order in which paragraphs 31, 32 and 32A adjust one payment; the Secretary of State's satisfaction is a stated input |
| Sch 4 para 32 heading and 32(1), (2) | 2535-2537 | inert | — | machinery: the Secretary of State's power to apply to a rent officer; its result is read at 32(3) and (4) |
| Sch 4 para 32(3), (4) | 2538-2539 | fork | uc3-sch4-social-sector: `Sch 4 para 32(4) — the rent officer's lower amount is used` and `Sch 4 para 34 Step 1 — the amount of a relevant payment to be taken into account` | U3-F23: the rent officer's lower amount replaces the amount of the payment altogether; "Housing Act functions" is a stated input |
| Sch 4 para 32A heading and 32A(1) | 2540-2541 | fork | uc3-sch4-social-sector: `Sch 4 para 32A(1) — the amount of the payment determined as if no reduction had been applied` | U3-F23 |
| Sch 4 para 32A(2)(a), (b) | 2542-2544 | encoded | uc3-sch4-social-sector: `Sch 4 para 32A(2) — an approved tenant incentive scheme` | |
| Sch 4 "The calculation of the housing costs element under this Part" sub-heading | 2545 | inert | — | title |
| Sch 4 para 33 heading and text | 2546-2551 | encoded | uc3-sch4-social-sector: `Sch 4 para 33 — the amount of the renter's housing costs element under Part 5` | the formula is shown as `[formula: S − H C C]` in this text |
| Sch 4 para 34 heading, lead-in, Steps 1 to 4 | 2552-2562 | encoded | uc3-sch4-social-sector: `Sch 4 para 34 Step 1 — ...`, `Sch 4 para 34 Step 2 — ...`, `Sch 4 para 34 Step 3 — ...`, `Sch 4 para 34 — amount S` | |
| Sch 4 para 35 heading and 35(1) | 2563-2564 | encoded | uc3-sch4-social-sector: type `Joint liability in the social rented sector` | |
| Sch 4 para 35(2) Steps 1 to 4 | 2565-2574 | encoded | uc3-sch4-social-sector: `Sch 4 para 35 — amount S for joint tenants` | |
| Sch 4 para 35(3) | 2575 | encoded | uc3-sch4-social-sector: `Sch 4 para 35 — amount S for joint tenants` (no other persons liable) | |
| Sch 4 para 35(4) | 2576-2581 | fork | uc3-sch4-social-sector: `Sch 4 para 35(4) — amount S by the formula` | U3-F22: no under-occupation deduction in a (4) or (5) case, because paragraph 36(2) names only paragraphs 34 and 35(3); the formula is shown as `[formula: ( (A)/(B) ) x C]` |
| Sch 4 para 35(5) | 2582 | encoded | uc3-sch4-social-sector: `Sch 4 para 35 — amount S for joint tenants` (the Secretary of State limb) | stated inputs |
| Sch 4 para 36 heading and 36(1) | 2583-2584 | encoded | uc3-sch4-social-sector: `Sch 4 para 36(1) — a deduction for under-occupation is to be made`, `Sch 4 para 36 — the number of excess bedrooms` | the entitlement is `Sch 4 para 10 — the number of bedrooms to which a renter is entitled` (paragraphs 8 to 12, without the Part 4 cap) |
| Sch 4 para 36(2)(a), (b) | 2585-2591 | encoded | uc3-sch4-social-sector: `Sch 4 para 36(2) — the amount of the under-occupation deduction` | |
| Sch 4 para 36(3) | 2592 | encoded | uc3-sch4-social-sector: `Sch 4 para 36(3) and (4) — the relevant percentage` | 14% |
| Sch 4 para 36(4) | 2593 | encoded | uc3-sch4-social-sector: the same rule | 25% |
| Sch 4 para 36(5) | 2594 | encoded | uc3-sch4-social-sector: `Sch 4 para 36(1) — a deduction for under-occupation is to be made` (field `regulation 26(4) to (6) (shared ownership) applies`) | reg 26 is uc1's |
| Sch 4 para 36(6)(a)(i)-(iii) | 2595-2600 | encoded | uc3-sch4-social-sector: `Sch 4 para 36(6) — no deduction is made because of domestic violence and a sanctuary scheme` | |
| Sch 4 para 36(6)(b) "person acting in an official capacity" | 2601-2602 | inert | — | pure citation of reg 98(4) (uc4); not the list in Sch 4 para 29(10), which is its own definition |
| Sch 4 para 36(6)(b), line between the two definitions | 2603 | repealed or blank in this text | — | the text shows `...` |
| Sch 4 para 36(6)(b) "sanctuary scheme" | 2604 | encoded | uc3-sch4-social-sector: field `the scheme is a scheme operated by a provider of social housing enabling victims of domestic violence to remain in their homes through the installation of additional security to the property or the perimeter of the property at which the victim resides` of `Facts for the under-occupation deduction` | |
| Sch 5 title and Part 1 heading | 2605-2606 | inert | — | title |
| Sch 5 para 1 heading and 1(1) | 2607-2608 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 1(2) — a claimant is an owner-occupier` | whether reg 26(3) applies is a stated input (uc1) |
| Sch 5 para 1(2) | 2609 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 1(2) — a claimant is an owner-occupier`, `Sch 5 para 1(2) — a joint owner-occupier` | |
| Sch 5 para 1(3) | 2610 | inert | — | machinery: says where the exception to s11(1) is |
| Sch 5 para 1(4) | 2611 | inert | — | machinery: says where the qualifying period is |
| Sch 5 para 1(5) | 2612 | inert | — | machinery: says where the calculation is |
| Sch 5 para 2 heading and lead-in | 2613-2614 | inert | — | title |
| Sch 5 para 2, first definition | 2615 | repealed or blank in this text | — | the text shows `...` |
| Sch 5 para 2, second definition | 2616 | repealed or blank in this text | — | the text shows `...` |
| Sch 5 para 2 "joint owner-occupier" | 2617 | inert | — | pure citation of para 1(2); encoded at `Sch 5 para 1(2) — a joint owner-occupier` |
| Sch 5 para 2, third definition | 2618 | repealed or blank in this text | — | the text shows `...` |
| Sch 5 para 2 "owner-occupier" | 2619 | inert | — | pure citation of para 1(2) |
| Sch 5 para 2 "qualifying period" | 2620 | inert | — | pure citation of para 5(2) |
| Sch 5 para 2 "relevant date" | 2621 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 2 — the relevant date` | defined and never used again in this range |
| Sch 5 para 2 "relevant payments" | 2622 | inert | — | pure citation of para 3 |
| Sch 5 para 2, last definition | 2623 | repealed or blank in this text | — | the text shows `...` |
| Sch 5 para 3 heading and 3(1) | 2624-2625 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 3 — the payment is a relevant payment` | |
| Sch 5 para 3(2) | 2626 | repealed or blank in this text | — | dots |
| Sch 5 para 3(3) | 2627 | fork | uc3-sch5-owner-occupiers: `Sch 5 para 3 — the payment is a relevant payment` | U3-F2: "paragraphs 7 and 8 of that Schedule" has no Schedule to refer to now that sub-paragraph (2) is dots; read as Schedule 1 |
| Sch 5 Part 2 heading | 2628 | inert | — | title |
| Sch 5 para 4 heading and 4(1)(a), (b) | 2629-2632 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 4 — section 11(1) of the Act does not apply to the owner-occupier for the assessment period` | earned income is Chapter 2 of Part 6 (uc2): stated inputs |
| Sch 5 para 4(2) | 2633 | encoded | uc3-sch5-owner-occupiers: the same rule (it does not read the nature of the work, its duration or the amount) | a test shows the answer unchanged |
| Sch 5 para 4(3) | 2634 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 4(3) — paragraph 4 does not prevent an amount calculated under Schedule 4 from being included` | reg 26(4) to (6) is uc1's |
| Sch 5 Part 3 heading | 2635 | inert | — | title |
| Sch 5 para 5 heading and 5(1) | 2636-2637 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 5(1) — the qualifying period ended in an earlier assessment period`, `Sch 5 para 5 — the owner-occupier is past the qualifying period` | |
| Sch 5 para 5(2)(a), (b) | 2638-2642 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 5(2) — the assessment period counts towards the qualifying period`, type `Kind of qualifying period` | 9 consecutive assessment periods |
| Sch 5 para 5(3)(a), (b) | 2643-2645 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 5(1) — the qualifying period ended in an earlier assessment period` (a period that does not count restarts the count at nil) | |
| Sch 5 para 6 heading and 6(1)(a), (b) | 2646-2649 | encoded | uc3-sch5-owner-occupiers: type `Owner-occupier entitled to a jobseeker's allowance or an employment and support allowance` | |
| Sch 5 para 6(2) | 2650 | fork | uc3-sch5-owner-occupiers: `Sch 5 para 6(2) — the assessment periods that the days of benefit are treated as` | U3-F25: "may be treated" is a permission (a stated input); "whole or part of one or more assessment periods" is read as days divided by the days in an assessment period, a fraction |
| Sch 5 para 7 heading and 7(1)(a)-(c) | 2651-2655 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 7(1) — this paragraph applies` | |
| Sch 5 para 7(2) | 2656 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 7(2) — the assessment periods carried forward to the further award` | |
| Sch 5 para 7(3) | 2657 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 5 — the owner-occupier is past the qualifying period` (first limb) | |
| Sch 5 para 7(4)(a), (b) | 2658-2660 | encoded | uc3-sch5-owner-occupiers: the field `the further award is made on a claim`, which no rule reads | the regulation 9(6) Claims and Payments Regulations 2013 is a pure citation; a test shows the answer unchanged |
| Sch 5 Part 4 heading | 2661 | inert | — | title |
| Sch 5 para 8 heading and 8(1) | 2662-2663 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 8 — the payment is taken into account` | the three conditions are reg 25(5) (uc1): stated inputs |
| Sch 5 para 8(2) | 2664 | fork | uc3-sch5-owner-occupiers: `Sch 5 para 8 — the payment is taken into account` | U3-F13: "to the extent that" read as the amount entered being the amount that meets the conditions |
| Sch 5 para 8(3) | 2665 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 8 — the payment is taken into account` | |
| Sch 5 para 9 heading and text | 2666-2667 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 9 — the amount of the owner-occupier's housing costs element` | |
| Sch 5 para 10 heading and dots | 2668-2669 | repealed or blank in this text | — | dots |
| Sch 5 para 11 heading and dots | 2670-2671 | repealed or blank in this text | — | dots |
| Sch 5 para 12 heading and dots | 2672-2673 | repealed or blank in this text | — | dots |
| Sch 5 para 13 heading and 13(1) | 2674-2675 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 13 — the amount in respect of service charge payments` | |
| Sch 5 para 13(2) Steps 1 to 3 | 2676-2682 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 13 — the monthly amount of a service charge payment`, `Sch 5 para 13 — the amount in respect of service charge payments` | |
| Sch 5 para 13(3)(a)-(d) | 2683-2688 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 13 — the monthly amount of a service charge payment` (the keel's `core — the monthly equivalent of a payment`) | "so for example": only the listed intervals are handled |
| Sch 5 para 13(4) | 2689 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 13 — the monthly amount of a service charge payment` | |
| Sch 5 para 13(4A)(a)-(c) and the line after them | 2690-2694 | fork | uc3-sch5-owner-occupiers: field `total number of the service charge payments which the owner-occupier is liable to make in that 12 month period` | U3-F1: the formulas are missing from this text, so the number of payments is a stated input |
| Sch 5 para 13(5) | 2695 | encoded | uc3-sch5-owner-occupiers: `Sch 5 para 13(5) — a service charge free period` | |
| Sch 5A title | 2696 | inert | — | title |
| Sch 5A para 1 heading and lead-in | 2697-2698 | encoded | uc3-sch5a-pre-2026-claimant: `Sch 5A para 1 — the claimant is a pre-2026 claimant` | |
| Sch 5A para 1(a) | 2699 | encoded | uc3-sch5a-pre-2026-claimant: `Sch 5A para 1(a) — entitled to an award including the LCWRA element by virtue of one of paragraphs 2 to 5` | |
| Sch 5A para 1(b) | 2700 | encoded | uc3-sch5a-pre-2026-claimant: `Sch 5A para 1 — the claimant is a pre-2026 claimant` (third limb) | a stated input: continuity of entitlement |
| Sch 5A para 2 heading and 2(1)(a), (b) | 2701-2704 | encoded | uc3-sch5a-pre-2026-claimant: `Sch 5A para 2 — the claimant was awaiting an assessment before 6th April 2026 and is determined to have LCWRA on or after it`, `Sch 5A — 6th April 2026` | reg 41(1)(a) is uc4's |
| Sch 5A para 2(2) | 2705 | encoded | uc3-sch5a-pre-2026-claimant: type `Route by which a decision is made`, which no rule reads | a test shows the answer unchanged; section 9 and 10 of the Social Security Act 1998 are pure citations |
| Sch 5A para 3 heading, lead-in, (a)(i), (ii), (b) | 2706-2711 | encoded | uc3-sch5a-pre-2026-claimant: `Sch 5A para 3 — limited capability for work and awaiting a further assessment before 6th April 2026` | reg 41(1)(b) is uc4's |
| Sch 5A para 4 heading, lead-in, (a)(i), (ii), (b) | 2712-2717 | encoded | uc3-sch5a-pre-2026-claimant: `Sch 5A para 4 — LCWRA before 6th April 2026 with the element left out by regulation 28(1)` | reg 28(1) is uc1's |
| Sch 5A para 5 heading, lead-in, (a), (b) | 2718-2721 | encoded | uc3-sch5a-pre-2026-claimant: `Sch 5A para 5 — entitled to an employment and support allowance before 6th April 2026` | |

## Fork register

Every reading the text does not settle is listed.
Each is "assumed, not ruled": nobody with authority has decided it.
The ids are those cited in the modules and in the coverage table; numbers U3-F10 and U3-F24 are skipped and used nowhere.

| id | provision | the question | reading taken | other reading | where |
| --- | --- | --- | --- | --- | --- |
| U3-F1 | Sch 4 para 7(3A); Sch 5 para 13(4A); lines 2202-2205, 2691-2694 | The text says the total number of payments in a 12 month period "shall be calculated by reference to the formula—" and no formula follows (no `[formula: ...]` marker survived the conversion, unlike paras 24(4), 33 and 36(2)). What is the formula? | Not reconstructed. The total number of payments the renter (owner-occupier) is liable to make in the 12 month period is a plain NUMBER input; the monthly equivalent is the amount of one payment times that number, divided by 12 (the words of 7(3) and 13(4)). | Reconstruct the formulas from another source (not done: the inputs are the only source). | uc3-sch4-payments.l4; uc3-sch5-owner-occupiers.l4 |
| U3-F2 | Sch 5 para 3(3); line 2627 | "paragraphs 7 and 8 of that Schedule": the antecedent was in para 3(2), which is a run of dots. | Read as Schedule 1, the only Schedule with paragraphs 7 and 8 about service charge payments; the same cross-reference is made in terms by Sch 4 para 3(3)(b). | Leave unresolved. | uc3-sch5-owner-occupiers.l4 |
| U3-F3 | Sch 1 para 8(7); line 1950 | Treats certain payments as service charge payments "for the purposes of paragraphs 3(g) and 4(2)"; para 4 of Schedule 1 is a run of dots in this text. | Encoded for para 3(g), which exists; the reference to para 4(2) has nothing to attach to and is not encoded. | Reconstruct para 4. | uc3-sch1-payments.l4 |
| U3-F4 | Sch 1 para 3B(1); line 1884 | Refers to "paragraph (3)(i)", which can only mean para 3(i). | Quoted as printed; read as paragraph 3(i). | None. | uc3-sch1-payments.l4 |
| U3-F5 | Sch 4 para 25(4); lines 2460-2463 | The accommodation by reference to which the maximum allowable amount is fixed is the one with the lower amount "when the calculation is first made", continues "for so long as" para 4 of Schedule 3 applies, and is re-determined on re-housing. That depends on history the rule cannot see. | The accommodation chosen when the calculation was first made (or last re-determined) is a plain input; the rule applies its current local housing allowance. | Compare the two allowances afresh each time. | uc3-sch4-private-sector.l4 |
| U3-F6 | Sch 4 para 10(2); lines 2235 | "allotted to whichever description results in the renter being entitled to the fewest bedrooms" is a minimisation over ways of pairing children. | Computed exhaustively over the four kinds of child (under 10 or not, one sex or the other), pairing each child with a compatible child whenever one exists (a maximum matching always covers any child who has a compatible partner). | A greedy allocation. | uc3-sch4-bedrooms.l4 |
| U3-F7 | Sch 4 para 4; lines 2176-2177 | "Section 11(1) of the Act does not apply to any renter who is 16 or 17 years old and is a care leaver": for joint renters, does one such renter take the element away from both? | The rule is asked of one renter at a time (a stated input: the renter's age and whether they are a care leaver). | The element is lost for the whole award if any joint renter is a 16 or 17 year old care leaver. | uc3-sch4-interpretation.l4 |
| U3-F8 | Sch 3 paras 5(4), 6(4), 7(3), 8(2), 9; Sch 4 para 11 | The text counts months ("the first 6 months of the absence", "exceeds, or is expected to exceed, 6 months", "for more than one month") and never says how a month is counted from a day. | Within the first N months means: the day is on or after the start day and before the day N months after it. A period that ends on a last day exceeds N months if the last day is on or after the day N months after the start day. So 1 January to 30 June is exactly 6 months and does not exceed them; 1 July does. The day N months later moves back to the last day of a shorter month (the keel's date rule). | Count from the day after the start; count whole calendar months. | uc3-periods.l4 |
| U3-F9 | Sch 4 para 10(1); lines 2227-2234 | "Two children of the same sex" and "the renter (or joint renters)" as one bedroom. | Sex is two groups (male, female); joint renters have one bedroom between them (para 12(6A), which gives an additional bedroom to a joint renter who cannot share, confirms that the couple would otherwise share). | A third group, or one bedroom per joint renter. | uc3-sch4-bedrooms.l4 |
| U3-F11 | Sch 4 para 12(6), (8), (9)(c); lines 2286-2307 | "Would (but for the provisions of this paragraph) be expected to share a bedroom", and whether the amount in sub-paragraph (8) is added to the one additional bedroom of (9)(c). | A child "would be expected to share" if giving them a bedroom of their own needs at least one more bedroom than the children would otherwise need; (8) gives as many additional bedrooms as are necessary for each such child to have their own; (9)(c) is read as the same amount, not another one on top. | (9)(c) adds one bedroom to the amount of (8). | uc3-sch4-bedrooms.l4 |
| U3-F12 | Sch 4 para 29(6) to (9); lines 2494-2501 | "In relation to England and Wales" and "In relation to Scotland". | The nation in which E's accommodation is (an input on the record). | The nation in which E was convicted or is supervised. | uc3-sch4-bedrooms.l4 |
| U3-F13 | Sch 1 para 8(4) and (6); Sch 4 para 6(2); Sch 5 para 8(2) | "To the extent that" and "only where". | The amount entered is the amount that meets the conditions; the payment under test is the part that fits the category. | Whole-payment tests. | uc3-sch1-payments.l4; uc3-sch4-payments.l4; uc3-sch5-owner-occupiers.l4 |
| U3-F14 | Sch 1 para 3A(5)(a); lines 1873-1875 | "Would be a hostel within the meaning of paragraph 29(10) of Schedule 4 but for it being owned or managed by a local authority": what has to be true of a building that is not a hostel only because of its owner? | The building meets limb (a) of the hostel test in Sch 4 para 29(10), is not a care home, would pass the test if a local authority counted as a provider of social housing, and is not a hostel on the full test. | Only the owner is tested; the other limbs of the hostel test are left open. | uc3-sch1-payments.l4 |
| U3-F15 | Sch 2 Parts 1 and 2 | Which Part prevails if both apply to one liability. | Part 2 prevails: every provision of Part 2 is an exception, and paragraphs 9(2) and 10(2) read Part 2 as overrides. | Part 1 prevails, or the liability is undecided. | uc3-sch2-liability.l4 |
| U3-F16 | Sch 2 para 2(3); line 1965 | "Regard may be had to the fact that continuing to make the payments may benefit the person with the liability": a permission about how a judgement is reached. | Not a condition; quoted beside the input for paragraph 2(2)(d). | An additional input. | uc3-sch2-liability.l4 |
| U3-F17 | Sch 2 para 6(4), (8); lines 2008-2025 | "Shares" and "voting power" are defined by what they are, not by how a percentage is measured. | The percentages are stated inputs. | Compute them from share registers. | uc3-sch2-liability.l4 |
| U3-F18 | Sch 2 para 6(5); lines 2004-2007 | "A" is the person, any of their associates, or the person and associates taken together. | Only the combined holding is computed, because every limb of 6(4) is monotone in the holding (the combined holding is at least as large as any single holder's). | Test each holder separately and together. | uc3-sch2-liability.l4 |
| U3-F19 | Sch 3 paras 5(4), 6(4), 7(3), 8(2) | The text bounds a situation by "more than one month" or "more than 12 months" and does not say from when. | From the first day on which the claimant is treated as occupying the accommodation under that paragraph (an input); the day asked about is the other input. | From the day the claimant moved. | uc3-sch3-occupation.l4 |
| U3-F20 | Sch 3 para 6(2) to (4); lines 2102-2107 | After 12 months, para 6(2) no longer treats the claimant as occupying both and para 6(3) is about one accommodation only; the text does not say what applies. | The rule gives an explicit value, "not covered: the text does not say which accommodation the claimant is treated as occupying once the 12 months of paragraph 6(4) have passed", and asserts it. | Fall back to the general rule of paragraph 1, or to paragraph 6(3). | uc3-sch3-occupation.l4 |
| U3-F21 | Sch 3 para 1(3); line 2057 | Which dwelling is normally occupied is "all the circumstances". | The answer is the input "this is the accommodation I normally occupy as my home". | Model the circumstances. | uc3-sch3-occupation.l4 |
| U3-F22 | Sch 4 paras 35(4), (5), 36(2); lines 2576-2590 | Paragraph 36(2) defines the under-occupation deduction only for paragraph 34 and for 35(3). | There is no deduction in a 35(4) or 35(5) case. | Apply the percentage to the share. | uc3-sch4-social-sector.l4 |
| U3-F23 | Sch 4 paras 31, 32, 32A; lines 2531-2541 | The order in which the commodity deduction, the rent officer's lower amount and the tenant incentive scheme reduction adjust one payment. | 32A first (as if no reduction had been applied), then 31 (the commodity deduction), then 32(4) (the rent officer's lower amount replaces the amount of the payment altogether unless the Secretary of State is satisfied it is not appropriate). | A different order. | uc3-sch4-social-sector.l4 |
| U3-F25 | Sch 5 para 6(2); line 2650 | "May be treated as if it were the whole or part of one or more assessment periods, as determined by the number of days". | A permission (a stated input); the days are divided by the days in an assessment period, so a part of a period is a fraction; the credited periods start the count of qualifying periods, and nine in all are needed. | Whole periods only. | uc3-sch5-owner-occupiers.l4 |

Not all of these are forks of the meaning of words; a few (F16, F17, F21) are decisions to carry a judgement as an input.

## Cross-references out of my ranges

38 places in the modules are marked `-- out of range:` (collect them with `grep -n 'out of range' uc3-sch*.l4`); the first twelve rows group them by what they depend on, naming the provision of mine and the module for each.
The remaining rows are dependencies that sit in a module header or inside a rule rather than behind a marker.
Every one is a stated input: no module reads, calls or imports another piece's module.

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| Sch 2 para 1 (uc3-sch2-liability); Sch 2 para 5(1) (uc3-sch2-liability); Sch 2 para 6(1) (uc3-sch2-liability); Sch 2 para 7(1) (uc3-sch2-liability); Sch 3 para 4 (uc3-sch3-occupation); Sch 3 para 5(3) (uc3-sch3-occupation); Sch 4 para 16(2) (uc3-sch4-contributions); Sch 4 para 2 "listed persons" (uc3-sch4-interpretation); Sch 4 para 28 (uc3-sch4-bedrooms); Sch 4 para 9(1) (uc3-sch4-bedrooms) | reg 4: "responsible for a child or qualifying young person" | uc1 | a BOOLEAN on the record that needs it ("responsible for ...") |
| Sch 4 para 11(2) (uc3-sch4-bedrooms) | reg 4(6)(a), 4(6)(b), 4(7): a child looked after by a local authority; a child who is a prisoner; an absence exceeding the specified duration | uc1 | one BOOLEAN each |
| Sch 4 para 29(1) (uc3-sch4-bedrooms); Sch 4 para 4 (uc3-sch4-interpretation) | reg 8: "care leaver" | uc1 | a BOOLEAN `care leaver` |
| Sch 4 para 11(3) (uc3-sch4-bedrooms); Sch 4 para 11(4) and (5) (uc3-sch4-bedrooms) | reg 11(1) to (3): temporary absence from Great Britain; death of a close relative; treatment | uc1 | one BOOLEAN each |
| Sch 4 para 11(3) (uc3-sch4-bedrooms) | reg 19(2): prisoners | uc1 | a BOOLEAN |
| Sch 3 para 3 (uc3-sch3-occupation); Sch 3 para 4 (uc3-sch3-occupation); Sch 3 para 5 (uc3-sch3-occupation); Sch 3 para 6 (uc3-sch3-occupation); Sch 3 para 7 (uc3-sch3-occupation); Sch 3 para 8 (uc3-sch3-occupation); Sch 4 para 3 (uc3-sch4-payments); Sch 5 para 7(1), (2) and (4) (uc3-sch5-owner-occupiers); Sch 5 para 8 (uc3-sch5-owner-occupiers) | reg 25(5): the payment, liability and occupation conditions | uc1 | BOOLEANs on the liability records; in the seat one answer feeds all three |
| Sch 4 para 1(1) and (2) (uc3-sch4-interpretation); Sch 5 para 1(1) and (2) (uc3-sch5-owner-occupiers) | reg 26(2), 26(3): who is a renter, who is an owner-occupier | uc1 | a BOOLEAN |
| Sch 5A para 4 (uc3-sch5a-pre-2026-claimant) | reg 28(1): the relevant period for the LCWRA element | uc1 | a day (stand-in) from a BOOLEAN |
| Sch 5A para 2 (uc3-sch5a-pre-2026-claimant); Sch 5A para 3 (uc3-sch5a-pre-2026-claimant) | reg 41(1)(a), (b): awaiting an assessment under Part 5 | uc4 | a day (stand-in) from a BOOLEAN |
| Sch 4 para 12(4) and (5) (uc3-sch4-bedrooms) | reg 89(3)(a): "adopter" | uc4 | a BOOLEAN |
| Sch 4 para 29(10) "person acting in an official capacity" (uc3-sch4-bedrooms); Sch 4 para 36(1) (uc3-sch4-social-sector) | reg 98(4): "health care professional", "registered social worker", "person acting in an official capacity" | uc4 | BOOLEANs, one per kind of person |
| Sch 5 para 4 (uc3-sch5-owner-occupiers) | Chapter 2 of Part 6: earned income | uc2 | a BOOLEAN `the owner-occupier has any earned income`, and the same for the other member of the couple |
| Sch 2 para 1 (`uc3-sch2-liability`); mentioned in the module header, not as a marker | reg 3(4): claiming as a single person | uc1 | a BOOLEAN `claiming as a single person by virtue of regulation 3(4)` |
| Sch 4 Part 5 para 36(5) (`uc3-sch4-social-sector`); Sch 5 para 4(3) (`uc3-sch5-owner-occupiers`); mentioned in the module headers, not as markers | reg 26(4) to (6): shared ownership | uc1 | a BOOLEAN `regulation 26(4) to (6) (shared ownership) applies` |
| Sch 5A para 1 (`uc3-sch5a-pre-2026-claimant`); named in the module header | reg 27A(1) and reg 27: regulation 27A(1) gives the first circumstances of a "pre-2026 claimant" and regulation 27 reads the result; Schedule 5A para 1 adds further circumstances | uc1 | none taken from uc1: this piece answers "does a Schedule 5A circumstance apply" (`Sch 5A para 1 — the claimant is a pre-2026 claimant`, seat question 55) and leaves regulation 27A(1)'s own test to uc1; KEEL-NOTES item 6 proposes uc1 take that answer as a BOOLEAN input (proposed, not ruled) |
| every `core — ...` and `reg 2 — ...` rule the modules call (local authority, close relative, foster parent, partner, prisoner, blind, the date rule, the monthly equivalent, the number of days in an assessment period) | reg 2 and the core helpers | uc-g0 (the keel) | used as the keel has them, not as inputs |
| every amount (Sch 4 Parts 3 to 5; Sch 5 Part 4) | reg 6: rounding | uc1 | not applied: the amounts are exact (see Before this is worth relying on) |
| Sch 4 para 25 (`uc3-sch4-private-sector`) | the Rent Officers Order 2013: the local housing allowance for the area and category of accommodation | external | a NUMBER input |
| Sch 4 para 32 (`uc3-sch4-social-sector`) | a rent officer's determination of a lower amount (Housing Act functions) | external | a BOOLEAN and a NUMBER |
| Sch 1 para 1 (`uc3-sch1-interpretation`) | the definitions point to other law: the National Health Service Act 2006 s275 and the 1978 Act s10F, the Care Standards Act 2000 (independent hospital, care home), the Regulation and Inspection of Social Care (Wales) Act 2016, the Public Services Reform (Scotland) Act 2010, the Charities Act 2011 and the Charities and Trustee Investment (Scotland) Act 2005 | external | a BOOLEAN per limb of each definition |
| Sch 1 paras 3, 7 (`uc3-sch1-payments`) | the Loans for Mortgage Interest Regulations 2017 (a qualifying loan; owner-occupier payments) | external | a BOOLEAN each |

## Needs from the core

1. **Regulation 4, "responsible for a child or qualifying young person".** 10 places here take it as a BOOLEAN. A keel rule over the household would let them derive it, and would make Sch 4 para 11(2) (reg 4(6), 4(7)) agree with reg 4.
2. **Regulation 25(5)'s three conditions** (payment, liability, occupation) as one record that Sch 4 para 6 and Sch 5 para 8 could take, instead of BOOLEAN inputs each.
3. **A month-counting convention.** `uc3-periods` holds two helper rules ("within the first N months of a start day"; "a period exceeds N months") over the keel's date rule. Any piece that counts months should share one convention (fork U3-F8); this is better as a keel rule.
4. **A rounding rule at the right step.** The keel has `core — an amount rounded to the nearest penny`; the text does not say at which step regulation 6 bites, so none of the amounts here is rounded.
5. **The Schedule 5A hand-off.** KEEL-NOTES item 6 proposes that uc1 encode regulation 27A(1) and take "meets a circumstance in Schedule 5A" as a BOOLEAN input, fed by this piece's answer. That is proposed, not ruled. This piece offers `Sch 5A para 1 — the claimant is a pre-2026 claimant` (layer 1) and seat question 55; it does not restate regulation 27A(1).
6. **`YMD`.** The stable prelude has none; every module uses the keel's shim. If the stable build gains a real constructor, the shim is the one place to change.

## What the text turns out to say

1. **A payment that is partly for services is a service charge payment as a whole, and so is not a rent payment.** Schedule 1 paragraph 7(2) takes in a payment that is "in whole or in part" for services or facilities; paragraph 7(4)(b) makes it irrelevant that it is made "as part of" a rent payment; paragraph 3(g) then excludes service charge payments from rent payments. A single payment of "rent including services" is therefore not a rent payment. Asserted (a seat case; `uc3-tests-sch1.l4` tests the 3(g) exclusion).
2. **In a Part 5 or Schedule 5 case, a payment that fails a condition of paragraph 8 is neither a service charge payment nor a rent payment.** Paragraph 7(1)(c) makes meeting the paragraph 8 conditions part of being a service charge payment. Paragraph 8(7) then treats a payment that fails only those conditions as a service charge payment "for the purposes of paragraphs 3(g) and 4(2)", so 3(g) still keeps it out of rent payments. Paragraph 4(2) is dots in this text (fork U3-F3). Asserted (`uc3-tests-sch1.l4`, paragraph 8(7) block).
3. **The disability payments are written out in nine places, in four different lists.** Seven payments in Schedule 3 paragraph 5(3)(b) and Schedule 4 paragraphs 12(3)(a), 12(6A)(a) and 15(2)(b) to (da); two in paragraph 12(6)(a); six without child disability payment in paragraph 16(2)(c) to (ea) and in the "entitled but not receiving" limbs of paragraphs 15(2)(e) and 16(2)(f); six without pension age disability payment in paragraph 29(5). A reader who assumes one list is wrong in at least three of the four. Asserted payment by payment (`uc3-tests-sch4-bedrooms.l4`).
4. **Parts of this text are blank.** Schedule 1 paragraph 3(e) and paragraphs 4 to 6; Schedule 4 paragraphs 4A to 4C, 12(1)(a), 12(7) and 21; Schedule 5 paragraph 2 (in part), 3(2) and paragraphs 10 to 12 are runs of dots. Schedule 4 paragraph 29 has no sub-paragraph (3). Schedule 5 paragraph 3(1) makes "relevant payments" service charge payments only, so the interest and alternative finance paragraphs (10 to 12) that would have added others are blank. Not asserted (an absence).
5. **Two sub-paragraphs promise a formula and give none.** Schedule 4 paragraph 7(3A) and Schedule 5 paragraph 13(4A) say the total number of payments "shall be calculated by reference to the formula" and no formula follows (fork U3-F1). The number is an input.
6. **After 12 months the text goes quiet.** Schedule 3 paragraph 6(2) stops treating the claimant as occupying both homes after 12 months, and nothing says what then applies (fork U3-F20). Asserted (`uc3-tests-sch3.l4` and a seat case).
7. **A shared-liability case under paragraph 35(4) or (5) has no under-occupation deduction.** Paragraph 36(2) defines the deduction only for paragraphs 34 and 35(3) (fork U3-F22). Asserted (`uc3-tests-sch4-parts.l4`).
8. **Equal allowances are not "different".** Schedule 4 paragraph 25(3)(b) needs the allowances for A and B to differ before paragraph 25(4) applies; when they are equal the ordinary allowance is used. Asserted (`uc3-tests-sch4-parts.l4` and a seat case).
9. **A non-dependant who is a son or daughter in the armed forces away on operations is counted for any period.** Paragraph 11(5)(d) has no time limit, and paragraph 11(4)(b) asks whether the renter's award included the housing costs element only "in the circumstances specified in sub-paragraph (5)(a) to (c)". Asserted (`uc3-tests-sch4-bedrooms.l4` and a seat case).
10. **Joint claimants are never a specified renter.** Paragraph 28(2) speaks of "a single person (or a member of a couple claiming as a single person)". Asserted (a seat case).
11. **The qualifying period of Schedule 5 must have ended before the assessment period in which the element starts.** Paragraph 5(1) includes the element "until the beginning of the assessment period that follows the assessment period in which the qualifying period ends"; nine consecutive qualifying periods before the one asked about are enough, eight are not (the seat counts the periods before this one). Paragraph 7(3) removes the qualifying period when an amount was already included in the award that ended. Asserted (`uc3-tests-sch5.l4` and seat cases).
12. **One joint renter with a listed payment exempts both from the deductions.** Paragraph 15(1)(b): no deduction "where at least one joint renter" is such a person. Asserted (`uc3-tests-sch4-contributions.l4` and a seat case).
13. **Paragraph 14(3) makes the element nil, not negative.** When the contributions exceed the amount, the amount is reduced to nil and no further reduction is made from the renter's award. Asserted (`uc3-tests-sch4-contributions.l4`).
14. **The range contains no commencement provision.** The only date it fixes is 6th April 2026 in Schedule 5A. Not asserted.
15. **Schedule 5A is in the line range but not in the brief's list of Schedules.** The brief describes the piece as Schedules 1 to 5 and gives lines 1821-2721; Schedule 5A is lines 2696-2721 and no other piece owns it, so it is encoded here. Not asserted.

## What the stable binary does not accept

The target is the stable build 1.6.98.
Each item below marked "probed" was tried on a one-line file in this session and the binary's answer read.

Loud (the binary refuses or warns, and says where):

- `a NOT EQUALS b`: a parse error, "unexpected NOT" (probed). Write `NOT (a EQUALS b)`.
- `x APPENDED TO ys`: a parse error, "unexpected TO" (probed). Write `append (ys) (LIST x)`.
- `length xs`: "I could not find a definition for the identifier" (probed); `count xs` works (probed).
- AND and OR at one indentation: a linter warning, "AND and OR operators appear at the same indentation level" (probed). Parenthesise every operand.
- A test file that is `IMPORT`ed, or an `IMPORT` of a module in another folder: IMPORT finds only modules beside the importing file.
- `REFUSE`, `#ASSERT REFUSED ... BECAUSE`, `YMD`, a section-level `GIVEN`, `TYPICALLY` on a field, sets (`SET OF`, `UNION`) and a bodiless `DECLARE` (opaque type) are rejected by the stable build, with the errors quoted in `references/dialects.md` of the writing-l4-rules skill (not probed again here); the modules use none of them except `YMD`, which the keel supplies as a shim.

Quiet (no error; the thing just is not there):

- There is no record update, so a test or builder writes the whole record again with `Type WITH field IS value` (recalled from earlier work in this session, not probed).
- `YMD` is not in the stable prelude; the keel's shim provides it (the keel says so in `uc-core.l4`).
- A field named `is big` in backticks compiles and reads back (probed), so no rule against names starting `is` or `has` is stated here.
- `l4 run` prints each satisfied assertion twice (a Message line and a Result line); count `Message:  assertion satisfied` only. A clean file prints `Checking succeeded.`
- Each `#ASSERT` is written on one line, so a call with dozens of arguments is one long line (recalled, not probed).
- Names are unique across all the modules in the folder, so helper rules carry a prefix (`uc3 test —`, `uc3 case —`, `uc3 seat —`) (recalled, not probed).
- Type-checking is slow: the imports alone took about six minutes under load, and the whole seat about the same.
- A blank line between `@export` and `GIVEN` compiled when tried earlier in this session; the seat is written without one (recalled, not probed again).

## What check.sh prints

Run in this folder as `L4=<wrapper around the stable l4 1.6.98> L4_TARGET=unstable ./check.sh`, after the last edit to any `.l4` file.
(`unstable` here only tells the script to skip its comparison with a main build; the brief sets this command. The wrapper ran the real binary and kept a copy of each module's output so the warnings could be counted; it changes nothing the script reads.)
Standard output:

```
module                                    errors satisfied  failed  refused  expected
uc-core-bodies.l4                              0         0       0        0         0
uc-core-payments.l4                            0         0       0        0         0
uc-core-persons.l4                             0         0       0        0         0
uc-core.l4                                     0         0       0        0         0
uc3-cases-seat.l4                              0       256       0        0         0
uc3-disability-payments.l4                     0         0       0        0         0
uc3-periods.l4                                 0         0       0        0         0
uc3-sch1-interpretation.l4                     0         0       0        0         0
uc3-sch1-payments.l4                           0         0       0        0         0
uc3-sch2-liability.l4                          0         0       0        0         0
uc3-sch3-occupation.l4                         0         0       0        0         0
uc3-sch4-bedrooms.l4                           0         0       0        0         0
uc3-sch4-contributions.l4                      0         0       0        0         0
uc3-sch4-interpretation.l4                     0         0       0        0         0
uc3-sch4-payments.l4                           0         0       0        0         0
uc3-sch4-private-sector.l4                     0         0       0        0         0
uc3-sch4-social-sector.l4                      0         0       0        0         0
uc3-sch4-two-accommodations.l4                 0         0       0        0         0
uc3-sch5-owner-occupiers.l4                    0         0       0        0         0
uc3-sch5a-pre-2026-claimant.l4                 0         0       0        0         0
uc3-seat.l4                                    0         0       0        0         0
uc3-tests-sch1.l4                              0       118       0        0         0
uc3-tests-sch2.l4                              0       106       0        0         0
uc3-tests-sch3.l4                              0        75       0        0         0
uc3-tests-sch4-bedrooms.l4                     0       281       0        0         0
uc3-tests-sch4-contributions.l4                0        42       0        0         0
uc3-tests-sch4-parts.l4                        0       106       0        0         0
uc3-tests-sch4-payments.l4                     0        38       0        0         0
uc3-tests-sch5.l4                              0       115       0        0         0
TOTAL (29 modules)                             0      1137       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Standard error:

```
check.sh: the target is unstable, so the main check was skipped.
```

The script's exit 0.
Counted in the saved copy of each module's output: `DiagnosticSeverity_Warning` appears 0 times in all 29 modules.

## Before this is worth relying on

1. **The source is a plain-text rendering, not the official text.** Nothing here has been checked against the official text. The deposit's metadata lists 12 outstanding effects (ten against the table of contents, two against regulation 99(6)(a) and (b)) and 4 prospective unapplied effects that it does not place (KEEL-NOTES, "Unapplied effects"); none of the 12 is in this range, and the 4 may be. It also says the text is a revised text that "may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish".
2. **The expected values were written by the same agent that wrote the rules.** The layer-1 tests and the seat cases were derived from the text before each run. For the layer-1 tests a negative control (one expected value changed on a copy) printed `assertion failed` as it should. For the seat cases a control on a scratch copy of the seat and its imports changed three expected values (one TRUE to FALSE, one FALSE to TRUE, one number by one) and all three printed `assertion failed`. A misreading shared by rule and test passes both. A lawyer should read the forks.
3. **23 forks are assumed, not ruled** (see the register). The ones most likely to change an amount are U3-F22 (no under-occupation deduction in a shared case), U3-F23 (order of the adjustments) and U3-F1 (the number of payments with free periods).
4. **The formulas for rent free periods are missing from the text** (fork U3-F1); the number of payments is an input.
5. **Nothing is rounded.** Regulation 6 is outside this range and the text does not say at which step it bites, so the amounts are exact decimals or fractions.
6. **Judgements are inputs.** Whether the Secretary of State is satisfied (Sch 2 para 10; Sch 4 paras 24(5), 31, 32, 35(5); Sch 5 para 6), and the all-the-circumstances tests in Sch 2 para 2 and Sch 3 para 1(3), are asked, not decided.
7. **Everything out of range is an input** (see the cross-references): who is responsible for a child, the three conditions of regulation 25(5), regulation 26's classes, earned income, and the local housing allowance.
8. **The seat has limits** (see Seat): one person per list condition, two service charges, one hostel stay, and the stand-in days of Schedule 5A.
9. **No one outside this session has read the wording of the questions.** The `@desc` text was written for a person who does not know the Regulations; it has not been tested on one.
