# Equal Opportunity Act 2010 (Vic) -- baseline encoding, the person who says they were wronged

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`eoa-rules.l4`), the
dates in a small one (`eoa-dates.l4`, built-in date functions only), and the person's questions in `eoa-seat.l4`, which
imports the rules and restates none. The cases are in `eoa-cases.l4`.

## Edition

- **Act:** Equal Opportunity Act 2010, Act No. 16/2010, Version No. 032, incorporating amendments as at 15 April 2026,
  deposited at `../../registers/source-bundle/equal-opportunity-act-2010.txt` (sha256 bca02743...b248205b since the 2026-11-07 reconversion; encoded from 07154252...d473b10ca, which differs only in the bullets below), a
  plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see that file's `.meta.json` and
  `subjects/au/vic/README.md`). The register showed it as the current version on that day. Not checked against the
  authorised PDF, which was not saved.
- **Numbers set elsewhere:** none. Every number the encoding uses is in the Act: 5 partners (ss 30, 31, 32), 21 years
  (s 28A), 12 months (s 116(a)), 30 days (s 119(3)), 28 days (s 121(5), in a description). No regulations under the Act
  are deposited, and none sets a number these provisions use. The disability standards under the Disability
  Discrimination Act 1992 (Cth), s 160B determinations under the Building Act 1993 and VCAT exemptions under s 89 are asked
  as facts.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `eoa-dates.l4` | 0 | 0 | 0 | 0 |
| `eoa-rules.l4` | 0 | 0 | 0 | 0 |
| `eoa-seat.l4` | 0 | 0 | 0 | 0 |
| `eoa-cases.l4` | 0 | 0 | 189 | 189 |

Every expected value was worked by hand from the text, every exported question at least twice, with the edges: s 116(a)
on exactly 12 months (1 March 2025 to 1 March 2026: not more), the day after, the day before, and from 29 February 2024;
s 119(3) on day 30 (31 May 2026 for an agreement of 1 May 2026), day 31, the day of the agreement, still open on day 30
and closed on day 31, and a request before the agreement; s 28A at 20 and 21; firms of 5 and of 4 partners; the s 21(2)
contract-worker carve-out; the s 104(1)(g) bad-faith proviso on (g) and on another head; each exception inside and just
outside its own area or attribute. The Act's own examples (s 8 ex 1, s 9 ex 2, s 24, s 28 ex 2, s 37) are cases.

## Seat

**The person who says they were wronged** (`eoa-seat.l4`): the individual who says they were discriminated against,
sexually harassed or victimised, chiefly at work -- a job applicant, a person offered employment, an employee, a contract
worker, a person invited to be or who is a partner, a person seeking or holding membership of a union or other industrial
organisation, a person seeking or holding an occupational qualification -- and who may bring a dispute to the Victorian
Equal Opportunity and Human Rights Commission or apply to VCAT. "Was I discriminated against?", "Is it prohibited at work,
or does an exception let them do it?", "Must my employer accommodate my caring responsibilities, or adjust for my
disability?", "Was I sexually harassed, and does the Act reach the person who did it?", "Was I victimised?", "Is the
employer liable for its employee?", "Can I bring a dispute or a VCAT claim, and can the Commission turn it away as late?",
"Is my request for a settlement record in time?".

No seat for the employer, the Commission or VCAT. What they must prove (ss 9(2), 12(6), 13(2), 108(2), 110) is asked as
whether they have proved it; their judgments are asked as facts. The exception questions are asked from the same seat:
"Can my employer rely on this exception against me?". An employer seat could be added beside this one later.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: none is needed; Commonwealth disability standards,
  Building Act determinations and VCAT exemptions are facts.
- **The actors the text names.** Followed: employer, principal, contract worker, firm, partner, industrial organisation,
  qualifying body, religious body, the Commission, the Tribunal (VCAT).
- **Judgments answered conditionally.** Followed: "reasonable", "unreasonably", "proportionate", "substantial reason",
  "genuine occupational requirement", "reasonably necessary", "a reasonable person would have anticipated", "satisfied",
  "considers" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "attribute" (ss 4, 6), "discrimination" (ss 7-9,
  12), "sexual harassment" (s 92), "victimises" (s 104) and the areas of Part 4 Divisions 1 and 2 are worked out;
  "disability", "carer", "parent", "detriment", "disability standard", "post-secondary education provider", "religious
  body" are asked, with the Act's glosses in the `@desc`.
