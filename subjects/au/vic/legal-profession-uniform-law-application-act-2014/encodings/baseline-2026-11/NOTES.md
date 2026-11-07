# Legal Profession Uniform Law Application Act 2014 (Vic) -- baseline encoding, the client charged legal costs

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of this Victorian subject; nothing existing was touched. The dates are in `lpul-dates.l4`
(built-in date functions only, no daydate), the rules and the client's questions in `lpul-client.l4` (each exported
question calls a rule defined beside it and never restates it), and the worked cases in `lpul-cases-client.l4`.

The focus asked for: the Act applies the Uniform Law, and Schedule 1 is the Legal Profession Uniform Law itself (costs
disclosure, costs agreements, costs assessment). The Act is large (Schedule 1 alone has 478 sections), so this baseline
takes Part 4.3 (legal costs) of the Uniform Law nearly whole, with the claims machinery a client meets around it: the
s 272 time limit for a costs complaint, the Commissioner's costs dispute powers (ss 291-294), and the Victorian Act's own
costs provisions (s 97 appeal from the Costs Court, s 99 costs disputes at VCAT). A person bringing an injury or
compensation claim on a "no win, no fee" agreement meets exactly these provisions.

Other encodings of the same Uniform Law exist for Western Australia (`subjects/au/wa/legal-profession-uniform-law-wa/` and
`.../legal-profession-uniform-law-application-act-2022/`), written from the lawyer's seat. They were not read for values
and nothing was taken from them; this encoding is from the client's seat and from the Victorian text.

## Edition

