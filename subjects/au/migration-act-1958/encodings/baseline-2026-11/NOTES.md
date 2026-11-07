# Migration Act 1958 — baseline encoding, the asylum seeker's seat (protection visas)

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; a question that reaches a gap answers `NOTHING` or a `not covered` value, and the cases assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

This is a new layer beside the two existing encodings of the Act, which stay untouched: `baseline-2026-10` (partner and skilled visas, from the visa holder's seat) and `naive-2026-10`. Both leave protection visas out. This encoding was written as part of a run over the Acts behind compensation, social justice and other claims, with the focus "asylum seeker matters". No ledger entry asked for it.

Three files:

| File | What it holds |
|---|---|
| `mig-prot-dates.l4` | the date arithmetic (built-in date functions only, no daydate): plain days, comparisons, working days with a list of public holidays |
| `mig-protection.l4` | every rule, and the 29 exported questions, under `§§` headings in the order an asylum claim meets them |
| `mig-cases-protection.l4` | the worked cases |

Every exported question is named as the asylum seeker would ask it, with `@export` and a `@desc` on every input. Inputs are plain facts or records of plain facts.

**Regulative rules.** Each is run inside a question that takes plain dates; no question takes a DEONTIC or an EVENT.

| Rule | Party | Modal | Seat question that runs it |
|---|---|---|---|
| `s 347(3) -- I must apply to the ART in time` | me | MUST apply WITHIN 28 days (14 if detained when notified); LEST BREACH, "the ART cannot extend it (s 347(5)) and has no jurisdiction" | `Am I in time to apply to the ART question` |
| `reg 4.31B(2) -- I must pay the ART fee in time` | me | MUST pay WITHIN the 7-day period beginning on the day of notification of the ART's decision (day 0 to day 6); LEST BREACH | `Have I paid the ART fee in time question` |

The case file asserts, through a helper `ends fulfilled` (a `CONSIDER … WHEN FULFILLED`), that a trace ends FULFILLED or does not; each breach is also `#TRACE`d with an `-- expect:` line, because on the stable `l4` a breached trace cannot be compared with `EQUALS`.

**Dates.** "Within 28 days after the day" a person is notified (s 347(3)) excludes that day (Acts Interpretation Act 1901 s 36(1), borrowed, not deposited): notified 17 November 2026 gives 15 December 2026. "The 7-day period beginning on the day" (reg 4.31B(2)) includes it: notified 3 March 2027 gives 9 March 2027. "Working days" (ss 48B, 91F, 91L, 494C(4)(a), 379C(4)(a)) are not defined in the Act; they are read as days that are not a Saturday, a Sunday or a public holiday in the place, and the public holidays are an input (a list of dates), because no holiday calendar is deposited. A last day on a weekend or holiday is **not** moved (Acts Interpretation Act s 36(2)); the descriptions of the deadline questions say so (fork F7).

## Edition

- **Act:** Migration Act 1958, No. 62, 1958, **Compilation No. 171, compilation date 4 June 2026** ("Includes amendments: Act No. 75, 2025"; register id C2026C00232), retrieved from the Federal Register of Legislation on 22 September 2026, as deposited at `../../registers/source-bundle/C1958A00062.txt`. Sections used are at lines 637 (s 5AAA), 648 (s 5AA), 886-958 (ss 5H-5M), 1222-1307 (ss 35A-36A), 1595 (s 46A), 1755-1800 (ss 48A, 48B), 2491-2663 (ss 91A-91WB), 4860-4910 (ss 197C, 197D), 9914-10070 (ss 336M-349), 10293 (s 368), 10447-10500 (ss 379A-379C), 11613-11680 (ss 494B, 494C).
- **Regulations:** Migration Regulations 1994 (F1996B03551), Compilation No. 289, compilation date 2 October 2026 (register id F2026C01017), retrieved 20 October 2026, as deposited at `../../../migration-regulations-1994/registers/source-bundle/F1996B03551.txt`: reg 2.16(3) (line 2975: a refusal is notified by a s 494B method) and reg 4.31B (line 7050: the ART fee for a reviewable protection decision, $2,151, and when it is paid). Both set a number or a date the Act uses.
- **Not deposited or not read, so inputs:** the regulations prescribing safe third countries and prescribed connections (s 91D), the classes excluded from Subdivision AI (s 91C(1)(c)), the excluded maritime arrival classes (s 5AA(3)(c)), the temporary visas prescribed for s 46A(1)(b)(ii) and the visas and requirements prescribed for s 46A(1A); "member of the same family unit" (reg 1.12, not read); the international instruments prescribed for s 5H(2)(a); the current indexed ART fee (regs 4.31BA, 4.31BB).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `mig-prot-dates.l4` | (exercised through the cases) | 0 errors, 0 warnings |
| `mig-protection.l4` | `mig-cases-protection.l4` | 233 written, 233 satisfied; 2 traces, each a BREACH as its `-- expect:` line says |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. A copy of the case file with one expected value changed (2151 to 2152) gave 232 satisfied and 1 failed, so the runner does report a wrong value. Every expected value was written by hand from the text before the run. Every exported question has cases, with the edges: day 28 and day 29 (day 14 and 15 if detained), applying on the day of notification, a period across a year end and a month end, the fee period's first and last day and the day after, the seventh working day across Christmas and New Year holidays, a notice given on a Saturday, post within Australia with and without a holiday.

## Seat

**The asylum seeker**: a non-citizen in Australia who claims that Australia owes them protection — who applies for a protection visa, whose application is decided, refused or whose visa is cancelled, who may apply to the Administrative Review Tribunal, and who may face removal. The questions are the ones that person asks: "Am I a refugee?", "Do I meet the complementary protection criterion?", "Can I make a valid application?", "Can I apply again after a refusal?", "Must my visa be refused over my documents?", "When was I notified?", "By when must I apply to the ART, and what do I pay?", "Can I be sent back to the country I fear?".

The Minister, officers, ASIO, the ART and the Parliament get no seat. Their satisfactions, beliefs, considerations, assessments, certificates and determinations are asked as facts, worded as such ("the Minister is satisfied …", "the Minister has serious reasons for considering …", "ASIO has assessed me …").

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates:** followed. Reg 2.16(3) and reg 4.31B are brought in; nothing else (see Edition).
- **The actors the text names:** the Minister, the officer, ASIO, the ART, the applicant, the family visa holder.
- **Judgments handed to others are answered conditionally:** every "Minister is satisfied", "serious reasons", "substantial grounds", "considers, on reasonable grounds", "reason to believe", "reasonable explanation" and "public interest" determination is an input. The person's own well-founded fear and the "real chance" of persecution are asked as facts too: the questions answer "if the decision-maker accepts these facts".
- **The Act's own definitions are worked out from facts:** refugee (s 5H), well-founded fear (s 5J), particular social group (s 5L), effective protection measures (s 5LA), particularly serious crime (s 5M, as a choice), significant harm (s 36(2A)), unauthorised maritime arrival and excluded maritime arrival (s 5AA), reviewable protection decision (s 338A), when a s 197D decision is complete (s 197D(6)). Borrowed or regulation-defined terms are asked as facts with a gloss: member of the same family unit, immigration cleared, transitory person, protection finding (s 197C(4)-(7), which itself rests on the Minister's record).
- **One case:** one person, one application, one decision, one country at a time (s 36(3) and s 197C are asked about one country).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (see Scope).

