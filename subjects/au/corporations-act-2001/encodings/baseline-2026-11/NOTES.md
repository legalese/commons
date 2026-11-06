# Corporations Act 2001 (Cth) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This encoding is a new layer beside the two existing ones, `baseline-2026-10` (the founder-director of a proprietary
company) and `naive-2026-10` (the same seat, first pass). Neither was touched, and nothing here imports them. They encode
s 674(2) and s 674A from the director's side; this one encodes s 674A from the investor's side, with the compensation
order that follows.

Three files and a case file:

- `fsc-dates.l4` -- the date helpers (built-in date functions only, no daydate import, no `YMD`): plain days, 6 years,
  weekdays and business days;
- `fsc-claimant.l4` -- 32 exported questions of the claimant, in six `§§` groups, with the s 1056A(1) duty as one
  regulative rule and its trace helper;
- `fsc-cases.l4` -- the cases.

## Edition

- **Act:** Corporations Act 2001, Compilation No. 149, compilation date 19 September 2026, includes amendments to Act
  No. 87, 2026 (register id C2026C00432), as deposited at `../../registers/source-bundle/C2004A00818.txt` (the seven
  volumes joined).
- **Regulations:** the Corporations Regulations 2001 are **not deposited**. What they prescribe is asked as a fact:
  further eligible whistleblowers, eligible recipients, regulated entities and Commonwealth authorities (Part 9.4AAA); the
  s 917C(3)(ba) kinds of product; exclusions from cooling-off (s 1019A(2), s 1019B(5A)) and other ways of notifying (s
  1019B(2)(c)); professional standards schemes (s 1044B, not encoded).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `fsc-dates.l4` | 0 | 0 | 0 | 0 |
| `fsc-claimant.l4` | 0 | 0 | 0 | 0 |
| `fsc-cases.l4` | 0 | 0 | 199 | 199 |

Every expected value was worked by hand from the text, and every date from the calendar. The edges: 6 years from 29
February (to 28 February) and from 31 December; the fifth business day from a Monday, a Saturday and across Easter 2026
(two holidays counted); the 14 cooling-off days on the last day and the day after, with and without an earlier
confirmation; the 28 days of s 1056(2) for objecting and complaining on the last day and the day after, an objector in
time who complains late, neither notice and one notice; the s 1056A duty done on day 0, day 28 and day 29, still open on
day 28 and late on day 29; the s 1057 28th day and the day after, with and without a Court extension; the 90 days of s
1317AAD on the 90th and 91st day after; every s 917B, 917C and 917D outcome; each s 961B shortcut and its limits; each
exclusion in ss 961J(2), (3), 1041H(3), (4), 1053(4), 1317AADA, 1317AAE(2) to (4); the s 1041I(1B) reduction at 0%, 12.5%,
25% and 100%; the full and short lists of s 1317AE orders.

## Seat

**The individual who brings, or may bring, a claim under the Act's consumer and whistleblower provisions** (`fsc-claimant.l4`):

- the **retail client** given personal advice: "Did my adviser act in my best interests?", "Did they break s 961G, 961H or
  961J?", "Which licensee can be made to pay me, and by when must I sue?", "Is the licensee responsible for its
  representative?";
- the **retail client who bought a financial product** and wants out: "Can I return it, and by what day?";
- the **investor** misled or kept uninformed: "Can I recover for misleading conduct, how much after my share, by when?",
  "Can I get a compensation order against a listed company, or a director involved, that kept the market uninformed, and by
  when?";
- the **superannuation member, or person with an interest in a death benefit**, at AFCA: "Is mine a superannuation
  complaint?", "Am I bound by the determination?", "What must AFCA do?", "Can I complain about the death benefit decision,
  and by when must I object or complain?", "Was I told of someone else's complaint in time, and by when must I apply to be
  joined?", "Can I still appeal?";
- the **whistleblower**: "Am I an eligible whistleblower?", "Does my disclosure qualify?", "When can I go to a journalist?",
  "Am I protected, and is my disclosure kept out of evidence?", "Was revealing my identity unlawful?", "Can the court order a
  remedy, what orders, and can I be made to pay costs?".

