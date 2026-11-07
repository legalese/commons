# Dust Diseases Act 2005 (SA) -- baseline encoding, the claimant in a dust disease action (and the defendant)

> **Edition.** The Act encoded is the register's current version of 1 January 2021, and the Dust Diseases Regulations
> 2021 its version of 17 June 2021, both fetched from www.legislation.sa.gov.au on 6 November 2026 (the unauthorised
> RTFs; the authorised versions are the PDFs). Unlike most South Australian texts in Commons they do **not** come from
> the Open Australian Legal Corpus (collected 10 March 2025), so that corpus's "may be out of date" warning does not
> apply as such; but the register's own note warns that references to other legislation and to bodies are not updated
> automatically, and a later version may exist. Check legislation.sa.gov.au before relying on it.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`dda-core.l4`) holds every rule of the Act and of the Regulations, with its few date
helpers (built-in date functions only, no daydate); two seat layers ask the questions and restate none of the rules: the
claimant (`dda-seat.l4`, required) and the defendant (`dda-seat-defendant.l4`); each has a cases file (`dda-cases.l4`,
`dda-cases-defendant.l4`), and the defendant's has mirror cases asking the same facts from both seats.

Answers are named outcomes (enumerations), not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used: where the text says
no in its own words (a "means" definition, an "If ...", "only applies", "does not apply", a list the Regulations are
handed) the outcome begins "no:"; where a provision is limited to dust disease actions or to the District Court and SAET
without saying "only", or is silent, it begins "not covered:". That follows the 2026-11-04 and 2026-11-05 rulings in
substance. Judgments the Act hands to the court ("in the court's opinion", "if it is satisfied", "considers it
appropriate", "appears to the court", "in the absence of proof to the contrary") are inputs, answered conditionally.
No REFUSE, no `#ASSERT REFUSED`, no BECAUSE. No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use as advice.

**No regulative rule.** The Act puts no duty with a deadline on the claimant or the defendant: it is a procedural and
evidentiary Act (forum, priority, costs, presumptions, damages, direct action, appeals). Its "will" and "must" bind the
court (ss 5, 9(3), 10), which gets no seat; their effect for the person is encoded as plain answers. The time limits for
a dust disease claim are in the Limitation of Actions Act 1936 (which this Act amended), not here.

This is the first encoding of the Act and of the Regulations; nothing existing was touched.

## Edition

- **Act:** Dust Diseases Act 2005 (SA), version 1.1.2021 (the last amendment, the Supreme Court (Court of Appeal)
  Amendment Act 2019, to s 11A), deposited at `../../registers/source-bundle/dust-diseases-act-2005.txt` (text sha256
  e021e249...2c1e per its `.meta.json`). The Current Titles list of 22 September 2026 gave the same version.
- **Regulations:** Dust Diseases Regulations 2021 (SA), version 17.6.2021, deposited at
  `../../../dust-diseases-regulations-2021/registers/source-bundle/dust-diseases-regulations-2021.txt` (text sha256
  ea679183...66ec). They set the "prescribed industrial or commercial process" of ss 8(2) and 9(2): reg 4 and Schedule 1
  (ten processes, each with a relevant date), reg 5 and Schedule 2 (the first five, from 1 January 1940). Encoded in
  full, apart from regs 1 to 3 and Schedule 3 (machinery; the revocation of the 2006 Regulations).
- **Not encoded here, linked by subject:** the estate's damages for a dust-related condition (Survival of Causes of
  Action Act 1940 s 3(2), `../../../survival-of-causes-of-action-act-1940/encodings/baseline-2026-11/`), the time limits
  (`../../../limitation-of-actions-act-1936/encodings/baseline-2026-11/`), damages generally (Civil Liability Act 1936,
  `../../../civil-liability-act-1936/encodings/baseline-2026-11/`), SAET's own procedure and Part 5 appeals (South
  Australian Employment Tribunal Act 2014, deposited), and the Magistrates Court's jurisdictional limits (Magistrates
  Court Act 1991, deposited). Cross-subject IMPORT is not possible on the stable `l4`, so these are named, not called.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `dda-core.l4` | 0 | 0 | 0 | 0 |
