# Survival of Causes of Action Act 1940 (SA) -- baseline encoding, the claimant whose claim meets a death

> **Edition.** The text encoded is the register's current version of 8 February 2006, fetched from
> www.legislation.sa.gov.au on 6 November 2026 (the unauthorised RTF; the authorised version is the PDF). Unlike most
> South Australian texts in Commons it does **not** come from the Open Australian Legal Corpus (collected 10 March
> 2025), so that corpus's "may be out of date" warning does not apply; but the Act's own note warns that references to
> other legislation are not updated automatically. Check legislation.sa.gov.au before relying on it.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A small date module (`soca-dates.l4`, built-in date functions only, no daydate), a seat-neutral core
(`soca-core.l4`) that holds every rule, a seat layer (`soca-seat.l4`) that asks the questions and restates none of them,
and a cases file (`soca-cases.l4`) that asserts every question. Answers are named outcomes (enumerations), not
`MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used: where the text says no in its own words ("does not apply", "shall not
include", "No proceedings shall be maintainable ... unless") the outcome begins "no:"; where the text is silent it begins
"not covered:" or "s 3 does not exclude it", which follows the 2026-11-04 and 2026-11-05 rulings in substance. No
REFUSE, no `#ASSERT REFUSED`, no BECAUSE outside `LEST BREACH`. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use as advice.

**One regulative rule.** s 4(b)'s "proceedings are taken ... not later than six months after his executor or
administrator took out probate or letters of administration" is a `DEONTIC` (`PARTY the claimant MUST take proceedings
against the estate WITHIN <days to the last day> LEST BREACH ... BECAUSE ...`), run by `EVALTRACE` inside
`were proceedings taken within six months after the grant (s 4(b))`; on the stable `l4` a `CONSIDER` on an `EVALTRACE`
matches `FULFILLED` only, so anything else is read as late. The exported questions take plain dates, never a DEONTIC or
an EVENT.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Survival of Causes of Action Act 1940 (SA), version 8.2.2006 (the last amendment, the Dust Diseases Act
  2005 Sch 1 cl 3, to s 3(2)), deposited at `../../registers/source-bundle/survival-of-causes-of-action-act-1940.txt`
  (text sha256 aa250932...6faf per its `.meta.json`). The Current Titles list of 22 September 2026 gave the same
  version.
- **No regulations.** The Act sets its own numbers (the two six-month periods) and its own list (the Schedule of
  prescribed dust diseases), both encoded.
- **Not encoded here, linked by subject:** the dependants' own action for a death (Civil Liability Act 1936 Part 5,
  `../../../civil-liability-act-1936/encodings/baseline-2026-11/`), the apportionment rules s 6(2) applies (Law Reform
  (Contributory Negligence and Apportionment of Liability) Act 2001, deposited, not encoded), the limitation periods
  (Limitation of Actions Act 1936), and probate and administration (not deposited). Cross-subject IMPORT is not possible
  on the stable `l4`, so these are named, not called.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `soca-dates.l4` | 0 | 0 | 0 | 0 |
| `soca-core.l4` | 0 | 0 | 0 | 0 |
| `soca-seat.l4` | 0 | 0 | 0 | 0 |
| `soca-cases.l4` | 0 | 0 | 115 | 115 |

Negative control: with s 4(b)'s "six months after" the grant changed to seven, the cases failed exactly the 10 predicted
assertions (the five "by when" dates, the two direct day-after checks, and the three day-after cases of "Can I still sue
the estate"); the core was restored and rechecked (115 of 115).

Edges asserted: the last day of each six-month period and the day after; month ends (31 August less or plus six months
is 28 February, or 29 in a leap year); a year boundary; proceedings on and before the day of the grant (fork F2); each
limb of s 3(2) failing in turn; each limb of s 3(3) ((a) a Schedule disease, (b) another lung, pleura or peritoneum
condition, with and without dust); all 14 Schedule diseases; each limb of s 4 ((a) pending; (b) arising and taking);
both limbs of s 5; defamation in both directions.

## Seat

**The claimant (required): the person whose claim meets a death.** That is the executor or administrator (or a
beneficiary) of a person who died with a claim, the person with a dust-related condition who asks what their estate
would keep, and the injured person whose claim lies against someone who has died (`soca-seat.l4`, 9 questions). Every
question is one that person would ask: "Does the claim survive for the estate?", "Can the estate recover this kind of
damages?", "Will my estate keep those damages if I die of my dust disease?", "Does my claim survive against the estate?",
"Can I still sue the estate, and am I in time?", "By when must I take proceedings?", "How early may my claim have
arisen?", "Does the estate's claim affect my own claim for the death?", "Does the contributory negligence Act apply?".

No seat for a court. A second party seat (the executor answering a claim against the estate) would ask the same s 2(1)(b),
s 4 and s 5 questions with the same answers, so none is written.

The 2026-10-18 defaults:

- **The Act alone.** Followed: the Schedule is the Act's own; no regulations exist.
- **The actors the text names.** Followed: the deceased person, the estate, the executor or administrator, the
  dependants, the person liable.
- **Judgments answered conditionally.** Followed: whether a cause of action existed or was vested, whether the wrong
  caused the death, whether a condition is "attributable to dust", whether the person "dies as a result of that
  condition", whether the action was "finally determined" are asked as facts.
- **The Act's definitions worked out; borrowed terms asked.** Followed: s 3(3) "dust-related condition" and the
  Schedule are worked out; "cause of action", "tort", "defamation", "dependants", "probate or letters of administration"
  are borrowed and asked.
- **One case:** one cause of action and one death.
- **The Act's terms with plain glosses:** in the `@desc`s and comments.
- **Machinery out:** s 1, s 7.

## Scope

**In (the whole operative Act):** s 2 (all), s 3 (all, with the Schedule), s 4, s 5, s 6 (all).

**Out, and why:**

- s 1 (short title): machinery.
- s 7 (repeal of three English statutes as part of South Australian law): spent; nothing for the person to do or ask.
- The transitional provision of the Survival of Causes of Action (Dust-Related Conditions) Amendment Act 2001, s 5
  (printed in the legislative history): it extends s 3(2) to actions commenced before 11 October 2001 unless finalised,
  settled or withdrawn before then. It is not part of the Act and matters only to actions pending in 2001.
- The amount of any head of damages: the Act says only which heads the estate may recover; quantum is the general law.

## Forks (decided case by case, ruling of 2026-11-05)

Each is the provision, the function, the answer taken, and the other reading, for a reviewer to overrule.

- **F1** s 4(b), `moved by months` (soca-dates.l4): "six months before" and "six months after" are counted to the same
  day of the month, or the last day of a shorter month (31 August plus six months is 28 or 29 February). The other
  reading takes the Acts Interpretation Act 1915 (SA) rule for months (not deposited) or counts 182 days.
- **F2** s 4(b), `were proceedings taken within six months after the grant (s 4(b))`: proceedings taken on or before
  the day of the grant are "not later than six months after" it, so in time. The other reading requires them to be
  taken after the grant (there is no personal representative to sue before then).
- **F3** s 4(b) with s 5, `are proceedings against the estate maintainable (s 4)`: for a cause of action that s 5 deems
  to have subsisted before the death, "arose" is the day the damage was suffered (asked as a date), which falls on or
  after the death and so always meets the first limb. The other reading treats the deemed cause of action as arising
  just before death (the same result) or asks whether s 4(b)'s first limb reaches it at all.
- **F4** s 2(1)(a), `does it survive for the estate (s 2(1)(a), (2))`: no cause of action vested at death answers
  "not covered", not "no": the section says what survives, not that nothing else does.
- **F5** s 3(1)(d), `can the estate recover that head (s 3)`: funeral expenses, and a loss or gain consequent on the
  death, where the wrong did not cause the death answer "not covered" (the paragraph is a "where" that fails, but its
  effect is a rule of calculation, not a grant; the 2026-11-05 "where" ruling would give "no"). Reviewer to choose.
- **F6** s 3, same function: "other damages" (medical expenses or earnings lost before death, property) answer "s 3
  does not exclude it", never "yes": the Act limits damages, it does not grant them.
- **F7** s 3(2), `s 3(2) applies`: "commences an action" is read as the person who died commenced it in life; an action
  begun by the executor after death does not qualify. The other reading lets the estate's action count.
- **F8** s 3(2) and s 3(1)(a)(ii): s 3(2)'s "bodily and mental harm" is read as the same head as s 3(1)(a)(ii)'s
  "bodily or mental harm".
- **F9** s 6(1), `does the surviving claim affect the dependants' action (s 6(1))`: a person who is not a dependant gets
  "not covered", not "no": s 6(1) saves a right; it does not deny one.
