# Powers of Attorney Act 2003 (NSW) -- baseline encoding, the principal (and the family member or beneficiary)

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 2 March 2025). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). Two regulative rules (the attorney's
prohibition on acting knowing the power has ended, s 49; the six months for a s 23 application), each run by
`EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except
in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. It is part of a run of baseline encodings of the
NSW Acts a person meets when bringing or answering a claim. For claims work the Act matters where an injured or
elderly person's affairs are run by an attorney: whether the power is enduring and survives incapacity, what the
attorney may do with the person's money (gifts, benefits to the attorney), when a substitute may act, when the power is
suspended by financial management, who may ask a tribunal to review it, and a will beneficiary's claim to what is left
of property the attorney sold (ss 22, 23, with a six-month time limit).

## Edition

- **Act:** Powers of Attorney Act 2003 No 53, corpus document `nsw_legislation:2025-03-02/act-2003-053` (in force
  2 March 2025), deposited at `../../registers/source-bundle/act-2003-053.txt` (sha256 0f13650b...2aa52 as committed),
  taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot
  challenge. Not the authorised text.
- **Not deposited:** the Powers of Attorney Regulation (the s 8 prescribed form, the s 19(2)(e) prescribed witnesses,
  the s 5(g) vacancies, the s 25(3) exclusions, the s 44(1)(a)(ii) certifiers), the Minister's s 19(2)(c) course order,
  the commencement proclamation (s 2), the NSW Trustee and Guardian Act 2009 (managed estates, s 83), the Guardianship
  Act 1987 and the Conveyancing Act 1919 provisions continued by s 6(3). What they decide is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `poa-dates.l4` | 0 | 0 | 0 | 0 |
| `poa-core.l4` | 0 | 0 | 0 | 0 |
| `poa-seat-family.l4` | 0 | 0 | 0 | 0 |
| `poa-cases.l4` | 0 | 0 | 147 | 147 |
| `poa-cases-family.l4` | 0 | 0 | 51 | 51 |

Every expected value was worked by hand from the text, with the edges: each s 19(2) witness, in and out of the
definition; the witness who is an attorney; nominal consideration against a statement of valuable consideration (s 15);
each s 16 event; each Schedule 3 recipient and expense, an unreasonable value, an unnamed third party; each s 5 vacancy;
joint, several, and joint and several attorneys, before and after the 2013 amendment; the 1 July 1920 day and the day
before (s 52); leases of 36 and 37 months (s 52(4)); the last day of the s 23 six months and the day after, across a
short February (2026 and leap 2024) and a year end, an application on or before the day of the grant, and an extension
after expiry; the general power reviewed in NCAT and in the Supreme Court (s 33(3)); a second application to the other
tribunal, withdrawn with approval and not (s 27). Mirror cases put the same review facts to both seats.

## Seats

**First seat, the principal** (`poa-core.l4`): the person who gives the power of attorney (s 3(1)). Every exported
question is one the principal would ask ("Is my power enduring?", "Is it irrevocable?", "Can my attorney act for me in
something I can no longer understand?", "Can my attorney give this gift, or use my money for themselves?", "Can my
substitute act now?", "Is my power suspended because my estate is managed?", "Can I revoke it now?", "Can I ask for a
review?"). The attorney's duty under s 49 is encoded as what it means for the principal ("Has my attorney committed an
offence?").

**Second seat, the family member, named beneficiary or other interested person** (`poa-seat-family.l4`): a beneficiary
under a deceased principal's will whose gift the attorney sold or dealt with (ss 22, 23), or a relative, guardian or
friend who wants a tribunal to look at the power (ss 35, 36). It imports `poa-core.l4` and uses the same review rule
(`may apply for a review`), so the two seats cannot disagree; mirror cases check it.

The attorney gets no seat of their own; one could be added (s 38 advice and directions, ss 47, 49). Officials (the
Supreme Court, NCAT, the Registrar-General, the NSW Trustee and Guardian) get no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; the regulations are not deposited, so what
  they prescribe is asked (see Edition). The Act's own numbers (6 months in s 23(3), 3 years in s 52(4), 1 July 1920
  in s 52(1), 5 years' imprisonment in ss 44(5) and 49) are in the L4.
- **The actors the text names.** Followed: principal, attorney, substitute attorney, third party, named beneficiary,
  guardian, enduring guardian, review tribunal, Supreme Court, NCAT.
- **Judgments answered conditionally.** Followed: reasonableness of gifts and benefits (Schedule 3), the Court's view
  under ss 28-31, the tribunal's satisfaction and opinion under ss 35, 36, and good faith (s 48) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: ss 4 (incommunicate), 5 (vacancy), 3(1)
  (valuable consideration), 8 (prescribed power), 15 (irrevocable), 19 (enduring, prescribed witness), 22(6) (named
  beneficiary), 25(5) (interstate enduring power), 44(1) (certified copy) and Schedule 3 cl 1(3) (relative, close
  friend) are worked out. Departure: the composite questions (for example ss 18 and 21, s 50) take "my power is
  enduring" or "irrevocable" as a yes/no, with the `@desc` pointing to the question that works it out, rather than
  repeating every s 15 and s 19 fact in each question.
- **One case.** One power of attorney (and, for ss 22, 23, one deceased principal's estate).
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (definitions, as used); s 4 (incommunicate); s 5 (vacancy); s 6 (which law governs); s 8 (prescribed
power); s 10 (no trustee functions); ss 11, 12, 13 and Schedule 3 (gifts and benefits); s 15 (irrevocable); s 16 (what
does not end it); s 17 (initial incapacity); s 18 (supervening incapacity); s 19 (enduring); s 20 (acceptance); s 21
(effect of an enduring power); s 22 (ademption and the beneficiary's interest; real and personal estate); s 23 (the
application and its six months); s 25 (interstate enduring powers); s 27 (one tribunal at a time); s 28 (Court may end
an irrevocable power); ss 29-32 (confirmation orders and their effect); s 33 (reviewable powers, which tribunal); s 35(1)
(interested persons); s 36(3)(b), (4), (5) (invalidity, operational orders, no revocation while declared incapable);
s 44(1) (certified copies); s 45 (delegation); s 45A (substitutes); s 46 (joint and several attorneys); ss 47, 48
(reliance after termination); s 49 (offence) with s 54(1); s 50 (managed estates); s 52 (registration for deeds
affecting land).

**In comments only:** s 7 (general law preserved: the source of many `NOTHING` answers); s 9 (authority of a
prescribed power, behind the express-words answers of ss 11-13); s 14A and Sch 5 cl 6 (amendments do not change an
existing authority); s 26 (the two tribunals, as an enumeration); s 36(3)(a), (3A), (6)-(11) (other orders and their
effect); s 42 (procedure for an incommunicate principal, in a `@desc`); s 44(2)-(5); Sch 5 cls 3, 10.

**Out, and why:** ss 1, 2, 53, 56, 57 and Sch 5 cls 1, 2, 5: machinery. s 14 (regulations may amend Schedule 3):
machinery. s 24 and Sch 5 cl 4 (the repealed shared-home rule, kept for intestacies before 2010): spent for any death
now. ss 34, 35(2)-(5), 37, 38: the tribunals' own procedure, referral and powers to treat an application as one for a
financial management order, and the attorney's application for advice (an attorney seat would take s 38). s 43 (the
attorney may sign in their own name): no question the principal asks turns on it. s 51 (registration is permitted):
encoded only through s 52. s 50(9)-(12) (Supreme Court's further powers and the protected-estate declaration): court
powers with no fact the principal could state beyond those asked. Schedule 1 (the Conveyancing Act 1919 Part 16 and
Schedule 7, continuing for powers executed before the Act commenced): a separate body of law; s 6 tells the person
which applies (fork F1). Sch 5 cls 7-9: transitional, spent or covered by the questions' assumptions.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 6 -- every question except `Which law governs my power of attorney` and the review, s 25 and s 52
  questions -- the power is assumed to be created by an instrument executed on or after commencement; an older power
  is not asked about -- ask the s 6 fact in every question and answer `NOTHING` for an older power under Parts 2-4 and
  Part 6 Divisions 1-2.
- **F2** s 19(2)(c) "a licensee under the Conveyancers Licensing Act 2003, or an employee of the NSW Trustee and
  Guardian or a trustee company ..., who has successfully completed a course of study approved by the Minister" --
  `is a prescribed witness` -- the course requirement is read as attaching to the licensed conveyancer as well as to
  the two employees -- it attaches only to the employees (finding 3).
- **F3** s 20(1) "does not operate to confer any authority ... until" -- `Is this attorney still barred from acting
  under my enduring power` -- ruling (d) of 2026-11-05: the bar is encoded (`JUST TRUE` before acceptance, `JUST FALSE`
  after); the answer never claims the attorney has authority -- answer "has authority" `JUST TRUE` after acceptance.
- **F4** s 18 "is effective to the extent that" -- `Can my attorney act for me in something I cannot understand` --
  for an act beyond the principal's understanding under a power that is neither enduring nor irrevocable, `NOTHING`
  (a grant limited in its own words, no "only"; the general law, kept by s 7, decides) -- `JUST FALSE`, reading s 18
  with the note to it and s 3(3)(a) as making such a power ineffective (finding 1).
- **F5** ss 11(1), 12(1), 13(1) "unless the instrument ... expressly authorises" -- the gift and benefit questions --
  where the instrument expressly authorises it in its own words, `JUST TRUE` (with s 9(1)) -- `NOTHING`, the
  instrument's construction under the general law deciding (the notes to ss 11-13 say so).
- **F6** s 45(2) "Nothing in this section enables an attorney irrevocably to appoint ... unless" -- `Can my attorney
  appoint someone else to act` -- `JUST FALSE` -- `NOTHING`, since s 45(2) only says this section does not enable it.
- **F7** s 50(14) "This section has effect subject to Part 3" -- `Is my power suspended because my estate is managed`
  -- for an irrevocable power, `NOTHING` -- `JUST FALSE`, reading s 16(1)(d), (d1) as keeping an irrevocable power
  effective while the estate is managed (finding 4).
- **F8** s 35(1)(d) "any other person who, in the opinion of the review tribunal, has a proper interest" -- `may apply
  for a review` -- a person outside (a)-(d) is `JUST FALSE` (the four heads cover everyone, the last on the tribunal's
  opinion) -- `NOTHING`, the list not being closed with "only".
- **F9** s 23(3) "within 6 months from the date of the grant" -- `the last day to apply under s 23`, `By what day must I
  apply to the Supreme Court under s 23`, `Is my s 23 application in time` -- the six months end on the same day of the
  month six months after the grant, or that month's last day where shorter (31 August -> end of February); an
  application on that day is in time -- the Interpretation Act 1987's counting rules (not deposited) might give another
  end day.
- **F10** s 23(3) -- `Is my s 23 application in time` -- an application filed before the grant is counted as made on
  the day of the grant, so in time -- such an application is premature and not "within 6 months from" the grant.
- **F11** s 23(1) "On the application of a named beneficiary ... or such other person as the Supreme Court considers has
  a proper interest" -- `Is my s 23 application in time` -- someone who is neither answers `JUST FALSE` -- `NOTHING`.
- **F12** s 36(12) "This section has effect subject to the provisions of Part 3" -- `Can the tribunal remove the
  attorney or change the power` -- for an irrevocable power, `NOTHING` -- `JUST FALSE` for orders that would revoke or
  vary it, reading s 16 as protecting it from them.
- **F13** s 46 -- `Does a vacancy end my power of attorney` -- a sole attorney's vacancy answers `NOTHING` (s 46 is
  about two or more attorneys; the general law decides, and s 45A may let a substitute act) -- `JUST TRUE`.
- **F14** s 47 "an act that would have been within the scope of the power" -- `Can my attorney rely on the power after
  it ended` -- an act outside the scope answers `NOTHING` -- `JUST FALSE`.
- **F15** s 49 -- `The most my attorney can be imprisoned for under s 49` -- returns 0 where s 49 is not broken on the
  facts, rather than `NOTHING` -- a `MAYBE NUMBER`.
- **F16** s 33(2), (3) with s 6(6)(a) -- the review questions -- an older "protected" power counts as enduring (said in
  the `@desc`), and a review of a revocation of an enduring power is covered by the same answer -- separate inputs.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 10, 11(1), 12(1), 13(1) | the attorney under a prescribed power | no power (disability) unless expressly authorised | the trustee, gift and benefit questions |
| s 20(1) | the attorney under an enduring power | no power until acceptance | `Is this attorney still barred ...` (an "until" bar) |
| s 23(3) | the applicant | duty with a deadline (6 months from the grant), relievable by extension | MUST rule, WITHIN the days to the last day |
| s 27(2) | the applicant for review | disability: no second application elsewhere | `may apply for a review` |
| s 36(5) | the principal | disability: no revocation while declared incapable | `Can I revoke my enduring power now` |
| s 45(1) | the attorney | disability: no delegation unless express | `Can my attorney appoint someone else to act` |
| s 47, 48(1) | the attorney; the third party | privilege to rely on the power | the two reliance questions |
| s 49 | the attorney | prohibition, offence (5 years, on indictment) | SHANT rule |
| s 52(1) | the principal's land | deed without effect unless registered | `Is my attorney's deed ... without effect ...` |

