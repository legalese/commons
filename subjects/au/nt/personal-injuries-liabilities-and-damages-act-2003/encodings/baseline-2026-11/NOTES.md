# Personal Injuries (Liabilities and Damages) Act 2003 (NT) — baseline encoding, the claimant's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18, the rulings on negatives of 2026-11-04 and 2026-11-05, and the `writing-l4-rules` skill (with `references/regulative.md`).
There is no REFUSE in it; a question that reaches a gap answers `not covered` with a reason, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the Acts behind personal injury, compensation and other civil claims, with the focus "the provisions a claimant meets". The Act is of moderate size (about 80 sections), so the whole operative Act is encoded from the claimant's seat, and the machinery, purposes and the court's procedural powers are left out (listed below). There was no earlier encoding of this Act to keep. No ledger entry was open for it.

Three modules:

- `pild-dates.l4` — the date arithmetic, the only module that imports `daydate`.
- `pild-claimant.l4` — the rules and the 35 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order: does the Act apply (s 4); a death claim (s 5 — arises only on a death); can the person who hurt me escape liability (ss 7, 7A, 8, 9, 10); can I use their apology (ss 12, 13 — arises only if someone apologised); contributory negligence and intoxication (ss 14–17); child abuse in an institution (Part 3A — arises only for a person abused as a child): what is child abuse, what is an institution, who is associated with it, the reversed onus (ss 17E, 17F), vicarious liability (s 17G), the proper respondent and associated trusts (ss 17H–17M), successors and unincorporated institutions (ss 17P–17R); how much can I get (Part 4): aggravated and exemplary damages, the earnings cap, future loss, free care, non-pecuniary loss, interest, structured settlements; and Part 4A — arises only for a person assaulted, battered or falsely imprisoned in custody, or for that offender's victim.
- `pild-cases-claimant.l4` — 215 assertions and 2 traces.

**Regulative rules.** `s 17K(3) -- the institution must identify its associated trusts within 28 days`: `PARTY the institution MUST identify its associated trusts and give the court information on their financial capacity WITHIN the s 17K(3) period in days HENCE FULFILLED LEST BREACH BY the institution BECAUSE ...`, the period (28) named once and used by both the rule and the date question. `s 32J(5) -- the public entity must give me the details within 28 days`: the same shape for the public entity defendant, with `the s 32J(5) period in days` (28). Both are duties owed in the claimant's (or victim's) proceeding, with deadlines counted in days from the application or request (day 0). The exported questions take plain facts (dates) and give the last day; the rules are asserted in the case file through `CONSIDER EVALTRACE ... WHEN FULFILLED` (the action on day 28: fulfilled; on day 29: not), and one breach of each is `#TRACE`d with an `-- expect:` line.

## Edition

Reprint **REPP078**, as in force at 25 March 2024, from the Northern Territory Legislation register (retrieved 6 November 2026), as deposited at `../../registers/source-bundle/Personal-Injuries-Liabilities-and-Damages-Act-2003-NT-current-reprint-REPP078.txt`. The register showed it as the current reprint on that day.

Dates taken from the endnotes (List of legislation): the Act commenced on **1 May 2003**; the Amendment Act 2010 (which inserted s 7A and s 36) on **15 December 2010**. The Amendment Act 2022 commenced "pt 2: 3 June 2022; pt 3: 30 September 2022; rem: 1 January 2023"; the endnotes do not say which Part of it inserted Part 4A Divisions 1–3. **s 32B is taken to have commenced on 3 June 2022** (inferred from the numbering of the amending sections: see finding 8). **Part 3A is taken to have commenced on 30 September 2022**, by the same inference. Check both against the Amendment Act 2022 (not deposited) before relying on the s 32B(5) edge or the Part 3A edge (finding 6).

