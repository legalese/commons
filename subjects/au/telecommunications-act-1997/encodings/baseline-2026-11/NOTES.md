# Telecommunications Act 1997, Schedule 3 — baseline encoding, the seat of the owner or occupier of land a carrier works on

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
There is no REFUSE in it; a question that reaches a gap answers `not covered` with the reason, or `NOTHING`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is a second encoding of this Act, beside `baseline-2026-10` (Part 19, the end-user wanting a broadband connection), which is untouched; this one shares no module with it. No ledger entry asked for it; it was written in a run over the Acts behind compensation and other claims, with the focus "the provisions a claimant meets".

**Why Schedule 3.** The Act has no class-action or group-claim provisions. The claims a member of the public brings under it are (a) damages from a statutory infrastructure provider under Part 19 Division 4A (already in `baseline-2026-10`), and (b) compensation from a carrier for loss or damage from its work on land under Schedule 3 cl 42, with the matching compensation for an acquisition of property (cl 62, s 591). This encoding takes (b) and the steps the landholder meets before it: the notice, the tree request, the removal and restoration duties, and who owns and pays for the facility.

There are 13 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a landholder meets them (notice; trees; temporary facilities; restoration; compensation; acquisition; ownership and subdivision). The acquisition group arises only where a court would find an acquisition of property, as its heading says.

**Regulative rules.** Four, each a rule over time; three run inside plain-fact seat questions (no question takes a DEONTIC or an EVENT):

| Rule | Party | Modal | Seat question that runs it |
|---|---|---|---|
| `cl 17(4), (4A) -- the carrier must not begin before the notice period has run` | the carrier | SHANT begin WITHIN (period − 1) business days of the notice day | `Was the notice I was given good enough` |
| `cl 18(1), (2) -- I am asked to do it myself; only if I do not may the carrier` | me, then the carrier | DO the requested lopping WITHIN the period in the request; LEST the carrier MAY do it | none (traced in the cases; the seat question decides on the same facts arithmetically) |
| `cl 8A -- the carrier must remove the temporary facility within 28 days` | the carrier | MUST remove WITHIN 28 days | `Was the temporary facility removed in time` |
| `cl 9(2), 9A(3), (4) -- the carrier must begin restoring my land in time` | the carrier | MUST begin restoring WITHIN 10 business days, or the later time agreed | `Did the carrier begin restoring my land in time` |

A helper, `the rule ends fulfilled` (a `CONSIDER … WHEN FULFILLED`), tells fulfilment from breach or an open rule; on the stable `l4` a breached trace cannot be compared with `EQUALS`. The cases assert through it and `#TRACE` two breaches with `-- expect:` lines.

**Clocks.** Notice, tree-request and restoration periods are in business days as the person counts them (an input); the removal period and the calendar-year limits in days. Schedule 3 does not define "business day" (the Act defines it only section by section, as in s 55(3)), so the Acts Interpretation Act 1901 s 2B meaning, borrowed and not deposited, would apply: not a Saturday, a Sunday or a public holiday in the place concerned. No holiday calendar is deposited, so the encoding does not count business days from dates.

## Edition

The compilation registered as **C2026C00224** (Compilation No. 117, compilation date 4 June 2026), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2004A05145.txt`: Schedule 3 Part 1 at lines 15102–15885, Part 3 at 15905–15928, s 591 at 14059.

**No instrument is deposited.** The Telecommunications (Low-impact Facilities) Determination (cl 6(3)), the regulations (cl 3(b)(ii), 7(5)(d), 14, the listed international agreements) and the Telecommunications Code of Practice (cl 15, which holds the landholder's objection procedure) are not deposited. Whether a facility is low-impact, and what the Code requires, are facts the person states or are out of scope.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ta97-landholder.l4` | `ta97-cases-landholder.l4` | 106 written, 106 satisfied; 2 `#TRACE`s, each a BREACH as its `-- expect:` line says |

`l4 run` on both files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text; edges asserted include the 10th and 9th business day of notice, the 2nd and 1st for a low-effect inspection, work begun on the notice day, day 28 and 29 for removal, 183/184 and 90/91 days in a calendar year, the 10th and 11th business day for restoration (begun, and not begun), an agreed "later" start of exactly 10, and a claim equal to and one dollar over the inferior court's limit.

## Seat

**The landholder**: the owner of land a carrier inspects, builds on or maintains a facility on, or an occupier of it other than the owner (a tenant, a farmer on leased land). "Must the carrier tell me before it comes onto my land, and how far ahead? Was the notice good enough? Can it cut down my trees? How long can a temporary tower stay? When must it put my land back? Can I get compensation, and where do I sue? Who pays if my property is in effect taken? Is the cable mine? Must I pay if I subdivide?"

Schedule 3 is addressed to carriers. Their duties are encoded as what they mean for the landholder. No question is asked from the seat of the carrier, the ACMA or the Minister. A carrier seat would be possible (the carrier is a business with duties) and is not written.

The 2026-10-18 defaults:

