# Jurisdiction of Courts (Cross-vesting) Act 1987 (Tas) — baseline encoding, the party's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18, the rulings on negatives of 2026-11-04 and 2026-11-05 (copied below), and the `writing-l4-rules` skill (with `references/regulative.md`).
There is no REFUSE in it; where the text does not answer, a question gives an answer tagged `NOTHING-kind` in its own words, and the tests assert it; where the text says no in its own words, the answer is tagged "the text's no".
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the Acts behind personal injury, compensation and other claims work. Its focus is **cross-vesting**: where a civil claim is heard, when it must or may be moved between the Supreme Court of Tasmania, the courts of other States and Territories and the federal courts, and what follows a move. The Act is short (17 sections), so **the whole operative Act** is encoded; only machinery is left out (listed below). There was no earlier encoding of this Act to keep, and no ledger entry was open for it (Tasmania has no requirement ledger).

Three modules:

- `tasjcxv-dates.l4` — a calendar date and a count of days (built-in date functions only; no `daydate` import).
- `tasjcxv-claims.l4` — the rules and the 21 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order: proceedings the Act deals with (ss 3, 3A); vesting (ss 4, 9); transfer (ss 5, 6A); special federal matters (s 6, with ss 6(8) and 7(7) together); appeals (s 7); removal into the Supreme Court (s 8); Trade Practices Act matters (s 10); conduct and costs (ss 11, 12); appeals from transfer decisions and enforcement (ss 13, 14).
- `tasjcxv-cases.l4` — 140 assertions and 2 traces.

**Regulative rule.** The Act fixes no period of its own. The one duty with a deadline that a party meets is the notice a party may be directed to give: `s 6(5)(b) -- give the notice within the time the court directed`: `PARTY the directed party MUST give written notice of the special federal matter to both Attorneys-General WITHIN the days allowed HENCE FULFILLED LEST BREACH BY the directed party BECAUSE ...`, with day 0 the day of the direction. It runs inside the exported question `s 6(5)(b) -- have I given the notice in time` through `CONSIDER EVALTRACE ... WHEN FULFILLED`; the question takes only dates, a number and yes/no. One fulfilment and one breach are `#TRACE`d with `-- expect:` lines.

## Edition

Jurisdiction of Courts (Cross-vesting) Act 1987 (Tas), No. 78 of 1987, consolidated version published 2025-09-22 and current on Tasmanian Legislation Online on 6 November 2026, retrieved 2026-11-06T12:09:43Z, as deposited at `../../registers/source-bundle/act-1987-078.txt`. Last amendments shown: No. 41 of 2001 (s 3A), No. 11 of 2001 (ss 4, 5, 6, 6A, 10, 11, 14), No. 66 of 2007 (s 5(8)). **Regulations:** none; no number in the Act is set by an instrument.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `tasjcxv-dates.l4`, `tasjcxv-claims.l4` | `tasjcxv-cases.l4` | 140 written, 140 satisfied; 2 traces as their `-- expect:` lines say (one FULFILLED, one BREACH) |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read; a deliberately wrong assertion in a scratch file showed as `assertion failed`. Every expected value was written by hand from the text. Edges asserted: each exclusion of ss 3(1), 3A on every question that carries it; each limb of each "where" (ss 5(6), 5(8), 6(3)-(4), 7(6), 8, 10, 14(3)); each court pair in s 5, with and without the s 6A facts, and one s 6A(1) limb missing; each appeal route in s 7, including s 7(1) taking priority with a Schedule Act matter; the last day of a 14-day direction and the day after, both given and not given; a notice given before the direction; a 7-day direction across the end of February 2027.

## Seat

**The party to a civil proceeding**: usually the person bringing a claim (the plaintiff, applicant or claimant), whose proceeding is in a Tasmanian court or tribunal, the Federal Court, the Family Court or a Supreme Court of another State or Territory. "Does this Act deal with my proceeding? Can a court outside Tasmania hear my Tasmanian claim? Must my proceeding be transferred, and where? Can I apply? Can my lawyer follow it? Can the Supreme Court keep my special federal matter? Have I given the notice the court directed in time? Where does my appeal go? Can my case be removed into the Supreme Court, or sent down to a lower court? Which law will be applied? Do the steps already taken count? Who orders the earlier costs? Can I appeal the transfer? Can I enforce the judgment?" The party answering the claim asks the same questions with the same answers, so no second seat is added. No seat is given to the courts, the Governor or the Attorneys-General: what a court finds, considers or is satisfied of is asked as a fact.

