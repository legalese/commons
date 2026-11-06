# Safety, Rehabilitation and Compensation Regulations 2019 (Cth) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Regulations; nothing existing was touched. The Act's own encoding
(`subjects/au/safety-rehabilitation-and-compensation-act-1988/encodings/baseline-2026-10/`) brought in no instrument; this
encoding is the layer for the Regulations, and because the stable `l4` cannot IMPORT across subjects, the few words of the
Act that each regulation fills in (s 4 "medical treatment" (i) and "Entity" (c), s 7(8)-(9), s 8(9B)-(9G), ss 61(1A),
62(6)) are encoded here beside it, quoted from the Act's deposit, rather than imported. Nothing in the Act's encoding is
restated.

The focus asked for is the provisions a claimant meets. Almost every operative provision of the Regulations is met by a
claimant, directly or through who pays and manages their claim, and those are encoded whole; what is out is listed under
Scope with the reason. The rules are in `srcr-rules.l4`, the questions in `srcr-seat.l4` (which imports the rules and never
restates one), the cases in `srcr-cases.l4`.

## Edition

- **Regulations:** Safety, Rehabilitation and Compensation Regulations 2019 (F2019L00423), Compilation No. 2, compilation
  date 1 April 2024, includes amendments up to F2023L01692 (register id F2024C00663), registered 26 July 2024; deposited at
  `../../registers/source-bundle/F2019L00423.txt` (text sha256 16b7b30f02ba2389da9345c7c49f35fa182f47cac88606bee4c5af13d5e4e24b
  per its `.meta.json`), a plain-text conversion of the Word file from the Federal Register of Legislation, retrieved
  19 October 2026. It is the latest compilation at retrieval.
- **Act (for the provisions the Regulations fill in):** Compilation No. 82, compilation date 1 July 2026 (C2026C00285),
  at `../../../safety-rehabilitation-and-compensation-act-1988/registers/source-bundle/C2004A03668.txt`.
- **Numbers set elsewhere:** the Wage Price Index numbers (regs ss 8, 10) are published by the Australian Statistician and
  are inputs. The Safety, Rehabilitation and Compensation Directions 2019 (cited in the note to s 19) are not deposited.
- **A formula is missing from the deposit:** regs ss 9 and 11 (finding 1).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read; one deliberately wrong assertion (an increase of $37.03 for $37.04) was run once in a scratch copy, since deleted,
and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `srcr-rules.l4` | 0 | 0 | 0 | 0 |
| `srcr-seat.l4` | 0 | 0 | 0 | 0 |
| `srcr-cases.l4` | 0 | 0 | 133 | 133 |

Every exported question has cases, with the edges: every Schedule 2 Entity and another employer; each s 7 profession,
registration against membership, and the two cases outside s 7; every s 8A period and a sample of the Act's; the
firefighter presumption at its period and just under (5, 10 and 15 years), on 3 and 4 July 2011 and on 16 and 17 December
2022 (reg s 36), for a State employer, without exposure, and for an unlisted disease; every combination of the indexation
routes; the first indexation date either side of 1 July and on it; F at a whole 0.001, just over it, with a fifth decimal
cut off, with no rise and with a fall; the increase with and without rounding up; the s 11A(1) last day for 20 and 60 days,
on and before 1 April 2024, without a s 54 claim, with a pause, a pause covering the day of receipt, overlapping pauses, a
pause after the last day and one on it; the regulative rule on the last day and the day after, decided and not; the
reconsideration period across a year end, before 1 April 2024, and for a s 38 request; each licence answer for an
authority and a corporation, suspended and revoked, before and after revocation, with and without the licence's scope.

## Seat

