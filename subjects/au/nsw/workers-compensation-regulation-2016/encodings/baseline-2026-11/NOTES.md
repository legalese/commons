# Workers Compensation Regulation 2016 (NSW) -- baseline encoding, the injured worker

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 24 July 2024). It is unofficial and may be out of date: amendments after that version, and any
> indexation since, are missing. Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Five regulative rules (cll 8J(2), 8K(2)-(3),
8M(2), 8N(1), 9(2) with 10(2)) run by `EVALTRACE` inside exported questions that take only plain facts. No REFUSE, no
`#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no
human gate. Not for public use as advice.

This is the first encoding of the Regulation; nothing existing was touched. Two neighbouring encodings already use a
few of its clauses and stay as they are: the 1987 Act's baseline
(`subjects/au/nsw/workers-compensation-act-1987/encodings/baseline-2026-10/`: cl 8AB, cll 35-36, Schedule 5) and the
1998 Act's baseline (`subjects/au/nsw/workplace-injury-management-and-workers-compensation-act-1998/encodings/baseline-2026-11/`:
cl 42). This encoding takes the rest of what a claimant meets in the Regulation.

## Edition

- **Regulation:** Workers Compensation Regulation 2016, corpus document `nsw_legislation:2024-07-24/sl-2016-0559`,
  deposited at `../../registers/source-bundle/sl-2016-0559.txt` (sha256 9c24119b...b92ee2f5), from the Open Australian
  Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the authorised
  text, and possibly out of date.
- **Words of the 1987 Act** that the Regulation's clauses feed (ss 19, 19A, 19B; Schedule 3 cll 2, 4, 5) are quoted
  from the deposited `subjects/au/nsw/workers-compensation-act-1987/registers/source-bundle/act-1987-070.txt` (corpus
  version 2023-10-30, same caveat). The stable `l4` cannot IMPORT across subjects, so they are quoted in comments.
- **Not deposited:** the Workers Compensation Guidelines and approved forms; SIRA's indexation orders (the maximum weekly
  compensation amount used by cl 8G(2) is an input defaulting to the deposited 1987 Act figure of $1,838.70); the value
  of a penalty unit.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.
2026-11-07:

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wcr-dates.l4` | 0 | 0 | 0 | 0 |
| `wcr-disease.l4` | 0 | 0 | 0 | 0 |
| `wcr-earnings.l4` | 0 | 0 | 0 | 0 |
| `wcr-claims.l4` | 0 | 0 | 0 | 0 |
| `wcr-cases-disease.l4` | 0 | 0 | 59 | 59 |
| `wcr-cases-earnings.l4` | 0 | 0 | 100 | 100 |
| `wcr-cases-claims.l4` | 0 | 0 | 82 | 82 |

241 assertions, all satisfied. One `#TRACE` (cl 8N(1), nothing paid by day 15) with an expect line: BREACH by the
insurer with the offence reason, as expected. Every expected value was worked by hand from the text, with the day counts
in comments: the 364-day period across a leap year, the first and second COVID-19 prescribed periods (84 days; 2 or
more days; the 27 September cap), 7 and 6 days of unpaid leave, the $155 floor, ages 17 and 18, the last day and the day
after of each 5, 7, 14 and 21 day period, exactly 3 months in cl 9, titres 640/320 and 400/200, 14 and 13 days between
samples, a judgment equal to each final offer, and one month from 31 January and from 1 March.

## Seat

**The injured worker** (for work injury damages, the claimant). Every exported question is one the worker would ask:
"Is my disease presumed to come from work?", "Does my test count?", "What are my pre-injury average weekly earnings?",
"Must the insurer approve our agreement?", "By when must it decide, and did it?", "Must it send me that report?", "Can I
recover the cost of my report?", "Who pays the costs of my damages case?". Provisions addressed to the insurer, the
employer, a medical assessor, the Authority or the court are encoded as what they mean for the worker. No other seat:
the employer's duties in this Regulation (return-to-work programs, registers, premiums, wage returns) are owed to the
insurer and the Authority, and officials get none.

The 2026-10-18 defaults:

- **The Regulation alone, with the instruments that set its numbers.** The Regulation sets its own numbers ($155, 38
  hours, 5/7/14/21 days, the titres, the prescribed periods). The one outside number, the maximum weekly compensation
  amount (cl 8G(2)), is an input defaulting to the deposited 1987 Act figure; a declared figure changes the answer.