- **The Act alone**, with the instruments that set its numbers asked as inputs (none deposited).
- **The actors the text names:** the carrier (with its employees, contractors and their employees, cl 43), the owner, the occupier, the person who subdivided, the Commonwealth (s 591), a court of competent jurisdiction.
- **Judgments handed to others are answered conditionally:** whether work "need[s] to be carried out without delay" (cl 17(6), 18(4)), whether the carrier "considers" notice impracticable (cl 17(6A), 18(3A)), the carrier's "opinion" (cl 53), the "reasonable amount" of compensation (never computed), whether there is an "acquisition of property" in the constitutional sense (cl 62, s 591), whether "the circumstances indicate otherwise" (cl 47). Each is an input.
- **The Act's own definitions are worked out from facts:** an activity under Division 2, 3 or 4; the owner and the occupier "other than the owner"; the four conditions of cl 17(4A) and (7) (called here a "low-effect inspection", which is not the Act's term); the temporary facilities of cl 6(5)(b)–(g) and 7(3A); a court of competent jurisdiction (cl 42(3)). Borrowed terms ("acquisition of property", "just terms", "business day", "public holiday") are asked as facts or left to the person's count.
- **One case:** one carrier's activity on one parcel of land.
- **The Act's own terms**, each with a plain gloss in a comment.
- **Machinery out:** facility installation permits (Division 6), exemptions from State and Territory laws (Division 7), ACMA guidelines and public information (cl 41, 48–51), and the power to make the Code of Practice.

## Scope

**In:** Schedule 3 cl 2 (the definitions used), cl 5, 6, 7 (as the kind of activity, a fact), cl 6(5)(b)–(g) and 7(3A) (as the kinds of temporary facility), cl 8A, 8B, 8C, 9, 9A, 17, 18, 42, 43, 46(7), 47(a), 53; Part 3, cl 62, 63; s 591(1), (2).

**Out, and why:**

- cl 1, 3, 4 (outline; designated overhead lines; tower extensions): definitional detail for the carrier's powers, not a step the landholder takes.
- cl 6(1)–(9), 7(1)–(10) in their detail (what a carrier may install or maintain without a permit, the low-impact determination): the carrier's authority, which turns on an instrument not deposited. Taken as a fact.
- cl 8, 10, 11–16 (as little damage as practicable, good engineering practice, utilities, standards, international agreements, regulations, the Code of Practice, permit conditions): "all reasonable steps" duties and duties defined by instruments; they matter to a landholder chiefly as part of a negligence or compensation argument, which cl 42 already gives. Named in comments only.
- cl 19, 20 (notice to roads authorities and utilities; passage over roads): addressed to authorities, not the individual.
- Division 6, cl 21–35 (facility installation permits) and Division 7, cl 36–39 (exemptions from State and Territory laws): carrier and ACMA machinery; a landholder meets them only through a public inquiry, and the review cl 35 allows is only of a refusal to issue a permit.
- cl 41, 44, 45, 46(1)–(6), 47(b), 48–52, 54: ACMA guidelines; State laws that discriminate against carriers; the ACMA's power to cap tort damages (only (7), which excludes cl 42 claims from any cap, is in); network units; public information; Commonwealth laws not displaced; service of notices by newspaper (cl 54, a carrier's fallback; it would affect when a landholder is taken to have been given notice).
- Part 2, cl 60, 61 (pre-1997 facilities and trespass): transitional.
- s 591(3)'s extension to other Acts; Schedule 3A (submarine cables) and the rest of the Act.
- The Telecommunications Code of Practice and its objection procedure: not deposited (finding 2).

## Negatives (the 2026-11-04 and 2026-11-05 rulings)

The guide's rulings are applied as follows; each fork below is open for a reviewer to overrule.

