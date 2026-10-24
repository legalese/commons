# Income Tax Assessment Act 1936, Part VA (tax file numbers) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; the one case outside the encoding answers `not covered`, and a test asserts it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0055` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep.

Every question is a function named as the person starting a job would ask it, with `@export` and a `@desc` on every input, so it can be deployed to Legalese Cloud.

## Edition

The compilation registered as **C2026C00333** (Federal Register of Legislation, retrieved 22 September 2026, seven volumes in one file), as deposited at `../../registers/source-bundle/C1936A00027.txt`. Part VA is at lines 11481–12100 of the deposit.

Nothing else is brought in. The two figures Part VA gives the payer (10 penalty units, ss 202CD and 202CF(3)) are quoted in comments, not computed.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `itaa36-tfn.l4` | `itaa36-cases-tfn.l4` | 51 written, 51 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-22). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The individual starting a job**: Chloe at 15 with a casual supermarket job, Jake at 15 with no job, Daniel at 16 with a casual job. The questions are the ones that person asks: "Do I have to give my employer my TFN?", "How do I get one?", "I've applied but don't have it yet — how long do I have?", "What happens if I don't quote it?".

Most of Part VA is addressed to the Commissioner or the payer. Those provisions are encoded as what they mean for that person: what the Commissioner must do with my application, from when I may treat it as refused, when an interim notice to my employer stands in for my number, by when my employer must send my declaration on, and by when it must tell the Commissioner I made none.

The 2026-10-18 defaults:

- **The Act alone.** Part VA only. No instrument sets a number Part VA needs.
- **The actors the text names:** me (the applicant, the recipient), my payer, the Commissioner, the Tribunal.
- **Judgments handed to others are answered conditionally.** The Commissioner's satisfaction about my identity, about an existing TFN, and the s 202CE notices are asked as facts.
- **The Act's own definitions are worked out from facts:** recipient (s 202A, s 202AA), whether a declaration states my TFN (s 202CB), whether it is in effect (s 202CA). The borrowed term — which payments must be withheld from under Subdivisions 12-B, 12-C, 12-D of Schedule 1 to the TAA — is asked as a fact ("paid wages as an employee").
- **One case:** one person and one payer.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** s 202 (objects), s 202AB, s 202CA(3) as a power (its effect is an input), s 202EH, s 202FA, Division 8.

## Read with the Taxation Administration Act 1953 baseline

`../../../taxation-administration-act-1953/encodings/baseline-2026-10/` answers the parts of c020, k020 and d012 that are in that Act, and they are not restated here:

- s 8C(2): not quoting a TFN is not, by itself, a failure to give information;
- ss 8WA, 8WB: who may ask for my TFN (an employer asking on a TFN declaration commits no offence, because Part VA provides for it) and what they may do with it;
- Schedule 1 s 12-35: tax is withheld from my wages whatever my age and whether or not I quoted a TFN; the amount, including the higher amount where no TFN is quoted, comes from the withholding schedules, which are not deposited.

The stable `l4` cannot IMPORT across encoding folders, so the link is recorded here and in the module header, not in code.

## Scope

**In:** s 202A (recipient, payer, tax file number, TFN declaration, child), s 202AA, s 202B, s 202BA(1)–(3), (5), (6), s 202BC, s 202BD(2), (6), s 202C, s 202CA(1)–(2), s 202CB(1)–(4), s 202CC, s 202CD(1)(b), s 202CE(1)–(3), (6), s 202CF(1), (1A), (3), s 202EA(2), s 202F(1).

**Out:** Division 4 and ss 202EB–202EH (investments, entities, non-residents); Division 8; the alienated personal services limbs of "payer" and "recipient"; s 202BA(4), s 202BB, s 202BE and s 202BF except as decisions to review; s 202CB(5); s 202CB(6)–(8) and s 202CE(7)–(9) (declarations given by a claimant to Centrelink, a Secretary or the Repatriation Commission: `not covered`); s 202CEA; s 202CF(2) (the 2000 transitional notice); s 202CG except as s 202CF(1A); s 202F(2)–(4).

