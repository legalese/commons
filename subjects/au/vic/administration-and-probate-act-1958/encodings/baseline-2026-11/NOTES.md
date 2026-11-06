# Administration and Probate Act 1958 (Vic) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The law is in three rule modules
(`ap-survival.l4`: s 29, s 30, the s 3 dust-related condition and the First Schedule, s 99AC; `ap-intestacy.l4`: Part IA with
s 70M and s 106; `ap-family-provision.l4`: Part IV with s 3 domestic partner and s 101), a date module (`ap-dates.l4`, built-in
date functions only) and a module of the four steps with a deadline (`ap-duties.l4`). The questions are asked in one seat
module (`ap-seat.l4`), which imports them and restates no rule.

## Edition

- **Act:** Administration and Probate Act 1958, Act No. 6191/1958, Version No. 130, incorporating amendments as at
  22 October 2025, deposited at `../../registers/source-bundle/administration-and-probate-act-1958.txt` (sha256
  00cdfc0a...1f5bf6 as committed), a plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see
  that file's `.meta.json` and `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **Formulas sidecar:** the three embedded equations (`.formulas.md`) are each B / C, multiplied by A in the text (s 31B,
  s 70M, s 71). Only s 70M's is encoded; it was transcribed from the Word file, not yet checked against the authorised PDF.
- **Dates from the endnotes:** s 4 of the Administration and Probate (Dust Diseases) Act 2000 commenced 10 May 2000 (s 99AC);
  Part 2 of the Justice Legislation Amendment (Succession and Surrogacy) Act 2014 on 1 January 2015 (s 101); the 2017
  Succession and Related Matters amendments (Part IA as it now stands) on 1 November 2017 (s 106). The endnotes are not part
  of the Act; they are the deposited record of commencement.
- **Numbers set elsewhere:** the partner's statutory legacy for a year after the first is published by the Minister in the
  Government Gazette (s 70N), not deposited: an input, with $451,909 (s 70M(1)) and the s 70M(2)-(4) formula encoded so a
  person can work it from the CPI. The Reserve Bank cash rate (for the legacy interest rate) and the limitation period's last
  day (for s 29(3)) are inputs.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read: each
