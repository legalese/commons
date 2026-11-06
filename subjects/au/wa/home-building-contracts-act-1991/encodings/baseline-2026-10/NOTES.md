# Home Building Contracts Act 1991 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual the law is applied to. It follows the design defaults ruled on 2026-10-18. It uses no REFUSE. It was checked with the stable `l4` from VS Code extension 1.6.98.

There was no pipeline, no coverage table, no independent test pass and no human gate. Not for public use as advice.

There was no earlier encoding of this Act to replace.

Every question is exported for Legalese Cloud with `@export` and `@desc` (29 questions).

Files:

- `hbc-contracts.l4`: which contracts the Act covers, what the contract must contain, the deposit cap and progress payments, termination, variations, the building permit condition, the fixed price and price rises, defects, inspection, contracting out, home indemnity insurance, and the complaint time limits.
- `hbc-cases-contracts.l4`: built by the scratchpad generator `gen_wa_home-building-contracts-act-1991_baseline.py`.

## Edition

- **The Act.** The compilation of the Home Building Contracts Act 1991 (No. 61 of 1991) deposited at `../../registers/source-bundle/mrdoc_45904.txt` (legislation.wa.gov.au mrdoc 45904, retrieved 2026-09-07). The deposit gives no compilation number or date. Its compilation table ends with the Directors' Liability Reform Act 2023 Pt. 3 Div. 34, in operation 5 Apr 2023.
- **The Regulations.** The Home Building Contracts Regulations 1992, version 03-k0-00, currency from 1 Sep 2025, deposited at `../../../home-building-contracts-regulations-1992/registers/source-bundle/mrdoc_48796.txt` (mrdoc 48796, retrieved 2026-10-20). Used:
  - r 2A: the s 3 thresholds become $7,500 and $500,000 (the Act's text says $6,000 and $200,000);
  - r 3 and Schedule 1: the Notice for the Home Owner, which is also the only source used for the complaint time limits;
  - r 3A: a 20% deposit for cabinetry work more than half off-site;
  - r 5: a $500 maximum excess;
  - r 7: the s 25A minimum amount becomes $20,000 (the Act says $10,000);
  - r 7A: deposit cover becomes $40,000 (the Act says $20,000);
  - r 7B: minimum cover becomes $200,000 (the Act says $100,000).

Working days and months are counts the owner states; the encoding does no calendar arithmetic.

## Checks

One case file, **50 assertions satisfied**, 0 errors, 0 warnings, with the stable `l4` (VS Code extension 1.6.98). The module alone also checks with no errors or warnings.

A copy with one expected value altered (the c051 deposit cap, $22,100 to $22,000) was run as a control. The runner reported the failures.

## Seat

**The home owner contracting a builder**: the "owner", "the person for whom ... home building work is to be performed under the contract" (s 3(1)).

The life event asks, in the owner's words, "What must my building contract contain, and must I be insured?" Most of the Act is addressed to the builder: it must ensure the contract is written and signed (s 4(4)), must not take more than the capped deposit (s 10), must not include a rise-and-fall clause (s 13), and must insure the work (s 25C). Each is encoded as what it means for the owner: whether the contract is covered, what may be asked of the owner and when, whether the owner may end the contract, and what the insurance gives the owner.

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers.** Followed. The Regulations are deposited and override five of the Act's own figures (see Edition).
- **The actors the text names.** Followed: the owner, the builder, the insurer, the Minister (exemption periods, as a fact) and the Building Commissioner (complaints).
- **A judgment handed to someone else is answered conditionally.** Followed. These are facts:
  - whether a stage payment has been shown not to be a genuine progress payment (s 10(3));
  - whose failure meant the building permit was late (s 9(2), Schedule 1);
  - whether a failure is a "defect" (s 11(2));
  - whether a variation was caused by unforeseeable circumstances (s 8(1)(b)).
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out: home building work contract (s 3 with r 2A); residential building work and cost of the building work (s 25A with r 7); developer (s 25A).
  - Asked as facts: cost plus contract (whether the price is undetermined); whether a building permit is required (Building Act 2011); whether the work is a prescribed building service (Building Services (Registration) Act 2011); whether a Minister's exemption order is running (s 25I).
- **One case is the text's natural unit.** Followed: one contract between the owner and a builder.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words.
- **Operative sections in; machinery out.** Followed. Out: approved-fund approval, review, regulations, retrospectivity, prosecutions and infringement notices.

**Departure.** The complaint itself is made under the Building Services (Complaint Resolution and Administration) Act 2011, which is not encoded. Its time limits (3 years for a contract dispute, 6 years for building standards) are read only from the prescribed notice in Schedule 1 to the Regulations. They are what the owner is told, not the operative rule.

## The lives

| Event | Decision asked | Answer in the encoding |
|---|---|---|
| Chloe **c051** (2028-02-20), Byford house-and-land package, $620,000, with Liam | `Is my contract a home building work contract`, `Is my contract made as the Act requires`, `Must I be given the notice before I sign`, `What is the most deposit my builder may take`, `Must my builder insure my work`, `Must I get the insurance certificate before any payment`, `How much must the insurance cover me for`, `How much of my deposit is insured` | Covered by Part 2; notice required before signing; deposit at most **$22,100**; insurance required, certificate before any payment, cover at least **$200,000**, deposit insured in full |

These are **assumed**, and labelled as such in the generator:

- the package split: land $280,000 and building contract $340,000, the same split as the WA First Home Owner Grant baseline uses;
- the builder's deposit at the full 6.5% ($22,100).

The scenario's "five per cent deposit" is the home-loan deposit under the Home Guarantee Scheme. It is not the builder's deposit, and this Act does not touch it.

## Why this scope

The scope is what the event asks, plus what any owner signing a building contract meets:

- whether the contract is covered;
- what it must contain;
- how much may be paid, and when;
- how it may be varied or its price raised;
- the permit condition;
- defects;
- insurance;
- how to end the contract and when to complain.

Unconscionable and misleading conduct (ss 15, 15A) are left out because each is a judgment for the Building Commissioner or the Tribunal on a complaint, and would reduce to a single fact. Prime cost items (s 12) turn on what an item "could reasonably cost", the same kind of judgment. Owner-builders (Part 3A Division 3) are a different seat.

## What the Act turns out to say

1. The Act's own text puts contracts of $200,000 or more outside Part 2, but r 2A raises that to $500,000 and the floor from $6,000 to $7,500. So a contract is covered only if its stated amount is more than $7,500 and less than $500,000. Asserted.
2. Home indemnity insurance has no upper limit. A $550,000 build is outside Part 2 (no deposit cap, no written-contract rule), but it must still be insured. Asserted.
3. The deposit cap is 6.5% of the contract price (s 10(1)(a)). For cabinetry work more than half done off-site, r 3A allows 20%. Asserted.
4. The owner may end the contract if it is not written, dated and signed (s 4(5)), but not because the Notice for the Home Owner was never given. Section 4(5) reaches only s 4(1); the notice is s 4(3). Asserted.
5. A cost plus contract must be headed and acknowledged as one (s 14(1)). Section 14(2) disapplies that for contracts within para (b) of the definition, so a cost plus contract of $500,000 or more needs neither. Asserted.
6. Termination must be by signed written notice before the work is complete (s 19(2)). Asserted.
7. A variation forced by a written direction or by unforeseeable circumstances escapes the writing-and-signature rule only if the builder gives a statement of reason and cost within 10 working days (s 8(2)). A rise in labour or material costs is never "unforeseeable" (s 8(4)). Asserted.
8. If the owner disputes that circumstances were unforeseeable, the complaint must be made within 10 working days of the statement (s 8(3)). Asserted.
9. The price is fixed: a rise-and-fall clause is void (s 13(2)). Rises are allowed for a new law, a tax rise after the contract, or a start delayed over 45 working days by the owner or by no-one (s 13(4)). The owner may end the contract within 10 working days if such a rise exceeds 5% of the price, but must pay the builder's reasonable costs (Schedule 1 cl 4). Asserted.
10. If the building permit is not granted within 45 working days, the contract stays in force either way. If the builder alone is at fault, the price stays put; otherwise the builder may raise it (Schedule 1 cll 1-3). The condition does not apply to associated work alone (s 9(5)(b)). Asserted.
11. Defects must be notified in writing within 4 months of practical completion, or a longer period in the contract (s 11). Asserted.
12. Insurance is needed only above $20,000 (r 7), only where a building permit is needed and the work is a prescribed building service (s 25B(4A)), and not for associated work alone. Asserted, except the associated-work exclusion, which is encoded but not asserted.
13. The certificate must reach the owner before the builder demands any payment, deposit included (s 25C(2)). Asserted.
14. Cover must be at least the lesser of $200,000 and the cost of the work (r 7B). Deposit loss is covered up to $40,000 (r 7A), but not for a developer of 4 or more homes or under a cost plus contract. Claims may be made for 6 years after practical completion (s 25D(1)(d)), and the excess can be at most $500 (r 5). Asserted, except the developer and cost plus exclusions, which are encoded but not asserted.
15. The Act still prints $6,000, $200,000, $10,000, $20,000 and $100,000. All five are displaced by regulation. Anyone reading the Act alone gets every one of them wrong.

## What would need doing before this is worth anything

- A coverage table and an independent test pass.
- The Building Services (Complaint Resolution and Administration) Act 2011, so that complaints and their time limits come from the operative text rather than the notice.
- Sections 15 and 15A as conditional questions, if Legalese Studio's design wants them.
- Transportable dwellings (ss 10(2), 25D(2), (3)) and owner-builders (Part 3A Division 3).
- A calendar for working days (public holidays by area), so that deadlines can be dates rather than counts.
- Confirmation of Chloe's package split and builder's deposit from the scenario owner.

## Q&A layer (seat and situations as parameters)

Added 6 November 2026 (batch qa11), following the graffiti model
(`../../../graffiti-vandalism-act-2016/encodings/baseline-2026-10/`, D2, D4, D8). The baseline files are unchanged;
the layer is added beside them: `hbc-qa.l4` (imports `prelude` and `hbc-contracts`) and `hbc-qa-cases.l4`.

### Roles

Every exported question takes `my role` IS A `Role` first ("Which of these describes you"), and answers
`does not arise for you` for a role it is not about without reading any other input.

| Role | Why | Questions |
|---|---|---|
| `I am the home owner having home building work done` | the baseline's seat (s 3(1) "owner") | 29 |
| `I am the builder doing home building work for an owner` | the Act's duties fall on the builder (ss 4, 5, 7, 8, 10, 13, 14, 25C) | 15 |

The Building Commissioner, the State Administrative Tribunal and the insurer are not seats. There are 43 questions;
one (s 11, defects) is asked of both roles.

### Situation inputs

Each is placed straight after `my role`; when it is FALSE the question answers `does not arise for you` and reads
nothing else. A shared input has one name, type and `@desc`.

| Input | Type | Does not arise when | Questions |
|---|---|---|---|
| `the building work has started` | BOOLEAN | FALSE | Once work has started may my builder demand this payment; Once work has started may I demand this payment from the owner |
| `the contract is being varied` | BOOLEAN | FALSE | Must this variation be in writing and signed by me; Was my variation made the way the Act requires; Within how many working days must I dispute the builder's unforeseen circumstances; Must this variation be in writing and signed by the owner; By when must I give the owner my variation statement |
| `the builder wants to raise the price, or has given notice of a rise` | BOOLEAN | FALSE | Can my builder put my price up for this reason; After a notified price rise may I end the contract; May I put the owner's price up for this reason |
| `the owner ended the contract after a notified price rise (Schedule 1 clause 4(b))` | BOOLEAN | FALSE | If I end the contract over a price rise must I pay the builder's reasonable costs; If the owner ends the contract over my price rise must they pay my reasonable costs |
| `the building permit was not granted within 45 working days` | BOOLEAN | FALSE | If the permit is late what happens to my contract; If the permit is late what happens to my contract with the owner |
| `a defect in the work has been found` | BOOLEAN | FALSE | Must the builder make good this defect (both roles) |

### Decisions

- **One `Contract` record for both roles.** The baseline's record speaks as the owner in two fields ("is signed by the
  builder and by me", "I was given the notice before I signed"). It is kept unchanged (layers add, nothing is
  replaced), and its `@desc` here says that "I" and "me" in its fields mean the owner. No builder question reads those
  two fields.
