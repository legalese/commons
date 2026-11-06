# Federal Circuit and Family Court of Australia Act 2021 (Cth) -- baseline encoding, the party bringing a claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`fcfca-dates.l4`,
built-in date functions only, no daydate), the rules and the exported questions in one module (`fcfca-claims.l4`), and the
worked cases in `fcfca-cases.l4`.

The focus asked for: courts, procedure, time limits, damages (interest) and costs, as a claimant meets them. The Act is a
court constitution Act of 285 sections, most of them about judges, officers and administration. The encoding takes the
provisions a party to a civil claim in the Federal Circuit and Family Court of Australia (Division 2) actually meets --
where the claim goes and how it is heard, summary judgment, discovery, the overarching purpose and directions, mediation
and arbitration, interest before and after judgment, enforcement, costs and security for costs, review of a Registrar's
decision, appeals, suppression orders and vexatious proceedings orders -- and, from Chapter 3, the appeal routes and the
bar on starting family law cases in Division 1.

## Edition

- **Act:** Federal Circuit and Family Court of Australia Act 2021, Compilation No. 12, compilation date 10 June 2025
  (includes amendments up to Act No. 118, 2024; register id C2025C00376), the latest compilation when retrieved on
  13 October 2026, deposited at `../../registers/source-bundle/C2021A00012.txt`.
- **Numbers set elsewhere, not deposited, so asked as inputs:** the judgment interest rate "fixed by the Rules of Court"
  (s 212(3)(a)); the "time prescribed by the Rules of Court" for seeking review of a delegate's decision (s 256(1)(a));
  the judgments "prescribed" as needing leave to appeal (s 28(1)(b), regulations). The Federal Circuit and Family Court
  of Australia (Division 2) (General Federal Law) Rules 2021 and the regulations under the Act are not in Commons. The
  Family Law Rules 2021 are deposited but govern family law proceedings, which ss 211-215 exclude, so they set none of the
  numbers this encoding uses. The penalty unit (s 236) is set by Crimes Act 1914 s 4AA and indexed; the answer stays in
  penalty units.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. Two
deliberately wrong assertions (the s 211 total moved by one dollar; the s 215 last day moved by one day) were run once in
a scratch copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `fcfca-dates.l4` | 0 | 0 | 0 | 0 |
| `fcfca-claims.l4` | 0 | 0 | 0 | 0 |
| `fcfca-cases.l4` | 0 | 0 | 176 | 176 |

Every exported question has cases, with the edges: each Division route of s 135; each s 133 element missing in turn; both
summary judgment directions and the Family Law Act carve-out (child support kept); discovery with and without a
declaration; each consequence of ss 191 and 192 and the s 191A carve-out; each dispute resolution process with and
without consent in each kind of proceeding; each s 172(1) condition missing; the s 172(5) cap above, at and below the
claim; every s 211 bar; the s 211 amount with every excluded part, a paid liability, a liability paid after judgment,
judgment on the day the cause arose, and a year across 29 February 2028 (366 days); the s 212 amount at the Rules rate, a
lower rate, a "lower" rate that is higher, and payment on the day of entry; security for costs given on day 0, on the
last day, the day after, not yet given before and after the last day, and across 29 February 2028; review of a delegate's
decision on the last day, the day after, with further time, and across 29 February 2028; every kind of Division 2
decision for appeal, with and without a prescribed judgment; every High Court route; each suppression ground and each
kind of information; every s 239 route including a lawyer acting for the vexatious person; each s 241 and ss 243-244
outcome; s 242(4); each s 50 outcome.

**No mirror cases.** One seat.

## Seat

**The party bringing (or answering) a civil claim in Division 2** (`fcfca-claims.l4`): usually the applicant who brings a
claim for money, damages, a declaration or other relief -- a worker's Fair Work claim, a discrimination claim, a debt, a
Commonwealth tenancy dispute -- and the same person as appellant, as the person whose information may be suppressed, as
the subject of a vexatious proceedings application, or as the party affected by a Registrar's decision. "Which Division
does my claim go to?", "Can it be ended early?", "Do I have to go to mediation?", "How much interest can I get?", "Will I
pay costs?", "Am I in time to give security?", "Can I appeal?". Where a question is two-sided (summary judgment) the
person says which side they are on.