- **The actors the text names.** Worker, employer, insurer, the person a claim is made on, medical assessor, Authority,
  court, mediator, President.
- **Judgments answered conditionally.** "reasonably satisfied" (cl 8D), "satisfied that the agreed amount reasonably
  reflects" (cl 8K(4)), "reasonable excuse" (cll 8K(3), 168), "financially material" (cll 8C, 8EA), "serious threat"
  (cl 41(5)), "clinically compatible illness" (Sch 2) are inputs.
- **The text's definitions worked out; borrowed terms asked.** Worked out: the relevant earning period and its
  adjustments, person under legal incapacity (cl 8K(11), an "includes" list, with a residual input), payment increase
  decision, forensic medical report, the Schedule 1 and 2 tables, prescribed employment (s 19B(9) with cl 5D). Asked:
  current work capacity, work capacity decision, Sch 3 cl 5(3)(c) applying, injury management plan objectives.
- **One case.** One worker, one injury, one employment (fork F4), one claim.
- **The text's terms with plain glosses.** In each `@desc`.
- **Operative clauses in; machinery out.** See Scope.

## Scope

**In** (by module):
- `wcr-disease.l4` -- Part 2: cl 4 with Schedule 1 (all rows); cl 5 with Schedule 2 Part 1 (all tests); cl 5A; cl 5B
  with Schedule 2 Part 2; cl 5C(1), (3)-(5), (7); cl 5D (with 1987 Act s 19B(6), (9)).
- `wcr-earnings.l4` -- Part 3: cll 6AA, 6, 7. Part 4: cll 8, 8AA, 8AB; Division 2 cll 8A, 8B, 8C, 8D (as a question),
  8E, 8EA; Division 3 cl 8G; Division 4 cll 8H(2), (3), 8I, 8J(2) (regulative), 8K(1)-(5), (8), (11) and (2)-(3)
  (regulative), 8L, 8M(1), (2) (regulative); Division 5 cl 8N (regulative). Part 5: cll 9 and 10 (the 14 and 21 days
  regulative).
- `wcr-claims.l4` -- Part 8: cl 37; cl 38(1); cl 38A; cl 41; cll 42A, 42B. Part 9: cll 44-49. Part 17 Division 3
  Subdivision 2: cll 94-99. cl 168. cl 175(2).

**Out, and why:**
- cl 5C(2), (6) (textual modifications of the 1987 Act), cl 8F (factors to "take into account": a judgment with no
  rule to compute), cl 8J(3)-(4), 8K(6)-(7), (9)-(10), 8M(3)-(4) (forms, interim payment decisions, notification with no
  time): procedure or judgment.
- cl 35, cl 36 and Schedule 5: encoded in the 1987 Act's baseline. cl 42: encoded in the 1998 Act's baseline.
- cl 38(2), cl 38B (coal miners), cl 39, cl 40: notices and registers owed by the employer or insurer to others; coal
  miners are a separate scheme.
