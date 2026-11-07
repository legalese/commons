# Powers of Attorney Act 2014 (Vic) -- baseline encoding, the principal and the attorney

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The modules:

- `poa-dates.l4`: the date helpers (built-in date functions only, no daydate, no `YMD`), restated from the Guardianship
  and Administration Act 2019 encoding because a module cannot import across subjects.
- `poa-rules.l4`: the rules, seat-neutral where the text is, each with its section and the words it comes from; two
  regulative rules (ss 79, 133).
- `poa-seat.l4`: the principal's questions (29), importing the rules and restating none.
- `poa-seat-attorney.l4`: the attorney's questions (16), a second seat over the same rules.
- `poa-cases.l4` and `poa-cases-attorney.l4`: the cases; the second also holds the mirror cases.

The focus asked for: decision making capacity and its assessment (ss 4, 5), making an enduring power of attorney (form,
witnessing, acceptance), when it becomes exercisable (s 39), the attorney's duties and conflict transactions, VCAT's
powers, and compensation for an attorney's breach (s 77), for an injured person whose claim and damages an attorney may
run and manage. The focus named "Part 4" for making the power and "Part 5" for the duties; in the Act, making is Part 3
Division 4 (ss 32-38), commencement Part 4 (ss 39-42), ending Part 5 (ss 43-62) and the duties Part 6 (ss 63-83B). All
four are encoded, with Part 1's definitions and Part 8 (VCAT).

## Edition

