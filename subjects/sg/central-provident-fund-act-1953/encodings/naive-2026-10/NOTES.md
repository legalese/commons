# Central Provident Fund Act 1953, section 15 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
1 July 2026.

**Checks:** `l4 run cpf-cases.l4`, `l4 run cpf-medisave-cases.l4`, `l4 run cpf-rates-and-death-cases.l4`,
`l4 run cpf-allocation-and-exemption-cases.l4`, `l4 run cpf-self-employed-cases.l4`,
`l4 run cpf-self-employed-rates-cases.l4` and `l4 run cpf-exemption-current-cases.l4` -- 274 assertions satisfied,
0 errors, 0 warnings. Of these, 60 predate 11 October 2026. On that day 41 were added for REQ-0001 and REQ-0012,
35 for REQ-0002 and REQ-0003, and 46 for REQ-0268; on 12 October 2026 a further 46 were added for REQ-0268 from the
Self-Employed Persons Regulations, and 46 for REQ-0265 from the current Exemption Order.

## Scope — read this first

The CPF Act is about **911,000 characters**. This encodes **s 7, s 15(1)–(6),
s 16 and s 25(1)**, plus the s 2 definition of "applicable person". That is a
few pages out of a very large statute.

*(The section below describes the first pass only. See "Added with sections 7,
16 and 25" at the foot of this file, which corrects it.)*

Not encoded: contributions (ss 7–9D), the subsidiary accounts (s 13), housing
and investment charges, nominations (s 25), the Retirement Sum Scheme machinery
in s 15AA, the Board's discretionary power in s 15(4), section 16 (which s 15(2)
and (3) are both expressed to be subject to), and everything from Part 3A
onwards.

The prescribed retirement sum, the prescribed classes of applicable person, and
the Board's conditions are all **facts supplied**. The regulations were not
retrieved, and they carry most of the practical content.

## Three observations

**1. There are now only two routes out of the Fund, and one of them is leaving
the country.** s 15(2) once had seven paragraphs. (c) to (g) were repealed
between 2021 and 2024, and what remains is:

- **(a)** the member has attained 55; or
- **(b)** the member **is not an applicable person** — that is, is neither a
  citizen nor a permanent resident of Singapore (nor of a prescribed class).

So the Act's own structure now reads: wait until 55, or cease to be a citizen or
permanent resident. Asserted on the foreigner aged 40, who may withdraw at any
age.

**2. The retirement-sum set-aside binds the member who stays and not the one
who goes.** s 15(6) attaches the set-aside to entitlements under (2)(a), (3) and
(4). It does **not** attach to (2)(b). Two members with identical accounts
therefore come out very differently:

| | credit | retirement sum | may withdraw |
|---|---|---|---|
| citizen, aged 60, s 15(2)(a) | $200,000 | $100,000 | **$100,000** |
| non-citizen, aged 40, s 15(2)(b) | $200,000 | $100,000 | **$200,000** |

Asserted as a pair. There is an obvious policy reading — the retirement sum
exists to fund a retirement in Singapore, and someone who has ceased to be a
citizen or permanent resident is not having one — so this is recorded as a
consequence of the drafting rather than as a defect. It is worth stating because
it is invisible unless (2), (3) and (6) are read together.

**3. s 15(3) attaches to one ground and not the other.** The annual further
withdrawal is for "a member of the Fund who has withdrawn any money from the
Fund **on the ground that he or she has attained 55 years of age**". A member who
withdrew under (2)(b) is outside it — which makes sense, because they were
entitled to the whole sum and have nothing left to come back for, but the
drafting achieves it by naming the ground rather than by saying so.

## An honest limit

