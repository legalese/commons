# Coroners Act 2003 (SA) -- baseline encoding, the family member of a person who has died

> **Edition.** The text encoded is the register's current version of 31 January 2023, fetched from
> www.legislation.sa.gov.au on 6 November 2026 (the unauthorised RTF; the authorised version is the PDF). Unlike most
> South Australian texts in Commons it does **not** come from the Open Australian Legal Corpus (collected 10 March
> 2025), so that corpus's "may be out of date" warning does not apply; the Current Titles list of 22 September 2026 gave
> the same version. The Act's own note warns that references to other legislation and to bodies are not updated
> automatically. Check legislation.sa.gov.au before relying on it.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A small date module (`cor-dates.l4`, built-in date functions only), a seat-neutral core (`cor-core.l4`)
that holds every rule, a seat layer (`cor-seat.l4`) that asks the questions and restates none, and one case file
(`cor-cases.l4`). Answers are named outcomes (enumerations), booleans where the text gives a "means" definition or an
"if" condition, numbers for penalties and dates for time limits; no `MAYBE BOOLEAN`, so no `NOTHING-kind` tags. Where
the text says no in its own words the outcome is a "no: ..." naming the provision; where it is silent the outcome says
"not covered", "s N does not apply" or "s N gives no ...", following the 2026-11-04 and 2026-11-05 rulings in substance.
No REFUSE, no `#ASSERT REFUSED`, no BECAUSE outside `LEST BREACH`. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use as advice.

**One regulative rule.** s 27(3)'s time limit for an appeal against a finding is written as a `DEONTIC` (`PARTY` the
appellant `MUST` apply `WITHIN` the days to the last day of the month, `LEST BREACH ... BECAUSE`), and the seat's "Is my
appeal in time?" runs it with `EVALTRACE` over the person's dates (plain facts in, the duty built inside). The other
duties are not written as rules: s 28's "immediately" has no period to count (it is asked as a fact, F13); s 25(5) and
(7) bind Ministers and count in sitting days, for which no calendar is deposited (only the 6 months are computed); the
Court's "as soon as practicable" (s 25(1), (4)) has no period either.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Coroners Act 2003 (SA), version 31.1.2023 (the last amendments in force are the Voluntary Assisted Dying Act
  2021, Sch 1 cl 6, and the Statutes Amendment (Attorney-General's Portfolio) (No 3) Act 2022, Pt 2, both commenced
  31 January 2023; the Children and Young People (Safety and Support) Act 2025, Sch 2 cl 13, is listed as uncommenced
  and not incorporated, finding 10), deposited at
  `../../registers/source-bundle/coroners-act-2003.txt` (text sha256 3f59a470...09754e3d per its `.meta.json`).
- **Regulations not deposited**, so inputs: the procedures excluded from kind (d) of a reportable death, the
  circumstances prescribed under kind (i), the classes of material under s 37(2)(d), the fees under s 37(5), the form of
  consent under s 29(2)(c). The Coroner's Court rules (nomination of a family representative, s 20A(4)(b)) are not
  deposited either.
