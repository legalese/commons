# Equal Opportunity Act 1984 (SA) -- baseline encoding, the complainant

UNOFFICIAL. Based on content from the South Australian Legislation website at 6 November 2026; (c) State of South
Australia, licensed under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version (the authorised version is the
register's PDF).

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on
2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`saeo-dates.l4`,
built-in date functions only, no daydate), the rules in `saeo-rules.l4`, and the complainant's questions in
`saeo-seat.l4`, which imports the rules and restates none. The cases are in `saeo-cases.l4`. The date helper and the
trace pattern follow the Work Health and Safety Act 2012 (SA) baseline
(`subjects/au/sa/work-health-and-safety-act-2012/encodings/baseline-2026-11/`); the stable `l4` cannot IMPORT across
subjects, so they are written again here, not shared.

## Edition

- **Act:** Equal Opportunity Act 1984 (SA), the South Australian register's current unauthorised RTF, version 1.4.2025
  (in force from 1 April 2025), retrieved from www.legislation.sa.gov.au on 6 November 2026 and deposited at
  `../../registers/source-bundle/equal-opportunity-act-1984.txt` (text sha256 0251b7e8...b4cd per the meta, checked with
  line endings normalised). Unlike the SA texts taken earlier from the Open Australian Legal Corpus (collected 10 March
  2025), this one comes from the official register; the register's Current Titles list of 22 September 2026 gave it as
  current. It may still have been amended since: check legislation.sa.gov.au before relying on anything here.
- **Regulations:** none deposited. The Act's own numbers (12 months, 3 months, 1 month) need none. The regulations may
  prescribe a class of assistance animal (s 5(1)), sporting circumstances (s 48(d)), a class of person whose help is
  evidence of domestic abuse (s 95A(4)(b)(iii)) and exemptions (s 106(2)(b)); each is asked as a fact, and a regulation
  would change the answers only through that fact.
- **Borrowed terms asked as facts:** assistance animal (by the Dog and Cat Management Act 1995), domestic abuse (by the
  Intervention Orders (Prevention of Abuse) Act 2009), registered health practitioner, unfair dismissal proceedings
  under the Fair Work Act 1994 (SA) Chapter 3 Part 6 and the Fair Work Act 2009 (Cth) Part 3-2, award or agreement under
  the Fair Work Act 1994.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; two
deliberately wrong assertions (a complaint lodged the day after the 12 months, a referral notice the day after the 3
months, each asserted in time) were run once in a scratch file in this folder (deleted) to confirm that a failure shows
as `DiagnosticSeverity_Error`, "assertion failed". Satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `saeo-dates.l4` | 0 | 0 | 0 | 0 |
| `saeo-rules.l4` | 0 | 0 | 0 | 0 |
| `saeo-seat.l4` | 0 | 0 | 0 | 0 |
| `saeo-cases.l4` | 0 | 0 | 224 | 224 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the
s 93(2) last day and the day after (15 / 16 March 2026; 28 February / 1 March 2025 from 29 February 2024), a lodging
before the act, and a late lodging the Commissioner extended; the s 96B(2) month (28 February / 1 March 2026 from 31
January; 15 / 16 July from 15 June); the s 95B(1)(c) 3 months (28 February / 1 March 2026 from 30 November 2025); the
s 95A(3) 12 months (1 / 2 July 2026); every limb of every criteria section, each with the fact that defeats it; each
position against an act its section lists and one it does not; each exemption against a ground it reaches and one it
does not.

## Seat