- **Act:** Legal Profession Uniform Law Application Act 2014, Act No. 17/2014, Version No. 018, incorporating amendments
  as at 11 October 2023, with Schedule 1 (the Legal Profession Uniform Law), deposited at
  `../../registers/source-bundle/legal-profession-uniform-law-application-act-2014.txt` (sha256 4487c989...ac2ef77f as
  committed, per its `.meta.json`), a plain-text conversion of the Word file the owner saved by hand on 6 November 2026,
  reconverted on 7 November 2026 to restore the decimal point in the s 79(1) formula ("0·7 (A + B)") and the bullets of
  the Schedule 3 notes that the first conversion dropped (no provision encoded here changed; the first text's sha256 was
  89f65e9d...1f0b5057)
  (see that file's `.meta.json` and `subjects/au/vic/README.md`). Version 018 was the current version on 2026-11-06. Not
  checked against the authorised PDF, which was not saved.
- **Numbers set elsewhere:**
  - The s 174(4), (5) thresholds are in the Law itself: Sch 4 cl 18(3), (4) give $750 and $3000 "until a Uniform Rule
    prescribing an amount ... takes effect". No such rule is in the deposited text of the General Rules (below).
  - The Legal Profession Uniform General Rules 2015 are not deposited for Victoria. They are uniform (made once for all
    participating jurisdictions), and the WA deposit (`subjects/au/wa/legal-profession-uniform-general-rules-2015/`,
    version 00-a0-02, from 1 July 2022) was read for two rules: r 75 (the interest cap: the Reserve Bank's Cash Rate
    Target on the bill's date plus 2 percentage points, used in the s 195 question with the Cash Rate Target asked) and
    r 72A (when s 178(1), (2) do not apply, asked as one fact); r 71 (Victorian State owned enterprises and NSW State
    owned corporations are commercial clients) is folded into the "specified in the Uniform Rules" choice. Whether the Victorian application of the Rules matches
    that WA version on any given day is not checked.
  - The amounts marked "(indexed)" in ss 291-293 and the Victorian Act s 99 ($100 000, $10 000, $25 000) are indexed under
    s 471 "in accordance with the Uniform Rules". No indexed figure is deposited, so the Law's own figures are used; an
    indexed figure would change the answers at the edges.
  - The Victorian commencement of Part 4.3 (1 July 2015) is from the Act's endnotes (Chapters 2-7 of the Uniform Law,
    Special Gazette No. 151, 16 June 2015).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (two
deliberately wrong assertions were run once in a scratch file in this folder, since deleted, and showed as errors).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lpul-dates.l4` | 0 | 0 | 0 | 0 |
| `lpul-client.l4` | 0 | 0 | 0 | 0 |
| `lpul-cases-client.l4` | 0 | 0 | 158 | 158 |

Every exported question has cases, with the edges: $750 and $751, $3000 and $3001; an uplift fee of exactly 25% and
25.01%; the cooling-off period across a weekend, a holiday and Melbourne Cup day, the notice on the last day and the day
after; the 30th and 31st day for an itemised bill request, the 21st and 22nd for the itemised bill; 29 and 30 days for
interest, the rate at the cap and 0.01 over, a bill exactly 6 months after completion and one day more (31 August plus
6 months); the 29th and 30th day before suit; 12 months to the day for a costs assessment and a day more, and 29 February;
a cut of exactly 15% and just under; the 60th day and the 4-month waiver window for a complaint; $99 999 / $100 000 and
$9 999 / $10 000; $25 000 and $25 001, the 60th and 61st day for VCAT; a settlement disclosure the day before, the same
day before and after execution, and the day after.

## Seat

**The client charged legal costs** (`lpul-client.l4`): the person a law practice charges for legal services -- for this
focus typically a person bringing an injury or compensation claim -- or a third party payer who must pay a client's
costs. "Does Part 4.3 protect me?", "What must my lawyer tell me about costs, and when?", "Is my no-win-no-fee agreement
valid?", "What is the most uplift fee I can be charged?", "When does my cooling-off period end?", "How much must be repaid
to me?", "Can I still ask for an itemised bill?", "May I be charged interest?", "Can my lawyer sue me yet?", "Can I have
the bill assessed, and by when?", "Who pays for the assessment?", "By when must I complain about the bill?", "Can the
Commissioner deal with it?", "Can I take it to VCAT?".

The law practice is the other party the text names; it could have its own seat layer later (`lpul-seat-practice.l4`). No
seat for the Victorian Legal Services Board, the Victorian Legal Services Commissioner, a costs assessor, the Costs Court,
the Supreme Court or VCAT: their satisfactions, beliefs, findings and determinations are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: Sch 4 cl 18 gives the thresholds; two uniform
  General Rules are used from the WA deposit as stated under Edition; indexed amounts are the Law's figures.
- **The actors the text names.** Followed: the client, the associated and non-associated third party payer, the law
  practice and a law practice retained by it, the designated local regulatory authority (the Board for Chapter 4, the
  Commissioner for Chapter 5: Vic Act s 10 Table 1), the costs assessor, the designated tribunal (the Supreme Court for
  s 198: Table 2 item 2), VCAT.
- **Judgments answered conditionally.** Followed: "takes all reasonable steps to satisfy itself" (s 174(3)), "reasonable
  belief that a successful outcome ... is reasonably likely" (s 182(2)(a)), "on reasonable request" (s 190), "just and
  fair" (ss 198(4), 272(2)), "believes that ... it is not fair and reasonable" (s 204(2)), the r 72A satisfaction, and
  "significant change" (s 174(1)(b)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: commercial or government client (s 170(2), as
  a choice of its heads), the thresholds, the conditional costs agreement requirements, the cooling-off period in clear
  business days (s 6 "business day"), the required period (s 272(3)), the s 291 limits. Asked: the Corporations Act
  entity kinds (one choice), litigious matter (s 6, as a fact), solicitor-client basis, fixed costs legislative provision,
  completion of the matter, complying bill.
- **One case.** One client (or third party payer), one law practice, one matter.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of every input.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In (Uniform Law, Schedule 1):** s 6 definitions used (business day, legal costs, litigious matter, uplift fee, costs
assessor); s 170 (commercial or government clients); s 171 (third party payers, as a choice); s 172(4) (noted only);
s 174; s 175; s 177; s 178; s 179; s 180(2), (4); s 181; s 182; s 183; s 185; s 187; s 190; s 191; s 194; s 195;
ss 196, 197, 198 (except (6), (8)-(10)); s 204; s 268(3); s 272(2), (3); s 284(2); ss 291-294; Sch 4 cl 18(1)(a), (3),
(4). **Victorian Act:** s 10 Tables 1 and 2 (which authority and tribunal); s 97 (named in the assessment question); s 99.

**Regulative rules:** four. s 177 (the law practice MUST disclose before the settlement is executed, LEST BREACH), s 181(4)
(I DO end the agreement WITHIN the cooling-off period, LEST the period runs out), s 187(2) (I DO request WITHIN 30 days),
s 187(3) (the law practice MUST give the itemised bill WITHIN 21 days, LEST BREACH). Each is run by EVALTRACE inside an
exported question that takes only dates and facts, through the helper the Victims of Crime and County Court Act
encodings use (a CONSIDER on an EVALTRACE matches FULFILLED only).

**Out, and why:**
- s 169 (objectives), s 173 (avoid increased costs), s 172(1)-(3) (fair and reasonable): standards for the costs assessor
  and the Commissioner, with no fact test the client can state; s 172(4) is evidence, not entitlement.
- s 176 (disclosure to an associated third party payer): its effect for the third party payer is in the s 178 question.
- s 180(1), (3), s 184, s 186, s 188, s 189, s 192, s 193: forms and procedure; the s 188 and s 192 content is folded into
  "a bill that complies" in the s 194 question; s 189 rests on General Rules r 73.
- ss 199-203, 205: the costs assessor's functions and the appeal (Vic Act s 97 sends it to the Supreme Court Act 1986 and
  its Rules, not deposited); s 198(6), (8)-(10): procedure and the non-associated payer's assessment.
- s 206 (security), s 207 (disciplinary consequences for the principal), s 208 (rule-making): not the client's questions.
- Civil penalties (ss 182(4), 183(1)): payable by the law practice; the client's consequence is in s 185.
- Chapter 5 outside costs disputes (complaints generally, disciplinary matters, compensation orders under Part 5.5),
  s 272(1) (named in an answer only), ss 285-290 (the Commissioner's process).
- Sch 4 cl 18(1)(b), (2): matters begun under the old legislation (answered "not covered").
- The rest of the Victorian Act and Schedule 1 (admission, practising certificates, trust money, fidelity cover,
  professional indemnity insurance, regulators): outside the costs focus.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 195(5), 198(3), 272(2)(a) "6 months", "12 months", "4 months" -- `the same day` n `months after` -- the period
  ends on the same day of the month n months later, or that month's last day where it has no such day -- the day before,
  or the first day of the next month.
- **F2** s 181(4) "not less than 5 clear business days" -- `s 181(4) -- the last day of the cooling-off period` -- the day
  the agreement is made is not counted; the period ends at the end of the n-th business day after it; a notice given on
  the day of making, or on a weekend or holiday inside the period, is within it -- the period counted from the next day
  even if not a business day, or "clear" also excluding the day of the notice.
- **F3** s 177(1) "before the settlement is executed" -- `s 177 -- the settlement disclosure` -- a disclosure on the day of
  execution counts only if made before execution -- any disclosure on the day counts.
- **F4** ss 178, 180-185 -- `ss 178, 180-185 -- the conditional costs agreement` -- the first defect in section order is
  the answer (any one makes the agreement void) -- every defect listed.
- **F5** s 185(2), (3) -- `s 185(2)-(4) -- what must be repaid` -- for an uplift fee in breach of s 182, the uplift fee
  received is the answer -- s 185(2) adding any excess on the rest of the costs.
- **F6** ss 187(2), (3), 194(2)(b), 195(2), 272(3), Vic s 99(2) "within n days after", "at least 30 days after", "30 days
  or more after", "60 days after" -- the last day (or the first permitted day) is the day plus n -- the day plus n minus 1.
- **F7** Vic s 99(1)(a) "not more than $25 000 (indexed)" -- `Vic s 99 -- the costs dispute at VCAT` -- the amount as the
  person states it, with no GST rule (s 294 governs ss 291-293 only; finding 4); $25 000 itself is within -- GST
  excluded by analogy with s 294.
- **F8** ss 170(1)(b), 198(5) -- `ss 196-198, Vic s 99(9) -- the costs assessment` -- a third party payer who would be a
  commercial or government client is outside Part 4.3, so the question answers "not covered" and s 198(5) has nothing
  to act on (finding 2) -- s 198 read as reaching them, with no late application.
- **F9** s 204(2)(c) "reduced by 15% or more on assessment" -- `s 204 -- who pays for the assessment` -- 15% of the costs
  claimed -- 15% of the costs as assessed, or of the whole bill including costs not challenged.
- **F10** s 174(7) "make the disclosure required by subsection (1) or (if applicable) subsection (5)" -- `s 174(1)(b),
  (7), (8) -- the further disclosure` -- the form is applicable while the new likely total is $3000 or less -- the form
  is never applicable once the lower threshold is passed.
- **F11** s 195(1), (3) -- `s 195 -- interest may be charged` -- s 195(3)'s statement in the bill is required for
  interest under a costs agreement too (s 195(1) is "under this section") -- (3) reaching only interest under (2).
- **F12** s 272(2) -- `s 272(2) -- the costs complaint in time` -- a duty whose condition (the Commissioner's
  satisfaction) is not yet decided: "can still be waived" -- NOTHING.
- **F13** s 178(2) -- `s 178 -- what follows` -- the person disclosed to gets "nothing under s 178 for me", worded as this
  section's answer only -- NOTHING.
- **F14** s 181(5) -- `s 181(5) -- what the law practice may recover after cooling-off` -- a notice outside the period:
  NOTHING (s 181(5) sets no limit; the agreement governs) -- JUST the agreement's full amount, which the encoding cannot
  know.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding follows the rulings; it carries no `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the s 170(1) flat negative ("This Part does not apply to") and the Sch 4 cl 18(1)(a) "if" give `JUST FALSE`
for "Does Part 4.3 protect me?"; the "must not ... until" bars of ss 178(1)(c), 194, 198(7)(b) are encoded as a bar
(`JUST TRUE` while it holds, `JUST FALSE` once none does), never as a right to sue; the periods of ss 181(4), 187(2),
(3), 195, 198(3), 272 and Vic s 99(2) are fixed in the text's words, so outside them the answer is no; s 182(2)(b)'s cap
outside a litigious matter is a scope limit and answers `NOTHING`; a question whose subject Part 4.3 does not reach
answers `NOTHING` or a "not covered" constructor.

## What the Act turns out to say

1. **The disclosure points the client to the Board, not the Commissioner.** s 174(2)(a)(iv) requires telling the client
   of the right "to seek the assistance of the designated local regulatory authority in the event of a dispute about
   legal costs". s 174 is in Chapter 4, for which the Victorian Act s 10 Table 1 item 6 designates the Victorian Legal
   Services Board; costs disputes are dealt with under Chapter 5 by the Victorian Legal Services Commissioner (item 7).
   The `@desc` names the Board, as the text does. Whether the two are in practice one office is not in the deposited
   text.
2. **s 198(5) speaks of persons s 170(1) has taken out of Part 4.3.** s 170(1)(b) says Part 4.3 "does not apply to ... a
   third party payer who would be a commercial or government client", and saves only ss 181(1), (7), (8), 182, 183,
   185(3)-(5); s 198 is not saved. Yet s 198(5) withholds the late-application route from exactly that third party payer,
   which only matters if s 198 applies to them. Encoded by s 170 (F8); a lawyer's reading is needed.
3. **s 178(1)(b) and (c) end at different points.** (c) bars suing "until they have been assessed or any costs dispute has
   been determined by the designated local regulatory authority or under jurisdictional legislation" (which reaches a
   VCAT determination under Vic s 99); (b) frees the client from paying only "until they have been assessed or any costs
   dispute has been determined by the designated local regulatory authority", without "or under jurisdictional
   legislation". After a VCAT determination the practice may sue, but on the words of (b) the client is still not
   required to pay. The answer's wording speaks of "a costs dispute ... determined" generally.