satisfied assertion is reported as "assertion satisfied", and the counts below are those reports against the `#ASSERT` lines.
The machine was heavily loaded; a case file took about 16 minutes.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ap-dates.l4` | 0 | 0 | 0 | 0 |
| `ap-duties.l4` | 0 | 0 | 0 | 0 |
| `ap-survival.l4` | 0 | 0 | 0 | 0 |
| `ap-intestacy.l4` | 0 | 0 | 0 | 0 |
| `ap-family-provision.l4` | 0 | 0 | 0 | 0 |
| `ap-seat.l4` | 0 | 0 | 0 | 0 |
| `ap-cases-survival.l4` | 0 | 0 | 62 | 62 |
| `ap-cases-intestacy.l4` | 0 | 0 | 94 | 94 |
| `ap-cases-family-provision.l4` | 0 | 0 | 65 | 65 |

Every expected value was worked by hand from the text, with the edges: the 30th and 29th day after a death (and across
29 February 2028); the month-end and leap-year cases of "within 3 months" and "within 6 months"; the last day and the day
after for s 29(3), s 30, s 70Q, s 70R and s 99; an estate worth exactly the statutory legacy and $1 more; an estate just over
the legacy once the chattels are taken out; a full-time student aged 18, 25 and 26; 1.9 and 2 years living together; a
child's death exactly a year after the deceased's and a day later; s 99AC on each side of 10 May 2000; the s 70M rounding at
$1 and $10 and a fall in the index; s 99A's notice of intention on its last day and the day after.

## Seat

**The claimant** (`ap-seat.l4`): the individual who claims on or through a deceased person's estate, or whose claim meets a
death. That is the family member or other person seeking family provision (Part IV: "Am I an eligible person?", "Can the
Court make an order for me?", "By when must I apply?", "Can I still challenge a distribution?"); the partner or relative
taking on an intestacy (Part IA: "Do the intestacy rules apply?", "Did I survive long enough?", "Who takes?", "What do I
take?", "Can I buy the house from the estate, and by when?"); the injured person whose wrongdoer has died, or the family or
executor of an injured person who died (s 29: "Does the claim survive?", "Can the estate recover for pain and suffering from
mesothelioma?", "Can I still sue the estate, and by when?"); and the person served with the executor's s 30 notice.

No seat for the personal representative, the Court, the Minister or the Crown: their acts and judgments are asked as facts,
and their duties are encoded for what they mean to the claimant (the s 70Q notice the partner must be given, the
distributions s 99A protects).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: no instrument is deposited; the Gazette amount of
  the statutory legacy, the RBA cash rate and the limitation date are inputs; the s 70M formula is encoded.
- **The actors the text names.** Followed: the deceased, the intestate, the partner, issue, relatives, the eligible person,
  the personal representative, the Court, the Crown.
- **Judgments answered conditionally.** Followed: moral duty, adequate provision, dependency, "just and reasonable", "properly
  made", the Court's extensions and orders are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: dust-related condition (s 3, First Schedule),
  domestic partner and unregistered domestic partner (s 3), disability and eligible person (s 90), the legacy interest rate
  (s 3), the partner's statutory legacy (s 70M). Asked: registered domestic or caring relationship (Relationships Act 2008),
  tort, personal injuries, "would have been able to take proceedings under the Family Law Act 1975", personal chattels'
  value, residuary estate's value.
- **One case.** One estate, seen by one claimant.
- **The Act's terms with plain glosses.** Followed, in every `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3(1) (aunt or uncle, cousin, domestic partner, dust-related condition, intestate, legacy interest rate, partner,
registered caring and domestic partner, spouse, unregistered domestic partner), s 29(1), (2)(a), (c), (2A), (3), (4) (in the
facts asked), (5); s 30(1)-(3) (as the step and its consequence); Part IA: ss 70A, 70B (definitions used), 70C, 70J, 70K,
70L, 70M, 70O, 70P (who may elect), 70Q, 70R, 70W(2), 70Z, 70ZA, 70ZB, 70ZC-70ZE (as "agreement or order", or equal shares),
70ZF-70ZL; Part IV: ss 90, 90A, 91(1)-(5), 99, 99A; transitionals ss 99AC, 101, 106; the First Schedule.

**Regulative rules:** four, in `ap-duties.l4`, each run by EVALTRACE inside an exported question that takes only dates and
facts: s 30 (the claimant MUST take proceedings WITHIN three months of the notice, LEST the Court may bar the claim), s 70Q
(the personal representative MUST give the right to elect notice WITHIN 30 days of the grant), s 70R (the partner MUST elect
WITHIN 3 months, LEST only a Court extension saves it), s 99 (the eligible person MUST apply WITHIN 6 months of the grant,
LEST only a Court extension before final distribution saves it).

**Out, and why:**
- s 29(2)(b) (breach of promise of marriage): an action now abolished by Commonwealth law (Marriage Act 1961 (Cth) s 111A,
  not deposited, not checked here); noted.
- Part I Divisions 1A-5, 7, 8 other than ss 29 and 30 (wills deposit, grants, executors, administration of assets, commission,
  caveats, offences), s 31B (the threshold for paying without a grant, formula F1): machinery for the personal representative
  and payers; no claimant decision.
- Part IA ss 70D (entitled in more than one capacity: assumed by the questions, not asked), 70E, 70F, 70G (noted: lifetime
  gifts do not reduce entitlements, so no hotchpot is asked), 70H, 70I (the trust for sale and investment), 70S-70V, 70X, 70Y
  (procedure of the election, valuation and transfer; the personal representative's duties), 70N (the Minister's notice).