The 2026-10-18 defaults:

- **The Act alone.** The Commonwealth cross-vesting Act (its definition of "special federal matter" and its Schedule), the Family Law Act 1975 (s 41), the Corporations Act 2001 (Part 9.6A), the ADJR Act 1977 (definition of "enactment"), the Trade Practices Act 1974 (Part V) and the Constitution (s 75(v)) are named, not encoded; what they decide is asked as a fact.
- **The actors the text names:** the party (including an intervener, s 3(1)), the Supreme Court of Tasmania, the Supreme Courts and State Family Courts of other States and Territories, the Federal Court and the Family Court, the Full Courts, the High Court, the Attorneys-General, a lower Tasmanian court or tribunal.
- **Judgments handed to others are answered conditionally:** "it appears to the court that ... it is more appropriate" or "otherwise in the interests of justice" (s 5), "considers it appropriate" (s 6A), "satisfied that there are special reasons" and "a reasonable time" (s 6(3), (4)), "in the opinion of the court" (s 6(1A), (2)(b)), "through inadvertence" (ss 6(8), 7(7)), "the interests of justice require" (s 7(6)), "it appears to the Supreme Court" (s 8), "as the court considers appropriate" (s 11(1)(c)) are inputs.
- **Definitions:** "proceeding" (s 3(1)), "party" (s 3(1)), "State matter" (s 3(1)), the reading of s 3(2), "federal matter proceeding" (s 6A(1)) are worked from facts; "special federal matter", "State Family Court", "Commonwealth authority", "officer of the Commonwealth" and the Schedule Acts are asked as facts.
- **One case:** one proceeding (with the related proceeding that ss 5(6), 6A and 8 speak of as a fact about it).
- **Terms:** the Act's own words in the identifiers, with plain glosses in the `@desc` lines.
- **Machinery out** (below).

## Scope

In: the whole operative Act. s 3(1), (2); s 3A; s 4(3)-(5); s 5(1)-(4), (6)-(9); s 6(1)-(9) (s 6(5)(a), the adjournment and its costs, named in an answer; s 6(6) named in an answer; s 6(9) asked as a fact); s 6A(1)-(7); s 7(1)-(7); s 8(1)-(3); s 9 (folded into the answers of ss 4 and 5); s 10; s 11(1), (3); s 12; s 13; s 14(2), (3).

Out, and why:

