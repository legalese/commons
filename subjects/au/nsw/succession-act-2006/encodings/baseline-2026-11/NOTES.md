# Succession Act 2006 (NSW), Chapter 3 -- baseline encoding, the person seeking family provision

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 14 July 2023). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). One regulative rule (the applicant's
12 months to file, s 58(2)), run by `EVALTRACE` inside exported questions that take only plain facts. No REFUSE, no
`#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no
human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. It covers Chapter 3 (family provision and notional
estate) whole, ss 55 to 100, with the Chapter 1 definitions Chapter 3 uses and the Schedule 1 Part 3 transitional rule.
Chapters 2 (wills) and 4 (intestacy) are left for other encodings (see Scope).

## Edition

- **Act:** Succession Act 2006 No 80, corpus document `nsw_legislation:2023-07-14/act-2006-080` (in force 14 July
  2023), deposited at `../../registers/source-bundle/act-2006-080.txt` (text sha256 9f828f5f...c559d), taken from the Open
  Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the
  authorised text.
- **Not deposited:** the Succession Regulation (s 98(4) mediation and advertising rules, s 99(2) maximum costs); the
  Interpretation Act 1987 s 21C (de facto relationship); the Property (Relationships) Act 1984 (domestic relationship);
  the Status of Children Act 1996 (presumptions of parentage); the Children and Young Persons (Care and Protection) Act
  1998 (parental responsibility); the Probate and Administration Act 1898 (s 55 grants); the Civil Procedure Act 2005
  and Uniform Civil Procedure Rules 2005 (forms, signing). What they decide is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `sfp-dates.l4` | 0 | 0 | 0 | 0 |
| `sfp-claims.l4` | 0 | 0 | 0 | 0 |
| `sfp-cases.l4` | 0 | 0 | 155 | 155 |

Every expected value was worked by hand from the text, with the edges: the last day of the 12 months, the day after,
the day of death, and a death on 29 February (s 58); the first day of the three-year and one-year windows and the day
before each, with a 29 February death (s 80(2)); a transaction taking effect on the day of death and the day after;
six months exactly and a day short, a 29-day and a 30-day notice period, distribution on the specified day and the day
after, and the day before and on the twelve months (ss 93, 94(4)); designation equal to, nil, and one dollar over the
estate (s 89(2)); each head of s 57 and each s 3(4) exclusion; each limb of s 59(3), (4).

## Seat

**The applicant**, or would-be applicant, for a family provision order: the spouse, de facto partner, child, former
spouse, dependant (grandchild or household member) or close personal companion of the person who died. Every exported
question is one that person would ask ("Am I eligible?", "By when must I apply?", "Can the Court make an order for
me?", "Can it reach this property?", "Can this gift, joint tenancy or super benefit be brought back?", "Is the executor
protected if they distribute before I claim?", "Does my release bind me?"). The legal representative (executor or
administrator) and the beneficiaries who would lose property to an order or a notional estate order carry duties and
exposure under the Chapter; a beneficiary or holder seat could be added beside this one. The Court gets no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Chapter sets its own periods (12 months,
  6 months, 30 days, 3 years, 1 year); the Succession Regulation (maximum costs, mediation) is not deposited and is
  out.
- **The actors the text names.** Followed: the eligible person, the deceased person, the legal representative, the
  beneficiary, the transferee and deceased transferee, the Court.
- **Judgments answered conditionally.** Followed: inadequate provision, factors warranting the application, intention
  to deny provision, moral obligation, disadvantage (s 83), special circumstances, sufficient cause, fraud and undue
  influence, "properly made", and the state of the estate are inputs worded "the Court finds ...". The amount of
  provision (s 59(2)) is never computed.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "eligible person" (s 57 with s 3(1)), "close
  personal relationship" (s 3(3), (4)), "child" as widened by s 3(2) and s 57(2), "relevant property transaction"
  (ss 75, 76) and its effect date (s 77) are worked out; "spouse", "de facto relationship", "domestic relationship",
  "child" in the general sense, "domiciled" and "full valuable consideration" are asked.
- **One case.** One applicant, one estate.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3(1)-(4) as Chapter 3 uses it; s 55 (in glosses: administration, legal representative); s 57 (eligible
persons); s 58 (time and filing; s 58(1) in a comment); s 59 (when an order may be made; s 59(2) as the Court's
discretion); s 63 (property available); s 64 (property outside NSW); s 70(2), (3) (variation for another eligible
person); s 72(1) (effect of an order); s 73 (notional estate treated as estate); ss 74-77 (relevant property
transactions and when they take effect); s 78 (purpose of a notional estate order); ss 79-82 (the four routes); s 83
(disadvantage); s 87 (comment); s 88 (estate insufficient); s 89(2), (3) (how much, trustee-only holders); s 90 (late
or repeat applications); ss 93, 94 (protection of the legal representative); ss 95, 96 (releases); s 97 (in a gloss);
s 98(2) (mediation; (3) in a comment); s 99(1) with s 78(2) (costs); Sch 1 Pt 3 cl (1), (2) (deaths before Chapter 3).

**Out, and why:** s 56 (binds the Crown) and Sch 1 Pt 3's other clauses: machinery. s 60 (matters the Court may
consider): a list of considerations for the Court's discretion, not a test with an answer; it informs the "Court
finds" inputs. s 61 (disregarding non-applicants), s 62 (interim orders and restraint), ss 65-69 and 71 (form, content,
ancillary orders, undertakings, exoneration, vesting), s 72(2) (abatement), ss 84-86 (effect of a notional estate order,
more than one order, subject to Division 3), s 89(1) (matters to weigh), s 91 (grant for the purposes of an
application), s 92 (substitution of property), s 98(3)-(5), s 99(2)-(4), s 100 (evidence of a deceased person's
statements): these are powers and procedure of the Court with no question the applicant can answer from facts. The
s 99(2) maximum costs are in a regulation not deposited. Chapter 2 (wills) and Chapter 4 (intestacy) are separate
subjects of the same Act, left for other encodings.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 3(1), 57(1) -- `Am I an eligible person` -- no head holds: `JUST FALSE`, because s 3(1) "eligible person means
  a person who may make an application ... under section 57" hands the definition to the list (ruling of 2026-11-05,
  delegated definitions (a)) -- `NOTHING`, the s 57 list not being closed with "only".
- **F2** s 57(2) -- `I count as their child` -- the s 57(2) heads count only where the dead person was in a de facto or
  domestic relationship at death; otherwise that route answers no and the person must rely on being a child in the
  general sense -- the s 57(2) children are children anyway under the general law in many cases (adopted, born of the
  relationship), which the encoding asks separately.
- **F3** s 58(2) "not later than 12 months after the date of the death" -- `By when must I apply`, `Can my application be
  made when I file it` -- the last day is the same day of the month a year later (a 29 February death: 28 February), and
  filing on it is in time -- the Interpretation Act 1987's counting rules (not deposited) might give another day.
- **F4** s 58(2) -- `Can my application be made when I file it` -- a filing dated before the death answers `JUST FALSE` --
  `NOTHING`, the Act not contemplating it.
- **F5** Sch 1 Pt 3 cl (1), (2) -- `Am I an eligible person`, `Can the Court make a family provision order for me` -- a
  death before Chapter 3 commenced answers `NOTHING` (the Family Provision Act 1982 applies; outside the sources); the
  commencement day (1 March 2009) is not in the deposited text and is asked as a yes/no fact -- compute it from the date
  of death once the commencement proclamation is deposited.
- **F6** s 95(1) -- `Can the Court make a family provision order for me` -- an approved, unrevoked release of the right
  to apply out of the whole estate answers `JUST FALSE`; a release of part (s 95(3)) is not modelled -- the release
  operates only "to the extent" approved, which a fuller encoding would ask.
- **F7** s 63(3), (5) -- `Can an order for me be made out of this property` -- estate property distributed otherwise than
  in compliance with s 93, and not designated, answers `NOTHING` (s 63(3) bars only a s 93 distribution; s 63(5) speaks
  of distributed property generally) -- `JUST FALSE` under s 63(5)'s "if", or `JUST TRUE` as still estate.
- **F8** s 76(2) -- `it is a relevant property transaction` -- each listed circumstance is taken to put property in
  another's hands, so the s 75(1) result is not asked for it -- ask it for every head.
- **F9** s 80(2)(a), (b) "within 3 years [one year] before the date of the death" -- `section 80 applies to the
  transaction` -- the window runs from the same day of the month three (one) years before the day of death, inclusive,
  to the day of death inclusive; a lifetime transaction taking effect on the day of death falls in (a) or (b), not (c)
  -- the window excludes its first day, or a same-day transaction counts under (c) "on or after the deceased person's
  death".
- **F10** s 89(2) -- `What is the most that can be designated as notional estate` -- read arithmetically: the provision
  the Court thinks should be made, plus costs ordered from notional estate, less what the actual estate can supply;
  never below nil -- the cap is "in the Court's opinion" and the Court may weigh value changes and income (s 89(1)(c),
  (d)), so the figure is the Court's.
- **F11** s 83(1)(a)-(d) -- `Can this property be designated ...`, `Can property passed on ...` -- the four limbs are one
  input ("disadvantaged ... or involved using (or not using) a right or power that could have benefited them") -- one
  input per limb.
- **F12** s 94(4) "in compliance with section 93 (1)" -- `Is the legal representative protected ...` -- read as s 93(1)(a)
  to (d), because (e) (no notice of an intended application) can never hold for a representative who has received
  notice of one -- read literally, s 94(4) never applies (finding 1).
- **F13** s 70(3) -- `Can an existing order be varied to provide for me` -- assumes the person asking is an eligible
  person (asked by the first question), and asks only the sufficient cause -- ask the eligibility facts again.
- **F14** ss 93(2), 94 -- `Is the legal representative protected ...` -- where no protection applies the answer is
  `JUST FALSE`, meaning "these sections give no protection on these facts", never "the representative is liable" (the
  ruling of 2026-11-05 (b) on defences, applied to a protection) -- `NOTHING`, liability being for the general law.
- **F15** s 59(4) with s 59(3)(b)(iii) -- `Can the Court make a family provision order for me` -- after a refusal, the
  third undisclosed-property condition is read as "would not have refused" -- literally "would not have made the
  previous family provision order", which no refused application had (finding 2).
- **F16** s 93(1)(d) "the time specified in the notice has expired" -- `Is the legal representative protected ...` --
  distribution on the specified day is too early; the next day is the first permitted -- the time expires at the start
  of the specified day.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 57, s 59(1) | the eligible person | power to apply; the Court's power to order | `Am I an eligible person`, `Can the Court make a family provision order for me` |
| s 58(2) | the applicant | duty with a deadline (12 months), unless extended or consented | MUST rule, WITHIN the days to the last day |
| s 63(3), s 64 | the Court | disability (no order against s 93-distributed property; outside NSW only if domiciled) | `Can an order for me be made out of this property` |
| ss 79-83, 88-90 | the Court | power to designate notional estate, with disabilities | `Can this property be designated ...`, `Can property passed on ...` |
| s 84 | holders of designated property | liability: rights extinguished | comment |
| ss 93, 94 | the legal representative | privilege to distribute; immunity from the applicant's claim | `Is the legal representative protected ...` |
| s 95(1) | the releasing person | disability: a release binds only if approved | `Does my release of my right to apply have effect` |
| s 98(2) | the Court | duty to refer to mediation | `Must my application go to mediation first` |

## What the Act turns out to say

1. **s 94(4) cross-refers to a condition it cannot meet.** It protects a representative "who receives notice of an
   intended application" if the distribution was "in compliance with section 93 (1)", but s 93(1)(e) requires that the
   representative "does not have notice of any application or intended application". Read literally, s 94(4) never
   applies. Fork F12 reads it as s 93(1)(a)-(d); asserted.
2. **s 59(4) borrows a test written for orders.** It allows a new application after a refusal "only if, at the time of
   refusal, there existed all the circumstances regarding undisclosed property described in subsection (3)(b)", but
   s 59(3)(b)(iii) is "the Court would not have made the previous family provision order", which does not fit a refusal.
   Fork F15; asserted on the reading taken. And after a refusal, a substantial detrimental change (s 59(3)(a)) does not
   open a new application; asserted.
3. **Transactions on death need no intention.** ss 76(2)(a)-(e) and 77(2), (3) make a joint tenancy left unsevered, an
   unexercised power, a life policy and a superannuation or fund benefit take effect "on" the death, so s 80(2)(c)
   catches them whenever they were set up, with no three-year or one-year window and no finding of intention or moral
   obligation; only ss 83, 87-90 stand in the way. Asserted.
4. **s 94(4) does not require a proper distribution,** unlike s 93(2), s 94(1) and s 94(3). Asserted as written.
5. **"By reason only of".** s 59(1)(b) adds the "factors which warrant" finding only for a person eligible solely as a
   former spouse, dependant or close companion; a child who is also a former household dependant needs no such finding.
   Asserted.
6. **s 57(1)(e)(ii) is wide.** "at that particular time or at any other time" means any household membership at any
   time, joined to any dependence at any time.
7. **The commencement day of Chapter 3 is not in the text.** Sch 1 Pt 3 speaks of "the commencement of this clause";
   the day (1 March 2009) has to come from the commencement proclamation. Fork F5.
8. **s 63(3) protects only a s 93 distribution.** Distribution in breach of s 93 leaves the property's status to the
   general law and to s 79 (fork F7).
9. **Numbers left to regulations.** Maximum costs payable from the estate (s 99(2)) and mediation rules (s 98(4)) are in
   regulations not deposited.

## Questions (exported)

`sfp-claims.l4` (17), in the Act's order: `Am I an eligible person` (ss 3, 57, Sch 1 Pt 3), `Must the Court find factors
warranting my application` (s 59(1)(b)), `By when must I apply` (s 58(2)), `Can my application be made when I file it`
(s 58(2), (3), with the MUST rule), `Can the Court make a family provision order for me` (ss 57-59, 95(1)), `Must my
application go to mediation first` (s 98(2)), `Can an order for me be made out of this property` (ss 63, 64, 73(2)), `Is
this a relevant property transaction` (ss 74-76), `Can this property be designated as notional estate for me` (ss 77-80,
83, 88-90), `Can property passed on by the first recipient be designated as notional estate for me` (ss 81-83, 88-90),
`What is the most that can be designated as notional estate` (s 89(2)), `Is the legal representative protected if they
distribute before my claim` (ss 93, 94), `Does my release of my right to apply have effect` (s 95), `Can the approval
of my release be revoked` (s 96), `Can an existing order be varied to provide for me` (s 70(2), (3)), `Can my costs be
paid out of the estate or notional estate` (ss 78(2), 99(1)), `How does an order for me take effect` (s 72(1)).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the commencement proclamation for Chapter 3 and compute F5 from the date of death.
- Have a lawyer review the forks, especially F7 (distributions outside s 93), F9 (the s 80 windows), F12 (s 94(4)) and
  F15 (s 59(4)).
- Deposit the Succession Regulation for maximum costs and mediation.
- A beneficiary or holder seat for those who lose property to an order.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