`the amount this member may withdraw` is the function a person would actually
want to call, and it is the one least safe to rely on. It reads s 15(1), (2),
(3) and (6), and it **does not** read s 16 (to which (2) and (3) are both
subject), s 15(4) (the Board's discretion to allow more), s 15AA, or any of the
charges that can be registered against an account. A real answer needs all of
those. The function is correct for the subsections it covers and silent about
the rest, which is not the same as being right.

## What would need doing before this is worth anything

- The regulations fixing the retirement sum.
- s 15AA, s 15(4), and the charge provisions.
- No case law was searched.


---

# Added with sections 7, 16 and 25

## s 16 corrects the first pass, and the first pass was too generous

The earlier note said that `the amount this member may withdraw` was "the
function someone would want to call and the one least safe to rely on", because
it did not read s 16. It now does, and the difference is large.

**s 16 ring-fences the medisave account.** A member may not withdraw it under
s 15(2)(a) (reaching 55) or s 15(3) (the annual further withdrawal); the Board
must not allow it under s 15(4); and under s 15AA(1) only with the Minister's
approval.

So for a 55-year-old citizen with **$200,000** in the Fund, of which **$60,000**
is medisave, and a **$100,000** retirement sum:

| | |
|---|---|
| first pass, s 15 alone | $200,000 − $100,000 = **$100,000** |
| with s 16 | ($200,000 − $60,000) − $100,000 = **$40,000** |

Both rules are kept, and both are asserted, so the difference is visible rather
than silently corrected. The older one states what s 15 says on its own; the
newer one states what s 15 and s 16 say together.

A member whose medisave balance is large enough can reach **nothing at all**: on
$200,000 with $150,000 in medisave, the non-medisave credit is $50,000, which
will not cover the $100,000 retirement sum, so the withdrawable amount is zero
despite $200,000 in the Fund. Asserted.

## The asymmetry, sharpened

The earlier note recorded that the retirement-sum set-aside binds the member who
stays and not the one who goes. s 16 widens that gap, because **s 16(1) names
s 15(2)(a) and s 15(3) and does not name s 15(2)(b)**:

| | retirement sum set aside? | medisave reachable? | takes |
|---|---|---|---|
| citizen, 60 | yes | no | **$40,000** |
| non-citizen, 40 | no | **yes** | **$200,000** |

The member who remains a citizen or permanent resident loses both. The member
who ceases to be one loses neither. There is a coherent policy reading — the
retirement sum funds a retirement here and medisave pays for healthcare here —
but the difference is now a factor of five on identical balances, and it is
assembled from three provisions that never mention each other.

## Two more

**s 7(3) is narrower than a general failure-to-pay offence, and far heavier.**
It bites only where the employer **has already recovered** the employee's share
from their wages and then fails to pay it over. An employer who never deducted
anything and never paid anything is outside this subsection. The maximum is a
fine not exceeding $10,000 **or imprisonment for a term not exceeding seven
years** — the heaviest custodial maximum encountered anywhere in these seven
Acts, and it is for keeping money already taken from a worker's pay.

**A member who is not an applicable person may empty the Fund but may not say
who gets it.** s 25(1) allows a nomination only by "a member of the Fund (**being
an applicable person**) who is at least 16 years of age". So the same person who
may withdraw everything under s 15(2)(b) may not make a nomination at all.
Asserted as that pair.

Also encoded: s 25(1)(a)(ii)(B) splits a large nomination to a citizen or
permanent resident — the Minister's maximum is transferred into the nominee's
own CPF accounts and the excess is paid out to them in cash.

## Contribution rates and death (added 11 October 2026 for REQ-0001 and REQ-0012)

A third module, `cpf-rates-and-death.l4`, answers two requirements raised by the
`cradle-to-grave-simone` scenario.

### REQ-0001: the shares for an employee aged 23 on $4,200 in August 2026

First Schedule paragraph 1, in force from 1 January 2026. For wages over $750 the employer
pays a total of **37%** of ordinary wages, up to the Ordinary Wage Ceiling, and may recover
**20%** from the employee. The ceiling is $8,000 a month from 2026 (para 7(ea)). So $4,200
gives **$1,554** in total: **$840** deducted from the employee and **$714** borne by the
employer, exactly as the entry expected. Asserted.

