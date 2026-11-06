# Trustee Act 1958 (Vic) -- baseline encoding, the beneficiary

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in one module (`ta-rules.l4`), the
dates in a small one (`ta-dates.l4`, built-in date functions only, no daydate and no `YMD`), and the beneficiary's
questions in `ta-seat.l4`, which imports the rules and restates none. The cases are in `ta-cases.l4`.

## Edition

- **Act:** Trustee Act 1958, Act No. 6401/1958, Version No. 127, incorporating amendments as at 1 September 2023 (the
  current version on 6 November 2026), deposited at `../../registers/source-bundle/trustee-act-1958.txt` (sha256
  11aaa28a...ae22c1b as committed), a plain-text conversion of the Word file the owner saved by hand on 6 November 2026
  (see that file's `.meta.json` and `subjects/au/vic/README.md`). Not checked against the authorised PDF, which was not
  saved.
- **Numbers set elsewhere:** none. Every figure the encoding uses is in the Act itself: two-thirds (s 12A), three-fifths
  (s 16), one-tenth, ten years, six months, two-fifths (s 17), twenty per cent (s 31(9)), two months (s 33), eighteen
  years and five per cent (s 37), $2000 and one-half (s 38), one year and four trustees (ss 40, 41), twenty-eight days
  (s 51(2)(i)), five per cent (s 77). The Act has no regulation-making section; the Metric Conversion (Trustee Act)
  Regulations 1973 (endnotes) only converted s 33's distances. The commencement date used by s 37(5) (1 April 1959) is
  from endnote 1, not the operative text. The County Court's jurisdictional limit (s 3) is in the County Court Act 1958:
  asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a
deliberately wrong assertion was run once in a scratch file, since deleted, and showed as `DiagnosticSeverity_Error`,
"assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ta-dates.l4` | 0 | 0 | 0 | 0 |
| `ta-rules.l4` | 0 | 0 | 0 | 0 |
| `ta-seat.l4` | 0 | 0 | 0 | 0 |
| `ta-cases.l4` | 0 | 0 | 213 | 213 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the
eighteenth birthday and the day before (and a 29 February birth); the s 6(3) review on the anniversary, the day after, and
across 29 February 2028; the s 51(2)(i) request on day 28 and day 29; the s 33 claims day exactly two months after the
last notice and a day short (and from 31 December); s 12A at exactly two-thirds and a dollar over; s 16 at three-fifths
and a dollar over; s 17 at one-tenth and a dollar under, at ten years, six months and two-fifths and either side; s 23 at
the insurable value and a dollar over; s 31(9) at exactly 120% and a dollar under; s 38 where $2000 and half the capital
cross ($4000, $4002), below $2000 of capital, and after earlier advances; s 37(5) on 31 March and 1 April 1959; s 41 one
year out of Victoria to the day and a day more; s 41(6) at four trustees and five; s 44 with one and two individuals left;
s 69 with a bare majority and with half.

## Seat

**The beneficiary** (`ta-seat.l4`): the individual for whom property is held on trust, under a will, a deed or a court
order -- in this claims work above all a child (or an adult under a disability) whose compensation or damages are held
on trust until they turn 18, asking through a parent, guardian or administrator where they cannot ask themselves. "Can
my trustee invest in this, and to what standard?", "Has my trustee reviewed the investments in time?", "Can my money be
used for my maintenance while I am under 18?", "Must the income be paid to me now I am 18, and what happens to what was
saved?", "How much of my capital can be advanced to me?", "Whose consent is needed before property is appropriated to my
share?", "Who can replace my trustee, and can my trustee retire?", "Can the Court appoint a trustee, make orders for my
property, vary my trust, excuse my trustee or impound my interest?", "What happens if my trustee ignores my written
direction?", "Is my trustee shielded from this loss?".

No seat for the trustee (a further seat for an individual trustee, a parent holding a child's damages for example, is
welcome later and could draw on the same rules), the Court, State Trustees or a trustee company: the Court's and the
trustee's judgments are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets all its own numbers (see Edition).
- **The actors the text names.** Followed: trustee, personal representative, beneficiary, principal beneficiary, minor,
  parent, guardian, person with power by law to consent, separate trustee of a settled share, trustee company, the
  Court, purchaser.
- **Judgments answered conditionally.** Followed: "expedient", "prudent", "reasonably believed", "reasonable", "unfairly
  prejudice", "honestly and reasonably", "ought fairly to be excused", "for the benefit of", "wilful default", "good
  faith", "appropriate to the circumstances of the trust" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "Court" (s 3), "housing loan" (s 12E(6)), the
  s 31(13) "settled legacy share or interest" (as the choice of interest), the s 39 protective trusts and the s 37 ages are
  worked out; "vested", "contingent", "intermediate income", "patient" (Mental Health and Wellbeing Act 2022),
  "represented person" (Guardianship and Administration Act 2019), "prescribed interest in land" are asked.
- **One case.** One beneficiary's interest under one trust.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**Focus:** trustees' powers and duties, investment, and the Court's supervision (for example of damages held for a
minor). The whole of Part I is encoded where it gives a fact test; Parts II to IV and s 77 so far as a beneficiary meets
them.

