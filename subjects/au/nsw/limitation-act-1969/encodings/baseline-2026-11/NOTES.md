# Limitation Act 1969 (NSW) -- baseline encoding, the person bringing the claim

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025
> (corpus document dated 16 June 2022). It is unofficial and may be out of date: amendments after that version are
> missing. Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 in substance. A seat-neutral core
(`la-core.l4`) holds every rule, with one regulative rule (the action must be brought within the limitation period)
run by `EVALTRACE` inside a function that takes only plain facts. The seat layer (`la-seat.l4`) asks the questions and
restates no rule. Dates sit in one small module (`la-dates.l4`, built-in date functions only, no daydate, no `YMD`). No
REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.

Answers are named outcomes (enumerations) or dates, not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used. Where the
text says no in its own words (the s 6A(2) "means" list, s 6A(3) "only if", s 7 "nothing in this Act", s 62D's "if it
appears ... that") the outcome begins "no:"; where it does not answer (a settlement made without a judgment, under
Schedule 5) the outcome says "the Act does not say"; where a provision's scope is not met without an "only" (s 50D,
s 62A, s 62D for a claim outside Division 6) it says the provision "does not reach this". Judgments the Act leaves to
the court are inputs. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This is the first encoding of the Act; nothing existing was touched. The Choice of Law (Limitation Periods) Act 1993
baseline (`subjects/au/nsw/choice-of-law-limitation-periods-act-1993/encodings/baseline-2026-11/`) points here; the
stable `l4` cannot IMPORT across subjects, so the two are not linked in code.

## Edition

- **Act:** Limitation Act 1969 No 31, corpus document `nsw_legislation:2022-06-16/act-1969-031` (in force 16 June
  2022), deposited at `../../registers/source-bundle/act-1969-031.txt` (sha256 b97741c5...fed380d as committed), from
  the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge.
  Not the authorised text.
- **Not deposited:** the commencement of Division 6 of Part 2 (finding 1) and any amendment after 16 June 2022.
- **Regulations:** none set a number the encoded sections use.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `la-dates.l4` | 0 | 0 | 0 | 0 |
| `la-core.l4` | 0 | 0 | 0 | 0 |
| `la-seat.l4` | 0 | 0 | 0 | 0 |
| `la-cases.l4` | 0 | 0 | 114 | 114 |

