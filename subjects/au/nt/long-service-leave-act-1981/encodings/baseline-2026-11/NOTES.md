# Long Service Leave Act 1981 (NT) — baseline encoding, the employee's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18, the rulings on negatives of 2026-11-04 and 2026-11-05 (copied below), and the `writing-l4-rules` skill (with `references/regulative.md`).
There is no REFUSE in it; where the text does not answer, a question answers `NOTHING` with a `NOTHING-kind` tag in the source, and the tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the Acts behind personal injury, compensation and other claims work, here under employment: the Act is one of the state and territory long service leave Acts that the Commonwealth Fair Work Act leaves in place. The Act is short (about 20 sections), so **the whole operative Act** is encoded; only machinery and transitional provisions are left out (listed below). There was no earlier encoding of this Act to keep, and no ledger entry was open for it (the Northern Territory has no requirement ledger yet).

Three modules:

- `ntlsl-dates.l4` — the date arithmetic (built-in date functions only; no `daydate` import).
- `ntlsl-employee.l4` — the rules and the 26 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order: does the Act apply (ss 6, 7, 8(4), (5), 13); continuous service (s 12); the entitlement (s 8, with ss 6(4), 7(6), 9); taking the leave (s 8(6), (7), s 16); when the employment ends or the employee dies (s 10 — arises only when the employment ends); how much (ss 7(2), (4), 11); when I must be paid (s 11(6)–(8)); records, offences and enforcement (ss 14, 17, 18, 18A).
- `ntlsl-cases.l4` — 152 assertions and 3 traces.

**Regulative rules.** `s 11(6) -- pay the whole of the leave before it starts`: `PARTY my employer MUST pay my long service leave the amount PROVIDED the amount AT LEAST the amount owed WITHIN the days allowed HENCE FULFILLED LEST BREACH BY my employer BECAUSE ...`, with day 0 the day the leave was fixed and the deadline the agreed due day (the last working day before the leave, the pay day before it, or another agreed time, s 11(8)(b)). `s 11(7)(b) -- pay the estate within 12 months of the death`: the same shape, owed to the personal representative, with day 0 the death and the deadline the same day 12 months on. A part payment does not count. Both run inside exported questions (`Was my leave pay paid on time`, `Was my estate paid on time`) through `CONSIDER EVALTRACE ... WHEN FULFILLED`; the questions take only dates and amounts. One fulfilment and two breaches are `#TRACE`d with `-- expect:` lines.

## Edition