4. **The VCAT limit has no GST rule and a different comparison.** ss 291-293 compare amounts "less than" $100 000 or
   $10 000 and s 294 disregards GST; Vic s 99(1)(a) and (4)(a) use "not more than" $25 000 and say nothing of GST (F7).
   Asserted at $25 000 and $25 001.
5. **No cap on an uplift fee outside litigation.** s 182(2) (reasonable belief in success, 25% cap) applies only "If a
   conditional costs agreement relates to a litigious matter". A conditional costs agreement for non-litigious work may
   carry any uplift fee the Law does not otherwise forbid (s 182(3) still requires its basis and estimate). Asserted
   (40% outside litigation is valid on these facts).
6. **Two different "itemised bill" events start two clocks.** s 194(2)(b)(ii) counts from the day the person "receives an
   itemised bill"; s 272(3)(b) from the day "the request was complied with". The encoding asks the day given, and uses it
   for both; where giving and receipt differ (post), the two clocks differ.
7. **s 195(5) turns on "completion of the matter"**, which the Law does not define. Asked as a fact.
8. **The thresholds still come from the transitional clause.** Sch 4 cl 18(3), (4) fix $750 and $3000 "until a Uniform
   Rule prescribing an amount" takes effect; the General Rules (WA deposit, from 1 July 2022) prescribe none (r 72 carries
   a note saying so), so the transitional figures are the operative ones a decade on.

## Before this is worth relying on

- Check the conversion against the authorised PDF.
- Deposit the Legal Profession Uniform General Rules 2015 as they apply in Victoria (rr 71-76), and the s 471 indexed
  amounts; then replace the WA-deposit reading and the Law's base figures.
- A lawyer's view on findings 2, 3 and 6 and forks F2, F3, F8 and F9, an independent test pass and a human gate.
- A seat layer for the law practice, if wanted, beside this one.
