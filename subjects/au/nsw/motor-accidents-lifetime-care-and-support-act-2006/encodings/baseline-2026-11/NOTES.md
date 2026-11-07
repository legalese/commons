# Motor Accidents (Lifetime Care and Support) Act 2006 (NSW) -- baseline encoding, the injured person (and s 54's owner or driver)

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 1 July 2021). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer; enumerated answers carry a "the Act does not
say" constructor instead). Two regulative rules (the participant's 28 days to ask for an assessor, s 24(2), and to refer
an assessor's determination for review, s 25(2)), each run by `EVALTRACE` inside an exported question that takes only
plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The focus is the provisions an injured person
meets: whether the Act reaches the injury, eligibility, applying and acceptance, how long participation lasts, the pause
in the damages time limit, what the Authority pays for, the disputes and their time limits and costs. s 54 (recovery
from an uninsured owner or driver) is encoded from that person's seat, in its own module.

## Edition

- **Act:** Motor Accidents (Lifetime Care and Support) Act 2006 No 16, corpus document
  `nsw_legislation:2021-07-01/act-2006-016` (in force 1 July 2021), deposited at
  `../../registers/source-bundle/act-2006-016.txt` (text sha256 0395999e...4975e8db as committed, matching
  the `.meta.json`), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited:** the LTCS Guidelines (s 58: the eligibility criteria, the assessment methods, application time
  limits), the regulations (excluded and prescribed treatment and care needs, s 5A; maximum fees, s 32; maximum legal
  costs, s 21(3)), the Motor Accidents Compensation Act 1999 (motor accident, s 3B cover, Chapter 3), the Motor Accident
  Injuries Act 2017, the Limitation Act 1969 and the Interpretation Act 1987. What they decide is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ltcs-dates.l4` | 0 | 0 | 0 | 0 |
| `ltcs-scheme.l4` | 0 | 0 | 0 | 0 |
| `ltcs-seat-owner-driver.l4` | 0 | 0 | 0 | 0 |
| `ltcs-cases.l4` | 0 | 0 | 128 | 128 |
| `ltcs-cases-owner-driver.l4` | 0 | 0 | 26 | 26 |

Every expected value was worked by hand from the text, with the edges: the 16th birthday on the day of the accident
and the day after (s 3); an accident on 1 October 2007 and the day before (s 4(1)); the third birthday on and the day
after acceptance (s 9(5), (5A)); acceptance and birthdays on 29 February; the last day of interim participation and the
day after (ss 9, 11(2)); the day count over the whole two years (730 days) and to a lifetime acceptance (292 days); the
28th day after a certificate and the 29th (ss 24(2), 25(2)), across February and a year end; a request before the
certificate; a contribution or legal cost equal to, one dollar under and one dollar over its cap (ss 11AA(2), 21(4));
contributory negligence of 0, 25, 100 and 101 per cent (s 54(2)); each defence proved and not (s 54(7), (8)).

## Seats

**The injured person** (`ltcs-scheme.l4`): the person who suffered the motor accident injury, or a parent, guardian or
other person acting for them, who is or may become a "participant in the Scheme". The questions are theirs ("Does the
Act apply to my injury?", "Am I eligible?", "Who can apply for me?", "Must the Authority accept me?", "Until when am I
an interim participant?", "Does the time limit for my damages claim stop running?", "Will the Authority pay for
this?", "Where does my dispute go, and by when?", "Must I comply with this request?", "Will the Authority pay my legal
costs?").

**The owner or driver of an uninsured vehicle, or another person at fault** (`ltcs-seat-owner-driver.l4`): s 54 makes
them liable to the Authority for the present value of its treatment and care liabilities, with defences. Their
questions: "Can the Authority recover from me?" and "How much?". The two modules share no names and neither imports the
other; no question turns on both, so there are no mirror cases.

No seat for the Authority, the assessors, the panels, the Personal Injury Commission, the State Insurance Regulatory
Authority or the insurer: what they do is encoded as what it means for the person in the seat. (The insurer of a claim
is a party the Act gives powers to, ss 8, 14, 15; it could have a seat later.)

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed, but the instruments are not deposited: the
  regulations' maximum legal costs (s 21) and the Guidelines' criteria (s 7) are inputs. The Act's own numbers (16 years,
  1 October 2006 and 2007, 3 and 5 years of age, 2 years, 28 days, 3 assessors) are encoded.
- **The actors the text names.** Followed: the Authority, the insurer of a claim, assessors, Assessment and Review
  Panels, the Commission, approved providers, the owner and driver, the court.
- **Judgments answered conditionally.** Followed: the Authority's satisfaction (s 9), its assessment (s 11A), its
  opinion of special circumstances (s 11B(2)), what is reasonable or necessary (ss 11A, 11AA, 17, 27), the grounds for
  review (ss 15, 25), the court's satisfaction on the s 54 defences, and the shares in responsibility (s 54) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "relevant Scheme commencement date", "motor
  accident injury" (from "caused by a motor accident"), "treatment and care needs" (s 5A), "assessed treatment and care
  needs", "approved provider" (as required) and "present value of treatment and care liabilities" are worked out;
  "motor accident", "motor accident insurance cover", "third-party policy" and Chapter 3 of the 1999 Act are asked.
- **One case.** One person, one motor accident injury.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (relevant Scheme commencement date, motor accident injury); s 4 (application); s 5A (treatment and care
needs); s 7 (eligibility); ss 7A, 7B (buying in); s 8(1), (2) (who may apply; s 8(3)-(6) in comments); s 9 (acceptance
and duration); s 11(2) (the pause in time limits; s 11(1) in a comment); ss 11A, 11AA, 11B, 11C (payments); ss 14, 15
(eligibility disputes and review); ss 17, 18 (costs of eligibility disputes); s 20 (motor accident injury disputes);
s 21 (legal costs of those disputes); ss 23-25, 27, 29 (treatment and care needs assessment, disputes, review,
co-operation, legal costs); s 54 (recovery from the owner or driver, or another person at fault); Schedule 3 cl 2 (in a
comment).

**Out, and why:** ss 1, 2 (name, commencement); s 5 (borrowing the 1999 Act's meanings: applied by asking); ss 12, 13,
22 (definitions of panels and the appointment of assessors); ss 16, 26 (determinations and assessments final and
binding: no question of the person turns on them beyond what is asked); s 19, s 28 (Guidelines on procedure); Part 5
(ss 30-32: what the Authority pays hospitals and providers, at rates set by Gazette orders and regulations not
deposited; s 31(3) is the provider's right); Part 6 (the Authority, its chief executive and functions); Part 7 except
s 54 (the Fund and its levy); ss 56-60, 62-64 (contracting out, Crown, Guidelines, service, information exchange,
protection of assessors, regulations, offences); ss 66, 67 (spent reviews); Schedule 1 (the chief executive);
Schedule 3 cll 1, 3, 4 (savings and transitional). Damages for the injury, and the time limits themselves, are in other
Acts (the Motor Accidents Compensation Act 1999, the Motor Accident Injuries Act 2017, the Limitation Act 1969).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 7A(3)(a), 7B(3)(a) "would have been eligible ... had the motor accident occurred [immediately after the
  relevant Scheme commencement date / in New South Wales]" -- `the reach of the Act` -- the counterfactual moves only the
  date or the place, so s 4(3)'s insured vehicle is still required for a buy-in -- for s 7B, an interstate vehicle is
  treated as if it had NSW cover, so s 4(3) does not apply.
- **F2** ss 7A, 7B -- `the reach of the Act`, `the eligibility for` -- an accident both outside NSW and before the
  relevant Scheme commencement date: "the Act does not say" -- either buy-in reaches it (s 7B's "whether before or after
  the commencement of this section" read as covering any date), or neither does.
- **F3** ss 7A(1), 7B(1) "may be accepted as a lifetime participant" -- `the eligibility for`, `Must the Authority
  accept me as a participant` -- a buy-in whose injury meets only the interim criteria: "the Act does not say" -- not
  eligible (`JUST FALSE`), since the only acceptance on offer is lifetime.
- **F4** ss 7A(1), 9(2) -- `Must the Authority accept me as a participant` -- once the contribution is paid and the
  Authority is satisfied, s 9(2)'s "must accept" applies to a buy-in -- s 7A(1)'s "may be accepted" leaves the Authority a
  discretion even then.
- **F5** s 11A(1) "all of the reasonable expenses" -- `Will the Authority pay for this` -- an unreasonable expense is
  "the Act does not say" (a grant limited by its own words) -- the Authority need not pay it.
- **F6** s 9(5) "for a period of 2 years only" -- `the last day of interim participation for ... accepted on ...` -- the
  two years include the day of acceptance (last day: the day before the second anniversary); "until the person is 5"
  ends the day before the fifth birthday; an anniversary on 29 February falls on 28 February -- the Interpretation Act
  1987 s 36 (not deposited) excludes the first day, which would add a day.
- **F7** s 3(1) "under 16 years of age", s 9(5), (5A) "3 years of age", "5 years of age" -- `the age of someone born
  on ... on ...` -- a person born on 29 February reaches an age on 28 February in a common year -- on 1 March.
- **F8** s 11(2) "While a person is an interim participant ... time does not run" -- `How many days has my interim
  participation stopped time running` -- the days are counted from the day of acceptance to the last day of interim
  participation (or the day before lifetime acceptance), both ends included -- the day of acceptance is excluded, or the
  Limitation Act's own rules on suspension decide.
- **F9** s 54(3) -- `the Authority may recover under s 54 from` -- recovery from another person partly at fault stands
  apart from s 54(1)'s conditions (fault of an owner or driver, no third-party policy); s 54(6) and (11) still apply --
  s 54(3) is a rider on s 54(1), so it applies only where the vehicle was uninsured (the section heading names "third
  party tortfeasors" alongside uninsured vehicles, which supports either).
- **F10** s 54(2), (3) -- `How much can the Authority recover from me` -- for another person at fault, only that
  person's share is applied, not the s 54(2) reduction as well -- both apply.
- **F11** ss 24(2), 25(2) "more than 28 days after", "not later than 28 days after" -- the two rules -- the 28th day after
  the certificate is given is in time and the 29th is not (WITHIN 28 from day 0, the day given) -- the day of giving is
  day 1.
- **F12** s 5A(1) "the treatment and care needs ... are" -- `Will the Authority pay for this` -- something outside the
  list (and not prescribed) is not a treatment and care need, and the Authority is not required to pay -- `the Act does
  not say`.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| s 8(1), 7A(4), 7B(4) | the person, the insurer | power to apply; the insurer's disability for a buy-in | `Can this person apply for me` |
| s 9(2), (3) | the Authority | duty to accept | `Must the Authority accept me as a participant` |
| s 9(6) | the Authority | disability: no second interim acceptance | constructor `it cannot accept me as an interim participant again` |
| s 11A(1), 11B | the Authority | duty to pay; no duty (with a privilege to elect) | `Will the Authority pay for this` |
| s 24(1), (2) | the participant; the Authority | power to request within 28 days; duty to refer | MUST rule, WITHIN 28 |
| s 25(1), (2) | the participant | power to refer within 28 days, on grounds | MUST rule, WITHIN 28 |
| s 27 | the participant | duty to comply with reasonable requests | `Must I comply with this request` |
| s 54 | owner, driver, other person at fault | liability to recovery, with defences | `Can the Authority recover the participant's care costs from me` |

