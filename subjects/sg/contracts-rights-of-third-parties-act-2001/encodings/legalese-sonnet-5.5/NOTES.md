# Contracts (Rights of Third Parties) Act 2001 (Singapore) — encoding `legalese-sonnet-5.5`

Status: `draft`.
No domain expert has read this against the text.
Target compiler: `main`.
Compiled against `1.6.109 (main, 4c887e0, 2026-11-04)`, compared with `1.6.108 (main, 2ae7c9b, 2026-11-02)`.
Written by a single Sonnet 5.5 agent working alone from the brief in `BRIEF.md` (a copy of the brief is beside this file), on 2026-11-05.

## Method

- The Act has no Parts and no Schedules, so layer 1 follows its nine sections: one module for each of sections 1, 2, 3, 4, 7, 8 and 9, one for sections 5 and 6 together, a nouns module, a three-valued helper module, and one hand-gathered module (`crtpa-enforce.l4`, ruling E1 option B, see the fork register).
- Layer 1 is written from the text alone, in the Act's order.
  Every rule carries `@ref` and a quotation copied from the text file by `srcrefs.py quote`, never retyped.
- Every rule in layer 1 has a test file (`crtpa-test-*.l4`) whose expected values were written from the text, with the reason beside each, before the module was run.
- Layer 2 is `crtpa-seat.l4` (the questions) and `crtpa-cases-seat.l4` (worked cases), both written for the seat below.
  Both files were produced by small scripts kept in the author's scratchpad; the generated L4 is the artefact, and the scripts are not part of this deposit.
