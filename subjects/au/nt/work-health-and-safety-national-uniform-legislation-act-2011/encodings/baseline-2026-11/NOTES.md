# Work Health and Safety (National Uniform Legislation) Act 2011 (NT) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module
(`whsnt-dates.l4`, the only module that imports `daydate`), the rules and the 28 exported questions in `whsnt-claims.l4`,
and the worked cases in `whsnt-cases.l4`.

The focus asked for is **the provisions a person bringing or answering a claim meets**. A work health and safety Act is
not a compensation Act: it gives an individual one civil claim of its own (Part 6, s 112, in the Work Health Court) and
says so (s 267). The rest of what a claimant meets is the machinery around a death, injury or dangerous incident and the
worker's own rights: whether it was a notifiable incident (ss 35 to 37), the right to stop unsafe work (ss 84, 88, 103),
what an offender faces (ss 31 to 34B), asking for a prosecution, the DPP's part and the time to prosecute (ss 231 to 232,
34E), review of an inspector's or the regulator's decision (Part 12), compensation for an inspector's use of power
(s 184), void contract terms (s 272) and charging workers for safety (s 273). Part 6 and Part 12 are encoded whole, less
the exceptions under Scope. The shape follows the Commonwealth Act's claims baseline
(`subjects/au/work-health-and-safety-act-2011/encodings/baseline-2026-11/`) so the two can be read side by side; nothing is
imported from it (cross-folder IMPORT is not possible) and every rule was written again from the NT text, which differs
in many places (findings 4 to 9).

## Edition

- **Act:** Work Health and Safety (National Uniform Legislation) Act 2011 (NT), Act No. 39 of 2011, assented 14 December
  2011, commenced 1 January 2012. The deposited text is reprint **REPW025**, "as in force at 1 February 2020", the
  current reprint on the NT Legislation register when retrieved on 6 November 2026; its last listed amendment is the
  Work Health and Safety (National Uniform Legislation) Amendment Act 2019 (No. 37 of 2019, commenced 1 February 2020:
  industrial manslaughter, ss 34A to 34E; s 231 substituted; ss 231A, 231B inserted):
  `../../registers/source-bundle/Work-Health-and-Safety-National-Uniform-Legislation-Act-2011-NT-current-reprint-REPW025.txt`.
- **Numbers set elsewhere:** the NT Act states its penalties in dollars in each section (no schedule and no
  indexation), except industrial manslaughter by a body corporate, 65 000 penalty units, whose dollar value the Penalty
  Units Act sets (not deposited; the answer is given in penalty units). The Work Health and Safety (National Uniform
  Legislation) Regulations are not deposited: they can add or exclude kinds of serious injury or illness and dangerous
  incident (ss 36, 37), name the "prescribed purposes" of s 88, and make decisions reviewable (s 223 item 13). Those
  answers are NOTHING or asked as facts.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. Two