**In:** ss 3 ("Court"), 5, 6, 7(4), 8, 11, 12, 12A, 12B, 12D, 12E (with (6)), 14, 15, 16, 17(3), (4), 23, 28(1), 31(1),
(5)-(9), (13), 33(1), (3), 36(1), 37(1)-(3), (5), 38, 39, 41(1)-(3), (6), (9), 44, 48, 51(2)(i), 55, 63, 63A, 64, 67, 68,
69, 77; s 2(3) (contrary intention) where a question turns on it; s 69(7) and s 24 in descriptions.

**Regulative rules:** two. s 6(3): the trustee MUST review the performance of the trust investments WITHIN the year from
the last review, LEST breach. s 51(2)(i): the trustee MUST convey, receive or sue as the person absolutely entitled
directed WITHIN 28 days of the written request, LEST the case for a vesting order arises. Each is run by EVALTRACE inside
an exported question that takes only dates and yes/no facts, through a helper in the shape of the Civil Procedure Act 2010
encoding's.

**Out, and why:**
- ss 1, 2(1), (2), 4, 12F, 70 (title, repeals and savings, application, transitional, Settled Land Act trustees):
  machinery.
- s 7(1)-(3) (the general law's duties preserved): they point to the general law with no fact test; s 7(4) is in.
- s 9, 9A, 10 (schemes of arrangement, rights issues, RITS, calls on shares): powers with no condition a beneficiary could
  test; s 9(6) (consideration held as capital) could be added.
- s 12C (factors the Court may consider in a breach action): a list for the Court's judgment, no test.
- s 12E(2)-(5) (the Minister's declarations, the insurer's offence): administration and an offence by the insurer.
- ss 13, 18-22, 24-27, 29, 30, 32, 34, 35 (sale powers, receipts, compounding, raising money, purchaser protection,
  devolution, insurance money, custody, reversionary interests, audit, agents abroad, concurrence, delegation abroad,
  rents and covenants, calls on shares, notice): powers of the trustee or protections of third parties with no fact
  test for the beneficiary beyond those encoded. s 26(2) (the trustee need not act on a reversionary interest until
  required in writing, with costs provided) and s 27(4) (a company trustee's audit fee needs the Court's approval) could
  be added.
- ss 31(2)-(4), (10)-(12), (14) (what appropriation extends to, valuation, its binding effect, purchaser protection): no
  test for the beneficiary beyond the consents.
- s 33(1)(b), (2), (4), (5) (form and publication of the notice): taken as one fact ("advertised as section 33 requires").
- s 37(4) (annuities) and the proportionate-part proviso to s 37(1): could be added; no question asks them.
- s 40, 41(4), (5), (7), (8), (10), 42, 43, 45-47 (number of trustees of land, who may exercise the power, new trustees'
  powers, vesting on appointment, evidence of vacancy, disclaimer, trustee companies): machinery of appointment; s 42(1)(c)
  is the same rule as s 44(1) and is noted there.
- ss 49, 50, 52-54, 56-62 (effect of orders, other vesting orders, commission of inquiry): the Court's machinery; the
  beneficiary's own route (s 51(2)(i)) and the minor's (s 55) are in.
- ss 65, 66 (absent trustee as defendant, costs): the Court's powers with no test.
- ss 71-76, 78 (custodian trustees, convicts, settled residue, periodical payments, foreign representatives, indemnity
  to banks): not the focus, or third-party protections.
- Schedules 1, 2: repeals and the form of notice.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 6(3), 33(1), 37, 41(1) -- `the date` n `months after`, `the day the person attains` -- a period of months or
  years ends on the same day of the month, or the month's last day where it is shorter (two months from 31 December is 28
  February; a person born 29 February attains an age on 28 February) -- 1 March.