## What the Act turns out to say

1. **The Act never says an ordinary power ends on incapacity.** s 18 says a power is effective "to the extent" the act
   is within the principal's understanding, and s 3(3)(a) speaks of a power "suspended or restricted in operation by
   reason of mental incapacity", but no section suspends it. The familiar rule is the general law (s 7). Fork F4;
   asserted (`NOTHING`).
2. **The heading "Divisions 5" followed by "39-41 (Repealed)" and then "Division 7"** suggests the corpus rendering lost
   the words "and 6" (Divisions 5 and 6 repealed). Nothing turns on it here; check the official text.
3. **s 19(2)(c) is ambiguous** on whether a licensed conveyancer must also have completed the Minister's course. The
   comma placement reads most naturally as applying the course to all three; the encoding takes that (fork F2) and
   asserts a conveyancer without the course is not a prescribed witness.
4. **"Subject to Part 3" (ss 36(12), 50(14)) points to a Part that does not speak of tribunal orders or managed
   estates.** s 16 protects an irrevocable power against the principal's acts, incapacity, bankruptcy and death, not
   against a tribunal or financial management. What the cross-references take away is unclear. Forks F7, F12;
   asserted (`NOTHING`).
5. **s 23(3) runs from "the grant or resealing in this State"**: where probate is granted elsewhere and resealed in
   NSW, the NSW resealing is the start. The question asks for one date, the NSW grant or resealing.
