# Design question: when a condition fails, `JUST FALSE` or `NOTHING`?

**Status (2026-11-04): OPEN design question, not ruled.**
**This note makes no recommendation.**
It states one question, sets out the evidence for it, and lists the options.
No lawyer has read the encodings it cites, and the rule they follow (below) is itself "assumed, not ruled".

**How each example was checked.**
Every quotation of the statute is linked to its line in the raw text under the subject's `registers/source-bundle/`, and a script checked that each quoted fragment occurs in that line (an ellipsis marks words left out).
Every function is read at the file and line given, at `main` commit `31ce4c287` (the permalinks below name it in full).
For the six folders of legalese/commons#37 that commit is byte-identical to #37's head `7ef2d201e` (`git diff 7ef2d201e 31ce4c287 -- subjects/<subject>` is empty for each).
Every answer shown is the expected value of an `#ASSERT` in the deposit, at the line given.
On 2026-11-04 each of those assertion lines was satisfied when its module was run with `l4 run` on 1.6.98 (`7689b0d`, sha256 `82ea44ad…`) and on 1.6.108 (`2ae7c9b`).
I did not re-run whole rows for this note, and I chose the examples as the clearest I found, not by sampling.
The counts quoted from the rows' `NOTES.md` were copied from those files, not re-derived.

## 1. The question

The encodings of the US Food and Nutrition Act (SNAP) and of the UK's Social Security Contributions and Benefits Act 1992 (SSCBA) were each written in parts, by one agent per part.
Each function answers a question about one provision, and it answers `JUST TRUE`, `JUST FALSE` (a "no"), or `NOTHING` (the text gives no answer).
When a condition in the text fails, the parts do not always give the same kind of answer.
Some answer `JUST FALSE`; others, for a clause of the same shape and wording, answer `NOTHING`.
The examples in section 4 put two functions side by side on one input each.

**The question: when the condition in a provision is not met, what should the function answer, and who or what decides it?**
Today each part's encoder decides, branch by branch, under the rule in section 2.
The branch carries a comment saying which reading it took, and the part's `NOTES.md` lists the marginal ones.
The rule leaves readings (a) and (b) open, so the parts can differ.

## 2. The rule the encoders were given

