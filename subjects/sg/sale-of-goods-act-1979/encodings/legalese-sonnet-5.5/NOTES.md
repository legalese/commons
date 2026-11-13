# NOTES: Sale of Goods Act 1979 (Singapore; the Act applied from England), 2020 Revised Edition, informal consolidation in force from 1/4/2022

**Status: draft, target main.**
Checked: `check.sh` on the main build (numbers in "What `check.sh` prints"); `srcrefs.py check --strict` on every layer-1 module (0 problems); `l4 run` on every file with no `DiagnosticSeverity_Error` or `_Warning`.
Not checked: no domain expert has read it against the text, and the text itself is a converter's rendering, not the official text.
Method: a single Sonnet 5.5 agent working alone from the brief (`BRIEF.md`), with no subagents.
Revised 2026-11-05: Meng's rulings of that date on periods, "where" conditions and scope limits (typed 04:30) and on "when", "upon" and "whenever" and the "until" bars (typed 06:04) are applied across the Act (see "Fork register" and "Changes of 2026-11-05"); the counts in this file are those of the revised files.
Edition encoded: the 2020 Revised Edition, informal consolidation, version in force from 1/4/2022, as deposited in `inputs/SGA1979.txt` (sha256 `7bf1c02abaa9483745010dfe1f283e763091f967768b95df351ebf39bdad0923`, 2115 lines).
Source terms: `SOURCE-LICENSE.md` points at the subject-level note `inputs/STUB-SOURCE-LICENSE.md` and does not repeat it.
The lines quoted in comments are copied mechanically from that file, and `srcrefs.py` checks every quoted line against it.

## Layers and files

Layer 1 is the Act, by its own structure, one module per Part or natural group, each with a case file written beside it.
Layer 2 is the seat.

| module | covers | rules (DECIDE) | case file (assertions) |
| --- | --- | --- | --- |
| `soga-nouns.l4` | shared enumerations | 0 | none |
| `soga-part1-application.l4` | s 1 (which contracts the Act applies to; the Schedule pointers) | 4 | `soga-cases-part1.l4` (61) |
| `soga-part2-formation.l4` | ss 2 to 15A | 70 | `soga-cases-part2.l4` (233) |
| `soga-part3-effects.l4` | ss 16 to 26 | 41 | `soga-cases-part3.l4` (169) |
| `soga-part4-performance.l4` | ss 27 to 37 | 51 | `soga-cases-part4.l4` (152) |
| `soga-part5-unpaid-seller.l4` | ss 38 to 48 | 35 | `soga-cases-part5.l4` (120) |
| `soga-part6-actions.l4` | ss 49 to 54 | 22 | `soga-cases-part6.l4` (70) |
| `soga-part7-supplementary.l4` | ss 55 to 62 (s 58 omitted; s 63 is machinery) | 19 | `soga-cases-part7.l4` (56) |
| `soga-interpretation.l4` | s 61 (definitions and rules of reading) | 25 | `soga-cases-interpretation.l4` (83) |
| `soga-schedule.l4` | the Schedule and the gates in ss 11(5), 12(6), 13(4), 14(6), 15(3) and 35(8), and two date-aware wrappers (s 14(2) and s 61(1) "business" by the contract date) | 56 | `soga-cases-schedule.l4` (238) |
| `soga-routes.l4` | two effects gathered by hand (E1 option B) | 2 | `soga-cases-routes.l4` (19) |
| `soga-duties.l4` | the duties as regulative rules (ss 19(3), 27, 28, 29(3), 32(2), 32(3), 34, 46(4), 57(4)); `#TRACE` illustrations, twin decision functions are asserted in the Part files | 0 | none |
| `soga-seat.l4` | layer 2: the seat's 88 questions | 88 | `soga-cases-seat.l4` (275) |
| `soga-cases-findings.l4` | findings that cross Parts, and the main binary's behaviour (findings 1 to 4) | - | `soga-cases-findings.l4` (16) |

Total assertions: 1492, in 12 case files (1324 before the revision of 2026-11-05; 1445 before the "until" bars of the same day).

Also in this folder: `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md` (a copy of the brief).

## Seat

The seat is **a buyer of goods under a contract of sale in Singapore, asking on facts they can state what terms are implied, when the property and the risk pass, what they may do if the goods are late, defective or not as described, and what they owe the seller**.
It is the brief's seat, taken as given; this encoding did not choose it.
The Act is written about two parties (the seller and the buyer) and about a court; the buyer is the one who needs to ask the Act questions about implied terms, ownership, risk, delivery, rejection and remedies, so a buyer's question form covers the sections that matter in daily dealings.
The seat layer is two files.
`soga-seat.l4` has 88 questions in 12 groups, in the Act's order; every question has `@export` and `@desc`, takes plain inputs worded as the buyer would be asked, and calls a layer-1 rule.
It restates no rule, and no layer-1 module changes to suit it.
`soga-cases-seat.l4` has 275 assertions, at least one per question, 61 of them asserting `NOTHING` (the Act does not answer on those facts).
There is no seat for an official: where the Act speaks of the court (ss 52, 53 and others) or of the seller, the carrier and the auctioneer, the rule is in layer 1 and the buyer meets it only through the questions.
Only three questions ask "Yes / No / I am not sure": the two that take other provisions' answers (the gathered routes in `soga-routes.l4`) and the s 10(2) question about the terms of the contract; there "I am not sure" becomes `NOTHING`, never `FALSE`.
Every other question takes plain yes/no, number, date or list-choice inputs, one per fact.
The header of `soga-seat.l4` says that `NOTHING` means the Act does not answer on these facts and must never be read as no.

Where the seat layer maps the buyer's answer to a layer-1 input, a comment `-- input mapping` says so, and the mapping is in `soga-seat.l4`: `My answer`, `what I say, as a fact`, `what I say, as the Act's no, if yes`, `the Act's answer to the opposite question` (for a question worded the other way round from its rule: s 30(2A) and s 35A(1)) and `my date if it has happened`.
A question that asks for an amount, a party or a stage cannot answer "no", so ten of the 88 are yes/no companions that call the yes/no twin of the value function (for example "Must I pay a reasonable price for necessaries" beside "What must I pay for necessaries"); the value question says `NOTHING` where the companion says `JUST FALSE`.
Four questions were added for provisions the seat had skipped: s 8(1), s 10(2), s 14(1) and s 30(3).
Four questions ask an "until" bar (fork F12): "Is the property in unascertained goods still barred from passing to me (s 16)?", the same for s 18 Rule 2 and Rule 3, and "Is delivery to me still not possible because a third person holds the goods (s 29(4))?"; each says Yes (`JUST TRUE`) while the bar is in force and No (`JUST FALSE`) from the event on or where the rule does not apply, and sits beside the question "Has the property passed ...", which is unchanged.
The s 19(1) question "Does the seller keep the property because he reserved the right of disposal" now answers through the bar too: before this revision it called the function that says the property passes, so it answered No while the seller did keep the property (the question was worded the wrong way round, and the case beside it asserted the wrong-way answer).

## What is encoded and what is not

Everything in the deposited text has a row in the coverage table below.
**Encoded** (a tested rule or definition with a citation): every operative section and subsection of ss 1 to 62 except the three omitted or not-applicable sections; the 17 defined terms of s 61(1) and the rules of reading in s 61(2) to (5); paragraphs 1 to 6 and 9 to 13 of the Schedule, including the text of the sections they substitute.
**Repealed or blank in this text:** ss 22, 40 and 58, one deleted definition in s 61(1), and paragraphs 7 and 8 of the Schedule.
**Inert:** the title, long title, Part headings and arrangement of sections (reason 1); the Schedule's title (reason 1); the Legislative History, key to abbreviations and comparative table, which the text says are "not part of the Act" (reasons 1 and 2); s 63, the short title (reason 2). The rows are listed with their reasons below.
**Not encoded because the Act does not give the answer:** the borrowed terms (inputs), the judgments handed to the court (inputs), and the questions in "What the text does not answer" below.
**Rules in the style of a duty** (the seller must deliver, the buyer must accept and pay, the carrier must re-deliver, the seller must not bid at an auction) are written twice: as a regulative rule in `soga-duties.l4` and as a decision-function twin in the Part that holds the section. Only the twin is asserted.

### Reading a result: FALSE and NOTHING

Every decision function answers `JUST TRUE`, `JUST FALSE` or `NOTHING`, or a `MAYBE` number, date or enum.
**`JUST FALSE` is the Act saying no in its own words.**
In this row that means one of these.
A definition that says "means" and the thing is outside the words.
A condition the Act introduces with "if", "unless", "except" or "provided" and the condition fails.
A "where" condition that is not met (ruled 2026-11-05, (b)); "when", "upon" and "whenever" count as "where" (ruled 2026-11-05T06:04, fork F10).
"while", "in the case of", "in any other case" and "on the claimant's application" are read the same way when they introduce one condition on which a right, duty or deeming depends (assumed, not ruled: fork F10).
A period the Act fixes in its own words ("within", "not later than", "from ... until", "at any time before", "on or after ... and before") when the date falls outside it (ruled 2026-11-05, (a)).
A list the Act closes with "only" or "namely".
A flat negative ("is not", "does not", "no person", "it is not lawful").
**`NOTHING` is the Act not answering on these facts.**
That covers silence, a list the Act does not close, "includes", an undefined term, a rule that points to a power, an Act or a contract outside the sources, and a scope limit with no "only" where the case falls outside the scope (ruled 2026-11-05, (c)).
It also covers a function that returns a number, a party, a date or a stage: it cannot say no, so where the "where" condition fails it says `NOTHING` and its yes/no twin (`... applies`) says `JUST FALSE`.
A caller must never turn `NOTHING` into `FALSE`.
**An "until" bar** ("the property does not pass until X", "there is no delivery unless and until X") is encoded as its own yes/no function and never claims that the thing has happened (ruled 2026-11-05T06:04, fork F12).
The bar answers `JUST TRUE` while it is in force, `JUST FALSE` once X has happened, and `JUST FALSE` where the rule does not apply (the "where" is unmet, or "unless a different intention appears" and one does).
The function that says the thing has happened (the property has passed, there is delivery) is left as it was: `JUST FALSE` before X and `NOTHING` from X.
So ask the bar when you want to know whether the property is held back: after X the Act has not said that the property has passed, and no function here says so.
Every `JUST FALSE` branch in layer 1 carries `-- FALSE-kind (the text says no in its own words): "<quoted words>"`; every `NOTHING` branch carries `-- NOTHING-kind (<why>)`, with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
`work/lint.py` (not shipped) checked that no branch lacks its tag: 0 untagged on the final run.
In the seat layer `NOTHING` is shown to the buyer as "the Act does not say on these facts".
A "no" in this row is never a finding that the buyer has no remedy: for example `NOTHING` from `route (E1 B) the buyer may maintain an action against the seller for damages` means the Act's listed routes do not apply, not that no other action exists.

## Jural relations

