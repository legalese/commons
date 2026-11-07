# Anti-Discrimination Act 1991 (Qld) -- baseline encoding, the complainant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The focus is **the provisions a person bringing
a complaint meets**: what counts as unlawful discrimination (attributes, direct and indirect discrimination, the areas of
activity, the exemptions most often relied on), sexual harassment, requests to contravene, unnecessary information,
vilification, discriminatory advertisements, victimisation, vicarious liability, and the complaint machinery of chapter 7
from the complaint to the tribunal's orders. The Act has about 300 sections; the many narrow exemptions, representative
complaints, investigation, offences, opinions and administration are out (see Scope).

Files: the dates in `adaq-dates.l4` (built-in date functions only, no daydate), the rules and the exported questions in
`adaq-complainant.l4`, and the worked cases in `adaq-cases-complainant.l4`.

## Edition

- **Act:** Anti-Discrimination Act 1991 (Qld), Act No. 85 of 1991 (`act-1991-085`), the version in force from 19 May 2025,
  current on 6 November 2026, deposited at `../../registers/source-bundle/act-1991-085.txt` (text sha256
  `e99d7b92d68e093283a67add157076d9d5ef58a9f4af724493a109590c15afcd` per its `.meta.json`; a Windows checkout with CRLF
  line endings hashes differently). A plain-text conversion of the Queensland Legislation HTML view, not the authorised PDF.
- **Numbers in the Act itself:** 1 year (ss 138, 141A, 175); 28 days (ss 141(1), 142(2), 166(1), 167(2), 167(4)(c),
  168(2), 168A(3)(d), 169(2), (3), 170(2)); 6 months (s 167(1)); 6 or more people in a partnership (ss 16-18, 56, 57, 70,
  71); 3 people (s 87(b)); under 21 (ss 33, 127(1A)); under 12 (s 111(2)); 45 and 170 penalty units and 3 months (s 129).
- **Not deposited, and asked as facts or left out:** the Acts Interpretation Act 1954 (s 38, reckoning of time, fork F1);
  the value of a penalty unit (Penalties and Sentences Act 1992 and regulation), so s 129 is answered in penalty units;
  the Respect at Work and Other Matters Amendment Act 2024 (the date s 7B commenced, which s 285AA turns on) and the
  former ss 204-206; the Industrial Relations Act 2016 (industrial relief; chapter 12, part 9, division 2 and part 10);
  every borrowed term (near relative, educational institution in fact, worker, agent in fact, public act in fact).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read:
every diagnostic in the case file is `DiagnosticSeverity_Information` "assertion satisfied"; the other two files report
"Checking succeeded" with no diagnostics.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `adaq-dates.l4` | 0 | 0 | 0 | 0 |
| `adaq-complainant.l4` | 0 | 0 | 0 | 0 |
| `adaq-cases-complainant.l4` | 0 | 0 | 202 | 202 |

Every exported question has cases, with the edges: each s 8 link and an unlisted characteristic; the attribute as the
only, a substantial, and an insubstantial reason; each limb of s 11 missing; a partnership of 6 and of 5; a for-profit
supplier, a non-profit association as supplier and as club; trade union activity with and without the Industrial
Relations Act provisions; political belief between council members; each exemption in and out of its area and attribute,
youth wages at 20 and 21, shared accommodation for 3 and 4 others, a sex restriction in sport for under-12s; a complaint on
the anniversary and the day after, from 29 February to a non-leap year, a series straddling the year with and without
good cause; 28 days across a year end and in a leap year; s 166 with no extension, an extension asked mid-period, on the
day of the decision, on the last day with refusal on a Friday, one day too late, and granted; 6 months from 31 August into
a leap and a non-leap February and across a year end; agreeing to a respondent's referral on the 28th and 29th day, with
and without a valid extension; each lapse notice answered on the 28th and 29th day or not at all.

## Seat