- **Act:** Powers of Attorney Act 2014, Act No. 57/2014, Version No. 007, incorporating amendments as at 26 April 2021
  (the register's current version, "In force", when read on 7 November 2026), deposited at
  `../../registers/source-bundle/powers-of-attorney-act-2014.txt` (committed text sha256
  3d897075aa804a914658835edae0c1cd80428f9aae0b6680695b0f4510685c1d, per its `.meta.json`), a plain-text conversion of
  the Word file `14-57a007.docx` the owner saved by hand on 7 November 2026 (see that file's `.meta.json` and
  `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not saved. Version 007 includes the
  remote witnessing provisions (ss 5A-5D, inserted by Act No. 11/2021 from 26 April 2021).
- **Numbers set elsewhere:** the Act's own numbers are in the Act (age 18, 2 witnesses, $100, 6 months, 28 days, 600
  and 2400 penalty units, 5 years). Not deposited, so asked as inputs or left out: the Powers of Attorney Regulations
  (the prescribed forms, the s 67(3) prescribed amount -- an input, 0 for none -- and the prescribed class of special
  witness), the value of a penalty unit (Monetary Units Act 2004; penalties answered in penalty units), the
  Interpretation of Legislation Act 1984 (period counting, fork F2; s 53 on forms "to the like effect"), and the
  borrowed terms "insolvent under administration", "authorised to witness affidavits", "trustee company" (Trustee
  Companies Act 1984) and "administration order" and "guardianship order" (Guardianship and Administration Act 2019).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `poa-dates.l4` | 0 | 0 | 0 | 0 |
| `poa-rules.l4` | 0 | 0 | 0 | 0 |
| `poa-seat.l4` | 0 | 0 | 0 | 0 |
| `poa-seat-attorney.l4` | 0 | 0 | 0 | 0 |
| `poa-cases.l4` | 0 | 0 | 234 | 234 |
| `poa-cases-attorney.l4` | 0 | 0 | 79 | 79 |

Every exported question (45) has cases, with the edges: age 17 and 18 (making the power, the attorney, the signer and
a witness); each s 26 head tried; each s 28 bar, the carer-payment exception and the dishonesty disclosure for financial
and personal attorneys; each execution failure in order, and remote witnessing with and without its conditions; every
commencement choice with and without loss of capacity, s 41 after regaining it, and s 83 with and without VCAT's
authority, including an authorised attorney whose power is not yet exercisable; every Part 5 ground alone and death
together with another; every conflict exception, the joint purchase with and without the principal's capacity, prior
authority and validation of completed and uncompleted transactions; the gift record at $99.99 and $100 and against a
prescribed amount above and below $100; 6 months from 31 August (the last day of February, 2027 and leap 2028), from
the earlier of two deaths, and an extension, the last day and the day after; 28 days for a rehearing, the last day and
the day after, and from written reasons; every constructor of every choice. Mirror cases ask the same facts from both
seats (eligibility, acting now, conflict, gifts, payment, disagreement, compensation, penalty).

## Seats

**The principal** (`poa-seat.l4`): the person who makes, or has made, an enduring power of attorney -- here typically an
injured person whose injury may take away, or has taken away, their decision making capacity, and whose claim, damages
or compensation an attorney may bring, settle, receive and manage. "Can I make one?", "Who can be my attorney?", "Was it
signed and witnessed properly?", "May my attorney settle my claim now?", "Is it still in force?", "May my attorney buy a
house in both our names with my damages?", "Can I be compensated, and by when?", "Can I go to VCAT, and by when for a
rehearing?". Where a relative asks for the person (as nearest relative, or for the estate after death), the questions
are still worded from the principal's seat.

**The attorney** (`poa-seat-attorney.l4`): a second seat, for the party the Act puts duties and liabilities on (CLAUDE.md,
ruled 2026-10-21) -- here typically a family member acting under an injured person's power. "Am I eligible?", "May I act
now?", "Must I notify anyone first?", "May I buy property in both our names?", "May I make this gift, and must I record
it?", "Must I keep records, and my money separate?", "May I be paid?", "May I resign?", "Whom must I tell my appointment
ended?", "Could I be made to compensate, or be relieved?", "What is the penalty for dishonest use?". It calls the same
rules, so the two seats cannot disagree; the answers are the rules' own choices, worded from the principal's side ("my
attorney"), which the attorney reads as about themself. The two layers define no name in common.

No seat for VCAT, the Supreme Court or the Public Advocate: their satisfaction, orders and determinations are asked as
facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; the regulations are not deposited (see Edition).
- **The actors the text names.** Followed: the principal, the attorney and alternative attorney, the person signing at
  the principal's direction, the witnesses and special witness, relatives and the nearest relative, care workers, health
  and accommodation providers, trustee companies, the Public Advocate, VCAT, the Supreme Court, the executor or
  administrator of the estate.
- **Judgments answered conditionally.** Followed: the limbs of capacity (s 4), "reasonable" gifts and maintenance
  (ss 67, 68), "is or may be a conflict" (s 64), "serious depletion" (s 72(2)), the Court's or VCAT's view that the
  attorney "acted honestly and reasonably and ought fairly to be excused" (s 74), good faith and knowledge (ss 73, 75),
  VCAT's satisfaction (ss 117, 118, 120(2)), "special interest" (ss 78, 122, 130) and "material" (s 66) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "care worker", "nearest relative", "financial
  matter", "personal matter" (with its medical treatment exclusion), "decision making capacity", "eligible attorney"
  (s 22(4) with s 28). Asked: "relative" (as a yes/no with the list in the description), "domestic partner",
  "insolvent under administration", "offence involving dishonesty", "authorised to witness affidavits", "special
  witness", "trustee company", "administration order", "guardianship order", whether something is lawful by an attorney.
- **One case.** One power of attorney, one attorney, one transaction, one gift, one claim for compensation, one VCAT order.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 3 (care worker, financial and personal matter, legal matter, nearest relative, relative, special witness),
s 4, s 5 (in the capacity question's description), s 5A (remote witnessing, as conditions of execution); Part 3:
ss 22, 23, 26, 28, 30, 31(2), 32-38; Part 4: ss 39, 40, 41, 42 (described); Part 5: ss 43, 44, 45-49 (execution of a
revocation, with ss 32-36), 50 (described), 51-56, 59-61; Part 6: ss 63 (described), 64-72, 73-79, 80 (described),
83; Part 8: ss 116 (described), 117-120, 122, 124 (described), 126, 128 (described), 130, 133; Part 9: s 135.

**Regulative rules:** two, each a DEONTIC rule run by EVALTRACE inside an exported question that takes only dates and
facts (the helper shape of the Guardianship and Administration Act 2019 and Medical Treatment Planning and Decisions Act
encodings): s 133 (I DO apply for a rehearing WITHIN 28 days of the day of the order) and s 79 (I DO apply for
compensation WITHIN the days to 6 months after the first death, or the extended day). Day 0 is the day the period runs
from; the last day is in time. The Act's other duties (ss 5, 40, 50, 54(3), 58, 61, 63-69) carry no deadline and are
answered as yes/no duties.

**Out, and why:**
- ss 1, 2, 139 and Part 10 (ss 140-156) and the endnotes: machinery and transitional. (s 142 brings ss 4, 42, Part 6
  Divisions 2-4, ss 82, 83 and parts of Part 8 to old enduring powers made under the Instruments Act 1958: not asked.)
- Part 2 (ss 6-20): general non-enduring powers of attorney, which end when the principal loses capacity; not the focus.
- Part 7 (ss 84-114): supportive attorney appointments; a different instrument, and its own encoding (s 136 likewise).
- ss 5B-5D: which copy is the document, recording, and other duties of remote witnessing; procedure.
- ss 21, 63: the principles and general duties (honestly, diligently, in good faith, with reasonable skill and care; no
  profit; avoid conflicts; confidentiality). Judgments; they reach the principal through s 77 (a loss "caused by the
  attorney contravening"), which takes the contravention as an input; they are quoted in the attorney's descriptions.
- ss 24, 25, 27, 29, 34(2), 35(3): conditions and instructions, no delegation, executing instruments, positions, and the
  "employee of an attorney" clarifications (an employee is not excluded merely for being one; not asked).
- s 31(1), (1A), (3), (4) and s 62: appointing alternative attorneys and the effect of one attorney's power ending on the
  others; s 62(3A) (remaining majority attorneys act jointly) is not asked.
- ss 81, 82, 83A, 83B: deed, proof, and the exception to ademption (wills).
- ss 115, 121, 123, 125, 127, 129, 131, 132, 134, 134A-134C: VCAT procedure, notice, advisory opinions, and wills.
- s 137 (officers of bodies corporate) and s 138 (interstate powers): not asked.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 4(2), (4)(c), (d) -- `s 4 -- my decision making capacity` -- doubt resting only on appearance or an unwise
  decision is not "evidence to the contrary", so the presumption stands -- it is evidence, and the four limbs are then
  assessed (as in the Guardianship and Administration Act 2019 encoding).
- **F2** s 79 (6 months) -- `the date n months after` -- the period ends on the corresponding day of the later month, or
  its last day if it has none (31 August + 6 months = 28 February) -- the Interpretation of Legislation Act 1984's
  counting (not deposited) might give 1 March.
- **F3** s 77(3) "This section does not apply if Division 3 applies" -- `ss 73-77 -- whether I can be compensated` --
  Division 3 bars compensation to the extent it protects or relieves (s 76 compliance; s 75(1) good-faith reliance on an
  invalid or revoked power; s 74 relief of all; after relief of part, compensation for the rest) -- read literally, any
  s 74 order, even for part, takes away all of s 77 (finding 1).
- **F4** s 3 "financial matter", "legal matter" -- `Kind of matter`, `May my attorney run or settle my claim now` -- a
  claim for damages or compensation for an injury, its settlement and receiving the money are a financial matter (a
  legal matter relating to financial affairs; example (d), "receiving and recovering money payable") -- a claim about
  personal or lifestyle affairs could also be a personal matter.
- **F5** s 28(1)(c) "if the individual is to be an attorney for financial matters" -- `s 28 -- whether this person is
  eligible to be my attorney` -- an attorney for both personal and financial matters is one -- the paragraph reaches only
  an attorney for financial matters alone.
- **F6** s 31(2) -- `s 31(2) -- my alternative attorney may act` -- where the power specifies circumstances, only they
  authorise the alternative (the (b) list applies only "if no circumstances are specified") -- the (b) events also apply.
- **F7** s 40(1) -- `s 40 -- I must notify before acting` -- not the first time, or no one named: no s 40 duty (FALSE) --
  NOTHING (a duty whose condition is unmet).
- **F8** s 64(2)(c)(iii), (iv) "when the principal has decision making capacity for the matter" -- `ss 64, 65 -- whether
  my attorney may enter into the transaction` -- the principal's capacity at the time of the transaction -- capacity at
  any time, or at the making of the power.
- **F9** s 67(1) "Subject to any condition or restriction stated in an enduring power of attorney" -- `s 67(1) -- my
  attorney may make the gift` -- a condition or restriction that forbids the gift answers JUST FALSE -- NOTHING (the
  power's own terms, outside the Act).
- **F10** s 78 "A person may apply ... if the person is" -- `s 78 -- this person may apply for compensation` -- anyone
  else answers FALSE -- NOTHING, as the Guardianship and Administration Act 2019 encoding answers for its s 183 (which
  lists "The following persons may apply" without "if").
- **F11** s 117 "must not decide ... valid ... unless VCAT is satisfied" -- `s 117 -- VCAT may treat my defectively
  executed instrument as valid` -- when all three are satisfied, TRUE ("VCAT may") -- satisfaction is necessary only, so
  NOTHING.
- **F12** s 120(1)(d) -- `Part 5 -- whether my power is in force as to this attorney` -- a suspended power is answered
  "suspended", neither in force nor ended -- "not in force" for the period.
- **F13** s 22(1) "anything ... that a person can lawfully do by an attorney" -- `ss 22, 26 -- whether I can give this
  power` -- whether a power outside s 26 is lawful by an attorney is borrowed law, asked -- the encoding could list the
  general law's exceptions (it does not).
- **F14** s 83 "unless the attorney is authorised by VCAT to do so and then only so far as is authorised" -- `ss 22, 39,
  41, 83 -- whether my attorney may act now` -- VCAT's authority lifts the s 83 bar but does not make the power
  exercisable before s 39 does (an authorised attorney whose time has not come is "not yet") -- the authority itself
  lets the attorney act.

Sites decided without a fork line: the "means" definitions (care worker, nearest relative, personal matter) and the
"if", "only if", "unless", "may not ... unless", "must not ... unless" of ss 4(1), 23(1), 28, 35(2), 37, 44, 67(1),
68(1), 70, 74, 117, 118, 120(2), 122, 126, 130 give the text's own no; s 26 ("is not able") and s 69(2) ("does not
apply") are flat negatives; ss 22(4) and 28 are a delegated definition (no head: FALSE); the period of s 133 and of
s 79 once a death has happened are periods the text fixes. NOTHING or a "not covered" constructor: medical treatment
(outside "personal matter", s 3), s 64 and ss 67-69 for an attorney not for financial matters, s 66 for a personal
dealing that is not material, s 74 with nothing to relieve, s 77 without a loss caused by a contravention, and s 79
while both are alive.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## What the Act turns out to say

1. **s 77(3) is wider than s 74.** s 74 lets the Supreme Court or VCAT relieve an attorney "from all or part" of their
   personal liability; s 77(3) says "This section does not apply if Division 3 applies", with no "to the extent". Read
   literally, an order relieving an attorney of part of the liability takes away the whole of the compensation power,
   and since ss 73-76 are always part of the Act the words need reading as "applies in the case". The encoding reads
   them as barring compensation to the extent Division 3 protects or relieves (F3). Possible drafting slip. Asserted
   (relief of part: compensation for the rest).
2. **s 77(2)(c) and s 75(1) pull against each other.** s 77(2)(c): compensation may be ordered "even if the enduring power
   of attorney is invalid or has been revoked". s 75(1): an attorney who acts "in good faith and without knowing" of the
   invalidity or revocation "is entitled to rely on the power of attorney as against the principal". With s 77(3), the
   compensation of s 77(2)(c) reaches only an attorney who knew, or had reason to believe (s 73), that the power was
   invalid or revoked. Asserted (good faith: no; not in good faith: yes).
3. **No time limit while both are alive.** s 79 sets 6 months only from a death (of the principal, the attorney, or the
   first of them). While both live, the Act sets no time for a compensation application; the general law of limitation
   is not in the Act. As the Guardianship and Administration Act 2019 s 184. Asserted (NOTHING; "no time limit").
4. **The estate cannot go to VCAT under s 122 as of right.** s 78(c) lets "an executor or administrator of the
   principal's estate" apply for compensation, and s 77(2)(b) pays compensation to the estate; but s 122(1), who may
   apply to VCAT for orders about the power (its validity, a transaction's validity, accounts and audit), does not name
   the executor or administrator, who must show a "special interest" (s 122(1)(e)). Asserted (FALSE).
5. **s 120(2) guards only one of VCAT's powers.** Revoking an attorney's appointment (s 120(1)(b)) needs VCAT to be
   satisfied that the attorney is not complying and that the principal lacks capacity to make the same power; revoking
   "all or part of the enduring power" (s 120(1)(a)), varying it or suspending it carries no such condition. Stated;
   s 120(2) asserted.
6. **A joint purchase with an incapable principal's money is a conflict transaction.** s 64(2)(c)(iii), (iv) take an
   acquisition of property to be held jointly by the attorney and the principal out of the conflict duty only "when the
   principal has decision making capacity for the matter". An attorney who buys a home in both names with the damages of
   a principal who has lost capacity needs VCAT's prior authority (s 65(4)) or VCAT's validation once completed
   (s 65(5)); the principal cannot validate it without capacity. Dealing with property already held jointly needs no
   capacity ((i), (ii)). Asserted (F8).
7. **A family carer on a government carer payment is not a "care worker".** The s 3 definition excludes "a person who
   receives a carer payment or other benefit from the Commonwealth or a State ... for providing home care", even one also
   paid from the principal's own funds or compensation. Such a carer may be appointed attorney (s 28(1)(d)) and is not
   excluded as a witness as a care worker (s 35(2)(d)(iii)); a relative is excluded as a witness anyway. Asserted.
8. **The gift record threshold can fall below $100.** s 67(3)(b): a record is needed for a gift "of or over (i) the
   prescribed amount; or (ii) if an amount has not been prescribed, $100". A prescribed amount below $100 lowers the
   threshold. The regulations are not deposited; the amount is an input. Asserted ($50 prescribed, $50 gift: record).
9. **Two Acts, two nearest relatives.** This Act's "relative" has eight paragraphs, with "(c) parent or step-parent" and
   "(d) sibling or step-sibling" each one paragraph, so the elder of a parent and a step-parent is preferred. The
   Guardianship and Administration Act 2019 s 3 lists parents, step-parents, siblings and step-siblings in separate
   paragraphs (ten in all), so for the same person a parent outranks an older step-parent there but not here. The same
   family can have different nearest relatives under the two Acts. Asserted (the paragraph named).
10. **Penalties for the same wrong differ between the two Acts.** s 135: a body corporate that dishonestly uses an
    enduring power faces 2400 penalty units; the Guardianship and Administration Act 2019 ss 189, 190 give 2300 for an
    administrator doing the same with an order. The natural-person penalty (5 years or 600 penalty units) is the same.
    Asserted (2400).
11. **A court's damages order can stop an attorney.** Where a court orders damages for a person with a disability paid
    into court and out to an administrator or State Trustees, the Guardianship and Administration Act 2019 s 179(8)
    makes that work as an administration order; then s 83(1) of this Act stops the principal's attorney exercising any
    power for financial matters "unless ... authorised by VCAT ... and then only so far as is authorised". Asserted (an
    administration order, with and without VCAT's authority).

## Before relying on it

- Check the text against the authorised PDF (Version No. 007), not saved.
- A lawyer's review of the forks, especially F3 (s 77(3)), F8 (joint purchases), F12 (suspension) and F14 (s 83).
- Deposit the Powers of Attorney Regulations (the prescribed forms, the s 67(3) amount, special witnesses) and the
  Interpretation of Legislation Act 1984 (period counting, forms to the like effect).
- An independent test pass.
- Part 2 (non-enduring powers) and Part 7 (supportive attorney appointments) as further encodings.

Victoria has no requirement ledger, so no ledger line is closed or raised.
