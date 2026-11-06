# Wrongs Act 1958 (Vic): baseline encoding for the injured person

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
It is the first encoding of this Act; nothing beside it was changed.
There is no REFUSE in it. A question the encoding cannot answer returns `NOTHING`, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

Three modules:

- **`wrongs-core.l4`**, seat-neutral: date arithmetic (built-in date functions only, no daydate), the s 28G figures for two years, and the rules of Parts IVAA, V (s 26), VB, VBA, X, XI, XIII and XIIIA in scope, each with the section and the deposited line it comes from. Two chains of duties with deadlines are regulative rules (`DEONTIC`): ss 28LO-28LQ (the respondent's answer to a request to waive the impairment assessment, with the further-information and proper-respondent steps) and ss 28LW-28LWB (the respondent's response to a certificate of assessment, the same steps, and deemed acceptance).
- **`wrongs-seat.l4`**, the injured person's seat: 38 questions, each with `@export` and a `@desc` on every input, under `§§` headings in the Act's order of claims work (damages caps, the significant injury threshold, the steps with the respondent, negligence and mental harm, proportionate liability, child abuse). It restates no rule. No exported question takes a `DEONTIC` or `EVENT` input.
- **`wrongs-cases.l4`**, the cases: every exported question with its edges, and both regulative rules by `EVALTRACE`.

Victoria has no requirement ledger, so no ledger line is closed or raised.

## Edition

**Wrongs Act 1958**, Act No. 6420/1958, **Version No. 130, as at 25 February 2026**, deposited at `../../registers/source-bundle/wrongs-act-1958.txt` (sha256 `cc5d5a7a30d972f6c30302100ce0d7b154dfd9fedde9336c678a37e262293083`, the blob as committed).
The owner saved the Word file by hand on 2026-11-06 from the version page, the current version that day; `wrongs-act-1958.meta.json` records the file, its hash and the conversion, and `subjects/au/vic/README.md` records the deposit. Line numbers in the modules are lines of that text.
The version includes Part XIIIA (statutory vicarious liability for child abuse), inserted by the Justice Legislation Amendment (Vicarious Liability for Child Abuse) Act 2026 (No. 5/2026 s 3, in force 25 February 2026; endnote at line 2806).
The one embedded equation in the `.formulas.md` sidecar (s 28H, A x B / C) is the CPI indexation formula; it is not computed (see the figures below).