**The claimant** (`srcr-seat.l4`): the injured employee of the Commonwealth, a Commonwealth authority, an Entity or a
licensed corporation (licensee), who claims compensation under the Act. "Who is my employer's principal officer?", "Does
the scheme count my psychologist's treatment?", "As a firefighter, is my cancer presumed to come from my work?", "Which
1 July increase applies to my normal weekly earnings, from when, and by how much?", "By what day must my claim (or my
request for reconsideration) be decided, and was it?", "My employer's licence was suspended or revoked: who pays, who
manages my claim, must my employer pass my claim on, and who is my rehabilitation authority?".

No seat for Comcare, the Commission, the determining authority or the Minister. No employer seat was written: the licence
application provisions (Part 4 Division 1, Schedule 1) and the guarantee money provisions would be its questions.

The 2026-10-18 defaults:

- **The instrument alone, with the instruments that set its numbers.** Followed. The Regulations are themselves the
  number-setting instrument of the Act; the Act's words they fill in are encoded beside them (Method). The Wage Price
  Index numbers are inputs.
- **The actors the text names.** Followed: the employee (claimant), the determining authority, Comcare, the Commission,
  the licensed authority, the licensed corporation and their principal officers, the rehabilitation authority.
- **Judgments answered conditionally.** Followed: whether firefighting duties were "not insubstantial" (Act s 7(9)(a)) is
  folded into the years the claimant counts; "unless the contrary is established" is stated in the answer, not decided;
  the s 11A(3) end days that turn on what the authority "reasonably believes", and item 5's "reasonable and necessary",
  are the dates the claimant enters; Comcare's decisions under ss 25, 30(8) and 31 are asked as facts.
- **The text's definitions worked out; borrowed terms asked.** Followed: "quarter", "indexation date" (Act s 8(9C)),
  "preservation period", the s 7(2) requirements and the s 11A(3) covered days are worked out; "national registration
  authority" (Healthcare Identifiers Act 2010), "relevant professional association", s 54 compliance and the Wage Price
  Index are asked.
- **One case.** One claim (or one request for reconsideration) by one employee.
- **The text's terms with plain glosses.** Followed in each `@desc`.
- **Operative provisions in; machinery out.** Followed (see Scope).

## Scope

**In:** s 5 (as used); s 6 and Schedule 2; s 7; s 8A with Act s 7(8), (9)(b), (c); ss 8, 9, 10, 11 with Act s 8(9B),
(9C), (9E), (9F); s 11A with Act ss 61(1A), 62(6); s 19(2), (3)(a), (b) as they reach the claimant; s 21(2), (3)(a)-(c),
(7); s 22(1)(d); s 25(1) (as a fact); s 27(2), (3)(a), (b); s 28(1)(d), (3); s 30(8), (11); s 31(1) (as a fact); ss 36, 37.

**Regulative rules:** two. Act s 61(1A) with reg s 11A(1) (`MUST determine my claim WITHIN` the counted days) and Act
s 62(6) with reg s 11A(2) (`MUST decide my request to reconsider WITHIN` 29 days after the day of receipt), each with
`LEST BREACH BY the determining authority BECAUSE ...`; run by EVALTRACE inside "Was my claim determined in time?" and
"Was my request for reconsideration decided in time?", which take only plain facts. The duties to pass on a claim (ss 19,
21, 30) have no period ("on receiving") and are answered as yes or not answered.

**Out, and why:**
- ss 1, 3 (name, authority): machinery.
- Part 3, ss 12-14 (renewal dates and fees for approved rehabilitation program providers): they bind providers, not a
  claimant.
- Part 4 Division 1, ss 15-17 and Schedule 1 (applying for a licence): the employer's application; an employer seat.
- ss 18, 26 (purpose): no rule.
- ss 19(2)(c), (3)(a)(iv), (c); 21(2)(d), (3)(c)(ii), (d), (4), (5), (6), (8); 27(3)(c): what the licensee owes Comcare,
  premiums, and who is party to pending proceedings. s 21(5) (Comcare becomes the party to proceedings) matters to a
  claimant with a case on foot and is worth a question later.
- ss 20, 24, 30(1)-(7), (9), (10) (guarantee money): between the Commission, Comcare, the licensee and the guarantor; it
  enters only where s 30 starts the s 30(11) duty.