- **F10** s 4, same function: a cause of action not in tort gets "s 4 does not apply" (s 4 says "a cause of action in
  tort"); limitation law still applies and is not encoded here.

## What the Act turns out to say (findings)

1. **A tort claim against a person who dies can be lost in six months.** Unless proceedings were already pending at the
   death, s 4 bars a tort claim against the estate if it arose more than six months before the death, however long the
   ordinary limitation period, and otherwise requires proceedings within six months after the grant. Asserted (the day
   before and the day of the earliest day; the last day and the day after).
2. **The six months after the grant never start without a grant.** If no executor or administrator takes out probate
   or letters of administration, s 4(b)'s period does not begin; the Act gives the claimant no step of its own to start
   it (that lies in probate law, not deposited). Encoded as "not yet". Asserted.
3. **s 3(2) does not restore the lost years.** The dust-related condition exception restores pain and suffering,
   bodily and mental harm, curtailment of expectation of life and exemplary damages, but not s 3(1)(a)(iv)'s lost
   earning capacity for the period the person would have survived. Asserted.
4. **s 3(1) has no paragraph (c).** It was deleted in 2003 by the Law Reform (Delay in Resolution of Personal Injury
   Claims) Act 2002; the lettering was left at (a), (b), (d). The deposited text does not say what (c) was.
5. **s 3(2) needs the action to have been commenced in life and the death to be from the condition.** A person with
   mesothelioma who dies before suing, or dies of something else, leaves an estate under the s 3(1) exclusions (F7).
   Asserted.
6. **s 4 has no counterpart for claims that survive for the estate.** The executor of a person who died with a claim
   meets no time condition in this Act (only the limitation law); the six-month conditions bind only claims against an
   estate, and only in tort.
7. **Old pronouns.** s 2 (substituted in 2003) says "his or her"; ss 4 and 5 still say "his" and "him". Read as
   gender-neutral.
8. **s 6(2) brings in the 2001 apportionment Act** for claims for and against an estate, but the Act says nothing of
   how a reduction for the deceased's own fault is applied to the s 3 heads; that is the other Act's question.

## Before relying on it

Check the register for a version later than 8 February 2006; have a lawyer review forks F1, F2, F5 and F7; encode the
Law Reform (Contributory Negligence and Apportionment of Liability) Act 2001 and link it; run an independent test pass.
