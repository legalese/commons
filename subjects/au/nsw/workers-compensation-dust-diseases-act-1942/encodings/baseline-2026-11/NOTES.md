# Workers' Compensation (Dust Diseases) Act 1942 (NSW) -- baseline encoding, the claimant

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 18 October 2022). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Three regulative rules (the Authority's two
working days, s 8(1A); the claimant's seven days to report other compensation, s 8AA(3); the six months to appeal,
s 8I(1A)), each run by `EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no
`#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human
gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Workers' Compensation (Dust Diseases) Act 1942 No 14, corpus document `nsw_legislation:2022-10-18/act-1942-014`
  (in force 18 October 2022), deposited at `../../registers/source-bundle/act-1942-014.txt` (text sha256 df014d27...3f0ec0
  per its `.meta.json`), taken from the Open Australian Legal Corpus (collected 10 March 2025) because
  legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Not deposited here, asked as facts:** the Workers Compensation Act 1987 (the "Principal Act": the weekly, death and
  medical benefit figures, the s 26 funeral maximum, the Div 6 indexation notices) and the 1998 Act (notice and claim
  time limits) are separate subjects and cannot be imported across folders; the Workers' Compensation (Dust Diseases)
  Regulation (dust occupations, examinations) is not deposited; the commencement dates of the 1998 and 2010 amending Acts
  are not in the text.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `wcdd-dates.l4` | 0 | 0 | 0 | 0 |
| `wcdd-claims.l4` | 0 | 0 | 0 | 0 |
| `wcdd-cases.l4` | 0 | 0 | 170 | 170 |

Every expected value was worked by hand from the text, with the edges: the two working days from a Thursday, a Friday, a
Saturday, a Sunday and across New Year; a decision on the last working day and the day after, and before the trigger;
the seventh day and the eighth (s 8AA(3)), across a year end; six months from 31 August into a common and a leap
February, and the last day and the day after (s 8I); a child the day before and on the 16th and 21st birthdays, and a
29 February birthday; the lump sum in each of the four periods, partial percentages of 0, 40, 100 and 101; funeral
expenses at, under and one dollar over the cap; redemption at the cap and one dollar under; s 8(6)(b) and (c) at,
under and one dollar over; backdating to exactly 29 February 1968, the day before, and to the date of disablement.

## Seat

