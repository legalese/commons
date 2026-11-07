# Health and Community Services Complaints Act 2004 (SA) -- baseline encoding, the person complaining

> **Warning.** The text encoded here is the South Australian register's current version of the Act (4.12.2025) and of
> the Health and Community Services Complaints Regulations 2019 (18.3.2019), as the register's **unauthorised** RTFs,
> fetched on 6 November 2026; the authorised versions are the PDFs on legislation.sa.gov.au. Unlike the South
> Australian baselines taken from the Open Australian Legal Corpus (collected 10 March 2025), these texts came from the
> official register, because its bot challenge had lifted. They may still go out of date: check legislation.sa.gov.au
> before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`hcsc-core.l4`) holds every rule, with five regulative rules (the complaint within 2
years, s 27(1); meeting the Commissioner's requirement within the period specified, s 28; the Commissioner's
determination within 45 days, s 29(1); written notice of it within 14 days, s 29(6); a conciliation agreement entered
into in writing within 14 days, s 42(2)), each run by `EVALTRACE` inside a function that takes only plain facts. The
seat layer (`hcsc-seat.l4`) asks the questions and restates no rule. Dates sit in one small module (`hcsc-dates.l4`,
built-in date functions only, no daydate, no `YMD`). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in
`LEST BREACH`.

**Why this Act.** It is the claims route the claims list does not name: a person hurt or let down by a health or
community service (a hospital, a doctor, an aged care home, a disability or child protection service, an unregistered
practitioner) can complain to the Health and Community Services Complaints Commissioner without suing, and the
complaint runs beside, or gives way to, a negligence claim (s 33(3): court proceedings suspend it). It is the
equivalent, outside the courts, of the medical negligence and records-access claims on the list. The Act is also the
State's route for complaints about access to health records (s 25(1)(h)).