These are five situations of one seat, not five seats: each is an individual claiming against a firm, a company, a trustee
or a person. The `§§` and `§§§` headings group them, and the death benefit and whistleblower groups say in their heading
that they arise only in that situation, so the form can ask first.

No second seat. The Act's duties here fall on licensees, listed entities, trustees, AFCA and the people who victimise a
whistleblower. A licensee or employer seat could be added beside this one (ss 917F(7), 961L, 1317AE(3), 1317AI).

No seat for AFCA, ASIC, APRA, the Federal Court or the death benefit decision-maker as such: their satisfaction, views and
decisions are asked as facts; the decision-maker's duty to the person (s 1056A(1)) is encoded as what the person must be
given and by when.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act fixes every period and figure used;
  the Regulations' prescriptions are asked as facts and said to be.
- **The actors the text names.** Followed: the client, the provider, the representative, the financial services licensee
  and the responsible licensee, the responsible person (cooling-off), the listed disclosing entity and the person involved,
  AFCA, the trustee, the death benefit decision-maker, the Federal Court, the discloser, the regulated entity, the eligible
  recipient, the journalist and member of parliament, the first person, the employer.
- **Judgments answered conditionally.** Followed: "misleading or deceptive", "reasonable to conclude that the advice is
  appropriate", "reasonably apparent", "give priority", "knows, or is reckless or negligent", "reasonable grounds to
  suspect", "reasonable grounds to believe", AFCA's being "satisfied", "fair and reasonable", the court's share of
  responsibility, "vexatiously or without reasonable cause" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: the s 917C responsibility rules, the responsible
  licensee (s 961P), basic banking product (s 961F, as a choice), the cooling-off start (s 1019B(3)) and business day (s 9),
  superannuation complaint (s 1053), eligible whistleblower (s 1317AAA), regulated entity (s 1317AAB, as a choice), the
  qualifying disclosure routes (ss 1317AA, 1317AAD, 1317AADA), detriment (s 1317ADA, in the description). Asked: "involved"
  (s 79), "generally available" (s 676), "associate", "relative", "dependant".
- **One case.** One piece of advice, one product, one course of conduct, one complaint, one disclosure.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).
- **Departure D1: two of the Act's own definitions asked.** "Personal advice" (s 766B(3)) and "retail client" (s 761G,
  with its regulations) are the Act's own, but long and dependent on regulations that are not deposited; they are asked,
  with a gloss. They could be worked out in a later layer.
- **Departure D2: chained answers as inputs (fork F12).** Five questions take the answer of an earlier one as an input
  whose description names it (was a Division 2 duty broken; am I an eligible whistleblower; does my disclosure qualify, and
  how; can the court order a remedy), instead of repeating its facts. The form should ask the earlier question first.

## Scope

The focus named Chapter 7 financial services, Part 7.7A best interests, Part 7.10A AFCA, s 674 continuous disclosure, s
1041H, s 1317HA and Part 9.4AAA whistleblowers. The Act is seven volumes; this encoding takes the Parts and sections the
focus names and the claims machinery around them.

**In:** Part 7.6 Division 6, ss 917A, 917B, 917C, 917D, 917E, 917F(1), (2) (the licensee's responsibility for its
representative). Part 7.7A Division 2, ss 961, 961B (with 961C, 961E in the descriptions), 961F, 961G, 961H, 961J, 961M,
961P (961K, 961L, 961Q read for finding 1). Part 7.9 Division 5, ss 1019A, 1019B. Part 7.10 ss 1041H, 1041I. s 674A(2),
(3), (4), with s 1317E(3) (the table, read for which provisions are financial services civil penalty provisions), ss
1317HA(1), (2), 1317K. Part 7.10A: s 1051(2)(d), (4)(e) (with s 1052), and Division 3, ss 1053, 1053A, 1053B, 1055, 1056,
1056A, 1057. Part 9.4AAA: ss 1317AA, 1317AAA, 1317AAB, 1317AAC, 1317AAD, 1317AADA, 1317AAE, 1317AB, 1317AD, 1317ADA,
1317AE, 1317AH.

