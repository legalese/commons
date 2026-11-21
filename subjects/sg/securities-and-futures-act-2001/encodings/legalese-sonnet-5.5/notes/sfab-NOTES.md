# NOTES (sfab): Securities and Futures Act 2001 (Singapore), Part 12 (market conduct), ss 196 to 238

Part agent `sfab`: lines 34173 to 37498 of `inputs/SFA2001.txt`.
Layer 1 is the law, objectively (`sfab-*.l4`); layer 2 is the seat (`sfab-seat.l4`, `sfab-cases-seat.l4`).
Every claim below says how it was checked; the counts are produced by `work/audit/*.py` from the modules and the text, not typed by hand.

## Edition encoded

This is an encoding of the Securities and Futures Act 2001 (Singapore), 2020 Revised Edition, as the Singapore Statutes Online (SSO) informal consolidation "version in force from 29/6/2026 to 20/10/2026", retrieved 2026-10-09 (`inputs/SOURCES.md` has its hashes), carrying the amendments its amendment marks show.
The file `inputs/SFA2001.txt` is a PDF turned into plain text: it is a rendering and not the official text (SSO's terms, clause 8, say so).
A later consolidation may exist and was not read.
Nothing in this folder is "verified against the official text": every quotation was checked, by script, against the rendering and against nothing else.
The encoding is of that text only, and of this part of it: Part 12 (market conduct), sections 196 to 238, lines 34173 to 37498 of the rendering.
Nothing here suggests that the Singapore Government or the Attorney-General's Chambers has endorsed, checked or is associated with this work.

The modules of this part are `sfab-division-1.l4` (ss 196 to 204), `sfab-division-2.l4` (ss 205 to 212), `sfab-insider-1.l4` (ss 213 to 217), `sfab-insider-2.l4` (ss 218 to 221), `sfab-insider-3.l4` (ss 222 to 231), `sfab-civil.l4` (ss 232 to 236) and `sfab-attributed.l4` (ss 236A to 237; s 238 is inert), each with a test file `sfab-tests-<name>.l4`, one hand-written integration test `sfab-tests-integration.l4`, and the seat layer `sfab-seat.l4` with `sfab-cases-seat.l4`.
`sfab-attributed.l4` is generated from `work/gen/gen_attributed.py` (not shipped) so that the three families of Division 5 (corporations, partnerships, officers) read alike; the other modules are written from macro sources in `work/src/` (not shipped) that quote the text mechanically.

## Seat

The seat is the individual's, as the brief fixes it: an individual who is, or is about to become, a director or other officer, an employee or a substantial shareholder of a corporation (including the holding company of a group that has listed members), or who holds, deals in, issues or offers securities, debentures or units, asking on facts they can state what the Act requires or lets them do (what they must disclose and by when, what dealing is forbidden, what follows if it is not done).
Assumed, not ruled: the individual is whoever holds an interest in securities or offers them, since the Act is addressed to market participants and to the Authority.
There is no seat for the Authority, the Minister or the court.
Their powers in Part 12 (the Authority's action for a civil penalty, the court's orders, the Public Prosecutor's consent) are encoded in layer 1 for what they decide, and appear in layer 2 only as what they mean to the individual ("may the Authority bring an action against me ...", "what is the most I can be ordered to pay ...").

## Where PLAN.md and the brief differ

The brief governs.
These are the places I found where `inputs/PLAN.md` and the brief say different things, and what I did:

1. PLAN section 6 (the sfab row) says "Seams: none found" and "no call of s 3, s 4 or s 4A by number".
   The brief says to start the seam list from `inputs/XREFS.md`, which lists citations in my ranges of s 2, s 331, s 335 and s 341, and the text of ss 197, 202 and 230 speaks of persons "associated with" another, which is s 3.
   I took each of these as an INPUT named for the fact (see Seams (sfab)); I did not import `sfa-associates.l4`.
2. PLAN section 3.3 gives `s 2(1) "debenture"` as a keel function to call, and section 4.2 repeats it.
   My modules take "the instrument is a debenture as section 2(1) defines it" as a `MAYBE BOOLEAN` input instead of calling that function: the caller passes the keel's answer (JUST TRUE, JUST FALSE or NOTHING) and NOTHING stays NOTHING; the only keel function my modules call is `s 2(1) "securities-based derivatives contract"` (`sfab-division-1.l4`, s 196A(b) and (c)) and the period counters of `sfa-periods.l4`.
   My modules IMPORT three keel modules: `sfa-core`, `sfa-definitions-products` and `sfa-periods`.
   The other keel modules sit in the folder and are not imported because nothing in my ranges calls them.
3. PLAN section 8 asks for `## Compared with the earlier pass` and the brief says "only if you have `inputs/NAIVE-EVIDENCE/`": the folder is absent in this sandbox, so that section says so and compares nothing.
4. The brief says an unnamed party in a regulative rule is a core `Party`; every prohibition of Part 12 begins "A person must not ...", so each rule names `Individual "a person"` (a corporation or any other person is the same rule with another core `Party`); the Act names no narrower party.

## Coverage (sfab)

One row per unit of the text: each Part, Division and Subdivision heading, each section's marginal heading, each subsection, paragraph, sub-paragraph, defined term, and each row the text shows repealed or deleted.
The rows were made by script (`work/audit/rows.py`) from the labels the text itself prints (`(1)`, `(1A)`, `(a)`, `(i)`, `(A)`, a curly-quoted defined term at the start of a line) and joined to the `@ref` locator of the function that encodes the row's lines.
A row's lines are its own: from its label to the next label of any level, so that a line is in exactly one row (page furniture and amendment marks belong to the row they sit in).
A row whose covering function (or rule) carries a `-- SPLIT-SITE` or `-- FORK` tag has the disposition `fork` and points at the fork lines (`SS-nnn` split sites and `F-...` forks, in the Fork register below); every other row that has a function is `encoded`.
There is no `out-of-scope` row and no `deferred` row.

### Summary

| disposition | rows |
| --- | --- |
| encoded | 321 |
| fork | 265 |
| inert, reason 1 (not operative: headings) | 69 |
| inert, reason 2 (machinery: s 238, a rule-making power) | 7 |
| inert, reason 3 (text shown repealed or blank) | 0 (these are the next row) |
| repealed or blank in this text | 8 |
| **total rows** | **670** |

### Audit counts

| count | value | how it was made |
| --- | --- | --- |
| lines in the range 34173-37498 | 3326 | `HI - LO + 1` |
| blank lines | 948 | script |
| non-blank lines | 2378 | script |
| of which page furniture ("Informal Consolidation ..." and "2020 Ed. Securities and Futures Act 2001 <page>") | 134 | script |
| of which amendment-mark-only lines ("[4/2017]") | 157 | script |
| text lines (non-blank, not furniture, not a mark) | 2087 | script |
| sections in the range (s 196 to s 238, with the A-suffixed ones) | 58 | `inputs/HEADINGS.md` |
| rows by level: section lead-in (no subsection) 19, subsection 193, paragraph 272, sub-paragraph 94, sub-sub-paragraph 23 | 601 | script |
| rows that are defined terms (31 terms: "debenture", "administer", "defendant" and the rest) | 31 | script |
| marginal-heading rows + Part/Division/Subdivision rows | 58 + 11 | script |
| **rows in the table, before and after** | **663 before, 670 after** | first run of `rows.py`, then after the fixes below |
| rows with no covering function, before and after | 10 before, 0 after | the lead-ins of s 206, s 214(1), s 236B(9), s 236E(9) and paragraphs of ss 200(1), 210(2), 236J(1) and 236J(3) lay outside their function's `@ref` range; the ranges were extended and the lines quoted |
| label lines the sequence check rejected, before and after | 8 before, 1 after | definitions now reset the paragraph level; the one left is the cross-reference "(1A) or 219(1)" at line 35995, which is not a label |
| non-blank lines in no row | 0 | script: every non-blank line of 34173-37498 lies in some row (2378 of 2378 lines are in a row) |
| text lines quoted in a `-- src:` line | 1977 of 2087 | `work/audit/quoted.py`; the 110 unquoted text lines are all inside inert or repealed rows (headings, Division titles, s 238), none inside an encoded or fork row |

### Rows

| # | row | lines | disposition | L4 name, or the reason | forks |
| --- | --- | --- | --- | --- | --- |
| 1 | PART 12 | 34173-34175 | inert | reason 1: not operative (a heading) |  |
| 2 | Division 1 — Prohibited Conduct — Capital Markets Products | 34177-34179 | inert | reason 1: not operative (a heading) |  |
| 3 | s 196 (marginal heading) | 34181-34181 | inert | reason 1: not operative (a heading) |  |
| 4 | s 196 | 34183-34183 | encoded | `s 196 this Division applies to the act` |  |
| 5 | s 196(a) | 34185-34185 | fork | `s 196(a) this Division applies to the act occurring within Singapore` | SS-001 |
| 6 | s 196(a)(i) | 34187-34189 | fork | `s 196(a) this Division applies to the act occurring within Singapore` | SS-001 |
| 7 | s 196(a)(ii) | 34191-34192 | fork | `s 196(a) this Division applies to the act occurring within Singapore` | SS-001 |
| 8 | s 196(a)(iii) | 34194-34196 | fork | `s 196(a) this Division applies to the act occurring within Singapore` | SS-001 |
| 9 | s 196(a)(iv) | 34198-34200 | fork | `s 196(a) this Division applies to the act occurring within Singapore` | SS-001 |
| 10 | s 196(a)(v) | 34202-34203 | fork | `s 196(a) this Division applies to the act occurring within Singapore` | SS-001 |
| 11 | s 196(a)(vi) | 34205-34207 | fork | `s 196(a) this Division applies to the act occurring within Singapore` | SS-001 |
| 12 | s 196(a)(vii) | 34209-34210 | fork | `s 196(a) this Division applies to the act occurring within Singapore` | SS-001 |
| 13 | s 196(b) | 34212-34212 | fork | `s 196(b) this Division applies to the act occurring outside Singapore` | SS-002 |
| 14 | s 196(b)(i) | 34214-34216 | fork | `s 196(b) this Division applies to the act occurring outside Singapore` | SS-002 |
| 15 | s 196(b)(ii) | 34218-34225 | fork | `s 196(b) this Division applies to the act occurring outside Singapore` | SS-002 |
| 16 | s 196(b)(iii) | 34227-34229 | fork | `s 196(b) this Division applies to the act occurring outside Singapore` | SS-002 |
| 17 | s 196(b)(iv) | 34231-34233 | fork | `s 196(b) this Division applies to the act occurring outside Singapore` | SS-002 |
| 18 | s 196(b)(v) | 34235-34235 | fork | `s 196(b) this Division applies to the act occurring outside Singapore` | SS-002 |
| 19 | s 196(b)(vi) | 34237-34239 | fork | `s 196(b) this Division applies to the act occurring outside Singapore` | SS-002 |
| 20 | s 196(b)(vii) | 34241-34244 | fork | `s 196(b) this Division applies to the act occurring outside Singapore` | SS-002 |
| 21 | s 196A (marginal heading) | 34246-34246 | inert | reason 1: not operative (a heading) |  |
| 22 | s 196A | 34248-34248 | encoded | `s 196A(a) the instrument is a debenture for the purposes of this Division` |  |
| 23 | s 196A(a) "debenture" | 34250-34253 | encoded | `s 196A(a) the instrument is a debenture for the purposes of this Division` |  |
| 24 | s 196A(b) | 34255-34259 | encoded | `s 196A(b) the contract is a securities-based derivatives contract of the corporation` |  |
| 25 | s 196A(c) | 34261-34270 | encoded | `s 196A(c) the contract is a securities-based derivatives contract of the business trust` |  |
| 26 | s 197 (marginal heading) | 34272-34272 | inert | reason 1: not operative (a heading) |  |
| 27 | s 197(1) | 34274-34278 | fork | `s 197(1) the person's conduct contravenes the bar on conduct done to create a false or misleading appearance`; `s 197(1) a person must not act for the purpose of creating a false or misleading appearance` | SS-003, SS-004 |
| 28 | s 197(1)(a) | 34280-34281 | fork | `s 197(1) the person's conduct contravenes the bar on conduct done to create a false or misleading appearance`; `s 197(1) a person must not act for the purpose of creating a false or misleading appearance` | SS-003, SS-004 |
| 29 | s 197(1)(b) | 34283-34286 | fork | `s 197(1) the person's conduct contravenes the bar on conduct done to create a false or misleading appearance`; `s 197(1) a person must not act for the purpose of creating a false or misleading appearance` | SS-003, SS-004 |
| 30 | s 197(1A) | 34288-34293 | fork | `s 197(1A) the person's conduct contravenes the bar on conduct that creates a false or misleading appearance knowingly or recklessly`; `s 197(1A) a person must not do a thing that creates a false or misleading appearance knowingly or recklessly` | SS-005, SS-006 |
| 31 | s 197(1A)(a) | 34295-34298 | fork | `s 197(1A) the person's conduct contravenes the bar on conduct that creates a false or misleading appearance knowingly or recklessly`; `s 197(1A) a person must not do a thing that creates a false or misleading appearance knowingly or recklessly` | SS-005, SS-006 |
| 32 | s 197(1A)(b) | 34300-34305 | fork | `s 197(1A) the person's conduct contravenes the bar on conduct that creates a false or misleading appearance knowingly or recklessly`; `s 197(1A) a person must not do a thing that creates a false or misleading appearance knowingly or recklessly` | SS-005, SS-006 |
| 33 | s 197(2) | 34307-34308 | fork | `s 197(2) the person's conduct contravenes the bar on maintaining, inflating or depressing the market price`; `s 197(2) a person must not maintain, inflate or depress the market price by a sale with no change in beneficial ownership or a fictitious transaction` | SS-007 |
| 34 | s 197(2)(a) | 34310-34312 | fork | `s 197(2) the person's conduct contravenes the bar on maintaining, inflating or depressing the market price`; `s 197(2) a person must not maintain, inflate or depress the market price by a sale with no change in beneficial ownership or a fictitious transaction` | SS-007 |
| 35 | s 197(2)(b) | 34314-34316 | fork | `s 197(2) the person's conduct contravenes the bar on maintaining, inflating or depressing the market price`; `s 197(2) a person must not maintain, inflate or depress the market price by a sale with no change in beneficial ownership or a fictitious transaction` | SS-007 |
| 36 | s 197(3) | 34318-34325 | encoded | `s 197(3) the person's purpose is presumed to be to create a false or misleading appearance of active trading` |  |
| 37 | s 197(3)(a) | 34327-34331 | encoded | `s 197(3)(a) the person's purpose is presumed by reason of a transaction with no change in beneficial ownership` |  |
| 38 | s 197(3)(b) | 34333-34341 | encoded | `s 197(3)(b) the person's purpose is presumed by reason of an offer to sell matched by an offer to purchase` |  |
| 39 | s 197(3)(c) | 34343-34353 | encoded | `s 197(3)(c) the person's purpose is presumed by reason of an offer to purchase matched by an offer to sell` |  |
| 40 | s 197(4) | 34355-34361 | encoded | `s 197(4) the presumption under subsection (3) is rebutted` |  |
| 41 | s 197(5) | 34363-34369 | encoded | `s 197(5) the purchase or sale does not involve a change in the beneficial ownership` |  |
| 42 | s 197(5)(a) | 34371-34372 | encoded | `s 197(5) the purchase or sale does not involve a change in the beneficial ownership` |  |
| 43 | s 197(5)(b) | 34374-34377 | encoded | `s 197(5) the purchase or sale does not involve a change in the beneficial ownership` |  |
| 44 | s 197(6) | 34379-34388 | fork | `s 197(6) the defendant has the defence to a contravention of subsection (2)` | SS-008 |
| 45 | s 197(7) | 34390-34391 | encoded | `s 197(7) the act is within the reference to a transaction of purchase or sale in subsection (3)(a)` |  |
| 46 | s 197(7)(a) | 34393-34394 | encoded | `s 197(7) the act is within the reference to a transaction of purchase or sale in subsection (3)(a)` |  |
| 47 | s 197(7)(b) | 34396-34400 | encoded | `s 197(7) the act is within the reference to a transaction of purchase or sale in subsection (3)(a)` |  |
| 48 | s 198 (marginal heading) | 34402-34403 | inert | reason 1: not operative (a heading) |  |
| 49 | s 198(1) | 34405-34419 | fork | `s 198(1) the person's transactions contravene the bar on market manipulation in securities of a corporation`; `s 198(1) a person must not carry out 2 or more transactions in a corporation's securities with the intent to induce others to deal` | SS-009 |
| 50 | s 198(2) | 34421-34432 | fork | `s 198(2) the person's transactions contravene the bar on market manipulation in securities of a business trust`; `s 198(2) a person must not carry out 2 or more transactions in a business trust's securities with the intent to induce others to deal` | SS-010 |
| 51 | s 198(3) | 34434-34434 | encoded | `s 198(3)(a) the act is within the reference to transactions in securities or securities-based derivatives contracts of a corporation` |  |
| 52 | s 198(3)(a) | 34436-34437 | encoded | `s 198(3)(a) the act is within the reference to transactions in securities or securities-based derivatives contracts of a corporation` |  |
| 53 | s 198(3)(a)(i) | 34439-34441 | encoded | `s 198(3)(a) the act is within the reference to transactions in securities or securities-based derivatives contracts of a corporation` |  |
| 54 | s 198(3)(a)(ii) | 34443-34447 | encoded | `s 198(3)(a) the act is within the reference to transactions in securities or securities-based derivatives contracts of a corporation` |  |
| 55 | s 198(3)(b) | 34449-34450 | encoded | `s 198(3)(b) the act is within the reference to transactions in securities or securities-based derivatives contracts of a business trust` |  |
| 56 | s 198(3)(b)(i) | 34452-34454 | encoded | `s 198(3)(b) the act is within the reference to transactions in securities or securities-based derivatives contracts of a business trust` |  |
| 57 | s 198(3)(b)(ii) | 34456-34465 | encoded | `s 198(3)(b) the act is within the reference to transactions in securities or securities-based derivatives contracts of a business trust` |  |
| 58 | s 199 (marginal heading) | 34467-34467 | inert | reason 1: not operative (a heading) |  |
| 59 | s 199 | 34469-34471 | fork | `s 199 the person's statement or information contravenes the bar on false or misleading statements`; `s 199 a person must not make a false or misleading statement likely to induce dealing or move the price` | SS-011, SS-012 |
| 60 | s 199(a) | 34473-34475 | fork | `s 199 the person's statement or information contravenes the bar on false or misleading statements`; `s 199 a person must not make a false or misleading statement likely to induce dealing or move the price` | SS-011, SS-012 |
| 61 | s 199(b) | 34477-34479 | fork | `s 199 the person's statement or information contravenes the bar on false or misleading statements`; `s 199 a person must not make a false or misleading statement likely to induce dealing or move the price` | SS-011, SS-012 |
| 62 | s 199(c) | 34481-34487 | fork | `s 199 the person's statement or information contravenes the bar on false or misleading statements`; `s 199 a person must not make a false or misleading statement likely to induce dealing or move the price` | SS-011, SS-012 |
| 63 | s 199(d) | 34489-34490 | fork | `s 199 the person's statement or information contravenes the bar on false or misleading statements`; `s 199 a person must not make a false or misleading statement likely to induce dealing or move the price` | SS-011, SS-012 |
| 64 | s 199(e) | 34492-34496 | fork | `s 199 the person's statement or information contravenes the bar on false or misleading statements`; `s 199 a person must not make a false or misleading statement likely to induce dealing or move the price` | SS-011, SS-012 |
| 65 | s 200 (marginal heading) | 34498-34499 | inert | reason 1: not operative (a heading) |  |
| 66 | s 200(1) | 34501-34501 | fork | `s 200(1) the person's conduct contravenes the bar on fraudulently inducing a person to deal`; `s 200(1) a person must not fraudulently induce another person to deal in capital markets products` | SS-013 |
| 67 | s 200(1)(a) | 34503-34505 | fork | `s 200(1) the person's conduct contravenes the bar on fraudulently inducing a person to deal`; `s 200(1) a person must not fraudulently induce another person to deal in capital markets products` | SS-013 |
| 68 | s 200(1)(b) | 34507-34507 | fork | `s 200(1) the person's conduct contravenes the bar on fraudulently inducing a person to deal`; `s 200(1) a person must not fraudulently induce another person to deal in capital markets products` | SS-013 |
| 69 | s 200(1)(c) | 34509-34514 | fork | `s 200(1) the person's conduct contravenes the bar on fraudulently inducing a person to deal`; `s 200(1) a person must not fraudulently induce another person to deal in capital markets products` | SS-013 |
| 70 | s 200(1)(d) | 34516-34523 | fork | `s 200(1) the person's conduct contravenes the bar on fraudulently inducing a person to deal`; `s 200(1) a person must not fraudulently induce another person to deal in capital markets products` | SS-013 |
| 71 | s 200(2) | 34525-34530 | fork | `s 200(2) the defendant has the defence to a contravention constituted by recording or storing information` | SS-014 |
| 72 | s 200(3) | 34532-34545 | encoded | `s 200(3) the public accountant's opinion is admissible as evidence of the financial position of the company` |  |
| 73 | s 201 (marginal heading) | 34547-34547 | inert | reason 1: not operative (a heading) |  |
| 74 | s 201 | 34549-34550 | fork | `s 201 the person's conduct contravenes the bar on manipulative and deceptive devices`; `s 201 a person must not employ a manipulative or deceptive device in connection with a subscription, purchase or sale` | SS-015 |
| 75 | s 201(a) | 34552-34552 | fork | `s 201 the person's conduct contravenes the bar on manipulative and deceptive devices`; `s 201 a person must not employ a manipulative or deceptive device in connection with a subscription, purchase or sale` | SS-015 |
| 76 | s 201(b) | 34554-34556 | fork | `s 201 the person's conduct contravenes the bar on manipulative and deceptive devices`; `s 201 a person must not employ a manipulative or deceptive device in connection with a subscription, purchase or sale` | SS-015 |
| 77 | s 201(c) | 34558-34562 | fork | `s 201 the person's conduct contravenes the bar on manipulative and deceptive devices`; `s 201 a person must not employ a manipulative or deceptive device in connection with a subscription, purchase or sale` | SS-015 |
| 78 | s 201(d) | 34564-34568 | fork | `s 201 the person's conduct contravenes the bar on manipulative and deceptive devices`; `s 201 a person must not employ a manipulative or deceptive device in connection with a subscription, purchase or sale` | SS-015 |
| 79 | s 201A (marginal heading) | 34570-34570 | inert | reason 1: not operative (a heading) |  |
| 80 | s 201A(1) | 34572-34579 | fork | `s 201A(1) the person's execution of an order contravenes the bar on bucketing a derivatives contract`; `s 201A(1) a person must not knowingly execute an order for a derivatives contract without effecting it in good faith` | SS-016 |
| 81 | s 201A(2) | 34581-34587 | fork | `s 201A(2) the person's execution of an order contravenes the bar on bucketing a spot foreign exchange contract`; `s 201A(2) a person must not knowingly execute an order for a spot foreign exchange contract without effecting it in good faith` | SS-017 |
| 82 | s 201B (marginal heading) | 34589-34589 | inert | reason 1: not operative (a heading) |  |
| 83 | s 201B | 34591-34591 | fork | `s 201B the person's conduct contravenes the bar on manipulating the price of derivatives contracts and cornering`; `s 201B a person must not manipulate the price of a derivatives contract or its underlying thing, or corner an underlying thing` | SS-018 |
| 84 | s 201B(a) | 34593-34596 | fork | `s 201B the person's conduct contravenes the bar on manipulating the price of derivatives contracts and cornering`; `s 201B a person must not manipulate the price of a derivatives contract or its underlying thing, or corner an underlying thing` | SS-018 |
| 85 | s 201B(b) | 34598-34601 | fork | `s 201B the person's conduct contravenes the bar on manipulating the price of derivatives contracts and cornering`; `s 201B a person must not manipulate the price of a derivatives contract or its underlying thing, or corner an underlying thing` | SS-018 |
| 86 | s 202 (marginal heading) | 34603-34603 | inert | reason 1: not operative (a heading) |  |
| 87 | s 202(1) | 34605-34608 | fork | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions`; `s 202(1) a person must not circulate a statement or information about the price effect of an illegal transaction` | SS-019, SS-020 |
| 88 | s 202(1)(a) | 34610-34623 | fork | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions`; `s 202(1) a person must not circulate a statement or information about the price effect of an illegal transaction` | SS-019, SS-020 |
| 89 | s 202(1)(b) | 34625-34634 | fork | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions`; `s 202(1) a person must not circulate a statement or information about the price effect of an illegal transaction` | SS-019, SS-020 |
| 90 | s 202(1)(c) | 34636-34644 | fork | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions`; `s 202(1) a person must not circulate a statement or information about the price effect of an illegal transaction` | SS-019, SS-020 |
| 91 | s 202(1)(d) | 34646-34662 | fork | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions`; `s 202(1) a person must not circulate a statement or information about the price effect of an illegal transaction` | SS-019, SS-020 |
| 92 | s 202(2) | 34664-34664 | encoded | `s 202(2) a condition in subsection (1) is satisfied` |  |
| 93 | s 202(2)(a) | 34666-34669 | encoded | `s 202(2) a condition in subsection (1) is satisfied` |  |
| 94 | s 202(2)(b) | 34671-34678 | encoded | `s 202(2) a condition in subsection (1) is satisfied` |  |
| 95 | s 203 (marginal heading) | 34680-34680 | inert | reason 1: not operative (a heading) |  |
| 96 | s 203(1) | 34682-34693 | fork | `s 203(1) the person's failure to notify the approved exchange contravenes the bar on failing to disclose`; `s 203(1) the person to whom subsection (1) applies must notify the approved exchange of the information it requires to be disclosed` | SS-021, SS-022 |
| 97 | s 203(2) | 34695-34695 | encoded | `s 203(2) subsection (1) applies to the person` |  |
| 98 | s 203(2)(a) | 34697-34699 | encoded | `s 203(2) subsection (1) applies to the person` |  |
| 99 | s 203(2)(b) | 34701-34706 | encoded | `s 203(2) subsection (1) applies to the person` |  |
| 100 | s 203(2)(c) | 34708-34712 | encoded | `s 203(2) subsection (1) applies to the person` |  |
| 101 | s 203(3) | 34714-34717 | encoded | `s 203(3) the contravention of subsection (1) is an offence` |  |
| 102 | s 204 (marginal heading) | 34719-34719 | inert | reason 1: not operative (a heading) |  |
| 103 | s 204(1) | 34721-34724 | fork | `s 204(1) the penalty on conviction for contravening a provision of Division 1`; `s 204(1) the person is guilty of an offence` | SS-023 |
| 104 | s 204(2) | 34726-34728 | encoded | `s 204(2) proceedings for an offence in respect of the contravention are barred` |  |
| 105 | s 204(2)(a) | 34730-34731 | encoded | `s 204(2) proceedings for an offence in respect of the contravention are barred` |  |
| 106 | s 204(2)(b) | 34733-34739 | encoded | `s 204(2) proceedings for an offence in respect of the contravention are barred` |  |
| 107 | Division 2 — Prohibited Conduct — Financial Benchmarks | 34741-34741 | inert | reason 1: not operative (a heading) |  |
| 108 | s 205 (marginal heading) | 34743-34743 | inert | reason 1: not operative (a heading) |  |
| 109 | s 205 | 34745-34745 | encoded | `s 205 this Division applies to the act` |  |
| 110 | s 205(a) | 34747-34749 | fork | `s 205(a) this Division applies to the act occurring within Singapore` | SS-024 |
| 111 | s 205(b) | 34751-34757 | fork | `s 205(b) this Division applies to the act occurring outside Singapore` | SS-025 |
| 112 | s 206 (marginal heading) | 34759-34759 | inert | reason 1: not operative (a heading) |  |
| 113 | s 206 | 34761-34761 | encoded | `s 206 "administer" the activity is to administer the financial benchmark` |  |
| 114 | s 206 "administer" | 34763-34764 | encoded | `s 206 "administer" the activity is to administer the financial benchmark` |  |
| 115 | s 206 "international body" | 34766-34769 | encoded | `s 206 "international body" the body is an international body` |  |
| 116 | s 206 "public authority" | 34771-34771 | encoded | `s 206 "public authority" the body is a public authority` |  |
| 117 | s 206 "public authority"(a) | 34773-34777 | encoded | `s 206 "public authority" the body is a public authority` |  |
| 118 | s 206 "public authority"(b) | 34779-34784 | encoded | `s 206 "public authority" the body is a public authority` |  |
| 119 | s 206 "public authority"(c) | 34786-34789 | encoded | `s 206 "public authority" the body is a public authority` |  |
| 120 | s 207 (marginal heading) | 34791-34791 | inert | reason 1: not operative (a heading) |  |
| 121 | s 207(1) | 34793-34800 | fork | `s 207(1) the person's conduct contravenes the bar on conduct done to create a false appearance as to a financial benchmark`; `s 207(1) a person must not act for the purpose of creating a false or misleading appearance as to a financial benchmark` | SS-026, SS-027 |
| 122 | s 207(2) | 34802-34809 | fork | `s 207(2) the person's conduct contravenes the bar on conduct that creates a false appearance as to a financial benchmark knowingly or recklessly`; `s 207(2) a person must not do a thing that creates a false or misleading appearance as to a financial benchmark knowingly or recklessly` | SS-028, SS-029 |
| 123 | s 207(2)(a) | 34811-34814 | fork | `s 207(2) the person's conduct contravenes the bar on conduct that creates a false appearance as to a financial benchmark knowingly or recklessly`; `s 207(2) a person must not do a thing that creates a false or misleading appearance as to a financial benchmark knowingly or recklessly` | SS-028, SS-029 |
| 124 | s 207(2)(b) | 34816-34821 | fork | `s 207(2) the person's conduct contravenes the bar on conduct that creates a false appearance as to a financial benchmark knowingly or recklessly`; `s 207(2) a person must not do a thing that creates a false or misleading appearance as to a financial benchmark knowingly or recklessly` | SS-028, SS-029 |
| 125 | s 208 (marginal heading) | 34823-34823 | inert | reason 1: not operative (a heading) |  |
| 126 | s 208 | 34825-34828 | encoded | `s 208 section 207 does not apply to the thing done` |  |
| 127 | s 208(a) | 34830-34830 | encoded | `s 208 section 207 does not apply to the thing done` |  |
| 128 | s 208(b) | 34832-34834 | encoded | `s 208 section 207 does not apply to the thing done` |  |
| 129 | s 208(c) | 34836-34839 | encoded | `s 208 section 207 does not apply to the thing done` |  |
| 130 | s 209 (marginal heading) | 34841-34841 | inert | reason 1: not operative (a heading) |  |
| 131 | s 209 | 34843-34846 | fork | `s 209 the person's statement contravenes the bar on false or misleading statements to a benchmark administrator`; `s 209 a person must not make a false or misleading statement to a person administering a financial benchmark` | SS-030, SS-031 |
| 132 | s 209(a) | 34848-34850 | fork | `s 209 the person's statement contravenes the bar on false or misleading statements to a benchmark administrator`; `s 209 a person must not make a false or misleading statement to a person administering a financial benchmark` | SS-030, SS-031 |
| 133 | s 209(b) | 34852-34862 | fork | `s 209 the person's statement contravenes the bar on false or misleading statements to a benchmark administrator`; `s 209 a person must not make a false or misleading statement to a person administering a financial benchmark` | SS-030, SS-031 |
| 134 | s 210 (marginal heading) | 34864-34864 | inert | reason 1: not operative (a heading) |  |
| 135 | s 210(1) | 34866-34871 | fork | `s 210(1) the penalty on conviction for contravening a provision of Division 2`; `s 210(1) the person is guilty of an offence` | SS-032 |
| 136 | s 210(2) | 34873-34875 | encoded | `s 210(2) proceedings for an offence in respect of the contravention are barred` |  |
| 137 | s 210(2)(a) | 34877-34878 | encoded | `s 210(2) proceedings for an offence in respect of the contravention are barred` |  |
| 138 | s 210(2)(b) | 34880-34886 | encoded | `s 210(2) proceedings for an offence in respect of the contravention are barred` |  |
| 139 | s 211 (marginal heading) | 34888-34887 | inert | reason 1: not operative (a heading) |  |
| 140 | s 212 (marginal heading) | 34888-34887 | inert | reason 1: not operative (a heading) |  |
| 141 | s 211 | 34888-34888 | repealed or blank in this text | the text shows `[Repealed by Act 4 of 2017]` |  |
| 142 | s 212 | 34890-34890 | repealed or blank in this text | the text shows `[Repealed by Act 4 of 2017]` |  |
| 143 | Division 3 — Insider Trading | 34892-34892 | inert | reason 1: not operative (a heading) |  |
| 144 | s 213 (marginal heading) | 34894-34894 | inert | reason 1: not operative (a heading) |  |
| 145 | s 213 | 34896-34896 | encoded | `s 213 this Division applies to the act` |  |
| 146 | s 213(a) | 34898-34898 | fork | `s 213(a) this Division applies to the act occurring within Singapore` | SS-033 |
| 147 | s 213(a)(i) | 34900-34902 | fork | `s 213(a) this Division applies to the act occurring within Singapore` | SS-033 |
| 148 | s 213(a)(ii) | 34904-34908 | fork | `s 213(a) this Division applies to the act occurring within Singapore` | SS-033 |
| 149 | s 213(a)(iii) | 34910-34912 | fork | `s 213(a) this Division applies to the act occurring within Singapore` | SS-033 |
| 150 | s 213(a)(iv) | 34914-34915 | fork | `s 213(a) this Division applies to the act occurring within Singapore` | SS-033 |
| 151 | s 213(a)(v) | 34917-34917 | fork | `s 213(a) this Division applies to the act occurring within Singapore` | SS-033 |
| 152 | s 213(a)(v)(A) | 34919-34920 | fork | `s 213(a) this Division applies to the act occurring within Singapore` | SS-033 |
| 153 | s 213(a)(v)(B) | 34922-34922 | fork | `s 213(a) this Division applies to the act occurring within Singapore` | SS-033 |
| 154 | s 213(b) | 34924-34924 | fork | `s 213(b) this Division applies to the act occurring outside Singapore` | SS-034 |
| 155 | s 213(b)(i) | 34926-34928 | fork | `s 213(b) this Division applies to the act occurring outside Singapore` | SS-034 |
| 156 | s 213(b)(ii) | 34930-34933 | fork | `s 213(b) this Division applies to the act occurring outside Singapore` | SS-034 |
| 157 | s 213(b)(iii) | 34935-34937 | fork | `s 213(b) this Division applies to the act occurring outside Singapore` | SS-034 |
| 158 | s 213(b)(iv) | 34939-34940 | fork | `s 213(b) this Division applies to the act occurring outside Singapore` | SS-034 |
| 159 | s 213(b)(v) | 34942-34942 | fork | `s 213(b) this Division applies to the act occurring outside Singapore` | SS-034 |
| 160 | s 213(b)(v)(A) | 34944-34945 | fork | `s 213(b) this Division applies to the act occurring outside Singapore` | SS-034 |
| 161 | s 213(b)(v)(B) | 34947-34949 | fork | `s 213(b) this Division applies to the act occurring outside Singapore` | SS-034 |
| 162 | s 214 (marginal heading) | 34951-34951 | inert | reason 1: not operative (a heading) |  |
| 163 | s 214(1) | 34952-34952 | encoded | `s 214(1) "CIS unit" the thing is a CIS unit` |  |
| 164 | s 214(1) "Collective Investment Scheme unit / CIS unit" | 34953-34953 | encoded | `s 214(1) "CIS unit" the thing is a CIS unit` |  |
| 165 | s 214(1) "Collective Investment Scheme unit / CIS unit"(a) | 34954-34962 | encoded | `s 214(1) "CIS unit" the thing is a CIS unit` |  |
| 166 | s 214(1) "Collective Investment Scheme unit / CIS unit"(b) | 34964-34964 | encoded | `s 214(1) "CIS unit" the thing is a CIS unit` |  |
| 167 | s 214(1) "Collective Investment Scheme unit / CIS unit"(b)(i) | 34966-34969 | encoded | `s 214(1) "CIS unit" the thing is a CIS unit` |  |
| 168 | s 214(1) "Collective Investment Scheme unit / CIS unit"(b)(ii) | 34971-34975 | encoded | `s 214(1) "CIS unit" the thing is a CIS unit` |  |
| 169 | s 214(1) "Collective Investment Scheme unit / CIS unit"(b)(ii)(A) | 34977-34978 | encoded | `s 214(1) "CIS unit" the thing is a CIS unit` |  |
| 170 | s 214(1) "Collective Investment Scheme unit / CIS unit"(b)(ii)(B) | 34980-34981 | encoded | `s 214(1) "CIS unit" the thing is a CIS unit` |  |
| 171 | s 214(1) "debenture" | 34983-34986 | encoded | `s 214(1) "debenture" the instrument is a debenture for the purposes of this Division` |  |
| 172 | s 214(1) "financial performance" | 34988-34991 | encoded | `s 214(1) "financial performance" the matter is the financial performance of a business trust` |  |
| 173 | s 214(1) "information" | 34993-34993 | encoded | `s 214(1) "information" the matter is information` |  |
| 174 | s 214(1) "information"(a) | 34995-34997 | encoded | `s 214(1) "information" the matter is information` |  |
| 175 | s 214(1) "information"(b) | 34999-35000 | encoded | `s 214(1) "information" the matter is information` |  |
| 176 | s 214(1) "information"(c) | 35002-35006 | encoded | `s 214(1) "information" the matter is information` |  |
| 177 | s 214(1) "information"(c)(i) | 35008-35008 | encoded | `s 214(1) "information" the matter is information` |  |
| 178 | s 214(1) "information"(c)(ii) | 35010-35012 | encoded | `s 214(1) "information" the matter is information` |  |
| 179 | s 214(1) "information"(c)(iii) | 35014-35014 | repealed or blank in this text | the text shows `[Deleted by Act 4 of 2017]` |  |
| 180 | s 214(1) "information"(d) | 35016-35017 | encoded | `s 214(1) "information" the matter is information` |  |
| 181 | s 214(1) "information"(e) | 35019-35019 | encoded | `s 214(1) "information" the matter is information` |  |
| 182 | s 214(1) "information"(e)(i) | 35021-35025 | encoded | `s 214(1) "information" the matter is information` |  |
| 183 | s 214(1) "information"(e)(ii) | 35027-35030 | encoded | `s 214(1) "information" the matter is information` |  |
| 184 | s 214(1) "information"(f) | 35032-35032 | encoded | `s 214(1) "information" the matter is information` |  |
| 185 | s 214(1) "persons who commonly invest" | 35034-35040 | encoded | `s 214(1) "persons who commonly invest" the persons are persons who commonly invest` |  |
| 186 | s 214(1) "purchase" | 35042-35047 | encoded | `s 214(1) "purchase" the act is a purchase of a securities-based derivatives contract or CIS unit` |  |
| 187 | s 214(1) "sell" | 35049-35054 | fork | `s 214(1) "sell" the act is a sale of a securities-based derivatives contract or CIS unit` | F-sell |
| 188 | s 214(1) "sell"(a) | 35056-35056 | fork | `s 214(1) "sell" the act is a sale of a securities-based derivatives contract or CIS unit` | F-sell |
| 189 | s 214(1) "sell"(b) | 35058-35061 | fork | `s 214(1) "sell" the act is a sale of a securities-based derivatives contract or CIS unit` | F-sell |
| 190 | s 214(1) "trust property" | 35063-35066 | encoded | `s 214(1) "trust property" the thing is trust property` |  |
| 191 | s 214(2) | 35068-35068 | encoded | `s 214(2)(a) the contract is a securities-based derivatives contract of the corporation` |  |
| 192 | s 214(2)(a) | 35070-35074 | encoded | `s 214(2)(a) the contract is a securities-based derivatives contract of the corporation` |  |
| 193 | s 214(2)(b) | 35076-35082 | encoded | `s 214(2)(b) the contract is a securities-based derivatives contract of the business trust` |  |
| 194 | s 215 (marginal heading) | 35084-35084 | inert | reason 1: not operative (a heading) |  |
| 195 | s 215 | 35086-35087 | encoded | `s 215 the information is generally available` |  |
| 196 | s 215(a) | 35089-35089 | encoded | `s 215 the information is generally available` |  |
| 197 | s 215(b) | 35091-35091 | encoded | `s 215 the information is generally available` |  |
| 198 | s 215(b)(i) | 35093-35095 | encoded | `s 215 the information is generally available` |  |
| 199 | s 215(b)(i)(A) | 35097-35099 | encoded | `s 215 the information is generally available` |  |
| 200 | s 215(b)(i)(B) | 35101-35108 | encoded | `s 215 the information is generally available` |  |
| 201 | s 215(b)(i)(C) | 35110-35112 | encoded | `s 215 the information is generally available` |  |
| 202 | s 215(b)(ii) | 35114-35116 | encoded | `s 215 the information is generally available` |  |
| 203 | s 215(c) | 35118-35119 | encoded | `s 215 the information is generally available` |  |
| 204 | s 215(c)(i) | 35121-35121 | encoded | `s 215 the information is generally available` |  |
| 205 | s 215(c)(ii) | 35123-35126 | encoded | `s 215 the information is generally available` |  |
| 206 | s 216 (marginal heading) | 35128-35129 | inert | reason 1: not operative (a heading) |  |
| 207 | s 216 | 35131-35137 | encoded | `s 216 a reasonable person would be taken to expect the information to have a material effect on the price or value` |  |
| 208 | s 216(a) | 35139-35140 | encoded | `s 216 a reasonable person would be taken to expect the information to have a material effect on the price or value` |  |
| 209 | s 216(b) | 35142-35145 | encoded | `s 216 a reasonable person would be taken to expect the information to have a material effect on the price or value` |  |
| 210 | s 217 (marginal heading) | 35147-35148 | inert | reason 1: not operative (a heading) |  |
| 211 | s 217(1) | 35150-35161 | encoded | `s 217(1) trading is taken to be permitted on the organised market` |  |
| 212 | s 217(2) | 35163-35167 | encoded | `s 217(2) the person is taken to procure the act or omission by the other person` |  |
| 213 | s 218 (marginal heading) | 35169-35170 | inert | reason 1: not operative (a heading) |  |
| 214 | s 218(1) | 35172-35172 | fork | `s 218(1) subsections (2), (3), (4), (5) and (6) apply to the connected person`; `s 218 subsection (2) and (3) apply to the person under subsection (1) or (1A)` | SS-035 |
| 215 | s 218(1)(a) | 35174-35180 | fork | `s 218(1) subsections (2), (3), (4), (5) and (6) apply to the connected person`; `s 218 subsection (2) and (3) apply to the person under subsection (1) or (1A)` | SS-035 |
| 216 | s 218(1)(b) | 35182-35183 | fork | `s 218(1) subsections (2), (3), (4), (5) and (6) apply to the connected person`; `s 218 subsection (2) and (3) apply to the person under subsection (1) or (1A)` | SS-035 |
| 217 | s 218(1)(b)(i) | 35185-35185 | fork | `s 218(1) subsections (2), (3), (4), (5) and (6) apply to the connected person`; `s 218 subsection (2) and (3) apply to the person under subsection (1) or (1A)` | SS-035 |
| 218 | s 218(1)(b)(ii) | 35187-35194 | fork | `s 218(1) subsections (2), (3), (4), (5) and (6) apply to the connected person`; `s 218 subsection (2) and (3) apply to the person under subsection (1) or (1A)` | SS-035 |
| 219 | s 218(1A) | 35196-35196 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 220 | s 218(1A)(a) | 35198-35198 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 221 | s 218(1A)(a)(i) | 35200-35204 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 222 | s 218(1A)(a)(ii) | 35206-35207 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 223 | s 218(1A)(a)(ii)(A) | 35209-35212 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 224 | s 218(1A)(a)(ii)(B) | 35214-35215 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 225 | s 218(1A)(b) | 35217-35217 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 226 | s 218(1A)(b)(i) | 35219-35226 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 227 | s 218(1A)(b)(ii) | 35228-35236 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 228 | s 218(1A)(c) | 35238-35239 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 229 | s 218(1A)(c)(i) | 35241-35241 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 230 | s 218(1A)(c)(ii) | 35243-35244 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 231 | s 218(1A)(c)(ii)(A) | 35246-35254 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 232 | s 218(1A)(c)(ii)(B) | 35256-35263 | fork | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | SS-036 |
| 233 | s 218(2) | 35265-35266 | fork | `s 218(2) the connected person's dealing or procuring contravenes the bar`; `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-037, SS-038 |
| 234 | s 218(2)(a) | 35268-35269 | fork | `s 218(2) the connected person's dealing or procuring contravenes the bar`; `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-037, SS-038 |
| 235 | s 218(2)(a)(i) | 35271-35272 | fork | `s 218(2) the connected person's dealing or procuring contravenes the bar`; `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-037, SS-038 |
| 236 | s 218(2)(a)(ii) | 35274-35275 | fork | `s 218(2) the connected person's dealing or procuring contravenes the bar`; `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-037, SS-038 |
| 237 | s 218(2)(b) | 35277-35279 | fork | `s 218(2) the connected person's dealing or procuring contravenes the bar`; `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-037, SS-038 |
| 238 | s 218(2)(b)(i) | 35281-35282 | fork | `s 218(2) the connected person's dealing or procuring contravenes the bar`; `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-037, SS-038 |
| 239 | s 218(2)(b)(ii) | 35284-35287 | fork | `s 218(2) the connected person's dealing or procuring contravenes the bar`; `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-037, SS-038 |
| 240 | s 218(3) | 35289-35293 | fork | `s 218(3) the connected person's communication of the information contravenes the bar`; `s 218(3) the connected person must not communicate the inside information to a person likely to deal` | SS-039, SS-040, SS-041 |
| 241 | s 218(3)(a) | 35295-35296 | fork | `s 218(3) the connected person's communication of the information contravenes the bar`; `s 218(3) the connected person must not communicate the inside information to a person likely to deal` | SS-039, SS-040, SS-041 |
| 242 | s 218(3)(a)(i) | 35298-35302 | fork | `s 218(3) the connected person's communication of the information contravenes the bar`; `s 218(3) the connected person must not communicate the inside information to a person likely to deal` | SS-039, SS-040, SS-041 |
| 243 | s 218(3)(a)(ii) | 35304-35305 | fork | `s 218(3) the connected person's communication of the information contravenes the bar`; `s 218(3) the connected person must not communicate the inside information to a person likely to deal` | SS-039, SS-040, SS-041 |
| 244 | s 218(3)(b) | 35307-35309 | fork | `s 218(3) the connected person's communication of the information contravenes the bar`; `s 218(3) the connected person must not communicate the inside information to a person likely to deal` | SS-039, SS-040, SS-041 |
| 245 | s 218(3)(b)(i) | 35311-35312 | fork | `s 218(3) the connected person's communication of the information contravenes the bar`; `s 218(3) the connected person must not communicate the inside information to a person likely to deal` | SS-039, SS-040, SS-041 |
| 246 | s 218(3)(b)(ii) | 35314-35317 | fork | `s 218(3) the connected person's communication of the information contravenes the bar`; `s 218(3) the connected person must not communicate the inside information to a person likely to deal` | SS-039, SS-040, SS-041 |
| 247 | s 218(4) | 35319-35322 | encoded | `s 218(4) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 248 | s 218(4)(a) | 35324-35325 | encoded | `s 218(4) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 249 | s 218(4)(b) | 35327-35330 | encoded | `s 218(4) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 250 | s 218(4)(c) | 35332-35332 | encoded | `s 218(4) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 251 | s 218(4)(d) | 35334-35340 | encoded | `s 218(4) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 252 | s 218(4A) | 35342-35346 | encoded | `s 218(4A) the presumption in subsection (4B) applies` |  |
| 253 | s 218(4A)(a) | 35348-35353 | encoded | `s 218(4A) the presumption in subsection (4B) applies` |  |
| 254 | s 218(4A)(b) | 35355-35359 | encoded | `s 218(4A) the presumption in subsection (4B) applies` |  |
| 255 | s 218(4B) | 35361-35362 | encoded | `s 218(4B) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 256 | s 218(4B)(a) | 35364-35364 | encoded | `s 218(4B) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 257 | s 218(4B)(b) | 35366-35367 | encoded | `s 218(4B) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 258 | s 218(4B)(b)(i) | 35369-35372 | encoded | `s 218(4B) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 259 | s 218(4B)(b)(ii) | 35374-35380 | encoded | `s 218(4B) the connected person is presumed to have known that the information was not generally available and might have a material effect` |  |
| 260 | s 218(5) | 35382-35382 | encoded | `s 218(5)(a) the person is a connected person` |  |
| 261 | s 218(5)(a) "connected person" | 35384-35386 | encoded | `s 218(5)(a) the person is a connected person` |  |
| 262 | s 218(5)(b) | 35388-35388 | encoded | `s 218(5)(b) the person is connected to the corporation` |  |
| 263 | s 218(5)(b)(i) | 35390-35391 | encoded | `s 218(5)(b) the person is connected to the corporation` |  |
| 264 | s 218(5)(b)(ii) | 35393-35394 | encoded | `s 218(5)(b) the person is connected to the corporation` |  |
| 265 | s 218(5)(b)(iii) | 35396-35398 | encoded | `s 218(5)(b) the person is connected to the corporation` |  |
| 266 | s 218(5)(b)(iii)(A) | 35400-35408 | encoded | `s 218(5)(b) the person is connected to the corporation` |  |
| 267 | s 218(5)(b)(iii)(B) | 35410-35413 | encoded | `s 218(5)(b) the person is connected to the corporation` |  |
| 268 | s 218(6) "officer" | 35415-35416 | encoded | `s 218(6) the person is an officer of the corporation for the purposes of subsection (5)` |  |
| 269 | s 218(6)(a) | 35418-35418 | encoded | `s 218(6) the person is an officer of the corporation for the purposes of subsection (5)` |  |
| 270 | s 218(6)(b) | 35420-35421 | encoded | `s 218(6) the person is an officer of the corporation for the purposes of subsection (5)` |  |
| 271 | s 218(6)(c) | 35423-35423 | encoded | `s 218(6) the person is an officer of the corporation for the purposes of subsection (5)` |  |
| 272 | s 218(6)(d) | 35425-35425 | encoded | `s 218(6) the person is an officer of the corporation for the purposes of subsection (5)` |  |
| 273 | s 218(6)(e) | 35427-35429 | encoded | `s 218(6) the person is an officer of the corporation for the purposes of subsection (5)` |  |
| 274 | s 219 (marginal heading) | 35431-35432 | inert | reason 1: not operative (a heading) |  |
| 275 | s 219(1) | 35434-35434 | fork | `s 219(1) subsections (2) and (3) apply to the insider` | SS-042 |
| 276 | s 219(1)(a) | 35436-35442 | fork | `s 219(1) subsections (2) and (3) apply to the insider` | SS-042 |
| 277 | s 219(1)(b) | 35444-35444 | fork | `s 219(1) subsections (2) and (3) apply to the insider` | SS-042 |
| 278 | s 219(1)(b)(i) | 35446-35446 | fork | `s 219(1) subsections (2) and (3) apply to the insider` | SS-042 |
| 279 | s 219(1)(b)(ii) | 35448-35458 | fork | `s 219(1) subsections (2) and (3) apply to the insider` | SS-042 |
| 280 | s 219(2) | 35460-35460 | fork | `s 219(2) the insider's dealing or procuring contravenes the bar`; `s 219(2) the insider must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-043, SS-044 |
| 281 | s 219(2)(a) | 35462-35465 | fork | `s 219(2) the insider's dealing or procuring contravenes the bar`; `s 219(2) the insider must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-043, SS-044 |
| 282 | s 219(2)(b) | 35467-35472 | fork | `s 219(2) the insider's dealing or procuring contravenes the bar`; `s 219(2) the insider must not deal in, or procure dealing in, the securities while in possession of inside information` | SS-043, SS-044 |
| 283 | s 219(3) | 35474-35478 | fork | `s 219(3) the insider's communication of the information contravenes the bar`; `s 219(3) the insider must not communicate the inside information to a person likely to deal` | SS-045, SS-046, SS-047 |
| 284 | s 219(3)(a) | 35480-35483 | fork | `s 219(3) the insider's communication of the information contravenes the bar`; `s 219(3) the insider must not communicate the inside information to a person likely to deal` | SS-045, SS-046, SS-047 |
| 285 | s 219(3)(b) | 35485-35490 | fork | `s 219(3) the insider's communication of the information contravenes the bar`; `s 219(3) the insider must not communicate the inside information to a person likely to deal` | SS-045, SS-046, SS-047 |
| 286 | s 220 (marginal heading) | 35492-35492 | inert | reason 1: not operative (a heading) |  |
| 287 | s 220(1) | 35494-35497 | encoded | `s 220(1) the prosecution or claimant must prove that the accused or defendant intended to use the information in contravention` |  |
| 288 | s 220(1A) | 35498-35501 | encoded | `s 220(1) the prosecution or claimant must prove that the accused or defendant intended to use the information in contravention` |  |
| 289 | s 220(2) | 35503-35514 | encoded | `s 220(2) the prosecution or claimant must prove the absence of facts that would preclude the act from being a contravention by virtue of sections 222 to 230` |  |
| 290 | s 221 (marginal heading) | 35516-35516 | inert | reason 1: not operative (a heading) |  |
| 291 | s 221(1) | 35518-35521 | fork | `s 221(1) the penalty on conviction for contravening section 218 or 219`; `s 221(1) the person is guilty of an offence` | SS-048 |
| 292 | s 221(2) | 35523-35524 | encoded | `s 221(2) proceedings for an offence in respect of the contravention are barred` |  |
| 293 | s 221(2)(a) | 35526-35527 | encoded | `s 221(2) proceedings for an offence in respect of the contravention are barred` |  |
| 294 | s 221(2)(b) | 35529-35535 | encoded | `s 221(2) proceedings for an offence in respect of the contravention are barred` |  |
| 295 | s 222 (marginal heading) | 35537-35538 | inert | reason 1: not operative (a heading) |  |
| 296 | s 222 | 35540-35546 | encoded | `s 222 sections 218(2) and 219(2) do not apply to the redemption of units` |  |
| 297 | s 222(a) | 35548-35549 | encoded | `s 222 sections 218(2) and 219(2) do not apply to the redemption of units` |  |
| 298 | s 222(b) | 35551-35554 | encoded | `s 222 sections 218(2) and 219(2) do not apply to the redemption of units` |  |
| 299 | s 223 (marginal heading) | 35556-35556 | inert | reason 1: not operative (a heading) |  |
| 300 | s 223(1) | 35558-35558 | encoded | `s 223(1) sections 218(2) and 219(2) do not apply to the underwriting act` |  |
| 301 | s 223(1)(a) | 35560-35562 | encoded | `s 223(1) sections 218(2) and 219(2) do not apply to the underwriting act` |  |
| 302 | s 223(1)(b) | 35564-35564 | encoded | `s 223(1) sections 218(2) and 219(2) do not apply to the underwriting act` |  |
| 303 | s 223(1)(c) | 35566-35570 | encoded | `s 223(1) sections 218(2) and 219(2) do not apply to the underwriting act` |  |
| 304 | s 223(2) | 35572-35574 | encoded | `s 223(2) sections 218(3) and 219(3) do not apply to the underwriting communication` |  |
| 305 | s 223(2)(a) | 35576-35579 | encoded | `s 223(2) sections 218(3) and 219(3) do not apply to the underwriting communication` |  |
| 306 | s 223(2)(b) | 35581-35586 | encoded | `s 223(2) sections 218(3) and 219(3) do not apply to the underwriting communication` |  |
| 307 | s 223(2)(b)(i) | 35588-35590 | encoded | `s 223(2) sections 218(3) and 219(3) do not apply to the underwriting communication` |  |
| 308 | s 223(2)(b)(ii) | 35592-35595 | encoded | `s 223(2) sections 218(3) and 219(3) do not apply to the underwriting communication` |  |
| 309 | s 224 (marginal heading) | 35597-35597 | inert | reason 1: not operative (a heading) |  |
| 310 | s 224(1) | 35599-35609 | encoded | `s 224(1) sections 218(2) and 219(2) do not apply to the purchase` |  |
| 311 | s 224(2) | 35611-35616 | encoded | `s 224(2) sections 218(2) and 219(2) do not apply to the sale` |  |
| 312 | s 225 (marginal heading) | 35618-35619 | inert | reason 1: not operative (a heading) |  |
| 313 | s 225 | 35621-35624 | encoded | `s 225 sections 218(3) and 219(3) do not apply to the communication` |  |
| 314 | s 226 (marginal heading) | 35626-35626 | inert | reason 1: not operative (a heading) |  |
| 315 | s 226(1) | 35628-35628 | encoded | `s 226(1)(a) the corporation is taken to possess the information that its officer possesses` |  |
| 316 | s 226(1)(a) | 35630-35633 | encoded | `s 226(1)(a) the corporation is taken to possess the information that its officer possesses` |  |
| 317 | s 226(1)(b) | 35635-35639 | encoded | `s 226(1)(b) the corporation is presumed to know or ought reasonably to know the matter or thing` |  |
| 318 | s 226(2) | 35641-35643 | encoded | `s 226(2) the corporation does not contravene section 218(2) or 219(2) by reason of its officer's information` |  |
| 319 | s 226(2)(a) | 35645-35646 | encoded | `s 226(2) the corporation does not contravene section 218(2) or 219(2) by reason of its officer's information` |  |
| 320 | s 226(2)(b) | 35648-35657 | encoded | `s 226(2) the corporation does not contravene section 218(2) or 219(2) by reason of its officer's information` |  |
| 321 | s 226(2)(c) | 35659-35660 | encoded | `s 226(2) the corporation does not contravene section 218(2) or 219(2) by reason of its officer's information` |  |
| 322 | s 227 (marginal heading) | 35662-35663 | inert | reason 1: not operative (a heading) |  |
| 323 | s 227(1) | 35665-35665 | encoded | `s 227(1)(a) the partner is taken to possess the information that another partner, an employee or a manager possesses` |  |
| 324 | s 227(1)(a) | 35667-35668 | encoded | `s 227(1)(a) the partner is taken to possess the information that another partner, an employee or a manager possesses` |  |
| 325 | s 227(1)(a)(i) | 35670-35674 | encoded | `s 227(1)(a) the partner is taken to possess the information that another partner, an employee or a manager possesses` |  |
| 326 | s 227(1)(a)(ii) | 35676-35681 | encoded | `s 227(1)(a) the partner is taken to possess the information that another partner, an employee or a manager possesses` |  |
| 327 | s 227(1)(b) | 35683-35690 | encoded | `s 227(1)(b) every partner is presumed to know or ought reasonably to know the matter or thing` |  |
| 328 | s 227(2) | 35692-35702 | encoded | `s 227(2) the partners do not contravene section 218(2) or 219(2) by reason of one partner's, manager's or employee's information` |  |
| 329 | s 227(2)(a) | 35704-35706 | encoded | `s 227(2) the partners do not contravene section 218(2) or 219(2) by reason of one partner's, manager's or employee's information` |  |
| 330 | s 227(2)(a)(i) | 35708-35712 | encoded | `s 227(2) the partners do not contravene section 218(2) or 219(2) by reason of one partner's, manager's or employee's information` |  |
| 331 | s 227(2)(a)(ii) | 35714-35717 | encoded | `s 227(2) the partners do not contravene section 218(2) or 219(2) by reason of one partner's, manager's or employee's information` |  |
| 332 | s 227(2)(b) | 35719-35725 | encoded | `s 227(2) the partners do not contravene section 218(2) or 219(2) by reason of one partner's, manager's or employee's information` |  |
| 333 | s 227(2)(c) | 35727-35728 | encoded | `s 227(2) the partners do not contravene section 218(2) or 219(2) by reason of one partner's, manager's or employee's information` |  |
| 334 | s 227(3) | 35730-35735 | encoded | `s 227(3) the partner does not contravene section 218(2) or 219(2) merely because the partner is taken to possess the information` |  |
| 335 | s 228 (marginal heading) | 35737-35738 | inert | reason 1: not operative (a heading) |  |
| 336 | s 228 | 35740-35752 | encoded | `s 228 the individual does not contravene section 218(2) or 219(2) merely because the individual is aware of the individual's own intentions or activities` |  |
| 337 | s 229 (marginal heading) | 35754-35754 | inert | reason 1: not operative (a heading) |  |
| 338 | s 229(1) | 35756-35764 | encoded | `s 229(1) the corporation does not contravene section 218(2) or 219(2) merely because the corporation is aware of its own intentions or activities` |  |
| 339 | s 229(2) | 35766-35774 | encoded | `s 229(2) the corporation does not contravene section 218(2) or 219(2) merely because an officer is aware of the corporation's intentions or activities` |  |
| 340 | s 229(3) | 35776-35779 | encoded | `s 229(3) subsection (2) applies to the officer's awareness` |  |
| 341 | s 229(4) | 35781-35790 | encoded | `s 229(4) the person does not contravene section 218(2) or 219(2) by dealing on behalf of a corporation merely because the person is aware of the corporation's intentions or activities` |  |
| 342 | s 229(5) | 35792-35799 | encoded | `s 229(5) subsection (4) applies to the person's awareness` |  |
| 343 | s 230 (marginal heading) | 35801-35802 | inert | reason 1: not operative (a heading) |  |
| 344 | s 230(1) | 35804-35809 | encoded | `s 230(1) the holder or representative does not contravene section 218(2) or 219(2) by an unsolicited transaction for a principal` |  |
| 345 | s 230(1)(a) | 35811-35815 | encoded | `s 230(1) the holder or representative does not contravene section 218(2) or 219(2) by an unsolicited transaction for a principal` |  |
| 346 | s 230(1)(b) | 35817-35820 | encoded | `s 230(1) the holder or representative does not contravene section 218(2) or 219(2) by an unsolicited transaction for a principal` |  |
| 347 | s 230(1)(c) | 35822-35825 | encoded | `s 230(1) the holder or representative does not contravene section 218(2) or 219(2) by an unsolicited transaction for a principal` |  |
| 348 | s 230(2) | 35827-35828 | encoded | `s 230(2) section 230 does not affect the application of sections 218(2) and 219(2) to the principal` |  |
| 349 | s 231 (marginal heading) | 35830-35830 | inert | reason 1: not operative (a heading) |  |
| 350 | s 231(1) | 35832-35836 | fork | `s 231(1) the person has the parity of information defence to the contravention by dealing or procuring` | SS-049 |
| 351 | s 231(1)(a) | 35838-35843 | fork | `s 231(1) the person has the parity of information defence to the contravention by dealing or procuring` | SS-049 |
| 352 | s 231(1)(b) | 35845-35847 | fork | `s 231(1) the person has the parity of information defence to the contravention by dealing or procuring` | SS-049 |
| 353 | s 231(2) | 35849-35852 | fork | `s 231(2) the person has the parity of information defence to the contravention by communicating` | SS-050 |
| 354 | s 231(2)(a) | 35854-35856 | fork | `s 231(2) the person has the parity of information defence to the contravention by communicating` | SS-050 |
| 355 | s 231(2)(b) | 35858-35860 | fork | `s 231(2) the person has the parity of information defence to the contravention by communicating` | SS-050 |
| 356 | Division 4 — Civil Liability | 35862-35862 | inert | reason 1: not operative (a heading) |  |
| 357 | s 232 (marginal heading) | 35864-35864 | inert | reason 1: not operative (a heading) |  |
| 358 | s 232(1) | 35866-35870 | fork | `s 232(1) the Authority may bring an action in a court against the person to seek an order for a civil penalty` | SS-051, SS-052 |
| 359 | s 232(2) | 35872-35875 | fork | `s 232(2) the court may make an order against the person for the payment of a civil penalty`; `s 232(2) the highest civil penalty the court may order` | SS-053 |
| 360 | s 232(2)(a) | 35877-35877 | fork | `s 232(2)(a) three times the profit gained or the loss avoided` | F-232-2a |
| 361 | s 232(2)(a)(i) | 35879-35880 | fork | `s 232(2)(a) three times the profit gained or the loss avoided` | F-232-2a |
| 362 | s 232(2)(a)(ii) | 35882-35883 | fork | `s 232(2)(a) three times the profit gained or the loss avoided` | F-232-2a |
| 363 | s 232(2)(b) | 35885-35887 | encoded | `s 232(2)(b) the fixed amount in the cap` |  |
| 364 | s 232(3) | 35889-35893 | encoded | `s 232(3) the lowest civil penalty the court may order`; `s 232(2) and (3) the civil penalty ordered is within the limits` |  |
| 365 | s 232(3)(a) | 35895-35896 | encoded | `s 232(3) the lowest civil penalty the court may order`; `s 232(2) and (3) the civil penalty ordered is within the limits` |  |
| 366 | s 232(3)(b) | 35898-35900 | encoded | `s 232(3) the lowest civil penalty the court may order`; `s 232(2) and (3) the civil penalty ordered is within the limits` |  |
| 367 | s 232(4) | 35902-35908 | fork | `s 232(4) the court may make the order on the terms agreed between the Authority and the defendant despite subsections (2) and (3)` | SS-054 |
| 368 | s 232(5) | 35910-35913 | encoded | `s 232(5) section 232 does not prevent the Authority from entering into the agreement` |  |
| 369 | s 232(6) | 35915-35920 | encoded | `s 232(6) the civil penalty is to be treated as a judgment debt due to the Government`; `s 232(6) the person on whom a civil penalty is imposed must pay it into the Consolidated Fund` |  |
| 370 | s 232(7) | 35922-35929 | fork | `s 232(7) the Authority may recover the civil penalty on behalf of the Government as though it were a judgment debt due to the Authority` | SS-055 |
| 371 | s 232(8) | 35931-35937 | encoded | `s 232(8) a defence available in a prosecution is also available to the defendant to the action` |  |
| 372 | s 233 (marginal heading) | 35939-35940 | inert | reason 1: not operative (a heading) |  |
| 373 | s 233(1) | 35942-35944 | encoded | `s 233(1) the action under section 232 is barred because 6 years have expired from the date of the contravention` |  |
| 374 | s 233(2) | 35946-35950 | encoded | `s 233(2) the action under section 232 is barred because the person has been convicted or acquitted` |  |
| 375 | s 233(3) | 35952-35955 | encoded | `s 233(3) the action under section 232 must be stayed`; `s 233(3) the stayed action under section 232 may thereafter be continued` |  |
| 376 | s 233(3)(a) | 35957-35959 | encoded | `s 233(3)(a) the person has been discharged in respect of the contravention and the discharge does not amount to an acquittal` |  |
| 377 | s 233(3)(b) | 35961-35962 | encoded | `s 233(3)(b) the charge against the person in respect of the contravention has been withdrawn` |  |
| 378 | s 234 (marginal heading) | 35964-35964 | inert | reason 1: not operative (a heading) |  |
| 379 | s 234(1) | 35966-35973 | fork | `s 234(1) the contravening person is liable to pay compensation to the claimant` | SS-056, SS-057, SS-058 |
| 380 | s 234(1)(a) | 35975-35980 | encoded | `s 234(1)(a) the claimant had been dealing in capital markets products of the same description contemporaneously with the contravention` |  |
| 381 | s 234(1)(b) | 35982-35982 | encoded | `s 234(1)(b) the claimant had suffered loss by reason of the difference in price` |  |
| 382 | s 234(1)(b)(i) | 35984-35986 | encoded | `s 234(1)(b) the claimant had suffered loss by reason of the difference in price` |  |
| 383 | s 234(1)(b)(ii) | 35988-35990 | encoded | `s 234(1)(b) the claimant had suffered loss by reason of the difference in price` |  |
| 384 | s 234(1)(b)(ii)(A) | 35992-35996 | encoded | `s 234(1)(b)(ii)(A) the price to compare is the price had the information been generally available` |  |
| 385 | s 234(1)(b)(ii)(B) | 35998-36001 | encoded | `s 234(1)(b)(ii)(B) the price to compare is the price had the contravention not occurred` |  |
| 386 | s 234(1A) | 36003-36008 | fork | `s 234(1A) the contravening person is liable to pay compensation to the claimant whether or not the person gained a profit or avoided a loss` | SS-059 |
| 387 | s 234(1A)(a) | 36010-36012 | encoded | `s 234(1A)(a) the contravening person has contravened section 199, 200 or 201 by a false statement or a concealed fact` |  |
| 388 | s 234(1A)(a)(i) | 36014-36016 | encoded | `s 234(1A)(a) the contravening person has contravened section 199, 200 or 201 by a false statement or a concealed fact` |  |
| 389 | s 234(1A)(a)(ii) | 36018-36018 | encoded | `s 234(1A)(a) the contravening person has contravened section 199, 200 or 201 by a false statement or a concealed fact` |  |
| 390 | s 234(1A)(b) | 36020-36020 | encoded | `s 234(1A)(b) the claimant relied on the statement or was ignorant of the fact, and suffered loss` |  |
| 391 | s 234(1A)(b)(i) | 36022-36029 | encoded | `s 234(1A)(b) the claimant relied on the statement or was ignorant of the fact, and suffered loss` |  |
| 392 | s 234(1A)(b)(ii) | 36031-36033 | encoded | `s 234(1A)(b) the claimant relied on the statement or was ignorant of the fact, and suffered loss` |  |
| 393 | s 234(2) | 36035-36045 | fork | `s 234(2) the amount of compensation under subsection (1)` | F-234-2 |
| 394 | s 234(2A) | 36047-36048 | encoded | `s 234(2A) the amount of compensation under subsection (1A)` |  |
| 395 | s 234(2A)(a) | 36050-36054 | encoded | `s 234(2A) the amount of compensation under subsection (1A)` |  |
| 396 | s 234(2A)(a)(i) | 36056-36065 | fork | `s 234(2A)(a)(i) the amount of the loss referred to in subsection (1)(b)` | F-234-2 |
| 397 | s 234(2A)(a)(ii) | 36067-36083 | fork | `s 234(2A)(a)(ii) the amount of the loss that reasonably results from the claimant's reliance or ignorance` | F-234-2 |
| 398 | s 234(2A)(b) | 36085-36098 | fork | `s 234(2A)(b) the amount of the loss that reasonably results from the claimant's reliance or ignorance in any other case` | F-234-2 |
| 399 | s 234(3) | 36100-36103 | encoded | `s 234(3) a defence available in a prosecution is also available to the defendant to the action` |  |
| 400 | s 234(4) | 36105-36109 | encoded | `s 234(4) the action under section 234 is barred because 6 years have expired from the date of completion of the dealing` |  |
| 401 | s 234(5) | 36111-36114 | encoded | `s 234(5) the court is to take into account the matters in paragraphs (a) to (e)` |  |
| 402 | s 234(5)(a) | 36116-36119 | encoded | `s 234(5)(a) the matter is one the court is to take into account` |  |
| 403 | s 234(5)(b) | 36121-36128 | encoded | `s 234(5)(b) the matter is one the court is to take into account in the case of a contravention effected by a transaction` |  |
| 404 | s 234(5)(c) | 36130-36131 | encoded | `s 234(5)(c) the matter is one the court is to take into account` |  |
| 405 | s 234(5)(d) | 36133-36138 | encoded | `s 234(5)(d) the matter is one the court is to take into account in the case of a contravention under section 203, 218 or 219` |  |
| 406 | s 234(5)(e) | 36140-36143 | encoded | `s 234(5)(e) the matter is one the court is to take into account` |  |
| 407 | s 234(6) "maximum recoverable amount" | 36145-36147 | fork | `s 234(6) the maximum recoverable amount` | F-234-6 |
| 408 | s 234(6)(a) | 36149-36150 | fork | `s 234(6) the maximum recoverable amount` | F-234-6 |
| 409 | s 234(6)(b) | 36152-36162 | fork | `s 234(6) the maximum recoverable amount` | F-234-6 |
| 410 | s 235 (marginal heading) | 36164-36165 | inert | reason 1: not operative (a heading) |  |
| 411 | s 235(1) | 36167-36174 | fork | `s 235(1) no action under section 234 may be brought without the permission of court` | F-235-1 |
| 412 | s 235(1)(a) | 36176-36177 | fork | `s 235(1) no action under section 234 may be brought without the permission of court` | F-235-1 |
| 413 | s 235(1)(b) | 36179-36182 | fork | `s 235(1) no action under section 234 may be brought without the permission of court` | F-235-1 |
| 414 | s 235(2) | 36184-36187 | encoded | `s 235(2) the pending action under section 234 must be stayed`; `s 235(2) the stayed action may thereafter be continued` |  |
| 415 | s 235(2)(a) | 36189-36190 | encoded | `s 235(2) the pending action under section 234 must be stayed`; `s 235(2) the stayed action may thereafter be continued` |  |
| 416 | s 235(2)(b) | 36192-36198 | encoded | `s 235(2) the pending action under section 234 must be stayed`; `s 235(2) the stayed action may thereafter be continued` |  |
| 417 | s 235(3) | 36200-36207 | encoded | `s 235(3) permission under subsection (1) or (2) may be granted`; `s 235(3) the claimant must comply with the court's directions on the filing and proof of the claim` |  |
| 418 | s 236 (marginal heading) | 36209-36209 | inert | reason 1: not operative (a heading) |  |
| 419 | s 236(1) | 36211-36211 | fork | `s 236(1) the relevant court may fix a date on or before which all claimants have to file and prove their claims` | SS-060, SS-061 |
| 420 | s 236(1)(a) | 36213-36213 | fork | `s 236(1) the relevant court may fix a date on or before which all claimants have to file and prove their claims` | SS-060, SS-061 |
| 421 | s 236(1)(b) | 36215-36232 | fork | `s 236(1) the relevant court may fix a date on or before which all claimants have to file and prove their claims` | SS-060, SS-061 |
| 422 | s 236(2) | 36234-36237 | encoded | `s 236(2) the date fixed is not earlier than 3 months from the date the conviction or the order was made final` |  |
| 423 | s 236(3) | 36239-36244 | fork | `s 236(3) the relevant court may make an order against the contravening person to pay compensation to the claimant` | SS-062, SS-063 |
| 424 | s 236(3A) | 36246-36250 | fork | `s 236(3A) the compensation amount ordered is the lesser of paragraphs (a) and (b)`; `s 236(3A) the compensation amount ordered for the claimant` | F-236-3A |
| 425 | s 236(3A)(a) | 36252-36255 | fork | `s 236(3A) the compensation amount ordered is the lesser of paragraphs (a) and (b)`; `s 236(3A) the compensation amount ordered for the claimant` | F-236-3A |
| 426 | s 236(3A)(b) | 36257-36266 | fork | `s 236(3A) the compensation amount ordered is the lesser of paragraphs (a) and (b)`; `s 236(3A) the compensation amount ordered for the claimant` | F-236-3A |
| 427 | s 236(4) | 36268-36268 | encoded | `s 236(4) the conviction is made final` |  |
| 428 | s 236(4)(a) | 36270-36270 | encoded | `s 236(4) the conviction is made final` |  |
| 429 | s 236(4)(b) | 36272-36275 | encoded | `s 236(4) the conviction is made final` |  |
| 430 | s 236(4)(c) | 36277-36279 | encoded | `s 236(4) the conviction is made final` |  |
| 431 | s 236(4)(d) | 36281-36283 | encoded | `s 236(4) the conviction is made final` |  |
| 432 | s 236(5) | 36285-36286 | encoded | `s 236(5) the order imposing a civil penalty is made final` |  |
| 433 | s 236(5)(a) | 36288-36289 | encoded | `s 236(5) the order imposing a civil penalty is made final` |  |
| 434 | s 236(5)(b) | 36291-36291 | encoded | `s 236(5) the order imposing a civil penalty is made final` |  |
| 435 | s 236(5)(c) | 36293-36295 | encoded | `s 236(5) the order imposing a civil penalty is made final` |  |
| 436 | s 236(5)(d) | 36297-36298 | encoded | `s 236(5) the order imposing a civil penalty is made final` |  |
| 437 | Division 5 — Attributed Liability | 36300-36300 | inert | reason 1: not operative (a heading) |  |
| 438 | s 236A (marginal heading) | 36302-36302 | inert | reason 1: not operative (a heading) |  |
| 439 | s 236A | 36304-36304 | encoded | `s 236A "defendant" an individual liable to an order for a civil penalty under section 236H` |  |
| 440 | s 236A "defendant" | 36306-36310 | encoded | `s 236A "defendant corporation" a corporation liable under section 236B or 236C` |  |
| 441 | s 236A "defendant corporation" | 36312-36312 | encoded | `s 236A "defendant partnership" a partnership or limited liability partnership liable under section 236E or 236F` |  |
| 442 | s 236A "defendant corporation"(a) | 36314-36317 | encoded | `s 236A "defendant partnership" a partnership or limited liability partnership liable under section 236E or 236F` |  |
| 443 | s 236A "defendant corporation"(b) | 36319-36320 | encoded | `s 236A "defendant partnership" a partnership or limited liability partnership liable under section 236E or 236F` |  |
| 444 | s 236A "defendant partnership" | 36322-36326 | encoded | `s 236A "partnership" in Subdivision (2) the partnership at the time of the contravention` |  |
| 445 | s 236A "defendant partnership"(a) | 36328-36333 | encoded | `s 236A "partnership" in Subdivision (2) the partnership at the time of the contravention` |  |
| 446 | s 236A "defendant partnership"(b) | 36335-36336 | encoded | `s 236A "partnership" in Subdivision (2) the partnership at the time of the contravention` |  |
| 447 | s 236A "partnership" | 36338-36342 | encoded | `s 236A "partnership" in Subdivision (2) the partnership at the time of the contravention` |  |
| 448 | Subdivision (1) — Corporations | 36344-36344 | inert | reason 1: not operative (a heading) |  |
| 449 | s 236B (marginal heading) | 36346-36347 | inert | reason 1: not operative (a heading) |  |
| 450 | s 236B(1) | 36349-36351 | fork | `s 236B(1) the corporation is guilty of the offence as if it had committed the contravention`; `s 236B(1) the corporation is liable to be proceeded against and punished accordingly` | SS-064 |
| 451 | s 236B(1)(a) | 36353-36353 | fork | `s 236B(1) the corporation is guilty of the offence as if it had committed the contravention`; `s 236B(1) the corporation is liable to be proceeded against and punished accordingly` | SS-064 |
| 452 | s 236B(1)(b) | 36355-36361 | fork | `s 236B(1) the corporation is guilty of the offence as if it had committed the contravention`; `s 236B(1) the corporation is liable to be proceeded against and punished accordingly` | SS-064 |
| 453 | s 236B(2) | 36363-36364 | encoded | `s 236B(2) proceedings against the corporation under subsection (1) are barred` |  |
| 454 | s 236B(2)(a) | 36366-36367 | encoded | `s 236B(2) proceedings against the corporation under subsection (1) are barred` |  |
| 455 | s 236B(2)(b) | 36369-36380 | encoded | `s 236B(2) proceedings against the corporation under subsection (1) are barred` |  |
| 456 | s 236B(3) | 36382-36390 | fork | `s 236B(3) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` | SS-065, SS-066 |
| 457 | s 236B(4) | 36392-36397 | fork | `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty`; `s 236B(4) the highest civil penalty the court may order`; `s 236B(4) the lowest civil penalty the court may order` | SS-067, F-232-2a |
| 458 | s 236B(4)(a) | 36399-36399 | fork | `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty`; `s 236B(4) the highest civil penalty the court may order`; `s 236B(4) the lowest civil penalty the court may order` | SS-067, F-232-2a |
| 459 | s 236B(4)(a)(i) | 36401-36403 | fork | `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty`; `s 236B(4) the highest civil penalty the court may order`; `s 236B(4) the lowest civil penalty the court may order` | SS-067, F-232-2a |
| 460 | s 236B(4)(a)(ii) | 36405-36407 | fork | `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty`; `s 236B(4) the highest civil penalty the court may order`; `s 236B(4) the lowest civil penalty the court may order` | SS-067, F-232-2a |
| 461 | s 236B(4)(b) | 36409-36409 | fork | `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty`; `s 236B(4) the highest civil penalty the court may order`; `s 236B(4) the lowest civil penalty the court may order` | SS-067, F-232-2a |
| 462 | s 236B(5) | 36410-36410 | repealed or blank in this text | the text shows `[Deleted by Act 4 of 2017]` |  |
| 463 | s 236B(6) | 36412-36416 | encoded | `s 236B(6) sections 232(4) to (7) and 233 apply to the action under subsection (3)` |  |
| 464 | s 236B(7) | 36418-36418 | encoded | `s 236B(7) the defence is also available to the corporation in an action under subsection (3)` |  |
| 465 | s 236B(7)(a) | 36420-36421 | encoded | `s 236B(7) the defence is also available to the corporation in an action under subsection (3)` |  |
| 466 | s 236B(7)(b) | 36423-36432 | encoded | `s 236B(7) the defence is also available to the corporation in an action under subsection (3)` |  |
| 467 | s 236B(8) | 36434-36435 | encoded | `s 236B(8) the consent or connivance of the corporation is established` |  |
| 468 | s 236B(8)(a) | 36437-36440 | encoded | `s 236B(8) the consent or connivance of the corporation is established` |  |
| 469 | s 236B(8)(b) | 36442-36445 | encoded | `s 236B(8) the consent or connivance of the corporation is established` |  |
| 470 | s 236B(8)(c) | 36447-36451 | encoded | `s 236B(8) the consent or connivance of the corporation is established` |  |
| 471 | s 236B(9) | 36453-36453 | encoded | `s 236B(9) "board of directors"` |  |
| 472 | s 236B(9) "board of directors" | 36455-36456 | encoded | `s 236B(9) "board of directors"` |  |
| 473 | s 236B(9) "corporate culture" | 36458-36461 | encoded | `s 236B(9) "corporate culture"` |  |
| 474 | s 236B(9) "high managerial agent" | 36463-36468 | encoded | `s 236B(9) "high managerial agent"` |  |
| 475 | s 236C (marginal heading) | 36470-36471 | inert | reason 1: not operative (a heading) |  |
| 476 | s 236C(1) | 36473-36480 | fork | `s 236C(1) the corporation commits a contravention and is liable to an order for a civil penalty` | SS-068 |
| 477 | s 236C(1)(a) | 36482-36482 | fork | `s 236C(1) the corporation commits a contravention and is liable to an order for a civil penalty` | SS-068 |
| 478 | s 236C(1)(b) | 36484-36489 | fork | `s 236C(1) the corporation commits a contravention and is liable to an order for a civil penalty` | SS-068 |
| 479 | s 236C(2) | 36491-36496 | fork | `s 236C(2) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` | SS-069, SS-070 |
| 480 | s 236C(3) | 36498-36502 | fork | `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty`; `s 236C(3) the highest civil penalty the court may order`; `s 236C(3) the lowest civil penalty the court may order` | SS-071, F-232-2a |
| 481 | s 236C(3)(a) | 36504-36504 | fork | `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty`; `s 236C(3) the highest civil penalty the court may order`; `s 236C(3) the lowest civil penalty the court may order` | SS-071, F-232-2a |
| 482 | s 236C(3)(a)(i) | 36506-36508 | fork | `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty`; `s 236C(3) the highest civil penalty the court may order`; `s 236C(3) the lowest civil penalty the court may order` | SS-071, F-232-2a |
| 483 | s 236C(3)(a)(ii) | 36510-36512 | fork | `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty`; `s 236C(3) the highest civil penalty the court may order`; `s 236C(3) the lowest civil penalty the court may order` | SS-071, F-232-2a |
| 484 | s 236C(3)(b) | 36514-36514 | fork | `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty`; `s 236C(3) the highest civil penalty the court may order`; `s 236C(3) the lowest civil penalty the court may order` | SS-071, F-232-2a |
| 485 | s 236C(4) | 36515-36515 | repealed or blank in this text | the text shows `[Deleted by Act 4 of 2017]` |  |
| 486 | s 236C(5) | 36517-36521 | encoded | `s 236C(5) sections 232(4) to (7) and 233 apply to the action under subsection (2)` |  |
| 487 | s 236C(6) | 36523-36533 | encoded | `s 236C(6) the defence is also available to the corporation in an action under subsection (2)` |  |
| 488 | s 236C(7) | 36535-36537 | encoded | `s 236C(7) the matter is one the court is to take into account in deciding negligence` |  |
| 489 | s 236C(7)(a) | 36539-36541 | encoded | `s 236C(7) the matter is one the court is to take into account in deciding negligence` |  |
| 490 | s 236C(7)(b) | 36543-36545 | encoded | `s 236C(7) the matter is one the court is to take into account in deciding negligence` |  |
| 491 | s 236C(7)(c) | 36547-36549 | encoded | `s 236C(7) the matter is one the court is to take into account in deciding negligence` |  |
| 492 | s 236D (marginal heading) | 36551-36552 | inert | reason 1: not operative (a heading) |  |
| 493 | s 236D(1) | 36554-36559 | fork | `s 236D(1) the corporation is liable to pay compensation to the claimant` | SS-072, SS-073, SS-074 |
| 494 | s 236D(1)(a) | 36561-36563 | fork | `s 236D(1) the corporation is liable to pay compensation to the claimant` | SS-072, SS-073, SS-074 |
| 495 | s 236D(1)(b) | 36565-36565 | fork | `s 236D(1) the corporation is liable to pay compensation to the claimant` | SS-072, SS-073, SS-074 |
| 496 | s 236D(1)(b)(i) | 36567-36569 | fork | `s 236D(1) the corporation is liable to pay compensation to the claimant` | SS-072, SS-073, SS-074 |
| 497 | s 236D(1)(b)(ii) | 36571-36573 | fork | `s 236D(1) the corporation is liable to pay compensation to the claimant` | SS-072, SS-073, SS-074 |
| 498 | s 236D(1)(b)(ii)(A) | 36575-36583 | encoded | `s 236D(1)(b)(ii)(A) the price to compare is the price had the information been generally available` |  |
| 499 | s 236D(1)(b)(ii)(B) | 36585-36588 | encoded | `s 236D(1)(b)(ii)(B) the price to compare is the price had the contravention not occurred` |  |
| 500 | s 236D(2) | 36590-36593 | fork | `s 236D(2) the amount of compensation under subsection (1)` | F-234-2 |
| 501 | s 236D(2)(a) | 36595-36596 | fork | `s 236D(2) the amount of compensation under subsection (1)` | F-234-2 |
| 502 | s 236D(2)(b) | 36598-36603 | fork | `s 236D(2) the amount of compensation under subsection (1)` | F-234-2 |
| 503 | s 236D(3) | 36605-36605 | encoded | `s 236D(3) the defence is also available to the corporation in an action under this section` |  |
| 504 | s 236D(3)(a) | 36607-36608 | encoded | `s 236D(3) the defence is also available to the corporation in an action under this section` |  |
| 505 | s 236D(3)(b) | 36610-36617 | encoded | `s 236D(3) the defence is also available to the corporation in an action under this section` |  |
| 506 | s 236D(4) | 36619-36623 | encoded | `s 236D(4) the action under section 236D is barred because 6 years have expired from the date of completion of the dealing` |  |
| 507 | s 236D(5) | 36625-36633 | encoded | `s 236D(5) the court is to take into account the matters in section 234(5)` |  |
| 508 | s 236D(6) "maximum recoverable amount" | 36635-36635 | fork | `s 236D(6) the maximum recoverable amount` | F-234-6 |
| 509 | s 236D(6)(a) | 36637-36638 | fork | `s 236D(6) the maximum recoverable amount` | F-234-6 |
| 510 | s 236D(6)(b) | 36640-36647 | fork | `s 236D(6) the maximum recoverable amount` | F-234-6 |
| 511 | Subdivision (2) — Partnerships and limited liability partnerships | 36649-36649 | inert | reason 1: not operative (a heading) |  |
| 512 | s 236E (marginal heading) | 36651-36653 | inert | reason 1: not operative (a heading) |  |
| 513 | s 236E(1) | 36655-36658 | fork | `s 236E(1) the partnership or limited liability partnership is guilty of the offence as if it had committed the contravention`; `s 236E(1) the partnership or limited liability partnership is liable to be proceeded against and punished accordingly` | SS-075 |
| 514 | s 236E(1)(a) | 36660-36661 | fork | `s 236E(1) the partnership or limited liability partnership is guilty of the offence as if it had committed the contravention`; `s 236E(1) the partnership or limited liability partnership is liable to be proceeded against and punished accordingly` | SS-075 |
| 515 | s 236E(1)(b) | 36663-36671 | fork | `s 236E(1) the partnership or limited liability partnership is guilty of the offence as if it had committed the contravention`; `s 236E(1) the partnership or limited liability partnership is liable to be proceeded against and punished accordingly` | SS-075 |
| 516 | s 236E(2) | 36673-36675 | encoded | `s 236E(2) proceedings against the partnership or limited liability partnership under subsection (1) are barred` |  |
| 517 | s 236E(2)(a) | 36677-36682 | encoded | `s 236E(2) proceedings against the partnership or limited liability partnership under subsection (1) are barred` |  |
| 518 | s 236E(2)(b) | 36684-36692 | encoded | `s 236E(2) proceedings against the partnership or limited liability partnership under subsection (1) are barred` |  |
| 519 | s 236E(3) | 36694-36704 | fork | `s 236E(3) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` | SS-076, SS-077 |
| 520 | s 236E(4) | 36706-36712 | fork | `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236E(4) the highest civil penalty the court may order`; `s 236E(4) the lowest civil penalty the court may order` | SS-078, F-232-2a |
| 521 | s 236E(4)(a) | 36714-36714 | fork | `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236E(4) the highest civil penalty the court may order`; `s 236E(4) the lowest civil penalty the court may order` | SS-078, F-232-2a |
| 522 | s 236E(4)(a)(i) | 36716-36718 | fork | `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236E(4) the highest civil penalty the court may order`; `s 236E(4) the lowest civil penalty the court may order` | SS-078, F-232-2a |
| 523 | s 236E(4)(a)(ii) | 36720-36722 | fork | `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236E(4) the highest civil penalty the court may order`; `s 236E(4) the lowest civil penalty the court may order` | SS-078, F-232-2a |
| 524 | s 236E(4)(b) | 36724-36724 | fork | `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236E(4) the highest civil penalty the court may order`; `s 236E(4) the lowest civil penalty the court may order` | SS-078, F-232-2a |
| 525 | s 236E(5) | 36725-36728 | repealed or blank in this text | the text shows `[Deleted by Act 4 of 2017]` |  |
| 526 | s 236E(6) | 36730-36734 | encoded | `s 236E(6) sections 232(4) to (7) and 233 apply to the action under subsection (3)` |  |
| 527 | s 236E(7) | 36736-36736 | encoded | `s 236E(7) the defence is also available to the partnership or limited liability partnership in an action under subsection (3)` |  |
| 528 | s 236E(7)(a) | 36738-36739 | encoded | `s 236E(7) the defence is also available to the partnership or limited liability partnership in an action under subsection (3)` |  |
| 529 | s 236E(7)(b) | 36741-36748 | encoded | `s 236E(7) the defence is also available to the partnership or limited liability partnership in an action under subsection (3)` |  |
| 530 | s 236E(8) | 36750-36752 | encoded | `s 236E(8) the consent or connivance of the partnership or limited liability partnership is established` |  |
| 531 | s 236E(8)(a) | 36754-36757 | encoded | `s 236E(8) the consent or connivance of the partnership or limited liability partnership is established` |  |
| 532 | s 236E(8)(b) | 36759-36762 | encoded | `s 236E(8) the consent or connivance of the partnership or limited liability partnership is established` |  |
| 533 | s 236E(8)(c) | 36764-36768 | encoded | `s 236E(8) the consent or connivance of the partnership or limited liability partnership is established` |  |
| 534 | s 236E(9) | 36770-36770 | encoded | `s 236E(9) "corporate culture"` |  |
| 535 | s 236E(9) "corporate culture" | 36772-36779 | encoded | `s 236E(9) "corporate culture"` |  |
| 536 | s 236E(9) "executive partners" | 36781-36782 | encoded | `s 236E(9) "executive partners"` |  |
| 537 | s 236E(9) "high managerial agent" | 36784-36790 | encoded | `s 236E(9) "high managerial agent"` |  |
| 538 | s 236F (marginal heading) | 36792-36793 | inert | reason 1: not operative (a heading) |  |
| 539 | s 236F(1) | 36795-36800 | fork | `s 236F(1) the partnership or limited liability partnership commits a contravention and is liable to an order for a civil penalty` | SS-079 |
| 540 | s 236F(1)(a) | 36802-36803 | fork | `s 236F(1) the partnership or limited liability partnership commits a contravention and is liable to an order for a civil penalty` | SS-079 |
| 541 | s 236F(1)(b) | 36805-36811 | fork | `s 236F(1) the partnership or limited liability partnership commits a contravention and is liable to an order for a civil penalty` | SS-079 |
| 542 | s 236F(2) | 36813-36819 | fork | `s 236F(2) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` | SS-080, SS-081 |
| 543 | s 236F(3) | 36821-36829 | fork | `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236F(3) the highest civil penalty the court may order`; `s 236F(3) the lowest civil penalty the court may order` | SS-082, F-232-2a |
| 544 | s 236F(3)(a) | 36831-36831 | fork | `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236F(3) the highest civil penalty the court may order`; `s 236F(3) the lowest civil penalty the court may order` | SS-082, F-232-2a |
| 545 | s 236F(3)(a)(i) | 36833-36835 | fork | `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236F(3) the highest civil penalty the court may order`; `s 236F(3) the lowest civil penalty the court may order` | SS-082, F-232-2a |
| 546 | s 236F(3)(a)(ii) | 36837-36839 | fork | `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236F(3) the highest civil penalty the court may order`; `s 236F(3) the lowest civil penalty the court may order` | SS-082, F-232-2a |
| 547 | s 236F(3)(b) | 36841-36841 | fork | `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236F(3) the highest civil penalty the court may order`; `s 236F(3) the lowest civil penalty the court may order` | SS-082, F-232-2a |
| 548 | s 236F(4) | 36842-36842 | repealed or blank in this text | the text shows `[Deleted by Act 4 of 2017]` |  |
| 549 | s 236F(5) | 36844-36848 | encoded | `s 236F(5) sections 232(4) to (7) and 233 apply to the action under subsection (2)` |  |
| 550 | s 236F(6) | 36850-36856 | encoded | `s 236F(6) the defence is also available to the partnership or limited liability partnership in an action under subsection (2)` |  |
| 551 | s 236F(7) | 36858-36861 | encoded | `s 236F(7) the matter is one the court is to take into account in deciding negligence` |  |
| 552 | s 236F(7)(a) | 36863-36865 | encoded | `s 236F(7) the matter is one the court is to take into account in deciding negligence` |  |
| 553 | s 236F(7)(b) | 36867-36869 | encoded | `s 236F(7) the matter is one the court is to take into account in deciding negligence` |  |
| 554 | s 236F(7)(c) | 36871-36876 | encoded | `s 236F(7) the matter is one the court is to take into account in deciding negligence` |  |
| 555 | s 236G (marginal heading) | 36878-36879 | inert | reason 1: not operative (a heading) |  |
| 556 | s 236G(1) | 36881-36888 | fork | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | SS-083, SS-084, SS-085 |
| 557 | s 236G(1)(a) | 36890-36892 | fork | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | SS-083, SS-084, SS-085 |
| 558 | s 236G(1)(b) | 36894-36894 | fork | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | SS-083, SS-084, SS-085 |
| 559 | s 236G(1)(b)(i) | 36896-36898 | fork | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | SS-083, SS-084, SS-085 |
| 560 | s 236G(1)(b)(ii) | 36900-36902 | fork | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | SS-083, SS-084, SS-085 |
| 561 | s 236G(1)(b)(ii)(A) | 36904-36908 | encoded | `s 236G(1)(b)(ii)(A) the price to compare is the price had the information been generally available` |  |
| 562 | s 236G(1)(b)(ii)(B) | 36910-36913 | encoded | `s 236G(1)(b)(ii)(B) the price to compare is the price had the contravention not occurred` |  |
| 563 | s 236G(2) | 36915-36918 | fork | `s 236G(2) the amount of compensation under subsection (1)` | F-234-2 |
| 564 | s 236G(2)(a) | 36920-36924 | fork | `s 236G(2) the amount of compensation under subsection (1)` | F-234-2 |
| 565 | s 236G(2)(b) | 36926-36931 | fork | `s 236G(2) the amount of compensation under subsection (1)` | F-234-2 |
| 566 | s 236G(3) | 36933-36933 | encoded | `s 236G(3) the defence is also available to the partnership or limited liability partnership in an action under this section` |  |
| 567 | s 236G(3)(a) | 36935-36936 | encoded | `s 236G(3) the defence is also available to the partnership or limited liability partnership in an action under this section` |  |
| 568 | s 236G(3)(b) | 36938-36945 | encoded | `s 236G(3) the defence is also available to the partnership or limited liability partnership in an action under this section` |  |
| 569 | s 236G(4) | 36947-36951 | encoded | `s 236G(4) the action under section 236G is barred because 6 years have expired from the date of completion of the dealing` |  |
| 570 | s 236G(5) | 36953-36958 | encoded | `s 236G(5) the court is to take into account the matters in section 234(5)` |  |
| 571 | s 236G(6) "maximum recoverable amount" | 36960-36960 | fork | `s 236G(6) the maximum recoverable amount` | F-234-6 |
| 572 | s 236G(6)(a) | 36962-36963 | fork | `s 236G(6) the maximum recoverable amount` | F-234-6 |
| 573 | s 236G(6)(b) | 36965-36975 | fork | `s 236G(6) the maximum recoverable amount` | F-234-6 |
| 574 | Subdivision (3) — Officers, partners, etc., of entities | 36977-36977 | inert | reason 1: not operative (a heading) |  |
| 575 | s 236H (marginal heading) | 36979-36979 | inert | reason 1: not operative (a heading) |  |
| 576 | s 236H(1) | 36981-36984 | fork | `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` | SS-086, SS-087 |
| 577 | s 236H(1)(a) | 36986-36992 | fork | `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` | SS-086, SS-087 |
| 578 | s 236H(1)(b) | 36994-37002 | fork | `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` | SS-086, SS-087 |
| 579 | s 236H(2) | 37004-37009 | fork | `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty`; `s 236H(2) the highest civil penalty the court may order`; `s 236H(2) the lowest civil penalty the court may order` | SS-088, F-232-2a |
| 580 | s 236H(2)(a) | 37011-37011 | fork | `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty`; `s 236H(2) the highest civil penalty the court may order`; `s 236H(2) the lowest civil penalty the court may order` | SS-088, F-232-2a |
| 581 | s 236H(2)(a)(i) | 37013-37015 | fork | `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty`; `s 236H(2) the highest civil penalty the court may order`; `s 236H(2) the lowest civil penalty the court may order` | SS-088, F-232-2a |
| 582 | s 236H(2)(a)(ii) | 37017-37019 | fork | `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty`; `s 236H(2) the highest civil penalty the court may order`; `s 236H(2) the lowest civil penalty the court may order` | SS-088, F-232-2a |
| 583 | s 236H(2)(b) | 37021-37026 | fork | `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty`; `s 236H(2) the highest civil penalty the court may order`; `s 236H(2) the lowest civil penalty the court may order` | SS-088, F-232-2a |
| 584 | s 236H(3) | 37028-37028 | repealed or blank in this text | the text shows `[Deleted by Act 4 of 2017]` |  |
| 585 | s 236H(4) | 37030-37034 | encoded | `s 236H(4) sections 232(4) to (7) and 233 apply to the action under subsection (1)` |  |
| 586 | s 236H(5) | 37036-37036 | encoded | `s 236H(5) the defence is also available to the defendant in an action under subsection (1)` |  |
| 587 | s 236H(5)(a) | 37038-37039 | encoded | `s 236H(5) the defence is also available to the defendant in an action under subsection (1)` |  |
| 588 | s 236H(5)(b) | 37041-37047 | encoded | `s 236H(5) the defence is also available to the defendant in an action under subsection (1)` |  |
| 589 | s 236I (marginal heading) | 37049-37049 | inert | reason 1: not operative (a heading) |  |
| 590 | s 236I(1) | 37051-37057 | fork | `s 236I(1) the defendant is liable to pay compensation to the claimant` | SS-089, SS-090, SS-091 |
| 591 | s 236I(1)(a) | 37059-37061 | fork | `s 236I(1) the defendant is liable to pay compensation to the claimant` | SS-089, SS-090, SS-091 |
| 592 | s 236I(1)(b) | 37063-37063 | fork | `s 236I(1) the defendant is liable to pay compensation to the claimant` | SS-089, SS-090, SS-091 |
| 593 | s 236I(1)(b)(i) | 37065-37067 | fork | `s 236I(1) the defendant is liable to pay compensation to the claimant` | SS-089, SS-090, SS-091 |
| 594 | s 236I(1)(b)(ii) | 37069-37071 | fork | `s 236I(1) the defendant is liable to pay compensation to the claimant` | SS-089, SS-090, SS-091 |
| 595 | s 236I(1)(b)(ii)(A) | 37073-37081 | encoded | `s 236I(1)(b)(ii)(A) the price to compare is the price had the information been generally available` |  |
| 596 | s 236I(1)(b)(ii)(B) | 37083-37086 | encoded | `s 236I(1)(b)(ii)(B) the price to compare is the price had the contravention not occurred` |  |
| 597 | s 236I(2) | 37088-37090 | fork | `s 236I(2) the amount of compensation under subsection (1)` | F-234-2 |
| 598 | s 236I(2)(a) | 37092-37093 | fork | `s 236I(2) the amount of compensation under subsection (1)` | F-234-2 |
| 599 | s 236I(2)(b) | 37095-37100 | fork | `s 236I(2) the amount of compensation under subsection (1)` | F-234-2 |
| 600 | s 236I(3) | 37102-37102 | encoded | `s 236I(3) the defence is also available to the defendant in an action under this section` |  |
| 601 | s 236I(3)(a) | 37104-37105 | encoded | `s 236I(3) the defence is also available to the defendant in an action under this section` |  |
| 602 | s 236I(3)(b) | 37107-37113 | encoded | `s 236I(3) the defence is also available to the defendant in an action under this section` |  |
| 603 | s 236I(4) | 37115-37119 | encoded | `s 236I(4) the action under section 236I is barred because 6 years have expired from the date of completion of the dealing` |  |
| 604 | s 236I(5) | 37121-37126 | encoded | `s 236I(5) the court is to take into account the matters in section 234(5)` |  |
| 605 | s 236I(6) "maximum recoverable amount" | 37128-37128 | fork | `s 236I(6) the maximum recoverable amount` | F-234-6 |
| 606 | s 236I(6)(a) | 37130-37133 | fork | `s 236I(6) the maximum recoverable amount` | F-234-6 |
| 607 | s 236I(6)(b) | 37135-37142 | fork | `s 236I(6) the maximum recoverable amount` | F-234-6 |
| 608 | Subdivision (4) — General | 37144-37144 | inert | reason 1: not operative (a heading) |  |
| 609 | s 236J (marginal heading) | 37146-37146 | inert | reason 1: not operative (a heading) |  |
| 610 | s 236J(1) | 37148-37149 | fork | `s 236J(1) no action against the defendant may be brought without the permission of court` | F-235-1 |
| 611 | s 236J(1)(a) | 37151-37152 | fork | `s 236J(1) no action against the defendant may be brought without the permission of court` | F-235-1 |
| 612 | s 236J(1)(b) | 37154-37156 | fork | `s 236J(1) no action against the defendant may be brought without the permission of court` | F-235-1 |
| 613 | s 236J(1)(c) | 37158-37165 | fork | `s 236J(1) no action against the defendant may be brought without the permission of court` | F-235-1 |
| 614 | s 236J(1)(d) | 37167-37168 | fork | `s 236J(1) no action against the defendant may be brought without the permission of court` | F-235-1 |
| 615 | s 236J(1)(e) | 37170-37183 | fork | `s 236J(1) no action against the defendant may be brought without the permission of court`; `s 236J(1) the pending action must be stayed`; `s 236J(1) the stayed action may thereafter be continued` | F-235-1 |
| 616 | s 236J(2) | 37185-37185 | encoded | `s 236J(2) permission under subsection (1) may be granted` |  |
| 617 | s 236J(2)(a) | 37187-37189 | encoded | `s 236J(2) permission under subsection (1) may be granted` |  |
| 618 | s 236J(2)(b) | 37191-37198 | encoded | `s 236J(2) permission under subsection (1) may be granted` |  |
| 619 | s 236J(3) | 37200-37203 | fork | `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court` | F-235-1 |
| 620 | s 236J(3)(a) | 37205-37209 | fork | `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court` | F-235-1 |
| 621 | s 236J(3)(b) | 37211-37214 | fork | `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court` | F-235-1 |
| 622 | s 236J(3)(c) | 37216-37228 | fork | `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court`; `s 236J(3) the pending action under section 236D, 236G or 236I must be stayed`; `s 236J(3) the stayed action under section 236D, 236G or 236I may thereafter be continued` | F-235-1 |
| 623 | s 236J(4) | 37230-37243 | encoded | `s 236J(4) permission under subsection (3) may be granted`; `s 236J(4) the claimant must comply with the court's directions on the filing and proof of the claim` |  |
| 624 | s 236K (marginal heading) | 37245-37245 | inert | reason 1: not operative (a heading) |  |
| 625 | s 236K(1) | 37247-37249 | fork | `s 236K(1) the court may fix a date on or before which all claimants have to file and prove their claims` | SS-092, SS-093 |
| 626 | s 236K(1)(a) | 37251-37251 | fork | `s 236K(1) the court may fix a date on or before which all claimants have to file and prove their claims` | SS-092, SS-093 |
| 627 | s 236K(1)(b) | 37253-37270 | fork | `s 236K(1) the court may fix a date on or before which all claimants have to file and prove their claims` | SS-092, SS-093 |
| 628 | s 236K(2) | 37272-37273 | encoded | `s 236K(2) section 236(2) to (5) applies with the necessary modifications to the action under subsection (1)` |  |
| 629 | s 236K(2)(a) | 37275-37277 | encoded | `s 236K(2)(a) a reference to the contravening person is read as the defendant corporation, the defendant partnership or the defendant` |  |
| 630 | s 236K(2)(b) | 37279-37289 | encoded | `s 236K(2)(b) a reference to an action under section 234 is read as an action under section 236D, 236G or 236I` |  |
| 631 | s 236K(3) "claimant" | 37291-37296 | encoded | `s 236K(3) "claimant" a person who would qualify as a claimant under section 236D, 236G or 236I` |  |
| 632 | s 236L (marginal heading) | 37298-37298 | inert | reason 1: not operative (a heading) |  |
| 633 | s 236L(1) | 37300-37301 | fork | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | SS-094, SS-095, SS-096 |
| 634 | s 236L(1)(a) | 37303-37304 | fork | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | SS-094, SS-095, SS-096 |
| 635 | s 236L(1)(b) | 37306-37311 | fork | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | SS-094, SS-095, SS-096 |
| 636 | s 236L(1)(c) | 37313-37324 | fork | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | SS-094, SS-095, SS-096 |
| 637 | s 236L(2) | 37326-37335 | encoded | `s 236L(2) the third party is to be given notice and an opportunity to show cause why the order should not be made` |  |
| 638 | s 236L(3) | 37337-37342 | encoded | `s 236L(3) the application for an order for disgorgement is barred because 6 years have expired from the date of the contravention` |  |
| 639 | s 236L(4) | 37344-37347 | encoded | `s 236L(4) the court is not to make an order for disgorgement, or not of the entire benefit, against the third party` |  |
| 640 | s 236L(4)(a) | 37349-37352 | encoded | `s 236L(4) the court is not to make an order for disgorgement, or not of the entire benefit, against the third party` |  |
| 641 | s 236L(4)(b) | 37354-37361 | encoded | `s 236L(4) the court is not to make an order for disgorgement, or not of the entire benefit, against the third party` |  |
| 642 | s 236L(5) | 37363-37367 | fork | `s 236L(5) the court may make an order for disgorgement against the third party of a sum that is equitable` | SS-097 |
| 643 | s 236L(6) | 37369-37375 | fork | `s 236L(6) the court may fix a date on or before which all claimants have to file and prove their claims`; `s 236L(6) the date fixed is not earlier than 6 months from the date the order for disgorgement was made final` | SS-098 |
| 644 | s 236L(7) | 37377-37380 | fork | `s 236L(7) the court may order that the claimant be paid out of the sum under the final order for disgorgement` | SS-099, SS-100 |
| 645 | s 236L(7)(a) | 37382-37389 | fork | `s 236L(7) the amount to be paid to the claimant out of the sum under the final order for disgorgement` | F-236L-7 |
| 646 | s 236L(7)(b) | 37391-37398 | fork | `s 236L(7) the amount to be paid to the claimant out of the sum under the final order for disgorgement` | F-236L-7 |
| 647 | s 236L(8) | 37400-37405 | encoded | `s 236L(8) the sum remaining under the order to be paid into the Consolidated Fund` |  |
| 648 | s 236L(9) | 37407-37409 | fork | `s 236L(9)(a) each claimant may recover the sum due as though it were a judgment debt due to the claimant`; `s 236L(9) the third party must pay the sums under the order for disgorgement within the time specified in the court order` | SS-101 |
| 649 | s 236L(9)(a) | 37411-37413 | fork | `s 236L(9)(a) each claimant may recover the sum due as though it were a judgment debt due to the claimant`; `s 236L(9) the third party must pay the sums under the order for disgorgement within the time specified in the court order` | SS-101 |
| 650 | s 236L(9)(b) | 37415-37420 | fork | `s 236L(9)(b) the Authority may recover the remaining sum as though it were a judgment debt due to the Authority` | SS-102 |
| 651 | s 236L(10) | 37422-37427 | encoded | `s 236L(10) no subsequent application for an order for disgorgement may be made against the third party` |  |
| 652 | s 236L(11) | 37429-37430 | encoded | `s 236L(11) the order for disgorgement is made final` |  |
| 653 | s 236L(11)(a) | 37432-37433 | encoded | `s 236L(11) the order for disgorgement is made final` |  |
| 654 | s 236L(11)(b) | 37435-37438 | encoded | `s 236L(11) the order for disgorgement is made final` |  |
| 655 | s 236L(11)(c) | 37440-37441 | encoded | `s 236L(11) the order for disgorgement is made final` |  |
| 656 | s 236L(11)(d) | 37443-37443 | encoded | `s 236L(11) the order for disgorgement is made final` |  |
| 657 | s 236L(12) | 37444-37444 | encoded | `s 236L(12) "benefit" a profit gained or loss avoided as a result of the contravention` |  |
| 658 | s 236L(12) "benefit" | 37446-37448 | encoded | `s 236L(12) "benefit" a profit gained or loss avoided as a result of the contravention` |  |
| 659 | s 236L(12) "claimant" | 37450-37454 | encoded | `s 236L(12) "claimant" a person who would qualify as a claimant under section 234` |  |
| 660 | Division 6 — Miscellaneous | 37456-37458 | inert | reason 1: not operative (a heading) |  |
| 661 | s 237 (marginal heading) | 37460-37460 | inert | reason 1: not operative (a heading) |  |
| 662 | s 237 | 37462-37466 | encoded | `s 237 a District Court has jurisdiction to hear and determine the action or application regardless of the monetary amount` |  |
| 663 | s 238 (marginal heading) | 37468-37468 | inert | reason 1: not operative (a heading) |  |
| 664 | s 238(1) | 37470-37470 | inert | reason 2: machinery (a rule-making power) |  |
| 665 | s 238(1)(a) | 37472-37474 | inert | reason 2: machinery (a rule-making power) |  |
| 666 | s 238(1)(b) | 37476-37480 | inert | reason 2: machinery (a rule-making power) |  |
| 667 | s 238(2) | 37482-37483 | inert | reason 2: machinery (a rule-making power) |  |
| 668 | s 238(2)(a) | 37485-37489 | inert | reason 2: machinery (a rule-making power) |  |
| 669 | s 238(2)(b) | 37491-37492 | inert | reason 2: machinery (a rule-making power) |  |
| 670 | s 238(2)(c) | 37494-37497 | inert | reason 2: machinery (a rule-making power) |  |

## Fork register (sfab)

Every ambiguity I met, the readings I saw, the one I took and the text that licenses each.
Three kinds of entry: the forks of drafting (`F-...`), the two groups the grant ruling of 2026-11-12 (limit 3) asks to be listed with counts (the "where"/"when"/"upon"-gated `may` group and the "entitled" group), and one fork line for each of the 102 split sites (`SS-001` to `SS-102`), which are also counted under Split sites (sfab).

### Forks of drafting

| id | provision | the text and the readings | taken | the other reading | functions carrying the tag |
| --- | --- | --- | --- | --- | --- |
| F-232-2a | s 232(2)(a)(i) and (ii), and the same pattern in the cap functions of ss 236B(4), 236C(3), 236E(4), 236F(3) and 236H(2) | The cap is "the greater of (a) 3 times (i) the amount of the profit that the person gained as a result of the contravention; or (ii) the amount of the loss that the person avoided as a result of the contravention; (b) $2 million." The "or" between (i) and (ii) does not say what to do when there is both a profit and an avoided loss. | Taken: the greater of the two (3 times the larger of the profit and the loss), then the greater of that and $2 million. The text licensing it: "not exceeding the greater of the following", which makes the cap the highest of its candidates. | Other reading: the profit if there was a profit and the loss only if there was none (or the court chooses between them). That gives a lower cap in a case with both. A person asking "what is the most I can be ordered to pay" gets the higher cap under the taken reading. | `s 232(2)(a) three times the profit gained or the loss avoided`; `s 236B(4) the highest civil penalty the court may order`; `s 236C(3) the highest civil penalty the court may order`; `s 236E(4) the highest civil penalty the court may order`; `s 236F(3) the highest civil penalty the court may order`; `s 236H(2) the highest civil penalty the court may order` |
| F-234-2 | s 234(2) and s 234(2A), and the same pattern in ss 236D(2), 236G(2) and 236I(2) | The compensation is "the amount of the loss suffered by the claimant ... after deducting any amount of compensation paid or payable to the same claimant in respect of the same contravention ..., up to the maximum amount recoverable." If the deductions exceed the loss the text names no result. | Taken: nothing is owed (0). The text licensing it: compensation is "the amount of the loss ... after deducting", and an amount of compensation cannot be negative. | Other reading: `NOTHING` (the text does not say what happens when the deduction exceeds the loss). I returned a number, not a `MAYBE`, because the function answers an amount; a caller who wants the other reading changes the three `THEN 0` branches marked `FORK F-234-2`. | `s 234(2) the amount of compensation under subsection (1)`; `s 234(2A)(a)(i) the amount of the loss referred to in subsection (1)(b)`; `s 234(2A)(a)(ii) the amount of the loss that reasonably results from the claimant's reliance or ignorance`; `s 234(2A)(b) the amount of the loss that reasonably results from the claimant's reliance or ignorance in any other case`; `s 236D(2) the amount of compensation under subsection (1)`; `s 236G(2) the amount of compensation under subsection (1)`; `s 236I(2) the amount of compensation under subsection (1)` |
| F-234-6 | s 234(6) (and ss 236D(6), 236G(6), 236I(6)): "maximum recoverable amount" | "(a) the amount of the profit that the contravening person gained; or (b) the amount of the loss that the contravening person avoided, as a result of the contravention, after deducting all amounts of compensation ... previously ordered ... to other claimants". The "or" does not say which applies when both exist, and the deduction can leave a negative amount. | Taken: the greater of the two, less the deduction, and 0 where the result would be negative ("nothing recoverable"). | Other reading: the profit if there was a profit, else the loss; or `NOTHING` for a negative result. Same flip points as F-232-2a and F-234-2. | `s 234(6) the maximum recoverable amount`; `s 236D(6) the maximum recoverable amount`; `s 236G(6) the maximum recoverable amount`; `s 236I(6) the maximum recoverable amount` |
| F-235-1 | s 235(1) (and ss 236J(1), 236J(3) by the same pattern) | "no action under section 234 may be brought against the contravening person in respect of a contravention ... which resulted in the contravening person gaining a profit or avoiding a loss after the commencement of -- (a) criminal proceedings ... or (b) an action under section 232". Read literally, "after the commencement of" can qualify the gaining of the profit or the avoiding of the loss; read sensibly, it qualifies when the action is brought. | Taken: it qualifies when the action is brought (an action brought after criminal proceedings or a section 232 action has commenced needs the court's permission). The text licensing it: s 235(2), which deals with an action "pending on the date of commencement of" the same proceedings, only makes sense if the bar in s 235(1) is about the date of the action. | Other reading: the profit or loss must itself arise after the commencement. That would leave an action about a profit made before the proceedings without a bar. The branch is marked `NOTHING-kind` and `MARGINAL-READING (b)` where the gate is unmet. | `s 235(1) no action under section 234 may be brought without the permission of court`; `s 236J(1) no action against the defendant may be brought without the permission of court`; `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court` |
| F-236-3A | s 236(3A)(b) | The court's order is the lesser of (a) the compensation the claimant has proven and (b) "the pro-rated portion of the maximum recoverable amount, calculated according to the relationship which the amount referred to in paragraph (a) bears to the total amount of all other claims". Read literally the ratio is a/others, which is undefined when there is no other claim and exceeds the whole when the others are small. | Taken: the share is a/(a + others), the claimant's own claim being counted among "all claims proved" (and 0 when nothing is proven, which also keeps the ratio from dividing by zero). The text licensing it: "pro-rated portion", which is a share of a whole that includes the claimant. | Other reading: the literal ratio a/others. With no other claim it is undefined (and would be `NOTHING`). The two readings give different amounts whenever there is more than one claim. | `s 236(3A) the compensation amount ordered for the claimant` |
| F-236L-7 | s 236L(7) | The court may order that "each claimant who has filed and proven the claimant's claim" be paid out of the sum under the final order. The text names no amount when nothing is proved. | Taken: nothing is proved, so nothing is paid (0). | Other reading: `NOTHING`. The amount function returns a number, so the zero is the branch marked `FORK F-236L-7`. | `s 236L(7) the amount to be paid to the claimant out of the sum under the final order for disgorgement` |
| F-227 | s 227(1)(b) | "it is to be presumed that every partner ... knows or ought reasonably to know that matter or thing". Unlike s 226(1)(b) ("it is to be presumed, until the contrary is proved") the text of s 227(1)(b) names no way to rebut it. | Taken: `JUST TRUE` once the fact (a partner, employee or manager knows the matter in that capacity) is given; no rebuttal path is invented. | Other reading: the presumption is rebuttable as in s 226(1)(b), and the function would take a "the contrary is proved" input. I did not add one because the text does not say it. | a decision made in the rule's form; see the provision |
| F-sell | s 214(1) "sell" | In the rendering, "sell", in relation to securities-based derivatives contracts or CIS units, "includes a contract or arrangement under which a party acquires an option or right from another party -- (a) grant or assign the option or right; or (b) take, or cause to be taken, such action as releases the option or right". The verb of the lead-in ("acquires") does not fit the limbs ("grant or assign", "take ... action"). | Taken: encoded as the text reads, with the two limbs as alternatives; the mismatch is not repaired. | Other reading: the limbs describe what the other party does, or the lead-in should read "disposes of". I cannot tell which from the rendering, which may also have dropped words; a later consolidation was not read. | `s 214(1) "sell" the act is a sale of a securities-based derivatives contract or CIS unit` |
| F-203-days | s 203(1) | The duty is to notify "as they occur or arise" the information the approved exchange's listing rules or other requirements require. The Act sets no time of its own. | Taken: the number of days within which the approved exchange requires the person to notify is an INPUT (the input `the number of days within which the approved exchange requires the person to notify it`); the rule is `MUST ... WITHIN` that many days. No deadline is invented. | Other reading: a rule with no deadline, which could never show a breach (a late notice would still read `FULFILLED`). I did not choose it because the duty is a duty to notify as events occur, so a delay is a breach once the exchange's time is known. | a decision made in the rule's form; see the provision |
| F-218-def | s 218(5) | Section 218(5) defines "connected person" "In this Division" (ss 213 to 231). Section 2(1) also defines "connected person", "in relation to -- (a) an individual" as the individual's relatives and the firms, limited liability partnerships and corporations in which the individual or a relative controls not less than 20% of the voting power (line 2226 onward). The two terms differ. | Taken: the Division's own definition (`s 218(5)(a)` and `(b)`), with `s 218(6)` for "officer"; the keel's `s 2(1) "connected person"` is not called. | Other reading: apply the keel's s 2(1) term in Division 3. The text of s 218(5) says it defines the term "In this Division", which licenses the taken reading. | a decision made in the rule's form; see the provision |
| F-party | every SHANT and MUST rule of Part 12 | The prohibitions say "A person must not ..." and name no narrower party. | Taken: `PARTY Individual "a person"` (the core `Party` for a natural person); the same rule, with another core `Party` constructor, serves a corporation. | Other reading: a separate rule per kind of person. The text does not distinguish, so I did not. | a decision made in the rule's form; see the provision |
| F-3-assoc | ss 197(3)(b) and (c), 197(5)(b), 202(2)(a) and (b) and 230(1)(c), where the text says "associated with" or "an associate of" | The text says "a person associated with the person". Section 3 defines association and is encoded in the keel, but my modules do not import `sfa-associates.l4`. | Taken: each such fact is a `MAYBE BOOLEAN` input named for the fact with the words "(as section 3 reads)": the caller supplies the keel's answer (`JUST TRUE`, `JUST FALSE` or `NOTHING`), and `NOTHING` stays `NOTHING`. | Other reading: import `sfa-associates.l4` and call `s 3(1)` with its nine inputs. That makes a seat question ask nine extra facts for every association question; the brief fixes the seam as an input. | a decision made in the rule's form; see the provision |

### The "may" group gated by "where", "when", "upon" or "whenever", and the "entitled" group (grant ruling of 2026-11-12, limit 3)

The Guide says: "do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way)". I did not change them: the answers are as the Guide's periods ruling (b) and the delegated-definitions ruling (c) give them (`JUST FALSE` when the gate fails).

**"where"/"when"/"upon"-gated `may` functions: 9** (a "may" or "may be granted" function whose gate is a "where", "whenever" or "when"; answer left as ruled: `JUST FALSE` on a failed gate; the other reading is `NOTHING`).

- s 232(1) `s 232(1) the Authority may bring an action in a court against the person to seek an order for a civil penalty` (SS-051, SS-052)
- s 236(1) `s 236(1) the relevant court may fix a date on or before which all claimants have to file and prove their claims` (SS-060, SS-061)
- s 236B(3) `s 236B(3) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` (SS-065, SS-066)
- s 236C(2) `s 236C(2) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` (SS-069, SS-070)
- s 236E(3) `s 236E(3) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` (SS-076, SS-077)
- s 236F(2) `s 236F(2) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` (SS-080, SS-081)
- s 236H(1) `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` (SS-086, SS-087)
- s 236K(1) `s 236K(1) the court may fix a date on or before which all claimants have to file and prove their claims` (SS-092, SS-093)
- s 236L(1) `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` (SS-094, SS-095, SS-096)

**"entitled"-group functions: 4.** No function of this part is named with the word "entitled": the text says "liable to pay compensation" (ss 234(1), 236D(1), 236G(1), 236I(1)), which is the claimant's claim stated from the side of the person who bears it.
I list those four, because the Guide says "an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it)". Their answer is as the text says: `JUST FALSE` where an element of the liability is not met (marked `SPLIT-SITE (i)`), `NOTHING` where the liability is limited by its own wording.

- s 234(1) `s 234(1) the contravening person is liable to pay compensation to the claimant` (SS-056, SS-057, SS-058)
- s 236D(1) `s 236D(1) the corporation is liable to pay compensation to the claimant` (SS-072, SS-073, SS-074)
- s 236G(1) `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` (SS-083, SS-084, SS-085)
- s 236I(1) `s 236I(1) the defendant is liable to pay compensation to the claimant` (SS-089, SS-090, SS-091)

**"may" functions whose `if` gate fails and answer `NOTHING`, not `JUST FALSE`: 10** (limit 1 of the same ruling: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"). One fork line each, as SS (ii) [IF] rows below; the other reading is `JUST FALSE` (a failed "if" counts as the text's no, marginal reading (a)).

- s 232(2) `s 232(2) the court may make an order against the person for the payment of a civil penalty` (SS-053)
- s 232(4) `s 232(4) the court may make the order on the terms agreed between the Authority and the defendant despite subsections (2) and (3)` (SS-054)
- s 232(7) `s 232(7) the Authority may recover the civil penalty on behalf of the Government as though it were a judgment debt due to the Authority` (SS-055)
- s 236B(4) `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty` (SS-067)
- s 236C(3) `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty` (SS-071)
- s 236E(4) `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty` (SS-078)
- s 236F(3) `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty` (SS-082)
- s 236H(2) `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty` (SS-088)
- s 236L(9) `s 236L(9)(a) each claimant may recover the sum due as though it were a judgment debt due to the claimant` (SS-101)
- s 236L(9) `s 236L(9)(b) the Authority may recover the remaining sum as though it were a judgment debt due to the Authority` (SS-102)

### Split-site fork lines

One line per site: the provision, the function, the answer taken, the other reading, the words that license the answer, and the line of `inputs/ENCODING-GUIDE.md` section 5 (or the dated ruling in it) the answer relies on, quoted.
To apply a ruling, flip the branch on the line `sfab-<module>.l4:<line>` (the line carries the `-- SPLIT-SITE` comment); every site has a test case marked `-- S` in `sfab-tests-<module>.l4`, which asserts the answer taken and would be flipped with it.

| id | kind | provision | function | where | answer taken | other reading | words that license the answer taken | Guide line relied on (quoted) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SS-001 | (i) [SCOPE] | s 196(a) | `s 196(a) this Division applies to the act occurring within Singapore` | `sfab-division-1.l4:62` | NOTHING | JUST FALSE: the list of acts it applies to is read as closed, so an act outside it is the text's no (JUST FALSE) | "This Division applies to"; "acts occurring within Singapore in relation to" | the periods ruling of 2026-11-05, item (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" |
| SS-002 | (i) [SCOPE] | s 196(b) | `s 196(b) this Division applies to the act occurring outside Singapore` | `sfab-division-1.l4:98` | NOTHING | JUST FALSE: the list of acts it applies to is read as closed, so an act outside it is the text's no (JUST FALSE) | "acts occurring outside Singapore in relation to" | the periods ruling of 2026-11-05, item (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" |
| SS-003 | (i) [OWN] | s 197(1) | `s 197(1) the person's conduct contravenes the bar on conduct done to create a false or misleading appearance` | `sfab-division-1.l4:186` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A person must not do any thing, cause any thing to be done or engage in any course of conduct" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-004 | (i) [IF] | s 197(1) | `s 197(1) the person's conduct contravenes the bar on conduct done to create a false or misleading appearance` | `sfab-division-1.l4:189` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if the person’s purpose, or any of the person’s purposes" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-005 | (i) [OWN] | s 197(1A) | `s 197(1A) the person's conduct contravenes the bar on conduct that creates a false or misleading appearance knowingly or recklessly` | `sfab-division-1.l4:223` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "that creates, or is likely to create, a false or misleading appearance of active trading" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-006 | (i) [IF] | s 197(1A) | `s 197(1A) the person's conduct contravenes the bar on conduct that creates a false or misleading appearance knowingly or recklessly` | `sfab-division-1.l4:226` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if"; "the person knows that doing that thing" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-007 | (i) [OWN] | s 197(2) | `s 197(2) the person's conduct contravenes the bar on maintaining, inflating or depressing the market price` | `sfab-division-1.l4:251` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "by means of any purchase or sale of any capital markets products that does not involve a change in the beneficial ownership" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-008 | (i) [DEFENCE] | s 197(6) | `s 197(6) the defendant has the defence to a contravention of subsection (2)` | `sfab-division-1.l4:394` | JUST FALSE | NOTHING: the defence is a limit on the offence, so a case outside it is not covered (NOTHING) | "it is a defence if the defendant establishes" | the delegated-definitions ruling of 2026-11-05, item (b): ""it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts"" |
| SS-009 | (i) [OWN] | s 198(1) | `s 198(1) the person's transactions contravene the bar on market manipulation in securities of a corporation` | `sfab-division-1.l4:453` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "2 or more transactions in securities"; "with the intent to induce other persons" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-010 | (i) [OWN] | s 198(2) | `s 198(2) the person's transactions contravene the bar on market manipulation in securities of a business trust` | `sfab-division-1.l4:482` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "2 or more transactions in securities"; "with the intent to induce other persons" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-011 | (i) [OWN] | s 199 | `s 199 the person's statement or information contravenes the bar on false or misleading statements` | `sfab-division-1.l4:568` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "that is false or misleading in a material particular and is likely" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-012 | (i) [IF] | s 199 | `s 199 the person's statement or information contravenes the bar on false or misleading statements` | `sfab-division-1.l4:571` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if, when the person makes the statement or disseminates the information" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-013 | (i) [OWN] | s 200(1) | `s 200(1) the person's conduct contravenes the bar on fraudulently inducing a person to deal` | `sfab-division-1.l4:607` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "induce or attempt to induce another person to deal in capital markets products" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-014 | (i) [DEFENCE] | s 200(2) | `s 200(2) the defendant has the defence to a contravention constituted by recording or storing information` | `sfab-division-1.l4:634` | JUST FALSE | NOTHING: the defence is a limit on the offence, so a case outside it is not covered (NOTHING) | "it is a defence if it is established that" | the delegated-definitions ruling of 2026-11-05, item (b): ""it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts"" |
| SS-015 | (i) [OWN] | s 201 | `s 201 the person's conduct contravenes the bar on manipulative and deceptive devices` | `sfab-division-1.l4:682` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "in connection with the subscription, purchase or sale of any capital markets products" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-016 | (i) [OWN] | s 201A(1) | `s 201A(1) the person's execution of an order contravenes the bar on bucketing a derivatives contract` | `sfab-division-1.l4:709` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "without having effected in good faith a purchase or sale" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-017 | (i) [OWN] | s 201A(2) | `s 201A(2) the person's execution of an order contravenes the bar on bucketing a spot foreign exchange contract` | `sfab-division-1.l4:732` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "without having effected in good faith a purchase or sale" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-018 | (i) [OWN] | s 201B | `s 201B the person's conduct contravenes the bar on manipulating the price of derivatives contracts and cornering` | `sfab-division-1.l4:760` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "manipulate or attempt to manipulate the price of a derivatives contract traded on an organised market" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-019 | (i) [OWN] | s 202(1) | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions` | `sfab-division-1.l4:857` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "to any of the following effect" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-020 | (i) [IF] | s 202(1) | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions` | `sfab-division-1.l4:862` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if any condition in subsection (2) is satisfied" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-021 | (i) [OWN] | s 203(1) | `s 203(1) the person's failure to notify the approved exchange contravenes the bar on failing to disclose` | `sfab-division-1.l4:919` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A person to whom this subsection applies" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-022 | (i) [IF] | s 203(1) | `s 203(1) the person's failure to notify the approved exchange contravenes the bar on failing to disclose` | `sfab-division-1.l4:922` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if the person is required by the approved exchange under the listing rules" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-023 | (i) [OWN] | s 204(1) | `s 204(1) the person is guilty of an offence` | `sfab-division-1.l4:974` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "Any person who contravenes any of the provisions of this Division" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-024 | (i) [SCOPE] | s 205(a) | `s 205(a) this Division applies to the act occurring within Singapore` | `sfab-division-2.l4:39` | NOTHING | JUST FALSE: the list of acts it applies to is read as closed, so an act outside it is the text's no (JUST FALSE) | "acts occurring within Singapore in relation to financial benchmarks" | the periods ruling of 2026-11-05, item (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" |
| SS-025 | (i) [SCOPE] | s 205(b) | `s 205(b) this Division applies to the act occurring outside Singapore` | `sfab-division-2.l4:51` | NOTHING | JUST FALSE: the list of acts it applies to is read as closed, so an act outside it is the text's no (JUST FALSE) | "acts occurring outside Singapore in relation to financial benchmarks that are administered in Singapore" | the periods ruling of 2026-11-05, item (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" |
| SS-026 | (i) [OWN] | s 207(1) | `s 207(1) the person's conduct contravenes the bar on conduct done to create a false appearance as to a financial benchmark` | `sfab-division-2.l4:126` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A person must not do any thing, cause any thing to be done or engage in any course of conduct" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-027 | (i) [IF] | s 207(1) | `s 207(1) the person's conduct contravenes the bar on conduct done to create a false appearance as to a financial benchmark` | `sfab-division-2.l4:129` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if the person’s purpose, or any of the person’s purposes" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-028 | (i) [OWN] | s 207(2) | `s 207(2) the person's conduct contravenes the bar on conduct that creates a false appearance as to a financial benchmark knowingly or recklessly` | `sfab-division-2.l4:161` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "that creates, or is likely to create, a false or misleading appearance" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-029 | (i) [IF] | s 207(2) | `s 207(2) the person's conduct contravenes the bar on conduct that creates a false appearance as to a financial benchmark knowingly or recklessly` | `sfab-division-2.l4:164` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if"; "the person knows that doing that thing" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-030 | (i) [OWN] | s 209 | `s 209 the person's statement contravenes the bar on false or misleading statements to a benchmark administrator` | `sfab-division-2.l4:223` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "to a person who carries out the activity of administering a financial benchmark" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-031 | (i) [IF] | s 209 | `s 209 the person's statement contravenes the bar on false or misleading statements to a benchmark administrator` | `sfab-division-2.l4:226` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if"; "the person intends that the statement, information or opinion be used" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-032 | (i) [OWN] | s 210(1) | `s 210(1) the person is guilty of an offence` | `sfab-division-2.l4:254` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "Any person who contravenes any of the provisions of this Division" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-033 | (i) [SCOPE] | s 213(a) | `s 213(a) this Division applies to the act occurring within Singapore` | `sfab-insider-1.l4:52` | NOTHING | JUST FALSE: the list of acts it applies to is read as closed, so an act outside it is the text's no (JUST FALSE) | "acts occurring within Singapore in relation to" | the periods ruling of 2026-11-05, item (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" |
| SS-034 | (i) [SCOPE] | s 213(b) | `s 213(b) this Division applies to the act occurring outside Singapore` | `sfab-insider-1.l4:84` | NOTHING | JUST FALSE: the list of acts it applies to is read as closed, so an act outside it is the text's no (JUST FALSE) | "acts occurring outside Singapore in relation to" | the periods ruling of 2026-11-05, item (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" |
| SS-035 | (i) [WHERE] | s 218(1) | `s 218(1) subsections (2), (3), (4), (5) and (6) apply to the connected person` | `sfab-insider-2.l4:120` | JUST FALSE | NOTHING: a "where" that limits a prohibition in its own wording gives NOTHING (the "In short" line on NOTHING) | "Subject to this Division, where" | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| SS-036 | (i) [IF] | s 218(1A) | `s 218(1A) subsections (2), (3), (4A), (5) and (6) apply to the person connected to a business trust or scheme corporation` | `sfab-insider-2.l4:199` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "Subsections (2), (3), (4A), (5) and (6) apply if" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-037 | (i) [WHERE] | s 218(2) | `s 218(2) the connected person's dealing or procuring contravenes the bar` | `sfab-insider-2.l4:228` | JUST FALSE | NOTHING: a "where" that limits a prohibition in its own wording gives NOTHING (the "In short" line on NOTHING) | "Subject to this Division, where" | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| SS-038 | (i) [OWN] | s 218(2) | `s 218(2) the connected person's dealing or procuring contravenes the bar` | `sfab-insider-2.l4:233` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "The connected person must not (whether as principal or agent)" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-039 | (i) [WHERE] | s 218(3) | `s 218(3) the connected person's communication of the information contravenes the bar` | `sfab-insider-2.l4:270` | JUST FALSE | NOTHING: a "where" that limits a prohibition in its own wording gives NOTHING (the "In short" line on NOTHING) | "Subject to this Division, where" | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| SS-040 | (i) [OWN] | s 218(3) | `s 218(3) the connected person's communication of the information contravenes the bar` | `sfab-insider-2.l4:274` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "The connected person must not, directly or indirectly, communicate the information" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-041 | (i) [IF] | s 218(3) | `s 218(3) the connected person's communication of the information contravenes the bar` | `sfab-insider-2.l4:277` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if the connected person knows, or ought reasonably to know" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-042 | (i) [WHERE] | s 219(1) | `s 219(1) subsections (2) and (3) apply to the insider` | `sfab-insider-2.l4:391` | JUST FALSE | NOTHING: a "where" that limits a prohibition in its own wording gives NOTHING (the "In short" line on NOTHING) | "Subject to this Division, where" | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| SS-043 | (i) [WHERE] | s 219(2) | `s 219(2) the insider's dealing or procuring contravenes the bar` | `sfab-insider-2.l4:414` | JUST FALSE | NOTHING: a "where" that limits a prohibition in its own wording gives NOTHING (the "In short" line on NOTHING) | "Subject to this Division, where" | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| SS-044 | (i) [OWN] | s 219(2) | `s 219(2) the insider's dealing or procuring contravenes the bar` | `sfab-insider-2.l4:419` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "The insider must not (whether as principal or agent)" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-045 | (i) [WHERE] | s 219(3) | `s 219(3) the insider's communication of the information contravenes the bar` | `sfab-insider-2.l4:451` | JUST FALSE | NOTHING: a "where" that limits a prohibition in its own wording gives NOTHING (the "In short" line on NOTHING) | "Subject to this Division, where" | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| SS-046 | (i) [OWN] | s 219(3) | `s 219(3) the insider's communication of the information contravenes the bar` | `sfab-insider-2.l4:455` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "The insider must not, directly or indirectly, communicate the information" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-047 | (i) [IF] | s 219(3) | `s 219(3) the insider's communication of the information contravenes the bar` | `sfab-insider-2.l4:458` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "if the insider knows, or ought reasonably to know" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-048 | (i) [OWN] | s 221(1) | `s 221(1) the person is guilty of an offence` | `sfab-insider-2.l4:518` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A person who contravenes section 218 or 219, shall be guilty of an offence" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-049 | (i) [DEFENCE] | s 231(1) | `s 231(1) the person has the parity of information defence to the contravention by dealing or procuring` | `sfab-insider-3.l4:475` | JUST FALSE | NOTHING: the defence is a limit on the offence, so a case outside it is not covered (NOTHING) | "it is a defence if the court is satisfied that" | the delegated-definitions ruling of 2026-11-05, item (b): ""it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts"" |
| SS-050 | (i) [DEFENCE] | s 231(2) | `s 231(2) the person has the parity of information defence to the contravention by communicating` | `sfab-insider-3.l4:499` | JUST FALSE | NOTHING: the defence is a limit on the offence, so a case outside it is not covered (NOTHING) | "it is a defence if the court is satisfied that" | the delegated-definitions ruling of 2026-11-05, item (b): ""it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts"" |
| SS-051 | (ii) [WHENEVER] | s 232(1) | `s 232(1) the Authority may bring an action in a court against the person to seek an order for a civil penalty` | `sfab-civil.l4:29` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "Whenever it appears to the Authority that any person has contravened any provision in this Part" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-052 | (ii) [CONSENT] | s 232(1) | `s 232(1) the Authority may bring an action in a court against the person to seek an order for a civil penalty` | `sfab-civil.l4:31` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-053 | (ii) [IF] | s 232(2) | `s 232(2) the court may make an order against the person for the payment of a civil penalty` | `sfab-civil.l4:45` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "the court may make an order against the person for the payment of a civil penalty" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-054 | (ii) [IF] | s 232(4) | `s 232(4) the court may make the order on the terms agreed between the Authority and the defendant despite subsections (2) and (3)` | `sfab-civil.l4:117` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "the court may make an order against a person against whom an action has been brought under this section if the Authority, with the consent of the Public Prosecutor, has agreed" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-055 | (ii) [IF] | s 232(7) | `s 232(7) the Authority may recover the civil penalty on behalf of the Government as though it were a judgment debt due to the Authority` | `sfab-civil.l4:171` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "the Authority may recover the civil penalty on behalf of the Government" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-056 | (i) [OWN] | s 234(1) | `s 234(1) the contravening person is liable to pay compensation to the claimant` | `sfab-civil.l4:341` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A person who has acted in contravention of any of the provisions in this Part" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-057 | (i) [IF] | s 234(1) | `s 234(1) the contravening person is liable to pay compensation to the claimant` | `sfab-civil.l4:343` | JUST FALSE | NOTHING: the element limits the prohibition in its own wording, so a case that fails it is not covered (NOTHING) | "is, if the contravening person had gained a profit or avoided a loss as a result of that contravention" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" |
| SS-058 | (i) [OWN] | s 234(1) | `s 234(1) the contravening person is liable to pay compensation to the claimant` | `sfab-civil.l4:346` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "liable to pay compensation to any person"; "(called in this section and sections 235 and 236 the claimant) who" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-059 | (i) [OWN] | s 234(1A) | `s 234(1A) the contravening person is liable to pay compensation to the claimant whether or not the person gained a profit or avoided a loss` | `sfab-civil.l4:398` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "the contravening person is, whether or not the contravening person had gained a profit or avoided a loss as a result of that contravention"; "liable to pay compensation to the claimant, if" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-060 | (ii) [WHERE] | s 236(1) | `s 236(1) the relevant court may fix a date on or before which all claimants have to file and prove their claims` | `sfab-civil.l4:807` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "where the contravening person"; "has been convicted of an offence under this Part"; "other than by way of a default judgment or a consent order" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-061 | (ii) [AFTER] | s 236(1) | `s 236(1) the relevant court may fix a date on or before which all claimants have to file and prove their claims` | `sfab-civil.l4:809` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "after the conviction or the order imposing the civil penalty has been made final" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-062 | (ii) [AFTER] | s 236(3) | `s 236(3) the relevant court may make an order against the contravening person to pay compensation to the claimant` | `sfab-civil.l4:838` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "may, after the expiry of the date fixed under subsection (1), make an order" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-063 | (ii) [WHO] | s 236(3) | `s 236(3) the relevant court may make an order against the contravening person to pay compensation to the claimant` | `sfab-civil.l4:840` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "to each claimant who has filed and proven that claimant's claim for compensation" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-064 | (i) [WHERE] | s 236B(1) | `s 236B(1) the corporation is guilty of the offence as if it had committed the contravention` | `sfab-attributed.l4:97` | JUST FALSE | NOTHING: a "where" that limits a prohibition in its own wording gives NOTHING (the "In short" line on NOTHING) | "Where an offence of contravening any provision in this Part is proved to have been committed by an employee or an officer of a corporation" | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| SS-065 | (ii) [WHERE] | s 236B(3) | `s 236B(3) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` | `sfab-attributed.l4:143` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "Where it appears to the Authority that a corporation is liable to be punished under subsection (1) for a contravention committed by a contravening person" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-066 | (ii) [CONSENT] | s 236B(3) | `s 236B(3) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` | `sfab-attributed.l4:145` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the corporation" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-067 | (ii) [IF] | s 236B(4) | `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty` | `sfab-attributed.l4:170` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "If the court in subsection (3) is satisfied on a balance of probabilities that the corporation is liable to be punished under subsection (1)" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-068 | (i) [OWN] | s 236C(1) | `s 236C(1) the corporation commits a contravention and is liable to an order for a civil penalty` | `sfab-attributed.l4:308` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A corporation which fails to prevent or detect a contravention of any provision in this Part committed by an employee or officer of the corporation" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-069 | (ii) [WHERE] | s 236C(2) | `s 236C(2) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` | `sfab-attributed.l4:323` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "Where it appears to the Authority that a corporation has committed a contravention under subsection (1)" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-070 | (ii) [CONSENT] | s 236C(2) | `s 236C(2) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` | `sfab-attributed.l4:325` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the corporation" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-071 | (ii) [IF] | s 236C(3) | `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty` | `sfab-attributed.l4:349` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "If the court is satisfied on a balance of probabilities that the corporation has committed a contravention under subsection (1)" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-072 | (i) [OWN] | s 236D(1) | `s 236D(1) the corporation is liable to pay compensation to the claimant` | `sfab-attributed.l4:457` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A defendant corporation which has gained a profit or avoided a loss as a result of the contravention of a provision in this Part by the contravening person referred to in section 236B(1) or 236C(1)" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-073 | (i) [OWN] | s 236D(1) | `s 236D(1) the corporation is liable to pay compensation to the claimant` | `sfab-attributed.l4:459` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "which has gained a profit or avoided a loss as a result of the contravention" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-074 | (i) [OWN] | s 236D(1) | `s 236D(1) the corporation is liable to pay compensation to the claimant` | `sfab-attributed.l4:462` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "any person (called in this section the claimant) who" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-075 | (i) [WHERE] | s 236E(1) | `s 236E(1) the partnership or limited liability partnership is guilty of the offence as if it had committed the contravention` | `sfab-attributed.l4:599` | JUST FALSE | NOTHING: a "where" that limits a prohibition in its own wording gives NOTHING (the "In short" line on NOTHING) | "Where an offence of contravening any provision of this Part is proved to have been committed by a partner or employee of a partnership or a partner, manager or employee of a limited liability partnership" | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| SS-076 | (ii) [WHERE] | s 236E(3) | `s 236E(3) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` | `sfab-attributed.l4:649` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "Where it appears to the Authority that a partnership or a limited liability partnership is liable to be punished under subsection (1) for a contravention committed by a contravening person" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-077 | (ii) [CONSENT] | s 236E(3) | `s 236E(3) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` | `sfab-attributed.l4:651` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the partnership or limited liability partnership" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-078 | (ii) [IF] | s 236E(4) | `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty` | `sfab-attributed.l4:677` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "If the court in subsection (3) is satisfied on a balance of probabilities that the partnership or limited liability partnership is liable to be punished under subsection (1)" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-079 | (i) [OWN] | s 236F(1) | `s 236F(1) the partnership or limited liability partnership commits a contravention and is liable to an order for a civil penalty` | `sfab-attributed.l4:823` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A partnership or limited liability partnership which fails to prevent or detect a contravention of any provision in this Part committed by a partner or employee of the partnership or a partner, manager or employee of the limited liability partnership, as the case may be" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-080 | (ii) [WHERE] | s 236F(2) | `s 236F(2) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` | `sfab-attributed.l4:839` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "Where it appears to the Authority that a partnership or limited liability partnership has committed a contravention under subsection (1)" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-081 | (ii) [CONSENT] | s 236F(2) | `s 236F(2) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` | `sfab-attributed.l4:841` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the partnership or limited liability partnership" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-082 | (ii) [IF] | s 236F(3) | `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty` | `sfab-attributed.l4:866` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "If the court is satisfied on a balance of probabilities that the partnership or limited liability partnership has committed a contravention under subsection (1)" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-083 | (i) [OWN] | s 236G(1) | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | `sfab-attributed.l4:977` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A defendant partnership which has gained a profit or avoided a loss as a result of the contravention of a provision in this Part by the contravening person referred to in section 236E(1) or 236F(1)" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-084 | (i) [OWN] | s 236G(1) | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | `sfab-attributed.l4:979` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "which has gained a profit or avoided a loss as a result of the contravention" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-085 | (i) [OWN] | s 236G(1) | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | `sfab-attributed.l4:982` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "any person (called in this section the claimant) who" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-086 | (ii) [WHERE] | s 236H(1) | `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` | `sfab-attributed.l4:1127` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "Where it appears to the Authority that a corporation, partnership, limited liability partnership or unincorporated association (called in this section the contravening person) has contravened any provision in this Part" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-087 | (ii) [CONSENT] | s 236H(1) | `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` | `sfab-attributed.l4:1129` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the defendant" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-088 | (ii) [IF] | s 236H(2) | `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty` | `sfab-attributed.l4:1153` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "If the court is satisfied on a balance of probabilities that the contravening person has contravened a provision in this Part with the consent or connivance of the defendant" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-089 | (i) [OWN] | s 236I(1) | `s 236I(1) the defendant is liable to pay compensation to the claimant` | `sfab-attributed.l4:1241` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "A defendant who has gained a profit or avoided a loss as a result of the contravention of a provision in this Part by a contravening person referred to in section 236H(1)" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-090 | (i) [OWN] | s 236I(1) | `s 236I(1) the defendant is liable to pay compensation to the claimant` | `sfab-attributed.l4:1243` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "who has gained a profit or avoided a loss as a result of the contravention" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-091 | (i) [OWN] | s 236I(1) | `s 236I(1) the defendant is liable to pay compensation to the claimant` | `sfab-attributed.l4:1246` | NOTHING | JUST FALSE: the element is part of the text's own condition for the offence, so its failure is the text saying no (MARGINAL-READING (a)) | "any person (called in this section the claimant)" | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-092 | (ii) [WHERE] | s 236K(1) | `s 236K(1) the court may fix a date on or before which all claimants have to file and prove their claims` | `sfab-attributed.l4:1558` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "where a defendant corporation, defendant partnership"; "has been convicted of an offence under this Division"; "other than by way of a default judgment or a consent order" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-093 | (ii) [AFTER] | s 236K(1) | `s 236K(1) the court may fix a date on or before which all claimants have to file and prove their claims` | `sfab-attributed.l4:1560` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "may, after the conviction or the order imposing the civil penalty has been made final, fix a date" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-094 | (ii) [WHERE] | s 236L(1) | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | `sfab-attributed.l4:1647` | JUST FALSE | NOTHING: the "In short" line on grants points the other way: a grant limited by its own wording gives NOTHING | "where"; "a person has been convicted by a court of an offence in respect of a contravention of any provision in this Part" | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" |
| SS-095 | (ii) [APPLICATION] | s 236L(1) | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | `sfab-attributed.l4:1649` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "the court may, on the application of the Authority or any claimant, make an order" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-096 | (ii) [WHO] | s 236L(1) | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | `sfab-attributed.l4:1651` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "against any other person (called in this section a third party) who has received the whole or any part of the benefit of that contravention" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-097 | (ii) [WHO] | s 236L(5) | `s 236L(5) the court may make an order for disgorgement against the third party of a sum that is equitable` | `sfab-attributed.l4:1716` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "against a third party referred to in subsection (4) of a sum that is, in the opinion of the court, equitable" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-098 | (ii) [AFTER] | s 236L(6) | `s 236L(6) the court may fix a date on or before which all claimants have to file and prove their claims` | `sfab-attributed.l4:1730` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "The court may, after the order for disgorgement has been made final, fix a date" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-099 | (ii) [AFTER] | s 236L(7) | `s 236L(7) the court may order that the claimant be paid out of the sum under the final order for disgorgement` | `sfab-attributed.l4:1754` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "The court may, after the expiry of the date fixed under subsection (6), order" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-100 | (ii) [WHO] | s 236L(7) | `s 236L(7) the court may order that the claimant be paid out of the sum under the final order for disgorgement` | `sfab-attributed.l4:1756` | NOTHING | JUST FALSE: the gate is read like a "where" (periods ruling, item (b)) or as the text's own condition, giving JUST FALSE | "each claimant who has filed and proven the claimant’s claim for compensation" | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" |
| SS-101 | (ii) [IF] | s 236L(9) | `s 236L(9)(a) each claimant may recover the sum due as though it were a judgment debt due to the claimant` | `sfab-attributed.l4:1809` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "each claimant may recover the sum due to the claimant under the order for disgorgement" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| SS-102 | (ii) [IF] | s 236L(9) | `s 236L(9)(b) the Authority may recover the remaining sum as though it were a judgment debt due to the Authority` | `sfab-attributed.l4:1833` | NOTHING | JUST FALSE: a failed "if" is the text's no (MARGINAL-READING (a)): JUST FALSE | "the remaining sum under the order for disgorgement may be recovered by the Authority" | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |

## Jural relations (sfab)

Hohfeld's correlatives: a claim (right) against a duty; a privilege (liberty) against a no-right; a power against a liability; an immunity against a disability.
One row per provision (a section, or a subsection where the section has them) that creates a relation, naming the party holding the claim, privilege, power or immunity, the party bearing the correlative, the section and the L4 rule or function that encodes it.
Each relation is stated once, from one side; the relation is chosen from what the provision's own functions say, and the parties are the ones the text names (the Authority, the Public Prosecutor, the court, the claimant, the person).
A provision that creates no relation (a definition, a counting or scope rule) is listed once, at the end, as `none`.

| provision | kind | holder (claim, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | encoded by |
| --- | --- | --- | --- | --- |
| s 197(1) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 197(1) the person's conduct contravenes the bar on conduct done to create a false or misleading appearance`; `s 197(1) a person must not act for the purpose of creating a false or misleading appearance` |
| s 197(1A) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 197(1A) the person's conduct contravenes the bar on conduct that creates a false or misleading appearance knowingly or recklessly`; `s 197(1A) a person must not do a thing that creates a false or misleading appearance knowingly or recklessly` |
| s 197(2) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 197(2) the person's conduct contravenes the bar on maintaining, inflating or depressing the market price`; `s 197(2) a person must not maintain, inflate or depress the market price by a sale with no change in beneficial ownership or a fictitious transaction` |
| s 197(3) | Power / Liability | the prosecution or claimant (may rely on the presumption) | the person (subject to the presumption unless rebutted) | `s 197(3) the person's purpose is presumed to be to create a false or misleading appearance of active trading`; `s 197(3)(a) the person's purpose is presumed by reason of a transaction with no change in beneficial ownership`; `s 197(3)(b) the person's purpose is presumed by reason of an offer to sell matched by an offer to purchase`; `s 197(3)(c) the person's purpose is presumed by reason of an offer to purchase matched by an offer to sell` |
| s 197(4) | Power / Liability | the person (may rebut the presumption by establishing the facts the subsection names) | the prosecution or claimant (liable to lose the presumption) | `s 197(4) the presumption under subsection (3) is rebutted` |
| s 197(6) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 197(6) the defendant has the defence to a contravention of subsection (2)` |
| s 198(1) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 198(1) the person's transactions contravene the bar on market manipulation in securities of a corporation`; `s 198(1) a person must not carry out 2 or more transactions in a corporation's securities with the intent to induce others to deal` |
| s 198(2) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 198(2) the person's transactions contravene the bar on market manipulation in securities of a business trust`; `s 198(2) a person must not carry out 2 or more transactions in a business trust's securities with the intent to induce others to deal` |
| s 199 | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 199 the person's statement or information contravenes the bar on false or misleading statements`; `s 199 a person must not make a false or misleading statement likely to induce dealing or move the price` |
| s 200(1) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 200(1) the person's conduct contravenes the bar on fraudulently inducing a person to deal`; `s 200(1) a person must not fraudulently induce another person to deal in capital markets products` |
| s 200(2) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 200(2) the defendant has the defence to a contravention constituted by recording or storing information` |
| s 200(3) | Privilege (liberty) / No-right | any party to the proceedings (may adduce the public accountant's opinion as evidence) | the other party (cannot object to its admissibility on that ground) | `s 200(3) the public accountant's opinion is admissible as evidence of the financial position of the company` |
| s 201 | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 201 the person's conduct contravenes the bar on manipulative and deceptive devices`; `s 201 a person must not employ a manipulative or deceptive device in connection with a subscription, purchase or sale` |
| s 201A(1) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 201A(1) the person's execution of an order contravenes the bar on bucketing a derivatives contract`; `s 201A(1) a person must not knowingly execute an order for a derivatives contract without effecting it in good faith` |
| s 201A(2) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 201A(2) the person's execution of an order contravenes the bar on bucketing a spot foreign exchange contract`; `s 201A(2) a person must not knowingly execute an order for a spot foreign exchange contract without effecting it in good faith` |
| s 201B | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 201B the person's conduct contravenes the bar on manipulating the price of derivatives contracts and cornering`; `s 201B a person must not manipulate the price of a derivatives contract or its underlying thing, or corner an underlying thing` |
| s 202(1) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions`; `s 202(1) a person must not circulate a statement or information about the price effect of an illegal transaction` |
| s 203(1) | Claim / Duty | the approved exchange | the person to whom s 203(1) applies | `s 203(1) the person's failure to notify the approved exchange contravenes the bar on failing to disclose`; `s 203(1) the person to whom subsection (1) applies must notify the approved exchange of the information it requires to be disclosed` |
| s 203(3) | Immunity / Disability | the person who failed to notify (not guilty unless the failure is intentional or reckless) | the State (cannot prosecute an innocent failure) | `s 203(3) the contravention of subsection (1) is an offence` |
| s 204(1) | Power / Liability | the court (on prosecution) | the person convicted | `s 204(1) the penalty on conviction for contravening a provision of Division 1`; `s 204(1) the person is guilty of an offence` |
| s 204(2) | Immunity / Disability | the person (a civil penalty has been ordered or agreed) | the prosecutor (cannot institute proceedings for the offence) | `s 204(2) proceedings for an offence in respect of the contravention are barred` |
| s 207(1) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 207(1) the person's conduct contravenes the bar on conduct done to create a false appearance as to a financial benchmark`; `s 207(1) a person must not act for the purpose of creating a false or misleading appearance as to a financial benchmark` |
| s 207(2) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 207(2) the person's conduct contravenes the bar on conduct that creates a false appearance as to a financial benchmark knowingly or recklessly`; `s 207(2) a person must not do a thing that creates a false or misleading appearance as to a financial benchmark knowingly or recklessly` |
| s 208 | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 208 section 207 does not apply to the thing done` |
| s 209 | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 209 the person's statement contravenes the bar on false or misleading statements to a benchmark administrator`; `s 209 a person must not make a false or misleading statement to a person administering a financial benchmark` |
| s 210(1) | Power / Liability | the court (on prosecution) | the person convicted | `s 210(1) the penalty on conviction for contravening a provision of Division 2`; `s 210(1) the person is guilty of an offence` |
| s 210(2) | Immunity / Disability | the person (a civil penalty has been ordered or agreed) | the prosecutor (cannot institute proceedings for the offence) | `s 210(2) proceedings for an offence in respect of the contravention are barred` |
| s 218(2) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 218(2) the connected person's dealing or procuring contravenes the bar`; `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` |
| s 218(3) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 218(3) the connected person's communication of the information contravenes the bar`; `s 218(3) the connected person must not communicate the inside information to a person likely to deal` |
| s 218(4) | Power / Liability | the prosecution or claimant (may rely on the presumption) | the person (subject to the presumption unless rebutted) | `s 218(4) the connected person is presumed to have known that the information was not generally available and might have a material effect` |
| s 218(4A) | Power / Liability | the prosecution or claimant (may rely on the presumption) | the person (subject to the presumption unless rebutted) | `s 218(4A) the presumption in subsection (4B) applies` |
| s 218(4B) | Power / Liability | the prosecution or claimant (may rely on the presumption) | the person (subject to the presumption unless rebutted) | `s 218(4B) the connected person is presumed to have known that the information was not generally available and might have a material effect` |
| s 219(2) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 219(2) the insider's dealing or procuring contravenes the bar`; `s 219(2) the insider must not deal in, or procure dealing in, the securities while in possession of inside information` |
| s 219(3) | Claim / Duty | the State (the Public Prosecutor prosecutes; the Authority may also seek a civil penalty under s 232) | the person (no narrower party is named) | `s 219(3) the insider's communication of the information contravenes the bar`; `s 219(3) the insider must not communicate the inside information to a person likely to deal` |
| s 220(1) | Claim / Duty | the accused or defendant (may require proof) | the prosecution or claimant (bears the burden) | `s 220(1) the prosecution or claimant must prove that the accused or defendant intended to use the information in contravention` |
| s 220(2) | Claim / Duty | the accused or defendant (may require proof) | the prosecution or claimant (bears the burden) | `s 220(2) the prosecution or claimant must prove the absence of facts that would preclude the act from being a contravention by virtue of sections 222 to 230` |
| s 221(1) | Power / Liability | the court (on prosecution) | the person convicted | `s 221(1) the penalty on conviction for contravening section 218 or 219`; `s 221(1) the person is guilty of an offence` |
| s 221(2) | Immunity / Disability | the person (a civil penalty has been ordered or agreed) | the prosecutor (cannot institute proceedings for the offence) | `s 221(2) proceedings for an offence in respect of the contravention are barred` |
| s 222 | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 222 sections 218(2) and 219(2) do not apply to the redemption of units` |
| s 223(1) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 223(1) sections 218(2) and 219(2) do not apply to the underwriting act` |
| s 223(2) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 223(2) sections 218(3) and 219(3) do not apply to the underwriting communication` |
| s 224(1) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 224(1) sections 218(2) and 219(2) do not apply to the purchase` |
| s 224(2) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 224(2) sections 218(2) and 219(2) do not apply to the sale` |
| s 225 | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 225 sections 218(3) and 219(3) do not apply to the communication` |
| s 226(1) | Power / Liability | the State or claimant (may treat the fact as established); the prosecution or claimant (may rely on the presumption) | the person (is treated as having the knowledge or as having procured the act); the person (subject to the presumption unless rebutted) | `s 226(1)(a) the corporation is taken to possess the information that its officer possesses`; `s 226(1)(b) the corporation is presumed to know or ought reasonably to know the matter or thing` |
| s 226(2) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 226(2) the corporation does not contravene section 218(2) or 219(2) by reason of its officer's information` |
| s 227(1) | Power / Liability | the State or claimant (may treat the fact as established); the prosecution or claimant (may rely on the presumption) | the person (is treated as having the knowledge or as having procured the act); the person (subject to the presumption unless rebutted) | `s 227(1)(a) the partner is taken to possess the information that another partner, an employee or a manager possesses`; `s 227(1)(b) every partner is presumed to know or ought reasonably to know the matter or thing` |
| s 227(2) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 227(2) the partners do not contravene section 218(2) or 219(2) by reason of one partner's, manager's or employee's information` |
| s 227(3) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 227(3) the partner does not contravene section 218(2) or 219(2) merely because the partner is taken to possess the information` |
| s 228 | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 228 the individual does not contravene section 218(2) or 219(2) merely because the individual is aware of the individual's own intentions or activities` |
| s 229(1) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 229(1) the corporation does not contravene section 218(2) or 219(2) merely because the corporation is aware of its own intentions or activities` |
| s 229(2) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 229(2) the corporation does not contravene section 218(2) or 219(2) merely because an officer is aware of the corporation's intentions or activities` |
| s 229(4) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 229(4) the person does not contravene section 218(2) or 219(2) by dealing on behalf of a corporation merely because the person is aware of the corporation's intentions or activities` |
| s 230(1) | Privilege (liberty) / No-right | the person (free to do the act: the provision says it is not a contravention) | the State and the Authority (no claim that the act is a contravention) | `s 230(1) the holder or representative does not contravene section 218(2) or 219(2) by an unsolicited transaction for a principal` |
| s 231(1) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 231(1) the person has the parity of information defence to the contravention by dealing or procuring` |
| s 231(2) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 231(2) the person has the parity of information defence to the contravention by communicating` |
| s 232(1) | Power / Liability | the Authority (with the consent of the Public Prosecutor) | the person who has contravened (liable to be sued for a civil penalty) | `s 232(1) the Authority may bring an action in a court against the person to seek an order for a civil penalty` |
| s 232(2) | Power / Liability | the court | the person against whom the order is sought; the person ordered to pay (liable up to the amount) | `s 232(2) the court may make an order against the person for the payment of a civil penalty`; `s 232(2) the highest civil penalty the court may order`; `s 232(2)(a) three times the profit gained or the loss avoided`; `s 232(2)(b) the fixed amount in the cap` |
| s 232(3) | Power / Liability | the court | the person ordered to pay (liable up to the amount) | `s 232(3) the lowest civil penalty the court may order`; `s 232(2) and (3) the civil penalty ordered is within the limits` |
| s 232(4) | Power / Liability | the court | the person against whom the order is sought | `s 232(4) the court may make the order on the terms agreed between the Authority and the defendant despite subsections (2) and (3)` |
| s 232(5) | Privilege (liberty) / No-right | the Authority (free to agree with a person a civil penalty within the limits of subsection (2) or (3)) | the person (cannot say that section 232 forbids the agreement) | `s 232(5) section 232 does not prevent the Authority from entering into the agreement` |
| s 232(6) | Claim / Duty | the Government; the Government (the Consolidated Fund) | the person on whom the civil penalty is imposed | `s 232(6) the civil penalty is to be treated as a judgment debt due to the Government`; `s 232(6) the person on whom a civil penalty is imposed must pay it into the Consolidated Fund` |
| s 232(7) | Power / Liability | the Authority (or the claimant under s 236L(9)(a)) | the person who has not paid | `s 232(7) the Authority may recover the civil penalty on behalf of the Government as though it were a judgment debt due to the Authority` |
| s 232(8) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 232(8) a defence available in a prosecution is also available to the defendant to the action` |
| s 233(1) | Immunity / Disability | the person against whom the action would be brought | the Authority (cannot commence the action under section 232) | `s 233(1) the action under section 232 is barred because 6 years have expired from the date of the contravention` |
| s 233(2) | Immunity / Disability | the person against whom the action would be brought | the Authority (cannot commence the action under section 232) | `s 233(2) the action under section 232 is barred because the person has been convicted or acquitted` |
| s 233(3) | Immunity / Disability | the person (the defendant) | the Authority (cannot continue the action under section 232 until the stay is lifted) | `s 233(3) the action under section 232 must be stayed`; `s 233(3) the stayed action under section 232 may thereafter be continued`; `s 233(3)(a) the person has been discharged in respect of the contravention and the discharge does not amount to an acquittal`; `s 233(3)(b) the charge against the person in respect of the contravention has been withdrawn` |
| s 234(1) | Claim / Duty | the claimant | the contravening person (or the defendant corporation, partnership, officer or other defendant under Division 5) | `s 234(1) the contravening person is liable to pay compensation to the claimant`; `s 234(1)(a) the claimant had been dealing in capital markets products of the same description contemporaneously with the contravention`; `s 234(1)(b) the claimant had suffered loss by reason of the difference in price`; `s 234(1)(b)(ii)(A) the price to compare is the price had the information been generally available`; `s 234(1)(b)(ii)(B) the price to compare is the price had the contravention not occurred` |
| s 234(1A) | Claim / Duty | the claimant | the contravening person (or the defendant corporation, partnership, officer or other defendant under Division 5) | `s 234(1A) the contravening person is liable to pay compensation to the claimant whether or not the person gained a profit or avoided a loss`; `s 234(1A)(a) the contravening person has contravened section 199, 200 or 201 by a false statement or a concealed fact`; `s 234(1A)(b) the claimant relied on the statement or was ignorant of the fact, and suffered loss` |
| s 234(2) | Claim / Duty | the claimant (to the amount of compensation) | the contravening person | `s 234(2) the amount of compensation under subsection (1)` |
| s 234(2A) | Claim / Duty | the claimant (to the amount of compensation elected or ordered) | the contravening person | `s 234(2A) the amount of compensation under subsection (1A)`; `s 234(2A)(a)(i) the amount of the loss referred to in subsection (1)(b)`; `s 234(2A)(a)(ii) the amount of the loss that reasonably results from the claimant's reliance or ignorance`; `s 234(2A)(b) the amount of the loss that reasonably results from the claimant's reliance or ignorance in any other case` |
| s 234(3) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 234(3) a defence available in a prosecution is also available to the defendant to the action` |
| s 234(4) | Immunity / Disability | the person against whom the action would be brought | the claimant (cannot bring the action) | `s 234(4) the action under section 234 is barred because 6 years have expired from the date of completion of the dealing` |
| s 234(6) | Claim / Duty | the claimant (up to the maximum recoverable amount) | the contravening person | `s 234(6) the maximum recoverable amount` |
| s 235(1) | Immunity / Disability | the contravening person (the defendant) | the claimant (cannot bring an action under section 234 without the court's permission) | `s 235(1) no action under section 234 may be brought without the permission of court` |
| s 235(2) | Immunity / Disability | the contravening person (the defendant) | the claimant (a pending action under section 234 is stayed and cannot be continued without the court's permission) | `s 235(2) the pending action under section 234 must be stayed`; `s 235(2) the stayed action may thereafter be continued` |
| s 235(3) | Power / Liability; Claim / Duty | the court; the court (and the other claimants who share the sum) | the Authority or claimant (liable to have permission refused) and the defendant; the claimant | `s 235(3) permission under subsection (1) or (2) may be granted`; `s 235(3) the claimant must comply with the court's directions on the filing and proof of the claim` |
| s 236(1) | Power / Liability | the court | the person against whom the order is sought | `s 236(1) the relevant court may fix a date on or before which all claimants have to file and prove their claims` |
| s 236(2) | Immunity / Disability | the claimants (a date for claims is not earlier than 3 months after the order or conviction is made final) | the court (cannot fix an earlier date) | `s 236(2) the date fixed is not earlier than 3 months from the date the conviction or the order was made final` |
| s 236(3) | Power / Liability | the court | the person against whom the order is sought | `s 236(3) the relevant court may make an order against the contravening person to pay compensation to the claimant` |
| s 236(3A) | Power / Liability | the court | the person ordered to pay (liable up to the amount) | `s 236(3A) the compensation amount ordered is the lesser of paragraphs (a) and (b)`; `s 236(3A) the compensation amount ordered for the claimant` |
| s 236B(1) | Power / Liability | the State (the Public Prosecutor may proceed against the corporation as if it had committed the offence) | the corporation (liable to be proceeded against and punished) | `s 236B(1) the corporation is guilty of the offence as if it had committed the contravention`; `s 236B(1) the corporation is liable to be proceeded against and punished accordingly` |
| s 236B(2) | Immunity / Disability | the corporation (against proceedings under (1) in the cases the subsection names) | the prosecutor (cannot proceed) | `s 236B(2) proceedings against the corporation under subsection (1) are barred` |
| s 236B(3) | Power / Liability | the Authority (with the consent of the Public Prosecutor) | the person who has contravened (liable to be sued for a civil penalty) | `s 236B(3) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` |
| s 236B(4) | Power / Liability | the court | the person against whom the order is sought; the person ordered to pay (liable up to the amount) | `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty`; `s 236B(4) the highest civil penalty the court may order`; `s 236B(4) the lowest civil penalty the court may order` |
| s 236B(7) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 236B(7) the defence is also available to the corporation in an action under subsection (3)` |
| s 236C(1) | Power / Liability | the Authority and the court (a civil penalty may be sought and ordered) | the corporation that failed to prevent or detect (liable to an order for a civil penalty) | `s 236C(1) the corporation commits a contravention and is liable to an order for a civil penalty` |
| s 236C(2) | Power / Liability | the Authority (with the consent of the Public Prosecutor) | the person who has contravened (liable to be sued for a civil penalty) | `s 236C(2) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` |
| s 236C(3) | Power / Liability | the court | the person against whom the order is sought; the person ordered to pay (liable up to the amount) | `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty`; `s 236C(3) the highest civil penalty the court may order`; `s 236C(3) the lowest civil penalty the court may order` |
| s 236C(6) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 236C(6) the defence is also available to the corporation in an action under subsection (2)` |
| s 236D(1) | Claim / Duty | the claimant | the contravening person (or the defendant corporation, partnership, officer or other defendant under Division 5) | `s 236D(1) the corporation is liable to pay compensation to the claimant`; `s 236D(1)(b)(ii)(A) the price to compare is the price had the information been generally available`; `s 236D(1)(b)(ii)(B) the price to compare is the price had the contravention not occurred` |
| s 236D(2) | Power / Liability | the court | the person ordered to pay (liable up to the amount) | `s 236D(2) the amount of compensation under subsection (1)` |
| s 236D(3) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 236D(3) the defence is also available to the corporation in an action under this section` |
| s 236D(4) | Immunity / Disability | the person against whom the action would be brought | the claimant (cannot bring the action) | `s 236D(4) the action under section 236D is barred because 6 years have expired from the date of completion of the dealing` |
| s 236D(6) | Power / Liability | the court | the person ordered to pay (liable up to the amount) | `s 236D(6) the maximum recoverable amount` |
| s 236E(1) | Power / Liability | the State (the Public Prosecutor may proceed against the partnership as if it had committed the offence) | the partnership or limited liability partnership (liable to be proceeded against and punished) | `s 236E(1) the partnership or limited liability partnership is guilty of the offence as if it had committed the contravention`; `s 236E(1) the partnership or limited liability partnership is liable to be proceeded against and punished accordingly` |
| s 236E(2) | Immunity / Disability | the partnership or limited liability partnership (against proceedings under (1) in the cases the subsection names) | the prosecutor (cannot proceed) | `s 236E(2) proceedings against the partnership or limited liability partnership under subsection (1) are barred` |
| s 236E(3) | Power / Liability | the Authority (with the consent of the Public Prosecutor) | the person who has contravened (liable to be sued for a civil penalty) | `s 236E(3) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` |
| s 236E(4) | Power / Liability | the court | the person against whom the order is sought; the person ordered to pay (liable up to the amount) | `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236E(4) the highest civil penalty the court may order`; `s 236E(4) the lowest civil penalty the court may order` |
| s 236E(7) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 236E(7) the defence is also available to the partnership or limited liability partnership in an action under subsection (3)` |
| s 236F(1) | Power / Liability | the Authority and the court (a civil penalty may be sought and ordered) | the partnership or limited liability partnership that failed to prevent or detect (liable to an order for a civil penalty) | `s 236F(1) the partnership or limited liability partnership commits a contravention and is liable to an order for a civil penalty` |
| s 236F(2) | Power / Liability | the Authority (with the consent of the Public Prosecutor) | the person who has contravened (liable to be sued for a civil penalty) | `s 236F(2) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` |
| s 236F(3) | Power / Liability | the court | the person against whom the order is sought; the person ordered to pay (liable up to the amount) | `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty`; `s 236F(3) the highest civil penalty the court may order`; `s 236F(3) the lowest civil penalty the court may order` |
| s 236F(6) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 236F(6) the defence is also available to the partnership or limited liability partnership in an action under subsection (2)` |
| s 236G(1) | Claim / Duty | the claimant | the contravening person (or the defendant corporation, partnership, officer or other defendant under Division 5) | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant`; `s 236G(1)(b)(ii)(A) the price to compare is the price had the information been generally available`; `s 236G(1)(b)(ii)(B) the price to compare is the price had the contravention not occurred` |
| s 236G(2) | Power / Liability | the court | the person ordered to pay (liable up to the amount) | `s 236G(2) the amount of compensation under subsection (1)` |
| s 236G(3) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 236G(3) the defence is also available to the partnership or limited liability partnership in an action under this section` |
| s 236G(4) | Immunity / Disability | the person against whom the action would be brought | the claimant (cannot bring the action) | `s 236G(4) the action under section 236G is barred because 6 years have expired from the date of completion of the dealing` |
| s 236G(6) | Power / Liability | the court | the person ordered to pay (liable up to the amount) | `s 236G(6) the maximum recoverable amount` |
| s 236H(1) | Power / Liability | the Authority (with the consent of the Public Prosecutor) | the person who has contravened (liable to be sued for a civil penalty) | `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` |
| s 236H(2) | Power / Liability | the court | the person against whom the order is sought; the person ordered to pay (liable up to the amount) | `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty`; `s 236H(2) the highest civil penalty the court may order`; `s 236H(2) the lowest civil penalty the court may order` |
| s 236H(5) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 236H(5) the defence is also available to the defendant in an action under subsection (1)` |
| s 236I(1) | Claim / Duty | the claimant | the contravening person (or the defendant corporation, partnership, officer or other defendant under Division 5) | `s 236I(1) the defendant is liable to pay compensation to the claimant`; `s 236I(1)(b)(ii)(A) the price to compare is the price had the information been generally available`; `s 236I(1)(b)(ii)(B) the price to compare is the price had the contravention not occurred` |
| s 236I(2) | Power / Liability | the court | the person ordered to pay (liable up to the amount) | `s 236I(2) the amount of compensation under subsection (1)` |
| s 236I(3) | Immunity / Disability | the person (defendant) | the court (cannot convict, or order a penalty or compensation, on proof of the defence) | `s 236I(3) the defence is also available to the defendant in an action under this section` |
| s 236I(4) | Immunity / Disability | the person against whom the action would be brought | the claimant (cannot bring the action) | `s 236I(4) the action under section 236I is barred because 6 years have expired from the date of completion of the dealing` |
| s 236I(6) | Power / Liability | the court | the person ordered to pay (liable up to the amount) | `s 236I(6) the maximum recoverable amount` |
| s 236J(1) | Immunity / Disability | the person (the defendant) | the claimant or the Authority (cannot bring or continue the action without permission or the stay lifted) | `s 236J(1) no action against the defendant may be brought without the permission of court`; `s 236J(1) the pending action must be stayed`; `s 236J(1) the stayed action may thereafter be continued` |
| s 236J(2) | Power / Liability | the court | the Authority or claimant (liable to have permission refused) and the defendant | `s 236J(2) permission under subsection (1) may be granted` |
| s 236J(3) | Immunity / Disability | the person (the defendant) | the claimant or the Authority (cannot bring or continue the action without permission or the stay lifted) | `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court`; `s 236J(3) the pending action under section 236D, 236G or 236I must be stayed`; `s 236J(3) the stayed action under section 236D, 236G or 236I may thereafter be continued` |
| s 236J(4) | Power / Liability; Claim / Duty | the court; the court (and the other claimants who share the sum) | the Authority or claimant (liable to have permission refused) and the defendant; the claimant | `s 236J(4) permission under subsection (3) may be granted`; `s 236J(4) the claimant must comply with the court's directions on the filing and proof of the claim` |
| s 236K(1) | Power / Liability | the court | the person against whom the order is sought | `s 236K(1) the court may fix a date on or before which all claimants have to file and prove their claims` |
| s 236L(1) | Power / Liability | the court | the person against whom the order is sought | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` |
| s 236L(2) | Claim / Duty | the third party (to notice and an opportunity to show cause) | the court (must give them before ordering disgorgement) | `s 236L(2) the third party is to be given notice and an opportunity to show cause why the order should not be made` |
| s 236L(3) | Immunity / Disability | the third party (against an application for disgorgement made after 6 years from the contravention) | the Authority (cannot apply out of time) | `s 236L(3) the application for an order for disgorgement is barred because 6 years have expired from the date of the contravention` |
| s 236L(4) | Immunity / Disability | the third party (against an order, or against an order for the entire benefit, in the cases the subsection names) | the court (cannot make the order) | `s 236L(4) the court is not to make an order for disgorgement, or not of the entire benefit, against the third party` |
| s 236L(5) | Power / Liability | the court | the person against whom the order is sought | `s 236L(5) the court may make an order for disgorgement against the third party of a sum that is equitable` |
| s 236L(6) | Power / Liability | the court | the person against whom the order is sought | `s 236L(6) the court may fix a date on or before which all claimants have to file and prove their claims`; `s 236L(6) the date fixed is not earlier than 6 months from the date the order for disgorgement was made final` |
| s 236L(7) | Power / Liability | the court | the person against whom the order is sought | `s 236L(7) the court may order that the claimant be paid out of the sum under the final order for disgorgement`; `s 236L(7) the amount to be paid to the claimant out of the sum under the final order for disgorgement` |
| s 236L(8) | Claim / Duty | the Government (the Consolidated Fund) | the person who holds the sum remaining under the order (it is to be paid into the Consolidated Fund) | `s 236L(8) the sum remaining under the order to be paid into the Consolidated Fund` |
| s 236L(9) | Power / Liability; Claim / Duty | the Authority (or the claimant under s 236L(9)(a)); each claimant and the Authority under the order for disgorgement | the person who has not paid; the third party | `s 236L(9)(a) each claimant may recover the sum due as though it were a judgment debt due to the claimant`; `s 236L(9) the third party must pay the sums under the order for disgorgement within the time specified in the court order`; `s 236L(9)(b) the Authority may recover the remaining sum as though it were a judgment debt due to the Authority` |
| s 236L(10) | Immunity / Disability | the third party (against a subsequent application for disgorgement) | the Authority and claimants (cannot apply again) | `s 236L(10) no subsequent application for an order for disgorgement may be made against the third party` |
| s 237 | Power / Liability | a District Court (jurisdiction over an action or application under Division 4 or 5, whatever the amount) | the parties to that action or application (subject to the court) | `s 237 a District Court has jurisdiction to hear and determine the action or application regardless of the monetary amount` |

Provisions that create no relation (`none`): s 196, s 196A, s 197(5), s 197(7), s 198(3), s 202(2), s 203(2), s 205, s 206, s 213, s 214(1), s 214(2), s 215, s 216, s 217(1), s 217(2), s 218(1), s 218(1A), s 218(5), s 218(6), s 219(1), s 229(3), s 229(5), s 230(2), s 234(5), s 236(4), s 236(5), s 236A, s 236B(6), s 236B(8), s 236B(9), s 236C(5), s 236C(7), s 236D(5), s 236E(6), s 236E(8), s 236E(9), s 236F(5), s 236F(7), s 236G(5), s 236H(4), s 236I(5), s 236K(2), s 236K(3), s 236L(11), s 236L(12).
They are definitions, scope rules ("this Division applies to"), counting rules and deeming rules of interpretation, or they carry the relation of another provision (for example s 218(1) and s 219(1) switch on the duties of s 218(2) and (3), s 219(2) and (3); ss 236B(6), 236C(5), 236E(6), 236F(5), 236H(4) apply ss 232(4) to (7) and 233 to the action).
The sections the text shows repealed (ss 211, 212) and the deleted subsections create nothing.
Coverage check: every one of the 179 provisions of layer 1 (a section or subsection that has a function) is in the table above or in the `none` list: 133 relation rows and 46 `none`.
Section 238 (rules of court) is inert (reason 2) and has no row here.

## Marginal readings for a lawyer (sfab)

The two readings the brief leaves to a lawyer: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
I took both as the status quo.
Every branch that rests on one carries `-- MARGINAL-READING (a)` or `(b)` on its own line; they are listed here with the other reading.
The other reading of (a) is `NOTHING` (the "if" is not the text's no); the other reading of (b) is `JUST FALSE` (the limit is the text's no).

| provision | function | at | reading | answer taken | other reading | words | split site |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s 197(4) | `s 197(4) the presumption under subsection (3) is rebutted` | `sfab-division-1.l4:349` | (a) | JUST FALSE | NOTHING | "may be rebutted if the defendant establishes" |  |
| s 197(5) | `s 197(5) the purchase or sale does not involve a change in the beneficial ownership` | `sfab-division-1.l4:373` | (a) | JUST FALSE | NOTHING | "does not involve a change in the beneficial ownership if any of the following persons has an interest" |  |
| s 202(2) | `s 202(2) a condition in subsection (1) is satisfied` | `sfab-division-1.l4:799` | (a) | JUST FALSE | NOTHING | "the condition is either" |  |
| s 204(2) | `s 204(2) proceedings for an offence in respect of the contravention are barred` | `sfab-division-1.l4:993` | (b) | NOTHING | JUST FALSE | "No proceedings shall be instituted against a person for an offence in respect of a contravention of any of the provisions of this Division after" |  |
| s 210(2) | `s 210(2) proceedings for an offence in respect of the contravention are barred` | `sfab-division-2.l4:273` | (b) | NOTHING | JUST FALSE | "No proceedings shall be instituted against a person for an offence in respect of a contravention of any of the provisions of this Division after" |  |
| s 215 | `s 215 the information is generally available` | `sfab-insider-1.l4:335` | (a) | JUST FALSE | NOTHING | "information is generally available if" |  |
| s 216 | `s 216 a reasonable person would be taken to expect the information to have a material effect on the price or value` | `sfab-insider-1.l4:358` | (a) | JUST FALSE | NOTHING | "would be taken to expect information to have a material effect on the price or value of securities, securities‑based derivatives contracts or CIS units, if the information would, or would be likely to, influence" |  |
| s 218(5)(b) | `s 218(5)(b) the person is connected to the corporation` | `sfab-insider-2.l4:71` | (a) | JUST FALSE | NOTHING | "a person is connected to a corporation if" |  |
| s 221(2) | `s 221(2) proceedings for an offence in respect of the contravention are barred` | `sfab-insider-2.l4:536` | (b) | NOTHING | JUST FALSE | "No proceedings shall be instituted against a person for an offence in respect of a contravention of section 218 or 219 after" |  |
| s 226(2) | `s 226(2) the corporation does not contravene section 218(2) or 219(2) by reason of its officer's information` | `sfab-insider-3.l4:191` | (a) | JUST FALSE | NOTHING | "does not contravene section 218(2) or 219(2) by entering into a transaction or agreement at any time merely because of information in the possession of an officer of the corporation if" |  |
| s 227(2) | `s 227(2) the partners do not contravene section 218(2) or 219(2) by reason of one partner's, manager's or employee's information` | `sfab-insider-3.l4:278` | (a) | JUST FALSE | NOTHING | "do not contravene section 218(2) or 219(2) by entering into a transaction or agreement at any time merely because one or more"; "are in actual possession of information if" |  |
| s 230(1) | `s 230(1) the holder or representative does not contravene section 218(2) or 219(2) by an unsolicited transaction for a principal` | `sfab-insider-3.l4:434` | (a) | JUST FALSE | NOTHING | "does not contravene section 218(2) or 219(2) by subscribing for, purchasing or selling"; "if" |  |
| s 232(1) | `s 232(1) the Authority may bring an action in a court against the person to seek an order for a civil penalty` | `sfab-civil.l4:31` | (b) | NOTHING | JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action" | SS-052 |
| s 232(2) | `s 232(2) the court may make an order against the person for the payment of a civil penalty` | `sfab-civil.l4:45` | (a) | NOTHING | JUST FALSE | "the court may make an order against the person for the payment of a civil penalty" | SS-053 |
| s 232(4) | `s 232(4) the court may make the order on the terms agreed between the Authority and the defendant despite subsections (2) and (3)` | `sfab-civil.l4:117` | (a) | NOTHING | JUST FALSE | "the court may make an order against a person against whom an action has been brought under this section if the Authority, with the consent of the Public Prosecutor, has agreed" | SS-054 |
| s 232(7) | `s 232(7) the Authority may recover the civil penalty on behalf of the Government as though it were a judgment debt due to the Authority` | `sfab-civil.l4:171` | (a) | NOTHING | JUST FALSE | "the Authority may recover the civil penalty on behalf of the Government" | SS-055 |
| s 233(1) | `s 233(1) the action under section 232 is barred because 6 years have expired from the date of the contravention` | `sfab-civil.l4:198` | (b) | JUST FALSE | NOTHING | "must not be commenced after the expiration of 6 years from the date of the contravention" |  |
| s 233(2) | `s 233(2) the action under section 232 is barred because the person has been convicted or acquitted` | `sfab-civil.l4:215` | (a) | JUST FALSE | NOTHING | "must not be commenced if the person has been convicted or acquitted in criminal proceedings"; "except where the person has been acquitted on the ground of the withdrawal of the charge" |  |
| s 233(3) | `s 233(3) the action under section 232 must be stayed` | `sfab-civil.l4:228` | (b) | NOTHING | JUST FALSE | "must be stayed after criminal proceedings have been commenced against the person" |  |
| s 233(3) | `s 233(3) the stayed action under section 232 may thereafter be continued` | `sfab-civil.l4:239` | (b) | NOTHING | JUST FALSE | "must be stayed after criminal proceedings have been commenced against the person" |  |
| s 234(1) | `s 234(1) the contravening person is liable to pay compensation to the claimant` | `sfab-civil.l4:343` | (a) | JUST FALSE | NOTHING | "is, if the contravening person had gained a profit or avoided a loss as a result of that contravention" | SS-057 |
| s 234(1) | `s 234(1) the contravening person is liable to pay compensation to the claimant` | `sfab-civil.l4:346` | (b) | NOTHING | JUST FALSE | "liable to pay compensation to any person"; "(called in this section and sections 235 and 236 the claimant) who" | SS-058 |
| s 234(1A) | `s 234(1A) the contravening person is liable to pay compensation to the claimant whether or not the person gained a profit or avoided a loss` | `sfab-civil.l4:398` | (b) | NOTHING | JUST FALSE | "the contravening person is, whether or not the contravening person had gained a profit or avoided a loss as a result of that contravention"; "liable to pay compensation to the claimant, if" | SS-059 |
| s 234(4) | `s 234(4) the action under section 234 is barred because 6 years have expired from the date of completion of the dealing` | `sfab-civil.l4:538` | (b) | JUST FALSE | NOTHING | "must not be commenced after the expiration of 6 years from the date of completion of the dealing in which the loss occurred" |  |
| s 235(1) | `s 235(1) no action under section 234 may be brought without the permission of court` | `sfab-civil.l4:668` | (b) | NOTHING | JUST FALSE | "in respect of a contravention of any of the provisions in this Part which resulted in the contravening person gaining a profit or avoiding a loss" |  |
| s 235(1) | `s 235(1) no action under section 234 may be brought without the permission of court` | `sfab-civil.l4:670` | (b) | NOTHING | JUST FALSE | "after the commencement of" |  |
| s 235(1) | `s 235(1) no action under section 234 may be brought without the permission of court` | `sfab-civil.l4:672` | (a) | JUST FALSE | NOTHING | "Except with the permission of court" |  |
| s 235(2) | `s 235(2) the pending action under section 234 must be stayed` | `sfab-civil.l4:694` | (b) | NOTHING | JUST FALSE | "being an action that is pending on the date of commencement of" |  |
| s 235(2) | `s 235(2) the stayed action may thereafter be continued` | `sfab-civil.l4:704` | (b) | NOTHING | JUST FALSE | "must be stayed, and may not thereafter be continued except with the permission of court" |  |
| s 236(1) | `s 236(1) the relevant court may fix a date on or before which all claimants have to file and prove their claims` | `sfab-civil.l4:809` | (b) | NOTHING | JUST FALSE | "after the conviction or the order imposing the civil penalty has been made final" | SS-061 |
| s 236(3) | `s 236(3) the relevant court may make an order against the contravening person to pay compensation to the claimant` | `sfab-civil.l4:838` | (b) | NOTHING | JUST FALSE | "may, after the expiry of the date fixed under subsection (1), make an order" | SS-062 |
| s 236(3) | `s 236(3) the relevant court may make an order against the contravening person to pay compensation to the claimant` | `sfab-civil.l4:840` | (b) | NOTHING | JUST FALSE | "to each claimant who has filed and proven that claimant's claim for compensation" | SS-063 |
| s 236(4) | `s 236(4) the conviction is made final` | `sfab-civil.l4:758` | (a) | JUST FALSE | NOTHING | "a conviction is made final if" |  |
| s 236(5) | `s 236(5) the order imposing a civil penalty is made final` | `sfab-civil.l4:781` | (a) | JUST FALSE | NOTHING | "an order imposing a civil penalty is made final if" |  |
| s 236B(1) | `s 236B(1) the corporation is guilty of the offence as if it had committed the contravention` | `sfab-attributed.l4:97` | (a) | JUST FALSE | NOTHING | "Where an offence of contravening any provision in this Part is proved to have been committed by an employee or an officer of a corporation" | SS-064 |
| s 236B(2) | `s 236B(2) proceedings against the corporation under subsection (1) are barred` | `sfab-attributed.l4:125` | (b) | NOTHING | JUST FALSE | "No proceedings shall be instituted against a corporation under subsection (1) after" |  |
| s 236B(3) | `s 236B(3) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` | `sfab-attributed.l4:145` | (b) | NOTHING | JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the corporation" | SS-066 |
| s 236B(4) | `s 236B(4) the court may make an order against the corporation for the payment of a civil penalty` | `sfab-attributed.l4:170` | (a) | NOTHING | JUST FALSE | "If the court in subsection (3) is satisfied on a balance of probabilities that the corporation is liable to be punished under subsection (1)" | SS-067 |
| s 236C(1) | `s 236C(1) the corporation commits a contravention and is liable to an order for a civil penalty` | `sfab-attributed.l4:308` | (b) | NOTHING | JUST FALSE | "A corporation which fails to prevent or detect a contravention of any provision in this Part committed by an employee or officer of the corporation" | SS-068 |
| s 236C(2) | `s 236C(2) the Authority may bring an action in a court against the corporation to seek an order for a civil penalty` | `sfab-attributed.l4:325` | (b) | NOTHING | JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the corporation" | SS-070 |
| s 236C(3) | `s 236C(3) the court may make an order against the corporation for the payment of a civil penalty` | `sfab-attributed.l4:349` | (a) | NOTHING | JUST FALSE | "If the court is satisfied on a balance of probabilities that the corporation has committed a contravention under subsection (1)" | SS-071 |
| s 236D(1) | `s 236D(1) the corporation is liable to pay compensation to the claimant` | `sfab-attributed.l4:457` | (b) | NOTHING | JUST FALSE | "A defendant corporation which has gained a profit or avoided a loss as a result of the contravention of a provision in this Part by the contravening person referred to in section 236B(1) or 236C(1)" | SS-072 |
| s 236D(1) | `s 236D(1) the corporation is liable to pay compensation to the claimant` | `sfab-attributed.l4:459` | (b) | NOTHING | JUST FALSE | "which has gained a profit or avoided a loss as a result of the contravention" | SS-073 |
| s 236D(1) | `s 236D(1) the corporation is liable to pay compensation to the claimant` | `sfab-attributed.l4:462` | (b) | NOTHING | JUST FALSE | "any person (called in this section the claimant) who" | SS-074 |
| s 236D(4) | `s 236D(4) the action under section 236D is barred because 6 years have expired from the date of completion of the dealing` | `sfab-attributed.l4:536` | (b) | JUST FALSE | NOTHING | "must not be commenced after the expiration of 6 years from the date of completion of the contemporaneous dealing in which the loss occurred" |  |
| s 236E(1) | `s 236E(1) the partnership or limited liability partnership is guilty of the offence as if it had committed the contravention` | `sfab-attributed.l4:599` | (a) | JUST FALSE | NOTHING | "Where an offence of contravening any provision of this Part is proved to have been committed by a partner or employee of a partnership or a partner, manager or employee of a limited liability partnership" | SS-075 |
| s 236E(2) | `s 236E(2) proceedings against the partnership or limited liability partnership under subsection (1) are barred` | `sfab-attributed.l4:629` | (b) | NOTHING | JUST FALSE | "No proceedings shall be instituted against any partner of the partnership or the limited liability partnership under subsection (1) after" |  |
| s 236E(3) | `s 236E(3) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` | `sfab-attributed.l4:651` | (b) | NOTHING | JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the partnership or limited liability partnership" | SS-077 |
| s 236E(4) | `s 236E(4) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty` | `sfab-attributed.l4:677` | (a) | NOTHING | JUST FALSE | "If the court in subsection (3) is satisfied on a balance of probabilities that the partnership or limited liability partnership is liable to be punished under subsection (1)" | SS-078 |
| s 236F(1) | `s 236F(1) the partnership or limited liability partnership commits a contravention and is liable to an order for a civil penalty` | `sfab-attributed.l4:823` | (b) | NOTHING | JUST FALSE | "A partnership or limited liability partnership which fails to prevent or detect a contravention of any provision in this Part committed by a partner or employee of the partnership or a partner, manager or employee of the limited liability partnership, as the case may be" | SS-079 |
| s 236F(2) | `s 236F(2) the Authority may bring an action in a court against the partnership or limited liability partnership to seek an order for a civil penalty` | `sfab-attributed.l4:841` | (b) | NOTHING | JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the partnership or limited liability partnership" | SS-081 |
| s 236F(3) | `s 236F(3) the court may make an order against the partnership or limited liability partnership for the payment of a civil penalty` | `sfab-attributed.l4:866` | (a) | NOTHING | JUST FALSE | "If the court is satisfied on a balance of probabilities that the partnership or limited liability partnership has committed a contravention under subsection (1)" | SS-082 |
| s 236G(1) | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | `sfab-attributed.l4:977` | (b) | NOTHING | JUST FALSE | "A defendant partnership which has gained a profit or avoided a loss as a result of the contravention of a provision in this Part by the contravening person referred to in section 236E(1) or 236F(1)" | SS-083 |
| s 236G(1) | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | `sfab-attributed.l4:979` | (b) | NOTHING | JUST FALSE | "which has gained a profit or avoided a loss as a result of the contravention" | SS-084 |
| s 236G(1) | `s 236G(1) the partnership or limited liability partnership is liable to pay compensation to the claimant` | `sfab-attributed.l4:982` | (b) | NOTHING | JUST FALSE | "any person (called in this section the claimant) who" | SS-085 |
| s 236G(4) | `s 236G(4) the action under section 236G is barred because 6 years have expired from the date of completion of the dealing` | `sfab-attributed.l4:1056` | (b) | JUST FALSE | NOTHING | "must not be commenced after the expiration of 6 years from the date of completion of the contemporaneous dealing in which the loss occurred" |  |
| s 236H(1) | `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` | `sfab-attributed.l4:1129` | (b) | NOTHING | JUST FALSE | "the Authority may, with the consent of the Public Prosecutor, bring an action in a court against the defendant" | SS-087 |
| s 236H(2) | `s 236H(2) the court may make an order against the defendant for the payment of a civil penalty` | `sfab-attributed.l4:1153` | (a) | NOTHING | JUST FALSE | "If the court is satisfied on a balance of probabilities that the contravening person has contravened a provision in this Part with the consent or connivance of the defendant" | SS-088 |
| s 236I(1) | `s 236I(1) the defendant is liable to pay compensation to the claimant` | `sfab-attributed.l4:1241` | (b) | NOTHING | JUST FALSE | "A defendant who has gained a profit or avoided a loss as a result of the contravention of a provision in this Part by a contravening person referred to in section 236H(1)" | SS-089 |
| s 236I(1) | `s 236I(1) the defendant is liable to pay compensation to the claimant` | `sfab-attributed.l4:1243` | (b) | NOTHING | JUST FALSE | "who has gained a profit or avoided a loss as a result of the contravention" | SS-090 |
| s 236I(1) | `s 236I(1) the defendant is liable to pay compensation to the claimant` | `sfab-attributed.l4:1246` | (b) | NOTHING | JUST FALSE | "any person (called in this section the claimant)" | SS-091 |
| s 236I(4) | `s 236I(4) the action under section 236I is barred because 6 years have expired from the date of completion of the dealing` | `sfab-attributed.l4:1318` | (b) | JUST FALSE | NOTHING | "must not be commenced after the expiration of 6 years from the date of completion of the contemporaneous dealing in which the loss occurred" |  |
| s 236J(1) | `s 236J(1) no action against the defendant may be brought without the permission of court` | `sfab-attributed.l4:1388` | (b) | NOTHING | JUST FALSE | "no action may be brought against" |  |
| s 236J(1) | `s 236J(1) no action against the defendant may be brought without the permission of court` | `sfab-attributed.l4:1390` | (b) | NOTHING | JUST FALSE | "after the commencement of" |  |
| s 236J(1) | `s 236J(1) no action against the defendant may be brought without the permission of court` | `sfab-attributed.l4:1392` | (a) | JUST FALSE | NOTHING | "Except with the permission of court" |  |
| s 236J(1) | `s 236J(1) the pending action must be stayed` | `sfab-attributed.l4:1406` | (b) | NOTHING | JUST FALSE | "any such action in paragraph (a), (b) or (c) pending on the date of commencement" |  |
| s 236J(1) | `s 236J(1) the stayed action may thereafter be continued` | `sfab-attributed.l4:1416` | (b) | NOTHING | JUST FALSE | "must be stayed, and may not thereafter be continued except with the permission of court" |  |
| s 236J(3) | `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court` | `sfab-attributed.l4:1467` | (b) | NOTHING | JUST FALSE | "no action under section 236D, 236G or 236I may be brought against the defendant corporation, defendant partnership or defendant in respect of a primary contravention" |  |
| s 236J(3) | `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court` | `sfab-attributed.l4:1469` | (b) | NOTHING | JUST FALSE | "after the commencement of" |  |
| s 236J(3) | `s 236J(3) no action under section 236D, 236G or 236I may be brought without the permission of court` | `sfab-attributed.l4:1471` | (a) | JUST FALSE | NOTHING | "Except with the permission of court" |  |
| s 236J(3) | `s 236J(3) the pending action under section 236D, 236G or 236I must be stayed` | `sfab-attributed.l4:1485` | (b) | NOTHING | JUST FALSE | "pending on the date of commencement of the proceedings or action in paragraph (a), (b) or (c)" |  |
| s 236J(3) | `s 236J(3) the stayed action under section 236D, 236G or 236I may thereafter be continued` | `sfab-attributed.l4:1495` | (b) | NOTHING | JUST FALSE | "must be stayed, and may not thereafter be continued except with the permission of court" |  |
| s 236K(1) | `s 236K(1) the court may fix a date on or before which all claimants have to file and prove their claims` | `sfab-attributed.l4:1560` | (b) | NOTHING | JUST FALSE | "may, after the conviction or the order imposing the civil penalty has been made final, fix a date" | SS-093 |
| s 236L(1) | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | `sfab-attributed.l4:1649` | (b) | NOTHING | JUST FALSE | "the court may, on the application of the Authority or any claimant, make an order" | SS-095 |
| s 236L(1) | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` | `sfab-attributed.l4:1651` | (b) | NOTHING | JUST FALSE | "against any other person (called in this section a third party) who has received the whole or any part of the benefit of that contravention" | SS-096 |
| s 236L(3) | `s 236L(3) the application for an order for disgorgement is barred because 6 years have expired from the date of the contravention` | `sfab-attributed.l4:1679` | (b) | JUST FALSE | NOTHING | "must not be commenced after the expiration of 6 years from the date on which the contravention referred to in that subsection was committed" |  |
| s 236L(4) | `s 236L(4) the court is not to make an order for disgorgement, or not of the entire benefit, against the third party` | `sfab-attributed.l4:1704` | (a) | JUST FALSE | NOTHING | "if the court is satisfied, on a balance of probabilities, that" |  |
| s 236L(5) | `s 236L(5) the court may make an order for disgorgement against the third party of a sum that is equitable` | `sfab-attributed.l4:1716` | (b) | NOTHING | JUST FALSE | "against a third party referred to in subsection (4) of a sum that is, in the opinion of the court, equitable" | SS-097 |
| s 236L(6) | `s 236L(6) the court may fix a date on or before which all claimants have to file and prove their claims` | `sfab-attributed.l4:1730` | (b) | NOTHING | JUST FALSE | "The court may, after the order for disgorgement has been made final, fix a date" | SS-098 |
| s 236L(7) | `s 236L(7) the court may order that the claimant be paid out of the sum under the final order for disgorgement` | `sfab-attributed.l4:1754` | (b) | NOTHING | JUST FALSE | "The court may, after the expiry of the date fixed under subsection (6), order" | SS-099 |
| s 236L(7) | `s 236L(7) the court may order that the claimant be paid out of the sum under the final order for disgorgement` | `sfab-attributed.l4:1756` | (b) | NOTHING | JUST FALSE | "each claimant who has filed and proven the claimant’s claim for compensation" | SS-100 |
| s 236L(9) | `s 236L(9)(a) each claimant may recover the sum due as though it were a judgment debt due to the claimant` | `sfab-attributed.l4:1809` | (a) | NOTHING | JUST FALSE | "each claimant may recover the sum due to the claimant under the order for disgorgement" | SS-101 |
| s 236L(9) | `s 236L(9)(b) the Authority may recover the remaining sum as though it were a judgment debt due to the Authority` | `sfab-attributed.l4:1833` | (a) | NOTHING | JUST FALSE | "the remaining sum under the order for disgorgement may be recovered by the Authority" | SS-102 |
| s 236L(10) | `s 236L(10) no subsequent application for an order for disgorgement may be made against the third party` | `sfab-attributed.l4:1847` | (b) | NOTHING | JUST FALSE | "After the expiry of the date fixed under subsection (6), no person may make any subsequent application" |  |
| s 236L(11) | `s 236L(11) the order for disgorgement is made final` | `sfab-attributed.l4:1868` | (a) | JUST FALSE | NOTHING | "an order for disgorgement is made final if" |  |

Counts: 30 branches rest on reading (a), 55 on reading (b), 85 in all.

Two groups of branches are tagged against the grain, because a dated ruling of the Guide decides them, and the tag lists the reading the ruling set aside:

- **6 branches tagged (b) answer `JUST FALSE`** (s 233(1), s 234(4), s 236D(4), s 236G(4), s 236I(4), s 236L(3)): a period the text fixes in its own words, outside which the Guide gives `JUST FALSE` (periods ruling of 2026-11-05, item (a): "a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`"). Reading (b), a prohibition limited by its own wording does not count as the text's no, would give `NOTHING`.
- **10 branches tagged (a) answer `NOTHING`** (s 232(2), s 232(4), s 232(7), s 236B(4), s 236C(3), s 236E(4), s 236F(3), s 236H(2), s 236L(9)): the "may" functions whose `if` gate failed, which the grant ruling of 2026-11-12, limit 1, answers `NOTHING` ("answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"). Reading (a), a failed "if" counts as the text's no, would give `JUST FALSE`. These are the ten SS (ii) [IF] sites.

**Split sites that fit none of the Guide's dated rulings (16)**: a "may" limited by "with the consent of" (6), "after" (5), "on the application of" (1) or by the persons it names (4).
The only line they rely on is the "In short" sentence ("limits a grant or prohibition in its own wording and the case falls outside the limit"). They are SS-052, SS-061, SS-062, SS-063, SS-066, SS-070, SS-077, SS-081, SS-087, SS-093, SS-095, SS-096, SS-097, SS-098, SS-099, SS-100.

### Reading a result: FALSE and NOTHING (sfab)

Every decision function of this part answers `MAYBE BOOLEAN` (or a number, a `Penalty`, or a regulative rule); a function never turns `NOTHING` into `FALSE`.

- `JUST TRUE` is yes: the provision's condition is met on the facts given (for a bar, "the conduct contravenes the bar"; for an exception, "the exception relieves the case").
- `JUST FALSE` is the text's own no, said in its own words.
  In Part 12 that means: a "means" definition whose limbs all fail; an element the text introduces with "if", "where", "unless", "only if" or "whenever" that is not met (for example `s 197(1)`: "if the person's purpose, or any of the person's purposes, ..." not met); a flat negative ("shall not", "may not", "must not be commenced"); a defence not established, worded as "this section gives no defence on these facts" and never as "no defence at all".
  Each such branch carries `-- FALSE-kind (the text says no in its own words): "<the words>"`, and the words are checked by script to occur in the rendering (work/audit/quotes.py: 318 quoted fragments, 0 problems).
- `NOTHING` is "the text does not say": the case is outside a limit the text puts on a prohibition or a grant in its own wording ("A person must not do any thing ..." when nothing was done; "the Authority may, with the consent of the Public Prosecutor, bring an action" when the consent is missing), a list the text does not close, a term the text leaves undefined, or a matter the text hands to a source outside the folder (the Authority's regulations under section 341, the approved exchange's listing rules, the Rules of Court).
  Each such branch carries `-- NOTHING-kind (<why>)` with one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- A seat question answers the same way.
  `JUST TRUE` is "yes" to the question as it is worded; `JUST FALSE` is "the text says no"; `NOTHING` is "this encoding does not say": a caller must never read `NOTHING` as "no", and in particular a failed gate on a power ("may the Authority bring an action against me") is `NOTHING`, never "the Authority may not".
- A bar is titled as a bar, a permission as a permission, and a defence as a defence: the seat audit below lists the two questions whose names and bodies differed and were fixed.

## Seams (sfab)

A seam is an answer another part, the keel or a later wave computes; a part cannot import another before the merge, so the answer comes in as an INPUT named for the fact (PLAN section 4).
`inputs/XREFS.md` lists the sections my ranges cite that another agent or a later wave encodes: s 2 (keel), s 331, s 335 and s 341 (later).
PLAN section 6 says "Seams: none found" for sfab; the brief governs (see Where PLAN.md and the brief differ).

### Seams I took, and what each is

| other provision | asked in | input (type) | kind |
| --- | --- | --- | --- |
| s 2(1) "debenture" (keel) | s 196A(a) and s 214(1) "debenture" | `the instrument is a debenture as section 2(1) defines it` and `... as section 2 defines it` (MAYBE BOOLEAN) | the keel's answer arrives as an input; NOTHING stays NOTHING |
| s 2(1) "securities-based derivatives contract" (keel) | s 196A(b), s 196A(c), s 214(2) | the keel function is called (`sfa-definitions-products`) with its three inputs | imported keel function (the only keel function called) |
| s 2(1) "administering a financial benchmark" (keel) | s 206 "administer" | `the act is administering a financial benchmark as section 2(1) defines it` (MAYBE BOOLEAN) | input |
| s 2(1) "approved exchange", "organised market", "listing rules" (keel) | s 196, s 203, s 217 | plain BOOLEAN inputs ("the person is an entity whose securities are listed for quotation on an approved exchange", "the person is required by the approved exchange, under the listing rules or any other requirement, to notify it ...") | inputs named for the fact |
| s 3 association (keel; `sfa-associates.l4`) | ss 197(3)(b), (c), 197(5)(b), 202(2)(a), (b), 230(1)(c) | `... (as section 3 reads)` (MAYBE BOOLEAN) | input; the keel's `s 3(1)` is not imported (F-3-assoc) |
| s 331 (later wave: corporate offenders and unincorporated associations) | ss 236H(5) and 236I(3) ("a defence ... if he or she were prosecuted under section 331") and s 236J(3) ("criminal proceedings ... under section 236B(1), 236E(1) or 331") | `a defence would be available to the defendant if he or she were prosecuted under section 331 in respect of that contravention (the answer under the section whose defence it is)` (MAYBE BOOLEAN) and `the action is brought after the commencement of criminal proceedings against the defendant under section 236B(1), 236E(1) or 331 in respect of the same contravention` (BOOLEAN) | input from a later wave; NOTHING stays NOTHING |
| s 335 (later wave: general penalty) | s 203(3) "Despite section 204 or 335" | none: section 335 is named only to be displaced | not a seam |
| s 341 (later wave: regulations) | ss 2(1) "securities-based derivatives contract" prescription (inside the keel function), s 206 "international body" and "public authority" | `regulations under section 341 prescribe the body as an international body`, `the Authority has prescribed the organisation as a public authority by regulations under section 341`, `regulations under section 341 prescribe the contract, or its class, as not being one` (BOOLEAN) | inputs: the regulations are not a source here |
| the Business Trusts Act 2004 s 2 | s 214(1) "trust property" | `the thing is trust property within section 2 of the Business Trusts Act 2004` (BOOLEAN) | input (another Act is never read from memory) |
| the Criminal Procedure Code 2010 ss 377, 378; Rules of Court under s 238 | s 236(4)(c), s 236(5)(c), s 236L(11)(c) | `no notice of appeal ... is lodged within the time prescribed by sections 377 and 378 of the Criminal Procedure Code 2010` and `... by Rules of Court made under section 238` (BOOLEAN) | inputs: the prescribed times are not in this Act |
| the approved exchange's listing rules | s 203(1) | `the number of days within which the approved exchange requires the person to notify it` (NUMBER) | input (F-203-days) |

### Seams between my own modules

My modules do not import each other (a name defined in two imported modules cannot be used, and the seat layer imports all of them), so where a function needs the answer of another provision's function, in the same module or in another, the answer is an input whose name ends `(the answer under section N)`; the seat layer feeds each from the function that computes it:

| the answer under | taken as an input in |
| --- | --- |
| section 196(a) | division-1 |
| section 196(b) | division-1 |
| section 197(3) | division-1 |
| section 197(3)(a) | division-1 |
| section 197(3)(b) | division-1 |
| section 197(3)(c) | division-1 |
| section 197(5) | division-1 |
| section 202(2) | division-1 |
| section 203(1) | division-1 |
| section 203(2) | division-1 |
| section 205(a) | division-2 |
| section 205(b) | division-2 |
| section 206 | division-2 |
| section 213(a) | insider-1 |
| section 213(b) | insider-1 |
| section 215 | insider-2 |
| section 216 | insider-2 |
| section 218(1) | insider-2 |
| section 218(1) or (1A) | insider-2 |
| section 218(1A) | insider-2 |
| section 218(4A) | insider-2 |
| section 218(5)(a) | insider-2 |
| section 218(5)(b) | insider-2 |
| section 219(1) | insider-2 |
| section 229(3) | insider-3 |
| section 229(5) | insider-3 |
| section 232(2) | civil |
| section 232(2) and (3) | civil |
| section 232(2)(a) | civil |
| section 232(2)(b) | civil |
| section 232(3) | civil |
| section 233(3) | civil |
| section 233(3)(a) | civil |
| section 233(3)(b) | civil |
| section 234(1) | attributed |
| section 234(1)(a) | civil |
| section 234(1)(b) | civil |
| section 234(1A)(a) | civil |
| section 234(1A)(b) | civil |
| section 234(2A)(a)(i) | civil |
| section 234(2A)(a)(ii) | civil |
| section 234(2A)(b) | civil |
| section 234(6) | civil |
| section 235(2) | civil |
| section 236(4) or (5) | civil |
| section 236(4) or (5) as applied by section 236K(2) | attributed |
| section 236A | attributed |
| section 236D(6) | attributed |
| section 236G(6) | attributed |
| section 236I(6) | attributed |
| section 236J(1) | attributed |
| section 236J(3) | attributed |
| section 236L(11) | attributed |
| section 236L(4) | attributed |
| the section contravened | civil |
| the section that is contravened | division-1, division-2, insider-2 |
| the section whose defence it is | attributed, civil |

The seat layer feeds each such input from the answer of the function that computes it, and does not restate a rule.

### Sections of mine that other parts cite (from `inputs/XREFS.md`)

Later waves cite ss 197, 198, 199, 200, 201, 202 and 218 (line 51504), s 209 (line 51873), and ss 232 and 234 (line 53513) of this Act; the keel also cites "section 200", "section 204" and "section 209" at lines 2945 to 3089, which are sections of the Financial Services and Markets Act 2022, not of this Act, so there is no seam there (PLAN section 4.1, and its finding 5).
The functions a later wave would call are the ones named `s 197(1) ...`, `s 218(2) ...`, `s 232(1) ...`, `s 234(1) ...` in the coverage table.

## Split sites (sfab)

The two questions the Guide leaves to the encoder, recorded site by site: (i) an unmet element of an offence or a contravention (`JUST FALSE` or `NOTHING`?); (ii) a "may" gated by "where", "when", "upon", "on application", "with the consent of" and the like (`JUST FALSE`, the periods ruling's rule (b), or `NOTHING`, the grant ruling?).
I adopted no blanket rule: each site was decided on its own words and the Guide line it relies on is quoted in its fork line (Fork register, Split-site fork lines).

**Total: 102 sites in 68 functions; 67 of kind (i), 35 of kind (ii).**

| kind | sub-type (the gate or element) | sites | answer taken | other reading | Guide line relied on | fork lines |
| --- | --- | --- | --- | --- | --- | --- |
| (i) | DEFENCE | 4 | JUST FALSE | NOTHING | the delegated-definitions ruling of 2026-11-05, item (b): ""it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts"" | SS-008, SS-014, SS-049, SS-050 |
| (i) | IF | 12 | JUST FALSE | NOTHING | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on JUST FALSE: "a condition the text introduces with "if", "only if", "as long as" or "unless"" | SS-004, SS-006, SS-012, SS-020, SS-022, SS-027, SS-029, SS-031, SS-036, SS-041, SS-047, SS-057 |
| (i) | OWN | 37 | NOTHING | JUST FALSE | the "In short" sentence of section 5 (ruling of 2026-11-04), the line on NOTHING: "limits a grant or prohibition in its own wording and the case falls outside the limit" | SS-003, SS-005, SS-007, SS-009, SS-010, SS-011, SS-013, SS-015, SS-016, SS-017, SS-018, SS-019, SS-021, SS-023, SS-026, SS-028, SS-030, SS-032, SS-038, SS-040, SS-044, SS-046, SS-048, SS-056, SS-058, SS-059, SS-068, SS-072, SS-073, SS-074, SS-079, SS-083, SS-084, SS-085, SS-089, SS-090, SS-091 |
| (i) | SCOPE | 6 | NOTHING | JUST FALSE | the periods ruling of 2026-11-05, item (c): "a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`" | SS-001, SS-002, SS-024, SS-025, SS-033, SS-034 |
| (i) | WHERE | 8 | JUST FALSE | NOTHING | the periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`" | SS-035, SS-037, SS-039, SS-042, SS-043, SS-045, SS-064, SS-075 |
| (ii) | AFTER | 5 | NOTHING | JUST FALSE | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" | SS-061, SS-062, SS-093, SS-098, SS-099 |
| (ii) | APPLICATION | 1 | NOTHING | JUST FALSE | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" | SS-095 |
| (ii) | CONSENT | 6 | NOTHING | JUST FALSE | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" | SS-052, SS-066, SS-070, SS-077, SS-081, SS-087 |
| (ii) | IF | 10 | NOTHING | JUST FALSE | the grant ruling of 2026-11-12, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" | SS-053, SS-054, SS-055, SS-067, SS-071, SS-078, SS-082, SS-088, SS-101, SS-102 |
| (ii) | WHENEVER | 1 | JUST FALSE | NOTHING | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" | SS-051 |
| (ii) | WHERE | 8 | JUST FALSE | NOTHING | the periods ruling of 2026-11-05, item (b), and the delegated-definitions ruling of 2026-11-05, item (c); listed under the grant ruling of 2026-11-12, limit 3: "a "where ..." condition: when it fails the answer is `JUST FALSE`; and (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" | SS-060, SS-065, SS-069, SS-076, SS-080, SS-086, SS-092, SS-094 |
| (ii) | WHO | 4 | NOTHING | JUST FALSE | the "In short" sentence of section 5 (ruling of 2026-11-04): this site fits none of the dated rulings, so it is also listed under Marginal readings: "limits a grant or prohibition in its own wording and the case falls outside the limit" | SS-063, SS-096, SS-097, SS-100 |

Of the 67 sites of kind (i), 43 answer `NOTHING` and 24 answer `JUST FALSE`; of the 35 sites of kind (ii), 26 answer `NOTHING` and 9 answer `JUST FALSE`.

**Tests.** Each site has a test on the inputs that reach its branch (the case marked `-- S`) and a test on inputs that do not (the unmarked cases of the same function, where the two readings agree), asserted with the answer taken.
Checked by `work/audit/splitcov.py`: 68 functions carry sites; every one has at least as many `-- S` cases as it has sites and at least one unmarked case; short functions: 0.
A ruling that flips a site changes the branch and the expected value of its `-- S` cases, and leaves the unmarked cases alone.

Sites by provision (pointers to the fork lines):

| provision | fork lines |
| --- | --- |
| s 196(a) | SS-001 |
| s 196(b) | SS-002 |
| s 197(1) | SS-003, SS-004 |
| s 197(1A) | SS-005, SS-006 |
| s 197(2) | SS-007 |
| s 197(6) | SS-008 |
| s 198(1) | SS-009 |
| s 198(2) | SS-010 |
| s 199 | SS-011, SS-012 |
| s 200(1) | SS-013 |
| s 200(2) | SS-014 |
| s 201 | SS-015 |
| s 201A(1) | SS-016 |
| s 201A(2) | SS-017 |
| s 201B | SS-018 |
| s 202(1) | SS-019, SS-020 |
| s 203(1) | SS-021, SS-022 |
| s 204(1) | SS-023 |
| s 205(a) | SS-024 |
| s 205(b) | SS-025 |
| s 207(1) | SS-026, SS-027 |
| s 207(2) | SS-028, SS-029 |
| s 209 | SS-030, SS-031 |
| s 210(1) | SS-032 |
| s 213(a) | SS-033 |
| s 213(b) | SS-034 |
| s 218(1) | SS-035 |
| s 218(1A) | SS-036 |
| s 218(2) | SS-037, SS-038 |
| s 218(3) | SS-039, SS-040, SS-041 |
| s 219(1) | SS-042 |
| s 219(2) | SS-043, SS-044 |
| s 219(3) | SS-045, SS-046, SS-047 |
| s 221(1) | SS-048 |
| s 231(1) | SS-049 |
| s 231(2) | SS-050 |
| s 232(1) | SS-051, SS-052 |
| s 232(2) | SS-053 |
| s 232(4) | SS-054 |
| s 232(7) | SS-055 |
| s 234(1) | SS-056, SS-057, SS-058 |
| s 234(1A) | SS-059 |
| s 236(1) | SS-060, SS-061 |
| s 236(3) | SS-062, SS-063 |
| s 236B(1) | SS-064 |
| s 236B(3) | SS-065, SS-066 |
| s 236B(4) | SS-067 |
| s 236C(1) | SS-068 |
| s 236C(2) | SS-069, SS-070 |
| s 236C(3) | SS-071 |
| s 236D(1) | SS-072, SS-073, SS-074 |
| s 236E(1) | SS-075 |
| s 236E(3) | SS-076, SS-077 |
| s 236E(4) | SS-078 |
| s 236F(1) | SS-079 |
| s 236F(2) | SS-080, SS-081 |
| s 236F(3) | SS-082 |
| s 236G(1) | SS-083, SS-084, SS-085 |
| s 236H(1) | SS-086, SS-087 |
| s 236H(2) | SS-088 |
| s 236I(1) | SS-089, SS-090, SS-091 |
| s 236K(1) | SS-092, SS-093 |
| s 236L(1) | SS-094, SS-095, SS-096 |
| s 236L(5) | SS-097 |
| s 236L(6) | SS-098 |
| s 236L(7) | SS-099, SS-100 |
| s 236L(9) | SS-101, SS-102 |

## Rules with no breach path (sfab)

**None.** All 24 regulative rules of this part have a `#TRACE` that reaches `BREACH`, and each trace has a `-- EXPECT <word>` comment on the line above it, written by the test generator from the rule's form and the text, not copied from output (a prohibition: the forbidden act occurs, so `BREACH`, and nothing done by day 5 is `RESIDUAL`; a duty with a time: done on the last day is `FULFILLED`, the day after is `BREACH`, the day before is `RESIDUAL`).

The five duties (`MUST ... WITHIN`) take their time from outside the Act, so the breach path exists only once that number of days is given: s 203(1) (the approved exchange's requirement, F-203-days), s 232(6) (the time in the court order or agreement, per s 232(7)), s 235(3) and s 236J(4) (the court's directions on filing and proof of a claim) and s 236L(9) (the time specified in the order for disgorgement).
The number of days is an input, never a number from memory; a rule with no stated time and no stated consequence would have no breach path, and none was needed.

| rule | party and word | traces and their EXPECT |
| --- | --- | --- |
| `s 197(1) a person must not act for the purpose of creating a false or misleading appearance` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 197(1A) a person must not do a thing that creates a false or misleading appearance knowingly or recklessly` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 197(2) a person must not maintain, inflate or depress the market price by a sale with no change in beneficial ownership or a fictitious transaction` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 198(1) a person must not carry out 2 or more transactions in a corporation's securities with the intent to induce others to deal` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 198(2) a person must not carry out 2 or more transactions in a business trust's securities with the intent to induce others to deal` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 199 a person must not make a false or misleading statement likely to induce dealing or move the price` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 200(1) a person must not fraudulently induce another person to deal in capital markets products` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 201 a person must not employ a manipulative or deceptive device in connection with a subscription, purchase or sale` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 201A(1) a person must not knowingly execute an order for a derivatives contract without effecting it in good faith` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 201A(2) a person must not knowingly execute an order for a spot foreign exchange contract without effecting it in good faith` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 201B a person must not manipulate the price of a derivatives contract or its underlying thing, or corner an underlying thing` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 202(1) a person must not circulate a statement or information about the price effect of an illegal transaction` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 203(1) the person to whom subsection (1) applies must notify the approved exchange of the information it requires to be disclosed` | MUST (with a time) | BREACH x1, FULFILLED x1, RESIDUAL x1 |
| `s 207(1) a person must not act for the purpose of creating a false or misleading appearance as to a financial benchmark` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 207(2) a person must not do a thing that creates a false or misleading appearance as to a financial benchmark knowingly or recklessly` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 209 a person must not make a false or misleading statement to a person administering a financial benchmark` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 218(2) the connected person must not deal in, or procure dealing in, the securities while in possession of inside information` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 218(3) the connected person must not communicate the inside information to a person likely to deal` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 219(2) the insider must not deal in, or procure dealing in, the securities while in possession of inside information` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 219(3) the insider must not communicate the inside information to a person likely to deal` | SHANT | BREACH x1, RESIDUAL x1 |
| `s 232(6) the person on whom a civil penalty is imposed must pay it into the Consolidated Fund` | MUST (with a time) | BREACH x1, FULFILLED x1, RESIDUAL x1 |
| `s 235(3) the claimant must comply with the court's directions on the filing and proof of the claim` | MUST (with a time) | BREACH x1, FULFILLED x1, RESIDUAL x1 |
| `s 236J(4) the claimant must comply with the court's directions on the filing and proof of the claim` | MUST (with a time) | BREACH x1, FULFILLED x1, RESIDUAL x1 |
| `s 236L(9) the third party must pay the sums under the order for disgorgement within the time specified in the court order` | MUST (with a time) | BREACH x1, FULFILLED x1, RESIDUAL x1 |

Provisions that bar or stay an action (ss 233, 235(1) and (2), 236J(1) to (3), 236L(3) and (10)) or direct the court (s 236L(2)) address the Authority, the claimant or the court and name no act of the seat: they are decision functions and appear in no trace.

## Compared with the earlier pass

`inputs/NAIVE-EVIDENCE/` is absent in this sandbox (the brief names it; `ls inputs` shows `COMMONS-CLAUDE.md`, `ENCODING-GUIDE.md`, `EXAMPLE-sg-employment-act-seat`, `HEADINGS.md`, `KEEL-NOTES.md`, `PARTS.md`, `PLAN.md`, `SFA2001.meta.json`, `SFA2001.txt`, `SOURCES.md`, `STUB-SOURCE-LICENSE.md`, `XREFS.md`, `srcrefs.py`).
So no case was compared, no earlier answer was read, and no case differs: this section lists nothing.
I did not look for the earlier pass anywhere else.

## What the text turns out to say (numbered findings)

Each finding says how it was checked.

1. Sections 211 and 212 are shown only as "211. [Repealed by Act 4 of 2017]" and "212. [Repealed by Act 4 of 2017]", each on a line of its own (lines 34888 and 34890), with no marginal heading.
   `inputs/HEADINGS.md` therefore prints the heading of s 212 as "211. [Repealed by Act 4 of 2017]" and the heading of s 211 as empty. Both are rows `repealed or blank in this text`.
   (checked: `awk 'NR>=34886 && NR<=34892' inputs/SFA2001.txt` and `inputs/HEADINGS.md` lines 633 and 634.)
2. Six deletions inside sections are shown as "[Deleted by Act 4 of 2017]" with no text: s 214(1) "information" paragraph (c)(iii) (line 35014), s 236B(5) (36410), s 236C(4) (36515), s 236E(5) (36725), s 236F(4) (36842) and s 236H(3) (37028).
   Each is a row `repealed or blank in this text`; the numbering of the neighbouring subsections is unchanged, so a cross-reference to them would point at nothing; there is none (`grep -n "236B(5)\|236C(4)\|236E(5)\|236F(4)\|236H(3)\|214(1)(c)(iii)" inputs/SFA2001.txt` prints nothing).
   (checked: the coverage rows generated by `work/audit/rows.py`, and `grep -n "Deleted by Act" inputs/SFA2001.txt` over lines 34173 to 37498.)
3. The keel's `s 2(1) "securities-based derivatives contract" the contract is a securities-based derivatives contract` answers only `JUST TRUE` or `JUST FALSE` (a `BRANCH` with a `JUST FALSE` otherwise), never `NOTHING`.
   So the `NOTHING` branch in `s 196A(b)` and `s 196A(c)` ("the keel's s 2(1) answer is NOTHING") cannot be reached by calling that function; it is kept so that a keel function that one day answers `NOTHING` flows through unchanged, and no test reaches it (the tests of `s 196A(b)` and `(c)` assert only `JUST TRUE` and `JUST FALSE`).
   (checked: `sfa-definitions-products.l4` lines 91 to 103, and the comments at `sfab-division-1.l4:140` and `:160`.)
4. Section 218(5) defines "connected person" for Division 3 only, in different words from s 2(1).
   See F-218-def. A seat question "am I a connected person" (`Under section 218(5)(a)`) therefore asks the Division's own facts, not the keel's.
   (checked: lines 35382 to 35420 of the rendering and `sfab-insider-2.l4:10-12`.)
5. Section 218 has subsections (1), (1A), (2), (3), (4), (4A), (4B), (5) and (6): s 218(1) applies (2), (3), (4), (5) and (6), and s 218(1A) applies (2), (3), (4A), (5) and (6).
   So a person connected to a business trust or a scheme corporation (s 218(1A)) is under the presumption of (4A) and (4B) and not that of (4); the encoding follows the text and has a function for each of (4), (4A) and (4B).
   (checked: lines 35172 to 35200 and 35319 to 35380 of the rendering.)
6. Sections 226(1)(b) and 227(1)(b) both say "it is to be presumed", but only s 226(1)(b) adds "until the contrary is proved".
   See F-227: I did not give s 227(1)(b) a rebuttal path the text does not state.
   (checked: lines 35635 to 35639 and 35683 to 35690 of the rendering.)
7. Section 203(1) sets no time of its own for the duty to notify: it is "as they occur or arise", measured by the approved exchange's listing rules or other requirement; section 203(3) then says "Despite section 204 or 335" a failure is not an offence "unless the failure to notify is intentional or reckless".
   The days are an input (F-203-days); s 335 (the general penalty) is named only to be displaced, so it is not a seam; the offence is a decision function (`s 203(3)`) and the duty is a rule with a trace that reaches `BREACH` when the days are missed.
   (checked: lines 34682 to 34717 of the rendering.)
8. The penalty provisions of Part 12 are identical in amount: ss 204(1), 210(1) and 221(1) each say "a fine not exceeding $250,000 or to imprisonment for a term not exceeding 7 years or to both".
   None states a daily fine, and the three functions return `Penalty OF 250000, 84, TRUE, 0` (84 months, "both" allowed, no daily fine). The amounts are copied from the text and are not inputs.
   (checked: lines 34721 to 34724, 34866 to 34869 and 35518 to 35521; `grep -n "Penalty OF" sfab-*.l4`.)
9. The civil-penalty cap of s 232(2) has two "or" limbs that do not say which applies when both a profit and an avoided loss exist, and s 232(3) sets a floor ($100,000 for a corporation, $50,000 in any other case) that applies to an order under (2) but not to an agreed order under (4).
   See F-232-2a. The floor function is tested on both sides of each amount.
   (checked: lines 35866 to 35908 of the rendering.)
10. Section 235(1)'s "after the commencement of" can be read as qualifying the profit or loss rather than the bringing of the action.
   See F-235-1.
   (checked: lines 36167 to 36180 of the rendering.)
11. Section 236(3A)'s pro-rating clause divides by "the total amount of all other claims", which is undefined when there is no other claim.
   See F-236-3A; the function also guards the case where nothing is proven, which would otherwise divide by zero.
   (checked: lines 36246 to 36264 of the rendering and `sfab-civil.l4` (the `s 236(3A) the compensation amount ordered for the claimant` function).)
12. Several definitions of Division 5 are repeated in parallel wording in the sections of each family: "corporate culture" and "high managerial agent" in s 236B(9) and s 236E(9) (the words differ where the entity differs: "employee, agent or officer of the corporation" against "partner, manager or employee of the partnership"), and "maximum recoverable amount" in ss 234(6), 236D(6), 236G(6) and 236I(6); s 236K(3) and s 236L(12) both define "claimant" by pointing at s 234.
   They are separate rows and separate functions (the text states each in its own section), generated from one pattern so that they cannot drift apart.
   (checked: the coverage rows with a defined term (31 rows).)
13. A page break falls inside a sentence in many places (for example s 200(1) between paragraphs (c) and (d), and s 236C(1) between "committed by an" and "employee or officer"); the page furniture lines sit between the halves.
   Quotations are made as separate runs on either side of the furniture; a quoted fragment that spans a break (in a `-- FALSE-kind` comment) is checked with the furniture removed.
   (checked: `work/audit/quotes.py`; its first run flagged six fragments: four spanned a page break (verbatim once the furniture is removed, so the script now removes it), one was my own header comment, and one was not verbatim (the words "a partnership or a limited liability partnership" in s 236F(2), where the text says "a partnership or limited liability partnership"); that one is fixed.)
14. The line-by-line audit that every non-blank text line of the range lies inside a quoted run (`work/audit/quoted.py`) found eight real gaps (ten lines) that `srcrefs.py` does not see, because it checks that the quotations are accurate and not that every line is quoted: the closing word "products." of s 200(1) (line 34521), the closing words of s 210(2) (line 34884), paragraphs (d) and (e) of s 236J(1) (lines 37167 to 37171), and the lead-ins "In this Division --" of s 206 and s 214(1) and "In this section --" of s 236B(9) and s 236E(9).
   All are now quoted and inside the `@ref` range of the function that encodes them; what remains unquoted is 110 lines, every one inside an inert row (headings, Division and Subdivision titles, s 238) or a repealed row.
   (checked: the script's own output (0 unquoted lines inside an encoded or fork row).)
15. The seat audit (every question's name against the direction and subject of the layer-1 function it calls) found two differences, both fixed: `Under section 218(1)` named the bars "in section 218(2) and (3)" but calls the function that applies subsections (2) to (6), and `Under section 234(2)` asked "how much compensation must I pay" but calls the amount of compensation the person is liable to pay under (1).
   The other 48 names match their bodies in direction (bars as bars, permissions as permissions, defences as defences, exceptions as exceptions).
   (checked: the 50 question names printed beside the first line of their bodies (see the final report).)

## Seat layer (sfab)

Fifty questions in `sfab-seat.l4`, grouped under `§` headings in the text's order, each with `@export` and `@desc`, each named `Under section N, ...`, each calling a layer-1 function and restating no rule.
`sfab-cases-seat.l4` has 120 assertions on facts a person in the seat would state.
Every question is listed below with the layer-1 function it calls: the direction audit compared the two (a bar is titled as a bar, a permission as a permission, a defence as a defence).

| # | question | calls |
| --- | --- | --- |
| 1 | Under section 197(1), does my conduct contravene the bar on acts done to create a false or misleading appearance of active trading | `s 197(1) the person's conduct contravenes the bar on conduct done to create a false or misleading appearance` |
| 2 | Under section 197(1A), does my conduct contravene the bar on acts that create a false or misleading appearance, done knowingly or recklessly | `s 197(1A) the person's conduct contravenes the bar on conduct that creates a false or misleading appearance knowingly or recklessly` |
| 3 | Under section 197(2), does my conduct contravene the bar on maintaining, inflating or depressing the market price | `s 197(2) the person's conduct contravenes the bar on maintaining, inflating or depressing the market price` |
| 4 | Under section 197(3)(b), is my purpose presumed to be to create a false or misleading appearance because I offered to sell and a matching offer to purchase was made | `s 197(3)(b) the person's purpose is presumed by reason of an offer to sell matched by an offer to purchase` |
| 5 | Under section 197(4), is the presumption of my purpose rebutted | `s 197(4) the presumption under subsection (3) is rebutted` |
| 6 | Under section 198(1), do my transactions contravene the bar on market manipulation in a corporation's securities | `s 198(1) the person's transactions contravene the bar on market manipulation in securities of a corporation` |
| 7 | Under section 199, does my statement contravene the bar on false or misleading statements | `s 199 the person's statement or information contravenes the bar on false or misleading statements` |
| 8 | Under section 200(1), does my conduct contravene the bar on fraudulently inducing a person to deal | `s 200(1) the person's conduct contravenes the bar on fraudulently inducing a person to deal` |
| 9 | Under section 200(2), do I have the defence to a contravention constituted by recording or storing information | `s 200(2) the defendant has the defence to a contravention constituted by recording or storing information` |
| 10 | Under section 201, does my conduct contravene the bar on manipulative and deceptive devices | `s 201 the person's conduct contravenes the bar on manipulative and deceptive devices` |
| 11 | Under section 201A(1), does my execution of an order contravene the bar on bucketing a derivatives contract | `s 201A(1) the person's execution of an order contravenes the bar on bucketing a derivatives contract` |
| 12 | Under section 201B, does my conduct contravene the bar on manipulating derivatives prices and cornering | `s 201B the person's conduct contravenes the bar on manipulating the price of derivatives contracts and cornering` |
| 13 | Under section 202(1), does my circulation of a statement contravene the bar on disseminating information about illegal transactions | `s 202(1) the person's circulation of a statement or information contravenes the bar on disseminating information about illegal transactions` |
| 14 | Under section 203(1), does my failure to notify the approved exchange contravene the continuous disclosure bar | `s 203(1) the person's failure to notify the approved exchange contravenes the bar on failing to disclose` |
| 15 | Under section 203(3), is my failure to notify the approved exchange an offence | `s 203(3) the contravention of subsection (1) is an offence` |
| 16 | Under section 204(1), what is the most I can be fined on conviction for contravening a provision of Division 1, in dollars | `s 204(1) the penalty on conviction for contravening a provision of Division 1` |
| 17 | Under section 204(1), what is the longest imprisonment I can be given on conviction for contravening a provision of Division 1, in months | `s 204(1) the penalty on conviction for contravening a provision of Division 1` |
| 18 | Under section 204(2), are criminal proceedings against me barred because a civil penalty has been ordered or agreed | `s 204(2) proceedings for an offence in respect of the contravention are barred` |
| 19 | Under section 207(1), does my conduct contravene the bar on acts done to create a false or misleading appearance as to a financial benchmark | `s 207(1) the person's conduct contravenes the bar on conduct done to create a false appearance as to a financial benchmark` |
| 20 | Under section 208, does section 207 not apply to what I did | `s 208 section 207 does not apply to the thing done` |
| 21 | Under section 209, does my statement contravene the bar on false or misleading statements to a person administering a financial benchmark | `s 209 the person's statement contravenes the bar on false or misleading statements to a benchmark administrator` |
| 22 | Under section 210(1), what is the most I can be fined on conviction for contravening a provision of Division 2, in dollars | `s 210(1) the penalty on conviction for contravening a provision of Division 2` |
| 23 | Under section 215, is the information generally available | `s 215 the information is generally available` |
| 24 | Under section 216, would a reasonable person be taken to expect the information to have a material effect on the price or value | `s 216 a reasonable person would be taken to expect the information to have a material effect on the price or value` |
| 25 | Under section 218(5)(a), am I a connected person | `s 218(5)(a) the person is a connected person` |
| 26 | Under section 218(1), do subsections (2), (3), (4), (5) and (6) of section 218 apply to me as a connected person | `s 218(1) subsections (2), (3), (4), (5) and (6) apply to the connected person` |
| 27 | Under section 218(2), does my dealing or procuring contravene the bar on a connected person dealing while in possession of inside information | `s 218(2) the connected person's dealing or procuring contravenes the bar` |
| 28 | Under section 218(3), does my communication of the information contravene the bar on a connected person communicating inside information | `s 218(3) the connected person's communication of the information contravenes the bar` |
| 29 | Under section 218(4), am I presumed to have known that the information was not generally available and material | `s 218(4) the connected person is presumed to have known that the information was not generally available and might have a material effect` |
| 30 | Under section 219(1), do the bars in section 219(2) and (3) apply to me as an insider | `s 219(1) subsections (2) and (3) apply to the insider` |
| 31 | Under section 219(2), does my dealing or procuring contravene the bar on an insider dealing while in possession of inside information | `s 219(2) the insider's dealing or procuring contravenes the bar` |
| 32 | Under section 219(3), does my communication of the information contravene the bar on an insider communicating inside information | `s 219(3) the insider's communication of the information contravenes the bar` |
| 33 | Under section 222, do sections 218(2) and 219(2) not apply to my redemption of units in a collective investment scheme | `s 222 sections 218(2) and 219(2) do not apply to the redemption of units` |
| 34 | Under section 228, do I not contravene section 218(2) or 219(2) merely because I am aware of my own intentions or activities | `s 228 the individual does not contravene section 218(2) or 219(2) merely because the individual is aware of the individual's own intentions or activities` |
| 35 | Under section 230(1), do I as a licence holder or representative not contravene section 218(2) or 219(2) by an unsolicited transaction for a principal | `s 230(1) the holder or representative does not contravene section 218(2) or 219(2) by an unsolicited transaction for a principal` |
| 36 | Under section 231(1), do I have the parity of information defence to a contravention by dealing or procuring | `s 231(1) the person has the parity of information defence to the contravention by dealing or procuring` |
| 37 | Under section 231(2), do I have the parity of information defence to a contravention by communicating | `s 231(2) the person has the parity of information defence to the contravention by communicating` |
| 38 | Under section 221(1), what is the most I can be fined on conviction for contravening section 218 or 219, in dollars | `s 221(1) the penalty on conviction for contravening section 218 or 219` |
| 39 | Under section 221(1), what is the longest imprisonment I can be given on conviction for contravening section 218 or 219, in months | `s 221(1) the penalty on conviction for contravening section 218 or 219` |
| 40 | Under section 232(2), what is the most I can be ordered to pay as a civil penalty, in dollars | `s 232(2) the highest civil penalty the court may order` |
| 41 | Under section 232(3), what is the least civil penalty a court can order me to pay, in dollars | `s 232(3) the lowest civil penalty the court may order` |
| 42 | Under section 233(1), is a civil penalty action against me barred because 6 years have passed since the contravention | `s 233(1) the action under section 232 is barred because 6 years have expired from the date of the contravention` |
| 43 | Under section 234(1), am I liable to pay compensation to the claimant | `s 234(1) the contravening person is liable to pay compensation to the claimant` |
| 44 | Under section 234(2), what is the amount of compensation I am liable to pay the claimant under section 234(1), in dollars | `s 234(2) the amount of compensation under subsection (1)` |
| 45 | Under section 235(1), is an action for compensation under section 234 barred against me unless the court gives permission | `s 235(1) no action under section 234 may be brought without the permission of court` |
| 46 | Under section 236H(1), may the Authority bring an action against me for a civil penalty as an officer, partner or manager of an entity that contravened Part 12 | `s 236H(1) the Authority may bring an action in a court against the defendant to seek an order for a civil penalty` |
| 47 | Under section 236H(2), what is the most I can be ordered to pay as a civil penalty as an officer, partner or manager, in dollars | `s 236H(2) the highest civil penalty the court may order` |
| 48 | Under section 236I(1), am I liable to pay compensation to the claimant as an officer, partner or manager | `s 236I(1) the defendant is liable to pay compensation to the claimant` |
| 49 | Under section 236L(1), may a court order me to disgorge a benefit as a third party | `s 236L(1) the court may make an order against the third party for disgorgement of the benefit` |
| 50 | Under section 236L(4), am I protected against an order for disgorgement, or against disgorgement of the entire benefit | `s 236L(4) the court is not to make an order for disgorgement, or not of the entire benefit, against the third party` |

## What the stable binary does not accept

I used `l4 1.6.110 (main, e51181d, 2026-11-11)` and, for the second reading of every module, `1.6.109 (main, 4c887e0, 2026-11-04)`.
Every file in this folder checks and runs clean on both builds, and no module reads differently on the two builds (`check.sh` prints `same` on every line, below).
I did not keep a log of every error met while writing, so I claim no list of rejected constructs beyond the following limits, which shaped the encoding (each says whether it is the brief's own list or something I checked):

- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` (other than `LEST BREACH BECAUSE`) are not available (the brief's list): not used.
  A script over every `sfab-*.l4` file found none outside a `LEST BREACH BECAUSE`.
- `YMD`, `WAIT UNTIL`, `TYPICALLY`, sets, the ledger and `EVERY` are not used (the same script found none); dates are `Date day month year`, waits are `WAITUNTIL`.
- A regulative rule's outcome cannot be asserted: a `#TRACE` prints `FULFILLED`, `BREACH` or a residual obligation and produces no assertion line, so `check.sh` counts nothing for it (its own header says so).
  I compared every trace by hand, on both builds, with `work/tests/runcheck.py`, which reads each `-- EXPECT <word>` comment above a trace and the printed outcome, on 110 and on 109.
  The 53 traces all match their `EXPECT` comment and are the same on both builds.
  Because a trace is not an assertion, each prohibition and duty is also encoded as a decision function over the facts (`s 197(1) the person's conduct contravenes the bar ...`), and those are asserted.
- An unparenthesised `NOT` swallows what follows it, so every `NOT` is parenthesised or stands alone before a closing parenthesis, a `THEN` or the end of a line (the audit found 55 uses that stand alone, and none that binds more than intended).
- A name defined in two imported modules cannot be used at all, so every top-level name of this part begins with its provision label (`s 197(1) ...`) and every seat question with `Under section N,`; the audit found 370 top-level names and 0 that do not.
- `IMPORT` finds only modules in the importing file's folder, so the seat layer and all test files sit beside the modules, and the answers of one module that another needs (for example the answer under s 218 that s 221 asks) are INPUTS of the second, not calls (see Seams (sfab)).

## Checks run by script

All of these are in `work/audit/` (not shipped) and were run on the files in this folder when this file was generated; the raw last lines are printed below the list.

- `srcrefs.py check --refs inputs/SFA2001.txt sfab-*.l4`, with and without `--strict`: the last lines are `srcrefs check: 1977 src: lines, 236 runs, 290 locators, 0 problems` and `srcrefs check: 1977 src: lines, 236 runs, 290 locators, 0 problems`.
- `quotes.py`: every quoted fragment of a `-- FALSE-kind` or `-- NOTHING-kind` comment is a verbatim substring of lines 34173-37498 after normalising the non-breaking hyphen, curly quotes and white space, and removing page furniture: `fragments checked 318 problems 0`.
- `quoted.py`: every text line outside an inert or repealed row is inside a `-- src:` line: `unquoted lines inside an encoded or fork row: 0 []`; `quoted lines inside an inert or repealed row: 1 [35014]`.
- `lint.py` over all `sfab-*.l4` files: every `NOT` is parenthesised or stands alone before a `THEN`, a closing parenthesis or the end of a line; no `REFUSE`, no `BECAUSE` outside `LEST BREACH BECAUSE`, no `YMD`, `TYPICALLY`, `EVERY`, set operation or `WAIT UNTIL`; every `#ASSERT` is on one line; every input line has an `@desc`; every top-level name (functions, `DECLARE` types and constructors) begins with its provision label and every seat question with `Under section`; every regulative rule has a `#TRACE` that reaches `BREACH` with a `-- EXPECT` comment on the line above: `files 17, input lines 798, top-level names 370, NOT standing alone 55, regulative rules 24, traces 53, problems 0`.
- `splitcov.py`: `functions with sites 68 sites 102 short 0`.
- `runcheck.py`: all test files run with 0 errors, 0 failed and 0 refused on both builds, and every trace matches its `-- EXPECT` and is the same on both builds (its output is in `work/logs/`; the gate below repeats the counts).
- a deliberate wrong expectation, put in a scratch copy of `sfab-tests-division-2.l4` (one `EQUALS JUST TRUE` flipped to `EQUALS JUST FALSE`), was reported as a failed assertion by `l4 run`, so the instrument can fail; the scratch copy was deleted in the same command.

```
srcrefs check: 1977 src: lines, 236 runs, 290 locators, 0 problems
srcrefs check: 1977 src: lines, 236 runs, 290 locators, 0 problems
fragments checked 318 problems 0
unquoted lines inside an encoded or fork row: 0 []
quoted lines inside an inert or repealed row: 1 [35014]
functions with sites 68 sites 102 short 0
files 17, input lines 798, top-level names 370, NOT standing alone 55, regulative rules 24, traces 53, problems 0
```

## What `check.sh` prints

Run as `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` in this folder, target `main`, `JL4_LIBRARY_PATH` unset:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sfa-application.l4                             0         0       0        0         0 |      0         0       0        0  same
sfa-associates.l4                              0         0       0        0         0 |      0         0       0        0  same
sfa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-benchmarks.l4                  0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-markets.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-persons.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-products.l4                    0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-rest.l4                        0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-schemes.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-interests.l4                               0         0       0        0         0 |      0         0       0        0  same
sfa-investors.l4                               0         0       0        0         0 |      0         0       0        0  same
sfa-periods.l4                                 0         0       0        0         0 |      0         0       0        0  same
sfab-attributed.l4                             0         0       0        0         0 |      0         0       0        0  same
sfab-cases-seat.l4                             0       120       0        0         0 |      0       120       0        0  same
sfab-civil.l4                                  0         0       0        0         0 |      0         0       0        0  same
sfab-division-1.l4                             0         0       0        0         0 |      0         0       0        0  same
sfab-division-2.l4                             0         0       0        0         0 |      0         0       0        0  same
sfab-insider-1.l4                              0         0       0        0         0 |      0         0       0        0  same
sfab-insider-2.l4                              0         0       0        0         0 |      0         0       0        0  same
sfab-insider-3.l4                              0         0       0        0         0 |      0         0       0        0  same
sfab-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sfab-tests-attributed.l4                       0       352       0        0         0 |      0       352       0        0  same
sfab-tests-civil.l4                            0       189       0        0         0 |      0       189       0        0  same
sfab-tests-division-1.l4                       0       176       0        0         0 |      0       176       0        0  same
sfab-tests-division-2.l4                       0        47       0        0         0 |      0        47       0        0  same
sfab-tests-insider-1.l4                        0        78       0        0         0 |      0        78       0        0  same
sfab-tests-insider-2.l4                        0       105       0        0         0 |      0       105       0        0  same
sfab-tests-insider-3.l4                        0        77       0        0         0 |      0        77       0        0  same
sfab-tests-integration.l4                      0        31       0        0         0 |      0        31       0        0  same
TOTAL (29 modules)                             0      1175       0        0           |      0      1175       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

The baseline it replaced: the folder as supplied held the 12 keel modules only, which print 0 assertions (the keel's own test files are not in the sandbox); the keel's full folder printed `TOTAL (26 modules) ... 1069` satisfied (`inputs/KEEL-NOTES.md`, "What `check.sh` prints").
This part adds 17 modules and 1175 satisfied assertions in all (1175 is the total on the line above; every one of them is in an `sfab-` file), 0 errors, 0 failed, 0 refused, and `same` on every module for the second stable build.
`check.sh` does not see a different `#TRACE` outcome: I compared the traces on the two builds by hand (`runcheck.py`, 53 traces, 0 differences).


## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

No site of this part changed under it (2026S1bC): the functions of this part that stay Boolean after the protocol split already answered as the ruling reads, and its protocol-shaped functions keep limit 3 of the grant ruling until they are re-encoded.
