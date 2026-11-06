# Industrial Relations Act 1979 (WA) -- baseline encoding, the employee

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`ira-dates.l4`,
built-in date functions only, no daydate), the shared rules and the one regulative rule in `ira-rules.l4`, and the
employee's 36 questions in `ira-employee.l4`, which imports both. The cases are in `ira-cases.l4`.

The focus given was **the state system for employers that are not constitutional corporations**, and within it the
provisions a person bringing or answering a claim meets: whether the state system reaches the employment, who is an
employee, unfair dismissal and denied contractual benefit claims to the Industrial Relations Commission, enforcement of
entitlements and orders in the industrial magistrate's court, stop bullying applications, sexual harassment in connection
with work, and the Part 6B protections (damaging action and sham contracting).

## Edition

- **Act:** Industrial Relations Act 1979 (WA), No. 114 of 1979, compilation as deposited at
  `../../registers/source-bundle/mrdoc_49816.txt` (sha256 e6d52776...46c37ba3), retrieved from the Western Australian
  Legislation website on 7 September 2026. Its compilation table runs to the Industrial Relations Legislation Amendment
  Act 2024 (No. 43 of 2024), whose ss 100-103 commenced on 1 September 2026; the only uncommenced amendment listed is the
  State Superannuation (Transitional and Consequential Provisions) Act 2000 s 75, not encoded. Check against the current
  compilation before relying on anything here.
- **Regulations setting the Act's numbers:** the Industrial Relations (General) Regulations 1997, deposited at
  `subjects/au/wa/industrial-relations-general-regulations-1997/registers/source-bundle/mrdoc_48228.txt` (version
  01-h0-00, from 23 January 2025). Read: r 5(1) and r 6 (the s 29AA prescribed amount: $90 000, indexed every 1 July by
  an ABS earnings ratio, rounded to $100), r 5(2) (how the contract salary is worked out), r 7 and Schedule 4 (local
  governments and regional local governments declared under s 80A from 1 January 2023). The indexed amount in force on a
  given day is published by the Commission and is not in the text, so it is an input; the r 6 indexation factor is a
  formula over ABS figures, also not computed. The r 5(2)(b), (c) formulas were lost in conversion (finding 6).
- **Borrowed terms asked as facts:** national system employer (Fair Work Act 2009 (Cth) s 14), "harsh, oppressive or
  unfair", "impracticable", "reasonable management action carried out in a reasonable manner", "unwelcome", "reasonable
  excuse", the s 7A real-substance judgment, anti-discrimination legislation (listed in s 51BZD(1), in the description).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read