**The complainant** (`adaq-complainant.l4`): the individual who was subjected to an alleged contravention of the Act --
discrimination, sexual harassment, victimisation, vilification, an unlawful request for information, a discriminatory
advertisement -- and complains to the Human Rights Commissioner, with the complaint possibly going on to QCAT or the
Queensland Industrial Relations Commission. "Is what happened to me unlawful?", "Is the employer liable too?", "Can I
complain, and by when?", "Can my complaint be rejected or lapse?", "How do I get it to the tribunal, and by when?", "Who
has to prove what?", "What can the tribunal order?". The respondent meets the same rules from the other side; no seat is
written for it. No seat for the commissioner, the commission, QCAT or the industrial relations commission.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. Every number the encoded provisions use is in
  the Act. No regulation sets a number they use (s 106A(1)(n) and s 111(4)(d) prescriptions are outside the scope).
- **The actors the text names.** Followed: the complainant, the respondent, the commissioner, the tribunal (QCAT or the
  industrial relations commission), the worker or agent, the employer or principal, the relevant entity.
- **Judgments answered conditionally.** "not reasonable" (s 11), "a reasonable person would have anticipated" (s 119(f)),
  "genuine occupational requirements", "unjustifiable hardship", "reasonably necessary", "reasonable steps", "reasonable
  precautions", "good cause" (s 138(2)), "the reasonable opinion" of the commissioner (ss 137, 139, 168, 169), "the
  balance of fairness" (s 175(2)): all asked, never decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "attribute" (s 7, schedule 1), "discrimination
  on the basis of an attribute" (s 8), "direct discrimination" (s 10), "indirect discrimination" (s 11), "sexual
  harassment" (s 119), "victimisation" (s 130), "work-related matter" and "tribunal" (schedule 1), "club" (its profit
  limb). Asked: "public act" (an "includes" definition), "worker", "agent", "industrial relief", "impairment" (as part of
  the attribute choice).
- **One case.** One complainant's complaint about one respondent's conduct (a series of contraventions in one complaint
  for the time limit).
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** See Scope.

## Scope

**In (38 exported questions):**
- ss 7, 8 (is the ground a protected attribute); s 10 (direct); s 11 (indirect).
- Chapter 2, part 4: ss 6(2)(a)(iii), 13-23, 37-39, 45, 46 (with (2)), 52-57, 66-71, 76, 77, 81-85, 93-95, 101, 102, and
  schedule 1 "club" (is the area covered).
- Exemptions: ss 25(1), 25(3), (6), 33, 35, 36, 44, 49, 51, 87, 92, 100, 104-108, 109(1)(d), (2), 111, 112, with s 205
  (does the exemption apply).
- ss 118-120 (sexual harassment); ss 122, 123 (requests to contravene); s 124 (unnecessary information); s 124A
  (vilification); s 127 (advertisements); ss 129-131 (victimisation; the s 129 maximum penalty); s 133 (vicarious
  liability).