**The complainant** (`saeo-seat.l4`): the person who is discriminated against, sexually harassed or victimised at work or
in seeking work -- a job applicant, an employee (including an unpaid worker or a non-judicial office holder, s 5(1)), a
commission agent, an independent contractor, a contract worker, a partner or a person seeking any of those positions --
and who complains to the Commissioner for Equal Opportunity and takes the complaint on to SAET or the Tribunal. "Was I
discriminated against on this ground?", "Is it unlawful, or does an exemption cover it?", "Was it sexual harassment, and
was it unlawful?", "Was I victimised?", "Is my employer liable for its employee?", "Can I complain, and by when?",
"Can the Commissioner decline it, and can I still get it heard?", "Where will it be heard, and what can be ordered?",
"Can I appeal?", "Does my unfair dismissal claim shut this one out?". No seat for the employer, principal or firm (a
natural further layer, `saeo-seat-employer.l4`), and none for the Commissioner, SAET, the Tribunal or the Supreme Court:
their opinions, satisfactions and findings are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no regulation is needed for a number (see
  Edition).
- **The actors the text names.** Followed: the person aggrieved, the employer, the principal, the firm, the employee and
  agent, the educational authority, the Commissioner, SAET, the Tribunal, the Supreme Court.
- **Judgments answered conditionally.** Followed: "less favourably than ... would treat" (s 6(3)), "a substantial reason"
  (s 6(2)), "not reasonable in the circumstances" (the criteria sections), "unreasonable" (s 66(d)), "genuine
  occupational requirement" and every other exemption's conditions, "reasonable person ... would have anticipated"
  (s 87(9)), "reasonable to expect" and "reasonable steps" (ss 87(7), 91), "reasonably asserted", "false allegation" and
  "good faith" (s 86), the Commissioner's opinions and satisfactions (ss 93(1)(c), 93(2a), 95A, 95B), what the Tribunal
  determines (s 96) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: disability (s 5(1)), caring responsibilities
  (s 5(3), (4)), unfavourable treatment and acting on a ground (s 6), the criteria for every ground (ss 29, 51, 66, 85A,
  85T), sexual harassment and working with (s 87(9)), victimisation (s 86(2), (3)) are worked out from facts.
- **One case.** One act (or series of acts) against one person, one complaint.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 5(1) (disability; employee, employer and employment so far as they bear on positions, in glosses), s 5(3),
(4); s 6(2)-(4); the criteria sections ss 29, 51, 66, 85A, 85T; the work Divisions in full: Part 3 Division 2 (ss 30-34),
Part 4 Division 2 (ss 52-56), Part 5 Division 2 (ss 67-71), Part 5A Division 2 (ss 85B-85F, with s 85EA), Part 5B
Division 2 (ss 85U-85Z); the general exemptions of each Part so far as they can reach work (ss 45, 47, 50, 64, 65,
79, 79A, 80, 82, 84, 85N, 85P, 85ZI-85ZM, 85ZN, 85ZO) and a s 92 exemption; s 86; s 87(1), (7), (9); ss 90, 91; Part 8:
s 93(1)-(2b), (4), s 95A, s 95B(1)-(3), s 96(1)-(3b), s 96B, s 98A(1)-(3)(b); s 100(2)-(5).

**Regulative rules:** four, each run by EVALTRACE inside a question that takes only plain facts: the s 93(2) complaint
(`PARTY the complainant MUST lodge the complaint WITHIN` the days to the 12-month day, `LEST BREACH ... BECAUSE`), inside
`Is my complaint in time` and `Can I make the complaint`; the s 96B(2) review application, inside `Can I apply for review
of the refusal`; the s 95B(1)(c) written notice requiring referral, inside `Must the Commissioner refer my complaint`;
the s 95A(3) request to proceed, inside `Can my declined complaint be reinstated`.

