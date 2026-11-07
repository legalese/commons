# Work Health and Safety Act 2011 (NSW) -- baseline encoding, the worker

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 2 March 2025). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (the business's written
notice within 48 hours, s 38(4)(b); the regulator's answer within 3 months, s 231(2)), each run by `EVALTRACE` inside an
exported question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No
pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is the provisions a person bringing or
answering a claim meets. The Act is large (Parts 1-14, about 320,000 characters); the Parts a worker meets after harm,
risk or reprisal are encoded and the rest is listed under Scope with reasons.

## Edition

- **Act:** Work Health and Safety Act 2011 No 10, corpus document `nsw_legislation:2025-03-02/act-2011-010` (in force
  2 March 2025), deposited at `../../registers/source-bundle/act-2011-010.txt` (sha256 1e6dd34a...d76e8175 as committed,
  as its meta records), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited:** the Work Health and Safety Regulation 2017 (prescribed injuries and incidents, s 36, s 37;
  "prescribed purposes", s 88; prescribed classes of worker, s 7(1)(i)); the CPI figures behind s 242B; the Work
  Health and Safety (Mines and Petroleum Sites) Act 2013 (ss 38(8), 39(4)). What they decide is asked as a fact, or
  answered `NOTHING`.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `whs-dates.l4` | 0 | 0 | 0 | 0 |
| `whs-claims.l4` | 0 | 0 | 0 | 0 |
| `whs-cases.l4` | 0 | 0 | 198 | 198 |

Every expected value was worked by hand from the text, with the edges: the 48th hour after exposure to a substance and
48.5 hours (s 36(c)); the 48th and 49th hour for the written notice (s 38(4)(b)); a record kept from 29 February
(s 38(7)); the last day of the one-year period and the day after, from 29 February (s 113(1)); the day the six months end
and the day after, the last day of 18 months and the day after, from 31 August (s 231(1)); the last day of the
regulator's three months from 30 November, and the day after (s 231(2)); each limb of s 232(1) winning in turn; every
penalty in dollars at each deposited penalty-unit value, rounded down, with the Local Court cap just under and just over
(1,206 against 1,200 units); years with no deposited unit value.

## Seat

**The worker** (s 7): the person who carries out work for a business or undertaking and is hurt, exposed to risk, or
treated adversely for raising safety; with them the prospective worker and the person in a commercial arrangement whom
Part 6 protects, and any person (often the injured worker, or the family of a worker who died) who asks the regulator to
prosecute under s 231. Every exported question is one that person would ask ("Am I a worker?", "Was my injury a serious
injury?", "Must my employer tell the regulator?", "Must the site be left alone?", "May I stop unsafe work?", "Can I take
them to the Industrial Court for punishing me for raising safety, and by when?", "What can the court order?", "What
offence was it, and what is the most they can be fined?", "Can I ask for a prosecution, and must the regulator answer
me?", "Can I sue under this Act?", "Can they charge me for safety gear?").

The business (the person conducting the business or undertaking) is the other party the Act puts duties on; a
business seat could be added beside this one, drawing on the same rules. Officials (the regulator, inspectors, the
Director of Public Prosecutions, the courts) get no seat: what they must do is encoded as what the worker is owed and by
when (ss 231(2)-(4)).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets its own penalties; the penalty
  unit values to 2024-25 are taken from the editorial note in the deposited text (fork F9). The Regulation is not
  deposited; its effects are asked.
- **The actors the text names.** Followed: the person conducting a business or undertaking, the officer, the worker,
  the health and safety representative, the regulator, the inspector, the Director of Public Prosecutions, the
  Industrial Court, the Local Court, the secretary of an industrial organisation of employees.
- **Judgments answered conditionally.** Followed: a reasonable concern (s 84), the treatment an injury "required"
  (s 36), a serious risk (s 37), gross negligence, recklessness and reasonable excuse (ss 31, 34C), a substantial reason
  and the reasonableness defence (ss 112(4), 113), unreasonable failure to do alternative work (s 88), fresh evidence
  (s 232(2)) are inputs, phrased "if the court finds".
- **The Act's definitions worked out; borrowed terms asked.** Followed: worker (s 7), person conducting a business or
  undertaking (s 5), notifiable incident (s 35), serious injury or illness (s 36), dangerous incident (s 37),
  discriminatory conduct (s 105), prohibited reason (s 106) are worked out; "officer" (Corporations Act s 9), "union",
  "employee" and "body corporate" are asked.
- **One case.** One incident, one worker, one course of conduct.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 5 (business or undertaking); s 7 (worker); ss 30-34, 34B-34F (offences, industrial manslaughter, volunteers,
unincorporated associations, no limitation for industrial manslaughter); ss 35-39 (notifiable incidents; notice; the
48-hour written notice; the five-year record; preserving the site); ss 83-88 (stopping unsafe work, the
representative's direction, the worker's duty after stopping, continuity of engagement); ss 104-115 (discriminatory
conduct, prohibited reasons, coercion, misrepresentation, the s 111 orders on conviction, the s 112 civil application,
the one-year limit, the presumption and the defence in s 113, ss 114 and 115); s 229B (which court; the Local Court cap);
s 230 (who may prosecute); s 231 (asking the regulator to prosecute; the regulator's and the DPP's deadlines); s 232
(limitation for prosecutions); ss 242A-242C (penalty units); s 267 (civil liability); s 272 (no contracting out); s 273
(no levy on workers).

**Out, and why:**
- **Part 2 Divisions 1-4 (ss 13-29), the duties themselves.** Whether a duty was owed and breached ("so far as is
  reasonably practicable", s 18) is the court's finding, taken as an input to the offence question. Encoding the content
  of each duty would be a separate, larger encoding.
- **s 34A (police responding to an armed offender):** a narrow exception for police, not met by a claimant.
- **s 110 (proof in a prosecution for discriminatory conduct):** quoted in comments; the prosecution's burden, not a
  question the worker answers. The worker's own route is the civil application (Division 3), encoded.
- **Part 4 (authorisations), Part 5 Divisions 1-5 and 7-8 (consultation, representatives, committees, issue resolution,
  provisional improvement notices):** the representation machinery, not the claim.
- **Part 7 (entry permits), Parts 8-11 (the regulator, inspectors, notices, enforceable undertakings):** the regulator's
  machinery. An undertaking's contravention enters only through s 232(1)(c).
- **Part 12 (review of decisions):** the reviewable decisions (s 223 table) concern representation, notices and permits,
  not a claim for harm.
- **Part 13 Divisions 2-7 (sentencing orders, penalty notices, bodies corporate, the Crown, public authorities, civil
  penalties):** orders and attribution for the court and the regulator; civil penalty proceedings are brought by the
  regulator or an inspector (s 260), not the worker.
- **ss 268-271F, 272A-273B, 274-276C, Schedules:** information, privilege, immunity, dust disease and silica registers,
  insurance against penalties, codes of practice, regulation-making, savings and transitional: machinery or not met by
  the claimant.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 38(7), 113(1), 231(1)-(4), 232(1) -- `plus months`, `plus years` and every date question -- a period of
  months or years "after" a day ends on the same day of the month that many months later, or that month's last day where
  shorter (29 February plus a year is 28 February); the day it runs from is not counted -- the Interpretation Act 1987
  (not deposited) might give another last day in a short month.
- **F2** s 7(1) "in any capacity ... including" -- `Am I a worker` -- any work for a business or undertaking counts, so
  the listed capacities and prescribed classes are not asked one by one -- ask each capacity, to show the list.
- **F3** s 5 -- `Is the one I work for a person conducting a business or undertaking` -- "business or undertaking" is not
  defined; where there is none, `NOTHING` -- `JUST FALSE`, reading s 5 as a definition.
- **F4** s 36 "requiring the person to have" -- `Is my injury or illness a serious injury or illness`,
  `Must the business notify the regulator` -- the treatment the injury required is asked, not the treatment given; the
  48th hour after exposure is "within 48 hours" -- "within 48 hours" ends before the 48th hour.
- **F5** s 38(4)(b) "within 48 hours of that requirement being made" -- the 48-hour rule -- counted in hours from the
  requirement; a notice in the 48th hour is in time -- counted to the end of the second day.
- **F6** s 39 -- `Must the site be left undisturbed` -- whether a notifiable incident occurred is asked as a fact (the
  notification question works it out); "so far as is reasonably practicable" qualifies the duty and is not asked; an
  action s 39(3) "does not prevent" answers `JUST FALSE` -- work out the notifiable incident here too.
- **F7** s 112(6) "each of the following is an eligible person" -- `Can I apply to the Industrial Court` -- the list is
  not closed with "only", so anyone else answers `NOTHING` -- the list is exhaustive (`JUST FALSE`).
- **F8** s 115(b) "cannot ... recover any compensation under Division 3" -- `What orders can the Industrial Court make
  for me` -- the compensation order is taken off the list -- the order may be made but not recovered.
- **F9** s 242B -- `the value of a penalty unit in the financial year starting` -- the formula of s 242B(1)(b) is lost in
  the deposited text; the editorial note's amounts to 2024-25 are used, and other years answer `NOTHING` -- compute later
  years from published CPI figures (not deposited).
- **F10** s 34C maximum penalty "(a) for an individual -- imprisonment for 25 years" -- `What is the most the offender
  can be fined` -- no fine for an individual: `NOTHING` -- a fine under general sentencing law (outside the Act).
- **F11** s 231(1)(b) "after 6 months but not later than 18 months after that occurrence" -- `From what day can I ask the
  regulator to prosecute`, `Can I ask the regulator to prosecute` -- the window opens the day after the six months end
  and closes at the end of the last day of 18 months -- it opens on the six-month day itself.
- **F12** s 231(4) "advise ... the regulator within 1 month" -- `By what day must the DPP advise the regulator` -- the
  month runs from the referral -- from the regulator's receipt of the person's request for a referral.
- **F13** s 84 "A worker may cease" -- `May I cease unsafe work` -- someone not a worker answers `NOTHING` (a scope limit
  without "only"); a representative's direction given without the training (s 85(6)) or without consulting when
  consulting was reasonable (s 85(2), (3)) answers `JUST FALSE` -- the worker may still rely on a defective direction
  given in good faith.
- **F14** s 106(h) -- `Is it taken to be for a prohibited reason` -- a concern raised with someone outside the (h) list is
  not offered and counts as "none of these reasons" (`JUST FALSE`) -- `NOTHING`.
- **F15** s 112 -- `Can I apply to the Industrial Court` -- conduct outside s 112(2) answers `NOTHING` (the Act does not
  bar the application, it gives no order) -- `JUST FALSE`.
- **F16** s 113(3) -- `Does the person who acted have the section 113(3) defence` -- for coercion (s 112(2)(c)) the
  subsection does not speak: `NOTHING` -- `JUST FALSE` ("this section gives no defence").
- **F17** ss 31, 34C -- `Which offence was it` -- Category 1 needs conduct exposing someone to the risk, not a failure to
  comply with the duty; industrial manslaughter needs a failure that caused a death -- Category 1 also needs a failure.
- **F18** s 230(1)(c), (3) -- `Can my union bring the prosecution` -- industrial manslaughter is not a Category 1 or 2
  offence, so the secretary is not limited by s 230(3) (`JUST TRUE`) -- s 230(3) is read to cover it too (finding 5).
- **F19** s 232(2) -- `By what day must a prosecution be brought` -- fresh evidence matters only once the ordinary
  period has ended; before that, the ordinary last day is given -- always report that the period may be extended.
- **F20** s 229B(4) -- `What is the most the offender can be fined` -- the Local Court cap applies to every offence,
  industrial manslaughter by a body corporate included -- the cap does not reach a penalty fixed in dollars (finding 4).

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 38(1) | the business | duty: notify immediately | `Must the business notify the regulator` |
| s 38(4)(b) | the business | duty with a deadline (48 hours) | MUST rule, WITHIN 48 |
| s 38(7) | the business | duty: keep the record 5 years | `Until what day must the business keep the record of my incident` |
| s 39(1) | the person with management or control | duty until the inspector arrives | `Must the site be left undisturbed` |
| s 84 | the worker | privilege to cease work | `May I cease unsafe work` |
| s 86 | the worker | duty to notify and remain available | `What must I do after I cease work` |
| s 88 | the worker | immunity: continuity unaffected | `Does section 88 protect the continuity of my engagement` |
| ss 104, 107, 108, 109 | anyone | duty not to | `Is it discriminatory conduct`, `Did they break the prohibition on misrepresentation` |
| s 112(1) | the eligible person | power to apply | `Can I apply to the Industrial Court` |
| s 113(1) | the eligible person | disability after one year | `By what day must I apply to the Industrial Court` |
| s 115 | the person | disability: no second claim | `Can I apply to the Industrial Court` |
| s 231(1) | any person | power to request a prosecution | `Can I ask the regulator to prosecute` |
| s 231(2) | the regulator | duty with a deadline (3 months) | MUST rule |
| s 231(3)(b), (4) | the regulator; the DPP | duties with deadlines (1 month) | date questions |
| s 267 | everyone | no right of action conferred | `Does this Act give me a right to sue for the breach` |
| s 272 | the parties | disability: term void | `Is this term of my contract void` |
| s 273 | the business | duty not to levy | `Can the business charge me for health and safety` |

## What the Act turns out to say

1. **The Act gives an injured worker no claim for damages.** s 267 says nothing in the Act confers a civil right of action
   for a contravention, except Part 6 (and the regulator's civil penalty proceedings). The worker's own civil route under
   this Act is the Industrial Court application for discriminatory or coercive conduct; damages for injury lie in
   negligence and the workers compensation Acts (separate subjects). Asserted.
2. **The penalty unit formula is missing from the deposited text.** s 242B(1)(b) says "the amount calculated as follows"
   and then gives only the definitions of A and B; the formula was lost in conversion. The editorial note's table, headed
   "Fee unit amount" although the section is about penalty units, gives the values to 2024-25. Values from 2025-26 are not
   in the text (fork F9). Asserted (`NOTHING` for 2025 and 2018).
3. **Two different standards of reason.** The offence needs the prohibited reason to be "the dominant reason"
   (s 104(2)), presumed unless the accused proves otherwise (s 110(2)); the civil application needs only "a substantial
   reason" (s 112(4)), likewise presumed (s 113(2)). The civil route is the easier one for the worker. Asserted for the
   civil route.
4. **The Local Court cap reaches the most serious offences.** s 229B(4) caps a Local Court fine at 1,200 penalty units
   "despite any higher maximum" ($144,504 in 2024-25), and s 229B(3A) sends industrial manslaughter and Category 1 offences
   by a body corporate to summary hearing unless the prosecutor elects indictment. On the words, a body corporate's
   industrial manslaughter heard summarily in the Local Court is capped at under 1% of the $20,000,000 maximum; the
   Industrial Court (also summary) has no such cap. Asserted (fork F20).
5. **Union prosecutions of industrial manslaughter.** s 230(3) restricts a union secretary only for Category 1 and
   Category 2 offences. Industrial manslaughter (s 34C, added 2024) is neither, so on the words a secretary may bring it
   directly, although an individual's industrial manslaughter must be tried on indictment (s 229B(2)). Possibly a gap left
   when Part 2A was added. Asserted (fork F18).
6. **The request window and the limitation period do not line up.** A person may ask the regulator to prosecute only
   between six and 18 months after the occurrence (s 231(1)), but the limitation period runs two years from when the
   regulator learns of the offence (s 232(1)(a)), and longer after an inquest. After 18 months the Act gives no request.
   Asserted.
7. **s 231(4) gives the DPP "1 month" without saying from when.** Read as from the referral (fork F12).
8. **s 115(c) carves out only failure in workers compensation.** A pending workers compensation claim still bars a
   Part 6 application under s 115(a) if it is "in relation to the same matter"; whether a compensation claim for an injury
   is the same matter as a reprisal for raising safety is left open (asked as a fact).
9. **Industrial manslaughter has no fine for an individual.** s 34C(a) sets imprisonment for 25 years only (fork F10).

## Questions (exported)

`whs-claims.l4` (34), in the Act's order: `Am I a worker` (s 7); `Is the one I work for a person conducting a business or
undertaking` (s 5); `Is my injury or illness a serious injury or illness` (s 36); `Was it a dangerous incident` (s 37);
`Must the business notify the regulator` (ss 35-38); `Was the written notice of my incident given in time` (s 38(4)(b),
MUST rule); `Until what day must the business keep the record of my incident` (s 38(7)); `Must the site be left
undisturbed` (s 39); `May I cease unsafe work` (ss 84, 85); `What must I do after I cease work` (s 86); `Does section 88
protect the continuity of my engagement` (s 88); `Is it discriminatory conduct` (s 105); `Is it taken to be for a
prohibited reason` (ss 106, 112(4), 113(2)); `By what day must I apply to the Industrial Court` (s 113(1)); `Can I apply
to the Industrial Court` (ss 112, 113(1), 115); `Does the person who acted have the section 113(3) defence`; `What orders
can the Industrial Court make for me` (ss 112(3), 114(3), 115(b)); `What orders can the criminal court make for me`
(ss 111, 114(2)); `Did they break the prohibition on misrepresentation` (s 109); `Which offence was it` (ss 31-34, 34C,
34D); `What is the most the offender can be fined` (penalties, ss 229B(4), 242B, 242C); `What is the longest prison
term` (ss 31, 34C); `Which court deals with the prosecution` (s 229B); `Can my union bring the prosecution` (s 230);
`From what day can I ask the regulator to prosecute`, `What is the last day I can ask the regulator to prosecute`, `Can
I ask the regulator to prosecute` (s 231(1)); `Has the regulator answered my request in time` (s 231(2), MUST rule);
`By what day must the regulator refer my matter to the DPP` (s 231(3)(b)); `By what day must the DPP advise the
regulator` (s 231(4)); `By what day must a prosecution be brought` (ss 232, 34E); `Does this Act give me a right to sue
for the breach` (s 267); `Is this term of my contract void` (s 272); `Can the business charge me for health and safety`
(s 273).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation,
  the penalties (indexed each 1 July) and the penalty unit values (finding 2).
- Deposit the Work Health and Safety Regulation 2017 for the prescribed injuries, incidents and purposes.
- Have a lawyer review the forks, especially F7 (eligible persons), F8 (s 115(b)), F11 (the request window), F18
  (union prosecutions of industrial manslaughter) and F20 (the Local Court cap).
- Link the encoding to the workers compensation baselines for the injured worker's compensation and damages.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