## What the Act turns out to say

1. **The text is as at 1 July 2021.** Later amendments are missing; the Act has been amended since (the deposited text
   already points to the Personal Injury Commission Act 2020). Check every answer against the current text.
2. **s 11(2) names only the 1999 Act.** Time stops for "section 109 ... of the Motor Accidents Compensation Act 1999 or
   a provision of the Limitation Act 1969". For an accident under the Motor Accident Injuries Act 2017 (from 1 December
   2017), the 2017 Act's own time limits are not named. In this version the Act's links to the 2017 scheme are partial:
   s 48 and the note to s 49 refer to the 2017 Act, but "insurer of a claim" (s 3), s 4(3) (s 3B cover), s 11 and
   s 54(6) and (9) still refer to the 1999 Act. Whether the 2017 Act fills the gap is outside this encoding. Asserted
   (`NOTHING` for another time limit).
3. **Eligibility is not in the Act.** s 7(1) leaves the criteria for lifetime and interim participation wholly to the
   LTCS Guidelines; the Act fixes only the bar for damages already awarded (s 7(3)). The criteria are an input.
4. **No time limits for eligibility disputes.** ss 14 and 15 set no time for referring an eligibility dispute or seeking
   review, unlike ss 24(2) and 25(2) (28 days each). s 8(6)(c) lets the Guidelines restrict the time for applications.
