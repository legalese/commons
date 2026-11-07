# Limitation of Actions Act 1958 (Vic): baseline encoding for the person who wants to sue

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
It is the first encoding of this Act; nothing beside it was changed.
There is no REFUSE in it. A question the encoding cannot answer returns `NOTHING`, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

Three modules:

- **`limitation-core.l4`**, seat-neutral: date arithmetic (built-in date functions only, no daydate), which time limit applies (s 4, s 5(9), s 23AB, s 27B, s 27N, ss 27O-27Q, s 40), discoverability (s 27F), legal incapacity (s 27J), the last day for the injured person's own action (ss 27D, 27E, 27I, 27J), for a survivor action (ss 27G, 27I(3)) and for a dependants' action for a death (ss 27F(4), 27H, 27Q), extension (ss 27K-27M, 23A), Division 5's earlier judgments and settlements (ss 27OA, 27QA-27QF, 27R, 27T), and Part I with Part II outside Part IIA (ss 5, 23, 27). One regulative rule: the bar itself (see below). Each rule names its section and the deposited line it comes from.
- **`limitation-seat.l4`**, the seat: 15 questions, each with `@export` and a `@desc` on every input, under `§§` headings (which time limit; discoverability; my own injury; after a death; asking the court for more time; child abuse claims; outside Part IIA; am I in time). It restates no rule. No exported question takes a `DEONTIC` or `EVENT` input.
- **`limitation-cases.l4`**, the cases: every exported question with its edges, and the bar by `EVALTRACE`.

Victoria has no requirement ledger, so no ledger line is closed or raised.

**The regulative rule.** The Act states bars ("shall not be brought after the expiration of"), not duties. The bar is written once as a rule, `the limitation bar`: the plaintiff `DO bring the action WITHIN` the days to the last day, `HENCE FULFILLED`, `LEST BREACH ... BECAUSE "the limitation period has expired and the action is barred"`. Here BREACH means "barred", not a wrong by the plaintiff. It is tested by `EVALTRACE` (in time on the last day; barred on the day after and when no action comes), and mirrored by the plain question "Am I in time if I start my action on this day".

## Edition

**Limitation of Actions Act 1958**, Act No. 6295/1958, **Version No. 113, as at 2 October 2026**, deposited at `../../registers/source-bundle/limitation-of-actions-act-1958.txt` (sha256 `84e874841a2b4d3ad2348a1304bd7b36be7b23607bfb485db8d2ab886eb689bd`, the blob as committed).
The owner saved the Word file by hand on 2026-11-07 from the version page, the current version that day; `limitation-of-actions-act-1958.meta.json` records the file, its hash and the conversion, and `subjects/au/vic/README.md` records the deposit. Line numbers in the modules are lines of that text.
The version includes s 23AB (no limitation period for certain dust-related conditions) and the amendment of s 40, inserted by the Workplace Legislation Amendment (Accident Compensation and Other Matters) Act 2026 (No. 45/2026 ss 18E, 18F, in force 2 October 2026; endnote at line 1218), and the Division 5 amendments of the Justice Legislation Amendment (Vicarious Liability for Child Abuse) Act 2026 (No. 5/2026 ss 4-9, in force 25 February 2026; endnote at line 1212). That commencement day ends the window of ss 27OA, 27QA(1A) and 27T: 13 November 2024 to 25 February 2026, both days in.

No regulations set a number this encoding uses. Borrowed terms are asked as facts: dust-related condition (Administration and Probate Act 1958 s 3(1)), survivor action (Administration and Probate Act 1958 s 29), an action arising under Wrongs Act 1958 Part III, represented person (Guardianship and Administration Act 2019), the compensation schemes of ss 27B(2) and 40, and the National Redress Scheme deed or offer of s 27QA(3). Minority is fixed at under 18 (Age of Majority Act 1977, not deposited).

## Checks

| Module | Assertions |
|---|---|
| `limitation-core.l4` | none (0 errors, 0 warnings) |
| `limitation-seat.l4` | none (0 errors, 0 warnings) |
| `limitation-cases.l4` | 120 written, 120 satisfied (0 errors, 0 warnings) |

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (2026-11-07). A copy of the case file with two expected values changed was run outside the repository, to confirm that failures are reported (2 failed, as expected); it was not kept.
Every expected value was worked by hand from the deposited text, with the arithmetic or reason in the comment above the assertion. The edges asserted include: 20 and 21 May 2003 (s 27N); an 18th birthday on the day of the act and the day after; 27 and 28 days of incapacity (s 27J(1)(b)); an incapacity partly before discoverability, and one that ended before the act; discoverability by the deceased exactly 3 years before the death and more than 3 years (s 27G(a)); the death before age 25 (s 27I(3)); the long-stop ending first and the discoverability limb ending first; 29 February to 28 February; 12 and 13 November 2024, 25 and 26 February 2026 (the window); 30 June and 1 July 2018 (s 27OA); fraud discovered before and after accrual; the s 23 proviso (a); the last day and the day after for the bar.

