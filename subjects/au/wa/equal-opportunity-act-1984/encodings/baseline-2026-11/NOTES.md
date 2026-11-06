# Equal Opportunity Act 1984 (WA) -- baseline encoding (work, and the complaint)

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this Act in Commons. Four files:

- `eoa-dates.l4` -- date arithmetic with the built-in date functions (not the daydate library);
- `eoa-work.l4` -- the meaning of discrimination for every ground, the employer's duties to job applicants and
  employees, the work exceptions, sexual and racial harassment in employment, victimisation, and who is answerable
  (10 exported questions);
- `eoa-complaints.l4` -- the complaint to the Commissioner for Equal Opportunity and the inquiry by the State
  Administrative Tribunal (21 exported questions);
- `eoa-cases.l4` -- the worked cases.

Every exported question has `@export` and a `@desc` on every input, takes plain facts (yes/no, a number, a date, a
choice from a list), and none takes a DEONTIC or an EVENT. The deadlines the complainant meets are regulative rules
(`PARTY ... MUST ... WITHIN ... HENCE FULFILLED LEST BREACH ... BECAUSE`), run by `EVALTRACE` inside the questions:

- s 83(4): lodge the complaint within 12 months after the alleged contravention (late, it needs the Commissioner's
  acceptance on good cause, s 83(5));
- s 83A(2): answer a lapse warning within 21 days, or the complaint lapses (s 83A(3));
- s 83A(4)(d): pursue a withdrawn or lapsed complaint afresh within 6 months;
- s 90(1): require the Commissioner to refer a dismissed complaint to the Tribunal within 21 days after receiving the
  notice (a permission with a fixed time, written as MUST so that missing it shows; missing it is no breach of a duty).

## Edition

- **The Act:** the compilation of the Equal Opportunity Act 1984 (WA) on the Western Australian Legislation website,
  retrieved 7 September 2026 (law_a253, mrdoc 48472), deposited at `../../registers/source-bundle/mrdoc_48472.txt`. Its
  compilation table ends with the Industrial Relations Legislation Amendment Act 2024 Pt 4 Div 1 (No. 43 of 2024, in
  operation 31 January 2025), which inserted s 83B; the entry before it is the Births, Deaths and Marriages
  Registration Amendment (Sex or Gender Changes) Act 2024 Pt 4 Div 7 (No. 31 of 2024, in operation 30 May 2025), which
  widened "gender reassigned person" in s 4(1). Both are encoded.
- **The focus given was "reforms under way".** Commons records nothing about reform Bills for this Act, and none is
  deposited. This encoding is of the Act as compiled; it says nothing about any Bill or amending Act not in that
  compilation. A reform that changes the grounds, the definitions of discrimination, the exceptions, the 12-month time
  limit, the complaint process or the $40,000 damages cap would change the answers (finding 1).
- **Regulations:** the Equal Opportunity Regulations 1986 are not deposited. The Act lets regulations declare
  positions for which sex is a genuine occupational qualification (s 27(2)(h)), switch off Part IVA for notifiable
  infectious diseases (s 66U) and prescribe sporting activities (s 35(2)(d)). The first is folded into an input
  ("the employer has shown ... a genuine occupational qualification"); the others are outside this encoding's scope.
  No regulation sets a number this encoding uses. Penalties in this Act are in dollars, not penalty units.

## Checks

- Stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset: `l4 run eoa-dates.l4`, `l4 run eoa-work.l4`,
  `l4 run eoa-complaints.l4`, `l4 run eoa-cases.l4`.
- **171 assertions written, 171 satisfied, 0 errors, 0 warnings** in every file (2026-11-07). All assertions are in
  `eoa-cases.l4`.
- Every expected value was worked by hand from the text before the file was run; all 171 held on the first full run.
  No expected value was copied from the encoding's output.
- Three expectations were changed in a scratch copy (a complaint lodged one day late given as in time; $40,001 given
  as awardable; a referral notice served on day 22 given as in time); the run reported all three as failing, so the
  runner catches a wrong expectation.

## Seat

