# Victorian Civil and Administrative Tribunal Act 1998 (Vic) -- baseline encoding, the party to a VCAT proceeding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this Victorian subject; nothing existing was touched. The dates are in `vcat-dates.l4`
(built-in date functions only, no daydate), the rules and the party's questions in `vcat-party.l4` (each exported question
calls a rule defined beside it, or is itself a one-line reading of a single subsection), and the worked cases in
`vcat-cases-party.l4`.

The focus asked for: VCAT jurisdiction, procedure, costs and appeals, as a person bringing or answering a claim meets
them. The Act is large (Part 4 alone has 13 Divisions, and Schedule 1 varies the procedure for some 60 enabling Acts), so
this baseline takes the provisions a party meets from the decision to the appeal: the two jurisdictions; getting reasons
for a decision to be reviewed; the decision during review; missing the hearing; representation, interpreters and
support persons; the application fee; extension of time; withdrawal; the 12-month dismissal of discrimination
applications; conduct that disadvantages another party; settlement offers; costs; reimbursement of fees; VCAT's
reasons; re-opening an order made in one's absence; enforcement; and appeals. With them go the Schedule 1 variations for
the claims proceedings in this run: Transport Accident Act 1986 (Pt 20), consumer small claims (Pt 2AB), the Equal
Opportunity Act 2010 (Pt 7) and domestic building work disputes (Pt 6 cl 12B).

## Edition

- **Act:** Victorian Civil and Administrative Tribunal Act 1998, Act No. 53/1998, Version No. 145, as at 28 July 2026,
  deposited at `../../registers/source-bundle/victorian-civil-and-administrative-tribunal-act-1998.txt` (sha256
  502aa68b...ef94ba as committed, per its `.meta.json`), a plain-text conversion of the Word file the owner saved by hand
  on 6 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Version 145 was the current version
  on 2026-11-06. Not checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the Act sets its own periods and the s 148(9) $3000. The application, referral and
  mediation fees are "the prescribed fee" (ss 68, 70, 88): the Victorian Civil and Administrative Tribunal Regulations
  are not deposited, so no fee amount is encoded and the s 132 "other prescribed ground" is asked as one fact. The
  Magistrates' Court's jurisdictional limit (s 121) belongs to the Magistrates' Court Act 1989 and is asked. The time
  limits VCAT's rules set (s 120(2)) and the Supreme Court's rules that may displace s 148(2)(a) are not deposited.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read
(two deliberately wrong assertions were run once in a scratch file in this folder, since deleted, and showed as errors).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `vcat-dates.l4` | 0 | 0 | 0 | 0 |
| `vcat-party.l4` | 0 | 0 | 0 | 0 |
| `vcat-cases-party.l4` | 0 | 0 | 192 | 192 |

Every exported question has cases, with the edges: the 28th and 29th day for a request for reasons and the decision
day itself; the decision-maker's 28th and 29th day and an enabling Act's 14 and 60 days; the 30th and 31st day for the
fee (in a 28-day February), a fee paid a day late, and a postponed fee paid on and after its date; exactly 12 months and
a day more for a discrimination application, and 29 February; a settlement offer of 13 and 14 days, accepted on its last
day and the day after, cut short by orders before, on and after its last day; the 60-day and 45-day reasons periods and
an extension; the 14th and 15th day for written reasons; the 28th and 29th day for leave to appeal, with and without
written reasons moving the start; the 14th and 15th day to institute an appeal; $3000 and $3001 in a credit claim; an
amount owing at the Magistrates' Court limit and a dollar over. The settlement offer costs rule is asked from both seats
(the offeror and the party who did not accept) on the same facts, with answers that agree.

## Seat

**The party** (`vcat-party.l4`): the individual who brings a claim or an application for review to VCAT -- a person
seeking review of a decision about their transport accident compensation, a consumer with a small claim, a person who
complains of discrimination, a building owner -- or who answers one as an individual respondent. "Is my case original
or review?", "By when must I ask for reasons?", "Can I have a lawyer?", "Will VCAT strike my claim out for the fee?",
"Do I need leave to withdraw?", "Will I have to pay the other side's costs?", "Did my settlement offer work?", "Do I get
my fees back?", "Can I have an order made in my absence re-opened?", "By when must I seek leave to appeal?".

No seat for VCAT, its President, the principal registrar, the decision-maker as an official, or the Supreme Court:
their satisfactions, opinions, beliefs, orders and directions are asked as facts. A business respondent could have its
own seat layer later (`vcat-seat-respondent.l4`); the questions here are mostly symmetrical, and the s 112 costs rule is
already asked from both sides.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own periods and amounts; the
  fee regulations are not deposited (above).