The Court, its Judges, the Chief Judge, the Chief Justice, Registrars, the Chief Executive Officer and the Minister get no
seat: their satisfactions, opinions, directions and orders are asked as facts. No second seat (respondent) was written:
the respondent's questions are the same rules asked from the other side, and the focus is the claimant.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. The instruments that set the numbers (Rules of
  Court, regulations) are not deposited, so the numbers are inputs, each named in the question's `@desc`. Where the Act
  sends the claimant to another Act (the Family Law Act 1975, the Fair Work Act 2009 s 570, the AHRC Act s 46PSA, the
  Public Interest Disclosure Act 2013 s 18, the Federal Court of Australia Act 1976 for general federal law appeals), the
  answer names that Act and stops.
- **The actors the text names.** Followed: the parties, the applicant, the party's lawyer, the Court, a Judge, the Chief
  Judge, the Chief Justice, the delegate, the mediator, the arbitrator, the High Court.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: "no reasonable prospect" (s 143);
  the s 176 declaration; failure of the overarching purpose duty (s 191); failure to follow a direction (s 192); "good
  cause" (s 211(3)(b)); the Court's interest rate (s 211(3)(c)); "justice so requires" a lower rate (s 212(3)(b)); each
  "necessary" ground (s 231); the Court's satisfaction under ss 239(1), 243 and 244(4); the Chief Judge's direction
  (s 135(5)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "family law or child support
  proceedings" (s 7, by s 132) and the narrower "proceedings under the Family Law Act 1975"; "Commonwealth tenancy
  dispute" (s 7, with s 133(1)); acting in concert (s 237). Asked: "vexatious proceeding" (s 7's definition is an
  inclusive list of judgments for the Court: "includes"), "question of law", "prescribed judgment", "cause of action".
- **One case is the text's natural unit.** Followed: one proceeding, one judgment, one order.
- **The Act's own terms, each with a plain gloss.** Followed in the constructor names and the comments.
- **Machinery out.** Followed: constitution of the courts, judges, officers, Rules-making, administration.

## Rulings on negatives (2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the rule requires:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case** (Meng, typed 2026-11-05T10:25:24Z): each such site gets one fork line below.

Most questions here answer with an enumeration rather than `MAYBE BOOLEAN`; each constructor is commented in the code as
"the text's no" or "NOTHING-kind", and the NOTHING-kind constructors are worded "does not reach it" or "this Act does not
give".

## Forks (readings taken where the text allows another)

- **F1** s 7 / ss 156, 191A, 228, 239(3): "proceedings under the Family Law Act 1975" is read as narrower than "family law
  or child support proceedings", so child support proceedings keep ss 143, 161, 191, Part 7 and s 239(2), while ss 136,
  176, 211-215 exclude them. Other reading: treat both phrases alike. Function `a proceeding under the Family Law Act 1975`.
- **F2** s 133: where a dispute fails the s 133(1) conditions, NOTHING (s 133(2) lets the Minister confer more by
  instrument, none deposited). Other reading: JUST FALSE.
- **F3** s 211(3): where good cause is shown, the "must" falls away; whether the Court may still award interest is not
  said: NOTHING-kind. Other reading: no interest.
- **F4** s 211: the amount is the most the Act allows at the Court's rate -- simple interest (s 211(4)(a) bars interest on
  interest) on the whole of the eligible money for the whole period, 365 days a year. The Court may give less or a lump
  sum. The 365-day year is this encoding's, not the Act's. Other reading: actual/actual day count.
- **F5** s 212: simple interest at 365 days a year; the Act says neither simple nor compound and leaves the rate to the
  Rules.
- **F6** s 256: the Rules' period is counted from the delegate's decision, in plain days, and not rolled past a weekend
  or holiday (the Rules, not deposited, govern counting). Other reading: count from notice of the decision; apply Acts
  Interpretation Act s 36.