- The preamble; s 1 (short title); s 2 (commencement): machinery.
- s 15 (reading down to the State's legislative power): a rule of construction for the courts, with no question a party can answer.
- s 16 (suspension or cessation by the Governor's proclamation): machinery; the encoding assumes the Act is in force in relation to the Commonwealth and every State.
- s 17 (proceedings pending before the 1992 amendments): transitional, of historic reach only.
- Omitted provisions (ss 4(1), (2), 5(1)(b)(i), (iii), 5(5), 11(2), 14(1)): no text to encode (finding 1).
- s 5(9), s 6A(5), (6): no question of their own; s 5(9) and s 6A(5) are why the s 5 answers speak only of transfers, never of new jurisdiction.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3(1) "State Family Court" (borrowed, by proclamation under s 41(2) of the Family Law Act) — the `Court` enumeration and s 4(4) — taken as the Family Court of Western Australia, the only such court; Tasmania has none — any other State court proclaimed later.
- **F2** s 3(2) — `a Supreme Court of another State, read with s 3(2)` — "the Supreme Court of another State" in ss 5(2), (3), 8(1)(b)(i) and 10(a) includes the Family Court of Western Australia — read only where the Act says "the Supreme Court of a State".
- **F3** s 5(2)-(4) limbs (i) and (ii) — `s 5 -- must my proceeding be transferred` — the related-proceeding limb (i) and the listed-matters limb (ii) both end in "it is more appropriate", so one finding stands for both — separate inputs for each limb.
- **F4** s 6A(2), (4) "considers it appropriate ... having regard to the interests of justice" — `s 5 -- must my proceeding be transferred` — either finding ("more appropriate" or "otherwise in the interests of justice") counts — only an express finding under s 6A.
- **F5** s 6(1) "pending in the Supreme Court" — `s 6 -- must my special federal matter go to a federal court` — the Supreme Court of Tasmania only (s 3(2) adds nothing, Tasmania having no State Family Court) — none.
- **F6** s 5(7) — `s 5(7) -- can I apply for a transfer` — someone who is not a party and has not intervened gets `NOTHING`-kind: the list is not closed with "only" — `JUST FALSE`.
- **F7** s 6(5)(b) "direct a party to give a notice" (no time in the Act) — `s 6(5)(b) -- notice on this day is in time` — days are counted from the day of the direction, and a notice on the last day allowed is in time — the direction's own wording, which may fix a calendar date.
- **F8** s 7(4) "the Full Court of the Federal Court or of the Family Court, as the case requires" — `s 7 -- where can my appeal go` — either federal Full Court is accepted as a s 7(4) route — only the one "the case requires", which the encoding does not decide.
- **F9** s 7(6) "unless the interests of justice require that the Court proceed" — `s 7(6) -- must the Full Court send ...` — once the "unless" is met, the answer is no transfer, and the decision is saved by s 7(7)(a) — the Court is merely not obliged either way.
- **F10** ss 6(8), 7(7) — `s 6(8), s 7(7) -- is the decision invalid ...` — outside their words (no inadvertence, no s 7(6) decision), `NOTHING`-kind: the sections say what does not invalidate, not what does — `JUST FALSE` (invalid).
- **F11** s 6(5)(b) — `s 6(5)(b) -- have I given the notice in time` — a notice given before the direction counts as given on day 0 (in time) — a notice before the direction is not "in accordance with" it.
- **F12** s 6(2) — `s 6 -- must my special federal matter go to a federal court` — a special federal matter under a paragraph s 6(2) does not name must still be transferred (s 6(1)), but where to is `NOTHING`-kind — no duty at all.
- **F13** s 6(7) — `s 6(7) -- can the Supreme Court still give me urgent interim relief` — relief that is not urgent and interlocutory: `NOTHING`-kind (a saving limited by its own wording) — `JUST FALSE`.
- **F14** s 13 — `s 13 -- can I appeal that decision` — other decisions: `NOTHING`-kind; s 13 bars only the two kinds — `JUST TRUE` (an appeal lies).
- **F15** s 14(2) — `s 14(2) -- can I enforce the judgment in Tasmania` — other judgments: `NOTHING`-kind — `JUST FALSE`.
- **Order of answers.** In s 6 the exclusions of ss 3(1), 3A come first, then s 6(9), then s 6A(3), then an order under s 6(3); in s 7, s 7(1) and (2) come before s 7(3)-(5). A case meeting two grounds is told the first.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "does not include" of s 3(1) ("proceeding") and the "does not apply" of s 3A (flat negatives); the "means" definition of State matter (s 3(1)); the "does not ... invest ... or confer" of s 4(5); the "where" conditions of ss 5(1)-(4), (6), 7(6), 8(1), 10, 11(1), (3), 12, 14(3); the "if" of ss 5(8), 6(1), 6(3), 6(7), 12; the "before ... must be satisfied" of s 6(4); the "does not apply" of ss 6(9), 6A(2), (3); the "shall not" of s 7(1), (2); the "only in" of s 7(3), (4); the "does not lie" of s 13; the "not being" of s 14(3)(a) give the text's no. Transfers between courts this Act does not deal with, a non-party's application (s 5(7)), a paragraph s 6(2) does not name, relief outside s 6(7), decisions outside ss 6(8), 7(7), appeals s 7 does not route, decisions s 13 does not name and judgments s 14(2) does not name give a `NOTHING-kind` answer (*limited by its own wording*, *silent*, *points outside the sources*).

## What the Act turns out to say

1. **The federal courts no longer receive Tasmanian jurisdiction.** s 4(1) and (2), which vested State jurisdiction in the Federal Court and the Family Court, were omitted by No. 11 of 2001, with s 5(1)(b)(i) and (iii), s 5(5), s 11(2) and s 14(1). The Act now moves State matters only between State and Territory Supreme Courts (and the Family Court of Western Australia), and moves proceedings into the Supreme Court of Tasmania from the federal courts; s 5(9) and s 6A(5) say no court gains jurisdiction it would not otherwise have. Asserted (s 4 to a federal court: `NOTHING`-kind).
2. **s 5(1) has only one limb left.** Subsections (2)-(4) let the transferring court act where it is "otherwise in the interests of justice"; s 5(1), after the 2001 omissions, keeps only the "having regard to ... it is more appropriate" limb (ii), so an interests-of-justice finding alone does not require a transfer from the Supreme Court of Tasmania to a federal court. Asserted.
3. **s 6(2) names paragraphs of a Commonwealth definition this deposit does not hold.** It sends paragraphs (a), (b), (c), (d) and (e) of the Commonwealth Act's "special federal matter" to the Federal Court and paragraph (ab) to the Family Court, the Family Court of Western Australia or the Supreme Court of the Northern Territory. Whether the Commonwealth definition now has other paragraphs was not checked (the Commonwealth Act is not deposited here); if it does, s 6(1) requires a transfer that s 6(2) does not direct (fork F12). Asserted.
4. **s 10 names Divisions of the Trade Practices Act 1974.** Division 1 and 1A of Part V of that Act (consumer protection and product safety) are, on the encoder's understanding, no longer in force under those numbers since the Act became the Competition and Consumer Act 2010 and the Australian Consumer Law took their place; the Tasmanian text has not been amended to follow. If so, s 10 reaches only proceedings about matters still arising under the old Divisions. This is not checked against a deposited Commonwealth text, and the encoding asks the s 10(b) fact as written.
5. **"Family Court" is the Family Court of Australia** (s 3(1)). That court has, on the encoder's understanding, been continued as the Federal Circuit and Family Court of Australia (Division 1) since 2021; the Tasmanian text still uses the old name. The encoding keeps the text's name; whether the reference carries over is a question for the Commonwealth law and the Acts Interpretation rules, not this text.
6. **The Act fixes no time for anything a party does.** Applications for transfer (s 5(7)) or removal (s 8(1)) have no deadline. The only deadline a party meets is set by the court when it directs a notice under s 6(5)(b), so the one regulative rule takes the days allowed as an input.
7. **Transfer decisions cannot be appealed** (s 13(a)), nor the choice of rules of evidence and procedure under s 11(1) (s 13(b)). A party's only say is the application (s 5(7)) and the hearing of it. Asserted.
8. **A court's error in keeping a case is saved, not punished.** ss 6(8) and 7(7) say a decision made through inadvertence without the s 6 order or notice, or by the Full Court in a s 7(4) appeal, is not invalid under those sections; they do not say a deliberate failure invalidates it (fork F10).
9. **s 7(5) is permissive without an actor.** An appeal from a State Family Court judge with a Schedule Act matter and another matter "may be dealt with as if" no matter arose under a Schedule Act; the text does not say who decides. The answer is the text's own words.
10. **The parties' convenience is excluded by name** as a special reason for keeping a special federal matter (s 6(3)); the `@desc` says so, and the court's satisfaction is an input.

## Before this is worth relying on

- An independent test pass and a lawyer's review of forks F2, F3, F4, F7, F10 and F12, and of findings 3, 4 and 5 against the current Commonwealth texts (the cross-vesting Act's definition of special federal matter and Schedule, the Competition and Consumer Act 2010, the Federal Circuit and Family Court of Australia Act 2021).
- Check the deposited consolidation against the authorised version.
- The Acts Interpretation Act 1931 (Tas) rules on reckoning time are not applied beyond fork F7.
- Deployment to Legalese Cloud, by a person with access.