deliberately wrong assertions (a request on the day after the s 231(2) window asserted allowed; 30 November + 3 months
asserted to be 1 March) were run once in a scratch copy, since deleted, and showed as "assertion failed" (173 satisfied,
2 failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `whsnt-dates.l4` | 0 | 0 | 0 | 0 |
| `whsnt-claims.l4` (28 questions) | 0 | 0 | 0 | 0 |
| `whsnt-cases.l4` | 0 | 0 | 175 | 175 |

Every expected value was worked by hand from the text before the run. Every exported question has cases, with the
edges: each s 36 and s 37 head, a prescribed exclusion, and a case outside the heads (NOTHING); s 84 for a prisoner in
custody; each offence and each kind of offender for the maximum penalty, including industrial manslaughter by a worker
(none); each limb and defeater of ss 108 and 109; s 106(h) inside and outside its list; the last day and the day after
under s 113(1) and the s 231 window, from 29 February and from 31 August; the s 231(5) notice on the last day and the day
after, given and not given, and lifted by s 231(8); 30 November + 3 months; each period of s 232 winning in turn,
31 December + 6 months, fresh evidence for Category 1 and not Category 2, industrial manslaughter; each eligible-person
head of s 223 used, a person outside it, a delegate's decision, and a decision outside the table; the improvement
notice's compliance period under, at and over 14 days; s 226 with and without a request for information, answered and
not, and a request giving fewer than 7 days; each branch of ss 228 and 229B; each period of s 229(2).

**No mirror cases.** One seat.

## Seat

**The claimant** (`whsnt-claims.l4`): the individual the law is applied to, asking in their own words. The worker hurt or
put at risk at work, or their family: "Was it a notifiable incident?", "May I stop unsafe work?", "Is my continuity of
engagement kept?", "What is the most the offender can get?", "May I ask the regulator to prosecute, and between which
days?", "By what day must the regulator give me notice, and is it late?", "Must the DPP be involved?", "Until when can
they be prosecuted?". The worker, prospective worker or other person punished, pressured or misled for a safety reason
(Part 6): "Is it discriminatory conduct?", "Was it for a prohibited reason?", "Was I coerced or induced?", "Was I
misled?", "Can they be convicted?", "What orders can the criminal court make?", "Can I take them to the Work Health
Court, and am I in time?", "By what day must I start?", "What orders can the Work Health Court make?". The worker
affected by a notice or decision (Part 12): "Can I have it reviewed, and where?", "By what day must I ask for internal
review?", "When is it taken to be confirmed?", "Is it on hold?", "By what day must I go to the Work Health Court?". And:
"Can I get compensation for what an inspector did?", "Does the Act give me a right to sue?", "Is the contract term
void?", "Was I unlawfully charged for safety?".

No seat for the regulator (the Work Health Authority, s 4; NT WorkSafe in practice), an inspector, the Director of
Public Prosecutions or the Work Health Court; their duties appear as what the person is owed and by when (s 231(5) as a
regulative rule on the regulator). No seat for the person accused of discriminating or for the business: a business
seat over the Part 2 duties would be a further layer.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets its own penalties; the
  Regulations (not deposited) are reached only through NOTHING answers and facts (ss 36, 37, 88, 223 item 13).
- **The actors the text names.** Followed: the worker and prospective worker, the person in a commercial arrangement,
  the person conducting a business or undertaking, the eligible person and their representative, the regulator,
  inspectors, the internal reviewer, the Director of Public Prosecutions, the Work Health Court.
- **Judgments answered conditionally.** Followed: "reasonable concern" (s 84), "unreasonably failed" (s 88), "reasonably
  believes" (s 231), "reasonable in the circumstances" (s 113(3)), "would not be expected to rely on it" (s 109(2)), "a
  reasonable direction" (s 108(3)), "just" (s 184(3)), the court's satisfaction about fresh evidence (s 232(2)), a court
  stay (s 229B(2)), and the burdens the Act puts on the other side (ss 110(2), 113(2), (3)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: notifiable incident, serious injury or illness,
  dangerous incident (ss 35 to 37), discriminatory conduct (s 105), prohibited reason (s 106), eligible person (s 112(6)),
  reviewable decision and eligible person (s 223), prescribed time (s 224(3)). Asked: "worker" (s 7, its heads named in
  the input), "employee", "commercial arrangement", "WHS undertaking", "workers' compensation", "prisoner in custody".
- **One case.** One incident, one course of conduct against one person, one offence, one decision.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 35, 36, 37 (with s 38(1)'s "immediately" in the question); ss 84, 88, 103; the maximum penalties of ss 31, 32,
33, 34B (with its (1)(b) offender element), 104, 107, 108, 109; Part 6 whole: ss 104 (with (2)), 105, 106, 107 (as
s 112(2)(b) and its penalty), 108, 109, 110, 111, 112, 113, 114, 115; Part 13 Division 1: ss 231(1), (2), (3), (5), (6) (in
the question's wording), (8), (10) (in the input), 231A(1), (4), 231B, 232, with s 34E; s 184; Part 12: ss 223 (items 1 to
12, with 4A and 4B), 224, 226, 228(1) to (5), 229(1) to (3), 229B(1), (2); s 267; s 272; s 273 (with its penalty).

**Regulative rules:** two. s 231(5) as the regulator's obligation (`MUST ... WITHIN ... LEST BREACH ... BECAUSE`), counted in
days to the day 3 months after it received the request, run by EVALTRACE inside "Is the regulator late?"; and s 273 as a
prohibition (`SHANT`) on the business, run by EVALTRACE inside "Was I unlawfully charged for safety?". Both questions take
only plain facts.

**Out, and why:**
- Part 1 (definitions used where needed; s 12B strict liability, s 12A Criminal Code: reflected in inputs), Part 2
  Divisions 1 to 4 (the duties themselves: they bind the business, officers and workers; a claimant meets them only as
  "a duty was broken", which the offence questions take as given), the elements of ss 31 to 33 and s 34B(1)(a), (c) to
  (e) (for the court), s 34 (volunteers and unincorporated associations), ss 34A, 34C, 34D (alternative offence
  machinery; 34E is in).
- s 38(2) to (7), s 39: the business's notification and site duties ("immediately", "until an inspector arrives"), with
  no period the claimant can count; Part 4 (authorisations).
- Part 5 except ss 84, 88, 103: consultation, representatives, committees, issue resolution, s 85 (the representative's
  direction; s 88 covers its worker), ss 86, 87 (named in the s 84 question), s 89, provisional improvement notices.
- Part 7 (entry permits; items 4A and 4B of s 223 are in), Part 8 (the regulator), Part 9 except s 184 (ss 182, 183: the
  inspector's duties, with no period), Part 10 (notices, except as reviewable decisions), Part 11 (WHS undertakings,
  except as s 232(1)(c) facts).
- Part 12: s 225 (who reviews), s 227 (written reasons, "as soon as practicable"), s 228(6) (how long a stay lasts),
  s 229A (frivolous applications), ss 229C, 229D (the court's powers): the tribunal's and the reviewer's, not the
  person's questions.
- Part 13: s 230 (who may prosecute), s 231(4), (7), (9), s 231A(2), (3) (the DPP's 25 business days run to the regulator,
  not to the person), s 233, Divisions 2 to 7 (sentencing orders, infringement notices, bodies corporate, the Crown, public
  authorities, civil penalty proceedings, which only the regulator or an inspector may bring, s 260; s 267 says so in
  "Does the Act give me a right to sue?").
- Part 14: ss 268 to 271, codes of practice, regulation-making; Part 15 (transitional); Schedules 1 to 3.
- No requirement ledger exists for the Northern Territory, and no ledger entry names this Act; none was raised.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

How they fall here:
- `JUST FALSE`: s 35 for a listed head excluded by the Regulations ("does not include"), and with no death, injury or
  exposure at all ("means"); s 84 ("if"), s 103 ("nothing in this Part applies"); s 88 ("if"); s 105 and s 106 ("if");
  s 104(2) ("only if"); s 108 and s 109 (flat negatives with closed lists; s 109(2) "does not apply if"); s 231 ("if",
  "No request may be made more than 12 months after"); s 223 (the table closes who is eligible); s 267 ("nothing in this
  Act is to be construed as conferring").
- `NOTHING`: ss 35 to 37 for an injury or incident outside the listed heads (the Regulations may add it); s 88 when the
  worker did not cease work under the Division; s 223 for a decision outside the table; s 228 for the regulator's own
  decisions on internal review; s 267 for the Regulations' duties; s 272 for a term that neither excludes, limits,
  modifies nor transfers.

### Forks

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 105(2), `s 105 -- is it discriminatory conduct`: organising or threatening is folded into each head; other
  reading: none, the answer is the same.
- **F2** s 106(h), `s 106 -- was it for a prohibited reason`: raising a concern only with someone outside (h)(i) to
  (viii), such as the media, is JUST FALSE for (h); other reading: it may fall under (j) ("taking action ... to seek
  compliance"), which the person would choose instead.
- **F3** s 115 "a law of the Commonwealth or a State", `ss 112, 113(1), 115 -- can I start` and `s 112(3) -- what orders
  can the court make`: the person says whether the other claim was under such a law, the `@desc` adding "or, if it
  counts as one, a Territory"; other reading: a Territory law (the NT Anti-Discrimination Act 1992, the Return to Work
  Act 1986) never counts, so s 115 never bars a claimant who complained under NT law. Turns on the Interpretation Act
  1978 (NT), not deposited.
- **F4** "1 year after", "6 months", "3 months", "12 months" (ss 113(1), 231, 232), `months after` and `years after`: a
  day that does not exist in the later month is that month's last day (29 February 2024 + 1 year = 28 February 2025;
  31 August + 6 months = 28 February; 30 November + 3 months = 28 February; 31 December + 6 months = 30 June); other
  reading: roll forward to the 1st of the next month.
- **F5** ss 112, 113(1), 115, `ss 112, 113(1), 115 -- can I start`: the first failing condition is reported, in the order
  reach, eligibility, time, other claims; other reading: report every bar.
- **F6** s 112(3), (4), s 113(3), s 114(3), `s 112(3) -- what orders can the court make`: once the other side proves the
  reason was not substantial, or proves the defence, or a s 111 order was made, no s 112 order is listed, not even "any
  other order" under (3)(d); other reading: (3)(d) and s 112(5) leave the court other orders.
- **F7** s 231(1)(b), `s 231 -- the window`: "no prosecution ... has been brought within 6 months of the occurrence" can
  be known only once the 6 months have passed, so the first day to ask is the day after the day 6 months on; other
  reading: the day 6 months on itself.
- **F8** s 231(3), `s 231 -- may I ask for a prosecution`: a request that is not in writing with the particulars and
  grounds is not a request the section allows (JUST FALSE); other reading: a defective request is still a request, and
  only its form is wrong.
- **F9** s 231(8), `s 231(5) -- is the regulator late`: "need not give the notice" lifts the duty when information about
  the occurrence is on the regulator's website, whenever it was published; other reading: only information published
  before the 3 months end lifts it.
- **F10** s 224(1) "a decision made by the regulator or a delegate of the regulator", `ss 223, 224, 229 -- can I have the
  decision reviewed`: an inspector's decision is not the regulator's or a delegate's (inspectors decide under their own
  powers, Part 10), and a delegate's decision is asked as a fact; other reading: an inspector acting under a delegation
  is a delegate, and every decision goes straight to the Work Health Court.
- **F11** s 224(3)(a), `s 224 -- by what day must I ask for internal review`: the improvement notice states a day
  (s 192), not a period; the compliance period is the days from issue to that day, compared with 14, counted from the
  day the notice came to the person's notice; other reading: the earlier of the compliance day and 14 days after notice.
- **F12** s 226(4), `s 226 -- when is the decision taken to be confirmed`: a request giving fewer than 7 days is read as
  giving 7; other reading: the request is defective and the 14 days never stopped.
- **F13** s 229(2)(c), `s 229(2) -- by what day must I apply to the Work Health Court`: when the court requires reasons,
  (c)'s 14 days after the statement replace (a) or (b); other reading: whichever ends later. The court may extend the
  time in any case (s 229(3)); that is not computed.
- **F14** s 267(c), `s 267 -- does the Act give me a right to sue`: for duties under the Regulations the Act takes no
  position (NOTHING); for every other contravention outside Parts 6 and 7 and Division 7, JUST FALSE; Division 7 proceedings
  may be brought only by the regulator or an inspector (s 260), so Part 7 contraventions also answer JUST FALSE for the
  individual; other reading: NOTHING for Part 7 (s 267 does not itself say no for the excepted Parts).
- **F15** s 273, `s 273 -- was I unlawfully charged for safety`: the prohibition has no period; `WITHIN 1` stands for
  the one period the question asks about, so a trace with no charge ends FULFILLED.
- **F16** ss 35 to 37, `ss 35 to 37 -- was it a notifiable incident`: "requiring the person to have immediate treatment"
  is the person's fact; outside the listed heads the answer is NOTHING because the Regulations may add kinds; other
  reading: JUST FALSE, the "means" definition closing the list until a regulation is shown.
- **F17** s 88, `s 88 -- is my continuity of engagement kept`: where the worker did not cease work under the Division the
  section does not speak (NOTHING); other reading: JUST FALSE (the "if" fails).
- **F18** s 228, `ss 228, 229B -- is the decision on hold during review`: on internal review of the regulator's own
  decisions (which have none, s 224(1)) the answer is NOTHING; other reading: JUST FALSE.
- **F19** s 34B(1)(b), `the most an offender can get`: an individual who is not a business or undertaking or its officer
  cannot commit industrial manslaughter, and the answer says so rather than "imprisonment for life"; other reading: none.

## What the Act turns out to say

1. **The Act gives no right to sue for an injury.** s 267 says nothing in the Act confers a civil right of action for a
   contravention, except in Part 6, Part 7 and Division 7 of Part 13; Division 7 proceedings may be brought only by the
   regulator or an inspector (s 260). An injured worker's claim lies in negligence or workers' compensation (the Return to
   Work Act 1986), outside this Act. Asserted.
2. **Misrepresentation gives no civil claim, and coercion a thin one.** s 112(2) reaches discriminatory conduct (a),
   procuring it (b) and s 108 coercion (c), not s 109; for s 108 the Work Health Court may grant an injunction or "any other
   order", but not compensation or reinstatement, and neither the presumption (s 113(2)) nor the defence (s 113(3))
   applies. Asserted.
3. **Two thresholds for the same reason.** The civil claim needs the safety reason to be "a substantial reason"
   (s 112(4)); the offence needs it to be "the dominant reason" (s 104(2)). Both are presumed, and the other side must
   disprove them on the balance of probabilities (ss 110(2), 113(2)). Asserted.
4. **s 115 names only "a law of the Commonwealth or a State".** A Territory claimant's most likely other claims (under the
   NT Anti-Discrimination Act 1992, or for workers' compensation under the Return to Work Act 1986) are under Territory
   law. Whether "State" includes the Territory turns on the Interpretation Act 1978 (NT), not deposited (fork F3). The
   Note to Part 6 Division 1 says the Division does not limit the Anti-Discrimination Act 1992.
5. **The NT s 231 is not the Commonwealth's.** A request may be about a Category 1, 2 or 3 offence or industrial
   manslaughter (the Commonwealth excludes Category 3); it opens only after 6 months without a prosecution and closes 12
   months after the occurrence (the Commonwealth allows 6 to 18 months, and a coronial route); the regulator owes a
   written notice of the status within 3 months (s 231(5), (6)), not a referral to the DPP on request. Asserted (Category
   3, the window's edges, the notice).
6. **A prosecution brought after the 6 months does not, on the words, bar a request.** s 231(1)(b) asks whether a
   prosecution was "brought within 6 months of the occurrence"; one brought in month 7 leaves (1)(b) satisfied. The
   encoding follows the words (the input asks about the 6 months only). Not asserted beyond the input's wording.
7. **Industrial manslaughter has no time limit, but its fallback does.** s 34E(1) lifts s 232 for industrial
   manslaughter; s 34E(2) keeps it for the alternative verdict under s 31 or 32. A family that wants the alternative
   available needs the proceeding brought within the s 232 period. Asserted.
8. **Industrial manslaughter is only for the business or its officer, and a body corporate's fine is in penalty units.**
   s 34B(1)(b); 65 000 penalty units (dollar value outside the Act). All other penalties are fixed dollar amounts in the
   section, not indexed. Asserted.
9. **Review goes to the Work Health Court, and a court review does not stay the decision.** s 229(1) names the Work
   Health Court; s 229B(1) says an application "does not affect the operation or implementation of the decision" unless
   the court orders otherwise. Yet s 179(6)(d) requires a forfeiture notice to say the person "may apply for a stay of the
   decision if the person applies for a review", and forfeiture is the regulator's decision, with no internal review and
   so no s 228 stay; and s 179(6)(b) counts "28 days after the date of the notice" where s 229(2)(a) counts from when the
   decision "first came to the applicant's notice". Not asserted (a drafting finding); the encoding follows ss 229 and
   229B.
10. **The internal review can be confirmed earlier than 14 days.** If the reviewer asks for information and the person
    does not answer in time, the decision is confirmed "at the end of that time" (s 226(5)). Asserted (22 March against
    24 March).
11. **s 228(6)(a) speaks of "the prescribed period for applying for an external review"**, but s 229(2) fixes the
    periods in the Act; read as those periods. Not encoded (s 228(6) is out).
12. **The reprint is dated 1 February 2020.** The register showed REPW025 as current and in force on 6 November 2026. If an
    amendment after February 2020 is not yet in a reprint, this encoding would miss it. The court's name, the "Work
    Health Court", is the Act's; its constitution after the Local Court (Related Amendments) Act 2016 is outside the Act.

## Before this is worth relying on

- The Work Health and Safety (National Uniform Legislation) Regulations (NT), deposited, for the prescribed kinds of
  serious injury and dangerous incident (ss 36, 37), the prescribed purposes of s 88, item 13 of s 223, and the
  emergency services workers of s 108(4)(c).
- The Interpretation Act 1978 (NT) for "State" in s 115 (fork F3) and for counting periods, and the Penalty Units Act for
  the value of a penalty unit.
- A check that no amendment after REPW025 is in force (finding 12).
- An independent test pass, and a lawyer's look at the forks, especially F3, F4, F7, F10 and F14.
- The claims an injured worker actually brings (workers' compensation under the Return to Work Act 1986, negligence
  under the common law and the Personal Injuries (Liabilities and Damages) Act 2003) are in other Acts and are not here.
- Wider sources: no NT WorkSafe guidance or court decision was read.