Negative control, in a scratch copy: with the 28-day incapacity threshold lowered to 27 and the s 51 bar lengthened
from 30 to 31 years, the cases failed exactly the 5 predicted assertions (the 27-day incapacity, the continuing
incapacity's bar, the deed's 30-year bar, the fraud case's 30-year bar, the action brought the day after the bar).

Every expected value was worked by hand from the text, with day counts checked against a calendar independently of the
encoding and written beside the cases. Edges: the 18th birthday and the day before (and a 29 February birthday),
6 December 2002 and the day before, 1 September 1990 and the day before, "from and including" against "from", 29
February plus 3 years, an incapacity of 27 and of 28 days, an incapacity beginning on the last day and on the day after,
the deceased's discovery exactly 3 years and 3 years and a day before the death (s 50C(2)(a)), the 30-year bar, the
s 62D year after the 18th birthday to the day and a day over, the s 62A cap against the 3-year period (equal, and a day
apart). All 114 were satisfied on the first run.

## Seat

**The person bringing the claim (required)** (`la-seat.l4`, 9 questions): the person injured or wronged, including the
person abused as a child; the personal representative suing for that person's estate (a survivor action); the relatives
suing for the death (a compensation to relatives action). Questions: "Is there any time limit on my child abuse
claim?", "My claim was out of time, or an earlier action failed or was settled: can I sue now?", "Which limitation
period applies?", "By when must I commence?", "Was I in time?", "From what day is my claim discoverable?", "Can the
court extend my 12-year long-stop, and to when?", "Can the court extend my time because my parent failed to sue for
me?", "What happens to my right if my time runs out?". Provisions addressed to the court are encoded as what they mean
for that person: a period, a last day, an extension that may be ordered on stated conditions.

No seat for the defendant (a defendant's layer would be welcome: s 53, s 54, s 62C and the costs rules matter to them)
and none for the court.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no regulation sets a number used. One date
  from outside the deposit (finding 1).
- **The actors the text names.** Followed: the plaintiff, the defendant (the person against whom the cause of action
  lies), the deceased, the personal representative, the relatives (beneficiaries), the parent or guardian and close
  associate, the court.
- **Judgments answered conditionally.** Followed: discoverability ("knows or ought to know", s 50D), "sufficiently
  serious", "close associate" (s 50E(2)), "incapable of, or substantially impeded in, the management of his or her
  affairs", "reasonable diligence" (s 55), "just and reasonable" (s 62A, Sch 5 cl 10), "irrational decision" and
  "evidence to establish the cause of action" (s 62D), whether abuse was "serious" or "connected" (s 6A) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "child abuse" (s 6A(2), (3)), "disability"
  (s 11(3), s 50F(2)), "capable parent or guardian", "protected person" (as one fact), "discoverable" (s 50C(2),
  s 50D(4), s 50E), "survivor action" and "compensation to relatives action" (s 50B, as the plaintiff's kind).
  Borrowed and asked: "deed", "judgment", "penalty", a claim under another Act.
- **One case:** one claim by one plaintiff against one defendant.
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** ss 1-5, 6(1), 9, 10, 11A, 77, 78; Schedule 1.

## Scope

**In:** s 6A (no limitation period for child abuse actions) with Schedule 5 Part 3 (cll 8-10: claims already barred,
earlier actions and judgments, agreements connected with a judgment); s 7(a) (another Act's period displaces this Act);
s 11 definitions used (personal injury, breach of duty, disability); s 13 (the earliest bar); s 14 (6 years: contract
not under deed, tort, recognizance, money under an enactment); s 16 (deed, 12 years); s 17 (judgment, 12 years); s 18
(penalty, 2 years); s 18A (personal injury, 3 years, for an act before Division 6 and a cause accruing from 1 September
1990); s 19 (compensation to relatives, 3 or 6 years from the death); Part 2 Division 6 (ss 50A-50F: the 3-year
post-discoverability and 12-year long-stop periods, survivor and relatives actions, minors injured by close relatives,
disability); s 51 (30-year ultimate bar); s 52 (disability, outside Division 6); s 55 (fraud, deceit, concealment);
ss 62A, 62D, 62F (court extensions for a Division 6 claim); s 63 (extinction of the right).

**Out, and why:**

- **Part 3 Division 3 (ss 57-62: personal injury causes before the 2002 amendments, including the discretionary
  extension for latent injury, ss 60A-60M).** A pre-2002 personal injury claim is answered with its s 18A or s 19
  period only, and the answer does not show that a court may extend it under Division 3; a cause accruing before
  1 September 1990 answers "not covered". A second pass should add Subdivisions 2 and 3; they turn on "material facts of
  a decisive character" and are long.
- s 14A, 14B, 14C and Part 3 Division 2A (frustrated contracts, defamation), s 15 (accounts), ss 20-26 (arbitral
  awards, conversion, shipping, equitable relief, arrears of income, forfeiture of leases, contribution between
  tortfeasors), Part 2 Divisions 3-5 (land, mortgages, trusts), Part 4 ss 64-68A, Part 4 Division 2 (arbitration),
  Division 3 (ss 73A-78): not the claims this baseline serves; "another kind of claim" answers "not covered".
- s 53 (notice to proceed to a curator: the defendant's step, and excluded from Division 6 by s 50F(5)); s 54
  (confirmation by acknowledgment or payment: a debt rule, left for a pass on money claims); s 56 (mistake: the same
  shape as s 55, left out for want of a claims use).
- ss 62B (the matters the court considers: glossed in the s 62A input's `@desc`), 62C (the relatives' order that the
  deceased's expiry has no effect), 62E (costs).
- s 8(2) (Dust Diseases Tribunal Act 1989 s 12A) and the motor accident schemes (s 50A(3)) are folded into "a claim for
  which another Act fixes the limitation period" (s 7(a)).
- Schedule 5 Parts 1, 2 and 4 (the 1990, 2005 and 2020 transitional rules).

## Forks (the text does not say; one reading taken)

- **F1** "running from" a day: the day is not counted, and the period ends on the same day of the month that many
  months later, or that month's last day where it is shorter (29 February 2016 plus 3 years is 28 February 2019). A
  person born on 29 February turns 18 on 28 February in a common year.
- **F2** s 50C(1)(a) "3 years running from and including the date on which the cause of action is discoverable": the
  discoverable day counts, so the last day is the day before the third anniversary (finding 2).
- **F3** The day of the abuse, for s 6A, is the day it was perpetrated, or its first day where it went on over a period;
  abuse continuing past the 18th birthday is child abuse for the part before it.
- **F4** Division 6 is taken to have commenced on 6 December 2002 (finding 1).
- **F5** s 50E and a compensation to relatives action: s 50E(1) reaches any cause "founded on the death of or injury to"
  the victim, so it is applied to the relatives too, with the day the victim would have turned 25; and its long-stop
  (from the 25th birthday) is taken over s 50C(3)'s (from the death) (finding 4).
- **F6** Disability counts only where the injured person sues for themselves, and only that person's disability: the
  relatives' or the personal representative's disability is not modelled, nor s 52(1)(e)(ii) (death).
- **F7** One spell of incapacity, after minority where both count; days counted once. A spell must last 28 days or more
  in a row (or be continuing) and must begin on or before the period's last day.
- **F8** s 52(3): s 52 is never applied to a penalty or forfeiture (the "aggrieved party" exception is not modelled).
- **F9** s 51: the 30 years run from the day each Part 2 period runs from (for Division 6, the discoverable day and the
  long-stop day separately), and cap the period after s 52 and s 55 ("notwithstanding the provisions of this Part").
- **F10** s 55: the time before discovery "does not count", read as the period counting from the later of its start and
  the discovery day, for both Division 6 periods. s 55(4) (a purchaser in good faith) is out.
- **F11** s 62A: whether the long-stop ends first is judged on the two periods' last days (a period stopped by a
  continuing incapacity is judged on its 30-year day).
- **F12** s 62D(2)(a): a period stopped by a continuing incapacity has not "expired ... within 1 year after" 18.
- **F13** The regulative rule's day 0 is the day of the act or omission.
- **F14** s 18A is applied to every personal injury claim before Division 6 (s 11's "breach of duty" includes trespass to
  the person and duties under contract and statute).

## What the Act turns out to say (findings)

1. **Division 6's start is not in the text.** s 50A(2) applies Division 6 to acts or omissions "on or after the
   commencement of this Division"; the deposited corpus text carries no commencement note. 6 December 2002 is taken
   from the Civil Liability Amendment (Personal Responsibility) Act 2002, outside the deposit; check it against the
   authorised text.
2. **Two kinds of "3 years".** s 50C(1)(a) runs "from and including" the discoverable day; s 18A and s 19 run "from"
   their day. Read literally, a Division 6 claim's 3-year period ends a day earlier than the older periods (a claim
   discoverable on 10 March 2015 must be brought by 9 March 2018). Asserted.
3. **s 62A's cap is a day longer than the period that still bars.** The court may extend the long-stop "not ... beyond
   the period of 3 years after the date on which the cause of action is discoverable"; but the 3-year
   post-discoverability period ends the day before that (finding 2) and still bars the action, so the extension can
   never reach its own cap. The latest day is the 3-year period's last day. Asserted (discoverable 1 June 2016: cap
   1 June 2019, last day 31 May 2019). s 51(2) excepts only Division 3 Subdivision 3 orders, so the 30-year bar also
   limits a Division 4 extension.
4. **s 50E and relatives.** s 50E(3) adjusts "turns 25" for a survivor action when the victim dies young, but not for a
   compensation to relatives action, which s 50E(1) also reaches; and s 50C(3) (long-stop from the death) and
   s 50E(1)(b) (from the 25th birthday) both claim the relatives' long-stop. Fork F5.
5. **The s 6A(6) example is a note.** The power to dismiss or stay where a fair trial is impossible is given in a Note,
   which s 11A says is not part of the Act; the encoding cites s 6A(6) itself, which preserves the court's powers.
6. **Schedule 5 and settlements.** cl 8(2) extends "judgment" to an agreement made before and in connection with a
   judgment; a settlement made with no judgment is not dealt with by this Act (another Act may deal with it). Answered
   "the Act does not say". Asserted.
7. **Disability differs by regime.** Outside Division 6 a minor is under a disability while under 18 (s 11(3)(a)) and
   gets s 52(1)(e)'s three years after it ends; in Division 6 a minor with a capable parent or guardian is not under a
   disability at all (s 50F(2)(a)) and there is no three-year extension (s 50F(5)). Asserted.
8. **s 6A(3) bites narrowly.** Connected abuse after 18 is already outside s 6A(2); s 6A(3) adds only the case of
   connected abuse before 18 tied to sexual or serious physical abuse after 18. Asserted.

## Before relying on it

- Check the deposited text and the 6 December 2002 date against the authorised text on legislation.nsw.gov.au, and look
  for amendments after 16 June 2022 (to s 6A and Schedule 5 in particular).
- Add Part 3 Division 3 (pre-2002 personal injury extensions), s 54 and s 56, and a defendant's layer.
- An independent test pass and the human gates.
