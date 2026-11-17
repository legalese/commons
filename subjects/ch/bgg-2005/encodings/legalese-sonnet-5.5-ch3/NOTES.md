# NOTES: Federal Supreme Court Act (BGG, SR 173.110), chapter 3 (Art. 72 to 89), in L4

Encoding `legalese-sonnet-5.5-ch3`: a single Sonnet 5.5 agent working alone from the brief, on the stable `l4` 1.6.110 (main, e51181d, 2026-11-11, sha256 `9c7656f74151383da2c7344ad53269a8754bd874af8eb513180d61dc145016c7`), checked against the second stable build 1.6.109.
Status: draft.
How each claim below was verified: every count is printed by a script run in this folder (`check.sh`, `coverage.py`, `quotecheck.py`, `srcrefs.py`); every statement about what the text says was written beside a quoted German phrase that `quotecheck.py` found in the text file.
No domain expert has read this encoding against the text.

## What the source is, and what these words are

The text is a plain-text rendering of Fedlex's consolidated German version of chapter 3 of the BGG, applicable from 2026-04-01, made by a converter script.
It is not the official text, and nothing here is verified against the official text.
The deposit does not say whether the consolidated version or only the publication of each amending act in the Official Compilation (AS) is authoritative (`SOURCE-LICENSE.md`, and `inputs/STUB-SOURCE-LICENSE.md` beside the text).
Every quotation of the text is German, copied by script from the file (`-- src:` lines; `srcrefs.py check` reports 0 problems), and every other German phrase in a comment is checked against the file by `quotecheck.py`.
Every identifier, `@desc` string, seat question, test comment and sentence of this file is English: it is a gloss and a reading, not the text, and it is not a translation of the law.

## Seat

The seat is a person affected by a decision: a party to civil or criminal proceedings, or to proceedings in a public-law matter, who lost, or a person with another interest the text names.
They ask, on facts they can state, whether they may appeal to the Federal Supreme Court, which appeal it is, whether the value in dispute is enough, whether they have standing, which decisions are excluded from appeal, and whether the case must first have gone through the cantons' highest instance.
This is the seat the brief fixes; the chapter is addressed to exactly this reader, because it says when the Federal Supreme Court takes an appeal against which decisions, and from whom.
There is never a seat for an official.
Provisions that address an authority only are in layer 1 for what they decide and appear in layer 2 only for what they mean to the person.

