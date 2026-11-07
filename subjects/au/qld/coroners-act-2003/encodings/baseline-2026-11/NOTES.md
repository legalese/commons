# Coroners Act 2003 (Queensland) -- baseline encoding, the family of the person who died

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

This is the first encoding of this subject; nothing existing was touched. Nine files:

| File | What it holds |
|---|---|
| `coq-common.l4` | dates (built-in date functions, no daydate), the regulative vocabulary and its EVALTRACE helper, schedule 2 "family member"; 1 question |
| `coq-deaths.l4` | part 2 (ss 7, 8, 8A, 9, 10, 10AA) and part 3 division 1 (ss 11, 11AAA, 11A, 12(1)); 6 questions |
| `coq-body.l4` | part 3 division 2 (ss 19(5), (6), 20(3)-(5), 21(3)-(5), 23A, 24(4)-(9), 26(2)(f), (3), (4)) and s 95, with the s 24(6) regulative rule; 10 questions |
| `coq-inquest.l4` | part 3 division 3 (ss 27-30, 36, 39, 45, 46, 46A, 50, 51(2)), with the s 30(3) regulative rule; 11 questions |
| `coq-access.l4` | part 3 divisions 4 and 5 (ss 52, 54-57, 59-62A); 3 questions |
| `coq-cases-*.l4` | the worked cases, one file for each of the four rule modules (the family member cases are with the deaths cases) |

Each exported question calls a rule defined beside it and named by section, so that a later seat layer (a witness, a
doctor, a service provider) can import the rules. The two duties with a numbered deadline (s 24(6): at most every 6
months; s 30(3): within 6 months or the longer period) are regulative rules (`PARTY the coroner MUST ... WITHIN ... LEST
BREACH ... BECAUSE`), run by `EVALTRACE` inside exported questions that take only plain facts. The other deadlines
("immediately" in s 7(3), "as soon as reasonably practicable" in s 26(3)) have no number and are stated in the answers.
The 14-day application windows (ss 11A(4), 30(5), (7)) are periods for the person's own application, not duties, and are
date arithmetic.

## Edition

- **Act:** Coroners Act 2003 (Qld), Act No. 13 of 2003 (`act-2003-013`), the version in force from 29 October 2026,
  current on 6 November 2026, deposited at `../../registers/source-bundle/act-2003-013.txt` (text sha256
  `6b85fcaefc15d55b7f51a33def8b96803e923e9e83f14348bf9b12c636fbd853` per its `.meta.json`; a Windows checkout with CRLF
  line endings hashes differently). A plain-text conversion of the Queensland Legislation HTML view, not the authorised
  PDF.
- **Numbers set elsewhere:** none needed. The Act's own numbers are used: 14 days (ss 11A(4), 30(5), (7)), 6 months (ss
  24(6), 30(9)), 2 days (s 20(3)), 28 days (ss 32(2), 34(3), not encoded), and the maximum penalties in penalty units
  (ss 7(3), 55(2), 95(1)). The value of a penalty unit (Penalties and Sentences Act 1992 and Regulation) is not
  deposited, so penalties are stated in units. No Coroners Regulation is deposited; nothing encoded here depends on
  one (the fees of s 99(2)(b) are out of scope).
- **Not deposited and not read:** the Acts Interpretation Act 1954 (Qld), which governs the counting of time; the
  readings taken instead are forks F5-F7.

## Checks

Stable `l4` of the L4 VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), from this folder, `JL4_LIBRARY_PATH`
unset, at most two at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `coq-common.l4` | 0 | 0 | 0 | 0 |
| `coq-deaths.l4` | 0 | 0 | 0 | 0 |
| `coq-body.l4` | 0 | 0 | 0 | 0 |
| `coq-inquest.l4` | 0 | 0 | 0 | 0 |
| `coq-access.l4` | 0 | 0 | 0 | 0 |
| `coq-cases-deaths.l4` | 78 | 78 | 0 | 0 |
| `coq-cases-body.l4` | 54 | 54 | 0 | 0 |
| `coq-cases-inquest.l4` | 63 | 63 | 0 | 0 |
| `coq-cases-access.l4` | 26 | 26 | 0 | 0 |
| **Total** | **221** | **221** | 0 | 0 |

Every exported question has cases, with the edges: the 14th day and the 15th, the day of receipt itself, a year end and
29 February 2028 for the 14-day windows; the last day and the day after for both regulative rules, with 31 August plus
6 months (28 February) and the leap year; each "only if" and "unless" limb on and off. Two `#TRACE` directives show a
breach of each regulative rule (the stable `l4` cannot compare a breached trace with `EQUALS`; the questions use
`CONSIDER ... WHEN FULFILLED`). Expected values were worked by hand from the text, never copied from output.

