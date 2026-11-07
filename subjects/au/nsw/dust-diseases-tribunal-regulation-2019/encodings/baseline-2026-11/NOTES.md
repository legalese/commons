# Dust Diseases Tribunal Regulation 2019 (NSW) -- baseline encoding, the claimant

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document `nsw_legislation:2022-07-01/sl-2019-0405`). It is unofficial and may be out of date: amendments after that
> version are missing. Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Four regulative rules, each run by
`EVALTRACE` inside an exported question that takes only plain facts (dates, numbers, yes/no, choices):

- the plaintiff's notices to the registrar within 5 or 1 business days (cl 16(6), 23(5), 34(2));
- the plaintiff's further information no later than 5 business days before mediation (cl 26(8));
- a defendant's notice of a medical examination and the examination itself (cl 29(1), (2)), the second rule under the
  first's `HENCE`;
- the payment due under an accepted offer within 28 days (cl 88(6)), whose `LEST` opens the accepting party's permission
  to withdraw (cl 93(1)(a)).

Business days (cl 11(1)) and the ignored Christmas period (cl 11(2)) are counted in `ddtr-dates.l4`, which uses only the
built-in date functions. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Regulation; nothing existing was touched. The parent Act has its own baseline
(`../../../dust-diseases-tribunal-act-1989/encodings/baseline-2026-11/`), which asks the Regulation's figures as inputs
because the Regulation was not then deposited; the two cannot import each other (different folders).

## Edition

- **Regulation:** Dust Diseases Tribunal Regulation 2019 (2019-405), corpus document
  `nsw_legislation:2022-07-01/sl-2019-0405` (in force 1 July 2022), deposited at
  `../../registers/source-bundle/sl-2019-0405.txt` (text sha256 ae9980...0c832 per its `.meta.json`), taken from the Open
  Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the
  authorised text. Its Editorial note to Sch 1 Part 2 cl 2 carries fee units for 2023-24 and 2024-25, so the text is
  later than the version date suggests (finding 1).
- **Not deposited, asked as facts:** which days are public holidays throughout New South Wales (a borrowed term); the
  Uniform Civil Procedure Rules 2005 and the Tribunal's rules; the Dust Diseases Tribunal (Standard Presumptions --
  Apportionment) Order 2007; the Interpretation Act 1987 (how "within" and "before" periods are counted); Part 4 of the
  repealed 2013 Regulation.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read
