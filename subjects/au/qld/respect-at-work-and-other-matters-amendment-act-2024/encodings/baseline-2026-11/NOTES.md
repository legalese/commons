# Respect at Work and Other Matters Amendment Act 2024 (Queensland) -- baseline encoding, the complainant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this subject; nothing existing was touched. The Anti-Discrimination Act 1991, which this
Act amends, is deposited beside it (`subjects/au/qld/anti-discrimination-act-1991/`) with no encoding yet.

**The focus is commencement.** This is an amending Act whose own s 2 commences it in three groups, and the deposited
1991 Act shows that only one of them has commenced as s 2 provides. The encoding therefore:

1. encodes s 2 for every provision of the Act (`rawq-commencement.l4`), as passed;
2. checks each provision against the deposited Anti-Discrimination Act 1991 (the version in force from 19 May 2025,
   current on 6 November 2026), by hand, and records what that text shows;
3. encodes, for the complainant, the amended provisions a complaint meets, taking the 1 July 2025 group's commencement
   as two plain facts (has it commenced; on what day) rather than assuming 1 July 2025.

Files: `rawq-dates.l4` (built-in date functions only, no daydate); `rawq-commencement.l4` (s 2 and the deposited-text
check); `rawq-claimant.l4` (the complainant's 17 exported questions, each calling a rule defined beside it, grouped
under `§§` headings in the Act's order); `rawq-cases-claimant.l4` (worked cases).

## Edition

- **Act:** Respect at Work and Other Matters Amendment Act 2024 (Qld), `act-2024-047`, as passed (published on the
  register 2024-09-19). It is not in the in-force collection on 6 November 2026. Deposited at
  `../../registers/source-bundle/act-2024-047.txt` (text sha256 `004b8e9e...d8f813` of the committed file, per its
  `.meta.json`; a Windows checkout with CRLF line endings hashes differently). A plain-text conversion of the
  Queensland Legislation HTML view, not the authorised PDF.
- **Read against:** the Anti-Discrimination Act 1991 (Qld), `act-1991-085`, the version in force from 19 May 2025,
  current on 6 November 2026 (`../../../anti-discrimination-act-1991/registers/source-bundle/act-1991-085.txt`).
- **Not deposited, and asked as facts:** whether the 1 July 2025 group has commenced and on what day (the later
  legislation that deferred it is not deposited); whether a person conducts a business or undertaking (Work Health
  and Safety Act 2011 s 5); whether a union is registered under the Industrial Relations Act 2016 or the Fair Work
  (Registered Organisations) Act 2009. **Not deposited, and not answered:** the Acts Interpretation Act 1954 (for
  provisions s 2 does not name), the Administrative Review Tribunal Act 2024 (Cwlth) s 8 commencement day, the former
  ss 146 to 152, 204 to 206 (whose text the 1991 Act no longer holds), and the QCAT Act and Industrial Relations Act 2016
  rules on costs.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read:
every diagnostic in the case file is `DiagnosticSeverity_Information` "assertion satisfied" (146 distinct ranges).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `rawq-dates.l4` | 0 | 0 | 0 | 0 |
| `rawq-commencement.l4` | 0 | 0 | 0 | 0 |
| `rawq-claimant.l4` | 0 | 0 | 0 | 0 |
| `rawq-cases-claimant.l4` | 0 | 0 | 146 | 146 |

Every exported question has cases, with the edges: the day before and the day of 1 December 2024 and 1 July 2025;
each s 2 group and the unnamed provisions; the 1 July 2025 group not commenced, commenced on 1 July 2025 (as passed),
and commenced on an invented later day (1 March 2027), with conduct the day before and the day of it; the last day of
the 1-year and 2-year complaint periods and the day after; a contravention exactly 1 year before the commencement and
the day before that (s 283); 29 February; a complaint made before the commencement about a contravention the new
period would cover; each s 120A to 120E relationship and each limb of s 120; each event in s 148(2) and (3), the
complainant's own position, and the tribunal's opt-out date and the day before it; each costs role.

## Seat

**The complainant** (`rawq-claimant.l4`): the person who was subjected to an alleged contravention of the
Anti-Discrimination Act 1991 -- discrimination, sexual harassment, harassment on the basis of sex, a work environment
hostile on the basis of sex, vilification -- and who complains, or may complain, to the Queensland Human Rights
Commissioner, alone or as a member of a class in a representative complaint. "Has this change commenced?", "Is my
attribute protected?", "Was it harassment on the basis of sex?", "Does the positive duty protect me?", "Am I in time,
and by when must I complain?", "Who may act as my agent?", "Can I bring, leave or still complain outside a
representative complaint?", "Can costs be ordered against me?", "Who must prove what?".

No second seat is written. The respondent (an employer or business) meets the same provisions from the other side,
and the positive duty is a duty on it; a respondent seat would be a natural addition once the 1 July 2025 group
commences. No seat for the commissioner, the tribunal, the industrial relations commission or the Minister.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers and dates.** Followed, with a departure the focus forces:
  s 2's own days are encoded, but the later legislation that deferred the 1 July 2025 group is not deposited, so that
  group's commencement is asked (two facts), as the guide says to do for a number set by an instrument not deposited.
  The deposited 1991 Act is read as evidence of what has commenced, and its s 285AA (finding 3) is followed for the
  burden of proof because it is the law the complainant now meets.
- **The actors the text names.** Followed: the complainant, class members, a registered employee organisation, the
  respondent, the commissioner, the tribunal.
- **Judgments answered conditionally.** Whether a reasonable person would have anticipated offence (ss 120(1)(c),
  124E(2)(c)), whether there is a substantial common issue (s 146(1)(b)(iii)), whether a complaint is work-related, and
  whether a person is bound by a chapter 2 to 5 prohibition are asked; whether the commissioner finds good cause
  (s 138(2)) is stated in the answer, never decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "harassment on the basis of sex" (s 120),
  "subjects ... to a work environment that is hostile on the basis of sex" (s 124E(2)), "attribute" (schedule 1, from
  s 7's list), "class member" (by its parts). Asked: "person conducting a business or undertaking" (WHS Act s 5),
  "registered organisation", "work-related matter".
- **One case.** One complaint (or one representative complaint), one alleged contravention.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Here s 2 is the focus and is in; the commissioner's investigation and
  compliance machinery (chapter 7 part 1A), guidelines, functions and the amendments of court and judicial Acts are out.

## Scope

**In (rules and exported questions):**
- s 2 -- every provision, by group (`When does this change commence under s 2`, `Had this change commenced on that day
  under s 2 as passed`), and its status against the deposited 1991 Act (`What is the commencement status of this
  change`);
- s 7 (amending 1991 Act s 7: new and renamed attributes) with schedule 1 "attribute";
- s 18 (new ch 3 pt 3: s 120 and ss 120A to 120E, harassment on the basis of sex);
- s 22 (new s 124E, with s 124F as the gloss of the asked judgment);
- s 25 (new ch 5C: s 131I) with s 52(4) (schedule 1 "contravention") and the s 131H note;
- ss 28(2), (6) (new s 134(2)) with s 51 (new s 284);
- s 29 (new s 138) with s 51 (new s 283) -- the complaint period, as a regulative rule;
- s 31 (new ss 146, 148, 149) and s 47 (new ss 195, 196) -- representative complaints, separate complaints, opting out;
- s 48 (s 209(5), costs);
- s 47A (new ss 204, 205) with s 51 (new s 285A) and the 1991 Act's s 285AA -- the burden of proof;
- s 51 (new s 285) -- existing representative complaints.

**Out, and why:**
- ss 7A, 7B (combined attributes; new direct and indirect discrimination, ss 10, 11, 11A): definitions of the
  substantive wrong whose areas (ch 2 pts 4, 5) are in the 1991 Act, not here; encoding them belongs with a 1991 Act
  encoding. Their commencement is in.
- s 21 (vilification, ch 4 pt 4) and s 124 changes: the same reason. Commencement in.
- ss 30, 44 (ss 141A, 175 -- the out-of-time deferral and referred complaints): named in the time-limit answer, not
  encoded as questions; s 283(2) keeps the former versions for old contraventions.
- ss 32 to 36, 39 to 43, 49, 50 (investigations, compliance notices, undertakings, guidelines, functions): powers of the
  commissioner, QCAT and the industrial relations commission; for the complainant they appear only as "the
  commissioner may investigate and enforce" in the positive duty answer.
- ss 147, 150 to 152A, 170(6), 172(2), 193(4), (5), 194, 197 to 203A: the form of a representative complaint and the
  commissioner's and tribunal's powers over it; the complainant's position under them appears in the separate
  complaint and opt-out answers.
- ss 286, 287 (existing investigations and directions): machinery.
- Parts 3 to 11 and schedule 2 (Corrective Services Act, Criminal Code, courts and judges, Penalties and Sentences Act,
  QCAT Act, Supreme Court Act, Youth Justice Act, Human Rights Act, Commonwealth tribunal references): amendments of
  other Acts; only their commencement is encoded.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 2(1)(b) "sections ... 46 to 48" -- `s 2 -- when it commences` -- s 47A, numbered between ss 47 and 48, is
  within the range and commences on 1 December 2024 (the deposited 1991 Act agrees: new ss 204 and 205 are in it, and
  its s 285AA speaks of them "as in force from 1 December 2024") -- a range names only the sections so numbered when
  the Bill was introduced, so s 47A falls in s 2(2)(a) (1 July 2025).
- **F2** provisions s 2 does not name (ss 1, 2, 55, 59A, part 4's heading, parts 5, 6A, 7, 8, 9, 9A, 10) --
  `s 2 -- when it commences`, `s 2 -- commenced by` -- "left to the Acts Interpretation Act 1954", NOTHING for a day --
  on assent (the usual rule, but that Act is not deposited and the assent day is not in the deposited text).
- **F3** s 2(2) -- `the July 2025 changes are in force on` -- the whole 1 July 2025 group commences together, on one
  asked day -- later legislation may have split it, as s 285AA's tie to "section 7B" hints; then a question would need
  the day for its own provision.
- **F4** s 7(2) "(n) sexual orientation" in place of "(n) sexuality" -- `s 7 -- added by the amending Act` -- the same
  ground renamed, protected throughout -- a new ground from commencement, if "sexual orientation" (now defined,
  including lack of capacity for attraction) is wider than "sexuality" was.
- **F5** s 7(3) "(p) family, carer or kinship responsibilities" -- same function -- family responsibilities are an old
  ground; carer and kinship responsibilities beyond the family are new -- the whole ground is new, since the definition
  of "family responsibilities" is omitted (s 52(1)).
- **F6** new prohibitions (ch 3 pt 3, s 124E, ch 5C, the new attributes) and conduct before they commence -- the
  harassment, hostile environment, positive duty and attribute questions -- conduct before the commencement is not
  caught -- the Act says nothing expressly; a retrospective reading is not open on the text, but the answer is a
  reading.
- **F7** s 131I(1) "This section applies to a person who, under chapter 2, 3, 4 or 5, must not engage in ..." --
  `s 131I -- the positive duty` -- a scope limit with no "only": outside it, "not covered" (NOTHING kind) -- "no" (the
  section applies only to such persons).
- **F8** s 195(1)(a) "before the date fixed" -- `ss 148(1)(a), 195 -- opting out` -- notice given on the opt-out date
  is too late -- notice on that date, before the day ends, is in time.
- **F9** s 283(1) "more than 1 year before the commencement" -- `s 283(1) -- more than 1 year before the
  commencement` -- more than 1 year when the day 1 year after the contravention is before the commencement day (a
  contravention on 1 July 2024 is not more than 1 year before 1 July 2025) -- counting so that the anniversary day
  itself is more than a year.
- **F10** "within 1 year of" (former s 138(1)), "within 2 years after" (new s 138(1)) -- `the date ... years after`,
  `s 138 -- am I in time` -- the period ends at the end of the anniversary day; a contravention on 29 February runs to
  28 February -- to 1 March, or the day before the anniversary.
- **F11** same function, a complaint dated before the alleged contravention -- "in time" -- "not covered".
- **F12** s 148(2), (3) "other than the complainant" -- `ss 148, 149 -- my own complaint` -- the complainant stays
  barred by s 148(1)(b) unless they opt out -- the complainant is outside s 148(1)(b) altogether (they made the
  complaint, so a "separate" complaint is not in point).
- **F13** burden of proof -- `ss 204, 205, 285AA -- the burden of proof now` -- the exported answer follows the 1991
  Act's s 285AA (later legislation, deposited) rather than s 285A as passed, and a contravention on the commencement day
  itself is not "before" it -- s 285A as passed (kept, not exported, as `ss 204, 205, 285A -- new burden of proof under
  the Act as passed`; finding 3).
- **F14** s 146 before 1 December 2024 -- `s 146(1) -- I may make a representative complaint`, `s 146(2) -- ...` --
  NOTHING (the former s 146 governs and is not deposited) -- JUST FALSE.
- **F15** s 284 "a complaint made before the commencement" -- `ss 134, 284 -- my agent` -- the day the complaint is
  made decides, whatever the day of the contravention -- the day the agent was appointed.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: s 120 ("happens if"), s 124E(2) ("if") and schedule 1 "attribute" ("means") are definitions, so a failed
limb is a "no" constructor; s 134(2) ("can not be") and s 148(1)(b) ("is not entitled ... unless") are flat
negatives, "no"; s 131I(2) "only if" is "no"; s 2's fixed days are periods the text fixes, JUST FALSE before them;
s 146 ("if") answers JUST FALSE when a limb fails; s 131I(1) is a scope limit, "not covered" (F7); a provision s 2 does
not date, and s 146 before 1 December 2024, answer NOTHING (F2, F14); costs outside a representative complaint, and
anything the former law governs under s 285, are "not covered".

## What the Act turns out to say

1. **The 1 July 2025 group did not commence on 1 July 2025.** s 2(2) sets 1 July 2025 for the provisions of part 2
   not in force on 30 June 2025, part 3, ss 56 to 59, part 6 and schedule 1. None of the part 2 or schedule 1 changes
   is in the Anti-Discrimination Act 1991 in force from 19 May 2025 and still current on 6 November 2026: s 7 still
   lists "sexuality" and "family responsibilities", ss 10 and 11 keep the comparator and proportion tests, s 138 keeps
   "1 year", s 175 "more than 1 year", there is no ch 3 pt 3, s 124E, ch 5C or ch 7 pt 1A, and schedule 1's
   "unfavourably" wording is unchanged in 14 places. The 1991 Act's s 285AA, inserted by later legislation, speaks of
   "the commencement of section 7B of the amendment Act" without a day. Later legislation, not deposited here, has
   deferred (or changed) the commencement. Asserted (status "due on 1 July 2025 ... does not contain it" for ss 7B,
   18, 28(2), 29, 51 (ss 283 to 287) and schedule 1). The deferring Act should be found and deposited; every question
   here asks the commencement as two facts until it is.
2. **s 47A commenced on 1 December 2024** (F1). It is not named in s 2(1) but falls within "46 to 48"; the deposited
   1991 Act shows the new ss 204 and 205. Asserted (`p s47A` is `Dec` and "commenced ... contains it").
3. **As passed, the new burden of proof had no transitional rule for seven months.** s 47A (new ss 204, 205) commenced
   on 1 December 2024, but s 285A, which keeps the former ss 204 to 206 for complaints made before, or about conduct
   before, "the commencement", was in the 1 July 2025 group. On the Act alone, from 1 December 2024 until s 285A
   commenced, the new burden reached complaints about any conduct, however old. The 1991 Act's s 285AA closes the gap
   retrospectively ("taken to have applied from 1 December 2024") and moves the dividing day to the commencement of
   s 7B. Asserted (`ss 204, 205, 285A -- new burden of proof under the Act as passed` TRUE where `Who must prove what in
   my complaint` gives the former rules, on the same facts).
4. **ss 55 and 59A and parts 5, 6A, 7, 8, 9, 9A and 10 are not named in s 2** (F2). "Sections 56 to 59" stops before
   s 59A (Criminal Code s 340, serious assaults), which sits in part 4 with ss 56 to 59. These presumably commenced on
   assent; the deposited sources do not say. Asserted (`p cc other`, `p courts` are `unnamed`).
5. **A breach of the positive duty is not a complaint.** The s 131H note says so, and the definition of
   "contravention" as s 52(4) amends it adds harassment on the basis of sex but not the positive duty. The
   complainant's route is to the commissioner's own investigation (ch 7 pt 1A, s 173B(2), when the commissioner suspects non-compliance), which the person cannot
   compel. Asserted (every "yes" answer of `Does the positive duty protect me` says so).
6. **The 2-year period reaches back one year, no further.** s 283 keeps the former 1-year limit (and the good-cause
   route, s 138(2), s 141A, s 175(2)) for a contravention more than 1 year before the commencement; a contravention in
   the year before it gets 2 years. A complaint made before the commencement meets the 1-year limit even if it would be
   in time under the new one. Asserted (30 June / 1 July 2024 against a 1 July 2025 commencement; 1 April 2026 against
   1 March 2027).
7. **s 7 renumbering.** s 7(4) inserts "(r) a combination ...", and s 7(5) renumbers "(pa) to (r)" as "(q) to (x)",
   which carries the existing (q) "association with, or relation to" to (w) and the new (r) to (x). The count works (8
   paragraphs to 8 letters); it relies on (r) being placed after (q) before the renumbering.
8. **Drafting slips.** s 285(3) "under section former 198" (for "former section 198"); ss 42(1) and 43(1) "accepted under
   173J" (without "section"); s 173B(2) "not complying with duty" (without "the"). Neither changes an answer here. s 285(3) also speaks of directions under "former section
   150" by the commissioner, whose new counterpart is s 152A.
9. **Who may be an agent changes, but only for new complaints.** s 134(2) shuts out officers and employees of, and
   persons acting for, unregistered bodies purporting to represent industrial interests, in work-related complaints;
   s 284 keeps it off complaints made before the commencement. Asserted.
10. **Costs protect class members.** s 209(5)(a), in force since 1 December 2024, bars costs against a class member
    other than the complainant; outside representative complaints the tribunal's own Act governs, not encoded.
    Asserted.

## Before relying on this encoding

- Find and deposit the legislation that deferred the 1 July 2025 group, and its commencement instrument; then replace
  the two asked facts with the day (and split the group if that legislation split it, F3).
- Deposit the Acts Interpretation Act 1954 (F2) and check the assent day.
- Encode the Anti-Discrimination Act 1991 itself (areas, exemptions, ss 10, 11, 11A as amended), so that this layer's
  questions can sit on it; ss 7A, 7B and 21 belong there.
- An independent test pass, and a lawyer's review of F1, F6, F12 and F13.
- A respondent seat (the positive duty, s 205 exemptions), once the 1 July 2025 group commences.