The other bands are 34/18 (above 55 to 60), 25/12.5 (above 60 to 65), 16.5/7.5 (above 65 to
70) and 12.5/5 (above 70). Wages of $500 to $750 phase in the employee share. The total is
rounded to the nearest dollar with 50 cents rounding up, and the employee share drops any
fraction (para 7(b), (c)). An older band starts the month **after** the birthday month
(para 7(a)). The tables are column-shifted in the `.txt` deposit; the rates were read cell
by cell.

Not encoded: additional wages, the graduated rates for new permanent residents, foreign
and public-sector employees, and the allocation into the three accounts (REQ-0002, which
needs subsidiary legislation).

### REQ-0012: CPF moneys on death are outside the estate by statute

The entry asked this as a case-law question. The Act answers it. s 24(3A): moneys paid out
on a member's death "are deemed to be impressed with a trust in favour of" the nominee
(or, with no nomination, those entitled through the Public Trustee under s 25A), and "are
deemed not to form part of the deceased member's estate or to be subject to his or her
debts". A will leaving everything to the spouse does not reach them.

One trap is s 25(5)(a): a nomination is **revoked by the member's marriage**. A nomination
made before marrying does not survive the wedding, and the moneys then go through the
Public Trustee route. Asserted.

## Allocation and the Exemption Order (added 11 October 2026 for REQ-0002 and REQ-0003)

### Allocation into the accounts is a ministerial direction, published by the Board

Section 13(4) requires the Board to credit each contribution to the member's accounts "in such manner as the
Minister may direct". The direction is not subsidiary legislation. The ratios in `cpf-allocation.l4` therefore
come from the CPF Board's one-page **"CPF Allocation Rates from 1 January 2026"**, supplied by hand. Because
it is not legislation, it is not deposited.

The Board's method:
- Medisave is computed first, then the special account (the retirement account above 55).
- The ordinary account gets the remainder.

The examples are in cents, but the page does not say how a fraction of a cent is rounded. The encoding rounds
each of the first two credits to the nearest cent; that is the encoder's reading. Both of the page's examples
are asserted.

**REQ-0002:** $1,554 at age 23 gives medisave **$335.97**, special **$251.90** and ordinary **$966.13**.
The ledger expected 336 / 252 / 966, which is the same split rounded to whole dollars.

Not modelled: the footnote on members aged 55 and above after the special account closes. Their contributions
go to the retirement account only up to the Full Retirement Sum, and to the ordinary account after that.

### The Exemption Order: an approved internship is exempt, but this is the 2018 text

`cpf-exemption.l4` encodes the **Central Provident Fund (Exemption) Order 2018** (S 61/2018), made under s 69.
The text is deposited at `../../registers/source-bundle/CPFA1953-S61-2018.txt`. **The PDF supplied is the
version as made, in force from 1 January to 1 February 2018; later amendments have not been checked.**

What it exempts:
- Para 3: no contributions for an employee who is neither a citizen nor a PR.
- Para 2 and the Schedule: no contributions for specified employees. These include:
  - domestic workers on 14 hours a week or less;
  - UN staff;
  - certain seamen;
  - SHATEC trainees;
  - students (paras 5 to 8).

The students covered:
- Para 5: a student of a university "whose function of providing university education is determined by
  any written law", of ITE, of a polytechnic, or of certain schools, "employed for training approved by the
  institution concerned".
- Para 6: private-institution students on MOE-subsidised full-time programmes.
- Para 7: overseas students required to train here for 6 months or less, who give the employer written
  confirmation.
- Para 8: school pupils on holiday jobs, but not once they have done A levels.

**REQ-0003:** an NUS student whose internship is part of the course is exempt under para 5(a). No
contributions are payable on the $1,200. The test is whether the *institution approved the training*,
not whether she is full-time. An internship the university has not approved is not exempt. Both are asserted.