## Negatives (the 2026-11-04 and 2026-11-05 rulings)

The rulings, word for word as section 5 of `docs/ENCODING-GUIDE.md` records them: a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit. Periods ruling: (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`.

Applied here. Questions that return a plain BOOLEAN encode "if" conditions and flat negatives only, where FALSE is the text's own no: ss 5AAA, 5J(3), 5L, 36(2A), 36(2)(aa), 36(3), 36A, 5AA, 46A, 91K, 91V, 91W/91WA, 197C(3), 197D(6), and the fee period. `MAYBE BOOLEAN` where the text can be silent: s 5J(5) (`NOTHING` for harm outside the listed instances: "without limiting"), s 5LA (`NOTHING` where the s 5LA(2) deeming of ability fails), s 5J and s 5H (`NOTHING` when a component is open, or for a family social group, or outside Australia), s 48A, ss 338A/347A, ss 494C/379C (`NOTHING` for an ART online account: s 379A has no such method).

Fork lines (case-by-case sites, for the reviewer to overrule):

| # | Provision | Function | Answer taken | Other reading |
|---|---|---|---|---|
| F1 | s 5L "is to be treated as a member ... if", when it fails | `s 5L -- member of a particular social group` | `FALSE` (an "if" condition) | `NOTHING` (the deeming does not say the person is not a member) |
| F2 | s 5LA(2) "is taken to be able ... if", when it fails | `s 5LA -- effective protection measures are available` | `NOTHING` | `JUST FALSE` (read (2) as the whole test of "able") |
| F3 | s 48A with no refusal and no cancellation | `s 48A -- no further protection visa application` | `JUST FALSE` (the bar does not reach me) | `NOTHING` (a bar whose "if" is unmet) |
| F4 | s 48A after leaving the migration zone other than as (1A), (1AB) deem | the same | `NOTHING` | `JUST TRUE` (the words "has made ... while in the migration zone" are met) or `JUST FALSE` (inferred from (1A), (1AB)) |
| F5 | s 338A(1)(c), (d) "other than a decision ... relying on" an excluded ground | `ss 338A, 347A -- I can apply to the ART` | `JUST FALSE` (no Part 5 review) | `NOTHING` (s 500 may give review of such decisions; not encoded) |
| F6 | a decision outside s 338A(1) | the same | `NOTHING` (it may be a reviewable migration decision under s 338, not encoded) | `JUST FALSE` |
| F7 | Acts Interpretation Act s 36(2), a last day on a weekend or holiday | `By when must I apply to the ART question`, `Am I in time to apply to the ART question`, the fee questions | the last day as counted, not moved | move a weekend last day to the Monday |
| F8 | s 5H(1) "a particular person in Australia", for a person outside Australia | `s 5H -- refugee` | `NOTHING` (a scope limit with no "only") | `JUST FALSE` |
| F9 | s 5J(1)(a) for a family social group (s 5K, not encoded) | `s 5J -- the Convention reason` | `NOTHING` | work s 5K out from facts (which fears to disregard) |
| F10 | "working day", undefined | `working days after` | weekdays that are not listed public holidays in the place | a calendar of a particular State or Territory |
| F11 | reg 4.31B(2), a payment made before the period begins | `Have I paid the ART fee in time question` | `FALSE` (outside the period the text fixes: periods ruling (a)) | treat an early payment as in time |

## Scope

**In (Act):** s 5AAA; s 5AA(1), (1A), (3); ss 5H, 5J, 5L, 5LA; s 5M (as a choice); s 35A (in glosses); s 36(1A)-(6); s 36A; s 46A(1), (1A), (2), (7) (the determination is an input); ss 48A, 48B(1); ss 91C, 91D(1), 91E, 91F(1); ss 91J, 91K, 91L(1); s 91V(1)-(3); ss 91W, 91WA, 91WB; s 197C(1)-(3), (7A), (9) (the protection finding of (4)-(7) is an input); s 197D(6); ss 338A, 339 (as an input), 347(3), (5), 347A(4), (5), 348(1); s 368(7); ss 379A, 379C(2)-(5); ss 494B, 494C(2)-(6). **(Regulations):** reg 2.16(3); reg 4.31B(1)-(4).

**Out, and why:**

- s 5K (family as a particular social group: which fears and persecution to disregard): a reasoning rule on the evidence, not reducible to facts the person can state without the decision-maker's analysis; a family social group answers `NOTHING`.
- The Schedule 2 criteria of the protection visa subclasses (Protection (Class XA), temporary protection, safe haven enterprise): the brief brings in regulations that set the Act's numbers; these are further criteria (s 35A(6)(b)) and are named as out in the s 36 question's description.
- s 36A(1)-(2) beyond whether the record must be made; s 197C(4)-(7) (what counts as a protection finding): the finding is the Minister's record, asked as a fact.
- ss 46A(3)-(6), 48B(2)-(6), 91F(2)-(6), 91L(2)-(6) (statements to Parliament, personal exercise), s 91D(2)-(4), s 91G (transitional applications), s 46B (transitory persons), s 37A, s 39A (annual numbers), ss 91X, 91Y (publication of names): machinery or outside the claimant's questions.
- s 91V(4)-(8) (immigration clearance statements): not a protection visa step.
- Part 5 beyond who may apply and by when: procedure, invitations, hearings, decisions on the papers (ss 357A-368D), remittal orders (s 349, reg 4.33), the conclusive certificate power (s 339, an input).
- s 494C(7), s 379C(7) (later actual receipt after an error), s 494D, s 379G (authorised recipients): not encoded.
- s 500 review, s 501 character, detention and removal duties (ss 189-198), ministerial intervention powers, bridging visas for asylum seekers.
- Regs 4.31BA, 4.31BB (CPI indexation of the fee): the current fee is an input; see finding 7.

## What the Act turns out to say

1. **The identity-document refusal (s 91W(3)) does no work.** Subsection (2) applies only if the applicant "does not have a reasonable explanation" ((2)(c)); subsection (3) disapplies (2) only where the Minister is satisfied the applicant has a reasonable explanation and produces evidence or took reasonable steps. Anyone (3) could help is already outside (2)(c), so the documents requirement in (3)(b) never bites. Contrast s 91WA(2), where explanation and evidence must both be shown. Asserted (a reasonable explanation without documents is not a s 91W refusal; a bogus document with an explanation but no documents is a s 91WA refusal).
2. **s 48A does not say that leaving Australia ends the bar.** Its words are met by anyone who "while in the migration zone, has made" a refused application and is in the zone again; only (1A) and (1AB), which deem continuous presence after a removal, imply that a departure otherwise breaks the bar. The encoding answers `NOTHING` for a person who has left in another way (fork F4). Asserted.
3. **Refugee status and the visa part company.** An ASIO adverse assessment or the Minister's view that a person is a danger does not stop the person being a refugee under s 5H (only the "serious reasons" of s 5H(2) do), but it stops the visa under s 36(1B), (1C). Asserted both ways.
4. **s 338A(2)(b) excludes only cancellations the Minister makes personally.** A refusal made personally by the Minister is not excluded by (2)(b) (it may be excluded by a s 339 certificate). Asserted.
5. **s 36(3) reaches complementary protection too.** Subsection (3) says Australia "is taken not to have protection obligations", and s 36(2)(aa) is framed as protection obligations; s 197C(5)(f) confirms ("except that subsection 36(2C) or (3) applied"). An unused right to live in a safe third country defeats both routes. Asserted.
6. **The protection review fee is paid after the ART decides, not on application.** Reg 4.31B(2) fixes "the 7-day period beginning on the day" the applicant is notified of the ART's decision. Read literally, a payment before that day is outside the period (fork F11). Asserted.
7. **The indexed fee is not in the compiled text.** Reg 4.31B(1) still reads $2,151, raised each 1 July from 2025 by the formula of reg 4.31BB; in the deposited conversion the formula itself is lost ("in accordance with the formula:" is followed directly by "where:"). A `F1996B03551.formulas.md` sidecar, transcribed from the authorised rendering, would be needed to compute the fee; the current figure is an input.
8. **Late is final.** s 347(5) turns off s 19 of the ART Act, so a review application one day late cannot be extended and, by s 348(1) and its note, the ART has no jurisdiction. The rule's breach says so. Asserted on day 29 (and day 15 if detained).
9. **"Working day" is not defined.** ss 48B, 91F and 91L do not say in which place a working day is counted (ss 494C(4)(a) and 379C(4)(a) say "in the place of that address"). The encoding takes a list of holidays from the person.

## Before relying on it

- An independent test pass, and a check of every fork line by a lawyer, especially F1, F2, F4 and F5.
- The Schedule 2 criteria of the protection visa subclasses, and reg 1.12 (member of the same family unit), encoded from the deposited Regulations.
- s 5K, s 197C(4)-(7) and s 36A worked out from facts rather than asked.
- The reg 4.31BB formula transcribed into a sidecar, and the fee computed.
- A holiday calendar for each State and Territory, if the working-day questions are to be used without the person listing holidays, and a decision on F7.
