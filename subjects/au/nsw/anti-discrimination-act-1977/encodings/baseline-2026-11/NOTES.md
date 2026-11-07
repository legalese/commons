# Anti-Discrimination Act 1977 (NSW) -- baseline encoding, the person with the complaint

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025
> (corpus document dated 1 July 2024). It is unofficial and may be out of date: amendments after that version are
> missing (the complaint time limit and the sexual harassment and religious provisions have been the subject of
> amendment since). Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 in substance. A seat-neutral core
(`ada-core.l4`) holds every rule, with four regulative rules (the complainant's steps that have time limits: lodging
within 12 months of the conduct, requiring referral within 21 days of a decline, applying to register a conciliation
agreement within 6 months, reviving an abandoned complaint within 12 months after the 28 days), each run by
`EVALTRACE` inside a function that takes only plain facts. The seat layer (`ada-seat.l4`) asks the questions and
restates no rule. Dates sit in one small module (`ada-dates.l4`, built-in date functions only, no daydate, no `YMD`).
No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.

Answers are named outcomes (enumerations, some carrying the section as text) or dates and amounts, not
`MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used. Where the text says no in its own words (a definition introduced by
"discriminates ... if", "sexually harasses ... if", "do not apply to employment", "nothing in this Division renders
unlawful", "unless", "is not liable", "may not", a closed list such as s 87A(1)) the outcome begins "no"; where a
provision's scope is not met and the text has no "only" (s 50, s 53, Part 4E's s 49ZU, s 22B's list of relationships)
it says the section "does not reach this". Judgments the Act leaves to the President, the Tribunal or a court are
inputs. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The Civil and Administrative Tribunal Act 2013
baseline (`subjects/au/nsw/civil-and-administrative-tribunal-act-2013/encodings/baseline-2026-11/`) holds the Tribunal's
own procedure; the stable `l4` cannot IMPORT across subjects, so the two are not linked in code.

## Edition

- **Act:** Anti-Discrimination Act 1977 No 48, corpus document `nsw_legislation:2024-07-01/act-1977-048` (in force
  1 July 2024), deposited at `../../registers/source-bundle/act-1977-048.txt` (sha256 of the deposited text
  c16a7666...a11c18, as recorded in its `.meta.json`), from the Open Australian Legal Corpus (collected 10 March 2025)
  because legislation.nsw.gov.au returned a bot challenge. Not the authorised text.
- **Not deposited:** amendments after 1 July 2024; the Anti-Discrimination Regulation (no regulation sets a number the
  encoded sections use; the prescribed jobs, offices and drugs it may name are folded into inputs).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ada-dates.l4` | 0 | 0 | 0 | 0 |
| `ada-core.l4` | 0 | 0 | 0 | 0 |
| `ada-seat.l4` | 0 | 0 | 0 | 0 |
| `ada-cases.l4` | 0 | 0 | 186 | 186 |

Negative control, in a scratch copy: with the small-employer exclusion raised from 5 to 6 employees and the 12-month
complaint period lengthened to 13 months, the cases failed 7 assertions: the 6-employee case, the three last-day dates,
and the complaints lodged on 11 March 2026, 2 June 2026 and 1 March 2025. (Eight were predicted; the eighth, the
complaint of 1 June 2026, stays "partly late" under 13 months as well, so the prediction, not the encoding, was wrong.)

Every expected value was worked by hand from the text, with weekdays and day counts checked against a calendar
independently of the encoding and written beside the cases. Edges: 5 and 6 employees; each exclusion on the grounds it
reaches and on those it does not; the inherent requirements exception for hiring and dismissal and not for terms or
other detriment; under 21 for an offer, for terms and for dismissal; the 12-month day and the day after, from
29 February; the 21 days by hand and by post (a Monday, a Friday and a Saturday posting, and a weekday holiday); the
18-month day and the day after, from 31 August; 6 months from 31 August; 28 days plus 12 months from 1 February 2024;
$100,000 and $100,001.

## Seat