- The coverage table below was built by `coverage.py` (in this folder; run `python3 -I coverage.py CRTPA2001.txt . --md`) from the text file: it scans the text for its units, holds one row per unit, and fails if a non-blank line is in no row, if a unit it found is in no row, if a row claims a unit it did not find, or if a rule named in a row does not exist.
- Reuse: the two Interpretation Act modules staged for this text are copied unchanged and imported by name (see `## Dependencies`).
- Edition encoded: Contracts (Rights of Third Parties) Act 2001, 2020 Revised Edition, informal consolidation from Singapore Statutes Online (retrieved 2026-10-01; the text file's own front matter says the revised edition "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021", `CRTPA2001.txt` lines 6-7).
- The text file is a plain-text rendering made by a converter script.
  It is not the official text, and nothing here is "verified against the official text".

## Seat

**The seat: a person who is not a party to a contract but is named in it or benefits from it, asking on facts they can state whether they may enforce a term, whether the parties may still vary or cancel it, and what defences the promisor has.**

Why this seat: the Act exists to give such a person a right (s 2(1)), protect it from being cancelled behind their back (s 3), and say what the promisor can set up against it (s 4).
The Guide (section 2) requires a seat for the individual to whom the law is applied, and the third party is that individual; the brief names this seat.

Defaults followed: every question is phrased as that person asks it ("May I ...?", "Am I ...?", "Must the court ... reduce my award?"); every input is a fact the person can state, or a judgment they may answer "I am not sure"; the court and the arbitral tribunal appear only for what they mean to the person (their consent dispensed with, conditions imposed, their award reduced); there is no seat for an official.
Departures: none that I know of.
A few questions (s 2(7), s 7(6), s 7(7)) ask about "the party I am asking about", "this Convention" or "this document" because the Act's own words define those terms in neutral language; they are still asked of the person in the seat.
No second seat (the promisor, the promisee) was written: the brief fixes one seat, and the promisor's and promisee's positions appear in layer 1 as the bearers of the correlative duties in the table below.

Layer 2 is 58 questions in `crtpa-seat.l4`, each with `@export` and an `@desc` on every input, grouped under `§§` headings in the Act's order, and 185 case assertions in `crtpa-cases-seat.l4` (at least one case for every question, and 19 cases marked `OUTSIDE THE ENCODING`, each asserted as `NOTHING`, where the text stops answering).

## What is encoded and what is not

- Every provision of the text is in the coverage table with one disposition.
  The operative text (ss 1 to 9) is encoded or flagged as a fork; the rest (title page, arrangement of sections, long title, headings, the Act's own commencement and short title, the legislative history, abbreviations and comparative table, page furniture) is inert for reason 1 or 2.
  Nothing is `repealed`, `out-of-scope` or `deferred`.
- 74 section-named rules in layer 1, plus the nouns and three-valued helper modules and the hand-gathered route.
- Regulative rules, where the text names the bearer and states a duty, permission or prohibition: `s 3(1) ... SHANT`, `s 3(4) ... MAY`, `s 4(6) ... SHANT`, `s 6 ... MUST`.
  The text gives no deadline for any of them, so none has a `WITHIN` (an assumption stated in the fork register, G32).
- What is not encoded because the Act itself does not say it: what other laws provide (the Limitation Act 1959 period, the Unfair Contract Terms Act 1977, the Bills of Lading Act 1992, the Carriage by Air Act 1988, the Companies Act 1967 and the Limited Liability Partnerships Act 2005 as the Act cites them), the Minister's orders under s 7(6)(b) and (c), and the court's or tribunal's judgments (satisfaction under s 3(4) and (5), the extent of a reduction under s 6).
  Each is an input that the person states, asked as a fact, and answers `NOTHING` when not stated (findings F13 to F17).

### Reading a result: FALSE and NOTHING

Every decision function in layer 1 returns a three-valued answer.
**`JUST TRUE`** is an answer the Act gives: the thing holds, on these facts.
**`JUST FALSE`** is "the Act says no to this case in its own words", and means exactly that and no more.
In particular it never means "the promisor has no defence at all" or "the contract has no other force": a `JUST FALSE` from a rule about one defence, one exception or one route means that rule gives the person nothing on these facts, and s 8(1) preserves every right or remedy that exists apart from the Act.
**`NOTHING`** is "the Act does not answer on these facts": it is silent, lists without closing the list, leaves a term undefined, points outside the sources (another Act, an order, a court's judgment), or limits a grant or a prohibition in its own wording and the case falls outside the limit.
Never read `NOTHING` as no; never turn it into `FALSE` in a caller.
Where a result is a number, a date, a choice from a list or an Act and so cannot carry `JUST FALSE`, a yes/no twin carries the "no" and the value function answers `NOTHING` (assumed, not ruled).

The rulings of 2026-10-29, 2026-11-04 and 2026-11-05 decide which words count as a "no": a definition that says "means"; an "if", "only if", "unless" or "until" the text introduces; a list closed with "only"; a flat negative ("does not", "may not", "must not be refused"); a "where" that is not met; a period the text fixes; and, for defences, a defence the text hands to a fact that is not proved.
Everything else is `NOTHING`.
Two readings that a lawyer should confirm are listed in `## Marginal readings for a lawyer`.

## Jural relations

Hohfeld kinds: claim ↔ duty; privilege ↔ no-right; power ↔ liability; immunity ↔ disability.
The kinds are recorded here only, not in the person-facing answers (ruling N2).
Where the text names the bearer of a prohibition, the prohibition is derived as a `SHANT` rule from the same answer.

| Provision | Kind | Holder | Correlative (bearer) | L4 rule |
| --- | --- | --- | --- | --- |
| s 1(1) short title | none | | | |
| s 1(2), (3) which contracts the Act reaches | none (a rule of application) | | | `s 1(2) the restriction on the application of this Act applies to the contract` |
| s 2(1) the third party may enforce a term | claim (and power to sue on it) | the third party | the promisor (duty to perform the term for the third party) | `s 2(1) the third party may in the third party's own right enforce the term of the contract` |
| s 2(1)(a), (1)(b), (2), (3), (4) the conditions of that right | none (conditions of the s 2(1) claim) | | | `s 2(1)(a) ...`, `s 2(1)(b) ...`, `s 2(2) ...`, `s 2(3) ...`, `s 2(4) ...` |
| s 2(5) remedies | claim to the remedy; immunity from refusal as a volunteer | the third party | the promisor (duty); the promisor and the court (disability to refuse on that ground) | `s 2(5) the remedy is available to the third party`, `s 2(5) the remedy may be refused on the ground that, as against the promisor, the third party is a volunteer` |
| s 2(6), (7) reading rule and definitions | none | | | `s 2(6) ...`, `s 2(7) ...` |
| s 3(1) no rescission or variation without consent | immunity (and derived prohibition) | the third party | the parties to the contract (disability; SHANT) | `s 3(1) the parties to the contract may not rescind or vary the contract without the third party's consent`, `s 3(1) the parties to the contract SHANT rescind or vary the contract without the third party's consent` |
| s 3(2) the assent | none (form and timing of the assent) | | | `s 3(2)(a) ...`, `s 3(2)(b) ...` |
| s 3(3) express term of the contract | privilege (where the contract so provides) | the parties to the contract | the third party (no-right) | `s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account` |
| s 3(4), (5) dispensing with consent | power | the court or arbitral tribunal | the third party (liability to have the consent dispensed with) | `s 3(4) the court or arbitral tribunal may dispense with the third party's consent`, `s 3(4) the court or arbitral tribunal MAY dispense with the third party's consent`, `s 3(5) ...` |
| s 3(6) conditions on dispensing | power | the court or arbitral tribunal | the third party and the parties (liability to the conditions, including compensation) | `s 3(6) ...` (two rules) |
| s 3(7) which courts | power (jurisdiction) | the General Division of the High Court and a District Court | the parties and the third party (liability) | `s 3(7) the jurisdiction conferred on the court by subsections (4), (5) and (6) is exercisable by this body` |
| s 4(1) when s 4 applies | none | | | `s 4(1) subsections (2) to (5) apply` |
| s 4(2), (3), (4) defences, set-off, counterclaim | privilege | the promisor | the third party (no-right to stop the promisor relying on the matter) | `s 4(2) ...`, `s 4(3) ...`, `s 4(4)(a) ...`, `s 4(4)(b) ...` |
| s 4(5) express term | none (the contract's own term limits (2) and (4)) | | | `s 4(5) subsections (2) and (4) are subject to an express term of the contract that takes the matter away` |
| s 4(6) third party sued | duty (derived prohibition) | the third party (SHANT) | the party who sued the third party (claim) | `s 4(6) the third party may not enforce the term in proceedings brought against the third party`, `s 4(6) the third party SHANT enforce the term in proceedings brought against the third party` |
| s 5 the promisee's right | immunity | the promisee | the third party and s 2 (disability to alter it) | `s 5 section 2 affects a right of the promisee to enforce a term of the contract` |
| s 6 double liability | duty (MUST) | the court or arbitral tribunal | the promisor (claim to the reduction) | `s 6 the court or arbitral tribunal must reduce any award to the third party`, `s 6 the court or arbitral tribunal MUST reduce any award to the third party`, `s 6 the award to the third party after the reduction` |
| s 7(1) to (5) exceptions | disability (no right in these contracts) | the third party | the contracting parties (immunity from the third party's claim) | `s 7(1) ...` to `s 7(5) section 2 confers a right on the third party in the case of the contract` |
| s 7(5) exception to the exception | privilege | the third party (to avail of an exclusion or limitation) | the person who would resist it (no-right) | `s 7(5) the third party may in reliance on section 2 avail of an exclusion or limitation of liability in the contract` |
| s 7(6), (7) definitions | none | | | `s 7(6) ...` (two rules), `s 7(7) ...` |
| s 8(1) rights apart from the Act | immunity | the third party | the promisor and s 2 (disability) | `s 8(1) section 2 affects a right or remedy of the third party that exists or is available apart from this Act` |
| s 8(2), (3) other Acts | none (switch-off and extension of other Acts) | | | `s 8(2) ...`, `s 8(3) ...` |
| s 8(4) not a party for other written law | immunity | the third party | any other written law's operation (disability) | `s 8(4) the third party is treated as a party to the contract for the purposes of any other written law` |
| s 9(1), (2) arbitration | power (to take part as a party) | the third party | the promisor (liability to be arbitrated against) | `s 9(1) the third party is treated as a party to the arbitration agreement`, `s 9(2) the third party is treated as a party to the arbitration agreement` |
| back matter (legislative history, abbreviations, comparative table) | none | | | |

## Coverage

```
coverage rows: 129 hand rows + 12 automatic page-furniture rows = 141
  encoded              82
  fork                 7
  inert (reason 1)     50
  inert (reason 2)     2
text units the scan counted: 111 (sections 9, subsections+paragraphs 69, defined terms 11, history items 5, abbreviations 12, comparative-table rows 5)
non-blank lines of the text: 343; covered by some row: 343
rules named in the table: 74 distinct, all defined
```

Dispositions: `encoded` is a rule, definition or table in layer-1 L4 with a test and `@ref`; `fork` is a site that can be read two or more ways, with the fork-register entry named; `inert, reason 1` is not operative (title, headings, table of contents, legislative history, abbreviations, comparative table, page furniture); `inert, reason 2` is machinery (the short title, s 1(1), and the Act's own commencement date); nothing is `repealed or blank`.
A bracketed label after `encoded`, such as `(M5)`, names a marginal reading in `## Marginal readings for a lawyer`; the row is still encoded.

The table was built after layer 1 was written, not before it (the skill's step 3 says before), so no row was ever `deferred`.
Enumerating the rows for the table surfaced one provision that had no rule: the parenthesis of s 2(5) ("and the rules relating to damages, injunctions, specific performance and other remedy apply accordingly"), which was quoted under the rule for s 2(5) but not encoded.
It got its own rule before the script's first run (`s 2(5) the rules relating to damages, injunctions, specific performance and other remedy apply to the third party's remedy accordingly`), with three tests and a seat question, and it is row S02-5b.
That row was never `inert`, so no row moved out of `inert`; the first run of `coverage.py` gave the 141 rows below, and the scan found 111 units.
Rows left `inert`: 2 with reason 2 (T04, S01-1) and every other `inert` row with reason 1; the list is in the table.

| Row | Lines | Provision | What the text says | Disposition | Encoded by |
| --- | --- | --- | --- | --- | --- |
| T01 | 1-18 | front matter | title page, edition statement, publisher | inert, reason 1 |  |
| T02 | 19-29 | arrangement of sections | table of contents (headings of ss 1 to 9) | inert, reason 1 |  |
| T03 | 31-32 | long title | "An Act to make provision for the enforcement of contractual terms by third parties." | inert, reason 1 |  |
| T04 | 34 | commencement date | "[1 January 2002]", the Act's own commencement | inert, reason 2 |  |
| S01 | 36 | s 1 heading | Short title and application | inert, reason 1 |  |
| S01-1 | 37-39 | s 1(1) | short title | inert, reason 2 |  |
| S01-2 | 41-43 | s 1(2) | the Act does not apply to a contract entered into before the end of the 6 months from 1 January 2002 | fork G1,G2 | `s 1(2) the last day of the period of 6 months from 1 January 2002, as the Interpretation Act counts it`<br>`s 1(2) the contract was entered into before the end of the period of 6 months from 1 January 2002`<br>`s 1(2) the restriction on the application of this Act applies to the contract`<br>`s 1(2) this Act applies in relation to the contract` |
| S01-3 | 45-46 | s 1(3) | the restriction does not apply to a contract which (a) and (b) | encoded | `s 1(3) the restriction in subsection (2) does not apply in relation to the contract` |
| S01-3a | 48 | s 1(3)(a) | entered into on or after 1 January 2002 | encoded | `s 1(3)(a) the contract is entered into on or after 1 January 2002` |
| S01-3b | 50 | s 1(3)(b) | expressly provides for the application of this Act | encoded | `s 1(3)(b) the contract expressly provides for the application of this Act` |
| P01 | 52-57 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S02 | 59 | s 2 heading | Right of third party to enforce contractual term | inert, reason 1 |  |
| S02-1 | 61-63 | s 2(1) | a person who is not a party may, in the third party's own right, enforce a term if (a) or (b); "Subject to the provisions of this Act" | encoded | `s 2(1) the third party may in the third party's own right enforce the term of the contract`<br>`ss 1, 2 and 7 taken together the third party may enforce the term of the contract` |
| D01 | 62 | s 2(1) "third party" | defined term: a person who is not a party to a contract | encoded | `s 2(1) the person is a third party` |
| S02-1a | 65 | s 2(1)(a) | the contract expressly provides that the third party may | encoded | `s 2(1)(a) the contract expressly provides that the third party may enforce the term` |
| S02-1b | 67-68 | s 2(1)(b) | subject to (2), the term purports to confer a benefit on the third party | encoded (M1) | `s 2(1)(b) the term purports to confer a benefit on the third party and subsection (2) does not take it out` |
| S02-2 | 70-72 | s 2(2) | (1)(b) does not apply if the parties did not intend the term to be enforceable | encoded (M2) | `s 2(2) subsection (1)(b) does not apply to the term` |
| S02-3a | 74-75 | s 2(3) (first limb) | the third party must be expressly identified by name, as a member of a class or as answering a particular description | fork QB | `s 2(3) the third party is expressly identified in the contract by name, as a member of a class or as answering a particular description` |
| S02-3b | 76 | s 2(3) (second limb) | but need not be in existence when the contract is entered into | encoded | `s 2(3) the third party must be in existence when the contract is entered into` |
| S02-4 | 78-80 | s 2(4) | no right to enforce otherwise than subject to and in accordance with any other relevant terms | encoded | `s 2(4) section 2 confers a right on the third party to enforce the term otherwise than subject to and in accordance with the other relevant terms of the contract` |
| S02-5a | 82-85 | s 2(5) (remedies) | any remedy that would have been available in an action for breach of contract is available to the third party | encoded | `s 2(5) the remedy is available to the third party` |
| S02-5b | 86-87 | s 2(5) (parenthesis) | the rules relating to damages, injunctions, specific performance and other remedy apply accordingly | encoded | `s 2(5) the rules relating to damages, injunctions, specific performance and other remedy apply to the third party's remedy accordingly` |
| S02-5c | 87-89 | s 2(5) (volunteer) | such remedy must not be refused on the ground that the third party is a volunteer | encoded | `s 2(5) the remedy may be refused on the ground that, as against the promisor, the third party is a volunteer` |
| S02-6 | 91-94 | s 2(6) | where a term excludes or limits liability, enforcing means availing of the exclusion or limitation | encoded | `s 2(6) references in this Act to the third party enforcing the term are to be construed as references to availing of the exclusion or limitation`<br>`s 2(6) what a reference to the third party enforcing the term is construed as` |
| S02-7 | 96-97 | s 2(7) | in relation to a term enforceable by a third party: promisee and promisor | encoded | `s 2(7) the party is the promisee`<br>`s 2(7) the party is the promisor` |
| D02 | 99-100 | s 2(7) "promisee" | defined term: the party by whom the term is enforceable against the promisor | encoded | `s 2(7) the party is the promisee` |
| D03 | 102-103 | s 2(7) "promisor" | defined term: the party against whom the term is enforceable by the third party | encoded | `s 2(7) the party is the promisor` |
| P02 | 104-106 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S03 | 108 | s 3 heading | Variation and rescission of contract | inert, reason 1 |  |
| S03-1 | 110-115 | s 3(1) | the parties may not, by agreement, rescind or vary so as to extinguish or alter the third party's entitlement without consent if (a), (b) or (c) | encoded (M5) | `s 3(1) the parties to the contract may not rescind or vary the contract without the third party's consent`<br>`s 3(1) one of the circumstances in (a), (b) and (c) exists`<br>`s 3(1) the parties to the contract SHANT rescind or vary the contract without the third party's consent` |
| S03-1a | 117-118 | s 3(1)(a) | the third party has communicated assent to the term to the promisor | encoded | `s 3(1)(a) the third party has communicated the third party's assent to the term to the promisor` |
| S03-1b | 120-122 | s 3(1)(b) | the promisor is aware that the third party has relied on the term (knowledge of the precise terms no condition) | encoded | `s 3(1)(b) the promisor is aware that the third party has relied on the term`<br>`s 3(1)(b) and (c) knowledge of the precise terms of the term is a condition` |
| S03-1c | 124-127 | s 3(1)(c) | the promisor can reasonably be expected to have foreseen reliance, and the third party has in fact relied | encoded | `s 3(1)(c) the promisor can reasonably be expected to have foreseen that the third party would rely on the term and the third party has in fact relied on it` |
| S03-2 | 129 | s 3(2) | the assent mentioned in subsection (1)(a) | encoded | `s 3(2)(a) the assent may be by this form` |
| S03-2a | 131 | s 3(2)(a) | may be by words or conduct | encoded | `s 3(2)(a) the assent may be by this form` |
| S03-2b | 133-135 | s 3(2)(b) | if sent by post or other means, is not regarded as communicated until received (an "until" bar, ruling (d)) | encoded (M6) | `s 3(2)(b) the assent cannot yet be regarded as communicated to the promisor`<br>`s 3(2)(b) the assent has been communicated to the promisor` |
| S03-3 | 137-138 | s 3(3) | subsection (1) is subject to any express term of the contract under which (a) or (b) | fork M3 | `s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account` |
| S03-3a | 140-141 | s 3(3)(a) | the parties may by agreement rescind or vary without the third party's consent | fork M3 | `s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account` |
| S03-3b | 143-145 | s 3(3)(b) | the consent is required in circumstances specified in the contract instead of those in (1)(a), (b), (c) | encoded | `s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account` |
| S03-4 | 147-150 | s 3(4) | where consent is required under (1) or (3), the court or tribunal may, on the parties' application, dispense with it if satisfied that (a) or (b) | encoded (M5, M7) | `s 3(4) the court or arbitral tribunal may dispense with the third party's consent`<br>`s 3(4) the court or arbitral tribunal MAY dispense with the third party's consent` |
| S03-4a | 152-153 | s 3(4)(a) | the consent cannot be obtained because the third party's whereabouts cannot reasonably be ascertained | encoded | `s 3(4) the court or arbitral tribunal may dispense with the third party's consent` |
| P03 | 155-158 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S03-4b | 160-161 | s 3(4)(b) | the third party is mentally incapable of giving consent | encoded | `s 3(4) the court or arbitral tribunal may dispense with the third party's consent` |
| S03-5 | 163-167 | s 3(5) | the court or tribunal may dispense with a consent required under (1)(c) if satisfied reliance cannot reasonably be ascertained | encoded (M5, M7) | `s 3(5) the court or arbitral tribunal may dispense with a consent that may be required under subsection (1)(c)` |
| S03-6 | 169-171 | s 3(6) | on dispensing with consent the court or tribunal may impose such conditions as it thinks fit, including compensation | encoded (M5) | `s 3(6) the court or arbitral tribunal may impose such conditions as it thinks fit`<br>`s 3(6) the court or arbitral tribunal may impose a condition requiring the payment of compensation to the third party` |
| S03-7 | 173-175 | s 3(7) | the jurisdiction is exercisable by both the General Division of the High Court and a District Court | encoded | `s 3(7) the jurisdiction conferred on the court by subsections (4), (5) and (6) is exercisable by this body` |
| P04 | 177 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S04 | 179 | s 4 heading | Defences, etc., available to promisor | inert, reason 1 |  |
| S04-1 | 181-183 | s 4(1) | subsections (2) to (5) apply where proceedings are brought by a third party in reliance on section 2 | encoded | `s 4(1) subsections (2) to (5) apply` |
| S04-2 | 185-186 | s 4(2) | the promisor has available, by way of defence or set-off, any matter that (a) and (b) | encoded (M8) | `s 4(2) the matter is available to the promisor by way of defence or set-off`<br>`s 4(2), (3) and (4)(a) taken together the matter is available to the promisor by way of defence or set-off` |
| S04-2a | 188-189 | s 4(2)(a) | arises from or in connection with the contract and is relevant to the term | encoded (M8) | `s 4(2) the matter is available to the promisor by way of defence or set-off` |
| S04-2b | 191-193 | s 4(2)(b) | would have been available if the proceedings had been brought by the promisee | encoded (M8) | `s 4(2) the matter is available to the promisor by way of defence or set-off` |
| S04-3 | 195-196 | s 4(3) | the promisor also has available, by way of defence or set-off, any matter if (a) and (b) | encoded (M5) | `s 4(3) the matter is available to the promisor by way of defence or set-off because an express term provides for it` |
| S04-3a | 198-200 | s 4(3)(a) | an express term of the contract provides for it to be available in proceedings brought by the third party | encoded | `s 4(3) the matter is available to the promisor by way of defence or set-off because an express term provides for it` |
| S04-3b | 202-204 | s 4(3)(b) | it would have been available if the proceedings had been brought by the promisee | encoded | `s 4(3) the matter is available to the promisor by way of defence or set-off because an express term provides for it` |
| P05 | 205-207 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S04-4 | 209 | s 4(4) | the promisor also has available (a) by way of defence or set-off and (b) by way of counterclaim | encoded | `s 4(4)(a) the matter is available to the promisor by way of defence or set-off as it would have been against a party`<br>`s 4(4)(b) the matter is available to the promisor by way of counterclaim as it would have been against a party` |
| S04-4a | 211 | s 4(4)(a) | by way of defence or set-off any matter | encoded (M8) | `s 4(4)(a) the matter is available to the promisor by way of defence or set-off as it would have been against a party` |
| S04-4b | 213-214 | s 4(4)(b) | by way of counterclaim any matter not arising from the contract | encoded (M8) | `s 4(4)(b) the matter is available to the promisor by way of counterclaim as it would have been against a party` |
| S04-4c | 216-218 | s 4(4) (tail) | that would have been available against the third party if the third party had been a party to the contract | encoded | `s 4(4)(a) the matter is available to the promisor by way of defence or set-off as it would have been against a party`<br>`s 4(4)(b) the matter is available to the promisor by way of counterclaim as it would have been against a party` |
| S04-5 | 220-222 | s 4(5) | subsections (2) and (4) are subject to any express term as to the matters that are not to be available | fork M3 | `s 4(5) subsections (2) and (4) are subject to an express term of the contract that takes the matter away` |
| S04-6 | 224-230 | s 4(6) | a third party sued may not enforce a term in reliance on section 2 if the third party could not have done so as a party | encoded (M5) | `s 4(6) the third party may not enforce the term in proceedings brought against the third party`<br>`s 4(6) the third party SHANT enforce the term in proceedings brought against the third party` |
| S05 | 232 | s 5 heading | Enforcement of contract by promisee | inert, reason 1 |  |
| S05-0 | 234-235 | s 5 | section 2 does not affect any right of the promisee to enforce any term | encoded | `s 5 section 2 affects a right of the promisee to enforce a term of the contract` |
| S06 | 237 | s 6 heading | Protection of promisor from double liability | inert, reason 1 |  |
| S06-0 | 239-241 | s 6 (lead-in) | where under section 2 a term is enforceable by a third party and the promisee has recovered a sum in respect of (a) or (b) | encoded | `s 6 the court or arbitral tribunal must reduce any award to the third party` |
| S06-a | 243 | s 6(a) | the third party's loss in respect of the term | encoded | `s 6(a) the promisee has recovered from the promisor a sum in respect of the third party's loss in respect of the term` |
| S06-b | 245-246 | s 6(b) | the expense to the promisee of making good to the third party the default of the promisor | encoded | `s 6(b) the promisee has recovered from the promisor a sum in respect of the expense to the promisee of making good to the third party the default of the promisor` |
| S06-t | 248-251 | s 6 (tail) | in any proceedings brought in reliance on that section by the third party the court or tribunal must reduce any award to such extent as it thinks appropriate | encoded | `s 6 the award to the third party after the reduction`<br>`s 6 the court or arbitral tribunal MUST reduce any award to the third party` |
| P06 | 253-256 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S07 | 258 | s 7 heading | Exceptions | inert, reason 1 |  |
| S07-1 | 260-262 | s 7(1) | no right in the case of a contract on a bill of exchange, promissory note or other negotiable instrument | encoded | `s 7(1) section 2 confers a right on the third party in the case of the contract` |
| S07-2 | 264-266 | s 7(2) | no right in the case of any contract binding on a company and its members under section 39 of the Companies Act 1967 | encoded | `s 7(2) section 2 confers a right on the third party in the case of the contract` |
| S07-3 | 268-271 | s 7(3) | no right in the case of a registration document of an LLP or an LLP agreement | encoded | `s 7(3) section 2 confers a right on the third party in the case of the contract` |
| P07 | 273 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S07-4 | 275-276 | s 7(4) | no right to enforce a term of a contract of employment against an employee | encoded | `s 7(4) section 2 confers a right on the third party to enforce a term of the contract of employment against an employee` |
| S07-5 | 278-279 | s 7(5) | section 2 confers no right in the case of (a) or (b), except that a third party may avail of an exclusion or limitation of liability | fork QA | `s 7(5) section 2 confers a right on the third party in the case of the contract`<br>`s 7(5) the third party may in reliance on section 2 avail of an exclusion or limitation of liability in the contract` |
| S07-5a | 281 | s 7(5)(a) | a contract for the carriage of goods by sea | encoded | `s 7(5)(a) the contract is a contract for the carriage of goods by sea` |
| S07-5b | 283-285 | s 7(5)(b) | a contract for the carriage of goods by rail or road, or of cargo by air, subject to the rules of the appropriate international transport convention | encoded | `s 7(5)(b) the contract is a contract for the carriage of goods by rail or road, or for the carriage of cargo by air, which is subject to the rules of the appropriate international transport convention` |
| S07-5c | 287-288 | s 7(5) (exception) | except that a third party may in reliance on that section avail the third party of an exclusion or limitation of liability in such a contract | fork QA | `s 7(5) the third party may in reliance on section 2 avail of an exclusion or limitation of liability in the contract`<br>`s 7(5) section 2 confers a right on the third party in the case of the contract` |
| S07-6 | 290 | s 7(6) | in subsection (5), the two definitions | encoded | `s 7(6) the Convention is the appropriate international transport convention for the contract`<br>`s 7(6) the contract is a contract for the carriage of goods by sea` |
| D04 | 292 | s 7(6) "appropriate international transport convention" | defined term: means (a) air, (b) rail, (c) road | encoded | `s 7(6) the Convention is the appropriate international transport convention for the contract` |
| S07-6a | 294-297 | s 7(6) "appropriate ..." (a) | air: the Convention with the force of law under section 3 of the Carriage by Air Act 1988 | encoded | `s 7(6) the Convention is the appropriate international transport convention for the contract` |
| S07-6b | 299-302 | s 7(6) "appropriate ..." (b) | rail: the Convention with the force of law under the written law the Minister may by order prescribe | encoded | `s 7(6) the Convention is the appropriate international transport convention for the contract` |
| P08 | 303-305 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S07-6c | 307-310 | s 7(6) "appropriate ..." (c) | road: the Convention with the force of law under the written law the Minister may by order prescribe | encoded | `s 7(6) the Convention is the appropriate international transport convention for the contract` |
| D05 | 312-313 | s 7(6) "contract for the carriage of goods by sea" | defined term: means a contract of carriage (a) or (b) | encoded | `s 7(6) the contract is a contract for the carriage of goods by sea` |
| S07-6d | 315-316 | s 7(6) "contract ... by sea" (a) | contained in or evidenced by a bill of lading or sea waybill | encoded | `s 7(6) the contract is a contract for the carriage of goods by sea` |
| S07-6e | 318-320 | s 7(6) "contract ... by sea" (b) | an undertaking contained in a ship's delivery order is given under or for its purposes | encoded | `s 7(6) the contract is a contract for the carriage of goods by sea` |
| P09 | 322 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| D06 | 324-326 | s 7(7) "bill of lading" | defined term (by reference to the Bills of Lading Act 1992) | encoded | `s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name` |
| D07 | 324-326 | s 7(7) "sea waybill" | defined term (by reference to the Bills of Lading Act 1992) | encoded | `s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name` |
| D08 | 324-326 | s 7(7) "ship's delivery order" | defined term (by reference to the Bills of Lading Act 1992) | encoded | `s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name` |
| S07-7 | 324-326 | s 7(7) | "bill of lading", "sea waybill" and "ship's delivery order" have the meanings given by the Bills of Lading Act 1992 | encoded | `s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name` |
| P10 | 328 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S08 | 330 | s 8 heading | Supplementary provisions relating to third party | inert, reason 1 |  |
| S08-1 | 332-333 | s 8(1) | section 2 does not affect any right or remedy of a third party that exists apart from this Act | encoded | `s 8(1) section 2 affects a right or remedy of the third party that exists or is available apart from this Act` |
| S08-2 | 335-339 | s 8(2) | section 2(2) of the Unfair Contract Terms Act 1977 does not apply where the negligence consists of breach of an obligation arising from a term of a contract and the person enforcing is a third party relying on section 2 | encoded | `s 8(2) section 2(2) of the Unfair Contract Terms Act 1977 does not apply` |
| S08-3 | 341-343 | s 8(3) | in section 6 of the Limitation Act 1959 the references to an action founded on a contract include an action brought in reliance on section 2 | encoded | `s 8(3) the action is one founded on a contract for the purposes of section 6 of the Limitation Act 1959`<br>`s 8(3) the period that applies to the action, in years` |
| S08-4 | 345-347 | s 8(4) | a third party is not, by virtue of section 2(5) or 4(4) or (6), treated as a party for the purposes of any other written law | encoded | `s 8(4) the third party is treated as a party to the contract for the purposes of any other written law` |
| P11 | 349-352 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |
| S09 | 354 | s 9 heading | Arbitration provisions | inert, reason 1 |  |
| S09-1 | 356 | s 9(1) (lead-in) | Where (a) and (b) | encoded (M5) | `s 9(1) the third party is treated as a party to the arbitration agreement` |
| D09 | 358-359 | s 9(1)(a) "substantive term" | defined term: a term the third party has a right under section 2 to enforce, that is subject to an arbitration term | encoded | `s 9(1) the third party is treated as a party to the arbitration agreement` |
| S09-1a | 358-361 | s 9(1)(a) | a right under section 2 to enforce a term (the substantive term) is subject to a term providing for the submission of disputes to arbitration (the arbitration agreement) | encoded | `s 9(1) the third party is treated as a party to the arbitration agreement` |
| D10 | 359-361 | s 9(1)(a) "arbitration agreement" | defined term: the term providing for the submission of disputes to arbitration | encoded | `s 9(1) the third party is treated as a party to the arbitration agreement` |
| S09-1b | 363-365 | s 9(1)(b) | the arbitration agreement is an agreement in writing for the purposes of the Arbitration Act 2001 or Part 2 of the International Arbitration Act 1994 | encoded | `s 9(1) the third party is treated as a party to the arbitration agreement` |
| S09-1t | 367-371 | s 9(1) (tail) | the third party is treated as a party to the arbitration agreement as regards disputes about the third party's enforcement of the substantive term | encoded | `s 9(1) the third party is treated as a party to the arbitration agreement`<br>`s 9(1) the Act for the purposes of which the third party is treated as a party` |
| S09-2 | 373 | s 9(2) (lead-in) | Where (a), (b) and (c) | encoded (M5) | `s 9(2) the third party is treated as a party to the arbitration agreement` |
| S09-2a | 375-379 | s 9(2)(a) | a third party has a right under section 2 to enforce a term providing for disputes between the third party and the promisor to be submitted to arbitration | encoded | `s 9(2) the third party is treated as a party to the arbitration agreement` |
| D11 | 378-379 | s 9(2)(a) "arbitration agreement" | defined term for the purposes of s 9(2) | encoded | `s 9(2) the third party is treated as a party to the arbitration agreement` |
| S09-2b | 381-383 | s 9(2)(b) | the arbitration agreement is an agreement in writing for the purposes of either Act | encoded | `s 9(2) the third party is treated as a party to the arbitration agreement` |
| S09-2c | 385-386 | s 9(2)(c) | the third party does not fall to be treated under subsection (1) as a party to the arbitration agreement | encoded | `s 9(2) the third party is treated as a party to the arbitration agreement` |
| S09-2t | 388-393 | s 9(2) (tail) | the third party is, if the third party exercises the right, treated as a party, and as having been so immediately before the exercise | encoded | `s 9(2) the third party is treated as a party to the arbitration agreement` |
| B01 | 394-398 | legislative history (heading and note) | "This Legislative History ... is not part of the Act." | inert, reason 1 |  |
| B02 | 400-408 | legislative history 1 | Act 39 of 2001 | inert, reason 1 |  |
| B03 | 410-413 | legislative history 2 | 2002 Revised Edition | inert, reason 1 |  |
| B04 | 415-426 | legislative history 3 | Act 5 of 2005 (Limited Liability Partnerships Act 2005) | inert, reason 1 |  |
| B05 | 428-443 | legislative history 4 | Act 40 of 2019 (Supreme Court of Judicature (Amendment) Act 2019) | inert, reason 1 |  |
| B06 | 445-454 | legislative history 5 | Act 5 of 2021 (Electronic Transactions (Amendment) Act 2021) | inert, reason 1 |  |
| B07 | 456 | abbreviations (heading) | Abbreviations | inert, reason 1 |  |
| X458 | 458 | abbreviation "C.P." | abbreviations table row | inert, reason 1 |  |
| X460 | 460 | abbreviation "G.N. No. S (N.S.)" | abbreviations table row | inert, reason 1 |  |
| X462 | 462 | abbreviation "G.N. No." | abbreviations table row | inert, reason 1 |  |
| X464 | 464 | abbreviation "G.N. No. S" | abbreviations table row | inert, reason 1 |  |
| X466 | 466 | abbreviation "G.N. Sp. No. S" | abbreviations table row | inert, reason 1 |  |
| X468 | 468 | abbreviation "L.A." | abbreviations table row | inert, reason 1 |  |
| X470 | 470-472 | abbreviation "L.N." | abbreviations table row | inert, reason 1 |  |
| X474 | 474 | abbreviation "M. Act" | abbreviations table row | inert, reason 1 |  |
| X476 | 476 | abbreviation "M. Ordinance" | abbreviations table row | inert, reason 1 |  |
| X478 | 478 | abbreviation "Parl." | abbreviations table row | inert, reason 1 |  |
| X480 | 480-481 | abbreviation "S.S.G.G. (E) No." | abbreviations table row | inert, reason 1 |  |
| X483 | 483 | abbreviation "S.S.G.G. No." | abbreviations table row | inert, reason 1 |  |
| B08 | 484-489 | comparative table (heading and note) | "provided to help readers locate the corresponding provisions in the last Revised Edition" | inert, reason 1 |  |
| B09 | 491 | comparative table (column heads) | 2020 Ed. / 2002 Ed. | inert, reason 1 |  |
| C493 | 493 | comparative table row | 7—(3) 7—(2A) | inert, reason 1 |  |
| C494 | 494 | comparative table row | (4) (3) | inert, reason 1 |  |
| C495 | 495 | comparative table row | (5) (4) | inert, reason 1 |  |
| C496 | 496 | comparative table row | (6) (5) | inert, reason 1 |  |
| C497 | 497 | comparative table row | (7) (6) | inert, reason 1 |  |
| P12 | 499 | page furniture | page numbers, date stamps, running heads, amendment marks | inert, reason 1 |  |

## Dependencies

Two modules staged from the Commons row `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/` (Commons main d468311a6ea4bab765b1ee7ccc8f0d7ccb29a357), copied byte for byte (checked with `cmp` against the staged files on 2026-11-05) and imported by name:

| Module | Commons path | Blob | Sections used |
| --- | --- | --- | --- |
| `sgia-interpretation-time.l4` | `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-interpretation-time.l4` | fe60ab2c1f2326a5b061e163761bd63e4f47e12a | s 2(1) "month" and the counting of a period of months from a day, used by `s 1(2) the last day of the period of 6 months from 1 January 2002, as the Interpretation Act counts it` in `crtpa-s1-application.l4`; the module has no rule that counts months from a day and returns `NOTHING` (asserted in `crtpa-test-s1.l4`) |
| `sgia-p1-definitions.l4` | `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-p1-definitions.l4` | ca5e2607c635962769a753d71154ad4ae6055f59 | s 2(1) definitions: the entry for "month" (a calendar month), asserted in `crtpa-test-s1.l4` |

The staged copies carry a 3-line header that is the only addition; the blob in the table is that of the file in Commons.
Other Acts the text cites (the Companies Act 1967, the Limited Liability Partnerships Act 2005, the Unfair Contract Terms Act 1977, the Limitation Act 1959, the Carriage by Air Act 1988, the Bills of Lading Act 1992, the Arbitration Act 2001, the International Arbitration Act 1994) are not staged: each is taken as a named input citing the section and is listed under the findings below as one to fill later.
The Interpretation Act's own time rules (counting days, a Sunday or public holiday) are not used: the Act sets no period measured in days.

## Fork register

Every ambiguity: the readings I saw, the one I took, and the text that licenses each.
The four rulings are copied word for word from the brief.

### Rulings (word for word)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

How I applied them (each site is also marked in the L4 by a comment that begins `FALSE-kind` or `NOTHING-kind`):
- E1: each section answers on its own (option C).
  I wrote one hand-gathered function (`ss 1, 2 and 7 taken together the third party may enforce the term of the contract`, crtpa-enforce.l4:61) and one (`s 4(2), (3) and (4)(a) taken together the matter is available to the promisor by way of defence or set-off`, crtpa-s4-defences.l4:188), in plain L4, option B as guidance for hand-gathering only; both take the answers of the section rules as inputs and hold no law of their own.
  No construct that gathers a legal effect by name was looked for.
- N2: every flat negative of the Act (ss 2(4), 2(5) last limb, 4(6), 5, 7(1) to (5), 8(1), 8(4)) answers `JUST FALSE` inside its scope; the bearer is named in s 3(1) (the parties to the contract) and s 4(6) (the third party), so those two have a derived `SHANT` rule; s 6 and s 3(4) name the court or arbitral tribunal and have `MUST` and `MAY` rules.
  The Hohfeld kinds are in the table above and nowhere in an answer.
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
  Where I could not tell which of (a), (b) and (c) a clause is, it is a fork below (G17, G18).
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
  The note on (d) asks that the deontic mechanism examine a trace; s 3(2)(b) gives no party a duty, permission or prohibition, so there is no obligation for a trace to examine, and I modelled it as the two yes/no functions of the ruling over two facts the person states (sent, received).
  That is recorded as G34 for a human to overrule.

### Judgment calls (QA to QF)

One line per site: question, provision, function, file:line, the answer taken, the other reading.

| Q | Provision | Function | File:line | Answer taken | Other reading |
| --- | --- | --- | --- | --- | --- |
| QA | s 1(2) with (3) | `s 1(2) this Act applies in relation to the contract` | crtpa-s1-application.l4:121 | `NOTHING` when the "Subject to subsection (3)" is met (a lifted bar grants nothing); `JUST FALSE` when the restriction bites; the restriction question `s 1(2) the restriction on the application of this Act applies to the contract` (crtpa-s1-application.l4:100) carries the no/yes | `JUST TRUE` (the exception permits it) |
| QA | s 7(5) | `s 7(5) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:209 | `NOTHING` when "except that a third party may ... avail" is met; `JUST FALSE` otherwise; the exception's own grant is a separate function, `s 7(5) the third party may in reliance on section 2 avail of an exclusion or limitation of liability in the contract` (crtpa-s7-exceptions.l4:229), `JUST TRUE` (the text's own "may ... avail") | `JUST TRUE` for the bar function too; or `NOTHING` plus a yes/no "is it barred?" twin |
| QA | s 3(3)(a) | `s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account` | crtpa-s3-variation.l4:197 | `JUST FALSE` (a prohibition lifted by an express term: the requirement does not apply; M3) | `NOTHING` |
| QA | s 4(5) | `s 4(2) the matter is available to the promisor by way of defence or set-off` | crtpa-s4-defences.l4:68 | `JUST FALSE` when an express term takes the matter away ("subject to", M3); the same in the two rules for s 4(4)(a) and s 4(4)(b) | `NOTHING` |
| QB | s 2(3) first limb | `s 2(3) the third party is expressly identified in the contract by name, as a member of a class or as answering a particular description` | crtpa-s2-right.l4:97 | `JUST FALSE` for identification by implication only or none (read as a condition of the right granted in s 2(1)) | `NOTHING` (a bare "must") |
| QB | s 2(5) | `s 2(5) the remedy is available to the third party` | crtpa-s2-right.l4:143 | `NOTHING` when the remedy would not have been available to a party (a grant "is to be available", limited by its own wording) | `JUST FALSE` |
| QC | none | (no Schedule; nothing in the text is "listed in" a list that describes kinds of thing) | | not arising | |
| QD | s 6 | `s 6 the court or arbitral tribunal must reduce any award to the third party` | crtpa-s5-s6-promisee.l4:65 | the duty-arises function answers `JUST FALSE` when the "Where" is unmet and `NOTHING` when the proceedings are not ones the duty speaks of; there is no separate compliance function; the `MUST` rule is `FULFILLED` when the duty does not arise | `JUST TRUE` ("nothing is unmet"), or a compliance function answering `NOTHING` beside the arises function |
| QD | s 3(1), s 4(6) | `s 3(1) ... SHANT ...`, `s 4(6) ... SHANT ...` | crtpa-s3-variation.l4:313; crtpa-s4-defences.l4:235 | `FULFILLED` when the prohibition does not arise (asserted) | `JUST TRUE` in a yes/no form, or `NOTHING` |
| QE | none | ("other than X" parenthesis) | | not arising: `grep -n "other than" CRTPA2001.txt` returns no line (the Act has "otherwise than" in s 2(4), which is treated as the flat negative it is, not as QE) | |
| QF | none | (state ledger) | | not applicable: this encoding writes no events to a ledger | |

### Other forks

| Id | Provision | Function | File:line | Answer taken | Other reading |
| --- | --- | --- | --- | --- | --- |
| G1 | s 1(2) | `s 1(2) the contract was entered into before the end of the period of 6 months from 1 January 2002` | crtpa-s1-application.l4:42 | the Interpretation Act module has no rule counting months from a day, so the last day is `NOTHING`; a contract of 30 June 2002 or earlier is within the period (`JUST TRUE`), of 2 July 2002 or later is outside it (`JUST FALSE`), and of 1 July 2002 is undecided (`NOTHING`); a contract made on the last day itself is "before the end" of the period | the last day is 30 June 2002 (1 January counted) or 1 July 2002 (1 January not counted), and a contract made on that day is, or is not, "before the end" |
| G2 | s 1(2), (3) | `s 1(2) this Act applies in relation to the contract` | crtpa-s1-application.l4:121 | `JUST FALSE` where the restriction bites, `NOTHING` otherwise, because the text states no affirmative "the Act applies"; `NOTHING` here does not mean that the Act does not apply (after the six months, or where s 1(3) lifts the restriction, the text is silent about it), and the seat's description of the question says so; the combined question of G3 answers `JUST TRUE` on the same facts because it asks whether the third party may enforce the term, and a restriction that does not bite is no bar there, so each answer is right for its own question | `JUST TRUE` after the period |
| G3 | ss 1, 2, 7 | `ss 1, 2 and 7 taken together the third party may enforce the term of the contract` | crtpa-enforce.l4:61 | hand-gathered (option B): `JUST FALSE` if any of s 1(2), s 2(1), s 2(3), s 2(4), s 7(1) to (5) says no; `JUST TRUE` only if the restriction does not apply and s 2(1) and (3) are `JUST TRUE`; a `NOTHING` from an s 7 exception means the contract is outside that exception and does not bar | each section's answer on its own, with no gathered function |
| G4 | s 2(1) | `s 2(1) the person is a third party` | crtpa-s2-right.l4:26 | `JUST FALSE` for a party to the contract (the definition "a person who is not a party") | `NOTHING` |
| G5 | s 2(3) second limb | `s 2(3) the third party must be in existence when the contract is entered into` | crtpa-s2-right.l4:110 | always `JUST FALSE`: "need not be in existence" | `NOTHING` when the person was in existence |
| G6 | s 2(4) | `s 2(4) section 2 confers a right on the third party to enforce the term otherwise than subject to and in accordance with the other relevant terms of the contract` | crtpa-s2-right.l4:122 | `JUST FALSE` where enforcement would not be in accordance with the other terms; `NOTHING` where it would (the negative reaches only the former) | `JUST FALSE` in both |
| G7 | s 2(5) | `s 2(5) the remedy may be refused on the ground that, as against the promisor, the third party is a volunteer` | crtpa-s2-right.l4:163 | `JUST FALSE` for that ground; `NOTHING` for another ground | `JUST FALSE` or `JUST TRUE` for any ground |
| G8 | s 2(6) | `s 2(6) references in this Act to the third party enforcing the term are to be construed as references to availing of the exclusion or limitation` | crtpa-s2-right.l4:179 | the yes/no function answers `JUST FALSE` for any other term (a "Where" unmet); its value twin answers `NOTHING` | `NOTHING` for both |
| G9 | s 2(7) | `s 2(7) the party is the promisee` | crtpa-s2-right.l4:204 | `NOTHING` where the term is not one a third party can enforce (the definitions are "in relation to a term ... enforceable by a third party": a scope limit); inside the scope the other position is `JUST FALSE` | `JUST FALSE` |
| G10 | s 3(1) | `s 3(1) the parties to the contract may not rescind or vary the contract without the third party's consent` | crtpa-s3-variation.l4:159 | `JUST TRUE` when the bar applies; `JUST FALSE` when the third party has no right under s 2 or none of (a), (b), (c) exists (M5); `NOTHING` for a variation that neither extinguishes nor alters the entitlement, for a change not made by agreement, and where the third party has consented ("without ... consent" limits the prohibition) | `JUST FALSE` for those three |
| G11 | s 3(1)(b), (c) | `s 3(1)(b) and (c) knowledge of the precise terms of the term is a condition` | crtpa-s3-variation.l4:65 | `JUST FALSE`: knowledge is no condition ("whether or not the third party has knowledge of its precise terms") | none |
| G12 | s 3(2)(a) | `s 3(2)(a) the assent may be by this form` | crtpa-s3-variation.l4:105 | words and conduct `JUST TRUE`; silence or another form `NOTHING` (the list is not closed with "only") | `JUST FALSE` for silence |
| G13 | s 3(3)(b) | `s 3(1) with (3) the parties ...` | crtpa-s3-variation.l4:197 | a contract term requiring consent in circumstances it specifies replaces (a), (b), (c) with those circumstances, as the person states them | the contract's circumstances are added to (a), (b), (c) |
| G14 | s 3(4), (5) | `s 3(4) the court or arbitral tribunal may dispense with the third party's consent` | crtpa-s3-variation.l4:228 | the court's or tribunal's satisfaction is a judgment handed to it: a conditional input, `NOTHING` when not stated; an application by the parties is a "where" (M7) | the satisfaction is a fact the person states as true or false |
| G15 | s 3(6) | `s 3(6) the court or arbitral tribunal may impose such conditions as it thinks fit` | crtpa-s3-variation.l4:267 | `JUST FALSE` if it has not dispensed with the consent (M5) | `NOTHING` |
| G16 | s 3(7) | `s 3(7) the jurisdiction conferred on the court by subsections (4), (5) and (6) is exercisable by this body` | crtpa-s3-variation.l4:285 | the two named courts `JUST TRUE`; another court or an arbitral tribunal `NOTHING` | `JUST FALSE` for those |
| G17 | s 4(1), (2), (3), (4) | `s 4(2) the matter is available to the promisor by way of defence or set-off`, `s 4(3) ...`, `s 4(4)(a) ...` and `s 4(4)(b) ...` | crtpa-s4-defences.l4:68; crtpa-s4-defences.l4:93; crtpa-s4-defences.l4:115; crtpa-s4-defences.l4:139 | one answer for all four: when a limb of the grant is unmet the subsection gives the promisor no defence on these facts, `JUST FALSE` (M8 for s 4(2), (4)(a) and (4)(b); s 4(3) is M5), and never "the promisor has no defence at all"; s 4(1)'s "where" unmet is `JUST FALSE` for all of them. The wording differs (s 4(2) and (4) say "any matter that" and "any matter not arising from the contract", s 4(3) says "any matter if"), and the wording alone would split them; three reasons that do not rest on it decided me. (1) The subsection answers a question the person asks, "may the promisor rely on this?", and "no, not under this subsection, on these facts" is the true answer for all four, whatever the drafter's choice between "that" and "if". (2) The same function already answers `JUST FALSE` when s 4(1) fails, so a split would make the answer depend on which condition failed first, a difference a person cannot use. (3) The gathered function over (2), (3) and (4)(a) combines the three: with two of them `NOTHING` it would answer `NOTHING` on facts where every limb had been checked and none held, and a person asking what defence the promisor has would be told "not answered" where the answer is "none of these three gives it". Not read as "it is a defence ... to prove that X" (ruling (b)): s 4 is a grant, so ruling (b) is applied by analogy, not by its words | `NOTHING` for s 4(2), (4)(a) and (4)(b) when a limb is unmet, as a scope limit with no "only" (ruling (c): "any matter that" reaches only the matters it describes and says nothing of others), keeping `JUST FALSE` for s 4(3); the matter that falls outside one grant may fall inside another, or inside general law the Act leaves alone |
| G18 | s 4(6) | `s 4(6) the third party may not enforce the term in proceedings brought against the third party` | crtpa-s4-defences.l4:209 | `JUST FALSE` when the "Where" is unmet or the "if" is unmet (M5); the counterfactual ("could not have done so had the third party been a party") is a judgment the person states, `NOTHING` when not | `NOTHING` for the unmet "if" |
| G19 | s 4(5) | `s 4(5) subsections (2) and (4) are subject to an express term of the contract that takes the matter away` | crtpa-s4-defences.l4:44 | `JUST TRUE` with such a term; `NOTHING` without one (the subject-to speaks only of such a term) | `JUST FALSE` without one |
| G20 | s 5 | `s 5 section 2 affects a right of the promisee to enforce a term of the contract` | crtpa-s5-s6-promisee.l4:23 | `JUST FALSE` for the promisee's right; `NOTHING` for any other right | `JUST FALSE` for any right |
| G21 | s 6 | `s 6 the award to the third party after the reduction` | crtpa-s5-s6-promisee.l4:90 | the extent is the court's or tribunal's judgment (an input); a reduction below nothing or above the award is not one the text describes (`NOTHING`); when the duty does not arise the value is `NOTHING` and the yes/no function carries the no (assumed, not ruled) | `JUST` the award unreduced |
| G22 | s 7(1) to (4) | `s 7(1) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:30 | `JUST FALSE` inside the scope of the flat negative, `NOTHING` outside it (the exception does not say section 2 confers a right elsewhere) | `JUST TRUE` outside |
| G23 | s 7(5)(b) | `s 7(5)(b) the contract is a contract for the carriage of goods by rail or road, or for the carriage of cargo by air, which is subject to the rules of the appropriate international transport convention` | crtpa-s7-exceptions.l4:177 | the mode type names what is carried, and the three descriptions are cargo by air, goods by rail and goods by road; each of the three modes also has a choice for any other carriage by that mode (passengers, say), and so does `carriage by sea` and `carriage by some other mode`; `JUST FALSE` for every choice that is not one of the three descriptions (a closed description: the text says "goods" and "cargo", and a contract to carry passengers is not within (b) even when a Convention governs it); checked against the words for each of air, rail and road | `NOTHING` for the choices outside the three descriptions; or one `Mode of carriage` value per mode with a separate yes/no input for "goods or cargo" |
| G24 | s 7(6) | `s 7(6) the Convention is the appropriate international transport convention for the contract` | crtpa-s7-exceptions.l4:138 | `JUST FALSE` for sea, another mode, and any carriage by air, rail or road that is not cargo (by air) or goods (by rail or road): the definition says "means" and gives a limb (a) for "cargo by air", (b) for "goods by rail" and (c) for "goods by road", so passengers by air have no appropriate convention in this Act's sense, whatever the Carriage by Air Act 1988 does for them; the air limb and the Minister's order for rail and road are facts the person states (`NOTHING` when not) | `NOTHING` for sea and for the carriage of passengers |
| G25 | s 7(6), (7) | `s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name` | crtpa-s7-exceptions.l4:90 | the meaning is the other Act's: the person's statement, `NOTHING` when not stated | none |
| G26 | s 8(2) | `s 8(2) section 2(2) of the Unfair Contract Terms Act 1977 does not apply` | crtpa-s8-supplementary.l4:42 | `JUST TRUE` where both limbs hold; `JUST FALSE` otherwise (a "where" unmet) | `NOTHING` otherwise |
| G27 | s 8(3) | `s 8(3) the action is one founded on a contract for the purposes of section 6 of the Limitation Act 1959` | crtpa-s8-supplementary.l4:58 | `JUST TRUE` for an action brought in reliance on s 2; `NOTHING` otherwise (the clause "includes"); the period is the Limitation Act's, an input | `JUST FALSE` otherwise |
| G28 | s 8(4) | `s 8(4) the third party is treated as a party to the contract for the purposes of any other written law` | crtpa-s8-supplementary.l4:88 | `JUST FALSE` by the three named routes; `NOTHING` by any other (s 9 treats the third party as a party for the arbitration Acts) | `JUST FALSE` by every route |
| G29 | s 9(1) | `s 9(1) the third party is treated as a party to the arbitration agreement` | crtpa-s9-arbitration.l4:37 | `JUST FALSE` if (a) or (b) is unmet (a "Where"); `NOTHING` for a dispute that is not between the third party and the promisor about the third party's enforcement of the substantive term; the Act "as the case may be" is a separate value function | `JUST FALSE` for another dispute |
| G30 | s 9(2) | `s 9(2) the third party is treated as a party to the arbitration agreement` | crtpa-s9-arbitration.l4:91 | `JUST TRUE` at and after the exercise and "immediately before" it; `NOTHING` for an earlier time; `JUST FALSE` if the third party does not exercise the right (M5) or already falls under (1) | `NOTHING` if not exercised |
| G31 | s 2(1) | `s 2(1) the third party may in the third party's own right enforce the term of the contract` | crtpa-s2-right.l4:79 | "Subject to the provisions of this Act": the other provisions are asked in their own rules and gathered in `crtpa-enforce.l4` (G3); the two routes are `JUST FALSE` when neither holds (M1) | `NOTHING` when neither holds |
| G32 | ss 3(1), 3(4), 4(6), 6 | the four regulative rules | crtpa-s3-variation.l4:313; crtpa-s3-variation.l4:333; crtpa-s4-defences.l4:235; crtpa-s5-s6-promisee.l4:116 | no `WITHIN`: the text states no deadline, and none was invented | a deadline of the person's choosing as an input |
| G33 | s 3(1) | `s 3(1) the parties to the contract SHANT rescind or vary the contract without the third party's consent` | crtpa-s3-variation.l4:313 | the prohibition is on rescinding and on varying so as to extinguish or alter, each its own act (a `RAND` of two prohibitions) | one prohibition on both together |
| G34 | s 3(2)(b) | `s 3(2)(b) the assent cannot yet be regarded as communicated to the promisor` | crtpa-s3-variation.l4:125 | the "until" bar as two yes/no functions over two facts (ruling (d)); no obligation to trace | model the posting and the receipt as events in a trace (the note on ruling (d)) |

## Marginal readings for a lawyer

The two readings the brief flags for a lawyer, taken as the status quo: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text's no; (b) a prohibition or grant limited by its own wording does not.
Every branch that rests on one is listed here, found by scanning the comments in the L4: M1 1, M2 1, M3 4, M5 8, M6 1, M7 2, M8 3, NEG 17, SCOPE 31, CLOSED 5 (73 branches in 63 function-readings).
Label M4 was reserved during drafting for a reading that did not survive and is unused; the labels in the L4 comments are kept as written so they stay greppable.

Legend: what each label means, and the other reading.

| Label | Reading taken | The other reading |
| --- | --- | --- |
| M1 | M1 failed "if" is the text's no | NOTHING: s 2(1) says what the third party may do "if" (a) or (b), and not what follows if neither holds. |
| M2 | M2 failed "if" is the text's no | NOTHING: s 2(2) says (1)(b) "does not apply if" the parties did not intend it, and not that it applies if they did. |
| M3 | M3 "subject to" an express term is the text's no for the matter it removes | NOTHING: "subject to any express term" limits the grant by its own wording, and the text does not say in terms that the grant fails where the express term applies. |
| M5 | M5 failed "if" is the text's no, clause by clause | NOTHING: an "if" does not itself say "if not, then not". |
| M6 | M6 "if sent by post" unmet is the text's no | NOTHING: "if sent ... by post or other means" does not itself say what holds when it is not sent. |
| M7 | M7 "on the application of" counted like "upon" (ruling (c)) | NOTHING: "on the application of" is not introduced by "if" or "where"; the ruling (c) treats it like "upon". |
| M8 | M8 an unmet limb of a grant of a defence is "this subsection gives no defence on these facts" | NOTHING: "any matter that ..." in s 4(2) and (4) limits the grant by its own wording, as a scope limit with no "only" (ruling (c)); the matter that falls outside it may fall inside another grant. |
| N2 | N2 flat negative is the text's no | NOTHING: a flat negative counted as the text's no (ruling N2), but a reader who counts only a closed list as a no would answer NOTHING here. |
| (b) | (b) limited by its own wording is NOT a no (NOTHING) | JUST FALSE: a grant or prohibition limited by its own wording, read as saying no outside the limit (ruling: scope limit without "only" answers NOTHING). |
| closed | closed description read as a no | NOTHING: a description that is not closed with "only" does not say no to a case it does not describe. |

| Label | Function | File:line | Branches |
| --- | --- | --- | --- |
| M1 | `s 2(1) the third party may in the third party's own right enforce the term of the contract` | crtpa-s2-right.l4:79 | 1 |
| M2 | `s 2(2) subsection (1)(b) does not apply to the term` | crtpa-s2-right.l4:45 | 1 |
| M3 | `s 3(1) with (3) the parties to the contract may not rescind or vary the contract without the third party's consent, taking an express term of the contract into account` | crtpa-s3-variation.l4:197 | 1 |
| M3 | `s 4(2) the matter is available to the promisor by way of defence or set-off` | crtpa-s4-defences.l4:68 | 1 |
| M3 | `s 4(4)(a) the matter is available to the promisor by way of defence or set-off as it would have been against a party` | crtpa-s4-defences.l4:115 | 1 |
| M3 | `s 4(4)(b) the matter is available to the promisor by way of counterclaim as it would have been against a party` | crtpa-s4-defences.l4:139 | 1 |
| M5 | `s 3(1) one of the circumstances in (a), (b) and (c) exists` | crtpa-s3-variation.l4:91 | 1 |
| M5 | `s 3(1) the parties to the contract may not rescind or vary the contract without the third party's consent` | crtpa-s3-variation.l4:159 | 1 |
| M5 | `s 3(4) the court or arbitral tribunal may dispense with the third party's consent` | crtpa-s3-variation.l4:228 | 1 |
| M5 | `s 3(5) the court or arbitral tribunal may dispense with a consent that may be required under subsection (1)(c)` | crtpa-s3-variation.l4:251 | 1 |
| M5 | `s 3(6) the court or arbitral tribunal may impose such conditions as it thinks fit` | crtpa-s3-variation.l4:267 | 1 |
| M5 | `s 4(3) the matter is available to the promisor by way of defence or set-off because an express term provides for it` | crtpa-s4-defences.l4:93 | 1 |
| M5 | `s 4(6) the third party may not enforce the term in proceedings brought against the third party` | crtpa-s4-defences.l4:209 | 1 |
| M5 | `s 9(2) the third party is treated as a party to the arbitration agreement` | crtpa-s9-arbitration.l4:91 | 1 |
| M6 | `s 3(2)(b) the assent cannot yet be regarded as communicated to the promisor` | crtpa-s3-variation.l4:125 | 1 |
| M7 | `s 3(4) the court or arbitral tribunal may dispense with the third party's consent` | crtpa-s3-variation.l4:228 | 1 |
| M7 | `s 3(5) the court or arbitral tribunal may dispense with a consent that may be required under subsection (1)(c)` | crtpa-s3-variation.l4:251 | 1 |
| M8 | `s 4(2) the matter is available to the promisor by way of defence or set-off` | crtpa-s4-defences.l4:68 | 1 |
| M8 | `s 4(4)(a) the matter is available to the promisor by way of defence or set-off as it would have been against a party` | crtpa-s4-defences.l4:115 | 1 |
| M8 | `s 4(4)(b) the matter is available to the promisor by way of counterclaim as it would have been against a party` | crtpa-s4-defences.l4:139 | 1 |
| N2 | `s 1(2) the restriction on the application of this Act applies to the contract` | crtpa-s1-application.l4:100 | 1 |
| N2 | `s 1(2) this Act applies in relation to the contract` | crtpa-s1-application.l4:121 | 1 |
| N2 | `s 2(1) the person is a third party` | crtpa-s2-right.l4:26 | 1 |
| N2 | `s 2(3) the third party must be in existence when the contract is entered into` | crtpa-s2-right.l4:110 | 1 |
| N2 | `s 2(4) section 2 confers a right on the third party to enforce the term otherwise than subject to and in accordance with the other relevant terms of the contract` | crtpa-s2-right.l4:122 | 1 |
| N2 | `s 2(5) the remedy may be refused on the ground that, as against the promisor, the third party is a volunteer` | crtpa-s2-right.l4:163 | 1 |
| N2 | `s 3(1)(b) and (c) knowledge of the precise terms of the term is a condition` | crtpa-s3-variation.l4:65 | 1 |
| N2 | `s 5 section 2 affects a right of the promisee to enforce a term of the contract` | crtpa-s5-s6-promisee.l4:23 | 1 |
| N2 | `s 7(1) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:30 | 1 |
| N2 | `s 7(2) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:43 | 1 |
| N2 | `s 7(3) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:58 | 1 |
| N2 | `s 7(4) section 2 confers a right on the third party to enforce a term of the contract of employment against an employee` | crtpa-s7-exceptions.l4:72 | 1 |
| N2 | `s 7(5) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:209 | 1 |
| N2 | `s 8(1) section 2 affects a right or remedy of the third party that exists or is available apart from this Act` | crtpa-s8-supplementary.l4:24 | 1 |
| N2 | `s 8(4) the third party is treated as a party to the contract for the purposes of any other written law` | crtpa-s8-supplementary.l4:88 | 3 |
| (b) | `s 1(3) the restriction in subsection (2) does not apply in relation to the contract` | crtpa-s1-application.l4:78 | 1 |
| (b) | `s 1(2) this Act applies in relation to the contract` | crtpa-s1-application.l4:121 | 1 |
| (b) | `s 2(4) section 2 confers a right on the third party to enforce the term otherwise than subject to and in accordance with the other relevant terms of the contract` | crtpa-s2-right.l4:122 | 1 |
| (b) | `s 2(5) the remedy is available to the third party` | crtpa-s2-right.l4:143 | 1 |
| (b) | `s 2(5) the rules relating to damages, injunctions, specific performance and other remedy apply to the third party's remedy accordingly` | crtpa-s2-right.l4:153 | 1 |
| (b) | `s 2(5) the remedy may be refused on the ground that, as against the promisor, the third party is a volunteer` | crtpa-s2-right.l4:163 | 1 |
| (b) | `s 2(7) the party is the promisee` | crtpa-s2-right.l4:204 | 1 |
| (b) | `s 2(7) the party is the promisor` | crtpa-s2-right.l4:223 | 1 |
| (b) | `s 3(1) the parties to the contract may not rescind or vary the contract without the third party's consent` | crtpa-s3-variation.l4:159 | 3 |
| (b) | `s 3(5) the court or arbitral tribunal may dispense with a consent that may be required under subsection (1)(c)` | crtpa-s3-variation.l4:251 | 1 |
| (b) | `s 3(7) the jurisdiction conferred on the court by subsections (4), (5) and (6) is exercisable by this body` | crtpa-s3-variation.l4:285 | 1 |
| (b) | `s 4(5) subsections (2) and (4) are subject to an express term of the contract that takes the matter away` | crtpa-s4-defences.l4:44 | 1 |
| (b) | `s 5 section 2 affects a right of the promisee to enforce a term of the contract` | crtpa-s5-s6-promisee.l4:23 | 1 |
| (b) | `s 6 the court or arbitral tribunal must reduce any award to the third party` | crtpa-s5-s6-promisee.l4:65 | 1 |
| (b) | `s 6 the award to the third party after the reduction` | crtpa-s5-s6-promisee.l4:90 | 1 |
| (b) | `s 7(1) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:30 | 1 |
| (b) | `s 7(2) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:43 | 1 |
| (b) | `s 7(3) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:58 | 1 |
| (b) | `s 7(4) section 2 confers a right on the third party to enforce a term of the contract of employment against an employee` | crtpa-s7-exceptions.l4:72 | 1 |
| (b) | `s 7(7) the document has the meaning given by the Bills of Lading Act 1992 for its name` | crtpa-s7-exceptions.l4:90 | 1 |
| (b) | `s 7(5) section 2 confers a right on the third party in the case of the contract` | crtpa-s7-exceptions.l4:209 | 2 |
| (b) | `s 7(5) the third party may in reliance on section 2 avail of an exclusion or limitation of liability in the contract` | crtpa-s7-exceptions.l4:229 | 2 |
| (b) | `s 8(1) section 2 affects a right or remedy of the third party that exists or is available apart from this Act` | crtpa-s8-supplementary.l4:24 | 1 |
| (b) | `s 8(4) the third party is treated as a party to the contract for the purposes of any other written law` | crtpa-s8-supplementary.l4:88 | 1 |
| (b) | `s 9(1) the third party is treated as a party to the arbitration agreement` | crtpa-s9-arbitration.l4:37 | 1 |
| (b) | `s 9(1) the Act for the purposes of which the third party is treated as a party` | crtpa-s9-arbitration.l4:58 | 1 |
| (b) | `s 9(2) the third party is treated as a party to the arbitration agreement` | crtpa-s9-arbitration.l4:91 | 1 |
| closed | `s 7(5)(b) the contract is a contract for the carriage of goods by rail or road, or for the carriage of cargo by air, which is subject to the rules of the appropriate international transport convention` | crtpa-s7-exceptions.l4:177 | 5 |

## What the text turns out to say

Numbered findings.
A finding ends "Asserted." where a case in `crtpa-cases-seat.l4` or a test in a `crtpa-test-*.l4` file asserts it.

1. **The Act never says that it applies.**
   It says only that it does not apply to a contract entered into before the end of the six months from 1 January 2002 (s 1(2)), and that the restriction does not apply to one entered into on or after that date which expressly provides for it (s 1(3)).
   So a question "does the Act apply to my contract?" answers `JUST FALSE` for a contract inside the restricted period, and `NOTHING` for a later one, and for one that uses s 1(3).
   `NOTHING` there does not mean that the Act does not apply: after the six months the text is silent about whether the Act applies, and the seat's description of that question says so.
   The combined question "taking sections 1, 2 and 7 together may I enforce a term" answers `JUST TRUE` on the same facts because it asks something else: it treats the s 1(2) restriction as a bar, and a restriction that does not bite is no bar, so what remains is s 2's own `JUST TRUE` for a third party named in the contract (G2, G3).
   Both are kept; each answers the question it is asked.
   Asserted (`crtpa-cases-seat.l4`, section 1 cases; `crtpa-test-s1.l4`).
2. **The end of the six months is not computable from the Interpretation Act module.**
   The module has a definition of "month" (calendar month) and no rule that counts months from a day; the six-month period's last day (30 June 2002 or 1 July 2002) therefore stays undecided, and a contract of 1 July 2002 answers `NOTHING`.
   Which count I use, and why: neither.
   A count with the first day inside the period (1 January is day one) ends at the end of 30 June 2002, and one without it (the period starts the next day) ends at the end of 1 July 2002.
   Counting months from a day needs a rule on that point; the Act gives none, the staged Interpretation Act module gives none (its header says so), and nothing else in the sources does.
   So 30 June 2002 and earlier are inside the period on both counts (`JUST TRUE`), 2 July 2002 and later are outside it on both (`JUST FALSE`), and 1 July 2002 is the one day the two counts split on: `NOTHING`.
   A count that takes 30 June 2002 as the last day gives `JUST FALSE` for a contract of 1 July; one that takes 1 July as the last day gives `JUST TRUE` for it.
   The text does not point either way, so I did not choose (G1).
   Asserted (`crtpa-test-s1.l4`; the case marked `OUTSIDE THE ENCODING` for 1 July 2002).
3. **A contract made before 1 January 2002 can never use s 1(3), even if it expressly provides for the Act.**
   Both limbs are joined by "and".
   Asserted (`crtpa-cases-seat.l4`, the case of 20 December 2001).
4. **A third party need not exist when the contract is made, but must be expressly identified.**
   An unborn child or a company not yet incorporated can be named by name, class or description; identification by implication alone is not "expressly identified".
   Asserted (`crtpa-cases-seat.l4`, section 2 cases; judgment call QB).
5. **Whether the third party's right under s 2(1)(b) is taken out turns on a judgment of the contract's meaning (s 2(2)), which the person may not be able to make.**
   The answer is `NOTHING` while that judgment is not stated.
   Asserted (`crtpa-cases-seat.l4`: "I am not sure" cases).
6. **The remedy of s 2(5) is defined by a counterfactual (what a party would have had), and the Act does not say what that is for any given remedy.**
   The person states it; the rules on damages, injunctions and specific performance apply "accordingly" but are not in the Act.
   Asserted (`crtpa-cases-seat.l4`, the remedy and remedy-rules cases).
7. **The bar of s 3(1) has three disjunctive triggers, knowledge of the term's precise terms is irrelevant, and consent defeats the bar.**
   Asserted (`crtpa-test-s3.l4`; the bar cases in `crtpa-cases-seat.l4`).
8. **The bar of s 3(1) reaches only rescission and a variation that extinguishes or alters the third party's entitlement, by agreement.**
   A variation that does neither, and a change not made by the parties' agreement, are outside it, and the Act is silent about them.
   Asserted (the two cases marked `OUTSIDE THE ENCODING` in the bar cases).
9. **An express term of the contract can switch the bar off (s 3(3)(a)) or replace its triggers (s 3(3)(b)).**
   Asserted (`crtpa-test-s3.l4`, `crtpa-cases-seat.l4`).
10. **An assent sent by post is not communicated until received (s 3(2)(b)), but the Act never says it is communicated on receipt.**
    The bar is modelled; the Act's silence after receipt answers `NOTHING`.
    Asserted (`crtpa-test-s3.l4`; the cases asking "Has my assent been communicated to the promisor").
11. **Dispensing with consent needs an application by the parties (s 3(4) to (6)); the court's or tribunal's satisfaction is its own judgment.**
    The jurisdiction is allocated by s 3(7) between the General Division of the High Court and a District Court only; the Act does not allocate it to an arbitral tribunal in terms, although ss 3(4) to (6) speak of "court or arbitral tribunal".
    Asserted (`crtpa-test-s3.l4`; the cases for s 3(7) marked `OUTSIDE THE ENCODING`).
12. **The promisor's defences come by three routes (s 4(2), (3), (4)); the Act has no general statement of "every defence".**
    A matter outside all three is one that none of those subsections gives the promisor on these facts: `JUST FALSE`, worded "this section gives no defence on these facts" and never "the promisor has no defence at all" (G17).
    An express term can take away (2) and (4) but not (3), which is itself an express-term route (s 4(5)).
    Asserted (`crtpa-test-s4.l4`; the cases asking "taking section 4(2), (3) and (4)(a) together").
13. **For the carriage exceptions of s 7(5) and (6), the Act needs other laws: the Bills of Lading Act 1992 for what a bill of lading is, the Carriage by Air Act 1988 for the air Convention, and Ministers' orders for the rail and road Conventions.**
    None is among the sources; each is a fact the person states, and the answer is `NOTHING` while it is not.
    Asserted (`crtpa-test-s7.l4`; the cases for s 7(6) and (7) marked `OUTSIDE THE ENCODING`).
14. **The exception to the exception in s 7(5) is a grant of a privilege, and a lifted bar grants nothing.**
    The bar function answers `NOTHING` when the exception is met; the exception has its own function that answers `JUST TRUE`.
    Asserted (`crtpa-test-s7.l4`; judgment call QA).
15. **The court or tribunal's reduction under s 6 has no formula.**
    "To such extent as it thinks appropriate" is its judgment; the award after the reduction answers `NOTHING` until it is stated.
    Asserted (`crtpa-test-s5-s6.l4`; the cases asking "What will my award be after the reduction").
16. **The period for an action brought in reliance on s 2 is the Limitation Act 1959's, not this Act's.**
    Section 8(3) only extends the Limitation Act's wording to the action.
    Asserted (`crtpa-test-s8-s9.l4`; the cases for s 8(3) marked `OUTSIDE THE ENCODING`).
17. **Section 8(4) names three routes by which the third party is not treated as a party for other written law, while section 9 treats the third party as a party for the two arbitration Acts.**
    The Act does not say whether a route other than the three is a party route; the answer for such a route is `NOTHING`.
    Asserted (`crtpa-test-s8-s9.l4`; the case marked `OUTSIDE THE ENCODING` for s 8(4)).
18. **Section 9(2) reaches the third party only if (1) does not, only if the right is exercised, and speaks of "immediately before the exercise": an earlier time is not covered.**
    Asserted (`crtpa-test-s8-s9.l4`; the cases for s 9(2) marked `OUTSIDE THE ENCODING`).
19. **No provision of the Act states a deadline for any duty, permission or prohibition.**
    The four regulative rules have none.
    Not asserted by a case (a DEONTIC that leaves something standing cannot be compared on this binary); read by eye in the traces and asserted where the rule is `FULFILLED`.
20. **Section 2(1) is "Subject to the provisions of this Act", so s 2(1) alone is not the answer to "may the third party enforce?"**
    The answer is gathered from ss 1(2), 2(1), 2(3), 2(4) and 7(1) to (5); the gathered function is option B only (fork G3).
    Asserted (`crtpa-test-enforce.l4`; the cases asking "Taking sections 1, 2 and 7 together" in `crtpa-cases-seat.l4`).
21. **What the main binary does not accept (measured on 1.6.109 on 2026-11-05).**
    (a) A `DEONTIC` value can be compared with `EQUALS` in an `#ASSERT` only when it is `FULFILLED`; a rule that leaves an obligation, permission or prohibition standing gives `eval/unsupported-equality`.
    I tried three forms (against `FULFILLED`, against the same rule applied again, and against a written-out `PARTY ... MUST ...`), and each gave that error.
    So the outcomes with something standing are the `#TRACE` directives in `crtpa-test-s3.l4`, `crtpa-test-s4.l4` and `crtpa-test-s5-s6.l4`, read by eye; the same conditions are asserted through the decision-function twins.
    (b) A single capital letter such as `A` or `B` cannot be a constructor name: `DECLARE Letter IS ONE OF A B` gives `parse/unexpected-A`.
    (c) The rest of the dialect limits in the brief (no `REFUSE`, no section `GIVEN`, no `TYPICALLY`, no sets, no ledger, parenthesised `NOT`, one-line `#ASSERT`, `Date d m y`, `WAITUNTIL`) were followed and not re-tested here.
    (d) `check.sh` compares counts only, so a different `#TRACE` outcome between the two main builds would not show; I compared the full `l4 run` output of the three trace files on 1.6.109 and 1.6.108, and it is identical (same number of lines, `diff` empty).

22. **In s 7(5)(b) and s 7(6) the words are "goods" for rail and road and "cargo" for air, so a contract to carry passengers is not within them.**
    The `Mode of carriage` choices name what is carried as well as the mode: cargo by air, goods by rail and goods by road are the three descriptions, and each of air, rail and road has a second choice for any other carriage by that mode (passengers, say).
    A contract to carry passengers by air, governed by the Convention in force under section 3 of the Carriage by Air Act 1988, is therefore not within s 7(5)(b): `s 7(5)(b) ...` answers `JUST FALSE` for it, `s 7(6) the Convention is the appropriate international transport convention ...` answers `JUST FALSE`, the bar of s 7(5) does not speak, and in the gathered question the right to enforce stands.
    Cargo by air under the same Convention is barred.
    Checked word by word for each mode: air (s 7(5)(b), s 7(6)(a), "cargo"), rail (s 7(6)(b), "goods"), road (s 7(6)(c), "goods"); sea is not in (b) at all, and its own definition in s 7(6) is by documents (a bill of lading or sea waybill, or a ship's delivery order undertaking), not by what is carried, so it is unchanged.
    Whether baggage or mail is "cargo" is a question the text does not decide; a person with baggage or mail chooses the "something other than cargo" answer or the cargo answer on their own reading.
    Asserted (`crtpa-test-s7.l4`, the lines on passengers and the end-to-end pair; `crtpa-cases-seat.l4`, the cases for s 7(5), s 7(6) and the gathered question).
23. **Questions a person might put to the Act that its text does not answer, and that no function here answers.**
    (a) How much compensation the court or tribunal may require under s 3(6): the text says "including a condition requiring the payment of compensation to the third party" and states no amount or measure.
    (b) A term that would put a burden on the third party: the Act confers a right to enforce a term (s 2) and says nothing of a duty imposed on the third party, beyond what s 4 lets the promisor set up against the third party (defences, set-off and counterclaims) and s 4(6).
    (c) Whether the third party's right can be assigned: the text does not mention assignment.
    (d) How long the third party has to assent under s 3(1)(a): s 3(2) says how assent may be given and when it is communicated, and gives no time limit.
    (e) A contract under a foreign governing law: the text does not say whether, or how, the Act reaches it.
    Each of these has no function and no case, and an answer to any of them would be an invention; a person who asks gets no tool for it.

## Unstable dialect

No second, unstable encoding was written.
I looked at time (the one dated rule is the cut-off of s 1(2), a function of one date; nothing is in force on different dates), versions (this text is a single revised edition, and the amendments listed in its legislative history are already consolidated into it) and workarounds on main (the limit on comparing a standing `DEONTIC` in an `#ASSERT`, handled by traces and decision-function twins; the missing month count lies in the staged Interpretation Act module, not in the dialect), and found no shape that earns one.
I did not run the unstable build.

## What `check.sh` prints

Run in this folder on 2026-11-05 with `L4=<1.6.109>` and `L4_MAIN=<1.6.108>`, `JL4_LIBRARY_PATH` unset.
The 23 modules include the two staged Interpretation Act modules.
There was no earlier `check.sh` run for this encoding to replace as a baseline; the one run before this, made before 8 `FULFILLED` assertions were added to the s 3, s 4 and s 5-6 tests, printed 513 satisfied on both builds with every other column zero.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
crtpa-cases-seat.l4                            0       185       0        0         0 |      0       185       0        0  same
crtpa-enforce.l4                               0         0       0        0         0 |      0         0       0        0  same
crtpa-kleene.l4                                0         0       0        0         0 |      0         0       0        0  same
crtpa-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
crtpa-s1-application.l4                        0         0       0        0         0 |      0         0       0        0  same
crtpa-s2-right.l4                              0         0       0        0         0 |      0         0       0        0  same
crtpa-s3-variation.l4                          0         0       0        0         0 |      0         0       0        0  same
crtpa-s4-defences.l4                           0         0       0        0         0 |      0         0       0        0  same
crtpa-s5-s6-promisee.l4                        0         0       0        0         0 |      0         0       0        0  same
crtpa-s7-exceptions.l4                         0         0       0        0         0 |      0         0       0        0  same
crtpa-s8-supplementary.l4                      0         0       0        0         0 |      0         0       0        0  same
crtpa-s9-arbitration.l4                        0         0       0        0         0 |      0         0       0        0  same
crtpa-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
crtpa-test-enforce.l4                          0        13       0        0         0 |      0        13       0        0  same
crtpa-test-s1.l4                               0        37       0        0         0 |      0        37       0        0  same
crtpa-test-s2.l4                               0        54       0        0         0 |      0        54       0        0  same
crtpa-test-s3.l4                               0        79       0        0         0 |      0        79       0        0  same
crtpa-test-s4.l4                               0        44       0        0         0 |      0        44       0        0  same
crtpa-test-s5-s6.l4                            0        23       0        0         0 |      0        23       0        0  same
crtpa-test-s7.l4                               0        67       0        0         0 |      0        67       0        0  same
crtpa-test-s8-s9.l4                            0        36       0        0         0 |      0        36       0        0  same
sgia-interpretation-time.l4                    0         0       0        0         0 |      0         0       0        0  same
sgia-p1-definitions.l4                         0         0       0        0         0 |      0         0       0        0  same
TOTAL (23 modules)                             0       538       0        0           |      0       538       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py check --refs` over the 21 files of this encoding: srcrefs check: 372 src: lines, 67 runs, 79 locators, 0 problems.
`l4 run` shows no error or warning on any file, and the total of assertions satisfied is 538, with none failed or refused.
No test is meant to fail, so there is no `expected_red`.

## What would need doing before this encoding is worth relying on

- A lawyer to read it against the official text and rule on the marginal readings above (M1, M2, M3, M5, M6, M7, M8, the flat-negative and scope-limit branches) and on G1 (the six months), G2, G3, G17, G34 and QB.
- The questions the Act leaves to other laws to be answered in Commons and fed in: the Limitation Act 1959 period, the Minister's orders under s 7(6)(b) and (c), the meaning of "bill of lading", "sea waybill" and "ship's delivery order" in the Bills of Lading Act 1992, section 3 of the Carriage by Air Act 1988, section 39 of the Companies Act 1967, the Limited Liability Partnerships Act 2005, and section 2(2) of the Unfair Contract Terms Act 1977.
  I raised no ledger entry for them: I may write only under the deposit folder.
- A rule for how an `Interpretation Act` count of months from a day is to be done, which would settle 1 July 2002 (G1); the answer belongs in that row, not here.
- A trace-based model of s 3(2)(b), if the human reading of ruling (d) wants one (G34).
- The seat form to be tried on the website, since it has not been.
- A re-run of `check.sh` on the stable `l4` when one ships, and a re-copy of the Interpretation Act modules if they change.
