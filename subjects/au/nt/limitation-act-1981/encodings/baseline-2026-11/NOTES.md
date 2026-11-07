# Limitation Act 1981 (NT) -- baseline encoding, the claimant

UNOFFICIAL. Not an official version of the Limitation Act 1981 (NT). Copyright in Northern Territory legislation is owned
by the Northern Territory. Quoted under the Northern Territory copyright policy of 8 October 1996 (see SOURCE-LICENSE.md).

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`nla-dates.l4`,
built-in date functions only, no daydate), the rules in `nla-rules.l4`, and the claimant's questions in `nla-seat.l4`,
which imports the rules and restates none. The cases are in `nla-cases.l4`. The shape follows the Limitation Act 2005
(WA) baseline beside it in `subjects/au/wa/`.

## Edition

- **Act:** Limitation Act 1981 (NT), reprint REPL026 as in force at 11 August 2025, as deposited at
  `../../registers/source-bundle/Limitation-Act-1981-NT-current-reprint-REPL026.txt` (text sha256 b12e58ac...0d3be),
  retrieved from legislation.nt.gov.au on 6 November 2026. It includes the Limitation Amendment (Child Abuse) Act 2017
  (from 15 June 2017), the Law Reform (Dust Diseases) Amendment Act 2007 and the Defamation Legislation Amendment Act 2025
  (from 11 August 2025).
- **Numbers set elsewhere:** none. The Act fixes all its own periods; no regulations under s 51 set any. The days taken
  from the endnotes are encoded: commencement 26 February 1982 (s 9(2)), 15 June 2017 (s 53), 1 November 1987 (s 48A),
  11 August 2025 (s 56(1)).
- **Borrowed terms asked as facts:** when a cause of action "first accrues" (the common law; the Act has no discoverability
  rule for personal injury); "sexual abuse", "serious physical abuse", "psychological abuse" (s 5A, undefined); "concerns
  notice" (Defamation Act 2006 s 11A); whether "any other enactment" prescribes a period (s 5); "infant" (finding 2).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (one