- **The actors the text names.** Followed: the applicant, the other party, the decision-maker, the Tribunal, the
  principal registrar, the President, the Trial Division and Court of Appeal.
- **Judgments answered conditionally.** Followed: "satisfied that it is fair" (s 109(3)), "the Tribunal believes"
  (s 78(1)), "in the opinion of the Tribunal ... not more favourable" (s 112(1)(d)), "orders otherwise" (ss 112(2),
  115C(3)), "satisfied that it would be unfair" (Sch 1 cl 12B(3)), "considers that ... financial hardship" (s 132(1)),
  "reasonable excuse" and "appropriate" (s 120(4)), "prejudice ... that cannot be remedied" (s 126(4)), "satisfied that
  no other party ... will be unfairly disadvantaged" (Sch 1 cl 4D(1)(a)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: original and review jurisdiction (ss 41, 42),
  compliance of a settlement offer (ss 112(1)(a), 113(4), 114(2)), the periods. Asked: "small claim" (ACL and FT Act
  Chapter 7), "question of law", "professional advocate" (s 62(8), as facts about the other party), the Magistrates'
  Court's limit, "credit enactment" (s 148(10), as one fact).
- **One case.** One proceeding, one party in the seat, one order or offer at a time.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 40-43, 48 (jurisdiction); s 45 (request for reasons); s 46(1)-(3) (reasons by the decision-maker); s 47(1),
(2) (order for reasons, named); s 49(1), (2) (lodging material); s 50(1)-(3) (decision pending review); s 51(5) (applicant
absent at a review hearing); s 51A(5) (no withdrawal costs only because of reconsideration); s 62(1), (2)(a) (as for an
individual), s 62(8) (named); ss 63, 63A; s 68(3)-(5); s 74(1), (2)(a)-(b), (d); s 78; s 99(2); ss 109(1)-(3); ss 112-115;
s 115C (named s 115B); s 117(1)-(4); s 120(1)-(4C); ss 121, 122; s 126(1), (3), (4); s 132(1)-(3); s 148(1)-(6), (9),
(10). **Schedule 1:** Pt 2AB cls 4C-4F, 4I; Pt 6 cl 12B; Pt 7 cls 17, 18, 22; Pt 20 cls 92-94.

**Regulative rules:** six, each run by EVALTRACE inside an exported question that takes only dates and facts, through the
helper the other Victorian baselines use (a CONSIDER on an EVALTRACE matches FULFILLED only): s 45(2) (I DO request
reasons WITHIN 28 days), s 46(1) (the decision-maker MUST give reasons WITHIN 28 days or the enabling Act's period, LEST
BREACH), s 114(1), (6) (I DO accept by signed notice WITHIN the offer's period), s 117(2) (I DO request written reasons
WITHIN 14 days), s 148(2) (I DO apply for leave WITHIN 28 days), s 148(3) (I DO institute the appeal WITHIN 14 days).

**Out, and why:**
- Part 1 (preliminary, definitions), Part 2 (establishment, members, administration), Part 6 (Rules Committee), Part 7
  (miscellaneous): machinery.
- Part 3A (federal subject matter) and s 77 (more appropriate forum, with the s 77(4) limitation extension): a
  constitutional sorting of cases with no fact test a party can state beyond "federal subject matter"; worth a layer of
  its own.
- ss 52-57 (planning-court limitation, Cabinet and Crown privilege certificates, policy statements), s 46(4)-(7),
  s 47(3)-(7), s 49(3)-(5), s 50(4)-(7), s 51(1)-(4), s 51A(1)-(4): powers and procedure of officials, with nothing the
  party can compute; their effect for the party is in the questions above.
- ss 59-61, 60A (parties, joinder, unincorporated associations), s 62(2)(b)-(g), (3)-(7), (9) (representation of bodies;
  the seat is an individual), ss 64-66 (constitution), ss 67, 69-73 (form of applications, referral fee, rejection,
  service, intervention): procedure.
- ss 75, 76 (summary dismissal): wholly in VCAT's opinion; s 75(2) compensation follows it. Named in NOTES only.
- s 79 (security for costs), ss 80-82 (directions, third-party documents, consolidation), Division 5 (compulsory
  conferences, mediation: ss 83-93A), Division 5A (RDRV, residential tenancies), Division 6 (experts, referees, referral
  of questions of law), Division 7 except s 99(2) (hearings, evidence, privilege): procedure whose outcomes are VCAT's
  choices. The mediation fee (s 88(4)) is prescribed and not deposited.