## Self-employed Medisave (added 11 October 2026 for REQ-0268)

`cpf-self-employed.l4` and `cpf-self-employed-cases.l4` (46 assertions). The question (Jun Hao scenario,
event j043) was: a self-employed delivery rider born 30 August 2006 declares $31,000 of trade income for a
year. What Medisave contribution must he make, and by when?

1. **The answer, as far as the Act gives one.** Under **s 9A(1)** he must pay contributions to the Fund on his
   "income". He must pay the amount "computed in the manner prescribed" (para (a)), "before the expiry of the
   prescribed period, or any longer period that the Board specifies" (para (b)), and "in the approved manner"
   (para (c)). Whether the $31,000 is "income" depends on **s 9A(3)**: it must be assessable income from a trade,
   business, profession or vocation, ascertained under s 37(1) of the Income Tax Act 1947, excluding employment
   under a contract of service and any income the regulations exclude. **The Act gives no figure and no date.**
   The rate, the income floor, any cap, the age bands (s 9A(2) allows them) and the payment period are all left to
   regulations under s 77(1). So is the meaning of "self-employed person" itself (s 2). The Act does not name
   those regulations, and none is deposited.
2. **Stand-in, not law.** The first assertion passes 8% of income over a $6,000 floor, capped at $7,680. This is
   the encoder's recollection of the CPF Board's figures for a member under 35 with income over $18,000, and it
   has **not been checked**. On those inputs he owes **$2,480** (8% of $31,000). The deadline assertions use a
   30-day stand-in period. The ledger expected "the Board's published self-employed Medisave rate"; that is
   right about where the figure lives, but the Act does not make it a *Medisave* rate (see 3).
3. **s 9A does not say "Medisave".** Contributions under s 9A are credited "in such manner as the Minister may
   direct" (**s 13(4)(b)**). The only place the Act sends self-employed contributions to the medisave account is
   **s 13A(1)(a)**: an authority licensing under an Act in the Third Schedule may make s 9A contributions, credited
   to the medisave account, a condition of the licence. The Road Traffic Act 1961 is item 34. That the money all
   goes to Medisave is the Minister's direction and the Board's practice, not the Act.
4. **A platform rider may be outside s 9A altogether.** By **s 8A(9)**, ss 9A and 9B "do not apply to any platform
   remuneration paid or payable to a platform worker on or after a date prescribed by regulations". The date is in
   regulations that are not deposited. A platform worker born on or after 1 January 1995 is a **Group A worker**
   (Fourth Schedule para 5(a)), and for him the platform operator pays under s 8A and the Fourth Schedule. Jun Hao
   (born 2006) is Group A if the $31,000 is platform remuneration. The Act does not say whether a platform worker
   is a "self-employed person": that term is defined only by regulation. What it does say is that platform
   remuneration paid after the date leaves s 9A. *Inference:* the carve-out goes by the kind of income, not the
   person, so any other trade income stays under s 9A. The REQ-0268 facts call him "self-employed" and his money
   "trade income", so the first assertions treat it as non-platform income. The platform reading is asserted
   alongside.
5. **Not paying.** Interest runs daily at the prescribed rate from the prescribed date (**s 9(2)**). The Board may
   waive it (**s 9(3)**), and the Minister may waive the contribution (**s 9C**). Failing to pay "within such period
   as may be prescribed" is an offence under **s 58(1)(e)**; s 5(7)(d) confirms that is the self-employed limb. The
   penalty is the general one in **s 61(1)**: a fine up to $5,000, imprisonment up to 6 months, or both. For a
   repeat offender it is $10,000 or 12 months. **There is no minimum fine**, because s 61(2)'s minimums attach only
   to ss 7(5), 8A(5) and 58(1)(b). On conviction the court may order the contributions and interest paid
   (**s 61B(1)**). The Board may sue for them as a Government debt (**s 65**), and it may compound the offence for up
   to $1,000 if the offence is prescribed as compoundable (**s 63**).