| `dda-seat.l4` | 0 | 0 | 0 | 0 |
| `dda-seat-defendant.l4` | 0 | 0 | 0 | 0 |
| `dda-cases.l4` | 0 | 0 | 123 | 123 |
| `dda-cases-defendant.l4` | 0 | 0 | 21 | 21 |

Negative control: with the Regulations' "prescribed business" (Sch 1 cl 1, "more than 20 persons") changed to "at least
20", the cases failed exactly the 5 predicted assertions (four 20-employee cases in `dda-cases.l4`, one in
`dda-cases-defendant.l4`; the mirrors still agreed); the core was restored and rechecked (123 of 123, 21 of 21).

Edges asserted: each limb of the s 3 definitions failing in turn, and (a) to (d) whatever the cause; the day before and
the day of 8 February 2006 (Sch 1 cl 4); the day before and the day of each relevant date in Schedule 1 (1 January 1940,
1 January 1960, 1 July 1971, 1 January 1976) and of 1 January 1940 in reg 5; 20 and 21 employees; item 10's
premises exclusion; each of the four s 11(1) defendant states; the insurer's cap at, a dollar under and a dollar over the
indemnity; both kinds of SAET decision.

## Seats

**The claimant (required): the plaintiff in a dust disease action.** Usually the injured person (a person with
asbestosis, mesothelioma or another asbestos disease); after a death, the person suing for it (the estate or the
dependants). `dda-seat.l4`, 19 questions, in the Act's order:

- s 3, Sch 1 cl 4: `Is my claim a dust disease action`, `Does the Act apply to my action`;
- ss 4A, 5: `Where can I bring my dust disease action`, `Can I include another claim in my SAET proceedings`,
  `Will my action be given priority`;
- s 7: `On what basis will costs be allowed in my action`;
- s 8 (with reg 4, Sch 1): `Will it be presumed that my exposure caused my disease`,
  `Is the defendant presumed to have known of the danger`, `Can earlier evidence against the same defendant be used in my
  action`, `Must I prove a matter not seriously in dispute`, `Can I be made to pay the costs of proving facts I would not
  admit`, `Can an earlier finding be applied in my action`;
- s 9 (with regs 4, 5): `Can I get damages now and more later if I develop another dust disease`,
  `Should I be awarded exemplary damages against this defendant`, `Will I be compensated for my lost capacity to do
  domestic work for others`;
- ss 10, 11, 11A: `Will my claim be decided before contribution between the defendants`, `Can I sue the defendant's
  insurer directly`, `How much can I recover from the insurer`, `Where does my appeal go`.

**The defendant (second seat): the person or business sued, another tortfeasor liable for the same damage, or the
insurer sued directly.** `dda-seat-defendant.l4`, 4 questions: `Can I claim contribution in SAET` (s 4A(3)),
`Am I presumed to have known of the danger` (s 8(2)), `Should exemplary damages be awarded against me` (s 9(2)),
`What is the most I can be made to pay as the insurer` (s 11(3)). The three shared with the claimant have mirror cases.

No seat for the District Court, SAET or the Supreme Court.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers and dates.** Followed: the Dust Diseases Regulations 2021
  are in; they are the only instrument the Act hands a number or list to.
- **The actors the text names.** Followed: the plaintiff, the injured person, the defendant (including a third party
  against whom contribution is sought), tortfeasors, the insurer, the District Court, SAET, the South Australian
  Employment Court, the Supreme Court, the Court of Appeal.
- **Judgments answered conditionally.** Followed: relevance (s 8(4)), "not seriously in dispute" (s 8(3)(b)), the
  court's satisfaction (s 9(2)), its opinion on delay (s 10), what it considers appropriate (s 7(2)), proof to the
  contrary (s 8(1), (2)), and what is established, proved or admitted are all asked as facts.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "dust disease", "dust disease action" (s 3) and
  the Regulations' "prescribed business" and Schedules are worked out from facts, in every claimant question that turns
  on them; "civil action", "breach of duty", "tortfeasor", "insolvent", "interlocutory order" and "jurisdictional limits
  of the Magistrates Court" are borrowed and asked.