(and a deliberately broken copy of the cases file was run once to see that failures are reported).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ddtr-dates.l4` | 0 | 0 | 0 | 0 |
| `ddtr-process.l4` | 0 | 0 | 0 | 0 |
| `ddtr-fees.l4` | 0 | 0 | 0 | 0 |
| `ddtr-offers.l4` | 0 | 0 | 0 | 0 |
| `ddtr-cases.l4` | 0 | 0 | 238 | 238 |

Every expected value was worked by hand from the text, counting business days on a calendar, with the edges: every
base period in the timetable for malignant and non-malignant claims with one and several defendants; each extension
(suspension, cross-claim extension, registrar and mediator deferrals, revoked mediators, objections to an Assessor) and
both caps at the limit and one over; deadlines across 25 December to 9 January, ignored and (by agreement) counted;
weekday public holidays moving a deadline; a notice on the last business day and the next; the further information on
the latest day and the day after; a medical examination notified and held on the last day and a day late; the fee for
every flat Schedule 1 item at the 2022-23 unit and several at the 2023-24 and 2024-25 units, with the rounding of 50
cents down; payment under an accepted offer on day 28 and day 29.

## Seat

**The claimant**: the plaintiff who is or was suffering from the asbestos-related condition, or a person claiming
through them (including a Compensation to Relatives Act 1897 claim); after the plaintiff's death, the authorised
representative (cl 11, 18(2)). In Part 5, "plaintiff includes a cross-claimant" (cl 87), so a claimant's cross-claim is
covered. Every exported question is one that person would ask ("Is my claim malignant?", "Is my claim in the claims
resolution process?", "By what date must this step be done?", "Did I notify the registrar in time?", "Is the
defendant's medical examination in time?", "Can I refuse the defendant more time for cross-claims?", "Must I be at the
mediation?", "Who pays for the mediation?", "How much is the filing fee?", "Is my fee postponed?", "What costs order
follows the rejected offer?", "Can I withdraw my acceptance?"). The Tribunal, the registrar, the mediator and the
Contributions Assessor get no seat: their determinations, satisfaction and discretions are inputs, answered
conditionally. A defendant seat (cross-claims, replies, apportionment, the single claims manager, Division 6, cl 55)
could be added beside this one.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** This is the instrument that sets the Act's numbers
  (s 32H, 32I, 34); its own Schedule 1 fee unit is encoded. Departure: the 2023-24 and 2024-25 fee units come from the
  Editorial note, because the CPI formula was lost from the deposited text (finding 2).
- **The actors the text names.** Followed: the plaintiff, the defendants and cross-defendants, the original defendants,
  the registrar, the mediator, the Contributions Assessor, the authorised representative, the Tribunal.
- **Judgments answered conditionally.** Followed: the Tribunal's satisfaction on urgency (cl 20(2), (3)), "substantial
  prejudice" (cl 25(5), (8)), "reasonable requirement" (cl 26(8)), "not reasonably discoverable" (cl 30(1)(a)),
  "unreasonably left in dispute" (cl 41), "substantial injustice" (cl 42(6)), an "exceptional case" (cl 89, 90) and leave
  (cl 93(1)(b)) are inputs.
- **The text's definitions worked out; borrowed terms asked.** "Asbestos-related condition", "malignant claim",
  "non-malignant claim", "business day" (less public holidays), "authorised representative", "period for acceptance",
  "pro bono party", "pensioner party" and "legally assisted party" are worked out; "public holiday throughout New South
  Wales", "community legal service" and "Commonwealth health concessions" are asked.
- **One case.** One claim, with its defendants.
- **The text's terms with plain glosses.** Followed, in each `@desc`.
- **Operative clauses in; machinery out.** Followed (see Scope).

## Scope

**In:** Part 2: cl 4(1)(b), (1A), 4A, 6, 7, 9, 10(1), (2) (as an answer), Sch 1 Part 1 items 1-8, 13-15, 17, Sch 1 Part 2
cl 2(1)(a), 3 (with the Editorial note). Part 3: cl 11 (definitions, the Christmas period), 13, 14, 16(1)-(3), (5), (6),
17(3), (4), 18(1), (2), 20(1)-(5), 23(5), 25(2)-(5), (7), (8), 26(4), (5), (8), 28(2), 29(1)-(5), 30, 34(1), (2), (6),
(7), 35(1), (3), (4), 36(7), 39(3), 41, 42(1), (4)-(6), (10), 46(2), 49(1), 51(2), 52(7), 52(9), 54(4), (5), 67(3)(g),
100(4). Part 5: cl 87, 88(4)-(6), 89, 90, 91 (in the comparison the person states), 92(1), 93(1), 94(2).

**Out, and why:**
- cl 1, 2, 3, 100(1)-(3), (5)-(7): name, commencement, repeal and spent transitional provisions (100(4) is in).
- cl 4(1)(a), (2), cl 5, cl 8: corporations' fees, the Crown, who pays generally: not the individual claimant's seat.
- Sch 1 items 9-12 and 16 (per-page, per-request and registry-opening fees): left for a later pass; Sch 1 Part 2 cl 1, 4
  (publishing the indexed fees): machinery.
- cl 12, 15, 19: objectives, procedural law, service: no fact the claimant states turns on them.
- cl 17(1), (2): the effect of the process on the Tribunal's own procedure; reflected in the "in the process" question.
- cl 18(3)-(6), 20(6)-(10), 21, 27: suspension of apportionment on death, the Tribunal's own conditions for removal, the
  evidence for urgency, resumption proposals and the joinder of new defendants: Tribunal procedure or defendants'
  machinery; the suspended days are an input to the timetable.
- cl 22, 23(1)-(4), (6), (7), 24: the content and form of the statement of particulars (Form 1) and the timetable: no
  deadline or yes/no answer beyond those encoded. Schedule 2 (the forms) is out.
- cl 25(1), (6), (9)-(13), 26(1)-(3), (6), (7), (9), (10), 28(1), 29(6), 31: the defendants' and cross-defendants' own
  duties.
- cl 32, 33, 34(3)-(5), (8), 35(2), 36(1)-(6), 37, 38, 39(1), (2), (4)-(6), 40, 43-45, 47, 48: the registrar's and
  mediator's functions, the nature of mediation, evidence by audio visual link and outside NSW, mediators' liability,
  privilege and secrecy.
- Division 5 except cl 51(2), 52(7), (9), 54(4), (5); Divisions 6 and 7 (late cross-claims, the single claims manager):
  apportionment among defendants is not the claimant's business, beyond its deadlines and cl 52(9)(a).
- cl 67(1), (2), (3)(a)-(f), (h), 68, 69: the Tribunal's procedure after the process; cl 69 appears only as the
  consequence named in answers.
- Part 4 (subpoenas): the issuing party's and the Tribunal's procedure; a candidate for a later pass.
- cl 86, 88(1)-(3), (7)-(10), 92(2), (3), 93(2), 94(1), (3), 95, 96: the form of offers, the defendant's side, and
  disclosure to the Tribunal.
- Part 6: cl 97 (the practitioner's claims information, Form 3), 98 (costs assessment), 99 (interest to the Treasurer):
  practitioners' and the registrar's duties, machinery.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** cl 13(1) -- `Is my claim in the claims resolution process` -- a claim made by someone not claiming through the
  sufferer: `JUST FALSE` (the heading says "applies only") -- `NOTHING` (a scope limit with no "only" in the clause).
- **F2** cl 16(2), (3) -- `Is my claim in the claims resolution process` -- after the end point, an agreement to extend
  keeps the claim in: `JUST TRUE` -- the extension's own period (not stated in the text) decides.
- **F3** cl 11(1) "public holiday throughout New South Wales" -- every business-day question -- asked as a count of
  weekday public holidays in the period, added to the period -- a holiday calendar from the Public Holidays Act 2010.
- **F4** cl 25(7) "all subsequent time periods" -- `the period in business days for` -- the cross-claim period itself and
  every period ending later than it; not an original defendant's reply (counted from service of the claim) -- every
  period that ends at or after the cross-claim period, or only steps that follow cross-claims in the process.
- **F5** cl 25(4), 34(6) caps -- `How many business days does this step have` -- an extension or deferral above its cap:
  `NOTHING` -- the excess is ignored and the cap applies.
- **F6** cl 34(2)(b) "unless an application for a consent judgment or order has been filed"; cl 26(8) "reasonable
  requirement" -- `Is my notice to the registrar in time`, `Have I given the further information in time` -- the
  "unless" met, or an unreasonable requirement: `NOTHING` -- `JUST TRUE` (no duty, so nothing late).
- **F7** cl 26(8) -- `Have I given the further information in time` -- a requirement made after the latest day:
  `JUST FALSE` -- only the "as soon as practicable" limb applies.
- **F8** cl 29 -- `Is the medical examination requirement in time` -- a cross-defendant: `NOTHING` -- `JUST FALSE` (the
  Note says it needs the Tribunal's leave once the process ends).
- **F9** cl 6(2)(b), 7(2)(b) "judgment is in favour of that party, but costs and damages are not awarded (or only nominal
  damages are awarded)" -- `Is my fee postponed or waived` -- costs without damages, or damages without costs: "unclear"
  -- the fee is not taken unless both are awarded; or only when neither is.
- **F10** cl 88(4) -- `What is the shortest time my offer can be open` -- a claim never in the process: `NOTHING` -- 28
  days (it is always "before the required information exchange").
- **F11** cl 93(1)(a) -- `Can I withdraw my acceptance` -- money paid late, after the 28 days: the right to withdraw has
  arisen -- late payment cures it.
- **F12** cl 11(2) "the time fixed ... for the doing by a party of any act" -- `By when must this step be done` -- the
  Christmas period is ignored for every Part 3 period, including the registrar's referral, the Assessor's determination
  and the conclusion of mediation -- only for acts by a party.
- **F13** cl 26(8), 28(2) "no later than 5 business days before", cl 42(5) "at least 2 business days before" --
  `the latest day` -- the day reached by counting n business days back from the day before the start -- clear days
  (the Interpretation Act 1987 s 36, not deposited).
- **F14** cl 46(2) -- `Can judgment be entered for me on the settlement` -- where the bar does not apply: `NOTHING`
  (cl 46(1) is a power) -- `JUST TRUE`.
- **F15** cl 29(3) -- `Is the medical examination requirement in time` -- once all parties vary the period, the
  examination date is not checked -- the varied period (not an input) is checked.

## Rulings on negatives (recorded word for word, as the guide requires)

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means"
> definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as
> "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may
> not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a
> term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case
> falls outside the limit.

The periods ruling of 2026-11-05 ((a) outside a period the text fixes, `JUST FALSE`; (b) a failed "where", `JUST FALSE`;
(c) a scope limit with no "only", `NOTHING`) and the case-by-case ruling of the same day are followed; each case-by-case
site is a fork line above.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| cl 16(6), 23(5), 34(2) | the plaintiff | duty with a deadline in business days | MUST rule, `Is my notice to the registrar in time` |
| cl 26(8) | the plaintiff | duty, no later than 5 business days before mediation | MUST rule, `Have I given the further information in time` |
| cl 28(2) | the defendant | duty owed to the plaintiff | `By when must the defendant answer my request` |
| cl 29(1), (2) | the original defendant | duty (a condition of requiring an examination) | MUST rule under MUST, `Is the medical examination requirement in time` |
| cl 29(4) | the plaintiff | claim-right to a joint examination | `Can I choose a joint medical examination` |
| cl 25(5), (8) | the plaintiff | deemed consent; disability to refuse without prejudice | `Can I refuse more time for cross-claims`, `May I refuse consent to joining the insurer` |
| cl 17(3) | the plaintiff | liberty to amend without leave | `May I amend my statement of claim without leave` |
| cl 30 | the plaintiff | liberty, limited; contravention for costs | `May I change the facts I rely on` |
| cl 39(3) | the plaintiff | duty to be present | `Must I be present at the mediation` |
| cl 42 | the plaintiff | liability to give evidence; immunity after (6) | two questions |
| cl 49(1) | the defendants | liability for mediation costs | two questions |
| cl 18(2) | the authorised representative | duty to notify | `Must I notify the plaintiff's death` |
| cl 6, 7, 9 | the claimant | liability to fees, postponed or removed | three questions |
| cl 89, 90 | the plaintiff; the defendant | claim-rights to costs orders | `What costs order follows the offer` |
| cl 88(6), 93(1) | the defendant; the accepting plaintiff | duty to pay; power to withdraw | MUST rule with a MAY under LEST, `Can I withdraw my acceptance` |
| cl 94(2) | the plaintiff | power to elect | `What can I do if the defendant does not comply` |