**Regulative rule:** one. s 1056A(1): the death benefit decision-maker MUST give notice of the AFCA complaint WITHIN 28
days after AFCA notifies it, LEST breach; run by EVALTRACE inside `Was I told of the death benefit complaint in time`,
which takes only dates and yes/no facts.

**Out, and why:**
- Part 7.7A Division 3 (ongoing fee arrangements, ss 962 to 962S) and Divisions 4 and 5 (conflicted remuneration, ss 963
  to 963L): duties of the licensee, met by the client mostly as an AFCA or s 1317HA claim; s 962S (fees deducted without
  consent) and s 963E could be added.
- ss 953B, 953C (liability for a defective Financial Services Guide or Statement of Advice) and s 1022B (defective PDS):
  a claimant's route, with a 6-year limit; next to add.
- ss 1041E, 1041F, 1041G (false statements, inducing by false statements, dishonest conduct): also under s 1041I; could be
  added beside s 1041H.
- Division 2A (proportionate liability, ss 1041L to 1041S) and s 1044B (professional standards caps): they reduce what a
  s 1041H claimant recovers from each wrongdoer; the reduction question says so.
- s 674(2), ss 675, 675A, 676, 677: s 674(2) is encoded from the director's seat in `baseline-2026-10`; it gives the
  investor no compensation order (finding 6). s 675A (unlisted entities) is why a non-listed entity answers NOTHING.
- s 1317S and s 1317QB (relief from liability, state of mind): for the court.
- AFCA machinery: Part 7.10A Divisions 1, 2 and 4 (authorisation, mandatory requirements other than the two that reach the
  complainant, ASIC directions, information sharing), ss 1054 to 1054C, 1055A to 1055D, 1057A, 1057B, 1058. The AFCA Rules
  themselves (time limits, monetary limits for non-superannuation complaints) are the scheme's rules, not the Act's.
- Part 7.10B (the Compensation Scheme of Last Resort): could be added for a claimant with an unpaid AFCA determination.
- ss 1317AC (the offence and civil penalty of victimisation, ASIC's route; s 1317AD is the claimant's), 1317AF, 1317AG
  (identity before courts), 1317AI, 1317AJ (whistleblower policies).
- The definitions of retail client and personal advice (departure D1); banning orders; every penalty.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 6 years after" (ss 961M(6), 1041I(2), 1317K) -- `the last day of 6 years after` -- the period starts the
  day after and its last day is the same date six years on, or that month's last day where it is shorter (29 February 2024
  gives 28 February 2030) -- 1 March 2030 (rolling over).
- **F2** "within 28 days after being given notice" (s 1056(2)), "within 28 days after being so notified" (s 1056A(1)),
  "not later than the 28th day after the day" (s 1057(2)(a)) -- `the date` 28 `days after` -- the last day is the notice day
  plus 28 -- the notice day counted as the first.
- **F3** s 961B(2) "satisfies the duty ... if the provider proves" -- `Did my adviser meet the best interests duty` -- where
  the steps are not proved the answer is "not shown to be satisfied: for the court under s 961B(1)" -- failing to prove
  the steps is itself a breach (the subsection read as the only way to satisfy the duty).
- **F4** a duty whose "if" is unmet (s 961H(1) "If it is reasonably apparent"; s 961J(1) "If the provider knows, or
  reasonably ought to know") -- `Did my adviser breach s 961H`, `... s 961J` -- JUST FALSE -- NOTHING (the section does not
  speak to the case).
- **F5** s 961P(b) "under the rules in section 917C" -- `Which licensee can be ordered to compensate me under s 961M` --
  the s 917C sorting alone, without the s 917A(1) reliance conditions and without s 917D -- s 917C as it operates within
  Division 6, with s 917A(1) and s 917D (s 953B(3A) switches s 917D off expressly for its own purpose; s 961P is silent).
- **F6** s 1056(3) "has not been given either of the notices" -- `Can I complain to AFCA about the death benefit decision`
  -- read as "given neither"; where only one notice was given, neither (2) nor (3) bars the complaint -- "not given one or
  other of them", so (3) applies whenever a notice is missing.
- **F7** s 1317AAD(1)(b) "at least 90 days have passed since" and (e) "after the end of the period" -- `the first day after
  the 90 days have passed since` -- the 90 days start the day after the disclosure and have passed at the start of the 91st
  day after it, the earliest day for the written notice -- the 90th day after it.