**The employee or job applicant, and then the complainant** (`eoa-work.l4`, `eoa-complaints.l4`): the person who says an
employer discriminated against them on one of the Act's grounds (sex, marital status, pregnancy, breast feeding or
bottle feeding, gender history, family responsibility or family status, sexual orientation, race, religious or
political conviction, impairment, age, publication of their details on the Fines Enforcement Registrar's website),
that someone sexually or racially harassed them at work or when they were seeking work, or that they were victimised
for using the Act; and who complains to the Commissioner for Equal Opportunity and may go on to the State
Administrative Tribunal. Questions: "Is this discrimination as the Act defines it?", "Am I a gender reassigned person?
Do I have an impairment, a family responsibility?", "Was what my employer did unlawful, or does an exception let it do
it?", "Was I harassed unlawfully?", "Was I victimised?", "Is my employer answerable for what its employee did?", "Who
may lodge my complaint, and by when?", "Can it still be accepted late?", "Does taking sexual harassment to the
industrial system stop my complaint?", "Can I withdraw it, has it lapsed, can I revive it?", "If it is dismissed, can I
get it to the Tribunal?", "Who may appear for me in conciliation?", "Will the Commissioner help me at the Tribunal?",
"What can the Tribunal order, and how much can it award me?", "Can I appeal?", "Whom may I tell about my sexual
harassment complaint?".

The employer, harasser and victimiser are the persons the Act binds; no seat was written for them (see "Before this is
worth relying on"). The Commissioner, the Tribunal and the Minister get no seat: their opinions and decisions are asked
as facts.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No regulation is deposited or needed for a
  number. The Industrial Relations Act 1979 (s 83B), the Gender Reassignment Act 2000 and the Births, Deaths and
  Marriages Registration Act 1998 (s 4(1)), the Fines, Penalties and Infringement Notices Enforcement Act 1994 (s 67A)
  and the State Administrative Tribunal Act 2004 (s 134) are borrowed and asked as facts.
- **The actors the text names.** Followed: the aggrieved person, employee, applicant, complainant, employer,
  respondent, harasser, victimiser, trade union, the Commissioner, the Tribunal.
- **Judgments handed to someone else are answered conditionally.** Followed. "Not reasonable having regard to the
  circumstances", "reasonable grounds for believing", "genuine occupational qualification", "unjustifiable hardship",
  "reasonable health and safety considerations", "good faith", "good cause", the Commissioner's opinions and
  satisfaction, and the Tribunal's findings are inputs. Under s 123 the respondent must prove an exception, so each
  exception input reads "has the employer shown that ...".
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: discrimination for every ground
  (ss 5, 8 to 10A, 35A, 35AB, 35O, 36, 53, 66A, 66V, 67A), gender reassigned person, impairment, family responsibility
  or family status (s 4(1)), sexual and racial harassment (ss 24(3), (4), 49A(3), 49D). Asked: the facts under them.
- **One case is the text's natural unit.** Followed: one act of an employer (or harasser, or victimiser) towards one
  person, and the one complaint about it.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

In:

- s 4(1) (complainant, complaint, employment, family responsibility or family status, gender reassigned person,
  impairment, near relative, race, relative, representative complaint, respondent), s 5;
- the meaning of discrimination: ss 8, 9, 10, 10A, 35AB, 35A, 35O, 36, 53, 66A, 66V(1), (3), 67A;
- discrimination against applicants and employees: ss 11, 35AC, 35B, 35P, 37, 54, 66B, 66W, 67B;
- the exceptions that reach an employer's acts towards applicants and employees: ss 11(3), 27, 28, 29, 31, 33,
  35AC(3), 35B(3), (4), 35K, 35M, 35P(3), 35ZD, 37(3), 50, 51, 54(4), 66, 66B(3), 66Q(1), (2), 66R, 66S, 66W(3), 66ZM,
  66ZN(1), 66ZP, 66ZQ, 66ZS(1), 69, 72, 73(1);
- sexual harassment in employment (s 24(1), (3), (4)), racial harassment in employment (ss 49A(1), (3), 49D),
  victimisation (s 67), liability (ss 160, 161);
- complaints and the Tribunal: ss 83, 83A, 83B, 89, 90, 91, 92, 93(1)-(3), 107(3), (3a), (5), 108, 123, 126, 127,
  134(1), 165.

Out, and why:

- **The other work relationships** in each Part's Division 2 (commission agents, contract workers, partnerships of 6 or
  more, professional or trade organisations, qualifying bodies, employment agencies: ss 12-17 and their fellows), and
  s 24(2), s 49A(2). They repeat the employee rules for other relationships; the focus is the employee and applicant.
  A second pass could add them by widening `What was done`.
- **The other areas** (Division 3 of each Part: education, access to places, goods, services and facilities,
  accommodation, land, clubs, sport, superannuation; ss 25, 26, 49B, 49C harassment in education and accommodation),
  ss 23 and 35AQ (requests for information) and their exceptions (ss 30, 32(2), 34, 35, 66T, 66ZO, 66ZR, 67I(3)):
  outside the employment focus.
- **s 32(1), s 35L** (accommodation of different standards for employees), **s 66ZN(2)** (judicial retirement) and
  **s 66U**: narrow; no regulation deposited for s 66U.
