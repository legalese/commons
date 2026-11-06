# Guardianship and Administration Act 2019 (Vic) -- baseline encoding, the adult for whom a guardian or administrator is sought or appointed

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`gaa-rules.l4`), the
dates in another (`gaa-dates.l4`, built-in date functions only, no daydate, no `YMD`), and the questions in one seat module
(`gaa-seat.l4`) that imports the rules and never restates one. The cases are in `gaa-cases.l4`.

The focus asked for: guardians and administrators for adults without decision-making capacity, including the management
of a compensation award. That is Part 3 of the Act (guardianship and administration orders), encoded with Part 1's
definitions and capacity test, Part 4 (supportive orders), the time limits of Part 7 (rehearings and reassessments), and
Part 9's claims machinery: money a court orders paid to a person with a disability (s 179), the administrator's fees
(s 175), compensation from a guardian or administrator and its time limit (ss 181-186), and the offences of dishonest use
of an order (ss 188-192).

## Edition

- **Act:** Guardianship and Administration Act 2019, Act No. 13/2019, Version No. 010, incorporating amendments as at
  15 April 2026 (the register's current version when read on 6 November 2026), deposited at
  `../../registers/source-bundle/guardianship-and-administration-act-2019.txt` (committed text sha256
  4d4935d0fd4810b46ec9f67a595008ccd43e2f816d101d903f4c57b264f049f3, per its `.meta.json`), a plain-text conversion of the
  Word file the owner saved by hand on 6 November 2026 (see that file's `.meta.json` and `subjects/au/vic/README.md`). Not
  checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:** the Act's own numbers are in the Act (the 30, 42, 28, 14 day periods, 21-day urgent orders,
  12 months and 3 years for reassessment, 6 months for compensation, 2 years for unclaimed effects, $100, $10 000, the
  penalty units). Not deposited, so asked as inputs or left out: the regulations (the s 61(4)(b) prescribed amount, an
  input with 0 for "none prescribed"; the s 194 annual fees), the VCAT rules' remuneration scale and the Corporations Act
  Chapter 5D fee limit (s 175, named in the answer, not computed), the value of a penalty unit (Monetary Units Act 2004;
  penalties answered in penalty units), and the Interpretation of Legislation Act 1984 (period counting; fork F2).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `gaa-dates.l4` | 0 | 0 | 0 | 0 |
| `gaa-rules.l4` | 0 | 0 | 0 | 0 |
| `gaa-seat.l4` | 0 | 0 | 0 | 0 |
| `gaa-cases.l4` | 0 | 0 | 217 | 217 |

Every exported question (38) has cases, with the edges: age 17 and 18; 21 and 22 days for an urgent order and its
renewal; day 42 and 43 (s 37), day 30 and 31 across 29 February 2028 (s 28), day 28 and 29 and from written reasons
(s 152), day 14 and 15 (s 164); 6 months from 31 August (the last day of February) and from the earlier of two deaths, and
an extension (s 184); the 12-month day, a reassessment on the third anniversary itself and the day after (s 159); the
anniversary itself and the day after, and a 29 February appointment (s 61(2)); $99.99 and $100, and a prescribed amount
(s 61(4)(b)); $10 000 and $10 000.01 (s 93(3)); the second anniversary and the day after (s 74); every constructor of
every choice.

## Seat

**The adult for whom a guardian or administrator is sought or appointed** (`gaa-seat.l4`): the person with a disability
who may lack decision-making capacity -- the proposed represented person, the represented person, the supported person --
including the person whose damages or compensation award is paid into court and managed by an administrator. "Do I have
decision-making capacity?", "Can VCAT appoint someone for me?", "May my administrator collect my compensation?", "Where does
the money the court awarded me go?", "What may my administrator charge?", "Can I be compensated for my administrator's
breach, and by when?", "Can I get a rehearing, and by when?". Where a relative, carer or personal representative asks for
the person (the s 183 applicants, the estate after death), the questions are still worded from the person's seat.

No seat for VCAT, the courts, the Public Advocate or State Trustees: their satisfaction, orders and determinations are
asked as facts. A seat for the guardian or administrator (the duties of ss 41, 55-63, 177) would be a further layer,
`gaa-seat-administrator.l4`, over the same rules.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; no regulations or rules are deposited (see Edition).
- **The actors the text names.** Followed: the person, the guardian, the administrator, the supportive guardian and
  administrator, the relatives and nearest relative, the primary carer, VCAT, the Supreme, County and Magistrates' Courts,
  State Trustees, the Public Advocate, the examiner or auditor of accounts.
- **Judgments answered conditionally.** Followed: VCAT's satisfaction (ss 30, 32, 87, 88), "in need" (s 31), "promote ...
  wellbeing", "reasonable" gifts (s 47), "reasonably believes ... deplete seriously" (s 177(5)), "acted honestly and
  reasonably and ought fairly to be excused" (s 182), good faith and reasonable care (s 61(6)), the court's "considers ...
  may be in need" (s 179(1)), and the limbs of capacity (s 5) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "disability", "decision-making capacity",
  "nearest relative", "Court" (s 179(9)), "significant financial transaction" (s 93) are worked out; "domestic partner",
  "close friend", "licensed trustee company", "ADI", "civil proceeding" are asked.
- **One case.** One order, one appointment, one transaction, one gift, one award, one claim for compensation.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (disability, nearest relative; relative), s 5 (capacity); Part 3: ss 22, 23, 28 (and s 85), 30, 31 (as one
input), 32, 36(3), 37, 38(1)(c), 39, 40, 46, 47, 51, 52(a), 53, 54, 57, 58, 61(2), (4)(b), (5)-(7), 69(2), 71, 72, 73,
74, 75; Part 4: ss 79, 80, 87(2), 88, 90(1)(d), 93, 95; Part 7: ss 150, 151, 152, 153, 159(2), 164(4)-(6); Part 9: ss 175,
177(4), (5), 179(1)-(3), (8), (9), 181, 182, 183, 184, 186 (in a description), 188-192.

**Regulative rules:** five, each a DEONTIC rule run by EVALTRACE inside an exported question that takes only dates and facts
(the helper shape of the Medical Treatment Planning and Decisions Act encoding): s 28 (VCAT MUST start hearing WITHIN 30
days of receipt, unless a compulsory conference or mediation), s 37 (VCAT MUST hold the hearing WITHIN 42 days of an urgent
order), s 152 (I DO apply for a rehearing WITHIN 28 days of the day of the order), s 164 (I DO request a hearing WITHIN 14
days of the notice; the breach is that VCAT need not hold one), s 184 (I DO apply for compensation WITHIN the days to 6
months after the first death, or the extended day). Day 0 is the day the period runs from; the last day is in time.

**Out, and why:**
- ss 1, 2, 7 (object), 194, 195 and Part 10 (repeal, savings and transitional, ss 196-206) and the endnotes: machinery.
- Part 2 (ss 10-21): the Public Advocate's office, functions and powers. An official; what it means for the person
  appears where the Act names it (s 183(e), s 167(2) noted, rehearing standing).
- Part 5 (ss 99-139): administration (missing person) orders. A different person (the missing person) and a different
  case; it largely mirrors Part 3 Divisions 6-8 and would be its own encoding.
- Part 6 (ss 140-149): special medical procedures. Medical consent, with the Medical Treatment Planning and Decisions Act
  2016 (encoded beside this one); outside the focus.
- Part 8 (ss 168-174): interstate orders. Registration machinery.
- ss 4, 6, 8, 9, 41, 55, 56, 59, 60, 94: principles and duties of the guardian, administrator and supporter. They bind the
  appointee; they matter to the person through s 181 (a loss "caused by ... contravening this Act"), which takes the
  contravention as an input. A seat for the appointee would encode them.
- ss 24-27, 29, 81-84, 86, 154-156, 160-163, 165: contents of applications and notices, parties and attendance. Procedure;
  s 25(b) (the person is always a party) is used in the rehearing question.
- ss 33, 34, 35, 43, 44, 45, 48-50, 52 (except (a)), 62-68, 70, 76-78, 89, 91, 92, 96-98, 157, 158, 166, 167, 176, 178,
  180, 185, 187, 193: VCAT's own powers and procedure, the remaining administrator powers, wills, the Fund, enforcement
  orders, criminal liability of officers. Noted where an answer depends on them (s 52(i) and s 51 in the proceedings
  question; s 158 -- a rehearing application does not stop the order operating -- is not asked).
- s 45(2) (reassessment within 42 days of a compliance order) and s 61(1), (3) (VCAT's other account times): not asked.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 5(2), (4)(c), (d) -- `s 5 -- my decision-making capacity` -- doubt resting only on appearance or an unwise
  decision is not "evidence to the contrary", so the presumption stands -- it is evidence, and the four limbs are then
  assessed.
- **F2** ss 159, 184, 74, 61(2) (periods of months and years) -- `the date n months after` -- the period ends on the
  corresponding day of the later month, or its last day if it has none (29 February + 12 months = 28 February) -- the
  Interpretation of Legislation Act 1984's counting (not deposited) might give 1 March.
- **F3** s 23(2), s 80(2) -- `ss 22, 23, 79, 80 -- whether an application can be made for me` -- a person who does not
  live in Victoria and has no property here is outside the grant for a money order (not covered) -- s 23(1) alone lets
  anyone apply for any adult with a disability.
- **F4** ss 32(1), (2), 88(1) -- `ss 32, 88 -- this person may be appointed for me` -- an individual under 18, or a body
  corporate as guardian or supporter, is outside the grant (NOTHING) -- a flat no.
- **F5** s 36(3) "remains in force for the period specified" -- `s 36(3) -- the last day my urgent order is in force` --
  the period excludes the day of making (21 days from 1 March ends 22 March) -- it includes it (ends 21 March).
- **F6** s 150(1) "(other than an urgent order appointing a guardian or an administrator)" -- `ss 150, 151, 153 -- whether
  I can apply for a rehearing` -- not covered (NOTHING-kind) -- a flat no.
- **F7** ss 150, 151, 159(3) -- the same function -- a reassessment someone applied for is "an application" within s 150,
  so a party may seek a rehearing without leave -- s 151 alone governs reassessments, and gives no rehearing of one made
  on application.
- **F8** s 159(2)(b) "at least once within each 3 year period after making the order" -- `s 159(2) -- the last day for
  VCAT's next reassessment of my order` -- fixed periods counted from the making (the third, sixth, ninth anniversary) --
  a rolling 3 years from the last reassessment (finding 3).
- **F9** ss 54, 69(2) -- `ss 46, 52, 54, 69 -- my administrator may collect my compensation or damages` -- the powers
  continue until the administrator knows of the death or the end of the order (JUST TRUE before, JUST FALSE after) --
  s 54 ends them at death whatever the administrator knows (finding 4).
- **F10** ss 46(1)(e), 51(1) -- `ss 38, 40, 51 -- my guardian or administrator may bring or defend a proceeding in my name`
  -- an administrator without the s 51 power specified: NOTHING (the financial matters specified may still include
  settling a claim, s 3 "legal matter") -- a flat no as for a guardian under s 38(1)(c).
- **F11** s 75(1), (2) -- `s 75 -- whether my own dealing is void` -- the "without an order of VCAT or the written consent
  of the administrator" of (1) is read into (2), so a consented dealing is not void -- (2) read alone voids it (finding 5).
- **F12** s 93(2)(b) "excluding entering into a residential tenancy" -- `s 93 -- my supportive guardian or administrator
  may give effect to my decision` -- renting the home is not a significant financial transaction (JUST TRUE) -- the list
  "includes", so it may still be one (NOTHING).
- **F13** s 179(3)(b) "paid out to the administrator (if any) for that person or State Trustees" -- `s 179(3) -- where the
  money a court awards me goes` -- to the administrator where there is one, otherwise State Trustees -- either, as the
  court chooses.

Sites decided without a fork line: s 30(2) and s 87(2) ("may only ... if") and s 47(1) ("if") answer JUST FALSE when a
limb fails; ss 39, 53 (flat "does not confer") JUST FALSE; s 74's 2 years (a period the text fixes) FALSE before it ends;
s 72 when a s 73 order withholds the document ("subject to") JUST FALSE; ss 179(1), 183, 72 outside their grants, s 61(2)
and s 47 where VCAT has ordered otherwise, and s 184 while neither person has died answer NOTHING or a "not covered" /
"no time limit" constructor.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definitions (disability, nearest relative, Court in s 179(9)), the "if" of ss 5(1), 47(1),
179(3), "may only ... if" (ss 30(2), 87(2)), "does not confer" (ss 39, 53), "is not entitled ... unless" (s 175(1), s 95),
"is void" (s 75(2)), "until" (s 69(2), rule (d)), and the periods of ss 28, 37, 74, 152, 164 and 184 give the text's own
no; the sites above give NOTHING or a "not covered" constructor.

## What the Act turns out to say

1. **s 152(1) counts from "the order on the rehearing or the reassessment".** For a first rehearing of an application,
   no order "on the rehearing" exists yet, and s 153(b) bars a rehearing of a rehearing. The section is read as counting
   from the order sought to be reheard (as s 88(3) of the Medical Treatment Planning and Decisions Act 2016 says plainly).
   Possible drafting slip. Asserted (28 days from the order).
2. **The gift threshold is stated two ways.** The note to s 47 says details are needed for gifts "of or over $100 or the
   prescribed amount (whichever is greater)"; s 61(4)(b) says "of or over the prescribed amount (or, if an amount is not
   prescribed, of or over $100)". If a regulation prescribed less than $100 the two differ. The section governs (notes are
   not operative). Asserted ($150 against a prescribed $200: not detailed; $50 against a prescribed $50: detailed).
3. **Reassessments can be nearly five years apart.** s 159(2)(b) requires one "within each 3 year period after making the
   order", fixed periods on the literal reading. An order made on 1 March 2026 and reassessed on 15 February 2027 (inside
   the first period) need not be reassessed again until 1 March 2032, the end of the second period (F8). Asserted.
