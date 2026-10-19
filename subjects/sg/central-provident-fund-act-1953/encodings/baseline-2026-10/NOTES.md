# Central Provident Fund Act 1953 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the
`writing-l4-rules` skill, from the seat of the individual to whom the law is
applied, with the design defaults ruled on 2026-10-18. No `REFUSE`: where the
encoding cannot answer it says so with an explicit value (`NOTHING` for a
contribution it has no text for, or a constructor named `not covered by this
encoding: ...`). No pipeline, no coverage table, no independent test pass, no
human gate. It is not for public use as advice.

This encoding replaces the encoding moved to solutions on 19 October 2026 and the
first-pass encoding `naive-2026-10`. It covers what the first pass covered: s 15
with s 16, s 7, s 25(1), the First Schedule rates from 2026, s 24(3A) and
s 25(5), the s 13(4) allocation, the Exemption Order (current text), s 9A and the
Self-Employed Persons Regulations. It adds s 24(2), s 24(3B), s 25(3), s 7(5),
s 7(6A), s 9(2) and (3), and the First Schedule paragraph 5(a) rule on when an
older band starts. The first pass's hand-checked figures for REQ-0001
($1,554 / $840 / $714), REQ-0002 ($335.97 / $966.13), REQ-0003 (the NUS intern),
REQ-0012, REQ-0265 (the domestic employee) and REQ-0268 ($2,480 within 30 days)
were re-derived from the text and reused. Three of its readings are corrected
(findings 5, 7 and 8 below). The as-made 2018 Exemption Order and the stand-in
self-employed rate are not carried over: the current Order and the Regulations
replace them.

**Edition:** the Act in the 2020 Revised Edition, informal consolidation, version
in force from 1 July 2026, as deposited at
`../../registers/source-bundle/CPFA1953.txt` (First Schedule paragraph 1 as
amended by S 886/2025, in force 1 January 2026). Brought in because they set the
Act's numbers and dates, and both deposited: the Central Provident Fund
(Exemption) Order 2018, 2025 Revised Edition, version in force from 1 June 2026
(`CPFA1953-OR10.txt`), and the Central Provident Fund (Self-Employed Persons)
Regulations 1992, version in force from 1 January 2026 (`CPFA1953-RG25.txt`).

**Checks:** with the stable `l4` of VS Code extension 1.6.98,
`l4 run cpf-cases-withdrawal.l4` (23 assertions),
`l4 run cpf-cases-contributions.l4` (22) and
`l4 run cpf-cases-self-employed.l4` (15): 60 assertions satisfied, 0 errors,
0 warnings. Each module also runs clean on its own.

| file | what it holds |
|---|---|
| `cpf-withdrawal.l4` | s 2 "applicable person", s 15(1), (2), (3), (6), s 16(1), s 24(2), (3A), (3B), s 25(1), (3), (5) |
| `cpf-contributions.l4` | s 7(1) to (6A), First Schedule paras 1 and 5, s 13(4), Exemption Order paras 2 to 5 and the Schedule |
| `cpf-self-employed.l4` | s 9A, s 8A(9), s 9(2) and (3), s 58(1)(e), s 61(1), and the Self-Employed Persons Regulations |
| `cpf-cases-*.l4` | generated fixtures, hand-written expected values |

## Seat

**The member of the Fund**: the employee or self-employed person whose money it
is. The Act speaks mostly to the Board, employers and the Minister, but what it
decides lands on the member: what goes in each month, what an employer may take
from my pay, when I can take money out and how much, whether creditors can reach
it, and who gets it when I die. Every decision is named as the member would ask
it (`How much may I withdraw, once the Board authorises it`,
`What is the most my employer may deduct from my wages for CPF this month`,
`How much must I contribute for the year`, `Where does my CPF money go when I die`),
and every input is a fact the member could state. In the contributions module the
member is the employee. In the self-employed module the member is the
self-employed person. Duties of the employer (s 7(3), (5)) are asked as what the
employer may not do to me.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.**
  Followed. The First Schedule is part of the Act. The Exemption Order and the
  Self-Employed Persons Regulations are brought in because they are deposited.
  The instruments that are not deposited are inputs, and the module says so where
  each is used: the prescribed retirement sum, the reserved amount, the classes
  prescribed as applicable persons, the Minister's maximum for a nominee's
  transfer, and the Minister's s 13(4) allocation ratios (published by the Board,
  not subsidiary legislation).
- **The actors the text names.** Followed: the Board, the Minister, the employer,
  the Public Trustee, the Official Assignee, the nominee.