Answers are named outcomes (enumerations, some carrying a date or a paragraph reference), not `MAYBE BOOLEAN`, so no
`NOTHING-kind` tag is used and the 2026-11-04 and 2026-11-05 rulings are followed in substance only: where the text
says no in its own words (a "means" definition, "may only be made", "does not apply", "is not binding unless", "does
not constitute") the outcome begins "no"; where a power is given only in stated circumstances and they are not met, the
outcome says the section "does not reach this" (rule (c) of the 2026-11-05 ruling on periods, "where" and scope
limits); "it is a defence"-like protections that fail are worded "gives no protection on these facts" (rule (b) of the
2026-11-05 ruling on defences). Judgments the Act leaves to the Commissioner, the conciliator or a court are inputs.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Health and Community Services Complaints Act 2004, version 4.12.2025 (the one the register's Current Titles
  list of 22 September 2026 gave), deposited at `../../registers/source-bundle/health-and-community-services-complaints-act-2004.txt`.
- **Regulations:** Health and Community Services Complaints Regulations 2019, version 18.3.2019, deposited at
  `subjects/au/sa/health-and-community-services-complaints-regulations-2019/registers/source-bundle/`. Used: reg 4 (the
  housing exclusion from "community service"), reg 7 and Sch 2 (the code of conduct, named only), reg 8 (the prescribed
  offences for ss 56B, 56C). No regulation includes a further class in "health service" or "community service",
  prescribes a class under s 25(4)(c), or declares a further kind of prescribed child protection complaint (s 28A(8)(b)).
  The stable `l4` cannot IMPORT across subjects, so the Regulations' content is written into the core with its
  regulation number.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hcsc-dates.l4` | 0 | 0 | 0 | 0 |
| `hcsc-core.l4` | 0 | 0 | 0 | 0 |
| `hcsc-seat.l4` | 0 | 0 | 0 | 0 |
| `hcsc-cases.l4` | 0 | 0 | 149 | 149 |

Negative control: on a scratch copy, with the s 29(6) window changed from 14 to 13 days and the s 42(2) window from 14
to 15 days, the cases failed exactly the 3 predicted assertions (notice on the 14th day; writing on the 15th day; not yet
in writing on the 15th day); the scratch copy was discarded.

Every expected value was worked by hand from the text, with day counts written beside the s 29 and s 42 cases. Edges:
2 years to the day and the day after; 29 February 2024 plus 2 years; the s 27(3) presumption with the reasonable day
earlier and later than the actual day; notice on 31 May and 1 June 2004 (s 27(2)(b)); the 45th and 46th day, with 10
days of allowed delay, and across a year end (20 December 2026 to 3 February 2027); 14 days across a leap February
(20 February to 5 March 2028); the consumer's 16th birthday (s 24(b)(ii), (iii)); each "means" exclusion; the s 25(2)
and (4) carve-outs; s 56C with the investigation only commenced.

## Seat

**The person complaining (required)** (`hcsc-seat.l4`, 22 questions): the consumer of a health or community service
(patient, client, resident, a child), or the person complaining for them (a parent, an attorney, a substitute
decision-maker, a family member or the executor after a death). Every question is one that person would ask: "Is my
service one I can complain about?", "May I make this complaint?", "Is this a ground I can complain on?", "Who is my
complaint about a volunteer against?", "By when must I complain?", "Must I go to the provider first?", "Will my child
protection complaint go to the Ombudsman?", "Who will deal with my complaint?", "Was I in time with the Commissioner's
request?", "By when must the Commissioner decide on my complaint?", "By when must I be told the decision?", "Can the
Commissioner stop dealing with my complaint?", "What happens if I withdraw?", "Can my complaint go to conciliation?",
"Can someone help me at conciliation?", "Can what was said in conciliation be used in court?", "Is my conciliation
agreement binding?", "Will I get a copy of the outcome?", "Can the provider be stopped from practising?", "Can my
identity be kept from the provider?", "Is it an offence to punish me for complaining?", "Can I be sued for
complaining?". Provisions addressed to the Commissioner are encoded as what they mean for that person: a last day, a
copy they must be given, a power that may be used on stated conditions.

No seat for the provider (a provider's seat would be welcome as a second layer: ss 30(5), 47(5), 55(5), (7), 56, 56E
give the provider duties and rights) and none for the Commissioner, the Ombudsman or a registration authority.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Regulations 2019 where they fill in a
  provision encoded (regs 4, 8).
- **The actors the text names.** Followed: the complainant, the consumer, the provider, the volunteer, the
  Commissioner, the conciliator, the Ombudsman, the registration authority, the Tribunal.
- **Judgments answered conditionally.** Followed: "unreasonably" (s 25, with s 85), "satisfied" (ss 24(g), 25(6),
  27(2)(a), 37(3), 56C), "opinion" (ss 24(l), 56B, 56C, 74(b)), "appears to the Commissioner" (ss 29(4), (5), 30(8)),
  "reasonable belief" (ss 56B, 74(a)), "good reason" (ss 29(5), 33(1)(h)), "significant factor" (s 79(2)), "good
  faith" (ss 79(3), 83), an enduring relationship that "can be demonstrated" (s 24(i)) are inputs or conditions.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "health service", "community service" (s 4
  with reg 4), "prescribed child protection complaint" (s 28A(8)), "prescribed offence" (reg 8). Asked: "child" (fork
  F3), "at risk" (Children and Young People (Safety) Act 2016), "administrative act" (Ombudsman Act 1972), "approved
  provider" (Aged Care Act 1997 (Cth)), "nationally registered health practitioner", "health professional" (glossed in
  the `@desc`, not worked out), "volunteer".
- **One case:** one complaint, by one complainant, about one provider.
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** see Scope.

## Scope

**In:** s 4 (health service, community service, health status report) with reg 4; s 24 (who may complain, except the
Minister and the Chief Executive); s 25 (grounds, (2), (4), (5), (6)); s 26(2) (through s 33(1)(f)); s 27 (time limit,
extension, presumption); s 28 (further information) with s 33(1)(h); s 28A (child protection complaints to the
Ombudsman); s 29(1), (3), (4), (5), (6) (assessment, timing, notice); s 30(7), (8), (10), (11) (informal mediation);
s 33 (no further action, suspension); s 34 (withdrawal); s 37 (assistance, representation); s 39(3), (4); s 40(1);
s 42 (enforceable agreements); s 43(1)(c) as it bears on s 34; s 45(6); s 54(2); s 55(1)(b), (5), (10); ss 56B, 56C,
56D(2)(a), 56F(2) with reg 8; s 57(1)-(5); s 65 (named); s 74; ss 78, 79; s 83(1)(a), (b).

**Out, and why:**

- Part 2 (the Commissioner's office, functions, committees, staff, reports), Part 3 (making the Charter), s 72
  (delegation), ss 76, 77 (returns), ss 87-89 and the transitional provisions: machinery.
- s 24(j), (k) (the Minister and the Chief Executive as complainants), s 27(4) (the children's oversight bodies'
  complaints): officials, no seat.
- ss 30(1)-(6), 31, 32, 35, 36, 38, 41, 44, 46-53 (investigation powers, warrants, privilege) and s 80, s 81: the
  Commissioner's powers over providers and witnesses; a provider's or witness's seat would take them. s 50 (a witness's
  expenses) and s 53 (privilege) would suit a witness seat.
- s 55(2)-(9), (11), s 56 (the provider's review in the Tribunal), s 56E (review of orders), s 56EA (interstate orders):
  the provider's side.
- s 56A and Sch 2 of the Regulations (the code of conduct for health care workers, 17 clauses): named as an input
  ("a code of conduct applies"; "a breach of the prescribed code"); encoding each clause is a separate task.
- Part 7 beyond s 57(1)-(5) (ss 58-66, the traffic between the Commissioner and registration authorities): between
  officials; s 65 is named in an answer.
- s 73 (adverse comments), s 75 (confidentiality, an offence for officials), s 82, s 84, s 85 (used as the gloss for
  "unreasonably"), s 86, s 86A.

## Forks (the text does not say; one reading taken)

- **F1** "within 2 years from the day on which": the last day is the same day of the month 24 months later (the first
  day not counted), or that month's last day where shorter (29 February 2024 plus 2 years is 28 February 2026); "within
  45 days after receiving it", "within 14 days after": that many days after, the day itself not counted. Asserted.
- **F2** a housing service of a prescribed housing entity that reg 4 does not exclude (no Tribunal review open) is taken
  to be a community service under paragraph (a). Asserted.
- **F3** "child" (s 24(b), s 27(2)(b)) is not defined in the Act; read as a person under 18.
- **F4** s 27(3) "presumed to have notice ... at the time he or she might reasonably be expected to have had such
  notice": the day of notice is taken as the earlier of the actual day and the reasonably expected day. The other
  reading: the presumption replaces the actual day, which could postpone the start for a complainant who in fact knew
  early. Asserted both ways.
- **F5** "after May 2004" (s 27(2)(b)): on or after 1 June 2004. Asserted.
- **F6** s 33(1)(h)'s "within a reasonable time" is taken to be the "reasonable period" the Commissioner specifies
  under s 28(2), as extended.
- **F7** the conciliator's s 37(2) direction reaches assistance only (its words), not representation under s 37(3).
  Asserted.
- **F8** "before the court" (s 33(3)(a)) is read as before a court; proceedings before a tribunal, authority or other
  body are under s 33(1)(d). Asserted.
- **F9** s 79(2) says a significant factor is sufficient; where the complaint was not even a significant factor, the
  treatment is taken not to be "on the ground" of it. Asserted.
- **F10** s 56B and s 56C both open: s 56C (the final order) is given first; s 56B is given where only its conditions
  are met. With the investigation only "commenced", s 56C is not open (it needs one "carried out"). Asserted.
- **F11** s 24(d) (the donee of a power of attorney) and s 24(da) are applied as written whether or not the consumer has
  died; the general law on the end of a power at death is not brought in.

## What the Act turns out to say (findings)

1. **A medico-legal report cannot be complained about.** "Health service" "does not include ... the process of writing,
   or the content of, a health status report" (s 4 (k)), defined as a report on a person's health prepared other than
   to provide a health service. An independent medical examiner's report for an insurer, employer or court in a claim
   is such a report, so its content and its writing are outside the Act. Asserted.
2. **Access to records, but not a copy.** s 25(1)(h)(i) makes it a ground that a provider denied or unreasonably
   restricted access to records, but s 25(2)(b) says nothing in s 25(1) requires a provider "to alter, or to hand over a
   copy of, medical records". Where access ends and "a copy" begins (an emailed scan, a printout to read on site) is not
   said. Asserted as two outcomes.
3. **Disclosure to an insurer.** A disclosure to "an insurer who has an appropriate interest in the information" is not
   a s 25(1)(i) ground (s 25(4)(b)); "appropriate interest" is not defined, so a claimant cannot tell from the text
   whether a disclosure to the other side's insurer is caught.
4. **The child extension has become general.** s 27(2)(b) lets the Commissioner extend time, without the (a) factors,
   for any complaint about a service to a child where notice came "after May 2004". The date reads as a transitional
   anchor (the Act was assented to in 2004); for complaints made now, it covers every late complaint about a service to
   a child.
5. **"the court".** s 33(3)(a) requires suspension when proceedings "have been commenced before the court"; no court
   is defined (fork F8). For a claimant, commencing a damages action suspends the complaint; finishing it (all issues
   adjudicated) ends it (s 33(2)).
6. **Three confidentiality rules, three wordings.** s 30(10) (informal mediation) needs "consent of the parties"; ss
   40(1) and 45(6) need "consent of all parties". s 40(1) also covers "information provided for the purposes of
   conciliation"; ss 30(10) and 45(6) cover only "anything said or done". Encoded as three provisions with one shape.
7. **"the prescribed health service provider".** s 56D(2)(b) refers to "the prescribed health service provider", a term
   defined nowhere in the Act; Division 5 otherwise speaks of "a person who has provided a health service". Probably a
   relic of an earlier draft; reported as a likely drafting error.
8. **s 25(1)(h)(ii) says "the health service provider".** The rest of s 25 says "health or community service provider",
   so on its words the "information about the consumer's condition" limb reaches only health service providers. The
   encoding asks for the allegation without distinguishing; a lawyer should say whether the narrowing is meant.
9. **Gaps in lettering.** s 24 runs (b), (d) with no (c); the definition of "registration law" runs (a), (b), (d); s
   75(2) runs (d), (f); ss 15, 67-71 and Part 8 are absent. These are repeals left unrenumbered, not errors.

## Before relying on it

Check the text against the authorised PDFs and the register's current versions; have a lawyer review the forks
(especially F4, F7, F10) and findings 2, 3 and 8; encode the provider's seat (ss 30(5), 55, 56, 56E) and the Sch 2 code
of conduct; run an independent test pass.