- ss 134, 135, 136, 137 (who may complain, form, agreements not to complain); ss 138, 141A (time; is my complaint in
  time); ss 139, 140, 142(1), (4) (rejection); s 141 (the commissioner's 28 days); s 142(2) (reasons for rejection);
  ss 153, 154 (dismissed workers).
- Schedule 1 "tribunal", "work-related matter" (which tribunal); s 160 (missing a conference); ss 164, 189 (settlement
  agreements); ss 164A, 165 (referral after a conference); s 166 (referral after a s 165 notice, with extensions);
  s 167 (referral after 6 months; a respondent's request).
- ss 168, 168A, 169, 170 (lapse notices; the day a withdrawn complaint lapses); s 169(3), (4) (review of a lapse).
- ss 144, 190 (protecting orders); s 175 (late complaints at the tribunal); ss 204, 205, 285AA (proof); ss 209, 210, 154
  (orders).

**Regulative rules:** five, each run by EVALTRACE inside an exported question that takes only plain facts (a CONSIDER on
an EVALTRACE matches FULFILLED only):
- s 138(1): I DO make my complaint WITHIN the days to the anniversary of the contravention;
- s 142(2): I DO ask for written reasons WITHIN 28 days of receiving notice of the rejection;
- s 167(4): I MUST agree in writing to the respondent's referral WITHIN 28 days (or the extended time) LEST BREACH: the
  complaint lapses;
- ss 169(2), 170(4): I DO answer the commissioner's notice WITHIN 28 days;
- s 169(3): I DO apply to the tribunal to review the lapse WITHIN 28 days.
Except under s 167(4), the BREACH marks only that the time passed; not complaining is not a wrong.

**Out, and why:**
- ss 1-5, 3A, 6, 9, 12, 24, 37, 40, 45, 47, 52, 58, 66, 72, 76, 78, 81, 86, 93, 96, 103, 117, 121, 125, 132 (title, Crown,
  ships, explanatory and purpose provisions): no question of their own; s 5 (unjustifiable hardship factors) is folded into
  the exemption test input.
- Exemptions not in the list (ss 26, 27, 30-32, 34, 41, 43, 48, 50, 59-65, 73-75, 79, 80, 88-91, 97-99, 106A, 106B, 110):
  narrow to their settings (domestic services, childcare, single-sex accommodation, couples, partners' retiring age,
  restricted capacity, single-sex or religious schools, age-based admission, cultural sites, minors, superannuation and
  insurance data, wills and gifts, workers' and students' accommodation, religious and charitable accommodation, club
  exceptions, compulsory retirement ages, visa policies, charities). A second pass could add them to the same enumeration.
- s 113, 113AA, 113A (tribunal-granted exemptions): an application by the person seeking an exemption, not the
  complainant.
- ss 114-116 (discrimination by a worker, agent, member or committee): noted; the complainant's question is s 133.
- s 128 (inducement to publish an advertisement): an offence about the publisher, not the complainant.
- Chapter 5B, ss 131B-131G (residents of regional communities and large resource projects): every term is borrowed from
  the Strong and Sustainable Resource Communities Act 2017, not deposited.
- ss 143, 143(2A), (2B) (the respondent's notice and response): the respondent's duties; s 143(3) is noted in s 160.
- s 145, s 191 (anonymity directions and orders): the commissioner's and tribunal's discretion, giving the complainant no
  question beyond "may ask"; noted.
- ss 146-152, 194-203, 285 (representative complaints): a class mechanism; a separate seat (the representative
  complainant) would be needed.
- ss 154A-157 (investigation), 158, 159, 161-163, 164AA, 171-174 (the conduct of conciliation, authorisations,
  authentication): the commissioner's powers. s 162 (a right to an interpreter) and s 163 (representation with
  permission) are noted, not encoded. s 172 (the commissioner may extend any part 1 time limit if no undue hardship and
  reasonable grounds) qualifies every part 1 deadline; it is noted in the descriptions rather than taken as an input
  everywhere (finding 9).
- ss 174A-174C, 176-178, 185, 186, 193, 193A, 207, 208 (the tribunal's functions, constitution, joinder, amendment, staff,
  withdrawal, transfer, evidence): procedure under the relevant tribunal Act.
- Chapter 7, parts 4 and 5 (offences, unincorporated associations), chapter 8 (opinions), chapters 9-11 (administration,
  strategic reviews, the Commonwealth arrangement, service, protections, regulation-making, transitional provisions other
  than s 285AA): machinery.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 28 days of" and "28 days after" (ss 141, 142(2), 166, 167(4), 168-170) -- `the day ... days after` -- the
  named day is not counted (Acts Interpretation Act 1954 s 38, not deposited), so the last day is that day plus 28 -- the
  named day counted, one day less.
- **F2** "within 1 year of" (ss 138, 175) and "6 months after" (s 167) -- `the date ... years after`, `the same day ...
  months after` -- the last day of the year is the anniversary, 29 February in a year that has none is 28 February, and a
  month without the day gives its last day -- the day before the anniversary; 1 March.
- **F3** s 8 "includes" -- `Is the ground of my complaint a protected attribute` -- a link outside paragraphs (a)-(d) and
  s 7(q) is "not covered" -- "no".
- **F4** s 10(4) -- `Was I directly discriminated against` -- where the attribute is the only reason, s 10(4) is not
  needed and the treatment is on the basis of the attribute -- s 10(4) as the only test.
- **F5** s 136 bare "must" -- `Is my complaint in the proper form` -- a complaint missing an element is answered "no" --
  a defective complaint still counts, to be cured.
- **F6** s 137(1) -- `Does my agreement not to complain stop my complaint` -- where the commissioner does not think it
  fair, the complaint is not accepted, a rejection under s 142(4) -- the agreement has no effect on acceptance at all and
  s 137 only lets the commissioner override a contractual bar.
- **F7** ss 153, 154 -- `If I was dismissed, can I complain and seek industrial relief` -- industrial relief sought after
  lodging but before the acceptance notice falls under neither section ("not covered") -- s 153 read as barring any later
  application once a complaint is lodged.
- **F8** s 166(3), (4) -- `By when must I require referral after the conciliation notice` -- the days from the request to
  the notice of decision are added to the 28th day, and on a last-day request the later of that day and the next
  business day after the refusal is taken -- s 166(4) replacing s 166(3) for a last-day request (the two give the same
  day except when the day after the refusal is not a business day).
- **F9** s 167(1) -- `From when can I ask for referral because the complaint is taking too long` -- the request may be made
  on the day 6 months after the acceptance notice -- only from the day after.
- **F10** ss 168(3), 168A(4) -- `Does my complaint lapse after the notice` -- the lapse turns on the commissioner's view at
  the end of the 28 days, asked as one input, whatever the complainant did -- an answer in time stops the lapse.
- **F11** s 170(2) "after the notice is given" and s 168A(3)(d) "after receipt" -- the lapse functions -- one input, the
  day the complainant received (was given) the notice -- separate days for giving and receiving.
- **F12** s 124A "religion" -- `Was I vilified` -- read as the s 7(i) attribute "religious belief or religious activity" --
  a narrower "religion" (affiliation only).
- **F13** the exemptions -- `Does the exemption apply to me` -- each exemption's evaluative test is one input (the
  respondent's proof); ss 35 and 36 are grouped with ss 44, 51, 92 and 100; s 100 is applied to the club area generally,
  though it reaches only "failing to accept a person's application for membership"; s 109(1)(d) is applied in the
  accommodation area, where s 90 (with the same test) governs if it applies -- separate inputs per element; s 100 limited
  to membership applications.
- **F14** s 46(2) and schedule 1 "club" -- `Is the area covered by the Act` -- one input, "a non-profit association", for
  both -- separate inputs for the purposes limb and the profit limb.
- **F15** ss 122, 123, 124, 124A, 127, 133 -- scope limits with no "only" are answered "not covered" (ruling (c)); the
  flat "does not" of ss 124A(2), (3)(b) and 127(1A) and the defences are answered "no" or "has a defence" (ruling (b) of
  the delegated-definitions ruling: "this section gives no defence on these facts" where the defence fails).
- **F16** s 175(1) -- `Will the tribunal deal with my complaint` -- "more than 1 year after" counted as for s 138(1) -- a
  separate count.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions (schedule 1 "attribute", "club", "tribunal", "work-related matter") and the
"happens if" definitions of ss 10, 11, 119 and 130 answer "no" or FALSE when they fail; the "if" conditions of ss 87,
134(4) ("only if"), 138(2)(a) ("only if"), 139, 140, 160(1), 164A(1), 167(4), 175 and the flat negatives of ss 19(2),
20(2), 25(6), 46(2), 102(2), 109(2), 111(2), 124A(2), (3)(b), 127(1A), 165(3) give "no"; the periods of ss 138(1), 142(2),
166(1), 167(4)(c), 169(2), (3) and 170(2) give "no" or FALSE outside them; the "includes" of s 8, the scope limits of
ss 122, 123, 124(1), 124A(1), 127(1), 133(1) and 134 and the gap of ss 153-154 give "not covered"; the defences of
ss 124(3), 127(2) and 133(2) are answered "has a defence" when proved and otherwise leave the contravention standing;
s 136's bare "must" is the case-by-case site F5, and s 137's unmet "if" is F6.

## What the Act turns out to say

1. **Non-profit associations fall between two areas.** s 46(2) takes out of the goods and services area an association
   established for social, sporting, community or similar purposes that does not carry out its purposes to make a profit;
   the schedule 1 definition of "club" covers only an association that "carries out its purposes for the purpose of
   making a profit". As deposited, a non-profit sporting or social association refusing membership is in neither area.
   Asserted. Worth checking against the authorised PDF, since the club definition's profit limb is the reverse of what
   the structure suggests.
2. **The note to s 204 points at an onus that is not there.** s 204(3)'s note gives "section 11(3) and 205" as examples
   of provisions on who must prove a matter; s 11(3) as deposited says only that the person imposing a term need not be
   aware of the discrimination. Possibly a leftover from the former s 11 and ss 204-206. Not asserted.
3. **A dismissed worker who seeks industrial relief between lodging and acceptance is caught by neither s 153 nor
   s 154.** s 153(b) needs the worker not to have applied before lodging and being notified of acceptance; s 154 needs
   the application before lodging. Asserted (not covered).
4. **s 166(4) adds a day only at weekends.** Where an extension asked on the last day is refused, s 166(3) already
   excludes every day from the request to the refusal notice, so the period runs to the day after the refusal; s 166(4)
   (the refusal day or the next business day) adds something only when that next day is not a business day. Asserted
   (a Friday refusal gives the Monday).
5. **Two lapse notices turn on the commissioner, two on the complainant.** Under s 168 the complaint lapses if "at the
   end of 28 days" the commissioner still holds the opinion, and under s 168A if the commissioner reasonably considers the
   matter dealt with elsewhere after considering representations made in time; answering does not of itself stop the
   lapse. Under ss 169 and 170 the complainant's answer in time does. Asserted.
6. **The burden of proof depends on a date the Act does not state.** s 285AA keeps the former ss 204-206 for complaints
   about contraventions before "the commencement of section 7B of the amendment Act" and says it applied from 1 December
   2024; neither that commencement nor the former sections are in the deposited text. Asked as a fact. Asserted.
7. **After an unresolved conciliation conference there is no deadline for requiring referral.** s 164A has no time
   limit; only a s 165 notice that the complaint cannot be conciliated starts s 166's 28 days (and switches off ss 164A
   and 167). Asserted.
8. **Compensation has no cap.** s 209(1)(b) allows "an amount the tribunal considers appropriate", and s 209(6) counts
   offence, embarrassment, humiliation and intimidation as damage. Asserted (in the answer).
9. **Every part 1 time limit can be extended.** s 172 lets the commissioner extend any time limit in chapter 7, part 1
   (no undue hardship, reasonable grounds), on top of the specific extension rules of ss 166(2) and 167(4)(d); s 167(4)(d)
   is the stricter (a request before the 28 days pass). The encoding applies only the specific rules and asks for an
   extended day where one was given. Asserted for s 167(4)(d).
10. **Late complaints face two separate tests.** The commissioner may accept a complaint more than a year late for "good
    cause" (s 138(2)); the tribunal must then decide again, "on the balance of fairness", whether to deal with it
    (s 175(2)). Asserted.

## Before this is worth relying on

- Check the conversion against the authorised PDF, above all the schedule 1 definition of "club" (finding 1).
- Deposit the Acts Interpretation Act 1954 (s 38) and check forks F1 and F2.
- Deposit the Respect at Work and Other Matters Amendment Act 2024 and the former ss 204-206, and bring in the s 285AA
  commencement (finding 6).
- Add the remaining exemptions to `Does the exemption apply to me`, and a representative-complaint seat.
- A lawyer's view on findings 1-3 and forks F6, F7, F8, F10 and F13.
- Link to the QCAT Act 2009 and Industrial Relations Act 2016 encodings once IMPORT can reach another subject.
- An independent test pass and a human gate.