- **ss 70, 71, 74** (charities, voluntary bodies, aged housing): not employment.
- **s 68** (advertisements): an unlawful act anyone may complain of, but not one done to the person in the seat.
- **s 135** (Tribunal exemptions): an exemption in force would make conduct lawful; it is not asked (see "Before this
  is worth relying on").
- **Part VII Division 1, ss 80-82, 84-88, 93A, 94-96**: the Commissioner's office, functions and investigation powers.
  The complainant's duty to attend a compulsory conference (s 87) and the offences in ss 155-159 are not encoded.
- **ss 113-117** (representative complaints at the Tribunal), **s 122**, **ss 162-164, 166-169**, **Part VIII
  Divisions 1 and 3**, **Part IX** (equal employment opportunity management plans in public employment: duties of
  public authorities with no individual right) and **ss 1-3, 6, 7**: machinery.

## Fork register

Sites decided case by case under the ruling of 2026-11-05, each with the answer taken and the other reading, for the
human reviewer to overrule.

- **F1** s 83(4) "within 12 months after the date", s 83A(4)(d) "within a period of 6 months from" --
  `plus calendar months` in `eoa-dates.l4` -- the same day of the month that many months on, and the last day of the
  month where there is no such day (29 February 2024 + 12 months = 28 February 2025; 31 August 2025 + 6 months =
  28 February 2026); that day itself is in time. Other reading: the period ends the day before the corresponding date,
  or on 1 March. "within 21 days after" (ss 83A(2), 90(1)): the day plus 21, the day of service or receipt excluded.
- **F2** s 54(3) "discriminate against an employee on the ground of the employee's religious conviction by refusing the
  employee permission to carry out a religious practice ... being a practice (a) ... (b) ... (c)" -- `the work answer`
  -- refusing permission for a practice meeting (a) to (c) is taken as the discrimination itself, with no separate
  less-favourable-treatment test; outside (a) to (c), the text's no. Other reading: s 53 discrimination must also be
  shown.
- **F3** ss 35O(2), 36(1a), 66A(1a) (discrimination through a relative's or associate's attribute) against ss 35P,
  37, 66B ("on the ground of the person's sexual orientation", "on the ground of the race of that person", "on the
  ground of the person's impairment") -- `the work answer for discrimination` -- NOTHING-kind: the work sections speak
  of the person's own attribute, and the text does not say whether associate discrimination falls within them. Other
  reading: the definitions exist to be used by the unlawful-act sections, so associate discrimination is unlawful in
  work too (finding 5).
- **F4** s 66A(4) (guide dog or hearing dog) -- `the meaning of discrimination` -- treated as discrimination on the
  ground of impairment, so within s 66B. s 66A(4) does not itself say "on the ground of impairment". Other reading: it
  is a free-standing definition that s 66B, which speaks of "the person's impairment", does not reach.
- **F5** s 83(1) "a contravention of this Act, other than a contravention in respect of which a specific penalty is
  imposed" -- `s 83 -- who may lodge my complaint` -- the text's no. Other reading: NOTHING (the Act is silent on how
  such a contravention is raised).
- **F6** s 83(4) "the date on which the contravention ... is alleged to have been committed", for conduct over a
  period -- the person gives the last day. Other reading: each act runs from its own date.
- **F7** an event dated before the start of a period (a notice served before the dismissal notice was received) --
  `the day number of` -- counted as day 0, in time. Other reading: NOTHING.
- **F8** s 83A(3) "lapses at the end of that period" -- `s 83A(3) -- has my complaint lapsed` -- lapses at the end of
  the 21st day after service; with no notice served the answer gives that day. The question cannot know whether a
  notice will still be served, so "no notice" means none within the period.
- **F9** ss 24(3), 49A(3) "shall ... be taken to harass ... if" -- the harassment questions -- a deeming "if", read as
  the text's no when it is not met. Other reading: NOTHING (the ordinary meaning of harassment is not excluded).
- **F10** the exceptions -- `the work exception for` -- the first that applies, in the order of the Act, is reported;
  one is enough to make the act lawful. Several paragraphs are asked as one input where they share an effect (s 27(2)
  (a)-(h); s 66ZS(1)(a) and (b); s 72(a)-(d); s 31, s 35B(4) and s 35K).
- **F11** s 67(1) and s 160 outside their wording; s 83(1) for an unlisted lodger or an unwritten complaint; s 89
  without a ground; s 93(1) before any occasion; s 93(2) for a s 90 referral; s 126 before lodging; s 134 for a
  non-aggrieved party -- NOTHING-kind (a grant or prohibition limited by its own wording). Other reading: the text's no.

Sites decided without a fork line: the "means" definitions of s 4(1) and the "if" of each definition of
discrimination answer the text's no; so do "Nothing in ... renders it unlawful" (the exceptions), the flat negatives
of ss 83B(2), 92(1)(b), 107(3a), 165(1), the "unless" of s 83A(4)(c), the "where" of s 161(1), and s 161(2) ("does not
apply if it is established"). The periods the text fixes (ss 83(4), 83A(1), 83A(2), 83A(4)(d), 90(1)) answer the
text's no outside them, as the periods ruling says.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` answers in the work, harassment, victimisation, s 160 and complaint questions
(forks F3, F11 and the gender history scope limit), and follows these rulings:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## What the Act turns out to say

1. **The deposited text has no reform in it after January 2025.** The focus named reforms under way; the compilation's
   last amending Act is No. 43 of 2024 (s 83B, from 31 January 2025). Whatever reform of the Act is in train is not in
   the deposited text and is not encoded. The 12-month time limit (s 83(4)) and the $40,000 cap on damages
   (s 127(b)(i)), both fixed figures, are the ones a reform would most visibly change. Asserted as the compiled text
   stands.
2. **s 67A defines the fines-website ground "In this Division".** s 67A is the whole of Division 1 of Part IVC; the
   unlawful acts that use the definition are in Divisions 2 and 3. Read literally, s 67B would have no definition of
   discrimination to use. The encoding applies s 67A to s 67B, as the scheme plainly intends; it may be a drafting
   slip ("this Division" for "this Part"). Asserted (s 67B cases).
3. **The domestic-duties exceptions differ by ground for no stated reason.** Sex and sexual orientation: the choice of
   whom to employ only (s 11(3), s 35P(3): "subsection (1)(a) and (b)"), for work "on the premises on which the
   firstmentioned person resides". Family responsibility, race, impairment, age: all of subsection (1) (applicants,
   including the terms offered). Gender history: subsections (1) and (2) (employees too). Religious or political
   conviction: all of s 54, plus a small-employer exception (5 or fewer employees, not counting domestic workers;
   s 54(4)(b)). Marital status, pregnancy, breast feeding and the fines-website ground: none. s 11(3) also speaks of
   "a person" discriminating rather than "an employer". Asserted.
4. **Racial harassment by a customer is outside s 49A(1); sexual harassment by a customer is not outside s 24(1).**
   s 24(1) protects "an employee of that or any other person"; s 49A(1) only an employee of the harasser, an employee of
   the harasser's employer, and a job seeker with either. Asserted.
5. **Associate discrimination may not be unlawful in work.** ss 35O(2), 36(1a) and 66A(1a) define discrimination
   through a relative's or associate's attribute, but ss 35P, 37 and 66B make it unlawful to discriminate "on the
   ground of the person's" own attribute. The encoding answers NOTHING-kind (fork F3). Asserted. s 66V(2) (age, through
   an associate) is expressly confined to ss 66ZE to 66ZG.
