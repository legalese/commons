# Medical Treatment Planning and Decisions Act 2016 (Vic) -- baseline encoding, the person whose treatment it is

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`mtpd-rules.l4`), the
dates in another (`mtpd-dates.l4`, built-in date functions only, no daydate), and the questions in one seat module
(`mtpd-seat.l4`) that imports the rules and never restates one. The cases are in `mtpd-cases.l4`.

The focus asked for: advance care directives, medical treatment decision makers, consent. Those are Parts 2, 3 and 4 of
the Act, all encoded. Around them: decision-making capacity (s 4) and the eligible applicant definition (who may go to
VCAT), the consent gate for medical research (Part 5, ss 72, 75, 77, 80), rehearings and their time limit (s 88), health
information (s 94), interstate instruments (ss 95-97), the practitioner's protection from a claim (ss 49, 52), and the
offences that protect the person.

## Edition

- **Act:** Medical Treatment Planning and Decisions Act 2016, Act No. 69/2016, Version No. 012, incorporating amendments
  as at 1 July 2024 (the register's current version when read on 6 November 2026), deposited at
  `../../registers/source-bundle/medical-treatment-planning-and-decisions-act-2016.txt` (sha256 6da894cb...e1db60d2d, per
  its `.meta.json`), a plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see that file's
  `.meta.json` and `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the Act's numbers are in the Act (the 14 and 28 day periods, the penalty units). What the
  regulations prescribe (details of appointees, the training of a child's witness, prohibited statements, prescribed
  research procedures) is not deposited: each is asked as a fact. The value of a penalty unit (Monetary Units Act 2004) is
  not deposited: penalties are answered in penalty units.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `mtpd-dates.l4` | 0 | 0 | 0 | 0 |
| `mtpd-rules.l4` | 0 | 0 | 0 | 0 |
| `mtpd-seat.l4` | 0 | 0 | 0 | 0 |
| `mtpd-cases.l4` | 0 | 0 | 218 | 218 |

Every exported question has cases, with the edges: age 17 and 18 (presumption of capacity, a child's directive witness,
appointing a decision maker, s 55(4) against s 55(3), Part 5); one, two and three witnesses; each formal requirement
missed in turn; the day before and the day of an expiry date and of a revocation; each rung of the s 55 ladder; each
s 12(3) head; the last day and the day after for s 67(2) and s 88(3), with 28 days run across 29 February 2028 and from
written reasons; every constructor of every choice.

## Seat

**The person whose treatment it is** (`mtpd-seat.l4`): the individual who gives an advance care directive, appoints a
medical treatment decision maker or a support person, and may one day be treated, or asked to take part in research,
while unable to decide. "Do I have decision-making capacity?", "Is my directive valid, and in force?", "Is this statement
binding?", "Who decides for me?", "May I be treated without consent?", "Is the practitioner protected from my claim?",
"By when must I apply for a rehearing?". Where a family member or decision maker asks for the person, the questions are
still worded from the person's seat.

No seat for health practitioners, VCAT, the Public Advocate or ethics committees: their beliefs, opinions, consents and
orders are asked as facts. A seat for the medical treatment decision maker (the duties of s 61) would be a further layer.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no regulations are deposited (see Edition).
- **The actors the text names.** Followed: the person, the health practitioner, the medical research practitioner, the
  appointed medical treatment decision maker, the support person, the guardian, the spouse or domestic partner, the
  primary carer, children, parents, siblings, the witnesses, VCAT, the Public Advocate, the ethics committee.
- **Judgments answered conditionally.** Followed: "believes on reasonable grounds" (ss 51, 52, 53, 80), "reasonably
  believes" (ss 59, 62), "clinically appropriate" (s 60), "of the opinion ... unreasonable" (s 67), "reasonably available
  and willing and able" and "close and continuing relationship" (s 55), the four limbs of "significant treatment",
  "likely to recover ... within a reasonable time", VCAT's orders and satisfaction are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "adult", "child", "significant treatment",
  "routine treatment", "decision-making capacity", "eligible applicant", "instructional directive", "values directive",
  "medical treatment decision maker" are worked out; "mental health patient", "special medical procedure", "registered
  relationship", "authorised affidavit taker", "voluntary assisted dying" are asked.
- **One case.** One directive, one appointment, one treatment decision, one research procedure, one VCAT order.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (adult, child, eligible applicant, significant and routine treatment); s 4 (capacity); Part 2: ss 6, 8A, 12,
13, 14(2), 16, 17, 18, 19, 20, 21, 22(2)(a)(iii), (b); Part 3: ss 26, 28, 29 (as one input), 30, 31, 33, 34 (as one
input), 35, 36, 37, 38, 39(4), 42(2), 43(2), 45; Part 4: ss 48, 51, 52, 53, 54, 55, 57, 58, 59, 60(1), 62, 63, 67(1),
(2); Part 5: ss 72(1), (2), 75, 77 (the decision maker's consent, as an input), 79 and 80 (as one input), 84, 85; Part 6:
s 88; Part 7: ss 94, 95, 96, 97; Part 8: ss 102(2), 103 (in the s 55 input's description); the penalties of ss 14, 15,
41, 42, 84, 85.

**Regulative rules:** two. s 67(2): the Public Advocate MUST apply to VCAT WITHIN 14 days of the s 62 notification (day 0
the day of notification), LEST BREACH; s 88(3): the applicant DOes the rehearing application WITHIN 28 days of the day of
the order (day 0), LEST BREACH, the breach being the loss of the right to a rehearing. Each is run by EVALTRACE inside an
exported question that takes only dates and facts, through the helper shape the Wills Act 1997 encoding uses.

**Out, and why:**
- ss 1, 2, 100, 101, 104 and the endnotes: purpose, commencement, regulations, repeal, transitional research consents.
  s 102(1) (old refusal of treatment certificates continue under the repealed Act): noted, not encoded.
- s 5, s 22(1), (3), s 23, s 43(1), (3), ss 44, 46, ss 65, 66, 68-71, s 82, s 83, ss 86, 87, 89-92: what VCAT may be
  asked and must be satisfied of before it orders. VCAT's orders are inputs to the person's questions; the
  pre-conditions bind VCAT, not the person. Who may apply is in (eligible applicant).
- s 7 (principles), s 8 (no compulsion; used in one answer), s 9, s 10, s 11 (interpretation), s 25, s 49 (used in one
  answer), s 50, s 56, s 73, s 76, s 78, s 81, s 98, s 99: duties of practitioners, facilities and interpreters to
  search, record, certify and inform; they are taken as complied with or noted in the descriptions. A seat for the
  practitioner would carry them.
- s 15, s 41 as offences (the conduct) and s 93 (officers of bodies corporate): only the maximum penalties are encoded.
- s 24, s 47 (parties): noted in the eligible applicant question.
- s 32 (role of support person), s 39(1)-(3), s 40 (informing on resignation or revocation, which does not affect it):
  noted in the rules' comments.
- s 61 (how the decision maker must decide) and s 77(1)-(6): duties of the decision maker, whose decision is an input. A
  decision maker seat would carry them; s 61(5) and s 77(5) (no liability "of itself") are noted below.
- s 74 (the research practitioner's protection): parallel to s 52; not asked.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 13(a) with s 22(2)(b)(ii) -- `ss 13, 16, 17, 21, 22 -- whether my advance care directive is valid` -- lacking
  capacity for a statement is a failure "to comply with a requirement of this Part", so a VCAT declaration of validity
  cures it as it cures a formal defect -- the capacity condition of s 13 is not a "requirement of this Part" in s 22's
  sense and cannot be cured.
- **F2** s 19(2)(a) "remains in force until ... any expiry date that is specified in it" -- `ss 19, 20, 22 -- whether my
  advance care directive is in force` -- not in force on the expiry date itself -- in force through the expiry date.
- **F3** ss 28(1), 33 (a bare "must" not done) -- `ss 26-45 -- whether my appointment is valid` -- "not validly made",
  since s 45 speaks of "the attempt to make a valid appointment despite any non-compliance" -- NOTHING (the Act does not
  say an irregular appointment is invalid, and s 44(b) leaves invalidity to a VCAT declaration).
- **F4** s 42(2) -- the same function -- an induced support person appointment is not void (s 42 covers only decision
  makers), and the answer is "valid" if every formality is met -- NOTHING, since s 44(c) lets VCAT declare it invalid.
- **F5** s 39(4) (a bare "must" not done) -- `ss 30, 35, 38, 39 -- whether my appointment is in force` -- a resignation
  that is not in a signed, dated, witnessed writing does not end the appointment -- it ends it (s 39(1) "may resign" with
  s 39(4) as form only).
- **F6** s 63(1) "has not been able to locate an advance care directive or a medical treatment decision maker" --
  `Part 4 -- whether I may be given the treatment` -- read as "neither", so a directive with no relevant instructional
  directive and no decision maker leaves a gap (NOTHING-kind) -- read as "either is missing", so s 63 applies (finding 5).
- **F7** s 59 -- the same function -- s 59 is applied before s 60 and s 63, so a person likely to recover soon gets no
  routine treatment under s 63(1)(a) unless s 59 is met -- s 59 applies only where a directive or decision maker exists.
- **F8** s 53(1) "(other than electroconvulsive treatment)" -- `s 53 -- whether I may be treated in an emergency without
  consent` -- "not covered by s 53" (NOTHING-kind) -- a flat no.
- **F9** s 41 -- `the maximum penalty` -- one penalty with no body corporate figure: a body corporate is given the same
  600 penalty units (and an imprisonment term it cannot serve) -- the Sentencing Act 1991's body corporate multiplier (not
  deposited).
- **F10** s 55(2) -- `s 55 -- who my medical treatment decision maker is` -- a VCAT guardian is placed before s 55(4) for a
  child too, since s 55(2) is not limited to adults -- s 55(4) alone for a child.

Sites decided without a fork line: s 94 outside its terms, s 88(1) for a person neither a party nor given notice, s 72(1)
for a child, s 26(1) and s 31(1) outside their grants, and s 96 for a non-complying appointment answer NOTHING or a "not
covered" constructor (grants limited by their own wording, or silence).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions (adult, child, eligible applicant, significant treatment, medical treatment decision
maker), the "if" of ss 4(1), 13, 30, 35(1), 53(1), 62 and 88(1), "may only ... if" (ss 59, 63(1)(b)), "must not" (ss 72(2),
75), "does not take effect ... unless" (s 21(1)), "is void" (ss 14(2), 18(2), 42(2), 97), "is not permitted" (s 53(2)), the
"until" of s 19(2), and the periods of ss 67(2) and 88(3) give the text's own no; the protection of s 52 when its
conditions fail is worded "this section gives the practitioner no protection on these facts" (rule (b) on defences); the
sites above give NOTHING or a "not covered" constructor.

## What the Act turns out to say

1. **A refusal binds; a consent does not compel.** An instructional directive refusing treatment must be given effect by
   withholding or withdrawing it (s 60(1)(a)(i)), even over the decision maker's consent, unless the practitioner holds
   both s 51 beliefs; a consenting one is acted on only if the practitioner thinks it clinically appropriate
   (s 60(1)(a)(ii)), and s 8 says no directive can compel a particular treatment. Asserted.
2. **Interstate directives lose their binding force.** s 95(1) treats a complying interstate directive as given under the
   Act, but s 12(3)(c)(iii) makes every statement "made in a document of another State or a Territory recognised as an
   advance care directive under section 95" a values directive. A refusal written in New South Wales is, in Victoria,
   only a preference. Asserted.
3. **The person is not an "eligible applicant".** The s 3 list (health practitioner, decision maker, support person,
   Public Advocate, a person with a special interest) does not name the person who gave the directive or made the
   appointment, though ss 24, 47 and 71 make them a party once someone else applies. To start a proceeding about their
   own directive or capacity they must satisfy VCAT that they have a "special interest" in their own affairs. Asserted.
4. **A mental health patient's physical treatment has no Part 4 fallback.** s 48 removes only treatment for mental
   illness, but s 55(5) disapplies the decision maker ladder and s 63(3) disapplies the no-decision-maker rule "at any time
   that the person is a mental health patient", so ordinary physical treatment of a mental health patient without
   capacity and without a located directive has no route in this Act (the note points to s 92 of the Mental Health and
   Wellbeing Act 2022, not deposited). Asserted (the "not covered" answer).
5. **s 63 and a values-only directive.** s 60(1)(b) sends a decision to the decision maker when a directive has no
   relevant instructional directive; s 63 applies only where the practitioner "has not been able to locate an advance
   care directive or a medical treatment decision maker". A person with a values-only directive and nobody on the s 55
   ladder falls between them on the reading taken (F6). Asserted.
6. **Inducement voids a decision maker's appointment but not a support person's.** s 42 (offence and voidness) covers
   only appointed medical treatment decision makers; s 41 covers impersonating either. An induced support person
   appointment stands until VCAT declares it invalid under s 44(c) (F4). Asserted.
7. **Two "no liability of itself" clauses.** A decision maker who does not follow s 61's process (s 61(5)), or s 77's
   for research (s 77(5)), incurs no civil or criminal liability "of itself"; a person harmed must find liability
   elsewhere. Noted, not encoded.
8. **s 81(1) has a stray "a".** "a medical research practitioner a must sign a certificate" (the deposited text, as the
   Word file has it). Not encoded; noted for the authorised version.
9. **s 81(4) and s 84 print their penalties without "Penalty:".** The conversion shows "120 penalty units." and "240
   penalty units." on their own lines; read as the penalty. Asserted for s 84.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The regulations under s 100 (prescribed details, training, prohibited statements and procedures), the Mental Health and
  Wellbeing Act 2022 (mental health patients, s 92), the Guardianship and Administration Act 2019 (guardians, special
  medical procedures), the Powers of Attorney Act 2014 (s 103), the Monetary Units Act 2004, none deposited (the
  Guardianship and Administration Act 2019 has a subject here; its text was not read for this encoding).
- A lawyer's view on findings 2, 3, 4 and 5 and forks F1, F2, F3, F6 and F7; a decision maker seat (s 61); an independent
  test pass and a human gate.