- Part II (small estates, including s 71 and its formula F3) and Part III (foreign grants): procedure.
- Part IV ss 91A (the Court's factors), 93, 94, 96, 97, 98: the Court's discretion and the order's form and effect;
  s 91(4), (5) are given as the list of what the Court must weigh, not as an amount.
- The transitionals other than ss 99AC, 101, 106: spent or about procedure.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within 3 months of", "within 6 months after", "12 months after" (ss 30, 70R, 70W, 99, 99A, 29(3)(c)) -- `the date` n
  `months after` -- the last day is the same day of the month n months on, or that month's last day where it is shorter --
  the Interpretation of Legislation Act 1984 (not deposited) may count otherwise.
- **F2** s 29(3) -- `s 29(3) -- my last day to sue the estate` -- the later of (b)(i) and (c), without a court's (b)(ii) longer
  period, which no one can know in advance -- include it once granted (it is in `Can I sue the estate`).
- **F3** s 70C(1) "survives the intestate for at least 30 days" -- `s 70C -- survival` -- 30 or more days from the day of death
  to the day the person died (or to today) -- count from the hour of death, or exclude both days.
- **F4** s 70L(1), s 70ZB(1) -- `Part IA -- what the partners take together` -- the residuary estate's worth includes the
  chattels for the legacy threshold; the balance is the worth less the chattels and the legacy (legacy paid only so far as
  the rest allows); under s 70ZB(1)(a), (b) the partners share the whole once -- the threshold tested without the chattels,
  or the chattels not taken out before the balance.
- **F5** s 70L(1)(b)(iii) "interest ... at the legacy interest rate" -- `s 70L(1)(b)(iii) -- interest on the statutory
  legacy` -- simple interest on a 365-day year from the day of death to the day of payment -- compound, or a 366-day year in a
  leap year.
- **F6** s 70M(3) -- `s 70M(2)-(4) -- the partner's statutory legacy for the year` -- the amount in effect is the greater of
  last year's amount in effect and the amount calculated (the formula runs on from the reduced amount) -- a running ledger of
  reductions and set-offs, which gives the same figures on the cases here.
- **F7** s 70W(2)(b) "before ... the distribution" -- `s 70W(2) -- what I must pay into the estate, and by when` -- the last day
  is the day before the distribution day -- earlier on the distribution day itself.
- **F8** s 90 "a full-time student aged between 18 years and 25 years" -- `s 90 -- the kind of eligible person I am` -- 18 to 25
  in whole years at the death, both ends in -- to the 25th birthday only.
- **F9** s 90(j) "if the child of the deceased dies within one year of the deceased's death" -- the same function -- on or after
  the death and no later than 12 months after it -- also a child who died within the year before.
- **F10** s 29(2A)(b) "the death of that person is from a dust-related condition which has been caused by the act or omission"
  -- `s 29(2A) -- the dust disease exception applies` -- the death must also be caused by the act or omission (asked
  separately) -- the condition's cause alone suffices.
- **F11** ss 70ZI(3), 70ZK(3), where no sibling (or aunt or uncle) survives but one who died left a child -- `Part IA -- who
  takes the residuary estate` -- the child takes as a line, the estate being divided by lines -- (1) and (2) do not apply
  without a surviving sibling, and the next class takes.
- **F12** s 99A(3)(b) "has not received written notice that an application ... has been made to the Court within 3 months of
  the receipt of that notice" -- `s 99A -- I may proceed against the personal representative over the distribution` -- the
  application must have been made within the 3 months (read with s 99A(4)(b)) -- the written notice must be received within
  them.
- **F13** s 90 -- `s 90 -- the kind of eligible person I am` -- the first paragraph that holds for the relationship given, with
  (k) tested for anyone meeting no earlier paragraph -- a person may be eligible under two paragraphs (a grandchild who lived
  in the household) and might choose the one without the dependency test; the question asks one relationship at a time.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "shall not apply" (s 29(1) proviso), "shall not include" (s 29(2)), "no proceedings ... may be maintained ...
except" (s 29(3)), "This Part applies if" (s 70A), "does not apply if" (s 70O(2)), "means" (s 3 dust-related condition and
domestic partner; s 90 eligible person and disability), "must not make ... unless satisfied" (s 91(2)), "must be made before"
(s 99(3)), "No action shall lie" (s 99A) and the periods of ss 29(3), 30, 70Q, 70R and 99 give `JUST FALSE` or a definite
answer. `NOTHING` (tagged) where the text points outside itself (deaths before the 2015 and 2017 amendments; a distribution
agreement or order; the Court's extension not yet sought), is silent (a family with no line at the first level; no notice
given yet), or is limited by its own wording (s 29(3) outside tort; Divisions 3-5 and s 70P without a partner; s 99A outside
the distributions it protects).