- ss 22(1)(a)-(c), (e), (f), (2), (3); 28(1)(a)-(c), (e), (f), (2): the preserved licence; enters as the preservation
  period fact. ss 23, 29 (the Commission determines the end of that period): Commission machinery, asked as a fact.
- s 32 (compensation for an acquisition of property by Comcare's payment of guarantee money): it compensates the owner of
  that money, not an injured claimant.
- ss 33-35 (transition from the 2002 Regulations): only for licence applications and licence decisions before 28 March
  2019.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Delegated definitions, defences and "until" bars** ... (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all" ...

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here:
- `JUST FALSE`: s 7(2) "meets the requirements ... if" not met; Act s 7(8) "If an employee: (a) ... (d)" not met
  (worded in the question as "s 7(8) does not help", in the spirit of ruling (b) of 2026-11-05: s 7(1), (2) and the
  ordinary test remain); Act s 7(9)(c) "only if".
- `NOTHING`: an employer not in Schedule 2 (the Act's paragraphs (a), (b) point outside); a practitioner not in s 7(1),
  and treatment that is not therapeutic (scope limits); a disease not in the table, for its period; reg s 36 and s 37 not
  met (application provisions with no "only"); a claim not made under s 54; a s 38 request (silent); each licence
  provision whose "If the licence authorises ..." is not met (silent); a corporation's suspension (scope limit); outside
  the preservation period (silent).

### Forks

- **F1** Schedule 2, `Schedule 2 -- the principal officer of my employer`: another employer answers NOTHING; other
  reading: none (paragraphs (a), (b) of the Act's definition are outside the Regulations).
- **F2** s 7(1), `s 7 -- the treatment is prescribed medical treatment`: treatment by a listed practitioner that is not
  "therapeutic treatment" answers NOTHING; other reading: JUST FALSE, as s 7 prescribes nothing else.
- **F3** s 7(2)(b), same function: where a national authority exists, an unregistered member of a professional
  association answers JUST FALSE ("if there is no such authority"); other reading: none.
- **F4** reg s 36, `s 7(8) -- my employment is taken to have contributed to the disease`: a s 8A cancer sustained before
  4 July 2011, or decided before 17 December 2022, answers NOTHING; other reading: JUST FALSE, since item 13 then has no
  prescribed cancer.
- **F5** reg s 36 "after the commencement of that instrument" (17 December 2022): a decision on 17 December 2022 is taken
  as after it (`s 36 -- s 8A applies to the decision`); other reading: from 18 December 2022.
- **F6** Act s 8(9C) "the 1 July next following ... the date of that cessation", `s 8(9C) -- the first indexation date
  after I ceased`: a cessation on 1 July gives the next year's 1 July; other reading: that same day.
- **F7** regs ss 9, 11, `ss 9, 11 -- F`: "worked out to 4 decimal places" is cut off at the fourth place and "rounded up
  to 3 decimal places" raises any remainder to the next 0.001; other reading: round half up at each step.
- **F8** regs ss 9, 11, `ss 9, 11 -- the further increase in dollars`: the increase is WE x (F - 1), cut off at 3
  places and raised to the next cent; other reading: the lost formula gives the new earnings F x WE, rounded the same way
  (the same result when WE is in whole cents; finding 1).
- **F9** s 11A(1), `s 11A(1) -- the last day for determining my claim`: a claim not "made in accordance with section 54"
  starts no period (NOTHING); other reading: the period runs from receipt anyway.
- **F10** s 11A(1), (2) "starting on the day the determining authority receives": the day of receipt is the first of the
  20, 60 or 30 days; other reading: counting starts the next day (each answer a day later).
- **F11** s 30(11), `ss 19, 21, 30 -- my employer must pass my claim to Comcare`: for a former licensed corporation the
  duty arises only once s 30 applies (a guarantee demand) and for injury before revocation; otherwise NOTHING; other
  reading: none in the text, which gives a corporation no such duty outside s 30.
- **F12** ss 19(2), 21(2), 27(2), `ss 19, 21, 27, 28 -- who is liable for my compensation`: where the licence did not
  cover accepting liability, injury before revocation answers NOTHING; other reading: Comcare (the ordinary position
  under the Act, outside the Regulations).
- **F13** s 21(7), same function: Comcare is liable for injury on or after revocation whatever the licence's scope, as
  s 21(7) is not conditioned on s 21(2); other reading: only where s 21(2) applied.
- **F14** ss 22(1)(d), 28(1)(d), `ss 22, 28 -- my rehabilitation authority after revocation`: a person Comcare has
  arranged under s 25 or 31 is the answer in or out of the preservation period; outside it with no arrangement, NOTHING.

## What the Regulations turn out to say

1. **The indexation formula is missing from the deposit.** Regs ss 9 and 11 read "in accordance with the following
   formula: where:" with nothing between; the terms F and WE and the note ("there will be a further increase ... only if
   F is greater than 1.000") survive. The increase is encoded as WE x (F - 1) (fork F8). Before this encoding is relied on,
   the formula should be transcribed from the authorised rendering into a `F2019L00423.formulas.md` sidecar and the cases
   checked against it. Asserted under fork F8.
2. **Item 13 has no prescribed conditions.** Act s 7(8)(d) asks a prescribed cancer to meet "the conditions (if any)
   prescribed"; reg s 8A prescribes kinds and periods only, so (d) is always met. Asserted (lung, mesothelioma and
   cervical cancers presumed on the Act's (a)-(c) alone).
3. **Act s 8(9B) and (9E) both read on to a former employee.** A former employee's earnings cannot be increased under
   s 8(9) (it runs only "while the employee continues to be employed"); if there was also no s 8(6) or (7) increase, the
   s 8(9E) conditions are met as well, and (9E)(a) does not list a (9B) increase. On the words, both further increases
   apply each 1 July; the encoding says so and does not choose. Asserted.
4. **Pauses stop only the claim clock.** s 11A(3) is "For the purposes of subsection (1)"; the 30 days for a
   reconsideration (s 11A(2)) run straight through even when the authority asks for information. Asserted (no pause input
   for requests).
5. **s 37(b) applies s 11A to s 38 requests that s 11A does not cover.** s 37(b) speaks of "a request to reconsider a
   decision under section 38 or 62 of the Act"; s 11A(2) is made only "For the purposes of subsection 62(6)". No period is
   prescribed for reconsidering a rehabilitation determination. Asserted (NOTHING).
6. **A revoked corporation's later injuries leave the Act.** s 27(2)(a) ends its liability for injury on or after
   revocation and s 28(3) says the Act "ceases to apply to the former licensed corporation and its employees"; nothing
   here makes Comcare liable instead (contrast s 21(7) for authorities). The note to s 28 points to State and Territory
   workers' compensation. Asserted.
7. **No consequence for a missed period.** Neither Act s 61(1A) nor s 62(6) nor reg s 11A says what follows when the
   period passes: there is no deemed determination or deemed refusal. The encoding reports the breach of the duty and no
   more.
8. **A drafting slip in s 29(6).** In the section on former licensed corporations, s 29(6) and (6)(a) speak of "the former
   licensed authority" (copied from s 23(6)). Not encoded (Commission machinery); noted for the reader.
9. **s 11A(3) end days can turn on the authority's belief.** Items 3(c) and 4(c) end a pause on "the day on which the
   determining authority reasonably believes" a person has failed to comply or will not give evidence; a claimant may not
   know that day. The encoding takes the pause dates as entered.

## Before relying on it

Transcribe the regs ss 9 and 11 formula (finding 1); have a reader settle forks F4, F7, F8 and F10, which change answers
on real dates and amounts; add the s 21(5) proceedings question; and run an independent test pass.