4. **s 54 and s 69(2) disagree about death.** s 54: the order "lapses on the death of the represented person". s 69(2):
   the administrator "may exercise all or any of the powers ... until the administrator knows that the represented person
   ... has died". Read together (F9), an administrator who has not yet heard of the death may still collect a compensation
   payment. Asserted.
5. **s 75(2) has no consent carve-out.** (1) deems incapacity only "without an order of VCAT or the written consent of the
   administrator"; (2) voids "any dealing ... in relation to a financial matter that is subject to an administration
   order", with no such words. Read literally, a dealing the administrator consented to in writing is still void. The
   encoding reads the carve-out in (F11). Asserted.
6. **s 192 has no body corporate penalty.** ss 189 and 190 give "In the case of a body corporate, 2300 penalty units";
   s 192 gives only "In the case of a natural person" (and ends each penalty with a semicolon). A supportive administrator
   must be an individual (s 88(1)), so the gap may be deliberate; the encoding answers NOTHING for a body corporate.
   Asserted.
7. **The State is never liable.** s 186: "No compensation is payable by the State" for any act or omission of a guardian or
   administrator, including the Public Advocate as guardian and State Trustees as administrator. Stated in the compensation
   question's description, not computed.
8. **The court award machinery has no threshold of capacity.** s 179(3) applies to money ordered paid "to a person with a
   disability", the s 3 definition, which does not ask whether the person lacks capacity: on its words, an injured adult
   with a physical disability and full capacity has their damages paid into court and out to State Trustees, unless the
   court orders otherwise. Asserted (a physical disability, no administrator: State Trustees).

## Before relying on it

- Check the text against the authorised PDF (Version No. 010), not saved.
- A lawyer's review of the forks, especially F8 (reassessment periods), F9 (s 54 and s 69(2)), F11 (s 75(2)) and F13
  (s 179(3)(b)).
- Deposit the Guardianship and Administration Regulations (the s 61(4)(b) prescribed amount and the s 194 fees) and the
  Interpretation of Legislation Act 1984 (period counting), and the VCAT rules' remuneration scale.
- An independent test pass, and a seat for the guardian or administrator carrying the duties (ss 41, 55-63, 177).
- Part 5 (missing persons) and Part 6 (special medical procedures) as further encodings.
