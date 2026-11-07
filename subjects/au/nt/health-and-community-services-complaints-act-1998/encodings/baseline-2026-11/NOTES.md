# Health and Community Services Complaints Act 1998 (NT) -- baseline encoding, the user and the complainant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module
(`hcscnt-dates.l4`, the only module that imports `daydate`), the rules and the 34 exported questions in
`hcscnt-complaints.l4`, and the worked cases in `hcscnt-cases.l4`.

The focus asked for is the Territory's **health complaints and health records law not named in the claims list**. The
Northern Territory has no separate health records Act: a person's right to see the records a provider holds reaches this
Act as a complaint ground (s 23(1)(e)), and access to records held by public bodies is under the Information Act 2002
(its own subject, `subjects/au/nt/information-act-2002`). So this encoding is of the complaints Act, from the seat of the
person who received the service and the person complaining for them. The Act gives no damages and no right to sue; what a
claimant meets here is the route beside a claim: who may complain and about what, the 2-year limit, the Commissioner's
deadlines, when the complaint stops (including once a civil claim is being heard, s 30(4)), conciliation and its binding
agreements, what may be used later in court, the investigation, the registration Board, and protection from pressure,
reprisal and suit. Parts 5 and 6 are encoded nearly whole; Part 7 and Part 10 as they reach the person; the rest is
machinery (see Scope).

## Edition

- **Act:** Health and Community Services Complaints Act 1998 (NT), Act No. 29 of 1998, assented 30 March 1998, commenced
  10 June 1998. The deposited text is reprint **REPH016**, "as in force at 13 August 2026", the current reprint on the NT
  Legislation register when retrieved on 6 November 2026; its last listed amendment is the Attorney-General Legislation
  Amendment (Boards, Committees and Statutory Offices) Act 2026 (No. 21 of 2026, commenced 13 August 2026, repealing
  Part 9), and before it the Integrity and Ethics Commissioner Act 2025 (No. 32 of 2025, Part 2 and ss 7 to 11 and 16
  repealed or replaced, commenced 1 June 2026):
  `../../registers/source-bundle/Health-and-Community-Services-Complaints-Act-1998-NT-current-reprint-REPH016.txt`.
- **Numbers set elsewhere:** penalties are in penalty units, whose dollar value the Penalty Units Act sets (not
  deposited; answers are given in penalty units). The Health and Community Services Complaints Regulations are not
  deposited: they can add or exclude services (s 4), prescribe managers (s 23(3)), set the principles of s 5 and the
  internal complaints procedures of s 100; those are asked as facts or left out. The fees and expenses of s 59 are set
  by the Minister by Gazette notice (not deposited, not computed).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. Two