One row per provision (or group of provisions with the same relation); `none` where the provision is a definition, a counting rule, a gate or a saving.
The kinds are Hohfeld's: a claim (the other party's duty), a privilege (the other's no-right), a power (the other's liability), an immunity (the other's disability).
They are my reading and have not been confirmed by a lawyer.
Under ruling N2 they are recorded here and are **not** typed into any answer a rule gives.
The "L4 rule" column is the first layer-1 function whose citation covers the first provision of the row.

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 1(1) s 1(2) s 1(3) s 1(4) | - | application and gate provisions: they decide which text governs and create no relation between two persons | none | `s 1(1) this Act applies to the contract of sale of goods` |
| s 2(1) s 2(3) s 2(4) s 2(5) s 2(6) | - | definition or classification of the contract | none | `s 2(1) the contract is a contract of sale of goods` |
| s 2(2) | a part owner of goods | the other part owner | privilege/no-right | `s 2(2) there may be a contract of sale between one part owner and ano...` |
| s 3(1) | - | points to the general law of capacity (outside the sources) | none | `s 3(1) the party has capacity to buy and sell` |
| s 3(2) | the seller of necessaries sold and delivered | the buyer who is a minor or lacks capacity (must pay a reasonable price) | claim/duty | `s 3(2) the amount the buyer must pay for necessaries sold and deliver...` |
| s 3(3) | - | definition of "necessaries" | none | `s 3(3) the goods are necessaries` |
| s 4(1) | the parties to a contract of sale | anyone who would insist on a form (no formal requirement) | privilege/no-right | `s 4(1) a contract of sale may be made in this form` |
| s 4(2) | - | savings for the law relating to corporations | none | `s 4(2) section 4 affects the law relating to corporations` |
| s 5(1) s 5(2) | the parties to a contract of sale | anyone who would deny that existing, future or contingent goods can be sold | privilege/no-right | `s 5(1) the goods may be the subject of a contract of sale` |
| s 5(3) | - | characterisation of a purported present sale of future goods | none | `s 5(3) a purported present sale of future goods operates as an agreem...` |
| s 6 s 7 | seller and buyer (each) | the other party (neither can enforce the void or avoided contract) | immunity/disability | `s 6 the contract is void` |
| s 8(1) | the parties | each other (they may fix the price by contract, by a third party or by course of dealing) | privilege/no-right | `s 8(1) the price is determined as the subsection mentions` |
| s 8(2) | the seller | the buyer (must pay a reasonable price) | claim/duty | `s 8(2) the amount the buyer must pay where the price is not determined` |
| s 8(3) | - | reasonable price is a question of fact | none | `s 8(3) the Act's own figure for a reasonable price` |
| s 9(1) | seller and buyer (each) | the other party (the agreement to sell is avoided when the valuation is not made) | immunity/disability | `s 9(1) the agreement to sell is avoided` |
| s 9(2) | the party not at fault | the party at fault (damages) | claim/duty | `s 9(2) the party who may maintain an action for damages against the p...` |
| s 10(1) s 10(2) | - | rules of construction about time stipulations (no relation until the contract says what the time term is) | none | `s 10(1) a stipulation as to time of payment is of the essence of the ...` |
| s 10(3) | - | counting rule (meaning of "month") | none | `s 10(3) a month in a contract of sale means a calendar month` |
| s 11(1) | the buyer | the seller (the buyer may waive a condition or treat its breach as a breach of warranty) | power/liability | `s 11(1) the buyer may waive the condition` |
| s 11(2) | - | question of construction | none | `s 11(2) the stipulation is a condition or a warranty` |
| s 11(3) | the seller | the buyer (who has accepted the goods or part of them cannot reject for breach of condition) | immunity/disability | `s 11(3) the breach of a condition can only be treated as a breach of ...` |
| s 11(4) s 11(5) | - | savings; gate to the Schedule | none | `s 11(4) section 11 affects the condition or warranty` |
| s 12(1) s 12(2) s 12(4) s 12(5) | the buyer | the seller (implied condition and warranties about title) | claim/duty | `s 12(1) there is an implied condition that the seller has a right to ...` |
| s 12(3) s 12(6) | - | scope of the title provisions; gate to the Schedule | none | `s 12(3) this subsection applies to the contract of sale` |
| s 13(1) s 13(2) | the buyer | the seller (implied condition: goods correspond with the description) | claim/duty | `s 13(1) there is an implied condition that the goods will correspond ...` |
| s 13(3) s 13(4) | - | characterisation of a sale by description; gate to the Schedule | none | `s 13(3) the sale is prevented from being a sale by description` |
| s 14(1) | the seller | the buyer (no implied condition or warranty of quality or fitness except as the Act provides) | immunity/disability | `s 14(1) there is an implied condition or warranty about the quality o...` |
| s 14(2) s 14(3) s 14(4) | the buyer | the seller (implied conditions of satisfactory quality and fitness; terms annexed by usage) | claim/duty | `s 14(2) there is an implied condition that the goods supplied are of ...` |
| s 14(2A) s 14(2B) | - | definition of satisfactory quality and its aspects | none | `s 14(2A) the goods are of satisfactory quality` |
| s 14(2C) | the seller | the buyer (the condition does not extend to matters drawn to attention, examined, or visible on a sample) | immunity/disability | `s 14(2C) the condition implied by s 14(2) extends to the matter makin...` |
| s 14(5) s 14(6) | - | agent treated as principal; gate to the Schedule | none | `s 14(5) the sale by the agent is treated as a sale by a principal in ...` |
| s 15(1) s 15(3) | - | definition of sale by sample; gate to the Schedule | none | `s 15(1) the contract of sale is a contract for sale by sample` |
| s 15(2) | the buyer | the seller (implied conditions in a sale by sample) | claim/duty | `s 15(2) there are implied conditions as to correspondence with the sa...` |
| s 15A(1) | the seller | a buyer who does not deal as consumer (cannot reject for a slight breach) | immunity/disability | `s 15A(1) the breach is not treated as a breach of condition but may b...` |
| s 15A(2) s 15A(3) | - | contrary-intention rule; treatment of a breach | none | `s 15A(1) the breach is not treated as a breach of condition but may b...` |
| s 16 | seller and buyer (each) | the other party (no property passes in unascertained goods) | immunity/disability | `s 16 property in unascertained goods is transferred to the buyer` |
| s 17(1) | the parties | each other (they may fix when property passes) | power/liability | `s 17(1) the time at which the property in the goods is transferred to...` |
| s 17(2) s 18 | - | rules for finding the parties' intention | none | `s 17(2) regard shall be had to this source in ascertaining the intent...` |
| s 19(1) s 19(2) | the seller | the buyer (the seller may reserve the right of disposal) | power/liability | `s 19(1) the property in the goods passes to the buyer` |
| s 19(3) | the seller | a buyer who does not honour the bill of exchange (must return the bill of lading) | claim/duty | `s 19(3) the buyer's duty to return the bill of lading` |
| s 20(1) | - | allocation of risk (a burden that follows property), not a relation between two persons | none | `s 20(1) the party at whose risk the goods are` |
| s 20(2) | the party whose delivery was not delayed | the party at fault for delay (risk of loss caused by the delay) | claim/duty | `s 20(2) the party at whose risk the goods are as regards the loss` |
| s 20(3) | - | savings for duties of a bailee or custodier | none | `s 20(3) section 20 affects the duties or liabilities of the seller or...` |
| s 20A(1) s 20A(3) s 20A(4) s 20A(5) s 20A(6) | - | scope and counting rules for undivided shares | none | `s 20A(1) section 20A applies to the contract` |
| s 20A(2) | the buyer out of a bulk | the seller and the other owners in common (property in an undivided share passes) | power/liability | `s 20A(2) property in an undivided share in the bulk is transferred to...` |
| s 20B(1) s 20B(2) | a person who acts in reliance on the deemed consent | the other owners in common (no cause of action against that person) | immunity/disability | `s 20B(1) the owner in common is deemed to have consented to the deali...` |
| s 20B(3) | - | savings | none | `s 20B(3) section 20A or 20B imposes or affects the matter` |
| s 21(1) | the true owner of the goods | the buyer from a non-owner (acquires no better title than the seller had) | immunity/disability | `s 21(1) the buyer acquires a better title to the goods than the selle...` |
| s 21(2) | - | savings | none | `s 21(2) this Act affects the matter` |
| s 22 s 40 | - | shown in the text as not applicable (s 22) or omitted in the 1994 Revised Edition (s 40) | none | - |
| s 23 | a buyer in good faith from a seller with a voidable title | the person entitled to avoid the seller's title | power/liability | `s 23 the buyer acquires a good title to the goods` |
| s 24 s 25 | a person receiving the goods in good faith from a seller or buyer in possession | the original owner or seller | power/liability | `s 24 the delivery or transfer has the same effect as if the seller we...` |
| s 26 | - | definition of "mercantile agent" | none | `s 26 the person is a mercantile agent for the purposes of ss 24 and 25` |
| s 27 s 28 | buyer (delivery) and seller (acceptance and payment), concurrently | seller and buyer respectively | claim/duty | `s 27 the seller's duty to deliver the goods` |
| s 29(1) s 29(4) | - | questions depending on the contract; when delivery by a third person occurs | none | `s 29(1) whether the buyer is to take possession of the goods or the s...` |
| s 29(2) s 29(3) s 29(6) | the buyer | the seller (place of delivery; send within a reasonable time; expenses of making deliverable) | claim/duty | `s 29(2) the place of delivery` |
| s 29(5) | the party receiving the demand or tender | the party making it (may treat it as ineffectual if not at a reasonable hour) | immunity/disability | `s 29(5) the demand or tender of delivery may be treated as ineffectual` |
| s 30(1) s 30(2) | the buyer | the seller (the buyer may reject, or accept the contract quantity and reject the excess) | power/liability | `s 30(1) the buyer may reject the goods delivered` |
| s 30(2A) | the seller | a buyer who does not deal as consumer (cannot reject for a slight shortfall or excess) | immunity/disability | `s 30(2A) the buyer may reject the goods under subsection (1) or rejec...` |
| s 30(2B) s 30(4) | - | treatment of a shortfall; the section yields to usage or agreement | none | `s 30(2B) the shortfall or excess is treated as one that fell within s...` |
| s 30(3) | the seller | the buyer (pays at the contract rate for what is accepted) | claim/duty | `s 30(3) the amount the buyer must pay for the whole of the goods deli...` |
| s 31(1) | the buyer | the seller (the buyer is not bound to accept delivery by instalments) | immunity/disability | `s 31(1) the buyer is bound to accept delivery of the goods by instalm...` |
| s 31(2) | - | question of construction | none | `s 31(2) the breach of contract is a repudiation of the whole contract...` |
| s 32(1) | - | deemed delivery to a carrier | none | `s 32(1) delivery of the goods to the carrier is deemed to be a delive...` |
| s 32(2) s 32(3) | the buyer | the seller (reasonable contract with the carrier; notice to insure) | claim/duty | `s 32(2) the seller's duty to make a reasonable contract with the carr...` |
| s 33 | the seller | the buyer (takes the risk of deterioration necessarily incident to transit) | immunity/disability | `s 33 the buyer must take any risk of deterioration in the goods neces...` |
| s 34 | the buyer | the seller (opportunity of examining the goods) | claim/duty | `s 34 the seller's duty to afford the buyer an opportunity of examinin...` |
| s 35(1) s 35(4) | the seller | the buyer (deemed acceptance; loses the right to reject) | immunity/disability | `s 35(1) the buyer is deemed to have accepted the goods under subsecti...` |
| s 35(2) | the buyer | the seller (not deemed to have accepted before a reasonable opportunity to examine) | immunity/disability | `s 35(2) the buyer is deemed to have accepted the goods under subsecti...` |
| s 35(3) | a buyer who deals as consumer | the seller (the buyer cannot lose the s 35(2) protection by agreement, waiver or otherwise) | immunity/disability | `s 35(3) the buyer can lose his right to rely on subsection (2) by agr...` |
| s 35(5) s 35(6) s 35(7) s 35(8) | - | counting and clarifying rules; gate to the Schedule | none | `s 35(5) the question is material in determining whether a reasonable ...` |
| s 35A(1) s 35A(2) | the seller | the buyer (loses the right to reject the rest on accepting part; instalments) | immunity/disability | `s 35A(1) the buyer loses by accepting some of the goods his right to ...` |
| s 35A(3) s 35A(4) | - | treatment rule; contrary-intention rule | none | `s 35A(3) the goods are affected by the breach` |
| s 36 | the buyer | the seller (the buyer need not return rejected goods) | privilege/no-right | `s 36 the buyer is bound to return the rejected goods to the seller` |
| s 37(1) | the seller | the buyer (loss from neglect or refusal to take delivery, and a reasonable charge for care) | claim/duty | `s 37(1) the amount the buyer is liable to the seller for` |
| s 37(2) s 38(1) s 38(2) | - | savings; definition of "unpaid seller" | none | `s 37(2) section 37 affects the rights of the seller` |
| s 39(1) s 39(2) s 41(1) s 41(2) s 42 | the unpaid seller | the buyer (lien and right of retention) | privilege/no-right | `s 39(1)(a) the unpaid seller has by implication of law a lien on the ...` |
| s 43(1) | the buyer | the unpaid seller (the lien is lost on the events listed) | immunity/disability | `s 43(1) the unpaid seller loses his lien or right of retention` |
| s 43(2) | the unpaid seller | the buyer (the lien is not lost by obtaining judgment or decree for the price) | privilege/no-right | `s 43(2) the unpaid seller loses his lien or right of retention by rea...` |
| s 44 s 46(1) s 46(2) | the unpaid seller | the buyer and the carrier (stoppage in transit) | power/liability | `s 44 the unpaid seller has the right of stopping the goods in transit` |
| s 45(1) s 45(2) s 45(3) s 45(4) s 45(5) s 45(6) s 45(7) s 46(3) | - | counting rules (course of transit, end of transit, effect of notice) | none | `s 45(1) the goods are deemed to be in course of transit` |
| s 46(4) | the unpaid seller | the carrier (must re-deliver the goods; the seller bears the expenses) | claim/duty | `s 46(4) the carrier's duty to re-deliver the goods` |
| s 47(1) | the unpaid seller | the buyer and the buyer's transferees (the seller's rights are not affected by the buyer's disposition unless the seller assented) | immunity/disability | `s 47(1) the unpaid seller's right of lien or retention or stoppage in...` |
| s 47(2) | a transferee of the document of title for value, in good faith | the unpaid seller (rights are defeated, or subject to the transferee's rights) | immunity/disability | `s 47(2) the unpaid seller's right of lien or retention or stoppage in...` |
| s 48(1) | - | effect of lien or stoppage on the contract | none | `s 48(1) the contract of sale is rescinded` |
| s 48(2) | a buyer on re-sale by the unpaid seller | the original buyer (good title as against him) | immunity/disability | `s 48(2) the buyer on the re-sale acquires a good title to the goods a...` |
| s 48(3) s 48(4) | the unpaid seller | the original buyer (may re-sell; may rescind and recover loss) | power/liability | `s 48(3) the unpaid seller may re-sell the goods and recover from the ...` |
| s 49(1) s 49(2) | the seller | the buyer (action for the price) | claim/duty | `s 49(1) the seller may maintain an action against the buyer for the p...` |
| s 50(1) | the seller | the buyer (damages for non-acceptance) | claim/duty | `s 50(1) the seller may maintain an action against the buyer for damag...` |
| s 50(2) s 50(3) s 51(2) s 51(3) s 53(2) s 53(3) | - | measures of damages for the claims in ss 50(1), 51(1) and 53(1)(b) | none | `s 50(2) the measure of damages for non-acceptance` |
| s 51(1) | the buyer | the seller (damages for non-delivery) | claim/duty | `s 51(1) the buyer may maintain an action against the seller for damag...` |
| s 52(1) | the claimant (buyer) | the seller, and the court's power to direct specific performance | power/liability | `s 52(1) the court has power to direct that the contract shall be perf...` |
| s 52(2) | the claimant (buyer) | the seller (may apply at any time before judgment) | privilege/no-right | `s 52(2) the claimant's application may be made` |
| s 52(3) | - | form of the judgment or decree | none | `s 52(3) the judgment or decree may take this form` |
| s 53(1) | the buyer | the seller (set up the breach in diminution or extinction of the price; or claim damages) | power/liability | `s 53(1) the buyer is entitled to reject the goods by reason only of t...` |
| s 53(4) | the buyer | the seller (setting up the breach does not prevent a further action) | privilege/no-right | `s 53(4) setting up the breach of warranty in diminution or extinction...` |
| s 54 | - | savings of interest, special damages and recovery of money paid | none | `s 54 this Act affects the matter` |
| s 55(1) | the parties | each other (may negative or vary rights, duties and liabilities by agreement) | power/liability | `s 55(1) the right, duty or liability may be negatived or varied` |
| s 55(2) s 55(3) s 56 | - | construction rule; gates to the Schedule | none | `s 55(2) an express condition or warranty negatives a condition or war...` |
| s 57(1) s 57(2) | - | lots as separate contracts; completion of a sale by auction | none | `s 57(1) each lot is deemed to be the subject of a separate contract o...` |
| s 57(3) | the seller | bidders (may reserve a right to bid and a reserve price) | power/liability | `s 57(3) the sale by auction may be notified to be subject to, or a ri...` |
| s 57(4) | the buyer (bidder) | the seller and the auctioneer (must not bid, or knowingly take a bid from the seller) | claim/duty | `s 57(4) the seller's prohibition on bidding` |
| s 57(5) | the buyer | the seller (may treat the sale as fraudulent) | power/liability | `s 57(5) the sale may be treated as fraudulent by the buyer` |
| s 57(6) | the seller | bidders (may bid where a right to bid was reserved) | privilege/no-right | `s 57(6) the seller, or any one person on his behalf, may bid at the a...` |
| s 58 | - | omitted in the 1994 Revised Edition | none | - |
| s 59 | - | a reasonable time is a question of fact | none | `s 59 what is a reasonable time is a question of fact` |
| s 60 | a person holding a right under the Act | the person against whom it lies (enforceable by action) | claim/duty | `s 60 the right, duty or liability may be enforced by action` |
| s 61(1) (the 17 defined terms) | - | definitions | none | `s 61(1) the definitions of this section apply` |
| s 61(2) s 61(3) s 61(4) s 61(4A) s 61(4B) s 61(5) | - | rules of reading and counting; burden rule in s 61(4B); gate to the Schedule | none | `s 61(2) the thing is deemed to be done in good faith` |
| s 62(1) s 62(2) s 62(3) s 62(4) | - | savings of bankruptcy rules, common law, bills of sale and security transactions | none | `s 62(1) the rules in bankruptcy relating to contracts of sale apply t...` |
| s 63 | - | short title | none | - |
| sch para 1(1) sch para 1(2) sch para 1(3) | - | preliminary and gate provisions of the Schedule | none | `sch para 1(1) the Schedule modifies this Act as it applies to the con...` |
| sch para 2 | the seller | the buyer (s 11(3) as it stood for a contract before 22 April 1967) | immunity/disability | `sch para 2 s 11(3) as modified: the breach of a condition can only be...` |
| sch para 3 | the buyer | the seller (s 12 as it stood for a contract before 18 May 1973) | claim/duty | `sch para 3 s 12(a) there is an implied condition that the seller has ...` |
| sch para 4 | - | gate: s 13(3) omitted for a contract before 18 May 1973 | none | `sch para 4 section 13(3) applies to the contract` |
| sch para 5 sch para 6 | the buyer | the seller (s 14 as it stood for contracts in the two windows) | claim/duty | `sch para 5 s 14(1) there is an implied condition or warranty about th...` |
| sch para 7 sch para 8 | - | deleted by Act 43 of 1996 | none | - |
| sch para 9 sch para 10 | the parties | each other (s 55 as it stood: power to negative or vary, and its limits) | power/liability | `sch para 9 s 55(1) the right, duty or liability may be negatived or v...` |
| sch para 11(1) sch para 11(2) sch para 11(3) | the buyer in an international sale | the seller (ss 12 to 15 and 55 apply despite a foreign proper law chosen by a term) | immunity/disability | `sch para 11(1) the section set out in sub-paragraph (3) is substitute...` |
| sch para 12 sch para 13 | - | definition of "business" in s 61(1) for the dates stated | none | `sch para 12 the activity is a business` |

## Coverage table

One row per section, subsection, schedule paragraph, defined term and table row of the deposited text; the script that built it is `work/cov.py` (not shipped) and it reads the file.
Each row has exactly one disposition: `encoded`, `inert (reason n)`, `fork` or `repealed or blank in this text`.
Paragraphs (a), (b) and the like are inside their subsection's row and are encoded by the same function; the line ranges below are lines of `inputs/SGA1979.txt`.
A row that is `fork` also names the rule that encodes the reading taken.
A row that is `encoded` names its first function; a `[hand-gather Gn]` mark shows that a function gathers it with others by hand (see the fork register).

### Summary

| disposition | rows |
| --- | --- |
| encoded | 345 |
| fork | 17 |
| inert | 39 |
| repealed or blank in this text | 6 |
| **total** | **407** |

Two rows moved from `encoded` to `fork` on 2026-11-05 because a new fork reads them (s 14(2C): F9; s 48(3): F11); the total stays 407.
Three more (s 18(b), s 18(c), s 29(4)) moved for fork F12 and went back to `encoded` when Meng ruled it later the same day (06:04): their rows now name the bar twin beside the original function.
The sites of fork F10 ("when", "while", "in the case of" read as "where") stay `encoded`: that fork records a reading the text does not choose between two licensed alternatives (for "when", "upon" and "whenever", ruled), and the quoted words are cited on each branch.

### Audit

- Lines in the text file: 2116; non-blank: 1498; page furniture (running headers and footers): 88; non-blank lines outside every row: 0 (checked by the script).
- Rows before the audit pass (the script's non-overlapping partition of the lines): 385.
- Rows after the audit pass: 407 (the 385 script rows plus 22 overlapping rows, one for each defined term found inside an operative section; those rows share lines with their parent row and are listed at the end of the table).
- Text lines quoted in layer 1 (`-- src:N | ...`): 1092 of 1410 non-furniture non-blank lines; the other 318 are in inert or repealed rows, or are headings, marginal notes or amendment tags inside encoded rows (listed against their rows, reason 1).
- `srcrefs.py check --refs inputs/SGA1979.txt <every layer-1 module>`: 0 problems, and with `--strict`: 0 problems (final run).

### Rows

| row | lines | disposition | rule, fork or reason |
| --- | --- | --- | --- |
| front: title and edition banner | 1-15 | inert (reason 1) | title and edition banner |
| front: arrangement of sections | 16-179 | inert (reason 1) | table of contents: a list of headings and section numbers |
| front: long title and date of enactment | 180-181 | inert (reason 1) | long title and the bracketed date; creates no rule |
| Part 1 heading | 183-185 | inert (reason 1) | Part heading |
| s 1(1) | 187-190 | fork | F6; rule: `s 1(1) this Act applies to the contract of sale of goods`; lines not quoted (heading, marginal note or amendment tag; reason 1): 187. |
| s 1(2) | 192-194 | encoded | `s 1(2) this Act applies to the contract subject to the modification of the section mentio...` [hand-gather G1] |
| s 1(3) | 196-200 | encoded | `s 1(3) a modification of the section is indicated in the section by a reference to the Sc...` |
| s 1(4) | 202-204 | encoded | `s 1(4) this Act applies in relation to the contract without modification of the section` |
| Part 2 heading | 206-208 | inert (reason 1) | Part heading |
| s 2(1) | 210-216 | encoded | `s 2(1) the contract is a contract of sale of goods` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 210, 212. |
| s 2(2) | 218-219 | encoded | `s 2(2) there may be a contract of sale between one part owner and another` |
| s 2(3) | 221 | encoded | `s 2(3) the contract of sale is absolute or conditional` |
| s 2(4) | 223-224 | encoded | `s 2(4) the contract is called a sale` (+1 more) [hand-gather G3] |
| s 2(5) | 226-228 | encoded | `s 2(5) the contract is called an agreement to sell` (+1 more) [hand-gather G3] |
| s 2(6) | 230-232 | encoded | `s 2(6) the agreement to sell becomes a sale` (+1 more) [hand-gather G3] |
| s 3(1) | 234-237 | encoded | `s 3(1) the party has capacity to buy and sell`; lines not quoted (heading, marginal note or amendment tag; reason 1): 234. |
| s 3(2) | 239-241 | encoded | `s 3(2) the amount the buyer must pay for necessaries sold and delivered` |
| s 3(3) | 243-248 | encoded | `s 3(3) the goods are necessaries` |
| s 4(1) | 250-257 | encoded | `s 4(1) a contract of sale may be made in this form`; lines not quoted (heading, marginal note or amendment tag; reason 1): 250, 252. |
| s 4(2) | 259 | encoded | `s 4(2) section 4 affects the law relating to corporations` |
| s 5(1) | 261-268 | encoded | `s 5(1) the goods may be the subject of a contract of sale` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 261, 263. |
| s 5(2) | 270-272 | encoded | `s 5(2) there may be a contract for the sale of goods whose acquisition depends on a conti...` |
| s 5(3) | 274-276 | encoded | `s 5(3) a purported present sale of future goods operates as an agreement to sell` |
| s 6 | 278-282 | encoded | `s 6 the contract is void`; lines not quoted (heading, marginal note or amendment tag; reason 1): 278. |
| s 7 | 284-292 | encoded | `s 7 the agreement to sell is avoided`; lines not quoted (heading, marginal note or amendment tag; reason 1): 284. |
| s 8(1) | 294-300 | encoded | `s 8(1) the price is determined as the subsection mentions`; lines not quoted (heading, marginal note or amendment tag; reason 1): 294, 296. |
| s 8(2) | 302-303 | encoded | `s 8(2) the amount the buyer must pay where the price is not determined` |
| s 8(3) | 305-306 | encoded | `s 8(3) the Act's own figure for a reasonable price` |
| s 9(1) | 308-314 | encoded | `s 9(1) the agreement to sell is avoided` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 308. |
| s 9(2) | 316-318 | encoded | `s 9(2) the party who may maintain an action for damages against the party at fault` |
| s 10(1) | 320-326 | encoded | `s 10(1) a stipulation as to time of payment is of the essence of the contract`; lines not quoted (heading, marginal note or amendment tag; reason 1): 320, 322. |
| s 10(2) | 328-329 | encoded | `s 10(2) any other stipulation as to time is of the essence of the contract` |
| s 10(3) | 331-332 | fork | F1; rule: `s 10(3) a month in a contract of sale means a calendar month` |
| s 11(1) | 334-343 | encoded | `s 11(1) the buyer may waive the condition` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 334. |
| s 11(2) | 345-351 | encoded | `s 11(2) the stipulation is a condition or a warranty` |
| s 11(3) | 353-358 | encoded | `s 11(3) the breach of a condition can only be treated as a breach of warranty` (+1 more) |
| s 11(4) | 360-361 | encoded | `s 11(4) section 11 affects the condition or warranty` |
| s 11(5) | 363-364 | encoded | `s 11(5) paragraph 2 of the Schedule applies in relation to the contract` |
| s 12(1) | 366-372 | encoded | `s 12(1) there is an implied condition that the seller has a right to sell the goods` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 366. |
| s 12(2) | 374-375 | encoded | `s 12(2)(a) the implied warranty that the goods are free from an undisclosed charge or enc...` (+1 more) |
| s 12(2)(a) | 377-380 | encoded | `s 12(2)(a) the implied warranty that the goods are free from an undisclosed charge or enc...` |
| s 12(2)(b) | 382-389 | encoded | `s 12(2)(b) the implied warranty of quiet possession is broken` |
| s 12(3) | 391-394 | encoded | `s 12(3) this subsection applies to the contract of sale` |
| s 12(4) | 396-399 | encoded | `s 12(4) the implied warranty that known charges have been disclosed is broken` |
| s 12(5) | 401-403 | encoded | `s 12(5) the implied warranty that none of the named persons will disturb quiet possession...` |
| s 12(5)(a) | 405 | encoded | `s 12(5) the implied warranty that none of the named persons will disturb quiet possession...` |
| s 12(5)(b) | 407-409 | encoded | `s 12(5) the implied warranty that none of the named persons will disturb quiet possession...` |
| s 12(5)(c) | 411-414 | encoded | `s 12(5) the implied warranty that none of the named persons will disturb quiet possession...` |
| s 12(6) | 416-417 | encoded | `s 12(6) paragraph 3 of the Schedule applies in relation to the contract` |
| s 13(1) | 419-423 | encoded | `s 13(1) there is an implied condition that the goods will correspond with the description` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 419. |
| s 13(2) | 425-427 | encoded | `s 13(2) it is sufficient that the bulk of the goods corresponds with the sample` |
| s 13(3) | 429-434 | encoded | `s 13(3) the sale is prevented from being a sale by description` |
| s 13(4) | 436-437 | encoded | `s 13(4) paragraph 4 of the Schedule applies in relation to the contract` |
| s 14(1) | 439-444 | encoded | `s 14(1) there is an implied condition or warranty about the quality or fitness of the goo...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 439. |
| s 14(2) | 446-448 | encoded | `s 14(2) there is an implied condition that the goods supplied are of satisfactory quality` (+1 more) |
| s 14(2A) | 450-453 | encoded | `s 14(2A) the goods are of satisfactory quality` (+1 more) |
| s 14(2B) | 455-457 | encoded | `s 14(2B) the aspect is an aspect of the quality of the goods` |
| s 14(2B)(a) | 459-460 | encoded | `s 14(2B) the aspect is an aspect of the quality of the goods` |
| s 14(2B)(b) | 462 | encoded | `s 14(2B) the aspect is an aspect of the quality of the goods` |
| s 14(2B)(c) | 464 | encoded | `s 14(2B) the aspect is an aspect of the quality of the goods` |
| s 14(2B)(d) | 466 | encoded | `s 14(2B) the aspect is an aspect of the quality of the goods` |
| s 14(2B)(e) | 468 | encoded | `s 14(2B) the aspect is an aspect of the quality of the goods` |
| s 14(2C) | 470-471 | fork | F9; rule: `s 14(2C) the condition implied by s 14(2) extends to the matter making the quality unsati...` |
| s 14(2C)(a) | 473-474 | encoded | `s 14(2C) the condition implied by s 14(2) extends to the matter making the quality unsati...` |
| s 14(2C)(b) | 476-477 | encoded | `s 14(2C) the condition implied by s 14(2) extends to the matter making the quality unsati...` |
| s 14(2C)(c) | 479-484 | encoded | `s 14(2C) the condition implied by s 14(2) extends to the matter making the quality unsati...` |
| s 14(3) | 486-487 | encoded | `s 14(3) there is an implied condition that the goods are reasonably fit for the purpose m...` (+1 more) |
| s 14(3)(a) | 489 | encoded | `s 14(3) there is an implied condition that the goods are reasonably fit for the purpose m...` (+1 more) |
| s 14(3)(b) | 491-501 | encoded | `s 14(3) there is an implied condition that the goods are reasonably fit for the purpose m...` (+1 more) |
| s 14(4) | 503-504 | encoded | `s 14(4) an implied condition or warranty about quality or fitness is annexed by usage` |
| s 14(5) | 506-511 | encoded | `s 14(5) the sale by the agent is treated as a sale by a principal in the course of a busi...` |
| s 14(6) | 513-515 | fork | F8; rule: `s 14(6) paragraph 5 of the Schedule applies in relation to the contract` |
| s 15(1) | 517-522 | encoded | `s 15(1) the contract of sale is a contract for sale by sample`; lines not quoted (heading, marginal note or amendment tag; reason 1): 517, 519. |
| s 15(2) | 524-525 | encoded | `s 15(2) there are implied conditions as to correspondence with the sample and freedom fro...` (+2 more) |
| s 15(2)(a) | 527-530 | encoded | `s 15(2) there are implied conditions as to correspondence with the sample and freedom fro...` (+1 more) |
| s 15(2)(b) | 532-534 | encoded | `s 15(2) there are implied conditions as to correspondence with the sample and freedom fro...` (+1 more) |
| s 15(3) | 536-537 | fork | F7; rule: `s 15(3) paragraph 7 of the Schedule applies in relation to the contract` |
| s 15A(1) | 539-544 | encoded | `s 15A(1) the breach is not treated as a breach of condition but may be treated as a breac...` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 539, 541, 542. |
| s 15A(1)(a) | 546-548 | encoded | `s 15A(1) the breach is not treated as a breach of condition but may be treated as a breac...` (+1 more) |
| s 15A(1)(b) | 550-555 | encoded | `s 15A(1) the breach is not treated as a breach of condition but may be treated as a breac...` (+1 more) |
| s 15A(2) | 557-558 | encoded | `s 15A(1) the breach is not treated as a breach of condition but may be treated as a breac...` (+1 more) |
| s 15A(3) | 560-561 | encoded | `s 15A(3) the breach is treated as one that fell within subsection (1)(b)` |
| Part 3 heading | 563-565 | inert (reason 1) | Part heading |
| s 16 | 567-576 | encoded | `s 16 property in unascertained goods is transferred to the buyer` (+1 more: the bar `s 16 property in unascertained goods cannot yet be transferred`, F12); lines not quoted (heading, marginal note or amendment tag; reason 1): 567, 569. |
| s 17(1) | 578-582 | encoded | `s 17(1) the time at which the property in the goods is transferred to the buyer`; lines not quoted (heading, marginal note or amendment tag; reason 1): 578. |
| s 17(2) | 584-586 | encoded | `s 17(2) regard shall be had to this source in ascertaining the intention of the parties` |
| s 18 | 588-592 | encoded | `s 18 the following are rules for ascertaining the intention of the parties as to when the...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 588. |
| s 18(a) | 594-598 | encoded | `s 18(a) Rule 1: the property in the goods has passed to the buyer` |
| s 18(b) | 600-604 | encoded | `s 18(b) Rule 2: the property in the goods has passed to the buyer` (+1 more: the bar `s 18(b) Rule 2: the property cannot yet pass`, F12) |
| s 18(c) | 606-611 | encoded | `s 18(c) Rule 3: the property in the goods has passed to the buyer` (+1 more: the bar `s 18(c) Rule 3: the property cannot yet pass`, F12) |
| s 18(d) | 613-615 | encoded | `s 18(d) Rule 4: the property in the goods has passed to the buyer` |
| s 18(d)(i) | 617-618 | encoded | `s 18(d) Rule 4: the property in the goods has passed to the buyer` |
| s 18(d)(ii) | 620-629 | encoded | `s 18(d) Rule 4: the property in the goods has passed to the buyer` |
| s 18(e)(i) | 631-639 | encoded | `s 18(e)(i) Rule 5(i): the property in the goods has passed to the buyer` |
| s 18(e)(ii) | 641-646 | encoded | `s 18(e)(ii) Rule 5(ii): the seller is taken to have unconditionally appropriated the good...` |
| s 18(e)(iii) | 648-654 | encoded | `s 18(e)(iii) Rule 5(iii): the remaining goods are appropriated and the property has passe...` |
| s 18(e)(iii)(A) | 656-658 | encoded | `s 18(e)(iii) Rule 5(iii): the remaining goods are appropriated and the property has passe...` |
| s 18(e)(iii)(B) | 660 | encoded | `s 18(e)(iii) Rule 5(iii): the remaining goods are appropriated and the property has passe...` |
| s 18(e)(iv) | 662-669 | encoded | `s 18(e)(iv) Rule 5(iv): the property in the remaining goods has passed to the single buyer` |
| s 19(1) | 671-680 | encoded | `s 19(1) the property in the goods passes to the buyer` (+1 more: the bar `s 19(1) the property cannot yet pass because the right of disposal is reserved`, F12); lines not quoted (heading, marginal note or amendment tag; reason 1): 671. |
| s 19(2) | 682-684 | encoded | `s 19(2) the seller is taken to reserve the right of disposal` |
| s 19(3) | 686-691 | encoded | `s 19(3) the buyer's duty to return the bill of lading` (+2 more) |
| s 20(1) | 693-698 | encoded | `s 20(1) the party at whose risk the goods are`; lines not quoted (heading, marginal note or amendment tag; reason 1): 693. |
| s 20(2) | 700-702 | encoded | `s 20(2) the party at whose risk the goods are as regards the loss` |
| s 20(3) | 704-705 | encoded | `s 20(3) section 20 affects the duties or liabilities of the seller or buyer as a bailee o...` |
| s 20A(1) | 707-714 | encoded | `s 20A(1) section 20A applies to the contract`; lines not quoted (heading, marginal note or amendment tag; reason 1): 707. |
| s 20A(1)(a) | 716-718 | encoded | `s 20A(1) section 20A applies to the contract` |
| s 20A(1)(b) | 720-722 | encoded | `s 20A(1) section 20A applies to the contract` |
| s 20A(2) | 724-727 | encoded | `s 20A(2) property in an undivided share in the bulk is transferred to the buyer and he be...` (+1 more) |
| s 20A(2)(a) | 729-730 | encoded | `s 20A(2) property in an undivided share in the bulk is transferred to the buyer and he be...` (+1 more) |
| s 20A(2)(b) | 732 | encoded | `s 20A(2) property in an undivided share in the bulk is transferred to the buyer and he be...` (+1 more) |
| s 20A(3) | 734-737 | fork | F3; rule: `s 20A(3) the undivided share of the buyer in the bulk` |
| s 20A(4) | 739-743 | encoded | `s 20A(4) the undivided share of this buyer after proportionate reduction` |
| s 20A(5) | 745-748 | encoded | `s 20A(5) the quantity of paid-for goods still to be delivered after the delivery` |
| s 20A(6) | 750-752 | fork | F3; rule: `s 20A(6) the quantity of goods treated as paid for` |
| s 20B(1) | 754-760 | encoded | `s 20B(1) the owner in common is deemed to have consented to the dealing`; lines not quoted (heading, marginal note or amendment tag; reason 1): 754. |
| s 20B(1)(a) | 762-764 | encoded | `s 20B(1) the owner in common is deemed to have consented to the dealing` |
| s 20B(1)(b) | 766-770 | encoded | `s 20B(1) the owner in common is deemed to have consented to the dealing` |
| s 20B(2) | 772-775 | encoded | `s 20B(2) a cause of action accrues to anyone against the person who so acted` |
| s 20B(3) | 777 | encoded | `s 20B(3) section 20A or 20B imposes or affects the matter` |
| s 20B(3)(a) | 779-781 | encoded | `s 20B(3) section 20A or 20B imposes or affects the matter` |
| s 20B(3)(b) | 783-784 | encoded | `s 20B(3) section 20A or 20B imposes or affects the matter` |
| s 20B(3)(c) | 786 | encoded | `s 20B(3) section 20A or 20B imposes or affects the matter` |
| s 21(1) | 788-796 | encoded | `s 21(1) the buyer acquires a better title to the goods than the seller had`; lines not quoted (heading, marginal note or amendment tag; reason 1): 788, 790. |
| s 21(2) | 798 | encoded | `s 21(2) this Act affects the matter` |
| s 21(2)(a) | 800-802 | encoded | `s 21(2) this Act affects the matter` |
| s 21(2)(b) | 804-809 | encoded | `s 21(2) this Act affects the matter` |
| s 22 | 811 | repealed or blank in this text | the text shows "22. [Not applicable]" (line 811); the Legislative History says the Act applies "except sections 22 and 25(2)" |
| s 23 | 813-818 | encoded | `s 23 the buyer acquires a good title to the goods`; lines not quoted (heading, marginal note or amendment tag; reason 1): 813. |
| s 24 | 820-829 | encoded | `s 24 the delivery or transfer has the same effect as if the seller were expressly authori...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 820. |
| s 25 | 831-842 | encoded | `s 25 the delivery or transfer has the same effect as if the person making it were a merca...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 831. |
| s 26 | 844-848 | encoded | `s 26 the person is a mercantile agent for the purposes of ss 24 and 25`; lines not quoted (heading, marginal note or amendment tag; reason 1): 844. |
| s 26(a) | 850 | encoded | `s 26 the person is a mercantile agent for the purposes of ss 24 and 25` |
| s 26(b) | 852-855 | encoded | `s 26 the person is a mercantile agent for the purposes of ss 24 and 25` |
| s 26(c) | 857 | encoded | `s 26 the person is a mercantile agent for the purposes of ss 24 and 25` |
| s 26(d) | 859 | encoded | `s 26 the person is a mercantile agent for the purposes of ss 24 and 25` |
| Part 4 heading | 861-863 | inert (reason 1) | Part heading |
| s 27 | 865-869 | encoded | `s 27 the seller's duty to deliver the goods` (+4 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 865. |
| s 28 | 871-877 | encoded | `s 28 the seller's duty to be ready and willing` (+4 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 871. |
| s 29(1) | 879-883 | encoded | `s 29(1) whether the buyer is to take possession of the goods or the seller is to send them`; lines not quoted (heading, marginal note or amendment tag; reason 1): 879. |
| s 29(2) | 885-889 | encoded | `s 29(2) the place of delivery` |
| s 29(3) | 891-893 | encoded | `s 29(3) the seller's duty to send the goods within a reasonable time` (+1 more) |
| s 29(4) | 895-902 | encoded | `s 29(4) there is delivery by the seller to the buyer` (+2 more: the document-of-title limb, and the bar `s 29(4) delivery is not yet possible`, F12) |
| s 29(5) | 904-906 | encoded | `s 29(5) the demand or tender of delivery may be treated as ineffectual` |
| s 29(6) | 908-909 | encoded | `s 29(6) the party who must bear the expenses of putting the goods into a deliverable state` |
| s 30(1) | 911-916 | encoded | `s 30(1) the buyer may reject the goods delivered` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 911. |
| s 30(2) | 918-920 | encoded | `s 30(2) the buyer may accept the goods included in the contract and reject the rest` (+1 more) |
| s 30(2A) | 922 | encoded | `s 30(2A) the buyer may reject the goods under subsection (1) or reject the whole under su...` |
| s 30(2A)(a) | 924-925 | encoded | `s 30(2A) the buyer may reject the goods under subsection (1) or reject the whole under su...` |
| s 30(2A)(b) | 927-933 | encoded | `s 30(2A) the buyer may reject the goods under subsection (1) or reject the whole under su...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 933. |
| s 30(2B) | 935-936 | encoded | `s 30(2B) the shortfall or excess is treated as one that fell within subsection (2A)` |
| s 30(3) | 938-940 | encoded | `s 30(3) the amount the buyer must pay for the whole of the goods delivered and accepted` |
| s 30(4) | 942-943 | encoded | `s 30(4) section 30 gives way to a usage of trade, special agreement or course of dealing` |
| s 31(1) | 945-951 | encoded | `s 31(1) the buyer is bound to accept delivery of the goods by instalments`; lines not quoted (heading, marginal note or amendment tag; reason 1): 945. |
| s 31(2) | 953-961 | encoded | `s 31(2) the breach of contract is a repudiation of the whole contract or a severable brea...` |
| s 32(1) | 963-969 | encoded | `s 32(1) delivery of the goods to the carrier is deemed to be a delivery of the goods to t...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 963. |
| s 32(2) | 971-977 | encoded | `s 32(2) the seller's duty to make a reasonable contract with the carrier` (+2 more) |
| s 32(3) | 979-984 | encoded | `s 32(3) the seller's duty to give notice enabling the buyer to insure` (+2 more) |
| s 33 | 986-994 | encoded | `s 33 the buyer must take any risk of deterioration in the goods necessarily incident to t...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 986. |
| s 34 | 996-1003 | encoded | `s 34 the seller's duty to afford the buyer an opportunity of examining the goods` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 996. |
| s 35(1) | 1005-1008 | encoded | `s 35(1) the buyer is deemed to have accepted the goods under subsection (1)` (+1 more) [hand-gather G4]; lines not quoted (heading, marginal note or amendment tag; reason 1): 1005. |
| s 35(1)(a) | 1010-1011 | encoded | `s 35(1) the buyer is deemed to have accepted the goods under subsection (1)` (+1 more) |
| s 35(1)(b) | 1013-1015 | encoded | `s 35(1) the buyer is deemed to have accepted the goods under subsection (1)` (+1 more) |
| s 35(2) | 1017-1020 | encoded | `s 35(2) the buyer is deemed to have accepted the goods under subsection (1)` (+1 more) [hand-gather G4] |
| s 35(2)(a) | 1022-1023 | encoded | `s 35(2) the buyer is deemed to have accepted the goods under subsection (1)` (+1 more) |
| s 35(2)(b) | 1025-1026 | encoded | `s 35(2) the buyer is deemed to have accepted the goods under subsection (1)` (+1 more) |
| s 35(3) | 1028-1029 | encoded | `s 35(3) the buyer can lose his right to rely on subsection (2) by agreement, waiver or ot...` (+1 more) |
| s 35(4) | 1031-1033 | encoded | `s 35(4) the buyer is deemed to have accepted the goods after a reasonable time` (+1 more) [hand-gather G4] |
| s 35(5) | 1035-1041 | encoded | `s 35(5) the question is material in determining whether a reasonable time has elapsed for...` (+1 more) |
| s 35(6) | 1043-1044 | encoded | `s 35(6) the buyer is deemed to have accepted the goods by virtue of section 35 merely bec...` (+1 more) |
| s 35(6)(a) | 1046-1047 | encoded | `s 35(6) the buyer is deemed to have accepted the goods by virtue of section 35 merely bec...` (+1 more) |
| s 35(6)(b) | 1049-1050 | encoded | `s 35(6) the buyer is deemed to have accepted the goods by virtue of section 35 merely bec...` (+1 more) |
| s 35(7) | 1052-1056 | encoded | `s 35(7) the unit is a commercial unit` (+2 more) [hand-gather G4] |
| s 35(8) | 1058-1059 | fork | F7; rule: `s 35(8) paragraph 8 of the Schedule applies in relation to the contract` |
| s 35A(1) | 1061-1063 | encoded | `s 35A(1) the buyer loses by accepting some of the goods his right to reject the rest`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1061. |
| s 35A(1)(a) | 1065-1066 | encoded | `s 35A(1) the buyer loses by accepting some of the goods his right to reject the rest` |
| s 35A(1)(b) | 1068-1071 | encoded | `s 35A(1) the buyer loses by accepting some of the goods his right to reject the rest` |
| s 35A(2) | 1073-1075 | encoded | `s 35A(2) the buyer loses by accepting some of the goods in the instalment his right to re...` |
| s 35A(3) | 1077-1079 | encoded | `s 35A(3) the goods are affected by the breach` |
| s 35A(4) | 1081-1082 | encoded | `s 35A(4) section 35A applies to the contract` |
| s 36 | 1084-1093 | encoded | `s 36 the buyer is bound to return the rejected goods to the seller` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 1084. |
| s 37(1) | 1095-1102 | encoded | `s 37(1) the amount the buyer is liable to the seller for`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1095. |
| s 37(2) | 1104-1106 | encoded | `s 37(2) section 37 affects the rights of the seller` |
| Part 5 heading | 1108-1110 | inert (reason 1) | Part heading |
| s 38(1) | 1112-1117 | encoded | `s 38(1) the seller of goods is an unpaid seller`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1112, 1114. |
| s 38(1)(a) | 1119 | encoded | `s 38(1) the seller of goods is an unpaid seller` |
| s 38(1)(b) | 1121-1124 | encoded | `s 38(1) the seller of goods is an unpaid seller` |
| s 38(2) | 1126-1129 | encoded | `s 38(2) the person is a seller for the purposes of Part 5` |
| s 39(1) | 1131-1138 | encoded | `s 39(1)(a) the unpaid seller has by implication of law a lien on the goods or right to re...` (+2 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 1131. |
| s 39(1)(a) | 1140-1141 | encoded | `s 39(1)(a) the unpaid seller has by implication of law a lien on the goods or right to re...` (+2 more) |
| s 39(1)(b) | 1143-1145 | encoded | `s 39(1)(b) the unpaid seller has by implication of law a right of stopping the goods in t...` (+1 more) |
| s 39(1)(c) | 1147 | encoded | `s 39(1)(c) the unpaid seller has by implication of law a right of re-sale as limited by t...` |
| s 39(2) | 1149-1153 | encoded | `s 39(2) the unpaid seller has a right of withholding delivery similar to and co-extensive...` |
| s 40 | 1155 | repealed or blank in this text | the text shows "40. [Omitted in 1994 Revised Edition]" (line 1155) |
| s 41(1) | 1157-1163 | encoded | `s 41(1) the unpaid seller is entitled to retain possession of the goods until payment or ...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1157, 1159. |
| s 41(1)(a) | 1165-1166 | encoded | `s 41(1) the unpaid seller is entitled to retain possession of the goods until payment or ...` |
| s 41(1)(b) | 1168-1169 | encoded | `s 41(1) the unpaid seller is entitled to retain possession of the goods until payment or ...` |
| s 41(1)(c) | 1171 | encoded | `s 41(1) the unpaid seller is entitled to retain possession of the goods until payment or ...` |
| s 41(2) | 1173-1175 | encoded | `s 41(2) the seller may exercise his lien or right of retention although he is in possessi...` |
| s 42 | 1177-1185 | encoded | `s 42 the unpaid seller may exercise his lien or right of retention on the remainder`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1177. |
| s 43(1) | 1187-1190 | encoded | `s 43(1) the unpaid seller loses his lien or right of retention`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1187. |
| s 43(1)(a) | 1192-1194 | encoded | `s 43(1) the unpaid seller loses his lien or right of retention` |
| s 43(1)(b) | 1196-1197 | encoded | `s 43(1) the unpaid seller loses his lien or right of retention` |
| s 43(1)(c) | 1199 | encoded | `s 43(1) the unpaid seller loses his lien or right of retention` |
| s 43(2) | 1201-1204 | encoded | `s 43(2) the unpaid seller loses his lien or right of retention by reason only of obtainin...` |
| s 44 | 1206-1214 | encoded | `s 44 the unpaid seller has the right of stopping the goods in transit` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 1206, 1208. |
| s 45(1) | 1216-1222 | encoded | `s 45(1) the goods are deemed to be in course of transit` (+1 more) [hand-gather G5]; lines not quoted (heading, marginal note or amendment tag; reason 1): 1216. |
| s 45(2) | 1224-1226 | encoded | `s 45(2) the transit is at an end` (+1 more) [hand-gather G5] |
| s 45(3) | 1228-1237 | encoded | `s 45(3) the transit is at an end` (+1 more) [hand-gather G5] |
| s 45(4) | 1239-1242 | encoded | `s 45(4) the transit is at an end` (+1 more) [hand-gather G5] |
| s 45(5) | 1244-1247 | encoded | `s 45(5) the goods are in the possession of the master as a carrier and not as agent to th...` (+1 more) |
| s 45(6) | 1249-1251 | encoded | `s 45(6) the transit is deemed to be at an end` (+1 more) [hand-gather G5] |
| s 45(7) | 1253-1257 | encoded | `s 45(7) the remainder of the goods may be stopped in transit` (+1 more) |
| s 46(1) | 1259-1264 | encoded | `s 46(1) the unpaid seller may exercise his right of stoppage in transit by this method`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1259. |
| s 46(2) | 1266-1267 | encoded | `s 46(2) the notice may be given to this person` |
| s 46(3) | 1269-1272 | encoded | `s 46(3) the notice is effective` |
| s 46(4) | 1274-1280 | encoded | `s 46(4) the carrier's duty to re-deliver the goods` (+3 more) |
| s 47(1) | 1282-1289 | encoded | `s 47(1) the unpaid seller's right of lien or retention or stoppage in transit is affected...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1282, 1284. |
| s 47(2) | 1291-1294 | encoded | `s 47(2) the unpaid seller's right of lien or retention or stoppage in transit is defeated` (+1 more) |
| s 47(2)(a) | 1296-1298 | encoded | `s 47(2) the unpaid seller's right of lien or retention or stoppage in transit is defeated` |
| s 47(2)(b) | 1300-1303 | encoded | `s 47(2) the unpaid seller's right of lien or retention or stoppage in transit is defeated` (+1 more) |
| s 48(1) | 1305-1311 | encoded | `s 48(1) the contract of sale is rescinded`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1305, 1307. |
| s 48(2) | 1313-1315 | encoded | `s 48(2) the buyer on the re-sale acquires a good title to the goods as against the origin...` |
| s 48(3) | 1317-1321 | fork | F11; rule: `s 48(3) the unpaid seller may re-sell the goods and recover from the original buyer damag...` |
| s 48(4) | 1323-1330 | encoded | `s 48(4) the original contract of sale is rescinded` |
| Part 6 heading | 1332-1334 | inert (reason 1) | Part heading |
| s 49(1) | 1336-1343 | encoded | `s 49(1) the seller may maintain an action against the buyer for the price of the goods` (+1 more) [hand-gather G6]; lines not quoted (heading, marginal note or amendment tag; reason 1): 1336, 1338. |
| s 49(2) | 1345-1349 | encoded | `s 49(2) the seller may maintain an action for the price although the property in the good...` (+1 more) [hand-gather G6] |
| s 50(1) | 1351-1355 | encoded | `s 50(1) the seller may maintain an action against the buyer for damages for non-acceptance`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1351. |
| s 50(2) | 1357-1359 | encoded | `s 50(2) the measure of damages for non-acceptance` |
| s 50(3) | 1361-1369 | fork | F2; rule: `s 50(3) the measure of damages for non-acceptance where there is an available market` |
| s 51(1) | 1371-1377 | encoded | `s 51(1) the buyer may maintain an action against the seller for damages for non-delivery` (+1 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 1371, 1373. |
| s 51(2) | 1379-1381 | encoded | `s 51(2) the measure of damages for non-delivery` |
| s 51(3) | 1383-1387 | fork | F2; rule: `s 51(3) the measure of damages for non-delivery where there is an available market` |
| s 52(1) | 1389-1397 | encoded | `s 52(1) the court has power to direct that the contract shall be performed specifically`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1389, 1397. |
| s 52(2) | 1399-1402 | encoded | `s 52(2) the claimant's application may be made`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1402. |
| s 52(3) | 1404-1406 | encoded | `s 52(3) the judgment or decree may take this form` |
| s 53(1) | 1408-1417 | encoded | `s 53(1) the buyer is entitled to reject the goods by reason only of the breach of warranty` (+4 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 1408. |
| s 53(1)(a) | 1419-1420 | encoded | `s 53(1)(a) the buyer may set up against the seller the breach of warranty in diminution o...` |
| s 53(1)(b) | 1422-1423 | encoded | `s 53(1)(b) the buyer may maintain an action against the seller for damages for the breach...` (+1 more) |
| s 53(2) | 1425-1427 | encoded | `s 53(2) the measure of damages for breach of warranty` |
| s 53(3) | 1429-1432 | fork | F2; rule: `s 53(3) the loss for breach of warranty of quality` |
| s 53(4) | 1434-1437 | encoded | `s 53(4) setting up the breach of warranty in diminution or extinction of the price preven...` |
| s 54 | 1439-1446 | encoded | `s 54 this Act affects the matter`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1439, 1441. |
| Part 7 heading | 1448-1450 | inert (reason 1) | Part heading |
| s 55(1) | 1452-1458 | encoded | `s 55(1) the right, duty or liability may be negatived or varied`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1452. |
| s 55(2) | 1460-1464 | encoded | `s 55(2) an express condition or warranty negatives a condition or warranty implied by thi...` |
| s 55(3) | 1466-1468 | encoded | `s 55(3) paragraph 9 of the Schedule applies in relation to the contract` (+1 more) |
| s 56 | 1470-1474 | encoded | `s 56 paragraph 11 of the Schedule applies in relation to the contract`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1470. |
| s 57(1) | 1476-1479 | encoded | `s 57(1) each lot is deemed to be the subject of a separate contract of sale`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1476. |
| s 57(2) | 1481-1483 | encoded | `s 57(2) the sale by auction is complete` (+1 more) |
| s 57(3) | 1485-1487 | encoded | `s 57(3) the sale by auction may be notified to be subject to, or a right may be reserved ...` |
| s 57(4) | 1489-1493 | encoded | `s 57(4) the seller's prohibition on bidding` (+3 more) |
| s 57(5) | 1495-1496 | encoded | `s 57(5) the sale may be treated as fraudulent by the buyer` |
| s 57(6) | 1498-1500 | encoded | `s 57(6) the seller, or any one person on his behalf, may bid at the auction` |
| s 58 | 1502 | repealed or blank in this text | the text shows "58. [Omitted in 1994 Revised Edition]" (line 1502) |
| s 59 | 1504-1510 | encoded | `s 59 what is a reasonable time is a question of fact`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1504. |
| s 60 | 1512-1515 | encoded | `s 60 the right, duty or liability may be enforced by action`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1512. |
| s 61(1) | 1517-1519 | fork | F4; rule: `s 61(1) the definitions of this section apply`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1517. |
| s 61(1) "action" | 1521 | encoded | `s 61(1) the proceeding is an action` |
| s 61(1) "bulk" | 1523-1524 | encoded | `s 61(1) the mass or collection is a bulk` |
| s 61(1) "bulk"(a) | 1526 | encoded | `s 61(1) the mass or collection is a bulk` |
| s 61(1) "bulk"(b) | 1528-1530 | encoded | `s 61(1) the mass or collection is a bulk` |
| s 61(1) "business" | 1532-1533 | encoded | `s 61(1) the activity is a business` |
| s 61(1) "buyer" | 1535 | encoded | `s 61(1) the person is a buyer` |
| s 61(1) "claimant" | 1537-1539 | encoded | `s 61(1) the person is a claimant`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1539. |
| s 61(1) "contract of sale" | 1541 | encoded | `s 61(1) the contract is a contract of sale` |
| s 61(1) "credit-broker" | 1543-1546 | encoded | `s 61(1) the person is a credit-broker` |
| s 61(1) "credit-broker"(a) | 1548-1549 | encoded | `s 61(1) the person is a credit-broker` |
| s 61(1) "credit-broker"(b) | 1551 | encoded | `s 61(1) the person is a credit-broker` |
| s 61(1) "delivery" | 1553-1556 | encoded | `s 61(1) there is delivery` |
| s 61(1) "document of title to goods" | 1558-1562 | encoded | `s 61(1) the document is a document of title to goods` |
| s 61(1) "fault" | 1564 | encoded | `s 61(1) the thing is fault` |
| s 61(1) "future goods" | 1566-1567 | encoded | `s 61(1) the goods are future goods` |
| s 61(1) "goods" | 1569-1574 | encoded | `s 61(1) the thing is goods` |
| s 61(1) [definition deleted] | 1576 | repealed or blank in this text | the text shows "[Deleted by Act 25 of 2021 wef 01/04/2022]" (line 1576) where a definition stood |
| s 61(1) "property" | 1578-1579 | encoded | `s 61(1) the interest is property` |
| s 61(1) "sale" | 1581 | encoded | `s 61(1) the transaction is a sale` |
| s 61(1) "seller" | 1583 | encoded | `s 61(1) the person is a seller` |
| s 61(1) "specific goods" | 1585-1588 | encoded | `s 61(1) the goods are specific goods` |
| s 61(1) "warranty" | 1590-1594 | encoded | `s 61(1) the agreement is a warranty` |
| s 61(2) | 1596-1598 | encoded | `s 61(2) the thing is deemed to be done in good faith` |
| s 61(3) | 1600-1602 | encoded | `s 61(3) the person is deemed to be insolvent` |
| s 61(4) | 1604-1609 | encoded | `s 61(4) the goods are in a deliverable state` |
| s 61(4A) | 1611-1613 | encoded | `s 61(4A) the buyer deals as consumer` |
| s 61(4B) | 1615-1616 | encoded | `s 61(4B) the seller's claim that the buyer does not deal as consumer is made out` |
| s 61(5) | 1618-1621 | encoded | `s 61(5) paragraph 12 of the Schedule applies as regards the definition of business` (+1 more) |
| s 62(1) | 1623-1626 | encoded | `s 62(1) the rules in bankruptcy relating to contracts of sale apply to the contract notwi...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1623. |
| s 62(2) | 1628-1633 | encoded | `s 62(2) the rule of the common law applies to the contract` |
| s 62(3) | 1635-1636 | encoded | `s 62(3) this Act affects the matter` |
| s 62(4) | 1638-1640 | encoded | `s 62(4) the provisions of this Act about contracts of sale apply to the transaction` |
| s 63 | 1642-1646 | inert (reason 2) | short title: machinery (the Act's own citation) |
| sch: title, section references and heading | 1648-1656 | inert (reason 1) | the Schedule's title and its list of the sections that refer to it; the references are operative in each section's own gate (ss 1(2), 11(5), 12(6), 13(4), 14(6), 15(3), 35(8), 55(3), 56 and 61(5)) |
| sch para 1(1) | 1657-1660 | encoded | `sch para 1(1) the Schedule modifies this Act as it applies to the contract` [hand-gather G2]; lines not quoted (heading, marginal note or amendment tag; reason 1): 1657. |
| sch para 1(2) | 1662-1663 | encoded | `sch para 1(2) what a reference in the Schedule refers to` |
| sch para 1(3) | 1665 | fork | F5; rule: `sch para 1(3) the Schedule affects the contract` |
| sch para 2 | 1667-1671 | encoded | `sch para 2 s 11(3) as modified: the breach of a condition can only be treated as a breach...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1667. |
| sch para 3 | 1673-1676 | encoded | `sch para 3 s 12(a) there is an implied condition that the seller has a right to sell the ...` (+5 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 1673. |
| sch para 3, substituted s 12 | 1678-1681 | encoded | `sch para 3 s 12(a) there is an implied condition that the seller has a right to sell the ...` (+5 more) |
| sch para 3, substituted s 12(a) | 1683-1686 | encoded | `sch para 3 s 12(a) there is an implied condition that the seller has a right to sell the ...` (+1 more) |
| sch para 3, substituted s 12(b) | 1688-1689 | encoded | `sch para 3 s 12(b) there is an implied warranty that the buyer will have and enjoy quiet ...` (+1 more) |
| sch para 3, substituted s 12(c) | 1691-1694 | encoded | `sch para 3 s 12(c) there is an implied warranty that the goods will be free from any char...` (+1 more) |
| sch para 4 | 1696-1702 | encoded | `sch para 4 section 13(3) applies to the contract`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1696, 1702. |
| sch para 5 | 1704-1707 | fork | F8; rule: `sch para 5 s 14(1) there is an implied condition or warranty about the quality or f...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1704. |
| sch para 5, substituted s 14(1) | 1709-1714 | encoded | `sch para 5 s 14(1) there is an implied condition or warranty about the quality or fitness...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1709. |
| sch para 5, substituted s 14(2) | 1716-1718 | encoded | `sch para 5 s 14(2) there is an implied condition that the goods supplied are of merchanta...` (+1 more) |
| sch para 5, substituted s 14(2)(a) | 1720-1721 | encoded | `sch para 5 s 14(2) there is an implied condition that the goods supplied are of merchanta...` (+1 more) |
| sch para 5, substituted s 14(2)(b) | 1723-1725 | encoded | `sch para 5 s 14(2) there is an implied condition that the goods supplied are of merchanta...` (+1 more) |
| sch para 5, substituted s 14(3) | 1727-1734 | encoded | `sch para 5 s 14(3) there is an implied condition that the goods supplied are reasonably f...` (+1 more) |
| sch para 5, substituted s 14(4) | 1736-1737 | encoded | `sch para 5 s 14(4) an implied condition or warranty about quality or fitness is annexed b...` |
| sch para 5, substituted s 14(5) | 1739-1744 | encoded | `sch para 5 s 14(5) the sale by the agent is treated as a sale by a principal in the cours...` |
| sch para 5, substituted s 14(6) | 1746-1755 | encoded | `sch para 5 s 14(6) the goods are of merchantable quality`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1755. |
| sch para 5, substituted s 14(7) | 1757-1765 | encoded | `sch para 5 s 14(7) the reference to the seller in subsection (3) includes the person who ...` |
| sch para 6 | 1767-1770 | fork | F8; rule: `sch para 6 s 14(1) there is an implied condition or warranty about the quality or f...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1767. |
| sch para 6, substituted s 14(1) | 1772-1776 | encoded | `sch para 6 s 14(1) there is an implied condition or warranty about the quality or fitness...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1772. |
| sch para 6, substituted s 14(2) | 1778-1786 | encoded | `sch para 6 s 14(2) there is an implied condition that the goods will be reasonably fit fo...` |
| sch para 6, substituted s 14(3) | 1788-1792 | encoded | `sch para 6 s 14(3) there is an implied condition that the goods will be of merchantable q...` |
| sch para 6, substituted s 14(4) | 1794-1795 | encoded | `sch para 6 s 14(4) an implied condition or warranty about quality or fitness is annexed b...` |
| sch para 6, substituted s 14(5) | 1797-1798 | encoded | `sch para 6 s 14(5) an express condition or warranty negatives a condition or warranty imp...` |
| sch para 7 | 1800 | repealed or blank in this text | the text shows "7. [Deleted by Act 43 of 1996]" (line 1800); s 15(3) still points at it (fork F7) |
| sch para 8 | 1801-1806 | repealed or blank in this text | the text shows "8. [Deleted by Act 43 of 1996]" (lines 1801-1806); s 35(8) still points at it (fork F7) |
| sch para 9 | 1808-1811 | encoded | `sch para 9 s 55(1) the right, duty or liability may be negatived or varied` (+12 more); lines not quoted (heading, marginal note or amendment tag; reason 1): 1808. |
| sch para 9, substituted s 55(1) | 1813-1819 | encoded | `sch para 9 s 55(1) the right, duty or liability may be negatived or varied`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1813. |
| sch para 9, substituted s 55(2) | 1821-1822 | encoded | `sch para 9 s 55(2) an express condition or warranty negatives a condition or warranty imp...` |
| sch para 9, substituted s 55(3) | 1824-1826 | encoded | `sch para 9 s 55(3) the term is void` |
| sch para 9, substituted s 55(4) | 1828-1832 | encoded | `sch para 9 s 55(4) the term exempting from section 13, 14 or 15 is void` (+1 more) |
| sch para 9, substituted s 55(5) | 1834-1837 | encoded | `sch para 9 s 55(5) regard shall be had to this matter in determining whether reliance on ...` |
| sch para 9, substituted s 55(5)(a) | 1839-1842 | encoded | `sch para 9 s 55(5) regard shall be had to this matter in determining whether reliance on ...` |
| sch para 9, substituted s 55(5)(b) | 1844-1847 | encoded | `sch para 9 s 55(5) regard shall be had to this matter in determining whether reliance on ...` |
| sch para 9, substituted s 55(5)(c) | 1849-1852 | encoded | `sch para 9 s 55(5) regard shall be had to this matter in determining whether reliance on ...` |
| sch para 9, substituted s 55(5)(d) | 1854-1864 | encoded | `sch para 9 s 55(5) regard shall be had to this matter in determining whether reliance on ...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1860. |
| sch para 9, substituted s 55(5)(e) | 1866-1867 | encoded | `sch para 9 s 55(5) regard shall be had to this matter in determining whether reliance on ...` |
| sch para 9, substituted s 55(6) | 1869-1872 | encoded | `sch para 9 s 55(6) subsection (5) prevents the court from holding that the term is not a ...` |
| sch para 9, substituted s 55(7) | 1874-1876 | encoded | `sch para 9 s 55(7) the sale is a consumer sale` |
| sch para 9, substituted s 55(7)(a) | 1878-1879 | encoded | `sch para 9 s 55(7) the sale is a consumer sale` |
| sch para 9, substituted s 55(7)(b) | 1881-1882 | encoded | `sch para 9 s 55(7) the sale is a consumer sale` |
| sch para 9, substituted s 55(8) | 1884-1886 | encoded | `sch para 9 s 55(8) the sale falls to be treated as not being a consumer sale` |
| sch para 9, substituted s 55(9) | 1888-1894 | encoded | `sch para 9 s 55(9) the term is a term exempting from the provisions of the section` |
| sch para 9, substituted s 55(10) | 1896-1899 | encoded | `sch para 9 s 55(10) the term is a term of the contract` |
| sch para 9, substituted s 55(11) | 1901-1904 | encoded | `sch para 9 s 55(11) section 55 prevents the parties from negativing or varying a right, d...` |
| sch para 9, substituted s 55(12) | 1906-1916 | encoded | `sch para 9 s 55(12) the contract is a contract for the international sale of goods`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1913. |
| sch para 9, substituted s 55(12)(a) | 1918-1921 | encoded | `sch para 9 s 55(12) the contract is a contract for the international sale of goods` |
| sch para 9, substituted s 55(12)(b) | 1923-1924 | encoded | `sch para 9 s 55(12) the contract is a contract for the international sale of goods` |
| sch para 9, substituted s 55(12)(c) | 1926-1929 | encoded | `sch para 9 s 55(12) the contract is a contract for the international sale of goods` |
| sch para 10 | 1931-1934 | encoded | `sch para 10 s 55 the right, duty or liability may be negatived or varied`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1931. |
| sch para 10, substituted s 55 | 1936-1941 | encoded | `sch para 10 s 55 the right, duty or liability may be negatived or varied`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1936. |
| sch para 11(1) | 1943-1946 | encoded | `sch para 11(1) the section set out in sub-paragraph (3) is substituted for section 56`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1943. |
| sch para 11(2) | 1948-1949 | encoded | `sch para 11(2) section 56 and paragraph 11 are ignored in relation to the contract` |
| sch para 11(3) | 1951 | encoded | `sch para 11(3) s 56(1) sections 12 to 15 and 55 apply to the contract notwithstanding the...` |
| sch para 11, substituted s 56(1) | 1953-1967 | encoded | `sch para 11(3) s 56(1) sections 12 to 15 and 55 apply to the contract notwithstanding the...`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1953, 1967. |
| sch para 11, substituted s 56(2) | 1969-1972 | encoded | `sch para 11(3) s 56(2) subsection (1) prevents the parties from negativing or varying a r...` |
| sch para 11, substituted s 56(3) | 1974-1978 | encoded | `sch para 11(3) s 56(3) the contract is a contract for the international sale of goods` |
| sch para 11, substituted s 56(3)(a) | 1980-1983 | encoded | `sch para 11(3) s 56(3) the contract is a contract for the international sale of goods` |
| sch para 11, substituted s 56(3)(b) | 1985-1986 | encoded | `sch para 11(3) s 56(3) the contract is a contract for the international sale of goods` |
| sch para 11, substituted s 56(3)(c) | 1988-1991 | encoded | `sch para 11(3) s 56(3) the contract is a contract for the international sale of goods` |
| sch para 12 | 1993-1997 | encoded | `sch para 12 the activity is a business`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1993. |
| sch para 13 | 1999-2004 | encoded | `sch para 13 the definition of business in section 61(1) applies to the contract`; lines not quoted (heading, marginal note or amendment tag; reason 1): 1999. |
| leg: heading and disclaimer (not part of the Act) | 2005-2009 | inert (reason 1) | heading and the statement that the Legislative History "is not part of the Act" |
| leg history item 1: U.K. 1979, c. 54 | 2011-2021 | fork | F6; the application date in the history is not part of the Act and s 1(1) alone governs the dates (reading taken); rule: `s 1(1) this Act applies to the contract of sale of goods` |
| leg history item 2: 1994 Revised Edition | 2023-2025 | inert (reason 2) | revised-edition record (machinery: amendment history) |
| leg history item 3: Act 43 of 1996 | 2027-2035 | inert (reason 2) | amending-Act record, commencement 1 January 1997 (machinery: amendment history) |
| leg history item 4: 1999 Revised Edition | 2037-2039 | inert (reason 2) | revised-edition record (machinery: amendment history) |
| leg history item 5: Act 4 of 2014 | 2041-2050 | inert (reason 2) | amending-Act record (machinery: amendment history) |
| leg history item 6: 2020 Revised Edition | 2052-2054 | inert (reason 2) | revised-edition record (machinery: amendment history) |
| leg history item 7: Act 25 of 2021 | 2056-2065 | inert (reason 2) | amending-Act record, in force 1 April 2022 (machinery: amendment history) |
| abbreviations: heading | 2067 | inert (reason 1) | heading of a key to the Legislative History |
| abbreviation row at line 2069 | 2069 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2071 | 2071-2072 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2073 | 2073 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2075 | 2075 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2077 | 2077 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2079 | 2079 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2081 | 2081-2083 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2085 | 2085 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2087 | 2087 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2089 | 2089 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2091 | 2091-2092 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2094 | 2094-2096 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| comparative table: heading and explanation | 2097-2102 | inert (reason 1) | heading and explanation of a renumbering aid |
| comparative table: column heads | 2104 | inert (reason 1) | column heads of a renumbering aid |
| comparative table row 1 | 2105 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| comparative table row 2 | 2106-2107 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| comparative table row 3 | 2108 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| comparative table row 4 | 2109-2110 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| comparative table row 5 | 2111-2115 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| defined term "sale" (within s 2(4)) | 223-224 | encoded | `s 2(4) the contract is called a sale` |
| defined term "agreement to sell" (within s 2(5)) | 226-228 | encoded | `s 2(5) the contract is called an agreement to sell` |
| defined term "conditional (contract of sale)" (within s 2(3)) | 221 | encoded | `s 2(3) the contract of sale is absolute or conditional` |
| defined term "necessaries" (within s 3(3)) | 243-248 | encoded | `s 3(3) the goods are necessaries` |
| defined term "existing goods and future goods" (within s 5(1)) | 261-268 | encoded | `s 5(1) the goods are future goods` |
| defined term "month (calendar month)" (within s 10(3)) | 331-332 | encoded | `s 10(3) a month in a contract of sale means a calendar month` |
| defined term "satisfactory quality" (within s 14(2A)) | 450-453 | encoded | `s 14(2A) the goods are of satisfactory quality` |
| defined term "aspects of quality" (within s 14(2B)) | 455-457 | encoded | `s 14(2B) the aspect is an aspect of the quality of the goods` |
| defined term "sale by sample" (within s 15(1)) | 517-522 | encoded | `s 15(1) the contract of sale is a contract for sale by sample` |
| defined term "undivided share" (within s 20A(3)) | 734-737 | encoded | `s 20A(3) the undivided share of the buyer in the bulk` |
| defined term "mercantile agent" (within s 26) | 844-848 | encoded | `s 26 the person is a mercantile agent for the purposes of ss 24 and 25` |
| defined term "commercial unit" (within s 35(7)) | 1052-1056 | encoded | `s 35(7) the unit is a commercial unit` |
| defined term "unpaid seller" (within s 38(1)) | 1112-1117 | encoded | `s 38(1) the seller of goods is an unpaid seller` |
| defined term "seller (for the purposes of Part 5)" (within s 38(2)) | 1126-1129 | encoded | `s 38(2) the person is a seller for the purposes of Part 5` |
| defined term "good faith" (within s 61(2)) | 1596-1598 | encoded | `s 61(2) the thing is deemed to be done in good faith` |
| defined term "insolvent" (within s 61(3)) | 1600-1602 | encoded | `s 61(3) the person is deemed to be insolvent` |
| defined term "deliverable state" (within s 61(4)) | 1604-1609 | encoded | `s 61(4) the goods are in a deliverable state` |
| defined term "deals as consumer" (within s 61(4A)) | 1611-1613 | encoded | `s 61(4A) the buyer deals as consumer` |
| defined term "merchantable quality" (within sch para 5, substituted s 14(6)) | 1746-1755 | encoded | `sch para 5 s 14(6) the goods are of merchantable quality` |
| defined term "consumer sale" (within sch para 9, substituted s 55(7)) | 1874-1876 | encoded | `sch para 9 s 55(7) the sale is a consumer sale` |
| defined term "contract for the international sale of goods (para 9)" (within sch para 9, substituted s 55(12)) | 1906-1916 | encoded | `sch para 9 s 55(12) the contract is a contract for the international sale of goods` |
| defined term "contract for the international sale of goods (para 11)" (within sch para 11, substituted s 56(3)) | 1974-1978 | encoded | `sch para 11(3) s 56(3) the contract is a contract for the international sale of goods` |

### Functions added on 2026-11-05

Every new function belongs to a row that already existed, so the total of 407 stays; the only change to the rows is the two dispositions moved to `fork` (see the Summary).
Each function below is the first of its row's rules unless the row's own first function is named above it.

| row | function added | module | why |
| --- | --- | --- | --- |
| s 2(4) | `s 2(4) the rule naming the contract a sale applies` | soga-part2-formation | yes/no twin of a function that returns a stage |
| s 2(5) | `s 2(5) the rule naming the contract an agreement to sell applies` | soga-part2-formation | yes/no twin |
| s 2(4) to (6) [G3] | `ss 2(4) to (6) a rule naming the stage of the contract applies` | soga-part2-formation | yes/no twin of the gather |
| s 3(2) | `s 3(2) the duty to pay a reasonable price for necessaries applies` | soga-part2-formation | yes/no twin of a function that returns an amount |
| s 5(3) | `s 5(3) the rule that a purported present sale of future goods operates as an agreement to sell applies` | soga-part2-formation | yes/no twin |
| s 8(2) | `s 8(2) the duty to pay a reasonable price applies` | soga-part2-formation | yes/no twin |
| s 9(1) | `s 9(1) the duty to pay a reasonable price for goods delivered and appropriated applies` | soga-part2-formation | yes/no twin |
| s 9(2) | `s 9(2) the action for damages against the party at fault applies` | soga-part2-formation | yes/no twin of a function that returns a party |
| s 17(1) | `s 17(1) the rule that the property passes when the parties intend applies` | soga-part3-effects | yes/no twin of a function that returns a date |
| s 20(2) | `s 20(2) the rule on delay through the fault of a party applies` | soga-part3-effects | yes/no twin of a function that returns a party |
| s 30(1) | `s 30(1) the duty to pay at the contract rate for a short delivery that is accepted applies` | soga-part4-performance | yes/no twin |
| s 30(3) | `s 30(3) the duty to pay at the contract rate for the whole of an excess that is accepted applies` | soga-part4-performance | yes/no twin |
| s 31(2) | `s 31(2) the question of repudiation or severable breach arises` | soga-part4-performance | yes/no twin of a function that returns an effect |
| s 37(1) | `s 37(1) the liability for neglect or refusal to take delivery applies` | soga-part4-performance | yes/no twin |
| s 46(4) | `s 46(4) the rule placing the expenses of re-delivery on the seller applies` | soga-part5-unpaid-seller | yes/no twin of a function that returns a party |
| s 48(4) | `s 48(4) the rescission is without prejudice to any claim the seller may have for damages` | soga-part5-unpaid-seller | the damages limb of the subsection had no function |
| s 50(3) | `s 50(3) the market-price rule for non-acceptance applies` | soga-part6-actions | yes/no twin |
| s 51(3) | `s 51(3) the market-price rule for non-delivery applies` | soga-part6-actions | yes/no twin |
| s 53(3) | `s 53(3) the rule for breach of warranty of quality applies` | soga-part6-actions | yes/no twin |
| s 14(2) with sch paras 5 and 6 [G8] | `s 14(2) by date: there is an implied condition that the goods supplied are of satisfactory quality` | soga-schedule | the printed s 14(2) had no date |
| s 61(1) "business" with sch paras 12 and 13 [G9] | `s 61(1) by date: the activity is a business` | soga-schedule | the definition took no date |
| s 18(b) | `s 18(b) Rule 2: the property cannot yet pass` | soga-part3-effects | the "until" bar as its own yes/no (fork F12, ruled 2026-11-05T06:04) |
| s 18(c) | `s 18(c) Rule 3: the property cannot yet pass` | soga-part3-effects | the "until" bar (fork F12, ruled) |
| s 29(4) | `s 29(4) delivery is not yet possible` | soga-part4-performance | the "until" bar (fork F12, ruled) |
| s 16 | `s 16 property in unascertained goods cannot yet be transferred` | soga-part3-effects | the same words, "unless and until" (fork F12, assumed, not ruled) |
| s 19(1) | `s 19(1) the property cannot yet pass because the right of disposal is reserved` | soga-part3-effects | the same words, "until" (fork F12, assumed, not ruled) |
| seat: s 8(1), s 10(2), s 14(1), s 30(3) | four seat questions, and ten yes/no companions of the value questions | soga-seat | the seat had skipped these provisions or could not answer "no" |
| seat: s 16, s 18 Rule 2, s 18 Rule 3, s 29(4) | four seat questions asking the bar; the s 19(1) question now answers through the bar | soga-seat | fork F12 |

### Rows left inert, with the reason

| row | disposition | why |
| --- | --- | --- |
| front: title and edition banner | inert (reason 1) | title and edition banner |
| front: arrangement of sections | inert (reason 1) | table of contents: a list of headings and section numbers |
| front: long title and date of enactment | inert (reason 1) | long title and the bracketed date; creates no rule |
| Part 1 heading | inert (reason 1) | Part heading |
| Part 2 heading | inert (reason 1) | Part heading |
| Part 3 heading | inert (reason 1) | Part heading |
| Part 4 heading | inert (reason 1) | Part heading |
| Part 5 heading | inert (reason 1) | Part heading |
| Part 6 heading | inert (reason 1) | Part heading |
| Part 7 heading | inert (reason 1) | Part heading |
| s 63 | inert (reason 2) | short title: machinery (the Act's own citation) |
| sch: title, section references and heading | inert (reason 1) | the Schedule's title and its list of the sections that refer to it; the references are operative in each section's own gate (ss 1(2), 11(5), 12(6), 13(4), 14(6), 15(3), 35(8), 55(3), 56 and 61(5)) |
| leg: heading and disclaimer (not part of the Act) | inert (reason 1) | heading and the statement that the Legislative History "is not part of the Act" |
| leg history item 2: 1994 Revised Edition | inert (reason 2) | revised-edition record (machinery: amendment history) |
| leg history item 3: Act 43 of 1996 | inert (reason 2) | amending-Act record, commencement 1 January 1997 (machinery: amendment history) |
| leg history item 4: 1999 Revised Edition | inert (reason 2) | revised-edition record (machinery: amendment history) |
| leg history item 5: Act 4 of 2014 | inert (reason 2) | amending-Act record (machinery: amendment history) |
| leg history item 6: 2020 Revised Edition | inert (reason 2) | revised-edition record (machinery: amendment history) |
| leg history item 7: Act 25 of 2021 | inert (reason 2) | amending-Act record, in force 1 April 2022 (machinery: amendment history) |
| abbreviations: heading | inert (reason 1) | heading of a key to the Legislative History |
| abbreviation row at line 2069 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2071 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2073 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2075 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2077 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2079 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2081 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2085 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2087 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2089 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2091 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| abbreviation row at line 2094 | inert (reason 1) | row of a key to abbreviations used in the Legislative History |
| comparative table: heading and explanation | inert (reason 1) | heading and explanation of a renumbering aid |
| comparative table: column heads | inert (reason 1) | column heads of a renumbering aid |
| comparative table row 1 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| comparative table row 2 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| comparative table row 3 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| comparative table row 4 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |
| comparative table row 5 | inert (reason 1) | row of a renumbering aid between the 1999 and 2020 Editions |

No row was moved out of `inert`: this is a fresh encoding and every row was first given its disposition by the rules of the brief.
Four rows had no rule when the script first mapped rules to rows, and none was left inert: each gained a rule and tests, because the brief does not allow "a rule with one answer" or an interpretive line as a reason.
They are s 35A(4) (`s 35A(4) section 35A applies to the contract`), the lead-in of s 61(1) (`s 61(1) the definitions of this section apply`), Schedule paragraph 1(2) (`sch para 1(2) what a reference in the Schedule refers to`) and the lead-in line of paragraph 11(3), line 1951, which is quoted by `sch para 11(3) s 56(1)...`.

## Fork register

Rulings of 2026-11-04 (bench `commons-negation-1030`), word for word from the brief, and the rulings of 2026-11-05 that followed:

- **E1.** Do not look for, or propose, a language construct that gathers a legal effect "by name" from every section that gives it. Where several sections give the same legal effect, encode each section's answer on its own (option C). You may, by hand and in plain L4, write one function that gathers the routes to a legal effect where that helps a reader (option B as guidance for hand-gathering only); say in the fork register where you did. The Magna Carta pilot is not to be run.
- **N2.** A flat negative in the text ("shall not", "is not", "no person") counts as the text's no, so the answer is `JUST FALSE`, and where the text names who bears a prohibition, the prohibition (`SHANT`) is derived from that answer. Do not type the Hohfeld kind into the person-facing answer. Record the kinds in `NOTES.md` under `## Jural relations`.
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**Where E1 option B was used (hand-gathering).** Each section's own answer is its own function (option C). The functions below combine those answers by hand, in plain L4, because a reader asks one question; they add no rule of their own.

| no. | function | what it gathers |
| --- | --- | --- |
| G1 | `s 1(2) this Act applies to the contract subject to the modification of the section mentioned in the Schedule` | the windows of the Schedule and ss 55(3), 56 and 61(5), by the section named |
| G2 | `sch para 1(1) the Schedule modifies this Act as it applies to the contract` | the windows of paragraphs 2 to 13 |
| G3 | `ss 2(4) to (6) the stage of the contract of sale` | ss 2(4), (5) and (6), which each name the contract |
| G4 | `ss 35(1) to (7) the buyer is deemed to have accepted the goods` | the routes to deemed acceptance in s 35(1), (2), (4) and (7); s 35(6), which says what is not acceptance by itself, is its own function |
| G5 | `ss 45(1) to (7) the goods are in course of transit` | the rules in s 45(1), (2), (3), (4) and (6) for when the goods are in course of transit and when the transit ends; s 45(5) and (7) are their own functions |
| G6 | `ss 49(1) and (2) the seller may maintain an action against the buyer for the price` | the two routes to the seller's action for the price |
| G8 | `s 14(2) by date: there is an implied condition that the goods supplied are of satisfactory quality` | in `soga-schedule.l4`: the date gates of paragraphs 5 and 6 (before 19 May 1985 the printed s 14(2) is replaced) with s 1(1) and `s 14(2)` |
| G9 | `s 61(1) by date: the activity is a business` | in `soga-schedule.l4`: s 1(1), paragraph 13 (the definition omitted before 18 May 1973), paragraph 12 (18 May 1973 to 31 January 1978) and `s 61(1) the activity is a business` |
| G7 | `route (E1 B) the buyer has the right to reject the goods`, `route (E1 B) the buyer may maintain an action against the seller for damages` | in `soga-routes.l4`: the routes in ss 12(1), 13(1), 14(2), 14(3), 15(2), 30 (rejection) and ss 51(1), 53(1)(b) (damages), with what stops them (ss 11(3), 15A(1), 53(1)) |

No construct that gathers an effect by name was looked for or proposed.
The seat (`soga-seat.l4`) calls the G7 functions for its two gathered questions; each section's own answer is asked by a separate question.

**Forks.** Each fork lists the readings seen, the text that licenses each, and the reading taken.
Where the ruling of 06:04 (the "Delegated definitions, defences and "until" bars" line) bears on this Act: (d) governs Rule 2, Rule 3 and s 29(4) (fork F12): the "has passed" and "there is delivery" functions stay `JUST FALSE` before X and `NOTHING` after, and the twins `s 18(b) Rule 2: the property cannot yet pass`, `s 18(c) Rule 3: the property cannot yet pass` and `s 29(4) delivery is not yet possible` carry the bar; (c) governs the "when" sites of fork F10; (a) and (b) fit no site in this Act: no definition in it is handed to a list in the words of (a) (the lists in s 61(1) are "includes" lists, which stay `NOTHING`), and no provision says "it is a defence ... to prove" (the burden rules in ss 15A(3), 30(2B) and 61(4B) say "it is for the seller to show" and stay as recorded in the section "Marginal readings for a lawyer").

**F1. s 10(3) where a period of calendar months ends.**
Readings: Reading (i): the period from 31 January for one month ends on the last day of February. Reading (ii): it ends on 1 March or 3 March (the day count rolls on). Reading (iii): the Act does not say.
Text: "In a contract of sale, “month” prima facie means calendar month." (s 10(3), lines 331-332). The Act says what a month is and not where a month ends when the later month has no corresponding day. The Interpretation Act 1965 is not among the sources (`inputs/DEPENDENCIES.md` lists a staged module for its period rules; this row did not open or use that module).
Taken: Reading (iii). `s 10(3) the date on which a period of calendar months ends` answers `NOTHING` when the later month has no corresponding day, and the corresponding date otherwise. Asserted (finding 5).

**F2. ss 50(3), 51(3), 53(3) the sign of "the difference".**
Readings: Reading (i): where the market price is above the contract price (s 50(3)) the measure is nil. Reading (ii): it is negative. Reading (iii): the Act does not say. Likewise s 51(3) when the market price is below the contract price, and s 53(3) when the goods were worth more than a conforming set.
Text: "the difference between the contract price and the market or current price" (ss 50(3), 51(3)); "the difference between the value of the goods at the time of delivery to the buyer and the value they would have had if they had fulfilled the warranty" (s 53(3)). The text does not sign the difference.
Taken: Reading (iii): `NOTHING` when the difference would be negative, and the difference (including nil) otherwise. Asserted (finding 6).

**F3. s 20A(3) and (6) a bulk that holds nothing; a nil price.**
Readings: The share is the proportion paid for out of the quantity in the bulk; with a bulk of nil, or part payment of a nil price, the proportion is undefined.
Text: "such share as the quantity of goods paid for and due to the buyer out of the bulk bears to the quantity of goods in the bulk at that time" (s 20A(3), lines 735-737); "payment of part of the price for any goods shall be treated as payment for a corresponding part of the goods" (s 20A(6), lines 750-752).
Taken: `NOTHING` when the divisor is nil. Asserted (finding 7).

**F4. s 61(1) "unless the context otherwise requires".**
Readings: Reading (i): every defined term carries a flag for the context. Reading (ii): one lead-in function answers whether the definitions apply, and the caller consults it.
Text: "In this Act, unless the context otherwise requires —" (s 61(1), line 1519). The text does not say how a context is found.
Taken: Reading (ii). `s 61(1) the definitions of this section apply` takes the person's fact `the context otherwise requires` and answers `JUST FALSE` when it is true (marginal reading (a)); no definition function takes the flag. Asserted (soga-cases-interpretation.l4).

**F5. Schedule paragraph 1(3) and the gates with no floor of their own.**
Readings: Reading (i): each gate answers on its own words; a contract made before 1 January 1894 is within the window "made before 22 April 1967" or "before 18 May 1973" because no gate has a lower bound. Reading (ii): paragraph 1(3) is read into every gate.
Text: "Nothing in this Schedule affects a contract made before 1 January 1894." (para 1(3)); "made before 18 May 1973" (ss 12(6), 13(4), 15(3), paras 3, 4, 6, 10, 13).
Taken: Reading (i) for each gate and para 1(3) as its own function; `s 1(2)` (G1) applies the floor for the person. Asserted (finding 3).

**F6. s 1(1) against the Legislative History's application date.**
Readings: Reading (i): the Act applies to contracts made on or after 1 January 1894 (s 1(1)). Reading (ii): it applies in Singapore only from 12 November 1993, the "Application" date in the Legislative History, so an earlier contract is outside it.
Text: "This Act applies to contracts of sale of goods made on or after (but not to those made before) 1 January 1894." (s 1(1)); the History: "Application : 12 November 1993 (except sections 22 and 25(2))" and "It is not part of the Act".
Taken: Reading (i). The History is not part of the Act, and it dates when the Act began to apply in Singapore, not the contracts it governs; the Application of English Law Act 1993 is not among the sources. Asserted (finding 4).

**F7. ss 15(3) and 35(8) point at deleted paragraphs 7 and 8.**
Readings: Reading (i): the subsection says in its own words when "paragraph 7" (or "paragraph 8") applies, so the gate answers `JUST TRUE` inside its window and, by ruling (a) of 2026-11-05, `JUST FALSE` outside it. Reading (ii): the paragraph is deleted, so the subsection is spent and says nothing. Reading (iii): "subject to the modification" is read as no modification, because the deleted paragraph changes nothing, so sections 15 and 35 apply unmodified and `s 1(4) this Act applies in relation to the contract without modification of the section` would answer `JUST TRUE` for them.
Text: "Paragraph 7 of the Schedule applies in relation to a contract made before 18 May 1973." (s 15(3)); "Paragraph 8 ... before 22 April 1967." (s 35(8)); paragraphs 7 and 8: "[Deleted by Act 43 of 1996]".
Taken: Reading (i): the gate says that the paragraph applies, and the text then says nothing about what it did, so nothing further is derived. Reading (iii) is the one rejected for the s 1(4) function: s 1(4) turns on whether the section "does not contain such a reference", and ss 15(3) and 35(8) still contain one, so `s 1(4)` answers `JUST FALSE` for sections 15 and 35 (ruling (b)); what the deleted paragraph would have changed is not in the text. Reading (ii) is rejected because the two subsections are still printed in this consolidation. Asserted (finding 9).

**F8. s 14 for contracts made on or after 19 May 1985.**
Readings: Reading (i): the section as printed (satisfactory quality) governs every contract made on or after 19 May 1985, because the Schedule's windows for s 14 end there. Reading (ii): a later amending Act limits it to later contracts (the History records Act 43 of 1996 in force from 1 January 1997).
Text: "Paragraph 5 ... made on or after 18 May 1973 and before 19 May 1985, and paragraph 6 ... before 18 May 1973." (s 14(6)); the History, item 3. This consolidation has no window for the later date.
Taken: Reading (i), because it is what the text says; reading (ii) needs sources outside this row. Gates asserted (finding 10). `s 14(2) by date` (added 2026-11-05) answers `JUST FALSE` before 19 May 1985 (the substituted section governs) and the printed `s 14(2)` from that day on (finding 11).

**F9. s 14(2C) the matters the implied condition does not extend to.**
Readings: Reading (i): s 14(2) is the general rule and (2C) takes out three matters, so for any matter that is none of the three the condition does extend. Reading (ii): (2C) only subtracts and says nothing about any other matter.
Text: "The condition implied by subsection (2) does not extend to any matter making the quality of goods unsatisfactory — (a) which is specifically drawn to the buyer’s attention before the contract is made; (b) where the buyer examines the goods before the contract is made, which that examination ought to reveal; or (c) in the case of a contract for sale by sample, which would have been apparent on a reasonable examination of the sample." (s 14(2C), lines 470-481).
Taken: Reading (i) (assumed, not ruled): `s 14(2C) the condition implied by s 14(2) extends to the matter making the quality unsatisfactory` answers `JUST FALSE` when one of the three is met and `JUST TRUE` otherwise. Reading (ii) is the one rejected; it was the reading before the revision of 2026-11-05 (the function answered `NOTHING`). Asserted (soga-cases-part2.l4).

**F10. "when", "upon" and "whenever" (ruled 2026-11-05T06:04) and "while", "in the case of", "in any other case" and "on the claimant's application" (assumed, not ruled), read as "where".**
Readings: Reading (i): the word introduces one condition on which a right, a duty or a deeming depends, so a case that does not meet it is `JUST FALSE`, as ruling (b) says for "where". Reading (ii): the word names an occasion or a time and says nothing about other occasions, so the answer is `NOTHING`.
Text: the sites below, each quoted in the comment on its branch.
Taken: Reading (i) throughout.
Ruled (Meng, typed 2026-11-05T06:04:54.553Z, the fork-register line "Delegated definitions, defences and "until" bars", item (c): "when", "upon" and "whenever" count as "where"). The sites where "when" is read as "where": s 2(6) ("when the time elapses"); s 18 Rule 1 ("when the contract is made", the date from which the rule runs); Rule 4 ("When goods are delivered ... on approval"); s 23 ("When the seller of goods has a voidable title"); s 34 ("when the seller tenders delivery", "on request"); s 35(4) ("when after the lapse of a reasonable time"); s 37(1) ("When the seller is ready and willing"); s 44 ("when the buyer of goods becomes insolvent"); s 46(4) ("When notice of stoppage"); s 57(2) ("complete when the auctioneer announces"); s 61(2) ("when it is in fact done honestly"); s 61(4) ("when they are in such a state"). Neither "upon" nor "whenever" occurs in lines 186-2003 of the text (checked by a search of those lines), so the ruling reaches "when" only.
Assumed, not ruled (words the ruling does not name): s 15(2) and its two limbs ("In the case of a contract for sale by sample"); s 39(1)(a) ("while he is in possession"); s 39(1)(b) ("in case of the insolvency of the buyer"); s 52(1) ("on the claimant's application"); s 53(3) ("In the case of breach of warranty of quality"); s 55(4) and the Schedule copies of the same words ("in the case of a consumer sale", "in any other case"). Each comment on those branches says "assumed, not ruled; fork F10".
Reading (ii) is kept where the word introduces one of several listed occasions and the list has no "only": s 35(1) (two occasions of acceptance) and s 43(1) (three occasions of loss of the lien) stay `NOTHING` under ruling (c) of the periods line. The ruling that "when" counts as "where" does not say whether a list of alternative "when" occasions is exhaustive, so those two were left as they were.

**F11. s 48(3) whether the buyer's non-payment governs the perishable limb.**
Readings: Reading (i): "and the buyer does not within a reasonable time pay or tender the price" governs both "Where the goods are of a perishable nature" and "where the unpaid seller gives notice", so perishability alone does not permit the re-sale. Reading (ii): it governs only the notice limb, so perishability alone does.
Text: "Where the goods are of a perishable nature, or where the unpaid seller gives notice to the buyer of his intention to re-sell, and the buyer does not within a reasonable time pay or tender the price, the unpaid seller may re-sell the goods and recover from the original buyer damages for any loss occasioned by his breach of contract." (s 48(3), lines 1317-1321). The comma before "and" separates the non-payment clause from the second "where".
Taken: Reading (i) (assumed, not ruled): `(perishable OR notice) AND non-payment` is `JUST TRUE`, and every other case is `JUST FALSE` (ruling (b)). Reading (ii) is the one rejected; it was the reading before the revision of 2026-11-05. Asserted (soga-cases-part5.l4; the seat question `May the seller re-sell the goods and claim damages` follows).

**F12. "does not pass until X" and "no delivery unless and until X": the bar (Rule 2, Rule 3, s 29(4); ruled 2026-11-05T06:04).**
Readings (before the ruling): Reading (i): the text states only when the property does not pass, or when there is no delivery, so once X has happened it is silent and "has it passed" is `NOTHING`. Reading (ii): once X has happened the positive follows and the answer is `JUST TRUE`.
Ruled (Meng, typed 2026-11-05T06:04:54.553Z, the fork-register line "Delegated definitions, defences and "until" bars", item (d)): encode the bar as its own yes/no function and never claim that the thing has happened. Reading (ii) is rejected.
Text: Rule 2: "the property does not pass until the thing is done and the buyer has notice that it has been done" (s 18(b), lines 600-604); Rule 3: "the property does not pass until the act or thing is done and the buyer has notice that it has been done" (s 18(c), lines 606-611); s 29(4): "there is no delivery by seller to buyer unless and until the third person acknowledges to the buyer that he holds the goods on his behalf" (lines 895-898).
Taken: each existing function is left exactly as it was (`s 18(b) Rule 2: the property in the goods has passed to the buyer`, `s 18(c) Rule 3: the property in the goods has passed to the buyer`, `s 29(4) there is delivery by the seller to the buyer`): `JUST FALSE` before X and `NOTHING` from X. A twin is added beside each:
- `s 18(b) Rule 2: the property cannot yet pass`, `s 18(c) Rule 3: the property cannot yet pass` and `s 29(4) delivery is not yet possible`.
- Each is `JUST TRUE` while the bar is in force (the rule applies and X has not happened by the date asked about), and `JUST FALSE` once X has happened.
- Each is `JUST FALSE` where the rule does not apply: the "Where ..." condition is unmet (ruling (b)), or, for Rules 2 and 3, "Unless a different intention appears" and one does (the rule of 2026-10-29).
- For Rules 2 and 3, X is "the thing is done and the buyer has notice that it has been done", both by the date asked about. For s 29(4), X is "the third person acknowledges to the buyer that he holds the goods on his behalf", taken as of the time asked about because the function it twins takes it as a yes/no.
- Seat: "Is the property still barred from passing to me ... (s 18, Rule 2)?", the same for Rule 3, and "Is delivery to me still not possible because a third person holds the goods (s 29(4))?" The questions "Has the property passed ..." are unchanged and answer through the original functions.
- Cases on both sides of X and where the rule does not apply are in `soga-cases-part3.l4`, `soga-cases-part4.l4` and `soga-cases-seat.l4`.
Applied to the same words, assumed, not ruled: s 16 ("no property in the goods is transferred to the buyer unless and until the goods are ascertained", lines 571-573) gets `s 16 property in unascertained goods cannot yet be transferred`, which answers `NOTHING` where s 20A applies ("Subject to section 20A"), as the function it twins does; s 19(1) ("the property in the goods does not pass to the buyer until the conditions imposed by the seller are fulfilled", lines 676-680) gets `s 19(1) the property cannot yet pass because the right of disposal is reserved`. Both are the ruling's own words ("the property does not pass until"); the brief named only Rule 2, Rule 3 and s 29(4), so these two are an extension to be confirmed. The seat question on s 16 has a bar beside it; the existing seat question on s 19(1) was repointed at the bar (see "Seat").
Not twinned: s 35(2) ("he is not deemed to have accepted them under subsection (1) until he has had a reasonable opportunity of examining them") is a bar on a deeming, and the gathered question `ss 35(1) to (7)` consumes its function, so it stays as it was. s 57(2) ("until the announcement is made any bidder may retract his bid") is a permission with a period: `s 57(2) any bidder may retract his bid` is `JUST TRUE` before the announcement and `JUST FALSE` from it (ruling (a)). An earlier version of this fork said s 19(3) and s 46(3) have the same shape; they do not, because neither has an "until" event (s 19(3): "if he wrongfully retains the bill of lading, the property in the goods does not pass to him"; s 46(3): "ineffective unless given at such time"), so they stay as they were.

**F13. s 12(2)(b) who "the owner" is.**
Readings: Reading (i): "the owner or other person entitled to the benefit of any charge or encumbrance so disclosed or known" is one phrase, so "the owner" is the owner of the charge or encumbrance. Reading (ii): "the owner" is the owner of the goods, so a disturbance by the owner of the goods is also outside the warranty.
Text: "(b) the buyer will enjoy quiet possession of the goods except so far as it may be disturbed by the owner or other person entitled to the benefit of any charge or encumbrance so disclosed or known." (s 12(2)(b), lines 382-389).
Taken: Reading (i) (assumed, not ruled): the input `the disturbance is by the owner of, or a person entitled to the benefit of, a charge or encumbrance disclosed or known to the buyer` carries it, and a disturbance within it answers `JUST FALSE`; any other disturbance answers `JUST TRUE`. Under reading (ii) a disturbance by the owner of the goods would answer `JUST FALSE` as well. This fork was cited in the comment on that branch as "fork F12" before the register had an entry for it; it is F13 here and the comment says so.

**Defaults followed from the Commons guide.** The Act alone; the actors the text names; a judgment the text hands to someone else is a conditional input and never guessed; the Act's own definitions are worked out from facts, borrowed terms are asked as facts; one case is the text's natural unit; the Act's own words, each with a plain gloss in a comment. **Departed from:** none.

**Derived prohibitions (N2).** Where the text names who bears a flat negative, the prohibition is derived from the `JUST FALSE`: s 57(4) (the seller must not bid or employ a bidder, and the auctioneer must not knowingly take a bid from the seller) is `SHANT` in `soga-duties.l4`, with the twin `s 57(4) it is lawful for the seller to bid himself or to employ any person to bid at the sale` and `s 57(4) it is lawful for the auctioneer to take any bid from the seller or any such person`. The other flat negatives name no bearer as such and stay `JUST FALSE`.

## Marginal readings for a lawyer

The brief's rule of 2026-10-29 left two readings to a lawyer. Reading (a): a failed "if" (and its plain variants "unless", "except") counts as the text's no, clause by clause. Reading (b): a grant or prohibition limited by its own wording does not.
Ruling (a), (b) and (c) of 2026-11-05 settles most of what reading (b) covered: a period the text fixes, a "where" condition ("when", "upon" and "whenever" count as "where" by the ruling typed at 06:04; "while", "in the case of" and "in any other case" are still assumed: fork F10) and a scope limit with no "only". What is listed below rests on a reading that ruling does not reach.
Each branch below rests on one of the two readings. For each, the other reading is stated and would turn the `JUST FALSE` into `NOTHING` (for a (b) row, the `NOTHING` into `JUST FALSE`).
The count of the FALSE-kind branches in layer 1 is 328. Of these, 188 rest on a ruling of 2026-11-05 (each comment says `ruled 2026-11-05 (x)`: 57 on (a) a period, 97 on (b) a "where" or "if" condition, 12 on "when", 1 on "while", 5 on "in the case of", 3 on a period and a condition together, 4 that follow the "implied" function, 4 that apply marginal reading (a) where it had been left out, 2 on an "until" bar that does not apply because a different intention appears, and 3 on an "until" bar that has ended); 65 are marked marginal (a) and are listed below with one marginal (b) row on a `NOTHING` branch; and the other 75 are definitions that say "means", flat negatives and instructions that rest on ruling N2 (2026-11-04) and not on a marginal reading, plus the two bar-ended arms of s 16 and s 19(1) (assumed, not ruled: fork F12).
The "until" rows below (s 16, Rule 2, Rule 3, s 19(1), s 29(4), s 35(2)) describe the function that says the property has passed, or the acceptance or delivery, and are unchanged. The bar twins of fork F12 answer the other question, "is it still barred?", and rest on no marginal reading.

| rule | reading | the branch and the other reading | module |
| --- | --- | --- | --- |
| `s 61(1) the definitions of this section apply` | (a) | "unless" is read as the text's no when the context otherwise requires. | soga-interpretation |
| `s 61(3) the person is deemed to be insolvent` | (a) | a failed "if" is read as the text's no; the other reading is that "if" gives a sufficient condition only. | soga-interpretation |
| `s 61(4B) the seller's claim that the buyer does not deal as consumer is made out` | (a) | a burden rule is read as the text's no when the seller has not shown it; the other reading is that the text says only who must show. | soga-interpretation |
| `s 2(1) the contract is a contract of sale of goods` | (a) | "is a contract by which" is read as a definition, like "means", so a contract lacking either limb is not a contract of sale of goods; the other reading is that the sentence only describes the usual case and is silent about the rest. | soga-part2-formation |
| `s 11(3) the breach of a condition can only be treated as a breach of warranty` | (a) | "Subject to" is read like "unless": when s 35A applies the "can only be treated as a breach of warranty" rule does not hold. | soga-part2-formation |
| `s 11(3) the breach of a condition can only be treated as a breach of warranty` | (a) | "unless" is read as the text's no when the express or implied term exists. | soga-part2-formation |
| `s 12(3) this subsection applies to the contract of sale` | (a) | the sentence defines the class of contracts to which the subsection applies, so a contract outside that class is outside it; the other reading is that a "case of which" clause is a "where" clause and a contract outside it leaves the subsection silent. | soga-part2-formation |
| `s 12(1) there is an implied condition that the seller has a right to sell the go...` | (a) | "other than" is read like "except": a contract to which s 12(3) applies has no implied condition under s 12(1); the other reading is that the exclusion limits the grant and the subsection is then silent (s 12(4) and (5) give that contract warranties instead). | soga-part2-formation |
| `s 12(2)(a) the implied warranty that the goods are free from an undisclosed char...` | (a) | a warranty whose content is met is read as the text's no to its breach. | soga-part2-formation |
| `s 12(2)(b) the implied warranty of quiet possession is broken` | (a) | a warranty whose content is met is read as the text's no to its breach. | soga-part2-formation |
| `s 12(4) the implied warranty that known charges have been disclosed is broken` | (a) | a warranty whose content is met is read as the text's no to its breach. | soga-part2-formation |
| `s 13(1) the implied condition that the goods will correspond with the descriptio...` | (a) | a condition whose content is met is read as the text's no to its breach. | soga-part2-formation |
| `s 14(2A) the goods are of satisfactory quality` | (a) | "if" is read as the definition of satisfactory quality, so goods that do not meet the standard are not of satisfactory quality; the other reading is that "if" gives a sufficient condition only and the text is silent about goods that do not meet it. | soga-part2-formation |
| `s 14(2) the implied condition of satisfactory quality is broken` | (a) | a condition whose content is met is read as the text's no to its breach. | soga-part2-formation |
| `s 14(3) there is an implied condition that the goods are reasonably fit for the ...` | (a) | "except where" is read as the text's no when the buyer does not rely or it is unreasonable to rely. | soga-part2-formation |
| `s 14(3) the implied condition of reasonable fitness is broken` | (a) | a condition whose content is met is read as the text's no to its breach. | soga-part2-formation |
| `s 14(5) the sale by the agent is treated as a sale by a principal in the course ...` | (a) | "except where" is read as the text's no for that case. | soga-part2-formation |
| `s 15(2)(a) the implied condition that the bulk will correspond with the sample i...` | (a) | a condition whose content is met is read as the text's no to its breach. | soga-part2-formation |
| `s 15(2)(b) the implied condition that the goods will be free from a defect not a...` | (a) | a condition whose content is met is read as the text's no to its breach. | soga-part2-formation |
| `s 15A(1) the breach is not treated as a breach of condition but may be treated a...` | (a) | "unless" is read as the text's no when a contrary intention appears. | soga-part2-formation |
| `s 15A(1) the breach is not treated as a breach of condition but may be treated a...` | (a) | "if the buyer does not deal as consumer" is read as a condition whose failure is the text's no. | soga-part2-formation |
| `s 15A(3) the breach is treated as one that fell within subsection (1)(b)` | (a) | a burden rule is read as the text's no when the seller has not shown it; the other reading is that the text says only who must show, and is silent on the outcome of not showing. | soga-part2-formation |
| `s 16 property in unascertained goods is transferred to the buyer` | (a) | the no is the text's flat negative "unless and until", read as the text's no for the case before the event, inside the limit it sets; the other reading, (b), takes that limit in its own wording as making the branch NOTHING even before the event. | soga-part3-effects |
| `s 18 the following are rules for ascertaining the intention of the parties as to...` | (a) | "Unless" is read as the text's no when a different intention appears. | soga-part3-effects |
| `s 18(b) Rule 2: the property in the goods has passed to the buyer` | (a) | the no is the text's flat negative "until", read as the text's no for the case before the event, inside the limit it sets; the other reading, (b), takes that limit in its own wording as making the branch NOTHING even before the event. | soga-part3-effects |
| `s 18(c) Rule 3: the property in the goods has passed to the buyer` | (a) | the no is the text's flat negative "until", read as the text's no for the case before the event, inside the limit it sets; the other reading, (b), takes that limit in its own wording as making the branch NOTHING even before the event. | soga-part3-effects |
| `s 19(1) the property in the goods passes to the buyer` | (a) | the no is the text's flat negative "until", read as the text's no for the case before the event, inside the limit it sets; the other reading, (b), takes that limit in its own wording as making the branch NOTHING even before the event. | soga-part3-effects |
| `s 20A(1) section 20A applies to the contract` | (a) | "if the following conditions are met" is read as the text's no when a condition is not met; the other reading is that "if" gives a sufficient condition only. | soga-part3-effects |
| `s 20A(2) property in an undivided share in the bulk is transferred to the buyer ...` | (a) | "unless" is read as the text's no when the parties agree otherwise. | soga-part3-effects |
| `s 23 the buyer acquires a good title to the goods` | (a) | "provided" is read as a condition whose failure is the text's no. | soga-part3-effects |
| `s 28 delivery of the goods and payment of the price are concurrent conditions` | (a) | "Unless otherwise agreed" is read as the text's no when the parties have agreed otherwise. | soga-part4-performance |
| `s 28 the seller must be ready and willing to give possession of the goods to the...` | (a) | "Unless otherwise agreed" is read as the text's no when the parties have agreed otherwise. | soga-part4-performance |
| `s 28 the buyer must be ready and willing to pay the price in exchange for posses...` | (a) | "Unless otherwise agreed" is read as the text's no when the parties have agreed otherwise. | soga-part4-performance |
| `s 29(4) there is delivery by the seller to the buyer` | (a) | the no is the text's flat negative "unless and until", read as the text's no for the case before the event, inside the limit it sets; the other reading, (b), takes that limit in its own wording as making the branch NOTHING even before the event. | soga-part4-performance |
| `s 29(5) the demand or tender of delivery may be treated as ineffectual` | (a) | "unless made at a reasonable hour" is read as the text's no when it is made at a reasonable hour. | soga-part4-performance |
| `s 30(2B) the shortfall or excess is treated as one that fell within subsection (...` | (a) | a burden rule is read as the text's no when the seller has not shown it; the other reading is that the text says only who must show. | soga-part4-performance |
| `s 31(1) the buyer is bound to accept delivery of the goods by instalments` | (a) | a failed "Unless otherwise agreed" is read as the text's no; the other reading is that "Unless otherwise agreed" states an exception only and the text is silent when it fails. | soga-part4-performance |
| `s 32(2) the seller must make such contract with the carrier on behalf of the buy...` | (a) | "Unless otherwise authorised by the buyer" is read as the text's no when the buyer has authorised otherwise. | soga-part4-performance |
| `s 32(3) the seller must give the buyer such notice as may enable him to insure t...` | (a) | "Unless otherwise agreed" is read as the text's no when the parties have agreed otherwise. | soga-part4-performance |
| `s 33 the buyer must take any risk of deterioration in the goods necessarily inci...` | (a) | "(unless otherwise agreed)" is read as the text's no when the parties have agreed otherwise. | soga-part4-performance |
| `s 34 the seller is bound to afford the buyer a reasonable opportunity of examini...` | (a) | "Unless otherwise agreed" is read as the text's no when the parties have agreed otherwise. | soga-part4-performance |
| `s 35(2) the buyer is deemed to have accepted the goods under subsection (1)` | (a) | the no is the text's flat negative "until", read as the text's no for the case before the event, inside the limit it sets; the other reading, (b), takes that limit in its own wording as making the branch NOTHING even before the event. | soga-part4-performance |
| `ss 35(1) to (7) the buyer is deemed to have accepted the goods` | (a) | the no is the text's flat negative "until", read as the text's no for the case before the event, inside the limit it sets; the other reading, (b), takes that limit in its own wording as making the branch NOTHING even before the event. | soga-part4-performance |
| `s 35A(3) the goods are affected by the breach` | (a) | "if" is read as the definition of "affected", so goods in conformity are not affected; the other reading is that "if" gives a sufficient condition only. | soga-part4-performance |
| `s 35A(4) section 35A applies to the contract` | (a) | "unless" is read as the text's no when a contrary intention appears. | soga-part4-performance |
| `s 38(1) the seller of goods is an unpaid seller` | (a) | the two "when" cases are read as the definition of "unpaid seller" within the meaning of the Act, so a seller in neither case is not an unpaid seller; the other reading is that "when" limits the grant and the text is silent about other sellers. | soga-part5-unpaid-seller |
| `s 42 the unpaid seller may exercise his lien or right of retention on the remain...` | (a) | "unless" is read as the text's no when the part delivery shows an agreement to waive. | soga-part5-unpaid-seller |
| `s 44 the unpaid seller may resume possession of the goods and retain them until ...` | (a) | "as long as" is read as the text's no once the goods are no longer in course of transit. | soga-part5-unpaid-seller |
| `s 45(1) the goods are deemed to be in course of transit` | (a) | "until" is read as the text's no once the buyer or his agent has taken delivery. | soga-part5-unpaid-seller |
| `s 45(7) the remainder of the goods may be stopped in transit` | (a) | "unless" is read as the text's no when the part delivery shows an agreement to give up possession of the whole. | soga-part5-unpaid-seller |
| `s 46(3) the notice is effective` | (a) | a failed "unless" is read as the text's no; the other reading is that "unless" states an exception only and the text is silent when it fails. | soga-part5-unpaid-seller |
| `s 47(2) the unpaid seller's right of lien or retention or stoppage in transit is...` | (a) | a failed "can only be exercised subject to" is read as the text's no; the other reading is that "can only be exercised subject to" states an exception only and the text is silent when it fails. | soga-part5-unpaid-seller |
| `s 55(2) an express condition or warranty negatives a condition or warranty impli...` | (a) | "unless" is read as the text's no when the express term is not inconsistent. | soga-part7-supplementary |
| `s 57(6) the seller, or any one person on his behalf, may bid at the auction` | (b) | "the seller or any one person" is read as a limited grant, not as the text's no. | soga-part7-supplementary |
| `s 62(2) the rule of the common law applies to the contract` | (a) | a failed "except in so far as" is read as the text's no; the other reading is that "except in so far as" states an exception only and the text is silent when it fails. | soga-part7-supplementary |
| `sch para 3 s 12(a) there is an implied condition that the seller has a right to ...` | (a) | "unless" is read as the text's no when the circumstances show a different intention. | soga-schedule |
| `sch para 3 s 12(b) there is an implied warranty that the buyer will have and enj...` | (a) | "unless" is read as the text's no when the circumstances show a different intention. | soga-schedule |
| `sch para 3 s 12(c) there is an implied warranty that the goods will be free from...` | (a) | "unless" is read as the text's no when the circumstances show a different intention. | soga-schedule |
| `sch para 5 s 14(2) the implied condition of merchantable quality is broken` | (a) | "except that there is no such condition" is read as the text's no, so there is no breach as regards those defects. | soga-schedule |
| `sch para 5 s 14(3) there is an implied condition that the goods supplied are rea...` | (a) | "except where" is read as the text's no when the circumstances show non-reliance. | soga-schedule |
| `sch para 5 s 14(5) the sale by the agent is treated as a sale by a principal in ...` | (a) | "except where" is read as the text's no when the exception is met. | soga-schedule |
| `sch para 5 s 14(6) the goods are of merchantable quality` | (a) | "if" is read as the definition of merchantable quality; the other reading is that "if" gives a sufficient condition only. | soga-schedule |
| `sch para 6 s 14(5) an express condition or warranty negatives a condition or war...` | (a) | "unless" is read as the text's no when the express term is not inconsistent. | soga-schedule |
| `sch para 9 s 55(2) an express condition or warranty negatives a condition or war...` | (a) | "unless" is read as the text's no when the express term is not inconsistent. | soga-schedule |
| `sch para 9 s 55(8) the sale falls to be treated as not being a consumer sale` | (a) | a burden rule is read as the text's no when the party has not proved it; the other reading is that the text says only who must prove. | soga-schedule |
| `sch para 9 s 55(9) the term is a term exempting from the provisions of the secti...` | (a) | "is a reference to" is read as "means"; the other reading is that it names a sufficient kind of term only. | soga-schedule |

## Findings: what the text turns out to say

1. An unbracketed `NOT` covers everything to its right in the main binary: `NOT a OR b` is `NOT (a OR b)`. The run exits 0 with no message. Every `NOT` in layer 1 is bracketed. The unstable build refuses that spelling at check, so soga-cases-findings.l4 does not carry it: its four probe functions write the reading main gives with brackets, `NOT (a OR b)` and `NOT (a AND b)`, beside `(NOT a) OR b` and `(NOT a) AND b`, and assert what each answers on `TRUE TRUE` and `TRUE FALSE` inputs. They do not assert how a build parses the unbracketed text.

2. `Date d m y` rolls an impossible day or month forward with no error: `Date 31 2 2025` is 3 March 2025, `Date 15 14 2025` is February 2026. Asserted (soga-cases-findings.l4: `DATE_DAY (Date 31 2 2025) EQUALS 3` and three more).

3. The Schedule's gates for paragraphs 2 to 4, 6, 10 and 13 have no lower bound, so each answers `JUST TRUE` for a contract made before 1 January 1894; only paragraph 1(3) (and s 1(1)) take such a contract out, and `s 1(2)` applies that. Asserted (soga-cases-findings.l4 (`31 12 1893`)).

4. The Legislative History says the Act was applied in Singapore on 12 November 1993, but it is "not part of the Act" and s 1(1) alone gives the dates: a contract made on 11 November 1993, 12 November 1993 or 1 January 1894 is within the Act. Asserted (soga-cases-findings.l4 (s 1(1) on those three dates)).

5. The Act says what a month is (s 10(3)) but not where a period of months ends when the later month has no corresponding day; 31 January plus one month is `NOTHING`, and 15 January plus two months is 15 March. Asserted (soga-cases-part2.l4).

6. The Act does not sign "the difference" in ss 50(3), 51(3) and 53(3). A market price above the contract price (s 50(3)) gives `NOTHING`; an equal price gives nil. Asserted (soga-cases-part6.l4 (`1000 1100`, `1000 950`, `1100 1000` and the equal cases)).

7. A bulk of nil (s 20A(3)) or a nil price (s 20A(6)) gives `NOTHING`: the Act fixes a proportion and does not say what it is of nothing. Asserted (soga-cases-part3.l4 (`30 0`, `40 25 0`)).

8. Section 22 shows "[Not applicable]" and section 25 has no subsection (2) in this text, which matches the Legislative History's "except sections 22 and 25(2)". Neither is encoded, since there is nothing to encode. Not asserted: there is no rule to assert: s 22 is blank, and s 25 simply has no subsection (2).

9. Sections 15(3) and 35(8) still point at paragraphs 7 and 8 of the Schedule, which are deleted. Each gate is encoded as the subsection words it: `JUST TRUE` inside the window, `JUST FALSE` on the cut-off day and after (ruling (a) of 2026-11-05; the gate answered `NOTHING` there before). Asserted (soga-cases-schedule.l4 (`17 5 1973`, `18 5 1973`, `21 4 1967`, `22 4 1967`)).

10. The windows for paragraphs 5 and 6 meet without a gap: a contract made on 17 May 1973 is within paragraph 6 and not paragraph 5, and one made on 18 May 1973 is within paragraph 5; paragraph 5 ends on 18 May 1985 inclusive. Asserted (soga-cases-schedule.l4 (`17 5 1973`, `18 5 1973`, `18 5 1985`, `19 5 1985`)).

11. This consolidation gives the Schedule's two windows for s 14 and nothing between 19 May 1985 and the consolidation: it does not say whether "satisfactory quality" applies to a contract made, say, in 1990. The Legislative History records an amending Act (Act 43 of 1996) in force from 1 January 1997, and the Act's own text does not link it to s 14. Not asserted: the gap is silence in the text, so no case can assert it; what is asserted is that the s 14(6) gates end on 18 May 1985 (finding 10) and, under reading (i) of fork F8, that `s 14(2) by date` answers `JUST FALSE` for a contract made before 19 May 1985 and the printed `s 14(2)` from that day (soga-cases-schedule.l4).

12. Process note, not a finding about the Act: on the first run of `soga-cases-seat.l4` (before the revision of 2026-11-05), 4 of 219 seat assertions failed (the count of `assertion failed` lines was 8 because each failure prints twice). All four were hand-written expectations of mine that were wrong (s 12(2)(a) with a charge disclosed to the buyer; s 15(2)(b) with a defect that would be apparent on examination; s 15A(1) for a consumer and for a contrary intention). I re-read ss 12(2)(a), 15(2)(b) and 15A(1)-(2) and the layer-1 case files, which were written from the text, and changed only those expectations; the layer-1 rules were not changed. All 219 passed after that.

13. Eighteen decision functions return a number, a party or a stage (ss 2(4), 2(5), 3(2), 5(3), 8(2), 9(1), 9(2), 17(1), 20(2), 30(1), 30(3), 31(2), 37(1), 46(4), 50(3), 51(3), 53(3) and the gather of ss 2(4) to (6)). Such a function cannot say `JUST FALSE`, so each has a yes/no twin named `... applies` (or `... arises`) that does. Asserted in the Part's case file; the value function still answers `NOTHING` where the twin answers `JUST FALSE`.

14. Three seat questions returned the rule's value, not the answer to the question as worded: "Am I barred from rejecting a slight shortfall or excess" (s 30(2A)) returned the "may reject" value, and "If I accept some of the goods may I still reject the rest" (s 35A(1)) returned the "loses the right" value. The first two now go through `the Act's answer to the opposite question`. Asserted in soga-cases-seat.l4 (a non-consumer with a slight shortfall is barred: `JUST TRUE`; the buyer who accepts some goods may still reject the rest: `JUST TRUE`). A third was found while adding the "until" bars: "Does the seller keep the property because he reserved the right of disposal" (s 19(1)) returned the "property passes" value (`JUST FALSE` while the seller kept it); it now calls the s 19(1) bar (fork F12) and its case asserts `JUST TRUE` for a reserved right whose conditions are not fulfilled.

## What the text does not answer

The first six of these are `NOTHING` in the encoding, each with a case that asserts it in the case file for its Part; the last two are gaps in the text, which no case can assert.
- Where the delivery of goods is to be made when the contract fixes a place: s 29(1), (2) leave it to the contract ("depending in each case on the contract").
- Whether a stipulation is a condition or a warranty (s 11(2)), whether time is of the essence beyond payment (s 10(2)), whether a breach is a repudiation (s 31(2)), whether the master holds as carrier or as agent (s 45(5)): each "depends on the terms" or "the circumstances", and the person states the answer.
- Where a period of calendar months ends when the later month has no such day (finding 5); the sign of the measure of damages (finding 6); a nil bulk or a nil price (finding 7).
- Anything the text hands to another Act, the general law or a court: capacity (s 3(1)), "any other enactment" (ss 4(1), 14(1), 39(1)), the Unfair Contract Terms Act 1977 (ss 55(1), 61(4A)), the Factors Act 1889 (s 61(1) "document of title to goods").
- What follows when a scope limit with no "only" is not met (ruling (c) of 2026-11-05): for example ss 2(2), 4(2), 5(2), 13(2), 13(3), 20(3), 20B and 62(1) to (2). The answer is `NOTHING`. (s 12(1) for a contract to which s 12(3) applies is not in this list: it answers `JUST FALSE`, marginal reading (a), "other than" read like "except"; whether "other than" is a no or a scope limit is an open question.)
- Whether the property has passed (Rules 2 and 3, ss 16 and 19(1)), or there is delivery (s 29(4)), once the "until" event has happened: those functions answer `NOTHING` from the event on, and the bar functions answer `JUST FALSE` (fork F12, ruled 2026-11-05).
- Whether s 14 as printed governs every contract from 19 May 1985 (finding 11), and what paragraphs 7 and 8 provided before they were deleted (finding 9).
- Whether the buyer has any remedy not listed in ss 12 to 15, 30, 51 and 53 (`route (E1 B) ...` answers `NOTHING` when no listed route applies; it is not a finding that none exists).

## What the main binary does not accept

Version tested: `l4-main-109` (1.6.109, sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb`) and `l4-main-108` (1.6.108), which read every module the same way (`check.sh`, "main" columns).
**Silent failures (exit 0, no warning, a wrong answer) come first, because they are the ones that cost.**
1. **An unbracketed `NOT` covers everything to its right.** `NOT a OR b` is `NOT (a OR b)`, and `NOT a AND b` is `NOT (a AND b)`. Found when the test for `sch para 5 s 14(5)` failed with a wrong answer and no error; fixed by writing `(NOT a) OR b`. The probes of finding 1 write the wide reading with brackets, because the unstable build refuses the unbracketed spelling.
2. **`Date d m y` accepts any day and month number and rolls forward.** `Date 31 2 2025` is 3 March 2025 and `Date 15 14 2025` is 15 February 2026, with no error. Month arithmetic written as `Date d (m PLUS n) y` therefore gives a wrong date for 31 January plus one month. `s 10(3)` compares the day of the result with the day it started from and answers `NOTHING` when they differ. Asserted: finding 2.
3. **Two enum constructors with the same name in two imported modules** make the name unusable in the module that imports both, and the clash can sit unnoticed until a later module imports both (five clashes of `some other matter` and two of `a sale` were found this way and renamed). `work/dups.py` (not shipped) checks the import closure of the seat; 0 duplicates on the final run.
4. **`#TRACE` is not an assertion.** A `DEONTIC` value cannot be compared with `EQUALS` in `#ASSERT` (the brief says so; not re-tested here), so each regulative rule in `soga-duties.l4` has a decision-function twin in its Part module, and the twin is what is asserted. `check.sh` counts no assertion for `soga-duties.l4`, which is its row of zeros, not a defect.

**Loud failures (an error that teaches).**
5. A one-line `CONSIDER x WHEN y THEN z` is a parse error; `CONSIDER` and `WHEN` go on separate lines (seen early in this run; the error text was not kept).
6. `@ref` binds to the next syntax node. An `@ref` followed by a `DECLARE` before its rule, by a `§` heading, by a directive or by the end of a file is reported by `srcrefs.py` (the gate), not by `l4`. The generator in `work/` therefore puts every `DECLARE` above the quoted block.
7. Not used, because the brief rules them out and the main binary was not asked to accept them: `REFUSE`, `#ASSERT ... REFUSED`, `BECAUSE` outside `LEST BREACH ... BECAUSE`, `YMD`, `RULES EFFECTIVE DATE` and the temporal built-ins, sets, `EVERY`, `TYPICALLY`, section `GIVEN`.
8. `IMPORT` finds only modules in the importing file's own folder, so all modules and case files are flat and every file name begins `soga-`.

## What `check.sh` prints

Command: `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh` in this folder (target `main`, the default).
Baseline numbers it replaced: the run before the revision of 2026-11-05 (25 modules, 0 errors, 1324 satisfied, 0 failed, 0 refused, the same on both builds), and the run after the first pass of that day (1445 satisfied). The block below is the run after the "until" bars.
The main columns repeat the run with 1.6.108 (main, 2ae7c9b, 2026-11-02); every module has the same four counts on both builds.
`soga-duties.l4`, `soga-nouns.l4` and the other layer-1 modules show zeros because their assertions are in the case files, which import them; `soga-duties.l4` has only `#TRACE` illustrations.
No test is meant to fail: `expected_failed` in `check.sh` is empty and `encoding.json` lists no `expected_red`.

```text
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
soga-cases-findings.l4                         0        16       0        0         0 |      0        16       0        0  same
soga-cases-interpretation.l4                   0        83       0        0         0 |      0        83       0        0  same
soga-cases-part1.l4                            0        61       0        0         0 |      0        61       0        0  same
soga-cases-part2.l4                            0       233       0        0         0 |      0       233       0        0  same
soga-cases-part3.l4                            0       169       0        0         0 |      0       169       0        0  same
soga-cases-part4.l4                            0       152       0        0         0 |      0       152       0        0  same
soga-cases-part5.l4                            0       120       0        0         0 |      0       120       0        0  same
soga-cases-part6.l4                            0        70       0        0         0 |      0        70       0        0  same
soga-cases-part7.l4                            0        56       0        0         0 |      0        56       0        0  same
soga-cases-routes.l4                           0        19       0        0         0 |      0        19       0        0  same
soga-cases-schedule.l4                         0       238       0        0         0 |      0       238       0        0  same
soga-cases-seat.l4                             0       275       0        0         0 |      0       275       0        0  same
soga-duties.l4                                 0         0       0        0         0 |      0         0       0        0  same
soga-interpretation.l4                         0         0       0        0         0 |      0         0       0        0  same
soga-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
soga-part1-application.l4                      0         0       0        0         0 |      0         0       0        0  same
soga-part2-formation.l4                        0         0       0        0         0 |      0         0       0        0  same
soga-part3-effects.l4                          0         0       0        0         0 |      0         0       0        0  same
soga-part4-performance.l4                      0         0       0        0         0 |      0         0       0        0  same
soga-part5-unpaid-seller.l4                    0         0       0        0         0 |      0         0       0        0  same
soga-part6-actions.l4                          0         0       0        0         0 |      0         0       0        0  same
soga-part7-supplementary.l4                    0         0       0        0         0 |      0         0       0        0  same
soga-routes.l4                                 0         0       0        0         0 |      0         0       0        0  same
soga-schedule.l4                               0         0       0        0         0 |      0         0       0        0  same
soga-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
TOTAL (25 modules)                             0      1492       0        0           |      0      1492       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## What would need doing before this is worth relying on

1. **A lawyer has to read it against the official text.** The text it was written from is a converter's plain-text rendering of an informal consolidation, not the official text (see `SOURCE-LICENSE.md`); nothing here is "verified against the official text".
2. **The marginal readings need a ruling** (the section "Marginal readings for a lawyer"): every `JUST FALSE` there that rests on a failed "if", "unless" or "except" would become `NOTHING` on the other reading. Periods, "where" conditions and scope limits are ruled (2026-11-05), and so are "when", "upon" and "whenever" as "where" and the "until" bars (Rule 2, Rule 3, s 29(4)); the readings of "while", "in the case of", "in any other case" and "on the claimant's application" as "where" (fork F10), of s 14(2C) (F9), of s 48(3) (F11) and of the s 16 and s 19(1) bars (F12) are assumed, not ruled.
3. **The Hohfeld kinds in "Jural relations" are my reading** and have not been confirmed by a lawyer (N2: the kind is not typed into any answer).
4. **Borrowed terms are inputs and were not worked out**: dealing as consumer (Unfair Contract Terms Act 1977), documents of title (Factors Act 1889), capacity, bankruptcy rules, the common law and the law merchant, the Hire-Purchase Act 1965 (U.K.) in the Schedule, and "any other enactment". The person must state them; the "Dependencies" section lists each with its provisions and lines.
5. **Judgments the Act hands to the court are inputs**: a reasonable time, a reasonable price, a reasonable opportunity to examine, fault, good faith, whether a breach is so slight that rejection would be unreasonable.
6. **The windows of the Schedule are correct only if the contract date is.** "Made" is a fact about offer and acceptance that the person states as a date.
7. **Finding 11 (a gap from 19 May 1985 to the 1996 amendment) needs the Sale of Goods (Amendment) Act 1996 and its transitional provisions**, which are not among the sources.
8. **The seat questions have not been tried on a real buyer.** Their wording is the encoder's.
9. **The unstable dialect was not used for the main row** (see "Unstable dialect").

## Changes of 2026-11-05

The ruling of 2026-11-05 (fork register, beside E1 and N2) was applied across the Act, and the gaps found in an independent test pass were filled.
Layer-1 `NOTHING-kind` branches fell from 336 to 195 (194 after the first pass of the day; the s 16 bar adds one); 188 of the 328 `FALSE-kind` branches now say `ruled 2026-11-05 (x)` in their comment.
Every changed expectation in a case file was re-derived from the text and the ruling, then run; none was copied from the new output unread.

1. **Periods and "where" conditions, everywhere.** A period the text fixes in its own words now answers `JUST FALSE` outside it, and a "where" condition not met answers `JUST FALSE`; a scope limit with no "only" stays `NOTHING`. About 134 existing functions changed: Part 1 (`s 1(2)`, `s 1(4)`), Part 2 (ss 2(6), 6, 7, 9(1), 11(1), 11(3), 13(1), 14(2), 14(3), 15(1), 15(2), 15A(1) and the "broken" functions that follow them), Part 3 (Rules 1, 2's "where", 3's "where", 4, 5(i) to (iv), ss 19(2), 19(3), 20A(2), 23, 24, 25), Part 4 (ss 29(3), 30(1), 30(2), 31(2) twin only, 32(1) to (3), 33, 34, 35(4), 35(7), 36), Part 5 (ss 39, 41(1), 42, 44, 45(1) to (3), (6), (7), 46(4), 47(2), 48(2) to (4)), Part 6 (ss 49(1), 49(2), 50(1), 51(1), 52(1), 52(2), 53(1)(a), 53(1)(b)), Part 7 (ss 55(1), 55(3), 56, 57(1), 57(2), 59, 60), the interpretation module (s 61(2), 61(4), 61(5)) and the Schedule (the gates, the window of every paragraph, and the "where" conditions inside them). Eighteen functions that return an amount, a party, a date or a stage cannot say `JUST FALSE`, so each got a yes/no twin (finding 13) and the seat got ten companion questions. Forks F10 and F11 record the readings that are assumed, not ruled.
2. **Marginal reading (a) where it had been left out.** `s 12(2)(a)`, `s 12(2)(b)`, `s 12(5)` (the closed list in (c)) and `s 15(2)(b)` now answer `JUST FALSE` for the disclosed charge and the defect apparent on the sample. `s 14(2C)` answers `JUST TRUE` for a matter none of its three exclusions covers (fork F9).
3. **Seat.** A new question for s 14(1) (a private seller: `JUST FALSE`). `s 14(3) ... is broken` follows `s 14(3) ... implied` (a buyer who relied on their own engineer: `JUST FALSE` for both). The s 30(2A) and s 35A(1) questions answer as worded (`the Act's answer to the opposite question`), with cases that fail on the old wiring. The questions on s 44 and s 57(2) follow their rules. The acceptance question gained the two s 35(6) inputs.
4. **s 61(1) "goods".** `a thing in action` and `money` answer `JUST FALSE`; the rest of the "includes" definition stays `NOTHING`.
5. **ss 15(3) and 35(8).** Fork F7 now records three readings and the one taken.
6. **Left as they were:** s 10(1), s 20(1), s 31(1), s 21(1), s 20B(1)(b), s 30(2A) for a consumer, s 35(3), s 35A(1)(b). Rule 2, Rule 3 and s 29(4) were first left as they were with a fork line each; the ruling typed at 06:04 replaced that (item 10).
7. **Gaps filled:** seat questions for s 8(1), s 10(2) and s 30(3); the s 35(6) inputs; `s 14(2) by date`; `s 48(4) the rescission is without prejudice to any claim the seller may have for damages`; `s 61(1) by date: the activity is a business` (paragraphs 12 and 13). No gap is left as a stated gap.
8. **How the files were changed:** the `.l4` files were edited directly in this revision; the generator and templates of the first pass (not shipped) are no longer in step with them, and the files are the artefact.
9. **Docs:** the ruling lines in the fork register, forks F7 and F9 to F13, the section "Dependencies" and a "dependencies" key in `encoding.json`.
10. **The "until" bars (ruled at 06:04, fork F12).** Three new yes/no functions: `s 18(b) Rule 2: the property cannot yet pass` and `s 18(c) Rule 3: the property cannot yet pass` (soga-part3-effects), `s 29(4) delivery is not yet possible` (soga-part4-performance). The "has passed" and "there is delivery" functions are unchanged. Two more on the same words, assumed, not ruled: `s 16 property in unascertained goods cannot yet be transferred` and `s 19(1) the property cannot yet pass because the right of disposal is reserved`. Four seat questions (s 16, Rule 2, Rule 3, s 29(4)) and 47 assertions (25 in `soga-cases-part3.l4`, 4 in `soga-cases-part4.l4`, 18 in `soga-cases-seat.l4`).
11. **"when", "upon" and "whenever" are ruled as "where"** (fork F10): the fourteen comments that said "assumed, not ruled" at the "when" sites now say ruled; the ten at "while", "in the case of", "in any other case" and "on the claimant's application" still say assumed.
12. **A seat question that was worded the wrong way round, found while adding the bars:** "Does the seller keep the property because he reserved the right of disposal (s 19(1))?" called the function that says the property passes, so it answered `JUST FALSE` (No) while the seller kept the property, and its case asserted that. It now calls the s 19(1) bar and answers Yes then, No after the conditions are fulfilled.
13. **A fork the register did not have:** the comment on `s 12(2)(b)` cited "fork F12" for the reading of "the owner", and no such fork was recorded (F12 is the "until" bar). It is now F13, in the register, and the comment cites F13.

## Dependencies

What the text borrows from outside itself, and what this row does with each.
Every entry is a **named input to fill later**: the encoding asks the person to state the fact, and it does not contain the other Act.
Nothing here is staged except the Interpretation Act 1965 modules, which this row did not use.

**The Interpretation Act 1965 (Singapore) modules staged in `inputs/DEPENDENCIES.md`: read the listing only; did not open or use either module.**
I read `inputs/DEPENDENCIES.md`, which lists `sgia-interpretation-time.l4` and `sgia-p1-definitions.l4`; I did not open either module and no layer-1 file imports them.
Nothing in this Act calls for them: the only period in the operative text is s 10(3) (lines 331-332), which defines "month" for a contract of sale as a calendar month by itself, and fork F1 answers `NOTHING` where the later month has no corresponding day; the text contains no period of days, weeks or years (checked by a search of lines 186-2003 for those words).

| Act or instrument | status | what this row takes as an input | provisions that borrow, with lines of `inputs/SGA1979.txt` | functions |
| --- | --- | --- | --- | --- |
| Unfair Contract Terms Act 1977 | not staged; named input; to fill later | whether the Act prevents the negativing or variation of an implied term; whether the buyer deals as consumer | s 55(1) (lines 1454-1458); s 61(4A) (1611-1613); the burden in s 61(4B) (1615-1616) | `s 55(1) the right, duty or liability may be negatived or varied` (input `the Unfair Contract Terms Act 1977 prevents the negativing or variation`); `s 61(4A) the buyer deals as consumer` (input `Part 1 of the Unfair Contract Terms Act 1977 says the buyer deals as consumer`); ss 15A(1), 30(2A), 35(3) take "deals as consumer" as a yes/no input |
| Factors Act 1889, the enactments enabling an apparent owner to dispose of goods, special common law or statutory powers of sale, and orders of a court of competent jurisdiction | not staged; named input; to fill later | whether a document is a document of title; which of these matters this Act leaves untouched | s 21(2)(a) and (b) (lines 798-806); s 61(1) "document of title to goods" (1558-1559) | `s 21(2) this Act affects the matter`; `s 61(1) the document is a document of title to goods` (input `the Factors Act 1889 treats the document as a document of title to goods`) |
| The enactments relating to bills of sale (not named in the text) | not staged; named input; to fill later | which matter s 62(3) leaves untouched | s 62(3) (lines 1635-1636) | `s 62(3) this Act affects the matter` |
| The rules in bankruptcy | not staged; named input; to fill later | whether the rules apply | s 62(1) (lines 1625-1626) | `s 62(1) the rules in bankruptcy relating to contracts of sale apply to the contract notwithstanding anything in this Act` |
| The common law, including the law merchant | not staged; named input; to fill later | whether a rule of the common law applies | s 62(2) (lines 1628-1633) | `s 62(2) the rule of the common law applies to the contract` |
| The general law of capacity to contract and to transfer and acquire property | not staged; named input; to fill later | whether the party has capacity | s 3(1) (lines 236-237) | `s 3(1) the party has capacity to buy and sell` |
| "Any other Act" and "any other enactment" | not staged; named input; to fill later | whether another enactment requires a form, provides an implied term, or takes a right away | s 4(1) (line 254); s 14(1) (442) and its Schedule copies (1712, 1774); s 39(1) (1132) | `s 4(1) a contract of sale may be made in this form`; `s 14(1) there is an implied condition or warranty about the quality or fitness of the goods`; `s 39(1)(a)`, `s 39(1)(b)`, `s 39(1)(c)`; `sch para 5 s 14(1)`, `sch para 6 s 14(1)` |
| Hire-Purchase Act 1965 (U.K. 1965, c. 66), s 58(3) and (5) | not staged; named input; to fill later | whether the person conducted "antecedent negotiations" | Schedule paragraph 5, substituted s 14(7) (lines 1757-1764) | `sch para 5 s 14(7) the reference to the seller in subsection (3) includes the person who conducted the antecedent negotiations` (input `the person conducted antecedent negotiations`) |
| Sale of Goods (Amendment) Act 1996 (Act 43 of 1996) | not staged; named in the text, not an input | nothing: the Act's own text says "[Deleted by Act 43 of 1996]" for Schedule paragraphs 7 and 8 and the Legislative History records the amendment | lines 1800-1801; 2027 | none; forks F7 and F8, finding 11 |
| Application of English Law Act 1993 | not staged; named in the Legislative History, which is not part of the Act | nothing | lines 2017-2020 | none; fork F6 |

## Unstable dialect

A second, unstable-dialect encoding of some of these provisions exists: the provisions that the Schedule changes according to the date a contract was made, a shape where the unstable dialect reads the rule-version axis directly and main needs the gate-and-modified-function workaround used in `soga-schedule.l4`.
It pairs with this row, it was written only after this row was complete and checked, and this row is complete without it.
A further unstable-dialect module, written the same way, models the rules on when the property in goods passes (section 18 Rules 1 to 5 and section 29(4)) as a trace of dated events on the state ledger, which main cannot read; this row asks the "until" bars of section 18 Rules 2 and 3 and of section 29(4) as plain functions (fork F12).