## What the Act turns out to say

1. **s 70C(2) says too much.** It reads "a person referred to in subsection (1) is taken to have predeceased the intestate";
   subsection (1) refers to every person, not only one who fails to survive 30 days. Encoded on the evident meaning (only the
   person who does not survive 30 days). Asserted (29 and 30 days).
2. **A sibling's grandchild sends the estate to the Crown.** s 70ZI(3) passes a predeceased sibling's share only to "a child
   who survives"; but s 70ZJ (grandparents) and s 70ZK (aunts and uncles) apply only where the intestate leaves "no sibling
   and no issue of a sibling". Where the only relatives nearer than grandparents are a sibling's grandchildren, no Division 6
   provision gives them anything and the grandparents, aunts and uncles are barred: s 70ZL gives the estate to the Crown.
   Encoded literally, with its own answer. Asserted. A lawyer may read s 70ZI(3) more widely, or the bar more narrowly.
3. **s 70M(2) repeats itself:** "calculated in accordance with the following formula--with the following formula--". A
   drafting slip with no effect on the formula.
4. **s 93 cites the wrong section.** "Notice of an application under section 91 must be served ..."; since 2014 applications
   are made under s 90A, and s 91 is the Court's power to make the order. Not encoded (service is procedure); noted.
5. **The dust disease exception needs proceedings started in life.** s 29(2A)(c) gives the estate damages for pain and
   suffering, harm and lost expectation of life only where the person "commenced" proceedings before death and they were
   pending at death. A person who died of mesothelioma before suing leaves an estate barred from those damages by
   s 29(2)(c)(ii). Asserted.
6. **"Does not leave multiple partners" includes no partner.** s 70O(1) is literally met when there is no partner at all;
   Division 4 then has no one to elect. Answered `NOTHING`. Asserted.
7. **s 70L(1) and the chattels.** The partner takes "the personal chattels" and "the amount of the partner's statutory
   legacy" and "one half of the balance", but the threshold ("worth not more than the amount of the partner's statutory
   legacy") does not say whether the chattels count in the worth, nor whether "the balance" is after them (fork F4). Under
   s 70ZB(1) the partners share the chattels under (a) and also the whole residuary estate under (b), which on a literal
   reading counts the chattels twice.
8. **s 99A(3)(b) is ambiguous** on what must happen within 3 months (fork F12); s 99A(4)(b) resolves it toward the
   application.
9. **s 29(3)(c) runs from representation, without limit.** A claimant not barred at the death has six months from the grant,
   however long after the death that is; if no one takes out representation, the (c) period has not begun. Encoded as "six
   months after representation is taken out, and at least until" the ordinary last day. Asserted.

## Before this is worth relying on

- Check the conversion, and the s 70M formula, against the authorised PDF.
- The Gazette notices of the partner's statutory legacy (s 70N) for each year since 2018, to replace the input.
- The Limitation of Actions Act 1958 (the s 29(3) last day), the Relationships Act 2008 (registered relationships), the
  Interpretation of Legislation Act 1984 (counting months), none deposited here.
- A lawyer's view on findings 2, 5 and 7 and forks F4, F8, F11, an independent test pass and a human gate.