## Seat

**The family member of the person who died, or another person with a sufficient interest in the death** -- for example
a relative weighing a claim for compensation for a workplace, road, medical or custodial death. "Is the death
reportable? Must I report it? Must a coroner investigate, and which one? Can I object to an internal autopsy, watch it,
or ask for a test? When will the body be released, with or without organs kept? May we bury or cremate? Must there be
an inquest; can I ask for one, and by when must the coroner decide? Can I take part? Will I get the findings, and can I
use them or a witness's evidence in my claim? Can I have a finding set aside? Can I see the documents and the exhibits,
and get the property back?" For s 7 the seat is any person who becomes aware of the death; for ss 59-62 it is the
owner of the property, including the personal representative of the person who died.

No seat is written for a coroner, the State Coroner, the Coroners Court, the District Court, the police, the Minister
or the Attorney-General. Their duties appear as what the person in the seat must be given, may ask for, and by when.
A witness seat (ss 16, 17A, 37, 39 from the witness's side) and a seat for a doctor or service provider (ss 7(2), 22,
24A, 25, 26(5)) would be natural further layers.

The 2026-10-18 defaults:

- **The Act alone.** No instrument sets a number the encoded sections use. The Acts the definitions borrow from
  (Disability Services Act 2006, Mental Health Act 2016, Forensic Disability Act 2011, Child Protection Act 1999, NDIS
  Act, Coal Mining Safety and Health Act 1999, Petroleum and Gas (Production and Safety) Act 2004, Public Health Act
  2005, Transplantation and Anatomy Act 1979, Voluntary Assisted Dying Act 2021) are named, not encoded.
- **The actors the text names:** the coroner, the State Coroner, the Mining and Resources Coroner, the Coroners Court,
  the District Court, the Minister, the Attorney-General, the doctor, the relevant service provider.
- **Judgments handed to others are answered conditionally:** every "considers", "is satisfied", "reasonably believes"
  and "sufficient interest" is an input, as is the s 10AA "independent person" and the s 30(9)(b) longer period.