In the s 202CF question, the pension exemption (s 202EA(2)) and the s 202CE notices are not asked: a new employee's declaration is taken on its face there.

## The lives

| Event | Question asked of this Act | Answer in this encoding |
|---|---|---|
| chloe c020, 2018-03-14 | Must a 15-year-old have a TFN? How is it quoted to the supermarket? | No age rule and no duty: she may apply (s 202B) and the Commissioner must issue one once satisfied of her identity (s 202BA(1)). She is a recipient of the supermarket even if nothing is withheld (s 202AA(a)), so she may make a TFN declaration (s 202C(1)) but need not. A declaration saying her application is pending is effective for 28 days (to 16 April 2018 on a hypothetical 19 March start), and for good if she gives the number within them (s 202CB(3)). The supermarket owes no s 202CF notice; with no declaration it must notify the Commissioner by 2 April 2018 |
| jake k020, 2021-08-30 | A TFN at 15 with no job | He may apply, and must be issued a number, with no job (ss 202B, 202BA). With no payer he is no recipient and has no declaration to make. If no decision comes he may treat the application as refused from 28 September 2021 (s 202BC) and seek review (s 202F(1)(a)) |
| daniel d012, 2012-10-15 | A TFN and a casual job at 16 | His declaration stating his number is effective when made; his employer must send it on by 29 October 2012 (s 202CD(1)(b)) and owes no s 202CF notice. On a hypothetical last pay of 28 February 2013 it lapses after 28 February 2014 (s 202CA(1C)) |

**The lives are replayed on the 2026 compilation.** d012 (2012) and c020 (2018) are answered on Part VA as it stands in C2026C00333, not as it stood then (see finding 7). The lives give the event dates and ages only; the job start days, what each declaration said and when a number was passed on are the encoder's, labelled HYPOTHETICAL in the case file.

## What the Act turns out to say