6. **Labelled inferences in the encoding.** (a) The amount is modelled as rate x income above a floor, capped.
   The real table may phase rates in between bands, and the model is right only inside a single-rate band.
   (b) Interest is modelled as simple daily interest. (c) The s 58(1)(e) period is taken to be the s 9A(1)(b)
   period as the Board extends it.
7. **Subsidiary legislation needed to answer REQ-0268 with a figure:** the regulations under s 77(1) for s 9A.
   They define "self-employed person" (s 2, s 77(1)(e)), determine the income and exclusions, fix the computation
   (rates by age and income band, floor, cap), the prescribed period, and the s 9(2) interest rate and start date.
   The regulations under s 77(1) also prescribe the s 8A(9) date. The Act names none of them. *Unverified
   recollection, to be confirmed against SSO:* the instrument is the Central Provident Fund (Self-Employed Persons)
   Regulations. The Minister's s 13(4) direction on crediting is also needed; it is not legislation.

## Self-employed contribution rates (added 12 October 2026 for REQ-0268)

`cpf-self-employed-rates.l4` and `cpf-self-employed-rates-cases.l4` (46 assertions: 11 on the question's facts,
35 more). The source is the Central Provident Fund (Self-Employed Persons) Regulations 1992 (Rg 25), informal
consolidation in force from 1 January 2026, deposited at `../../registers/source-bundle/CPFA1953-RG25.txt`. It
supplies the figures that s 9A leaves to regulations (see the section above). The question, raised again by the
Haziq scenario (event from the Jun Hao scenario, event j043, 2028), is the same: a self-employed delivery rider,
born 30 August 2006, declares $31,000 of trade income for a year. What Medisave contribution must he make, and
by when?

1. **The answer: $2,480, payable not later than 30 days after the date the CPF Board issues the contributions
   notice for that year.** The Board may specify a longer period, and he may pay in instalments if the whole is
   paid by then. The steps:
   - He is a "self-employed person" if he is a citizen or permanent resident (reg 2(1); *assumed*).
   - The Regulations apply because his income is "more than $6,000" (reg 3(1)).
   - None of the $31,000 is platform remuneration, so reg 2A excludes nothing.
   - His column in First Schedule item 23 is fixed by his age "on 1 January of the relevant year". He was born in
     2006, so he is 20 on 1 January 2027 and 21 on 1 January 2028 (s 2(1A)(a) of the Act). Either way he is in
     the "has not attained 35" column.
   - His income is in the band "Exceeding $18,000", where the rate is "8% of the income ... subject to a maximum
     of $7,680". 8% of 31,000 = 2,480.
   - Reg 14 drops fractions of a dollar; there are none. Reg 8A deducts any s 9B estimated contributions; none
     are assumed.
   - The time is in **reg 7A(2)**, and instalments are allowed by reg 7A(3).
   - The amount is computed on the income "stated in a notice of assessment" (reg 7A(4)), so the declaration
     does not itself fix the figure; the Board's notice does.
   - *Inference:* the relevant year is taken to be the year the income was earned (2027 if he files in 2028).
     The rate and column are the same for 2026, 2027 and 2028.
2. **The stand-in in `cpf-self-employed.l4` happened to give the right figure on these facts, but its shape is
   wrong below $18,000.** It took 8% of the income, capped at $7,680, with a $6,000 floor. Item 23 agrees above
   $18,000. Below that, the rate is 4% from $6,000 to $12,000, then "$480 and 0.16 of the difference" between the
   income and $12,000, phasing in to 8% at $18,000. On $15,000 the stand-in gives $1,200, while the Regulations
   give $960. Every age column joins up at $12,000 and $18,000, and every cap is the top rate on $96,000. That is
   a check that the column-by-column `.txt` table was read correctly. The stand-in module is left as it was,
   with a pointer to this one; the new cases use the new module.
