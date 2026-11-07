# Discrimination Act 1991 (ACT) -- baseline encoding, the person discriminated against, harassed, vilified or victimised

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE. No pipeline, no
coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for: the provisions a claimant meets. The Act is of a size that can be taken nearly whole, and it is:
Parts 2, 3, 5, 7, 8 and 9 whole; Part 4 whole as a screen (which of its 42 exceptions could reach a given area and
ground), with the exceptions that turn on facts or numbers worked out one by one; s 109 as what an exemption covers;
s 121A; the dictionary's "irrelevant criminal record". What a claimant asks: is my attribute protected, was it
discrimination, does the Act cover where it happened, can they rely on an exception, was I sexually harassed,
vilified or victimised, is the employer answerable for its employee, must they adjust for me, and is it all, put
together, an unlawful act I can complain about.

This is the first encoding of the Act; nothing existed to extend. Three files: the dates (`disc-dates.l4`, built-in date
functions only, no daydate), the rules and the 30 exported questions (`disc-claims.l4`), and the worked cases
(`disc-cases.l4`). The one duty owed to the person in a form the text states as steps to be taken -- the insurer's or
super fund's duty to give access to the data it relied on (s 28 (3)) -- is a regulative rule (three ways of doing it
joined by ROR), run by EVALTRACE inside an exported question that takes only plain facts. The Act sets it no deadline
(finding 5), so the rule has no WITHIN and no LEST; the answer is "done" or "still owed". No other duty in the Act has a
deadline the person meets: the time limits for a complaint are in the Human Rights Commission Act 2005, not this Act.

## Edition