- **F2** s 6(3) "at least once in each year" -- `s 6(3) -- what became of the yearly review` -- within one year of the last
  review (or the first investment), the anniversary itself in time -- once in each calendar or financial year.
- **F3** s 2(3) "if and so far only as a contrary intention is not expressed" -- the s 37 and s 38 rules -- a contrary
  intention: JUST FALSE for s 37 (the "only"); NOTHING for s 38's amount (the instrument then decides) -- JUST FALSE for
  both.
- **F4** s 11(1) "Subject to the instrument creating the trust" -- `s 11 -- the trustee may provide the home` -- an
  instrument that forbids buying or arranging a home: JUST FALSE -- NOTHING (the instrument, not the Act, answers).
- **F5** s 14 "may, if so requested in writing ..., sell" -- `s 14 -- the trustee may sell at a beneficiary's written
  request` -- a power only, JUST TRUE meaning the trustee may sell -- a duty to sell on request.
- **F6** s 15 "No sale ... shall be impeached ... unless" -- `s 15 -- the sale may be impeached ...` -- the "unless" met:
  JUST TRUE -- NOTHING (s 15 merely stops barring; the challenge still needs a ground).
- **F7** s 17(3) "shall ... include provisions" -- `s 17(3) -- the deferred payment terms meet the minimums` -- terms
  short of a minimum: FALSE (a "shall" not met) -- NOTHING. The s 17(3)(c) "or for such less period as may be specified"
  is read as allowing any period of at most six months.
- **F8** s 17(4)(a) "at any time after two-fifths of the purchase money has been paid" -- `s 17(4) -- the trustee may
  convey ...` -- once exactly two-fifths is paid -- only once more than two-fifths is paid.
- **F9** s 36(1) "nor for any other loss unless the same happens through his own wilful default" -- `ss 28, 36 -- the
  trustee is shielded from the loss` -- the wilful default exception read across every head (another trustee, banker,
  agent, securities) -- only for "any other loss".
- **F10** s 38(1) "an amount not exceeding in all $2000 or half that capital (whichever is the greater)" -- `s 38(1) --
  the cap without the Court` -- "that capital" is the capital before any s 38 advance; "in all" totals every advance --
  half of what remains at each advance.
- **F11** s 41(1) "remains out of Victoria for more than one year" -- `s 41 -- who may appoint a replacement trustee` --
  from the day after the first anniversary of leaving -- counted in days (365).
- **F12** s 48(1) "whenever it is expedient ... In particular ... the Court may make an order ... in substitution for a
  trustee who is convicted ..., or ... bankrupt" -- `ss 48, 64 -- the Court may appoint ...` -- a particular ground is
  enough on its own (JUST TRUE); neither ground nor expedience: JUST FALSE ("whenever", ruling (c)) -- a particular ground
  still needs expedience.
- **F13** s 51(2)(i) "for twenty-eight days next after a request in writing" -- `s 51(2)(i) -- what my written request
  led to` -- the request day is day 0, acting on day 28 is in time, and the case for a vesting order opens on day 29 --
  acting on day 28 is already late.