case written wrongly at first, an "adult" who was in fact 12 at accrual, showed as `DiagnosticSeverity_Error`, "assertion
failed", and was corrected by changing the facts, not the expected value). `l4` prints each diagnostic twice; satisfied
assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `nla-dates.l4` | 0 | 0 | 0 | 0 |
| `nla-rules.l4` | 0 | 0 | 0 | 0 |
| `nla-seat.l4` | 0 | 0 | 0 | 0 |
| `nla-cases.l4` | 0 | 0 | 124 | 124 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the last
day to commence and the day after (10 / 11 March 2023; 1 / 2 June 2031 for a child); a period from 29 February; the day
before and the day of commencement (25 / 26 February 1982); an injury the day before and the day of the 18th birthday; a
disability beginning on the last day and one beginning after it; the s 36(4) 30-year cap; a confirmation on the last day
and the day after; s 44(3)(b)(i) learnt exactly a year before expiry and the day after, sued on the anniversary of learning
and the day after; the s 44AA notice 56 and 57 days before, 7 days before (the Act's own example) and on the last day; a
publication before 11 August 2025; the s 39 notice's six months ending on 28 February and the day after; s 48A on
31 October and 1 November 1987.

## Seat

**The claimant** (`nla-seat.l4`): the individual to whom a cause of action accrues and who brings or proposes to bring the
action -- the injured person, a worker with a dust disease, a survivor of child abuse, a family member suing for a death
under the Compensation (Fatal Injuries) Act 1974, a person defamed, a party to a contract or deed. "By when must I start my
action?", "Can I still start it on this day?", "Is there no limit for my abuse or dust disease claim?", "Am I under a
disability?", "Did their acknowledgment or payment give me more time?", "Can the court give me more time?", "My parent was
served a notice: by when must they sue for me?", "Can I sue now on an abuse claim dismissed or settled before 15 June
2017?". Two questions (ss 8, 24) are asked by the same individual when answering a claim. No seat for the court, the
putative defendant, an insurer or the Public Trustee: the court's satisfaction, judgments and orders are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers; none is borrowed.
- **The actors the text names.** Followed: the plaintiff, the putative defendant, the parent or guardian, the tutor, the
  Public Trustee, the court, the Supreme Court.
- **Judgments answered conditionally.** Followed: "satisfied", "just", "just and reasonable", "reasonable diligence",
  "material", "prejudiced" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "person under a disability" (s 4), "child abuse"
  (s 5A(6)), "dust disease" (s 12(3)), "confirms" (s 41(2)) are worked out from facts; accrual and the kinds of abuse are
  asked.
- **One case.** One cause of action, of one person.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 4 (person under a disability, disabled person), 5, 5A, 8, 9(2), 11 (by the kinds asked), 12, 14, 17, 24, 36, 38,
39, 40(1)(e), 41, 42, 43, 44, 44AA, 44A, 44C, 48A, 53, 54, 55, 56(1). ss 37 (appointment of a tutor), 40 (form of
notices), 44AAB (single publication rule, as the day of publication), 44B, 44D, 49 and 50 (joint rights and liabilities)
are in the descriptions of the questions they bear on.

**Regulative rules:** two.
- The time bar ("is not maintainable after the expiration of a limitation period") as what the plaintiff must do to keep
  the action: `PARTY the plaintiff MUST commence the action WITHIN` the days from accrual to the last day,
  `LEST BREACH ... BECAUSE` the limitation period has expired. Run by EVALTRACE inside `Can I still commence my action on
  this day`.
- s 39(1), (2): `PARTY the parent or guardian MUST bring the action as guardian ad litem WITHIN` the days to six months
  after service, `LEST PARTY the putative defendant MAY apply for the Public Trustee to be appointed tutor`. Run by
  EVALTRACE inside `Did my parent or guardian comply with the notice`.

Neither exported question takes a DEONTIC or an EVENT; both take plain dates.

**Out, and why:**
- ss 1-3 and the Schedule, s 9(1), (3), s 10, s 51, s 52, s 56(2)-(4): machinery, repeal and transitional provisions
  (s 9(2) is answered as "section 9 decides" for causes of action that arose before 26 February 1982; the old law is not
  encoded).
- s 6 (the Crown): binds the Crown; its exclusions (Crown revenue actions, prosecutions, Crown land) do not touch a
  claimant's own action. s 7 (equity's own refusal of relief): a saving, no rule to encode.
- ss 13, 15, 16, 18-23, 25-35E (accounts, judgments, penalties, arbitration awards, conversion of goods, admiralty,
  equitable relief, arrears of income, mortgages, trusts, money paid under a mistake by way of tax) and Part IV Division 1
  (ss 45-48, arbitration): not in the claims focus; the main question answers "not answered by this encoding" for those
  kinds of action.
- s 36(3) (penalties) falls with s 16.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "a limitation period of N years from" (ss 12, 14, 17, 24, 36, 39) and "within 6 months after" (s 39) --
  `the anniversary`, `the date ... months after` -- the day of the event excluded, so the last day is the anniversary
  (or the same day six months on); from 29 February, or from the 31st into a shorter month, the last day of that month --
  1 March (or the 1st of the next month). The NT Interpretation Act rule is not deposited.
- **F2** "infant" (s 4) -- `Part III Division 1 -- the last day counted from` -- a person is an infant until the 18th
  birthday, which ends the disability -- the day before.
- **F3** s 36 with two disabilities (s 36(2)) -- same -- infancy and one other spell; days already suspended by infancy
  are not counted twice; the s 36(1)(e) three years run from the end of the later spell; a spell beginning after the
  period has expired has none, one beginning on the last day counts -- each spell treated alone, or "has commenced to run"
  read as excluding a disability present at accrual.