deliberately wrong assertions (a determination on day 61 asserted on time; a complaint made 2 years and 1 day after
awareness asserted in time) were run once in a scratch copy, since deleted, and showed as "assertion failed" (157
satisfied, 2 failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `hcscnt-dates.l4` | 0 | 0 | 0 | 0 |
| `hcscnt-complaints.l4` (34 questions) | 0 | 0 | 0 | 0 |
| `hcscnt-cases.l4` | 0 | 0 | 157 | 157 |

Every expected value was worked by hand from the text before the run, and all held on the first run. Every exported
question has cases, with the edges: each head of the s 4 definitions, a service outside the Territory, the Regulations'
inclusion and exclusion (exclusion winning); each limb of "disability"; each head of s 22 with its condition met and
not; each class of s 23 ground and a matter outside it; the 2-year limit on the day 2 years on and the day after, with
and without good reasons, and from 29 February; the 60-day assessment on day 60 and day 61, the 14-day notice on day 14
and day 15, and steps not yet taken on the last day and the day after; each s 30 ground, s 30(3) with an issue not
raised, s 30(4) and (5), two grounds together; s 30(6) on the 14th day and the 15th, a requirement met before and after
the decision, no warning, no requirement, a period not yet expired; s 31 oral and written; s 40 at 47, 48 and 72 hours;
s 43 on the 13th and 14th day after the first agreement, unsigned, not in writing, outside conciliation; each use of
conciliation and investigation material; s 66 at 45 days, with 10 and with 20 extra days (capped at 15), an extension
not asked for in time, and the last day and the day after; each s 93 and s 94 head, the defences, and other detriment;
s 101 from the later of two days, from 31 August and from 29 February.

**No mirror cases.** One seat.

## Seat

**The user and the complainant** (`hcscnt-complaints.l4`): the individual the law is applied to, asking in their own
words. The person who received (or sought) a health service or a community service (aged care, disability services) --
"Is the service covered?", "Am I a user?", "Do I have a disability as the Act means it?" -- and the person complaining,
who may be the user or someone for them: "May I complain?", "Can I complain about this?", "Has my complaint been
received?", "By what day must I complain, and am I in time?", "By what day must it be assessed and must I be told?", "Is
the Commissioner late?", "Must the Commissioner stop?", "Can it be dropped because I did not send what was asked?", "If I
withdraw, when must it be confirmed?", "Can my identity be kept confidential?", "May I object to the conciliator?", "May
I be represented?", "May someone help me?", "When do I get the conciliator's report?", "Is our agreement binding?",
"Can what was said be used in court?", "If I must attend, may I bring someone, and am I paid?", "Do I get the
investigation report?", "By what day must the provider respond, and is it late?", "Will the practitioner's Board be
told?", "Was it an offence to pressure me, or a reprisal?", "Can I be sued for complaining?", "May my confidential
information be disclosed?", "Until when can an offender be prosecuted?".

No seat for the Commissioner (since 1 June 2026 the Integrity and Ethics Commissioner, s 9 notes), conciliators,
investigators, professional mentors, the relevant (National) Boards, the Minister, the Legislative Assembly or the
courts; their duties appear as what the person is owed and by when (ss 27(1) and 29 as a regulative rule on the
Commissioner). No seat for the provider: a provider seat over ss 28, 66, 99 and 100 would be a further layer (s 66(4) is
encoded as a regulative rule on the provider, run for the complainant who wants to know whether it is late).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Regulations, the Code and the Gazette
  notice of s 59 are not deposited; they are reached only through facts (s 4) or left out.
- **The actors the text names.** Followed: the user, the complainant and the persons in s 22, the provider, the manager,
  the applicable organisation, the Commissioner, conciliators, investigators, the relevant Board.
- **Judgments answered conditionally.** Followed: the Commissioner's satisfaction or opinion in ss 22(e), (j), 30(1),
  (2), (3), (5), 33(2), 40(2), 65(2)(c); "unreasonably" in s 23(1) (answered "yes, if the provider acted unreasonably");
  "sufficient details" in s 24(2); good faith (ss 95, 96, with the onus in s 96(2)); the defences of ss 93(2) and 94(4);
  "significant factor" in s 94(3).
- **The Act's definitions worked out; borrowed terms asked.** Worked out: health service, community service, service for
  aged people, service for people with a disability, disability, user (with s 4(2)), special needs group (s 4). Asked:
  "registered provider" (a National Board registration), "power of attorney", "applicable organisation" and "Carers
  Charter" (Carers Recognition Act 2006), "civil proceedings".
- **One case.** One complaint about one service (split complaints, s 32, are out).
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 4 (the definitions named above; s 4(2)); Part 5: ss 22, 23 (with (2)), 24(2) and (8) (with (3) and (4) in the
question's wording), 25 (through s 30(6)), 27(1), 29, 30 (all of it, (1)(a) to (c) through the s 22, s 23 and time-limit
questions), 31, 33(2) (with (1) in the wording); Part 6: ss 36, 40, 42(1) and (4), 43(1) to (3), 47(4) and (5); Part 7:
ss 54, 55(1), 59(1), 61, 65(2), 66(1), (2) (in the wording), (4), (5); Part 8: s 68(1), (3), (8); Part 10: ss 93, 94, 95(1)
and (2), 96, 97(1) (with (4)), 101.

**Regulative rules:** three. ss 27(1) and 29 as the Commissioner's chained obligation (`MUST` determine `WITHIN 60`, `HENCE`
`MUST` give written notice `WITHIN 14`, each `LEST BREACH ... BECAUSE`), run by EVALTRACE inside "Is the Commissioner late?";
s 66(4) as the provider's obligation, run inside "Is the provider late?"; and s 94(1) as a prohibition (`SHANT`) on the
person who acts against the complainant, run inside "Was it an unlawful reprisal?". All three questions take only plain
facts.