- **One case.** One course of conduct towards one person, by one employer or body.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 4 (attribute, employee, employer, employment, carer, contract worker, principal, as used), 6, 7, 8, 9, 10, 12,
13, 15, 16, 17, 18, 19, 20, 21, 22, 22A, 23, 24, 25, 26, 27, 28, 28A, 29, 30, 31, 32, 33, 34, 35, 36, 37, 75, 76, 82A, 83A,
86, 92, 93 to 102, 103, 104, 105, 106, 107, 108, 109, 110, 113(1), 115, 116, 117, 118 (in a description), 119(3), 120,
121(2), (3) (and (5) in a description), 122, 123(1), 125, 126, 127.

**Regulative rule:** one. s 119(3): the party MUST request a written record of the agreement WITHIN 30 days after the
agreement, LEST breach (the request is out of time; the agreement stays valid, s 119(7)). Run by EVALTRACE inside the
exported question `Is my request for a settlement record in time`, which takes only dates and a yes/no, through a helper in
the shape of the Civil Procedure Act 2010 encoding's.

**Out, and why:**
- ss 1, 2, 3, 5, 14 (purposes, commencement, objectives, Crown): machinery and interpretation.
- ss 10, 11 (motive irrelevant; acting with others or by omission): no fact of their own; in the `@desc` of the
  discrimination question.
- Part 4 Divisions 3 to 8 (education, goods and services and land, accommodation, clubs, sport, local government;
  ss 38-74): outside the focus (discrimination at work). Their sexual harassment counterparts (ss 98-102) are in, because
  Part 6 is short and has one definition. s 13(1)(b) (an exception in another Division) is covered only by the input "has
  an exception been proved".
- Part 5 ss 77-81A, 82, 82B, 83, 85, 87, 88 (pensions, superannuation, charities, religious bodies outside employment,
  legal incapacity, age concessions, special needs): not the exceptions an employer ordinarily relies on against a worker;
  s 88 is in through s 28. ss 89-91 (VCAT exemptions): an input; the 5-year limit (s 89(2)) is the Tribunal's.
- Part 6A (vilification, ss 102A-102G): outside the focus; a vilification claim can still be brought (the dispute question
  accepts it).
- ss 113(2)-(5), 114, 114A, 123(2)-(4), 124 (joint and group disputes, representative bodies): they turn on the
  Commission's or VCAT's satisfaction about other people, or on a body with no seat.