- **The builder's enums.** `Who failed` and `Reason for a price rise` speak as the owner ("me alone", "my failure
  alone"). The builder's s 9 and s 13 questions take builder-worded enums (`Who failed, as the builder sees it`,
  `Reason for my price rise`), mapped value for value to the baseline's by helpers with no OTHERWISE. Mirror cases show
  the builder and the owner get the same answer on the same facts.
- **The s 8(3) days (owner).** The baseline answers 10 for a statement of unforeseen circumstances and 0 otherwise.
  Here the question arises only on such a statement: for the other three causes it answers `does not arise for you`
  instead of 0. This is the one place an owner answer differs in form from the baseline's; where the question arises
  it is the baseline's 10.
- **Kept 0s.** The copy-of-contract days (s 5(3)), the insurance cover, the claim years and the excess answer 0 in the
  baseline where the Act sets nothing for that contract (it does not cover it, or no insurance is required). Whether
  it does is computed from the contract, not a fact the person states, so it is not a situation; the wrapped answers
  keep the 0, and the question texts say "0 if ...".
- **Schedule 1 cl 4(c).** The baseline's input "I terminated under clause 4" is its only input; it is the situation
  here, worded for both roles. Where it holds the answer is the baseline's yes.
- **s 4(1) for the builder** is asked as a duty ("Must my contract be in writing, dated and signed"), answered yes for
  a home building work contract, from the baseline's s 3 rule. s 8's statement time is a helper over the s 8(1), (2),
  (4) text, listing every cause.