6. **s 46(1A) needs both limbs.** A joint power that says it continues still ends when no attorney or substitute
   remains; and Sch 5 cl 10 leaves powers made before the 2013 amendment under the earlier s 46, whose text is not in
   the deposited Act (asserted `NOTHING`).
7. **The s 44 certifiers are in a repealed regulation.** Sch 5 cl 3 keeps the classes of the Conveyancing (General)
   Regulation 2003 cl 49 "until a regulation is made"; neither is deposited, so whether a certifier is in the class is
   asked.
8. **ss 22 and 23 give a named beneficiary a claim with its own time limit** (6 months from the grant, extendable even
   after expiry), separate from family provision claims under the Succession Act 2006. A beneficiary reading only the
   Succession Act would miss it.
9. **Every offence under the Act is indictable** (s 54(1)): knowingly false certification (s 44(5)) and acting knowing
   the power has ended (s 49) both carry 5 years' imprisonment.

## Questions (exported)

`poa-core.l4` (25), the principal: `Which law governs my power of attorney` (s 6), `Does my document create an enduring
power of attorney` (s 19), `Is this attorney still barred from acting under my enduring power` (s 20), `Does my
document create an irrevocable power of attorney` (ss 3, 15), `Does this event end my irrevocable power` (s 16), `Can
the Supreme Court end my irrevocable power` (s 28), `Can my attorney act for me in something I cannot understand`
(ss 16, 18, 21), `Can my attorney do an act I could not understand when I gave the power` (ss 17, 32), `Can the Supreme
Court confirm my power of attorney` (ss 4, 29-31), `Can my attorney act as trustee in my place` (ss 8, 10), `Can my
attorney give this gift of my property` (s 11, Sch 3 cl 1), `Can my attorney use my property to benefit themselves or
another` (ss 12, 13, Sch 3 cls 2, 3), `Can my attorney appoint someone else to act` (s 45), `Can my substitute attorney
act for me now` (ss 5, 20(4), 45A), `Does a vacancy end my power of attorney` (ss 5, 46), `Is my power suspended because
my estate is managed` (s 50), `Can my attorney rely on the power after it ended` (ss 47, 48(2)), `Can a person who dealt
with my attorney rely on the power` (s 48(1)), `Has my attorney committed the s 49 offence` (s 49, with the SHANT rule),
`The most my attorney can be imprisoned for under s 49` (ss 49, 54), `Can I revoke my enduring power now` (s 36(5)),
`Can I apply for a review of my power of attorney` (ss 4, 27, 33, 35), `Does my interstate enduring power work in NSW`
(s 25), `Is this a certified copy of my power of attorney` (s 44), `Is my attorney's deed affecting my land without
effect for want of registration` (s 52).

`poa-seat-family.l4` (7), the family member, beneficiary or interested person: `Do I keep my interest in what is left
from the attorney's dealing` (s 22(1), (5)-(7)), `Is it real estate or personal estate` (s 22(2)-(4)), `By what day must
I apply to the Supreme Court under s 23` (s 23(3)), `Is my s 23 application in time` (s 23(1), (3), (4), with the MUST
rule), `Can I apply for a review of the power of attorney` (ss 4, 27, 33, 35), `Can the tribunal declare the power
invalid` (s 36(3)(b)), `Can the tribunal remove the attorney or change the power` (s 36(4), (12)).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation
  (finding 2).
- Deposit the Powers of Attorney Regulation (the prescribed form, witnesses, vacancies, certifiers, exclusions) and
  work its lists out instead of asking them.
- Have a lawyer review the forks, especially F2 (conveyancers), F4 (ordinary powers and incapacity), F7 and F12
  ("subject to Part 3").
- An attorney seat (ss 38, 43, 47, 49) and links to the Guardianship Act 1987 and NSW Trustee and Guardian Act 2009
  encodings, if they are made.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