- **E1** (bench `commons-negation-1030`), verbatim from the guide: "option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else". Here: per-clause answers; compensation for loss (cl 42) and for acquisition (cl 62, s 591) are separate questions.
- **N2**, verbatim from the guide: "option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer". Here: cl 18(2) "may only engage in those activities if the request is not complied with" is read as a no once the request is complied with.
- **Periods, "where" and scope limits** (ruled 2026-11-05): a period the text fixes ("within 28 days", "within 10 business days", "at least 10 business days before") outside the period answers no (`late`, `too late`); a scope limit with no "only" (cl 8B, 8C reach only some kinds of tower) answers `NOTHING` for the kinds outside it.
- **Forks decided case by case** (Meng, 2026-11-05):
  - F1. cl 17(4), `Was the notice I was given good enough`: work beginning on the nth business day after the notice day meets "at least n business days before"; the other reading (clear days, Acts Interpretation Act s 36, borrowed) needs n + 1.
  - F2. cl 17(2)–(4), the same question: a notice with several defects reports the first in the order purpose, compensation statement, timing; the other reading lists them all.
  - F3. cl 18, `Can the carrier cut my trees or clear my vegetation`: trees not on private land, work outside Divisions 2–4, and a person neither owner nor occupier all answer `not covered` (the clause is silent for them); the other reading answers that the carrier needs no request (true of the clause, not of the carrier's power).
  - F4. cl 62, 63 and s 591, `Who must compensate me for an acquisition of my property`: where cl 62 applies, the carrier pays and s 591 is taken not to bite (the acquisition is then on just terms); a Schedule 3 acquisition before the 2005 amendments falls to s 591. The other reading lets s 591 run alongside cl 62.
  - F5. cl 8B, 8C, `Have temporary towers stayed beyond the calendar-year limit`: `NOTHING` for the kinds of facility with no calendar-year limit; the other reading answers `JUST FALSE` (never beyond a limit that does not exist).

## What the Act turns out to say

1. **The Act has no class-action or group-claim provisions.** For a claimant it offers individual statutory compensation: from a carrier for loss or damage from its work on land (cl 42), for an acquisition of property (cl 62, from the carrier; s 591, from the Commonwealth), and damages from a statutory infrastructure provider under Part 19 (in `baseline-2026-10`). Several landholders on one cable route each hold their own cl 42 claim.
2. **There is no objection procedure in the Act.** A landholder's right to object to a low-impact facility or a maintenance activity is in the Telecommunications Code of Practice made under cl 15, which is not deposited. The Act gives notice (cl 17) and the tree request (cl 18), not a right to stop the work.
3. **"At least 10 business days before" is not counted for the reader.** Schedule 3 does not say whether the notice day counts, nor define "business day" (finding 4). The encoding takes the 10th business day after the notice day as in time (fork F1); a clear-days reading would make it the 11th. Asserted on the encoding's reading.
4. **"Business day" in Schedule 3 is the Acts Interpretation Act's**, not the ACMA-open-in-the-ACT-and-Victoria definition the Act gives in particular sections (s 55(3) and others). Public holidays therefore follow the place concerned. The person's own count is the input.
5. **The restoration and damage duties are "all reasonable steps" duties.** cl 9 and 9A require the carrier to "take all reasonable steps to ensure" that restoration begins within 10 business days; a late start is where the question begins, not a breach by itself. The encoding's rule and question track the start itself and say so in the answer. Asserted.
6. **The notice exceptions are narrower than they look.** The public-place exception (cl 17(7)) is for inspections only, and the emergency-tower exception (cl 17(8)) only for installing one; maintenance of the same tower still needs notice. A low-effect inspection of private land still needs 2 business days' notice. Asserted.
7. **The landholder gets the first chance to cut their own trees.** The carrier must ask in writing at least 10 business days ahead, and "may only" do the work itself "if the request is not complied with" (cl 18(1), (2)). Where both an owner and an occupier are asked, the clause does not say whose compliance counts; the encoding answers from the asker's own compliance. Asserted.
8. **A holiday-period tower has no removal deadline;** cl 8A covers the other temporary towers (28 days after the triggering event), and the holiday tower is limited only to 90 days a calendar year at the place (cl 8C); event towers 183 (cl 8B). Asserted at 183/184 and 90/91.
9. **Compensation under cl 42 is open-ended and uncapped.** It "includes, without limitation" temporary as well as permanent damage and the taking of sand, soil, stone, gravel, timber, water and other things (cl 42(2)), and an ACMA cap on tort damages does not apply to it (cl 46(7)). It is owed to anyone with an interest in the property, not just the owner. Asserted.
10. **The Act sets no time limit for a cl 42 or cl 62 claim.** The limitation period would come from the general law of the forum (borrowed, not deposited). Not encoded; a claimant should not read the absence as "no limit".
11. **Any court may hear a cl 42 claim if its debt limit is at least the claim:** the Federal Court, the State or Territory Supreme Court where the property is, or a local inferior court whose limit is "not less than" the amount claimed (cl 42(3)). A claim equal to the limit qualifies. Asserted.
12. **A carrier's facility stays the carrier's even when it becomes a fixture** (cl 47(a)), and **a landholder who subdivides pays the carrier's reasonable costs** of moving a facility the carrier thinks the subdivision makes necessary (cl 53): the one place Schedule 3 makes the landholder liable. Asserted.

## Raised in the ledger

Nothing raised. The Telecommunications Code of Practice (objections) and the Low-impact Facilities Determination would turn two inputs into computed answers; they could be raised as `no-source` entries if a scenario asks.

## Links

- `../baseline-2026-10/` — Part 19 (the end-user's connection and damages), the other encoding of this Act.
- Source: `../../registers/source-bundle/C2004A05145.txt`, `C2004A05145.meta.json`; licence `SOURCE-LICENSE.md`.

## What would need doing before this is worth relying on

- An independent test pass, and a lawyer's view on forks F1–F5.
- The Code of Practice and the Low-impact Facilities Determination deposited, and the objection procedure encoded beside cl 17.
- A business-day calculator over a deposited public-holiday calendar, so that the person can give dates rather than counts.
- The limitation periods that govern cl 42 claims in each State and Territory, as links to their encodings.
- cl 54 (service by newspaper), so that "given notice" can be worked out where the carrier could not find or serve the owner.
