# Economic Development Board Act 1961 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation (version in force from
1/4/2022), as deposited at `../../registers/source-bundle/EDBA1961.txt`. The cover
says the edition incorporates amendments up to 1 December 2021; the latest amendment
annotated in the body is Act 25 of 2021, with effect from 1 April 2022 (s 21(12)).

**Checks:** one case file, 57 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers requirement **REQ-0169** in `subjects/sg/requirements.jsonl`: tier 3
of the remaining Singapore Acts, ordered by everyday-life relevance. The requirement
asks what the Act decides for a person or business it applies to; no scenario has
asked a sharper question yet.

Most of the Act sets up the Board. The parts a business meets are the lending and
incentive provisions and the two offences, so this row takes: the definition of
"enterprise" (ss 2, 22), the powers over enterprises that need the Minister's
written approval and the loan-guarantee limit (s 18(2)), the Board's rights on
default (s 19(1)), early recall of a loan, advance or incentive (s 20), the High
Court route, its appeal period and the stay on release orders (s 21(1), (7), (11),
(13)), immunity for erroneous public information (s 14(3)), creditor protection of
staff pension moneys (s 11(2)(a), (b)), misuse of the Board's name or symbol (s 27A)
and secrecy (s 27B).

Not encoded: the Board's establishment and constitution (ss 3-5 and the Schedule),
its functions (s 6), directions, chief executive and staff (ss 7-9), committees and
delegation (s 12), finance, borrowing and shares (ss 16-17A), compulsory acquisition
(s 23), land registration (s 26), the seal (s 27), winding up (s 28), regulations
(s 29), the rest of s 11(2), s 14(1)-(2), s 19(2)-(4) and the interim-order mechanics
of s 21.

## What the Act turns out to say

### 1. The Board can call in a loan or incentive "despite any agreement to the contrary", including whenever it thinks it necessary

s 20 lets the Board require an enterprise to discharge its liabilities in full
immediately, by notice, on six grounds. Five are concrete (a misleading application,
breach, apprehended insolvency, uninsured or 20%-depreciated security, unreplaced
removal of machinery); the sixth is "if for any reason it is necessary in the opinion
of the Board to protect the interests of the Board". It reaches incentives as well as
loans and advances. Asserted.

### 2. On default the Board may take over the management of the business, with or without a court

s 19(1) gives the Board "the right to take over the management of the enterprise, as
well as the right to sell and realise" the security, on any default or breach, and
s 19(4) makes it the owner for suits. s 19 says nothing about a court order; s 21
provides a separate High Court route to the same reliefs. Whether s 19 is meant to be
exercised without a court is not stated; that it may be is an inference from the
contrast. Asserted (the s 19(1) conditions only).

### 3. The 20% depreciation ground is cured by further security; the uninsured ground is read as not cured

s 20(d): the security "is not insured and kept insured ..., or depreciates in value
... by more than 20% and further security to the satisfaction of the Board is not
given". The encoding reads the further-security clause as qualifying only the
depreciation limb, so exactly 20% is not a ground, 25% is, and 25% with further
security is not; an uninsured security is a ground even if further security is
offered. The other reading is grammatically possible. Asserted.

### 4. A default order under s 21(7) falls outside the 30-day appeal in s 21(13)

s 21(13) allows an appeal "within 30 days after the date of the order" only against
orders under subsections (9) and (10), the orders made after cause is shown. If the
enterprise shows no cause, s 21(7) obliges the Judge to "immediately make the interim
order final", and s 21(13) does not name that order. Other appeal routes were not
examined. A release order is stayed for the appeal period unless the Board says it
will not appeal (s 21(11)). Asserted.

### 5. A guarantee needs ministerial approval and a term of 25 years or less, unless the loan is publicly floated

s 18(2)(b): written approval of the Minister, and a loan "repayable within a period
not exceeding 25 years" or "floated in the public market". Underwriting, establishing
or investing in enterprises, and compensating people damaged by the Board's powers
also need written approval; lending and nominating directors do not. Asserted.

### 6. Secrecy binds former staff, and the misuse offence has no exceptions

s 27B binds anyone who "is or has been" a member, officer, employee, agent or
committee member. Disclosure is excused on five grounds ((c)-(g)); use of the
information for anyone's personal benefit (s 27B(2)) has none. The maximum is $10,000
or 12 months, against $10,000 or 6 months (plus $250 a day continuing) for using a
name or symbol that resembles the Board's so as to be likely to deceive or confuse
(s 27A). Asserted.

### 7. Smaller points

"Enterprise" covers any entity, for profit or not, Singapore or foreign, and a branch
(s 2). Pension and provident moneys of Board staff can be garnished only for debts
due to the Board or the Government (s 11(2)(a), (b)). Public information supplied
under a written law in good faith carries no liability for errors (s 14(3)).
Asserted.

## What would need doing before this is worth anything

- s 22 imports the pre-1997 Tourist Promotion Board Act definition of "tourist
  enterprise", which was not deposited and is not modelled.
- No case law on ss 19-21 was searched, and no subsidiary legislation (the
  particulars "prescribed" for a s 21 application) was retrieved.
- The s 20(d) reading in finding 3 needs a lawyer's view.
- Whether a s 21(7) order is appealable by another route needs checking against the
  Supreme Court of Judicature Act and the Rules of Court.
