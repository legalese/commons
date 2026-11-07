# Civil Liability Act 1936 (SA), Parts 7A and 7B -- baseline encoding, the person abused as a child

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus (South Australian legislation last
> collected on 10 March 2025): the Act as at 22 June 2023. It is unofficial and may be out of date: later amendments
> are missing. Check legislation.sa.gov.au before relying on anything here.

## Why this encoding, and where it sits

The task was South Australia's equivalents of the child abuse reforms other jurisdictions made after the Royal
Commission into Institutional Responses to Child Sexual Abuse: removing the limitation period, and making institutions
liable (a duty with a reversed onus, vicarious liability, a proper defendant for unincorporated bodies, and setting
aside old settlements). South Australia made them in two Acts:

- **Limitation of Actions Act 1936 Part 1A (s 3A)**, inserted by the Limitation of Actions (Child Abuse) Amendment Act
  2018 (in operation 1 February 2019), with that Act's Sch 1 cll 1-3 for claims barred before then. These are already
  encoded, with seat questions, in `subjects/au/sa/limitation-of-actions-act-1936/encodings/baseline-2026-11/`
  ("Is there any time limit on my claim for damages for abuse I suffered as a child?", "My child abuse claim was barred
  by time before 1 February 2019, or an earlier action failed: can I sue now?"). Nothing there was touched.
- **Civil Liability Act 1936 Parts 7A and 7B (ss 50A-50X)**, inserted by the Civil Liability (Institutional Child
  Abuse Liability) Amendment Act 2021 (52/2021) s 4, in operation 1 August 2022. These were not encoded: the Civil
  Liability Act's own baseline (`../baseline-2026-11/`) lists them as out of scope. **This encoding covers them.**

The task named the Limitation of Actions Act's folder. The encoding is filed here instead, beside the Act it encodes,
because Commons files an encoding under the subject whose text it encodes, and the Limitation of Actions Act's child
abuse provisions already have their questions. The existing Civil Liability Act baseline stays as it is; this is a
second encoding beside it (`baseline-2026-11b`), and the two share no code (the stable `l4` imports only within a
folder, so no name clashes are possible).

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`ica-core.l4`) holds every rule; the seat layer (`ica-seat.l4`) asks the questions
and restates no rule; the dates and the two commencement days sit in one small module (`ica-dates.l4`, built-in date
functions only, no daydate, no `YMD`). One regulative rule: the court's order under s 50J(7)(a) that the institution
identify its associated trusts within 28 days (or the period the court sets), `PARTY the institution MUST ... WITHIN
... HENCE FULFILLED LEST BREACH BY the institution BECAUSE ...`, run by `EVALTRACE` inside a function that takes only
plain facts (the day of the order, the period, whether and when it complied, today). No exported question takes a
DEONTIC or EVENT input. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.