**Exported questions (30):** `Is my condition a disability`; `Do I have caring responsibilities`; `Was I discriminated
against on this ground`; `Does the religious school exemption cover my job`; `Does the pregnancy exemption cover it`;
`Is the discrimination against me at work unlawful`; `Is the compulsory retirement term void`; `Was it sexual
harassment`; `Was the sexual harassment at work unlawful`; `Was my employer's failure to protect me unlawful`; `Was I
victimised`; `Is the employer liable for its employee or agent`; `Is the person who helped liable too`; `By when must I
lodge my complaint`; `Can the Commissioner extend my time`; `Can I make the complaint`; `Is my complaint in time`; `By
when must I apply for review of the refusal`; `Can I apply for review of the refusal`; `Can the Commissioner deal with my
complaint now`; `Could the Commissioner decline my complaint`; `Can my declined complaint be reinstated`; `By when must I
require referral of my declined complaint`; `Must the Commissioner refer my complaint`; `Where will my complaint be
heard`; `Can the tribunal make this order`; `Can I appeal to the Supreme Court`; `From when does my appeal time run`; `Am
I barred from a discrimination claim about my dismissal`; `Am I barred from an unfair dismissal claim`.

**Out, and why:**
- Part 1 ss 1, 7; Part 2 (the Commissioner's office, staff, functions, reports, delegation); Part 6A (practice
  guidelines, not binding, s 91B); Part 7 (how the Tribunal grants exemptions; a granted exemption is an input); ss 104,
  106: machinery.
- Divisions 3 to 6 of Parts 3, 4, 5, 5A and 5B (associations, qualifying bodies, education, land, goods and services,
  accommodation, superannuation) and the exemptions that only reach them (ss 35(2)-(3), 37(3), 38(2), 39(2), 40(3)-(4),
  48, 49, 63(2), 81, 85, 85M, 85O, 85Q, 85R): the focus is the claimant at work. The criteria sections, which every
  area uses, are in; a later layer could add each area as a further "unlawful" question over them.
- s 86A (conversion practices, defined by another Act), s 87(2)-(6g) and (8) (harassment in education, in goods,
  services and accommodation, by judicial officers, members of Parliament and councils, by qualifying bodies and
  associations), ss 87A, 87B, 88A, 89: outside work. s 88: (a) is a civil "unlawful" rule that reaches work too (a
  co-worker's contravention goes to SAET under s 95B(2)(b)), and (b) adds an offence; it is not a separate question
  here because the work question already covers unfavourable treatment because of an assistance animal (s 66(e) through
  the work Division), and s 88 is named in the forum question. A later layer could add "Was separating me from my
  assistance animal unlawful" over s 88(a).
- s 93(1a)-(1b) so far as binding a consenting person, (2c) (secondary students), (3), (5), (6), s 93AA (complaints
  against judicial officers and members of Parliament), ss 93A, 94, 95 (inquiries, investigation and conciliation
  powers, and the offences for not producing documents or attending), 95C, 95D, 96(6), 96A, 96C, 97, 98, 98A(3)(a), (c),
  (d), 98B, 98C, 99, 102, 103: the Commissioner's and the tribunals' powers and procedure, offences, and appeals
  procedure. s 99 (no other sanction) is stated in no question; it would answer every "what else can happen to them"
  with no.
- s 100(1), (6): (1) says only that nothing prevents an unfair dismissal claim; (6) is the Commissioner's role.
- Appeals from SAET (as distinct from the Tribunal) on a matter referred under s 95B(2): s 98A speaks only of "the
  Tribunal"; the route from SAET is in the South Australian Employment Tribunal Act 2014, not encoded here.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 12 months of the last of those acts" / "of the date on which the contravention is alleged to have been
  committed" (s 93(2)), "within 12 months after the date of that determination" (s 95A(3)), "within 3 months of being
  notified" (s 95B(1)(c)), "within 1 month after notification" (s 96B(2)) -- `the date ... months after` -- the day
  itself excluded, so the last day is the same day of the month that many months later; a day the later month lacks
  falls on its last day (29 February + 12 months = 28 February; 30 November + 3 months = 28 February) -- the Acts
  Interpretation Act 1915 (SA), not deposited, may differ at month ends.
- **F2** s 5(4) "immediate family member ... includes" -- `s 5(3) -- I have caring responsibilities` -- a relative outside
  the list who needs care: NOTHING -- JUST FALSE, reading the list as closed.
- **F3** ss 34(1)(a), 56(1)(a), 71(1)(a), 85F(1)(a), 85Z(1)(a) "an employer employing a person for purposes not
  connected with a business" -- `the not-connected-with-a-business exemption can reach` -- read to cover the applicant
  for that employment as well as the employee; (b) reaches only independent contractors, not commission agents -- only
  the employee.
- **F4** s 87(1) -- `s 87(1) -- the sexual harassment at work was unlawful` -- the "while in attendance ... or in
  circumstances where" limb failing: JUST FALSE; not harassment, or neither working together nor seeking to: NOTHING (a
  prohibition limited in its own wording; other subsections may reach it) -- JUST FALSE for all.
