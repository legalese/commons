# Forks — row `legalese`, Penal Code 1871

This register holds the structural choices the row made in the changes of 2026-09-21 (NOTES.md, "The 2026-09-21 changes"): a granularity, a factoring, a reading taken.
Each fork below rests on the Code's text.

**Five forks are genuine ambiguities in the text and are open for human review:** PC-2, PC-3, PC-4, PC-6 and PC-8.
The other seven are marked *presentation*: the text is not ambiguous there and the readings give the same answers, so review decides only how the encoding is laid out.
In every fork the reading taken, marked "Encoded now", stands until ruled.

Each fork gives its status, the provision, the readings, what each reading does to the encoding and its answers, and the reading encoded now, with the statutory reason for it.
The module headers carry the row's other interpretation calls beside the fixtures that make them; they are not repeated here.
The text is the subject's `registers/source-bundle/PC1871.txt`.
The row `legalese-whole-code` keeps its own registers in `../legalese-whole-code/notes/*-forks.md`; where it forked on the same words, the fork below says so.

## PC-1 — s 380: a defining section or a punishing one (presentation)

**Status:** presentation; open for human review as to layout only; the reading taken stands until ruled.
**Provision.** Heading: "Theft in dwelling house, etc."
"380. Whoever commits theft in any building, tent or vessel, which building, tent or vessel is used as a human dwelling, or for the custody of property, shall be punished with imprisonment for a term which may extend to 7 years, and shall also be liable to fine."
**Readings.** (A) s 380 is a punishing section that adds elements of its own to a theft, as ss 379A, 381 and 382 do. (B) s 380 defines an offence, theft in dwelling, whose first element is theft.
**Consequences.** Under (A) the decision is `offence under s 380` and there is no defining rule. Under (B) a `commits theft in dwelling` rule would be added and `offence under s 380` would call it.
Both readings require the same facts, so no answer and no charge text changes either way.
**Encoded now.** (A). s 378 is the only section in the group that says "is said to commit"; s 380 says only "shall be punished", and a charge is laid under the punishing section (CPC 2010 s 123(4)).
**The name.** The module calls the offence "theft in dwelling", a short form of the heading. The field names that carry it (`Theft in Dwelling Facts`, `theft in dwelling` on `Complaint`) stay as they are under either reading.

## PC-2 — s 380: does "used ... for the custody of property" reach a shop?

**Status:** open, for human review; the reading taken stands until ruled.
**Provision.** "in any building, tent or vessel, which building, tent or vessel is used as a human dwelling, or for the custody of property".
**Readings.** (A) Any building in which property is kept, goods kept for sale included, so a shop is within it. (B) Only a building whose use is storage (a warehouse, a store-room), so a shop open to the public is outside it, and a shop theft is s 379 alone.
**Consequences.** `for the custody of property` is an input, so the reading is not in a rule: it is carried by the leaf's `@desc` ("A shop is — goods are kept there") and by the shop fixtures, which answer it TRUE.
Under (A), `Tan Mei Ling, in the supermarket` makes out s 380, and `Tan Mei Ling's complaint` in `charge-sheet.l4` lists s 380 and s 379.
Under (B), the `@desc` changes and those fixtures answer FALSE; s 380 is then not made out on them and the complaint lists s 379 alone. No rule changes.
**Encoded now.** (A). The words are "custody of property", not "storage", and custody is keeping: a shop keeps its goods.
The section sets "custody of property" beside "a human dwelling" as one of two uses and limits neither by the purpose the property is kept for.
No case on the row's bench decides it.
**Not a fork: the two groups are in series.** "which building, tent or vessel" is an express co-reference, so the place and its use are asked of one locus, and a flat five-leaf conjunction is a wrong answer rather than a reading (NOTES.md, section 380).

## PC-3 — s 390(2): does "voluntarily" govern "attempts to cause"?

**Status:** open, for human review; the reading taken stands until ruled.
**Provision.** "the offender, for that end, voluntarily causes or attempts to cause to any person death, or hurt, ..."
**Readings.** (A) "voluntarily" stands before both verbs and governs both. (B) It governs "causes" only, and an attempt needs no adverb.
**Consequences.** Under (A) `voluntarily` is a leaf in series, followed by the choice of `causes` or `attempts to cause`. Under (B) the leaves would be `voluntarily causes` OR `attempts to cause`, as before 2026-09-21, and an involuntary attempt would satisfy s 390(2).
No fixture has `attempts to cause` TRUE, so no answer on the bench differs between the two; the field names do (`voluntarily causes` became `voluntarily` and `causes`, a breaking change for anything that supplies `Robbery Facts` by name).
**Encoded now.** (A). One adverb precedes two verbs joined by "or" that share one object list, and nothing in the subsection repeats or confines it.
**Same words, other row.** `legalese-whole-code` forks the same words as P-3 in `notes/property-forks.md` and takes (A).