- Parts 6, 7 (return-to-work programs, rehabilitation provider approval), 10, 11, 12, 14 (policies, self-insurers,
  funds), 13 with Schedule 4 (deemed ministers of religion: a table of names, for the Act's worker definition), 15, 16
  (penalty notices, advertising), 18 (premiums), Schedule 3 (policy terms): machinery or duties between employer,
  insurer and Authority.
- Part 17 Divisions 1, 2, 4-6 and Schedules 6, 7 (maximum costs and costs assessment): the law practice's costs, a large
  fee table; out for this pass, recorded as the main gap for a claimant (who pays is in, how much is not).
- cll 164-167, 169-174, 176: machinery.
- **cl 177 (lump sum death benefit, additional compensation fees):** the formula was lost when the corpus converted the
  text (finding 5). Not encodable from the deposit.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** every "within n days after" and "within one month of" -- `wcr-dates.l4` -- the last day is the day plus n, or
  the same day number a month later (the month's last day where there is none) -- the Interpretation Act 1987 (not
  deposited) read otherwise.
- **F2** cl 4(2) with Schedule 1 -- `Does Schedule 1 presume my disease is work-related` -- a disease and employment not
  opposite each other answer `JUST FALSE` (cl 4 prescribes only what is set out) -- `NOTHING` ("listed in Schedule N",
  decided case by case under the 2026-11-05 ruling).
- **F3** Schedule 2 Part 1 "where possible, conducted at the same laboratory" -- `the test gives a prescribed result for`
  -- advice, not a requirement -- a requirement whenever it was possible.
- **F4** 1987 Act Sch 3 cl 2(1) "any employment" -- `What are my pre-injury average weekly earnings` -- one employment
  per question; a worker with several adds the results -- the Regulation's adjustments applied across employments
  together.
- **F5** cl 8D -- `the adjusted earning period` -- alignment with the pay period is not applied to the computed period
  (it is the insurer's choice, asked by `May my earning period be aligned with my pay`) -- applied whenever permitted.
- **F6** cl 8E -- `the adjusted earning period` -- the unpaid leave must begin within the period, and at least 7 days of
  the run without earnings must lie in it; one run of leave per question -- leave begun before the period counts from
  the period's first day.
- **F7** Sch 3 cl 2(1) "weekly average" -- `What are my pre-injury average weekly earnings` -- gross earnings for the
  days that count, times 7, divided by those days -- divided by whole weeks.
- **F8** cl 8K(1) "an application ... in accordance with clause 8J" -- `Must the insurer approve our PIAWE agreement` --
  a late application answers `NOTHING` -- `JUST FALSE` (no duty arises).
- **F9** cl 8K(3) "within 7 days after the earlier of" -- `the day the 7 days to determine run from` -- the earlier of
  the two days even if it is before the application was received -- never earlier than receipt.
- **F10** cl 9(1)(a) "a period of less than 3 months" -- `Does clause 9 rule out work assistance` -- 1 January to
  31 March is 3 months, 1 January to 30 March less -- counted in days (90 or 91).
- **F11** cl 41(3) "identified in a statement under clause 38(1)(d)" -- `Must the insurer send me a copy of the report`
  -- read as the notice's statement of reports (cl 38(1)(b)) -- read literally, no report could ever be identified
  there (finding 2).
- **F12** cl 44(4)(b), (c) -- `Is this a forensic medical report` -- (c) is applied first, so a s 119 report obtained
  for another claim is not one in this claim -- (b) "includes" prevails.
- **F13** cl 44(3) "an additional forensic medical report" -- `How many forensic medical reports may each side have
  admitted` -- one more in all (2) -- one more for each further specialty (finding 3).
- **F14** cl 46(3) -- `Must my forensic report go to the medical assessor` -- a second forensic report of the same party
  is not disclosed, even one admitted under cl 44(3) -- cl 46(1)(a) requires it (finding 3).
- **F15** cll 94, 95 "no less favourable", "less favourable" -- `Who pays the costs of my damages case` -- compared by
  the amount of damages -- by all the terms of the offer.
- **F16** cll 94, 95(1) -- `Who pays the costs of my damages case` -- cl 94 first where both could apply (a claimant
  offer below the insurer's) -- cl 95 first. cl 99 is applied to the deemed claimant offer of cl 97 too, not to the
  deemed $0.
- **F17** cl 168 -- `Must I pay the costs of the medical assessment` -- costs outside (1)(a)-(d), or with a reasonable
  excuse, answer `NOTHING` (s 330 of the 1998 Act decides) -- `JUST FALSE`.

The rulings on negatives (2026-11-04 and 2026-11-05) are recorded word for word in `docs/ENCODING-GUIDE.md` section 5;
the `NOTHING-kind` tags here follow them: "silent", "points outside the text", "scope limit with no 'only'", "limited
by its own wording", and "scope limit with 'only'" (cl 8(2)), used only where the answer is an amount or a period, which
cannot be `JUST FALSE`.

## What the text turns out to say

1. **cl 6 prescribes for a repealed section.** cl 6 sets the $155 minimum "for the purposes of section 44C(7) of the
   1987 Act"; the deposited 1987 Act shows ss 44C-44I as repealed. It works only through the transitional provisions
   that keep the old s 44C for injuries before 21 October 2019 (Schedule 6). Not encoded beyond the $155.
2. **cl 41(3) points at the wrong paragraph.** The exception is for a report "identified in a statement under clause
   38(1)(d)", but cl 38(1)(d) is "details of the procedure for requesting a review"; the statement identifying reports is
   cl 38(1)(b) (and (a) for documents the worker submitted). Read as (b) (fork F11).
3. **Part 9 pulls two ways on a second specialty.** cl 44(3) allows "an additional forensic medical report ... in that
   specialty" where specialists of different qualifications treated the worker ("that specialty" has no clear
   antecedent, and "an additional" may mean one or one per specialty); cl 46(1)(a) requires an admitted report to be
   disclosed to the medical assessor; cl 46(3) says nothing in cl 46 permits more than one forensic report of a party to
   be disclosed. Forks F13, F14; asserted (3 specialties: 2 reports; a second report already sent: no disclosure).
4. **Two definitions of forensic medical report.** cl 44(4) has the exclusion (c) for reports obtained for another
   claim and limits (b) to specialists; cl 46(4) has no (c) and says "medical practitioner" in (b). The encoding uses
   cl 44(4) for both clauses.
5. **cl 177's formula is missing.** The deposit keeps "the fee calculated in accordance with the following formula is
   prescribed -- Where -- A is $1,309. ... G is ..." and both tables, but not the formula. It needs a
   `sl-2016-0559.formulas.md` sidecar transcribed from the authorised rendering before cl 177 can be encoded.
6. **cl 8EA is spent for later injuries.** The prescribed periods end on 27 September 2020, so they can fall in the
   52 weeks only for injuries up to 27 September 2021. Asserted for an injury on 1 March 2021.
7. **cl 8K(3) can set a deadline before the application exists.** If the insurer accepted liability before the
   application arrived, "7 days after the earlier of" may already have passed when it is received. Fork F9.
8. **Schedule 2 Part 2 typo:** "a PCR test that is listed n the Australian Register"; harmless.
9. **cl 8N(1)'s penalty is in penalty units**, whose value is set elsewhere (not deposited); the breach reason quotes
   20 penalty units only.

## Questions (exported)

`wcr-disease.l4` (7): `Does Schedule 1 presume my disease is work-related`, `Does my test show I contracted the
disease`, `Have I been engaged in firefighting employment`, `Is my work prescribed employment for COVID-19`, `Does my
test show I contracted COVID-19`, `Until when am I presumed unable to work`, `Am I taken to be partially incapacitated
during isolation`.

`wcr-earnings.l4` (22): `My PIAWE after the minimum`, `The prescribed number of hours for my injury`, `What is my
relevant earning period`, `What are my pre-injury average weekly earnings`, `May my earning period be aligned with my
pay`, `My PIAWE as an apprentice, trainee or young worker`, `By when must our PIAWE agreement application be made`,
`Was our PIAWE agreement application made in time`, `Must the insurer approve our PIAWE agreement`, `What PIAWE apply
under our agreement`, `May the insurer approve a variation of our agreement`, `By when must the insurer decide our
PIAWE agreement`, `Has the insurer decided our PIAWE agreement in time`, `By when must the insurer act on the
withdrawal`, `Has the insurer acted on the withdrawal in time`, `Is it a payment increase decision`, `By when must the
insurer pay the increase`, `Has the insurer paid the increase in time`, `Does clause 9 rule out work assistance`, `Does
clause 10 rule out education or training`, `By when must my return to work claim be decided`, `Has my return to work
claim been decided in time`.

`wcr-claims.l4` (14): `To whom must I give notice of my hearing loss`, `Does my dispute notice contain what clause 38
requires`, `Does my damages dispute notice contain what clause 38A requires`, `Must the insurer send me a copy of the
report`, `Was my review dealt with as clause 42A requires`, `Does my review decision notice contain what clause 42B
requires`, `Is this a forensic medical report`, `How many forensic medical reports may each side have admitted`, `May
my supplementary report be admitted`, `Must my forensic report go to the medical assessor`, `Does clause 47 stop me
recovering the cost of my report`, `Must I pay the costs of the medical assessment`, `Who pays the costs of my damages
case`, `Which certificate governs the day`.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation and
  figure.
- Transcribe the cl 177 formula into a sidecar and encode it; encode Schedules 6 and 7 (maximum legal costs).
- Have a lawyer review the forks, especially F8 (late agreement applications), F11 (cl 41(3)), F13 and F14 (Part 9),
  and F15-F16 (costs).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
