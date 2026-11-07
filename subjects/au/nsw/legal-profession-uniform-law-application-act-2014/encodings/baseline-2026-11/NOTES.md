# Legal Profession Uniform Law Application Act 2014 (NSW) -- baseline encoding, the client

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 2 March 2025). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). One regulative rule (the s 83 review period)
run by `EVALTRACE` inside an exported question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This is the first encoding of the Act; nothing existing was touched. The Act's job (s 4) is to apply the Legal
Profession Uniform Law as a law of NSW and add NSW's own provisions. The Uniform Law itself (Schedule 1 to the Victorian
application Act) is not deposited, so where an NSW provision turns on it (a costs agreement complying with Division 4 of
Part 4.3, a default covered by Part 4.5, the s 195(4) interest rate) the answer is asked as a fact. The encoding takes the
NSW provisions a client bringing or answering a claim meets: the maximum costs in personal injury damages matters
(Schedule 1), costs where a claim or defence has no reasonable prospects of success (Schedule 2), fixed costs (s 59),
costs assessment, review and appeal (Part 7) and claims against the Fidelity Fund (Part 9 Division 2).

## Edition

- **Act:** Legal Profession Uniform Law Application Act 2014 No 16, corpus document
  `nsw_legislation:2025-03-02/act-2014-016` (in force 2 March 2025), deposited at
  `../../registers/source-bundle/act-2014-016.txt` (sha256 36978c4d...ff5f7 as committed), taken from the Open
  Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au returned a bot challenge. Not the
  authorised text.
