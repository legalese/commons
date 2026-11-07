# Limitation Act 1981 (NT) -- baseline encoding of the child abuse provisions, the survivor

UNOFFICIAL. Not an official version of the Limitation Act 1981 (NT). Copyright in Northern Territory legislation is owned
by the Northern Territory. Quoted under the Northern Territory copyright policy of 8 October 1996 (see SOURCE-LICENSE.md).

## Method

**Baseline, second layer.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

**Focus: the Territory's equivalents** of the child abuse reforms made across Australia after the Royal Commission into
Institutional Responses to Child Sexual Abuse: the removal of limitation periods for child abuse claims, the setting
aside of earlier judgments and settlements, and organisational liability. In the Territory the first two are in this Act
(s 5A and Part V Division 2, ss 53-55, both inserted by the Limitation Amendment (Child Abuse) Act 2017); the third is
in the Personal Injuries (Liabilities and Damages) Act 2003 Part 3A (finding 1).

**Extend case.** `../baseline-2026-11/` (the whole-Act claimant baseline) already answers s 5A and ss 53-55 in two
questions each, coarsely. It stays untouched; this folder is a layer beside it. It cannot IMPORT that folder (the stable
`l4` resolves IMPORT only within a folder), so it writes its own rules for these sections, in more depth: the s 5A(6)
definition worked out from dates (the 18th birthday) and the kind of conduct, the s 5A(4) death and estate claims, s 5
against s 5A, s 5A(5), the s 53(1) definition of "limitation period", the commencement edge for ss 54 and 55, and
s 54(5)(b), (c). The two layers agree on every point they share; where this one is finer it says so (F3, F4, F6).

Modules: `nlca-dates.l4` (built-in date functions only, no daydate), `nlca-rules.l4` (the law; nothing exported),
`nlca-seat.l4` (the survivor's six questions, importing the rules and restating none), `nlca-cases.l4` (the cases).

## Edition

- **Act:** Limitation Act 1981 (NT), reprint REPL026 as in force at 11 August 2025, as deposited at
  `../../registers/source-bundle/Limitation-Act-1981-NT-current-reprint-REPL026.txt` (text sha256 b12e58ac...0d3be per
  its `.meta.json`), retrieved from legislation.nt.gov.au on 6 November 2026. s 5A and ss 53-55 are as inserted by the
  Limitation Amendment (Child Abuse) Act 2017 (Act No. 10, 2017), commenced 15 June 2017 (Gaz S31) per the endnotes; no
  later amendment touches them.
- **Numbers set elsewhere:** none. The one date used, 15 June 2017 (the s 53(1) "commencement"), is from the endnotes.
- **Borrowed terms asked as facts:** "sexual abuse", "serious physical abuse", "psychological abuse" (undefined); whether
  the injury "arises from" the abuse; whether "any other enactment" prescribes a period (s 5); "legal professional
  negligence" (defined in s 53(1) but asked as the kind of earlier judgment); the court's findings.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read and counted by distinct source range. One slip in the cases file at first (a date literal before a postfix
function, unbracketed: a type error, not a wrong expected value) was fixed by bracketing.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `nlca-dates.l4` | 0 | 0 | 0 | 0 |
| `nlca-rules.l4` | 0 | 0 | 0 | 0 |
| `nlca-seat.l4` | 0 | 0 | 0 | 0 |
| `nlca-cases.l4` | 0 | 0 | 79 | 79 |

Every expected value was worked by hand from the text, with the edges: abuse on the day before the 18th birthday and on
it (including a birth on 29 February); psychological abuse with and without sexual or serious physical abuse; abuse in
1975; each kind of action in s 5A(1), (4); s 5 with and without another Act's period; a judgment or settlement on
14 June 2017 and on 15 June 2017; an action brought on 14 and 15 June 2017; a period fixed by another Act (s 53(1));
every court in s 54(5)-(7), with a judgment of the same court, a different court and a settlement; each combination of
damages and costs in s 54(5)(b), (c).

## Seat

**The survivor** (`nlca-seat.l4`): the individual against whom child abuse was perpetrated, who brings or proposes to
bring an action for damages for the injury. Where that person has died, the family member suing under the Compensation
(Fatal Injuries) Act 1974 and the person acting for the estate sit in the same seat, because s 5A(4) carries the
section to their causes of action. "Was what was done to me child abuse?", "Is there any time limit on my action?", "Can
the court still stop my case because it is so old?", "My earlier case was dismissed as out of time, settled, or still
running before 15 June 2017: can I sue now?", "Can this court set the earlier judgment or settlement aside?", "What from
my earlier case may the court take into account?". No seat for the defendant, the institution, an insurer or the court:
the court's findings ("just and reasonable", a fair trial not possible) are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. No instrument sets a number here.
- **The actors the text names.** Followed: the person abused, the court, the Supreme Court; the family and the estate
  through s 5A(4).
