# Limitation of Actions Act 1936 (SA) -- baseline encoding, the person bringing the action

> **Warning.** The text encoded here is the South Australian register's current version (1.7.2021) as its
> **unauthorised** RTF, fetched on 6 November 2026; the authorised version is the PDF on legislation.sa.gov.au. Unlike
> the other South Australian baselines of this month (taken from the Open Australian Legal Corpus, collected 10 March
> 2025), this text came from the official register, because its bot challenge had lifted. It may still go out of date:
> check legislation.sa.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`loa-core.l4`) holds every rule, with three regulative rules (commencing the action
within the time limited; the s 45A(1) notice within 6 years after the incident; the s 45A(5) action within 6 months
after the defendant's notice), each run by `EVALTRACE` inside a function that takes only plain facts. The seat layer
(`loa-seat.l4`) asks the questions and restates no rule. Dates sit in one small module (`loa-dates.l4`, built-in date
functions only, no daydate, no `YMD`). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.

Answers are named outcomes (enumerations), dates or numbers, not `MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used.
Where the text says no in its own words (a "means" definition, an "if" that fails, "cannot be extended", "does not
apply", "no person shall be entitled") the outcome begins "no:"; where it does not answer (an "includes" list, a case it
is silent on) the outcome says "the Act does not say"; where a scope limit without "only" is not met, the outcome says
the section "does not reach this" (rule (c) of the 2026-11-05 ruling on periods, "where" and scope limits, in
substance). Judgments the Act leaves to the court are inputs. No pipeline, no coverage table, no independent test pass,
no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The Civil Liability Act 1936 baseline
(`subjects/au/sa/civil-liability-act-1936/encodings/baseline-2026-11/`) points here for time limits; the stable `l4`
cannot IMPORT across subjects, so the two are not linked in code.

## Edition

- **Act:** Limitation of Actions Act 1936, version 1.7.2021 (the one the register's Current Titles list of 22 September
  2026 gave), deposited at `../../registers/source-bundle/limitation-of-actions-act-1936.txt` (sha256
  8d055dc9...bd06d3d8 as committed; the working copy may have CRLF line ends).
- **Transitional provisions used,** as printed in the legislative history: Limitation of Actions (Child Abuse)
  Amendment Act 2018 Sch 1 cll 1-3; Defamation Act 2005 Sch 1 cl 8(1); Defamation (Miscellaneous) Amendment Act 2020
  Sch 1 cl 5. Commencement dates from the history table: s 38 17.6.1993; s 38(2) 2.6.1994; s 37 1.1.2006; s 37(2)-(4),
  37A, 37B 1.7.2021; s 3A 1.2.2019.
- **Regulations:** none set a number the encoded sections use. The contents of the s 45A notice are "required by
  regulation" (s 45A(3)); that is out.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `loa-dates.l4` | 0 | 0 | 0 | 0 |
| `loa-core.l4` | 0 | 0 | 0 | 0 |
| `loa-seat.l4` | 0 | 0 | 0 | 0 |
| `loa-cases.l4` | 0 | 0 | 138 | 138 |

Negative control: with the s 45(3) cap changed from 360 to 361 months and the s 37(2) window from 55 to 54 days, the
cases failed exactly 3 times, as predicted (the 30-year cap, the continuing incapacity's latest day, the first day of the
concerns-notice window); the core was restored and rechecked.

Every expected value was worked by hand from the text, with day counts written beside the s 45 and s 46A cases. Edges:
29 February (3 years, 6 months and 3 years from a leap day), 31 August plus 6 months, the 18th birthday and the day
before, the 30-year cap, childhood and incapacity overlapping, the first and last days of the s 37(2) window and the
day before it, the Act's own Example in s 37(3) (notice 7 days before expiry, extended by 50 days), the commencement
days (16/17 June 1993, 1/2 February 1994, 31 December 2005/1 January 2006, 30 June/1 July 2021), the 12 months of
s 48(3)(b)(i) to the day on both sides, the s 46A twelve months against a shorter grant, and the s 45A six years to the
day (injured at exactly 15, and a day younger). One expected value was first written wrong by hand (the windfall case,
8 500 for 7 500); the arithmetic was redone from s 38(3b) and corrected; the encoding was not changed.

## Seat

**The person entitled to bring the action (required)** (`loa-seat.l4`, 17 questions): the injured person, the person
abused as a child, the person defamed, the creditor or legatee, the payer of an invalid tax, the executor suing for an
estate. Every question is one that person would ask: "Is there any time limit on my child abuse claim?", "Can I sue now
although my claim was barred before 2019?", "Which period applies?", "By when must I commence?", "Was I in time?", "Do I
get more time because I was away or in prison?", "From when does my time run for a republication?", "Can the court
extend my defamation time, and to when?", "Do I still have 12 months?", "Can the court extend my time?", "Can the court
excuse my notice?", "Must I give notice of my intended action, to whom and by when?", "Was my notice in time?", "By when
must I sue after the defendant's notice?", "What do I lose for not complying?", "How much of the invalid tax can I
recover?". Provisions addressed to the court are encoded as what they mean for that person: a period, a last day, an
extension that may be granted on stated conditions.

No seat for the defendant (a defendant's seat would be welcome as a second layer: s 45A(4), (5) give the defendant
rights) and none for the court.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no regulation sets a number used.
- **The actors the text names.** Followed: the person entitled, the person liable, the defendant, the child and parent
  or guardian, the third-party insurer, the executor or administrator, the first publisher and associates, the court.
- **Judgments answered conditionally.** Followed: "just and reasonable" (s 37B, 2018 Act cl 3(2)), "materially
  different" (s 37A(3)), "just" (s 48(3)), "material" (s 48(3a)), reasonable delay caused by the defendant
  (s 48(3)(b)(ii)), "essential" (s 47(2)(d)), "justice of the case" (s 50), "good reason to excuse" (s 45A(7)),
  "serious" physical abuse, "latent", and mental incapacity (s 45(2)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "child" (s 3(1), from the date of birth),
  "abuse" (s 3A(5), as far as it goes), "legal disability" (s 45(2)), "associate" (s 37A(6)), "windfall profit"
  (s 38(3b)), "relevant date" (s 45A(1)). Borrowed and asked: "concerns notice" (Defamation Act 2005), "associated
  entity" (Corporations Act 2001 s 50AAA), "intentional tort", "motor accident", "specialty".
- **One case:** one action, by one person, against one person liable (so s 40, joint debtors, is out).
- **The Act's terms with plain glosses:** in the `@desc`s.
- **Machinery out:** s 1, s 3(2), s 38A (choice of law), s 49 (saving), the Ipp transitional clause (a pointer only).

## Scope

**In:** Part 1A (s 3A, no limitation period for child abuse, with the 2018 Act Sch 1 cll 2 and 3 for claims barred
before 1 February 2019); s 33 (money charged on land and legacies: 15 years, restarting on payment or written
acknowledgment, and s 33(3) for s 45); s 34 (specialties and judgments: 15 years, and the proviso); s 35 (6 years);
s 36 (personal injury: 3 years, and (1a) latent injury); s 37 (defamation: 1 year, (2)-(3) the concerns notice);
s 37A (single publication rule); s 37B (court extension to 3 years); s 38 (mistake and restitution 6 years; invalid tax 6
months, no extension, the windfall rule); s 39 (the person liable absent from the State); s 45 (childhood and mental
incapacity, the 30-year cap); s 45A(1), (2), (5), (7) (a child's injury: notice within 6 years, to whom, the defendant's
notice to sue, what non-compliance costs); s 46 (no more time for the claimant's absence or imprisonment); s 46A (an
action surviving for an estate); s 47 (a time limit under 12 months in another law); s 48 (the court's power to extend,
with (3a) and (4)); s 50 (dispensing with a notice before action).

**Out, and why:**

- Part 2 (ss 4-30: entry, distress and actions to recover land or rent, and the accrual rules for estates, tenancies,
  mortgages and acknowledgments) and s 27 (redeeming a mortgage): property law, not the claims this baseline serves;
  a second pass could encode s 4 with ss 5-17 as accrual inputs.
- Part 3 (ss 31-32: trusts): the beneficiary's claims against a trustee matter to estate claims, but s 32's exceptions
  (fraud, trust property retained) need their own design; left for a second pass.
- s 37C (the electronic-publication date rule is for limitation only): no answer for the claimant to compute; the
  definitions it qualifies are glossed in the `@desc`s.
- s 38A (limitation laws are substantive; choice of law), s 49 (saving of other rules): machinery.
- s 40 (joint debtors) and ss 41-44 (acknowledgments and payments by co-debtors, oral acknowledgments, endorsements,
  set-off): the one-defendant unit, and evidence rules. s 42(1)'s demand for signed writing is reflected in the `@desc`
  ("acknowledged in signed writing").
- s 45A(3) (notice contents by regulation, not deposited), (4) (records and medical examination on request: a duty
  whose request the defendant controls; it is folded into the s 45A(7) compliance input), (6) (the court's power to
  split liability and damages).
- Defamation Act 2005 Sch 1 cl 8(2)-(3) (multi-publication proceedings straddling 1 January 2006): publications before
  1 January 2006 answer "not covered".
- s 38(1)(b) and s 38(2)(b) (causes and payments before 1993-1994): answer "not covered"; every such period has run.

## Forks (the text does not say; one reading taken)

- **F1** "within three years next after", "within six months after", "1 year running from the date of publication",
  "within twelve months from", "up to 3 years running from": the last day is the same day of the month that many months
  later (the first day not counted), or that month's last day where shorter (29 February 2020 plus 3 years is
  28 February 2023; 31 August 2023 plus 6 months is 29 February 2024). Asserted.
- **F2** s 3A "when the person was a child": abuse at 18 or over answers that s 3A "does not reach this", not a "no".
- **F3** where s 36(1a) (latent) or s 33(2)/s 34 (later acknowledgment) and s 39 (return) both move the start, the later
  day is taken.
- **F4** s 37(2), (3): with the period's last day L, "days remaining after the notice day" is L minus the notice day,
  so the new last day is the notice day plus 56; the window is L minus 55 to L. This is the only count that agrees with
  the Example. Asserted, including the Example.
- **F5** "after the commencement" (2020 Act Sch 1 cl 5): a publication on 1 July 2021 itself is treated as after it.
- **F6** "the commencement of the 1994 amending Act", which commenced in parts (2.6.1994; ss 3, 5, 6 on 9.6.1994): read
  as 2 June 1994, when s 38(2) itself began; "within four months before" includes 2 February 1994.
- **F7** s 45: one period of mental incapacity is taken; days of childhood and of incapacity after the right arose are
  counted once each, overlaps once; the extension is counted in days; the time at which "the right ... arose" is the
  accrual day (the s 39 return day where s 39 applies; the s 33(3) day for money charged on land), even where s 36(1a)
  starts a latent injury's period later. A still-continuing incapacity answers "extended while it continues", with the
  30-year limit as the latest day.
- **F8** the order of the extensions: s 37(2), then s 45, then s 46A. s 46A needs the day of the grant (if none yet,
  the answer is only as good as the expected day given).
- **F9** s 45A(1)(b) "extended by this Act to more than 6 years": worked out from s 36 and s 45 for childhood alone,
  with the cause of action accruing on the day of the incident; s 45A(2): the notice goes to the third-party insurer
  (read as instead of the person alleged liable, not as well).
- **F10** s 48(3)(b)(i) "within twelve months before the expiration": ascertained after the day twelve months before the
  last day (a fact learnt exactly twelve months before does not count). Asserted.
- **F11** s 38(3b) "has not paid back ... the amount of the payment": read as the part passed on; the recoverable sum is
  the amount paid less the part passed on and not paid back (never below 0).
- **F12** s 45A for a child abuse action (no limitation period under s 3A): answered "the Act does not say" (finding 5).
- **F13** s 48 is applied to the defamation period like any other period in this Act (finding 7).

## What the Act turns out to say (findings)

1. **s 11's heading reads "Where average of forfeiture is not taken by remainder-man".** "Average" is almost certainly
   "advantage" (the section is about a remainder-man not taking the advantage of a forfeiture). Part 2 is out of scope;
   reported as a likely error in the text.
2. **ss 37A(5), (6) and 37C(2), (3) say "this clause".** They are sections of this Act; the wording was carried over from
   the model defamation provisions, where they were clauses of a Schedule.
3. **s 39 mixes "absent from the State" with "the return of that person from beyond the seas".** A person liable who was
   interstate does not return "from beyond the seas". The encoding runs the time from the return to the State. Asserted.
4. **s 45A runs from the incident, s 36(1a) from knowledge.** For a latent injury to a child, the 6-year notice under
   s 45A(1) is counted from "the date of the incident out of which the injury arose", so it can fall due before anyone
   knows of the injury, while the action itself would not yet be out of time. The encoding does not model latency in
   s 45A (fork F9).
5. **s 45A and s 3A do not meet.** s 45A(1)(b) applies where "the time for bringing an action ... is extended by this
   Act to more than 6 years". s 3A (2018) does not extend the time; it removes the limitation period. Whether a child
   abuse action needs the s 45A notice is not said; the Exception for intentional torts shows the 2004 drafters had
   assault in mind. Asserted as "the Act does not say".
6. **The 1994 amending Act commenced in two parts,** so "the commencement of the 1994 amending Act" in s 38(2)(a), (b) has
   two candidate days (fork F6).
7. **s 48 and s 37B overlap.** s 48(3)(b) lets the court extend "a limitation of time prescribed by this Act" on late
   discovery or the defendant's conduct; nothing excludes the s 37 defamation period, which s 37B also lets the court
   extend (to 3 years at most). Only s 38(3) bars extension in express words. s 47 cannot touch any of this Act's own
   periods (none is under twelve months).

## Before relying on it

Check the text against the authorised PDF and the register's current version; have a lawyer review the forks
(especially F4, F7, F9); encode Part 3 (trusts) for estate claims, the defendant's seat (s 45A(4), (5)), and Part 2 if
land claims are wanted; run an independent test pass.