**Out, and why:**
- s 3 (objectives), s 5 (what the Commissioner has regard to: named in the s 23 answer), s 6, Part 3 (the Commissioner,
  staff, delegation, immunity, certificates, reports), Part 4 (references by the Minister and the Assembly): machinery.
- s 24(1), (5) to (7), s 25(1) to (3) except through s 30(6), s 25A (referrals in from the Information Commissioner and
  Ombudsman), s 26 (preliminary inquiries), s 27(2) to (5) (what the Commissioner may decide and where it may refer: the
  Commissioner's choices, with no period the person can count), s 28 (the provider's response: a provider seat), s 32
  (splitting), s 33(1) (in the wording only), s 34 (the Commissioner's handling of a referral).
- Part 6: ss 35, 37, 38, 39, 41, 44 to 46, 47(1) to (3) (the conciliator's and mentors' duties and offences, with no
  period the person meets).
- Part 7: ss 48 to 53, 55(2) to (4), 56 to 58, 60, 62 to 64 (privilege and Supreme Court applications), 65(1), (3),
  (4), 66(3), (6) to (9), 67: the Commissioner's powers and the witness's privileges; a witness seat would be a further
  layer.
- Part 8 except s 68(1), (3), (8): ss 68(2), (4) to (7), 69 to 77 are between the Commissioner and the Boards.
- Part 10: ss 85 to 92, 95(3), (4), 97(2) to (6), 98, 99, 100 (provider returns and internal procedures: a provider
  seat; the procedures are in the Regulations), 102, 104 to 106; Part 11 (transitional; s 107 reaches only services
  before 1998).
- No requirement ledger exists for the Northern Territory, and no ledger entry names this Act; none was raised.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

How they fall here (questions the text always answers return a plain BOOLEAN or a choice; the others a MAYBE):
- No (FALSE / JUST FALSE): s 4 ("means", "does not include"); s 4(2) ("is not a user merely because"); s 22 (closed in
  effect by s 30(1)(a)); s 23 outside the list (s 30(1)(b)); s 24(8) ("not ... until"); s 30(1)(c) (a period the text
  fixes); s 30(6), s 33(2), s 36 ("may ... if"); s 40 ("cannot ... unless", "not to give permission unless"); s 43(2)
  ("not binding unless"); s 47(4) and s 61(2) (flat negatives); s 65(2)(c) when the Commissioner does not consider it;
  s 68(1) ("if"); s 93 and s 94 when the conduct falls outside them, and their defences when proved; ss 95, 96 ("cannot be
  commenced", "is not liable"); s 97(1) ("must not ... unless"); s 101 (a period the text fixes).
- `NOTHING`: s 40(6) outside the "includes" list of special needs groups; s 43 for an agreement outside conciliation
  (s 43(3) leaves it to the general law); s 65(2)(a) (the report of a ministerial or Assembly reference goes to them, and
  the Act does not say whether the complainant gets it); ss 95, 96 without good faith (the Act gives no protection and
  says nothing more). s 94's "includes" list of reprisals is answered conditionally rather than NOTHING (fork F5).

### Forks

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 4 "health service", `s 4 -- is the service covered`: an administrative service directly related to a health
  service is read as needing to be provided in the Territory too; other reading: (b) brings in any such administrative
  service wherever it is provided.
- **F2** s 30(1), (3), (4), `s 30 -- must the Commissioner take no further action`: the first ground that applies is
  reported, in the Act's order; other reading: report every ground.
- **F3** "2 years" (s 30(1)(c)) and "12 months" (s 101), `years after` and `months after`: a day that does not exist in
  the later month is that month's last day (29 February 2024 + 2 years = 28 February 2026; 29 February 2028 + 12 months =
  28 February 2029); other reading: roll forward to 1 March.
- **F4** s 30(6)(a), `s 30(6) -- may the Commissioner drop my complaint for an unmet requirement`: "the period ... has
  expired" is tested on the day of the decision; other reading: it must have expired before the warning notice was given.
- **F5** s 94(2) "a reprisal includes", `s 94 -- was it an unlawful reprisal`: detriment other than the three listed
  heads is answered "an offence, if what they did counts as a reprisal"; other reading: NOTHING (the Act does not say).
- **F6** s 30(1)(c) "before the complaint was made", `s 30(1)(c) -- am I in time`: the day the complaint was made (oral
  or written), not the day it is taken to be received under s 24(8); other reading: a complaint is made only when the
  s 24(2) particulars are given.
- **F7** s 23(2), `s 23 -- can I complain about this`: a failure under s 23(2)(a) to (h) is itself acting unreasonably
  in providing the service ("includes the provider failing to"), so the answer is yes without a further judgment; other
  reading: whether the provider "failed" (for example, to exercise due care and skill) is itself the Commissioner's
  judgment, and the answer should be conditional like (1)(c).
- **F8** s 47(4)(a) "any court, tribunal or board", `ss 47, 61 -- can it be used`: "board" includes the relevant
  National Board, so what was said in conciliation is not admissible in its proceedings, while investigation material is
  (s 61(1)(b)); other reading: "board" means only bodies of a judicial kind.
- **F9** s 55(1), `ss 47, 61 -- can it be used`: material from an investigation may be used in the Commissioner's
  investigation (yes); other reading: none, s 47(4)(b) speaks only of conciliation.
- **F10** s 40(2)(d) "not less than 48 hours", `s 40 -- may I be represented at conciliation`: exactly 48 hours is enough;
  hours are the person's number; other reading: none.
- **F11** s 66(4), (5), `s 66(4) -- by what day must the provider respond`: the extension runs on from the 45th day and
  is capped at 15 days; an extension not asked for in writing before the 45 days ended counts as 0; other reading: the
  Commissioner may allow "any longer period" in (4) beyond the (5) cap.
- **F12** ss 27(1), 29, `ss 27(1), 29 -- is the Commissioner late`: "within 60 days after receiving it" and "within 14
  days of making a determination" both let the last day be the 60th or 14th day after; a step not yet taken is tested as
  if taken on the day asked about; other reading: "of" in s 29 counts the day of the determination as day 1.
- **F13** s 22, `s 22 -- may I make the complaint`: a person outside the heads gets a plain no (s 30(1)(a)); the CEO and
  the Minister ((f), (g)) are officials and are not offered; other reading: none.
- **F14** ss 95, 96, `ss 95, 96 -- can I be sued for complaining`: without good faith the answer is NOTHING (the Act
  gives no protection, the general law decides); other reading: JUST TRUE.

## What the Act turns out to say

1. **Section 14(1) is gone, but the definitions still point to it.** s 4 defines "staff member" as a person "provided to
   the Commissioner under section 14(1)" or "used by the Commissioner under section 14(2)(a)", and "contractor" by
   s 14(2)(b); s 110(2)(b) speaks of "section 14(1) or (2)(a)". The reprint's s 14 begins at (2), and (2) has no
   paragraphs (a) or (b): it is one sentence ("may engage consultants and make arrangements for the provision of advice
   and services"). The Integrity and Ethics Commissioner Act 2025 (s 104) amended s 14. A possible drafting gap; it
   reaches the person through s 97(4) (who must keep confidential information). Not encoded.
2. **s 111 applies an amendment to s 10, which the same Act repealed.** s 111 says the amendment by s 79 of the Integrity
   and Ethics Commissioner Act 2025 applies to an acting Commissioner; the endnotes show s 10 amended by s 79 and then
   repealed by s 102 of that Act. And s 102(3) still speaks of a "Deputy Commissioner", an office no section now creates.
   Not encoded.
3. **The 2-year limit runs from the user's awareness, whoever complains.** s 30(1)(c) counts from when "the user became
   aware", so a parent or representative complaining for the user is bound by the user's knowledge; and from when the
   complaint "was made", while s 24(8) says a complaint is not "received" until the name, address and details are in
   (fork F6). Asserted (the day 2 years on and the day after).
4. **A civil claim stops the complaint only once the court begins hearing it.** s 30(4) bars further action when the
   user "has commenced civil proceedings ... and the court has begun to hear the substantive matter"; until the hearing
   begins, a complaint and a claim can run together, and even after it an issue the claim will not decide may be
   considered (s 30(5)). Asserted.
5. **What is said in conciliation is shut out of every court, tribunal and board, but investigation material can go to
   the practitioner's Board.** s 47(4) against s 61(1)(b) (fork F8). A complainant who later sues for damages cannot use
   either (ss 47(4)(a), 61(2)). Asserted.
6. **A conciliation agreement binds only after a 14-day pause.** s 43(2)(c): it must be "entered into at least 14 days
   after the first agreement was reached", in writing and signed. The Act does not say how a binding agreement is
   enforced, and s 43(4)(b) forbids the conciliator to attest a signature without saying what happens if one does.
   Asserted (13 and 14 days).
7. **To be represented at conciliation the complainant must first tell the provider, in writing, 48 hours ahead.**
   s 40(2)(d), on top of the Commissioner's permission. Asserted (47 and 48 hours).
8. **The provider's 45 days can grow by at most 15, and only on a written request made in time.** s 66(4), (5): at most
   60 days; failing to answer is an offence of up to 40 penalty units. Asserted.
9. **The protections are offences, not rights to compensation.** ss 93 and 94 (up to 85 penalty units or 2 years) give
   the complainant no civil remedy in this Act; the prosecution must start within 12 months after the later of the
   offence and the Commissioner learning of it (s 101). A reprisal is defined only by three employment examples (fork F5).
   Asserted.
10. **"Refuse to entertain" and "take no further action".** s 30(6)(c) speaks of the Commissioner deciding "to refuse to
    entertain the complaint" where the rest of s 30 says "take no further action"; read as the same decision.
11. **Small slips.** s 66(8) "6 sittings days"; s 92(3) "misleading in the material particular"; s 5(1)(b), (c) still
    speak of the time "until the Code is approved" (whether and when it was approved is not in the Act). Not encoded.
12. **No separate health records Act.** The NT has none; a provider's refusal of access to a user's records is a
    complaint ground here (s 23(1)(e), "unreasonably"), and public-sector records are under the Information Act 2002.

## Before this is worth relying on

- The Health and Community Services Complaints Regulations (NT), deposited, for the services they add or exclude
  (s 4), the prescribed managers (s 23(3)), the principles (s 5) and the internal complaints procedures (s 100); and the
  Code of Health and Community Rights and Responsibilities, if approved (s 104).
- The Penalty Units Act for the value of a penalty unit, the Interpretation Act 1978 (NT) for counting periods (forks F3,
  F12), and the Minister's Gazette notice of fees and expenses (s 59).
- A check of findings 1 and 2 against the Integrity and Ethics Commissioner Act 2025.
- An independent test pass, and a lawyer's look at the forks, especially F5, F6, F7 and F8.
- The claims a person harmed by a health service actually brings (negligence, under the common law and the Personal
  Injuries (Liabilities and Damages) Act 2003) are in other Acts and are not here.
- Wider sources: no guidance from the Health and Community Services Complaints Commission and no court decision was read.
