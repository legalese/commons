# Social Security (Administration) Act 1999 — baseline encoding: overpayment, information notices and offences

## Method

**Baseline, added beside an existing one.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
It is a new layer: `../baseline-2026-10/` stays untouched and nothing here edits or restates it.
That encoding answers the claim, the start day, the reporting duties of ss 66A–74, mutual obligations, the day an adverse decision takes effect (s 118) and review (ss 109, 126–131, 142–147).
This one covers the provisions a person meets when the Department says they were overpaid: decisions made by computer, notice of a decision, the Secretary's information notices and the offence of not complying, the offences of Part 6 and the repayment order, and the ART provisions that bear on a contested debt.
It was written as part of a run of baseline encodings of Australian claims law; its focus is the income-averaging debt episode of 2016–2019 and the class action and review applications that followed, described here by subject only.

There is no REFUSE in it. Questions the text leaves open answer `NOTHING`, and a test asserts each.
Two duties with deadlines are regulative rules (`DEONTIC`, `PARTY … MUST … WITHIN … LEST BREACH … BECAUSE`) run inside the questions by `EVALTRACE`: compliance with a s 196 notice (s 197(1)) and telling the Department a new address (s 193(b)). No exported question takes a `DEONTIC` or an `EVENT`.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

Eighteen questions are exported, each with `@export` and a `@desc` on every input, grouped under `§§` headings; groups that arise only in a situation (a notice received, a prosecution, an ART case) say so in a comment.

## Read with

- `../baseline-2026-10/` (this Act): the claim, reporting, compliance, date of effect, review. Section 109 there answers how far back a win on review reaches, which turns on the day of notice that `On what day was notice of the decision given to me` (s 237) answers here.
- `../../../social-security-act-1991/`: qualification and rates. **Whether a debt exists, its amount, its recovery, write-off and waiver are in the 1991 Act's Chapter 5 (Part 5.2 onward), not this Act, and no Commons encoding covers them yet.** That is the heart of the debt question and the first thing that would need doing (below).

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here and in the module header, not in code.

## Edition

Compilation No. 163, compilation date 5 December 2025, includes amendments up to Act No. 73, 2025 (register id **C2026C00010**, in 2 volumes), as deposited at `../../registers/source-bundle/C2004A00580.txt`. No instrument is needed for the provisions encoded: the s 195(3A) income stream instrument only adds to a list item that is asked as one choice.

Borrowed, not deposited here, and not computed: the Acts Interpretation Act 1901 s 36(1) (a period "after" a day excludes that day; used for "14 days after" and "13 weeks after") and s 36(2) (a last day on a weekend or holiday rolls forward; not applied); ss 28A and 29 (service of notices other than decisions); the Criminal Code's fault elements (s 5.4 recklessness, asked as a fact) and its Divisions 137 and 145; the Crimes Act 1914 s 4B (a fine instead of imprisonment); the Administrative Review Tribunal Act 2024 s 31.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ssaa-overpayment-dates.l4` | (used by both) | — |
| `ssaa-overpayment.l4` | `ssaa-cases-overpayment.l4` | 99 written, 99 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text, with the edges: the last day of a s 196 period and the day after (16 and 17 March 2027 for a notice of 2 March), the 14th day after an address change and the 15th, the 91st day after s 195 information is given and the 92nd, a period one day short of 14 days with and without the Secretary's satisfaction.

## Seat

**The person paid**: the person who claims, receives or has received a social security payment and is told that they were overpaid, is asked to explain their income, or is accused of an offence. The questions are the ones that person asks:

- "A computer made this decision. Does it count, and whose decision is it?"
- "On what day was I given notice of it?"
- "Can they make me hand over this information? Does the letter even meet the rules? By when must I answer?"
- "What happens if I don't, or I'm late? Can what I give be used against me?"
- "What may my employer or bank be made to tell them about me, and must it be destroyed?"
- "Do these facts make out an offence, and what is the most a court can do to me?"
- "What happens to my ART case if the debt is settled, or the decision is changed?"

Every operative provision addresses the Secretary, the ART or a court. Each is encoded as what it means for the person.

The 2026-10-18 defaults:

