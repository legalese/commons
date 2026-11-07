# Civil Liability Act 2003 (Queensland) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

This is the first encoding of this subject; nothing existing was touched. Eight files:

| File | What it holds |
|---|---|
| `claq-dates.l4` | days, the financial year, the one year (2026-2027) for which a Minister's notice is deposited (built-in date functions, no daydate) |
| `claq-common.l4` | s 5 (claims the Act does not decide), the schedule 2 kinds of harm and "dust-related condition"; 1 question |
| `claq-liability.l4` | chapter 2 (breach, obvious and inherent risks, recreation, doctors and professionals, rescuers, proportionate liability, public authorities, volunteers and food donors, offenders, intoxication, failed sterilisation) and chapter 4 parts 1 and 1A (regret and apologies); 18 questions |
| `claq-damages.l4` | chapter 3 (general damages, earnings and super caps, consortium, care given and lost, interest, exemplary damages, the injury insurance scheme, mitigation notices, structured settlements) and s 73; 15 questions |
| `claq-abuse.l4` | chapter 2 part 2A (claims against institutions for child abuse), with the one regulative rule; 9 questions |
| `claq-cases-*.l4` | the worked cases, one file for each rule module (s 5 cases are with liability) |

Each exported question calls a rule defined beside it; the rules are named by section so that a later seat layer can
import them. The Act is large but tractable: every part a claimant meets is in, and the parts left out are machinery,
transition, principles for the court with no answer the claimant could be given, or steps between defendants (Scope).

## Edition

- **Act:** Civil Liability Act 2003 (Qld), Act No. 16 of 2003 (`act-2003-016`), the version in force from 1 July 2024,
  current on 6 November 2026, deposited at `../../registers/source-bundle/act-2003-016.txt` (text sha256
  `2c8cbf78...551f766333` per its `.meta.json`; a Windows checkout with CRLF line endings hashes differently). A
  plain-text conversion of the Queensland Legislation HTML view, not the authorised PDF.
- **Numbers set elsewhere, deposited and brought in:**
  - Civil Liability Indexation Notice 2026 (`sl-2026-0090`, in force from 1 July 2026), deposited at
    `subjects/au/qld/civil-liability-indexation-notice-2026/`: s 3 ($59,300 for s 58(1)(b)), s 4 (the general damages
    table for s 62), s 5 ($197,770 for s 64(2)), all "for the 2026-2027 financial year". Hand-copied into
    `claq-damages.l4` with the item numbers.
  - Civil Liability Regulation 2025 (`sl-2025-0109`, in force from 1 September 2025), deposited at
    `subjects/au/qld/civil-liability-regulation-2025/`: s 4 and sch 1 (the one entity prescribed for ss 26, 27), sch 2
    s 4 (multiple injuries: at most 100, more than 25% above the dominant maximum needs detailed reasons) and sch 2 s 14
    (an ISV is a whole number).
- **Not deposited, and asked as facts:** the notices for other financial years (the answer is "not covered" outside
  2026-2027); average weekly earnings (sch 2, declared by the Australian Statistician); the 10 year Treasury bond rate
  (s 60(3), Reserve Bank table F2); the prescribed discount rate (s 57(2), borrowed from the Civil Proceedings Act 2011
  s 61: a regulation's rate, or 5%; the present value itself is asked); the superannuation guarantee percentage (s 56(2),
  "a written law"); whether workers' compensation is payable and under which section (s 5); the commencement of part 2A
  division 2 (s 86); the assent of the 2010 amending Act (s 85(2)).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read:
every diagnostic in the case files is `DiagnosticSeverity_Information` "assertion satisfied".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `claq-dates.l4` | 0 | 0 | 0 | 0 |
| `claq-common.l4` | 0 | 0 | 0 | 0 |
| `claq-liability.l4` | 0 | 0 | 0 | 0 |
| `claq-damages.l4` | 0 | 0 | 0 | 0 |
| `claq-abuse.l4` | 0 | 0 | 0 | 0 |
| `claq-cases-liability.l4` | 0 | 0 | 116 | 116 |
| `claq-cases-damages.l4` | 0 | 0 | 90 | 90 |
| `claq-cases-abuse.l4` | 0 | 0 | 52 | 52 |