- **The Act's own definitions are worked out from facts:** reportable death (s 8), unnatural death (s 8A, an
  "includes": its limbs or the asked fact), death in care (s 9, as a choice among its heads), death in custody (s 10,
  with "custody"), health care related death (s 10AA), mining related reportable death (s 11AAA(3)), family member and
  not reasonably available (sch 2), prescribed tissue (s 24(11), in the input's wording), physical evidence and owner
  (ss 59(3), 60(3)), derivative evidence (s 39(5)). **Borrowed terms are asked:** spouse, disability, NDIS participant,
  specimen tissue, the notifiable conditions, coal mine, mine, petroleum and gas site, mining related injury (s 11AAA(4),
  whose heads are all terms of other Acts).
- **One case:** one death.
- **The Act's own terms**, quoted in the comment above each rule and glossed in the `@desc` lines and the choices.
- **Machinery out** (Scope).

## Scope

**In:**

- Part 2: ss 7(1)-(3), (7), 8, 8A, 9 (its heads as choices; s 9(3) and (4) folded into the glosses), 10, 10AA.
- Part 3 division 1: ss 11(2), (3), (4) (directions as inputs), (7), 11AAA(1), (3), (4), 11A, 12(1).
- Part 3 division 2: ss 19(1), (5), (6), 20(3)-(5), 21(3)-(5), 23A, 24(4)-(9), 26(2)(f), (3), (4).
- Part 3 division 3: ss 27, 28(1), 29, 30, 36, 39, 45(3)-(5), 46(1)-(3), 46A, 50, 51(2) (s 50B named in an answer).
- Part 3 division 4: ss 52, 54(1)-(4), (7), 55, 56, 57. Division 5: ss 59-62A.
- Part 5: s 95. Schedule 2: family member, not reasonably available.

**Out, and why:**

- Part 1, s 98, s 99, Part 6 (machinery, regulation-making, transition); Part 4 (the court and the coroners' offices),
  Part 4A (the Domestic and Family Violence Death Review and Advisory Board: an official body, nothing for the family
  to ask), ss 92-94, 97 (registers, databases, evidentiary aids, notices between officials).
- ss 7(4)-(6), 10A, 14, 15, 18, 18A, 25(4)-(6), 47, 47A, 48, 49, 54AA-54C, 58, 63, 63A (duties between officials).
- s 11AA (preliminary examinations): its s 11AA(5)(b) duty to consider a family member's concern mirrors s 19(5)(b) and
  could be added the same way; left out to keep the baseline to the autopsy itself.
- ss 12(2)-(4) (when the coroner stops: the coroner's decision, used as an input in ss 19 and 45), 13, 19(2)-(4),
  (7)-(9), 20(1), (2), (6)-(8), 21(1), (2), 23, 24(1)-(3), (10), 26(1), (2)(a)-(e), (6) (the coroner's own powers and
  the other paths of release).
- ss 16, 17, 17A, 22, 24A, 25(1)-(3), 26(5), 37, 41 (duties and protections of witnesses, doctors and the public:
  other seats).
- ss 31-35, 38, 40, 42-44 (inquest procedure with no answer the family could be given beyond s 36).
- ss 45(1), (2), (6), (7), 46(4) (what the findings contain: the s 45(2) matters are used in s 52), 50A, 50B (the
  coroners' own initiative), 51(1), (3), 53 (research access, not this seat), 54(5), (6) (police access), 96 (for a stillborn
  child only ss 12(2)(c), 19, 25(1)-(3), 26(2)(c) and 95 apply; the encoding does not ask whether the body is a
  stillborn child's).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 10AA(1), (2) "after the commencement", s 11A(1) "a death that happens after the commencement of this section"
  -- `s 10AA -- a health care related death`, `s 11A -- challenging the reportability decision` -- the death is taken
  to be after both commencements (neither day is in the deposited text) -- an earlier death is outside s 10AA and s 11A
  and would answer "not covered".
- **F2** ss 11(7) and 11AAA(1), both applying "despite" s 11(2) -- `ss 11(7), 11AAA -- which coroner` -- a mining
  related reportable death that is also an unnatural death in custody or in police operations goes to the Mining and
  Resources Coroner (s 11AAA is the later and more specific provision) -- s 11(7) restricts it to the State Coroner, a
  Deputy State Coroner or an approved coroner.
- **F3** s 29(2), (3) against s 27(1) -- `ss 27, 28, 29 -- must there be an inquest` -- a pending charge defers the
  inquest (and is checked before every s 27 head, including a direction or order under s 27(1)(b)-(d)); it does not
  excuse it -- an Attorney-General's direction or a court's order overrides s 29 (s 29 has no "despite").
- **F4** s 36(1) "The following persons may appear" (a list not closed with "only") -- `s 36 -- taking part in the
  inquest` -- "not covered" (NOTHING kind) for a person the court has not found to have a sufficient interest -- "no"
  (JUST FALSE kind), reading the list as the whole right of appearance.
- **F5** ss 11A(4), 30(5), (7) "within 14 days after the person receives the written reasons" -- `the last day of the 14
  days after` -- the day of receipt excluded, the last day is receipt plus 14, no extension when it falls on a weekend
  or public holiday -- the Acts Interpretation Act 1954 (Qld) (not deposited) may extend a last day that falls on a day
  the registry is closed.
- **F6** s 20(3) "at least 2 days notice" -- `Earliest day for the exhumation order question` -- the order may be made on
  the notice day plus 2 -- 2 clear days, plus 3.
- **F7** s 24(6) "at not more than 6-monthly intervals after the date of the order for the autopsy" -- `s 24(6) -- the
  last day of the interval` -- each decision within 6 months after the order (the first) or after the last decision --
  fixed 6-monthly anniversaries of the order, whatever day the last decision was made. "n months after" a day is the
  same day number, or the last day of a shorter month (also for s 30(9)(a)).
- **F8** ss 45(4), 46(2) (the recipient lists of a duty) -- `ss 45(4), 46(2) -- copies of the findings and comments` --
  a person outside the lists is told "the section does not require it" -- "not covered" (NOTHING kind), as an
  unclosed list.
- **F9** s 30(9)(b) "the longer period the coroner considers necessary" -- `s 30(9) -- the end of the prescribed period`
  -- a period the coroner names that ends before 6 months is not "longer", and the 6 months stand -- the coroner's
  period applies whatever its length.
- **F10** s 60(1), (2) -- `ss 59-62 -- return of physical evidence` -- "not lawful to possess" and the guidelines are
  checked before "still required", so the owner of an unlawful item is told it will not be returned even while it is
  still needed -- those answers arise only once the coroner decides the evidence is no longer required.
- **F11** s 7(1)(a) "a death that appears to be a reportable death" -- `s 7 -- the duty to report` -- asked as the
  person's own impression, not computed from s 8 -- the s 8 facts decide it.
- **F12** s 24(4), (5) with s 26(3) -- `ss 24(4), (5), 26(2)(f), (3), (4) -- release after the autopsy` -- the coroner,
  not satisfied of s 24(4)(a) and (b), must return the tissue to the body and then release it -- s 24(4) bars the
  release outright until satisfied, and s 24(5) only adds the return.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "means" and "if" definitions (family member, death in care, death in custody, health care related death,
mining related reportable death) answer no when a limb fails; s 8(1) "only if" and the flat negatives of s 8(4), (5)
give "no" constructors; "this section applies if" (ss 7(1), 39(1)) and "does not apply" (ss 19(1), 59(2)) give "does not
apply" or "no protection" constructors; "only if" (ss 23A(2), 54(3), 62A(2), (3)) and "must not ... unless" (ss 26(4),
95(1)) give "no"; the 14-day periods give "no" once ended (ruling of 2026-11-05 (a)); "includes" (s 8A) falls back to an
asked fact; unclosed lists and silences (s 36(1), s 39 on derivative evidence in a civil claim, s 51(2) on proving that
a finding was made, s 23A for other tests, s 50 for findings without an inquest, release on the other s 26(2) paths)
give "not covered" (NOTHING kind) worded as such. The case-by-case sites are forks F3, F8, F10 and F12.

## What the Act turns out to say

1. **Dictionary entries lost in the deposited text.** Schedule 2 reads "spouse ...", "de facto partner ...", "child in
   a placement with the consent of a parent or guardian ...", "children's commissioner ..." and "health procedure ...".
   The definitions themselves are missing, probably in conversion. "Spouse" is asked as a fact. The deposit should be
   checked against the authorised PDF.
2. **Only the deceased's chosen or highest-ranked relative is the "family member".** Schedule 2 picks one person in
   order (a documented wish, then spouse, adult child, parent, adult sibling). Paragraphs (v) and (vi) are not ranked
   against each other, so a close friend and an ATSI family member can both qualify. Asserted.
3. **Only one family member gets the findings as of right.** Under s 45(4)(a) the copy goes to the family member who
   has said they will accept it for the family. Other relatives get one only if they appeared at an inquest
   (s 45(4)(b)). Asserted.
4. **s 11A has a time limit on only one of its three routes.** An application to the District Court after the State
   Coroner refuses a review must be made within 14 days (s 11A(4)). Applying to the State Coroner (s 11A(2)(a)), or
   straight to the District Court where the State Coroner was the deciding coroner (s 11A(2)(b)), has no time limit.
   The parallel inquest route in s 30(4)(b), (5) does have one (14 days). Asserted.
5. **s 30(9)(b) lets the coroner extend the deadline without limit and without notice.** The "longer period the coroner
   considers necessary" has no ceiling, and nothing requires the applicant to be told of it.
6. **s 50 has no time limit and allows repeat District Court applications.** s 50(3) stops a State Coroner application
   after the District Court has refused, but nothing stops a second District Court application on the same grounds.
   Only the District Court can act on "no evidence" or "not reasonably supported" (s 50(5)(c), (d)). Asserted.
7. **The coroner's findings cannot prove a claimant's case.** The findings must not say anyone is or may be guilty or
   civilly liable (ss 45(5), 46(3)). The record is "not evidence in any court or tribunal of any fact asserted in it"
   (s 51(2)). Asserted.
8. **A witness's compelled evidence cannot be used against them in a later civil claim, but what it leads to may be.**
   s 39(3) bars the evidence itself "in any other proceeding" (perjury excepted). s 39(4) bars derivative evidence
   only "in a criminal proceeding". On derivative evidence in a civil claim s 39 is silent. Asserted as "not covered".
9. **ss 11(7) and 11AAA(1) both apply "despite" s 11(2) and can collide** where a mining death is also an unnatural
   death in custody or in police operations (F2). Asserted on the encoder's reading.
10. **s 29 has no "despite".** s 27(3) makes s 27(1)(b)-(d) apply despite the coroner's own decision, but neither s 27
    nor s 29 says which yields when someone has been charged (F3).
11. **Two commencement days are not in the text** (ss 10AA, 11A). Both sections reach only deaths after their
    commencement (F1).
12. **s 26(3) is tied to s 26(2)(f).** The duty to release "as soon as reasonably practicable after the autopsy" applies
    "for subsection (2)(f)", that is, once the coroner has decided the body is no longer needed. Until then the family
    has no deadline to point to. Asserted.
13. **s 62A(3) and s 54(3) limit the coroner's consent itself** ("may consent only if"). A consent given on neither
    ground does not give access. Asserted.
14. **s 7(3) "immediately" and s 26(3) "as soon as reasonably practicable" carry no number**, so neither is written as a
    regulative rule with WITHIN.

## Before this is worth relying on

- Check the deposited text against the authorised PDF, especially the schedule 2 entries that read "..." (finding 1).
- Settle the commencement days of ss 10AA and 11A (F1) and the counting of time under the Acts Interpretation Act 1954
  (Qld) (F5, F6), and bring that Act in if it is deposited.
- Have a Queensland coronial practitioner review forks F2, F3, F4, F7, F8 and F12.
- Add the preliminary examination (s 11AA(5)), and seat layers for a witness and for a doctor or service provider.
- An independent test pass, and the human gates.
