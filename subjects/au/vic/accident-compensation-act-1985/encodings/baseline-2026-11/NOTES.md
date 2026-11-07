# Accident Compensation Act 1985 (Vic) -- baseline encoding, the injured worker (legacy claims)

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Accident Compensation Act 1985, Act No. 10191/1985, Version No. 237, incorporating amendments as at 2 October 2026,
  deposited at `../../registers/source-bundle/accident-compensation-act-1985.txt` (sha256 3635e0cb...7a182fd1 as reconverted on 2026-11-07; first deposited as 60b465c4...d32d6dc0),
  a plain-text conversion of the Word file the owner saved by hand on 6 November 2026 (see that file's `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved.
- **The numbers the Act uses:** the Accident Compensation Act 1985 notice in Victoria Government Gazette No. S 363 of
  30 June 2026 (Division 2D indexation), deposited at
  `subjects/au/vic/workers-compensation-annual-indexation-notice/registers/source-bundle/GG2026S363.txt` (sha256
  04c8fe55...5945499a), text lines 9-336. The stable `l4` cannot IMPORT across subject folders, so the figures used are
  copied into `aca-amounts.l4` with their lines. As in that subject's encoding, the "before 1 July 2026" column is read as
  1 July 2025 to 30 June 2026 and the "from 1 July 2026" column as 1 July 2026 to 30 June 2027; any other day answers
  `NOTHING`.
- **Formulas sidecar:** none of the 12 embedded equations is in scope (they are in ss 5AD, 100-100C, 115B, 117B, 129B
  and 138); the s 98C formulas are linearised in the text itself and were read there.
- **Deposit corrected, 2026-11-07.** The first conversion dropped the characters the register sets in the Symbol font,
  so the s 98C(2) and (3) formulas this encoding reads were deposited without their multiplication signs ("$11 670 +
  [(D – 10) $9940]", "{...} 1·1"). The encoding had read them as multiplications from the start, so no value changed;
  the formulas quoted in `aca-amounts.l4` and `aca-weekly.l4` now carry the "x" the reconverted text restores. The other
  restored characters (the minus signs and "0·278" of s 91(3)(c), (3A)(c), the "9·5%" and "8·4%" of the s 91(10)
  example, the minus signs of s 98C(3A)) are in provisions this encoding leaves out. No finding depended on them.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `aca-dates.l4` | 0 | 0 | 0 | 0 |
| `aca-amounts.l4` | 0 | 0 | 0 | 0 |
| `aca-weekly.l4` | 0 | 0 | 0 | 0 |
| `aca-damages.l4` | 0 | 0 | 0 | 0 |
| `aca-cases-weekly.l4` | 0 | 0 | 107 | 107 |
| `aca-cases-damages.l4` | 0 | 0 | 132 | 132 |

Every expected value was worked by hand from the text (and the Gazette for the indexed figures), with the edges: the
first and last day of each date band, the 13/26, 91/117 and 78-week boundaries, the ceilings on 30 June and 1 July 2026,
the $257 and 20% limits of s 93CD, the 130-week rule, every s 98C band edge (9/10, 30/31, 70/71, 80/81, the 1.1 spinal
uplift and its $75,410 cap), the 120-day and 30-day periods across 24 December to 9 January, the 21/51/30-day windows,
each threshold one dollar under, the 90% costs line, and the 210-day window of s 135A(2AA).

## Seat

**The injured worker** whose injury arose before 1 July 2014 (s 4(1)(a)) and so is still governed by this Act. Every
exported question is one the worker would ask ("Which entitlement period am I in?", "How much is my weekly payment this
week?", "May I make my serious injury application now?", "Am I deemed to have a serious injury?", "By when must I apply
for leave?", "What can the court award me?", "Who pays the costs?"). Provisions addressed to the Authority (WorkSafe), a
self-insurer or the court (ss 93CD(3), 134AB(7), (13), (16), (22), (28), 135A(2D), (7)) are encoded as what they mean for
the worker: a deadline, a deemed serious injury, a deemed offer, a cap, a costs outcome. No other seat: the claims are
answered by the Authority or a self-insurer, and officials get none.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Gazette notice supplies the Division 2D
  figures for 2025-26 and 2026-27. Figures for other years are not deposited: `NOTHING`.
- **The actors the text names.** Followed: the worker, the Authority, the self-insurer, the court.
- **Judgments answered conditionally.** Followed: "assessed as having no current work capacity", "satisfied that",
  "determines", the court's leave, the serious injury narrative test of s 134AB(38)(b)-(d), the permanent 40% loss of
  s 134AB(38)(e)(ii) and contributory negligence are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: first and second entitlement period,
  pre-12 November 1997 claimant, serious injury (s 91E), impairment benefit rating (s 98C(2A) with Schedule 2), response
  date and the loss of earning capacity measure (s 134AB(38)(f), (g)) are worked out. The 2013 Act's terms this Act borrows
  by s 5(2)(a) (current work capacity, retirement age, State average weekly earnings) and pre-injury average weekly
  earnings as indexed are asked or taken from the Gazette.
- **One case.** One worker, one injury, one claim.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**
- **Which law** -- s 4(1); ss 134A(1), (3), 134AA (transport accidents as a fact), 134AB(1), (2), (2A), 135A(1).
- **Weekly payments** (Part IV Division 2) -- s 91E (definitions), ss 93, 93A(1)-(3), 93B(1)-(3), 93C(1), (2), 93CD(1),
  (3), (4), (5), 93CE(1)-(3), 93E, 93F, with s 100B (the ceilings) and ss 313, 315.
- **Non-economic loss** (Division 2A) -- s 98C(1A), (1), (2), (2A), (3), (3AA), (3AB), (4), (11) with Schedule 2; s 98D;
  s 265.
- **s 134AB** -- subsections (3), (4), (4A), (6), (6A), (7), (9), (12)(a)-(e), (13), (14), (15), (16), (17), (20A), (21),
  (21A), (22), (25), (26), (28), (28A), (28B), (32), (36), (36A), (36B), (37) (determination date, response date),
  (38)(e)-(g).
- **s 135A and s 135AC** -- s 135A(1), (2), (2A), (2AA), (2BB), (2D), (2DB), (3), (4)(b), (7), (11), (12), (13A), (14),
  (18), (18AA), (18AB), and s 135AC.

**Regulative rules:** two. One for s 134AB(7) with (9), one for s 135A(2D) with (2DB): the Authority or self-insurer MUST
advise WITHIN the period, LEST a breach whose reason is the deemed serious injury. They run on a day count (the
s 134AB(6A) count, or plain days for s 135A) inside the exported questions, which take only dates and facts. The other
time limits (s 93CD(3), s 134AB(12), (16)(b), s 135A(4)(b)) are conditions on the worker's own steps or dates for the
insurer, and are encoded as dates and yes/no answers.

**Out, and why:**
- Part I Division 2 (pre-injury average weekly earnings, ss 5A-5AD, Schedule 1A): an input, already indexed (the s 5AD
  equation is in the sidecar).
- Death benefits and dependants' pensions (ss 92-92D), s 134ABAA, s 135A(8), (9), s 135C: another seat (the dependants).
- ss 80-91D (entitlement, journeys, diseases, industrial deafness, lung injury, the s 91 assessment method): asked as facts
  (an injury that entitles the worker; a degree of impairment).
- ss 93CA, 93CAB, 93EA (surgery and hospital treatment after the second period or after retirement age), s 96, s 97.
- ss 98, 98A (the pre-1997 maims and pain and suffering lump sums), s 98E and Schedule 3B (no disadvantage), s 98C(3A),
  (3B) (further industrial deafness, lung), (6)-(10A).
- Division 2B (medical and like services), 2BA (provisional payments for mental injury), 2C.
- Division 3 claims procedure (ss 103-114F), including s 104B, whose determinations s 134AB uses: their dates and results
  are asked. Division 3A settlements (ss 115-119L). Divisions 4-7 (liability, payment, contribution between insurers
  ss 129A-129M, choice of law, conduct of common law proceedings, trustee company).
- s 134AB(5)-(5A), (8), (10), (11), (18), (19), (19A), (20), (20B), (23), (24), (27), (29)-(31), (33)-(35): forms,
  disclosure, evidence, jury, costs scales and representatives; s 134ABA (limitation periods disregarded; the Limitation
  of Actions Act 1958 is not deposited here); s 134AF; ss 134AFA-134AGB (legal costs orders).
- s 135A(2B), (2BA), (2C), (2DA), (2DC)-(2DG) as procedure (the (2DE) conference and offers mirror s 134AB(12) and are
  not separately encoded), (4A), (5), (6), (6A)-(6C), (10), (13), (13B)-(13D), (15)-(17), (18A), (18B); ss 135AB, 135AD.
- Divisions 9A-9C (terminally ill workers, dust conditions), Division 10, Parts VIII and IX (general, savings and
  transitional) except ss 265, 313, 315.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 91E first entitlement period (a) -- `the entitlement period of week` -- the pre-1997 26 weeks are counted as
  weeks of weekly payments -- the text counts "an aggregate period of incapacity for work ... after the worker became
  entitled", which could differ from weeks paid.
- **F2** s 93C(1)(a) "subject to paragraph (c)" -- `my weekly payments continue after the second entitlement period` --
  where the second period expires on or after 31 March 2024, (a) alone does not continue payments -- (a) and (c) as two
  independent routes.
- **F3** the Act's printed amounts -- `aca-amounts.l4`, `my s 98C lump sum` -- read as those in force from 1 July 2013 to
  30 June 2014 (the base Division 2D varies from 1 July 2014); the s 98C(11) maximum is known only for an injury in that
  year, and the bands up to 70% are taken never to reach it -- the printed figures may have been in force only on
  30 June 2014, and an earlier maximum may have been lower.
- **F4** ss 93A-93CD "the difference between" -- `the lesser of ... but not below nothing` -- a negative difference pays
  nothing -- the text is silent.
- **F5** s 93C(2) and s 93CD(5) -- `my weekly payment for` -- a worker continuing only through an approved s 93CD
  application is paid at the s 93CD(5) rate (80%, even for a pre-1997 serious injury) -- s 93C(2)(a)'s 90%.
- **F6** ss 313, 315 "commencement date" -- `my s 93CD application can be approved`, `the superannuation contribution` --
  5 April 2010 (the date s 93A(3) uses) -- the commencement of ss 34 and 37 of the 2010 amending Act, not stated in the
  deposit.
- **F7** s 93CE(1) nomination within 3 months -- `the superannuation contribution` -- asked as "nominated and gave a tax
  file number" -- s 93CE(4)(g) bars only the periods before the details are received.
- **F8** s 98C(2A)(a)(i)-(iii) -- `my s 98C(2) amount` -- (i) for a non-spinal Chapter 3 impairment, (ii) for a spinal
  one, (iii) when s 265 shuts out (ii); every open candidate priced and the highest taken -- (i) and (ii) both open for a
  spinal impairment.
- **F9** s 134AB(37) response date -- `What is my response date` -- 28 plain days ((6A) does not list (37)) -- counted
  leaving out 24 December to 9 January because the dates run on into (12).
- **F10** s 134AB(12)(e) after a deemed counter offer -- `I may commence proceedings` -- from the day after the deemed
  counter offer -- not earlier than 21 days after it, as for a real one.
- **F11** s 134AB(17) -- `what I may sue for under s 134AB` -- applied to a certificate under (16)(a) as to leave under
  (16)(b) -- (17) speaks only of "proceedings in accordance with subsection (16)(b)".
- **F12** s 135AC "the cause of action arose" -- `I may recover damages under s 135A` -- taken as the day of the injury --
  the Limitation of Actions Act 1958's accrual rules (s 135AD), not deposited.
- **F13** s 134AB(22), s 135A(7) maximum -- `the most the court may award` -- the maximum caps the damages assessed and the
  reductions follow -- the cap applied to the judgment after the reductions.
- **F14** s 134AB(25), s 135A(11) -- `the judgment after the reductions` -- each head reduced to no less than nothing --
  an excess of compensation over one head set against the other.
- **F15** s 135A(13A) -- `Who pays the costs` -- the amount is the judgment as entered (s 135A has no (28A)) -- the amount
  after the s 135A(11) reduction to the counter offer date, as under s 134AB(28A).
- **F16** s 134AB(4)(b)(i) "at least 18 months" -- `eighteen months after` -- the same day of the month 18 months on (a day
  that does not exist, such as 31 February, is left to the built-in date function) -- months of 30 days.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "shall not ... except", "may not ... unless", "must not ... unless", "may only ... after", "ceases ...
unless" and "is not entitled" give `JUST FALSE`; a period the text fixes ("within 120 days", "within 30 days", "not earlier
than 21 days, and not more than 51 days") gives `JUST FALSE` outside it; a figure, an earlier version of a section, the
Transport Accident Act or the 2013 Act that the deposit does not hold gives `NOTHING` (*points outside the text*); the
Act's own date limits (s 4(1), s 135A(1), s 315) give `NOTHING` (*limited by its own wording*).

## What the Act turns out to say

1. **s 129B(3): "(E / F) x F".** The Word file's equation (85-10191a237-F9) multiplies by F what it divides by F, while its
   "where" list defines C, E and F; the denominator was probably meant to be C. s 129B is contribution between insurers
   (out of scope), so nothing here depends on it. Check the authorised PDF.
2. **Every amount the Act prints is a 2013-14 figure.** Division 2D varies them "in respect of the financial year beginning
   on 1 July 2014 and each subsequent financial year": the dollars in ss 93A-93CD, 98C and 134AB(22) are not what anyone
   is paid now. The 2026-27 figures are in the Gazette ($1,740, $2,200 and $3,000 weekly ceilings; $79,890 / $1,798,500
   and $77,130 / $783,000 under s 134AB(22); $87,360 / $1,966,550 and $71,440 / $725,220 under s 135A(7)). Asserted.
3. **The s 98C bands up to 70% are frozen.** Their items in the Table to s 100C are gone ("* * * * *"), and their relevant
   date is the injury date, so a worker injured in 2013 and assessed in 2026 at 40% gets $122,260, the printed figure;
   over 70% the relevant date is the calculation date and the Gazette's figures apply ($410,870 at 71% in 2026-27).
   Asserted.
4. **s 93B(1)(a) does not depend on work capacity.** For a pre-12 November 1997 claimant with a serious injury the second
   period rate is 90% of PIAWE less 90% of current weekly earnings, with or without a current work capacity. The Gazette
   lists s 93B(1)(a)(ii) under "Where worker has no current work capacity", and the notice's own encoding
   (`workers-compensation-annual-indexation-notice/encodings/baseline-2026-10`) answers "not covered" for a serious injury
   with a capacity; this encoding, reading the Act, pays it ($1,290 on $2,000 PIAWE and $500 earnings in 2026-27).
   Asserted.
5. **A gap for old claims.** s 93A(1), s 93B(1), s 93C(2)(a), (b) and s 93CD(5)(a) rate only a "pre-12 November 1997
   claimant" (a worker entitled to weekly payments as at 12 November 1997); s 93A(2), (3) rate claims "first made" on or
   after 12 November 1997. A claim made before 12 November 1997 by a worker who was not entitled on that date has no rate,
   and s 91E gives it no first entitlement period. Answered `NOTHING`. Asserted.
6. **s 98C(11) takes back the indexation above $555,350.** "a worker is not entitled to an amount of compensation for
   non-economic loss ... that exceeds the maximum amount payable under this section as in force at the date of the
   relevant injury". Every injury under this Act is before 1 July 2014, so on a literal reading the 2026-27 maximum of
   $783,000 (s 98C(2)(e)(ii), (f)) can never be paid: an 81% rating for a March 2014 injury gets $555,350, not $783,000,
   and a 75% rating $555,350, not $576,310. Encoded literally; the formula amount is a separate question so that both are
   visible. Asserted. A lawyer should say whether (11) was meant for the (7)/(8) aggregate only.
7. **The 2003-2010 injuries are split oddly.** s 98C(3AB) sends the (2)(b) and (2)(c) amounts for injuries from 3 December
   2003 to 30 June 2010 back to the amounts then in force, but not (2)(d); (3AA) does send (2)(d) back for injuries
   before 3 December 2003. Read literally, a 40% rating for a 2008 injury takes the printed (2)(d) figure ($122,260) while
   a 20% rating takes the 2008 figure (not deposited). Nothing says what applies to injuries from 1 July 2010 to 30 June
   2013: the printed figures are used. Asserted.
8. **The Christmas rule does not reach everything.** s 134AB(6A) leaves out 24 December to 9 January for subsections (7),
   (10)-(14) and (16) only: not the 28 days of the response date (37), the 18 months of (4)(b), or anything in s 135A. A
   serious injury application received on 1 November 2026 must be answered by 18 March 2027, not 1 March. Asserted.
9. **No first day after a deemed counter offer.** s 134AB(12)(e) gives "not earlier than 21 days, and not more than 51
   days" after a real counter offer, but only "not more than 30 days" after a deemed one (F10). Asserted.
10. **s 135A has no (28A).** The costs comparison under s 134AB(28) reduces the judgment by compensation paid to the
    counter offer date (28A); s 135A(13A) uses the same words with no such rule (F15).
11. **The s 93CD rate for an old serious injury.** A pre-1997 claimant with a serious injury who continues under
    s 93C(1)(b) is paid at 90%; the same worker continuing only through an approved s 93CD application is paid at 80%
    (s 93CD(5)(a)) (F5). Asserted ($1,290 against $1,200).
12. **Transitional dates not in the text.** ss 313 and 315 apply ss 93CD and 93CE by "the commencement date" of the 2010
    amending Act's provisions, which the deposit does not state (F6).

## Before this is worth relying on

- Check the conversion and the Gazette figures against the authorised PDF and the published Gazette.
- The Gazette notices for years other than 2025-26 and 2026-27, and the earlier versions of s 98C and s 93CD that the
  transitional provisions keep alive.
- The 2013 Act's definitions borrowed by s 5(2)(a) (current work capacity, retirement age, State average weekly
  earnings), and Part I Division 2 (pre-injury average weekly earnings) with s 100 indexation.
- s 104B and the s 91 assessment, s 134ABA and the Limitation of Actions Act 1958, ss 98, 98A and 98E for the pre-1997 and
  no-disadvantage lump sums, the dependants' seat (ss 92-92D, 135A(8), 135C), Divisions 9A-9C (dust conditions).
- A lawyer's view on findings 4, 6 and 7, an independent test pass and a human gate.