- **F7** ss 230-231: where no s 231 ground is found, JUST FALSE ("on grounds permitted by this Part" closes the list).
  Where the information is outside s 230(1), NOTHING (a grant limited by its own wording).
- **F8** s 28(1): (b) reaches every prescribed judgment, a disqualification decision included (s 7: "judgment means a
  judgment, decree or order, whether final or interlocutory, a decision or a sentence"); (c) adds leave for disqualification decisions in child support jurisdiction and takes nothing from (b). The
  "prescribed" input is asked of the decision being appealed. Other reading: (c) is the only route for disqualification
  decisions, so a prescribed one outside child support needs no leave (the first baseline took this reading; corrected
  after verification, since nothing in (c) cuts down (b)).
- **F9** s 215: the period is from the order (or the latest variation) to the last day it allows; giving security on that
  last day is in time.
- **F10** s 136: where the public is excluded and the Judge also sits in Chambers, the exclusion order is reported.
- **F11** s 172(2): review of an award on a question that is not a question of law: NOTHING (the text gives review "on a
  question of law" and is silent on others).
- **F12** s 135: where another Act requires only the General Division, the General Division (s 135(4)(a) covers
  jurisdiction "not required ... to be exercised in the Fair Work Division").

## Scope

**In** (all in `fcfca-claims.l4`): s 7 (the definitions named in the module header); ss 26(1)(c), (h), (2)(b), 28(1),
50, 55(1)-(3), (6); ss 131(3), 132 (as the family law test), 133(1), 135, 136(1), (2), (2A), (3), (4), (7), 137(1), 143,
149(4), 153(6), 155, 156, 161, 168, 169, 170(1), (3), 172, 173(4), 176, 185, 190(1), 191, 191A, 192(3)-(4), 211, 212,
213, 214, 215, 228-234, 236, 237, 239, 241-244, 256(1)-(2).

**Regulative rules** (2), each run by EVALTRACE inside an exported question that takes only plain facts: s 215 (give
security within the time directed, LEST the proceeding may be dismissed or stayed) and s 256 (apply for review within the
Rules' time).

**Out, and why:**

- Chapter 2 and Chapter 4 Part 1 (the courts, judges, appointment, remuneration, pensions): machinery.
- Chapter 3 apart from ss 26, 28, 50 and 55: Division 1 hears family law at first instance only on transfer and otherwise
  sits on appeal; its practice provisions (ss 56-76) mirror Division 2's and serve family law appeals. s 46 (summary
  judgment in Division 1) is the twin of s 143 and was not repeated.
- ss 29-45, 47-49, 51-54 (Division 1 exercise of jurisdiction, transfers by the Chief Justice): powers of the court and
  its head, not a claimant's choice; s 51(4)/52(4) (no appeal from a transfer) are of the same kind as ss 149(4), 153(6),
  which are in.
- ss 134, 138-142 (associated matters, finality, completeness, orders, declarations, contempt): powers the claimant does
  not apply for in a way the Act conditions.
- ss 144-148, 149(1)-(3), (5), 150-152, 153(1)-(5), 154 (transfers between the Divisions and to the Federal Court, and
  their Rules): a court's discretion, on a party's application or its own initiative, guided by the Rules and the
  interests of justice; nothing a claimant can compute. Only the bars on appeal (ss 149(4), 153(6)) are in.
- s 173(1)-(3) (an order in the terms of an arbitration award, on a party's application, and its enforcement): the Court
  "may" make it and the registration it needs is under the Rules (not deposited); only the s 173(4) bar on a writ of
  attachment is in. A question "can my award be made an order" would be a good next one.
- ss 157-160, 162-167, 171 (the Court's and lawyers' duty to consider dispute resolution; regulations and Rules; consent
  orders; an arbitrator's referral of a question of law): duties of officials and lawyers, or procedure left to the Rules.
- ss 174-175, 177-184, 186-189, 193-210 (practice, representation, documents, venue, evidence, video links, witness
  offences, orders and reserved judgments): practice and procedure largely left to the Rules or the Court; s 175
  (representation) would be a useful next question.
- ss 235 (exception for court officials disclosing in a public official capacity: no seat for officials) and 238
  (Part 8 leaves the Court's other powers over vexatious proceedings untouched: a saving clause with no question).
- ss 216-227, 240, 245-285 (Rules, administration, officers, certificates of vexatious orders, the Sheriff and Marshal,
  family consultants, review of the Act, regulations), except s 256.
- Family Law Act 1975 Parts XI, XIA, XIB and s 117B; Fair Work Act 2009 s 570; AHRC Act s 46PSA; Public Interest
  Disclosure Act 2013 s 18; Federal Court of Australia Act 1976 appeals: other Acts, named in the answers and not encoded.

## What the Act turns out to say

1. **Two different family law carve-outs.** ss 136, 176, 211, 212, 213, 214 and 215 exclude "family law or child support
   proceedings"; ss 143(5), 156, 191A, 228 and 239(3) exclude only "proceedings under the Family Law Act 1975" (or
   jurisdiction under it). So in a child support proceeding summary judgment, conciliation, the overarching-purpose duty,
   suppression orders and vexatious proceedings orders under this Act all apply, while the interest, costs and security
   provisions do not. Asserted.
2. **Mediation is protected, conciliation is not (in this Act).** s 169(4) makes what is said at a court-referred
   mediation inadmissible; s 161 (conciliation, which also can be ordered without consent) has no such provision. Any
   protection for conciliation must come from the Rules or the Evidence Act 1995. Only the mediation half is asserted
   (s 169(4) answers NOTHING outside a s 169 referral); the absence for conciliation is a reading of s 161, which has no
   evidence question to test.
3. **Arbitration is the only process that needs consent** (s 170(3)); conciliation and mediation can be ordered without
   it (ss 161(3), 169(3)). Asserted.
4. **s 211 guarantees no minimum.** The Court must order interest (or a lump sum) unless good cause is shown, but it
   chooses the rate, the part of the money and the part of the period. The encoding gives the most the Act allows at a
   given rate; a claimant cannot compute what the Court will in fact give. Fork F4.
5. **s 212(3)(b) allows only a lower rate.** A rate the Court "determines" that is higher than the Rules' is not one the
   section authorises; the encoding keeps the Rules rate. Asserted.
6. **s 28(1)(c) is narrow.** It adds leave for an appeal from a refusal to disqualify only in child support
   jurisdiction; outside it, such a decision needs leave only if it is itself a prescribed judgment under (b). Asserted;
   fork F8.
7. **s 26(2)(a) cannot bite on a Division 2 judgment**: its three heads are all applications "in the Federal Circuit and
   Family Court of Australia (Division 1)". Only s 26(2)(b) limits appeals from Division 2. Asserted.
8. **The Act gives no appeal from Division 2 in general federal law or Fair Work claims.** s 26(1)(c) covers only the
   s 132 (family law and child support) jurisdiction; appeals in other claims lie under the Federal Court of Australia
   Act 1976, which this encoding does not answer (NOTHING-kind answer). Asserted.
9. **s 214(1)(b) lists "(ia)" before "(i)"**, an inserted paragraph kept out of alphabetical order; harmless, recorded
   for the reader comparing citations.
10. **s 172(5) protects only "the person who made the application"** for taxation under s 172(4); a party who did not
   apply has no cap from this section. Asserted.
11. **s 236's penalty is in penalty units** (60), whose dollar value is set and indexed under Crimes Act 1914 s 4AA (not
   brought in).

## Before relying on it

- Deposit the Federal Circuit and Family Court of Australia (Division 2) (General Federal Law) Rules 2021 and the
  regulations under the Act, and replace the three inputs they set (judgment interest rate, the review period, prescribed
  judgments).
- A lawyer's check of forks F1, F4, F6 and F8.
- An independent test pass and the two human gates.
- Questions on s 175 (who may represent me) and on the Division 1 twins (ss 46, 67-68) if family law appeals become a
  focus.