- **Act:** Discrimination Act 1991 (ACT), A1991-81, Republication No 54 (R54), effective 23 February 2026, last amended by
  A2026-4, as deposited at `../../registers/source-bundle/A1991-81.txt` (converted from the register's DOCX, which the
  register marks as an unauthorised version; the authorised text is the register's PDF).
- **Dates taken from the endnotes:** the "commencement day" of s 75 (6) is 11 April 2024 (endnote 3: Discrimination
  Amendment Act 2023 A2023-7, "remainder commenced 11 April 2024").
- **Numbers set elsewhere:** the Discrimination Regulation 2016 (further disabilities, s 5AA (1) (h); assistance animal
  requirements; prescribed sporting activities, ss 41 (2) (a) (iv), 57 (2) (d), 57M (2) (d); exceptions under s 123 (2))
  is not deposited: each is asked as a fact or offered as a choice. Ministerial declarations under s 30 (2) and s 52 (2)
  are asked. The Spent Convictions Act 2000 (spent and extinguished convictions, s 16) and the Fair Work Act 2009 (Cth)
  (modern awards) are asked as facts.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read
(the binary prints each diagnostic twice; counts are of distinct ranges). A deliberately wrong assertion (the s 75 duty
applying to a business on 11 April 2027) was run once in a scratch copy in this folder, since deleted, and showed as
"assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `disc-dates.l4` | 0 | 0 | 0 | 0 |
| `disc-claims.l4` | 0 | 0 | 0 | 0 |
| `disc-cases.l4` | 0 | 0 | 180 | 180 |

Every exported question has cases, with the edges: each kind of criminal record, a spent conviction each way on s 16;
direct, indirect, both, and a reasonable condition; every exception screen worked by hand through all 42 exceptions for
five area-and-ground pairs, including s 33B closed to religious conviction; 6 and 7 people in s 26; 20 and 21 years in
s 57B; 11 and 12 years in s 41; each paragraph of s 32 and s 32 (2), (3); the s 52 (2) declaration for premises only;
the exemption on its first day, its last day, the day after, a notice stating more than 3 years cut at 3, and a start on
29 February; each Part 5 setting and the "someone else" case; each s 67A (2) defence; s 68 with an honest and a
dishonest false claim; s 121A each way; s 74 each answer; s 75 for a business on 7 November 2026, 11 April 2027 and
12 April 2027, and for a government body on 11 and 12 April 2025. The dates module's leap-year rule is asserted
(2000, 1900, 29 February plus 3 and plus 4 years).

**No mirror cases.** One seat.

## Seat

**The person discriminated against, sexually harassed, vilified or victimised** (`disc-claims.l4`): the job applicant
or employee, the commission agent or contract worker, the partner, the union or professional member, the student, the
customer, the person seeking access to premises, the tenant or other occupier, the club member, the sportsperson or
competitor, the person dealing with an ACT public authority; and the person who sees a discriminatory advertisement.
"Is my attribute protected?", "Was it discrimination?", "Does the Act cover this?", "Can they rely on an exception?",
"Was it sexual harassment?", "Was I victimised?", "Is the employer answerable too?", "Did they have to adjust for me?",
"Is it, all together, unlawful?".

The person complained about gets no seat in this encoding (a second seat for the employer or provider could be added
beside it under the 2026-10-21 ruling; not written). The Human Rights Commission, the ACAT and the Minister get none:
the Commission's exemption is asked as what it covers (s 109); the Minister's declarations are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The regulation is not deposited (Edition).
  The commencement day is taken from the Act's own endnotes.
- **The actors the text names.** Followed: employer, principal, commission agent, contract worker, partner,
  organisation, qualifying body, employment agency, educational authority, provider, club, public authority, insurance
  or superannuation services provider, religious body, workplace participant, representative.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: "reasonable in the circumstances"
  (s 8 (4)); "reasonable, proportionate and justifiable" (ss 24, 28, 31, 33B, 33C, 41, 57); "unjustifiable hardship"
  (ss 51-54, 74 (2), with s 5B's factors in the `@desc`); "reasonably feels offended, humiliated or intimidated"
  (s 58); "incite hatred ..." (s 67A); "necessary to avoid injury to religious susceptibilities" (s 32); "all reasonable
  steps" (s 121A (3)); "reasonable" in ss 11, 26 (2), 27 (2).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "protected attribute" (s 7),
  "discrimination" (s 8, with s 4A), "irrelevant criminal record", "sexual harassment" (s 58), "discrimination action"
  (s 68 (2)), "near relative" (in the s 26 `@desc`), "commencement day" (s 75 (6)). Asked: "spent conviction" and
  "extinguished conviction" (Spent Convictions Act 2000), "award" (Fair Work Act 2009), "domestic partner" (Legislation
  Act 2001), "territory authority" and "administrative unit".
- **One case is the text's natural unit.** Followed: one act done to the person (or one advertisement, one refusal to
  adjust).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (Scope).

## Scope

**In.** s 4A (as the "one of the reasons" gloss), s 5AA and s 5B (as glosses), Part 2 whole (ss 7, 8); Part 3 whole
(ss 10-23C; s 11 on its own); Part 4 whole as the screen, with ss 24, 25, 26, 27, 28 (2), 28 (3), 32, 33B, 33C, 41, 46,
51 (2), 52, 53, 54, 57, 57B, 57M worked out from facts, and s 30 in the put-together question; Part 5 whole (ss 58-67);
Part 7 whole (ss 67A, 68, 69); Part 8 whole (s 70 as the onus in the put-together question, ss 71, 72 in its answer,
s 73); Part 9 whole (ss 74, 75, 76); s 109 (what an exemption covers); s 121A; the dictionary.

**Out, and why.**
- s 1-3, 4, 4AA (objects and interpretation: no facts to apply; s 4AA would favour the reading beneficial to the seat in
  every fork, and is noted there), s 5AA as a question (the list is a gloss in the `@desc`s), s 5AB (the person's own
  liability for an assistance animal: not a claim question), s 5A (a gloss of "pregnancy"), s 6 (MLAs as employers:
  folded into "employer"), s 6A (offences: none for the seat).
- Part 4 exceptions not worked one by one (ss 25A, 26A, 31, 33A, 33D, 35-39, 44, 45, 50, 51 (1), 56, 57C, 57E, 57G, 57H,
  57J, 57K, 57N, 57O, 57P, 57R): each is a single judgment or a single fact; the screen names them, and the put-together
  question takes "they establish an exception" as an input (s 70).
- s 109 (1)-(3), (5), (6) and s 110 (applying for and reviewing an exemption): the applicant is the person seeking the
  exemption, not the seat. s 121 (secrecy offence for officials), s 122, s 123 (regulation-making): machinery.
- **The complaint itself** (who may complain, time limits, conciliation, referral to the ACAT, remedies) is in the Human
  Rights Commission Act 2005 (deposited at `subjects/au/act/human-rights-commission-act-2005`, not encoded); the ACAT
  procedure is in the ACT Civil and Administrative Tribunal Act 2008 (encoded at
  `subjects/au/act/act-civil-and-administrative-tribunal-act-2008/encodings/baseline-2026-11`).
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 7 (1) "any of the following attributes (a protected attribute)" -- `s 7 -- is the ground a protected
  attribute` -- a closed list: an attribute outside it is the text's no -- NOTHING (s 7 (2) "includes" extends it).
- **F2** s 11 "being a practice -- (a) ... (b) ... (c)" -- `s 11 -- may my employer refuse my religious practice at
  work` -- conditions limiting the prohibition in its own wording: NOTHING-kind when one fails -- the text's no.
- **F3** Part 4 exceptions that name only some paragraphs of a section (ss 24, 25, 44, 45, 57B, 57C) or a sub-area --
  `Part 4 -- which exceptions could the other side rely on` -- screened at the level of the whole section (the screen
  says what could apply) -- screened paragraph by paragraph, which would need a finer area input.
- **F4** s 58 "in circumstances in which the other person reasonably feels offended, humiliated or intimidated" --
  `s 58 -- was it sexual harassment` -- qualifies all three limbs -- qualifies only "other unwelcome conduct".
- **F5** s 68 (2) (h) "other than a claim that is false and not made honestly", once met (decided case by case) --
  `s 68 -- was I victimised` -- the text's no -- NOTHING.
- **F6** s 74 (1) "if discrimination on the ground of the attribute is unlawful under this Act" -- `s 74 -- did they
  fail to make reasonable adjustments for me` -- the area is in Part 3 and no exception or exemption applies -- the
  person must also have suffered s 8 discrimination (which would make the duty circular).
- **F7** s 75 (4) "until 12 months after the commencement day" (and "3 years") -- `s 75 (4) -- from when does the
  positive duty apply` -- the period runs from the day after 11 April 2024, so the duty first applies on 12 April 2025
  (12 April 2027 for others) -- 11 April 2025 (11 April 2027). Legislation Act 2001 s 151 not deposited.
- **F8** s 109 (4) (c) "for the period not longer than 3 years specified in the notice" -- `s 109 -- does their
  exemption cover what they did` -- a notice stating longer is cut at 3 years, ending the day before the third
  anniversary of the start -- the notice is of no effect beyond its terms, or invalid.
- **F9** s 33C "another person (a prospective employee)" -- `s 33C -- can they rely on the inherent requirements of the
  job` -- only a person seeking the position (the text's no for an existing employee) -- "in relation to a position of
  employment" reaching an employee whose capacity changes.
- **F10** a 29 February start (s 109, "3 years") -- `plus years` in `disc-dates.l4` -- 28 February of the later year
  when it has no 29 February, the period ending the day before -- 1 March.
- **F11** s 57B (2) (a) "if the person is 21 years old or older -- in relation to the offer of employment to a person
  under 21 years old" -- `s 57B -- can my employer rely on youth wages` -- the person discriminated against is 21 or
  older and the offer went to someone under 21 -- any offer of employment to a person under 21.
- **F12** s 67A (1) "other than in private", and an act that does not incite -- `s 67A -- was I unlawfully vilified` --
  NOTHING-kind (a prohibition limited in its own wording) -- the text's no.
- **F13** Part 3 sections, an act outside a section's list, and an area outside Part 3 -- `Part 3 -- does the Act cover
  where I was discriminated against` and the put-together question -- NOTHING-kind -- the text's no.
- **F14** s 26 (1) (a) "not more than 6 people" -- `s 26 -- can they rely on the domestic accommodation exception` --
  people the accommodation is for, besides the provider and near relatives or carers who live there, counted as the
  text says; read as people, not bedrooms -- capacity rather than occupants.

Sites decided without a fork line: s 8 (2), (3) and s 58 are definitions ("if"): outside them, the text's no. Every
Part 4 exception is "does not make unlawful ... if": its condition failing is the text's no (the exception gives
nothing). s 23C (2), s 32 (2), (3), s 33B (2), s 41 (2), s 57 (2), s 57M (2), s 67A (2), s 121A (3) and s 76 are flat
negatives or "does not apply": the text's no. s 28 (3) and s 74 (1) are duties whose "if" is unmet: no duty (the text's
no).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries nine `NOTHING-kind` answers (s 7 (2), s 11, Part 3 twice, s 67A, s 68, s 69, s 73, and Part 5's
"someone else"). The questions answer with a choice from a list rather than a MAYBE BOOLEAN: the answer marked
"NOTHING-kind" is the NOTHING answer, and the answers marked "the text's no" are JUST FALSE. Plain BOOLEAN questions
(the exceptions, s 58, the criminal record, s 109) answer FALSE only where the text says no. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The periods the text fixes (s 75 (4), s 109 (4) (c)) answer the text's no outside the period (ruling (a)).

## What the Act turns out to say

1. **s 74 (3) calls a failure to adjust "an unlawful act", but the dictionary defines "unlawful act" as an act unlawful
   under Part 3, 5 or 7 only**; s 74 is in Part 9. s 74 (3)'s own words probably carry it, but provisions keyed to the
   defined term (s 70 onus, s 73 aiding, s 121A representatives, s 68 (2) (h), and a complaint about "an unlawful act"
   under the HRC Act s 42 (1) (c), per the note to s 121A) may not reach it on a strict reading. Encoded as an unlawful
   act. A possible drafting gap.
2. **No provision makes a failure of the s 75 positive duty an unlawful act**, and s 72 gives no right of action. A
   claimant cannot complain of a s 75 failure as such under this Act; the question says so.
3. **s 33C (inherent requirements) names only "a prospective employee"**. An existing employee whose capacity changes
   (after an injury, say) is outside it; the employer must find another exception or rely on s 8 (4). Asserted (fork F9).
4. **s 72: the Act gives no right of action**, and s 71: an unlawful act is not an offence. The route is a complaint
   under the Human Rights Commission Act 2005, whose time limits are not in this Act. Stated in the answers.
5. **s 28 (3) sets no time** for an insurer or fund to give access to its data, unlike most access duties; only
   inspection must be "at a reasonable time and place". Encoded as a duty without a deadline. Asserted ("still owed").
6. **The s 75 positive duty does not yet bind private organisations and businesses**: s 75 (4) (c) puts it off until 3
   years after 11 April 2024, so it first applies on 12 April 2027 (or 11 April, fork F7). On the day of this encoding
   (7 November 2026) only ACT government bodies and their managers are bound. Asserted.
7. **s 23 still refers to "part 5, 6 or 7"**, but Part 6 (vilification) was omitted by A2016-49 s 8 and its content
   moved to s 67A in Part 7 (endnote 4). A stale cross-reference; harmless.
8. **s 26A says "Part 3 or part 4 does not make unlawful"**, but Part 4 makes nothing unlawful (it holds exceptions).
   Probably meant "Part 3, 5 or 7". A likely drafting slip; not encoded beyond the screen.
9. **s 41 (2) (b) protects children under 12 from exclusion from sport by sex**, but ss 57 and 57M (disability, age)
   have no such floor. Asserted (11 and 12 years).
10. **s 109 (4) (c) does not say what happens if a notice states more than 3 years** (fork F8). Asserted as cut at 3.
11. **s 11's conditions, when not met, leave s 10 (2) open**: refusing a religious practice can still be discrimination
   in the terms of employment. The s 11 answer says so.

## Before this is worth relying on

- The Discrimination Regulation 2016 (prescribed disabilities, assistance animal requirements, prescribed sporting
  activities, regulation exceptions), not deposited.
- The Human Rights Commission Act 2005 complaint provisions (who may complain, time limits, outcomes), to be encoded beside
  this one; the Legislation Act 2001 (ACT) for counting time (forks F7, F8, F10).
- A lawyer's view on forks F2, F3, F6, F7, F9 and F11, and on findings 1, 2 and 8; the remaining Part 4 exceptions worked
  one by one; an independent test pass and a human gate.