6. **The Commissioner's help at the Tribunal follows only the Commissioner's own referral.** s 93(2) applies "When a
   complaint is referred to the Tribunal under subsection (1)"; a complaint the complainant forced to the Tribunal
   after a dismissal (s 90(2)) gets no duty of assistance, and s 93A (appeal help) needs s 93(2) help first. Asserted.
7. **No damages on a representative complaint.** s 127(b)(i) and (iii) exclude representative complaints and Minister's
   references; the Tribunal can still enjoin the conduct or void a contract. Asserted.
8. **s 83B (2024) runs one way.** A sexual harassment allegation taken to the industrial system (Industrial Relations
   Act 1979 s 29 referral or s 83E application) cannot then be complained of under s 83 unless the industrial step was
   withdrawn or failed for want of jurisdiction; the deposited Act says nothing of the reverse order. Asserted.
9. **s 54(4)(b)'s count.** "does not exceed 5": an employer of exactly 5 (not counting domestic workers) is outside
   s 54; of 6 is within it. The exception reaches religious and political conviction only. Asserted.
10. **Only the pregnancy definition carries a reasonableness defence to direct discrimination** (s 10(1)(b)); no other
    ground's direct limb does. Asserted.

## Before this is worth relying on

- Check whether any reform of the Act has passed or commenced since the compilation retrieved on 7 September 2026, and
  deposit it beside the current text; re-run the cases.
- Deposit the Equal Opportunity Regulations 1986 (s 27(2)(h) positions; s 66U; s 35(2)(d)).
- Ask whether a Tribunal exemption under s 135 covers the employer (not asked now).
- An independent test pass, and a human read of forks F2, F3, F4 and F9.
- An employer seat (`eoa-seat-employer.l4`) over the same rules, with mirror cases.
- The other work relationships and the other areas (Division 3 of each Part), if the Act is to be covered whole.