1. **There is no age rule in Part VA.** Section 202A defines "child" as "a person who is less than 16 years of age", but no provision of Part VA in this compilation uses the word. Nothing about applying (s 202B), issue (s 202BA) or declarations (s 202C) turns on age, so a 15-year-old (Chloe, Jake) and a 16-year-old (Daniel) stand where an adult does. No question takes an age. Asserted (c020, k020, d012 cases).
2. **Nothing in Part VA makes the individual get or quote a TFN.** A person "may apply" (s 202B(1)) and a recipient "may make a TFN declaration" (s 202C(1)). Part VA's penalties for the employment side fall on the payer (10 penalty units under s 202CD and s 202CF(3)); the only offences an individual can commit in Part VA concern investments (ss 202EC(4), 202EE(2)), which are out of scope. The cost of not quoting is the higher withholding under the TAA's schedules (see the TAA baseline). Asserted (`Do I have to give this payer my TFN`).
3. **A worker whose pay is too small for any tax to be withheld is still a "recipient".** "Eligible PAYG payment" is a payment from which an amount "must be withheld" under Subdivision 12-B, 12-C or 12-D, but s 202AA(a) treats a nil amount as an amount and s 202AA(c) disregards the exceptions in s 12-1. Asserted (c020).
4. **The 28 days run from the declaration, not from the application, and passing the number on within them keeps the pending statement good for ever.** Section 202CB(3) switches off the pending (or "don't know my number") statement only where the recipient "fails to inform the payer ... within 28 days after making the declaration", and then only "in respect of any time after the end of the period of 28 days". A number given after the 28 days does not revive it: the payer may write a number on only before sending the declaration on (s 202CD(4)), which it must do within 14 days. The way back is a new declaration (s 202CC). Asserted (c020: effective on 1 May 2018 when told on 2 April; ineffective from 17 April when never told, or told on 20 April).
5. **Section 202CF asks whether a declaration is "in effect"; s 202CB(1) says an unquoting declaration "is not effective".** This encoding reads s 202CF as needing a declaration that is both in effect (s 202CA) and effective (s 202CB), so a pending declaration within its 28 days answers s 202CF, and an interim notice without any declaration does not. Asserted (c020 and counterfactuals). An interpretive choice, not tested against any ruling.
6. **The deemed refusal and the interim notice both run 28 days, counted differently.** Under s 202BC(1) the Commissioner has "28 days after the application is made", so the applicant may give notice from the 29th day (Jake: from 28 September 2021). Under s 202BD(2) an interim notice is in force "for the period of 28 days commencing on the day specified", counting that day (20 March to 16 April 2018). While interim notices are in force to every payer named, no deemed refusal is possible (s 202BC(2)), and a further application must be refused (s 202BA(3)(b)). Asserted.
7. **The Tribunal is the Administrative Review Tribunal.** Section 202F now refers to the Administrative Review Tribunal Act 2024. On the lives' own dates (2012, 2018, 2021) review lay to the Administrative Appeals Tribunal; this encoding answers on the 2026 text, as the lives are replayed. A withdrawal and reissue under s 202BF is not reviewable; a refusal (actual or deemed), a cancellation and a s 202CE(3) notice are. Asserted (review cases); the AAT point is not asserted.
8. **The ledger entry's expected answer agrees with the text, with three additions.** The REQ-0055 assertion is borne out. The text adds that issue is subject to s 202BA(3) (an existing TFN or an interim notice in force requires refusal); that a declaration is also taken to state the TFN while an interim notice to the payer is in force (s 202CB(4)), or where it says the person has a number but does not know it (s 202CB(2)(b)), or is a listed pensioner's (s 202EA(2)); and that s 202CF does not apply if the Commissioner disclosed the TFN to the payer within the 14 days (s 202CF(1A)). Asserted.
9. **The lives cite this Act correctly.** The corrected SCENARIO.md tables for c020, k020 and d012 cite "Income Tax Assessment Act 1936 (Cth) (TFNs)" (CORRECTIONS-2026-10-21 Chloe #9, Jake #4, Daniel #4). Nothing in the lives' facts is contradicted by the text. Not asserted (a finding about the citation).

## The formulas sidecar (checked 24 October 2026)

The text deposit lost every formula image of the Act. They are now transcribed in `../../registers/source-bundle/C1936A00027.formulas.md` (128 entries: 109 formulas, 19 pictures; recovered 2026-10-24). This encoding was checked against it, and nothing changes:

- **Part VA has no formula.** No entry falls in ss 202 to 202F, and no rule here takes as an input, or answers `not covered` for, anything a formula gives.
- **No Part III offset or Part VIIB Medicare formula.** The sidecar has none in Part III's offsets (s 159N-type and s 160AAAA rebates) or in Part VIIB: those provisions are in words, and the deposit kept them.
- **No other encoding takes an amount these formulas give.** The Medicare Levy Act, the Medicare levy surcharge (fringe benefits) Act, the Rates Act and the FBT Act encodings borrow the 1936 Act's terms ("married", "dependant", "resident", "associate", s 160AAAA) as facts. None uses a formula.

Formulas an individual meets, for when this encoding is extended beyond Part VA:

- s 23AG(3), (4): tax on other income when overseas employment income is exempt;
- s 27H(2): the deductible amount of an annuity;
- s 82KZM(1)(c)(ii): spreading prepaid expenditure;
- s 26AJ(2)(d): investment-related lottery winnings;
- s 156(5)(b): the primary producer averaging rebate of a trustee.

## What would need doing before this is worth relying on

- **The withholding schedules** under TAA Schedule 1 s 15-25, including the no-TFN amount, so the cost of not quoting can be computed. No ledger entry yet names them.
- **Earlier compilations** of Part VA for 2012 and 2018, if the lives are to be answered on the law then in force.
- **The approved forms** (the TFN application and the TFN declaration) are not law and were not read; what they require as proof of identity is the Commissioner's.
- **Wider sources.** No ATO ruling, guidance or case law was read; finding 5 is an interpretive choice.
- **Division 4** (quoting a TFN to a bank or other investment body), if a life asks — Jake's or Chloe's first bank account would.