- **Borrowed, asked as facts:** the Acts in kinds (f) and (g) of a reportable death (protected persons, child
  guardianship, mental health, supported residential facilities, consent to treatment), the Mental Health Act 2009
  inpatient treatment order and approved treatment centre (s 21(1)(b)(v), (4), (5)), the Guardianship and
  Administration Act 1993 s 32(1)(b) order, the Voluntary Assisted Dying Act 2021, the Family Relationships Act 1975
  "domestic partner", Part 8 of the Evidence Act 1929, legal professional privilege, the corresponding laws in s 3(1).
  "Month" is a calendar month (Acts Interpretation Act 1915, borrowed, not deposited).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cor-dates.l4` | 0 | 0 | 0 | 0 |
| `cor-core.l4` | 0 | 0 | 0 | 0 |
| `cor-seat.l4` | 0 | 0 | 0 | 0 |
| `cor-cases.l4` | 0 | 0 | 210 | 210 |

Negative control (on a scratch copy): with the s 27(3) rule's deadline cut by one day and s 21(5) removed from the
s 21(1)(a) test, the cases failed exactly the 7 predicted assertions (the four "last day" appeals, the regulative
rule's day 31, the detained-person-under-a-guardianship-order inquest, and the s 21(5) custody test); the copy was
discarded.

Edges asserted: the last day of the s 27(3) month and the day after; findings on 31 January (2024 leap and 2025),
28 February and 15 December; an application on the findings day and the day before it; the s 25(5) 6 months from
31 August (to 28 February); the s 37A(2) 20th anniversary and the next day, including 29 February 2080 (2100 is not a
leap year); each limb of every "or" (State death, death in custody, the nine kinds of reportable death, s 21(1)(b),
s 27(7), s 34, s 37(2)) and each conjunct of every "and" (kind (e), s 3(2), s 28(2)(b), the Aboriginal or Torres Strait
Islander definition); and the order in which provisions displace one another (s 3(2a) and s 3(2), s 23(5) before
s 23A, s 37(2) before s 37(1), the authorisation before a s 32(2) dispute).

## Seat

**The family member (required): the relative of a person who has died or disappeared in South Australia, who meets the
coronial process and may later bring or answer a claim about the death** (`cor-seat.l4`, 32 questions). Some groups ask
for the same individual in the other positions the Act puts a person in: the one who must report a death (s 28), a
witness at the inquest (ss 23, 23A), and a person whose money or professional competence a finding touches (s 27).
Every question is one that person would ask: "Is the death reportable?", "Must there be an inquest?", "Am I the senior
next of kin?", "Can our lawyer appear?", "Must I answer?", "Can my answer be used against me in a damages claim?",
"Can the inquest decide who is liable?", "Can I appeal, and by when?", "Must I report this death?", "Can the body be
released for the funeral?", "Can the case be closed as undetermined natural causes?", "Can we get the records?",
"Can I sue the coroner or call the coroner as a witness?". Provisions addressed to the State Coroner, the Court, the
Attorney-General and Ministers are encoded as what they mean for the person: what must be done for them, what may be
done to the body, what they may ask for, and by when.

No seat for the State Coroner, the Court, an investigator, the Attorney-General or a Minister. No second party seat: the
Act puts its duties with consequences (s 28, s 34, the contempts) on "a person", which the one seat already asks.

The 2026-10-18 defaults:

- **The Act alone.** Followed; regulations and rules are not deposited, so their content is asked as facts.
- **The actors the text names.** Followed: the State Coroner, the Coroner's Court, a coroner, investigators, the
  Attorney-General, relevant Ministers, the Supreme Court, the family, its nominated representative, the senior next of
  kin, a medical practitioner, a police officer.
- **Judgments answered conditionally.** Followed: "considers it necessary or desirable", "sufficient interest" (s 20,
  s 25(4), s 27(7)(c)), "reasonable grounds" (s 23A, s 28, s 29(2)), "satisfied ... interests of justice" (s 23A(4),
  s 37A), "considers that the body is not further required" are inputs worded "the Court is of the opinion ...".
- **The Act's definitions worked out; borrowed terms asked.** Worked out: State death, death in custody (with s 21(4),
  (5)), reportable death (with s 3(2), (2a)), senior next of kin, family, Aboriginal or Torres Strait Islander person,
  s 27(7) sufficient interest. Borrowed: listed above.
- **One case:** one death or event, one inquest.
- **The Act's terms with plain glosses:** in the `@desc`s and answers.
- **Machinery out:** see Scope.

## Scope

**In:** s 3(1) (State death, death in custody, reportable death), s 3(2), (2a); s 19; s 20(1), (2), (6); s 20A; s 21
(all of it); s 22(1)(g)-(i), (2), (5); s 23(4), (5); s 23A (all of it, (7), (11), (12) used in reading); s 25(1)-(5);
s 26; s 27(1), (3), (4), (7); s 28; s 29; s 32; s 33; s 34; s 35; s 36; s 37; s 37A.

**Out, and why:**

- ss 1, 4-9 (appointments, functions, delegation, investigators' certificates), 10-18 (the Court's establishment,
  seal, constitution, staff, sittings, adjournment), 39 (annual report), 40-43 (process, service, rules, regulations)
  and the Schedule (1975 Act transitional provisions): machinery; the person can do nothing under them. s 13 (the Court's
  jurisdiction) is used in reading s 21 (F3).
- s 20(3)-(5) (evidence by affidavit or statement) and s 23(1)-(3) (summonses, arrest warrants): procedure the Court
  runs; their consequences for the person are in (s 20(6) offence, s 23(4) contempt, s 36 punishment).
- s 22(1)(a)-(f), (3), (4) (entry, inspection, recording, copying; investigators): powers over premises and documents,
  not questions the family asks; the obstruction offence in s 22(5) is in.
- s 24 (not bound by the rules of evidence): no question of its own.
- s 25(6)-(8) (supplementary reports; "relevant Minister"): between the State Coroner and Ministers; the s 25(5)
  6 months are computed.
- s 27(2), (5), (6) (the appeal's constitution and the Supreme Court's powers): what the appellate court does, not a
  question the appellant can answer from facts.
- ss 30, 31, 38 (interstate removal and assistance; research information): the person has no step under them.
- s 3(3) (circumstances of an event): interpretive.

## Forks (decided case by case, ruling of 2026-11-05)

Each is the provision, the function, the answer taken, and the other reading, for a reviewer to overrule.

- **F1** s 27(3), s 25(5), `cor the last day of ... months after`: "within one month after the findings are given" ends
  on the corresponding day of the next month (28 February -> 28 March), or the month's last day when there is none
  (31 January -> 28 or 29 February). The other reading (the Commonwealth Acts Interpretation Act s 2G method) starts
  the month the next day, giving 31 March for 28 February. A last day on a weekend or holiday is not moved.
- **F2** s 37A(2), `the first day the family may apply (s 37A(2))`: "after the expiration of 20 years following" the
  finding means from the day after the 20th anniversary; the other reading allows the anniversary itself.
- **F3** s 21(1), `must an inquest be held (s 21(1))`: an event s 21(1) does not list (a death neither reportable nor
  a (b)(v) death, or another event) answers "no ... the Court holds no inquest into it", read with s 13(1) (the Court's
  jurisdiction is over events "prescribed by or under this Act or any other Act"). The other reading is "not covered".
- **F4** s 21(1)(b)(i): a death that would be reportable but for s 3(2) (died interstate, released by the coroner
  there) is in (b)(i) in its own words; a voluntary assisted dying death (s 3(2a)) is not, so it gets "no" even if the
  State Coroner wants an inquest.
- **F5** s 21(5), `is a death in custody for s 21(1)(a)`: "Despite the definition of death in custody" is read as
  prevailing over every limb of that definition, so a detained person who dies of certified natural causes while under
  a guardianship s 32(1)(b) order gets a discretionary, not a mandatory, inquest. The other reading confines s 21(5) to
  people who are "in custody" only because of the order. s 21(5) is not applied to the s 3(1) definition itself (it
  speaks "for the purposes of subsection (1)(a)"), so such a death is still reportable under kind (c).
- **F6** ss 20A(5), 29(3), 37A(9), `is a senior next of kin`: "if the person did not have [X] or if they are not
  available" is asked as one fact per class (is there an X who is available); "any adult child" lets every adult child
  qualify. The other reading takes "they" to mean the whole earlier list.
- **F7** s 37, `can I see or copy it (s 37)`: s 37(2)'s permission route applies to any material with a restricted
  feature, including material outside the s 37(1) list (a photograph not admitted into evidence); material outside the
  list with no such feature is "not covered". The other reading confines s 37(2) to the s 37(1) categories.
- **F8** s 32, `can the body be released (s 32)`: once the authorisation is issued, a dispute no longer holds the body
  under s 32 (s 32(2) speaks of refraining from issuing it). Who then gets the body is for the law of possession, not
  this Act.
- **F9** s 22(1)(i), `can it be done to the body (s 22)`: "the Act asks for no consent from the family" for a
  post-mortem: the text is silent on consent; other Acts are not consulted.
- **F10** s 27(7), `may I appeal against the finding (s 27(1), (7))`: "a person has a sufficient interest ... if" is
  an "if" condition, so none of (a)-(c) answers "no ... s 27 gives you no appeal".
- **F11** s 33(2), `can I hold them liable (s 33)`: a dishonest act, or one outside official functions, answers
  "s 33(2) gives them no immunity", never "they are liable".
- **F12** s 25(4)(b): copies go to people who appeared, or whom the Court thinks interested, only after an inquest into
  a death in custody; for any other inquest the answer points to s 37(1)(d).
- **F13** s 28(1), `must I report the death (s 28)`: "immediately" has no period, so no deadline is computed and no
  regulative rule is written; whether the death "is or may be" reportable is asked as a fact (the seat can work it out
  with the reportable-death question).
- **F14** s 20(6), `the maximum fine in dollars`: "Maximum penalty: Imprisonment for 2 years" is encoded as a fine of 0
  (none set by this Act); a fine under general sentencing law (not deposited) is not considered.

## What the Act turns out to say (findings)

1. **The inquest cannot decide a claim.** s 25(3) forbids "any finding, or suggestion, of criminal or civil liability",
   and s 35 stops a coroner being called to give evidence about the coronial work. A person bringing a damages claim
   about the death gets the cause and circumstances, recommendations and the record (s 37), not a finding of fault.
   Asserted.
2. **Certified answers are shielded from the claim too.** s 23A(8) bars use of a certified answer, and anything
   obtained from it, "in any proceeding in a court or before any person or body authorised ... to hear, receive and
   examine evidence", which includes a later civil claim, not only a prosecution; the only exception is a prosecution
   for the answer's falsity (s 23A(9)), and it holds even if the certificate is quashed (s 23A(10)). Asserted.
3. **s 27(3) speaks of "an application under subsection (1)", but s 27(1) gives an "appeal".** Read as the appeal.
4. **s 25(4)(b) has subparagraphs (ii) and (iii) but no (i)**: the legislative history records "(b)(i) deleted by
   10/2021 s 10(3)" and the rest was not renumbered. Nothing turns on it.
5. **s 21(5) does not reach s 3(1).** It un-deems certain natural-causes deaths only "for the purposes of subsection
   (1)(a)", while s 21(4) deems "for the purposes of subsection (1)(a) and the definition of death in custody in
   section 3(1)". So the s 21(5) deaths keep whatever status the s 3(1) definition gives them, and a person in
   detention who dies under a guardianship order is still a "death in custody" for s 3(1) and s 28 (State Coroner, not
   police) but gets a discretionary inquest (F5). Asserted.
6. **The senior next of kin is defined three times** (ss 20A(5), 29(3), 37A(9)), almost word for word; only s 20A and
   s 37A extend "family" to kin under Aboriginal or Torres Strait Islander kinship rules. So kinship relatives may
   instruct the family's lawyer and ask for records, but only the senior next of kin can consent to an "undetermined
   natural causes" finding (s 29(2)(c)). Paragraph (c) says "a parent", paragraph (d) "living parent"; nothing turns on
   it once availability is asked.
7. **s 34 binds "a person", not only officials.** Read literally it covers a family member who gets records under s 37
   or s 37A. Its exception for "legal proceedings arising out of the administration of this Act" (s 34(d)) would not
   obviously cover a civil claim about the death; that use would need "required or authorised by ... law" (s 34(b), for
   example a subpoena) or consent (s 34(f)), and the dead person cannot consent. A question for a lawyer.
8. **Records are free under s 37A, not under s 37.** s 37A(8) forbids a fee; s 37(5) allows one fixed by regulation.
9. **A death in custody must be reported to the State Coroner**; telling a police officer does not satisfy s 28(1)
   ("or (except in the case of a death in custody) a police officer"). Asserted.
10. **Two things outside the sections bear on the answers.** The Children and Young People (Safety and Support) Act
    2025, Sch 2 cl 13, amends this Act but was uncommenced at the version deposited (probably the reference in kind
    (f)(ii) of a reportable death to the Children and Young People (Safety) Act 2017; not checked). And the 2021
    amending Act's transitional provision says s 23A and the new s 23 apply only to inquests commenced after 7 June 2021;
    the encoding assumes a later inquest.

## Before relying on it

Check the register for a version later than 31 January 2023; deposit the Coroners Regulations and the Coroner's Court
rules and replace the inputs that stand for them (excluded procedures, prescribed circumstances, s 37 classes and fees,
the s 29(2)(c) consent form, the s 20A(4)(b) nomination); have a lawyer review the forks and findings 5 and 7; run an
independent test pass.