Answers are named outcomes (enumerations), lists of named outcomes, or dates. Two internal helpers for s 50V return
`MAYBE BOOLEAN` (`NOTHING` where the answer turns on an open list); no exported answer does, so no `NOTHING-kind` tag
is used. Where the text says no in its own words (a "means" definition, an "if" that fails, "does not apply", "is not
associated only because", "must not", "may only ... if") the outcome begins "no:"; where the text lists without
closing the list ("includes") the outcome says "the Act does not say"; where a scope limit without "only" is not met
the outcome says the Division "does not reach this" (the 2026-11-04 and 2026-11-05 rulings in substance). Where a
section's "if" fails but the common law is preserved (s 50G(3)), the answer says no for that section only and that
the common law still applies (the 2026-11-05 ruling (b) on defences, by analogy). Judgments the Act leaves to the
court are inputs of one shape (`Court finding`: found so, found not so, not decided yet), never decided.

No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

## Edition

- **Act:** Civil Liability Act 1936 (SA), Open Australian Legal Corpus document
  `south_australian_legislation:2023-06-22/1936.2267.un` (as at 22 June 2023), deposited at
  `../../registers/source-bundle/civil-liability-act-1936.txt` (sha256 of the committed blob 14e3cc24...2c6e). The
  Current Titles list of 22 September 2026 gave the same version date (22.6.2023), but it has not been re-read since,
  and the corpus was collected on 10 March 2025.
- **Commencement days**, from the legislative histories: Parts 7A and 7B, 1 August 2022 (52/2021, Gazette 28.7.2022
  p2373, in this Act's history); s 3A of the Limitation of Actions Act 1936, 1 February 2019 (14/2018, Gazette
  22.11.2018 p4010, in that Act's history, deposited at
  `subjects/au/sa/limitation-of-actions-act-1936/registers/source-bundle/`).
- **Regulations:** none deposited that bear on Part 7A. The Civil Liability Regulations 2013 deposit is as at 2 October
  2015, before Part 7A existed. Whatever the regulations prescribe under s 50A(3) (who is or is not akin to an
  employee), s 50C(1)(e) (further associated persons), s 50F(3)(i) (further matters) and s 50J(3) (how notice of a
  claim is given to the head) is therefore not encoded; see "Before relying on it".

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ica-dates.l4` | 0 | 0 | 0 | 0 |
| `ica-core.l4` | 0 | 0 | 0 | 0 |
| `ica-seat.l4` | 0 | 0 | 0 | 0 |
| `ica-cases.l4` | 0 | 0 | 131 | 131 |

Negative control: with the s 50J(6)(a) 120 days changed to 119, the s 50J(7)(a) 28 days to 29, and the commencement of
Part 7A moved from 1 to 2 August 2022, the cases failed exactly 11 times, as predicted (the 119th-day case; the three
default last days and the two day-29 compliance cases; the 1 August 2022 cases for the duty, vicarious liability,
s 50U, s 50V and s 50W); the files were restored and rechecked.

Every expected value was worked by hand from the text, with day counts written beside the s 50J cases. Edges: ages 17
and 18; 31 July and 1 August 2022 (Divisions 2 and 3, s 50U, s 50V(1)(b), s 50W); 31 January and 1 February 2019
(s 50V(1)(a)); the 119th and 120th days after commencing (s 50J(6)(a)); the 28th and 29th days after the order and a
14-day order on its 14th and 15th days (s 50J(7)(a)); 28 days into a leap-year February and a common-year February;
each listed kind of abuse and each listed connection against an unlisted one; a "no" winning over an open list; the
s 50A(2) exceptions against a true employee; and both s 50W(6) bars at once.

## Seat

**The person abused as a child (required)** (`ica-seat.l4`, 15 questions), who brings or may bring a claim against an
institution, or that person's representative. Every question is one that person would ask: "Is my claim an abuse
claim against an institution?", "Was the person who abused me an employee of the institution, or akin to one?", "Is
the institution taken to have breached its duty to prevent the abuse?", "Is the institution vicariously liable?",
"Whom can I bring my claim against?", "Is today's institution the one that is liable?", "Can I sue again after an
earlier judgment that the defendant was not appropriate?", "Is this trust an associated trust?", "Out of what assets
can my judgment be paid?", "Can I ask the court to make a trust's trustee the nominee, and from when?", "By when must
the institution identify its associated trusts?", "Has it done so in time?", "Is my earlier settlement an affected
agreement?", "Can the court set it aside?", "Must I pay back what I received?". Provisions addressed to the
institution, the trustee or the court are encoded as what they mean for that person: whom to sue, what can pay, what
the court may do and on what finding.

No seat for the court. A seat for the institution (its duty, its nominee, its trusts, contribution between successors
under s 50R(6)) would be welcome as a second layer beside this one.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no regulation under Part 7A is deposited (see
  Edition). One borrowing from another Act: whether "section 3A of the Limitation of Actions Act 1936 applies" (s 50V(1)(a)),
  worked out from the same facts (fork F8), because the stable `l4` cannot import that Act's encoding.
- **The actors the text names.** Followed: the claimant, the institution, the person associated with it, the employee
  and the person akin to one, the designated carer, the former and current office holder, the head, the nominee, the
  trustee of an associated trust, the relevant successor, the court.
- **Judgments answered conditionally.** Followed: "all reasonable steps" (s 50F(2)), "supplies the occasion"
  (s 50G(1)(a)), "just and reasonable" (ss 50U(2), 50W(2)), "satisfied ... does not have sufficient assets"
  (s 50J(6)(b)(ii)), "a reason ... was to try to avoid" and "appropriate" (s 50J(5)(b), (c)), "substantially the same"
  beyond s 50R(2)'s sufficient test (s 50R(1)), "wholly unrelated" (s 50E(2), (3)), "serious" physical abuse.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "abuse" (as far as the list goes), "abuse
  claim", "child", "institution", "associated with" (as far as the list goes), "akin to an employee", "associated
  trust", "affected agreement", "relevant successor" (as a choice). Borrowed and asked: "employee" in its ordinary
  sense, "incorporated", "designated carer" (Children and Young People (Safety) Act 2017), "office of authority" (glossed),
  "National Redress Scheme" deed of release, "contract of insurance", "limitation period had expired".
- **One case:** one person abused as a child, one institution, one abuser (one period of abuse on one side of 1 August
  2022; the `@desc` says to ask twice for a period that straddles it).
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** s 50T (Corporations Act displacement), the regulation-making references, and the provisions that
  only empower institutions and trustees to act (s 50O(1)-(3), (5), s 50Q).

## Scope

**In:** Part 7A Division 1 (s 50A(1), (2): abuse, abuse claim, child, designated carer, employee and akin to an
employee, institution; s 50B associated trusts; s 50C associated persons; s 50D(1) which causes of action, with
s 50D(2) reflected in the `@desc` "private or public, including government"); Division 2 (s 50E duty, s 50F reversed
onus); Division 3 (s 50G vicarious liability); Division 4 (ss 50H, 50I, 50J(1)-(3), (5)-(7)(a), 50K: whom to sue);
Division 5 (ss 50L, 50M, 50N, 50O(4), 50P: what pays); Division 6 (s 50R(1)-(6)(a) continuity and joint and several
liability, s 50S(3) the head as current office holder, s 50U proceedings despite an earlier judgment). Part 7B (s 50V
affected agreements, s 50W setting aside, with (4) and (5) in the answer text, s 50X effect).

**Out, and why:**

- s 50A(3), s 50C(1)(e), s 50F(3)(i), s 50J(3)'s requirements: what the regulations prescribe; no regulation made
  under Part 7A is deposited (fork F4).
- s 50F(3) (the matters for "all reasonable steps") and s 50W(3) (the matters for setting aside): the court weighs them;
  they are named in the answers, not inputs.
- s 50J(4) (the institution's nomination, with consent) and s 50J(7)(b) (other orders): the institution's and the
  court's acts; the claimant states only whether there is a nominee.
- s 50K(b)-(i): what a nominee takes on, summarised in the route's answer text.
- s 50O(1)-(3), (5) and s 50Q: they empower the trustee or institution to pay despite trust terms or other duties; they
  matter to the payer, not to what the claimant can ask.
- s 50R(6)(b)-(g) (contribution between successor institutions, and its limits): between institutions, for a seat of
  the institution.
- s 50S(1), (2) (an office substantially the same): reflected in the s 50I route's wording.
- s 50T: machinery.
- Limitation of Actions Act 1936 s 3A and the 2018 Act Sch 1: encoded in that Act's baseline (above).

## Forks (the text does not say; one reading taken)

- **F1** s 50D(1) and Divisions 2 and 3: abuse before 1 August 2022 answers that Division 2 or 3 "does not reach this on
  its words" (finding 1). Asserted on both sides of the day.
- **F2** "a cause of action ... arose" (s 50D(1)) is read as arising on the day of the abuse; abuse over a period that
  straddles 1 August 2022 is asked twice.
- **F3** s 50C(1)(d) "(other than a designated carer who is the parent or guardian of the child)": the carve-out removes
  the parent or guardian from paragraph (d), but the list "includes" and is not closed, so the answer is "the Act does
  not say", not no. The other reading: no.
- **F4** no regulation under Part 7A is deposited; a person "prescribed by regulation" (s 50C(1)(e)) is asked as
  "some other connection" and answered "the Act does not say"; s 50A(3) is treated as prescribing nothing.
- **F5** s 50E(3) "wholly unrelated to that person's association with the delegator institution or the delegate
  institution": read as unrelated to both (finding 2). The other reading: unrelated to either one.
- **F6** s 50J(6)(a) "at least 120 days have passed since a proceeding ... was commenced": the 120 days have passed on
  the 120th day after the day of commencement (commenced 1 March 2024: from 29 June 2024). Asserted on the 119th and
  120th days.
- **F7** s 50J(7)(a) "within 28 days": counted from the day of the order, that day not counted; compliance on the 28th
  day after is in time. Asserted.
- **F8** s 50V(1)(a) "a cause of action to which section 3A of the Limitation of Actions Act 1936 applies": worked out
  here as a claim for damages relating to death or personal injury, resulting from abuse when the person was under 18,
  abuse "including" the same three kinds as s 50A (the two definitions are worded alike). A claim without an
  institution can satisfy limb (a) alone. Asserted.
- **F9** s 50W(6)(a) "a deed of release ... and an agreement relating to a relevant prior payment": each is protected on
  its own; one input asks for either.
- **F10** where the claim was against an unincorporated institution (s 50H(1)(b)(ii)), "in accordance with section
  50J" is taken to be every claim against the institution itself while unincorporated.
- **F11** whom to sue (ss 50H-50K) assumes the claim is an abuse claim and that today's institution is the same one or
  a successor (asked separately, s 50R); the former office holder still in office is sued under the general law, which
  the Act does not list.

## What the Act turns out to say (findings)

1. **Divisions 2 and 3 have no application rule.** s 50D(1) applies Part 7A "other than Division 2 and Division 3" to
   causes of action arising before or after 1 August 2022, and says nothing about Divisions 2 and 3. The plain
   implication, with the presumption against retrospectivity, is that the statutory duty and the reversed onus
   (ss 50E, 50F) and the statutory vicarious liability (s 50G) reach only abuse from 1 August 2022, so the survivors of
   historical abuse whom s 3A of the Limitation of Actions Act 1936 lets sue must rely on the common law for those
   questions. The text never says so in terms (fork F1). Asserted.
2. **s 50E(3)'s "or" is ambiguous.** "Wholly unrelated to that person's association with the delegator institution or
   the delegate institution" can mean unrelated to both (the duty is lost only if there is no link to either) or to
   either one. The first reading is taken (fork F5).
3. **Who proves "wholly unrelated"?** s 50F(2) puts on the institution the proof that it took all reasonable steps,
   but s 50E(2) and (3) take the duty away for abuse "wholly unrelated" to the association without saying who must show
   that. The encoding takes it as a fact stated by the claimant.
4. **"Leave" here, "permission" there.** s 50U(2) (an earlier judgment that the defendant was not appropriate) says the
   court "grants leave"; Sch 1 cl 3(2) of the Limitation of Actions (Child Abuse) Amendment Act 2018 (an earlier
   judgment on limitation) says "grants permission". The tests are the same ("just and reasonable"); only the word
   differs.
5. **s 50U reaches only judgments, not dismissals or discontinuances.** Compare the 2018 Act Sch 1 cl 3(1)(a)-(d),
   which lists actions started, discontinued, judged and dismissed. A claim earlier dismissed (rather than judged) on
   the ground that the defendant was not appropriate is not mentioned in s 50U.
6. **s 50V(1)(a) stops at 1 February 2019.** An agreement made after s 3A came into operation is never an affected
   agreement under limb (a), even where a limitation period had expired under another law; only limb (b) (before 1
   August 2022, no proper defendant) can then help. Asserted (1 February 2019 with time expired and a defendant
   available: no).
7. **s 50B(2) speaks of "Division 5 or Division 6"**, so a trust made a nominee by a s 50J(5) order counts as an
   associated trust for paying a claim and for continuity, but not for s 50J(5)(a) itself (which asks whether the trust
   "is, or used to be" associated). Encoded as "yes, for Divisions 5 and 6".

## Before relying on it

Check the text against the authorised version on legislation.sa.gov.au (the corpus copy is as at 22 June 2023);
deposit the Civil Liability Regulations as in force after 1 August 2022 and encode what they prescribe for s 50A(3),
s 50C(1)(e), s 50F(3)(i) and s 50J(3); have a lawyer review the forks (especially F1, F3, F5, F8); add the
institution's seat (ss 50E, 50J(4), (7), 50R(6)); run an independent test pass.