- **The Act alone.** Nothing from the 1991 Act is restated; borrowed Acts are named above and asked as facts.
- **The actors the text names:** the person, the Secretary (Services Australia), the ART, the court.
- **Judgments left to others, answered conditionally**, all asked as facts: whether the Secretary considers information relevant (ss 192, 194) or reasonably believes the person can give it (s 191A); whether the Secretary was satisfied a shorter period was reasonable (s 196(3), (6)); whether an excuse is reasonable (s 197(3), left to the court and answered as "no offence if …"); recklessness and knowledge (ss 212–216); whether the Secretary or the ART is satisfied under s 183.
- **The Act's own definitions worked out from facts:** a decision in writing (s 236(2)), the deemed determination and its day (s 83), the day notice is given (s 237), the s 196 notice, the closed list of s 195(2), the elements of each contravention in ss 212–216. **Borrowed terms asked as facts:** reckless, a law of the Commonwealth, a reasonable excuse.
- **One case:** one person, one notice or decision.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** delegation, authorised review officers, confidentiality, annual reports, regulations.

## Scope

**In:**
- ss 6A, 236: a decision made by a computer program, and the writing rule.
- s 83: a change made by computer is taken to be the Secretary's determination, made on the day of the change.
- s 237: the day notice of a decision is taken to be given.
- Part 5 Division 1: ss 191A, 192 (every paragraph, (a)–(k)), 193, 194, 195(2), (4)–(6), 196, 197, 197A, 197B, 198(2).
- s 166(3): when the Secretary uses s 192 at the ART's request under s 166(1), s 191A does not apply, so `Can I be required to give it` needs no reasonable belief for a s 192 matter (asked as a fact: was the Secretary acting on an ART request).
- Part 6: ss 211–219 (the contraventions, the penalty, the repayment order, the single-penalty cap), 223 and 224 (in the comment; their effect is that the repayment order is proved by certificate and enforced as a judgment), 233.
- ART: ss 176, 181, 182, 183.