(an evaluation error, `DATE_FROM_DMY produced an invalid date` for 29 February 2030, showed as `DiagnosticSeverity_Error`
while the date helpers were written; `the corresponding date` now avoids it).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ira-dates.l4` | 0 | 0 | 0 | 0 |
| `ira-rules.l4` | 0 | 0 | 0 | 0 |
| `ira-employee.l4` | 0 | 0 | 0 | 0 |
| `ira-cases.l4` | 0 | 0 | 159 | 159 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; the 28
days on the last day and the day after (dismissed Monday 2 March 2026: 30 / 31 March), a last day on a Saturday and on a
Sunday (moved to Monday 13 April 2026), a late referral accepted and not; the 6 years of s 82A on the last day and the day
after, a last day on a Saturday (Monday 9 March 2026), from 28 and 29 February 2024 (both end Thursday 28 February 2030)
and from 31 December 2019; s 83A(2) back from 29 February 2028 (1 March 2022) and with a record failure before and after
the proceedings began; s 51BU's 24 months on the last day and the day after, from 29 February 2024 (28 February 2026);
the 14 days of ss 51BK, 51BV with a Saturday; the s 29AA salary bar at the prescribed amount and $1 over, with and
without an industrial instrument; each penalty figure; each s 23A remedy branch; the regulative rule on day 28 and day 29.

## Seat

**The employee** (`ira-employee.l4`): the individual employee of an employer in the WA state system (a sole trader, a
partnership, an unincorporated association, a non-trading body, the State public sector, or a local government declared
under s 80A), and, for Division 3AA, the worker who is bullied or the person sexually harassed in connection with work.
"Is my employment in the state system?", "Am I an employee?", "Can the Commission hear my unfair dismissal claim, by when,
and what can it order?", "Can I claim a contractual benefit?", "Can I enforce my award, by when, and how far back?",
"Was I bullied, can I apply?", "Was I sexually harassed in connection with work, is the employer liable, where can I go?",
"Was the action against me unlawful, what can the court order?". No seat for the Commission, the Registrar, an industrial
inspector or the courts: their determinations and opinions are asked as facts. An employer seat (the small business
owner in the state system) would be a natural second layer; not written.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the General Regulations are read for the
  prescribed amount, the salary rule and the s 80A declarations (see Edition). The Interpretation Act 1984 (WA) ss 61, 62
  are read for counting periods (forks F1-F3), deposited at
  `subjects/au/wa/interpretation-act-1984/registers/source-bundle/mrdoc_49111.txt`.
- **The actors the text names.** Followed: the employee, worker and aggrieved person, the employer and principal, the
  Commission, the industrial magistrate's court, the Fair Work Commission.
- **Judgments answered conditionally.** Followed: "the Commission determines ... harsh, oppressive or unfair", "considers
  ... impracticable", "considers that it would be unfair not to [accept]", "reasonably believes", "reasonable excuse",
  "proves" (ss 51BS(3), 97A(2), 97D(2), 97E(2)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: employee (s 7, with s 7A asked), worker (s 51BH,
  s 51BG(2)(c), (3)), bullied at work (s 51BI), sexually harasses and in connection with work (ss 51BQ, 51BR), damaging
  action (s 97), serious contravention (s 83EA), industrial instrument and prescribed amount (s 29AA(5)) are worked out.
- **One case.** One employment, one dismissal, one allegation.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 7(1) (employee, employer), 7(1a), 7A, 24A, 81CAA (who is an employee and who must prove it); 80A with regs r 7,
Sch 4 (the state system); 29(1)(c), (d), (e), (f), 29(2)(a), (3), 29AA (referring unfair dismissal and contractual benefit
claims, the Fair Work Commission bar, the salary bar) with regs r 5; 23A(1)-(9) (unfair dismissal: matters to weigh,
remedies, the compensation cap); 82A, 83(1), (3), (4A), 83A, 83B(3), (5)(b), (7), 83E(1), (6), 83EA(2)-(4), 83EB
(enforcement in the industrial magistrate's court, its time limit, how far back, penalties, onus); 51BG, 51BH, 51BI,
51BJ, 51BK(1), 51BM(3) (bullying); 51BQ, 51BR, 51BS, 51BT(1), 51BU, 51BV(1), 51BZD (sexual harassment); 97, 97A, 97B(5),
97D, 97E, 97G(5) (damaging action, sham contracting). In descriptions only: ss 23A(10)-(12), 51BM(3), 51BZ, 51BZC, 83B(2)
(no fee), 84T.

**Regulative rule:** one, `the step must be taken` in `ira-rules.l4`: `PARTY` the actor `MUST` take the step `WITHIN` the
days allowed, `LEST BREACH ... BECAUSE` the time has passed. It runs by EVALTRACE inside "Is my unfair dismissal referral
in time or accepted" (s 29(2)(a)) and "Is my application to the industrial magistrate's court in time" (s 82A); both take
only plain facts.

**Out, and why:**
- ss 1-6, Part II Div 1 (ss 8-22), ss 22B, 24, 25-28, 29A-36, Part II Divs 2A-2G except as above (awards, industrial
  agreements, bargaining, conciliation, records, right of entry), Div 3 (General Orders), Div 4 and 5 (registered
  organisations), Part 2AA Div 2 (transition of instruments), Parts IIB, IIC, IV, V, 6C, VID (EEAs, apart from naming them
  in s 29AA(5)), VII and the Schedules: machinery, collective bargaining or the Commission's own procedure; they give the
  individual claimant no step, time limit or entitlement a fact can test.
- Division 2AA (public sector employment: s 36AA decisions, breach of public sector standards claims, reclassification)
  and s 29(1)(g)-(j), (l), (2)(b)-(d): a distinct public sector stream, worth its own layer.
- Division 3A (flexible working arrangement disputes, s 29(1)(k)) and Division 3B (equal remuneration, s 29(1)(b)):
  the entitlements live in the Minimum Conditions of Employment Act 1993 and in equal remuneration orders; not encoded here.
- ss 23B, 51BL, 51BN, 51BW, 51BX-51BY, 51BZ, 51BZA-51BZC, 83C-83D, 83F, 84, 84A-84V, 96A-96L, 97C, 97F-97H: the
  Commission's and court's orders and discretions, third parties, appeals, infringement notices, undertakings, compliance
  notices, freedom of association offences (crimes, not claims), advertising; s 97F appears only in the s 97G question.
- The Fair Work Act 2009 (Cth): whether an employer is a national system employer is asked, not worked out.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "no later than 28 days after the day on which" (s 29(2)(a)), "within 14 days after" (ss 51BK, 51BV), "within 6
  years after the day on which" (s 82A) -- the date functions -- the day of the event excluded (Interpretation Act s
  61(1)(b)) -- the event day counted.
- **F2** Interpretation Act s 61(1)(e) -- `the time limit of ...` -- a last day on a Saturday or Sunday moves to the Monday;
  public service, bank and public holidays are not computed (none deposited), so a last day on one reads a day early --
  holidays asked as a fact; or s 61(1)(e) not applied to the Commission's own s 51BK duty, which this encoding moves too.
- **F3** periods in years (ss 82A, 51BU, 83A(2)) -- `the last day of ... years after`, `the earliest day of ... years
  before` -- reckoned as 12 N months under s 62(3), to the corresponding date less one, the last day of February where
  there is no 29th; backwards (s 83A(2)), 29 February in a year with none taken as 1 March -- 28 February.
- **F4** s 51BU "more than 24 months after" -- `Can my sexual harassment proceeding be dismissed as late` -- a proceeding on
  the last day of the 24 months is not "more than"; not moved for a weekend (it is a power to dismiss, not a time limited
  for doing a thing); within 24 months the answer is `NOTHING` -- `JUST FALSE`.
- **F5** s 23A(6) "reinstatement or reemployment would be impracticable" -- the remedies and compensation questions --
  both must be impracticable (s 23A(4) re-employment is itself the fallback when reinstatement is impracticable) --
  either one impracticable suffices.
- **F6** s 29(1)(d) "a benefit, other than a benefit under an award or order" -- `Can the Commission determine my
  contractual benefit claim` -- `JUST FALSE` (that benefit is enforced under s 83 instead) -- `NOTHING`.
- **F7** s 29(1)(c) for a person who was not the employer's employee, s 29(1)(d) for a benefit not due under the contract,
  s 51BJ for a non-worker or one without the belief, s 83E(6) for a person not directly affected, ss 24A, 81CAA outside
  their facts -- `NOTHING` (limited by its own wording) -- `JUST FALSE`.
- **F8** s 23A(8), (9), s 83B(7) "6 months' remuneration", "12 months' remuneration" -- the compensation and s 83B
  questions -- half and the whole of a year's remuneration, the person giving the yearly figure (the average rate of s
  23A(9) included) -- 26 and 52 weeks of a weekly rate.
- **F9** s 83A(2)(a) "or" (b) -- `From what day can my underpayment be ordered` -- whichever reaches further back -- (b)
  displacing (a) once the record failure is found.
- **F10** s 97A(1) "is able to make" and s 97A(2) "made ... or proposed to make" -- `Did my employer take unlawful damaging
  action against me` -- one input covering being able to make, making or proposing to make the inquiry or complaint, and
  the employer's s 97A(2) proof answering it -- the reason element tested separately from the onus.
- **F11** s 29AA(5) prescribed amount "(a) $90 000 per annum; or (b) the salary specified ... in regulations" -- the
  salary bar -- the indexed regulation figure governs, asked as an input -- (a) as a floor.
- **F12** s 80A and the FW Act s 14 -- `the state system reaches the employment` -- `JUST TRUE` for an employer that is
  not a national system employer or is declared, `NOTHING` otherwise (the FW Act decides) -- `JUST FALSE` for a national
  system employer.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "means" definitions (ss 7 employee, 97 damaging action, 51BQ, 83EA(2)), "must not determine ... if" (s 29AA(1),
(3), (4)), "if, and only if" (s 23A(6)), "may make an order ... if" (s 23A(1)), "does not apply if" and "unless the
principal proves" (ss 51BI(2), 51BS(3), 97D(2)), "cannot be made ... unless" (s 51BZD), "must not make the order if"
(ss 97B(5), 97G(5)), "must not be made otherwise than under subsection (1)" (s 83(3)), "may only be made by an industrial
inspector" (s 83E(6B)), the periods of ss 29(2)(a) and 82A, and the "if" conditions of ss 51BH, 83EB give `JUST FALSE`.
`NOTHING` is answered where the FW Act decides (s 80A, F12: *points outside the text*); where ss 24A, 29(1)(c), (d), 51BJ,
51BU, 83E(6)(a) speak only of their own case (*limited by its own wording*, F4, F7); where the r 5(2)(b), (c) formulas
are lost (*points outside the text*); and for a referral or application before the dismissal or contravention (*silent*).
"(other than X)" in s 29(1)(d) is F6.

## What the Act turns out to say

1. **Only unfair dismissal has a time limit in s 29(2).** A denied contractual benefit claim (s 29(1)(d)), a bullying
   matter (s 29(1)(e)) and a sexual harassment referral (s 29(1)(f)) have none in the Act; s 51BU gives the Commission a
   power to dismiss a sexual harassment proceeding after 24 months, not a bar. The contractual benefit question says so.
2. **s 97A(1) and (2) do not match.** (1) prohibits damaging action because the employee "is able to make" an inquiry or
   complaint -- something every employee is -- while the reverse onus in (2) is discharged by proving the action was not
   because the employee "made ... or proposed to make" one. Encoded with one input for both (F10). Asserted (damaging
   action with the employer's proof: no contravention).
3. **s 29AA(5) gives the prescribed amount twice.** "(a) $90 000 per annum; or (b) the salary ... in regulations"; the
   regulations take $90 000 and index it, so (a) and (b) part company every 1 July and "or" does not say which governs
   (F11). Asserted at $90 000 / $90 001 and at a test indexed figure.
4. **s 23A(6) "reinstatement or reemployment would be impracticable"** read as both (F5); compensation is otherwise
   unavailable. Asserted (reinstatement impracticable, re-employment practicable: no compensation).
5. **s 83A(2)(b) can only help if the record failure came before the proceedings.** A failure during the proceedings gives
   a later start than (a). Read as whichever reaches further back (F9). Asserted both ways.
6. **The regulations' r 5(2)(b) and (c) formulas are lost** in the deposited text (the "formula" lines are empty), so the
   salary for an employee with less than 12 months' service or with unpaid leave cannot be worked out; the question
   answers `NOTHING` there. A `mrdoc_48228.formulas.md` sidecar from the authorised PDF would close it. Asserted.
7. **s 83B(7) sets a floor**: when the court revokes an unfilled reinstatement order it must order at least 6 months'
   remuneration and at most 12, against the 6-month ceiling of s 23A(8). Asserted.
8. **The Act never says which employers it reaches.** Its "employer" (s 7(1)) is any person employing an employee; the
   limit on the state system comes from the Fair Work Act 2009 (Cth), and s 80A only lets the State pull back FW Act s 14(2)
   employers (the local governments of Schedule 4). The coverage question answers `NOTHING` for a national system employer
   (F12). Asserted.
9. **s 51BK(1), 51BV(1) bind the Commission to start within 14 days** but give the applicant no remedy if it does not;
   the date is given for information.

## Before this is worth relying on

- Check the text against the authorised PDF and the current compilation (retrieved 7 September 2026).
- The indexed prescribed amount for each year from 1 July (published by the Commission), or a deposit of the ABS figures r 6
  uses; the r 5(2)(b), (c) formulas (finding 6).
- The public service, bank and public holidays for the Interpretation Act s 61(1)(e) (F2).
- Layers not written: the employer seat; Division 2AA (public sector claims); Divisions 3A and 3B; the Minimum Conditions
  of Employment Act 1993 and Long Service Leave Act 1958 entitlements that s 83 enforces.
- A lawyer's view on findings 2, 3 and 5 and forks F4-F6, F9-F12; an independent test pass and a human gate.