- **A judgment handed to someone else, answered conditionally.** Followed. The
  Board's authority under s 15(1) is an input, so the withdrawal figure is "once
  the Board authorises it", and `May money be paid out to me now` asks for that
  authority. The Board's extended period (reg 7A(2)(b)), its waiver of interest
  (s 9(3)) and its prescribed conditions (s 7(6A)) are inputs.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts.** Followed for "applicable person" (s 2), the age bands (s 2(1A)(a) and
  First Schedule para 5(a)), the Ordinary Wage Ceiling, "income" under reg 2A and
  the reg 3 threshold. "Assessable income" (Income Tax Act 1947), "domestic
  employee", "prior connected contract" and whether an institution is on the
  Schedule's list are asked as facts.
- **One case is the text's natural unit.** One member's account; one month of
  wages from one employment; one relevant year of self-employed income; one
  nominee.
- **The Act's own terms, each with a plain gloss.** Followed: "applicable
  person", "reserved amount", "retirement sum", "Ordinary Wage Ceiling",
  "second anniversary month", "relevant year" and "estimated contributions" are
  used as the text uses them and glossed in comments.
- **The operative sections in scope; the machinery out.** Followed in kind but
  not in full: the Act is about 911,000 characters, so the scope is the
  provisions a member meets most (see below). The Board, its officers,
  regulation-making and commencement are out.

## Why this scope

A member asks: what goes in from my job, what can my employer take from my pay,
when is no contribution due, what must I pay if I work for myself, when can I
take money out and how much, can my creditors reach it, and where does it go when
I die. Those are ss 7, 9A and 13(4) with the First Schedule, the Exemption Order
and the Regulations; ss 15 and 16; s 24; and s 25. Left out: additional wages,
the permanent-resident graduated rates (paras 1A to 1D), public-sector employees,
platform workers (s 8A and the Fourth Schedule), s 15(4), s 15AA and the
Retirement Sum Scheme, the housing and investment charges and schemes,
s 25(1)(a)(iii), s 25A beyond naming it, and everything from Part 3A onwards.

## What the Act turns out to say

1. **There are two routes out of the Fund, and leaving the country is the
   generous one.** s 15(2) keeps only (a) attaining 55 and (b) not being an
   applicable person; (c) to (g) are deleted. s 16(1) ring-fences medisave
   against (2)(a) and (3) only, and s 15(6) sets the retirement sum aside on
   (2)(a), (3) and (4) only. Neither names (2)(b). On $200,000 with $60,000 in
   medisave and a $100,000 retirement sum, a citizen aged 60 may take $40,000 and
   a foreigner aged 40 may take $200,000. Asserted.

2. **The member who can empty the Fund cannot nominate.** s 25(1) allows a
   nomination only by a member "(being an applicable person) who is at least 16
   years of age". The foreigner who takes everything under s 15(2)(b) may not
   say who receives it on death. Asserted, with a citizen of 16 (may) and 15
   (may not).

3. **The further withdrawal attaches to the 55 ground by name.** s 15(3) reaches
   a member who withdrew "on the ground that he or she has attained 55 years of
   age". Asserted both ways.

4. **The set-aside reads two ways.** s 15(6)(a)(ii) takes the retirement sum
   "from the sum standing to the member's credit in the Fund, after excluding any
   reserved amount". It does not exclude medisave. The encoding keeps back
   medisave, the reserved amount and the retirement sum, each in full. That is
   the first pass's reading, and it is labelled in the module. The other reading
   would let a medisave balance count towards the retirement sum. The
   regulations the set-aside is made under are not deposited. Asserted on the
   encoding's reading only ($20,000 with a $20,000 reserved amount; nothing where
   medisave is $150,000).

5. **The nominee's manner of receipt is the member's choice. The first pass
   assumed otherwise.** s 25(1)(a) gives the portion "as the memorandum
   indicates", by payment (i) or, for a citizen or permanent resident nominee, by
   transfer to their CPF accounts (ii). The first pass transferred automatically
   to any citizen or permanent resident nominee. Here a $300,000 transfer with a
   $200,000 Ministerial maximum puts $200,000 into the nominee's accounts, and the
   same portion by payment transfers nothing. s 25(3) sends a payment to a
   nominee under 18 to the Public Trustee, unless the nominee is the member's
   widow. Asserted.

6. **CPF paid on death is outside the estate, but not all of it.** s 24(3A)
   impresses the moneys with a trust for the nominees, or for those entitled
   through the Public Trustee, and deems them outside the estate and free of the
   member's debts. A nomination is revoked by marriage (s 25(5)(a)). s 24(3B)
   takes money payable to a spouse or former spouse under s 27B out of s 24(3A).
   s 27B is not encoded, so that case answers `not covered by this encoding`.
   Asserted. s 24(2) separately keeps the money from creditors and the Official
   Assignee, subject to a list of sections stated as one input.

