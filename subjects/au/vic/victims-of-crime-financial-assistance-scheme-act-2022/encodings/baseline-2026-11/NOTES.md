# Victims of Crime (Financial Assistance Scheme) Act 2022 (Vic) -- baseline encoding, the victim who applies

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in `voc-dates.l4` (built-in date
functions only, no daydate), the rules in `voc-rules.l4`, and the victim's questions in `voc-seat.l4`, which imports the
rules and never restates one. `voc-cases.l4` holds the worked cases.

The focus asked for: financial assistance for victims of crime -- who may apply, what can be paid, time limits. The Act is
small (75 sections), so Parts 2 to 4 are encoded nearly whole, with the s 72 indexation and the Part 7 transitional
provisions a person with an old Tribunal award or an old crime meets.

## Edition

- **Act:** Victims of Crime (Financial Assistance Scheme) Act 2022, Act No. 21/2022, Version No. 002, incorporating
  amendments as at 1 December 2025, deposited at `../../registers/source-bundle/victims-crime-financial-assistance-scheme-act-2022.txt`
  (sha256 2e830e17...2cb3dd750f as committed, per its `.meta.json`), a plain-text conversion of the Word file the owner
  saved by hand on 6 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Not checked against
  the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the Victims of Crime (Financial Assistance Scheme) Regulations 2024 (SR 127/2024) are indexed
  in `../victims-of-crime-financial-assistance-scheme-regulations-2024/` but their text is not deposited. Everything they
  prescribe is asked: the prescribed categories of primary victim (s 9(4)), special reporting categories (ss 22(2),
  31(2)(b)), the category A to D acts of violence and their minimum and maximum special financial assistance (s 11), the
  counselling-at-any-time circumstances (s 23(5)) and longer variation periods (s 48(2)(c)). The s 72 Gazette notices of
  indexed maximums are not deposited either: the amount questions take the maximum in force as an input (0 means the
  Act's figure), and a separate question works the s 72 formula from the CPI figures. The Act's own figures are used
  otherwise: $60 000 (s 10(1)), $20 000 (ss 10(2)(c), 14(3)(a)), $50 000 (ss 14(1), 16(1)), 3 and 10 years (s 23),
  6 months (s 27), 10 years (ss 36(5), 48(2)(a)), 28 days (ss 45(2), 46(2)), ages 18, 24 and 28 (ss 23, 48, 74).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file in this folder, since deleted, and showed as an error).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `voc-dates.l4` | 0 | 0 | 0 | 0 |
| `voc-rules.l4` | 0 | 0 | 0 | 0 |
| `voc-seat.l4` | 0 | 0 | 0 | 0 |
| `voc-cases.l4` | 0 | 0 | 194 | 194 |

Every exported question has cases, with the edges: the loss of earnings cap at $19 999, $20 000 and $20 001; the
$60 000 and $50 000 caps exactly and $1 over; an indexed maximum given; deductions and interim assistance larger than the
award (never below zero); insurance against a related victim's distress amount (s 18(2)); the last day of every period
and the day after (3 years, 10 years, 6 months, 28 days, turning 18, 24 and 28); turning 18 on the day of the crime and the
day after; 29 February and month ends; the s 72 rounding at a 5 and the no-reduction rule; every constructor of every
choice that changes an answer.

## Seat

**The victim who applies for financial assistance** (`voc-seat.l4`): a primary victim (injured by an act of violence
against them, injured trying to arrest, prevent or rescue, or a child injured by exposure), a secondary victim (injured by
witnessing it, or a parent of a child victim injured on learning of it), a related victim (close family member, dependant
or intimate partner of a person killed), and the person who paid that person's funeral. "Am I a victim under the scheme?",
"How much can I be paid?", "Can I get special financial assistance?", "By when must I apply?", "Can my late application be
decided?", "Must my application be refused?", "Has my application lapsed?", "Can I have the decision reviewed, and by
when?", "By when can I apply to vary?", "How much can I be made to repay?".

No seat for the scheme decision maker, VCAT, the police, the State or the offender. The decision maker's satisfactions,
opinions, determinations and decisions to take amounts into account are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; the Regulations and the Gazette notices are
  not deposited, so their numbers are asked (see Edition).