- ss 110, 111, 115A, 115B (as a rule), 115CA (planning permits under s 79 of the Planning and Environment Act 1987),
  115D: s 115B is a bare discretion and is named in the s 115C answer; s 115CA is a planning layer.
- ss 116, 118, 119, 120A: form and effect of orders, corrections, enforcement re-openings, with no fact test the party
  meets beyond those encoded.
- Division 10 except ss 126, 132; Division 11 (offences, contempt: ss 133-139); Divisions 12, 13 (service, register,
  publication); s 149 (stay pending appeal: discretion); s 148(7), (8) (the court's orders).
- Schedule 1 outside the parts named above (some 60 enabling Acts; the residential tenancies, guardianship, planning and
  freedom of information variations among them); Schedules 2 and 3.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 45(2), 46(1), 49(2), 68(4), 114(1), 117(1)-(3), 148(2), (3) "within n days after" a day -- `the date` n
  `days after` and the six rules -- the last day is the day plus n, and an act on that day is in time -- the last day is
  the day plus n minus 1.
- **F2** Sch 1 cl 18 "more than 12 months before" -- `Sch 1 cl 18 -- may be dismissed as more than 12 months old` -- more
  than 12 months when the application day is after the same day 12 months after the contravention (the last day of the
  month where it has no such day: 29 February 2024 gives 28 February 2025) -- 1 March 2025 for a 29 February start.
- **F3** s 45(2) "must be made in writing" -- `s 45 -- my request for reasons is valid` -- an oral request is not a
  request under s 45 (JUST FALSE) -- an oral request is a request that breaches a "must" (NOTHING; the "bare must not
  done" case left to the encoder on 2026-11-05).
- **F4** Sch 1 cl 92 "Nothing in section 109 applies to a proceeding under the Transport Accident Act 1986" --
  `s 74(2)(b) -- costs on withdrawal` -- the withdrawal costs power of s 74(2)(b) survives (JUST TRUE) -- cl 92 was meant
  to take all costs orders out of Transport Accident Act proceedings (finding 3).
- **F5** s 112(2) against Sch 1 cl 4I(1) -- `s 112 -- costs after a rejected offer` -- in a small claim "cannot order
  costs" prevails over the s 112(2) entitlement (no) -- s 112(2), the later and more specific entitlement, prevails.
- **F6** Sch 1 cl 12B(3) "is not required to make an award of costs" -- `ss 109, Sch 1 cls 4I, 12B, 92 -- my costs
  exposure` -- where VCAT is satisfied a cl 12B award would be unfair, s 109 decides -- cl 12B displaces s 109 entirely
  for a domestic building work dispute ("applies despite section 109"), leaving no costs power.
- **F7** s 115C(1)(b) "a proceeding under the Domestic Building Contracts Act 1995" -- `Kind of proceeding` -- one kind,
  the domestic building work dispute, stands for all Domestic Building Contracts Act proceedings in the s 115C question
  -- separate kinds for the other proceedings under that Act (same s 115C answer, different costs answer).
- **F8** s 117(2) "within 14 days" -- `What is the last day to ask for written reasons` -- counted from the day the oral
  reasons were given -- counted from the day the order was made, if different (finding 4).
- **F9** s 121(1)(a) "within the jurisdictional limit" -- `ss 121, 122 -- where I enforce the order` -- an amount equal
  to the limit is within it -- "within" means below.
- **F10** s 68(4) "If the fee is not paid within 30 days" -- `s 68(4), (5) -- strike-out for the fee` -- a fee paid after
  the 30 days still leaves VCAT able to strike out (the words) -- a fee paid before VCAT acts removes the power (finding
  5).
- **F11** s 74(1) "before it is determined" -- `s 74(1), Sch 1 cls 4E, 17 -- withdrawing my application` -- after
  determination the answer is "not covered" (a scope limit without "only", ruling (c) of 2026-11-05) -- "no".
- **F12** s 115 -- `s 115 -- an accepted offer not kept` -- s 115 applies in a review proceeding (s 112(1)(a)'s exclusion
  of review proceedings is not repeated in ss 113-115) -- ss 113-115 share s 112's scope.
- **F13** s 62(1)(b)(i), (2) -- `s 62, Sch 1 cl 4D -- I may be represented by a lawyer` -- for an individual the only
  s 62(2) head is (a) a child; the holder of a statutory office is not offered, as it is not the individual's own claim
  -- offer every s 62(2) head.
- **F14** s 51(5) -- `ss 51(5), 99(2) -- if I miss the hearing` -- applies to the applicant whether or not notice was
  given (the words) -- read with s 99(2), confirmation follows only an absence after notice (finding 2).

## Rulings on negatives followed

Recorded here as the guide asks, word for word from `docs/ENCODING-GUIDE.md` section 5:

- **Periods, "where" and scope limits** (ruled 2026-11-05): "(a) a period the text fixes in its own words ...: outside the
  period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope
  limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`."
- **Questions with no convention** (Meng, 2026-11-05): "decided site by site, at encoding time, on the text's own words
  and the encoder's best judgment ... Each such site gets one fork line" -- F3, F10, F11 above.

Applied: the s 45, s 117(2), s 148(2), (3) and s 114 periods answer JUST FALSE outside them; Sch 1 cl 18 answers NOTHING
outside Parts 4, 6, 6A and 7 (scope) and JUST FALSE within 12 months ("if"); s 45(1) answers NOTHING for a person not
entitled to review (scope); s 74(2)(d) answers NOTHING for different facts (silence); s 132(2) answers NOTHING where no
fee was relieved and JUST FALSE where no costs were awarded ("if"); s 148(9) answers NOTHING outside a credit enactment;
the flat negatives of Sch 1 cls 4F, 4I(1), 22, 94 and s 51A(5) answer JUST FALSE or "no".

## What the Act turns out to say

1. **Two separate costs regimes survive in Transport Accident Act proceedings.** Sch 1 cl 92 says nothing in s 109
   applies, but cl 93 expressly applies ss 112-115 (the settlement-offer costs presumption) to s 77 reviews. So a
   transport accident claimant at VCAT cannot be ordered to pay costs under s 109, yet can be, under s 112(2), for not
   accepting a complying offer that beats VCAT's orders. Asserted (the `TAC review` cases for s 109 and s 112).
2. **s 51(5) has no notice condition.** "If an applicant does not appear ... at the hearing of a proceeding for review of
   a decision, the Tribunal must confirm the decision" -- unlike s 99(2), which lets a hearing proceed only against a
   person given notice in accordance with the rules. Read literally, an applicant who was never told of the hearing still
   has the decision confirmed; the remedy is s 120 (re-opening an order made in one's absence). Asserted (F14).
3. **Sch 1 cl 92 reaches s 109 only.** Withdrawal costs (s 74(2)(b)) and s 75(2) compensation are separate powers and
   survive in Transport Accident Act proceedings; but s 78(2)(c) is an "order for costs under section 109", so in those
   proceedings s 78 loses its costs limb. Asserted for s 74(2)(b) (F4).
4. **s 117(2) names no starting point** for "within 14 days"; the day the oral reasons were given is taken. The choice
   matters because s 148(4) moves the start of the 28 days for leave to appeal to the day written reasons are given.
5. **s 68(4) speaks of a fee "not paid within 30 days"**, so a fee paid on day 31 does not, on the words, remove the
   power to strike out, though s 68(3) then lets the application proceed. Asserted (F10).
6. **In small claims, s 112(2) and Sch 1 cl 4I(1) collide.** s 112(2) gives an entitlement to a costs order; cl 4I(1)
   says VCAT "cannot order costs". The encoding takes cl 4I(1) (F5). Fee reimbursement is not costs (s 115D) and the
   s 115C presumption still applies to small claims. Asserted.
7. **Sch 1 cl 18 hangs a lateness ground on s 76**, the power to dismiss "for want of prosecution", so the 12-month
   dismissal of an Equal Opportunity Act application is exercisable only by the Tribunal as constituted or a presidential
   member (s 76(2)), not by any member who could dismiss under s 75.
8. **s 148(9), (10) has lost most of its list.** Only the Credit Act 1984 and s 45 of the Motor Car Traders Act 1986
   remain as "credit enactments" (paragraphs (a) and (c) are shown as repealed), so the $3000 indemnity condition now
   reaches very few proceedings.
9. **s 148(2)(a)'s 28 days yield to the Supreme Court's rules** ("unless the rules of the Supreme Court otherwise
   provide"), which are not deposited; the encoding uses 28 days and says so in the question.

## Before relying on it

- Check the edition against the authorised PDF of version 145, and against any later version.
- Deposit the Victorian Civil and Administrative Tribunal Regulations (fees, prescribed grounds for relief, the s 115C(1)(e)
  proceedings) and the VCAT Rules (the s 120(2) time limits, the s 126(2) relevant enactments), and the Supreme Court
  rules on leave to appeal from VCAT.
- An independent test pass, and a lawyer's view of forks F4, F5, F6 and F14 and findings 1-3.
- Layers for Part 3A (federal subject matter), the residential tenancies variations (Sch 1 Pt 17, Division 5A) and
  guardianship (Sch 1 Pt 9), which are frequent VCAT claims outside this focus.
