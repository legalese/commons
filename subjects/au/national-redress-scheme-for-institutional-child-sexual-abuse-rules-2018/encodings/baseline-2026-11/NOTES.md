# National Redress Scheme for Institutional Child Sexual Abuse Rules 2018 — baseline encoding, the survivor's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; where a section does not reach the facts, the answer says so ("Rules s N does not apply …"), or is `NOTHING`, and the cases assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is the first encoding in the Rules' own folder. No ledger entry asked for it; it was written in a run over the instruments behind personal injury, compensation and other claims, with the focus "childhood abuse". The parent Act has its own baseline (`subjects/au/national-redress-scheme-for-institutional-child-sexual-abuse-act-2018/encodings/baseline-2026-11/`), which already brought in Rules ss 4B, 6, 11, 12, 15, 26(3)-(5) and 33(3) for the Act's questions. This encoding takes the Rules as the instrument: it re-asks those sections in the Rules' own words (the stable `l4` cannot import across subjects, so nothing is shared in code) and adds the parts the Act baseline left out: ss 8-10 (government, Defence and child-migrant responsibility), 17 (revocation), 31 (the acceptance document), 34-35C (notices on an applicant's death), 37, 39 (notices after a serious conviction or a security notice), Part 11 (public-interest disclosure of the survivor's information), 71 (settlement deeds) and 72-74 (what the survivor must tell the Operator). Nothing in the Act encoding was changed.

There are **21 exported questions**, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a survivor meets them (eligibility, scope, responsibility, applying as a child, revocation, earlier payments, acceptance, payment, death, convictions and security notices, disclosure, settlement deeds, my duties to notify). Headings for situations the person may not be in say so in square brackets.

**Regulative rules.** Each runs inside a question that takes plain dates; no question takes a DEONTIC or an EVENT.

| Rule | Party | Modal | Seat question that runs it |
|---|---|---|---|
| `Rules s 15(2) -- the Operator must give me a notice 3 to 6 months before I turn 18` | the Operator | MUST give the notice, PROVIDED the day is not before the window opens, WITHIN the days to 3 months before turning 18; LEST breach | `Has the Operator given me my notice about turning 18 in time question` |
| `Rules s 74(2) -- I must notify the Operator before I accept my offer of redress` | I, the survivor | MUST notify in writing WITHIN the days from accepting the payment offer to accepting the offer of redress; LEST breach | `Did I tell the Operator about the payment in time question` |

The cases assert traces through a helper `ends fulfilled` (`CONSIDER … WHEN FULFILLED`), and `#TRACE` each breach with an `-- expect:` line, because a breached trace cannot be compared with `EQUALS` on the stable `l4`.

## Edition

National Redress Scheme for Institutional Child Sexual Abuse Rules 2018, **Compilation No. 9, compilation date 19 February 2025** (register id F2025C00180, includes amendments up to F2025L00132), retrieved from the Federal Register of Legislation on 6 November 2026, as deposited at `../../registers/source-bundle/F2018L00975.txt`. The Register gives the compilation an end date of 1 October 2028.

**From the parent Act** (deposited at `subjects/au/national-redress-scheme-for-institutional-child-sexual-abuse-act-2018/registers/source-bundle/C2018A00045.txt`, Compilation No. 9, 28 September 2024): the scheme sunset day, 1 July 2028 (Act s 193(1)(a); the Rules prescribe no later day), used by Rules s 15(1); and the Act provisions the Rules work under (ss 13, 14, 15, 29(4)-(7), 48(1A), 58, 59, 63, 71, 95, 181), quoted in comments where a question needs them. The Act's own tests (eligibility, scope, responsibility under s 15(2)-(4)) are asked as facts here; the Act baseline encodes them.

**Not deposited, so inputs:** the assessment framework (whether the maximum redress payment would be more than nil, Rules s 4B(1)(c)); the Ministers' declarations of participating institutions and of listed institutions (Act ss 164-164C).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nrsr-dates.l4` | (exercised through the cases) | 0 errors, 0 warnings |
| `nrsr-survivor.l4` | `nrsr-cases-survivor.l4` | 163 written, 163 satisfied; 2 traces, each a BREACH as its `-- expect:` line says |