## Seat

**The injured person, or after a death the estate or the dependants** (`limitation-seat.l4`): the person who wants to sue and asks whether, and until when, they still can. In the survivor action questions the seat is the executor or administrator; in the Part III questions it is a dependant; in the Division 5 questions it is the person who was abused as a child. The defendant, the insurer and the court get no seat: the court's powers (to extend, to set aside) appear as what the person may ask for and what follows, and its judgments as conditional inputs.
*Which time limit applies to my claim? Does Part IIA apply? When did my claim become discoverable? What is the last day I can sue for my injury; the estate for the deceased's injury; the dependants for the death? Can I ask a court to extend my time; what is my last day after an extension? Can I sue again on a child abuse claim that was dismissed or settled; can the court set the earlier judgment or settlement aside; can the payer recover what it paid me; can the court take it into account; do the 2026 changes apply to my claim? What is the last day outside Part IIA? Am I in time if I start on this day?*

No defendant seat is written.

**The 2026-10-18 defaults.**

- **The Act alone, with the instruments that set its numbers.** Followed. No regulations set a number used here. The parent schemes (Accident Compensation Act 1985, WIRC Act 2013, Transport Accident Act 1986, Wrongs Act 1958, Administration and Probate Act 1958) are named only to ask whether they apply; nothing is restated from them.
- **The actors the text names.** Followed: the plaintiff, the deceased, the executor or administrator, the dependants, the parent or guardian, the close associate, the defendant, the court, the Supreme Court.
- **A judgment handed to someone else answered conditionally.** Followed. "Ought to have known" (s 27F(2)) is folded into the dates the person gives; "just and reasonable" (ss 27K, 27QC, 27QE), the s 27L matters, the length of an extension, and the s 27I(2) close associate test ("might be influenced", "might be unwilling") are asked as facts, never decided.
- **Definitions worked out, borrowed terms asked.** The Act's own definitions in L4: under a disability (s 3(2)), long-stop limitation period (s 27A, through ss 27D, 27E, 27H, 27I), discoverable (s 27F), legal incapacity and capable parent or guardian (s 27J, with the 28-day test), previous judgment, previously barred and previously settled cause of action (s 27OA). Asked as facts: the borrowed terms listed under Edition.
- **One case.** One cause of action by one plaintiff against one defendant, with at most one spell of legal incapacity.
- **The Act's own terms with a plain gloss.** Followed, in the `@desc` of each input.
- **Operative sections in; machinery out.** Followed: s 1, s 2, s 38C (regulations), ss 36-38B (the Supreme Court jurisdiction declarations) are out.

## Scope

**In** (the focus: Part IIA personal injury actions as whole Divisions, with s 5, the Part II extensions and the choice of regime):