## PC-4 — s 403: does "dishonestly" govern "converts to his own use"?

**Status:** open, for human review; the reading taken stands until ruled.
**Provision.** "403. Whoever dishonestly misappropriates or converts to his own use movable property, shall be punished ..."
**Readings.** (A) "dishonestly" governs both verbs. (B) It governs "misappropriates" only, and conversion needs no dishonesty.
**Consequences.** Under (A), `the umbrella sold before the mistake was discovered` (both act leaves TRUE, `dishonestly` FALSE) is not an offence. Under (B) it is; re-factoring the ladder to (B) turns two of the module's 21 assertions red (measured 2026-09-21, NOTES.md).
**Encoded now.** (A). The adverb stands before both verbs, which share one object. Where the Code wants a second adverb for a second pair of verbs it writes one: s 405 repeats "dishonestly" before "uses or disposes of". s 403 does not.

## PC-5 — s 403: no "commits" rule (presentation)

**Status:** presentation; open for human review as to layout only; the reading taken stands until ruled.
**Provision.** s 403 runs from "Whoever dishonestly misappropriates" straight to "shall be punished". It never says "is said to commit", as s 378 does, or "commits 'criminal breach of trust'", as s 405 does. Its heading is "Dishonest misappropriation of property".
**Readings.** (A) `offence under s 403` is itself the defining ladder, and no rule is named for the heading. (B) A wrapper rule named for the heading (`commits dishonest misappropriation`) is added and `offence under s 403` calls it.
**Consequences.** None to any answer: a wrapper draws as one box on the ladder and adds nothing. Under (B) the module exports three things rather than two.
**Encoded now.** (A). The enacting words name no offence; the heading is used only in the wording of the refusal.

## PC-6 — s 405: which adverb goes with which limb

**Status:** open, for human review; the reading taken stands until ruled.
**Provision.** "dishonestly misappropriates or converts to his own use that property, or dishonestly uses or disposes of that property in violation of ..., or intentionally suffers any other person to do so".
**Readings.** (A) "dishonestly" governs the first two limbs and "intentionally" the third, each with its own verbs. (B) The adverbs pool, so a charge may say "dishonestly and intentionally" of any limb relied on.
**Consequences.** The ladder is the same under both; the recital differs. Under (A), with the first and third limbs both TRUE, it reads "did dishonestly misappropriate the said furniture, and did intentionally suffer another person so to do in respect of the said furniture". Under (B) it read "did dishonestly and intentionally misappropriate, and suffer another person to misappropriate the said furniture", the form replaced on 2026-09-21 (NOTES.md, s 405); three of the module's assertions pin (A).
**Encoded now.** (A). Each adverb is written in front of its own verbs.
**A further question, part of the same review.** Whose dishonesty "to do so" carries on the third limb. This row's leaf is named with the anaphor intact, and its `@desc` says that answering TRUE asserts the other person's dishonesty. `legalese-whole-code` forks the question as P-22 and takes the same reading; it is open there for a ruling.

## PC-7 — s 390(2): "carrying away or attempting to carry away" as two leaves (presentation)

**Status:** presentation; open for human review as to layout only; the reading taken stands until ruled.
**Provision.** "in order to commit theft, or in committing the theft, or in carrying away or attempting to carry away property obtained by the theft".
**Readings.** (A) Four occasion leaves in parallel: the two gerunds of the last phrase are separate leaves. (B) Three leaves, the last phrase one leaf.
**Consequences.** None to any answer: the occasions are joined by "or", and an OR of three in which one member is an OR of two gives the same answers as an OR of four.
Under (A) a fixture can hold exactly one occasion TRUE, which the getaway fixtures do, and `projections/robbery-390-2.sentences` reads 48 ways; under (B) it reads 36, and the getaway fixtures would need rewriting to one leaf. One field became two under (A), a breaking change for anything that supplies `Robbery Facts` by name.
**Encoded now.** (A).

## PC-8 — s 408: one condition of capacity or two