**Out, and why:**
- **Debts themselves** (whether one arises, its amount, recovery, garnishee, write-off, waiver): the 1991 Act's, not this Act's. s 42W (a compliance penalty is not a debt) is already beside the baseline-2026-10 compliance rules.
- ss 191 and 198(1): the Division's reach and its relationship with State law; nothing for the person to answer.
- s 195(1), (3), (3A), (3B): the purposes and the Minister's instrument behind a class notice to a third party; the person meets only what may be asked about them (s 195(2)) and the destruction rule.
- ss 199–200: the person's right to ask a former employer for an end-of-employment statement is a bare permission with no deadline; the employer's duty belongs to an employer seat.
- Part 5 Division 3 (ss 201–210, confidentiality): duties and offences of officers and third parties.
- Part 6 Division 4 (ss 220–222, joinder and trial) and Division 5 except s 233 (ss 225–232, an employer's or principal's liability for an agent): court procedure, and liability of a business rather than the person.
- ss 165A, 166(1)–(2), 168, 177: the ART's own powers and duties. s 166(3) is in (above), because it changes what the person can be required to give.
- ss 147A, 147B, 147C and 148: they switch off or modify provisions of the Administrative Review Tribunal Act 2024 for an ART review (s 147A: no stay under ART Act s 32(2); s 147B: no remittal under s 85; s 147C: no legal or financial assistance under s 294(1), (3) or (4) except in a guidance and appeals panel proceeding; s 148: the Secretary's documents may be called for early). They give the person no fact to answer and the ART Act is not deposited here, so no question is asked; what they mean for a person contesting a debt is finding 11 below. baseline-2026-10 covers s 147 items 1 and 8 only.
- s 238 (deductions for tax and child support), and the machinery of Part 7.
- s 5 (manner of notices): referred to in the s 237 comment only.

## Fork register

The rulings of 2026-11-04 and 2026-11-05 that this encoding's `NOTHING` and `JUST FALSE` answers rest on, copied word for word from docs/ENCODING-GUIDE.md section 5 as that section asks:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Eight sites in this encoding are decided under the last of these rulings, or are readings the rulings do not settle; each has a fork line below (F1–F8).

| # | Provision | Function | Answer taken | Other reading |
|---|---|---|---|---|
| F1 | s 196(1) "must be made by written notice" | `Do I commit an offence by not complying` | A requirement not made by a notice that meets s 196 is no requirement, so s 197 does not apply | Only a total absence of written notice voids it; a missing particular (say the s 196 statement) leaves the requirement standing |
| F2 | s 215(1) "must not obtain … knowing" | `Is it a contravention of Part 6 Division 2` | Without the knowledge: `NOTHING` (a prohibition limited in its own words) | `JUST FALSE`, as the other subsections, which are worded "contravenes … if" |
| F3 | s 193 "a person who owes a debt" | `Can I be required to give it` | A person who owes no debt, asked under s 193: `NOTHING` (scope without "only"; s 192 may still reach them) | `JUST FALSE` |
| F4 | ss 197A(2), 197B, silent on civil proceedings | `Can what I give be used against me` | `NOTHING` | `JUST TRUE` (nothing excludes it) |
| F5 | s 193(b) address duty | `Did I tell the Department my new address in time`, and the rule's breach text | Late notice of an address is a failure to comply with a requirement "to give information" under the Division (s 197(1)) | s 197(1) reaches only information and documents of the s 193(a) kind |
| F6 | s 237(1)(c) and (2)–(3) | `On what day was notice of the decision given to me` | Notice posted to the last known address is given on the day it would arrive in the ordinary course of post, unless the contrary is proved (s 237(3) read into (1)(c)) | (1)(c) deems notice given with no day, and (3) governs only notices posted under (2) |
| F7 | s 191A "can only … if", with s 166(3) | `Can I be required to give it` | No reasonable belief: `JUST FALSE` (an "only if"), except for a s 192 matter when the Secretary acts on an ART request under s 166(1), where s 191A "does not apply" and the answer turns on s 192 alone | s 166(3) reaches only the request itself, so a requirement the Secretary would have made anyway stays subject to s 191A (the question asks whether the Secretary was acting on the request, and takes the answer as given) |
| F8 | s 83(1) "If: (a) … (b) … (c) …" | `On what day is the computer's change taken to be a determination` | The "if" fails: the ruling's no, written `NOTHING` because the question asks for a day and there is none to give; here `NOTHING` means "s 83 deems no determination" | Split the question in two: a `BOOLEAN` that answers `JUST FALSE`, and a day asked only when it is true |

## What the Act turns out to say

1. **A decision made by a computer program counts, in writing, as the Secretary's.** s 6A(2) deems it "a decision made by the Secretary", and s 236(2) deems a decision "made, or recorded, by means of a computer" to be in writing. A change a computer makes to a rate, or a cancellation or suspension, is taken to be the Secretary's determination made on the day of the change, if made for a reason the Secretary could act on (s 83). A decision of an officer that is only spoken fails s 236(1). Asserted.
2. **Open question: does a computer decision go straight to the ART?** s 142(1)(b) lets the ART review "a decision … made personally by the Secretary", and s 129(4)(a) bars internal review of a decision "made by the Secretary himself or herself". s 6A(2) deems a computer decision to be the Secretary's, but not "personally" or "himself or herself". The words suggest internal review stays open; nothing here decides it. Not asserted.
3. **Notice posted to the last known address is given when the post would deliver it, unless the person proves otherwise** (s 237(1)(c), (3)). A notice in an online account is outside s 237 (s 5 lets the Secretary approve the manner, but says nothing of the day). The day matters: review within 13 weeks of it reaches back to the start (s 109, in baseline-2026-10). Asserted (posted 5 March 2027, ordinary course 9 March; proved 15 March).
4. **The Department can only require what it reasonably believes the person can give** (s 191A), and never so as to break a Commonwealth law (s 198(2)). A person asked for payslips from an employer that has closed may fall outside s 191A. **But not when the ART asks:** where the Secretary uses s 192 at the ART's request in an ART review, "Section 191A does not apply" (s 166(3)), so a person contesting a debt at the ART can be required to give what the Secretary has no reason to think they have, and s 197(1) then reaches a failure to comply, subject to s 197(2) (only so far as the person is capable). s 192 reaches beyond qualification and rate: income management (Part 3 Divisions 3AA and 3A), Parts 3AA and 3B, fares allowance, foreign social security agreements and assurances of support. Asserted.
5. **A notice must give at least 14 days, unless the Secretary is satisfied a shorter time is reasonable** (s 196(3), (6)). It must say what is wanted, how, by when, to which officer if any, and that it is given under s 196. A notice to appear must give a time and place and say the person may bring a lawyer. Asserted (notice of 2 March 2027: 16 March is the earliest last day; 15 March fails without the Secretary's satisfaction).
6. **Not complying is an offence with up to 12 months' imprisonment** (s 197(1)), twice the 6 months for not complying with a reporting notice (s 74, in baseline-2026-10). It applies only so far as the person can comply, and not with a reasonable excuse. Fear of self-incrimination is no excuse (s 197A(1)), but what is given cannot be used in other criminal proceedings (s 197A(2)); it can in an inquiry or investigation (s 197B). The Act is silent on civil proceedings, including recovering a debt (F4). Asserted.
7. **What an employer or bank may be made to say about a person is a closed list** (s 195(2), "but no other information"). It includes "any payments received by the person from the person given the notice, within the period of 52 weeks", so an employer can be made to give the pay it paid, but not hours worked; and, for employment, only start and end dates. Information given must be sorted within 13 weeks and the irrelevant part destroyed; if not sorted in time, all of it must be destroyed (s 195(4)–(6)). Asserted (given 1 March 2027: decision by 31 May; destruction due from 1 June if undecided).
8. **The offences need recklessness at least.** A false statement in a claim, to an officer, or that might deceive or affect a rate, is a contravention only if the person was reckless as to its falsity (ss 212–214, 216(3)); obtaining a payment not payable needs knowledge (s 215). An honest mistake makes none of them. Asserted.
9. **The most a court can do is 12 months for each offence, and a repayment order that cannot lead to gaol** (ss 217–219). A single penalty for several offences cannot exceed the sum of the maximums. The repayment order equals the amount paid because of the offence, is proved by the Secretary's certificate (s 223) and is enforced as a civil judgment (s 224); "a person is not to be imprisoned for failing to pay" it (s 218(2)). A person convicted only through an agent's conduct cannot be imprisoned (s 233). Asserted.
10. **Settling an ART debt case ends the application, not the debt question.** If the Secretary and the person agree in writing and the Secretary gives the ART a copy, the application is taken to be dismissed (s 181). What is owed is then what the agreement says. A decision varied after the person applies becomes the decision reviewed, unless the case had already gone to the guidance and appeals panel (s 182). Asserted.
11. **At the ART the decision keeps running, it cannot be sent back, and legal aid from the ART is all but closed** (ss 147A–147C). The ART "may stay operation or implementation" provision of its own Act (s 32(2)) "does not apply", so recovery of an overpayment can go on while the review is heard; the ART cannot remit the decision for reconsideration (s 147B); and the ART Act's legal or financial assistance is not available to a person who applies or proposes to apply, unless the case is a guidance and appeals panel proceeding (s 147C). The ART may call for the Secretary's statement and documents early, and the Secretary must take reasonable steps to comply (s 148). Not asserted: no question is asked.

## What would need doing before this is worth relying on

- **The 1991 Act's debt provisions** (Chapter 5: when an amount is a debt, how it is worked out, recovery, write-off, waiver, including the waiver for administrative error and the small-debt and special-circumstances waivers). Without them no question here says whether a person owes anything. Not raised in `subjects/au/requirements.jsonl` by this commit (many encodings were being committed in parallel); it should be raised as an encoder entry.
- **The Acts Interpretation Act 1901 s 36(2) roll-over**, so that a last day falling on a weekend or public holiday moves forward.
- **Finding 2** (computer decisions and review) for a lawyer.
- **Wider sources.** No Social Security Guide, ruling or case was read; the Federal Court's orders and settlement on income-averaged debts, and the Royal Commission's report, would bear on how ss 192 and 196 notices were used, but this encoding is of the text alone.