- **Choice of regime:** s 4, s 5(9), s 23AB, s 23(1A), s 23A(6), s 27B(1)-(3), s 27C, s 27N(1), (2), (4)-(6), s 27O, s 33 (as the reason a survivor or Part III action outside Part IIA is out), s 40.
- **Part IIA Division 1:** s 27A (long-stop limitation period; survivor action as a fact; guardian and parent as glosses), s 27B.
- **Part IIA Division 2:** ss 27C-27J, all of them.
- **Part IIA Division 3:** s 27K, s 27L (in the `@desc` of the court's decision, as factors), s 27M(1); s 27M(2) and s 23A(5) (application by summons, served on each defendant) noted only.
- **Part IIA Division 4:** s 27N, except (3).
- **Part IIA Division 5:** ss 27O, 27OA, 27P, 27Q, 27QA-27QF, 27R(2), (3), 27T; s 27R(1) and its Example (other powers, including a permanent stay where a fair trial is impossible) noted only; s 27S (a transitional for the 2020 definition, spent by the 2026 one) noted only.
- **Part I:** s 5(1)(a), (1AA), (1A).
- **Part II:** s 23(1) with proviso (a), s 23A(2), (4), (6), s 23AB, s 27(1).

**Out, and why:**

- **Part I, other heads:** defamation (s 5(1AAA)-(1AAD), ss 5A, 5B, 23B-23D), recognisances, awards and sums by enactment (s 5(1)(b)-(d)), accounts, specialties and judgments (s 5(2)-(4)), penalties (s 5(5)), interest (s 5(7)), equitable relief (s 5(8)), conversion (s 6), land, rent and mortgages (Divisions 3 and 4), taxes (ss 20A, 20B), trusts and estates (ss 21, 22). Outside the focus.
- **Part II, other heads:** s 23(1) provisos (b)-(d) (a second disability, land, penalties: outside the focus), s 23(2) (war), Division 3 (acknowledgment and part payment, ss 24-26), s 27(1) proviso (purchasers for value) and s 27(2) (tax).
- **s 23A(3)**: the court's factors for an extension outside Part IIA, the same in substance as s 27L(1); the court's decision is an input.
- **s 5(1B), (1C), ss 39, 39A, 39B, 41** (transitionals for earlier amendments), **s 27N(3)** (proceedings commenced in a court before 1 October 2003: not the seat's question), **ss 28-35** other than s 33 (arbitrations, foreclosure, set-off, acquiescence, the Crown, Weldon v Neal amendments, already-barred and pending actions).
- **The earlier law kept by s 40 and the cap of s 27N(4)**: both refer to the Act as in force before the Limitation of Actions (Amendment) Act 2002 or before Part IIA, which is not deposited. The regime question names them; the last-day questions answer `NOTHING` for an act or omission before 21 May 2003 (outside Division 5).
- **The periods of other Acts** that s 33 preserves: a survivor action or a Part III action outside Part IIA (for example for a tobacco death) takes its period from the Administration and Probate Act 1958 s 29 or the Wrongs Act 1958 s 20; `NOTHING` here.

## Negatives and legal effects

This row follows the corpus convention in `docs/ENCODING-GUIDE.md` section 5, "Rulings on negatives and legal effects" (2026-11-04 and 2026-11-05): a function answers `JUST FALSE` only where the text itself says no to the case in its own words, and `NOTHING` elsewhere. The rulings it relies on, word for word from that section:

- "(c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`." (Periods, "where" and scope limits, 2026-11-05.)
- "(a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`" (the same ruling), applied to the bar: after the last day the action is not in time.
- "Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z)", for the fork lines below.

In this row:

- `JUST FALSE`: s 27B(2) ("This Part does not apply to"); s 27O(2) ("Divisions 2 and 3 do not apply", for extending a s 27P action); s 27QA(3) ("This section does not apply"); s 27QF ("is not entitled to seek to recover").
- Plain BOOLEAN answers where the text's own words give both answers: s 3(2) (a definition), s 23AB ("No limitation period applies ... if"), s 27J(1) (a definition), the power to set aside (ss 27QB(3), 27QD(3), 27R(2), (3): "may not", "may"), ss 27QC(2), 27QE(2) ("if satisfied"), and the bar (a period the text fixes).
- `NOTHING`: s 27B where the claim is not for death or personal injury (a scope, rule (c)); s 27QA where none of its heads applies, and where there is no earlier outcome; s 27QF where nothing is set aside; s 27T outside its heads; an extension under s 23AB, s 40 or s 5(1)(a) (the Act gives no power and says nothing); the last-day questions for an act before 21 May 2003 (s 27N(4): the earlier law is not deposited) and for a child killed by a parent in a Part III action (finding 4); the regime for "another kind of action" and for a survivor or Part III action outside Part IIA (s 33).

**Fork lines** (case-by-case decisions under the ruling of 2026-11-05, for the reviewer to overrule):

1. Every period, `the last day of n years from`: a period of n years "from" a day excludes that day, so its last day is the same date n years on (29 February: 28 February). Other reading: the last day is the day before the anniversary. The Interpretation of Legislation Act 1984 (Vic) s 44, which governs, is not deposited.
2. s 27I(1)(b), `ss 27D, 27E, 27I, 27J -- the last day for the injured person's action`: "the long-stop limitation period for the cause of action is the period of 12 years from when the victim turns 25" replaces the 12-year limb of s 27D(1)(b) or s 27E(2)(b), and the victim, a minor at the act, also takes s 27E's 6 years from the s 27I deemed day. Other reading: s 27D and s 27E do not use the defined term, so s 27I(1)(b) changes only the defined term (finding 1); or s 27I sets a separate 3-year period.
3. s 27I(3) with s 27G, `ss 27D, 27E, 27G, 27I -- the last day for a survivor action`: where the deceased was a minor injured by a parent, guardian or close associate, the deemed day is the later of the death (or turning 25, if earlier) and the s 27G day, and the long-stop runs 12 years from the death (or turning 25). Other reading: s 27I(1)(a)'s "actually discoverable by the victim" means discoverability by the deceased alone, ignoring s 27G.
4. s 27E, `ss 27D, 27F(4), 27H, 27Q -- the last day for a dependants' action for a death`: a Part III action is "founded on" the death, not on "a personal injury to a person who was under a disability", so s 27D's 3 years applies whatever the deceased's age or capacity. Other reading: a Part III action for a death from an injury to a minor takes s 27E's 6 years.
5. ss 27R(2), 27QD(3), `ss 27QB, 27QD, 27R -- the court hearing the action has power to set it aside`: a settlement agreement given effect by no court order is not "of another court", so any court hearing the action may set it aside. Other reading: only the Supreme Court may set aside a settlement agreement.
6. s 27J(2), `s 27J(2) -- the days suspended`: suspension counts only the days of incapacity on or after the period's start, and none if the incapacity began after the period's unsuspended last day; a spell that runs on extends the period to its end. Other reading: incapacity before the period begins also postpones its start.
7. s 23(1), `ss 5, 23, 27 -- the last day for a Part I action`: the last day is the later of the ordinary period and 6 years from the end of the disability (the extension never shortens). Other reading: none needed; "notwithstanding that the period of limitation has expired".

## What the Act turns out to say

1. **The long-stop is defined but s 27D and s 27E do not use the defined term.** s 27A defines "long-stop limitation period" as 12 years from the act or omission; ss 27D(1)(b) and 27E(2)(b) restate the 12 years without the term; ss 27H and 27I(1)(b) then modify "the long-stop limitation period". The encoding reads ss 27H and 27I as changing the 12-year limb (fork line 2). Asserted (s 27I: 20 April 2042; s 27H: 10 February 2032).
2. **s 23AB names the worker and the dependants, not the estate.** "whether the cause of action is brought by the worker or the dependants of a deceased worker": a survivor action by the executor for a worker's dust-related condition is not within it, and Part IIA does not apply to dust-related conditions (s 27B(2)(d)). Its period comes from elsewhere (s 33). Asserted (`NOTHING`).
3. **s 23AB reaches actions under Wrongs Act Part VB, which is most claims for personal injury damages caused by fault.** So a worker's dust-related condition has no limitation period whether or not the worker sues under the workplace schemes; a dust-related condition of someone who is not a worker stays under s 5(1AA) or (1A). Asserted.
4. **s 27I and s 27H collide for a minor killed by a parent.** s 27H runs the long-stop of a Part III action from the death; s 27I(1)(b) runs it 12 years from when the victim "turns 25", which a dead child never does; s 27I(3) resolves this only for a survivor action. The encoding answers `NOTHING`. Asserted.
5. **Division 5 needs Part IIA to apply first.** s 27O(1)(a) applies Division 5 only to a cause of action "to which this Part applies or extends", so child abuse claims within the workplace schemes (s 27B(2)(a)) stay under s 40. Asserted.
6. **The 2026 window is one day longer than it may look.** "ending on the date of commencement" of No. 5/2026, which was 25 February 2026, the day after assent; a judgment or settlement on 25 February 2026 is in it. Asserted (25 in, 26 out).
7. **s 27QA(1) does not say "previous judgment".** Subsection (1) lets a previously barred cause of action be sued on after a dismissal on limitation grounds; a merits judgment on such a cause before 13 November 2024 is outside s 27QA and the encoding answers `NOTHING`. s 27OA's "previous judgment" (a) includes any judgment in a previously barred cause of action, so s 27QC(1) might reach further than s 27QA(1). Asserted (dismissal as out of time in 2010: yes; out of time in 2016, not previously barred: nothing).
8. **s 27S is spent.** It applies s 27OA "as amended by" the 2020 Act; s 27OA's definitions were substituted again in 2026 (No. 5/2026 s 4). Noted only.
9. **s 23(1)'s "less number of years" exception makes the extension longer for personal injury.** The words "(except under section 5(1AA) or (1A))" mean a person under a disability gets 6 years from the end of the disability, not 3. (s 23(1A) then removes s 23(1) for Part IIA actions, so this reaches only personal injury outside Part IIA, such as tobacco claims.) Asserted (1 January 2026).

## Before relying on it

- An independent test pass, and a lawyer's review of the fork lines and findings.
- The Act as in force before the Limitation of Actions (Amendment) Act 2002 (for s 40) and before Part IIA (for s 27N(4)), deposited and encoded.
- The Interpretation of Legislation Act 1984 (Vic) s 44, deposited, to settle fork line 1.
- More than one spell of legal incapacity (s 27J).
- The Part I heads and Part II divisions listed as out, especially acknowledgment and part payment (ss 24-26) and defamation.
- A defendant seat, if one is wanted.