- **F5** s 87(7) -- `s 87(7) -- my employer's failure to prevent further harassment is unlawful` -- a duty whose "if" is
  unmet (not reported, or no reasonable expectation of more): JUST FALSE -- NOTHING.
- **F6** s 91(3)(b) "including (i) ... and (ii) ..." -- `s 91 -- they are vicariously liable` -- (i) and (ii) read as
  required parts of the reasonable steps for the (3) defence; (2) stands alone as the general defence -- (i) and (ii) as
  examples only.
- **F7** s 93(1), (1c) -- `s 93 -- the complaint may be made` -- a complainant who is neither aggrieved nor a
  representative: NOTHING (a list not closed by "only"); a complaint not in writing, without the details, or not lodged
  with the Commissioner (a bare "must" not done): JUST FALSE -- JUST FALSE for the first; NOTHING for the second.
- **F8** the exemptions -- `the exemption ... reaches` -- each exemption's conditions are one input (except s 34(3)/85Z(2)
  and s 85Z(3), which have their own questions); s 85ZJ ("This Part does not render unlawful the granting to women of
  rights or privileges in connection with pregnancy or childbirth") read to reach every Part 5B ground; s 50 (religious
  bodies) read to reach work under Part 3, and s 85ZM only for ordination, appointment and training of clergy and members
  of religious orders -- s 85ZJ only for pregnancy; s 50(1)(ba), (c) not reaching employment.
- **F9** s 6(2) -- `ss 6, 29, 51, 66, 85A, 85T -- they discriminated against me` -- "a substantial reason" is required of
  every limb that says "because of" or "on the basis of" (the requirement limb included); not of the limbs that are a
  failure or a requirement to do something (ss 29(2a)(d), 66(ca)(i), (d)(i), 85T(7)(b)) -- the requirement limb's
  causation being the requirement itself.
- **F10** s 6(3) -- the same function -- the comparator applies to the limbs that say "treats ... unfavourably"; not to
  ss 29(2a)(d), 66(ca)(i), (d)(i), 85T(7)(b), which say "requires" or "fails to provide" -- the comparator for every limb.
- **F11** s 29(2a)(d) -- the same function -- "requires a person of a particular gender identity to assume
  characteristics of a sex with which the person does not identify": "the person" read as the person required -- the
  person requiring.
- **F12** s 85T(7)(b) -- the same function -- "requires a person to alter the person's appearance or dress and that
  appearance or dress is required by, or symbolic of, the other's religious beliefs": "the other" read as the person
  required to alter -- a third person.
- **F13** s 85U -- `Part 3-5B Division 2 -- the discrimination at work is unlawful` -- association with a child, which
  s 85U leaves out of Division 2: NOTHING (a scope limit with no "only") -- JUST FALSE, reading s 85U as closing the
  Division.
- **F14** s 86(2), (3) -- `s 86 -- I was victimised` -- (3)(a) "has made a false allegation" read as the allegation being
  in fact false; "reasonably" read only into (d); the ground being knowledge, intention or suspicion is folded into the
  one "what I did" input -- (3)(a) as the discriminator's belief that it was false.
- **F15** s 95A(1)(d) with (4) -- `s 95A(1) -- the Commissioner may decline my complaint` -- any of the (4) kinds of
  evidence is sufficient; a "prescribed" class asked as a fact (no regulations deposited) -- the Commissioner's view of
  sufficiency as a further input.
