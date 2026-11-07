# Limitation Act 1974 (Tas) -- baseline encoding of the child abuse provisions, the survivor

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026; (c) State of Tasmania, licensed
under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

**Focus: Tasmania's equivalents of the child abuse limitation removals and organisational liability amendments.** After
the Royal Commission into Institutional Responses to Child Sexual Abuse each Australian jurisdiction removed the limitation
period for child abuse claims, allowed old settlements to be set aside, and made organisations liable for abuse by people
associated with them. In Tasmania the first two are in this Act: s 5B (Limitation Amendment Act 2017, applied 1 July 2018)
and s 5C (No. 48 of 2019, applied 1 May 2020). The third is Part 10C of the Civil Liability Act 2002 (Tas), inserted by the
same 2019 Act; it is a different Act, and the stable `l4` cannot IMPORT across subjects, so it is out of this folder (see
Scope).

**An extension, not a replacement.** The claimant's baseline beside this one (`../baseline-2026-11/`) covers the whole Act
from the claimant's seat and asks ss 5B and 5C in brief. It stays untouched. This folder is a second, equal encoding that
takes the child abuse provisions further: the kinds of abuse that fall outside s 5B, and the ordinary limit that then
applies with the s 26A suspension that matters most to a child abused at home; ss 38 and 39(1) as limits on s 5B; and
s 5C clause by clause (the definition, the National Redress Scheme exclusion, which agreements become void, the bar on
clawing back what was paid, the offset). It reuses nothing by IMPORT (the folders cannot see each other); where the two
cover the same words they were written to agree, with one difference (finding 1).