**The claimant**: the worker disabled by a dust disease, or the dependant (surviving spouse, child or other relative)
of a worker who died, claiming from the Workers Compensation (Dust Diseases) Authority. Every exported question is one
that person would ask ("Is my disease a dust disease?", "Am I entitled to an award?", "Are we entitled after the
death?", "By when must the Authority decide?", "How much is the lump sum?", "Is the payment for my child still
payable?", "By when must I tell the Authority about other compensation?", "By when must I appeal?"). The Authority, the
Medical Assessment Panel, the Dust Diseases Board and the District Court get no seat: their certificates, findings,
opinions and discretions are inputs, answered conditionally. A third-party defendant seat (s 8E and Sch 1A) could be
added.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed as far as deposited: the Act's own figures
  (s 8(2B)) are encoded; the Principal Act's figures, the indexed amounts and the s 26 maximum are inputs.
- **The actors the text names.** Followed: the Authority, the Medical Assessment Panel, the worker, the dependants, the
  surviving spouse, the prescribed relative, the child, the District Court.
- **Judgments answered conditionally.** Followed: the panel's certificates, the Authority's findings and opinions
  (ss 8(1), (3A), (3B), (6A)), reasonableness (ss 8(2A), 9A), best interests (s 8(2E)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** "Dust disease", "spouse", "prescribed relative",
  "prescribed engagement" and the mine exclusion from "worker" are worked out; "worker", "dependant", "de facto
  partner" and "total cash earnings" are asked.
- **One case.** One claimant, one disease, one death.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (dust disease, worker, spouse); Sch 1; s 8(1) (worker; dependants under (b) and (c), with the proviso);
s 8(1A), (1AA); s 8(2)(c)(ii); s 8(2A); s 8(2B)(a)-(e) with (9) and Sch 2 cll 13, 14; s 8(2D)(b); s 8(2E); s 8(3A);
s 8(3B); s 8(6)(a)-(c); s 8(6A); s 8(7), (8); s 8AA(1)-(3), (5) (in a comment); s 8B(2); s 8I(1), (1A); s 9A; s 11;
Sch 2 cll 20, 21.

**Out, and why:**
- ss 1, 2, 12, 13, Sch 1B, Sch 2 Parts 1-5, 7 (name, commencement, repeals, the chief executive, spent transitional
  provisions; Broken Hill and Silicosis-scheme legacy recipients under s 2(5), s 9 and Sch 2 cl 4): machinery or spent.
- ss 5-7 (the Authority, the Board, the Fund, insurers' contributions, the panel's constitution): machinery; s 7(5)
  (certificate conclusive subject to appeal) is reflected by taking certificates as inputs.
- s 8(2) (a), (b), (d) and s 8(3): the rates are the Principal Act's (Part 3 Divs 1-3, 6 and Sch 6), a separate subject;
  only the figures this Act states are encoded. s 8(2C) (orders on pre-1967 awards) and s 8(2F), (2G) (the 1989 and
  1992 amendments): transitional; (2G) is a finding.
- s 8(4) (notice and claims follow the Principal Act and 1998 Act, made to the Authority): the time limits are in the
  1998 Act, not here; noted in the export descriptions.
- s 8(5A), s 8A (reduction to qualify for a pension, at the Authority's instance), s 8AA(4) (the Authority's order to
  pursue other compensation), s 8B(1), (3), s 8C, s 8D: discretionary powers whose outcome is the Authority's order; no
  fact the claimant states settles them.
- s 8E and Sch 1A: the third party's duties to reimburse and notify the Authority; not the claimant's (a defendant seat
  could add them). s 8G (prosecutions), s 10 (regulations): machinery.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3 "Dust disease means any disease specified in Schedule 1, and includes ..." -- `Is my disease a dust
  disease` -- a "means" definition widened by "includes": a disease outside both is `JUST FALSE` -- "includes" opens the
  list, `NOTHING`.
- **F2** s 8(1)(c) -- `Am I entitled as a dependant after the death` -- the worker-time finding in (c)(ii)(b) does not
  attach to (c)(i) (a person already receiving payments) -- it attaches to both.
- **F3** s 8(2B)(a)(i) "a prescribed relative ... and no other person" -- `Does section 8(2B) apply` -- two or more
  relatives under s 8(9)(b)(ii) with no spouse answer `NOTHING` -- one relative only (`JUST FALSE`), or each of several.
- **F4** s 8(6)(c) -- `By how much is my other weekly compensation reduced` -- the reduction cannot exceed the other Act's
  weekly payment -- the full difference, leaving a negative.
- **F5** s 8(8) "shall not ... determine a date earlier than" -- `From what day are my weekly payments payable` -- a date
  determined in breach answers `NOTHING` -- the floor date, or the application date.
- **F6** s 8(2B)(b)(iii) "in the case of a surviving spouse" -- `Is the weekly payment for this child payable` -- with no
  surviving spouse, `JUST FALSE` (s 8(2AA) sends children alone to the ordinary rates) -- `NOTHING`.
- **F7** s 8(1A) "within 2 working days" -- `By when must the Authority decide my claim` -- Monday to Friday, public
  holidays not skipped (no list deposited; 1 January 2027 counted, asserted) -- public holidays skipped under the
  Interpretation Act 1987 (not deposited).
- **F8** s 8I(1A) "within 6 months after notice" -- `By when must I appeal` -- the same day of the month six months on,
  or the month's last day where shorter -- the Interpretation Act's counting (not deposited).
- **F9** s 8(2B)(ba) "attained ... the age" -- `the age on`, child payment -- an age is attained on the anniversary; a
  29 February birthday on 1 March in a common year -- on 28 February.
- **F10** s 8(2B)(b) refers to "the dependent person referred to in paragraph (a)(i)" -- `What is the most my section
  8(2B) lump sum can be` -- the surviving spouse under (a)(ii) is read as that person too (a spouse is always a
  prescribed relative), so the lump sum is paid where there are children too -- the lump sum only where (a)(i) applies
  alone.
- **F11** s 9A, s 8I(1), s 11 -- the questions answer `NOTHING` where the asker is outside the provision (no required
  examination; not an affected person; no prior entitlement) -- `JUST FALSE`.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 8(1)(a)-(c) | the worker; the dependants | right to an award, on the panel's certificate and the Authority's finding | `Am I entitled ...` |
| s 8(1A), (1AA) | the Authority | duty with a deadline, with no invalidity | MUST rule, WITHIN 2 working days |
| s 8(2B), (2E) | the spouse, relative, child | right to fixed sums; the Authority's power to redeem, capped | `What is the most ...` |
| s 8(3B), (6A) | the Authority | power (may); duty to reduce (shall) | conditional questions |
| s 8(6)(a), 8AA(2) | the claimant | disability: no double compensation | `JUST FALSE` / barred |
| s 8AA(3) | the claimant | duty with a deadline; offence, 1 penalty unit | MUST rule, WITHIN 7 |
| s 8AA(5) | the claimant | immunity from repayment | comment |
| s 8I(1), (1A) | the affected person | power to appeal, lapsing after six months | DO rule (a condition, not a duty) |
| s 9A | the worker | right to reimbursement | `Can I be reimbursed ...` |

## What the Act turns out to say

1. **The Act sets almost none of its own rates.** Weekly, death and medical benefits are the Principal Act's, applied
   "with such modifications as may be necessary"; a claimant cannot get a figure from this Act alone except the
   s 8(2B) sums.
2. **The weekly figures in s 8(2B)(b)(ii), (iii) are stale.** The text says $137.30 and $69.40, but s 8(2G) says that
   from 1 July 1992 they are "taken to be" $141.40 and $71.50. The printed figures are older than a deeming 30 years
   old, and both are adjusted by notice under s 8(3)(d). The encoding answers whether the weekly payments are payable,
   not how much.
3. **The lump sum's periods hang on a date the text does not give.** s 8(2B)(b)(i) counts from "the commencement of" the
   2010 amending Act, which the consolidated text does not state; the claimant is asked which period the death fell in.
4. **Two working days is very short and has no consequence.** s 8(1A) sets it, and s 8(1AA) says a late decision is not
   invalid. The rule's `LEST BREACH` marks the lateness; the Act gives the claimant nothing for it.
5. **s 8(1)(c) shifts the attribution finding to the panel.** In (a) and (b) the Authority finds part-time attribution
   "on the report" of the panel; in (c)(ii)(b) the panel "further certifies" it. Taken as one input (fork F2).
6. **"A prescribed relative" is singular.** Where two parents (or siblings) depended on a worker with no spouse,
   s 8(2B)(a) may not apply at all. Fork F3; asserted `NOTHING`.
7. **s 8(2B)(b) names only the (a)(i) person**, yet (b)(iii) pays for children "in the case of a surviving spouse",
   which only arises under (a)(ii). Fork F10.
8. **s 8AA(3) runs from receipt "or" notification.** Read as whichever comes first; a person notified, then paid, has
   one seven-day period, not two.
9. **The notice and claim time limits are elsewhere.** s 8(4) borrows them from the Principal Act and 1998 Act; a
   claimant reading this Act alone learns only to send them to the Authority.

## Questions (exported)

`wcdd-claims.l4` (33), in the Act's order: `Is my disease a dust disease`, `Am I a worker under the Act`, `Am I the
worker's spouse under the Act`, `Am I entitled to an award for my disablement`, `Am I entitled as a dependant after the
death`, `By when must the Authority decide my claim`, `Was my claim decided in time`, `How much of the death benefit is
payable for a partial disablement`, `How much of the funeral expenses will be paid`, `Does section 8(2B) apply`, `What is
the most my section 8(2B) lump sum can be`, `Is the weekly spouse payment payable to me`, `Is the weekly payment for this
child payable`, `Who is paid for the child's weekly payment`, `What is the most a redemption lump sum can be`, `When is
my injury taken to have happened`, `Will my partial disablement be treated as total`, `Must the rate be reduced for
exposure outside worker time`, `Can I also claim under the 1987 Act for the same disablement`, `How much can still be
paid under the other Act for the death`, `By how much is my other weekly compensation reduced`, `Is my 1987 Act
entitlement extinguished`, `What is the earliest day my weekly payments can be backdated to`, `From what day are my
weekly payments payable`, `Am I barred because I was compensated elsewhere`, `By when must I tell the Authority about
other compensation`, `Have I told the Authority in time`, `How much is still payable after the interim award`, `By when
must I appeal`, `Can I appeal on that day`, `Can I be reimbursed for this examination cost`, `Do the partial incapacity
weekly payments extend to me though retired`, `Which wage figure sets my weekly payments`.

## Before relying on it

- Replace the corpus text with the current official text and re-check every quotation and figure (finding 2).
- Deposit the indexation notices and the 2010 Act's commencement date (findings 2, 3).
- Link to the Workers Compensation Act 1987, the 1998 Act and the Dust Diseases Tribunal Act 1989 encodings.
- Have a lawyer review forks F2, F3 and F10.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