`l4 run` on all three files: 0 errors, 0 warnings (2026-11-07); every diagnostic is `DiagnosticSeverity_Information`. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text before the run. Every exported question has cases, with the edges: arrival in 1983 and 1984 (s 4B, s 10 "before 1984"); abuse on 31 December 1976 and 1 January 1977 (s 9); an application exactly 4 months before turning 18 and one day later; an application on the day before and on the 18th birthday; a child turning 18 on the sunset day; a February with no matching day (the window computed from 30 June); a notice on the window's first and last days, the day before it opens and the day after it closes; a birthday of 29 February; earlier payments whose excluded parts equal and exceed the payment; a payment made for several institutions (s 26(6), `NOTHING`); a notification on the day the offer of redress is accepted and the day after; a sentence of 5 years and of 4.99 years.

## Seat

**The survivor**: a person who was sexually abused as a child in circumstances an institution was responsible for, and who applies for redress under the scheme. In Rules ss 34-35C (notices when the applicant dies) and s 33(3) the seat is the family member, executor or other person asking on the applicant's behalf. Questions are phrased as that person asks them: "Am I eligible as a child migrant?", "Is the government that placed me equally responsible?", "Can the decision be revoked?", "How much of my earlier settlement counts against my redress?", "Can my settlement deed stop me?", "Must I tell the Operator …, and by when?".

The Operator, the institutions, funders of last resort, the Ministers and the participating jurisdictions get no seat. Their duties are encoded as what they mean for the survivor (what must be given to me, by when; whether my information may be disclosed), and their findings are inputs.

The 2026-10-18 defaults:

- **The Rules, with the Act provisions they serve.** The sunset day comes from the Act; the assessment framework is not deposited (see Edition).
- **The actors the text names:** the person, the Operator, participating and government institutions, Commonwealth defence institutions, the Department administering the Immigration (Guardianship of Children) Act 1946, defendant institutions, released institutions and officials, executors and administrators, the listed Ministers.
- **Judgments handed to others are answered conditionally:** responsibility findings under Act s 15 ("would be primarily responsible", "approximately equally responsible"), "information … that would have [changed] the determination" (s 17(2)), "considers it appropriate" (Act s 48(1A)), "the person the Operator considers most appropriate" (ss 34-35C), the Operator's satisfaction (s 43(1)) — all inputs, or (s 43) an answer "may be certified, if the Operator is satisfied". "As soon as practicable" (ss 15(4), 72-74) is named, never decided.
- **The Rules' own definitions are worked out from facts:** the child-migrant conditions (ss 4B(2), 10(1)), the s 8 circumstances, the s 9 cadet conditions, the s 11(1) court order, the s 12 "only connection", relevant prior payment exclusions (s 26(3)-(5)). Borrowed terms (participating institution, ward, sexual offence, security notice) are asked as facts with a gloss.
- **One case:** one person's application, one institution or one payment at a time.
- **The Rules' own terms**, quoted in the comment above each rule.
- **Machinery out** (see Scope).

## Negatives (the 2026-11-04 and 2026-11-05 rulings)