- **F8** s 1019B(3) "the period of 14 days starting on ... the time when" -- `the last day of the cooling-off period` -- the
  whole of the 14th day after the start day is counted -- the period ends at the time of day it started.
- **F9** s 9 "business day" ("not a Saturday, a Sunday or a public holiday or bank holiday in the place concerned") --
  `the weekday` n `after` -- weekends are computed; the person counts the weekday holidays, which are added as further
  weekdays to count -- a holiday calendar for each place.
- **F10** s 1019B(2) "must be exercised by notifying ... (a) in writing; or (b) electronically; or (c) in any other way
  specified in the regulations" -- `Can I return the product under the cooling-off period` -- notice by another means is
  JUST FALSE -- NOTHING (the regulations, not deposited, may allow it).
- **F11** s 1041I(1) "who suffers loss or damage by conduct ... in contravention of section ... 1041H" -- `Can I recover
  my loss for misleading or deceptive conduct` -- conduct that is not misleading, or no loss, is JUST FALSE -- NOTHING.
- **F12** chained answers -- five questions (departure D2) -- an earlier answer taken as an input -- the earlier facts
  repeated.
- **F13** s 1053(1) "is a superannuation complaint if the complaint is" (a) to (j) -- `Is my complaint a superannuation
  complaint` -- JUST FALSE outside the list (an "if"); s 1053B keeps an ordinary AFCA complaint open -- NOTHING (the list
  not closed with "only").
- **F14** s 917C(3)(c) and s 917D(a) "within authority" -- `Is the licensee responsible to me for its representative` --
  one count of the licensees for which the conduct was within authority serves both -- a separate count of authorising
  licensees among those authorised for the class.

## The rulings on negatives (recorded word for word, as the encoding guide requires)

From `docs/ENCODING-GUIDE.md`, section 5, as it stood on 7 November 2026:

These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.
The rule of 2026-10-29 for what `JUST FALSE` and `NOTHING` mean is the convention the rows written since then follow (applied in legalese/commons#30 and #37); it was assumed, not ruled as a whole, and the rulings below settle parts of it.
In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

**How this encoding applies them.** JUST FALSE where the text says no in its own words: s 961G ("must only ... if"), the
s 961J(2), (3) exclusions ("does not apply"), s 1019A(1) ("applies if") and s 1019B(3), (5) ("can only", "cannot"), s
1041H(3), (4) ("does not contravene"), s 674A(2) and s 1317HA(1) ("if"), s 1053(1), (4), s 1056(1), (2), (3) ("cannot
... unless", "cannot ... if"), s 1057(2) (a period the text fixes), s 1317AAA ("is ... if"), ss 1317AA, 1317AAD ("qualifies
... if"), s 1317AAE(1), (2), (4), s 1317AD(1), (2), (2A) ("if"), s 1317AH(3) ("only if"). NOTHING, tagged, where the text
does not answer: outside s 961(1) (limited by its own wording); outside s 1041H(1)'s "in this jurisdiction ... in
relation to a financial product or a financial service" (limited by its own wording); an entity not under s 674A(1)
(limited by its own wording); a non-party or a question of fact under s 1057(1) (a grant limited in its own wording); an
entity outside s 1317AAB (open list); s 1317AB for a non-qualifying disclosure, and s 1317AB(1)(c) for the routes it does
not name (silent). The s 917A(1) case returns the constructor `Division 6 does not reach this conduct`, which is read as
NOTHING-kind (limited by its own wording).

## What the Act turns out to say

1. **A best interests breach is not a "financial services civil penalty provision".** The s 1317E(3) table lists ss
   961K(1), (2), 961L and 961Q(1) as "uncategorised", so s 1317HA gives no compensation order for them. The client's
   route is s 961M, and it runs only against licensees: the licensee that gave the advice, or the responsible licensee.
   The individual adviser is not a party s 961M names (other law may reach them). Asserted through the s 961M question.
2. **Consumer credit insurance is named in s 961B(3) and s 961J(2) but gets none of their relief.** Both apply where the
   advice "relates only to" basic banking, general insurance, consumer credit insurance or a combination, but both relieve
   only "in relation to the basic banking product and the general insurance product". An ADI's adviser on consumer credit
   insurance must still prove every s 961B(2) step and must still give priority under s 961J. Asserted.
3. **s 961P borrows "the rules in section 917C" without saying how much of Division 6 comes with them** (fork F5). s
   953B(3A) says expressly that s 917C applies despite s 917F and that s 917D does not; s 961P says neither.
4. **s 1056(2) bars a death benefit complaint only when the person both failed to object and failed to complain in
   time.** A person who objected within 28 days is not barred by the Act from complaining after the second 28 days
   (whatever the AFCA Rules may say). And a person given only one of the two notices is caught by neither (2) nor (3) on
   the reading taken (fork F6). Both asserted.
5. **The s 1056A(1) duty reaches only those the decision-maker "believes, after reasonable enquiry, may have an
   interest".** A person the decision-maker never identified has no claim to notice under the subsection; s 1056A(3)(b)
   lets AFCA join them anyway. Asked as a fact. Asserted.
6. **Since the fault-based provisions, an investor gets no compensation for a non-disclosure that was not known,
   reckless or negligent.** s 674(2) (the no-fault obligation) is not in the s 1317E(3) table at all; s 674A(2), (3) are
   "financial services" provisions, so s 1317HA reaches them. And s 1041H(4) takes the same non-disclosure out of s 1041H
   unless the s 674A fault is there. Both routes need knowledge, recklessness or negligence about the price effect.
   Asserted.
7. **Three 6-year clocks for one set of facts.** s 961M(6) runs "after the contravention", s 1041I(2) "after the day on
   which the cause of action arose" (usually when loss is first suffered), s 1317K "after the contravention". Advice
   given in 2020 that causes loss in 2023 can be out of time under s 961M while a s 1041I claim on the same advice is not.
8. **A public interest disclosure needs two steps after the 90 days, in order.** s 1317AAD(1)(e) requires the written
   notification "after the end of the period"; the disclosure itself must come after that notification. No gap between
   notice and disclosure is required. An emergency disclosure needs the notification but no waiting period. Asserted.
9. **A disclosure to a lawyer about Part 9.4AAA qualifies on that fact alone.** s 1317AA(3) does not require the
   discloser to be an eligible whistleblower, to have reasonable grounds, or to be outside the personal work-related
   grievance carve-out (s 1317AADA covers only (1) and (2); its Note says so). Asserted.
10. **The evidence protection of s 1317AB(1)(c) does not cover an internal disclosure.** It reaches disclosures under s
    1317AA(1) (to ASIC, APRA or a prescribed authority) and s 1317AAD only; a disclosure to an eligible recipient inside the
    entity gets the immunities of (a), (b) and (2) but not (c). Asserted.
11. **The s 1317AAE(4) investigation exception never covers the discloser's identity.** It is limited to information that
    "is not of the identity of the discloser". Asserted.
12. **Reinstatement is for termination; forced resignation counts only for compensation.** s 1317AE(1)(e) speaks of "the
    termination, or purported termination", while s 1317AE(2) adds "(including detrimental conduct that forces or forced the
    person to resign)" for the compensation orders only. Whether a forced resignation is a "purported termination" is left
    to the court; the encoding asks whether the conduct ended the employment.
13. **s 1019B(3) starts the cooling-off period at "the time when the confirmation requirement ... is complied with", a
    point in a day, or at "the end of the fifth business day", the end of one.** The two starts are not of the same kind;
    the encoding counts days (fork F8).

## Before relying on it

- An independent test pass, and a lawyer's look at forks F3, F5, F6 and F7.
- The Corporations Regulations 2001 deposited, so that the prescribed whistleblowers, recipients, entities, cooling-off
  exclusions and s 917C(3)(ba) products are worked out rather than asked.
- The retail client (s 761G) and personal advice (s 766B) definitions encoded (departure D1).
- ss 953B, 1022B and 1041E to 1041G added beside s 1041H, and Division 2A, so that a misled investor's whole claim can be
  answered.
- The AFCA Rules are not the Act; they set most of a non-superannuation complainant's limits and are not in Commons.