- **F4** s 36(1)(d), (e) -- same -- the suspension adds the plain days of the disability to the last day; (e) then gives at
  least 3 years from the end (or the death); a disability that has not ended suspends the period until the 30-year cap
  (s 36(4)) -- the suspension counted in whole years and months.
- **F5** s 41(1) "after ... commences to run but before the expiration" -- `the confirmation counts for` -- a confirmation
  on the first day of the reckoning or on the last day counts, and the whole period (with Part III) runs again from it,
  never shortening the time -- "after" excluding the first day; or only the Part II period restarting.
- **F6** s 44(3)(b)(i) "within 12 months before the expiration" and "within 12 months after the ascertainment" -- `s 44 --
  the court may extend` -- facts learnt after the same day a year before the last day; the action instituted no later than
  the anniversary of learning -- learnt on or after that day; or months counted differently.
- **F7** s 24(1)(b) where the principal action has no limitation period (child abuse, dust disease) -- `s 24 -- the last
  day for contribution` -- (b) never expires, so (a)'s 2 years alone -- (b) read as not applying and the contribution
  action therefore unlimited.
- **F8** s 56(1) "publication ... after the commencement of that section" -- `s 44AA -- the last day after a concerns
  notice` -- publication on or after 11 August 2025 (the commencement day) -- only from 12 August 2025.
- **F9** s 44AA(2) "56 days minus any days remaining after the notice day until the 1-year limitation period expires" --
  same -- read by the Act's own example: the days remaining are those strictly between the notice day and the last day, so
  a notice 1 to 56 days before the last day takes the period to 57 days after the notice day, and one given on the last
  day to 56 days after it -- the remaining days counted to and including the last day (always 56 days after the notice
  day), which contradicts the example by one day.
- **F10** s 44AA with Part III -- same -- applied to the period as Part III leaves it (the day it actually expires) -- to
  the bare 1-year period only.
- **F11** ss 42, 43 with s 36 -- `the reckoning start of`, `Part III Division 1 -- ...` -- the reckoning starts on the
  later of accrual and discovery, and a disability counts only from then; the 30-year cap still runs from accrual ("the date
  when the cause of action arose") -- the disability counted from accrual.
- **F12** s 39(1) where the action had already been brought before the notice was served -- `s 39 -- the outcome of the
  notice` -- complied with -- the notice requires a fresh action.
- **F13** ss 53-55 -- `ss 53-55 -- where Part V leaves my claim` -- s 54 read with its Division as reaching child abuse
  claims only; a settlement made because the claim was out of time treated as a judgment given on that ground (s 53(2)); a
  settlement made for other reasons answered "the Act does not clearly say" -- s 54(1) read literally for any cause of
  action (finding 7); or every settlement treated as a final determination barring a new action.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions (s 4 person under a disability, s 5A(6) child abuse, s 12(3) dust disease), "but only
if" (s 41(2)(a)), "is not maintainable after" (the time bar), "does not apply" (s 44(3)(aa) defamation, s 48A(2)), "may
not" (s 44A(3), s 54(7)) and the "if" of s 54(5) give `JUST FALSE` (or "this section gives no extension on these facts",
"the court may not extend it"). `NOTHING` is answered for s 5A where the action is not one for damages for personal
injury (*limited by its own wording*), for s 48A where the court is not satisfied or would not otherwise allow the
amendment (*silent*), before accrual, where another Act or the pre-1982 law decides, or for a kind of action outside the
encoding (*points outside the text*). The ss 53-55 question says "the Act does not clearly say" for a settlement made for
other reasons (*silent*, F13).

## What the Act turns out to say

1. **No discoverability rule for personal injury.** Unlike the WA, NSW and Victorian Acts, the NT Act runs the 3 years of
   s 12(1)(b) from the day the cause of action "first accrues" (the common law: for negligence, when damage is suffered)
   and gives no "date of discoverability". Late knowledge is met only by the court's power in s 44(3)(b)(i), which needs
   the action brought within 12 months of learning the material facts. The accrual day is asked as a fact.