- **F16** s 95B(1) -- `s 95B(1) -- the Commissioner must refer my complaint` -- a complaint still in conciliation or
  resolved: NOTHING (the duty has not arisen) -- JUST FALSE.
- **F17** s 96 with s 95B(3) -- `s 96 -- the tribunal may make the order` -- SAET, on a matter referred to it, read as
  having the s 96 orders ("may be determined by SAET in accordance with this Act") -- SAET's own Act's powers.
- **F18** s 98A(3)(b) -- `s 98A(3)(b) -- the day my appeal time runs from` -- where (3)(b) does not apply: NOTHING (the
  start is in s 71 of the SACAT Act, outside the sources) -- the decision day.
- **F19** s 100(4) -- `s 100(4), (5) -- I am barred from an unfair dismissal claim` -- a claim under the Fair Work Act
  2009 (Cth): NOTHING (the subsection names only the 1994 Act) -- barred, reading the section as a whole.
- **F20** s 85EA -- `s 85EA -- the provision is void` -- a provision of another instrument, or another kind of term:
  NOTHING -- JUST FALSE.
- **F21** s 84 -- `the exemption` e `reaches` g, `Part 3-5B Division 2 -- the discrimination at work is unlawful` -- the
  exemption reaches disability at work, and "in relation to the provision of access to or use of a place or facilities"
  together with the unjustifiable hardship (weighed under s 84(2)) is folded into the one "conditions met" input --
  confining it by the encoding to the s 66(ca) access limbs, or reading it as reaching only Divisions 3-6.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definition of disability (s 5(1)), the "if" definitions of caring responsibilities (s 5(3)),
of discriminating on each ground (ss 29, 51, 66, 85A, 85T), of sexual harassment (s 87(9)) and of victimisation
(s 86(2)), "does not constitute" (s 86(3)), "This Division does not apply" and "This Part does not render unlawful" (the
exemptions), the "if" of ss 34(3), 85Z(3), 87(7), 93(2a), 95A(1), 95A(3) and 100(2), "while" (s 87(1)), "cannot ...
unless" (s 93(1a)), "must be lodged within 12 months" (s 93(2)), "within 1 month" (s 96B(2)), "within 3 months"
(s 95B(1)(c)), "within 12 months" (s 95A(3)), "may not proceed ... until" (s 93(4)), "may not be made against a child"
(s 96(3b)), "does not apply" (s 100(3), (5)) and the s 91(2), (3) defence give `JUST FALSE`. `NOTHING` is answered where a
prohibition or grant is limited by its own wording and the facts fall outside it (the work sections for a position or
act they do not name, no discrimination; s 87(1) without harassment or a work connection; s 90; s 91 outside the course
of employment; s 93(1) for an outsider; s 96 before a contravention is determined; s 98A for another decision or a
non-party), where a list says "includes" (s 5(4)), where a scope has no "only" (s 85U), where the text is silent
(s 85EA for other instruments, s 100(4) for a Commonwealth claim) and where the answer is in another Act (s 98A(3)(b)
otherwise; s 96B with no refusal).

## What the Act turns out to say

1. **Breast feeding and children are outside the work Division.** s 85T(5) defines discrimination on the ground of
   association with a child (breast or bottle feeding an infant, being accompanied by a child), but s 85U applies Part 5B
   Division 2 to every other Part 5B ground and not to this one (s 85ZA does the same for Division 3). A worker treated
   badly for breast feeding has no claim under the work Division as such; they may have one on the ground of sex or
   caring responsibilities. Asserted (NOTHING).
2. **The exemption lists are uneven across grounds.** The equality-measures exemption of Part 5B (s 85ZK) names marital
   or domestic partnership status, caring responsibilities and domestic abuse, but not pregnancy, the identity of a
   spouse or religious appearance or dress; the charities exemption (s 85ZI) leaves out religious appearance or dress;
   and s 85ZJ (rights or privileges for women in connection with pregnancy or childbirth) is an exemption from Part 5B
   only, so it is no answer to a claim of sex discrimination under Part 3. Asserted for each.