### Not covered for the builder

- The builder's offences, fines and infringement notices (ss 30-31B, r 8), as in the baseline.
- Understated prime cost items (s 12), unconscionable or misleading conduct (ss 15, 15A), and the adjustment of rights
  after termination (s 20).
- The builder's own right to terminate (s 19 applies to "a party"), the review of a price rise (Schedule 1 cl 5), and
  the exemption-period notices (ss 25I-25L).
- Whether a progress payment the builder demands was given with the insurance certificate first is asked only as the
  owner's "May my builder ask me for this deposit now".

### Cases

`hbc-qa-cases.l4` has 193 cases, all satisfied:

- 42 ask each question for the role it is not about, with every other input ASSUMEd;
- 16 ask each situation question, for its own roles, with FALSE and the later inputs ASSUMEd;
- 135 are worked by hand from the text; 29 of them assert the owner's answer equal to the baseline export's own on the
  same facts, and 5 are mirror cases between the two roles.

The contracts are the baseline cases' own fixtures, copied unchanged. The role and situation cases are generated from
the exports' parameter lists by a script in the batch's scratch folder, which also checked every export: `my role`
first; each parameter name with one type and one `@desc` across the file; each situation second and read first in
every role branch; no DEONTIC or EVENT input. Two negative controls (a wrong permit outcome for the builder, ASSUMEd
inputs read after a holding situation) failed as they should. All four files of the encoding run with 0 errors and 0
warnings, and `l4 check hbc-qa.l4` succeeds.