Reprint **REPL021**, as in force at 14 October 2015 (last amended by the Statute Law Amendment (Directors' Liability) Act 2015), from the Northern Territory Legislation register (retrieved 6 November 2026, shown as in force and current), as deposited at `../../registers/source-bundle/Long-Service-Leave-Act-1981-NT-current-reprint-REPL021.txt`. The endnotes record formal general amendments to ss 1 and 7 by the Interpretation Legislation Amendment Act 2018 that the reprint does not show; they are described as of a formal nature and are taken not to change the rules.

The Act commenced on 10 November 1981 (endnotes). **Regulations.** No regulations under the Act are deposited. The only place the Act defers to them is s 7(2)(d) (further allowances counted as pay): `another allowance` answers `NOTHING`. The penalty unit's dollar value is fixed outside this Act, so the maximum penalty is given in penalty units.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ntlsl-dates.l4`, `ntlsl-employee.l4` | `ntlsl-cases.l4` | 152 written, 152 satisfied; 3 traces as their `-- expect:` lines say |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read; two deliberately wrong assertions in a scratch file showed as `assertion failed`. Every expected value was written by hand from the text; the Act's own worked examples (s 11(4): $7,800; s 11(5): $6,045) are asserted to the dollar. Edges asserted: 10 years and 9, 9.99 (s 8(1)); 7 and 6 years (s 10(2)); 14, 15, 19 and 20 years (ss 8(3), 10(1A)); the anniversary day and the day before, from 1 January and from 29 February (s 12); 2 months and a day over, from 1 March, 31 August and 31 December (ss 8(7), 12(4)(e)); 12 months and a day over, from 15 January and 29 February (ss 11(7)(b), 12(3), 12(4)(d)); 1, 3 and 4 periods, 4 weeks and 3.9 (s 8(6)(b)); the due day and the day after, a part payment (s 11(6)); 3 and 6 years from 29 February (ss 14(2), 18A); a zero divisor (s 11(1)).

## Seat

**The employee** (or former employee) to whom the Act gives long service leave: "Does the Act cover me? How many years of continuous service do I have, and did this break or absence cost me any? Am I entitled to long service leave, how many weeks have I accrued and how many can I take now? What must I be paid when my job ends? How is the pay worked out, and was it paid on time?" For the two questions a death raises (s 10(3) through the s 10 question, and s 11(7)(b)), the employee's **personal representative**, who asks them on the deceased employee's behalf. No seat is given to the employer, the Minister, the authorised person or the court; the Minister's approvals and exemptions (ss 8(5), 13) are asked as facts.

The 2026-10-18 defaults:

- **The Act alone.** The Acts it names (the Workplace Relations Act 1996 of the Commonwealth through "award", the Public Holidays Act 1981, the Defence Act 1903 and others in s 12(2), the Corporations Act 2001) are named, not encoded; what they decide is asked as a fact.
- **The actors the text names:** the employee, the employer, the personal representative, the Minister, the authorised person, the court.
- **Judgments handed to others are answered conditionally:** whether a necessity "justifies" leaving (s 10(2)(c)), serious misconduct (ss 10(1A), (2)(b)), the Minister's satisfaction (ss 8(5), 13), whether a term is "not as advantageous" (s 17(1)) are inputs. "As soon as practicable" (ss 8(6)(a), 11(7)) is not decided; only the 12-month outer limit of s 11(7)(b) is encoded.
- **Definitions:** "employee" (s 7(1)), "pay" (s 7(2)–(4)), "hours of work per week" and "rate of pay" (s 11(1)), qualifying service (s 12) are worked from facts; "award", "serious misconduct", "related corporation" are asked as facts.
- **One case:** one employment (with one employer, counting service that s 12 joins to it).
- **Terms:** the Act's own words in the identifiers, with plain glosses in the `@desc` lines.
- **Machinery out** (below).

## Scope

In: s 6(1), (2), (4); s 7(1)–(4), (6); s 8(1)–(8) (s 8(5) as an input; s 8(6)(a) noted); s 9 (in the accrued-leave question's description); s 10(1)–(4); s 11(1)–(8); s 12(1)–(9); s 13 (as an input); s 14(2) (with s 14(1) in the description); s 16; s 17(1); s 18(1), (2) (in descriptions); s 18A.

Out, and why:

- ss 1, 2, 3, 19 — title, commencement, repeal of the Ordinances, regulation-making: machinery.
- ss 4, 5 — savings and transitional provisions for leave under the 1965–1974 Ordinances and employment ended before 10 November 1981: of historic reach only.
- s 7(5) — deemed employers under a law governing an award: the employer's identity is a fact the employee states.
- s 8(5A) — the Minister's power to revoke an approval: asked as whether an approval is in force.
- s 14(1), (3) — what the record must show, and a false entry: stated in the records question's description; the duty is the employer's.
- s 15 — the authorised person's investigation: an official's power; s 15(2) is a duty owed to the authorised person.
- s 17(2) — the employer's evasion: in the continuity answers through ss 12(4)(a), 12(5)(b); otherwise an offence, not a question the employee can answer.
- s 18(4) — a s 14 offence is a regulatory offence: of no consequence to the employee's questions.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 8(7), 11(7)(b), 12(3), 12(4)(d), (e), 14(2), 18A "2 months", "12 months", "3 years", "6 years" — `the same day ... months after`, `the same day ... years after` — the period ends on the same day of the month that many months later, clamped to the last day of a shorter month (31 August + 2 months = 31 October; 31 December + 2 months = 28 February; 29 February + 12 months = 28 February) — the next day (1 March), or periods of 30 or 365 days.
- **F2** s 12(1), s 8 "completed year of continuous service" — `the completed years from ... to ...`, `s 12 -- my completed years of continuous service` — both the first and the last day are counted, so a year is complete at the end of the day before the anniversary; from 29 February the anniversary in a common year is 1 March; days that do not count (s 12(5)) push the first day later — the anniversary day itself as the end of the year, or 365-day years.
- **F3** s 12(4)(e) "re-employed by that employer within 2 months" — `s 12(2), (4) -- my service stays continuous` — outside the 2 months the service is not continuous: `JUST FALSE` (s 12(1) "is the period during which the employee served ... continuously") — `NOTHING`, since s 12(4) only deems continuity and does not say what breaks it.
- **F4** s 12(1), (6), (8) — `s 12(6), (8) -- my earlier service counts` — service with any other employer does not count: `JUST FALSE` (s 12(1) is a definition of the period "with the employer") — `NOTHING`.
- **F5** ss 10(1), (1A), 14(1)(c) "long service leave credit" (undefined) — `s 8(1), (8) -- my long service leave credit in weeks` — 1.3 weeks for each completed year once 10 years are reached, less leave taken (s 8(1), (8)) — only the leave available to take under s 8(2), (3) (the 10- and 5-year blocks). The contrast with s 10(1A), which limits a dismissed employee to the blocks "only", supports the reading taken.
- **F6** s 10, with ss 6(4), 7(6)(a), 8(8) — `s 10 -- the weeks of pay owed when my employment ends` — leave already taken is taken off every head, including s 10(1A) and s 10(2) — s 10(2) "1.3 weeks for each completed year of service" without deduction.
- **F7** s 11(1) "hours of work per week" (b) "the average number of hours per week ... during a year" — `s 11(1) -- my hours of work per week` — total ordinary hours in the year divided by 52 — divided by the weeks actually worked (leaving out unpaid absences, which s 12(5) does not count).
- **F8** s 10(2)(a) "on or subsequent to attaining the age at which he or she may retire" — `s 10 -- the weeks ...` — head (a) applies however the employment ended, so a 7-to-10-year employee dismissed for serious misconduct at retirement age is paid — head (a) read down by head (b)'s exclusion of serious misconduct.
- **F9** s 10(3) "had he or she otherwise ceased to be employed on the date of death" — `s 10 -- the weeks ...` — between 7 and 10 years, paid only if the employee had reached retirement age (s 10(2)(a)); otherwise `NOTHING` (finding 4) — treat death as ceasing "on account of illness, incapacity" (s 10(2)(c)), which would pay.
- **F10** s 6 — `ss 6, 7 -- how the Act applies` — grounds are reported in the order s 6(1), s 6(2)(a), (b), (c), s 7(1), s 13, s 8(5); an employee with two grounds is told the first — all grounds together.
- **F11** s 11(6) — `s 11(6) -- whether my leave pay was paid on time` — day 0 is the day the leave was fixed; a payment before that day counts as made on day 0 (in time) — a payment before the leave was fixed is not a payment "in respect of" it.
- **F12** s 17(1), with s 8(4), (5) — `s 17(1) -- my Act rights stand despite the agreement` — an agreement the Minister approved displaces the Act's benefits: `JUST FALSE` — s 17(1) applies even then (the approval requires the benefits to be no less favourable, so the case should not arise).
- **F13** s 12(3) "within a period of 12 months after completing that apprenticeship" — `s 12(3) -- my apprenticeship counts` — re-employment from the day of completion to the same day 12 months on; re-employment dated before completion answers `JUST FALSE` — `NOTHING` for that impossible order.
- **F14** s 8 "each completed year" — every question that takes completed years — a fractional number of years is rounded down — rejected as an input error.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "where" conditions of ss 6(1), 8(1), 12(3), 12(4)(b), (e), 10(2); the "does not apply" of s 6(2) and the "does not form part" of s 12(5) (flat negatives); the "means" definitions of employee (s 7(1)) and rate of pay and hours of work per week (s 11(1)); the "but not including" of s 7(2); the "except as provided" and "shall not pay" of s 10(4); the "in separate periods not exceeding 3, of not less than 4 weeks each" of s 8(6)(b); the periods of ss 8(7), 11(6), 11(7)(b) give `JUST FALSE` or a breach. The open definition of pay (s 7(2) "shall be read as including", with Regulations not deposited), the prohibition of s 16 and the protection of s 17(1) outside their own wording, a zero divisor in s 11(1), and the s 10(3) death below retirement age give `NOTHING` (*open definition*, *limited by its own wording*, *silent*).

## What the Act turns out to say

1. **Leave accrues every year but is taken in blocks.** s 8(1) entitles the employee, from 10 years, to 1.3 weeks for each completed year; s 8(2), (3) let it be taken only as 13 weeks at 10 years and 6.5 weeks at each further 5 years. At 12 years the employee has accrued 15.6 weeks but can take 13; the other 2.6 weeks are paid out if the employment ends (s 10(1)) but cannot be taken until 15 years. Both questions are exported, and asserted.
2. **"Long service leave credit" is not defined** (ss 4(2), 10(1), (1A), 14(1)(c)). It is read as the s 8(1) accrual less leave taken (fork F5).
3. **"Award" is defined by the Workplace Relations Act 1996 of the Commonwealth** (s 7(1)), which has since been replaced by the Fair Work Act 2009. Read literally, s 6(2)(b) excludes only employees covered by an award under the 1996 Act; whether a modern award or enterprise agreement that provides for long service leave excludes the Act is not answered by this text, so the question is asked as a fact. Worth checking against the Fair Work Act's own rules on state long service leave before relying on the answer.
4. **A death between 7 and 10 years of service.** s 10(3) pays the personal representative what s 10(2) would have paid "had he or she otherwise ceased to be employed on the date of death", but s 10(2) pays only on three kinds of ceasing (retirement age, termination by the employer, illness or necessity). The text does not say which the dead employee is taken to have had; only the retirement-age head can be decided from facts (fork F9). Asserted (`NOTHING`, and 11.7 weeks at retirement age).
5. **Retirement age outranks misconduct between 7 and 10 years.** s 10(2)(a) pays on any ceasing at or after retirement age; only head (b) excludes serious misconduct (fork F8). Asserted.
6. **s 10(1A) is a floor.** "an amount not less than" the leave for completed 10- and 5-year periods: the answer is the least the employer must pay; at 14 years a dismissed employee gets 13 weeks, not 18.2. Asserted.
7. **No time is fixed for paying a resigning employee.** s 11(7) sets when the employer pays on "retirement, termination of employment, ill health, death or domestic or other pressing necessity", but not on a resignation for another reason, though s 10(1) pays such an employee from 10 years. Whether "termination of employment" includes a resignation is open; this encoding encodes no deadline for s 11(7)(a) ("as soon as practicable") in any case.
8. **The s 11(2) sum after leave has been taken.** The payment is the sum, for each completed year "that comprises the period of service from which ... entitlement ... is derived", of RP × HWW × 1.3. Where some of the leave has been taken, the Act does not say which years' hours belong to the remaining credit, or how a part-year of credit (s 10(1) after leave taken) is priced; the amount question takes the years' hours as the person lists them.
9. **A small drafting slip.** s 11(6) refers to "the amount calculated under (2)", leaving out "subsection".
10. **Fixed money amounts.** The board and lodging values of s 7(2)(c) ($15 and $5 a week) have not changed since 1981 and are not indexed. The s 11(4), (5) examples are internally consistent ($7,800 and $6,045), and are asserted.
11. **Absence and continuity are separate.** A gap of up to 2 months before re-employment, a stand-down or a dispute does not break continuity (s 12(4)) but does not count towards the years (s 12(5)); the encoding gives two questions for them, and the completed-years question takes the days that do not count.

## Before this is worth relying on

- An independent test pass and a lawyer's review of forks F3, F5, F8, F9 and F12, and of finding 3 (the "award" definition and the Fair Work Act).
- Check the Interpretation Legislation Amendment Act 2018 changes to ss 1 and 7 against an authorised version.
- The Interpretation Act 1978 (NT) rules on reckoning time are not applied beyond fork F1.
- Deployment to Legalese Cloud, by a person with access.
