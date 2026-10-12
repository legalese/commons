# Singapore Corporation of Rehabilitative Enterprises Act 1975 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
17/6/2024"), deposited at `../../registers/source-bundle/SCREA1975.txt`. The revised
edition incorporates amendments to 1 December 2021; the latest amendment annotated is
Act 16 of 2024 (Law Enforcement and Other Matters Act 2024), on ss 17A and 36, with
commencement 17 June 2024 in the legislative history.

**Checks:** one module (`screa-corporation.l4`), one case file
(`screa-cases-corporation.l4`), 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0208** in `subjects/sg/requirements.jsonl`: tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

Most of the Act constitutes and funds a statutory body. This row takes what a
prisoner, an inmate, a discharged offender, an employee or an outside business meets:
who counts as a prisoner or inmate (s 2), which of the Corporation's functions and
powers reach whom (ss 15(c), (e), (g), 16(c), (g), (h), (k)), the symbol offence
(s 17A), delegation (s 17), the size of the Corporation and the quorum (ss 4(1),
6(2)), execution under seal (s 35(2)), remuneration and personal immunity (ss 21, 22),
the financial year (s 24) and the Government's share of a transferred employee's
pension (s 14(2)). Not encoded: establishment and business names (s 3), tenure and
pay of members (ss 4(2)-(5), 5), the rest of the meeting rules (s 6), ss 8, 9, the
1976 transfers (ss 10-13, 14(1)), the other s 16 powers, staff and pension schemes
(ss 18-20), finance (ss 25-29), s 35(1), (3), (4) and regulations (s 36). No
regulations under s 36 and no order prescribing an institution for "inmate" were
retrieved.

## What the Act turns out to say

### 1. Nothing in the Act is an entitlement for a prisoner

Training, work, pay, aftercare, and grants or loans to discharged offenders are all
framed as functions (s 15) or as things the Corporation "may" do (s 16). A prisoner
working for the Corporation may be paid "such salaries, wages, remuneration or
allowances as the Corporation thinks fit" (s 16(c)); the Act sets no minimum and gives
no right to claim. The encoding answers "may the Corporation", never "must it".
Asserted (as powers).

### 2. Using the Corporation's symbol is a crime, with no mental element stated

Since 17 June 2024 (Act 16 of 2024), anyone who uses a symbol identical to the
Corporation's, or one so similar as to deceive or confuse "or to be likely to", without
its **prior written** permission, commits an offence: up to $10,000 or 6 months or
both, plus up to $250 for every day or part of a day the offence continues after
conviction (s 17A(2)). The section says nothing about knowledge or intent. A business
with a lookalike logo is exposed. Asserted (offence, $10,000 maximum, $2,500 for 10
further days).

### 3. A drug inmate is not a "prisoner", so s 15(e) work is for prisoners only

s 2 separates "prisoner" (anyone, convicted or not, detained in a prison or
reformative training centre) from "inmate" (detained in an approved institution under
the Misuse of Drugs Act 1973 or a prescribed place). Most functions name "prisoners
and inmates", but s 15(e), providing work "for the purposes of section 67 of the
Prisons Act 1933", names "any prisoner" only. A remand prisoner awaiting trial is a
prisoner; a person in an unprescribed police lock-up is neither. Asserted.

### 4. Prisoners and inmates are carved out of staff loans and staff welfare

The Corporation may lend to its employees, including for housing (s 16(g)), and
promote welfare and recreation for present and past employees (s 16(h)), but both
expressly exclude "prisoners and inmates". An inmate on the Corporation's payroll can
be paid (s 16(c)) but cannot get a staff loan. Once discharged, the same person can
receive a grant, loan or guarantee, but only "for the purposes of any vocation, trade
or business carrying on by them" (s 16(k)). Asserted.

### 5. Borrowing is never delegable; lending and underwriting cannot go to an employee

s 17(2) lets the Corporation delegate anything except borrowing to a committee, the
Chairperson, a member or the chief executive officer; s 17(4) lets it delegate to an
employee anything except borrowing, raising or granting loans or advances, and
underwriting securities of industrial enterprises. The encoding reads the s 17(4)
exception as covering loans and advances generally; the phrase could be read as
confined to industrial enterprises throughout. Asserted on the encoding's reading.

### 6. The quorum floor is 3, and one-third is not rounded down

s 6(2): one-third of the members or 3, whichever is higher. With 4(1) allowing 5 to 15
members, the floor of 3 governs up to 9 members; with 16 (possible only with a
temporary member, which is not modelled) 5 present would fall short. Asserted.

### 7. The seal needs a member and a countersignature

s 35(2): a sealed instrument "must be signed by a member and must be countersigned by
the chief executive officer or by some other person duly authorised". The chief
executive officer is not among the members listed in s 4(1), so the CEO cannot be the
first signatory (an observation from that list). Asserted.

### 8. Personal immunity needs good faith and the Act's purposes

s 22 shields members, employees and persons acting under the Corporation's direction
from personal liability for things done in good faith for carrying out the Act. It
does not say the Corporation itself is immune. An independent contractor not under its
direction is outside it (the encoding's reading of "acting under its direction").
Asserted.

### 9. s 14(2) is circularly worded

The Government's share of a transferred employee's pension is expressed as the portion
"as the same bears to the proportion which" Government emoluments bear to total
emoluments. The encoding reads it as benefit times Government emoluments over total,
and notes the payment runs from Government to Corporation, not to the employee.
Asserted on that reading.

### 10. The arrangement of sections is column-shifted in Part 4

In the deposit's arrangement, "Functions of Corporation" and "Powers" carry no number,
"15." sits against "Appointment of committees" and "16." against "Corporation's
symbol", while "17." and "17A." have no title. The encoding follows the body (s 15
Functions, s 16 Powers, s 17 committees, s 17A symbol). Not asserted.

## What would need doing before this is worth anything

- Regulations under s 36 (amended by Act 16 of 2024), and any order prescribing an
  institution for "inmate", were not retrieved.
- The Law Enforcement and Other Matters Act 2024 was not read; the 17 June 2024 date is
  from the legislative history and the annotations.
- The Corporation's symbols themselves (s 17A(1)) were not retrieved.
- No case law was searched.
- Findings 5, 8 and 9 rest on the encoder's readings and need a lawyer's view.