- **F14** s 31(6)(a) "by the trustee thereof (if any) not being also the trustee making the appropriation" and (8) "save
  that if there is a trustee of the legacy share or interest his consent shall be required" -- `s 31 -- a consent for my
  share is needed`, `s 31 -- who may consent for my share` -- in the list of who may consent, a separate trustee appears
  only for a settled share or annuity fund (s 31(6)(a)); in whether a consent is needed, the saving in s 31(8) applies to
  any share that has a separate trustee -- the saving too only for a settled share.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "unless expressly prohibited" (s 5), "is not liable" (ss 12, 12A), "shall not exceed" (s 23), "shall not
be made so as to affect prejudicially" (s 31(1)(a)), "no consent shall be required" and "shall not be necessary" (s 31(8),
(9)), "shall not apply" (ss 37(5), 63A(4)), "only if" (ss 16(3), 37(3)), "unless" (ss 15, 31(5), (6), 38(5), 63A(1)
proviso), the "if", "where" and "whenever" conditions of ss 11(2), 12A, 12D, 12E, 14, 16, 41(1), 41(6), 44, 48, 51(2)(i),
55, 63, 67, 68, and the periods "during the minority", "on attaining the age of eighteen years ... thenceforth" (s 37),
"at the expiration of the time fixed" (s 33(3)) and "after two-fifths ... has been paid" (s 17(4)) give `JUST FALSE`.
`NOTHING` is answered where ss 6(1), 6(3), 38 defer to the instrument or the Court (*points outside the text*), where
ss 6(2), 8(1), 8(2), 12, 12B, 15, 16, 23, 37(3), 77 do not reach the case (*limited by its own wording*, *silent*), where
s 63A(1) does not list the person (an adult able to assent), and where ss 48, 51(2)(i), 63, 64 leave an applicant who is not beneficially
interested or absolutely entitled unaddressed (*silent*: the lists are not closed with "only").

## What the Act turns out to say

1. **The Act does not itself supervise a minor's damages.** The focus names the Court's supervision of damages held for a
   minor. No section of this Act puts a child's compensation or damages under the Court's control: it gives the trustee
   who holds them powers and duties (Part I, ss 37, 38), lets the trustees pay money into the Supreme Court (s 69, a
   permission, not a requirement), and lets the Court make orders for a minor's property (s 55), consent to larger
   advances (s 38), consent to appropriations for a minor (s 31(7)(a)) and approve variations on a minor's behalf
   (s 63A). Where a court's order holds a child's damages in court or with a trustee, that comes from the rules of court
   and the order itself, outside this Act and not deposited. Encoded: the Act's pieces only.
2. **s 17(4)(a) cross-refers to a provision that no longer exists in that form.** It requires a mortgage taken back on a
   deferred-payment sale to "include provisions to the like effect as those set out in subsection (2) of section eleven of
   this Act". Section 11 was substituted in 1995 (No. 104/1995 s 4); s 11(2) now lets a trustee keep a dwelling house for
   a beneficiary and contains no mortgage provisions. The reference looks stale (it presumably meant the covenants of the
   old s 11(2) or of s 16(1)). Not encoded (no question asks the mortgage's contents). For a lawyer.
3. **s 12E(1)(c) needs insurance "in the prescribed form", but nothing prescribes one.** The Act has no regulation-making
   section, and s 12E(3) lets the Minister specify terms and conditions by Gazette notice, not a form. Asked as a fact.
4. **s 12B states no rate of interest** for "the difference ..., with interest". The interest is an input.
5. **s 36(1) still shields a trustee from "the insufficiency or deficiency of any securities"**, a 1958 text that sits
   beside the 1995 prudent-person duties of s 6 and the preserved general-law duties of s 7 (including the duty to invest
   in investments that are not speculative). The shield is encoded as written; it does not answer whether s 6 was
   breached in choosing the securities. Asserted.
6. **s 38's $2000 is unindexed and can exceed the capital.** "$2000 or half that capital (whichever is the greater)" lets
   a trustee advance the whole of a share of $2000 or less. Encoded as at most the capital itself. Asserted. s 33(2)'s
   $2000 small-estate threshold is likewise unindexed.
7. **s 77 does not say what the five per cent is reckoned on** (the trust funds, the income, or what passes through the
   trustee's hands), nor over what period. The base is an input. Asserted.
8. **s 31(8) "an investment authorized by law"**: since 1995 s 5 lets a trustee invest "in any form of investment", so on
   one reading every investment is authorised by law and s 31(8) reaches every appropriation of an investment. Asked as a
   fact.
9. **Older wording.** s 39(1)(b)(i) speaks of the principal beneficiary's "wife or husband" (not a domestic partner); s 68
   still mentions "a married woman restrained from anticipation"; s 37(2) still turns on marriage under 18. Encoded as
   written ("spouse" in the questions means wife or husband).
10. **s 6(3) "at least once in each year"** does not say whether the year is a calendar, financial or rolling year (F2).
11. **s 3 against s 69(7).** "Court" includes the County Court for property within its limit, but payment into court
    under s 69 is to the Supreme Court only. Both encoded.
12. **Conversion.** s 17(4) prints its paragraphs (a) and (b) as "(4) (a)" with the subsection number on the paragraph line;
    s 12E(4)'s penalty ("50 penalty units.") stands on its own line. The text is otherwise as the Word file has it.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- The rules of court on money recovered for a minor or a person under a disability, and the County Court Act 1958's
  jurisdictional limit, neither deposited or encoded here.
- A lawyer's view on findings 1, 2, 5 and 8 and forks F3, F6, F9, F10 and F12; a seat for the individual trustee; an
  independent test pass and a human gate.