- **One case:** one dust disease action against one defendant (one insurer, one earlier finding, one process).
- **The Act's terms with plain glosses:** in the `@desc`s and comments.
- **Machinery out:** s 1, s 4 (object), s 12 (regulations); regs 1 to 3 and Schedule 3.

## Scope

**In:** ss 3, 4A (all), 5, 7 (all), 8 (all), 9 (all), 10, 11 (all), 11A, Schedule 1 clause 4; Dust Diseases Regulations
2021 regs 4 and 5, Schedules 1 and 2.

**Out, and why:**

- s 1 (short title), s 12 (regulation-making power): machinery.
- s 4 (object of the Act): states a purpose; nothing for the person to do or ask. It bears on how the Act is read.
- ss 2 and 6: not in the text (s 2 omitted under the Legislation Revision and Publication Act 2002; s 6 deleted in 2016).
- The amendments the Act made to the Civil Liability Act 1936, the Limitation of Actions Act 1936 and the Survival of
  Causes of Action Act 1940 (Schedule 1 Parts 1 to 3, omitted from the text): they live in those Acts now.
- The quantum of damages and costs, the content of the Magistrates Court and District Court costs bases, and SAET's
  procedure: other Acts and rules.

## Forks (decided case by case, ruling of 2026-11-05)

Each is the provision, the function, the answer taken, and the other reading, for a reviewer to overrule.

- **F1** Sch 1 cl 4(2), `does the Act apply to the action (Sch 1 cl 4)`: "before the commencement" means on or before 7
  February 2006; an action commenced, or a trial begun, on 8 February 2006 is not "before". The other reading treats the
  commencement day itself as before (if the Act took effect at the end of that day).
- **F2** regs 4(2), 5(2), `is prescribed for s 8(2) (reg 4)` and `is prescribed for s 9(2) (reg 5)`: "carried on from
  the date" includes that date, and the encoding asks for one day (the day of the exposure, or the first day of the
  process at the time in question). The other reading needs the whole process to fall on or after the date.
- **F3** ss 4A, 5, 7, 8(1), 8(3), 8(4), 9, 10, 11, 11A: outside a dust disease action (or, for ss 7 and 8(3), (4),
  outside the District Court and SAET) the answer is "not covered", not "no": these are scope limits without "only"
  (ruling (c) of 2026-11-05). The other reading, for the sections that open "If it is established in a dust disease
  action" (s 8(1)) or "If it is proved or admitted in a dust disease action" (s 9(1)), gives "no".
- **F4** s 9(2)(b) with s 8(2), `limb (b) of s 9(2) is met`: the s 8(2) presumption, unless the contrary is proved,
  counts as the court being satisfied that the defendant knew; and s 8(2)'s "could have resulted in the exposure of
  another" is taken from the claimant's answer that the process "resulted in my exposure". The other reading requires
  the court to be satisfied on the evidence alone for an award under s 9(2), leaving s 8(2) to liability.
- **F5** s 8(1), (2), `is causation presumed (s 8(1))`, `is knowledge presumed (s 8(2))`: where the contrary is proved
  the answer is "no: the presumption gives way". The other reading answers "not covered" (the Act says only what is
  presumed in the absence of such proof).
- **F6** s 7(2), `on what basis are costs allowed (s 7)`: the Magistrates Court basis needs both that the action is
  within that court's limits and that the court considers it appropriate; otherwise the District Court basis (s 7(1) or
  (1a)) applies. Not otherwise arguable, recorded for the reviewer.
- **F7** s 8(4), `can the earlier finding be applied (s 8(4))`: a finding by a body s 8(4)(a) does not list, or one the
  court does not consider relevant, gets "no" (the "If" fails). The other reading gives "not covered", leaving the
  general law of evidence to admit it.
- **F8** s 10, `is liability to the plaintiff decided first (s 10)`: where the court thinks the delay inconsequential the
  answer is "not necessarily" (the court may then deal with the questions together); it is not "no".