- **The actors the text names.** Followed: primary, secondary and related victim, the person who incurred funeral
  expenses, the applicant, the scheme decision maker and its delegate, VCAT, the police, a legal practitioner or other
  person representing the applicant.
- **Judgments answered conditionally.** Followed: "determined by the scheme decision maker to be an injury" (s 3(3)),
  "considers that it is reasonable" (s 3(2)), "is satisfied" (ss 11(2), 31(1)(a)), "considers ... special circumstances"
  (s 31(2)(a)), "considers that it is appropriate" (s 24), "exceptional circumstances" (ss 10(3), 14(3), 16(3)), "may
  take into account" (s 18(1)(b)), "actually and reasonably incurred" (the amounts are the amounts accepted) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: act of violence, criminal act, relevant offence
  (as a choice of its heads), injury, significant adverse effect, close family member, primary, secondary and related
  victim. Asked: dependant (one fact covering s 3(1)(a), (b)), intimate personal relationship (undefined), child abuse
  (Child Wellbeing and Safety Act 2005), family violence and domestic partner (Family Violence Protection Act 2008),
  sexual offence (as a fact in the time-limit question), guardian (with the s 3(1) exclusions in the `@desc`).
- **One case.** One applicant and one act of violence (a series of related criminal acts is one act of violence, s 4(4);
  its day is the last act's, s 23(6)).
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3(1) definitions (act of violence, criminal act, relevant offence, injury, significant adverse effect, close
family member), s 3(2), (3), (4); s 9 (primary victims, including (5) for special financial assistance), s 10, s 11,
s 13, s 14, s 15, s 16, s 17, s 18, s 19, s 20 (in the question descriptions); s 22(1)(e), (2); s 23; s 24; s 25(2);
s 27; s 31; s 36(5); s 37(3); s 40; ss 44, 45, 46; s 48(2); s 50(1), (2), (4); s 72(1)-(3), (6); s 74(1)-(3), (9);
s 75.

**Regulative rules:** four. s 23 (DO apply WITHIN the days to the last day, LEST out of time; "at any time" with no
WITHIN), s 27 (DO respond WITHIN 6 months, LEST lapse), ss 45(2), 46(2) (DO apply for review WITHIN 28 days or the extended
time). Each is run by EVALTRACE inside an exported question that takes only dates and facts, through the helper the County
Court Act 1958 and Accident Compensation Act 1985 encodings use (a CONSIDER on an EVALTRACE matches FULFILLED only).

**Out, and why:**
- ss 1, 2, 5, 6, 7 (purposes, commencement, objectives, guiding principles, matters to consider): no fact test.
- s 4 (related criminal acts): the scheme decision maker's judgment; the person gives the day of the last act.
- s 8 (effect of a primary victim's death on their own eligibility): the seat is a living applicant; a deceased primary
  victim's family applies as related victims.
- s 12 (categories taken to be injured without evidence): regulations not deposited; evidence, not eligibility.
- s 21 (who may apply on another's behalf), s 22(1)(a)-(d), (f) (form and content), s 26 (withdraw or amend before
  decision, written notice): procedure with no fact test beyond the right itself; s 21(6) keeps the victim the applicant.
- ss 28-30, 32-35 (standard of proof, expedition, no hearings, the matters for reasonable time, character, the decision
  and its notice): the decision maker's process; s 33's matters are its judgment. s 34(2) is reflected in the victim
  questions.
- ss 36(1)-(4), 37(1), (2), (4), 38, 39, 41, 42, 43, 47, 49, 51 (payment form, interim assistance, creditors, costs paid
  to representatives, recognition meetings, assignment to the State, other remedies, notices): the decision maker's
  powers or procedure; s 41 is discretionary and named in the s 40 question.
- Part 5 (ss 52-59) and ss 67-71, 73: administration, information gathering, confidentiality (an official's duty),
  guidelines, complaints, reports, the Consolidated Fund, trusts, review of the Act, regulations.
- ss 60-66 (publication, admissibility, cross-examination, fraud, false information): offences and evidence rules outside
  the claims focus; worth a question later ("Can I publish my decision?", s 62(3)).
- s 74(4)-(8): the decision maker's powers on a Tribunal award variation.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 23, 27, 36(5), 48(2), 74(2) "within 3 years after", "within 6 months", "within 10 years after", "within 6
  years after" -- `the same day ... years after`, `the same day ... months after` -- the period ends at the end of the
  same day of the month that many years or months later; where that month has no such day, its last day (29 February
  plus 3 years is 28 February) -- the day before the anniversary, or 1 March.
- **F2** s 3(1) "significant adverse effect ... includes" -- `s 3 -- the harm is a significant adverse effect` -- an open
  list read as closed over the choices offered (only property loss and no harm fail) -- NOTHING outside grief, distress,
  trauma or injury.
- **F3** ss 3(4), 9(5), 11(1) -- `s 11 -- the special financial assistance I can be paid` -- the act of violence for a
  person with only a significant adverse effect is not asked to have "resulted in injury" (s 3(4)(b) reads it as if
  they had) -- the definition's injury limb applied as written.
- **F4** s 18(1), (2) -- `s 18 -- the amount after the reductions` -- the reductions come off the amount after the caps;
  insurance and superannuation cannot reduce the part of it that is for distress (s 16(2)(c)), counted first within the
  cap -- the reductions come off each head before the caps (more generous where the heads exceed the cap), or the
  distress counted last.
- **F5** s 23(1), (2), (4) -- `s 23 -- the time for applying` -- where more than one period applies, the latest governs
  (s 23(4)'s "Despite subsection (1)" read as extending, never shortening; finding 1) -- s 23(4) replacing (1) for the
  victims it reaches.
- **F6** s 40 -- `s 40 -- I must be given a victim recognition statement` -- a duty whose "if" or request is unmet:
  JUST FALSE -- NOTHING (the Act is silent outside the duty).
- **F7** ss 48(2)(b), 74(2)(b) "at any time until the person turns 28 [24]" -- the last day is the day before the
  birthday -- the birthday itself.
- **F8** s 50(2), (4) -- `s 50 -- the most I can be required to repay` -- the two together never exceed the assistance
  paid -- added without a ceiling (s 50(4) is a separate power).
- **F9** s 72(2) "made to 4 decimal places" -- `rounded half up to 4 decimal places` -- rounded half up to 4 places,
  then to the dollar (so 100.49996 gives $101) -- truncated to 4 places, or the 4 places not used in the dollar rounding.
- **F10** s 23(2), (3), (4) "the victim was under [at least] the age of 18" -- the applicant victim's own age (for a
  related victim, theirs, not the deceased's) -- the primary victim's age.
- **F11** ss 3(1), 15(1) -- `s 15 -- I am a related victim` -- the relationship facts are asked once, as true both at the
  act and at the death (finding 3) -- asked separately for each time.
- **F12** s 13(1), (3) -- `s 13 -- I am a secondary victim` -- an offender present at the scene is not excluded by s 13
  (JUST TRUE; finding 2) -- NOTHING, or excluded by analogy with ss 9(6), 15(2).
- **F13** s 31 -- `s 31 -- my application must be refused` -- no ground: JUST FALSE (s 31 does not require refusal; the
  decision under ss 33, 34 is still to come) -- NOTHING.

Two sites follow the case-by-case convention without a fork line of their own: s 17 outside a person who incurred funeral
expenses for a primary victim who died answers NOTHING (a grant limited in its own wording); a review question where no
review is open answers NOTHING for "in time" (silent).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "is a person who" definitions of primary, secondary and related victim (ss 9, 13, 15, with s 9(4)'s
prescribed category asked as a fact), the "means" definitions of act of violence, criminal act and injury, the "is not"
exclusions (ss 9(6), 13(3), 15(2)), the "if" conditions of ss 11(1), 22(1)(e), 31(1), 40, the "unless" and "only if" of
s 75, the "not required if" of s 22(2), the periods of ss 23, 27, 36(5), 45, 46, 48, 74 and the "only once" of s 74(3)
give `JUST FALSE`; s 17 outside its grant and the review time where no review is open give `NOTHING` (*limited by its own
wording*, *silent*).

## What the Act turns out to say

1. **s 23(4) can shorten a related victim's time.** s 23(1)(b) gives a related victim 3 years after the death; s 23(4)
   says "Despite subsection (1)" an application "may be made within 10 years after the occurrence of an act of violence"
   for an adult victim of a sexual offence or family violence. Where the death comes more than 7 years after the act, read
   literally as displacing (1), s 23(4) would give the related victim less time than (1)(b). Encoded as the later of the
   two (F5). Asserted.
2. **s 13(3) excludes the offender only under s 13(2).** ss 9(6) and 15(2) exclude a person who "committed, and is
   criminally responsible for" the act of violence from being a primary or related victim; s 13(3) does so for a secondary
   victim only "under subsection (2)" (the parent who learns of it later). A person present at the scene who committed the
   act and was injured by witnessing it is not excluded by s 13 itself (F12); s 33 (character and behaviour) would reach
   them. Asserted.
3. **Close family membership is tested at two different times.** s 15(1) asks whether the person "at the time of the
   occurrence of the act of violence" was a close family member or dependant; the s 3(1) definitions test the
   relationship and the dependency "at the time of the victim's death". Where the victim lingers, a person who married or
   came to depend on the victim between the act and the death fits the definition but not s 15. Facts asked once (F11).
4. **The funeral expense payer gets none of the extended times.** s 23(2) to (5) speak of an application "by or on behalf
   of a victim"; "victim" (s 3(1)) means a primary, secondary or related victim, so a person applying only for funeral
   expenses (s 17) has only s 23(1)(b), whatever their age or the nature of the crime. Asserted.
5. **s 17(2) and s 20 pull against each other.** s 20: "A person is eligible to apply for, or receive, assistance in
   respect of a single act of violence in one capacity only"; s 17(2): funeral assistance for a secondary or related victim
   "is in addition to any assistance under Division 2 or 3". Read together, s 17(2) is an exception to s 20; s 31(1)(c)
   (an earlier application "in any capacity" must be refused) would then bar a second, separate funeral application, so
   the funeral expenses are best claimed in the same application. Noted in the question descriptions; not encoded as a
   bar.
6. **Delegates' decisions cannot go straight to VCAT.** s 44(1)(a) makes decisions "made by the scheme decision maker or a
   delegate" reviewable, but s 46(1) gives VCAT review only of a reviewable decision "made by the scheme decision maker";
   a delegate's decision goes to internal review (s 45), and the internal review decision (deemed the scheme decision
   maker's, s 45(5)) then to VCAT. Only the internal review time may be extended under this Act (s 45(3)). Asserted.
7. **The secondary victim's loss of earnings cap has no "higher prescribed amount".** s 10(2)(c) reads "of up to $20 000
   or the higher prescribed amount"; s 14(3)(a) reads "of up to $20 000" alone, though s 72(6) indexes both. Encoded with
   the same indexed input for both.
8. **A child exposed to violence with no injury gets no special financial assistance.** s 11(1)(a)(ii) reaches "a primary
   victim ... referred to in section 9(3)", and s 9(3) needs the child to be "injured"; s 9(5), which lets a significant
   adverse effect suffice, covers only an act "committed against the person". The question's input is worded "injured by
   hearing, seeing or being exposed to it" accordingly.
9. **Double rounding in s 72(2).** "A calculation ... is to be made to 4 decimal places but ... is to be rounded to the
   nearest whole dollar (with a calculation that ends in 5 being rounded up)". Taken literally, a figure such as $100.49996
   becomes 100.5000 and then $101 (F9). Asserted.
10. **s 18 does not say whether the reductions come before or after the caps** (F4); nor how a payment covering several
    heads is split between them. Asserted on the reading taken.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- Deposit the Victims of Crime (Financial Assistance Scheme) Regulations 2024 (prescribed categories, special reporting
  categories, the special financial assistance categories and amounts, higher prescribed amounts) and the s 72 Gazette
  notices; then replace the inputs with the figures.
- A lawyer's view on findings 1, 3, 5 and 10 and forks F4, F5 and F9, an independent test pass and a human gate.