Modules: `tlca-dates.l4` (dates, built-in date functions only, no daydate), `tlca-rules.l4` (the law), `tlca-seat.l4` (the
survivor's questions, importing the rules and restating none), `tlca-cases.l4` (the worked cases).

## Edition

- **Act:** Limitation Act 1974 (Tas), No. 98 of 1974, consolidated version published 2024-07-18 and current at point in
  time 2026-11-06, as deposited at `../../registers/source-bundle/act-1974-098.txt` (text sha256 af438489...6fada09),
  retrieved from legislation.tas.gov.au on 6 November 2026. It includes No. 52 of 2017 (ss 5B, 26(1A), 26A, 38A as
  substituted, applied 1 July 2018) and No. 48 of 2019 (s 5C, applied 1 May 2020).
- **Numbers set elsewhere:** none; the Act has no regulations. Two days are taken from the text: 1 July 2018, the
  commencement of s 5B and "amendment day" (history notes; s 38A(1)); 1 January 1975, the commencement of the Act (s 1(2)),
  for s 39(1).
- **Borrowed terms asked as facts:** "sexual abuse", "serious physical abuse", "psychological abuse" (ss 5B, 5C,
  undefined); "minor" and "child" (finding 9); whether an act was "lawful at the time" (s 5C(1)); whether an action was
  "barred before the commencement of this Act" (s 39(1), which turns on the law before 1975); whether another enactment
  prescribes a period (s 38); the date of discoverability (its "ought to have known" is a judgment, entered as a date);
  whether a limitation period had expired before a settlement (s 5C(1)); whether an agreement relates to the settlement or
  to the child abuse, and how far (s 5C(4)).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; a
deliberately wrong assertion was run once in a scratch file (since deleted) to confirm that a failure shows as
`DiagnosticSeverity_Error`, "assertion failed". Satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `tlca-dates.l4` | 0 | 0 | 0 | 0 |
| `tlca-rules.l4` | 0 | 0 | 0 | 0 |
| `tlca-seat.l4` | 0 | 0 | 0 | 0 |
| `tlca-cases.l4` | 0 | 0 | 89 | 89 |

Every expected value was worked by hand from the text, with the edges: each kind of abuse and of action in and out of
s 5B; ss 38 and 39(1) alone and together; s 38A(3) at 30 June and 1 July 2015; the last day and the day after (9 / 10 March
2023); 29 February as the date of discoverability and as a birthday; a minor's suspension cut at the day before the 18th
birthday, beginning before the date of discoverability, on the last day and on the day after it; an incapacity of 27 and
28 days and one not ended; s 5C settlements on 30 June and 1 July 2018; every branch of s 5C(4), (5) and (7), with half of
an odd total.

## Seat

**The survivor** (`tlca-seat.l4`): the person who was sexually or physically abused as a child and brings, or thinks of
bringing, an action for damages for the injury -- or, after the survivor's death, the family member or personal
representative bringing a Fatal Accidents Act 1934 action for it. "Can I sue at any time?", "By when must I sue?", "Is my
time stopped?", "Can a judge give me 6 years?", "Can I still sue on this day?", "Is what happened child abuse under
s 5C?", "Can I reopen the settlement I made?", "What becomes of the deed I signed?", "Can they get back what they paid
me?", "How much of it can the court count against my damages?". No seat for the court, the person or institution sued, an
insurer or the National Redress Scheme operator: the court's orders and judgments are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers. Part 10C of the
  Civil Liability Act 2002 is the other half of the reform, but a different Act (Scope).
- **The actors the text names.** Followed: the person (plaintiff), the intended defendant, the parent and capable parent,
  the legal representative, the judge and the relevant court, the parties to the agreement, the organisation (s 5C(3)(c)).
- **Judgments answered conditionally.** Followed: "just and reasonable" (s 5A(5), s 5C(6)), "interest(s) of justice"
  (s 5C(2), (3)), "ought to have known" (s 2(1)) and "may be ... influenced" (s 26A(2)) are inputs, or are named in the
  answer as the court's to decide.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "child abuse", "previously settled relevant right
  of action" (s 5C(1)), "capable parent", "relevant person" (s 26A) and the s 5B grant are worked out from facts.
- **One case.** One action about the abuse of one person (for s 5C: one settlement).
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (Scope).

## Scope

**In:** s 2(1) (date of discoverability, as an input); s 5A(3), (4), (5) for abuse outside s 5B; s 5B(1), (2) (and (3) in
the description); s 5C(1), (2), (3) (in the description: the factors are the court's), (4), (5), (6), (7), (8); s 26(1A);
s 26A(1), (2), (3), (4) (and (5) in the description); s 38; s 38A(1)-(3); s 39(1).

**Regulative rules:** two. (1) The time bar of s 5A(3) ("must not be brought after the expiration of") as what the
plaintiff must do: `PARTY the plaintiff MUST bring the action WITHIN` the days to the last day, `LEST BREACH ... BECAUSE`;
run by EVALTRACE inside `Can I still bring my abuse action on this day`. (2) s 5C(5) as a prohibition on the other party:
`PARTY the other party to the settlement SHANT seek to recover what it paid because the agreement is void`, run by
EVALTRACE inside `Can the other party get back what it paid me`. No exported question takes a DEONTIC or an EVENT.

**Out, and why:**
- **Civil Liability Act 2002 (Tas) Part 10C (ss 49C-49S) and s 4(9):** the organisational liability half of the reform --
  the duty of an organisation responsible for a child to prevent abuse by individuals associated with it, with its
  reversed onus (Division 2), vicarious liability for employees and those akin to employees (Division 3), and the proper
  defendant for an unincorporated organisation (Division 4). A different Act; its text is deposited at
  `subjects/au/tas/civil-liability-act-2002/`, and its encoding belongs there.
- The rest of this Act (contract, tort other than injury, land, trusts, tax refunds, acknowledgement, choice of law): in
  the claimant's baseline beside this one, or out there with its reasons.
- s 5A(6) (a personal representative's date of discoverability) and s 32 (fraud and mistake): in the claimant's baseline;
  here the date of discoverability is an input.
- s 26A(6), (7) (a legal representative's knowledge) and a second spell of suspension: one spell only here; the claimant's
  baseline takes two.
- s 38A(4) (actions begun before 1 July 2018), s 39(2) (actions begun before 1975): machinery for actions already begun.
- The effect of an earlier judgment or dismissal of the same claim: not in the Act (the general law).
- s 39(1)'s exception for revival by acknowledgement or part payment: it works through s 29, for debts and estates, not
  damages for injury.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 5A(3), (5) "3 years [6 years] commencing on the date of discoverability" -- `the final day of ... years
  commencing on` -- the date of discoverability is the first day, so the last day is the day before the anniversary; from
  29 February into a year without one, 28 February -- the day excluded (the Acts Interpretation Act 1931 (Tas), not
  deposited), making the anniversary the last day. As in the claimant's baseline (its F1).
- **F2** s 39(1) "Nothing in this Act enables any action to be brought that was barred before the commencement of this
  Act", with s 5B and s 38A(2) -- `s 5B -- the action may be brought at any time`, `the time limit for the abuse claim` --
  s 39(1) applies: an action already barred before 1 January 1975 is not revived (`JUST FALSE`) -- s 5B ("may be brought at
  any time") and s 38A(2)(a) ("whether the cause of action accrued before, on or after the amendment day") read as
  overriding s 39(1) by implication (finding 1).
- **F3** s 38A(3) "more than 3 years before that day" -- `s 5A(5) -- a judge may give 6 years` -- before 1 July 2015 -- on
  or before 1 July 2015.
- **F4** "minor" (ss 5B, 26A), "child" (s 5C) -- `the 18th birthday for birth on`, `the last serial of` -- under 18; a
  minor's spell ends at the latest on the day before the 18th birthday; for a birth on 29 February the birthday is 28
  February in a common year -- 1 March.
- **F5** s 26A(3) "suspended for each period in which the person is a relevant person" -- `the last serial with` -- the
  suspended days are added to the last day (so a suspension containing a 29 February the new period lacks adds a day:
  1 June 2031, not 31 May 2031, in the cases); a spell that began before the date of discoverability counts from that date;
  one that begins on the last day counts, one that begins after it does not; an incapacity of 28 days or more is suspended
  from its first day, and one not yet ended is counted -- the period recounted in years from the end of the suspension; or
  only the days after the 28th; or the 28 days required to have passed.
- **F6** s 5A(3) "negligence, nuisance or breach of duty" -- `the action is one s 5A names` -- an action for an intentional
  wrong (assault, battery) is included, so abuse outside s 5B takes 3 years from discoverability -- an intentional trespass
  is not a "breach of duty" and takes s 4(1)(a), 6 years from accrual, with s 26's disability extension (finding 8).
- **F7** s 5B(1)(a) "personal injury to a person arising from or related to the ... abuse ... of the person" --
  `the action is one s 5B names` -- the injured person must be the person abused; a relative's own injury takes s 5A --
  "related to" read widely enough to take in those injured through the abuse of another (finding 4).
- **F8** s 5C(4) "so much of the agreement, and any other agreement ... relating to the settlement, is ... void to the
  extent to which it relates to the child abuse" -- `s 5C(4) -- what becomes of the agreement` -- an agreement solely about
  the child abuse is wholly void; one partly about it, void to that extent; one relating to the settlement but not to the
  child abuse, not void -- "so much of the agreement" read as voiding the settlement agreement only in part, whatever it
  covers.
- **F9** s 5C(5) "cannot seek to recover ... on the basis that the agreement is void to that extent" --
  `s 5C(5) -- the other party may recover what it paid` -- `JUST FALSE` on the void ground; `NOTHING` on any other ground,
  before an order, or for an agreement s 5C(4) does not make void -- the bar read as protecting every payment once the
  settlement is set aside.
- **F10** s 5C(6), (7) -- `s 5C(6), (7) -- the most the court may take into account` -- an agreement solely about the child
  abuse: the whole amount, even if it also states a part; one that expressly indicates a part: that part; otherwise half --
  the court free to find the part itself where (7) does not apply.
- **F11** s 5C(1) "settled before the day on which section 5B commenced" -- `s 5C(1), (2), (8) -- what I can do about the
  settlement` -- the day the settlement agreement was made, compared with 1 July 2018 (30 June in, 1 July out) -- the day
  the settlement was performed or approved.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions of s 5C(1), "must not be brought after" (s 5A(3)), "may not be granted"
(s 38A(3)), "Nothing in this Act enables" (s 39(1)), "cannot seek to recover" (s 5C(5)), "does not apply" (s 5C(8)), "If a
court orders" (s 5C(4)) and the "while" of s 26A(4) give `JUST FALSE`, or an enumerated "does not reach" / "not void"
answer in the text's words. `NOTHING` is answered for s 5B where the facts fall outside its grant (*limited by its own
wording*; s 5A then governs), where another Act decides (s 38, *points outside the text*), for s 5C(5) on another ground,
before an order, or for an agreement not made void (*limited by its own wording*), and for an action this encoding does
not answer.

## What the Act turns out to say

1. **s 39(1) may keep the oldest claims barred.** s 5B removes the limitation period "despite section 5A and section 26A",
   and s 38A(2) applies the 2018 amendments "whether or not a period of limitation under the Act, as in force before the
   amendment day" had expired. Neither names s 39(1): "Nothing in this Act enables any action to be brought that was barred
   before the commencement of this Act" (1 January 1975); and s 38A(2)(b) speaks only of periods under this Act, not under
   the Acts it repealed. Read as written, a survivor whose action was already out of time under the law before 1975 cannot
   rely on s 5B. Encoded as written (F2), so this encoding answers `JUST FALSE` where the claimant's baseline beside it,
   which does not encode s 39(1), answers "no limitation period". A lawyer should say which is right. Asserted.
2. **s 5B covers sexual abuse, serious physical abuse and psychological abuse arising from either -- nothing else.**
   Psychological abuse on its own, neglect, and physical abuse that is not "serious" take the ordinary 3 years (s 5A).
   "Serious" is not defined. Asserted.
3. **A child outside s 5B gets no infancy extension.** s 26(1A) takes every s 5A and s 5B cause of action out of s 26, so
   a child neglected or psychologically abused has only s 26A: the clock stops while he or she is not in the custody of a
   capable parent, which excludes the parent who is "the intended defendant" and one who "may be ... influenced" by him or
   her. A child in a capable parent's custody has the parent's knowledge counted as the child's (s 26A(5)), and the 3 years
   run. Asserted (a neglected child born 1 June 2010: last day 1 June 2031).
4. **s 5B is for injury to the person abused.** (1)(a) speaks of "personal injury to a person arising from or related to
   the ... abuse ... of the person", and (1)(b) of "the death of a person arising from or related to the ... abuse ... of
   the person". A parent's own psychiatric injury on learning of a child's abuse takes s 5A (F7). Asserted.
5. **s 5B and s 5C define the abuse differently.** s 5C(1)'s "child abuse ... does not include an act that is lawful at the
   time at which it occurs"; s 5B has no such words. An act lawful when done can found an action at any time under s 5B,
   but a settlement of it cannot be reopened under s 5C. Asserted.
6. **s 5C does not reach a claim settled within time.** A "previously settled relevant right of action" needs a settlement
   "after a limitation period ... had expired"; a survivor who settled in time before 1 July 2018 has no s 5C route, though
   the same claim unsettled would now have no limit. As in the claimant's baseline (its finding 8). Asserted.
7. **s 5C(3)(c) speaks of "the organisation to which the agreement relates",** but s 5C is not confined to organisations:
   a settlement with an individual abuser is a "relevant right of action" too, and for it factor (c) has nothing to bite on.
   "Organisation" is not defined in this Act (the Civil Liability Act 2002 s 49C defines it for Part 10C, excluding the
   State). With "interest of justice" in (2) but "interests of justice" in (3), and "a relevant court" in (2) but "the
   Court" in (3), the section reads as drafted with institutional settlements in mind. No effect on the answers.
8. **Whether abuse outside s 5B takes 3 years or 6 turns on "breach of duty".** Abuse is usually an intentional wrong.
   s 5A(3) reaches "negligence, nuisance or breach of duty"; if an intentional trespass is not a "breach of duty", s 4(1)(a)
   gives 6 years from accrual, and s 26 (disability, including infancy) applies, because s 26(1A) excludes only s 5A and
   s 5B causes of action. The encoding takes s 5A (F6), as the claimant's baseline does; the other reading would give a
   child abused outside s 5B 6 years from turning 18.
9. **"Minor" and "child" are not defined in this Act** (the Civil Liability Act 2002 s 49C defines "child" as under 18 for
   its Part 10C; the Age of Majority Act 1973 (Tas) is not deposited). Read as under 18 (F4).
10. **s 5C(4) voids related agreements "despite any Act, law or rule of law"** but keeps "a contract of insurance": a
    confidentiality deed or release falls with the settlement to the extent it relates to the child abuse; the
    defendant's insurance does not. Asserted.
11. **s 5C(7)'s half is a default, and (6) still leaves the offset to the court.** The "half of the total" applies only
    when the agreement neither relates solely to the abuse nor says how much does; the court then takes into account at
    most that much, and only if just and reasonable. Asserted (half of 100,001 is 50,000.50).

## Before this is worth relying on

- Check the text against the authorised version on legislation.tas.gov.au.
- A lawyer's view on findings 1, 2, 5 and 8 and forks F2, F5-F9; the Acts Interpretation Act 1931 (Tas) for F1 and the Age
  of Majority Act 1973 (Tas) for F4.
- Encode Part 10C of the Civil Liability Act 2002 (Tas) in that subject, so that the three parts of the reform can be read
  together.
- An independent test pass and a human gate.