- **Judgments answered conditionally.** Followed: "just and reasonable" (s 54(5)) and the fair-trial finding of the
  s 5A(5) note are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "child abuse" (s 5A(6)), "commencement" and
  "limitation period" (s 53(1)), "a judgment given" (s 53(2)) are worked out; the kinds of abuse are asked.
- **One case.** One cause of action, of one person, from one act of abuse.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 5 (as it bears on s 5A), s 5A(1)-(6), s 53(1), (2), s 54(1)-(7), s 55(1), (2). The s 4 definition of
"judgment" bears on finding 5.

**Regulative rules:** none. s 5A(2) is a permission without a deadline ("may be brought at any time"), and ss 53-55 give
the court powers, not the survivor duties; nothing in the focus is a duty with a deadline. The time bar the survivor
escapes is modelled as a regulative rule in `../baseline-2026-11/` (`Can I still commence my action on this day`).

**Out, and why:**
- The rest of the Act: in `../baseline-2026-11/`, untouched (the ordinary periods, Part III, s 44 extensions, and
  contribution under s 24, whose interaction with child abuse is that baseline's fork F7).
- Organisational liability (duty to prevent child abuse, the reversed onus, vicarious liability, the proper respondent,
  associated trusts, successors and unincorporated institutions): not in this Act. It is Personal Injuries (Liabilities
  and Damages) Act 2003 Part 3A (ss 17A-17R), encoded at
  `subjects/au/nt/personal-injuries-liabilities-and-damages-act-2003/encodings/baseline-2026-11/` (claimant seat, Part 3A
  in scope). It cannot be imported here; see finding 1.
- The court's inherent and other powers saved by s 5A(5): outside the Act; answered only as far as the note says.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 5A(6)(c) "psychological abuse that arises from abuse mentioned in paragraph (a) or (b)" -- `s 5A(6)(a)-(c) --
  the conduct is of a listed kind` -- arising from sexual or serious physical abuse of anyone (asked as one fact) -- only
  from such abuse perpetrated against the same person while under 18.
- **F2** "under 18 years of age" (s 5A(6)) -- `the person was under 18 on` -- under 18 to the end of the day before the
  18th birthday; born on 29 February, 18 on 28 February -- 18 at the end of the birthday; or on 1 March.
- **F3** "before the commencement" and "at the commencement" (ss 54, 55) -- `is before the 2017 commencement`, `ss 53-55
  -- where my earlier case leaves me` -- strictly before 15 June 2017; a judgment or settlement on 15 June 2017 falls
  outside the Division (s 5A then governs directly); an action brought on 15 June 2017 is governed by s 5A directly --
  "before the commencement" including the commencement day.
- **F4** s 53(2) settlements -- same, and `is a judgment as mentioned in s 54(1) or (2)` -- a settlement made because the
  claim was out of time is a judgment "given on the ground that a limitation period ... had expired" (s 54(1)); one made
  for other reasons: "the Act does not clearly say" (s 54(3) speaks of what "a court had given") -- every pre-2017
  settlement barring a new action under s 54(3); or none barring it. Same answers as `../baseline-2026-11/` F13.
- **F5** s 54 -- same -- read with its Division heading and s 53(2) as reaching child abuse actions only -- read
  literally for any cause of action (finding 4).
- **F6** s 54(7) "a judgment of any other court" -- `s 54(5)(a), (6), (7) -- the court may set aside the earlier
  judgment` -- a settlement agreement is no court's judgment, so a court other than the Supreme Court hearing the action
  may set it aside -- only the Supreme Court may set a settlement aside.
- **F7** s 5 and s 5A -- `s 5A -- the effect on my action` -- the checks in the order: not child abuse; outside
  s 5A(1); another Act's period; otherwise none -- s 5 first (the Act not applying at all), which changes only the label.
- **F8** s 54(3) -- `ss 53-55 -- where my earlier case leaves me` -- a pre-2017 final judgment on other grounds bars the
  new action whatever period applied (s 53(1) does not matter to it) -- only where the period was one fixed by this Act.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions (s 5A(6) child abuse, s 53(1) limitation period) give the no (`JUST FALSE`, or
"section 5A does not apply", "Part V Division 2 does not reach it: the period was not one fixed by this Act"); "cannot"
(s 54(3)) gives "I cannot sue again"; the "if" of s 54(5) and the "may not" of s 54(7) give `JUST FALSE`. `NOTHING` (or
a "not decided" label) is answered where s 5A(1) or s 54(5) is limited by its own wording and the case falls outside it
(an action not for personal injury from the abuse; a judgment not "as mentioned in subsection (1) or (2)"; one on or
after 15 June 2017; a court other than the Supreme Court not hearing the action), and for the court's powers saved by
s 5A(5) where the court has not found a fair trial impossible (*points outside the text*). "(other than the Supreme
Court)" in s 54(7) is decided at F6's site.

## What the Act turns out to say

1. **The Territory's equivalents are split over two Acts.** The removal of limitation periods (s 5A) and the reopening
   of earlier judgments and settlements (ss 53-55) are in this Act, from 15 June 2017. Organisational liability is in the
   Personal Injuries (Liabilities and Damages) Act 2003 Part 3A, which commenced later (30 September 2022, per that
   encoding's finding 8): a duty on institutions to prevent child abuse with a reversed onus (ss 17D-17F), vicarious
   liability (s 17G), a proper respondent and associated trusts for unincorporated bodies (ss 17H-17M, 17Q, 17R) and
   successors (s 17P). The survivor uses the two together: this Act says there is no time limit, Part 3A whom to sue.
   Not asserted here (the other encoding cannot be imported).
2. **s 5A does not lift another Act's period.** s 5A(2) operates "Despite any other provision of this Act" and removes
   "any limitation period under this Act". A period prescribed by another enactment is not "under this Act", and s 5
   takes such an action out of this Act altogether. So a child abuse claim that another Act subjects to its own time
   limit keeps that limit, however s 5 and s 5A are read together (F7). Asserted.
3. **The two Acts define "child abuse" differently.** Both list sexual abuse, serious physical abuse and psychological
   abuse arising from either. The Personal Injuries (Liabilities and Damages) Act s 3(2) adds that, for serious physical
   abuse, "conduct that was lawful at the time it occurred is not child abuse"; s 5A(6) has no such exclusion. Physical
   punishment that was lawful when given but is "serious physical abuse" therefore has no limitation period under s 5A,
   but is not child abuse for Part 3A's organisational liability. Not asserted (the other Act's definition is not
   encoded here); recorded for a lawyer.
4. **s 54 is not limited in its words to child abuse.** s 54(1)-(3) speak of "a cause of action" with no mention of child
   abuse; only the Division heading and s 53(2)'s extension to child abuse settlements tie them to the 2017 amendment.
   Read with its Division (F5), as `../baseline-2026-11/` reads it (its finding 7). Asserted for a non-abuse action.
5. **A "judgment" includes an interstate or foreign judgment.** s 4 defines "judgment" to include "a judgment of a court
   of the Commonwealth or a State or another Territory ... or any country". On its face s 54(1) lets a Territory action
   be brought despite such a judgment, and s 54(6) lets the Supreme Court set one aside; s 54(7) stops other Territory
   courts setting aside "a judgment of any other court". Whether the Supreme Court can in fact set aside another
   jurisdiction's judgment is a question beyond the text. Encoded as written ("a different court"); asserted for the
   Supreme Court and for another court.
6. **s 54(2) is obscure.** It reopens a cause of action despite "a judgment in respect of legal professional negligence
   ... given on the ground that a limitation period applying to the cause of action had expired". It seems to mean a
   judgment in the survivor's claim against their former lawyers that turned on the abuse claim having been out of time,
   but it says "the cause of action", the one now sued on. Asked as a kind of earlier judgment and treated like s 54(1).
   Asserted.
7. **Only the court hearing the action may weigh what was paid.** s 54(5)(b), (c) let the court hearing the new action
   take into account damages and costs "paid or payable" under or in the earlier case. s 54(6) extends to the Supreme
   Court, when not hearing the action, only "the power ... to set aside a judgment". Costs the survivor was ordered to pay
   in the earlier action count as well as anything the survivor received. Asserted.
8. **A settlement can be set aside like a judgment.** Through s 53(2), "any judgment as mentioned in subsection (1) or
   (2)" in s 54(5)(a) reaches a settlement agreement made because the claim was out of time. s 54(7) restrains only the
   setting aside of "a judgment of any other court", so any court hearing the new action may set such a settlement aside
   (F6). Asserted.

## Before this is worth relying on

- Check the text against the authorised PDF of reprint REPL026 (retrieved 6 November 2026) and any later reprint.
- The Interpretation Act 1978 (NT) and the Age of Majority Act (NT) for F2 and F3.
- A lawyer's view on findings 2, 3, 5 and 6 and forks F1, F3-F6; case law on stays for delay in child abuse actions
  (s 5A(5)), none read.
- An independent test pass and a human gate.