Every one of the 43 exported questions has cases, with the edges: every band of the general damages table, its first
and last values, ISV 0 and 100, 101, 10.5 and -1, an injury on 1 December 2002, 30 June and 1 July 2026, 30 June and
1 July 2027; an uplift of exactly 25% and one more; general damages of $59,299 and $59,300 for s 58 and s 59A; 5.9 and 6
hours a week, 5 and 6 months (s 59); a breach on 30 June and 1 July 2010 (s 85); a blood alcohol of 149 and 150 (ss 47,
49); ages 15 and 16 (s 48); contributory negligence of 49% and 50% (s 52C); a future loss award of $197,770 and
$197,771 (s 64); the 119th and 120th day (s 33H(5)), across a leap day; the last day of a 28-day and a 14-day order and
the day after (s 33H(7)).

## Seat

**The claimant**: the person who suffered harm and claims damages for it -- the injured person (or, for a death, the
dependants or the estate), the person whose property was damaged or who suffered economic loss, and the person abused
as a child who claims against an institution. Questions are put as that person asks them ("Can I claim ...?", "What is
the most I can get ...?", "Whom can I sue ...?", "Must I prove ...?", "By when must the institution ...?"). Provisions
addressed to the court or a defendant (a doctor, a volunteer, an authority, an institution) are encoded for what they
mean to the claimant: whether the claim is barred, cut or capped, and what the claimant must be given and by when.

No second seat is written. The defendant (a doctor, a business, an institution) meets the same rules from the other side,
and a later `claq-seat-<party>.l4` layer could import these modules. No seat for the court, the Minister or the National
Injury Insurance Agency.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Indexation Notice 2026 and the Regulation
  2025 are brought in. Notices for other financial years are not deposited (the answer is "not covered").
- **The actors the text names.** Followed: the court, the defendant, doctors and professionals, public or other
  authorities, volunteers, community organisations, food donors, institutions, office holders, nominees, trustees.
- **Judgments answered conditionally.** Every "foreseeable", "obvious to a reasonable person", "significant degree of
  risk", "just and equitable", "satisfied", "harshly and unjustly", "reasonable", and the injury scale value, is asked
  and the answer given on it; none is decided.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: dust-related condition, obvious risk (s 13(5)),
  dangerous recreational activity, consumer (s 29), abuse (s 33A, both senses), associated trust (s 33B), the s 33C
  exclusions, gratuitous services (s 59), section 59A damages. Asked: "intoxicated" (the definition is a judgment),
  workers' compensation, average weekly earnings, the bond rate, the discount rate, National Injury Act terms
  (participant, lifetime participant), "professional", "indictable offence".
- **One case.** One claim by one claimant for one harm (one injury, one abuse claim).
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input and in each answer.
- **Operative sections in; machinery out.** ss 1-3, 6-8, 74, 75 and chapter 5 (except ss 85, 86, which decide what a
  claimant can have) are out.

## Scope

**In** (by module):

- `claq-common.l4`: s 4(1); s 5(1)-(3) (workers' compensation, dust-related conditions, tobacco; section 59A damages
  survive); schedule 2 "dust-related condition", "harm".
- `claq-liability.l4`: s 9(1); ss 13, 14, 15, 16; ss 17-19; ss 20-22; ss 25-27 with Regulation s 4 and sch 1; ss 28,
  29, 31, 32(1), 32D-32G; ss 36, 37 (s 35 named in the answers); ss 38-44 (volunteers and food donors); s 45;
  ss 47-49 (s 24 and s 48(5) in the answers); ss 49A, 49B; ss 68-72 and 72A-72D.
- `claq-damages.l4`: ss 50-52; ss 52A-52C; s 53; ss 54-56; s 58; s 59; ss 59A, 59B (s 59C glossed); s 60, with its
  example; ss 61, 62 with Notice s 4 and Regulation sch 2 ss 4, 14; s 64 with Notice s 5; s 66; s 73; s 85.
- `claq-abuse.l4`: ss 33A-33C; ss 33D, 33E with s 86; ss 33F-33I (ss 33O, 33P as asked facts); s 33H(5)-(7), with
  the one regulative rule; ss 33J-33MA.

**Regulative rule:** one. s 33H(7)(a): once the court orders it, the institution MUST identify its associated trusts
and give the information ordered WITHIN 28 days (or the period the court sets), LEST BREACH. It is run by EVALTRACE
inside `Has the institution identified its trusts in time`, which takes only dates and a yes/no; the not-yet-complied
case asks whether compliance on the as-at day would still be in time. No exported question takes a DEONTIC or an
EVENT.

**Out, and why:**
- ss 1-3, 6, 7, 8, 74, 75, and chapter 5 except ss 85 and 86: machinery and transition (s 75 is the source of the
  notice amounts, which are brought in; s 77's jury exception is spent).
- s 4(2)-(6): the provisions are tied to breaches on or after 2 December 2002, the day of assent, and the commencement
  of particular subsections; the day of assent and those commencements are not in the deposited text (the conversion
  drops history notes). Every question assumes a breach after these days; NOTES finding 4.
- ss 10, 11, 12, 23, 35, 46: principles the court applies, not an answer a claimant can be given; the onus in s 12 (on
  the plaintiff, for causation) and the s 35 principles are named in descriptions.
- ss 32(2)-(6), 32A-32C, 32H, 32I, 33: obligations and orders between concurrent wrongdoers and the court.
- ss 33N, 33Q: machinery. ss 33O, 33P: asked (in the description of the "whom can I sue" question).
- ss 55(1)-(3), 57: the court's method; the s 54 limit applies under s 55(4) and is encoded; the present value at the
  prescribed discount rate is asked.
- ss 59C, 59D: s 59C is glossed in the answer; s 59D bars a recipient's own claim, the recipient's seat.
- ss 63, 65, 67: the court's powers on structured settlements and costs of offers of compromise.
- Regulation sch 3-5 and sch 2 ss 1-3, 5-13: the ranges of ISVs for injuries, and the psychiatric impairment rating
  scale. The injury scale value is the court's assessment; it is asked as a number.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 5(1)(a), (b) "the harm ... is or includes an injury for which compensation is payable" -- `s 5 -- the Act
  reaches my claim` -- one injury with compensation payable takes the whole personal injury claim outside the Act, as
  the s 5 example says -- the Act still decides the claims for the other injuries.
- **F2** s 58(1)(b), s 59A(2)(a)(ii), s 64(2) (no period stated) -- `s 58(1) -- the consortium threshold met`,
  `s 64 -- notice of a proposed award` -- the amount fixed for the financial year in which the court assesses the
  damages or decides the award -- the amount for the year in which the injury arose, as s 62(4) says for general
  damages.
- **F3** s 62(1) "an injury arising after 1 December 2002" and s 62(4) "for the period within which the injury arose"
  -- `s 62 -- general damages` -- "not covered" (NOTHING) for an injury on or before 1 December 2002 and for a year whose
  notice is not deposited -- for the earlier injury, a JUST FALSE-kind "s 62 does not apply" (the common law then
  assesses general damages).
- **F4** s 54(2), (3) "the present value of 3 times average weekly earnings per week for each week", "the value when
  the award is made" -- `s 54 -- the limit on damages for loss of earnings` -- past weeks at 3 times average weekly
  earnings each, future weeks at a present-value multiplier the person gives -- past weeks also brought up to their
  value at the award (for example with interest or indexation), or average weekly earnings taken week by week.
- **F5** s 59(1)(c), s 59A(2)(e) "at least 6 hours per week", "at least 6 months" -- `s 59 -- gratuitous services to
  the injured person` -- 6 hours and 6 months are enough -- (none credible; recorded because the edge is asserted).
- **F6** s 15(2)(c) "a professional, other than a doctor", with s 21 -- `s 15 -- duty to warn of an obvious risk` --
  for a doctor and an obvious risk, s 15(1) applies (no proactive duty unless s 15(2)(a) or (b)) -- s 21 displaces s 15
  for doctors altogether (finding 7).
- **F7** s 31(1) with s 32G and ss 32D-32F -- `s 31 -- the most I can recover from this defendant` -- loss x (100% - my
  contributory negligence) x the defendant's share; for a fraudulent, intending or ACL s 18 wrongdoer, loss x (100% - my
  contributory negligence) -- the court's proportion for the defendant taken of the whole loss, with the plaintiff's
  share subtracted afterwards.
- **F8** s 33H(5)(a) "at least 120 days have passed since a proceeding ... was started" -- `s 33H(5)(a) -- the first
  day I may apply` -- the day 120 days after the start day -- the day after that (120 whole days between).
- **F9** s 86 "Chapter 2, part 2A, other than division 2, applies ... whether it arose before or after the
  commencement" -- `ss 33D, 33E -- presumed breach of the duty to prevent abuse` -- division 2 applies only to abuse
  after division 2 commenced (asked; the day is not in the deposited text) -- only to causes of action that accrued
  after it, which for abuse is usually the same day.
- **F10** s 33H(7)(a) "within 28 days or any other period" -- `s 33H(7)(a) -- identify the trusts within the period`
  -- the last day is the day 28 (or the set number of) days after the order, and compliance on the day of the order is
  in time -- the period ends a day earlier (the day of the order counted as day 1).
- **F11** s 72 (part 1) and s 72A(2) (part 1A) -- `ss 72, 72A-72D -- regret and apologies` -- s 72 keeps an individual's
  pre-proceeding expression of regret out even in a claim part 1A excludes (an assault or sexual misconduct claim) --
  part 1 read down to match part 1A (finding 6).
- **F12** ss 47 and 48-49 both arising -- `What is the least my damages are cut for intoxication` -- the larger minimum
  (50% over 25%) -- the two presumptions add (75%).
- **F13** s 33C(1) "the persons associated with an institution include" -- `s 33A -- an abuse claim` -- an unlisted
  person gives "not covered" (NOTHING kind: an unclosed "includes" list); s 33C(2), (3) give "no" (flat negatives) --
  an unlisted person is not associated.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "means" definitions (dust-related condition, dangerous recreational activity, consumer, abuse, institution)
answer no when a limb fails; the flat negatives with "unless" (ss 9(1), 13(5), 15(1), 21(1), 59(1)) and the flat "can
not" / "must not" / "does not" (ss 45(1), 49A(2), 52(1), 52B(2), 58(1), 60(1), 33C(2), (3), 59B) give "no" constructors;
"if" conditions unmet (ss 14, 16, 19, 22, 26, 27, 37(2), 33H(5)) give "does not apply" constructors; an unclosed
"includes" list (s 33C(1)) and a period whose notice is not deposited give "not covered" (NOTHING kind) (F3, F13);
s 22's defence, when not established, is worded "s 22 gives no defence on these facts", as ruling (b) of 2026-11-05
asks.

## What the Act turns out to say

1. **A stale cross-reference in s 59A.** s 59A(2)(a)(ii) still speaks of "the amount prescribed under section 58",
   but since the 2023 amendments (ss 87-89) s 58(1)(b) takes an amount "fixed by the Minister, by written notice under
   section 75"; nothing is "prescribed" under s 58 any more, and s 89 only continues amounts prescribed before the
   change. Read as the s 58 notice amount ($59,300 for 2026-2027) (F2). Asserted ($59,299 and $59,300).
2. **No year for two thresholds.** s 62(4) ties the general damages table to "the period within which the injury
   arose", but s 58(1)(b) and s 64(2) say only "the amount fixed ... for this provision [section]", and the notice
   fixes each "for the 2026-2027 financial year". Which year's amount applies to an injury of one year assessed in
   another is not said (F2).
3. **The general damages table is continuous.** Hand-checked: each band's base amount in Notice s 4 equals the top of
   the band below (5 x 2,010 = 10,050; 10,050 + 5 x 2,360 = 21,850; ... 359,750 + 10 x 6,540 = 425,150), so no ISV gives
   a jump; the most general damages can be, at ISV 100, is $494,150. Asserted.
4. **Commencement days are not in the text.** s 4(2)-(6) tie whole parts to breaches on or after "the day this Act
   receives assent" and the commencement of particular subsections; the deposited conversion drops the history notes
   that would give those days, so those gates are left out (Scope). Only 2 December 2002 (s 4(2)), 1 December 2002
   (ss 61, 62), 1 March 2005 (s 82) and 1 July 2010 (s 85) are in the text.
5. **A borrowed rate whose source disowns the award.** s 57(2) takes "prescribed discount rate" from the Civil
   Proceedings Act 2011 s 61, whose subsection (2) says that section "does not apply to an award of damages to which
   the Civil Liability Act 2003, chapter 3 applies". Only the definition is borrowed, so the rate is a Civil Proceedings
   regulation's rate, or 5%; no such regulation is deposited. The present value is asked.
6. **Regret survives where apologies do not.** Part 1A (apologies) does not apply to a claim for an unlawful
   intentional act done to cause injury or for unlawful sexual misconduct (s 72A(2)(c), (d)), but part 1 (expressions
   of regret, personal injury only) has no such exclusion: an individual's pre-proceeding expression of regret, so far
   as it admits nothing, stays inadmissible under s 72 in those claims (F11). Asserted.
7. **Doctors and obvious risks.** s 15(2)(c) takes doctors out of the professional exception, and s 21 sets when a
   doctor breaches the duty to warn. Read literally, a doctor owes no proactive duty to warn of an obvious risk unless
   asked or required by law (s 15(1)), while s 21 makes the doctor liable for not giving information a reasonable
   person would require; the note to s 15 points to s 21 without resolving the overlap (F6). Asserted (the doctor case).
8. **Two meanings of abuse.** For the presumed breach (division 2) abuse is only sexual or serious physical abuse
   (s 33A(a)); for the rest of part 2A it includes connected psychological abuse. A claim for connected psychological
   abuse is an abuse claim, but the institution is not presumed in breach for it. Asserted.
9. **Whom to sue depends on incorporation then and now.** s 33F (unincorporated then, incorporated now) and s 33G
   (unincorporated then and now, former office holder gone) cover the two gaps; an institution incorporated at the time
   is sued in the ordinary way, about which part 2A says nothing. A current office holder is "not personally liable"
   (s 33L). Asserted.
10. **Edges in the text.** "150mg or more of alcohol in 100mL of blood" (ss 47(5), 49(2)) includes 150; s 52C's "by less
   than 50%" excludes 50%; s 59's "at least 6 hours" and "at least 6 months" include 6; s 48 starts at "at least 16
   years". Asserted at each edge.
11. **One prescribed rescuer.** The Regulation's sch 1 prescribes a single entity for ss 26 and 27 (an aeromedical, air
   rescue and emergency helicopter service under an agreement with the State). Other first aid givers are not
   protected by these sections; Law Reform Act 1995 part 5 (preserved by ss 26(2), 27(2)) is not deposited. Asserted.
12. **Workers' compensation takes the whole claim out.** By the s 5 example, if any one injury from the event is one for
   which compensation is payable, the Act decides none of the personal injury claims arising from it, against any
   defendant, and whether compensation is claimed is immaterial (s 5(2)); only section 59A damages survive, and only
   for dust and tobacco injuries (s 5(3)). Those claims fall to the Workers' Compensation and Rehabilitation Act 2003,
   another subject. Asserted.

## Before this is worth relying on

- Deposit the Minister's notices for other financial years (at least 2024-2025 and 2025-2026, and 2027-2028 when made)
  and the earlier regulations s 89 continues, so that general damages, the s 58 threshold and the s 64 amount can be
  answered for injuries and awards outside 2026-2027.
- Settle F2 (which year's threshold) with a lawyer, and the overlap in finding 7.
- Deposit the Civil Proceedings Regulation (if one prescribes a discount rate), the Workers' Compensation and
  Rehabilitation Act 2003 ss 34, 35, the Law Reform Act 1995 part 5, and the Acts Interpretation Act 1954 (for F8 and
  F10).
- Find the commencement days the deposited text omits (s 4, s 86) and decide whether to encode s 4's gates.
- Check the conversion against the authorised PDF, an independent test pass, and a human gate.