3. **Neither the Act nor the Regulations call this a "Medisave" contribution.** Reg 4(1) says only that he must
   "pay contributions into the Fund on his or her own behalf". Rg 25 mentions the medisave account only in
   reg 9(4) and reg 10(4), which concern the reduction proportion for years before 2025 and for MPs, and in
   reg 17AB (voluntary contributions). Where reg 4 money is credited is still the Minister's direction under
   s 13(4)(b) of the Act. That direction is not legislation and is not deposited. So the question's word
   "Medisave" rests on that direction and Board practice, not on the text read here.
4. **The s 8A(9) date is 1 January 2025** (reg 2A(1)), inserted by S 888/2025 with effect from 1 January 2026.
   If his $31,000 were platform remuneration paid on or after 1 January 2025, s 9A would not reach it, and the
   Regulations' "income" would exclude it (reg 2A(2)). If he has both kinds of income, the contributions notice
   is computed on the notice-of-assessment income less his total APE (reg 7A(4A)). APE is defined in Fourth
   Schedule para 1 of the Act and is not encoded here. The ledger assumed non-platform income, and the first
   assertions follow it.
5. **The cap on everything (Third Schedule) is a separate thing from the First Schedule maximum.** For 2026
   onwards the figures are the same ($7,680 / $8,640 / $9,600 / $10,080), but they do different jobs:
   - The First Schedule maximum caps the reg 4 amount.
   - The Third Schedule cap is reached only on his written application under reg 9A, and only if he is also an
     employee or a platform worker with contributions made. It cuts his s 9A contributions so that "the
     aggregate amount of all contributions paid into the self-employed person's account" stays within the cap.
   - *Inference (labelled in the module):* which contributions count towards that aggregate is taken as an
     input. Reg 9A, unlike the old reg 9(3)(b), does not mention a medisave proportion.
   - On REQ-0268's facts (no employment, no platform work) reg 9A does not arise.
6. **What Rg 25 still does not supply:**
   - The s 9(2) interest rate and start date: Rg 25 contains no interest provision, so they are in another
     instrument, not identified.
   - The Minister's s 13(4) crediting direction.
   - Whether s 58(1)(e) is a compoundable offence: the Board's rules under s 63(2).
   - The date the Board will issue the contributions notice: an administrative act, so the encoding counts days
     from it.
   - *Inference (labelled):* reg 7A(2)(b)'s "extended period" is taken to end more than 30 days after issue.
7. **Version.** Read from the consolidation in force from 1 January 2026, current on SSO as at 13 October 2026.
   An amendment taking effect before the 2027 or 2028 relevant year would not be in the deposit.

## The current Exemption Order (added 12 October 2026 for REQ-0265)

`cpf-exemption-current.l4` encodes the **Central Provident Fund (Exemption) Order 2018 as it stands today**:
2025 Revised Edition, informal consolidation in force from 1 June 2026, deposited at
`../../registers/source-bundle/CPFA1953-OR10.txt`. Paras 2, 3, 3A, 4 and 5 and the Schedule are encoded.
`cpf-exemption.l4` (the version as made) is left as it was, with a one-line pointer to the new module.
Cases: `cpf-exemption-current-cases.l4`, 46 assertions.

1. **A university student on training approved by the university is still exempt today.** A citizen or PR
   who is a matriculated or registered student of a university "whose function of providing university
   education is determined by any written law", "employed for training approved by the institution
   concerned", is now specified in **Schedule para 6(a)** (para 5(a) as made). Para 2(2) exempts the employer
   from s 7 contributions and from community-fund contributions under s 76(3). The REQ-0003 answer stands
   on the current text. Asserted, together with the same facts under the as-made module.
2. **Yes, the Order has been amended.** The deposit's Legislative History lists S 73/2018 (from 1 March 2018),
   S 716/2024 (two commencements, 31 December 2021 and 1 October 2024), S 1031/2024 (from 1 January 2025),
   the 2025 Revised Edition (17 December 2025), S 895/2025 (from 31 December 2025) and S 325/2026 (from
   1 June 2026).
