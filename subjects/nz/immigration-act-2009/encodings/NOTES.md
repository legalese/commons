# NOTES: the Immigration Act 2009 (New Zealand), eligibility, unlawful status, work and deportation, row `legalese-aswathy`

**Draft. No New Zealand lawyer has reviewed this encoding against the Act.**

## What is encoded

The computable rules of the Immigration Act 2009 (version as at 10 July 2026, from the text converted from the PCO XML) on eligibility for a visa, unlawful status and work, the deportation liability of residence class visa holders for offending, and the employer offence. They sit under one top-level goal, `the immigration position for` (`imm-goal.l4`). For a non-citizen on a day, it answers whether they are barred from a visa, whether they are unlawfully in New Zealand and so barred from working, since when, the last day for a humanitarian appeal, and whether they are liable for deportation under s 161. Four goals sit under it:

1. **Eligibility** (`imm-status.l4`): ss 15-17.
2. **Unlawful status and work** (`imm-status.l4`): ss 9, 21, 154, 185.
3. **Deportation liability** (`imm-deportation.l4`): ss 157, 161, 167.
4. **Employers** (`imm-employers.l4`): s 350.

Modules: `imm-types.l4` (nouns only), `imm-status.l4`, `imm-deportation.l4`, `imm-employers.l4`, `imm-goal.l4`; tests in `imm-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** Visa criteria (in immigration instructions, not the Act), the visa classes and conditions (ss 43-91), refugee and protection status (Part 5), the other deportation grounds (ss 155-160, 162-163), deportation orders and the s 179 prohibition periods (the table is lost in the conversion), appeals to the Tribunal beyond their deadlines, detention, offences other than s 350, and the rest of the Act.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 9 | unlawfully in New Zealand | encoded: (1), (2)(a)-(b); (2)(c)-(d) not |
| s 15 | convicted or deported persons ineligible | encoded (the s 15(2) sentence rules are applied by the caller; s 15(3) exceptions an input) |
| s 16 | Minister's belief | an input |
| s 17 | exceptions | encoded: (1) |
| s 21 | no right to work | encoded: (a) |
| s 154 | liability if unlawful; 42-day appeal | encoded: (1), (2), (4); (5) not |
| s 157 | temporary visa holders | encoded: the 14 and 28 days; the Minister's determination is an input |
| s 161 | residence class visa holders convicted | encoded: (1)-(3); (4) by the caller; (5)-(7) first holding is an input |
| s 167 | period of liability | encoded |
| s 185 | reconsideration | encoded: (2) |
| s 350 | offences by employers | encoded |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 15(1)(b), 350(3) | Is the anniversary inside "the preceding 10 years" / "the preceding 12 months"? | Yes | A period counted back from the day includes the day a whole period before; the independent author agreed |
| F2 | ss 161(3), 167(2) | How does excluded time affect a period? | It extends the period by the number of days excluded | The period is "determined exclusive of" that time |
| F3 | ss 161(1), 167(1) | "Not later than N years after" | Up to and including the anniversary (as extended) | Ordinary reading |
| F4 | s 161(1)(a) | "Imprisonment for a term of 3 months or more" | A maximum of 0.25 years or more | Inputs are in years |
| F5 | s 9(2)(b) | Unlawful status of a person once lawful, with no expiry date given | Refused | s 9(2) needs the date |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `imm-tests.l4` (encoder) | 0 | 46 | 0 |
| `tests-independent.l4` | 0 | 93 | 0 |
| the 5 rule modules | 0 | 0 | 0 |
| **total** | 0 | 139 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) failed no assertion. Its noted differences are recorded as known limits below.

**Known limits.** The days imprisoned under s 161(3) are one input for all windows: the caller must give the days within the relevant window. The top-level appeal deadline assumes no s 185 reconsideration and no s 154(5) exclusion. The s 350 subsection numbers (deemed knowledge as (3), the notice-period defence as (4)) need checking against the PCO's numbering, since the converted text lost paragraph labels. Legislation Act 2019 s 55 (a time limit ending on a non-working day runs to the next working day) is not applied to the 14-, 28- and 42-day periods.

## Open questions for a New Zealand lawyer

1. F1: is the anniversary inside "the preceding 10 years" in s 15(1)(b)?
2. Does s 55 of the Legislation Act extend the s 154 and s 161 appeal periods when they end on a weekend?