**The person with the complaint (required)** (`ada-seat.l4`, 19 questions): the job applicant, employee, contractor or
other worker who was discriminated against, sexually harassed, victimised or retired because of age, and who complains
to the President of the Anti-Discrimination Board and may go on to the Civil and Administrative Tribunal. Questions:

- Discrimination at work: "Was what my employer did unlawful discrimination?"
- Sexual harassment at work (situation): "Was I unlawfully sexually harassed at work?"
- Forced retirement (situation): "Can I be made to retire because of my age?"
- Victimisation (situation): "Was I unlawfully victimised?"
- "Is my employer liable for what its employee did?"
- Making a complaint: "Can this complaint be made?", "By when must I lodge my complaint?", "Is my complaint in time?"
- After a decline (situation): "By when must I require referral to the Tribunal?", "Did I require referral in time?"
- Unresolved after 18 months (situation): "From when can I ask for referral?", "What happens to my request?"
- After a conciliation agreement (situation): "By when must I apply to register it?", "Can I register it?"
- After abandonment (situation): "By when can I revive my complaint?", "Can it be revived?"
- What the Tribunal may award (situation): "The most for my loss", "The most for a failure to comply", "Will the
  damages be paid to me?"

Provisions addressed to the President or the Tribunal are encoded as what they mean for that person: a ground on
which the complaint may be declined, a step they may require, a referral that must or must not follow, a cap.

No seat for the respondent (an employer's layer would be welcome: the exceptions, s 53(3) and the onus in s 104 are its
case) and none for the President, the Board or the Tribunal.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no regulation sets a number used.
- **The actors the text names.** Followed: the aggrieved person, the perpetrator, the employer, the principal, the
  employee or agent, the complainant, the respondent, the representative body, the President, the Tribunal, the
  Minister.
- **Judgments answered conditionally.** Followed: "less favourably ... in circumstances which are not materially
  different", "on the ground of", "not reasonable having regard to the circumstances", "substantially higher
  proportion", "genuine occupational qualification", "inherent requirements", "unjustifiable hardship" (s 49C, s 49U),
  "reasonably necessary to protect public health", the superannuation tests, "a reasonable person ... would have
  anticipated", "authorise", "all reasonable steps", "sufficient interest", "reasonable prospects of a conciliated
  agreement", the three s 92C(2) matters, and the Tribunal's assessment of loss are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "discriminates" on each ground (ss 7, 24,
  38B, 39, 49B, 49T, 49ZG, 49ZYA), "disability" (s 4, s 49A), "responsibilities as a carer" (s 49S), "transgender"
  (s 38A), "homosexuality" (s 49ZF), "sexually harasses" (s 22A), the s 22B relationships. Asked: "relative" and
  "associate" (s 4, glossed), "workplace participant" (s 22B(9), glossed), "private educational authority" (s 4,
  glossed), "related body corporate" (Corporations Act), "prohibited drug" (Drug Misuse and Trafficking Act),
  "protected defendant" and "offender in custody" (Civil Liability Act).
- **One case:** one complaint by one person against one employer or respondent, about one ground.
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** ss 1, 2, 5; Part 8 (the Board); Part 9 Division 4; Parts 9A, 9B, 10; Schedules.

## Scope