## What the Regulation turns out to say

1. **The text is newer than its version date.** The corpus labels it as in force 1 July 2022, but the Editorial note to
   Sch 1 Part 2 cl 2 gives fee units for 2023-24 ($110.93) and 2024-25 ($115.59), figures that could not be known in
   July 2022. The label should not be read as the date the text was last checked.
2. **The fee-unit formula is lost.** Sch 1 Part 2 cl 2(1)(b) keeps its variables ("A is the CPI number ...", "B is the CPI
   number for the December quarter of 2021", "where--") but the formula itself did not survive conversion. A
   `sl-2019-0405.formulas.md` sidecar, transcribed from the authorised rendering, is needed before later years can be
   computed; they answer `NOTHING`. Asserted.
3. **Fees for 2023-24 and 2024-25 rest on an Editorial note.** cl 3(2) says notes other than those in Schedule 1 are not
   part of the Regulation; the Editorial note sits in Schedule 1 but is the publisher's, not the maker's. The figures are
   what the lost formula produced, so they are used, and labelled. Rounding is to the nearest dollar with 50 cents down
   (Sch 1 Part 2 cl 3): 2.16 fee units at $103.05 is $222.588, so $223. Asserted.
4. **cl 6(2)(b) and 7(2)(b) are unclear where only one of costs and damages is awarded.** "Costs and damages are not
   awarded" can mean neither, or not both. Fork F9; asserted as "unclear".
5. **cl 11(2) speaks only of acts "by a party".** The Christmas period is ignored for "the time fixed ... for the doing by a
   party of any act", yet several Part 3 periods bind the registrar (referral, cl 34(3)), the Contributions Assessor
   (cl 52(7)) or the mediation as a whole (cl 35(1)). The encoding ignores it for all of them (fork F12); a literal reading
   would run those periods through the holidays while the parties' periods stop.
6. **cl 67(2)(a) has no starting point.** The registrar must set the first directions hearing "to take place within 10
   business days for malignant claims or 20 business days for non-malignant claims", without saying after what. Not
   encoded as a date for that reason.
7. **cl 25(7) "all subsequent time periods" is undefined.** A cross-claim extension extends the later periods, but the
   text does not say whether a period that ends on the same day as the cross-claim period (the malignant one-defendant
   medical notice, 10 business days) is "subsequent". Fork F4; asserted not extended.
8. **cl 88(4) is framed on Part 3's stages.** Part 5 applies to all claims (Note to cl 86), but the minimum times for a
   non-asbestos claim, never in the process and never removed under cl 20, fit none of cl 88(4)'s stages except, read
   literally, "before the required information exchange" for ever (28 days). Fork F10.
9. **cl 93(1)(a) survives late payment.** The right to withdraw an acceptance arises if the sum is "not paid ... within 28
   days"; the text does not say a later payment ends it. Fork F11; asserted.
10. **cl 52(9)(a) frees only the plaintiff.** The bar on challenging a Contributions Assessor's determination "is not
    binding on the plaintiff"; the determination binds the defendants for the plaintiff's settlement and judgment
    (cl 55(1)). Asserted.
11. **The medical examination periods are a defendant's limits, not the plaintiff's duty.** cl 29 never says the plaintiff
    must attend; it limits when an original defendant may notify and hold one. The question is framed that way.

## Questions (exported)

`ddtr-process.l4` (24), in the Regulation's order: `Is my claim malignant or non-malignant`, `Is my claim in the claims
resolution process`, `Is my claim urgent`, `How many business days does this step have`, `By when must this step be
done`, `Is my notice to the registrar in time`, `Have I given the further information in time`, `By when must the
defendant answer my request`, `Is the medical examination requirement in time`, `Can I choose a joint medical
examination`, `Can I refuse more time for cross-claims`, `May I refuse consent to joining the insurer`, `May I amend my
statement of claim without leave`, `May I change the facts I rely on`, `Must I be present at the mediation`, `Can I be
made to give evidence to the mediator`, `Can I be required to give evidence again`, `Can judgment be entered for me on
the settlement`, `Who pays for the mediation`, `What does each defendant pay for the mediation`, `Am I bound by the bar
on challenging the Assessor`, `Could I pay indemnity costs for leaving it in dispute`, `Can the Tribunal require me to
file an affidavit`, `Must I notify the plaintiff's death`.

`ddtr-fees.l4` (4): `How much is this Tribunal fee`, `Is my fee postponed or waived`, `Who pays the first directions
hearing fee`, `When does the first directions hearing fee become payable`.

`ddtr-offers.l4` (5): `What is the shortest time my offer can be open`, `Until when can the offer be accepted`, `What
costs order follows the offer`, `Can I withdraw my acceptance`, `What can I do if the defendant does not comply`.

## Before relying on it

- Replace the corpus text with the current official text and re-check every quotation, period and fee.
- Transcribe the Sch 1 Part 2 cl 2(1)(b) formula into a formulas sidecar and compute the fee unit for later years.
- Decide forks F4, F9, F11 and F12 with a lawyer; settle how "within" and "before" periods are counted (Interpretation
  Act 1987 s 36) and replace the public-holiday count with a calendar.
- Add a defendant seat (cross-claims, replies, apportionment, the single claims manager, Division 6, cl 55) and Part 4
  (subpoenas).
- Link the parent Act's baseline (its regulation-dependent inputs) to these answers in a cross-encoding register.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