**Status:** open, for human review; the reading taken stands until ruled.
**Provision.** "408.—(1) Whoever, being an employee, and being in any manner entrusted in such capacity with property, or with any dominion over property, commits criminal breach of trust in respect of that property ..."
**Readings.** (A) Two conditions: the accused is an employee, and the entrustment was made to him as an employee. (B) One: an employee who was entrusted, in whatever capacity.
**Consequences.** Under (A), `Carl Elias Moses, an employee but not entrusted as one` fails s 408 on the second leaf and still makes out s 406, and his complaint lists s 406 alone. Under (B) the second leaf goes, that fixture makes out s 408, and the complaint lists s 408 and s 406.
**Encoded now.** (A). "in such capacity" refers back to "being an employee" and qualifies the entrustment; on (B) the phrase does no work.

## PC-9 — s 409(1)(b) and (g): one leaf per alternative (presentation)

**Status:** presentation; open for human review as to layout only; the reading taken stands until ruled.
**Provision.** "(b) in the way of his trade, profession or business as a banker, a merchant, a factor, a broker, an attorney or an agent"; "(g) in his capacity as a key executive of a corporation, an unincorporated association or a partnership".
**Readings.** (A) One leaf per alternative: paragraph (b) is two lists in series, three leaves then six; paragraph (g) is `in his capacity as a key executive` then three leaves. (B) One BOOLEAN leaf per paragraph, with the alternative chosen named in a STRING particular and recited.
**Consequences.** None to any verdict: which alternative applies never decides whether the offence is made out, only whether some alternative in each list does. The recital and the facts record differ. `legalese-whole-code` takes (B) (its fork P-23) and gives the same verdicts.
**Encoded now.** (A).
**Not a fork: s 409(1)(c)'s carve-out.** "(other than by way of a trade, profession or business mentioned in paragraph (b))" is explicit; the leaf is named with it.

## PC-10 — s 392 restated as an implication (presentation)

**Status:** presentation; open for human review as to layout only; the reading taken stands until ruled.
**Provision.** "392. Whoever commits robbery shall be punished with ...; and if the robbery is committed after 7 p.m. and before 7 a.m., the offender shall be punished with ...".
**Readings.** (A) Keep `offence under s 392` as a `DECIDE … IF` and add, beside it, the section restated as `commits robbery` IMPLIES `liable under s 392`, so the ladder draws the liability as a consequent on the right. (B) The `DECIDE … IF` alone.
**Consequences.** None to any answer: nothing was replaced. (A) adds four decisions, eight assertions (three of which cannot fail; NOTES.md, s 392) and two projection figures; (B) removes them.
**Encoded now.** (A). A punishing section is one-way: "shall be punished" says nothing about who else may be so punished, and `IMPLIES` is the keyword that says so.
**A reading inside it, recorded before this register.** The `NOT` that makes the night limb displace the ordinary one is supplied, not read; `charge under s 392` makes the same call.

## PC-11 — ss 407 to 409 built on a nested s 405 record (presentation)

**Status:** presentation; open for human review as to layout only; the reading taken stands until ruled.
**Provision.** Each section states a capacity and then "commits criminal breach of trust in respect of such property" (s 407) or "in respect of that property" (ss 408, 409).
**Readings.** (A) `Aggravated CBT Facts` nests `breach of trust IS A CBT Facts`, and every rule ends in one call, `commits criminal breach of trust`. (B) Each rule restates s 405's elements over a flat record.
**Consequences.** None to any answer. Under (A) the one `property` field is shared by the entrustment and the breach, so "such" and "that property" cannot come apart; under (B) a record could carry two properties that disagree.
**Encoded now.** (A).

## PC-12 — the head-as-sink figures (presentation)

**Status:** presentation; open for human review as to layout only; the reading taken stands until ruled.
**Provision.** None; this is a choice about figures.
**Readings.** (A) Keep `projections/*-head.{svg,txt}`, which draw each decision's name as the rightmost box, beside the ordinary figures. (B) Remove them.
**Consequences.** None to any rule: they are generated from the row's L4 with an option of the ladder renderer.
**Encoded now.** (A).

## Where I looked and found no fork

- s 380's three places ("any building, tent or vessel") and two uses: closed lists in the section's own words.
- s 407's two purposes ("for the purpose of transportation for hire or storage for rent or charge"): the in-force text names no occupation; the carrier and the warehouse operator are its Illustration.
- s 409(1)(c): the carve-out is explicit (PC-9).
