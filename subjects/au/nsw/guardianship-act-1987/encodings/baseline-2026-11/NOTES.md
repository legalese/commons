# Guardianship Act 1987 (NSW) -- baseline encoding, the person with a disability

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 27 March 2021). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (the Secretary's three
days to apply for a guardianship order after a removal, s 13(2); the Tribunal's further consideration within an interim
financial management order's period, s 25H(3)), each run by `EVALTRACE` inside an exported question that takes only plain
facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. It was written as part of a run of baseline
encodings of the Acts that people bringing or answering claims meet. For this Act that means: who decides for a person
who cannot decide, how those decisions are made and challenged, when treatment may lawfully be given, and what claims
the Act bars, preserves or punishes.

## Edition

- **Act:** Guardianship Act 1987 No 257, corpus document `nsw_legislation:2021-03-27/act-1987-257` (in force 27 March
  2021), deposited at `../../registers/source-bundle/act-1987-257.txt`, taken from the Open Australian Legal Corpus
  (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Not deposited:** the Guardianship Regulation (prescribed forms, eligible witnesses, major and special treatment,
  corresponding laws, interstate instruments, classes of Public Guardian decisions open to review), the Interpretation Act
  1987 (counting periods; de facto partner), the NSW Trustee and Guardian Act 2009, the Powers of Attorney Act 2003, the
  Mental Health Act 2007, the Administrative Decisions Review Act 1997 and the Crimes (Sentencing Procedure) Act 1999
  (penalty unit). What they decide is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Exported questions | Assertions written | Satisfied |
|---|---|---|---|---|---|
| `ga-dates.l4` | 0 | 0 | 0 | 0 | 0 |
| `ga-core.l4` | 0 | 0 | 4 | 0 | 0 |
| `ga-enduring.l4` | 0 | 0 | 13 | 0 | 0 |
| `ga-orders.l4` | 0 | 0 | 25 | 0 | 0 |
| `ga-treatment.l4` | 0 | 0 | 11 | 0 | 0 |
| `ga-cases-enduring.l4` (core and Part 2) | 0 | 0 | 0 | 100 | 100 |
| `ga-cases-orders.l4` | 0 | 0 | 0 | 140 | 140 |
| `ga-cases-treatment.l4` | 0 | 0 | 0 | 91 | 91 |

Every expected value was worked by hand from the text, with the edges: the 16th and 18th birthdays and the day before,
a birthday on 29 February; a 30-day temporary order across a short February; one, three and five years from 29 February;
an interim order of exactly six months and one day over, and from 31 August to the end of February; the last day of the
interim period and the day after, with the further consideration completed on each; the third day after a removal and the
fourth, across a year end, and an application made after the day asked; the review-extended guardianship order on the
day the review is completed and the day after; every route in the s 33A hierarchy, with each person passed over; each
condition of ss 6C, 6H, 14, 15, 17, 25G, 37, 45 and 46 failing alone.

## Seat

**The person with a disability**: the adult (or young person of 16 or 17) who appoints an enduring guardian, about whom a
guardianship or financial management order is sought or made (the "person under guardianship", the "protected person"),
who is removed from premises under ss 11-13, or on whom medical or dental treatment is proposed (the "patient"). Every
exported question is one that person, or someone asking for them, would ask ("Can I appoint an enduring guardian?",
"Does my document work?", "Can an order be made about me?", "How long can it last?", "Must the Tribunal review it if I
ask?", "Can I sue for what was done to me?", "Who is my person responsible?", "Does the consent given for me count if I
object?", "Was treating me an offence?"). No other seat: the guardian, enduring guardian, manager, person responsible
and practitioner carry duties under the Act, and seats for them could be added beside this one; officials (the Tribunal,
the Public Guardian, the NSW Trustee, the Secretary) get none.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets its own numbers (16 and 18 years;
  1, 3 and 5 years; 30 days; 6 months; 3 days; the penalties). The Guardianship Regulation, which declares major and
  special treatment and prescribes forms, witnesses and corresponding laws, is not deposited: those facts are asked.
- **The actors the text names.** Followed: the appointor and appointee, substitute enduring guardian, guardian, alternative
  guardian, Public Guardian, NSW Trustee, manager, Secretary, Minister, Tribunal, Supreme Court, Children's Court, person
  responsible, practitioner.
- **Judgments answered conditionally.** Followed: every "the Tribunal is satisfied", "in the opinion of the Tribunal",
  "considers", "genuine concern", "best interests", "reasonable belief", "good faith" and capacity finding is an input.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "a person who has a disability" (s 3(2)), "person
  in need of a guardian" (s 3(1)), "has the care of" (s 3D), "close friend or relative" (s 3E), "eligible signer" and
  "eligible witness" (s 5), the kinds of treatment (s 33(1)), "incapable of giving consent" (s 33(2)), "object" (s 33(3))
  and "person responsible" (s 33A) are worked out. "Mentally ill person" (Mental Health Act 2007), "de facto partner",
  "legal capacity" and "parental responsibility" are asked.
- **One case.** One person, one appointment, one order, one proposed treatment.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**
- Part 1: s 3(1) (child, guardian, person in need of a guardian, spouse), s 3(2) (disability), s 3C (in comments), s 3D
  (care), s 3E (close friend or relative).
- Part 2, enduring guardians, whole: ss 5, 6, 6A, 6B, 6C, 6DA(2)-(3), 6E, 6H, 6HA, 6HB, 6HC (as a fact), 6I, 6J(1), (3),
  6K(1), (2), (4), (5), 6MA, 6O.
- Part 3, guardianship orders: ss 9, 13(2) (regulative), 14, 15, 16(1)(a), (2A), 17, 18, 21A(2), 23, 25(2)-(6), 25A, 25B,
  25C.
- Part 3A, financial management: ss 25F, 25G, 25H (with a regulative rule for (3)), 25I(1), 25K, 25M(2), (3), 25N(4),
  25O, 25P(2), 25Q, 25R.
- Parts 4 and 4A: ss 30 and 31F (no proceedings for acts in good faith under a direction).
- Part 5, medical and dental treatment, whole operative Part: ss 33, 33A, 34, 35, 36, 37, 44, 45, 45A (through the inputs
  of ss 36 and 46), 45AA(4), 45AB(1)(a), 46, 46A, 47.
- Part 5A: s 48B(1)-(4). Part 7: s 80A. Part 9: ss 100, 101.

**Out, and why:**
- Machinery: ss 1, 2, 3(3)-(6), 3A, 3B, 48, 77-80, 98 (service), 106-109, Schedule 3 (savings and transitional).
- s 4 (general principles): a duty on everyone exercising functions to "observe" principles that are all judgment; quoted
  nowhere as a rule. Its effect reaches the seat only through the Tribunal's judgments, which are inputs.
- s 3F (parties to proceedings): the person the proceedings are about is always a party (s 3F(2)(b), (3)(b), (4)(c),
  (5)(b), (7)(b)); the rest of the list does not change any answer from this seat.
- Service and notice duties (ss 6J(2), 10, 25(4), 25I(3)-(5), 25N(6), 25S(3), 27, 31C, 43): "as soon as practicable", with
  failure not vitiating the decision; no deadline a person can test.
- Tribunal and court powers that give the seat no question of its own: ss 6D (joint enduring guardians), 6F, 6G, 6L,
  6M, 6N (evidence), 8, 11, 12 (removal powers; only their s 13(2) limit is encoded), 16(2)-(4), 19, 20, 21, 21B, 21C,
  22, 22A (death of a guardian), 24, 25L, 25E, 25J, 25S-25U (review of a manager), 26-29, 31, 31A-31E, 31G, 42, 45AA(1)-(3),
  (5), 45AB(2), 48B(5)-(7).
- Offences not met by the seat: ss 102-105 (search warrants, obstruction, false representation, false statements).
- The damages and time limits of any claim the person brings: not in this Act (see finding 1).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 6, 6B, 9(2), 15(1)(a), 16(1)(a), 18, 25H(1), 33A(2), 34(1) (ages and periods) -- `ga-dates.l4` -- a person
  reaches an age on the anniversary of their birth (on 28 February in a common year for someone born on 29 February); a
  period of months or years from a day ends on the same day of the month later, or on that month's last day where
  shorter; a period of days does not count its first day -- the Interpretation Act 1987 (not deposited) might give
  another end day in a short month, or a 1 March birthday for a 29 February birth.
- **F2** s 3D(1) "include (but are not limited to)" -- `the person has the care of me` -- paid care, or no regular
  care, answers `NOTHING`; care only by the institution one lives in answers `JUST FALSE` (a flat "is not ... to be
  regarded") -- paid care answers `JUST FALSE`, reading "otherwise than for remuneration" as the test.
- **F3** s 3E(2) guidelines -- `Is this person my close friend or relative` -- answered from s 3E(1) alone, guidelines
  not deposited -- guidelines may widen or narrow it.
- **F4** s 6 "A person of or above the age of 18 years may" -- `Can I appoint an enduring guardian`, `Does my
  appointment document operate` -- under 18 answers `NOTHING` (a grant limited in its own words, no "only") -- `JUST
  FALSE`, reading s 6 as the only source of the power.
- **F5** s 6B "not eligible ... unless", "not eligible ... if" -- `Is this person eligible to be my enduring guardian` --
  where no bar applies, `JUST TRUE` -- `NOTHING`, since the Act states only disqualifications.
- **F6** s 6E(1) -- `Can my enduring guardian make this decision` -- managing money or property answers `NOTHING` (the
  list is not closed with "only") -- `JUST FALSE`, since every listed function, and (e), relates to the appointor's
  "person", and the estate is managed under the Powers of Attorney Act 2003 or Part 3A.
- **F7** ss 15(2)-(4), 17(4) -- `Can the Tribunal make this kind of guardianship order` -- where no bar applies, `JUST
  TRUE`; ss 15(2) ("practicable to make a continuing order appointing a person other than the Public Guardian") and 15(3)
  ("such an order can be made appointing some other person") are read as one fact -- two facts, "practicable" being
  narrower than "can be made".
- **F8** s 18(1A)(b) "5 years ... from the date on which it was made" for a renewed order -- `The last day my
  guardianship order can have effect` -- counted from the renewal -- counted from the date the order was first made.
- **F9** s 25(6) "extended until the completion of the review" -- `Is my guardianship order in force on this day` -- in
  force on the day the review is completed -- in force only until that day begins.
- **F10** s 13(2) "for more than 3 days ... before the expiration of that period" -- the s 13(2) rule and `May the
  Secretary still keep me` -- counted in whole days from the day of placement (day 0), the period ending at the end of day
  3; an application on day 3 is in time; on day 4 the keeping must end -- 72 hours from the moment of placement.
- **F11** s 25F -- `Can the Tribunal make a financial management order about me` -- with none of the listed occasions,
  `NOTHING` (no "only") -- `JUST FALSE`, s 25F read as the complete list of when an order may be made.
- **F12** s 34(1) "This Part applies to a patient ..." -- `Does Part 5 apply to me` -- outside it (under 16, or able to
  consent), `NOTHING`, a scope limit with no "only" (ruling (c) of 2026-11-05) -- `JUST FALSE`, the section read as a
  closed statement of the patients the Part covers.
- **F13** s 37(3) "is required to certify" -- `Can I be treated without consent` -- the certificate is a condition of
  minor treatment under s 37(2) ("subject to subsection (3)") -- a separate duty, whose breach does not make the treatment
  unauthorised.
- **F14** s 35(1) "must not ... unless" once an "unless" is met -- `Was treating me an offence` -- `JUST FALSE` (no
  offence) -- `NOTHING`, the section only saying when it is an offence.
- **F15** s 45AA(4) -- `Can the Tribunal consent to my treatment` -- treatment in an unapproved clinical trial answers
  `NOTHING` -- `JUST FALSE`, approval of the trial read as a precondition of any consent to participation.
- **F16** s 6HB(1)(a) -- `Has my enduring guardian validly resigned` -- while the appointor is not in need of a guardian,
  only written notice counts; the Tribunal's approval does not stand in for it (`JUST FALSE`) -- the approval also
  suffices.

## Rulings on negatives (recorded word for word)

From `docs/ENCODING-GUIDE.md` section 5, as ruled on 2026-11-04 and 2026-11-05, and followed here:

- **N2:** "flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from
  that answer".
- **Periods, "where" and scope limits:** "(a) a period the text fixes in its own words ...: outside the period the answer
  is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only"
  (for example "below" the minimum age): outside the scope the answer is `NOTHING`."
- **Delegated definitions, defences and "until" bars:** "(c) "when", "upon" and "whenever" count as "where" under rule (b)
  of the periods ruling above".
- **Questions with no convention:** decided site by site; each such site has a fork line above (F5, F7, F13, F14, F16).

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 6 | the appointor | power to appoint | `Can I appoint an enduring guardian` |
| s 6H | the appointor | power to revoke | `Does my revocation operate` |
| s 6E | the enduring guardian | power over the appointor's person | `Can my enduring guardian make this decision` |
| s 13(2) | the Secretary | duty with a deadline (apply within 3 days, or stop keeping the person) | MUST rule, WITHIN 3 |
| s 21A(2), 30, 31F, 100 | the guardian, enforcer, official | immunity; the seat's disability to sue | `Can I sue ...` questions |
| s 25H(3) | the Tribunal | duty with a deadline (complete further consideration, or the order is revoked) | MUST rule, WITHIN the period |
| s 25M(2) | the private manager | disability to interfere until directions or authorisation | `Can my estate manager take this action` |
| s 25Q(1) | the manager | duty to hand over the estate | `To whom must my estate be handed over` |
| s 35 | anyone treating a patient | prohibition, with a penalty | `Was treating me an offence` |
| s 46(2) | the person responsible or guardian | disability: consent of no effect | `Does the consent given for me have effect` |
| s 47 | the practitioner | liability preserved | `Can I still hold the practitioner liable` |
| s 101 | anyone holding information | prohibition, with a penalty | `May information about me be disclosed` |

## What the Act turns out to say

1. **The Act has no time limits or damages for a claim.** Its claims content is immunity (ss 21A(2), 25Q(3), 30, 31F,
   100), preservation of a practitioner's ordinary liability (s 47), and an offence for treating without consent (s 35).
   A person under guardianship who sues for an injury does so under other Acts and the court rules, through a tutor or
   manager; nothing here sets that machinery.
2. **"Guardian" has two meanings.** s 3(1) defines "guardian" widely (any guardian of the person, under any law, of
   anyone but a child under 16, including an enduring guardian); s 7 narrows it for Part 3 to the guardian appointed by a
   guardianship order. Part 5 (s 33A(4)(a), "the order or instrument appointing the guardian") uses the wide meaning, so
   an enduring guardian with the consent function heads the hierarchy. Encoded so.
3. **A renewed order's longer term may be counted from the wrong day.** s 18(1)(b) counts a renewed order's 3 years "from
   the date when it was renewed", but s 18(1A)(b) counts the 5 years for a renewed order "from the date on which it was
   made". Read literally, a renewed order's five years run from the original order, which may already be years old (fork
   F8).
4. **An interim financial management order may be both revoked and extended.** s 25H(3) takes an interim order to be
   revoked at the end of its period if the further consideration is unfinished; but an interim order is a financial
   management order (s 25D), and s 25N(5) extends a financial management order "until the completion of" a review begun
   before it would cease. Which prevails is not said. Encoded with s 25H(3) alone.
5. **The s 35 penalty and s 106 disagree on the court.** s 35(1) gives the minor and major treatment penalty "on summary
   conviction"; s 106(2) says proceedings for an offence under s 35(1) "shall be dealt with on indictment". The maximum
   penalties are encoded as written; the forum is not.
6. **The immunities differ in reach.** s 21A(2) bars "any action, liability, claim or demand" against the enforcer; s 30
   protects only the guardian, and only for acts under a Part 4 direction; s 31F protects "any person" acting under an
   adoption information direction; s 100 removes only personal liability, saying nothing of the State's. A person harmed
   by an official acting in good faith with reasonable care may still have a claim against someone other than the
   official personally; the Act does not say against whom.
7. **The confidentiality consent is not the subject's.** s 101(a) permits disclosure "with the consent of the person
   from whom the information was obtained", who may be a relative or a doctor rather than the person the information is
   about.
8. **An unreachable person responsible is passed over only for minor treatment.** s 33A(5) moves down the hierarchy when
   the person responsible declines in writing or is certified incapable, not when they cannot be contacted. s 37(2)(b)
   covers that case for minor treatment only; for major treatment the only other consent is the Tribunal's.
9. **s 6B(3) saves only the appointee.** If an appointee's spouse, parent, child, brother or sister later becomes a paid
   provider, s 6B(3) does not mention it. Since eligibility is tested at appointment, the appointment probably stands,
   but the Act does not say so.
10. **The text is from 2021.** The corpus version is dated 27 March 2021. Later amendments (for example to eligible
    witnesses, remote witnessing, or the Department's name) are not reflected.

## Before relying on it

- Replace the deposited text with the current authorised text from legislation.nsw.gov.au and recheck every section
  cited, especially ss 5, 6C, 18 and 25H.
- Deposit the Guardianship Regulation, so that major and special treatment, prescribed forms, eligible witnesses,
  corresponding laws and reviewable Public Guardian decisions can be worked out instead of asked.
- Have a lawyer settle forks F4, F8, F10, F12 and F14, and findings 3, 4 and 5.
- An independent test pass; seats for the guardian, manager and practitioner if wanted.