The rulings, word for word as section 5 of `docs/ENCODING-GUIDE.md` records them: a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit. Periods ruling: (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`. Delegated definitions and defences ruling (b): "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all".

Applied here, with enumerated answers that carry their own reason in place of bare booleans:

- **The text's own no, for that provision only** (the (b) wording, "this section gives no … on these facts"): s 4B ("eligible … if": "no, not under Rules s 4B …"; Act s 13(1) is another route); s 43(1) ("may certify … if": "no, not under Rules s 43 …"; Act s 95(1)(b) and (1A) are other routes); s 17 ("Rules s 17 gives the Operator no ground to revoke on these facts"); Act s 181(1) and Rules ss 73-74 ("no, not under …"); s 26(3)-(5) (flat "is not a relevant prior payment": `JUST 0`); Act s 29(5) ("cannot revoke").
- **The section does not reach the facts** (no claim either way; the Act decides): ss 6, 8, 9, 10, 11, 12, 15, 37, 39, 71 when their conditions fail ("Rules s N does not apply …", "… responsibility is decided under Act s 15").
- **`NOTHING`:** s 26(6) (a payment by or for several responsible institutions: the formula is lost, finding 1).

Fork lines (case-by-case sites, for the reviewer to overrule):

| # | Provision | Function | Answer taken | Other reading |
|---|---|---|---|---|
| F1 | s 4B(1) "also eligible … if" | `Am I eligible as a child migrant question` | "no, not under Rules s 4B" when a condition fails | `NOTHING` (the Act's general route is untouched, and further rules could prescribe more) |
| F2 | s 15(2) "at least 4 months before", "at least 3 months, but not more than 6 months, before" | `When will my application as a child be decided question`, `Has the Operator given me my notice about turning 18 in time question` | measured to the same day-number in the earlier month (the month's last day where it has none), both ends inclusive; agrees with the Act baseline's fork F13 | measured as Acts Interpretation Act periods ending on the birthday |
| F3 | a date of birth of 29 February | `the eighteenth birthday for` | 18 on 1 March in a year with no 29 February | 28 February |
| F4 | s 26(4)(a), (b) "to the extent that" | `How much of an earlier payment counts against my redress question` | the two parts subtracted as stated; the input asks that nothing be counted twice | the larger of the two parts only |
| F5 | s 33(3) and (4), both "Despite subsection (2)" | `Where will my redress payment be paid question` | after the person's death, (3) (the executor's account) before (4) (the administrator's account) | (4) whenever Act s 48(1A) applies |
| F6 | s 74(2) "in any case before accepting the offer of redress" | `Did I tell the Operator about the payment in time question` | a notification on the same day as the acceptance counts as before it | only a notification on an earlier day counts |
| F7 | s 11(1)(c) "if the order is that the defendant institution pay the group" | `Is an institution ordered by a court to pay me still responsible question` | a choice not to take a payment matters only for a group order | — |
| F8 | s 43(1) "if the Operator is satisfied that" | `Can my information be disclosed in the public interest question` | the facts asked as facts; the answer "may be certified, if the Operator is satisfied" | the Operator's satisfaction asked as an input |
| F9 | s 12(2) "the only connection … is one or more of" | `Is a government body that only regulated or funded responsible question` | at least one of regulated, funded, established, and no other connection | — |

## Scope

**In:** ss 4 (definitions used), 4B, 6, 8, 9, 10, 11, 12, 15, 17, 26(1)-(5) (with (6) as `NOTHING`), 31, 33, 34, 35, 35A, 35B, 35C, 37, 39, 42, 43, 44-54A, 71, 72, 73, 74.

**Out, and why:**
- ss 1, 3, the simplified outlines (ss 4A, 5, 7, 13, 15A, 16, 18, 30, 32, 35D, 36, 38, 40, 54AA, 54D, 55, 66, 70): machinery and summaries; read for meaning only.
- Part 4A (s 15B, State and Territory laws that may prevent someone giving information to the Operator): it concerns third parties asked for information, not the survivor; a list of 51 provisions with no test to compute.
- Part 6 Divisions 2, 4-7 (ss 19-25, 27-29A: sharing the maximum amount, the counselling component and reassessment surpluses among institutions and funders of last resort): duties between institutions; the survivor's amount turns on them only through Act s 30, and the formulas in ss 21(1), 23(2), 24(1), 25(1) and 27(3), and the fractions in the s 21(2) table, are missing from the deposit (finding 1).
- s 31A (contents of the notice to funders of last resort), Part 8A (ss 35E, 35F, notices to institutions about reassessment): notices between the Operator and institutions.
- Parts 11A and 11B (ss 54B, 54C, 54E: schools, universities and a youth club that are, or are not, State or Territory institutions): lists of named bodies, best looked up by name; a later layer could ask "is my school a State institution?".
- Part 12 (ss 56-65: declaring participating institutions and groups, representatives), Part 13 (ss 67-69: institutions' contributions to administration, funder-of-last-resort agreements), s 74A (protected symbol), s 75 (annual report): machinery, and other parties' affairs.

## What the Rules turn out to say

1. **The Rules' formulas are missing from the deposit.** Sections 21(1), 23(2), 24(1), 25(1), 26(6) and 27(3) each end "using the following formula:" with nothing after it, and in the s 21(2) table only item 1 has its fraction ("Half"); items 2-5 have none. The Word equation images were dropped and the Rules subject has no formulas sidecar. So s 26(6) answers `NOTHING` (asserted), and the cost-sharing rules are out. The Act baseline records the same gap (its finding 10).
2. **A child migrant is eligible under s 4B without being an Australian citizen or permanent resident.** Section 4B(1) repeats Act s 13(1)(a)-(d) and replaces (e) with the s 4B(2) child-migrant conditions. Asserted (eligible on the s 4B facts alone).
3. **Revocation follows a s 74 notice, but not a s 73 notice.** Section 17(3)(a) obliges revocation on "notification from the person under section 74". A payment offer accepted after the determination is made but before notice of it is given falls under s 73 (which turns on the notice, not the determination), so its notification is not a s 17(3)(a) ground; the Operator must revoke only once the payment is "paid" (s 17(3)(b), (4)(b)), or may revoke under s 17(2). Encoded as written.
4. **Section 11(3)'s two conditions pull against the Act's definitions.** It needs the defendant institution and others to be "approximately equally responsible for the abuser having contact", and the defendant institution, apart from the order, to have been "primarily responsible", which Act s 15(2) defines as "solely or primarily responsible for the abuser having contact". Both are asked as the Operator's findings, and s 11(3) is applied only when both are found. Asserted both ways.
5. **Section 11(1)(c) is a double negative** ("the person does not choose not to accept the person's share"), and only for an order to pay a group. A group member who declines their share keeps the institution responsible under the scheme. Asserted (fork F7).
6. **Section 39(2) names no notice for the reassessment cases it was extended to.** Section 39(1)(c) and (d) bring in Act s 71(2A) and (2B) (a reassessment agreement revoked; a new offer withdrawn and a reassessment decision revoked), and s 39(2)(b)(iii)-(iv) point to the reassessment notices, but the notice itself is still "of the withdrawal of the application and, if relevant, the revocation of the determination and withdrawal of the offer", none of which happens in those cases. The answers say so. Asserted.
7. **Section 37(1) mixes "or" and "and"**: "(a) becomes aware … [of a listed offence], or (b) has determined … special assessment …; and (c) decides … not to make a determination". Read as (a or b) and (c). Asserted.
8. **The duty to report a prison sentence (Rules s 72) reaches only sentences after the application** (Act s 181(1)(b)); a sentence before applying is not reported under s 72, though Act s 63 applies to it. Asserted.
9. **Rules s 33(3) and (4) both apply "Despite subsection (2)"**, with no order between them (fork F5).
10. **Section 12 is "subject to Division 2"**, so a government authority made equally responsible by ss 8-10 stays responsible even where its only other link is funding or regulation. Asserted.

## Raised in the ledger

Nothing. A formulas sidecar for the Rules deposit (finding 1) would let a later layer work out each institution's share (ss 21-25, 27) and s 26(6). The ledger `subjects/au/requirements.jsonl` was not changed.

## Links

- **National Redress Scheme for Institutional Child Sexual Abuse Act 2018** (`subjects/au/national-redress-scheme-for-institutional-child-sexual-abuse-act-2018/encodings/baseline-2026-11/`): the parent Act's survivor baseline. Where both encode a Rules section (ss 4B, 6, 11, 12, 15, 26(3)-(5), 33(3)), the readings were written to agree (the s 15(2) window, the s 26 exclusions); a later check should run the same facts through both.
- **Territories Stolen Generations Redress Scheme (Facilitation) Act 2021**: a related redress scheme.

## What would need doing before this is worth relying on

- An independent test pass against the text, and a lawyer's look at the fork lines F1-F9 and findings 3, 4 and 6.
- A formulas sidecar for the Rules deposit, then the cost-sharing sections.
- The assessment framework deposited (Rules s 4B(1)(c), and the amounts the Act needs).
- Mirror cases run through this encoding and the Act baseline.
- Checking that the deposited compilation (19 February 2025) is still current.