3. **The student paragraphs did not change in substance; they moved.** As-made paras 5 to 8 are now paras
   6 to 9, with the same words apart from updated Act citations, "student of" for "student in" in para 7(a),
   and the MOE web address. Para 2(1) and (2) now point at para 6(a). The new module reuses the as-made
   module's `Student` and `Institution` types, and four assertions check that both versions give the same
   result on the same student.
4. **The ledger's expected answer is partly wrong.** It said "the current version's Schedule paras 5 to 8
   and para 3 are as encoded". The students are now paras **6 to 9**; Schedule para 5 is "[Deleted by
   S 325/2026]". Schedule para 3 is now OECD staff at the IEA Regional Cooperation Centre, not the seamen.
   If "para 3" meant Order para 3 (foreign employees), that is unchanged word for word.
5. **Who else is exempt has changed.**
   - Domestic employees on 14 hours or less (as-made Schedule para 1) are now covered only by **Order
     para 4**. That is a transitional exemption for citizens and PRs whose contract, or a "prior connected
     contract", was made and begun before 1 June 2026, for months after 31 May 2026. Para 4(2)(c) imposes an
     hours test for the period up to 31 May 2026.
   - A new domestic contract made after 1 June 2026 is no longer exempt, even at 14 hours or less. Asserted
     against the as-made module, which exempted it.
   - Seamen on Swedish, Norwegian or East Asiatic Co terms are now covered only by **Order para 5**, also
     transitional: citizens on contracts made and begun before 1 June 2026, for periods after 31 May 2026.
   - New: **para 3A** exempts platform operators from s 8A contributions for foreign platform workers. New
     **Schedule para 2A** covers ICSID and MIGA employees in Singapore, and Schedule para 2 now reaches UN
     "related organisations". Schedule para 3 (OECD/IEA) is new as against the as-made text.
   - The as-made Schedule paras 4 (Seventh-Day Adventists) and 9 (SHATEC trainees) are not in the current
     text. **When** they left, and what current Schedule paras 4 and 5 said just before S 325/2026 deleted
     them, cannot be read from the deposit. The amending orders were not retrieved.
6. **May 2025 is not answered.** The version in force in May 2025 (after S 1031/2024, before the 2025
   Revised Edition) was not obtainable and is not deposited. The student words are identical in the 2018 and
   2026 texts, so *by inference only* they are likely to have read the same in May 2025. That rests on no
   text, and an amendment made and later reversed in between cannot be ruled out without S 73/2018,
   S 716/2024 and S 1031/2024.
7. **A fork in para 4(2)(c)(ii)(B).** "In every period of 7 consecutive days falling within **any one**
   calendar month" may mean some one month or each month. The encoding takes it as an input stated in the
   Order's own words and does not choose. Para 4(2)(c) is also taken on the facts of one qualifying contract.
8. **Still inputs:** whether an institution is within para 6, whether training is "approved by the
   institution", whether a person is a "domestic employee" (para 4(4)), a seaman, a platform worker or a
   student of a "private education institution" (Private Education Act 2009 s 2), and MOE's listed
   programmes and school holiday periods (on the MOE website).

## Still a small fraction of the Act

911,000 characters, of which this encodes s 7, s 15(1)–(6), s 16 and s 25(1).
Since 11 October 2026 the First Schedule rates and s 13(4) allocation are encoded (see above). Not encoded: s 15AA, s 15(4), the housing and investment charges, the rest
of s 25, and everything from Part 3A onwards.

**A caution carried over from the Work Injury Compensation Act.** The First
Schedule contribution rates are a long table that crosses page breaks, and in
that Act every such table in the deposited text was shifted by one row against
its key. The CPF rates were *not* encoded partly for that reason: they should be
recovered from the PDF and checked before anyone relies on them.