- **Not deposited:** the Legal Profession Uniform Law (Schedule 1 to the Legal Profession Uniform Law Application Act 2014
  (Vic)); the NSW local regulations (Legal Profession Uniform Law Application Regulation), which may replace the Schedule 1
  figures (cll 2(2), 3(5)), fix costs under s 59, prescribe disclosure under Sch 1 cll 4 and 5 and prescribe further
  "court documentation" under Sch 2 cl 4(4)(d); the costs assessment rules. The Act's own figures are used; a replacement
  figure would change the Schedule 1 answers. What the regulations require is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lpula-claims.l4` | 0 | 0 | 0 | 0 |
| `lpula-cases.l4` | 0 | 0 | 114 | 114 |

Every expected value was worked by hand from the text, with the edges: $100,000 recovered and $100,000.01; $50,000, where
20% meets the $10,000 floor (and 15% meets the $7,500 floor); the cl 8 deductions taking a payment across $100,000; each
cl 1(2) exclusion; a plaintiff who recovers nothing; both cl 3 increases at once (2 times the additional amount); an
offer equal to the award; a settlement with no award; $24,999 and $25,000 (District Court), $99,999 and $100,000 (Supreme
Court) in dispute; the 30th and 31st day after a certificate is forwarded, across a leap-year February; an application
on the day of a final costs determination and the day after.

## Seat

**The client**: the person bringing or answering a claim (usually the injured person claiming personal injury damages)
who pays, or is paid, legal costs. Every exported question is one the client would ask ("Does the maximum costs limit
apply to my claim?", "What is the most my lawyers can be paid?", "Can I be ordered to pay the other side more?", "Can my
law practice act on my claim?", "By what day must I apply for a review?", "Can I claim against the Fidelity Fund?").
Schedule 1 is two-sided, so the side (plaintiff or defendant) is an input and both mirror questions are exported. The
duties of law practices (Sch 2 cll 2, 4, 5(4); Sch 1 cl 2(4)(a)) are encoded as what they mean for the client. No seat is
written for the law practice: its duties here are owed to the client and the court, and a law practice seat could be
added beside this one. Officials (the court, costs assessors, review panels, the Manager, Costs Assessment, the Law
Society Council, the NSW Commissioner) get no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed as far as deposited: the local regulations and
  the Uniform Law are not deposited, so the Act's figures are used and what they would add is asked.
- **The actors the text names.** Followed: the plaintiff, the defendant, the law practice and its legal practitioner
  associates, the court, the costs assessor, the review panel, the Manager, Costs Assessment, the Law Society.
- **Judgments answered conditionally.** Followed: the responsible lawyer's reasonable belief (Sch 2 cl 2), whether it
  "appears" to the court (Sch 2 cl 5, Sch 1 cl 5(4)), the trial court's finding and its rebuttal (Sch 2 cl 6), a cl 6
  exclusion order, the Manager's satisfaction of hardship (ss 68(3), 83(4)), the share of the maximum agreed or ordered
  (cl 7) are inputs; a "may" is answered as "may", never as what will be done.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: "amount recovered" (cl 8), the maximum costs
  (cll 2, 3), a reasonable offer of compromise (cl 5(2)), "court documentation" (cl 4(4)), "ordered costs" (s 63).
  Asked: "personal injury damages" (Civil Liability Act 2002), "work injury damages", the Uniform Law terms.
- **One case.** One claim (with its costs), one costs assessment, or one default.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 4 (as the reason the Uniform Law's terms are asked); s 59(2) (fixed costs); Schedule 1 (cll 1-8, maximum costs
in personal injury damages matters, through s 61); Schedule 2 (cll 1-6, no reasonable prospects of success, through
s 62); Part 7 ss 63, 66, 68(3), 70(4)-(5), 74(1), 81, 83(1), (1A), (4), 86, 87(2), 89(1), 90; Part 9 Division 2
ss 122, 124 (claims against the Fidelity Fund).

**Out, and why:**
- Part 1 (name, commencement, definitions used only as glosses), Part 2 Division 1 ss 5-9 and Division 2 (designations,
  the Interpretation Act's reach, double jeopardy): machinery and allocation of functions between authorities.
- Parts 3 and 4 (the Admission Board, the Commissioner, the Councils, practising certificates and their fees): the
  regulators and the lawyer's own certificate, not the client's claim.
- Part 5 (statutory deposits and the Public Purpose Fund), Part 8 (professional indemnity insurance), Part 9 Division 1
  (the Fidelity Fund's establishment and management), s 123: fund administration; nothing for the client to ask apart
  from s 122.
- Part 7 machinery: ss 64-65, 67, 69, 70(1)-(3), (5A), 71-73, 75-80, 82, 84-85, 88, 89(2)-(4), 91-93G (how assessors and
  panels work, the rules committee, assessors' appointment and protection).
- Part 10 (NCAT review of certificate decisions and of compensation orders over $10,000 and disciplinary determinations):
  rights of the lawyer, not the client; a seat for the lawyer could take them.
- Part 11 (NCAT disciplinary procedure, including the Commissioner's 6-month period in s 137) and Part 12 (registers):
  the Commissioner's and the lawyer's process; the client complainant is not a party.
- Part 13 (penalty notices, liability, regulations) and Schedules 3-10 (boards, offices, HIH insurance, transitional
  provisions): machinery.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** Sch 1 (all clauses) "a claim for personal injury damages" -- every Schedule 1 question -- a claim that is not for
  personal injury damages is outside the Schedule's scope, which has no "only": `NOTHING` -- `JUST FALSE`, reading cl 2(1)'s
  "If the amount recovered on a claim for personal injury damages ..." as an "if" condition that the claim fails.
- **F2** Sch 1 cl 1(2)(a) -- `Schedule 1 fixes maximum costs for` -- a claim under the Motor Accident Injuries Act 2017 is
  not one of the listed exclusions, so the Schedule applies on its words (`JUST TRUE`) -- the reference to the repealed
  motor accidents Acts carries over to their successor (Interpretation Act 1987 s 68 or a savings provision), so the
  Schedule does not apply.
- **F3** Sch 1 cl 2(6) "the amount sought to be proved by the plaintiff at the hearing" -- `What are the maximum costs for
  my side` -- one input, the amount the plaintiff sought (at the hearing where there was one) -- where proceedings were
  started but settled before a hearing, the amount claimed in the originating process.
- **F4** Sch 1 cl 5(2) "terms that are no less favourable" -- `the offer of compromise is reasonable` -- compared on the
  amount alone (an award at least the plaintiff's offer, or at most the defendant's) -- a comparison of all the terms,
  including costs and interest.
- **F5** Sch 2 cl 5(3) "cannot be made after a final determination" -- `Can I seek repayment of the costs from my law
  practice` -- an application made on the day of the final determination is not "after" it -- the same-day application
  is after it if the determination came earlier that day.
- **F6** s 83(1) "within 30 days after the certificate ... has been forwarded" -- `By when must I apply for a review`,
  `Is my review application in time` -- counted from the day after forwarding (Interpretation Act 1987 s 36(1)), so the
  30th day after is the last day -- counting the day of forwarding.
- **F7** s 83(1) with Interpretation Act 1987 s 36(2) -- the same two questions -- a last day falling on a weekend or
  public holiday is not moved to the next business day (the borrowed rule is not encoded; an extension by the Manager is
  the input that covers it) -- move it.
- **F8** s 89(1) "A party to a costs assessment that has been the subject of a review under this Part may appeal" --
  `Can I appeal the review panel's decision` -- with no review, `section 89 gives me no appeal` (the grant's own condition)
  -- `NOTHING`, as a grant limited in its own wording.
- **F9** Sch 1 cl 3(2) "on the application of a party ... the other party" -- `the number of clause 3 additional amounts
  for` -- a rehearing ordered on the other side's application increases my maximum; on my own application, or on the
  court's motion, it does not -- where both sides applied, both maxima increase (not encoded: the input is the other
  side's application only).