### After the independent check (6 Nov 2026)

- **The site's form keeps the questions that take `the contract` open** for the role they are not about, and when
  their situation is FALSE (for example the owner keeps 41 of 43 questions, and "Once work has started may my builder
  demand this payment" stays open with `the building work has started` FALSE).
  - The layer is not wrong here: each of those questions answers `does not arise for you` from `my role` (and its
    situation) alone, and no case or evaluation failed.
  - The cause is the engine. To drop a question it evaluates every combination of its open yes/no and choice inputs, up
    to 1 024 (`PROBE_CAP` in `interact-engine.ts`). `Contract` has 13 yes/no fields and a choice of the kind of work is over that cap by itself, so every question that takes it
    stays open until it is answered.
  - No change to the layer fixes this without changing what is asked: splitting the record into its fields leaves the
    same number of yes/no facts, and narrowing it to what one question reads gives the form a second set of inputs for
    the same facts. The fix belongs in the engine (when over the cap, evaluate one completion with a trace; if it reads
    only answered inputs, the answer holds for every completion), as the Civil Liability Act encoding's notes say.
  No file was changed for this finding.
- **The builder's s 8 answer for a cost rise is corrected.** s 8(4) lets a cost rise alone vary the contract only "in
  accordance with section 7(1) and (2) or 13(4) or clause 4 of Schedule 1"; the answer had named s 7 only. It now has its
  own value, `no s 8 statement: a cost rise alone allows a variation only under s 7(1) and (2) (in writing, signed by the
  owner), s 13(4) or Schedule 1 clause 4`, and its case expects it. An agreed change keeps the s 7 answer.
- **Kept: the owner's s 8(3) question answers does not arise from `the cause`** (any cause but unforeseen
  circumstances), an ordinary input, not a situation input. This is the s 8(3) decision recorded above: what the
  builder's reason is, is one of the facts the question asks, not a situation the person is in. Every value of
  `Cause of the variation` is listed, so the ASSUMEd cases test it.
- The first form-engine run hit the service's "Evaluation resource limit exceeded"; run alone, it completed. That is
  the service's limit on a shared machine, not the layer.
- `hbc-qa-cases.l4` still has 193 cases, all satisfied.
