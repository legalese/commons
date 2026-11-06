# Asbestos and Silica Safety and Eradication Agency Act 2013 — baseline encoding, the seat of a person with an asbestos- or silica-related disease

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill (regulative rules for the Agency's duty to report and publish, and for my permission to answer the CEO).
There is no REFUSE in it; a question the Act does not answer returns `NOTHING`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is the first encoding of this Act. No ledger entry asked for it. It was written as part of a run over the Acts behind compensation and other claims, with the focus "the provisions a claimant meets", in the dust diseases area. The Act's title changed in 2024 (it was the Asbestos Safety and Eradication Agency Act 2013); the deposit is the renamed Act.

Every question is a function named as the person would ask it, with `@export` and a `@desc` on every input, so it can be deployed to Legalese Cloud. There are 16 exported questions under `§§` headings in this order: the national plans; the Agency's progress report; the CEO's request for information (a situation: "if the Agency's CEO has written to you"); and, in situations marked "if you are seeking a place on the Council" or "if you are appointed to the Council", eligibility, acting, term, pay, disclosure, resignation and termination.

**Regulative rules.**

| Rule | Party | Modal | Seat question that reads it |
|---|---|---|---|
| `s 8A(1), (3) -- the Agency must prepare the progress report before the end of 31 December` | the Agency | MUST prepare, WITHIN 183 days of 1 July (31 December is day 183), LEST BREACH BECAUSE | `Is the progress report on time question` |
| `s 8A(5) -- the Agency must make the report publicly available` | the Agency | MUST make public, no WITHIN (the Act sets no time) | (traced in the cases; `Must the Agency make the progress report public question` asks the plain fact) |
| `s 14A(5) -- I may give the CEO the information within the period in the notice` | me | MAY give, WITHIN the notice's period | `Must I give the CEO the information question` |

The seat questions take plain facts (dates, yes/no) and run the trace inside. For a report not yet prepared, `Is the progress report on time question` traces the rule as if the report were prepared today: in time means "not yet due", out of time means "overdue". The case file asserts traces through a helper `ends fulfilled` (a `CONSIDER … WHEN FULFILLED`); the breach and the open duty are also `#TRACE`d with an `-- expect:` line, because a breached trace cannot be compared with `EQUALS` on the stable `l4`.

## Edition

The compilation registered as **C2024C00186** (Compilation No. 4, compilation date 31 May 2024, including amendments up to Act No. 27, 2024), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2013A00058.txt`. Sections 5A–5B are at lines 74–98 of the deposit, s 8A at 146, s 14A at 189, ss 31–40 at 300–407.

Nothing else is brought in. No rules under s 48 are deposited (they would set Council allowances and default remuneration, which no question here computes). The Constitution's s 51(v) (s 14A(4)) is glossed, not read: "postal, telegraphic, telephonic, or other like services" is asked as a fact (post, telephone, email, an online form). The Public Governance, Performance and Accountability Act 2013 s 29 (disclosure of interests) and the Remuneration Tribunal Act 1973 s 7(11) are not read; the first is asked as a fact, the second answered `NOTHING`. Section 36 of the Acts Interpretation Act 1901 is applied to count s 14A(3)'s 14 days (the day of giving excluded); it is not deposited here.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `asa-person.l4` | `asa-cases-person.l4` | 86 written, 86 satisfied; 2 traces, each as its `-- expect:` line says |

`l4 run` on both files, from this folder: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text. The edges: 5 and 6 governments (ss 5A(2), 5B(2)); a report prepared on 31 December and on 1 January, and not yet prepared on 31 December and on 1 January; a notice's last day 13 and 14 days after it was given, across a year end and a 29 February; a term of 36 and 37 months; a resignation naming a day before, on, one day after and well after receipt; 2 and 3 consecutive meetings missed.

## Seat

**A person with, or caring for someone with, an asbestos-related or silica-related disease**, and any person the Agency asks for information (a former worker, a family member, an employer, a builder); in the marked situations, the same person as a candidate for, or member of, the Asbestos and Silica Safety and Eradication Council, which s 32(3)(b) opens to people who have or had these diseases and their family members, carers and advocates. The questions are the ones that person asks: "Does the national plan commit governments?", "Is the Agency's progress report late?", "Can the CEO ask me for information? Must I answer? By when? Does privacy law stop me?", "Am I eligible for the Council?", "Am I paid?", "When does my resignation take effect?", "Can the Minister remove me?".

The Act addresses the Agency, the CEO, the Council and the Minister. Their duties and powers are encoded as what they mean for that person. No question is asked from the seat of the Agency, the CEO or the Minister.

The 2026-10-18 defaults:

- **The Act alone.** No instrument brought in (see Edition).
- **The actors the text names:** the Agency, the CEO, the Council and its members, the Minister, authorised worker and employer bodies, the governments of the Commonwealth, States and Territories, and the person in the seat.
- **Judgments handed to others are answered conditionally:** the CEO's belief on reasonable grounds and satisfaction (s 14A(1)); the Minister's satisfaction and agreement (s 32(3), (4), (7)); misbehaviour and incapacity (s 40(a), (b)); reasonable excuse (s 40(e)). All are inputs.
- **The Act's own definitions are worked out from facts:** when s 14A applies to a person; when a plan "represents a commitment" (ss 5A(2), 5B(2)); eligibility for each Council place; the day a resignation takes effect; "public statutory corporation" (s 35(2)(b)). Borrowed terms (asbestos-related disease, misbehaviour, a s 51(v) service, the PGPA s 29 duty) are asked as facts with a gloss.
- **One case:** one notice from the CEO; one report for one financial year; one appointment.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (see Scope).

The plan input to the s 5A/5B and s 8A date questions is asked so the form can name the plan; the two plans' provisions are in the same words, so the answers do not depend on it.

## Negatives (the 2026-11-04 and 2026-11-05 rulings)

`JUST FALSE` where the text says no in its own words: "only if" (ss 5A(2), 5B(2), 32(3), (4), (7)); "applies to a person if" and "by written notice" (s 14A(1), (2)); "must not be shorter" and "must involve" (s 14A(3), (4)); "must not be more than 3 years" (s 33); "is not entitled" (s 35(2)); "not eligible ... unless" (s 34(3), (4)); the "if" of s 37(3) failing. `NOTHING` where the text is silent: no condition for the Commonwealth and the State, Territory and local government places (s 31(b), (c)); acting places s 34(3), (4) do not reach; a report not yet prepared (s 8A(5)); a request outside s 14A (s 14A(6)); full-time Commonwealth or Territory service (left to the Remuneration Tribunal Act); no s 40 ground (the list is not closed with "only").

Fork lines (case-by-case sites, for the reviewer to overrule):

| Provision | Function | Answer taken | Other reading |
|---|---|---|---|
| ss 5A(2), 5B(2) "only if ... at least 6" once met | `Does the national plan commit governments question` | `JUST TRUE` | `NOTHING` (the condition is necessary only) |
| s 14A(5) "may comply" | `Must I give the CEO the information question` | `JUST FALSE` (no duty: a request and a permission in the text's words) | `NOTHING` (the Act is silent on a duty) |
| s 14A(6) "a law of the Commonwealth ... or a law of a State or Territory" | `May I give the information despite another law question` | a contract or duty of confidence: `NOTHING` | `JUST TRUE` (the general law of a State is "a law of a State") |
| s 32(3), (4), (7) "only if" once met | `Am I eligible to be appointed to the Council question` | `JUST TRUE` | `NOTHING` |
| s 31(ea) "1 member who has expertise" | `Am I eligible to be appointed to the Council question` | without expertise `JUST FALSE`, with it `JUST TRUE` | `NOTHING` both ways (s 31 sets the composition, not eligibility) |
| s 34(3), (4) "eligible for appointment as that member (see subsection 32(3))" | `Can I be appointed to act on the Council question` | the whole of s 32 (for workers' and employers' places, s 32(4) or (7) too) | s 32(3) alone, as the bracketed pointer suggests |
| s 34(3), (4) "not eligible ... unless" once met | `Can I be appointed to act on the Council question` | `JUST TRUE` | `NOTHING` |
| s 40 grounds, none met | `Can the Minister terminate my Council appointment question` | `NOTHING` (list not closed with "only") | `JUST FALSE` (grounds for ending a statutory office are usually read as exhaustive) |

## Scope

**In:** ss 5A(2), 5B(2); s 8A(1), (3), (5); s 14A(1)–(6); s 31 (the places); s 32(3), (4), (7) (with (5), (6), (8), (9) as the meaning of "authorised" body, asked as a fact); s 33; s 34(2)–(4); s 35(2) (with (1) as the entitlement it qualifies); s 37(1), (3); s 39; s 40.

**Out, and why:**
- ss 1, 2, 2A, 4, 5 (title, commencement, object, Crown, external Territories) and s 3 beyond the terms used: machinery.
- ss 5A(1), 5B(1) (what the plans aim at): descriptive; the plans themselves are not deposited.
- ss 6–9 (the Agency's continuation, constitution, functions, constitutional limits in s 8(4), privileges): the Agency's machinery. Section 14A borrows s 8(1)(a), (b), (g), glossed in the `@desc`. Whether a request is within s 8(4)'s constitutional limits is not asked: it is a question about the Agency's power, for a court.
- s 8A(2), (4) (copies of the report to Ministers): between officials, nothing the person can act on.
- ss 10–24 except s 14A (the CEO's office, functions, directions, appointment, pay, leave, outside work, resignation, termination, delegation, committees): the office-holder's seat is not this one; a CEO seat could be added beside.
- ss 25–27 (staff, consultants, persons assisting), ss 28–30A (the Council's functions, guidelines, Ministerial directions, committees), s 32(1), (2) (how appointments are made), s 34(1) (an acting Chair, open to any Council member), s 35(1), (3), (4) beyond the entitlement, s 36 (leave), s 37(2), s 38, ss 41–41E (meetings, quorum, voting, minutes), s 41F (finance law), ss 42–44 (annual operational plan), ss 46–48 (delegation, review, rules): machinery.

## What the Act turns out to say

1. **The Act gives a person with an asbestos-related or silica-related disease no claim, payment or compensation.** It sets up an agency and a council to coordinate national action. Such a person meets it as someone the CEO can ask for information (s 14A), as a reader of the national plans and the Agency's progress reports (ss 5A, 5B, 8A), and as a possible Council member (s 32(3)(b)). Compensation for dust diseases is in State and Territory workers' compensation and dust diseases Acts, and in the common law.
2. **Answering the CEO is voluntary.** Section 14A is worded as a "request", and s 14A(5) says a person "may comply". There is no duty, no penalty and no consequence for not answering or answering late. Asserted (no answer; an answer five days late).
3. **But answering is protected against other laws.** Section 14A(6) makes the permission to comply effective "despite anything in" any other Commonwealth law or any State or Territory law, so a privacy or health-records law does not stop a person giving the information asked for. The text does not say whether a contract (a confidentiality clause in a settlement deed) or an equitable duty of confidence counts as "a law"; the encoding answers `NOTHING` (fork line). Asserted.
4. **The 14-day minimum (s 14A(3)) runs "after the notice is given"**, so with s 36 of the Acts Interpretation Act 1901 a notice given on 1 March may set 15 March but not 14 March. The Act does not say when a notice is "given" (by post or email); that is asked as a date. Asserted.
5. **The Council's list of places and the instrument's list do not match.** Section 31 has seven kinds of place, including (ea) "1 member who has expertise relevant to" asbestos or silica. Section 32(2), which says what the instrument of appointment must specify, lists six and has no expertise member, so an instrument cannot specify the (ea) place in the words the Act requires. Section 32(3) does not cover (ea) either. The encoding reads (ea)'s own words as its eligibility (fork line). Recorded and asserted.
6. **Section 32(2)(ca) and (cb) say "the member" representing workers (and employers), but s 31(d) and (e) provide for 2 of each.** Likely an amendment that changed s 31 without s 32(2). It changes no answer here. Recorded.
7. **People with these diseases, and their carers, can be Chair.** Section 32(3)(b) makes lived experience alone (as the Minister is satisfied of it) enough for the Chair, an "other member" place, and (with a nomination and the Minister's agreement) a workers' or employers' place. Asserted.
8. **The acting-appointment rule points only at s 32(3).** Section 34(3) and (4) say a person is not eligible to act in a s 31(d), (e) or (f) place "unless the person is eligible for appointment as that member (see subsection 32(3))". For the workers' and employers' places eligibility also needs a nomination and the Minister's agreement (s 32(4), (7)). The encoding reads the whole of s 32 in (fork line). Asserted. An acting Chair (s 34(1)) must be a Council member but meets no eligibility test of its own.
9. **Section 37(3) can put a member in breach for another's omission.** If the Council does not record a member's disclosure in its advice, recommendations or guidelines, the member "is taken not to have complied with section 29" of the PGPA Act, which is a ground for termination under s 40(e) unless the member has a reasonable excuse. Asserted.
10. **Section 40's grounds are not closed with "only".** Read under the 2026-11-04 rulings, the encoding answers `NOTHING` when none is met (fork line). Asserted.
11. **"6 of the governments of the Commonwealth and each State and Territory"** (ss 5A(2), 5B(2)) does not say whether the external Territories count. With the Commonwealth, six States and two internal self-governing Territories there are nine governments; 6 of 9 is the usual reading. The number is asked as a fact. Recorded.
12. **The silica report duty (s 8A(3)) came in with Act No. 27, 2024.** Which financial year it first covers depends on that Act's application provisions, which are not in the compilation. The encoding answers the date for any year asked. Recorded.
13. **Section 35(2) excludes State full-time employees from Council pay but not State university staff** (s 35(2)(b)(ii)). Asserted. Commonwealth and Territory employees are left to the Remuneration Tribunal Act 1973 (the Note): `NOTHING`.

## Raised in the ledger

Nothing. A person with a dust disease next needs the State and Territory dust diseases and workers' compensation Acts.

## What would need doing before this is worth relying on

- The Public Governance, Performance and Accountability Act 2013 (s 29 and its rules) and the Remuneration Tribunal Act 1973 (s 7(11)), deposited and encoded, so disclosure and pay need not be asked.
- The amending Act No. 27, 2024's application provisions, for when the silica report duty first applied.
- Any rules under s 48, if made.
- Case law on statutory office termination grounds, on "a law of a State" and confidentiality, and on giving notices.
- An independent test pass and a human review.