- **F10** s 81(1) "a rate ... that does not exceed" -- `Can the assessor set this interest rate` -- a rate above the s
  195(4) rate answers `NOTHING` (a grant limited in its own wording) -- `JUST FALSE`.
- **F11** Sch 2 cl 3 "This Schedule does not apply to legal services provided as a preliminary matter" -- `Can my law
  practice act on my claim or defence` -- `JUST TRUE` (Schedule 2 does not stop the preliminary work) -- `NOTHING` (the
  Schedule is silent once it does not apply).
- **F12** ss 68(3), 83(4) "may waive or postpone ... if satisfied" -- `Can my application fee be waived` -- without the
  Manager's satisfaction, `JUST FALSE` (an "if") -- `NOTHING`.

## What the Act turns out to say

1. **The motor accidents exclusion names repealed Acts.** Sch 1 cl 1(2)(a) excludes claims under the Motor Accidents Act
   1988 and the Motor Accidents Compensation Act 1999, both since replaced by the Motor Accident Injuries Act 2017, which
   the clause (as at 2 March 2025) does not name. On the words, Schedule 1 reaches personal injury damages claims under
   the 2017 Act. Fork F2; asserted (`JUST TRUE`). The 2017 Act's own costs controls were not checked.
2. **"For the purposes of this section" in a Schedule clause.** Sch 1 cl 3(4) says "section"; the provision is a clause
   of a Schedule. A drafting slip with no effect on the answer.
3. **A plaintiff who recovers nothing still has a $10,000 maximum.** cl 2(1) turns on "the amount recovered", which is
   $0 when the claim fails, so the cap applies and the plaintiff's maximum is the $10,000 floor. Asserted.
4. **cl 3(2) increases only the other party's maximum.** A rehearing ordered on a party's application raises the
   maximum of "the other party"; nothing is said where both applied or the court acted of its own motion. Fork F9.
5. **A settled claim never makes an offer "reasonable".** cl 5(2) defines a reasonable offer by the court's
   determination, order or award, so cl 5 cannot lift the cap where the claim settles. Asserted.
6. **cl 5(3) of Schedule 2 bars an application, not the court.** After a final costs determination "an application ...
   cannot be made", but cl 5(1) lets the court act "of its own motion" too; read literally the court's own power
   survives. The encoding answers only the client's application ("too late to apply").
7. **The review period runs from a forwarding the client may not see.** s 83(1) counts 30 days from when the
   certificate was "forwarded to the parties in accordance with the regulations or the costs assessment rules"; neither
   is deposited, so the forwarding day is asked.
8. **"The amount of costs in dispute" (s 89(1)) is not defined**: it is asked. The leave thresholds are "less than"
   $25,000 and $100,000, so exactly those amounts need no leave. Asserted.
9. **The figures may have been replaced.** cll 2(2) and 3(5) let the local regulations replace $100,000, $10,000, 20%,
   15% and $7,500; the regulations are not deposited, so the Act's figures are used.

## Questions (exported)

`lpula-claims.l4` (22), in the Act's order:

- s 59: `Does a fixed cost stop this charge`.
- Schedule 1: `Does the maximum costs limit apply to my claim`, `What are the maximum costs for my side`, `What is the
  most one of my law practices may be paid`, `Does the maximum stop my law practice charging me more`, `Does the maximum
  protect me from paying the other side more`, `Does the maximum limit what the other side can be ordered to pay me`,
  `Can the court make my law practice repay the extra costs of refusing the offer`.
- Schedule 2: `Can my law practice act on my claim or defence`, `Can my court document be filed`, `Can I seek repayment
  of the costs from my law practice`, `Can my law practice pass the indemnity on to me`.
- Part 7: `Can I apply for assessment of ordered costs`, `Can my application fee be waived`, `How much overpaid can I
  recover`, `Is the certificate a judgment`, `Can the assessor set this interest rate`, `By when must I apply for a
  review`, `Is my review application in time` (with the regulative rule), `Is the determination suspended`, `Can I
  appeal the review panel's decision`.
- Part 9: `Can I claim against the Fidelity Fund`.

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Deposit the Legal Profession Uniform Law Application Regulation and check whether it replaces any Schedule 1 figure,
  fixes costs under s 59, or sets the disclosure duties of Sch 1 cll 4 and 5.
- Deposit the Legal Profession Uniform Law and encode its costs provisions (Part 4.3) and fidelity cover (Part 4.5), so
  the inputs taken from it can be worked out.
- Have a lawyer review the forks, especially F1, F2 (motor accidents) and F4 (comparing offers).
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