**The s 28G figures.** s 28G prints $577 050; s 28H varies it every 1 July by the Melbourne CPI, which is not deposited. The Note after s 28HAAB (line 833) says the amount is "equivalent to" the amount for s 340(b)(ii) of the Workplace Injury Rehabilitation and Compensation Act 2013, indexed to the same effect, and that "the amount, as indexed under that Act, is published annually in the Government Gazette". The varied s 340(b)(ii) amounts are taken from the **Victoria Government Gazette No. S 363 of 30 June 2026**, deposited at `subjects/au/vic/workers-compensation-annual-indexation-notice/registers/source-bundle/GG2026S363.txt` (sha256 `04c8fe556bca3ef38185cf933965d9a6526da59cac06fb470eec02fe5945499a`), line 703: $759 510 for 1 July 2025 to 30 June 2026, $783 000 for 1 July 2026 to 30 June 2027 (the notice's two columns read as the WIRC Act baseline reads them). IMPORT cannot reach another subject's folder, so the two figures are copied by hand into `wrongs-core.l4`. A day of award outside those years answers `NOTHING` (asserted at both edges). See finding 1 and fork line 1.

**Other numbers the Act takes from elsewhere** are inputs: average weekly earnings (the Australian Statistician's estimate, ss 28F, 28IB, 28IE) and any discount rate prescribed by regulations (s 28I; no Wrongs regulations are deposited, and without one the Act's 5 per cent applies).

## Checks

| Module | Assertions |
|---|---|
| `wrongs-core.l4` | none (0 errors, 0 warnings) |
| `wrongs-seat.l4` | none (0 errors, 0 warnings) |
| `wrongs-cases.l4` | 238 written, 238 satisfied (0 errors, 0 warnings) |

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (2026-11-06). A copy of the case file with two expected values changed was run first, to confirm that failures are reported (3 failed, as expected); it was not kept.
Every expected value was worked by hand from the deposited text, with the arithmetic or reason in the comment above the assertion. The edges asserted include: 5 and 5.5 per cent (other injury), 4 and 5 (spinal), 9 and 10 (psychiatric); 5 and 5.5 per cent NAL hearing loss; 5.99 hours and 5.99 months, 5 hours and 6 months, for gratuitous attendant care; 39, 40 and 60 hours a week for the care caps; 5 and 6 hours and months for the dependants' care test; the 60th and 61st day for the respondent's answers, the 14th and 15th for the claimant's notice; 28 February and 29 February for 3 months after 30 November; 30 June and 1 July of 2025, 2026 and 2027 for the s 28G figures; 30 June and 1 July 2017 for Part XIII; ages 17 and 18; reductions of 0, 25, 100 and 120 per cent; fraud and no fraud; a later recovery capped by the loss.
Breached traces are asserted through a helper (`ends fulfilled`) and `NOT`, because `EVALTRACE ... EQUALS` cannot test a breach.

## Seat

**The injured person** (`wrongs-seat.l4`): the claimant or plaintiff, the person who suffered injury, mental harm, economic loss or property damage and asks what the Act lets them recover. In the child abuse groups the seat is the person who was abused as a child (now usually an adult); in the contributory negligence question it is also the dependants of a person who died. The respondent, the defendant, the organisation or institution, Medical Panels and the court get no seat: their duties and powers appear only as what the claimant must be given, and by when, and the court's judgments as conditional inputs.
*Does Part VB apply to my award? What is the most I can get for lost earnings each week, and for non-economic loss? What discount rate applies? Can I get damages for unpaid care I receive, or for my lost capacity to care for my dependants, and how much a week at most? Does my impairment meet the threshold; what is my hearing loss assessed at; is my injury significant; can I recover non-economic loss; can the court decide significance itself? By when must the respondent answer my waiver request or my certificate; by when must I reply to "not the proper respondent"; has my assessment been accepted or deemed accepted; until when is my limitation period suspended? Do Parts X and XI apply; could the defendant have been negligent; did the negligence cause my harm; am I presumed aware of an obvious risk; was the risk inherent; must I prove I was unaware; can a professional rely on peer opinion; what do I recover after my own contributory negligence? Was I owed a duty against pure mental harm; does s 73 let me recover for shock; can I recover consequential mental harm, or economic loss for mental harm? Is my claim apportionable; what is the most I can get against one defendant, or later against another? Is the organisation a relevant organisation; was my abuser associated with it; is it presumed to have breached its duty; whom do I sue; is the institution vicariously liable?*

No defendant, insurer or organisation seat is written. A respondent seat for Part VBA Division 4 (its 60- and 14-day duties) would draw on the same two rules.

**The 2026-10-18 defaults.**

- **The Act alone, with the instruments that set its numbers.** Followed, with one bridge: the s 28G figure comes from the Gazette's WIRC Act row, through the Note (finding 1). No Wrongs regulations are deposited; prescribed matters (an excluded class of award or claim, a discount rate) are inputs.
- **The actors the text names.** Followed: the claimant, the respondent, the plaintiff and the defendant, the court, the Medical Panel, the relevant organisation, the institution, the State, the nominated legal person.
- **A judgment handed to someone else answered conditionally.** Followed. "Reasonable" need, care, precautions and persons; "satisfied"; "just and equitable"; "appropriate"; obvious, inherent and insignificant risks; "akin to an employee"; "supplies the occasion"; whether peer opinion is "unreasonable"; "close relationship": each is asked as "would a court find ...", never decided.
- **Definitions worked out, borrowed terms asked.** The Act's own definitions in L4: threshold level (s 28LB), significant injury (s 28LF), hearing impairment (s 28LK), dependants (s 28B, the two kinds), relevant organisation, child and abuse (s 88), individual associated (s 90), institution (s 93B, asked as one fact), apportionable claim (ss 24AF, 24AG). Asked as facts: degree of impairment (A.M.A. Guides), dust-related condition (Administration and Probate Act 1958), asbestos-related condition (Asbestos Diseases Compensation Act 2008), health service, professional, public sector body (Public Administration Act 2004), recognised psychiatric illness, average weekly earnings.
- **One case.** One claim by one person against one respondent or defendant (for proportionate liability, one defendant among several).
- **The Act's own terms with a plain gloss.** Followed, in the `@desc` of each input.
- **Operative sections in; machinery out.** Followed: regulation-making powers (ss 24AR, 28K, 28LZP, 64, 76), the Supreme Court jurisdiction declarations (ss 24AQ, 27, 28J, 28LZO, 65, 77), the Convenor's administration (s 28LXA) and Medical Panel procedure are out.

## Scope

**In** (the focus: Part VB thresholds and caps, Part VBA thresholds, Part X negligence, Part XI mental harm, proportionate liability, Part XIII organisational child abuse liability, Part XIIIA statutory vicarious liability):

- **Part VB:** s 28B (definitions), s 28C(1), (2), (2A), s 28F, s 28G with s 28H (figures, see Edition), s 28I, s 28IA, s 28IB, s 28ID(1)-(4), s 28IE, s 28IF.
- **Part VBA:** s 28LB (threshold level), s 28LC, s 28LE, s 28LF, s 28LK, s 28LO(2)-(4), s 28LP, s 28LQ, s 28LV, s 28LW, s 28LWA, s 28LWB, s 28LWE(1)(a), (3), s 28LZG(10) and s 28LZGA(4) (as facts), s 28LZH, s 28LZN.
- **Part X:** ss 44, 45, s 48(1), s 51(1), (2), s 52 (as a gloss), ss 53, 54, 55, 56, 59, 60, s 63.
- **Part V:** s 26(1), (4) with s 63.
- **Part XI:** ss 68, 69, 72, 73, 74, 75.
- **Part IVAA:** ss 24AF(1), 24AG, 24AH(1) (as a fact), 24AI(1), 24AK, 24AM.
- **Part XIII:** s 88, s 90, s 91(2), (3), (5)-(7), s 92(1), s 93.
- **Part XIIIA:** s 93A(3), s 93B, s 93C(1), (3), s 93D.

**Out, and why:**

- **Other Parts**, outside the focus, for later layers: Part I and IA (criminal defamation, publishers), Part II (seduction), Part IIA (occupiers' liability), Part IIB (intoxication and illegal activity), Part IIC (apologies), **Part III (wrongful act causing death, ss 16-24, the dependants' action)**, Part IV (contribution between wrongdoers), Part IVA, Part VA (s 28A, tax on lost earnings), Part VBAA (prisoners), Part VC (structured settlements), Parts VI-IX (aircraft, good samaritans, food donors, champerty, straying animals, volunteers), **Part XII (public authorities)**, Part XIV.
- **Transitionals, assumed met:** the questions assume a proceeding commenced on or after 1 January 2004, the last of the days that ss 24AS (Part IVAA, from the commencement of No. 60/2003 s 3 on 1 January 2004), 28L(2) (23 October 2002), 28LA and 28LZQ (21 May and 1 October 2003), 28LAB, 28LAC, 66(3) and 78(2) (3 December 2003) turn on (commencement days from the endnotes, lines 2578-2592). The asbestos transitional (s 28LZR), the 2015 transitionals (ss 28LACA, 28LZS) and the courts' powers to resolve transitional difficulties (ss 28LACB, 28LZT) are out. Part XIII's own day (s 93) is encoded.
- **Within Part VB:** s 28HA (court may refer to earlier awards), s 28IC, s 28ID(5) (a third person's claim), s 28D, s 28E (no cause of action; noted).
- **Within Part VBA:** Division 3's assessment method (ss 28LG-28LJ, 28LL, 28LM: the degree of impairment is an input; s 28LJ's disregard of secondary psychiatric injury is in its `@desc` by reference to the A.M.A. Guides), certificate content (ss 28LN, 28LNA as a fact), s 28LR, s 28LT (service, as a fact), s 28LU, ss 28LWC, 28LWD, ss 28LX, 28LXA (costs and administration), Division 5 (Medical Panel procedure, except the deemed significance of ss 28LZG(10), 28LZGA(4) as facts; the deemed acceptance of s 28LZA(4) is not encoded), Division 6 filing and stays (ss 28LZM, 28LZMA), Division 7.
- **Within Parts X and XI:** ss 46, 47, 70, 71 (contracts and the common law), s 49, s 50 (duty to warn: reasonable care), ss 57, 58 (the standard for persons professing a skill), s 61 (non-delegable duties), s 62 (the standard for contributory negligence, a judgment, folded into the reduction input).
- **Within Part V:** s 26(1A)-(1C), (2), (5), (6), ss 27, 28, 28AA, 28AAB.
- **Within Part IVAA:** s 24AF(2), (3), s 24AH(2), s 24AI(2), (3), s 24AJ, s 24AL, ss 24AN-24AP, s 24AS (assumed, above).
- **Within Parts XIII and XIIIA:** s 89 (Part X applies, Part XII does not; noted), s 92(2), (3) (late nomination), s 93A(1), (2), s 93C(2), (4), (5) (the court's factors, in the `@desc`).

## Negatives and legal effects

This row follows the corpus convention in `docs/ENCODING-GUIDE.md` section 5, "Rulings on negatives and legal effects" (2026-11-04 and 2026-11-05): a function answers `JUST FALSE` only where the text itself says no to the case in its own words, and `NOTHING` elsewhere. In this row:

- `JUST FALSE`: s 28C(2) and s 24AG and ss 45, 69 ("excluded", "does not apply"); s 28LE ("not entitled ... unless"); s 54(1) ("If ... is presumed ... unless", rule (b) and the "unless" of the 2026-11-05 ruling for questions without a convention); s 56(1) ("where the plaintiff alleges", rule (b)); s 59(1) ("is not negligent ... if", answered as "s 59 gives no protection on these facts"); s 73(2), (3) ("not entitled ... unless", "No damages"); s 88 ("means", for child, abuse and relevant organisation, the last as a BOOLEAN); s 90(2) ("not associated solely because"); s 91(6) ("does not apply"); s 93C(3) ("is not").
- Plain BOOLEAN answers where the text's own words give both answers: s 28IA ("No damages ... unless", "no damages ... if"), s 28ID(2) ("may only do so if"), s 28LB, s 28LF ("is significant injury if", a definition), s 48(1), s 51, s 55, s 72, s 74, s 75, s 93C(1) ("is vicariously liable ... if").
- `NOTHING`: s 28C, ss 45, 69, ss 24AF where the claim is outside the class the Part names (a scope with no "only", rule (c)); s 28LE where Part VBA does not apply (another law governs); s 28IE under s 28IF ("do not apply": no cap from this section, the common law decides); s 54(2), (3) and s 56(2), (4) (the common law continues to apply); s 59 for a warning (s 60) or for someone not a professional; s 73 outside its "This section applies to"; s 24AI for a defendant who is not a concurrent wrongdoer (s 24AI(2)(b): other rules); s 90 outside its open list ("includes but is not limited to"); s 91 for abuse before 1 July 2017 (s 93) or an unsettled association; s 28G outside the two years of figures.

**Fork lines** (case-by-case decisions under the ruling of 2026-11-05, for the reviewer to overrule):

1. s 28G, s 28H, `s 28G, s 28H -- the maximum for non-economic loss`: the cap is the varied figure for the financial year in which the award is made, taken to equal the Gazette's WIRC Act s 340(b)(ii) figure because the Note says so. Other reading: compute s 28H from the CPI figures (not deposited) starting from $577 050; or take the year of the injury.
2. s 28LF(1)(ca), `s 28LF -- the injury is significant injury`: counts for a psychiatric injury, though subsection (1) is for "injury to a person (other than a psychiatric injury)". Other reading: (ca) covers only psychological injury that is not psychiatric, and a psychiatric injury from the loss of a child needs the 10 per cent threshold under (2).
3. s 28LZH(2), same function: a Medical Panel determination that the threshold is not satisfied answers "not significant" on every head, including loss of a foetus or breast and the deemed heads of (3). Other reading: s 28LZH(2) settles only the threshold heads ((a), (aa), (b)) and the other heads still stand.
4. s 28LW(4), `s 28LW, s 28LWE -- the status of the assessment`: a written response given after the 60th day does not undo the deemed acceptance. Other reading: a late acceptance is still an acceptance (same result), and a late intention to refer is of no effect (same result); no case turns on the difference.
5. s 26(1), s 63, `s 26, s 63 -- the damages after contributory negligence`: a reduction stated above 100 per cent is read as 100 (the claim is defeated). Other reading: none needed; the court cannot reduce by more.
6. s 90(1)(b), `s 90 -- the individual is associated with the organisation`: a minister or religious leader of an organisation that is not religious answers `NOTHING` (the open list of (a) may still catch them). Other reading: `JUST FALSE` for that head.

## What the Act turns out to say

1. **The indexed s 28G figure is never published as such.** s 28G prints $577 050 and s 28H indexes it, but the only published figure is the WIRC Act's s 340(b)(ii) amount, which the WIRC Act prints as $555 350. The two printed bases differ (the Wrongs Act's figure was last set by No. 62/2015); the bridge is the Note after s 28HAAB, and a Note is not part of the Act's operative text. If the Wrongs Act figure were indexed on its own and rounded under s 28HAAB, it could differ from the Gazette figure by a rounding step. The encoding uses the Gazette figure (fork line 1). Asserted ($759 510 and $783 000).
2. **s 28LF(1)(ca) speaks of psychiatric injury inside the subsection for injury "other than a psychiatric injury".** See fork line 2. Asserted (a psychiatric injury from the loss of a child at birth is significant).
3. **The Parts exclude different compensation schemes.** Part VB excludes awards under Part 7 of the WIRC Act (common law damages) but not Part 5; Part VBA, Part X and Part XI exclude Part 5 but not Part 7; Part IVAA excludes any claim "to which ... the Workplace Injury Rehabilitation and Compensation Act 2013 applies". Part VBA does not exclude the emergency, police, juries and education compensation laws, which Parts VB, X and XI exclude; Parts X and XI do not exclude victims of crime assistance, which Parts VB and IVAA exclude. Part VB still names the Victims of Crime Assistance Act 1996, and adds the 2022 Act only "to avoid doubt" (s 28C(2A)). Each list is encoded as it stands. Asserted (WIRC Part 5 under Part VB; WIRC Part 7 under Parts VBA, X and XI; victims of crime under Part X; emergency compensation under Part VBA).
4. **The threshold level is not uniform at the boundary.** "More than 5 per cent" for most injuries, but "5 per cent or more" for a spinal injury and "10 per cent or more" for a psychiatric injury (s 28LB, substituted in 2015). A 5 per cent spinal impairment qualifies; a 5 per cent knee impairment does not. Asserted.
5. **The two six-hours-and-six-months tests are not mirror images.** s 28IA(2) bars damages for gratuitous attendant care only if the care is for less than 6 hours a week "and" for less than 6 months, so 2 hours a week for 2 years is not barred; s 28ID(2)(c) requires care of at least 6 hours a week "and" at least 6 consecutive months, so both limbs must be met. Asserted (5 hours for 6 months; 2 hours for 24 months; 5 hours or 5 months under s 28ID).
6. **A Medical Panel's "not satisfied" and the other heads of significant injury.** s 28LZH(2) requires a court to accept such a determination as one "that the injury is not significant injury", while s 28LF(1)(c), (ca), (d) and (3) make an injury significant whatever the impairment. See fork line 3. Asserted.
7. **Part XIIIA excludes independent contractors; Part XIII includes contractors.** s 90(1)(a) makes a contractor an individual associated with the organisation, so the s 91 duty and its reverse onus reach abuse by a contractor; s 93C(3) says an independent contractor is not akin to an employee, so there is no statutory vicarious liability for the same abuse. Asserted (contractor: s 91 presumed breach; s 93C no).
8. **"Close relationship" is undefined** (s 73(2)(b)); it is asked as a fact. The duty question (s 72) and the shock question (s 73) are separate hurdles; s 72(2)(c) makes the relationship a circumstance, s 73(2)(b) a condition.
9. **The respondent's two 60-day windows coincide.** s 28LW(1) gives 60 days to respond and s 28LWE(1)(a) 60 days, from the same receipt, to refer; a respondent who responds on day 60 that it intends to refer has no time left, and is deemed to have accepted unless it refers that day (s 28LWE(3)). Asserted (referral on the 60th day; on the 61st).
10. **s 26(4): the dependants' action is not reduced for the deceased's contributory negligence.** The text says the action under Part III "shall not be defeated nor shall any damages ... be reduced by reason of" it. Asserted. (Part III itself is out of scope.)
11. **A register typo.** The side note before s 28IE (line 893) reads "S. 281E inserted by No. 102/2003 s. 10", for s 28IE. Noted only; it does not change the text.

## Before relying on it

- An independent test pass, and a lawyer's review of the fork lines and findings.
- The Gazette notice for 1 July 2027, when published and deposited, and its s 340(b)(ii) figure added; better, a published s 28G figure if one is found.
- The Parts listed as out, especially Part III (dependants' claims for a death), Part XII (public authorities), Part IV (contribution), Part IIB (intoxication) and Part VBAA (prisoners).
- The transitionals now assumed, if older claims matter.
- A respondent or defendant seat for the Division 4 duties, drawing on the same rules.