The family's rule of 2026-10-29 (applied in legalese/commons#30 and in the batch of #37) is written into each part's brief, for example [`ssc1-BRIEF.md:50-58`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/notes/ssc1-BRIEF.md#L50-L58).
In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
The brief leaves two readings "for a lawyer" and tells the encoder to take them as the status quo and list every branch that rests on one:

- **(a)** A failed "if" counts as the text's no, clause by clause, within the provision that holds the "if".
  (This is an inference: "if A then B" does not itself say "if not A then not B".)
  Flat negatives count as the text saying no.
- **(b)** A prohibition or grant limited by its own wording does not count as the text's no.

Each part's encoder applied this alone.
The independent test pass of #37 shows how often the answers then differ from what a second reader expected.
In SNAP, 96 reviewer assertions expected another answer where the encoding answers `NOTHING`, and 76 of them are on branches tagged "NOTHING-kind (limited by its own wording)", which is reading (b) ([`NOTES.md:346-347`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/NOTES.md#L346-L347)).
In SSCBA the figures are 72 and 68 ([`NOTES.md:411-412`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/NOTES.md#L411-L412)).
Both rows then list, in a section headed "The convention is not applied one way throughout, and the parts do not agree with each other", the pairs and families that a lawyer should look at first ([`NOTES.md:360-372`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/NOTES.md#L360-L372), [`NOTES.md:419-432`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/NOTES.md#L419-L432)).
The examples below are taken from those lists and re-read against the code.

## 3. Why it matters to two other threads

### 3.1 Legal effects: gathering one effect from every section that gives it

A legal effect, such as "this establishment may be authorized to accept benefits" or "the widow is entitled to the pension", is rarely given by one provision.
One section grants it, another conditions it, a third lifts the condition, a fourth withdraws it.
To say whether the effect holds, a reader gathers every section that gives, conditions or withdraws it and combines what each says.
Where a function depends on another provision, the deposits take that provision's answer as an input (the part notes call these seams).
Example 5 shows one: `s 2018(h)(1)` takes the answer of `s 2018(h)(2)(A)` as an input of type `MAYBE BOOLEAN`.
Whatever combines the answers has to say what a `NOTHING` from one section means next to a `JUST FALSE` from another.
So the choice made at each branch is an input to that step.
A combining step could read a `JUST FALSE` as a denial by that section and a `NOTHING` as leaving the effect to the other sections.
If it did, the same words answered differently in two parts would combine differently.

### 3.2 The closed-world step, or negation as failure

Negation as failure (NAF) concludes "not p" when p cannot be established from what is known; that is a closed-world reading.
A `JUST FALSE` on a failed condition takes that step on the text's behalf when the text did not say no: "the conditions for yes are not met, so no".
A `NOTHING` declines to take it.
Readings (a) and (b) are two answers to the question "where may the encoding take that step?": (a) takes it for a failed "if" and for flat negatives, and (b) refuses it for a bar or grant limited by its own wording.
The step also appears in the other direction, in the open: example 5 is a function that is `TRUE` unless the text says no, written because the surrounding encoding needed a `BOOLEAN`.
The question in section 1 is therefore the question of which silences become a "no", and where in the encoding that is decided.

## 4. Examples

In every table, "part" means the part of the Act's encoding that holds the function.
The tags quoted in "The encoder's ground" are the comments on the branches.

### Example 1a (SNAP): inside a cap worded as a bar

| | Part 6, `s 2034(f)(2) the term of the grant is within the limit` | Part 3, `s 2016a(b)(2)(B) another replacement may occur in the Federal fiscal year` |
|---|---|---|
| Statute words | "The term of a grant under subsection (b) may not exceed 5 years." ([`usc07-ch51.txt:3041`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/registers/source-bundle/usc07-ch51.txt#L3041)) | "(B) shall not occur more than 2 times per Federal fiscal year per household by a single State agency; and" ([`usc07-ch51.txt:1240`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/registers/source-bundle/usc07-ch51.txt#L1240)) |
| Function | [`snap6-s2034.l4:355-358`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap6-s2034.l4#L355-L358) | [`snap3-s2016a.l4:180-188`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap3-s2016a.l4#L180-L188) |
| Input inside the cap | a grant term of 5 years | 1 replacement already made this fiscal year |
| Answer | `JUST TRUE` ([`snap6-tests-s2034.l4:166`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap6-tests-s2034.l4#L166)) | `NOTHING` ([`snap3-tests-s2016a.l4:69`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap3-tests-s2016a.l4#L69)) |
| Input past the cap | 6 years: `JUST FALSE` ([`snap6-tests-s2034.l4:167`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap6-tests-s2034.l4#L167)) | 2 already made: `JUST FALSE` ([`snap3-tests-s2016a.l4:70`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap3-tests-s2016a.l4#L70)) |
| The encoder's ground | `TRUE-kind: "may not exceed 5 years" is respected` | `NOTHING-kind (limited by its own wording)`, "a ceiling: it does not say that a replacement must occur" |

Both texts are a ceiling in negative words, and both encodings read the case past the ceiling as the text's own no.
They differ inside the ceiling: part 6 names its function for the limit and answers its own name (`JUST TRUE`), and part 3 names it "may occur" and notes that a ceiling does not say a replacement must occur (`NOTHING`).
The SNAP notes list this family as "A predicate named for the limit against a function named for a permission" ([`NOTES.md:363-365`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/NOTES.md#L363-L365)).
**Question for a lawyer:** for a reader who asks "is a 5-year term allowed?" and "may a second replacement occur this year?", is the text's answer in the cap a yes, or silence?

### Example 1b (SNAP): past a cap worded "not more than"

| | Part 2, `s 2015(d)(2) the State may lower the age of the dependent child` | Part 3, `s 2017(d)(1)(B) the State agency may reduce the allotment of the household by the percentage` |
|---|---|---|
| Statute words | "A State that requested a waiver to lower the age specified in subparagraph (B) and had the waiver denied by the Secretary as of August 1, 1996, may, for a period of not more than 3 years, lower the age of a dependent child…" ([`usc07-ch51.txt:593`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/registers/source-bundle/usc07-ch51.txt#L593)) | "(B) the State agency may reduce the allotment of the household by not more than 25 percent." ([`usc07-ch51.txt:1275`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/registers/source-bundle/usc07-ch51.txt#L1275)) |
| Function | [`snap2-2015d.l4:309-316`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap2-2015d.l4#L309-L316) | [`snap3-s2017.l4:237-242`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap3-s2017.l4#L237-L242) |
| Input past the cap | a State whose waiver request was denied as of 1 August 1996 lowers the age to 3 for 4 years | benefits are reduced under a means-tested program, and the proposed reduction is 25.01 percent |
| Answer | `JUST FALSE` ([`snap2-tests-2015d.l4:134`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap2-tests-2015d.l4#L134)) | `NOTHING` ([`snap3-tests-s2017.l4:133`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap3-tests-s2017.l4#L133)) |
| At the cap | 3 years: `JUST TRUE` ([`snap2-tests-2015d.l4:133`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap2-tests-2015d.l4#L133)) | 25 percent: `JUST TRUE` ([`snap3-tests-s2017.l4:130`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap3-tests-s2017.l4#L130)) |
| The encoder's ground | `FALSE-kind (the text says no in its own words)`: "for a period of not more than 3 years" | `NOTHING-kind (limited by its own wording)`: "the State agency may reduce the allotment of the household by not more than 25 percent" |

Both are permissions with a cap in the same words, "not more than", and the two encodings answer opposite ways past it.
The SNAP notes record the pair: part 2 answers `JUST FALSE` past "not more than 3 years", and part 3 answers `NOTHING` past "not more than 25 percent" ([`NOTES.md:366-368`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/NOTES.md#L366-L368)).
**Question for a lawyer:** if a State lowers the age for 4 years, or an agency reduces the allotment by 30 percent, does the text say no, or does it say nothing about that case?

### Example 2 (SNAP): "(other than …)"

| | Part 2, `s 2015(d)(4)(I)(i)(II) the State agency is required to pay or reimburse the dependent care cost` | Part 6, `s 2031(e) the Secretary shall waive compliance with the requirement` |
|---|---|---|
| Statute words | "(II) the actual costs of such dependent care expenses that are determined by the State agency to be necessary for the participation of an individual in the program (other than an individual who is the caretaker relative of a dependent in a family receiving benefits under part A of title IV of the Social Security Act …)" ([`usc07-ch51.txt:655`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/registers/source-bundle/usc07-ch51.txt#L655)) | "With respect to the Project, the Secretary shall waive compliance with any requirement contained in this chapter (other than this section) that, if applied, would prevent the State from carrying out the Project or effectively achieving its purpose." ([`usc07-ch51.txt:2926`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/registers/source-bundle/usc07-ch51.txt#L2926)) |
| Function | [`snap2-2015d4.l4:299-305`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap2-2015d4.l4#L299-L305) | [`snap6-s2031.l4:1210-1214`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap6-s2031.l4#L1210-L1214) |
| Input in the excluded class | the person is the title IV caretaker relative; the cost is a necessary dependent care cost | the requirement is contained in this section; it would prevent the Project |
| Answer | `JUST FALSE` ([`snap2-tests-2015d4.l4:110`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap2-tests-2015d4.l4#L110)) | `NOTHING` ([`snap6-tests-s2031.l4:506`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap6-tests-s2031.l4#L506)) |
| The encoder's ground | `FALSE-kind (the text says no in its own words)`: "(other than an individual who is the caretaker relative …)" | `NOTHING-kind (limited by its own wording)`: "any requirement contained in this chapter (other than this section)"; the text "does not say a requirement of this section may not be waived, it only does not require the waiver" |

Each text excludes a class in a parenthesis "(other than …)", and each function is asked about a case in the excluded class.
One answers that the State agency is not required to pay, and the other that the text does not say whether the Secretary must waive a requirement of this section.
The SNAP notes list this family as `"(other than ...)"`: part 6 answers `NOTHING` for `s 2031(e)` and four siblings, and all five change together if "other than" is read as "except" ([`NOTES.md:369`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/NOTES.md#L369)).
**Question for a lawyer:** is an "(other than X)" parenthesis the text's own no for X, or only a limit on what the sentence grants?

### Example 3 (SSCBA): "where"

| | Part 7, `s 171ZU(1) the claimant mother is entitled to statutory shared parental pay` | Part 9, `sch 5 para A1(1) the person must elect` |
|---|---|---|
| Statute words | "(1) Regulations may provide that, where all the conditions in subsection (2) are satisfied in relation to a person who is the mother of a child (“the claimant mother”), the claimant mother is to be entitled in accordance …" ([`ukpga-1992-4.txt:3720`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/registers/source-bundle/ukpga-1992-4.txt#L3720)) | "(1) Where a person’s entitlement to a Category A or Category B retirement pension is deferred and the period of deferment is at least 12 months, the person shall, on claiming his pension or within a prescribed period after claiming it, elect in the prescribed manner either—" ([`ukpga-1992-4.txt:5069`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/registers/source-bundle/ukpga-1992-4.txt#L5069)) |
| Function | [`ssc7-12zc.l4:110-117`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc7-12zc.l4#L110-L117) | [`ssc9-sch5.l4:58-64`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc9-sch5.l4#L58-L64) |
| Input where the "where" fails | condition (a) of subsection (2) is not met (the prescribed conditions as to caring for the child); regulations provide for the entitlement and none disapplies a condition | entitlement deferred, for 1 January to 30 December 2025, a day short of 12 months |
| Answer | `JUST FALSE` ([`ssc7-tests-12zc.l4:167`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc7-tests-12zc.l4#L167)) | `NOTHING` ([`ssc9-tests-sch5.l4:46`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc9-tests-sch5.l4#L46)) |
| The encoder's ground | `FALSE-kind (the text says no in its own words)`; the comment marks the branch as a failed "where" and as reading (a) | `NOTHING-kind (limited by its own wording)`: "Where a person’s entitlement to a Category A or Category B retirement pension is deferred" |

Both sentences open a set of conditions with "where", and the two encodings treat a failed "where" differently.
Part 9's comment on its function says the conditions are introduced by "Where", which is not an "if", so a person outside them is not told "no" by the sub-paragraph ([`ssc9-sch5.l4:49-50`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc9-sch5.l4#L49-L50)).
The SSCBA notes say parts 1, 2 and 9 answer `NOTHING` for a failed "where", on the ground that "where" is not on the brief's list of grounds for `JUST FALSE`, and part 7 answers `JUST FALSE` in eight branches of Part 12ZC ([`NOTES.md:422-423`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/NOTES.md#L422-L423)).
The part 7 sentence is also a power to make regulations; the encoder models the regulations as a gate input, and the answer shown is for the failed "where" limb, with the gate on.
The same part 9 file answers `JUST FALSE` to the narrower question "is the period at least 12 months?" for the same period ([`ssc9-tests-sch5.l4:29`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc9-tests-sch5.l4#L29)); the `NOTHING` is on the duty that the "Where" introduces.
The notes state the dependency: if a ruling goes against reading (a) for "where", part 7's eight branches flip to `NOTHING`; if it goes the other way, the `NOTHING` branches of parts 1, 2 and 9 flip together.
**Question for a lawyer:** is a person outside the conditions of a sentence that opens "Where …" told "no" by that sentence, or is the sentence silent about them?

### Example 4 (SSCBA): "until"

| | Part 2, `s 38(2) the widow is entitled to the pension on the day` | Part 5, `s 127(b) section 124(1) has effect with the substituted paragraph (c) on the day` |
|---|---|---|
| Statute words | "(2) The widow shall not be entitled to the pension for any period after she remarries or forms a civil partnership, but, subject to that, she shall continue to be entitled to it until she attains pensionable age." ([`ukpga-1992-4.txt:1090`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/registers/source-bundle/ukpga-1992-4.txt#L1090)) | "(b) until the end of the period of 15 days beginning with that day, section 124(1) above shall have effect in relation to him as if the following paragraph were substituted for paragraph (c)—" ([`ukpga-1992-4.txt:2713`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/registers/source-bundle/ukpga-1992-4.txt#L2713)) |
| Function | [`ssc2-bereavement.l4:247-256`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc2-bereavement.l4#L247-L256) | [`ssc5-part7.l4:514-519`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc5-part7.l4#L514-L519) |
| Input just past the "until" | the day she attains pensionable age (1 January 2030); no remarriage date; entitled under s 38(1) | the 16th day after the day of return to work (return on 1 March 2024, day asked about 16 March 2024) |
| Answer | `JUST FALSE` ([`ssc2-tests-bereavement.l4:145`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc2-tests-bereavement.l4#L145)) | `NOTHING` ([`ssc5-tests-part7.l4:210`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc5-tests-part7.l4#L210)) |
| Inside the period | the day before: `JUST TRUE` ([`ssc2-tests-bereavement.l4:144`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc2-tests-bereavement.l4#L144)) | the 15th day: `JUST TRUE` ([`ssc5-tests-part7.l4:209`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/ssc5-tests-part7.l4#L209)) |
| The encoder's ground | `FALSE-kind (the text says no in its own words)`: "she shall continue to be entitled to it until she attains pensionable age" | `NOTHING-kind (limited by its own wording)`: "until the end of the period of 15 days beginning with that day" |

Both clauses end something at a stated point with "until", and the first encoder reads the end as a "no" while the second reads it as silence.
The SSCBA notes mark the second as the one item where the part's encoder thinks the lead could reasonably rule the other way, because the clause fits both the brief's `JUST FALSE` list ("until") and its `NOTHING` list ("a stated period"), and changing it alone would split that part's class of period-limited branches ([`NOTES.md:426`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/uk/social-security-contributions-and-benefits-act-1992/encodings/legalese-sonnet-5.5/NOTES.md#L426)).
**Question for a lawyer:** after the stated end, does "until" say that the entitlement or the modified effect has stopped, or only that the sentence no longer speaks to the case?

### Example 5 (SNAP): the closed-world step taken in the open

| | `s 2018(h)(1) the private establishment may be authorized to accept and redeem benefits` | `s 2018(h) permitted under section 2018(h)` |
|---|---|---|
| Statute words | "Subject to paragraph (2), no private establishment that contracts with a State agency to offer meals at concessional prices as described in paragraphs (3), (4), and (9) of section 2012(k) of this title may be authorized to accept and redeem benefits unless the Secretary determines that the participation of the private establishment is required to meet a documented need in accordance with section 2020(e)(25) of this title." ([`usc07-ch51.txt:1381`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/registers/source-bundle/usc07-ch51.txt#L1381)) | the same sentence |
| Function | [`snap1-s2018.l4:290-298`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap1-s2018.l4#L290-L298) | [`snap1-s2018.l4:307-308`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap1-s2018.l4#L307-L308) |
| Input | the establishment is one described in section 2012(k); the Secretary has made the determination; the answer of `s 2018(h)(2)(A)` is `JUST FALSE` | the determination has been made; the answer of `s 2018(h)(2)(A)` is `JUST FALSE` |
| Answer | `NOTHING` ([`snap1-tests-s2018.l4:134`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap1-tests-s2018.l4#L134)) | `TRUE` ([`snap1-tests-s2018.l4:143`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap1-tests-s2018.l4#L143)) |

This is not a cross-part pair.
It is two functions in one part, and it shows both threads in one place.
The first answers for one provision, taking the answer of its neighbour `s 2018(h)(2)(A)` as an input.
The determination does not itself authorize the establishment, so the answer is `NOTHING`.
The second is the `BOOLEAN` that the keel (the shared core and definitions of the Act's encoding) asked for, and it is `NOT (definitely no …)` of the first: it is `TRUE` unless the text says no.
The encoder's comment calls it "a lossy step the keel asked for: NOTHING becomes TRUE here, never FALSE" ([`snap1-s2018.l4:300-301`](https://github.com/legalese/commons/blob/31ce4c28785744363f78710620e1602456fc31bc/subjects/us/food-and-nutrition-act-of-2008/encodings/legalese-sonnet-5.5/snap1-s2018.l4#L300-L301)).
So a silence becomes a "yes" here because a type said `BOOLEAN`, and in the examples above a silence becomes a "no" or stays open depending on which part wrote the branch.
**Question for a lawyer:** where an encoding must give a yes or a no, which way should a silence fall, and should that be the same for every provision?

## 5. What the examples have in common

- In each pair the statute words have the same shape: a cap in negative words, a parenthetical exclusion, a clause that opens "where", a clause that ends at "until".
- In each pair the two encoders gave their ground in the branch comment, citing the brief's rule.
  The brief marks readings (a) and (b) "for a lawyer", so it leaves the point open.
- The answers differ for inputs a user can supply: a grant term, a number of replacements, a percentage, an age, a date.
  So a caller of the exported functions can get a "no" from one section and no answer from another for the same kind of clause.
- The examples are not the whole class.
  The `NOTES.md` lists name more families, among them "subject to", "throughout which", and a negative inside a relative clause, which this note does not illustrate.

## 6. Options

These are listed so the discussion can pick among them; none is recommended here.

1. **Leave the encoders to read the rule, and keep recording the reading.**
   Each branch keeps its tag and the marginal tables stay the record.
   The cost is the one shown above: the same wording can answer differently depending on which part holds it.
2. **Rule once per wording class and apply it to every row.**
   The classes the notes already name are a cap in negative words, a parenthetical exclusion, "where", "until", "subject to" and a class-named predicate.
   The notes say which branches would move together for each (for example all five "other than" branches of SNAP part 6, or part 7's eight "where" branches against the `NOTHING` branches of parts 1, 2 and 9).
3. **Expose both readings.**
   Each affected function would give its answer under (a) and under (b), or say which reading its answer rests on, and the caller or a later step would choose.
   That changes what the functions return, and I did not find a function in these rows that does it.
4. **Settle the combining step first.**
   Decide how the answers of several sections combine into one legal effect (section 3.1), and read the rule for a failed condition off that, so that a `NOTHING` or a `JUST FALSE` means what the combining step needs it to mean.

## 7. What this note does not do

- It does not rule, and it does not say any example is right or wrong.
- It does not specify how answers combine into a legal effect; it only says where that step depends on the choice.
- It does not re-derive the rows' counts, and it does not re-run whole rows.
- It does not look at the other rows that follow the same rule (the interpretation-act rows of #30, the Penal Code, the Welfare Reform Act, the Silver Support Scheme Act, Israel's Income Support Law); I did not check them for this note.