2. **"Infant" is not defined** in the Act. Read as a person under 18 (the age of majority, fixed outside this Act and not
   deposited with it) (F2). Asserted at the 18th birthday and the day before.
3. **A prisoner is a "person under a disability".** s 4 includes "a convicted person who, after conviction, is undergoing
   a sentence of imprisonment", so time stops running against a serving prisoner (s 36) and runs at least 3 years after
   release, up to 30 years from accrual. Asserted.
4. **A dust disease death claim keeps its 3 years.** s 12(2)(a) removes the limit for "an action for damages for personal
   injury arising from a dust disease", but s 12(2)(c) takes Compensation (Fatal Injuries) Act claims out of s 12(1) and
   s 17 gives them 3 years from the death with no dust exception, where s 5A(4) expressly carries the child abuse exception
   to those claims. Encoded as written: a family's claim after a dust disease death has 3 years (subject to s 44).
   Asserted.
5. **s 11 and personal injury on a deed.** s 12(1)(a) excludes a contract claim "evidenced by a deed"; a personal injury
   claim that also lies on a deed has 12 years under s 14 and 3 years in tort under s 12(1)(b), and s 11 takes the
   earlier. The encoding asks the kind of action once; such a claim should be entered as personal injury. Not asserted.
6. **s 44AA's example fixes the count.** "56 days minus any days remaining after the notice day until the 1-year
   limitation period expires", with the example "given 7 days before ... 6 days left", counts only the days strictly
   between the notice day and the last day. On that reading a notice given 1 to 56 days before the last day takes the
   period to 57 days after the notice day, and a notice on the last day and one on the day before both end 56 days after
   the last day. Encoded by the example (F9). Asserted on the example's own facts and on the last day.
7. **s 54 is not limited in its words to child abuse.** s 54(1) lets "an action ... be brought after the commencement on a
   cause of action" despite an earlier limitation judgment, with no mention of child abuse; only the Division heading and
   s 53(2) tie it to the 2017 amendment. Read with its Division (F13). Not asserted for other claims.
8. **s 53(2) and s 54(3) on settlements.** s 53(2) makes "a judgment given" include a settlement of a child abuse damages
   claim, but s 54(3) bars a new action only where "a court had given judgment in final determination ... on grounds other
   than" the limitation period. Whether a settlement made for reasons other than the time bar stops a new action is not
   said. Answered "the Act does not clearly say". Asserted.
9. **s 5 and s 44(1).** s 5 says the Act "does not apply to any action for which a period of limitation is prescribed by
   any other enactment", but s 44(1) gives the court power to extend a time limit prescribed by "this or any other Act",
   and s 44(3)(b)'s conditions bind only "a limitation period prescribed by this Act". Encoded as: another Act's period
   applies (s 5), and for it the s 44 power is not subject to the s 44(3)(b) conditions. Asserted.
10. **s 36 has no ceiling but 30 years.** A disability that never ends (a lasting incapacity, a long sentence) suspends the
    period until 30 years from accrual (s 36(4)), unless the putative defendant serves a notice to proceed on a tutor or
    guardian (s 38), which ends the suspension on service. Asserted (an open spell, a notice on 1 July 2021).

## Before this is worth relying on

- Check the text against the authorised PDF of reprint REPL026 (retrieved 6 November 2026) and any later reprint.
- The Interpretation Act 1978 (NT) rule for reckoning periods (F1) and the Age of Majority Act (NT) for "infant" (F2).
- Encode the out-of-focus Part II kinds (judgments, penalties, mortgages, trusts, arbitration) if wanted.
- A lawyer's view on findings 4, 6, 7, 8 and 9 and forks F3-F5, F9-F11, F13; an independent test pass and a human gate.
