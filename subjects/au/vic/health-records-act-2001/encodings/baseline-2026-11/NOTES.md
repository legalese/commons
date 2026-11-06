# Health Records Act 2001 (Vic) -- baseline encoding, the individual whose health information it is

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. Four modules:

- `hra-dates.l4` -- the date helpers (built-in date functions only, no daydate import, no `YMD`);
- `hra-rules.l4` -- the law more than one question uses: the s 3 definitions of health information (with personal
  information) and immediate family member, and the three duties with deadlines as regulative rules (s 34(2), s
  34(2)(b)(ii), HPP 6.9) with the helper that runs them;
- `hra-seat.l4` -- the 33 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings
  in the Act's order. Where a provision is used by one question only, the question applies its words there and quotes them;
- `hra-cases.l4` -- the cases.

## Edition

- **Act:** Health Records Act 2001, Act No. 2/2001, Version No. 050, incorporating amendments as at 1 May 2026 (the
  register's current version when read on 6 November 2026), deposited at
  `../../registers/source-bundle/health-records-act-2001.txt` (sha256 9761d4c1...97dbd6 as committed), a plain-text
  conversion of the Word file the owner saved by hand on 6 November 2026 (see the `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Commencement:** Part 5, Part 6 and s 20 came into operation on 1 July 2002 ("rest of Act on 1 July 2002", endnote 1),
  Schedule 1 on 1 March 2002. "The commencement of this section" in ss 20 and 25 is therefore 1 July 2002.
- **Numbers set elsewhere:** the Act fixes its own periods (7, 14, 21, 30, 45 and 60 days, 12 months, 7 years, age 25) and
  the $100 000 cap. The Health Records Regulations (maximum fees under s 100(1)(a) to (c), retention periods under s
  100(1)(d), prescribed exempt information, services and providers, prescribed circumstances) are not deposited: each is
  an input, or the answer is NOTHING where they would decide it. The Health Complaints Commissioner's guidelines under s
  22 are not deposited: where a provision turns on them, the input asks whether it is met.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hra-dates.l4` | 0 | 0 | 0 | 0 |
| `hra-rules.l4` | 0 | 0 | 0 | 0 |
| `hra-seat.l4` | 0 | 0 | 0 | 0 |
| `hra-cases.l4` | 0 | 0 | 197 | 197 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice, most
three or more times; each day period on its last day and the next (45 days across a month end and a year end, 21 days
across February 2027, 60 days across January and February); each regulative rule done on the last day, done the day
after, still open on the last day and late the day after; the 12-month, 7-year and age-25 periods from the 29th to the
31st of a month into February; the compensation cap at $100 000 and $1 over; each refusal ground alone and the order
between them.

## Seat

**The individual whose health information it is** (`hra-seat.l4`): the patient, the injured worker or road user, the
claimant who needs their records as evidence, or anyone whose health information an organisation holds. "Is this my
health information?", "Does the Act reach this body?", "Can I get my records, in what form, and must they be explained?",
"Must they give me access, or may they refuse?", "By when must they answer, and have they?", "What can they charge?", "Who
may ask for me?", "Must they correct it, or attach my statement?", "May they collect it, use it, disclose it, tell my
family?", "How long must my records be kept?", "Can I complain, by when, and what can the Tribunal give me?", "What is the
fine for pressuring me?". A person acting for the individual (a person named in a written authority, an authorised
representative, the executor or administrator of the estate) asks the same questions about them; s 85 and s 95 say who.

No seat for the organisation, the Health Complaints Commissioner, the Tribunal, the Minister or a registration board: the
organisation's beliefs, considerations and agreements, and the Commissioner's views, are asked as facts; their duties to
the individual (ss 34, 41, HPP 5.2, 6.5 to 6.10, 11) are encoded as what the person must be given, and by when. A seat for
the organisation (health service provider or insurer) could be added beside this one.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own periods and cap; the
  regulations and guidelines it defers to are not deposited and are inputs.
- **The actors the text names.** Followed: the individual, the organisation, the health service provider, the authorised
  representative, the legal representative, the immediate family member, the nominated health service provider, the
  Health Complaints Commissioner, the Tribunal, a law enforcement agency, a news medium.
- **Judgments answered conditionally.** Followed: "believes on reasonable grounds", "considers", "reasonably necessary",
  "able to establish", "sufficient interest", "sufficient maturity", "in accordance with guidelines", "unreasonably" are
  inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "health information", "personal information",
  "immediate family member", "relative", "interference with privacy" (s 18), "authorised representative" (s 85(6)),
  "incapable" (s 85(3), asked as the s 85(3) test in the @desc) are worked out or applied; "health service provider",
  "agency" (Freedom of Information Act 1982 and Privacy Act 1988), "registered medical practitioner", "mental health and
  wellbeing service provider", "supportive attorney", "medical treatment decision maker", "legal professional privilege"
  are asked.
- **One case.** One individual's health information held by one organisation, or one request, or one complaint.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

The focus: the Health Privacy Principles and access to your own health records, as used for evidence in a claim. Part 5
(access) is encoded nearly whole, with HPP 6; Part 3 and the HPPs the individual meets as rights (HPP 1.1, 2.1, 2.2, 2.4,
4.2, 5.2, 6, 11); Part 6 for standing, the time limits that bind the complainant, and the Tribunal's cap; Part 7 for the
offences that protect the individual; Part 2 and s 3 for whether the Act reaches the body and the information.

**In:** ss 3(1) (health information, personal information, immediate family member, relative, parent, sibling,
legal representative), 5, 10, 11, 13, 14, 14A, 15, 16, 17(2), 14F(2), 18, 20(1), (6), 25, 26, 27, 28(1)(c), (2), (4),
29(2), 30, 31 (in the answer), 32, 33(4), 34, 35, 36, 38, 39, 40(2) (in the answer), 41, 42(3), 45(1), (4), 47, 51(1)(d),
(5), (9), 57(1), (5), 63(3), (4), (9), 65(1), (2), 78(1)(a)(iv) and closing words, 79 to 83, 85(2) to (6), 95, 96, HPP 1.1,
2.1, 2.2, 2.4, 4.2, 5.2, 6.1 to 6.7, 6.9, 6.10, 11.1, 11.2.

**Regulative rules:** three, each run by EVALTRACE inside an exported question that takes only dates and yes/no facts.
s 34(2): the organisation MUST answer the access request (a written refusal, a fee notice, or access) WITHIN 45 days of
receipt, LEST breach, which s 35(a) deems a refusal of access; in `Has my access request been answered in time`. s
34(2)(b)(ii): the organisation MUST give access WITHIN the later of 7 days after the fee is paid and 45 days after receipt;
in `Have I been given access in time after paying`. HPP 6.9: the organisation MUST notify its decision on a correction
request WITHIN 30 days of receipt; in `Has my correction request been decided in time`.

**Out, and why:**
- ss 1, 2, 4, 6, 9 (purpose, commencement, interpretation, objects, the Crown): machinery or guidance with no fact test.
  s 7 (other Acts prevail) and s 8 (no civil cause of action) are recorded as findings, not encoded.
- s 12 (outsourcing), ss 14B to 14E (information sharing under the family violence, child wellbeing, health services and
  terrorism laws), s 17(1) (news media and HPP 1, 2, 9): exemptions for particular bodies and schemes outside the focus; s
  14F(1) likewise.
- s 19, s 20(2) to (5), s 21 (the contract and transitional exemptions of 2002 to 2004, long spent): no live fact test.
- Part 4 (the Commissioner's guidelines) and ss 22 to 24: machinery; where a provision turns on guidelines, an input.
- ss 28(1)(a), (b), (3), 29(1), 33(1) to (3): the manner of access and the form of a request, with no yes/no answer for the
  person beyond those encoded (s 33(3)(d), writing for a representative's request, could be added); ss 37, 42(1), (2),
  (4) (the offer and the nominee's functions): the organisation's and the nominee's, no fact test for the person; ss 43,
  44 (alternative arrangements; the implied contract term, which could be added).
- Part 6 except the provisions listed above: the Commissioner's and the Tribunal's powers and procedure (ss 46, 48 to 50,
  51(1) other than (d), 52 to 56, 58 to 62, 64, 66 to 77). The Commissioner's own time limits (s 49(1) 90 days to decide
  whether to entertain, s 51(1) 90 days to decline, ss 52(2), 58(2), 64(2) 14 days) bind an official and could be added as
  what the complainant must be given, and by when. s 72 (28 days to seek review of a compliance notice) is the
  organisation's in practice.
- s 84 (offences before the Commissioner) and Part 8 except ss 85, 95 and 96: machinery, protection and regulation-making.
- HPP 1.2 to 1.7, 2.3, 2.5, 3, 4.1, 4.3 to 4.5, 5.1, 6.8, 7, 8, 9, 10: duties on the organisation with no fact test the
  individual can state beyond "was it done"; a breach of any of them is an interference with privacy and reaches the
  complaint questions through s 18. HPP 10 (closure or sale of a practice, 21-day notice) could be added.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 34(1), s 33(4)(b) an oral request the organisation has asked to be made in writing -- `By when must the
  organisation answer my access request` -- NOTHING (no period runs; "need not take any further action") -- 45 days from
  the oral request.
- **F2** "12 months after" (s 51(1)(d)), "attains the age of 25 years" and "7 years after" (HPP 4.2) -- `the date` n `months
  after` -- the same day of the month, or that month's last day where it is shorter (29 February 2028 plus 12 months is 28
  February 2029) -- 1 March (rolling over).
- **F3** HPP 6.1 "must provide ... unless" and s 41 "must give ... within 14 days ... unless within that period" with the
  "unless" met -- `Must I be given access`, `By when must my nominee receive the information` -- the organisation may
  refuse / no date -- NOTHING (the text does not say what follows once the "unless" is met). Ruled case by case on
  2026-11-05.
- **F4** s 32(2A) "must not charge a fee ... for providing access" -- `What is the most I can be charged` -- the bar reaches
  access, not the explainer's fee under s 32(4) -- it reaches the explanation too.
- **F5** HPP 5.2 "On request by an individual" -- `Must it tell me what it holds` -- no request: JUST FALSE (read as "if") --
  NOTHING.
- **F6** HPP 4.2(b)(i) "after the individual attains the age of 25 years" -- `When may my records be deleted` -- from the
  25th birthday (attained at its start) -- the day after.
- **F7** s 45(4) "A complaint must be in writing" -- `Can this complaint be made` -- not in writing: JUST FALSE -- NOTHING
  (s 45(6) the Commissioner must help formulate it). Ruled case by case on 2026-11-05 (a bare "must" not done).
- **F8** ss 26, 27, HPP 6.1, s 85(5), HPP 6.2 when several grounds hold -- `Must I be given access` -- the first in that
  order (the two "must not" grounds first) -- every ground that holds.
- **F9** s 96 against s 16 -- `Do I have a right of access` -- a privileged document of an FOI agency: no access under this
  Act -- access only under the Freedom of Information Act 1982 (that Act has its own privilege exemption, outside the
  sources).
- **F10** s 27(1) "Subject to subsection (3)", (3) "may consent to the information being communicated" --
  `Must I be given access` -- consent lifts the s 27 bar -- (3) permits the giver to consent but does not say the
  organisation must then give access.
- **F11** HPP 4.2(b)(i) "health information collected while the individual was a child" -- `When may my records be deleted`
  -- one date for the record, using age 25 if any of it was collected in childhood -- separate dates for each part.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 3 and the "if, and only if" of s 18 answer plain TRUE/FALSE; "nothing in this Act
applies" (ss 10(5), 11(4), 13, 14, 14A, 15, 14F(2), 16, 17(2)), "this Act does not apply" (s 96), "must not" (ss 26, 27,
32(2A), (5), HPP 1.1, 2.2, 4.2), "may not be charged ... unless" (s 32(2)), "does not apply" (s 39(2)), "except" (s
85(2)(a)(i), (6)), "void" (s 85(4)), "does not include" (personal information), "does not constitute" (s 20(6)), the "if"
conditions of ss 28(1)(c), 30, 35, 39(1), 85(2)(b), HPP 2.4, 6.5, 6.6, 11.1 and the periods of ss 39(1) and 51(1)(d) give
`JUST FALSE`. `NOTHING` is answered where a grant does not reach the person or body (ss 10, 11, 25, 45, 47, 85, 95, HPP 2.4,
6.5) (*limited by its own wording*), where the regulations or another law decide (HPP 4.2, s 42(3) with no maximum) (*points
outside the sources*, *silent*), and where the Act does not speak (HPP 6.10 with no refusal) (*silent*). The date questions
answer `NOTHING` where no period runs (ss 34(1), 36, 38(1), 41).

## What the Act turns out to say

1. **No civil action; the Tribunal's cap is the remedy.** s 8(1) says nothing in the Act gives rise to a civil cause of
   action or a right enforceable in a court or tribunal "otherwise than in accordance with the procedures set out in this
   Act". A refused or late access request, or a privacy breach, goes to the Health Complaints Commissioner and then the
   Tribunal, which may order access (s 78(1)(a)(i)) and compensation of at most $100 000 (s 78(1)(a)(iv)), plus expenses.
   For a claimant needing records, the access route is Part 5 (or the Freedom of Information Act 1982 for a public
   hospital or department, s 16), not a court order under this Act. Asserted (the cap).
2. **Public bodies leave Part 5 for the FOI Act.** s 16 takes a document of an agency within the Freedom of Information
   Act 1982 out of Part 5, HPP 5.2 and HPP 6 entirely, for access and correction alike. A patient of a public hospital
   therefore has no Part 5 right, deadline or fee rule against it, while the same record at a private hospital is under
   Part 5. Asserted.
3. **s 57(1) reads on every s 56(4) notice.** s 57 is headed "What happens if conciliation or ruling is inappropriate?",
   but (1) gives the right to require referral "Within 60 days after receiving the Health Complaints Commissioner's notice
   under section 56(4)", and s 56(4) covers every decision under s 56(1): to conciliate, to proceed to a ruling, or to
   decline. Read literally, s 57(3) then lets the Commissioner dismiss a complaint it has decided to conciliate if the
   complainant does not require referral within 60 days, and s 57(5) bars further action. Encoded as written for the date
   (60 days from any s 56(4) notice); the dismissal reading is not encoded. Asserted (the date).
4. **A parent of a capable child cannot ask.** s 85(2)(a)(i) lets a child make the request personally unless incapable,
   and s 85(2)(b) lets an authorised representative (including "a parent of an individual, if the individual is a child",
   s 85(6)(e)) act only if the individual is incapable. A parent of a 15-year-old who can understand and make the request
   has no s 85 power to request the child's records; the child may name the parent in a written authority (s 30). Encoded
   as written. Asserted.
5. **The second nomination has no period.** s 40(2): "If a nomination lapses, the individual may make one more nomination
   under section 38(1)". s 38(2)'s periods run from the notice of refusal or the discussion, and will often have passed
   when an organisation objects (it has 14 days, s 39(1)). Whether the second nomination has its own 21 days is not said.
   Not encoded beyond the first nomination.
6. **s 27 consent.** s 27(1) is "Subject to subsection (3)", and (3) says only that the giver "may consent to the
   information being communicated". Read as lifting the bar (fork F10). Asserted.
7. **HPP 6.1(c) runs two grounds together.** "the information relates to existing legal proceedings between the
   organisation and the individual and the information would not be accessible by the process of discovery in those
   proceedingsor is subject to legal professional privilege or client legal privilege". Without the missing space and a
   comma, the scope of "or" is unclear: privilege alone, or privilege only in existing proceedings. s 96 takes privileged
   documents out of the Act anyway. One input covers both readings.
8. **Fees with nothing prescribed.** s 32(2) bars a fee for a manner of access "unless a maximum fee has been prescribed";
   s 42(3) caps the nominee's fee at "the prescribed maximum fee" but does not say what follows if none is prescribed. With
   the regulations not deposited, the s 42 answer is NOTHING where no maximum is prescribed. Asserted.
9. **Conversion and drafting artefacts.** s 11(1), s 15(1) and s 100(1) print their first paragraph without "(a)"; s
   66(5)(b) breaks mid-sentence ("who / was a complainant"); HPP 2.2(h)'s closing words and HPP 4.2's "whichever is the
   later" print at the margin. Read as the Word file has them; HPP 4.2's "whichever is the later" read as governing (i)
   and (ii) together.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The Health Records Regulations (maximum fees, retention periods, prescribed exemptions and circumstances) and the
  Commissioner's guidelines under s 22, none deposited.
- A lawyer's view on findings 3, 4, 5 and 7 and forks F3, F8, F9 and F10, an independent test pass and a human gate.