**In:** s 4 definitions used; s 4A (one of several reasons is enough, glossed); the definition of discrimination on all
eight grounds (ss 7, 24, 38A, 38B, 39, 49A, 49B, 49S, 49T, 49ZF, 49ZG, 49ZYA); discrimination against applicants and
employees on each ground (ss 8, 25, 38C, 40, 49D, 49V, 49ZH, 49ZYB) with their exclusions (private household, 5 or
fewer employees, private educational authority); the exceptions that reach those sections (ss 14, 15, 16, 21, 31, 35,
36, 38Q, 46, 49, 49D(4), 49P, 49PA, 49Q, 49V(4), 49ZYI, 49ZYJ, 49ZYK, 49ZYR, 49ZYS, 54, 56); Part 2A s 22A and s 22B(1)-(7);
Part 4E (ss 49ZU, 49ZV, 49ZX; s 49ZW in the answer's words); Part 5 s 50 and s 53; Part 9 ss 87A, 87C, 89B(2)(b), 91A(5)-(9),
92C, 93A, 93B, 94B, 96(1), 108(2)(a), (4), (5), (7), 111A, 112 (s 104's onus glossed).

**Out, and why:**

- **Discrimination in other areas** (Division 3 of each Part: education, goods and services, accommodation, registered
  clubs) and **the other work relationships** (commission agents, contract workers, partnerships, councillors,
  industrial organisations, qualifying bodies, employment agencies: ss 9-13, 26-30, 38D-38J, 41-45, 49E-49K, 49W-49ZC,
  49ZI-49ZN, 49ZYC-49ZYH). A second pass should add them; they follow the same pattern with their own exceptions.
- **Vilification** (Divisions 3A, 5 and Parts 4BA, 4C Division 4, 4F) and vilification complaints (s 88): not
  employment claims, and they turn on a "public act".
- Part 2A ss 22B(8), 22C-22J (harassment of members of Parliament, and in other areas); s 22E(3) (finding 1).
- s 51 (advertisements, an offence) and s 52 (aiding and abetting): the first is not a complaint matter (s 87A(1)); the
  second makes the helper liable, a respondent's question.
- Exceptions that do not reach a work claim (sport, insurance, credit, licensing, the welfare of children, charities,
  voluntary bodies, aged housing, adoption: ss 22, 37, 38P, 49R, 49ZYQ, 49ZYT-49ZYX, 55, 57, 59, 59A) and the Part 4A,
  4G "prescribed lawful" regulation powers.
- The President's handling of a complaint that gives the complainant no step or deadline: ss 87B, 88A-88C, 89, 89A,
  89B(1), (3), (4), 90-90C, 91, 91A(1)-(4), 91B, 91C, 92, 92A, 92B, 93, 94, 94A, 94C; the Tribunal's procedure: ss 95,
  96(2), 98-105, 108(1), (2)(b)-(g), (3), (6), 109, 113-116.

## Forks (the text does not say; one reading taken)

- **F1** A period of months "after" a day (s 89B(2)(b), s 91A(6), s 92C(2), s 93B(1)) ends on the same day of the
  month that many months later, or that month's last day where it is shorter. Conduct on 29 February 2024 is "more
  than 12 months before" a complaint made on 1 March 2025 and not one made on 28 February 2025.
- **F2** "within 21 days after the date" (s 93A(1)) and the "28 days" of s 92C(1) do not count the day itself.
- **F3** s 94B(1): a period that "is ... taken to run from, and includes, the seventh working day after the notice was
  posted" ends on that working day plus 20 days. Public and bank holidays "in the place to which the notice was
  addressed" are an input (the number falling on weekdays in the count); the s 94B "evidence sufficient to raise
  doubt" proviso is not modelled.
- **F4** s 93B(1): a complaint unresolved "within 18 months after the date on which it was made" can be the subject
  of a request from the next day.
- **F5** s 89B(2)(b) is a discretion, not a bar: it is written as a MUST with a LEST BREACH whose reason says only that
  the President may decline. A complaint with part of the conduct outside the 12 months is "partly late".
- **F6** Where both an exclusion (s X(3)) and an exception apply, the exclusion is reported; where several exceptions
  apply, the first in the Act's order is named. Either is a complete answer.
- **F7** The genuine occupational qualification for sex (s 31(2), (3)) and for age (s 49ZYJ(2), (3)) is asked as one
  judgment, prescribed jobs included. For sex a married-couple job (s 31(2)(i)) is part of that judgment, not of the
  marital-status input (s 46).
- **F8** s 56 (religious bodies) is asked as one fact covering paragraphs (a)-(d).
- **F9** s 49ZYI (junior employees) is treated as still operating: s 49ZYI(3) ends it on a proclaimed day, and the
  deposited text still prints it.
- **F10** The superannuation exceptions (ss 36, 38Q, 49, 49Q, 49ZYS) are one judgment input, "terms that meet the
  Act's superannuation exception for this ground". s 38Q is worded as "does not discriminate", not as an exception;
  the answer names it as the reason either way.
- **F11** s 53(1) is read literally: the act is attributed to the employer "unless the ... employer did not ...
  authorise" it, so an unauthorised act gives "no" (finding 2).
- **F12** The characteristic must be one the Act defines (disability, carer's responsibilities, transgender,
  homosexuality) for indirect discrimination as well as direct.
- **F13** s 93B(4) is applied only where the respondent asked and the complainant objected, and s 93B(5) only where the
  complainant asked and the respondent objected.

## What the Act turns out to say (findings)

1. **s 22E(3) points to a section that no longer holds orders.** It lets the Tribunal "make any order that it is
   empowered to make under section 113 (1) (b)" and bars damages "under section 113 (1) (b) (i)"; in the deposited
   text s 113 is "Enforcement of orders by the President" and has no subsections. The Tribunal's orders are in
   s 108(2), damages in s 108(2)(a). A cross-reference left behind by an earlier renumbering; not encoded (education).
2. **s 53(1) puts its test in a double negative.** "Is taken to have been done by the principal or employer also
   unless the principal or employer did not ... authorise" reads as liability for authorised acts only, with s 53(3)
   then excusing an employer that took all reasonable steps. Whether "authorise" is wider than its ordinary meaning is
   a question for the Tribunal; the encoding asks it as a judgment and answers literally. Asserted.
3. **s 108(7) default damages survive a Minister's referral.** s 108(2)(a) withholds compensation on a matter referred
   by the Minister under s 95(2), and s 108(2)(c) withholds redress orders, but s 108(2)(b), (d) orders remain, and
   s 108(7) lets the Tribunal order up to $100,000 "to the complainant" in default of compliance with them. Not
   asserted (the failure-to-comply question does not ask who referred the matter).
4. **The exclusions differ by ground.** Race (s 8(3)) and age (s 49ZYB(3)) exclude only a private household; carers
   (s 49V(3)) exclude a household and 5 or fewer employees but not a private educational authority; sex, transgender,
   marital status, disability and homosexuality exclude all three. A race or age claim against an employer of 2 stands;
   a carer's claim against a private school stands. Asserted.
5. **Two race-only exceptions.** s 15 (training for work outside NSW) and s 16 (ship or aircraft, engaged outside
   NSW) are in Part 2 only; no other Part has them. Asserted.
6. **Carers cannot rely on an associate's responsibilities.** Every other definition reaches the characteristic of a
   "relative or associate"; s 49T(1) speaks only of "the aggrieved person having responsibilities as a carer".
   Asserted.
7. **The inherent requirements exceptions are narrow.** s 49D(4) and s 49V(4) reach only s (1)(b) (who should be
   offered employment) and s (2)(c) (dismissal); unfavourable terms, denied promotion or another detriment get no
   inherent-requirements answer. Asserted.
8. **The 12-month limit is a discretion.** s 89B(2)(b) lets the President decline a complaint where "the whole or
   part" of the conduct is older than 12 months, and s 89B(4) makes that decision unreviewable by the Tribunal; a
   complaint about a course of conduct that began more than 12 months ago is at risk even where it continues. Asserted
   ("partly late"). The deposit is the 1 July 2024 version; check for a later change to the period.
9. **Posting changes the count.** By hand the 21 days run from the day after the notice; by post they run from and
   include the seventh working day after posting, so the last day is the 20th day after that working day (posted
   Monday 3 November 2025: seventh working day 12 November, last day 2 December 2025, against 24 November by hand).
   Asserted.

## Before relying on it

- Check the deposited text against the authorised text on legislation.nsw.gov.au, and look for amendments after
  1 July 2024 (the complaint period in s 89B, Part 2A, the religious and exceptions provisions, and s 49ZYI).
- Add the other work relationships and the other areas (Division 3 of each Part), and a respondent's (employer's)
  layer.
- An independent test pass and the human gates.