**Regulations.** No regulations under the Act are deposited. Where the Act defers to them the encoding uses the Act's own default or asks a question of fact, and says so: the s 22 discount rate (the Act's 5%), the s 30 interest rate (the Act's default, the 10-year bond rate), the prescribed guides for impairment (s 18; the degree of impairment is an input), the psychological injuries excluded from "impairment" (s 18), the volunteer remuneration amount and the extra community-work purposes (s 7(7): `not covered`), extra grocery products (s 7A(4)(d): `not covered`), extra associated individuals (s 17C(1)(e): `not covered`), and any further excluded claims (s 4(4): not asked; a regulation could exclude a claim this encoding says the Act reaches).

**Monetary units.** ss 27 and 32E state amounts in monetary units. Their dollar value is fixed outside this Act (under the Revenue Units Act 2009, not deposited), so those answers are given in monetary units.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `pild-dates.l4`, `pild-claimant.l4` | `pild-cases-claimant.l4` | 215 written, 215 satisfied; 2 traces breach as their `-- expect:` lines say |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read; two deliberately wrong assertions in a scratch file showed as `assertion failed` (re-run on the fix of 2026-11-07). Every expected value was written by hand from the text. Edges asserted: an incident on 1 May 2003 and 30 April 2003 (ss 4(2), 5(2), 17E, 17G); abuse on 30 and 29 September 2022 (the Part 3A edge for ss 17E, 17G, finding 6); a donation on 15 and 14 December 2010 (s 36); an incident on 3 and 2 June 2022 (s 32B(5)); a passenger aged 16 and 15 (s 15); a court percentage of 20, 25, 30 and 100 (s 17); a child of 17 and an adult of 18 (s 3); the 120th and 121st day after a proceeding was commenced (s 17K(1)(b)); the 28th and 29th day (ss 17K(3), 32J(5)); earnings at 3 times average weekly earnings and $1 over (s 20); 6 hours and 5.5 hours, 6 months and 5.5 months, 39, 40 and 70 hours (s 23); every step of the s 27 Table, 4.9%, 9.5%, 10.5%, 14.5%, 15%, 84%, 84.5%, 85% and 100%; assessments on 1 March, 31 August, 1 September, 31 December, 2 January and 28 February (s 30); every s 32E band, 0.5, 1, 1.5, 2, 2.5, 14, 15, 16, 29, 30, 59, 60 and 100 days; a series of wrongs under, at and over 15 000 units; debts larger than the award (s 32G); 12 months after 29 February 2024 and after 31 March 2026 (s 32H).

## Seat

**The injured person who brings the claim** (the claimant): "I was hurt in the Territory. Does this Act cover my claim? Can the person who hurt me escape liability? Will my damages be cut because I had been drinking? How much can I get for pain and suffering, and for the care my family gives me?" For Part 3A, the person abused as a child while in an institution's care. For Part 4A, two individuals the Part is applied to, both claimants: the person in custody who sues for assault, battery or false imprisonment (whose damages the Part caps and holds on trust), and the victim who sues that offender (for whom the Part reopens the limitation period and the trust money). No seat is given to the respondent, the institution, the public entity defendant, the Public Trustee or the court; what the Act lets them do appears as what it means for the claimant.

The 2026-10-18 defaults:

- **The Act alone.** The Acts it names (the Motor Accidents (Compensation) Act 1979, the Return to Work Act 1986, the Compensation (Fatal Injuries) Act 1974, the Limitation Act 1981, the Correctional Services Act 2014, the Youth Justice Act 2005, the Victims of Crime Assistance Act 2006, the Fines and Penalties (Recovery) Act 2001, the Food Act 2004, the Care and Protection of Children Act 2007, the Australian Consumer Law) are named, not encoded; what they decide is asked as a fact. Average weekly earnings (s 18) is an ABS figure, asked as an input.
- **The actors the text names:** the injured person, the claimant, the respondent, the volunteer and community organisation, the donor, the good Samaritan, the occupier or owner, the institution, the proper respondent, the associated trust and its trustee, the successor institution, the current and former office holder, the offender, the victim, the public entity defendant, the Public Trustee, the court.
- **Judgments handed to others are answered conditionally:** every "if the court is satisfied", "court determines" and "court finds" is an input (s 10(1), (2); ss 14(2), 15(2) as what the claimant establishes; s 17 percentage; ss 17E(2), 17F(2) answered "yes, unless the institution proves ..."; s 17G placement; ss 17J, 17L; s 17P "substantially the same"; ss 21, 23(1), 27, 30(1)). Good faith, recklessness, intoxication, authority are asked as facts.
- **The Act's own definitions are worked out from facts:** "child", "child abuse" and the s 3(2) carve-out; "intoxicated" with s 16; "community organisation", "community work", "volunteer" (s 7(7)); "grocery product" and "person who donates" (s 7A(4)); "good Samaritan" (s 8(4)); "expression of regret" (s 12); "institution" (s 17B); "individual associated with an institution" (s 17C); "individual akin to an employee" (s 17G(5)); "associated trust" (s 17K(4)); "gratuitous services" (s 18); "civil wrong", "victim claim" (s 32A); "series of related civil wrongs" (s 32E(4)). "Offender" (Correctional Services Act 2014 s 5), "detainee", "public entity defendant" (s 32C, a list of public bodies) and "offence punishable by imprisonment" are asked as facts.
- **One case:** one claim for one injury (or, for Part 4A, one civil wrong or one award).
- **The Act's own terms**, quoted in the comment above each rule, and glossed in the `@desc` lines.
- **Machinery out:** listed below.

## Scope

**In:** s 3 (as the definitions are used); s 4; s 5; s 7(1)–(4), (6), (7); s 7A with s 36; s 8; s 9; s 10; ss 12, 13 (and s 35(2)); ss 14–17; Part 3A: ss 17B, 17C, 17D (in the answers), 17E, 17F (with s 17F(5), in the answer), 17G, 17H, 17J, 17K, 17L, 17M(3), 17P, 17Q(1), 17R; Part 4: ss 18–23, 25, 27, 29–32 (and s 35(3)); Part 4A: ss 32A–32H, 32J(4), (5), 32K (in the victim's answer), 32M, 32P.

**Out, and why:**
- ss 1, 2, 6 (machinery); s 11 and s 24 (purposes); Part 5 (regulations); Part 6 save s 35(2), (3), and Part 7 save s 36 (transitional).
- s 7(5) and s 35(1) — indemnity or contribution agreements between a volunteer and the organisation: their matter, not the claimant's.
- s 17A — definitions, used in words.
- ss 17E(3), 17F(3), 17G(2) — the matters a court may or must weigh in deciding reasonable steps or the placement: folded into the court's finding (an input). ss 17E(4), 17F(4) (each of several institutions equally) and ss 17E(5), 17F(7), 17G(4) (awards under the other section taken into account) are stated in the answers.
- s 17F(6) (leave to attend a closed court), ss 17J(3), 17L(3), 17M(1), (2), (4), 17N (the trustee's powers and the Corporations Act displacement), s 17Q(2)–(4), s 17S — the court's and trustees' procedural powers.
- s 26 — the evidence of impairment (a medical practitioner's assessment under the prescribed guides): the degree the court determines is an input.
- s 32J(1)–(3), (6), (7) — the public entity's duty to notify victims (stated in the victim's answers; the victim's own right is s 32J(4), (5), encoded); s 32K(3)–(6) (in the victim's answer); s 32L (interest and fees on trust money); s 32N (immunity of officials).

## Fork register (questions with no convention, decided case by case)

The 2026-11-04 and 2026-11-05 rulings were followed in choosing between "no" and `not covered`; each line gives the provision, the function, the answer taken, and the other reading.

1. s 4(2), s 5(2)(a), s 36, s 32B(5) "after the commencement" / "before the commencement": an incident (death, donation) on the commencement day counts as after it (an Act commences at the start of its day). `Does this Act apply question`, `Does Part 4 apply to a death claim question`, `Is the donor liable question`, `Does Part 4A apply to my claim question`. Other reading: the commencement day is excluded.
2. s 4(3)(c) dust-related condition: a "means" definition; the two limbs are asked as one choice. `Does this Act apply question`.
3. s 7(7) "community organisation means" a religious body, a body corporate or an Agency: another body (an unincorporated club) answers "no protection" (a "means" definition). `Who is liable for the volunteer question`.
4. s 7(7) work for an unlisted purpose, and a paid volunteer: `not covered` (each list is closed only by regulations that are not deposited). Other reading: "no", taking the Regulations to prescribe nothing.
5. s 7A(4) "does not include a person who distributes": "no protection". `Is the donor liable question`. s 7A(4)(d) another product: `not covered`.
6. s 7A(2)(c), (d) when nothing needed handling or had a time limit: the condition does not arise, so the donor is protected.
7. s 8(4) "good Samaritan means": a helper who expected payment, or a person not apparently in need, answers "no protection".
8. s 12 "an expression of regret is": read as "means"; a statement acknowledging fault is not one, so s 13 does not keep it out (the answer does not say it is admissible). `Can I use the apology question`.
9. ss 14, 15: a presumption not rebutted is contributory negligence "established under this Division" for s 17. Other reading: s 17 needs a finding beyond the presumption.
10. ss 14, 15 with s 16: a court's alcohol finding makes the person intoxicated, whether or not the intoxication input is given.
11. s 17 "25% or a greater percentage": a court percentage below 25 is lifted to 25; one above 100 is held at 100. `My damages after the section 17 reduction question`.
12. s 3 "child abuse" (c), psychological abuse arising from (b): where the physical conduct was lawful at the time (s 3(2)), the psychological abuse arising from it is not child abuse either (it does not arise from "abuse specified in paragraph (b)"). `Is it child abuse question`. Other reading: s 3(2) is limited to paragraph (b), and the psychological abuse still counts.
13. s 17B(1) "while exercising care, supervision or authority": outside that time, "no" (a "while" condition).
14. s 17C(1) "includes", and s 17C(1)(e) prescribed individuals: another connection answers `not covered`.
15. ss 17E(2), 17F(2) "if the plaintiff proves ...": abuse by anyone else, or outside the institution's care, answers "no" for the reversed onus, with the ordinary law of negligence named.
16. s 17G(5) "individual akin to an employee ... is an individual who": read as "means"; a s 78 placement carer and an independent contractor answer "section 17G does not make the institution liable", with s 17G(3) (the general law) named.
17. s 17K(1)(b) "at least 120 days from the day the proceeding was commenced have passed": the day of commencement is not counted, so the earliest day to apply is the 121st day after it (a proceeding commenced 1 January 2026: from 2 May 2026). Other reading: the 120th day.
18. s 17K(1)(a)(ii) while the court has not yet decided a nomination: "not yet".
19. s 17K(4) "in any of the following circumstances": closed; none met answers "no".
20. s 17P(3) "without limiting subsection (2)": a succession it does not list answers "yes, if the court finds ... substantially the same".
21. s 21(2) "adjust ... by reference to the percentage possibility that the events might have occurred regardless": the amount is reduced by that percentage.
22. s 23(3), (4): the limit is per week of care: average weekly earnings for 40 hours or more, and one-fortieth of it per hour below 40.
23. s 27 a degree between the Table's whole percentages (10.5%, 14.5%) or between 84% and 85%: `not covered`. Other reading: round to the nearest whole percentage (the prescribed guides may only ever give whole numbers).
24. s 32E(1)(c) "for each day during which the false imprisonment continues": a part day counts as a day, so 1.5 days is 2 days. Other reading: whole days only.
25. s 32E(1) asked for a wrong other than assault, battery or false imprisonment: `not covered`, naming ss 32A, 32B(4) (Part 4A sets no maximum for it). `The most for one wrong question`. Other reading: "no maximum" as an answer. (Added on the fix of 2026-11-07; the first version answered 0, which read as a cap of zero.)

Also decided without a fork of the conventions: s 30(2)'s publication month for an assessment in January or February is July of the year before (the "period from 1 September of that year until the last day of February of the following year"); s 32H(2)(a) "the day 12 months after" is the same date 12 months on, clamped to the month's end (29 February 2024 gives 28 February 2025); s 32G withholding cannot exceed the award.

## What the Act turns out to say

1. **A volunteer of an unincorporated club is not protected.** s 7(7) limits "community organisation" to a religious body, a body corporate, or a Territory Agency or department. A volunteer for an unincorporated sports club or community group stays personally liable, and the club does not take the liability over. Asserted.
2. **s 4(3) has no paragraph (d).** The list runs (a), (b), (c), (e); a paragraph was omitted by an amendment and not renumbered. Nothing turns on it.
3. **Part 3 has no Divisions, but ss 16 and 17 speak of "this Division".** s 16 makes an alcohol finding conclusive "for the purposes of this Division", and s 17 applies "if contributory negligence is established under this Division". Part 3 (ss 14–17) is not divided. Read as Part 3; if read literally, ss 16 and 17 would have nothing to apply to. (s 16 also says "a Court" with a capital C, unlike the rest of the Act.)
4. **Non-pecuniary damages are fixed, not capped.** s 27(3) says the court "must award the following amount": once the degree of impairment is determined, the amount follows exactly (13 600 units for anything from 5% to under 10%, a Table for 10%–14%, the percentage of 680 000 from 15% to 84%, 680 000 from 85%). Under 5%, nothing (s 27(2)). The Table leaves gaps for a fractional percentage between 10% and 15%, and between 84% and 85%. Asserted, gaps `not covered`.
5. **No interest on pain and suffering or on free care** (s 29); interest on other heads runs from when the loss was first incurred to the assessment, at the 10-year bond rate published for January (assessments March to August) or July (September to February), unless regulations prescribe a rate (s 30). Asserted.
6. **Does Part 3A's reversed onus and vicarious liability reach abuse before Part 3A commenced?** s 17B(5) extends Part 3A Divisions 1, 4, 5 and 6 to causes of action that arose before Part 3A commenced, "despite section 4(2)". Divisions 2 (the reversed onus, ss 17D–17F) and 3 (vicarious liability, s 17G) are left out. Read literally, they are left to s 4(2), which reaches incidents after the commencement of "this Act" — 1 May 2003. But s 4(2) only limits the Act and does not extend it; naming four Divisions implies the other two do not reach earlier causes of action; and the presumption against retrospective changes to substantive liability points the same way. The encoding takes that reading: abuse from 1 May 2003 to before Part 3A commenced (taken as 30 September 2022, finding 8) answers `probably not`, and the answer states the literal reading too. The date of the abuse stands for the date the cause of action arose. Asserted at 1 May 2003, 1 June 2010, 29 and 30 September 2022, and 30 April 2003. (Fixed on 2026-11-07 after the independent verification; the first version answered on the literal reading without a hedge.)
7. **Part 4A does not apply to personal injury claims** (s 32B(3)). It reaches an offender's claims for assault, battery or false imprisonment only so far as they are not claims for damages for personal injury; the injury itself is claimed under the rest of the Act, uncapped by s 32E. Asserted.
8. **The commencement of s 32B is inferred, not read.** The endnotes list the Amendment Act 2022's commencement by Part but not which sections are in each Part. Its ss 4–9 (amending ss 3, 4, inserting Part 4A Divisions 1–3, amending the long title and s 27, repealing s 28) and ss 10–12 (amending s 3, inserting Part 3A, amending the long title again) look like Parts 2 and 3; s 13 (Part 4A Divisions 4, 5) the remainder. So s 32B is taken as commencing on 3 June 2022, Part 3A on 30 September 2022, and the trust provisions on 1 January 2023. The first two are used, at the s 32B(5) edge and the Part 3A edge (finding 6).
9. **Above 15 days, every false imprisonment band gives the same 15 000.** s 32E(1)(c) steps down from 1 000 to 500 to 250 units a day at 30 and 60 days, but s 32E(2) caps a wrong (or a related series) at 15 000; 15 days at 1 000 already reach it, and 30 × 500 and 60 × 250 are exactly 15 000. The lower daily rates never bite. Also, a false imprisonment of 2 days is capped at 2 000, the same as one of a day or less. Asserted.
10. **The trust applies to any defendant; the withholding and the victims' notice only to public ones.** s 32H(1) sends to the Public Trustee all damages "awarded by a court to an offender for a civil wrong to which this Part applies", whoever pays; s 32G (withholding for victims levies and fines) and s 32J (notice to victims) are for a "public entity defendant" only. Where a private defendant pays (for example a fellow prisoner sued for battery), the money is held for victims who are never told of it. Asserted (a private defendant withholds nothing, all goes on trust).
11. **Only a notified victim may ask for details** (s 32J(4)), and only while the money is held; the public entity then has 28 days (s 32J(5)). A victim not notified is `not covered`. Asserted.
12. **A victim's out-of-time claim is revived while trust money exists** (s 32P): the Limitation Act 1981 s 12(1) period "does not apply", and a barred cause of action "is reinstated", but only to commence the claim and for an order paying it from the trust (s 32K). Asserted.
13. **An associated trust's liability is limited to the trust property** (s 17M(3)); the institution must name its associated trusts within 28 days of the claimant's application (s 17K(3)), which may be made only after 120 days (s 17K(1)(b)). Asserted.
14. **Small drafting slips:** s 17Q(3) says "the unincorporated association" for the unincorporated institution; s 17R(3)(c), (d) say "current officer holder"; s 32E(1)(b) reads "–5 000". Nothing turns on them.

## Raised in the ledger

Nothing. No ledger entry named this Act, and no scenario life cites it.

## What would need doing before this is worth relying on

- **The Regulations under the Act**, if any are in force: the prescribed guides and excluded psychological injuries (s 18), the discount rate (s 22), the interest rate (s 30), the volunteer remuneration amount and extra purposes (s 7(7)), extra grocery products (s 7A(4)), extra associated individuals (s 17C(1)(e)), extra matters for ss 17E(3), 17F(3), and any excluded claims (s 4(4)).
- **The Amendment Act 2022**, to confirm the commencement of s 32B and of Part 3A (findings 6, 8), and the transitional effect of the 2022 change of s 27 to monetary units.
- **The Revenue Units Act 2009**, for the dollar value of a monetary unit.
- **The Limitation Act 1981** encoding (`subjects/au/nt/limitation-act-1981/`), for the time limit that s 32P sets aside; the Compensation (Fatal Injuries) Act 1974 (s 5). Linked here in words only; the stable `l4` cannot import across subjects.
- **The Interpretation Act 1978** rules on reckoning time and on commencement.
- **Case law** on "intoxicated", "materially contribute", "all reasonable steps", "gives occasion", "substantially the same", and on the temporal reach of Part 3A (finding 6). None was read.
- An independent test pass and a human review.