5. **s 27 has no consequence.** A participant "must comply" with reasonable requests, but the Act says nothing about
   what follows a refusal.
6. **Buying in.** ss 7A and 7B offer only lifetime participation, and neither says what happens to an accident that is
   both before the Scheme date and outside NSW (forks F2, F3). s 54(11) protects the owner or driver from recovery after
   a s 7A buy-in, but there is no matching provision for s 7B.
7. **s 54(3) sits uneasily in s 54.** Recovery from a person "other than the owner or driver of a motor vehicle" is
   placed among provisions about uninsured vehicles, and it is not clear whether s 54(1)'s conditions govern it, or
   whether s 54(2)'s reduction applies again (forks F9, F10).
8. **Vestiges.** s 59's heading still says "or Advisory Council", though no Advisory Council remains in the Act;
   Schedule 3 cl 4 speaks of approvals under s 10, which is repealed (the cl 4 transfer to s 11C explains it).
9. **The interim periods meet at the third birthday.** A child accepted the day before turning 3 stays interim until 5
   (to the second anniversary of acceptance), and one accepted on the third birthday stays for two years; the two rules give
   the same last day there (asserted: both 9 June 2027 for a child born 10 June 2022). A child accepted at 1 stays nearly
   four years.

## Questions (exported)

`ltcs-scheme.l4` (21), in the Act's order: `What is my relevant Scheme commencement date` (s 3(1)), `Does the Act apply
to my motor accident injury` (ss 3, 4, 7A, 7B), `Am I eligible to be a participant` (ss 4, 7, 7A, 7B), `Can this
person apply for me` (ss 7A(4), 7B(4), 8), `Must the Authority accept me as a participant` (ss 7A, 7B, 9), `What is the
last day of my interim participation` (s 9(5), (5A)), `Am I a participant on this day` (s 9(4)-(5B)), `Does section
11(2) stop time running on my damages claim` (s 11(2)), `How many days has my interim participation stopped time
running` (s 11(2)), `Will the Authority pay for this` (ss 5A, 11A, 11B, 11C), `What is the most the Authority will
contribute to alternative expenditure` (s 11AA(2)), `Where does my dispute go` (ss 14, 20, 24), `Can I have the
Assessment Panel's determination reviewed` (s 15), `What is the last day to ask for an assessor` (s 24(2)), `Must the
Authority refer my dispute to an assessor` (s 24, with the rule), `What is the last day to refer the assessor's
determination for review` (s 25(2)), `Can I refer the assessor's determination for review` (s 25, with the rule), `Must
I comply with this request` (s 27), `Will the Authority pay this cost of attending the panel` (s 17), `Will the
Authority pay my legal costs` (ss 18, 21, 29), `How much of my legal costs will the Authority pay` (s 21).

`ltcs-seat-owner-driver.l4` (2): `Can the Authority recover the participant's care costs from me` (s 54(1), (3),
(5)-(9), (11)), `How much can the Authority recover from me` (s 54(2)-(4)).

Situations for the website's form: the s 9 duration and s 11(2) questions arise only once accepted as a participant;
the Part 3 and Part 4 questions only in a dispute; the owner-driver module only after an accident with an uninsured
vehicle.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation,
  especially the references to the 1999 and 2017 Acts (finding 2).
- Deposit the LTCS Guidelines and the regulations, and bring their criteria and numbers in.
- Have a lawyer review the forks, especially F1-F4 (buying in), F6 and F8 (counting) and F9-F10 (s 54).
- Link the encoding to the motor accidents, limitation and civil liability encodings for damages and time limits.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
