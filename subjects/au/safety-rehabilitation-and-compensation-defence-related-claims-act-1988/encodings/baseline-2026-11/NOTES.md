# Safety, Rehabilitation and Compensation (Defence-related Claims) Act 1988 (Cth) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the rulings
on negatives of 2026-11-04 and 2026-11-05 (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

This is the first encoding of the Act; nothing existing was touched. No ledger line asks for it (it is a claims-law
baseline, by subject: workplace injury and disease), and no scenario life reaches it, so every case is hypothetical.

Three files:

- `drca-dates.l4` -- the dates the Act fixes (1 July 2026, 1 July 2004, 1 December 1988) and the day arithmetic. The only
  module that imports `daydate`.
- `drca-claimant.l4` -- the rules and the 28 exported questions, each with `@export` and a `@desc` on every input, grouped
  under `§§` headings in the Act's order. Three regulative rules (s 26, ss 46/47, s 48(2)) are run by `EVALTRACE` inside
  questions that take only plain facts (dates and yes/no).
- `drca-cases.l4` -- the cases.

The focus asked for is the provisions a claimant meets. This compilation is the Act as cut down by the Veterans'
Entitlements, Treatment and Support (Simplification and Harmonisation) Act 2025 (Act No. 17, 2025): weekly incapacity
payments (ss 19 to 23), rehabilitation (Part III), redemption (s 30) and most of Part VI are gone, and s 14AA closes the
Act to new claims from 1 July 2026. What remains is encoded whole for the claimant except as listed under Scope.

## Edition

- **Act:** Safety, Rehabilitation and Compensation (Defence-related Claims) Act 1988, No. 156, 1988, Compilation No. 20
  (compilation date 1 July 2026, includes amendments up to Act No. 17, 2025, register id C2026C00265), deposited at
  `../../registers/source-bundle/C1988A00156.txt` (text sha256 `c84a0c12a8d3575c7db85e4faedde2b9c0c5b492ed471da1965b672d1900355b`
  per its `.meta.json`), retrieved 13 October 2026 from the Federal Register of Legislation.
- **Formulas:** s 27(2) and s 49(4) from the sidecar `../../registers/source-bundle/C1988A00156.formulas.md` (transcribed
  2026-10-24 from the Word rendering of the same compilation).
- **Numbers set elsewhere, not deposited:** the CPI and Wage Price Index numbers that index the dollar amounts (ss 13,
  13AA), so each indexed amount is an input (enter the printed figure to use it); the approved Guide (s 28), so the
  degrees of impairment and non-economic loss are inputs; the legislative rules defining "catastrophic injury" (s 4(1));
  the regulations prescribing a cancer for item 13 of the s 7(8) table; the Minister's interest rate (s 26(3)), so the
  s 26 answer is in days; the value of a penalty unit (Crimes Act 1914), so penalties are in penalty units; the acute
  support package instrument (s 41B).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. Each deadline period (s 26(1) 30 days, ss 46(1), 47(1) 7 days, s 48(2) 28 days)
is stated once as a named number, and both the regulative rule (WITHIN) and the last-day question read it from there. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; one
deliberately wrong assertion was run once in a scratch copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `drca-dates.l4` | 0 | 0 | 0 | 0 |
| `drca-claimant.l4` | 0 | 0 | 0 | 0 |
| `drca-cases.l4` | 0 | 0 | 183 | 183 |

Every exported question has cases, with the edges: 30 June and 1 July 2026 (s 14AA); each service period against each
kind of claim, the property exception to the span rule, and each limb of s 4AA(4) and s 6A(2A); s 5(6) and both
exceptions; each qualifying period of the firefighter table at and just under the period; ages 15, 16, 24 and 25 for a
prescribed child; 9%, 9.99% and 10% (and 4% and 5% for hearing) under s 24; increases of 9 and 10 points (4 and 5 for
hearing) under s 25; the 30th and 31st day and a year end under s 26; the 7th and 8th day under ss 46, 47; the 28th and
29th under s 48(2); half the cost under, at and over the $200 cap under s 29; 24 and 25 months, ages 64 and 65, and 12 and
13 months under s 41B, for a former spouse of a member who has died as well as one whose member is living; the s 53(2) notice of the accident for a s 15 property claim, late and excused; equal and unequal amounts in ss 48, 49, 119. Every expected value was worked by hand from the text
before the run.

## Seat

**The claimant** (`drca-claimant.l4`): the member or former member of the Defence Force who suffered the injury, disease
or loss of an aid, and, where the member has died, the dependant (or the person seeking an acute support package).
"Can I still claim?", "Does the Act cover my service?", "Is it an injury?", "Is my cancer presumed to come from
firefighting?", "Is the Commonwealth liable?", "What do I get for my aid?", "Will my medical costs be paid?", "Was I a
dependant?", "What lump sum is payable on the death?", "What is paid a week for me as a child?", "How much permanent
impairment compensation?", "Does an increase count?", "Is interest payable, and from when?", "How much for non-economic
loss?", "What for household services, and for attendant care?", "Do I meet the Act's criteria for an acute support
package?", "Can I sue?", "By when must I tell the Commission about my damages claim, and did I?", "What must I repay
after damages?", "Can I still be paid after damages?", "What must I pay as a dependant who did not claim?", "Does my
notice and claim count?", "By when must I give the information asked for?", "What is left after State compensation?".

No seat for the Military Rehabilitation and Compensation Commission, the Commonwealth, the Board or the Tribunal: their
determinations and judgments are inputs, answered conditionally. No second seat: the Act puts no duties on another party
that a person would ask about from the other side (the Commonwealth's s 26 duty to pay is encoded from the claimant's side).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; none of those instruments is deposited, so the
  numbers are inputs (Edition).
- **The actors the text names:** the employee (a member of the Defence Force, s 5), dependants, the Commission, the
  Commonwealth, a third party, a State or foreign compensation scheme.
- **Judgments left to others, answered conditionally:** "significant degree" (s 5B), reasonable administrative action
  (s 5A), abnormal risk (s 6(3)), serious and wilful misconduct and serious and permanent impairment (s 14), firefighting a
  "not insubstantial portion" (s 7(9)), reasonable treatment (s 16), exceptional circumstances (s 144A), the degrees under
  the approved Guide (ss 24, 27), services "reasonably required" (s 29), crisis and parenting (s 41B), a late notice
  excused (s 53(3)).
- **The Act's own definitions worked out from facts:** dependant, prescribed child and the s 4(5) deeming (s 4), injury
  and disease (ss 5A, 5B, 6), the firefighter presumption (s 7(8), (9)), the coverage rule (s 4AA). Borrowed terms asked
  as facts: which VEA Part provides a pension (s 5(6)-(8)), whether CTPA s 8 applies (s 4AA(4)(c)), catastrophic injury,
  State workers' compensation and a "specified law" (ss 118, 119).
- **One case:** one member, one injury (or one death).
- **The Act's terms**, quoted in the comment above each rule.
- **Machinery out:** ss 1 to 3A, 13A, 109A, 109, 121B to 122A, Part XI except ss 144A and 144B, the indexation
  computations (ss 13, 13AA).

## Scope

**In:** s 4(1) (dependant, prescribed child, date of commencement), s 4(4), (5), (13); s 4AA(1) to (5); s 5(1), (6) to
(8); s 5A; s 5B; s 6(1), (1C), (3); s 6A(2), (2A) (for s 4AA(4)); s 7(7) to (10); s 14AA; s 14; s 15(1), (3); s 16(1),
(2), (4); s 17(2) to (6); s 24(1), (3) to (9); s 25(4), (5); s 26(1), (2), (4); s 27(1), (2); s 29(1), (3), (5); s 29A(1),
(3); s 41B(2), (5), (5A), (6); s 44(1), (3), (4); s 45(1) to (4); ss 46(1), 47(1); s 48(2) to (7); s 49; s 53(1) to (3);
s 54(1) to (3), (5); s 58(1), (3); s 118(1), (6); s 119(2), (6), (7); s 144A(1), (2); s 144B(5).

**Out, and why:**

- **s 7(1) to (6)** (diseases listed by the Minister, the incidence presumptions, the day a disease is sustained): turn on
  instruments and statistics not deposited; s 7(8) is in.
- **ss 8, 9** (normal weekly earnings): since 1 July 2026 they serve only Part X Division 3 (the 1971-Act former
  employees), which is out.
- **s 10 to 12, 13, 13AA** (recovery date, liability, indexation): definitions used inside other answers (s 10) or
  computations whose results are inputs.
- **s 16(3), (5); s 17(7) to (10); s 25(1) to (3); s 26(3); s 28; s 29(2), (4), (6), (7); s 29A(2), (4) to (6)**: matters
  the Commission weighs, payee and discharge rules, and the Guide's making; s 26(3)'s rate is not deposited.
- **s 41B(1), (7), (8)**: the instrument's content (not deposited).
- **s 43** (asking for payments to stop) and **s 52** (election between this Act and an award): simple elections, left for
  a later pass; **s 50, 51, 52A** (the Commission's own claims and recovery from third parties); **s 55, 56, 57, 59**.
- **Part VI** (ss 60 to 62): review is under Part 4 of Chapter 8 of the MRCA (not deposited here).
- **Part IX** (ss 109 to 115): machinery, assignment, set-off, death of a beneficiary, and VEA overpayments.
- **Part X** (ss 123 to 137): injuries before 1 December 1988 turn on the 1912, 1930 and 1971 Acts (not deposited); the
  Division 3 former employees were receiving 1971-Act weekly payments before 1 December 1988 and their amounts refer to
  repealed ss 19, 20 and 30 "as in force immediately before" 1 July 2026 (not in the deposit). The coverage question
  answers `not covered` for service before 1 December 1988.
- **Part XI** except ss 144A and 144B(5): the Commission's functions and administration.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here. Most questions answer with a named choice or an amount rather than `MAYBE`; a "no" choice or an
amount of 0 stands for `JUST FALSE`, and a `not covered` choice for `NOTHING`.

- **No (`JUST FALSE`):** s 14AA "may not be made"; s 4AA's "if" conditions and "but not before and on or after"; s 5(6)
  "does not apply"; the "means" definitions of injury, disease, dependant and prescribed child; s 7(7) "shall not be
  taken"; the s 7(8) "if" (presumption not applied); s 14(2), (3) "not payable"; s 15(1) "if" and (3); s 16(1) "being
  treatment that it was reasonable"; s 144A(1) "is not liable"; s 144B(5) "is not entitled"; s 17(2), (6); s 24(7), (7A);
  s 25(4), (5) "unless"; s 29(5) "not liable ... unless"; s 41B(2) "not eligible ... unless"; s 44(1) "does not lie"; s
  45(1) "at any time before"; s 48(4) "not payable"; s 53(1) "does not apply ... unless"; s 54(1), (3); s 118(1).
- **`NOTHING`:** service before 1 December 1988 (`not covered`: Part X points outside the sources); item 13 of the s 7(8)
  table (prescribed, not deposited); meeting the Act's acute support package criteria (necessary, not sufficient: the
  instrument decides).

### Forks

- **F1** s 4AA, `ss 4AA, 5 -- does the Act cover it`: service before 1 December 1988 answers `not covered` (Part X); other
  reading: "no", since s 4AA's "if" fails.
- **F2** s 5(6) to (8), same function: the pension provision is asked as one choice (none, VEA Part II operational after
  the Military Compensation Act 1994, VEA Part IV, other); other reading: ask (7)'s two limbs separately.
- **F3** s 4AA(4) "in accordance with section 6A", `s 4AA(4) -- treatment injury`: s 6A(2A) is applied as taking the
  injury out of the Act; other reading: s 6A(2A) only removes the deeming, leaving s 5A to be met otherwise.
- **F4** s 6(3), `s 6 -- treated as arising ...`: the abnormal-risk exclusion is applied to the places in s 6(1)(b), (c),
  (e) to (i) and recesses, not to violence (a) or directed travel (d); other reading: "a place referred to in that
  subsection" reaches the travel paragraphs too.
- **F5** s 29(1), `s 29(1) -- the floor`: where half the weekly cost exceeds $200, the floor is cut to the cap; other
  reading: the 50% floor prevails and the $200 is exceeded.
- **F6** s 25(4), (5), `s 25(4), (5) -- the increase counts`: "10%" and "5%" are read as percentage points of impairment;
  other reading: a 10% relative increase.
- **F7** s 41B(5)(c), (5A)(c), (6)(b)(i), `s 41B -- criteria met`: "no more than 2 years" is 24 whole months or fewer, and
  "within the previous 12 months" 12 whole months or fewer; other reading: count in days.
- **F8** ss 46(1), 47(1), `ss 46, 47 -- notified in time`: only the 7-day outer limit is tested; "as soon as practicable"
  could be earlier and is not asked.
- **F9** s 15, `s 15 -- compensation for my aid or appliance`: an accident that also injures answers 0 under s 15; other
  reading: none, but the replacement may then be medical treatment under s 16 (s 4(1) "medical treatment" (f)).
- **F10** s 26(4), `s 26 -- days of interest`: a review application answers 0 days ("does not apply"); other reading: no
  answer (`NOTHING`), since interest may then follow the review.
- **F11** s 41B(6), `s 41B -- criteria met`: a spouse at the death may also meet (6) ("was the spouse of an employee");
  other reading: (6) is only for a spouse whose relationship ended in the member's life. A former spouse of a member who has since died is offered (6) as its own choice, not a fork: (6) says
  "was the spouse of an employee", and s 41B(1)(b) reaches a related person of a deceased employee. (5A)(b)'s "another
  person who was the spouse of an employee at any time before the employee's death" covers the parent of the spouse at
  the death too, so that choice is worded that way.
- **F12** s 4(5), `s 4 -- am I a dependant`: the deeming overrides the stated dependence (a spouse living with the member
  who was only partly dependent is wholly dependent); other reading: none.
- **F13** ss 53, 54, `ss 53, 54 -- have I made a claim that counts`: the first failing step is reported (notice, form,
  date, certificate); other reading: report all.
- **F14** s 118(1), `ss 118, 119 -- DRCA compensation still payable`: any State workers' compensation recovered answers 0
  whatever its amount ("compensation is not payable"); s 118(6) is read as covering a foreign scheme the same way.

## What the Act turns out to say

1. **No new claims from 1 July 2026.** s 14AA bars any claim under Part V on or after "the date of commencement", which s
   4(1) defines as 1 July 2026; Note 1 sends such claims to the MRCA, and Note 2 points to s 88 of the CTPA (not
   deposited) for claims pending on that day. The Act now only carries claims already made. Asserted (30 June and 1 July
   2026, and through ss 53, 54).
2. **Weekly incapacity payments are no longer in this Act.** Division 3 of Part II (ss 19 to 23), Part III and s 30 were
   repealed by Act No. 17, 2025; Part X still calls on ss 19, 20 and 30 "as in force immediately before the commencement
   of Schedule 1" of that Act (ss 132A, 133, 137(5)), text this deposit does not hold. Not asserted.
3. **Spanning service is excluded for injuries and diseases, but not for property.** s 4AA(1)(b)(ii) and (2)(b)(ii) add
   "but not before and on or after, the MRCA commencement date", and (5) makes service across 1 July 2004 (or in separate
   periods either side) "before, and on or after"; s 4AA(3) for property has no such words. Asserted.
4. **The s 29(1) limits can collide.** Household services compensation is "not less than 50% of the amount per week paid
   ... nor more than $200": above $400 a week both cannot hold, and the cap is $200 even where the services cost less
   (unlike s 29(3), which is the lesser of $200 and the cost). Encoded with the cap prevailing (F5). Asserted.
5. **Indexation is uneven.** s 13 (CPI) indexes the amounts in ss 24(9), 27(2), 29(1), (3) and 137(1); s 13AA (Wage Price
   Index) those in s 17(3) to (5). The $110,000 cap on common law damages for non-economic loss (s 45(4)) is in neither
   list, so it is fixed. Asserted (110,000 in `ss 44, 45 -- can I sue`).
6. **Thresholds.** No permanent impairment compensation below 10% (5% binaural for hearing), with no threshold for a
   finger, toe, taste or smell (s 24(7), (7A), (8)); later increases count only at 10 (5 for hearing) points or more
   (s 25(4), (5), read as points, F6). Non-economic loss is ($15,000 x A) + ($15,000 x B), so at most $30,000 printed
   (s 27(2)). Asserted at each edge.
7. **Probable drafting error in s 137(1)(b):** "the amount of those payments if $62.99 per week or less" -- "if" for "is".
   The meaning is plain; s 137 is out of scope. Not asserted.
8. **The firefighter presumption is Commonwealth-only and cumulative.** Periods add up (s 7(9)(b)), only firefighting for
   the Commonwealth counts ((9)(c)), and the presumption yields to proof to the contrary. Asserted at 5, 10 and 15 years
   and just under.
9. **Medical costs are often paid under other Acts instead.** A member eligible for treatment under MRCA ss 281, 282, the
   VEA, the Special Access Act 2019 or the British Nuclear Tests Act 2006 gets no s 16(1) compensation unless the
   Commission finds exceptional circumstances (s 144A); and where s 144B moves the injury's treatment to the MRCA or VEA,
   s 16(1) stops (s 144B(5)). Asserted.
10. **Strict-liability notices.** A claim for damages must be notified to the Commission within 7 days of becoming aware
    of it (5 penalty units, ss 46, 47), and damages recovered within 28 days (10 penalty units, s 48(2)); repayment is the
    lesser of compensation paid and damages, except after an action for non-economic loss (s 48(3), (4A)). Asserted.

## Before relying on it

- The CTPA (s 88 and Part 3) and the MRCA (Chapter 8 Part 4, s 280A) to say what happens to claims pending on 1 July 2026
  and how review works now.
- The current indexed amounts (ABS CPI and WPI numbers) and the approved Guide.
- The legislative rules on catastrophic injury, the s 7 instruments and regulations, the Minister's s 26(3) interest rate,
  the s 41B instrument.
- An independent test pass and a lawyer's review of the forks, especially F3, F5 and F11.
- Part X, ss 43, 50 to 52A, 55 to 57 if former 1971-Act claimants or common law recovery matter.