- ss 111, 112 (the Commission's functions and principles), s 119(1), (2), (4)-(7) (who prepares and certifies the record),
  s 121(1), (4)-(7) (the Tribunal's power): powers and procedure.
- Part 9 apart from s 127 (ss 128-144: conduct and outcome of investigations), Parts 10, 11 (practice guidelines, reviews,
  action plans, the Commission and Board): powers of the Commission.
- Part 12 (offences: discriminatory advertising s 182, obstruction, false information): prosecuted by the Commission or
  police, not brought by the person; the dispute question answers NOTHING for an offence alone.
- Parts 13, 14 (general, repeal and transitional): machinery.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 7(2) "includes" -- `s 7(2), (3) -- the treatment was on the basis of an attribute` -- a basis outside (a) to (d)
  and (3): NOTHING (the list is not closed) -- JUST FALSE. Direct discrimination on that basis is then NOTHING too.
- **F2** ss 30(2), 31(3), (4) -- `Part 4 Divisions 1 and 2 -- the discrimination is prohibited` -- a firm of fewer than 5
  partners that discriminates unreasonably: NOTHING (the text permits reasonable discrimination and prohibits nothing) --
  JUST TRUE (the permission implies the prohibition).
- **F3** ss 17, 19, 22, 32 "must not ... unreasonably refuse" -- `ss 17, 19, 22, 32 -- the refusal to accommodate me is
  prohibited` -- a reasonable refusal: NOTHING (the prohibition limited by its own wording) -- JUST FALSE.
- **F4** ss 20, 22A, 33 "must make reasonable adjustments" -- `ss 20, 22A, 33 -- they must make the adjustment` -- an
  adjustment that is not reasonable: NOTHING -- JUST FALSE (ss 23, 34 then give the exception).
- **F5** ss 20(1), 22A(1), 33(1) "This section applies to a person with a disability who ... requires adjustments" -- same
  function -- no disability or no adjustment needed: NOTHING (a scope limit) -- JUST FALSE.
- **F6** permissions without "only": s 27 (not political staff work), s 28A (21 or over), s 29 (not an incentive, or not
  age), s 37 (terms not reasonable) -- their functions -- NOTHING (ruling (c) of 2026-11-05) -- JUST FALSE.
- **F7** ss 105, 106 -- `ss 105, 106 -- I can bring my claim against the person who authorised or assisted` -- the person
  authorised or assisted but no contravention followed: NOTHING (s 106 gives the claim only where it followed) -- JUST
  TRUE, since s 105 is itself in Part 7 and ss 113(1)(a), 123(1)(a) let a person claim a contravention of Part 7 "in
  relation to that person".
- **F8** s 108(3)(a) "must not ... disclose ... unless it is necessary" -- `s 108(3)(a) -- they must not pass my information
  on` -- the "unless" met: JUST FALSE -- NOTHING.
- **F9** s 116(a) "more than 12 months before" -- `the date` n `months before` -- 12 calendar months back to the same day of
  the month, or that month's last day where it is shorter; "more than" is strictly earlier than that day -- 365 days.
- **F10** s 116 "for any of the following reasons" -- `s 116 -- the Commission may decline my dispute` -- none of (a) to (e):
  JUST FALSE (the list read as closed; (e) is a catch-all) -- NOTHING.
- **F11** s 120(1) "after notifying the other party in writing, may lodge a copy of the signed and certified record" --
  `s 120 -- VCAT must register my agreement` -- a record unsigned, uncertified, or lodged without notice: JUST FALSE --
  NOTHING.
- **F12** ss 113(1), 123(1) "The following persons may" -- `ss 113(1), 123(1) -- the person bringing it may do so` --
  another person in none of the listed ways: NOTHING (not closed with "only") -- JUST FALSE.
- **F13** ss 82A(3), 83A(3) "does not permit discrimination on the basis of any attribute other than" -- `ss 82A, 83A --
  the religious employer exception applies` -- another attribute: JUST FALSE (a flat negative) -- NOTHING.
- **F14** s 119(3) "within 30 days after the agreement is reached" -- `s 119(3) -- what became of my request for a record`
  -- days counted from the day of the agreement, day 30 the last day, a request on the day of the agreement in time -- the
  agreement day counted as day 1 (day 29 the last).
- **F15** s 26 "the offering of employment" -- `s 26 -- a genuine occupational requirement exception applies` -- deciding
  who, the terms offered, refusing to offer: in; denying a training program: out (NOTHING) -- the training head counts as
  part of offering.
- **F16** s 28A "an employee who is under the age of 21 years" -- `s 28A -- I may be paid a youth wage` -- age at the time
  of the pay, in whole years -- age when engaged.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions (s 4 attribute, s 7(1) discrimination), the "if" conditions of ss 8, 9, 92, 104, 109
and of the exceptions (ss 23-26, 28, 75, 76, 82A, 83A, 86, 127), "unless" (ss 20(2), 104(1)(g), 108(3)(a)), "is not
required" (ss 20(5), (6)), "does not apply" (ss 15(3), 21(2), 25(2)), "does not discriminate" (s 12(2)), "does not
prohibit" (s 13(1)), "is not vicariously liable" (s 110), "inadmissible" (s 117), "does not permit" (ss 82A(3), 83A(3)) and
the periods of ss 116(a), 119(3), 121(3) give `JUST FALSE`. `NOTHING` is answered where the section's own list of heads,
positions, attributes or relationships does not reach the case (ss 7(2), 16-37, 93-102, 113(1)) or a permission is limited
in its own wording (ss 27, 28A, 29, 37, 120(3)) (*limited by its own wording*), where a small firm discriminates
unreasonably (ss 30, 31) or a s 105 contravention has no result (s 106) (*silent*), and where admissibility outside s 117
is for the law of evidence (*points outside the text*).

## What the Act turns out to say

1. **s 34(b) points at the wrong section.** s 23(b) (employers) conditions the disability exception on the employer having
   complied with s 20, the adjustment duty. Its twin for firms, s 34(b), reads "in the case of a person to whom section 32
   applies, the firm has complied with that section", and s 32 is the parent or carer duty; the adjustment duty for firms
   is s 33. s 34(c) itself refers to ss 33(3) and (4). Probably s 33 was meant. Encoded as printed: for a firm, (b) arises only where s 32 applies (a firm of 5 or more partners and a person
   with caring responsibilities). Asserted.
2. **s 22A is not "discrimination".** s 7(1)(b) makes a contravention of ss 17, 19, 20, 22, 32, 33 (and 40, 45, 54-56)
   discrimination. s 22A (a principal's adjustments for a contract worker with a disability), inserted in 2021, was not
   added to the list. A s 22A breach is still a contravention of Part 4 and can be brought under ss 113 and 122, but it
   is not "discrimination", so s 13 (exceptions) and anything keyed to discrimination do not reach it in terms. The
   adjustment question answers the duty for a contract worker as for an employee. Asserted for the duty only.
3. **Small firms.** A firm (or a firm being established) of fewer than 5 partners "may discriminate ... if the
   discrimination is reasonable" (ss 30(2), 31(3), (4)); nothing prohibits its unreasonable discrimination, which is read
   as unlawful only by implication (F2). The parent or carer duty binds only firms of 5 or more (s 32), the adjustment duty
   every firm (s 33). Asserted.
4. **A job applicant is owed less than a person offered the job.** s 16 protects applicants, but s 17 (caring
   responsibilities) and s 20 (adjustments) speak only of "a person offered employment" or an employee. And s 23 lets an
   employer rely on the disability exception against an applicant not yet offered without having had any s 20 duty to
   meet (s 23(b) is limited to "a person to whom section 20 applies"). Asserted.
5. **No time limit to apply to VCAT.** Part 8 sets none: s 122 applies "whether or not the person has brought a dispute to
   the Commission", and the only 12 months in Part 8 is a ground on which the Commission "may decline" (s 116(a)). Whether
   the Victorian Civil and Administrative Tribunal Act 1998 or VCAT's rules limit time was not checked here. Encoded: the
   dispute question asks no date.
6. **The positive duty cannot be enforced by the person.** s 15(3): "Part 8 does not apply to a contravention" of it; only
   the Commission may investigate (s 15(4)), and only where the matter "relates to a class or group of persons" and cannot
   reasonably be resolved by dispute resolution or a VCAT application (s 127(a)). A breach that affects one person alone
   is reachable by neither route. Asserted.
7. **Sexual harassment has no exceptions.** Part 5's exceptions are to "the prohibition of discrimination" (its heading and
   s 13); none applies to Part 6. In Part 6, "employee", "employer" and "employment" include volunteers and unpaid workers
   (s 4), so the work relationships cover them. Encoded: no exception input on the harassment question.
8. **"representative body"** is used in ss 4 ("party"), 114, 114A and 124 but defined nowhere; s 114(2) and s 124(2) say
   only when such a body has "sufficient interest". Not encoded.
9. **s 104(1)(g)'s proviso is confined to (g).** An allegation "false and ... not made in good faith" is unprotected, but a
   refusal under (h) or evidence under (d) has no such proviso. Asserted.
10. **Conversion.** s 104(1)(h)(iii) and the closing words of s 104(1) ("or because the person believes ...") print
    without the indent of their neighbours, and s 1(ab) and s 4 "sex characteristics" (a), (b) likewise; the text is
    otherwise as the Word file has it.
11. **Reconverted, 7 November 2026.** The converter that made the first deposit dropped the Word file's Symbol-font
    characters, which here were only the bullets before each item of the examples to ss 20, 22A, 33, 40, 45 and 56. The
    text was reconverted with the fixed converter and the bullets are restored; no number or sign was lost. The encoding
    relies on ss 20, 22A and 33 (the adjustment duty), but not on the wording of their examples beyond the paraphrase
    in the `do I need adjustments` description, which stands; ss 40, 45 and 56 are out of scope. No value, case or
    finding changed.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- A lawyer's view on findings 1, 2, 3 and 5 and on forks F2, F3, F4, F7, F10; an independent test pass and a human gate.
- The other areas of Part 4 (education, goods and services, accommodation, clubs, sport, local government) and their
  exceptions, Part 6A (vilification), and an employer seat (the positive duty, the exceptions it must prove, vicarious
  liability and reasonable precautions).
- Time limits and procedure for VCAT applications in the Victorian Civil and Administrative Tribunal Act 1998 (deposited
  beside this subject) and VCAT's rules.