3. **The not-connected-with-a-business exemption is narrower for contractors.** ss 34(1)(b), 56(1)(b), 71(1)(b),
   85F(1)(b), 85Z(1)(b) reach "a principal engaging a natural person as an independent contractor", not a commission
   agent; contract workers and partners are never reached. Asserted.
4. **The two halves of s 100 do not match.** (2) bars a claim under this Act after unfair dismissal proceedings under
   either the State or the Commonwealth Fair Work Act are determined; (4) bars only a later claim under the Fair Work Act
   1994 (SA). The saving in (3) turns on why the unfair dismissal claim was dismissed; the saving in (5) needs both the
   claim under this Act dismissed and the unfair dismissal claim unrelated to a ground of discrimination. Asserted.
5. **Two drafting slips in the criteria.** s 85T(7)(b) speaks of requiring "a person to alter the person's appearance or
   dress" that is symbolic of "the other's religious beliefs", with no "other" in the paragraph (F12); s 29(2a)(d)'s
   "the person does not identify" could refer to either person (F11). Both read for the person treated; neither needs a
   comparator (F10). Encoded and asserted.
6. **Indirect pregnancy discrimination needs an actual pregnancy.** s 85T(4)(a) covers "pregnancy or potential
   pregnancy"; (b) and (c) cover only "a pregnant woman". Asserted.
7. **The worker's claim goes to SAET, but the orders are written for the Tribunal.** s 95B(2) sends work discrimination
   and co-worker victimisation and harassment to SAET, and s 95B(3) lets SAET determine it "in accordance with this
   Act"; s 96 and s 98A speak only of "the Tribunal" (SACAT). Read so that SAET has the s 96 orders (F17); the appeal
   from SAET is left to the SAET Act (out of scope).
8. **No cap on compensation.** s 96(1)(a) leaves the amount to the Tribunal ("of such amount as the Tribunal thinks
   fit"), includes injury to feelings (s 96(3)) and requires other awards for the same acts to be taken into account
   (s 96(3a)); none may be awarded against a child, but it may be against whoever is vicariously liable for the child
   (s 96(3b)). Asserted.
9. **The time limit is soft.** The 12 months (s 93(2)) can be extended by the Commissioner even after it has expired, on
   good reason and if just and equitable (s 93(2a)); a refusal is reviewable by the Tribunal if sought within 1 month
   after notification (s 96B). Asserted at each edge.
10. **The employer's duty about outsiders is narrow.** s 87(7) applies only to an employee (not a contractor or agent),
    only to harassment by someone who is not a fellow worker, and only after the employee has reported specific
    circumstances and further harassment by the same person is reasonably to be expected. Asserted.
11. **A declined complaint can still be heard, but only on the complainant's written notice within 3 months.** s 95B(1)(c)
    then obliges the Commissioner to refer it; and a complaint declined for loss of contact or interest can be reinstated
    on a request within 12 months (s 95A(3)). Asserted at each edge.

## Before this is worth relying on

- Check the text against the authorised version on legislation.sa.gov.au, and that version 1.4.2025 is still current.
- Read the Acts Interpretation Act 1915 (SA) for counting months (F1), s 71 of the South Australian Civil and
  Administrative Tribunal Act 2013 for the appeal time (F18) and the South Australian Employment Tribunal Act 2014 for
  appeals from SAET (finding 7).
- Encode the other areas (associations, qualifying bodies, education, land, goods and services, accommodation,
  superannuation) and the rest of s 87 over the same criteria; an employer seat layer.
- A lawyer's view on findings 1, 2, 4, 5 and 7 and forks F3, F8, F9, F10, F13, F17, F19; an independent test pass and a
  human gate.