- **F9** s 11(2), (3), `the insurer's liability (s 11(2), (3))`: the insurer's liability is the smaller of what the
  absent defendant would have been liable for and what the insurer would have had to indemnify, both asked as dollar
  amounts. The other reading treats "extent" as including policy terms other than an amount (excesses, exclusions),
  which the second figure must then already reflect.
- **F10** s 3, `is a dust disease action (s 3)`: "civil action" is asked as a fact; a workers compensation claim is read
  as not a civil action. The other reading would ask the Return to Work Act's tribunal claims too.

## What the Act turns out to say (findings)

1. **"Dust disease" means asbestos disease only.** Despite the long title ("exposure to dust"), s 3 lists asbestosis,
   asbestos induced carcinoma, asbestos related pleural disease, mesothelioma, and any other disease "resulting from
   exposure to asbestos dust". Silicosis, coal dust pneumoconiosis and the other dust diseases are not dust diseases
   here, though the Survival of Causes of Action Act 1940's Schedule lists them as dust-related conditions. Asserted.
2. **Mesothelioma counts whatever its cause.** Paragraphs (a) to (d) are not tied to asbestos exposure in their words
   (the causal link is for the action itself, s 3 "dust disease action" (b), and the s 8(1) presumption). Asserted.
3. **s 8(2) is not limited to a dust disease action.** Sections 8(1), (3) and (4) are; s 8(2) presumes knowledge of
   anyone who carried on a prescribed process, in its words in any proceeding. Encoded without the limit.
4. **Two lists, two purposes.** Schedule 1 (for the s 8(2) presumption of knowledge) has ten processes, the last five
   with later dates; Schedule 2 (for the "prescribed process" limb of s 9(2)(a)) has only the first five, the miner's
   and manufacturer's processes. An installer or a non-manufacturer user of asbestos products can be presumed to have
   known of the danger, but meets s 9(2)(a) only if it knew the injured person was at risk. Asserted.
5. **The size of the business moves the date by eleven and a half years.** For design, supply, installation and use by
   others (items 6 to 9), a business with more than 20 persons is covered from 1 January 1960, any other from 1 July 1971.
   A business of exactly 20 is "any other". Asserted (20 and 21).
6. **Asbestos in the building is not enough.** Item 10, the catch-all from 1 January 1976, excludes a process whose only
   asbestos is in the structure of the premises. Asserted.
7. **s 8(4) leaves out South Australian tribunals.** It covers findings by "a court of this State, or a court or tribunal
   of the Commonwealth or another State or Territory". A finding by a South Australian tribunal that is not a court is
   not covered; SAET's dust disease findings are made by the South Australian Employment Court (s 4A(2)) and so are a
   court's. Asserted (a South Australian tribunal: no).
8. **s 9(2) says "should", not "must".** The award of exemplary damages is directed but not compelled; the answer says
   "should". s 9(3), by contrast, says "must", "despite any other Act or law".
9. **s 9(3) is about services the injured person gave others** (Sullivan v Gordon, as its note says), not services
   others give the injured person, which the Civil Liability Act 1936 s 58 governs; the two do not overlap on their
   words.
10. **The Act names the District Court but no longer gives it jurisdiction.** ss 5, 7 to 10 speak of "the District Court
    or SAET", but the only jurisdiction-conferring section left is s 4A (SAET); s 6 was deleted in 2016. The District
    Court's jurisdiction comes from its own Act.
11. **A misprint in the legislative history.** The table of provisions amended says s 11A was "inserted by 53/2016 s 50";
    the principal Act table gives Act 63 of 2016, Part 3 (ss 42 to 50), as the amending Act. 53/2016 is presumably
    63/2016. Not part of the operative text.
12. **No time limits.** The Act sets none; a dust disease claim's time limits are in the Limitation of Actions Act 1936.

## Before relying on it

Check the register for versions later than 1 January 2021 (Act) and 17 June 2021 (Regulations); have a lawyer review
forks F1, F2, F4 and F7; encode the South Australian Employment Tribunal Act 2014's appeal and procedure provisions and
the Magistrates Court's jurisdictional limits and link them; run an independent test pass.