7. **The age, rounding and ceiling rules are in First Schedule paragraph 5, not
   paragraph 7. Paragraph 5(a) also moves the band after a 55th birthday.**
   The first pass cited "paragraph 7(a), (b), (c), (ea)". Paragraph 7 in the
   deposit is about public-sector employees. The rules are in paragraph 5. Under
   paragraph 5(a), contributions for an employee "above 55" are payable "from the
   first day of the month following the month in which the employee attains that
   age". Reading "that age" as 55 itself, an employee whose 55th birthday was in
   an earlier month pays at 34% ($1,360 on $4,000), although band (a) is headed
   "55 years of age and below". In the birthday month they pay 37% ($1,480). The
   first pass put every 55-year-old at 37%. Asserted. The reading is labelled.

8. **The 2026 rates do not reach 2025.** Paragraph 1 runs "with effect from
   1 January 2026". The deposit gives the 2025 Ordinary Wage Ceiling ($7,400) but
   not the rates then in force. The first pass applied 2026 rates to 2025 and got
   $2,738 on $9,000. This encoding answers `NOTHING`. Asserted. In 2026 the
   ceiling caps $9,000 at $8,000: $2,960.

9. **REQ-0001 stands: $1,554, of which $840 comes from the pay of a 23-year-old
   on $4,200.** That is 37% and 20% of ordinary wages, the employer bearing $714.
   The low-wage phase-in gives $162 on $600. Half-dollars round up: $499.50
   becomes $500 (para 5(b)). Asserted.

10. **The seven-year maximum is for keeping money already taken from my pay.**
    s 7(3) bites only where the employer "has recovered" my share and fails to pay
    it in. The fine is up to $10,000 or imprisonment up to 7 years. s 7(5) makes
    taking more than the First Schedule share plus my voluntary contribution an
    offence. s 7(6A) lets a missed deduction be caught up only after an error "not
    occasioned by that employer's negligence", and only within 6 months.
    Asserted.

11. **The exemptions now turn on the date of the contract.** Under the current
    Order an NUS intern on training the university approved is exempt (Schedule
    para 6(a)). Without that approval, $444 is due on $1,200. A foreign employee's
    employer is exempt (para 3). A part-time domestic employee keeps the exemption
    only on a contract, or prior connected contract, from before 1 June 2026
    (para 4). A new contract is not exempt, however few the hours. Asserted. The
    "any one calendar month" fork in para 4(2)(c)(ii)(B) is left to the caller.

12. **The self-employed rider owes $2,480, within 30 days of the Board's notice.**
    Born 30 August 2006, he is 20 on 1 January 2027, so he is in the under-35
    column. Item 23 charges 8% of the whole income above $18,000 (capped at
    $7,680). Reg 7A(2) gives 30 days from the notice's issue, or the Board's
    longer period. Income of exactly $6,000 is not "more than $6,000", so nothing
    is due. Platform remuneration paid from 1 January 2025 is not income (reg 2A).
    Section 9B estimated contributions are deducted (reg 8A). The middle band
    phases in: $960 on $15,000. Asserted.

13. **Neither the Act nor the Regulations call this a Medisave contribution, and
    the allocation is not law.** Where any contribution is credited is "in such
    manner as the Minister may direct" (s 13(4)). The direction is not subsidiary
    legislation and is not deposited, so the ratios are inputs. With the Board's
    published ratios for age 23 stated (0.2162, 0.1621), $1,554 credits $335.97 to
    medisave and $966.13 to the ordinary account. Rounding each credit to the
    nearest cent is the encoder's inference. Asserted.

14. **Not paying is an offence with no minimum fine.** s 58(1)(e) with
    s 61(1): up to $5,000 or 6 months, $10,000 or 12 months for a repeat offender.
    s 61(2)'s minimums attach only to ss 7(5), 8A(5) and 58(1)(b). Interest runs
    daily under s 9(2) unless the Board waives it (s 9(3)). The rate is in no
    deposited instrument. Asserted.

## What would need doing before this is worth anything

- The regulations fixing the retirement sum, the reserved amount and the classes
  of applicable person, and with them the set-aside reading in finding 4.
- s 15(4), s 15AA and the Retirement Sum Scheme; the property charges that create
  reserved amounts; s 25A and s 27B.
- First Schedule paragraphs 1A to 1D, additional wages and the Relevant Additional
  Wages, public-sector employees, and platform workers under s 8A and the Fourth
  Schedule.
- The paragraph 5(a) reading in finding 7, checked against the PDF and Board
  practice. The rate tables cross page breaks and are column-shifted in the
  `.txt` deposit; they were read cell by cell, not checked against the PDF.
- The s 9(2) interest instrument, and the Minister's s 13(4) direction.
- No case law was searched, and no human gate has been sought.