Layer 2 is `bgg3-seat.l4` (33 questions, each with `@export` and `@desc` on every input, grouped under `§` headings in the text's order: civil, criminal, public law) and `bgg3-cases-seat.l4` (146 asserted cases, at least one per question; 30 of the 33 questions have a case that answers `NOTHING`, and the three standing questions, Art 76(1), 81(1) and 89(1), have none because a conjunction of requirements answers `JUST TRUE` or `JUST FALSE`, fork F3).
It IMPORTs the layer-1 modules and calls their functions; it restates no rule, and no layer-1 module was changed for it.
Which layer-1 provisions have no question in layer 2, and why:

- Art 76(2), 81(2), 81(3), 89(2)(a) and 89(2)(b) say which federal authority may appeal: they address authorities, not the person affected.
- The cantons' duties and permission in Art 75(2), 80(2), 86(2), 86(3) and 88(2) are regulative rules in layer 1; the person meets them through the decision functions asked as questions 'must my last cantonal instance be an upper court' (Art 75(2), 80(2), 86(2)), 'could my canton have used a non-court authority' (Art 86(3)) and 'must my canton give me a remedy' (Art 88(2)).
- Art 84(2) and the interior limbs and sub-items are reached through their composites (the question for Art 72 includes Art 72(2)(a) and (b), the question for Art 84(1) includes Art 84(2), and so on).

Three questions, Art 73, Art 79 and Art 83, are asked the other way round from layer 1 (fork F22): the provisions are bars, layer 1 answers in the text's polarity (a bar is `JUST FALSE`), and a person asks 'is my decision excluded', so the seat swaps the two definite answers and leaves `NOTHING` alone (see 'Seat polarity (independent reader)' below).
It takes 19 inputs (the kind of decision and 18 facts), most of which belong to one kind each; the form says so in each `@desc` and says to answer no or 0 for a fact that does not belong to the chosen kind.

The questions:

**Civil matters (Art 72 to 77)**

- `Art 72 the appeal in civil matters lies against my decision`: Can I appeal to the Federal Supreme Court in a civil matter against my decision (Art 72)?
- `Art 73 my decision is excluded from the appeal in civil matters`: Is my civil-law decision one that the Act excludes from the appeal because it was made in trade-mark opposition proceedings (Art 73)?
- `Art 74(1) the value in dispute in my case is enough`: Is the value in dispute in my civil case enough for an appeal (Art 74(1))?
- `Art 74(2) the appeal is admissible in my case although the value is short`: Can I still appeal in my civil case although the value in dispute is short (Art 74(2))?
- `Art 75(1) the appeal in civil matters is admissible against the decision of my lower instance`: Can I appeal in my civil case against the decision of the body that made it (Art 75(1))?
- `Art 75(2) my last cantonal instance is an upper court deciding as an appeal instance, or an exception applies`: Is my last cantonal instance the kind of court Art 75(2) requires, or does an exception apply (Art 75(2))?
- `Art 76(1) I am entitled to appeal in civil matters`: Am I entitled to appeal in my civil case (Art 76(1))?
- `Art 77(1) the appeal in civil matters is admissible against my arbitral award whatever the value in dispute`: Can I appeal in a civil matter against an arbitral award, whatever the value in dispute (Art 77(1))?
- `Art 77(2) the listed provision is applicable to my appeal against the arbitral award`: Does a given provision of the Act apply to my appeal against the arbitral award (Art 77(2))?
- `Art 77(2bis) I may draft my written submission in English`: May I draft my written submission in English in my appeal against an arbitral award (Art 77(2bis))?
- `Art 77(3) my complaint meets the condition for being examined`: Will the Court examine my complaint against the arbitral award (Art 77(3))?

**Criminal matters (Art 78 to 81)**

- `Art 78 the appeal in criminal matters lies against my decision`: Can I appeal to the Federal Supreme Court in a criminal matter against my decision (Art 78)?
- `Art 79 my decision of the Complaints Chamber is excluded from the appeal in criminal matters`: Is my criminal-matter decision of the Complaints Chamber excluded from the appeal because it is not about a coercive measure (Art 79)?
- `Art 80(1) the appeal in criminal matters is admissible against the decision of my lower instance`: Can I appeal in my criminal case against the decision of the body that made it (Art 80(1))?
- `Art 80(2) my last cantonal instance is an upper court deciding as an appeal instance, or the exception applies`: Is my last cantonal instance the kind of court Art 80(2) requires, or does the exception apply (Art 80(2))?
- `Art 81(1) I am entitled to appeal in criminal matters`: Am I entitled to appeal in my criminal case (Art 81(1))?

**Public-law matters (Art 82 to 89)**

- `Art 82 the appeal in public-law matters lies against my decision`: Can I appeal to the Federal Supreme Court in a public-law matter (Art 82)?
- `Art 83 my decision is excluded from the appeal in public-law matters`: Is my decision one that the Act excludes from the appeal in public-law matters (Art 83)?
- `Art 84(1) the condition for an appeal on international legal assistance in criminal matters is met in my case`: In international legal assistance in criminal matters, is my case one in which an appeal is admissible (Art 84)?
- `Art 84a the condition for an appeal on international administrative assistance in tax matters is met in my case`: In international administrative assistance in tax matters, is my case one in which an appeal is admissible (Art 84a)?
- `Art 85(1) the appeal is admissible in my pecuniary matter`: Is the value in dispute in my public-law money matter enough for an appeal (Art 85(1))?
- `Art 85(2) the appeal is admissible in my case although the value is short`: Can I still appeal in my public-law money matter although the value in dispute is short (Art 85(2))?
- `Art 86(1) the appeal in public-law matters is admissible against the decision of my lower instance`: Can I appeal in my public-law case against the decision of the body that made it (Art 86(1))?
- `Art 86(2) my immediate lower instance is an upper court, or another federal statute provides for appeal from another judicial authority`: Is my immediate lower instance an upper court, or does another federal statute provide for an appeal from the other judicial authority (Art 86(2))?
- `Art 86(3) my canton may have set up an authority other than a court as immediate lower instance`: Could my canton lawfully have used an authority that is not a court as the immediate lower instance in my case (Art 86(3))?
- `Art 87(1) the appeal lies directly against the cantonal enactment I challenge`: Can I appeal directly to the Federal Supreme Court against a cantonal enactment (Art 87(1))?
- `Art 87(2) Art 86 applies to my appeal against the cantonal enactment`: Where my canton gives a remedy against enactments, does Art 86 apply to my appeal (Art 87(2))?
- `Art 88(1) the appeal on voting rights is admissible against the act I challenge`: In a voting rights matter, can I appeal against the act I challenge (Art 88(1))?
- `Art 88(2) my canton must provide a remedy against the act`: Must my canton give me a remedy against an act that can violate my political rights (Art 88(2))?
- `Art 89(1) I am entitled to appeal in public-law matters`: Am I entitled to appeal in my public-law case (Art 89(1))?
- `Art 89(2)(c) a municipality or other public-law corporation like me is also entitled to appeal`: As a municipality or other public-law corporation, am I also entitled to appeal (Art 89(2)(c))?
- `Art 89(2)(d) another federal statute may give me the right to appeal`: Does another federal statute give me the right to appeal (Art 89(2)(d))?
- `Art 89(3) I am entitled to appeal in a voting rights matter as a voter`: As a voter, am I entitled to appeal in a voting rights matter (Art 89(3))?

## What is encoded, and what is not

Layer 1 is six modules in the text's own order, each followed by its tests:

| module | text | what it holds | tests |
| --- | --- | --- | --- |
| `bgg3-nouns.l4` | the whole chapter | the typed choices the questions share (deciding body, kind of decision, kind of public-law decision, subject of a legal assistance decision, person in a criminal appeal), the 40 kinds of decision in Art 83 (and a forty-first, 'none of these kinds') and the record of 18 facts they read, and the actor and acts of the cantons' duties | none (declarations) |
| `bgg3-civil.l4` | Art 72 to 77 | appeal in civil matters: what is appealable, the 15 000 and 30 000 franc limits and their exceptions, the lower instances, standing, arbitral awards | `bgg3-tests-civil.l4` |
| `bgg3-criminal.l4` | Art 78 to 81 | appeal in criminal matters: what is appealable, the Complaints Chamber exception, the lower instances, standing | `bgg3-tests-criminal.l4` |
| `bgg3-public-scope.l4` | Art 82 and 83 | appeal in public-law matters: what is appealable, and the limbs of the list of exceptions (a to zter: 42 limb functions over 40 kinds) with a dispatcher | `bgg3-tests-public-scope.l4` |
| `bgg3-public-limits.l4` | Art 84, 84a and 85 | legal assistance and tax assistance conditions, and the value limits | `bgg3-tests-public-limits.l4` |
| `bgg3-public-courts.l4` | Art 86 to 89 | the lower instances, direct appeal against enactments, voting rights matters, standing | `bgg3-tests-public-courts.l4` |

Every provision of the text has a row in the coverage table below.
The only things left out are the headings and the file header (inert, reason 1) and three provisions the text shows as repealed (Art 72(2)(b)(7), Art 81(1)(b)(4), Art 83(s)(1)).
Everything the chapter leans on and does not contain is asked as an input (a yes or no, or a number the person can state) and named under 'What the text does not answer' below.

Every decision function answers `MAYBE BOOLEAN`.
The name of each carries the provision it implements, in the form `Art 74(1)(a) the value in dispute is enough`, and says no more than the provision says.
Every function begins with `-- src:` lines copied from the text and an `@ref` locator for the lines quoted.
A function is a decision function where the provision fixes a condition for an appeal; the cantons' duties and one permission are also regulative rules (`PARTY Canton MUST ...`), run with `#TRACE` (see 'What the stable binary does not accept').
No deadline is stated by the text for any of these duties, so none is given.

## Reading the answers

### Reading a result: FALSE and NOTHING

The rule of 2026-10-29, in this subject's terms (assumed, not ruled by a lawyer; see 'Marginal readings for a lawyer' below).

- `JUST TRUE` means the text says yes to these facts: for example Art 74(2)(a), the appeal is admissible although the value is short when a legal question of fundamental importance arises.
- `JUST FALSE` means the text itself says no to these facts, in its own words.
  In this chapter that is a bar the text states flatly ("Die Beschwerde ist unzulässig gegen ..." in Art 73 and Art 79, and with a colon over the limbs of Art 83), a condition the text introduces with 'only if' ("nur zulässig, wenn" in Art 74(1), 84 and 84a) or 'unless' ("sofern nicht" in Art 86(1)(d)), and a conjunctive list of requirements an entitlement is built from (Art 76(1), 81(1), 89(1)).
  Each such branch in a `.l4` file carries a comment that begins `-- FALSE-kind (the text says no in its own words):` and goes on with the quoted German words.
- `NOTHING` means not covered: the text is silent, lists without closing the list, says 'includes', leaves a term undefined, points to another statute outside the sources, or limits a grant or a bar in its own wording and the case falls outside the limit.
  Each such branch carries `-- NOTHING-kind (<why>)` with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
  Most of the `NOTHING` answers here are the last one: the limbs of Art 83 are limited bars, so when the case falls outside a limb's own condition, the limb does not say yes and does not say no.
- A caller must never turn `NOTHING` into `FALSE`: 'the text does not decide' is not 'the appeal is inadmissible'.
- `REFUSE` does not exist on the stable binary: 'not covered' is `NOTHING`, asserted.

How the answers read for the person in the seat: `JUST TRUE` is 'the text says yes', `JUST FALSE` is 'the text says no', and `NOTHING` is 'this chapter does not decide it; look at chapter 4 and the other statutes it points to'.
The Art 73, Art 79 and Art 83 questions are the exception: their `JUST TRUE` means 'the Act excludes my decision' (fork F22).

## Jural relations

One row per provision that creates a relation.
Hohfeld's correlatives: claim and duty; privilege and no-right; power and liability (being subject to the power); immunity and disability.
The 'appeal' in the table is the Beschwerde to the Federal Supreme Court.
A provision that says an appeal is admissible gives the person a power (to bring the appeal) and makes the Federal Supreme Court and the other party liable to it; a provision that says it is inadmissible is the reverse (the person has a disability, the Court an immunity).
A provision that says the Court judges appeals ("beurteilt") is a claim of the person against the Court and the Court's duty.
Each rule is stated once, as a relation between two parties, and named neutrally: no relation is written twice from both sides.

| provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | kind | L4 rule (module) |
| --- | --- | --- | --- | --- |
| Art 72(1) | person affected by a decision in a civil matter | Federal Supreme Court | claim to have the appeal decided / duty to decide | `Art 72(1)` (civil) |
| Art 72(2)(a), (b) | person affected by a debt enforcement, bankruptcy, or civil-law-related public-law decision | Federal Supreme Court | claim / duty (the same appeal, extended) | `Art 72(2)(a)`, `Art 72(2)(b)` and its six items (civil) |
| Art 73 | Federal Supreme Court | person affected by a trade-mark opposition decision | immunity / disability | `Art 73` (civil) |
| Art 74(1) | Federal Supreme Court (below the amount) | person with a pecuniary claim below 15 000 or 30 000 francs | immunity / disability; at or above the amount, power / liability | `Art 74(1)`, `Art 74(1)(a)`, `Art 74(1)(b)` (civil) |
| Art 74(2) | person whose value is short but who has one of five grounds | Federal Supreme Court | power to appeal / liability | `Art 74(2)` and limbs (a) to (e) (civil) |
| Art 75(1) | person affected by a decision of the last cantonal instance, the Federal Administrative Court or the Federal Patent Court | Federal Supreme Court | power / liability | `Art 75(1)` (civil) |
| Art 75(2) | litigants in civil matters | cantons | claim to an upper court as last instance deciding on appeal (with three exceptions) / duty | `Art 75(2)` function and duty (civil) |
| Art 76(1) | person who took part, or had no chance to, and is especially affected | Federal Supreme Court, other parties | power / liability | `Art 76(1)` and limbs (a), (b) (civil) |
| Art 76(2) | Federal Chancellery, federal departments and subordinate services | Federal Supreme Court, other parties | power / liability | `Art 76(2)` (civil) |
| Art 77(1) | party to an arbitral award, whatever the value | Federal Supreme Court | power / liability | `Art 77(1)` and limbs (a), (b) (civil) |
| Art 77(2) | none (a routing rule: which procedural provisions do not apply to these appeals) | none | none | `Art 77(2)` (civil) |
| Art 77(2bis) | appellant against an arbitral award | Federal Supreme Court | privilege to write in English / no-right | `Art 77(2bis)` (civil) |
| Art 77(3) | appellant against an arbitral award | Federal Supreme Court | immunity from examination of complaints not raised and reasoned / disability | `Art 77(3)` (civil) |
| Art 78(1) | person affected by a decision in a criminal matter | Federal Supreme Court | claim to have the appeal decided / duty | `Art 78(1)` (criminal) |
| Art 78(2)(a), (b) | person affected by a decision on civil claims dealt with together, or on the execution of penalties and measures | Federal Supreme Court | claim / duty (extended) | `Art 78(2)(a)`, `Art 78(2)(b)`, `Art 78(2)` (criminal) |
| Art 79 | Federal Supreme Court | person affected by a Complaints Chamber decision that is not on a coercive measure | immunity / disability | `Art 79` (criminal) |
| Art 80(1) | person affected by a decision of the last cantonal instance or a Federal Criminal Court chamber | Federal Supreme Court | power / liability | `Art 80(1)` (criminal) |
| Art 80(2) | persons in criminal proceedings | cantons | claim to an upper court as last instance deciding on appeal / duty | `Art 80(2)` function and duty (criminal) |
| Art 81(1) | person who took part, or had no chance to, and has a legally protected interest | Federal Supreme Court, other parties | power / liability | `Art 81(1)` and limbs (a), (b), (b)(1)-(7) (criminal) |
| Art 81(2) | federal authority to which federal law says the decision is communicated | Federal Supreme Court, other parties | power / liability | `Art 81(2)` (criminal) |
| Art 81(3) | Federal Chancellery, federal departments and subordinate services (execution of penalties and measures) | Federal Supreme Court, other parties | power / liability | `Art 81(3)` (criminal) |
| Art 82 | person affected by a public-law decision, a cantonal enactment, or a voting rights matter | Federal Supreme Court | claim to have the appeal decided / duty | `Art 82` and limbs (a) to (c) (public-scope) |
| Art 83 (limbs (a) to (zter), except (m)) | Federal Supreme Court | person affected by a decision of one of the listed kinds | immunity / disability | `Art 83` dispatcher and one function per limb (public-scope) |
| Art 83(m), the departure | person affected by a remission decision on the direct federal tax or a cantonal or communal income or profit tax, with a legal question or a particularly important case | Federal Supreme Court | power / liability | `Art 83(m)` (public-scope) |
| Art 84(1) | person affected by a legal assistance decision on extradition, seizure, handing over or secret-sphere information in a particularly important case | Federal Supreme Court | power / liability (otherwise disability / immunity) | `Art 84(1)` (public-limits) |
| Art 84(2) | none (says what a particularly important case includes) | none | none | `Art 84(2)` (public-limits) |
| Art 84a | person affected by a tax assistance decision with a legal question or a particularly important case | Federal Supreme Court | power / liability (otherwise disability / immunity) | `Art 84a` (public-limits) |
| Art 85(1) | Federal Supreme Court | person with a pecuniary state liability claim below 30 000 francs, or a public-law employment claim below 15 000 francs | immunity / disability | `Art 85(1)`, `Art 85(1)(a)`, `Art 85(1)(b)` (public-limits) |
| Art 85(2) | person whose value is short but a legal question of fundamental importance arises | Federal Supreme Court | power / liability | `Art 85(2)` (public-limits) |
| Art 86(1) | person affected by a decision of the Federal Administrative Court, the Federal Criminal Court, the independent complaints authority for radio and television, or a last cantonal instance (unless the Federal Administrative Court can be appealed to) | Federal Supreme Court | power / liability | `Art 86(1)` and limbs (a) to (d) (public-courts) |
| Art 86(2) | persons in public-law proceedings | cantons | claim to an upper court as immediate lower instance / duty | `Art 86(2)` function and duty (public-courts) |
| Art 86(3) | cantons | persons in proceedings on decisions of predominantly political character | privilege to use an authority other than a court / no-right | `Art 86(3)` function and permission (public-courts) |
| Art 87(1) | person affected by a cantonal enactment where no cantonal remedy exists | Federal Supreme Court | power / liability | `Art 87(1)` (public-courts) |
| Art 87(2) | none (a routing rule: Art 86 applies where cantonal law gives a remedy) | none | none | `Art 87(2)` (public-courts) |
| Art 88(1) | person in a voting rights matter | Federal Supreme Court | power / liability | `Art 88(1)` and limbs (a), (b) (public-courts) |
| Art 88(2) | voters in cantonal matters | cantons | claim to a remedy against acts that can violate their political rights (not acts of parliament or government) / duty | `Art 88(2)` function and duty (public-courts) |
| Art 89(1) | person who took part, or had no chance to, is especially affected, and has an interest worthy of protection | Federal Supreme Court, other parties | power / liability | `Art 89(1)` and limbs (a) to (c) (public-courts) |
| Art 89(2)(a), (b) | Federal Chancellery, federal departments and subordinate services; the competent body of the Federal Assembly in federal staff matters | Federal Supreme Court, other parties | power / liability | `Art 89(2)(a)`, `Art 89(2)(b)` (public-courts) |
| Art 89(2)(c), (d) | municipalities and other public-law corporations complaining of a violation of constitutional guarantees; persons, organisations and authorities to whom another federal statute gives the right | Federal Supreme Court, other parties | power / liability | `Art 89(2)(c)`, `Art 89(2)(d)` (public-courts) |
| Art 89(3) | person entitled to vote in the matter concerned | Federal Supreme Court, other parties | power / liability | `Art 89(3)` (public-courts) |
| headings (chapter, three sections, 19 Article headings) | none | none | none | no rule (inert, reason 1) |

## Coverage table

Generated by `coverage.py` from the text file (`python3 -I coverage.py <text file> --table`), one row per unit: the file header, the chapter and section headings, one heading per Article, every numbered paragraph, an Article's unnumbered body, every list item and every sub-item.
Footnote lines are attached to the unit that carries their marker and have no rows of their own.
`coverage-map.tsv` lists the units each fork covers; `coverage.py` fails if a non-blank line is in no row or in two rows, if an `encoded` or `fork` row has no function or no assertion that calls it, or if a layer-1 function belongs to no row.
The columns 'assertions + traces' count the lines of the test and case files that call that row's own functions directly.
The 'seat questions' column lists the questions that reach a row's function, directly or through a composite.

- coverage: 163 units in 226 non-blank lines of the text (162 operative lines + 60 footnote lines + 4 header/source lines)
- encoded                             77
- fork                                59
- inert                               24
- repealed or blank in this text       3
- layer-1 functions: 136; seat questions: 33
- COVERAGE OK: every non-blank line of the text is in exactly one row; every encoded or fork row has a function and a test

Audit counts: the table is built from the text, so there is no earlier table to compare: rows before the audit 163, rows after 163; non-blank lines of the text counted 226; lines in no row 0; lines in two rows 0.

There is no `out-of-scope` row and no `deferred` row.
Rows moved out of `inert`: none (the earlier passes' reasons are not used).
Rows left `inert`: 24, all reason 1 (the file header, the chapter heading, three section headings, and 19 Article headings).
Rows `repealed or blank in this text`: 3 (Art 72(2)(b)(7), footnote 3; Art 81(1)(b)(4), footnote 22; Art 83(s)(1), footnote 44).

| unit | text lines | German text begins | disposition | modules | assertions + traces | seat questions |
| --- | --- | --- | --- | --- | --- | --- |
| file header | 1-5 | Schweizerisches Bundesrecht, SR 173.110: chapter 3 (Art. 72  | inert: reason 1, the file header and source note |  |  |  |
| Kapitel 3 | 7 | 3. Kapitel: Das Bundesgericht als ordentliche Beschwerdeinst | inert: reason 1, a heading |  |  |  |
| Abschnitt 1 | 8 | 1. Abschnitt: Beschwerde in Zivilsachen | inert: reason 1, a heading |  |  |  |
| Art 72 heading | 10 | Art. 72 Grundsatz | inert: reason 1, a heading |  |  |  |
| Art 72(1) | 11 | Das Bundesgericht beurteilt Beschwerden gegen Entscheide in  | encoded | civil | 6 | Art 72 |
| Art 72(2) | 12 | Der Beschwerde in Zivilsachen unterliegen auch: | encoded | civil | 8 | Art 72 |
| Art 72(2)(a) | 13 | Entscheide in Schuldbetreibungs- und Konkurssachen; | encoded | civil | 2 | Art 72 |
| Art 72(2)(b) | 14 | öffentlich-rechtliche Entscheide, die in unmittelbarem Zusam | fork F1 | civil | 6 | Art 72 |
| Art 72(2)(b)(1) | 15 | über die Anerkennung und Vollstreckung von Entscheiden und ü | encoded | civil | 3 | Art 72 |
| Art 72(2)(b)(2) | 16 | über die Führung des Grundbuchs, des Zivilstands- und des Ha | encoded | civil | 3 | Art 72 |
| Art 72(2)(b)(3) | 17 | über die Bewilligung zur Namensänderung, | encoded | civil | 3 | Art 72 |
| Art 72(2)(b)(4) | 18 | auf dem Gebiet der Aufsicht über die Stiftungen mit Ausnahme | encoded | civil | 4 | Art 72 |
| Art 72(2)(b)(5) | 19 (+fn 1) | auf dem Gebiet der Aufsicht über die Willensvollstrecker und | encoded | civil | 3 | Art 72 |
| Art 72(2)(b)(6) | 20 (+fn 2) | auf dem Gebiet des Kindes- und Erwachsenenschutzes, | encoded | civil | 3 | Art 72 |
| Art 72(2)(b)(7) | 21 (+fn 3) | … | repealed or blank in this text: shown as an ellipsis, with a footnote saying it is repealed |  |  |  |
| Art 73 heading | 23 | Art. 73 Ausnahme | inert: reason 1, a heading |  |  |  |
| Art 73 | 24 | Die Beschwerde ist unzulässig gegen Entscheide, die im Rahme | encoded | civil | 2 | Art 73 |
| Art 74 heading | 26 | Art. 74 Streitwertgrenze | inert: reason 1, a heading |  |  |  |
| Art 74(1) | 27 | In vermögensrechtlichen Angelegenheiten ist die Beschwerde n | fork F18 | civil | 7 | Art 74(1), Art 74(2) |
| Art 74(1)(a) | 28 | 15 000 Franken in arbeits- und mietrechtlichen Fällen; | fork F18 | civil | 8 | Art 74(1), Art 74(2) |
| Art 74(1)(b) | 29 | 30 000 Franken in allen übrigen Fällen. | fork F18 | civil | 5 | Art 74(1), Art 74(2) |
| Art 74(2) | 30 | Erreicht der Streitwert den massgebenden Betrag nach Absatz  | fork F2 | civil | 10 | Art 74(2) |
| Art 74(2)(a) | 31 | wenn sich eine Rechtsfrage von grundsätzlicher Bedeutung ste | encoded | civil | 2 | Art 74(2) |
| Art 74(2)(b) | 32 (+fn 4) | wenn ein Bundesgesetz eine einzige kantonale Instanz vorsieh | encoded | civil | 2 | Art 74(2) |
| Art 74(2)(c) | 33 | gegen Entscheide der kantonalen Aufsichtsbehörden in Schuldb | encoded | civil | 2 | Art 74(2) |
| Art 74(2)(d) | 34 | gegen Entscheide des Konkurs- und Nachlassrichters oder der  | encoded | civil | 2 | Art 74(2) |
| Art 74(2)(e) | 35 (+fn 5) | gegen Entscheide des Bundespatentgerichts. | encoded | civil | 2 | Art 74(2) |
| Art 75 heading | 37 | Art. 75 Vorinstanzen | inert: reason 1, a heading |  |  |  |
| Art 75(1) | 38 (+fn 6) | Die Beschwerde ist zulässig gegen Entscheide letzter kantona | fork F20 | civil | 6 | Art 75(1) |
| Art 75(2) | 39 | Die Kantone setzen als letzte kantonale Instanzen obere Geri | fork F5 | civil | 9 | Art 75(2) |
| Art 75(2)(a) | 40 (+fn 7) | ein Bundesgesetz eine einzige kantonale Instanz vorsieht; | encoded | civil | 2 | Art 75(2) |
| Art 75(2)(b) | 41 | ein Fachgericht für handelsrechtliche Streitigkeiten als ein | encoded | civil | 2 | Art 75(2) |
| Art 75(2)(c) | 42 (+fn 8) | eine Klage mit einem Streitwert von mindestens 100 000 Frank | encoded | civil | 3 | Art 75(2) |
| Art 76 heading | 44 | Art. 76 Beschwerderecht | inert: reason 1, a heading |  |  |  |
| Art 76(1) | 45 | Zur Beschwerde in Zivilsachen ist berechtigt, wer: | fork F3 | civil | 5 | Art 76(1) |
| Art 76(1)(a) | 46 | vor der Vorinstanz am Verfahren teilgenommen hat oder keine  | fork F3 | civil | 3 | Art 76(1) |
| Art 76(1)(b) | 47 (+fn 9) | durch den angefochtenen Entscheid besonders berührt ist und  | fork F3 | civil | 3 | Art 76(1) |
| Art 76(2) | 48 (+fn 10) | Gegen Entscheide nach Artikel 72 Absatz 2 steht das Beschwer | fork F3 | civil | 5 |  |
| Art 77 heading | 50 (+fn 11) | Art. 77 Schiedsgerichtsbarkeit[^11] | inert: reason 1, a heading |  |  |  |
| Art 77(1) | 51 (+fn 12) | Die Beschwerde in Zivilsachen ist ungeachtet des Streitwerts | encoded | civil | 4 | Art 77(1) |
| Art 77(1)(a) | 52 (+fn 13) | in der internationalen Schiedsgerichtsbarkeit unter den Vora | fork F14 | civil | 4 | Art 77(1) |
| Art 77(1)(b) | 53 (+fn 14,15) | in der nationalen Schiedsgerichtsbarkeit unter den Vorausset | fork F14 | civil | 4 | Art 77(1) |
| Art 77(2) | 54 (+fn 16) | Die Artikel 48 Absatz 3, 90–98, 103 Absatz 2, 105 Absatz 2,  | fork F6 | civil | 17 | Art 77(2) |
| Art 77(2bis) | 55 (+fn 17) | Rechtsschriften können in englischer Sprache abgefasst werde | fork F6 | civil | 2 | Art 77(2bis) |
| Art 77(3) | 56 | Das Bundesgericht prüft nur Rügen, die in der Beschwerde vor | fork F6 | civil | 4 | Art 77(3) |
| Abschnitt 2 | 58 | 2. Abschnitt: Beschwerde in Strafsachen | inert: reason 1, a heading |  |  |  |
| Art 78 heading | 60 | Art. 78 Grundsatz | inert: reason 1, a heading |  |  |  |
| Art 78(1) | 61 | Das Bundesgericht beurteilt Beschwerden gegen Entscheide in  | encoded | criminal | 7 | Art 78 |
| Art 78(2) | 62 | Der Beschwerde in Strafsachen unterliegen auch Entscheide üb | fork F7 | criminal | 10 | Art 78 |
| Art 78(2)(a) | 63 | Zivilansprüche, wenn diese zusammen mit der Strafsache zu be | fork F7 | criminal | 4 | Art 78 |
| Art 78(2)(b) | 64 | den Vollzug von Strafen und Massnahmen. | encoded | criminal | 2 | Art 78 |
| Art 79 heading | 66 | Art. 79 Ausnahme | inert: reason 1, a heading |  |  |  |
| Art 79 | 67 | Die Beschwerde ist unzulässig gegen Entscheide der Beschwerd | fork F4 F21 | criminal | 5 | Art 79 |
| Art 80 heading | 69 | Art. 80 Vorinstanzen | inert: reason 1, a heading |  |  |  |
| Art 80(1) | 70 (+fn 18) | Die Beschwerde ist zulässig gegen Entscheide letzter kantona | fork F4 F20 | criminal | 6 | Art 80(1) |
| Art 80(2) | 71 (+fn 19,20) | Die Kantone setzen als letzte kantonale Instanzen obere Geri | fork F5 | criminal | 6 | Art 80(2) |
| Art 81 heading | 73 | Art. 81 Beschwerderecht | inert: reason 1, a heading |  |  |  |
| Art 81(1) | 74 | Zur Beschwerde in Strafsachen ist berechtigt, wer: | fork F3 | criminal | 4 | Art 81(1) |
| Art 81(1)(a) | 75 | vor der Vorinstanz am Verfahren teilgenommen hat oder keine  | fork F3 | criminal | 3 | Art 81(1) |
| Art 81(1)(b) | 76 | ein rechtlich geschütztes Interesse an der Aufhebung oder Än | fork F3 | criminal | 11 | Art 81(1) |
| Art 81(1)(b)(1) | 77 | die beschuldigte Person, | encoded | criminal | 2 | Art 81(1) |
| Art 81(1)(b)(2) | 78 | ihr gesetzlicher Vertreter oder ihre gesetzliche Vertreterin | encoded | criminal | 2 | Art 81(1) |
| Art 81(1)(b)(3) | 79 (+fn 21) | die Staatsanwaltschaft, ausser bei Entscheiden über die Anor | fork F15 | criminal | 3 | Art 81(1) |
| Art 81(1)(b)(4) | 80 (+fn 22) | … | repealed or blank in this text: shown as an ellipsis, with a footnote saying it is repealed |  |  |  |
| Art 81(1)(b)(5) | 81 (+fn 23) | die Privatklägerschaft, wenn der angefochtene Entscheid sich | encoded | criminal | 3 | Art 81(1) |
| Art 81(1)(b)(6) | 82 | die Person, die den Strafantrag stellt, soweit es um das Str | encoded | criminal | 3 | Art 81(1) |
| Art 81(1)(b)(7) | 83 (+fn 24,25) | die Staatsanwaltschaft des Bundes und die beteiligte Verwalt | encoded | criminal | 2 | Art 81(1) |
| Art 81(2) | 84 (+fn 26) | Eine Bundesbehörde ist zur Beschwerde berechtigt, wenn das B | fork F3 | criminal | 3 |  |
| Art 81(3) | 85 | Gegen Entscheide nach Artikel 78 Absatz 2 Buchstabe b steht  | fork F3 | criminal | 5 |  |
| Abschnitt 3 | 87 | 3. Abschnitt: Beschwerde in öffentlich-rechtlichen Angelegen | inert: reason 1, a heading |  |  |  |
| Art 82 heading | 89 | Art. 82 Grundsatz | inert: reason 1, a heading |  |  |  |
| Art 82 | 90 | Das Bundesgericht beurteilt Beschwerden: | encoded | public-scope | 4 | Art 82 |
| Art 82(a) | 91 | gegen Entscheide in Angelegenheiten des öffentlichen Rechts; | encoded | public-scope | 2 | Art 82 |
| Art 82(b) | 92 | gegen kantonale Erlasse; | encoded | public-scope | 2 | Art 82 |
| Art 82(c) | 93 | betreffend die politische Stimmberechtigung der Bürger und B | encoded | public-scope | 4 | Art 82 |
| Art 83 heading | 95 | Art. 83 Ausnahmen | inert: reason 1, a heading |  |  |  |
| Art 83 | 96 | Die Beschwerde ist unzulässig gegen: | fork F10 | public-scope | 71 | Art 83 |
| Art 83(a) | 97 | Entscheide auf dem Gebiet der inneren oder äusseren Sicherhe | fork F21 | public-scope | 3 | Art 83 |
| Art 83(b) | 98 | Entscheide über die ordentliche Einbürgerung; | encoded | public-scope | 2 | Art 83 |
| Art 83(c) | 99 | Entscheide auf dem Gebiet des Ausländerrechts betreffend: | encoded (through its sub-items) | public-scope | 15 | Art 83 |
| Art 83(c)(1) | 100 | die Einreise, | encoded | public-scope | 3 | Art 83 |
| Art 83(c)(2) | 101 | Bewilligungen, auf die weder das Bundesrecht noch das Völker | fork F21 | public-scope | 4 | Art 83 |
| Art 83(c)(3) | 102 | die vorläufige Aufnahme, | encoded | public-scope | 2 | Art 83 |
| Art 83(c)(4) | 103 | die Ausweisung gestützt auf Artikel 121 Absatz 2 der Bundesv | fork F8 | public-scope | 2 | Art 83 |
| Art 83(c)(5) | 104 (+fn 27) | Abweichungen von den Zulassungsvoraussetzungen, | encoded | public-scope | 2 | Art 83 |
| Art 83(c)(6) | 105 (+fn 28) | die Verlängerung der Grenzgängerbewilligung, den Kantonswech | encoded | public-scope | 2 | Art 83 |
| Art 83(d) | 106 | Entscheide auf dem Gebiet des Asyls, die: | encoded (through its sub-items) | public-scope | 7 | Art 83 |
| Art 83(d)(1) | 107 (+fn 29) | vom Bundesverwaltungsgericht getroffen worden sind, ausser s | fork F21 | public-scope | 4 | Art 83 |
| Art 83(d)(2) | 108 | von einer kantonalen Vorinstanz getroffen worden sind und ei | fork F21 | public-scope | 3 | Art 83 |
| Art 83(e) | 109 | Entscheide über die Verweigerung der Ermächtigung zur Strafv | encoded | public-scope | 2 | Art 83 |
| Art 83(f) | 110 (+fn 30) | Entscheide auf dem Gebiet der öffentlichen Beschaffungen, we | fork F9 | public-scope | 5 | Art 83 |
| Art 83(f)(1) | 111 | sich keine Rechtsfrage von grundsätzlicher Bedeutung stellt; | fork F9 | public-scope | 4 | Art 83 |
| Art 83(f)(2) | 112 (+fn 31) | der geschätzte Wert des zu vergebenden Auftrags den massgebe | encoded | public-scope | 4 | Art 83 |
| Art 83(fbis) | 113 (+fn 32,33) | Entscheide des Bundesverwaltungsgerichts über Verfügungen na | encoded | public-scope | 3 | Art 83 |
| Art 83(g) | 114 | Entscheide auf dem Gebiet der öffentlich-rechtlichen Arbeits | fork F21 | public-scope | 4 | Art 83 |
| Art 83(h) | 115 (+fn 34) | Entscheide auf dem Gebiet der internationalen Amtshilfe, mit | fork F21 | public-scope | 3 | Art 83 |
| Art 83(i) | 116 | Entscheide auf dem Gebiet des Militär-, Zivil- und Zivilschu | encoded | public-scope | 2 | Art 83 |
| Art 83(j) | 117 (+fn 35) | Entscheide auf dem Gebiet der wirtschaftlichen Landesversorg | encoded | public-scope | 3 | Art 83 |
| Art 83(k) | 118 | Entscheide betreffend Subventionen, auf die kein Anspruch be | encoded | public-scope | 3 | Art 83 |
| Art 83(l) | 119 | Entscheide über die Zollveranlagung, wenn diese auf Grund de | encoded | public-scope | 3 | Art 83 |
| Art 83(m) | 120 (+fn 36) | Entscheide über die Stundung oder den Erlass von Abgaben; in | fork F16 | public-scope | 6 | Art 83 |
| Art 83(n) | 121 | Entscheide auf dem Gebiet der Kernenergie betreffend: | encoded (through its sub-items) | public-scope | 6 | Art 83 |
| Art 83(n)(1) | 122 | das Erfordernis einer Freigabe oder der Änderung einer Bewil | encoded | public-scope | 2 | Art 83 |
| Art 83(n)(2) | 123 | die Genehmigung eines Plans für Rückstellungen für die vor A | encoded | public-scope | 2 | Art 83 |
| Art 83(n)(3) | 124 | Freigaben; | encoded | public-scope | 2 | Art 83 |
| Art 83(o) | 125 | Entscheide über die Typengenehmigung von Fahrzeugen auf dem  | encoded | public-scope | 2 | Art 83 |
| Art 83(p) | 126 (+fn 37,38) | Entscheide des Bundesverwaltungsgerichts auf dem Gebiet des  | encoded (through its sub-items) | public-scope | 7 | Art 83 |
| Art 83(p)(1) | 127 | Konzessionen, die Gegenstand einer öffentlichen Ausschreibun | encoded | public-scope | 3 | Art 83 |
| Art 83(p)(2) | 128 (+fn 39) | Streitigkeiten nach Artikel 11a des Fernmeldegesetzes vom 30 | encoded | public-scope | 2 | Art 83 |
| Art 83(p)(3) | 129 (+fn 40,41) | Streitigkeiten nach Artikel 8 des Postgesetzes vom 17. Dezem | encoded | public-scope | 2 | Art 83 |
| Art 83(q) | 130 | Entscheide auf dem Gebiet der Transplantationsmedizin betref | encoded (through its sub-items) | public-scope | 4 | Art 83 |
| Art 83(q)(1) | 131 | die Aufnahme in die Warteliste, | encoded | public-scope | 2 | Art 83 |
| Art 83(q)(2) | 132 | die Zuteilung von Organen; | encoded | public-scope | 2 | Art 83 |
| Art 83(r) | 133 (+fn 42,43) | Entscheide auf dem Gebiet der Krankenversicherung, die das B | fork F13 | public-scope | 3 | Art 83 |
| Art 83(s) | 134 | Entscheide auf dem Gebiet der Landwirtschaft betreffend: | encoded (through its sub-items) | public-scope | 2 | Art 83 |
| Art 83(s)(1) | 135 (+fn 44) | … | repealed or blank in this text: shown as an ellipsis, with a footnote saying it is repealed |  |  |  |
| Art 83(s)(2) | 136 | die Abgrenzung der Zonen im Rahmen des Produktionskatasters; | encoded | public-scope | 2 | Art 83 |
| Art 83(t) | 137 | Entscheide über das Ergebnis von Prüfungen und anderen Fähig | encoded | public-scope | 2 | Art 83 |
| Art 83(u) | 138 (+fn 45,46) | Entscheide auf dem Gebiet der öffentlichen Kaufangebote (Art | encoded | public-scope | 2 | Art 83 |
| Art 83(v) | 139 (+fn 47) | Entscheide des Bundesverwaltungsgerichts über Meinungsversch | encoded | public-scope | 2 | Art 83 |
| Art 83(w) | 140 (+fn 48) | Entscheide auf dem Gebiet des Elektrizitätsrechts betreffend | encoded | public-scope | 3 | Art 83 |
| Art 83(x) | 141 (+fn 49,50) | Entscheide betreffend die Gewährung von Solidaritätsbeiträge | fork F21 | public-scope | 4 | Art 83 |
| Art 83(y) | 142 (+fn 51) | Entscheide des Bundesverwaltungsgerichts in Verständigungsve | encoded | public-scope | 2 | Art 83 |
| Art 83(z) | 143 (+fn 52,53) | Entscheide betreffend die in Artikel 71c Absatz 1 Buchstabe  | encoded | public-scope | 3 | Art 83 |
| Art 83(zbis) | 144 (+fn 54,55) | Entscheide über die Gewährung von Wasserrechtskonzessionen f | encoded | public-scope | 3 | Art 83 |
| Art 83(zter) | 145 (+fn 56,57,58,59) | Entscheide über Beschwerden von Organisationen nach den Arti | encoded | public-scope | 2 | Art 83 |
| Art 84 heading | 147 | Art. 84 Internationale Rechtshilfe in Strafsachen | inert: reason 1, a heading |  |  |  |
| Art 84(1) | 148 | Gegen einen Entscheid auf dem Gebiet der internationalen Rec | fork F17 | public-limits | 7 | Art 84(1) |
| Art 84(2) | 149 | Ein besonders bedeutender Fall liegt insbesondere vor, wenn  | encoded | public-limits | 3 | Art 84(1), Art 84a |
| Art 84a heading | 151 (+fn 60) | Art. 84a[^60] Internationale Amtshilfe in Steuersachen | inert: reason 1, a heading |  |  |  |
| Art 84a | 152 | Gegen einen Entscheid auf dem Gebiet der internationalen Amt | fork F17 | public-limits | 6 | Art 84a |
| Art 85 heading | 154 | Art. 85 Streitwertgrenzen | inert: reason 1, a heading |  |  |  |
| Art 85(1) | 155 | In vermögensrechtlichen Angelegenheiten ist die Beschwerde u | fork F18 | public-limits | 8 | Art 85(1), Art 85(2) |
| Art 85(1)(a) | 156 | auf dem Gebiet der Staatshaftung, wenn der Streitwert wenige | fork F18 | public-limits | 5 | Art 85(1), Art 85(2) |
| Art 85(1)(b) | 157 | auf dem Gebiet der öffentlich-rechtlichen Arbeitsverhältniss | fork F18 | public-limits | 4 | Art 85(1), Art 85(2) |
| Art 85(2) | 158 | Erreicht der Streitwert den massgebenden Betrag nach Absatz  | fork F2 | public-limits | 6 | Art 85(2) |
| Art 86 heading | 160 | Art. 86 Vorinstanzen im Allgemeinen | inert: reason 1, a heading |  |  |  |
| Art 86(1) | 161 | Die Beschwerde ist zulässig gegen Entscheide: | fork F20 | public-courts | 7 | Art 86(1) |
| Art 86(1)(a) | 162 | des Bundesverwaltungsgerichts; | encoded | public-courts | 2 | Art 86(1) |
| Art 86(1)(b) | 163 | des Bundesstrafgerichts; | encoded | public-courts | 4 | Art 86(1) |
| Art 86(1)(c) | 164 | der unabhängigen Beschwerdeinstanz für Radio und Fernsehen; | encoded | public-courts | 2 | Art 86(1) |
| Art 86(1)(d) | 165 | letzter kantonaler Instanzen, sofern nicht die Beschwerde an | fork F11 | public-courts | 4 | Art 86(1) |
| Art 86(2) | 166 | Die Kantone setzen als unmittelbare Vorinstanzen des Bundesg | fork F5 | public-courts | 5 | Art 86(2) |
| Art 86(3) | 167 | Für Entscheide mit vorwiegend politischem Charakter können d | fork F12 | public-courts | 4 | Art 86(3) |
| Art 87 heading | 169 | Art. 87 Vorinstanzen bei Beschwerden gegen Erlasse | inert: reason 1, a heading |  |  |  |
| Art 87(1) | 170 | Gegen kantonale Erlasse ist unmittelbar die Beschwerde zuläs | fork F11 | public-courts | 3 | Art 87(1) |
| Art 87(2) | 171 | Soweit das kantonale Recht ein Rechtsmittel gegen Erlasse vo | encoded | public-courts | 3 | Art 87(2) |
| Art 88 heading | 173 | Art. 88 Vorinstanzen in Stimmrechtssachen | inert: reason 1, a heading |  |  |  |
| Art 88(1) | 174 | Beschwerden betreffend die politische Stimmberechtigung der  | fork F20 | public-courts | 3 | Art 88(1) |
| Art 88(1)(a) | 175 | in kantonalen Angelegenheiten gegen Akte letzter kantonaler  | encoded | public-courts | 4 | Art 88(1) |
| Art 88(1)(b) | 176 | in eidgenössischen Angelegenheiten gegen Verfügungen der Bun | encoded | public-courts | 5 | Art 88(1) |
| Art 88(2) | 177 | Die Kantone sehen gegen behördliche Akte, welche die politis | fork F19 | public-courts | 6 | Art 88(2) |
| Art 89 heading | 179 | Art. 89 Beschwerderecht | inert: reason 1, a heading |  |  |  |
| Art 89(1) | 180 | Zur Beschwerde in öffentlich-rechtlichen Angelegenheiten ist | fork F3 | public-courts | 5 | Art 89(1) |
| Art 89(1)(a) | 181 | vor der Vorinstanz am Verfahren teilgenommen hat oder keine  | fork F3 | public-courts | 3 | Art 89(1) |
| Art 89(1)(b) | 182 | durch den angefochtenen Entscheid oder Erlass besonders berü | fork F3 | public-courts | 2 | Art 89(1) |
| Art 89(1)(c) | 183 | ein schutzwürdiges Interesse an dessen Aufhebung oder Änderu | fork F3 | public-courts | 2 | Art 89(1) |
| Art 89(2) | 184 | Zur Beschwerde sind ferner berechtigt: | encoded (through its sub-items) | public-courts | 12 | Art 89(2)(c), Art 89(2)(d) |
| Art 89(2)(a) | 185 | die Bundeskanzlei, die Departemente des Bundes oder, soweit  | fork F3 | public-courts | 4 |  |
| Art 89(2)(b) | 186 | das zuständige Organ der Bundesversammlung auf dem Gebiet de | encoded | public-courts | 3 |  |
| Art 89(2)(c) | 187 | Gemeinden und andere öffentlich-rechtliche Körperschaften, w | fork F3 | public-courts | 3 | Art 89(2)(c) |
| Art 89(2)(d) | 188 | Personen, Organisationen und Behörden, denen ein anderes Bun | encoded | public-courts | 2 | Art 89(2)(d) |
| Art 89(3) | 189 | In Stimmrechtssachen (Art. 82 Bst. c) steht das Beschwerdere | encoded | public-courts | 3 | Art 89(3) |

## Fork register

Each entry is a place where the text can be read two or more ways with different outcomes.
Each gives the readings, the text that licenses each, the one taken, and the rule that encodes it.
The coverage table marks the rows each fork covers; a `.l4` file carries `(fork F#)` beside the branch.
The rulings cited are in the brief: the rule of 2026-10-29 and the rulings of 2026-11-04, 2026-11-05 and 2026-11-12 on negatives and legal effects.
E1 (option C: per-section answers, no gathering across sections) and N2 (a flat negative counts as the text's no) are applied throughout.

- **F1. Art 72(2)(b), the 'insbesondere' list and the pension carve-out.**
  Text: "öffentlich-rechtliche Entscheide, die in unmittelbarem Zusammenhang mit Zivilrecht stehen, insbesondere Entscheide: ...", and item 4 "auf dem Gebiet der Aufsicht über die Stiftungen mit Ausnahme der Vorsorge- und Freizügigkeitseinrichtungen".
  Readings: (i) the test is the immediate connection with civil law, which the person states, and the six items are examples that also give yes; a public-law decision outside both answers `NOTHING`; (ii) the six items are the whole of the category, so a public-law decision outside them is `JUST FALSE`.
  Taken: (i), because "insbesondere" does not close the list (NOTHING-kind: includes).
  The same reading keeps a pension institution's decision as `NOTHING` unless the person states an immediate connection with civil law, in which case the chapeau gives `JUST TRUE`; (ii) would make it `JUST FALSE`.
  Rule: `Art 72(2)(b)`, with items `Art 72(2)(b)(1)` to `(6)` in `bgg3-civil.l4`.
- **F2. Art 74(2) and Art 85(2), no limb holds although the value is short.**
  Text: "Erreicht der Streitwert den massgebenden Betrag nach Absatz 1 nicht, so ist die Beschwerde dennoch zulässig: ..." (Art 74(2), five limbs); "... so ist die Beschwerde dennoch zulässig, wenn sich eine Rechtsfrage von grundsätzlicher Bedeutung stellt" (Art 85(2)).
  Readings: (i) the subsection gives no saving on these facts, so `JUST FALSE`, in the manner of the 'no defence on these facts' ruling of 2026-11-05 (b); (ii) `NOTHING`, because the subsection grants and its list does not close.
  Taken: (i), flagged; the answer when the value reaches the amount is `NOTHING` either way (the subsection is not engaged).
  Rule: `Art 74(2)` in `bgg3-civil.l4`, `Art 85(2)` in `bgg3-public-limits.l4`.
- **F3. Functions named 'entitled' and the 'wenn' gates of standing.**
  Text: "Zur Beschwerde in Zivilsachen ist berechtigt, wer: a. ...; und b. ..." (Art 76(1)); the same shape in Art 81(1) and 89(1); "wenn der angefochtene Entscheid die Bundesgesetzgebung in ihrem Aufgabenbereich verletzen kann" (Art 76(2), 81(3), 89(2)(a)); "Eine Bundesbehörde ist zur Beschwerde berechtigt, wenn das Bundesrecht vorsieht, dass ihr der Entscheid mitzuteilen ist" (Art 81(2)); "wenn sie die Verletzung von Garantien rügen" (Art 89(2)(c)).
  Readings: (i) where a stated condition fails the provision's own question is answered `JUST FALSE` (the rule of 2026-10-29, reading (a)); (ii) `NOTHING`, because an entitlement is a claim and the 2026-11-12 ruling does not settle it.
  Taken: (i), listed as the ruling of 2026-11-12 (limb 3) requires; not changed.
  Rule: every function in the F3 rows of the coverage table.
- **F4. Art 79 and Art 80(1), the Complaints Chamber.**
  Text: Art 80(1) "Die Beschwerde ist zulässig gegen Entscheide letzter kantonaler Instanzen und gegen Entscheide der Beschwerdekammer und der Berufungskammer des Bundesstrafgerichts"; Art 79 "Die Beschwerde ist unzulässig gegen Entscheide der Beschwerdekammer des Bundesstrafgerichts, soweit es sich nicht um Entscheide über Zwangsmassnahmen handelt".
  Readings: (i) each section answers for itself: Art 80(1) says `JUST TRUE` for the Complaints Chamber, Art 79 says `JUST FALSE` for a decision that is not on a coercive measure, and nothing gathers the two; (ii) Art 79 as the specific rule prevails, so the combined answer for such a decision is `JUST FALSE`.
  Taken: (i), by E1 option C.
  Rule: `Art 79` and `Art 80(1)` in `bgg3-criminal.l4`.
- **F5. Art 75(2), 80(2), 86(2): a duty not done.**
  Text: "Die Kantone setzen als letzte kantonale Instanzen obere Gerichte ein. Diese entscheiden als Rechtsmittelinstanzen; ausgenommen sind die Fälle, in denen: ..." and the parallel texts.
  Readings: (i) a duty on the cantons whose breach the text gives no consequence for the person: where the last instance is not an upper court deciding on appeal and no exception applies, `NOTHING`; (ii) `JUST FALSE`: the appeal is not admissible then.
  Taken: (i), because the text states no consequence (a bare 'must' not done: the 2026-11-05 decision case by case).
  The duty is also a regulative rule with no deadline, because the text states none.
  Rule: the three functions and the three duties in `bgg3-civil.l4`, `bgg3-criminal.l4` and `bgg3-public-courts.l4`.
- **F6. Art 77(2), 77(2bis), 77(3): to which appeals they speak.**
  Text: "Die Artikel 48 Absatz 3, 90–98, 103 Absatz 2, 105 Absatz 2, 106 Absatz 1 sowie 107 Absatz 2, soweit dieser dem Bundesgericht erlaubt, in der Sache selbst zu entscheiden, sind in diesen Fällen nicht anwendbar"; "Rechtsschriften können in englischer Sprache abgefasst werden"; "Das Bundesgericht prüft nur Rügen, die in der Beschwerde vorgebracht und begründet worden sind".
  Readings: (i) the paragraphs stand in Art 77 and speak of the appeals in Art 77(1) only; outside them `NOTHING`; (ii) Art 77(3) (which does not say 'in diesen Fällen') is a general rule for appeals in civil matters.
  Taken: (i).
  Rule: `Art 77(2)`, `Art 77(2bis)`, `Art 77(3)` in `bgg3-civil.l4`.
- **F7. Art 78(2)(a), civil claims 'wenn' dealt with together.**
  Text: "Zivilansprüche, wenn diese zusammen mit der Strafsache zu behandeln sind".
  Readings: (i) a failed 'wenn' is the text's no (`JUST FALSE`); (ii) `NOTHING`, a grant limited by its own wording.
  Taken: (i), the rule of 2026-10-29 reading (a); flagged.
  Rule: `Art 78(2)(a)` and `Art 78(2)` in `bgg3-criminal.l4`.
- **F8. Art 83(c)(4), 'und' between expulsion and removal.**
  Text: "die Ausweisung gestützt auf Artikel 121 Absatz 2 der Bundesverfassung und die Wegweisung".
  Readings: (i) the two are alternatives, so a decision on either is within the limb; (ii) the limb reaches only a decision that is both.
  Taken: (i), because an expulsion under the Constitution and a removal are different decisions.
  Rule: `Art 83(c)(4)` in `bgg3-public-scope.l4`.
- **F9. Art 83(f)(1), the reservation for certain procuring bodies.**
  Text: "sich keine Rechtsfrage von grundsätzlicher Bedeutung stellt; vorbehalten bleiben Beschwerden gegen Beschaffungen des Bundesverwaltungsgerichts, des Bundesstrafgerichts, des Bundespatentgerichts, der Bundesanwaltschaft sowie der oberen kantonalen Gerichtsinstanzen, oder" then item 2 on the threshold.
  Readings: (i) the reservation sits inside item 1 and lifts only item 1's bar; a reserved body's procurement below the threshold is still barred by item 2; (ii) the reservation lifts the whole limb (f).
  Taken: (i).
  Rule: `Art 83(f)(1)` and `Art 83(f)` in `bgg3-public-scope.l4`.
- **F10. Art 83, a decision that fits two limbs.**
  Text: the list a to zter.
  Readings: (i) the dispatcher takes one kind of decision, so one limb answers; (ii) all limbs that fit would be combined, and a bar from any one would settle it.
  Taken: (i), by E1 option C; the person chooses the kind.
  Rule: `Art 83` in `bgg3-public-scope.l4`.
- **F11. Art 86(1)(d) and Art 87(1), 'sofern'.**
  Text: "letzter kantonaler Instanzen, sofern nicht die Beschwerde an das Bundesverwaltungsgericht zulässig ist"; "Gegen kantonale Erlasse ist unmittelbar die Beschwerde zulässig, sofern kein kantonales Rechtsmittel ergriffen werden kann".
  Readings: (i) a failed 'sofern' gate answers `JUST FALSE` ('provided that' is one of the plain variants of 'if'); (ii) `NOTHING`, because both are grants ("ist die Beschwerde zulässig") and the ruling of 2026-11-12 lists but does not change gates of this kind.
  Taken: (i).
  Rule: `Art 86(1)(d)` and `Art 87(1)` in `bgg3-public-courts.l4`.
- **F12. Art 86(3), a power whose gate fails.**
  Text: "Für Entscheide mit vorwiegend politischem Charakter können die Kantone anstelle eines Gerichts eine andere Behörde als unmittelbare Vorinstanz des Bundesgerichts einsetzen".
  Readings: (i) `NOTHING`, because a function named for a power whose gate fails is not a 'may not' (the ruling of 2026-11-12, limb 1); (ii) `JUST FALSE`.
  Taken: (i).
  Rule: `Art 86(3)` function and permission in `bgg3-public-courts.l4`.
- **F13. Art 83(r), a limb that cites an article the text's footnote calls repealed.**
  Text: "gestützt auf Artikel 34 des Verwaltungsgerichtsgesetzes vom 17. Juni 2005 (VGG)" and footnote 43 "Dieser Art. ist aufgehoben".
  Readings: (i) encode the limb as printed: the person says whether the decision was taken under Art 34; (ii) treat the limb as spent, because the footnote names Art. 33 Bst. i VGG with Art. 53 Abs. 1 of the health insurance Act as the provision now.
  Taken: (i), since the VGG is outside the sources and the footnote is not operative text.
  Rule: `Art 83(r)` in `bgg3-public-scope.l4`.
- **F14. Art 77(1)(a) and (b), conditions in two other statutes.**
  Text: "unter den Voraussetzungen der Artikel 190–192" and "unter den Voraussetzungen der Artikel 389–395".
  Readings: (i) the conditions are facts the person states; where they are not met the limb answers `NOTHING` (a grant limited by its own wording, the conditions being in another Act); (ii) `JUST FALSE`.
  Taken: (i).
  Rule: `Art 77(1)(a)` and `Art 77(1)(b)` in `bgg3-civil.l4`.
- **F15. Art 81(1)(b)(3), the prosecutor and detention decisions.**
  Text: "die Staatsanwaltschaft, ausser bei Entscheiden über die Anordnung, die Verlängerung und die Aufhebung der Untersuchungs- und Sicherheitshaft".
  Readings: (i) the carve-out only means that item 3 gives the prosecutor no interest on such decisions; the prosecutor may still state a legally protected interest of its own under the chapeau; (ii) on such decisions the prosecutor has no standing at all.
  Taken: (i), because the list is introduced by "insbesondere".
  Rule: `Art 81(1)(b)(3)` and `Art 81(1)(b)` in `bgg3-criminal.l4`.
- **F16. Art 83(m), the departure.**
  Text: "Entscheide über die Stundung oder den Erlass von Abgaben; in Abweichung davon ist die Beschwerde zulässig gegen Entscheide über den Erlass der direkten Bundessteuer oder der kantonalen oder kommunalen Einkommens- und Gewinnsteuer, wenn sich eine Rechtsfrage von grundsätzlicher Bedeutung stellt oder es sich aus anderen Gründen um einen besonders bedeutenden Fall handelt".
  Readings: (i) where the departure's conditions fail, the bar stands: `JUST FALSE`; (ii) `NOTHING`, because the departure is a grant limited by its own wording.
  Taken: (i), because the first half of the limb is a flat bar on every deferral or remission decision and the departure only lifts it.
  Rule: `Art 83(m)` in `bgg3-public-scope.l4`.
- **F17. Art 84(1) and Art 84a, 'nur zulässig, wenn'.**
  Text: "ist die Beschwerde nur zulässig, wenn er eine Auslieferung, eine Beschlagnahme, ... betrifft und es sich um einen besonders bedeutenden Fall handelt" and Art 84a.
  Readings: (i) the function answers whether the stated condition is met (`JUST TRUE`) or the 'nur' fails (`JUST FALSE`) and is named for that, not for admissibility as a whole, because other provisions also bear on admissibility (Art 83(h), Art 85); (ii) a function named 'the appeal is admissible' that claims more than the text says.
  Taken: (i).
  The terms "besonders bedeutender Fall" and "Rechtsfrage von grundsätzlicher Bedeutung" are open-textured and are inputs; Art 84(2) says what a particularly important case includes ("insbesondere") and so does not close the list.
  Rule: `Art 84(1)`, `Art 84(2)` and `Art 84a` in `bgg3-public-limits.l4`.
- **F18. Art 74(1) and Art 85(1), the scope of the value limit.**
  Text: "In vermögensrechtlichen Angelegenheiten ist die Beschwerde nur zulässig, wenn der Streitwert mindestens beträgt: ..." and "In vermögensrechtlichen Angelegenheiten ist die Beschwerde unzulässig: ...".
  Readings: (i) outside a pecuniary matter the limit is not engaged and the answer is `NOTHING` (periods ruling (c): a scope limit); (ii) `JUST FALSE` or `JUST TRUE` for non-pecuniary matters.
  Taken: (i).
  The value in dispute ("Streitwert") is a number the person states; how it is worked out is in chapter 4, outside the sources.
  Rule: `Art 74(1)`, `Art 74(1)(a)`, `Art 74(1)(b)`, `Art 85(1)`, `Art 85(1)(a)`, `Art 85(1)(b)`.
- **F19. Art 88(2), the duty and its exclusion.**
  Text: "Die Kantone sehen gegen behördliche Akte, welche die politischen Rechte der Stimmberechtigten in kantonalen Angelegenheiten verletzen können, ein Rechtsmittel vor. Diese Pflicht erstreckt sich nicht auf Akte des Parlaments und der Regierung".
  Readings: (i) the flat negative counts as the text's no (N2 option A): `JUST FALSE` for an act of parliament or government; (ii) `NOTHING`.
  Taken: (i), as ruled.
  Rule: `Art 88(2)` function and duty in `bgg3-public-courts.l4`.
- **F20. Art 75(1), 80(1), 86(1), 88(1), lists of bodies not closed.**
  Text: "Die Beschwerde ist zulässig gegen Entscheide letzter kantonaler Instanzen, des Bundesverwaltungsgerichts und des Bundespatentgerichts" and the parallel lists.
  Readings: (i) the list is not closed with 'nur', so a decision of another body answers `NOTHING`; (ii) `JUST FALSE`.
  Taken: (i) (NOTHING-kind: list not closed).
  Rule: the four functions.
- **F21. Bars that carry an exception.**
  Text: Art 79 "soweit es sich nicht um Entscheide über Zwangsmassnahmen handelt"; Art 83(a) "soweit das Völkerrecht nicht einen Anspruch auf gerichtliche Beurteilung einräumt"; (c)(2) and (d)(2) "auf die weder das Bundesrecht noch das Völkerrecht einen Anspruch einräumt"; (d)(1) "ausser sie betreffen Personen, gegen die ein Auslieferungsersuchen ... vorliegt"; (g) "nicht aber die Gleichstellung der Geschlechter"; (h) "mit Ausnahme der Amtshilfe in Steuersachen"; (x) "ausser wenn sich eine Rechtsfrage von grundsätzlicher Bedeutung stellt".
  Readings: (i) when the exception holds the answer is `NOTHING`: the bar does not reach the case but the text does not say the appeal is admissible; (ii) `JUST TRUE`, the appeal is admissible.
  Taken: (i), the rule of 2026-10-29 for a prohibition limited by its own wording.
  Rule: the seven functions.
- **F22. The seat's questions on the bars (Art 73, Art 79, Art 83) are asked the other way round.**
  Not a reading of the text: a decision about the seat layer.
  Layer 1 keeps the text's polarity (a bar is `JUST FALSE`); the seat question 'is my decision excluded' swaps `JUST FALSE` and `JUST TRUE` and leaves `NOTHING`.
  The alternative was to ask 'is the appeal admissible' and have the form answer 'no' for an excluded decision, which a person reads as 'I may not appeal' even where the text only says 'not decided here'.
  Art 83 was swapped when the seat was written; Art 73 and Art 79 were swapped on 2026-11-18 after an independent reader found their wording misleading.
  Rule: `Art 73 my decision is excluded from the appeal in civil matters`, `Art 79 my decision of the Complaints Chamber is excluded from the appeal in criminal matters` and `Art 83 my decision is excluded from the appeal in public-law matters` in `bgg3-seat.l4`.

## What the text turns out to say

Numbered findings; each ends 'Asserted.' where an assertion in a test file or the case file shows it, and says 'Not asserted' with the reason where nothing can be.

1. The chapter fixes only three numbers: 15 000 and 30 000 francs (Art 74(1), Art 85(1)) and 100 000 francs (Art 75(2)(c)).
   Every other number it needs (the value in dispute, the threshold under the Public Procurement Act in Art 83(f)(2)) is borrowed and asked as an input.
   Asserted.
2. Art 74(1) and Art 85(1) use the same two amounts the opposite way round: Art 74(1) puts 15 000 on employment and tenancy cases and 30 000 on all others; Art 85(1) puts 30 000 on state liability and 15 000 on public-law employment.
   Asserted.
3. The boundary wording differs: Art 74(1) says "mindestens" (the amount itself is enough) and Art 85(1) says "weniger als" (the amount itself is not below), so at exactly 15 000 or 30 000 francs neither limit stands in the way (Art 74(1) is met and Art 85(1) does not bar).
   Asserted.
4. Art 75(2)(c) says "mindestens 100 000 Franken", so 100 000 itself qualifies and 99 999 does not.
   Asserted.
5. Art 79 and Art 80(1) both speak to the Complaints Chamber of the Federal Criminal Court and point different ways; each section answers for itself and nothing here combines them (fork F4).
   Asserted.
6. Art 83 is a list of bars and only limb (m) says "zulässig" in its own words; every other limb answers `JUST FALSE` (bars) or `NOTHING` (does not reach the case), never `JUST TRUE`.
   Asserted.
7. Art 83(f) joins two bars, no legal question of fundamental importance (item 1) and a value below the threshold (item 2); the reservation for certain procuring bodies sits in item 1, so a reserved body's contract below the threshold is still barred (fork F9).
   Asserted.
8. Art 83(c)(2) and Art 83(d)(2) use the same fact, a claim under federal or international law to the permit, and the encoding asks it once.
   Asserted.
9. Art 83(h) leaves tax assistance outside the bar and Art 84a then makes an appeal in tax assistance matters conditional on a legal question or a particularly important case: a person in tax assistance gets `NOTHING` from limb (h) and a condition from Art 84a.
   Asserted.
10. Art 84(1) has two conditions that must both hold (a listed subject, and a particularly important case); Art 84(2) gives two examples of a particularly important case ("insbesondere") and does not close the list, so a case that is important for other reasons also counts.
    Asserted.
11. Art 86(1)(d) and Art 86(2) lean on other statutes (appeal to the Federal Administrative Court, appeal from other judicial authorities); the encoding asks those as facts.
    Asserted.
12. Art 87(1) lets an appeal go directly against a cantonal enactment only where no cantonal remedy can be taken; where cantonal law gives a remedy Art 87(2) applies Art 86.
    Asserted.
13. Art 88(2) places a duty on the cantons to give a remedy and excludes acts of parliament and government in its own words.
    The exclusion is asserted; the duty is run as a trace and not asserted (see 'What the stable binary does not accept').
14. Art 89(1) has three cumulative requirements (taking part or no chance to, being especially affected, an interest worthy of protection); Art 76(1) has two, because it joins being especially affected and having an interest in one limb; Art 81(1) has two, the second being a legally protected interest with a list of persons who have one.
    Asserted.
15. Art 81(1)(b)(3) leaves the prosecutor's office out of the persons with an interest on detention decisions (fork F15).
    Asserted.
16. Art 77(2) excludes a list of procedural provisions from arbitral appeals by number and range (Art 90–98) and one only so far as it lets the Court decide the matter itself (Art 107(2)).
    Asserted.
17. Art 73 is the one flat bar in the civil section: an appeal is inadmissible against decisions in trade-mark opposition proceedings.
    Asserted.
18. Art 72(2)(b)(4) carves pension and vested-benefits institutions out of the foundation supervision item, but the carve-out is inside an 'insbesondere' item and so does not stop the chapeau (fork F1).
    Asserted.
19. Three provisions are shown repealed or blank: Art 72(2)(b)(7) (footnote 3), Art 81(1)(b)(4) (footnote 22) and Art 83(s)(1) (footnote 44).
    Not asserted: there is nothing to assert; they are rows of the coverage table.
20. Limb (r) of Art 83 cites Art 34 VGG, and footnote 43 says "Dieser Art. ist aufgehoben" (fork F13).
    Asserted only as printed, with the person stating whether the decision was taken under that article.
21. The chapter defines no term. The terms it leans on (Zivilsachen, Strafsachen, Angelegenheiten des öffentlichen Rechts, Streitwert, Rechtsfrage von grundsätzlicher Bedeutung, besonders bedeutender Fall) are undefined here, so the person states whether each applies.
    Asserted (every function takes them as inputs and the cases state them).
22. The text states no deadline and no consequence for the cantons' duties in Art 75(2), 80(2), 86(2) and 88(2); the regulative rules carry none.
    Not asserted: the stable binary cannot assert a regulative rule; each is run as a trace.
23. Seat: the Art 73, Art 79 and Art 83 questions swap the polarity of layer 1 (fork F22).
    Asserted (Art 83: cases for kinds (b), (c)(2), (d)(1), (f), (g), (h), (m), (t), (a), (zbis) and 'none of these kinds'; Art 73 and Art 79: the cases listed under 'Seat polarity (independent reader)').

## Seat polarity (independent reader)

An independent reader checked the wording of every seat question against what `JUST TRUE` and `JUST FALSE` mean in the layer-1 function it calls, and flagged three as misleading (message of 2026-11-18).
Only these three were changed, in `bgg3-seat.l4` and `bgg3-cases-seat.l4`; no layer-1 module and no other answer changed.

1. **Art 73.**
   Was: 'Is my civil-law decision one against which an appeal is admissible, or was it made in trade-mark opposition proceedings (Art 73)?'.
   It asked two things in one sentence, and layer 1 answers `JUST FALSE` exactly when the decision was made in opposition proceedings (the bar), so a person for whom the literal 'or' was yes saw `FALSE`.
   Now: 'Is my civil-law decision one that the Act excludes from the appeal because it was made in trade-mark opposition proceedings (Art 73)?', function `Art 73 my decision is excluded from the appeal in civil matters`.
   Polarity swapped: `JUST TRUE` = excluded; `NOTHING` unchanged.
2. **Art 79.**
   Was: 'Can I appeal in a criminal matter against a decision on a coercive measure (Art 79)?'.
   Art 79 is a bar on Complaints Chamber decisions that are not about a coercive measure; layer 1 answers `NOTHING` for a decision that is on a coercive measure, and the only definite value was `FALSE` for one that is not, which read against the wording as 'no, I cannot appeal against a coercive-measure decision', the opposite of the text.
   Now: 'Is my criminal-matter decision of the Complaints Chamber excluded from the appeal because it is not about a coercive measure (Art 79)?', function `Art 79 my decision of the Complaints Chamber is excluded from the appeal in criminal matters`.
   Polarity swapped: `JUST TRUE` = excluded; `NOTHING` unchanged (a decision on a coercive measure, or of another body).
   The question still takes the deciding body as an input, and its `@desc` says the question is about the Complaints Chamber and that any other body is not covered.
3. **Art 86(2).**
   Was: 'Is my immediate lower instance an upper court, as Art 86(2) requires (Art 86(2))?'.
   Layer 1 answers `JUST TRUE` for 'an upper court or another federal statute provides for an appeal from another judicial authority', but the wording asked only the first limb.
   Now: 'Is my immediate lower instance an upper court, or does another federal statute provide for an appeal from the other judicial authority (Art 86(2))?'.
   Wording only: no answer and no case changed.

In both swapped questions layer 1 never answers `JUST TRUE` (the text has no sentence that says yes), so the arm `JUST TRUE` to `JUST FALSE` is not reached today.
It is kept so that the swap stays total, as in Art 83, and it carries a `POLARITY SWAP` comment and no `FALSE-kind` tag, because no text is quoted for it.
No case reaches it.

Cases whose expected value changed (each case file line carries an `EXPECTED VALUE CHANGED 2026-11-18` comment above it):

| question | facts | expected before | expected now |
| --- | --- | --- | --- |
| Art 73 | decision made in trade-mark opposition proceedings | `JUST FALSE` | `JUST TRUE` |
| Art 79 | Complaints Chamber, decision not on a coercive measure | `JUST FALSE` | `JUST TRUE` |

Cases renamed to the new function with the expected value unchanged: Art 73 with no opposition proceedings (`NOTHING`); Art 79 for the Complaints Chamber on a coercive measure (`NOTHING`); Art 79 for the Appeals Chamber (`NOTHING`).
Case added: Art 79 for a last cantonal instance, not on a coercive measure (`NOTHING`).
The case file went from 145 to 146 asserted cases and all are satisfied.

## What the text does not answer

Asked as inputs, and a question that needs the missing rule is answered `NOTHING`; none is taken from memory.

- Chapters 4 and following (which decisions can be appealed, grounds, time limits, parties' submissions, how the value in dispute is worked out).
- The Federal Constitution (Art 121(2), cited in Art 83(c)(4)).
- Other statutes the chapter cites: the Private International Law Act (Art 190–192), the Civil Procedure Code (Art 389–395), the Code of Criminal Procedure (single cantonal instances in Art 80(2)), the Administrative Criminal Law Act (Art 81(1)(b)(7)), the Public Procurement Act (the threshold in Art 83(f)(2)), the Passenger Transport Act (Art 32i), the Telecommunications Act (Art 11a), the Postal Act (Art 8), the Administrative Court Act (Art 34), the Financial Market Infrastructure Act (Art 125–141), the Energy Act (Art 71c), the Electricity Supply Act (Art 9a), the Environmental Protection Act and the Nature and Cultural Heritage Act (Art 83(zter)), and the Act on coercive measures for welfare before 1981 (Art 83(x)).
- Which statutes make an appeal to the Federal Administrative Court admissible (Art 86(1)(d)), which give another judicial authority's decisions an appeal to the Federal Supreme Court (Art 86(2)), and which give a person standing (Art 89(2)(d)).
- Whether a decision is a civil, criminal or public-law matter, whether a value is 'in dispute', what is 'a legal question of fundamental importance' or 'a particularly important case', what is an 'interest worthy of protection' or 'legally protected': the chapter leaves all of them undefined.
- How the cantons organise their instances beyond the duties in Art 75(2), 80(2), 86(2) and 88(2), and what follows if a canton does not (nothing is stated).
- The text file is a script-made rendering and not the official text.

## What the stable binary does not accept

Observed on 1.6.110 and 1.6.109 during this encoding.
Loud failures first (an error the reader sees); then the silent one.

- Loud: a regulative rule (`PARTY ... MUST ...`) cannot be compared in an `#ASSERT`.
  ``#ASSERT `the duty` EQUALS `the duty` `` gives `eval/unsupported-equality`, 'assertion could not be evaluated: Trying to check equality on types that do not support it', and the values it prints are the rule's own text.
  So each duty and permission is run with `#TRACE`, and the same condition is encoded as a decision function that is asserted.
  The trace is printed, not asserted: a trace that does something prints `FULFILLED`, and the empty trace prints the residual obligation (`PARTY Canton MUST ... HENCE FULFILLED`) because no deadline is stated.
- Loud: a genitive (`facts's field`) cannot stand as an argument of a function call; the parser reports `parse/unexpected-genitive`.
  Parenthesise it: `(facts's field)`.
- Silent: `check.sh` compares counts, not trace outcomes, so a difference in what a `#TRACE` prints between the two builds does not turn it red.
  The trace outcomes of every test file were compared by hand between 1.6.110 and 1.6.109 and are identical (10 outcomes in three files).
- The brief lists further constructs the stable binary rejects (`REFUSE`, `#ASSERT REFUSED`, `BECAUSE` outside `LEST BREACH`, section-level `GIVEN`, sets); this encoding uses none of them, so none was tried.

## Marginal readings for a lawyer

Every branch below rests on a reading the 2026-10-29 rule marks for a lawyer.
Reading (a): a failed 'if' counts as the text's no, within the provision that holds it; flat negatives count as the text saying no (ruled as N2 option A, so only the 'if' inferences are listed).
Reading (b): a bar or grant limited by its own wording does not give a no when the case falls outside the limit.

Branches resting on reading (a), a failed 'if' answered `JUST FALSE` (the other reading answers `NOTHING`):

- `Art 74(2)(a)` (civil): "wenn sich eine Rechtsfrage von grundsätzlicher Bedeutung stellt"
- `Art 74(2)(b)` (civil): "wenn ein Bundesgesetz eine einzige kantonale Instanz vorsieht"
- `Art 74(2)` (civil): "so ist die Beschwerde dennoch zulässig:"
- `Art 76(1)(a)` (civil): "ist berechtigt, wer: a. vor der Vorinstanz am Verfahren teilgenommen hat oder keine Möglichkeit zur Teilnahme erhalten hat"
- `Art 76(1)(b)` (civil): "ist berechtigt, wer: ... durch den angefochtenen Entscheid besonders berührt ist und ein schutzwürdiges Interesse an dessen Aufhebung oder Änderung hat"
- `Art 76(1)` (civil): "Zur Beschwerde in Zivilsachen ist berechtigt, wer: a. ...; und b. ..."
- `Art 76(2)` (civil): "wenn der angefochtene Entscheid die Bundesgesetzgebung in ihrem Aufgabenbereich verletzen kann"
- `Art 78(2)(a)` (criminal): "Zivilansprüche, wenn diese zusammen mit der Strafsache zu behandeln sind"
- `Art 78(2)` (criminal): "Zivilansprüche, wenn diese zusammen mit der Strafsache zu behandeln sind"
- `Art 81(1)(a)` (criminal): "ist berechtigt, wer: a. vor der Vorinstanz am Verfahren teilgenommen hat oder keine Möglichkeit zur Teilnahme erhalten hat"
- `Art 81(1)(b)` (criminal): "ist berechtigt, wer: ... b. ein rechtlich geschütztes Interesse an der Aufhebung oder Änderung des angefochtenen Entscheids hat"
- `Art 81(1)` (criminal): "Zur Beschwerde in Strafsachen ist berechtigt, wer: a. ...; und b. ..."
- `Art 81(2)` (criminal): "wenn das Bundesrecht vorsieht, dass ihr der Entscheid mitzuteilen ist"
- `Art 81(3)` (criminal): "wenn der angefochtene Entscheid die Bundesgesetzgebung in ihrem Aufgabenbereich verletzen kann"
- `Art 86(1)(d)` (public-courts): "letzter kantonaler Instanzen, sofern nicht die Beschwerde an das Bundesverwaltungsgericht zulässig ist"
- `Art 87(1)` (public-courts): "Gegen kantonale Erlasse ist unmittelbar die Beschwerde zulässig, sofern kein kantonales Rechtsmittel ergriffen werden kann."
- `Art 89(1)(a)` (public-courts): "ist berechtigt, wer: a. vor der Vorinstanz am Verfahren teilgenommen hat oder keine Möglichkeit zur Teilnahme erhalten hat"
- `Art 89(1)(b)` (public-courts): "ist berechtigt, wer: ... b. durch den angefochtenen Entscheid oder Erlass besonders berührt ist"
- `Art 89(1)(c)` (public-courts): "ist berechtigt, wer: ... c. ein schutzwürdiges Interesse an dessen Aufhebung oder Änderung hat"
- `Art 89(1)` (public-courts): "Zur Beschwerde in öffentlich-rechtlichen Angelegenheiten ist berechtigt, wer: a. ...; b. ...; und c. ..."
- `Art 89(2)(a)` (public-courts): "wenn der angefochtene Akt die Bundesgesetzgebung in ihrem Aufgabenbereich verletzen kann"
- `Art 89(2)(c)` (public-courts): "wenn sie die Verletzung von Garantien rügen, die ihnen die Kantons- oder Bundesverfassung gewährt"
- `Art 85(2)` (public-limits): "so ist die Beschwerde dennoch zulässig, wenn sich eine Rechtsfrage von grundsätzlicher Bedeutung stellt"

Branches resting on reading (b), outside the limit answered `NOTHING` (the other reading answers `JUST FALSE`).
Every function below has at least one such branch; the number in brackets is how many.

- civil: `Art 72(1)` (1), `Art 72(2)(a)` (1), `Art 72(2)(b)(4)` (1), `Art 72(2)(b)` (1), `Art 72(2)` (1), `Art 72` (1), `Art 73` (1), `Art 74(1)(a)` (2), `Art 74(1)(b)` (2), `Art 74(2)(c)` (1), `Art 74(2)(d)` (1), `Art 74(2)(e)` (1), `Art 74(2)` (1), `Art 75(2)(a)` (1), `Art 75(2)(b)` (1), `Art 75(2)(c)` (1), `Art 75(2)` (1), `Art 76(2)` (2), `Art 77(1)(a)` (1), `Art 77(1)(b)` (1), `Art 77(1)` (1), `Art 77(2)` (1), `Art 77(2bis)` (1), `Art 77(3)` (1)
- criminal: `Art 78(1)` (1), `Art 78(2)(a)` (1), `Art 78(2)(b)` (1), `Art 78(2)` (1), `Art 79` (2), `Art 80(2)` (1), `Art 81(1)(b)(3)` (1), `Art 81(1)(b)(5)` (1), `Art 81(1)(b)(6)` (1), `Art 81(2)` (1), `Art 81(3)` (2)
- public-courts: `Art 86(1)(a)` (1), `Art 86(1)(b)` (1), `Art 86(1)(c)` (1), `Art 86(1)(d)` (1), `Art 86(2)` (1), `Art 86(3)` (1), `Art 87(1)` (1), `Art 87(2)` (1), `Art 88(1)(a)` (1), `Art 88(1)(b)` (1), `Art 88(2)` (1), `Art 89(2)(a)` (1), `Art 89(2)(b)` (1), `Art 89(2)(c)` (1), `Art 89(3)` (1)
- public-limits: `Art 84(1)` (1), `Art 84a` (1), `Art 85(1)(a)` (1), `Art 85(1)(b)` (1), `Art 85(1)` (1), `Art 85(2)` (1)
- public-scope: `Art 82(a)` (1), `Art 82(b)` (1), `Art 82(c)` (1), `Art 82` (1), `Art 83(a)` (1), `Art 83(b)` (1), `Art 83(c)(1)` (1), `Art 83(c)(2)` (1), `Art 83(c)(3)` (1), `Art 83(c)(4)` (1), `Art 83(c)(5)` (1), `Art 83(c)(6)` (1), `Art 83(d)(1)` (1), `Art 83(d)(2)` (1), `Art 83(e)` (1), `Art 83(f)(1)` (1), `Art 83(f)(2)` (1), `Art 83(f)` (1), `Art 83(fbis)` (1), `Art 83(g)` (1), `Art 83(h)` (1), `Art 83(i)` (1), `Art 83(j)` (1), `Art 83(k)` (1), `Art 83(l)` (1), `Art 83(m)` (1), `Art 83(n)(1)` (1), `Art 83(n)(2)` (1), `Art 83(n)(3)` (1), `Art 83(o)` (1), `Art 83(p)(1)` (1), `Art 83(p)(2)` (1), `Art 83(p)(3)` (1), `Art 83(q)(1)` (1), `Art 83(q)(2)` (1), `Art 83(r)` (1), `Art 83(s)(2)` (1), `Art 83(t)` (1), `Art 83(u)` (1), `Art 83(v)` (1), `Art 83(w)` (1), `Art 83(x)` (1), `Art 83(y)` (1), `Art 83(z)` (1), `Art 83(zbis)` (1), `Art 83(zter)` (1)

Also for the maintainer, from the ruling of 2026-11-12: the 'entitled'-named functions (fork F3) and the 'wenn' and 'sofern' gates on grants (forks F7, F11, F16) are listed and not changed.

## What check.sh prints

Run as `L4=<l4 1.6.110> L4_MAIN=<l4 1.6.109> ./check.sh` in this folder, with the target `main`.
There are no baseline numbers it replaced: this is a new encoding, and the per-file counts printed while the files were written (civil 150, criminal 74) are the same numbers.
The comparison with the second stable build is of counts; traces were compared by hand (above).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
bgg3-cases-seat.l4                             0       146       0        0         0 |      0       146       0        0  same
bgg3-civil.l4                                  0         0       0        0         0 |      0         0       0        0  same
bgg3-criminal.l4                               0         0       0        0         0 |      0         0       0        0  same
bgg3-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
bgg3-public-courts.l4                          0         0       0        0         0 |      0         0       0        0  same
bgg3-public-limits.l4                          0         0       0        0         0 |      0         0       0        0  same
bgg3-public-scope.l4                           0         0       0        0         0 |      0         0       0        0  same
bgg3-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
bgg3-tests-civil.l4                            0       150       0        0         0 |      0       150       0        0  same
bgg3-tests-criminal.l4                         0        74       0        0         0 |      0        74       0        0  same
bgg3-tests-public-courts.l4                    0        73       0        0         0 |      0        73       0        0  same
bgg3-tests-public-limits.l4                    0        39       0        0         0 |      0        39       0        0  same
bgg3-tests-public-scope.l4                     0       199       0        0         0 |      0       199       0        0  same
TOTAL (13 modules)                             0       681       0        0           |      0       681       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs <text file> bgg3-*.l4` reports 0 problems; `python3 -I quotecheck.py <text file> bgg3-*.l4` reports 0 quoted fragments missing from the text; `python3 -I coverage.py <text file>` prints COVERAGE OK.

## What would need doing before the encoding is worth relying on

- A Swiss lawyer should read every fork in the register and every branch under 'Marginal readings for a lawyer' against the official text.
- The text file must be compared with the official publication; this encoding says nothing about whether the consolidated version is the authoritative one.
- Chapter 4 and the statutes named under 'What the text does not answer' must be encoded or supplied as inputs before an answer from this chapter can be called an answer about whether an appeal lies: chapter 3 says which decisions are appealable and who may appeal, not how and by when.
- The Art 83 seat question has 19 inputs; a form would do better as a series of short questions by group of limbs, which would need new questions in layer 2 and no change in layer 1.
- The open-textured inputs (legal question of fundamental importance, particularly important case, interest worthy of protection) need guidance for a lay user that this chapter does not give.
- No time limits are given for the cantons' duties; the regulative rules would need them if a later text states any.
