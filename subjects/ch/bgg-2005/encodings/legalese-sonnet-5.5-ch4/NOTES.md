# NOTES: Federal Supreme Court Act (BGG, SR 173.110), chapter 4 (Art. 90 to 112), in L4

Encoding `legalese-sonnet-5.5-ch4`: a single Sonnet 5.5 agent working alone from the brief, on the stable `l4` 1.6.110 (main, e51181d, 2026-11-11) (sha256 `9c7656f74151383da2c7344ad53269a8754bd874af8eb513180d61dc145016c7`), checked against the second stable build 1.6.109 (main, 4c887e0, 2026-11-04).
The target is `main`: `check.sh` runs every module with both builds and compares the counts.
Status: draft.
How each claim below was verified: every count is printed by a script run in this folder (`check.sh`, `coverage.py`, `quotecheck.py`, `srcrefs.py`) or computed by the script that wrote this file; every statement about what the text says was written beside a German quotation that `quotecheck.py` found in the text file; every statement marked "Asserted." names the assertion lines that show it.
No domain expert has read this encoding against the text.
This folder also holds `bgg3-*.l4`, the chapter 3 row written by another agent: those six files are read-only copies, this encoding calls them from `bgg4-seams.l4` and never changes them.

## What the source is, and what these words are

The text is a plain-text rendering of Fedlex's consolidated German version of chapter 4 of the BGG (Art. 90 to 112), applicable from 2026-04-01, made by a converter script.
It is not the official text, and nothing here is verified against the official text.
The deposit does not say whether the consolidated version or only the publication of each amending act in the Official Compilation (AS) is authoritative (`SOURCE-LICENSE.md`, and `inputs/STUB-SOURCE-LICENSE.md` beside the text).
The file `ch-bgg-sr173110-ch4-art-90-112-20260401.txt` has 166 lines and 2208 words, sha256 `57b31040c47e38955d09531f374082497e4d38becfce47e28bcff1173fc5a8d3` (the value `inputs/SOURCES.md` records; `mknotes` compared them).
Chapter 3's text is given as context only; one sentence of it, Art 77(2), is quoted below because it names chapter 4.
Every quotation of the text is German, copied by script from the file (`-- src:` lines), and every other German phrase in a comment is checked against the file by `quotecheck.py`.
The English identifiers, `@desc` strings, seat questions and this file are a gloss of the German terms of art, not the text and not a translation of it.
The German term is in a comment beside its first use.

## Seat

The seat is a person affected by a decision: a party to civil or criminal proceedings, or to proceedings in a public-law matter, who lost, or a person with another interest the text names.
That person asks, on facts they can state, which decisions they may appeal, on what grounds, by when, what new submissions are allowed, whether the appeal stops the decision from taking effect, and what the cantons must provide.
Commons asks every Act from the position of the individual to whom the law is applied, because the Legalese website turns such a layer into a question form; a person who has lost a case is the individual chapter 4 is applied to.
There is never a seat for an official: the Court, the lower instance, the instructing judge and the federal authorities appear in layer 2 only as what their powers and duties mean for that person.

Layer 1 is the law, objectively, in 8 modules besides the nouns and the tests; layer 2 is the two files `bgg4-seat.l4` (46 questions in 8 sections) and `bgg4-cases-seat.l4` (180 assertions, at least one case per question).
42 of the 46 questions have a case that answers NOTHING; the other 4 cannot from their inputs: `Art 100 the number of days I have to appeal against a decision`, `Art 100 and 101 the last day on which I can file my appeal`, `Art 103 my appeal stops the decision taking effect`, `Art 107(1) the Court may go beyond my claims` (the first two return a number and a time limit, Art 103 takes the exceptions of paragraphs 2 and 3 as the only ones (fork F31), and Art 107(1) is a flat negative that answers JUST FALSE with no fact (fork F33)).
The seat layer restates no rule: each question calls a layer-1 function with plain inputs, one per fact the person can state, each with an `@desc` worded as the person is asked.
The questions that need both chapters (may I appeal this decision at all, and by when?) call chapter 3 and chapter 4 together through `bgg4-seams.l4`, which is layer 1, so the seam is written once.
The questions Art 77(2) of chapter 3 reaches (Art 90 to 98, 103(2), 105(2), 106(1), 107(2)) take one more input, whether the appeal is against an arbitral award under Art 77(1), and answer NOTHING for such an appeal.
Rows of the text with no seat question of their own: Art 102(2), Art 108(2), Art 109(1) second sentence, Art 111(2); each is official-facing or only disapplies a rule outside the sources (Art 102(2): the lower instance sends the files; Art 108(2): the president entrusts another judge; Art 109(1) second sentence: Art 58(1)(b) does not apply; Art 111(2): a federal authority's power to use cantonal remedies), and each is encoded in layer 1 for what it decides.

| section | question the person is asked | layer-1 function(s) it calls | cases |
| --- | --- | --- | --- |
| Which decisions can I appeal (Art 90 to 94) | May I appeal to the Federal Supreme Court against my decision, because of the kind of decision it is (Art 90 to 93)? | `Art 90 to 93 the appeal is admissible against the decision`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 4 |
| Which decisions can I appeal (Art 90 to 94) | If my decision is a preliminary or interim decision on jurisdiction or recusal, can I still challenge it later (Art 92(2))? | `Art 92(2) the decision can be challenged later` | 2 |
| Which decisions can I appeal (Art 90 to 94) | If I could not appeal my other preliminary or interim decision at the time, can I challenge it with the appeal against the final decision (Art 93(3))? | `Art 93(3) the preliminary or interlocutory decision can be challenged by the appeal against the final decision` | 3 |
| Which decisions can I appeal (Art 90 to 94) | May I appeal against an authority's unlawful refusal or delay in deciding (Art 94)? | `Art 94 the appeal lies against the unlawful refusal or delay of a decision` | 2 |
| On what grounds (Art 95 to 98) | May I complain to the Federal Supreme Court of a violation of this source of law (Art 95)? | `Art 95 the violation of the source of law can be complained of`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 3 |
| On what grounds (Art 95 to 98) | May I complain to the Federal Supreme Court about the application of foreign law (Art 96)? | `Art 96 the complaint about foreign law can be raised`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 4 |
| On what grounds (Art 95 to 98) | May I complain to the Federal Supreme Court about the lower instance's finding of the facts (Art 97)? | `Art 97 the complaint about the finding of the facts can be raised`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 4 |
| On what grounds (Art 95 to 98) | May I raise this complaint against a decision on provisional measures (Art 98)? | `Art 98 the complaint can be raised against the decision on provisional measures`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 3 |
| New submissions (Art 99) | May I put forward a new fact or new evidence before the Federal Supreme Court (Art 99(1))? | `Art 99(1) the new fact or new evidence may be put forward` | 3 |
| New submissions (Art 99) | May I make a new claim before the Federal Supreme Court (Art 99(2))? | `Art 99(2) the new claim is admissible` | 2 |
| By when must I appeal (Art 100 and 101) | How many days do I have to appeal against a decision (Art 100(1) to (4))? | `Art 100(1) to (4) the period in days for the appeal against a decision` | 5 |
| By when must I appeal (Art 100 and 101) | By what day must I file my appeal (Art 100 and 101)? | `Art 100 and 101 the time limit for filing` | 3 |
| By when must I appeal (Art 100 and 101) | Is my appeal in time (Art 100 and 101)? | `Art 100 and 101 the appeal is in time` | 3 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | Will the Court send my appeal to this recipient and set a time limit for observations (Art 102(1))? | `Art 102(1) the Federal Supreme Court must serve the appeal and set a time limit for observations` | 2 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | Will there be a further exchange of submissions (Art 102(3))? | `Art 102(3) a further exchange of submissions takes place` | 2 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | Does my appeal stop the decision from taking effect (Art 103)? Not for an arbitral award: ask the next question. | `Art 103 the appeal has suspensive effect` | 4 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | Does my appeal stop the decision from taking effect under Art 103(2), if it is an appeal against an arbitral award (Art 103(2) with Art 77(2))? | `Art 103(2) the appeal has suspensive effect to the extent of the claims`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 3 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | May the instructing judge order a provisional measure (Art 104)? | `Art 104 the instructing judge may order a provisional measure` | 2 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | Is the Federal Supreme Court bound by the facts the lower instance found (Art 105)? Not for an arbitral award: ask the next question about Art 105(2). | `Art 105 the Court is bound by the facts found by the lower instance` | 4 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | May the Court correct or supplement the lower instance's finding of the facts, if my appeal is against an arbitral award (Art 105(2) with Art 77(2))? | `Art 105(2) the Court may correct or supplement the finding of the facts`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 3 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | Will the Federal Supreme Court examine the violation I complain of (Art 106)? | `Art 106 the Court examines the violation of the rule`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 4 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | May the Court go beyond the claims I made (Art 107(1))? | `Art 107(1) the Court is permitted to go beyond the claims of the parties` | 1 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | If the Court upholds my appeal, may it give this outcome (Art 107(2))? | `Art 107(2) the Court may give this outcome when it upholds the appeal`, `Art 77(2) the answer of a chapter 4 provision stands for the appeal` | 4 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | By what day must the Court decide not to enter on my appeal in international legal assistance or tax assistance (Art 107(3))? | `Art 107(3) the last day for the decision not to enter` | 2 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | In my extradition appeal, is the Court held to the 15 days for a decision not to enter (Art 107(3), second sentence)? | `Art 107(3) the Court is bound by the period of 15 days` | 3 |
| Procedure: suspensive effect, provisional measures, the facts and the law (Art 102 to 107) | By what day must the Court decide my appeal against a Federal Patent Court decision on a licence (Art 107(4))? | `Art 107(4) the last day for the Court's decision on the licence appeal` | 3 |
| Simplified procedure (Art 108 and 109) | May the president of the division alone decide not to enter on my appeal (Art 108(1))? | `Art 108(1) the president of the division decides in the simplified procedure on non-entry` | 3 |
| Simplified procedure (Art 108 and 109) | Will the reasons I get be only a short statement of the ground of inadmissibility (Art 108(3))? | `Art 108(3) the reasons of the decision are confined to a short statement of the ground of inadmissibility` | 2 |
| Simplified procedure (Art 108 and 109) | May a bench of three judges decide not to enter on my appeal because the condition on which my kind of appeal is admissible, a question of fundamental importance or a particularly important case as Art 74 and 83 to 85 set it for this kind of appeal, is absent (Art 109(1))? | `Art 109(1) with chapter 3 the division decides in a bench of three on non-entry` | 18 |
| Simplified procedure (Art 108 and 109) | May a bench of three judges decide my appeal if they are unanimous that it is obviously unfounded or obviously well founded (Art 109(2))? | `Art 109(2) the division decides in a bench of three` | 3 |
| Simplified procedure (Art 108 and 109) | Will the reasons of the bench of three be only summary (Art 109(3))? | `Art 109(3) the decision is given summary reasons` | 2 |
| Simplified procedure (Art 108 and 109) | May the reasons of the bench of three refer wholly or partly to the decision I challenged (Art 109(3), second sentence)? | `Art 109(3) the reasons may refer wholly or in part to the challenged decision` | 2 |
| What the cantons must provide (Art 110 to 112) | Has my canton ensured that a court freely reviewed the facts and applied the law of its own motion (Art 110, with Art 75(2), 80(2) and 86)? | `Art 110 with chapter 3 the canton has ensured the review by a judicial authority` | 3 |
| What the cantons must provide (Art 110 to 112) | Must I be able to take part as a party before all the cantonal lower instances (Art 111(1), with Art 76(1), 81(1) and 89(1))? | `Art 111(1) with chapter 3 the person entitled to appeal must be able to take part as a party before all cantonal lower instances` | 2 |
| What the cantons must provide (Art 110 to 112) | Can the court directly below the Federal Supreme Court examine at least my complaints under Art 95 to 98 (Art 111(3))? | `Art 111(3) the immediate lower instance can examine at least the complaints under Art 95 to 98` | 2 |
| What the cantons must provide (Art 110 to 112) | Does the decision I received meet the requirements for a decision that can be appealed: written, with the parties' claims, the reasons, the operative part and a notice of remedies (Art 112(1))? | `Art 112(1) the decision meets the requirements of paragraph 1` | 3 |
| What the cantons must provide (Art 110 to 112) | Does my decision contain a notice of legal remedies, including the value in dispute where the Act gives a value limit (Art 112(1)(d), with Art 74(1) and 85(1))? | `Art 112(1)(d) with chapter 3 the decision contains a notice of legal remedies including the value in dispute where the Act provides a value limit` | 3 |
| What the cantons must provide (Art 110 to 112) | May the authority notify my decision promptly and without reasons (Art 112(2), first sentence)? | `Art 112(2) the authority may notify the decision promptly and without reasons` | 2 |
| What the cantons must provide (Art 110 to 112) | By what day can I demand the complete version of a decision notified without reasons (Art 112(2), second sentence)? | `Art 112(2) the last day to demand the complete version` | 2 |
| What the cantons must provide (Art 110 to 112) | Is my demand for the complete version of the decision in time (Art 112(2), second sentence)? | `Art 112(2) the demand for the complete version is in time` | 3 |
| What the cantons must provide (Art 110 to 112) | Does the bar on enforcing a decision notified without reasons still apply (Art 112(2), third sentence)? JUST TRUE means it cannot yet be enforced; JUST FALSE means the bar is lifted, not that the decision may be enforced. | `Art 112(2) the bar on enforcing the decision still applies` | 3 |
| What the cantons must provide (Art 110 to 112) | May the Federal Supreme Court send my decision back for improvement or quash it because it falls short of Art 112(1) (Art 112(3))? | `Art 112(3) the Court may remit the decision for improvement or quash it` | 2 |
| What the cantons must provide (Art 110 to 112) | Must the cantonal authority also notify my decision to a federal authority (Art 112(4))? | `Art 112(4) the cantonal authority must notify the decision to the federal authority` | 2 |
| Chapter 3 and chapter 4 together: may I appeal this decision at all, and by when? | In a civil matter: may I appeal my decision, am I entitled to, can that act be appealed, is my appeal in time, and what is the time limit (Art 72, 76, 90 to 94, 100 and 101)? | `Art 72, 76 and 90 to 101 the answers on appealing a civil decision and by when` | 15 |
| Chapter 3 and chapter 4 together: may I appeal this decision at all, and by when? | In a criminal matter: may I appeal my decision, am I entitled to, can that act be appealed, is my appeal in time, and what is the time limit (Art 78, 81, 90 to 94, 100 and 101)? | `Art 78, 81 and 90 to 101 the answers on appealing a criminal decision and by when` | 15 |
| Chapter 3 and chapter 4 together: may I appeal this decision at all, and by when? | In a public-law matter: may I appeal my decision, am I entitled to, can that act be appealed, is my appeal in time, and what is the time limit (Art 82, 89, 90 to 94, 100 and 101)? | `Art 82, 89 and 90 to 101 the answers on appealing a public-law decision and by when` | 15 |

## Reading the answers

### Reading a result: FALSE and NOTHING

Every layer-1 decision function answers `MAYBE BOOLEAN` (or a constructor that says the same), and the seat questions pass the answer on unchanged.
`JUST TRUE` is "the text says yes to this case".
`JUST FALSE` is "the text says no to this case in its own words": a flat negative ("nicht anfechtbar", "unzulässig", "darf nicht"), a condition the text introduces with "wenn", "sofern" or "solange", a list the text closes with "nur", or a period the text fixes in its own words and the case is outside it.
`NOTHING` is "chapter 4 does not decide this case": the text is silent, lists without closing the list, leaves a term undefined, points to a rule outside the sources (chapter 2, the Civil Procedure Code, the Patent Act, the Federal Council), or limits a grant or a bar in its own wording and the case falls outside the limit.
A caller must never turn `NOTHING` into `FALSE`: a person who is told `NOTHING` is not told they may not appeal, only that this chapter does not say.
Every branch that answers a no carries `-- FALSE-kind (the text says no in its own words): "<German>"` and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)`, with the reason one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
The modules carry 45 FALSE-kind and 111 NOTHING-kind comments.
The conventions are those of the chapter 3 row and of the rulings listed under "Rulings applied" below.
A function named for a grant or a power ("the Court may ...", "the president may ...") whose gate failed answers NOTHING and not a "may not" (ruling of 2026-11-12, limb 1); where the text closes the gate itself ("nur", "nicht") the answer is JUST FALSE.
"Not covered" is `NOTHING`; `REFUSE` does not exist on the stable binary.

## Seat polarity (independent reader)

An independent reader checked the wording of all 46 seat questions against what `JUST TRUE` and `JUST FALSE` mean in the function each one calls.
45 were right.
One was not: the Art 109(1) question in `bgg4-seat.l4`.
Its old wording asked for both absences: "May a bench of three judges decide not to enter on my appeal because it raises no question of fundamental importance and is no particularly important case (Art 109(1), with Art 74 and 83 to 85)?"
The function it calls consults only the one condition on which the person's kind of appeal turns (`Art 109(1) the condition on which the appeal is admissible, by chapters 3` in `bgg4-seams.l4`, read by `Art 109(1) the division decides in a bench of three on non-entry` in `bgg4-simplified.l4`).
Legal assistance in criminal matters turns only on "particularly important", public-law appeals below the value limit only on "fundamental importance", and tax assistance on either.
So the old wording promised more than a `JUST TRUE` says.
New wording: "May a bench of three judges decide not to enter on my appeal because the condition on which my kind of appeal is admissible, a question of fundamental importance or a particularly important case as Art 74 and 83 to 85 set it for this kind of appeal, is absent (Art 109(1))?"
`JUST TRUE` means yes: that condition is absent.
`NOTHING` means chapter 4 does not say, and this question never answers `JUST FALSE`; a two-line note above the question in `bgg4-seat.l4` says so.
No answer changed.
At that edit the DECIDE name, every input and its description, and every case were as they were (`bgg4-cases-seat.l4` was byte-identical to the file before it), and the `check.sh` counts were the same.
The repairs in the next section came after it and did change this question's inputs and cases.
The two inputs most affected, `a legal question of fundamental importance arises` and `the case is particularly important for other reasons`, keep their descriptions: each asks one fact, and the function combines the facts the person's kind of appeal turns on.

## Independent reader (blind test), repairs

A blind reader wrote scenarios from the German text before seeing the modules and then ran them against this encoding.
The team lead relayed the result (not re-run here): 277 assertions, 259 satisfied, 18 failed, 0 refused, 6 gaps; 13 of the 18 failures are readings the reader marks AMBIGUOUS, one is the reader's own mistake, and four findings were sent to this encoding for repair.
The ambiguous ones were not sent for repair; fork F26's text changed only because of repair 1.
No DECIDE name changed in these repairs; the inputs that changed are listed per repair.

**1. Art 109(1) and Art 74 (repaired; the main finding).**
The seam derived the condition only from chapter 3's Art 84(1), 84a and 85, so every civil appeal came out `on neither of these conditions` and the seat question answered NOTHING for it.
A civil sales dispute of 20 000 francs with no legal question of fundamental importance is below the limit of Art 74(1)(b) (30 000 francs) and is admissible only under Art 74(2)(a), so the text's own words let a bench of three decide not to enter: the answer is now JUST TRUE.
`bgg4-seams.l4` now derives Art 74 from chapter 3's `Art 74(1) the value in dispute is enough` and `Art 74(2)(b)` to `(e)`, when the kind of appeal is the civil one.
Seven inputs were appended to the seat question after the eleven it had, in this order: the kind of appeal; the case is an employment law case; the case is a tenancy law case; a federal statute provides for a single cantonal instance; the decision is of a cantonal supervisory authority in a debt enforcement or bankruptcy matter; the decision is of the bankruptcy and composition judge; the body that decided.
The readings, each asserted in the seat cases and in `bgg4-tests-seams.l4`:

- Below the limit and no ground of Art 74(2)(b) to (e) saves the appeal: the condition is "only if a legal question of fundamental importance arises", so the answer is JUST TRUE where none arises and NOTHING where one does.
- The limit is "mindestens" 15 000 francs in an employment or tenancy law case and 30 000 francs in all other cases: 14 999 is below the first and 15 000 is not, 29 999 is below the second and 30 000 is not, and both sides of each are asserted.
- At or above the limit the appeal depends on no such condition and Art 109(1) does not reach it: the answer is NOTHING and not JUST FALSE.
  The reader marked a labour case of 15 000 francs AMBIGUOUS between the two; this encoding keeps NOTHING because the competence of a bench of three is a power whose gate failed (ruling of 2026-11-12, limb 1), as it already was for Art 85(1) above its limit (fork F32).
- Below the limit but saved by another ground of Art 74(2) (a federal statute provides for a single cantonal instance; a decision of a cantonal supervisory authority in debt enforcement or bankruptcy; a decision of the bankruptcy and composition judge; a decision of the Federal Patent Court): the appeal is admissible on that ground and does not depend on the condition, so NOTHING.
  The reader's labour case of 14 999 francs under Art 74(2)(b) is the first of these.
- Art 74 belongs to the appeal in civil matters: for a criminal appeal, and for a public-law appeal in a pecuniary matter that is neither state liability nor public-law employment, the answer is NOTHING.

Fork F26 had listed the conditions not derived as Art 74(2)(a) and Art 83 (w), (z) and (zbis) and said the person states the condition in the chapter 4 question; the seat question never had an input for it.
Re-reading Art 83 for this repair showed that (f)(1), (m) and (x) also turn on such a condition.
F26 now lists the six, says the question has no input for them, and says the answer is NOTHING (also under "What the text does not answer").

**2. Art 107(3), second sentence (changed).**
`Art 107(3) the Court is bound by the period of 15 days` answered JUST FALSE where the exception applies and NOTHING otherwise, so the seat question "is the Court held to the 15 days" never said yes.
The text gives the 15 days as the rule for international legal assistance in criminal matters and tax assistance ("so fällt es den Nichteintretensentscheid innert 15 Tagen") and states one exception, in the second sentence, introduced with "wenn".
Where the exception is not made out the text's own words leave the Court bound, so the answer is now JUST TRUE; this needs no ruling the guide does not give, because a condition the text introduces with "wenn" counts as the text's no when it fails (reading (a) of the rule of 2026-10-29, as for a failed "wenn" elsewhere).
The other reading, NOTHING, is kept in fork F34.
The answer presumes a decision not to enter, which the first sentence limits to an appeal the Court considers inadmissible (the seat question says "for a decision not to enter"); an appeal that is not in the field of legal assistance in criminal matters is NOTHING for this function.
The seat question's inputs and DECIDE name are unchanged.

**3. Art 107(1) (changed).**
"Das Bundesgericht darf nicht über die Begehren der Parteien hinausgehen" is a flat negative with no condition and no limit of its own.
The function answered JUST FALSE only when the person said the decision the Court would give goes beyond the claims and NOTHING otherwise, so a person who asked the standing question "may the Court go beyond the claims I made?" got "not covered" unless they stated that the decision would exceed them.
The function now has no input and answers JUST FALSE (a bar, ruling N2; fork F33), and so does the seat question, which lost its one input.
Its wording and DECIDE name are unchanged.

**4. The value limit in the three records (a gap, recorded and not repaired).**
The reader wanted a field in the three records saying whether the appeal meets the value limit of chapter 3.
Adding it would change the record type that the three records share and the three functions that build it, and the value limit is chapter 3's own question (the Art 74(1) and Art 85(1) functions are in its row); this encoding asks it only inside Art 109(1) and Art 112(1)(d).
It is listed under "What the text does not answer".

**Cases whose expected value changed.**
These are all of them; every other expected value is as it was.

| file | what is asserted | old | new |
| --- | --- | --- | --- |
| `bgg4-cases-seat.l4` | `Art 107(1) the Court may go beyond my claims`, no fact stated | NOTHING | JUST FALSE |
| `bgg4-cases-seat.l4` | `Art 107(1) the Court may go beyond my claims`, the decision would go beyond the claims | JUST FALSE | (the input is gone; the case is the one above) |
| `bgg4-cases-seat.l4` | `Art 107(3) the Court is held to the 15 days in my extradition appeal`, an extradition appeal whose asylum application has a final decision | NOTHING | JUST TRUE |
| `bgg4-tests-procedure.l4` | `Art 107(1) the Court is permitted to go beyond the claims of the parties`, a decision that does not go beyond the claims | NOTHING | (the input is gone; JUST FALSE, asserted once) |
| `bgg4-tests-procedure.l4` | `Art 107(1) the Court is permitted to go beyond the claims of the parties`, a decision that goes beyond the claims | JUST FALSE | JUST FALSE, with no argument |
| `bgg4-tests-procedure.l4` | `Art 107(3) the Court is bound by the period of 15 days`, legal assistance in criminal matters and an asylum application with a final decision | NOTHING | JUST TRUE |

Same expected value, different arguments: the 16 layer-1 assertions on Art 109(1) in `bgg4-tests-seams.l4` and the 5 seat cases for the Art 109(1) question each gained the seven new arguments, and the public-law ones carry the public-law kind of appeal.
Added: 24 layer-1 assertions in `bgg4-tests-seams.l4` and 13 seat cases for Art 109(1), asserted from the text.
Forks added or changed: F26 (changed), F32, F33 and F34 (new).

## What is encoded, and what is not

Everything in the text file is encoded, apart from the headings and the amendment-history footnotes (inert, reason 1), and the two paragraphs the text shows as repealed (Art 100(6) and the second sentence of Art 111(3)), which have labelled stubs.
Layer 1, by module:

| module | provisions | layer-1 functions | of which regulative rules | tests |
| --- | --- | --- | --- | --- |
| `bgg4-nouns` | the types of the chapter | 0 | 0 | |
| `bgg4-appealable` | Art 90 to 94 | 13 | 0 | 57 assertions |
| `bgg4-cantonal` | Art 110 to 112 | 23 | 5 | 67 assertions, 6 traces |
| `bgg4-grounds` | Art 95 to 98 | 13 | 0 | 43 assertions |
| `bgg4-new-submissions` | Art 99 | 2 | 0 | 6 assertions |
| `bgg4-procedure` | Art 102 to 107 | 30 | 4 | 97 assertions, 7 traces |
| `bgg4-seams` | chapter 3 meets chapter 4 (Art 77(2), 90 to 101, 109(1), 110, 111(1), 112(1)(d)) | 13 | 0 | 122 assertions |
| `bgg4-simplified` | Art 108, 109 | 13 | 0 | 43 assertions |
| `bgg4-time-limit` | Art 100, 101 | 27 | 5 | 86 assertions, 11 traces |
| `bgg4-seat`, `bgg4-cases-seat` | layer 2 | 0 | 0 | 180 assertions |

In all: 134 layer-1 functions (of which 14 regulative rules and 2 labelled repealed stubs), 701 assertions and 24 traces.
131 of the functions are named by an assertion or a trace, 1 is exercised only through a function that calls it, and the stubs call and are called by nothing (`coverage.py` checks this).

Not encoded, because the text points outside it; each is asked as an input or answered NOTHING, and none is taken from memory:

- The rules on how time limits run, are suspended and are restored, on the value in dispute and on the parties (chapter 2, as the brief places them): the days left out of a count are an input (fork F10), the value in dispute is an input of chapter 3's Art 74(1) and Art 85(1).
- Art 42(2) (what a sufficient reasoning is, Art 108(1)(b)), Art 58(1)(b) (disapplied by Art 109(1)), Art 48(3) (named by chapter 3's Art 77(2)).
- The Patent Act (Art 40d, named in Art 100(2)(d) and 107(4)), the two conventions of 1980 on the return of a child (named in Art 100(2)(c)), and the law that says what a pecuniary matter, a Gestaltungsurteil or a sufficient complaint is: each is a Boolean the person states.
- The federal and cantonal law that allows a decision to be notified promptly and without reasons (Art 112(2) first sentence), and the Federal Council's determination of the decisions federal authorities are to be notified of (Art 112(4)): inputs.
- What governs an arbitral appeal where Art 77(2) makes a chapter 4 provision inapplicable.
- The open-textured terms: "unrechtmässig", "nicht wieder gutzumachender Nachteil", "offensichtlich unrichtig", "querulatorisch", "besonders bedeutender Fall", "Rechtsfrage von grundsätzlicher Bedeutung": each is a Boolean the person states.

## Jural relations

Hohfeld's correlatives: a claim is matched by a duty, a privilege (liberty) by a no-right, a power by a liability, an immunity by a disability.
Each relation is stated once, from its holder's side, in the table below, and never written twice in layer 1, once from each side.
The table has one row per paragraph, list item or sentence row of the coverage table that is operative text, so it covers the whole range; a provision that creates no relation (a counting rule, a repealed paragraph, a default, a disapplication of a rule outside the sources) is listed once as `none` with the reason.
The classification into Hohfeld kinds is the encoder's reading of the German and is not confirmed by a lawyer (ruling N2 keeps the kinds here, in this table, and does not type the person-facing answer).
For the time limits of Art 100 and 101 the text states a period and no consequence, so the row is a claim of the Court against the appellant only as the encoding reads it (fork F13).

| provision | kind (holder / bearer) | holder | bearer | rule |
| --- | --- | --- | --- | --- |
| Art 90 | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 90 the appeal is admissible against the decision` (+2 more) |
| Art 91 (intro) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 91 the appeal is admissible against the partial decision` |
| Art 91(a) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 91(a) the appeal is admissible against the decision that deals with only some of the claims` |
| Art 91(b) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 91(b) the appeal is admissible against the decision that ends the proceedings for only some of the joint litigants` |
| Art 92(1) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 92(1) the appeal is admissible against the preliminary or interlocutory decision on jurisdiction or recusal` |
| Art 92(2) | immunity / disability | the other parties (their benefit from the decision as it stands) | the party who did not appeal at once, disabled from challenging it later | `Art 92(2) the decision can be challenged later` |
| Art 93(1) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 93(1) the appeal is admissible against the other preliminary or interlocutory decision` |
| Art 93(1)(a) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 93(1)(a) the appeal is admissible because the decision may cause irreparable harm` |
| Art 93(1)(b) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 93(1)(b) the appeal is admissible because allowing it would immediately bring about a final decision` |
| Art 93(2) | immunity / disability | the parties to a decision in international legal assistance in criminal matters or in asylum (first sentence: no challenge of a preliminary or interlocutory decision at once) | the party who would challenge it, disabled; the reserved appeals on extradition detention and seizure (second sentence) are the appellant's power | `Art 93(2) the appeal is admissible against the preliminary or interlocutory decision in the field` |
| Art 93(3) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 93(3) the preliminary or interlocutory decision can be challenged by the appeal against the final decision` |
| Art 94 | power / liability | the person affected by the decision (the appellant) | the authority that unlawfully refused or delayed, liable to the appeal | `Art 94 the appeal lies against the unlawful refusal or delay of a decision` |
| Art 95 (intro) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 95 the violation of the source of law can be complained of` |
| Art 95(a) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 95(a) the violation of federal law can be complained of` |
| Art 95(b) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 95(b) the violation of international law can be complained of` |
| Art 95(c) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 95(c) the violation of cantonal constitutional rights can be complained of` |
| Art 95(d) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 95(d) the violation of cantonal provisions on political voting rights and on popular elections and votes can be complained of` |
| Art 95(e) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 95(e) the violation of intercantonal law can be complained of` |
| Art 96 (intro) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 96 the complaint about foreign law can be raised` |
| Art 96(a) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 96(a) the complaint that foreign law was not applied as Swiss private international law prescribes can be raised` |
| Art 96(b) | power / liability | the person affected by the decision (the appellant) | the other parties and the lower instance, liable to have the decision reviewed | `Art 96(b) the complaint that foreign law was applied wrongly can be raised` |
| Art 97(1) | immunity / disability | the other parties and the lower instance's finding of the facts | the appellant, disabled from complaining of the facts except on the stated conditions | `Art 97(1) the complaint about the finding of the facts can be raised` |
| Art 97(2) | power / liability | the appellant in military or accident insurance money benefits | the other parties and the lower instance, liable to have the decision reviewed | `Art 97(2) the complaint about the finding of the facts can be raised in military or accident insurance` |
| Art 98 | immunity / disability | the other parties and the decision on provisional measures | the appellant, disabled from complaining of anything but violations of constitutional rights | `Art 98 the complaint can be raised against the decision on provisional measures` |
| Art 99(1) | privilege / no-right | the appellant, to put forward new facts and evidence so far as the lower instance's decision gave occasion | the other parties (no-right to have them kept out in that case) | `Art 99(1) the new fact or new evidence may be put forward` |
| Art 99(2) | immunity / disability | the other parties | the appellant, disabled from bringing new claims | `Art 99(2) the new claim is admissible` |
| Art 100(1) | claim / duty | the Federal Supreme Court (to have the appeal filed within 30 days; as encoded, F13, the text states no consequence) | the appellant | `Art 100(1) the appellant's duty to file the appeal within 30 days` (+6 more) |
| Art 100(2) | claim / duty | the Federal Supreme Court (ten days; F13) | the appellant | `Art 100(2) the appellant's duty to file the appeal within ten days` (+1 more) |
| Art 100(2)(a) | claim / duty | the Federal Supreme Court (ten days; F13) | the appellant | `Art 100(2)(a) the period in days is ten for the decision of a cantonal supervisory authority in debt enforcement and bankruptcy matters` |
| Art 100(2)(b) | claim / duty | the Federal Supreme Court (ten days; F13) | the appellant | `Art 100(2)(b) the period in days is ten for the decision in international legal assistance in criminal matters or international administrative assistance in tax matters` |
| Art 100(2)(c) | claim / duty | the Federal Supreme Court (ten days; F13) | the appellant | `Art 100(2)(c) the period in days is ten for the decision on the return of a child` |
| Art 100(2)(d) | claim / duty | the Federal Supreme Court (ten days; F13) | the appellant | `Art 100(2)(d) the period in days is ten for the decision of the Federal Patent Court on a licence` |
| Art 100(3) | claim / duty | the Federal Supreme Court (five days; F13) | the appellant | `Art 100(3) the appellant's duty to file the appeal within five days` (+1 more) |
| Art 100(3)(a) | claim / duty | the Federal Supreme Court (five days; F13) | the appellant | `Art 100(3)(a) the period in days is five for the decision of a cantonal supervisory authority in bill-of-exchange enforcement` |
| Art 100(3)(b) | claim / duty | the Federal Supreme Court (five days; F13) | the appellant | `Art 100(3)(b) the period in days is five for the decision of a cantonal government on an appeal against a federal vote` |
| Art 100(4) | claim / duty | the Federal Supreme Court (three days; F13) | the appellant | `Art 100(4) the appellant's duty to file the appeal within three days` (+1 more) |
| Art 100(5) | none | a counting rule: when the period of an intercantonal conflict of competence begins to run | | `Art 100(5) the latest day the period begins to run` |
| Art 100(6) | none | repealed in this text | | `Art 100(6) is shown repealed in this text and is not encoded` |
| Art 100(7) | privilege / no-right | the person who appeals against an unlawful refusal or delay, at any time | the authority (no-right to rely on the lapse of time) | `Art 100(7) the appeal can be brought at any time` |
| Art 101 | claim / duty | the Federal Supreme Court (30 days from publication of the enactment; F13) | the appellant | `Art 101 the appellant's duty to file the appeal against an enactment within 30 days` (+2 more) |
| Art 102(1) | claim / duty | the lower instance and the other parties, participants and authorities entitled to appeal, to be served the appeal and given a time limit for observations "soweit erforderlich" | the Federal Supreme Court | `Art 102(1) the Court's duty to serve the appeal and set a time limit` (+1 more) |
| Art 102(2) | claim / duty | the Federal Supreme Court (the files, within the time limit) | the lower instance | `Art 102(2) the lower instance's duty to send the files within the time limit` (+1 more) |
| Art 102(3) | none | a rule on how the exchange of submissions runs ("in der Regel"); it gives no one a claim or power | | `Art 102(3) a further exchange of submissions takes place` |
| Art 103(1) | none | a default about the effect of the appeal ("in der Regel keine aufschiebende Wirkung"); it gives no one a claim or power | | `Art 103(1) the appeal has suspensive effect` |
| Art 103(2) | immunity / disability | the appellant, from enforcement of the decision to the extent of the claims | the other party and the enforcing authority, disabled | `Art 103(2) the appeal has suspensive effect to the extent of the claims` |
| Art 103(2)(a) | immunity / disability | the appellant against a decision that creates, changes or ends a legal relationship (Gestaltungsurteil), in civil matters | the other party, disabled from enforcing it meanwhile | `Art 103(2)(a) the appeal has suspensive effect in civil matters` |
| Art 103(2)(b) | immunity / disability | the appellant against an unconditional custodial sentence or a measure depriving of liberty, in criminal matters (not the decision on civil claims) | the enforcing authority, disabled | `Art 103(2)(b) the appeal has suspensive effect in criminal matters` |
| Art 103(2)(c) | immunity / disability | the appellant in international legal assistance in criminal matters against a final order or an order that allows information or objects or assets to be handed over | the requesting side and the enforcing authority, disabled | `Art 103(2)(c) the appeal has suspensive effect in international legal assistance in criminal matters` |
| Art 103(2)(d) | immunity / disability | the appellant in international administrative assistance in tax matters | the enforcing authority, disabled | `Art 103(2)(d) the appeal has suspensive effect in international administrative assistance in tax matters` |
| Art 103(3) | power / liability | the instructing judge, to order otherwise on suspensive effect (of its own motion or on a party's request) | the parties, liable | `Art 103(3) the instructing judge may make a different order on suspensive effect` |
| Art 104 | power / liability | the instructing judge, to order provisional measures (of its own motion or on a party's request) | the parties, liable | `Art 104 the instructing judge may order a provisional measure` |
| Art 105(1) | claim / duty | the parties (to have the judgment rest on the facts the lower instance found) | the Federal Supreme Court | `Art 105(1) the Court bases its judgment on the facts found by the lower instance` |
| Art 105(2) | power / liability | the Federal Supreme Court, to correct or supplement the finding of the facts of its own motion | the parties and the lower instance's finding, liable | `Art 105(2) the Court may correct or supplement the finding of the facts` |
| Art 105(3) | privilege / no-right | the Federal Supreme Court (not bound by the lower instance's finding, in military and accident insurance money benefits) | the parties (no-right to hold the Court to it) | `Art 105(3) the Court is bound by the finding of the facts` |
| Art 106(1) | claim / duty | the parties (to have the law applied of the Court's own motion) | the Federal Supreme Court | `Art 106(1) the Court applies the rule of its own motion` |
| Art 106(2) | immunity / disability | the lower decision, on fundamental rights and on cantonal and intercantonal law, unless a complaint was raised and reasoned | the Federal Supreme Court, disabled from examining them without such a complaint | `Art 106(2) the Court examines the violation` |
| Art 107(1) | immunity / disability | the parties (the claims as the limit of the judgment) | the Federal Supreme Court, disabled from going beyond the claims | `Art 107(1) the Court is permitted to go beyond the claims of the parties` |
| Art 107(2) | power / liability | the Federal Supreme Court, on upholding the appeal, to decide the matter itself or remit it | the parties and the lower instances, liable | `Art 107(2) the Court may give this outcome when it upholds the appeal` |
| Art 107(3) first sentence | claim / duty | the appellant (a decision of non-entry within 15 days after the exchange of submissions, in international legal assistance in criminal matters and administrative assistance in tax matters) | the Federal Supreme Court | `Art 107(3) the Court's duty to give the decision not to enter within 15 days` (+2 more) |
| Art 107(3) second sentence | privilege / no-right | the Federal Supreme Court (not bound by that period in extradition where the person has no final decision on an asylum application) | the person concerned (no-right to the 15 days) | `Art 107(3) the Court is bound by the period of 15 days` (+1 more) |
| Art 107(4) | claim / duty | the parties to the licence appeal (a decision within one month of the appeal being brought) | the Federal Supreme Court | `Art 107(4) the Court's duty to decide within one month` (+2 more) |
| Art 108(1) | power / liability | the president of the division, to decide alone on non-entry in the simplified procedure | the appellant, liable | `Art 108(1) the president of the division decides in the simplified procedure on non-entry` |
| Art 108(1)(a) | power / liability | the president of the division, on an obviously inadmissible appeal | the appellant, liable | `Art 108(1)(a) the president of the division decides in the simplified procedure on non-entry because the appeal is obviously inadmissible` |
| Art 108(1)(b) | power / liability | the president of the division, on an appeal obviously without sufficient reasoning (Art 42(2)) | the appellant, liable | `Art 108(1)(b) the president of the division decides in the simplified procedure on non-entry because the appeal obviously lacks sufficient reasoning` |
| Art 108(1)(c) | power / liability | the president of the division, on a querulous or abusive appeal | the appellant, liable | `Art 108(1)(c) the president of the division decides in the simplified procedure on non-entry because the appeal is querulous or an abuse of rights` |
| Art 108(2) | power / liability | the president of the division, to entrust another judge | the other judge and the parties, liable | `Art 108(2) the president of the division may entrust another judge with the decision` |
| Art 108(3) | privilege / no-right | the Federal Supreme Court (the reasons confined to a short statement of the ground of inadmissibility) | the appellant (no-right to fuller reasons) | `Art 108(3) the reasons of the decision are confined to a short statement of the ground of inadmissibility` |
| Art 109(1) first sentence | power / liability | the division, to decide in a bench of three on non-entry | the appellant, liable | `Art 109(1) the division decides in a bench of three on non-entry` (+2 more) |
| Art 109(1) second sentence | none | disapplies Art 58(1)(b), a rule outside the sources; it gives no one a claim or power of its own | | `Art 109(1) Art 58(1)(b) is applicable to the decision` |
| Art 109(2) | power / liability | the division, to decide unanimously in a bench of three | the parties, liable | `Art 109(2) the division decides in a bench of three` |
| Art 109(2)(a) | power / liability | the division, to dismiss an obviously unfounded appeal unanimously | the appellant, liable | `Art 109(2)(a) the division decides in a bench of three on dismissing the obviously unfounded appeal` |
| Art 109(2)(b) | power / liability | the division, to uphold an obviously well-founded appeal unanimously | the respondent, liable | `Art 109(2)(b) the division decides in a bench of three on upholding the obviously well founded appeal` |
| Art 109(3) first sentence | claim / duty | the parties (to summary reasons) | the Federal Supreme Court | `Art 109(3) the decision is given summary reasons` |
| Art 109(3) second sentence | privilege / no-right | the Federal Supreme Court (may refer wholly or partly to the challenged decision) | the parties (no-right to reasons of its own) | `Art 109(3) the reasons may refer wholly or in part to the challenged decision` |
| Art 110 | claim / duty | the person who can appeal (free review of the facts and the law applied of its own motion) | the canton, where it must set up a court as last cantonal instance | `Art 110 the cantons' duty to ensure the review by a judicial authority` (+3 more) |
| Art 111(1) | claim / duty | the person entitled to appeal (to take part as a party before all cantonal lower instances) | the canton | `Art 111(1) the cantons' duty to let a person entitled to appeal take part as a party` (+4 more) |
| Art 111(2) | power / liability | a federal authority entitled to appeal, to use the cantonal remedies and take part before every cantonal instance on its request | the canton and its instances, liable | `Art 111(2) the federal authority may take the remedies of cantonal law and take part before every cantonal instance` |
| Art 111(3) first sentence | claim / duty | the appellant (the complaints of Art 95 to 98 can be examined by the immediate lower instance) | the canton | `Art 111(3) the cantons' duty to let the immediate lower instance examine the complaints under Art 95 to 98` (+1 more) |
| Art 111(3) second sentence | none | repealed or blank in this text | | `Art 111(3) second sentence is shown repealed in this text and is not encoded` |
| Art 112(1) | claim / duty | the parties (written notification of a decision that can be appealed) | the cantonal authority | `Art 112(1) the cantonal authority's duty to notify the decision to the parties in writing` (+2 more) |
| Art 112(1)(a) | claim / duty | the parties (the claims, reasoning, evidence and declarations of the parties in the decision) | the cantonal authority | `Art 112(1)(a) the decision contains the claims, reasoning, evidence and procedural declarations of the parties` |
| Art 112(1)(b) | claim / duty | the parties (the governing reasons of fact and law) | the cantonal authority | `Art 112(1)(b) the decision contains the governing reasons of fact and law` |
| Art 112(1)(c) | claim / duty | the parties (the operative part) | the cantonal authority | `Art 112(1)(c) the decision contains the operative part` |
| Art 112(1)(d) | claim / duty | the parties (a notice of legal remedies with the value in dispute where the Act provides a value limit) | the cantonal authority | `Art 112(1)(d) chapter 3 provides a value limit for the appeal` (+2 more) |
| Art 112(2) first sentence | privilege / no-right | the cantonal authority (to notify promptly and without reasons where federal or cantonal law so provides) | the parties (no-right to reasons at that time) | `Art 112(2) the authority may notify the decision promptly and without reasons` |
| Art 112(2) second sentence | power / liability | the parties (to demand the complete version within 30 days) | the cantonal authority, liable | `Art 112(2) the parties' permission to demand the complete version within 30 days` (+2 more) |
| Art 112(2) third sentence | immunity / disability | the parties (the decision cannot be enforced until the period lapses unused or the complete version is notified) | the enforcing authority and the other party, disabled | `Art 112(2) the bar on enforcing the decision still applies` |
| Art 112(3) | power / liability | the Federal Supreme Court, to remit or quash a decision that falls short of paragraph 1 | the cantonal authority, liable | `Art 112(3) the Court may remit the decision for improvement or quash it` |
| Art 112(4) | claim / duty | a federal authority entitled to appeal (notification of the decisions the Federal Council determines) | the cantonal authority | `Art 112(4) the cantonal authority must notify the decision to the federal authority` |

## Seams to chapter 3

A seam is a place where a chapter 4 provision meets a chapter 3 function.
The chapter 3 modules are read-only, and no chapter 3 function calls a chapter 4 function (`mknotes` checked that no `bgg3-*.l4` file mentions `bgg4`), so every seam lives in `bgg4-seams.l4`, which imports all six chapter 3 modules and calls them.
Two seams are named by the text itself: Art 109(1) ("Art. 74 und 83–85") and chapter 3's Art 77(2), which names chapter 4; the others are seams of meaning: Art 110 ("Soweit die Kantone nach diesem Gesetz als letzte kantonale Instanz ein Gericht einzusetzen haben"), Art 111(1) ("Wer zur Beschwerde an das Bundesgericht berechtigt ist"), Art 112(1)(d) ("soweit dieses Gesetz eine Streitwertgrenze vorsieht") and the questions that ask both chapters at once.

| chapter 4 provision | chapter 3 function or type it calls | what a person asking both gets |
| --- | --- | --- |
| Art 90 to 93, Art 94, Art 100, Art 101 with chapter 3 Art 72 / 78 / 82 and Art 76(1) / 81(1) / 89(1) | `Art 72 the appeal in civil matters lies against the decision`, `Art 78 ...criminal...`, `Art 82 ...public-law...`; `Art 76(1)`, `Art 81(1)`, `Art 89(1)` (the "entitled to appeal" functions); `Person in a criminal appeal`; the three record functions `Art 72, 76 and 90 to 101 the answers ...`, `Art 78, 81 and 90 to 101 ...`, `Art 82, 89 and 90 to 101 ...` | A record of five fields, one per section and no combined verdict (ruling E1 option C, fork F28): chapter 3 says the appeal lies against the decision, chapter 3 says the person is entitled, chapter 4 says the act can be appealed, chapter 4 says the appeal is in time, chapter 4 says the time limit. Each field is JUST TRUE, JUST FALSE or NOTHING as its own chapter says; the person reads the five answers together, and none is turned into another. |
| Art 90 to 98, 103(2), 105(2), 106(1), 107(2) with chapter 3 Art 77(2) | `Art 77(2) the listed provision is applicable to the appeal against the arbitral award` (called as `Art 77(2) the answer of a chapter 4 provision stands for the appeal`) | For an appeal against an arbitral award of Art 77(1) the chapter 4 answer is NOTHING (fork F29); for any other appeal the chapter 4 answer stands; Art 99 is not named by Art 77(2) and stays applicable. |
| Art 111(1) | `Art 76(1)`, `Art 81(1)`, `Art 89(1)` by `Kind of appeal` (`Art 111(1) the person is entitled to appeal, by chapter 3`) | The cantons' duty to let a person take part as a party arises only for a person chapter 3 says is entitled (JUST TRUE); a chapter 3 NOTHING stays NOTHING, and a kind of appeal other than civil, criminal and public-law gives NOTHING. |
| Art 110 | `Art 86(3) the canton may set up an authority other than a court as immediate lower instance`; the duty of Art 75(2), 80(2) and 86(2), read through `Kind of appeal` (`Art 110 the canton must set up a court as last cantonal instance under chapter 3`) | The cantons' duty to ensure free review exists for a civil or criminal appeal and for a public-law appeal that is not a decision of predominantly political character; for such a decision, and for another kind of appeal, NOTHING. |
| Art 112(1)(d) | `Art 74(1) the value in dispute is enough` and `Art 85(1) the appeal is admissible in a pecuniary matter`, each called with a value of 0 francs (`Art 112(1)(d) chapter 3 provides a value limit for the appeal`) | Whether "dieses Gesetz eine Streitwertgrenze vorsieht" is asked of chapter 3: JUST TRUE where Art 74(1) or Art 85(1) engages a limit, NOTHING otherwise; where chapter 3 does not settle it the notice is judged both ways and the answer stands only if it is the same (fork F30). |
| Art 109(1) | `Art 74(1)`, `Art 74(2)(b)` to `(e)`, `Art 84(1)`, `Art 84(2)`, `Art 84a`, `Art 85(1)`, `Subject of a legal assistance decision`, `Kind of appeal` and `Deciding body` (`Art 109(1) the condition on which the appeal is admissible, by chapters 3`) | Which condition the appeal depends on is derived from chapter 3 for international legal assistance in criminal matters, tax assistance, a public-law pecuniary matter below the limit of Art 85(1) and a civil pecuniary matter below the limit of Art 74(1) (fork F32); the conditions of chapter 3's Art 83 (f)(1), (m), (w), (x), (z) and (zbis) are not derived and the question has no input for them, so the answer is NOTHING (fork F26). |
| Art 100, 101 | none: chapter 3 states no period | Chapter 4 supplies the periods; chapter 3 has no function for them to feed. |

Does chapter 4 now supply what chapter 3 answered NOTHING for, and does any chapter 3 function call it?

- **Which decisions can be appealed, and by when.** Chapter 3's notes say that it says "which decisions are appealable and who may appeal, not how and by when". Chapter 4 supplies both (`bgg4-appealable`, `bgg4-time-limit`), and none of chapter 3's functions calls them; the three record functions are where a person gets both chapters.
- **The value in dispute.** Chapter 3's notes say "how it is worked out is in chapter 4". The chapter 4 text does not say so: "Streitwert" occurs once in it, in Art 112(1)(d), which asks only whether the notice of remedies states a value where the Act provides a limit. So chapter 4 does not supply the rule, the value stays an input of `Art 74(1)` and `Art 85(1)`, and the brief places the rules on the value in dispute in chapter 2 (outside the sources, not checked here).
- **Chapter 3's Art 77(2)** names chapter 4. Its function takes the number of the provision; a search of the code lines of `bgg3-*.l4` for the Article numbers 90 to 112 finds only that function (`bgg3-civil.l4` lines 476 to 487), so it is the only place where chapter 3 asks about chapter 4.
- **The cantons' duties** (Art 75(2), 80(2), 86(2), 88(2)) have no time limit in chapter 3 and none in Art 110 to 112; chapter 4 states a time only for the notification of a decision (the 30 days to demand the complete version, Art 112(2)).

## Coverage table

Built by `coverage.py` from the text, one row per heading, paragraph, list item and sentence (where one paragraph carries two or three sentences that are encoded differently: Art 107(3), 109(1), 109(3), 111(3), 112(2)).
Every one of the 134 non-blank lines of the 166-line file falls in some row (`coverage.py` checks it and reports "problems: 0"), and every row has exactly one disposition.
The footnote lines 151 to 166 are one inert row of reason 1 (not operative: amendment history); two of them describe repealed rows, footnote 9 (Art 100(6), line 74) and footnote 15 (second sentence of Art 111(3), line 139), which are rows `repealed or blank in this text`; footnotes 1, 2, 3, 4, 7, 10, 11, 12, 14 and 16 record amendments and insertions, and footnotes 5, 6, 8 and 13 give a systematic-collection number (SR).
There is no `out-of-scope` and no `deferred` row.
The "seat questions" column counts the seat questions whose call graph reaches a function of the row.

Audit: the text has 23 Articles in 7 sections, 44 numbered paragraphs, 30 list items and 9 unnumbered article bodies in lines 1 to 150, so 83 operative lines; the table has 89 operative rows because five of those lines (Art 107(3), 109(1), 109(3), 111(3) and 112(2)) are cut into 11 sentence rows, which adds 6 rows; with 31 heading rows, the header row and the footnote row, 122 rows in all.
Counts: 17 encoded, 70 fork, 33 inert (all reason 1: 31 headings, the file header and the footnotes; none of reason 2 or 3), 2 repealed or blank in this text.
A row marked `fork` points at the fork register entry or entries (every reading, and the text that licenses each) and at the rule that encodes the reading taken.

| row | lines | German begins | disposition | modules | tests | seat questions |
| --- | --- | --- | --- | --- | --- | --- |
| File header | 1-5 | Schweizerisches Bundesrecht, SR 173.110: cha | inert (reason 1: not operative, the file header) |  |  |  |
| Chapter 4 heading | 7 | 4. Kapitel: Beschwerdeverfahren | inert (reason 1: a heading) |  |  |  |
| Section 1 heading | 8 | 1. Abschnitt: Anfechtbare Entscheide | inert (reason 1: a heading) |  |  |  |
| Art 90 heading | 10 | Art. 90 Endentscheide | inert (reason 1: a heading) |  |  |  |
| Art 90 | 11 | Die Beschwerde ist zulässig gegen Entscheide | encoded | appealable, seams | 61 | 12 |
| Art 91 heading | 13 | Art. 91 Teilentscheide | inert (reason 1: a heading) |  |  |  |
| Art 91 (intro) | 14 | Die Beschwerde ist zulässig gegen einen Ents | fork F1 | appealable, seams | 64 | 12 |
| Art 91(a) | 15 | nur einen Teil der gestellten Begehren behan | fork F1 | appealable, seams | 68 | 12 |
| Art 91(b) | 16 | das Verfahren nur für einen Teil der Streitg | encoded | appealable, seams | 66 | 12 |
| Art 92 heading | 18 | Art. 92 Vor- und Zwischenentscheide über die | inert (reason 1: a heading) |  |  |  |
| Art 92(1) | 19 | Gegen selbständig eröffnete Vor- und Zwische | encoded | appealable, seams | 63 | 13 |
| Art 92(2) | 20 | Diese Entscheide können später nicht mehr an | encoded | appealable, seams | 16 | 10 |
| Art 93 heading | 22 | Art. 93 Andere Vor- und Zwischenentscheide | inert (reason 1: a heading) |  |  |  |
| Art 93(1) | 23 | Gegen andere selbständig eröffnete Vor- und  | fork F2, F4 | appealable, seams | 65 | 12 |
| Art 93(1)(a) | 24 | wenn sie einen nicht wieder gutzumachenden N | fork F2 | appealable, seams | 67 | 12 |
| Art 93(1)(b) | 25 | wenn die Gutheissung der Beschwerde sofort e | fork F2 | appealable, seams | 68 | 12 |
| Art 93(2) | 26 | Auf dem Gebiet der internationalen Rechtshil | fork F2, F4 | appealable, seams | 66 | 12 |
| Art 93(3) | 27 | Ist die Beschwerde nach den Absätzen 1 und 2 | fork F3 | appealable, seams | 18 | 10 |
| Art 94 heading | 29 | Art. 94 Rechtsverweigerung und Rechtsverzöge | inert (reason 1: a heading) |  |  |  |
| Art 94 | 30 | Gegen das unrechtmässige Verweigern oder Ver | encoded | appealable, seams | 53 | 13 |
| Section 2 heading | 32 | 2. Abschnitt: Beschwerdegründe | inert (reason 1: a heading) |  |  |  |
| Art 95 heading | 34 | Art. 95 Schweizerisches Recht | inert (reason 1: a heading) |  |  |  |
| Art 95 (intro) | 35 | Mit der Beschwerde kann die Verletzung gerüg | fork F5 | grounds, seams | 19 | 9 |
| Art 95(a) | 36 | Bundesrecht; | fork F5 | grounds, seams | 21 | 9 |
| Art 95(b) | 37 | Völkerrecht; | fork F5 | grounds, seams | 21 | 9 |
| Art 95(c) | 38 | kantonalen verfassungsmässigen Rechten; | fork F5 | grounds, seams | 21 | 9 |
| Art 95(d) | 39 | kantonalen Bestimmungen über die politische  | fork F5 | grounds, seams | 21 | 9 |
| Art 95(e) | 40 | interkantonalem Recht. | fork F5 | grounds, seams | 21 | 9 |
| Art 96 heading | 42 | Art. 96 Ausländisches Recht | inert (reason 1: a heading) |  |  |  |
| Art 96 (intro) | 43 | Mit der Beschwerde kann gerügt werden: | fork F5 | grounds, seams | 17 | 9 |
| Art 96(a) | 44 | ausländisches Recht sei nicht angewendet wor | fork F5 | grounds, seams | 19 | 9 |
| Art 96(b) | 45 | das nach dem schweizerischen internationalen | fork F6 | grounds, seams | 20 | 9 |
| Art 97 heading | 47 | Art. 97 Unrichtige Feststellung des Sachverh | inert (reason 1: a heading) |  |  |  |
| Art 97(1) | 48 | Die Feststellung des Sachverhalts kann nur g | fork F7 | grounds, seams | 24 | 9 |
| Art 97(2) | 49 | Richtet sich die Beschwerde gegen einen Ents | fork F7 | grounds, seams | 20 | 9 |
| Art 98 heading | 51 | Art. 98 Beschränkte Beschwerdegründe | inert (reason 1: a heading) |  |  |  |
| Art 98 | 52 | Mit der Beschwerde gegen Entscheide über vor | encoded | grounds, seams | 17 | 9 |
| Section 3 heading | 54 | 3. Abschnitt: Neue Vorbringen | inert (reason 1: a heading) |  |  |  |
| Art 99 heading | 56 | Art. 99 | inert (reason 1: a heading) |  |  |  |
| Art 99(1) | 57 | Neue Tatsachen und Beweismittel dürfen nur s | fork F8 | new-submissions | 4 | 1 |
| Art 99(2) | 58 | Neue Begehren sind unzulässig. | encoded | new-submissions | 2 | 1 |
| Section 4 heading | 60 | 4. Abschnitt: Beschwerdefrist | inert (reason 1: a heading) |  |  |  |
| Art 100 heading | 62 | Art. 100 Beschwerde gegen Entscheide | inert (reason 1: a heading) |  |  |  |
| Art 100(1) | 63 | Die Beschwerde gegen einen Entscheid ist inn | fork F9, F10, F12, F13 | seams, time-limit | 83 | 9 |
| Art 100(2) | 64 | Die Beschwerdefrist beträgt zehn Tage: | fork F13 | time-limit | 15 | 6 |
| Art 100(2)(a) | 65 | bei Entscheiden der kantonalen Aufsichtsbehö | fork F11 | time-limit | 17 | 6 |
| Art 100(2)(b) | 66 | bei Entscheiden auf den Gebieten der interna | encoded | time-limit | 17 | 6 |
| Art 100(2)(c) | 67 | bei Entscheiden über die Rückgabe eines Kind | encoded | time-limit | 17 | 6 |
| Art 100(2)(d) | 68 | bei Entscheiden des Bundespatentgerichts übe | encoded | time-limit | 17 | 6 |
| Art 100(3) | 69 | Die Beschwerdefrist beträgt fünf Tage: | fork F13 | time-limit | 13 | 6 |
| Art 100(3)(a) | 70 | bei Entscheiden der kantonalen Aufsichtsbehö | fork F11 | time-limit | 16 | 6 |
| Art 100(3)(b) | 71 | bei Entscheiden der Kantonsregierungen über  | encoded | time-limit | 15 | 6 |
| Art 100(4) | 72 | Bei Entscheiden der Kantonsregierungen über  | fork F13 | time-limit | 11 | 6 |
| Art 100(5) | 73 | Bei Beschwerden wegen interkantonaler Kompet | fork F12 | time-limit | 34 | 5 |
| Art 100(6) | 74 | …[^9] | repealed or blank in this text | time-limit |  |  |
| Art 100(7) | 75 | Gegen das unrechtmässige Verweigern oder Ver | encoded | seams, time-limit | 43 | 5 |
| Art 101 heading | 77 | Art. 101 Beschwerde gegen Erlasse | inert (reason 1: a heading) |  |  |  |
| Art 101 | 78 | Die Beschwerde gegen einen Erlass ist innert | fork F9, F10, F13 | seams, time-limit | 51 | 5 |
| Section 5 heading | 80 | 5. Abschnitt: Weitere Verfahrensbestimmungen | inert (reason 1: a heading) |  |  |  |
| Art 102 heading | 82 | Art. 102 Schriftenwechsel | inert (reason 1: a heading) |  |  |  |
| Art 102(1) | 83 | Soweit erforderlich stellt das Bundesgericht | fork F27 | procedure | 4 | 1 |
| Art 102(2) | 84 | Die Vorinstanz hat innert dieser Frist die V | fork F13 | procedure | 5 |  |
| Art 102(3) | 85 | Ein weiterer Schriftenwechsel findet in der  | fork F14 | procedure | 2 | 1 |
| Art 103 heading | 87 | Art. 103 Aufschiebende Wirkung | inert (reason 1: a heading) |  |  |  |
| Art 103(1) | 88 | Die Beschwerde hat in der Regel keine aufsch | fork F31 | procedure | 7 | 1 |
| Art 103(2) | 89 | Die Beschwerde hat im Umfang der Begehren au | fork F15, F16 | procedure, seams | 25 | 10 |
| Art 103(2)(a) | 90 | in Zivilsachen, wenn sie sich gegen ein Gest | fork F15 | procedure, seams | 28 | 10 |
| Art 103(2)(b) | 91 | in Strafsachen, wenn sie sich gegen einen En | fork F15 | procedure, seams | 29 | 10 |
| Art 103(2)(c) | 92 | in Verfahren auf dem Gebiet der internationa | fork F15 | procedure, seams | 29 | 10 |
| Art 103(2)(d) | 93 | in Verfahren auf dem Gebiet der internationa | encoded | procedure, seams | 27 | 10 |
| Art 103(3) | 94 | Der Instruktionsrichter oder die Instruktion | fork F17 | procedure | 8 | 1 |
| Art 104 heading | 96 | Art. 104 Andere vorsorgliche Massnahmen | inert (reason 1: a heading) |  |  |  |
| Art 104 | 97 | Der Instruktionsrichter oder die Instruktion | fork F17 | procedure | 3 | 1 |
| Art 105 heading | 99 | Art. 105 Massgebender Sachverhalt | inert (reason 1: a heading) |  |  |  |
| Art 105(1) | 100 | Das Bundesgericht legt seinem Urteil den Sac | fork F18 | procedure | 6 | 1 |
| Art 105(2) | 101 | Es kann die Sachverhaltsfeststellung der Vor | fork F17, F18 | procedure, seams | 20 | 10 |
| Art 105(3) | 102 | Richtet sich die Beschwerde gegen einen Ents | fork F18 | procedure | 6 | 1 |
| Art 106 heading | 104 | Art. 106 Rechtsanwendung | inert (reason 1: a heading) |  |  |  |
| Art 106(1) | 105 | Das Bundesgericht wendet das Recht von Amtes | fork F19 | procedure, seams | 18 | 9 |
| Art 106(2) | 106 | Es prüft die Verletzung von Grundrechten und | fork F19 | procedure | 10 | 1 |
| Art 107 heading | 108 | Art. 107 Entscheid | inert (reason 1: a heading) |  |  |  |
| Art 107(1) | 109 | Das Bundesgericht darf nicht über die Begehr | fork F33 | procedure | 1 | 1 |
| Art 107(2) | 110 | Heisst das Bundesgericht die Beschwerde gut, | fork F5 | procedure, seams | 18 | 9 |
| Art 107(3) first sentence | 111 | Erachtet das Bundesgericht eine Beschwerde a | fork F9, F13, F20 | procedure | 14 | 1 |
| Art 107(3) second sentence | 111 | Auf dem Gebiet der internationalen Rechtshil | fork F34 | procedure | 9 | 1 |
| Art 107(4) | 112 | Über Beschwerden gegen Entscheide des Bundes | fork F13, F21 | procedure | 14 | 1 |
| Section 6 heading | 114 | 6. Abschnitt: Vereinfachtes Verfahren | inert (reason 1: a heading) |  |  |  |
| Art 108 heading | 116 | Art. 108 Einzelrichter oder Einzelrichterin | inert (reason 1: a heading) |  |  |  |
| Art 108(1) | 117 | Der Präsident oder die Präsidentin der Abtei | fork F17 | simplified | 4 | 1 |
| Art 108(1)(a) | 118 | Nichteintreten auf offensichtlich unzulässig | fork F17 | simplified | 6 | 1 |
| Art 108(1)(b) | 119 | Nichteintreten auf Beschwerden, die offensic | fork F17 | simplified | 6 | 1 |
| Art 108(1)(c) | 120 | Nichteintreten auf querulatorische oder rech | fork F17 | simplified | 6 | 1 |
| Art 108(2) | 121 | Er oder sie kann einen anderen Richter oder  | fork F17 | simplified | 3 |  |
| Art 108(3) | 122 | Die Begründung des Entscheids beschränkt sic | encoded | simplified | 2 | 1 |
| Art 109 heading | 124 | Art. 109 Dreierbesetzung | inert (reason 1: a heading) |  |  |  |
| Art 109(1) first sentence | 125 | Die Abteilungen entscheiden in Dreierbesetzu | fork F17, F22, F26, F32 | seams, simplified | 50 | 1 |
| Art 109(1) second sentence | 125 | Artikel 58 Absatz 1 Buchstabe b findet keine | encoded | simplified | 3 |  |
| Art 109(2) | 126 | Sie entscheiden ebenfalls in Dreierbesetzung | fork F17 | simplified | 4 | 1 |
| Art 109(2)(a) | 127 | Abweisung offensichtlich unbegründeter Besch | fork F17 | simplified | 7 | 1 |
| Art 109(2)(b) | 128 | Gutheissung offensichtlich begründeter Besch | fork F17 | simplified | 8 | 1 |
| Art 109(3) first sentence | 129 | Der Entscheid wird summarisch begründet. | encoded | simplified | 2 | 1 |
| Art 109(3) second sentence | 129 | Es kann ganz oder teilweise auf den angefoch | fork F17 | simplified | 2 | 1 |
| Section 7 heading | 131 | 7. Abschnitt: Kantonales Verfahren | inert (reason 1: a heading) |  |  |  |
| Art 110 heading | 133 | Art. 110 Beurteilung durch richterliche Behö | inert (reason 1: a heading) |  |  |  |
| Art 110 | 134 | Soweit die Kantone nach diesem Gesetz als le | fork F27 | cantonal, seams | 15 | 1 |
| Art 111 heading | 136 | Art. 111 Einheit des Verfahrens | inert (reason 1: a heading) |  |  |  |
| Art 111(1) | 137 | Wer zur Beschwerde an das Bundesgericht bere | fork F27 | cantonal, seams | 14 | 1 |
| Art 111(2) | 138 | Bundesbehörden, die zur Beschwerde an das Bu | fork F17 | cantonal | 3 |  |
| Art 111(3) first sentence | 139 | Die unmittelbare Vorinstanz des Bundesgerich | fork F27 | cantonal | 3 | 1 |
| Art 111(3) second sentence | 139 | …[^15] | repealed or blank in this text | cantonal |  |  |
| Art 112 heading | 141 | Art. 112 Eröffnung der Entscheide | inert (reason 1: a heading) |  |  |  |
| Art 112(1) | 142 | Entscheide, die der Beschwerde an das Bundes | fork F23 | cantonal | 13 | 1 |
| Art 112(1)(a) | 143 | die Begehren, die Begründung, die Beweisvorb | fork F23 | cantonal | 17 | 1 |
| Art 112(1)(b) | 144 | die massgebenden Gründe tatsächlicher und re | fork F23 | cantonal | 16 | 1 |
| Art 112(1)(c) | 145 | das Dispositiv; | fork F23 | cantonal | 16 | 1 |
| Art 112(1)(d) | 146 | eine Rechtsmittelbelehrung einschliesslich A | fork F23, F30 | cantonal, seams | 33 | 2 |
| Art 112(2) first sentence | 147 | Sofern es das Bundesrecht oder das kantonale | fork F24 | cantonal | 2 | 1 |
| Art 112(2) second sentence | 147 | Die Parteien können in diesem Fall innert 30 | fork F9, F10, F13 | cantonal | 12 | 2 |
| Art 112(2) third sentence | 147 | Der Entscheid ist nicht vollstreckbar, solan | fork F10, F25 | cantonal | 9 | 1 |
| Art 112(3) | 148 | Das Bundesgericht kann einen Entscheid, der  | fork F17 | cantonal | 2 | 1 |
| Art 112(4) | 149 | Für die Gebiete, in denen Bundesbehörden zur | encoded | cantonal | 3 | 1 |
| Footnotes (amendment history) | 151-166 | [^1] Fassung gemäss Ziff. I 2 des BG vom 1.  | inert (reason 1: not operative, amendment history; footnotes 9 and 15 show the two repealed rows) |  |  |  |

## Fork register

Every ambiguity, the readings seen, the one taken, and the text that licenses each.
The forks marked "ruling" follow a ruling of the brief and are listed so a reviewer can overrule them.
The row list under each fork is the rows of the coverage table it marks; F28 and F29 mark how sections are put together in `bgg4-seams` and so do not change the disposition of the rows they cover.

- **F1. Art 91(a): a failed "wenn".**
  Text: Art 91(a) "nur einen Teil der gestellten Begehren behandelt, wenn diese Begehren unabhängig von den anderen beurteilt werden können;"
  Readings: (i) a decision on only some of the claims that cannot be judged independently of the others is JUST FALSE (the text's own "wenn" failed, reading (a) of the rule of 2026-10-29); (ii) NOTHING (an "if A then B" does not itself say "if not A then not B").
  Taken: (i).
  Rows: Art 91 (intro), Art 91(a).
  Rule: `Art 91 the appeal is admissible against the partial decision`, `Art 91(a) the appeal is admissible against the decision that deals with only some of the claims` (and 6 more, with the composites and the seams that call them).
- **F2. Art 93(1)(a), (b) and 93(2): a failed "wenn".**
  Text: Art 93(1)(a) "wenn sie einen nicht wieder gutzumachenden Nachteil bewirken können; oder" / Art 93(1)(b) "wenn die Gutheissung der Beschwerde sofort einen Endentscheid herbeiführen und damit einen bedeutenden Aufwand an Zeit oder Kosten für ein weitläufiges Beweisverfahren ersparen würde."
  Readings: (i) a preliminary or interlocutory decision for which neither "wenn" of paragraph 1 (or, in the two fields, of paragraph 2) holds is JUST FALSE; (ii) NOTHING.
  Taken: (i).
  Rows: Art 93(1), Art 93(1)(a), Art 93(1)(b), Art 93(2).
  Rule: `Art 93(1)(a) the appeal is admissible because the decision may cause irreparable harm`, `Art 93(1) the appeal is admissible against the other preliminary or interlocutory decision`, `Art 93(2) the appeal is admissible against the preliminary or interlocutory decision in the field`, `Art 93(1)(b) the appeal is admissible because allowing it would immediately bring about a final decision` (and 6 more, with the composites and the seams that call them).
- **F3. Art 93(3): "Ist ..., so".**
  Text: Art 93(3) "Ist die Beschwerde nach den Absätzen 1 und 2 nicht zulässig oder wurde von ihr kein Gebrauch gemacht, so sind die betreffenden Vor- und Zwischenentscheide durch Beschwerde gegen den Endentscheid anfechtbar, soweit sie sich auf dessen Inhalt auswirken."
  Readings: (i) where the appeal at the time was not admissible or no use was made of it, a decision that does not affect the content of the final decision is NOTHING; where the condition "Ist die Beschwerde ... nicht zulässig oder wurde von ihr kein Gebrauch gemacht" fails the answer is JUST FALSE; (ii) JUST FALSE for a decision that does not affect the content.
  Taken: (i).
  Rows: Art 93(3).
  Rule: `Art 93(3) the preliminary or interlocutory decision can be challenged by the appeal against the final decision` (and 1 more, with the composites and the seams that call them).
- **F4. Art 90 to 93: gathering the four routes by hand.**
  Text: Art 90, 91, 92(1) and 93 each grant an appeal against decisions of their own kind, and none says that the others must also hold; ruling E1.
  Readings: (i) the composite `Art 90 to 93 the appeal is admissible against the decision` gathers Art 90, 91, 92(1) and 93 by hand: any JUST TRUE gives JUST TRUE, Art 93(2) answers in place of 93(1) in its two fields, a JUST FALSE of 91 or 93 gives JUST FALSE, otherwise NOTHING; each article still answers by itself (option B of ruling E1, by hand); (ii) per-article answers only, with no composite (option C of E1).
  Taken: (i).
  Rows: Art 93(1), Art 93(2).
  Rule: `Art 93(1) the appeal is admissible against the other preliminary or interlocutory decision`, `Art 93(2) the appeal is admissible against the preliminary or interlocutory decision in the field` (and 6 more, with the composites and the seams that call them).
- **F5. Art 95, 96 and 107(2): a list not closed with "nur".**
  Text: Art 95 (intro) "Mit der Beschwerde kann die Verletzung gerügt werden von:"
  Readings: (i) a source of law, a complaint or an outcome the list does not name is NOTHING; (ii) JUST FALSE (a closed list), which would make ordinary cantonal law "cannot be complained of".
  Taken: (i).
  Rows: Art 95 (intro), Art 95(a), Art 95(b), Art 95(c), Art 95(d), Art 95(e), Art 96 (intro), Art 96(a) and 1 more.
  Rule: `Art 96 the complaint about foreign law can be raised`, `Art 95(a) the violation of federal law can be complained of`, `Art 95 the violation of the source of law can be complained of`, `Art 95(b) the violation of international law can be complained of`, `Art 95(e) the violation of intercantonal law can be complained of` (and 5 more, with the composites and the seams that call them).
- **F6. Art 96(b): a failed "sofern".**
  Text: Art 96(b) "das nach dem schweizerischen internationalen Privatrecht massgebende ausländische Recht sei nicht richtig angewendet worden, sofern der Entscheid keine vermögensrechtliche Sache betrifft."
  Readings: (i) in a pecuniary matter the complaint about wrongly applied foreign law is JUST FALSE (the text's own "sofern ... keine vermögensrechtliche Sache" failed, reading (a)); (ii) NOTHING.
  Taken: (i).
  Rows: Art 96(b).
  Rule: `Art 96(b) the complaint that foreign law was applied wrongly can be raised` (and 2 more, with the composites and the seams that call them).
- **F7. Art 97(2) against Art 97(1).**
  Text: Art 97(1) "Die Feststellung des Sachverhalts kann nur gerügt werden, wenn sie offensichtlich unrichtig ist oder auf einer Rechtsverletzung im Sinne von Artikel 95 beruht und wenn die Behebung des Mangels für den Ausgang des Verfahrens entscheidend sein kann." / Art 97(2) "Richtet sich die Beschwerde gegen einen Entscheid über die Zusprechung oder Verweigerung von Geldleistungen der Militär- oder Unfallversicherung, so kann jede unrichtige oder unvollständige Feststellung des rechtserheblichen Sachverhalts gerügt werden.[^2]"
  Readings: (i) in military and accident insurance benefits paragraph 2 answers in place of paragraph 1 ("nur ... wenn"); (ii) paragraph 1 answers JUST FALSE there and paragraph 2 gives a separate JUST TRUE.
  Taken: (i).
  Rows: Art 97(1), Art 97(2).
  Rule: `Art 97(1) the complaint about the finding of the facts can be raised`, `Art 97(2) the complaint about the finding of the facts can be raised in military or accident insurance` (and 2 more, with the composites and the seams that call them).
- **F8. Art 99(1): "so weit".**
  Text: Art 99(1) "Neue Tatsachen und Beweismittel dürfen nur so weit vorgebracht werden, als erst der Entscheid der Vorinstanz dazu Anlass gibt."
  Readings: (i) whether only the lower instance's decision gave occasion for the new fact or evidence is a yes or no the person states; (ii) a degree: part of the new matter may be allowed.
  Taken: (i).
  Rows: Art 99(1).
  Rule: `Art 99(1) the new fact or new evidence may be put forward`.
- **F9. The day count.**
  Text: Art 100(1) "Die Beschwerde gegen einen Entscheid ist innert 30 Tagen nach der Eröffnung der vollständigen Ausfertigung beim Bundesgericht einzureichen."
  Readings: (i) the day after the notification (or publication, or end of the exchange) is day 1, so the last day is that day plus the period, and a step taken on the last day is in time; outside the period of a period the text fixes in its own words the answer is JUST FALSE (periods ruling (a) of 2026-11-05); (ii) the notification day is day 1 and the last day is one day earlier.
  Taken: (i).
  Rows: Art 100(1), Art 101, Art 107(3) first sentence, Art 112(2) second sentence.
  Rule: `Art 100(1) the appellant's duty to file the appeal within 30 days`, `Art 107(3) the Court's duty to give the decision not to enter within 15 days`, `Art 112(2) the parties' permission to demand the complete version within 30 days`, `Art 101 the appellant's duty to file the appeal against an enactment within 30 days`, `Art 100(1) the general period in days` (and 16 more, with the composites and the seams that call them).
- **F10. Days that rules outside this chapter leave out of the count.**
  Text: Art 100(1) "Die Beschwerde gegen einen Entscheid ist innert 30 Tagen nach der Eröffnung der vollständigen Ausfertigung beim Bundesgericht einzureichen."
  Readings: (i) the rules on suspension and restoration of time limits are in chapter 2, outside the sources, so the number of days they leave out of the count is an input (0 if none) and the last day moves by it; (ii) no such input (the last day is the plain count).
  Taken: (i).
  Rows: Art 100(1), Art 101, Art 112(2) second sentence, Art 112(2) third sentence.
  Rule: `Art 100(1) the appellant's duty to file the appeal within 30 days`, `Art 112(2) the parties' permission to demand the complete version within 30 days`, `Art 101 the appellant's duty to file the appeal against an enactment within 30 days`, `Art 100(1) the general period in days`, `Art 101 the appeal against an enactment is in time` (and 14 more, with the composites and the seams that call them).
- **F11. Bill-of-exchange enforcement: ten days or five.**
  Text: Art 100(2)(a) "bei Entscheiden der kantonalen Aufsichtsbehörden in Schuldbetreibungs- und Konkurssachen;" / Art 100(3)(a) "bei Entscheiden der kantonalen Aufsichtsbehörden in Schuldbetreibungs- und Konkurssachen im Rahmen der Wechselbetreibung;"
  Readings: (i) the decision of a cantonal supervisory authority in bill-of-exchange enforcement is both a (2)(a) and a (3)(a) decision; the shorter, more specific five days governs; (ii) ten days.
  Taken: (i).
  Rows: Art 100(2)(a), Art 100(3)(a).
  Rule: `Art 100(3)(a) the period in days is five for the decision of a cantonal supervisory authority in bill-of-exchange enforcement`, `Art 100(2)(a) the period in days is ten for the decision of a cantonal supervisory authority in debt enforcement and bankruptcy matters` (and 5 more, with the composites and the seams that call them).
- **F12. Art 100(5): the day the period starts from.**
  Text: Art 100(5) "Bei Beschwerden wegen interkantonaler Kompetenzkonflikte beginnt die Beschwerdefrist spätestens dann zu laufen, wenn in beiden Kantonen Entscheide getroffen worden sind, gegen welche beim Bundesgericht Beschwerde geführt werden kann."
  Readings: (i) in an intercantonal conflict of competence the period starts at the notification, but not later than the later of the two cantons' decision days; (ii) the period starts only at the later decision day.
  Taken: (i).
  Rows: Art 100(1), Art 100(5).
  Rule: `Art 100(1) the appellant's duty to file the appeal within 30 days`, `Art 100(1) the general period in days`, `Art 100(5) the latest day the period begins to run`, `Art 100(1) the last day of a period counted from the start day` (and 9 more, with the composites and the seams that call them).
- **F13. Time limits as regulative rules.**
  Text: Art 100(1) "Die Beschwerde gegen einen Entscheid ist innert 30 Tagen nach der Eröffnung der vollständigen Ausfertigung beim Bundesgericht einzureichen." / Art 101 "Die Beschwerde gegen einen Erlass ist innert 30 Tagen nach der nach dem kantonalen Recht massgebenden Veröffentlichung des Erlasses beim Bundesgericht einzureichen."
  Readings: (i) the text states a period and no consequence of missing it, so the regulative rule says `LEST BREACH` and a breach here means only that the period was missed; the decision functions give the answer for the person; (ii) no regulative rule, decision function only.
  Taken: (i).
  Rows: Art 100(1), Art 100(2), Art 100(3), Art 100(4), Art 101, Art 102(2), Art 107(3) first sentence, Art 107(4) and 1 more.
  Rule: `Art 107(4) the Court's duty to decide within one month`, `Art 100(1) the appellant's duty to file the appeal within 30 days`, `Art 100(2) the appellant's duty to file the appeal within ten days`, `Art 100(3) the appellant's duty to file the appeal within five days`, `Art 100(4) the appellant's duty to file the appeal within three days` (and 27 more, with the composites and the seams that call them).
- **F14. Art 102(3): "in der Regel".**
  Text: Art 102(3) "Ein weiterer Schriftenwechsel findet in der Regel nicht statt."
  Readings: (i) a case the person says is an exception to "in der Regel nicht" is NOTHING (the text names no exception); otherwise JUST FALSE (a flat negative, ruling N2); (ii) JUST FALSE for every case.
  Taken: (i).
  Rows: Art 102(3).
  Rule: `Art 102(3) a further exchange of submissions takes place`.
- **F15. Art 103(2)(a) to (c): a failed "wenn".**
  Text: Art 103(2)(a) "in Zivilsachen, wenn sie sich gegen ein Gestaltungsurteil richtet;" / Art 103(2)(b) "in Strafsachen, wenn sie sich gegen einen Entscheid richtet, der eine unbedingte Freiheitsstrafe oder eine freiheitsentziehende Massnahme ausspricht; die aufschiebende Wirkung erstreckt sich nicht auf den Entscheid über Zivilansprüche;"
  Readings: (i) an appeal in the named matter for which the "wenn" fails has JUST FALSE suspensive effect under paragraph 2 (reading (a)); (ii) NOTHING.
  Taken: (i).
  Rows: Art 103(2), Art 103(2)(a), Art 103(2)(b), Art 103(2)(c).
  Rule: `Art 103(2)(a) the appeal has suspensive effect in civil matters`, `Art 103(2)(b) the appeal has suspensive effect in criminal matters`, `Art 103(2) the appeal has suspensive effect to the extent of the claims`, `Art 103(2)(c) the appeal has suspensive effect in international legal assistance in criminal matters` (and 2 more, with the composites and the seams that call them).
- **F16. Art 103(2): "im Umfang der Begehren".**
  Text: Art 103(2) "Die Beschwerde hat im Umfang der Begehren aufschiebende Wirkung:"
  Readings: (i) the extent "im Umfang der Begehren" is not computed: the function says whether the appeal has the effect, and the effect reaches what the appeal claims; (ii) a per-claim answer.
  Taken: (i).
  Rows: Art 103(2).
  Rule: `Art 103(2) the appeal has suspensive effect to the extent of the claims` (and 2 more, with the composites and the seams that call them).
- **F17. A power or competence whose gate failed.**
  Text: Art 103(3) "Der Instruktionsrichter oder die Instruktionsrichterin kann über die aufschiebende Wirkung von Amtes wegen oder auf Antrag einer Partei eine andere Anordnung treffen." / Art 104 "Der Instruktionsrichter oder die Instruktionsrichterin kann von Amtes wegen oder auf Antrag einer Partei vorsorgliche Massnahmen treffen, um den bestehenden Zustand zu erhalten oder bedrohte Interessen einstweilen sicherzustellen."
  Readings: (i) NOTHING, never "may not" (ruling of 2026-11-12, limb 1); (ii) JUST FALSE.
  Taken: (i).
  Rows: Art 103(3), Art 104, Art 105(2), Art 108(1), Art 108(1)(a), Art 108(1)(b), Art 108(1)(c), Art 108(2) and 7 more.
  Rule: `Art 109(2) the division decides in a bench of three`, `Art 104 the instructing judge may order a provisional measure`, `Art 109(1) the division decides in a bench of three on non-entry`, `Art 105(2) the Court may correct or supplement the finding of the facts`, `Art 112(3) the Court may remit the decision for improvement or quash it` (and 15 more, with the composites and the seams that call them).
- **F18. Art 105: bound by the facts.**
  Text: Art 105(2) "Es kann die Sachverhaltsfeststellung der Vorinstanz von Amtes wegen berichtigen oder ergänzen, wenn sie offensichtlich unrichtig ist oder auf einer Rechtsverletzung im Sinne von Artikel 95 beruht." / Art 105(3) "Richtet sich die Beschwerde gegen einen Entscheid über die Zusprechung oder Verweigerung von Geldleistungen der Militär- oder Unfallversicherung, so ist das Bundesgericht nicht an die Sachverhaltsfeststellung der Vorinstanz gebunden.[^11]"
  Readings: (i) paragraph 3 gives JUST FALSE for military and accident insurance; where only paragraph 2's power ("kann") is engaged the answer is NOTHING; paragraph 1 gives JUST TRUE for facts the lower instance found; (ii) JUST FALSE whenever paragraph 2 applies.
  Taken: (i).
  Rows: Art 105(1), Art 105(2), Art 105(3).
  Rule: `Art 105(3) the Court is bound by the finding of the facts`, `Art 105(2) the Court may correct or supplement the finding of the facts`, `Art 105(1) the Court bases its judgment on the facts found by the lower instance` (and 2 more, with the composites and the seams that call them).
- **F19. Art 106: fundamental rights and cantonal law under paragraph 1.**
  Text: Art 106(1) "Das Bundesgericht wendet das Recht von Amtes wegen an." / Art 106(2) "Es prüft die Verletzung von Grundrechten und von kantonalem und interkantonalem Recht nur insofern, als eine solche Rüge in der Beschwerde vorgebracht und begründet worden ist."
  Readings: (i) paragraph 1 answers NOTHING for fundamental rights, cantonal law and intercantonal law (paragraph 2 limits it for them, but paragraph 1's sentence does not say no); paragraph 2 gives JUST TRUE or JUST FALSE for them; (ii) paragraph 1 answers JUST FALSE for them.
  Taken: (i).
  Rows: Art 106(1), Art 106(2).
  Rule: `Art 106(2) the Court examines the violation`, `Art 106(1) the Court applies the rule of its own motion` (and 2 more, with the composites and the seams that call them).
- **F20. Art 107(3): no exchange of submissions.**
  Text: Art 107(3) first sentence "Erachtet das Bundesgericht eine Beschwerde auf dem Gebiet der internationalen Rechtshilfe in Strafsachen oder der internationalen Amtshilfe in Steuersachen als unzulässig, so fällt es den Nichteintretensentscheid innert 15 Tagen seit Abschluss eines allfälligen Schriftenwechsels."
  Readings: (i) the 15 days run "seit Abschluss eines allfälligen Schriftenwechsels"; where there was none the text gives no start and the answer is NOTHING; (ii) the 15 days run from the filing of the appeal.
  Taken: (i).
  Rows: Art 107(3) first sentence.
  Rule: `Art 107(3) the Court's duty to give the decision not to enter within 15 days`, `Art 107(3) the last day for the decision not to enter`, `Art 107(3) the decision not to enter is given within 15 days`.
- **F21. Art 107(4): one month.**
  Text: Art 107(4) "Über Beschwerden gegen Entscheide des Bundespatentgerichts über die Erteilung einer Lizenz nach Artikel 40d des Patentgesetzes vom 25. Juni 1954[^13] entscheidet das Bundesgericht innerhalb eines Monats nach Anhebung der Beschwerde.[^14]"
  Readings: (i) the last day is the same day of the next month; where that month has no such day the text states no rule and the answer is NOTHING; (ii) the last day of that month.
  Taken: (i).
  Rows: Art 107(4).
  Rule: `Art 107(4) the Court's duty to decide within one month`, `Art 107(4) the Court decides within one month`, `Art 107(4) the last day for the Court's decision on the licence appeal`.
- **F22. Art 109(1): "oder" between the two negations.**
  Text: Art 109(1) first sentence "Die Abteilungen entscheiden in Dreierbesetzung über Nichteintreten auf Beschwerden, bei denen sich keine Rechtsfrage von grundsätzlicher Bedeutung stellt oder kein besonders bedeutender Fall vorliegt, wenn die Beschwerde nur unter einer dieser Bedingungen zulässig ist (Art. 74 und 83–85)."
  Readings: (i) the bench of three decides on non-entry where neither a legal question of fundamental importance arises nor is the case particularly important, whichever of the conditions the appeal depends on; (ii) where either is absent.
  Taken: (i).
  Rows: Art 109(1) first sentence.
  Rule: `Art 109(1) the division decides in a bench of three on non-entry`, `Art 109(1) the condition on which the appeal is admissible, by chapters 3`, `Art 109(1) with chapter 3 the division decides in a bench of three on non-entry`.
- **F23. Art 112(1): a requirement not met.**
  Text: Art 112(1) "Entscheide, die der Beschwerde an das Bundesgericht unterliegen, sind den Parteien schriftlich zu eröffnen. Sie müssen enthalten:"
  Readings: (i) a decision short of a requirement of paragraph 1 is JUST FALSE ("der den Anforderungen von Absatz 1 nicht genügt", paragraph 3); (ii) NOTHING (a bare duty not done).
  Taken: (i).
  Rows: Art 112(1), Art 112(1)(a), Art 112(1)(b), Art 112(1)(c), Art 112(1)(d).
  Rule: `Art 112(1) the cantonal authority's duty to notify the decision to the parties in writing`, `Art 112(1)(c) the decision contains the operative part`, `Art 112(1) the decision is notified to the parties in writing`, `Art 112(1) the decision meets the requirements of paragraph 1`, `Art 112(1)(d) chapter 3 provides a value limit for the appeal` (and 4 more, with the composites and the seams that call them).
- **F24. Art 112(2) first sentence: "Sofern es das Bundesrecht oder das kantonale Recht vorsieht".**
  Text: Art 112(2) first sentence "Sofern es das Bundesrecht oder das kantonale Recht vorsieht, eröffnet die Behörde ihren Entscheid in der Regel zeitnah und ohne Begründung.[^16]"
  Readings: (i) a gate of the kind "sofern" on a power, failed: NOTHING (ruling of 2026-11-12, limb 1); listed for the maintainer or a lawyer because the ruling's limb 3 names "where"-type gates; (ii) JUST FALSE (ruling (b) of the periods ruling).
  Taken: (i).
  Rows: Art 112(2) first sentence.
  Rule: `Art 112(2) the authority may notify the decision promptly and without reasons`.
- **F25. Art 112(2) third sentence: the bar.**
  Text: Art 112(2) third sentence "Der Entscheid ist nicht vollstreckbar, solange nicht entweder diese Frist unbenützt abgelaufen oder die vollständige Ausfertigung eröffnet worden ist."
  Readings: (i) encoded as "the bar on enforcement still applies" (JUST TRUE while it does, JUST FALSE once lifted); JUST FALSE does not say the decision may be enforced; no regulative rule, because the text names no bearer (ruling N2, "until" bars of 2026-11-05); (ii) a function "the decision can be enforced".
  Taken: (i).
  Rows: Art 112(2) third sentence.
  Rule: `Art 112(2) the bar on enforcing the decision still applies`.
- **F26. Art 109(1) and chapter 3: which conditions are derived.**
  Text: Art 109(1) first sentence "Die Abteilungen entscheiden in Dreierbesetzung über Nichteintreten auf Beschwerden, bei denen sich keine Rechtsfrage von grundsätzlicher Bedeutung stellt oder kein besonders bedeutender Fall vorliegt, wenn die Beschwerde nur unter einer dieser Bedingungen zulässig ist (Art. 74 und 83–85)."
  Readings: (i) the seam derives the condition from chapter 3's Art 74(1) and (2), Art 84(1), Art 84a and Art 85(1), (2); the conditions that chapter 3's Art 83 states in (f)(1), (m), (w), (x), (z) and (zbis) are not derived and the seat question has no input for them, so for an appeal that turns on one of them the answer is NOTHING; (ii) derive all of them.
  Taken: (i).
  Rows: Art 109(1) first sentence.
  Rule: `Art 109(1) the division decides in a bench of three on non-entry`, `Art 109(1) the condition on which the appeal is admissible, by chapters 3`, `Art 109(1) with chapter 3 the division decides in a bench of three on non-entry`.
- **F27. The cantons' and the Court's bare duties.**
  Text: Art 111(3) first sentence "Die unmittelbare Vorinstanz des Bundesgerichts muss mindestens die Rügen nach den Artikeln 95–98 prüfen können."
  Readings: (i) a duty on the cantons or the Court that was not done, or whose "soweit" gate failed, is NOTHING (the text states no consequence for the person); this is chapter 3's F5 read in chapter 4; (ii) JUST FALSE.
  Taken: (i).
  Rows: Art 102(1), Art 110, Art 111(1), Art 111(3) first sentence.
  Rule: `Art 102(1) the Court's duty to serve the appeal and set a time limit`, `Art 110 the cantons' duty to ensure the review by a judicial authority`, `Art 111(1) the cantons' duty to let a person entitled to appeal take part as a party`, `Art 111(3) the cantons' duty to let the immediate lower instance examine the complaints under Art 95 to 98`, `Art 111(1) the person is entitled to appeal, by chapter 3` (and 8 more, with the composites and the seams that call them).
- **F28. The record "may I appeal this decision at all, and by when?".**
  Text: the text of the sections does not say how their answers combine; ruling E1 (option C) applies.
  Readings: (i) one answer per section, no combined verdict (ruling E1, option C); (ii) a combined three-valued "all requirements met".
  Taken: (i).
  Rows: Art 90, Art 100(1), Art 100(7), Art 101.
  Rule: `Art 100(1) the appellant's duty to file the appeal within 30 days`, `Art 101 the appellant's duty to file the appeal against an enactment within 30 days`, `Art 100(1) the general period in days`, `Art 100(7) the appeal can be brought at any time`, `Art 101 the appeal against an enactment is in time` (and 15 more, with the composites and the seams that call them).
- **F29. Chapter 3 Art 77(2) names provisions of chapter 4.**
  Text: chapter 3, Art 77(2), line 54: "Die Artikel 48 Absatz 3, 90–98, 103 Absatz 2, 105 Absatz 2, 106 Absatz 1 sowie 107 Absatz 2, soweit dieser dem Bundesgericht erlaubt, in der Sache selbst zu entscheiden, sind in diesen Fällen nicht anwendbar.[^16]"
  Readings: (i) for an appeal against an arbitral award a named provision of chapter 4 is "nicht anwendbar", so a chapter 4 answer for that appeal is NOTHING (what governs it is outside the sources), never JUST FALSE; (ii) JUST FALSE ("the complaint is barred").
  Taken: (i).
  Rows: Art 90, Art 91 (intro), Art 91(a), Art 91(b), Art 92(1), Art 92(2), Art 93(1), Art 93(1)(a) and 24 more.
  Rule: `Art 92(2) the decision can be challenged later`, `Art 90 the appeal is admissible against the decision`, `Art 96 the complaint about foreign law can be raised`, `Art 106(1) the Court applies the rule of its own motion`, `Art 95(a) the violation of federal law can be complained of` (and 37 more, with the composites and the seams that call them).
- **F30. Art 112(1)(d) and the value limits of chapter 3.**
  Text: Art 112(1)(d) "eine Rechtsmittelbelehrung einschliesslich Angabe des Streitwerts, soweit dieses Gesetz eine Streitwertgrenze vorsieht."
  Readings: (i) whether the Act provides a value limit for the appeal is asked of chapter 3 (Art 74(1) and 85(1), called with a value of 0 francs); where chapter 3 does not settle it, the answer for the decision stands only if it is the same on both readings, otherwise NOTHING; (ii) take the limit as absent where chapter 3 gives none.
  Taken: (i).
  Rows: Art 112(1)(d).
  Rule: `Art 112(1)(d) chapter 3 provides a value limit for the appeal`, `Art 112(1)(d) the decision contains a notice of legal remedies including the value in dispute where this Act provides a value limit`, `Art 112(1)(d) with chapter 3 the decision contains a notice of legal remedies including the value in dispute where the Act provides a value limit` (and 3 more, with the composites and the seams that call them).
- **F31. Art 103(1) in the composite: "in der Regel".**
  Text: Art 103(1) "Die Beschwerde hat in der Regel keine aufschiebende Wirkung."
  Readings: (i) in `Art 103 the appeal has suspensive effect` the exceptions of paragraphs 2 and 3 are taken as the only exceptions, so with no order and no limb of paragraph 2 the composite answers JUST FALSE ("keine aufschiebende Wirkung"); `Art 103(1)` alone answers NOTHING where the person says another exception applies; (ii) the composite answers NOTHING unless the person says that no other exception applies.
  Taken: (i).
  Rows: Art 103(1).
  Rule: `Art 103(1) the appeal has suspensive effect` (and 1 more, with the composites and the seams that call them).
- **F32. Art 109(1) and Art 74: a civil appeal below the value limit.**
  Text: Art 109(1) first sentence "Die Abteilungen entscheiden in Dreierbesetzung über Nichteintreten auf Beschwerden, bei denen sich keine Rechtsfrage von grundsätzlicher Bedeutung stellt oder kein besonders bedeutender Fall vorliegt, wenn die Beschwerde nur unter einer dieser Bedingungen zulässig ist (Art. 74 und 83–85)."
  Readings: (i) for the appeal in civil matters (the kind of appeal is an input) in a pecuniary matter whose value is below the limit of Art 74(1) (30 000 francs, 15 000 in employment and tenancy law cases) the condition is "only if a legal question of fundamental importance arises", unless a ground of Art 74(2)(b) to (e) saves the appeal; where the limit is reached ("mindestens"), or Art 74 is not the rule that applies, the appeal depends on no such condition and the answer is NOTHING, as for Art 85 above its limit (the competence of the bench of three is a power whose gate failed, ruling of 2026-11-12, limb 1); (ii) JUST FALSE where the limit is reached.
  Taken: (i).
  Rows: Art 109(1) first sentence.
  Rule: `Art 109(1) the division decides in a bench of three on non-entry`, `Art 109(1) the condition on which the appeal is admissible, by chapters 3`, `Art 109(1) with chapter 3 the division decides in a bench of three on non-entry`.
- **F33. Art 107(1): a bar with no condition.**
  Text: Art 107(1) "Das Bundesgericht darf nicht über die Begehren der Parteien hinausgehen."
  Readings: (i) the standing question "may the Court go beyond the claims of the parties?" is JUST FALSE and asks for no fact: "darf nicht über die Begehren der Parteien hinausgehen" has no condition and no limit of its own (a flat negative, ruling N2); (ii) NOTHING where the decision the Court would give does not go beyond the claims, JUST FALSE only where it does.
  Taken: (i).
  Rows: Art 107(1).
  Rule: `Art 107(1) the Court is permitted to go beyond the claims of the parties`.
- **F34. Art 107(3) second sentence: the exception not made out.**
  Text: Art 107(3) second sentence "Auf dem Gebiet der internationalen Rechtshilfe in Strafsachen ist es nicht an diese Frist gebunden, wenn das Auslieferungsverfahren eine Person betrifft, gegen deren Asylgesuch noch kein rechtskräftiger Endentscheid vorliegt.[^12]"
  Readings: (i) in an extradition appeal the Court is held to the 15 days (JUST TRUE) except where the person has no final decision on an asylum application (JUST FALSE): the first sentence gives the 15 days as the rule for the field and the second sentence states one exception, introduced with "wenn", so where it is not made out the text's own words leave the Court bound (reading (a) of the rule of 2026-10-29); the answer presumes a decision not to enter, which the first sentence limits to an appeal the Court considers inadmissible; an appeal in tax assistance is not asked of this function (NOTHING); (ii) NOTHING where the exception is not made out (the sentence says when the Court is not bound and nothing else).
  Taken: (i).
  Rows: Art 107(3) second sentence.
  Rule: `Art 107(3) the Court is bound by the period of 15 days`, `Art 107(3) the decision not to enter is given within 15 days`.

## What the text turns out to say

Numbered findings; each ends "Asserted." where an assertion in a test file or the case file shows it, and says "Not asserted" with the reason where nothing can be.
The lines after a finding name the assertion (or trace) lines that show it; `mknotes` fails if a finding names a function no assertion names.

1. The chapter 3 modules define no appeal-kind type, although the brief expects one: chapter 3 says the kind of appeal by which module a rule sits in and by Boolean inputs.
   So `Kind of appeal` is defined once, in `bgg4-nouns`, and the rules that depend on the kind use it: Art 103(2) in `bgg4-procedure` and the seams for Art 110, Art 111(1) and Art 112(1)(d) in `bgg4-seams`.
   Not asserted: this is a fact about the files, which `mknotes` checks by listing every `DECLARE` in `bgg3-*.l4` (none is a kind of appeal).
2. Art 90 to 93 give four separate routes to an appeal against a decision: a decision that ends the proceedings (Art 90), a partial decision (Art 91), a preliminary or interlocutory decision on jurisdiction or recusal (Art 92(1)), and any other preliminary or interlocutory decision (Art 93).
   The text does not say that the routes are cumulative requirements of one yes, so each article answers alone.
   `Art 90 to 93 the appeal is admissible against the decision` gathers the four by hand, as guidance of ruling E1 option B and not as a feature of the language: any JUST TRUE gives JUST TRUE, Art 93(2) answers in place of Art 93(1) in its two fields, a JUST FALSE of Art 93(1) or Art 91 gives JUST FALSE, and otherwise the answer is NOTHING (fork F4).
   Asserted.
   Shown by: `bgg4-tests-appealable.l4` lines 13 to 133 (12).
3. Art 91(a) lets a decision that deals with only some of the claims be appealed only "wenn diese Begehren unabhängig von den anderen beurteilt werden können".
   Where that "wenn" fails the answer is JUST FALSE (reading (a), a failed "wenn", fork F1); a decision that ends the proceedings for only some of the joint litigants (Art 91(b)) needs no such condition.
   Asserted.
   Shown by: `bgg4-tests-appealable.l4` lines 20 to 36 (11).
4. Art 92(2), "Diese Entscheide können später nicht mehr angefochten werden", is a flat negative about the decisions of paragraph 1 (independently notified preliminary or interlocutory decisions on jurisdiction or recusal).
   For such a decision `Art 92(2) the decision can be challenged later` is JUST FALSE; for any other decision the sentence says nothing, so the answer is NOTHING.
   Asserted.
   Shown by: `bgg4-tests-appealable.l4` lines 41 to 51 (7).
5. Art 93(1) gives an appeal against any other independently notified preliminary or interlocutory decision on either of two "wenn" conditions: it can cause irreparable harm, or upholding the appeal would at once bring a final decision and spare a significant expenditure of time or cost for a lengthy evidentiary procedure.
   Where neither holds the answer is JUST FALSE (reading (a), fork F2); the second condition needs both of its halves.
   Asserted.
   Shown by: `bgg4-tests-appealable.l4` lines 56 to 74 (11).
6. Art 93(2) takes preliminary and interlocutory decisions in international legal assistance in criminal matters and in asylum out of Art 93(1): they are "nicht anfechtbar" (JUST FALSE), except that appeals against decisions on extradition detention and on the seizure of assets or valuables are reserved "sofern die Voraussetzungen von Absatz 1 erfüllt sind" (JUST TRUE when Art 93(1) holds).
   Outside those two fields the paragraph says nothing and the answer is NOTHING.
   Asserted.
   Shown by: `bgg4-tests-appealable.l4` lines 77 to 89 (7).
7. Art 93(3) says that a preliminary or interlocutory decision against which an appeal was not admissible, or against which none was brought, can be attacked by the appeal against the final decision "soweit sie sich auf dessen Inhalt auswirken".
   Where the antecedent fails the answer is JUST FALSE; where the decision does not affect the content of the final decision the answer is NOTHING, because the text grants only to the extent they do (fork F3).
   Asserted.
   Shown by: `bgg4-tests-appealable.l4` lines 91 to 98 (5).
8. Art 94 gives an appeal against the unlawful refusal or delay of "einen anfechtbaren Entscheid": the decision refused or delayed must itself be one that can be appealed, which the person states.
   Where all three facts hold the answer is JUST TRUE; where one does not the paragraph says no to no other case, so the answer is NOTHING.
   Asserted.
   Shown by: `bgg4-tests-appealable.l4` lines 103 to 109 (4).
9. Art 95 lists five sources of law whose violation can be complained of and does not close the list with "nur", so a source of law outside the five answers NOTHING, not JUST FALSE (fork F5).
   This is unlike Art 97(1) and Art 98, which are closed with "nur" and answer JUST FALSE.
   Asserted.
   Shown by: `bgg4-tests-grounds.l4` lines 11 to 28 (10).
10. Art 96(b) allows the complaint that foreign law was applied wrongly "sofern der Entscheid keine vermögensrechtliche Sache betrifft": in a pecuniary matter the complaint is JUST FALSE (a failed "sofern", reading (a), fork F6); Art 96(a) has no such limit.
   Asserted.
   Shown by: `bgg4-tests-grounds.l4` lines 33 to 43 (9).
11. Art 97(1) allows a complaint about the finding of the facts "nur" if it is obviously wrong or rests on a violation of law under Art 95, and if correcting the defect can be decisive for the outcome; otherwise JUST FALSE.
   Art 97(2) allows "jede unrichtige oder unvollständige Feststellung" in military and accident insurance money benefits and replaces paragraph 1 there (fork F7).
   Asserted.
   Shown by: `bgg4-tests-grounds.l4` lines 48 to 68 (14).
12. Art 98 limits the complaints against decisions on provisional measures to "nur die Verletzung verfassungsmässiger Rechte": any other complaint against such a decision is JUST FALSE; for a decision that is not on provisional measures the sentence says nothing.
   Asserted.
   Shown by: `bgg4-tests-grounds.l4` lines 73 to 77 (4).
13. Art 99 allows new facts and evidence "nur so weit" as the lower instance's decision first gave occasion, and says new claims are "unzulässig".
   "So weit" is read as a yes or no the person states (fork F8), and a claim that is not new is NOTHING under Art 99(2), because the flat negative reaches only new claims.
   Asserted.
   Shown by: `bgg4-tests-new-submissions.l4` lines 10 to 17 (6).
14. The time limit is 30 days (Art 100(1)), ten days for the four kinds of decision of Art 100(2)(a) to (d), five days for the two of Art 100(3)(a), (b), and three days for a decision of a cantonal government on a National Council election (Art 100(4)); Art 101 gives 30 days from the publication of an enactment.
   The text does not say how the days are counted; the day after the notification is taken as day 1 (fork F9), so with a notification on 1 March 2026 the last day of the general period is 31 March, filing on 31 March is in time and filing on 1 April is not.
   The day before the last day, the last day and the day after are asserted for each period: ten days (in time on 10 and 11 March, not on 12 March), five days (5 and 6 March, not 7 March), three days (3 and 4 March, not 5 March) and Art 101 (30 June and 1 July, not 2 July, from a publication on 1 June).
   Asserted.
   Shown by: `bgg4-tests-time-limit.l4` lines 54 to 140 (43).
15. A decision of a cantonal supervisory authority in bill-of-exchange enforcement is a decision of Art 100(2)(a) (ten days) and of Art 100(3)(a) (five days).
   The shorter, more specific period is taken as governing (fork F11): the composite gives five days, and the last day from 1 March is 6 March.
   Asserted.
   Shown by: `bgg4-tests-time-limit.l4` lines 41 to 60 (10).
16. Art 100(5) starts the period of an appeal in an intercantonal conflict of competence "spätestens dann" as a decision exists in both cantons against which an appeal lies.
   It is encoded as: the period starts on the notification day, but not later than the later of the two cantons' decision days (fork F12).
   Notified on 1 May with the two decisions on 10 and 20 April, the period starts from 20 April and the last day is 20 May; notified on 5 April, it starts from 5 April.
   Asserted.
   Shown by: `bgg4-tests-time-limit.l4` lines 65 to 71 (6).
17. Art 100(7), "jederzeit", has no period: for an unlawful refusal or delay of a decision the appeal can be brought at any time, and `Art 100 and 101 the time limit for filing` returns `the appeal can be brought at any time` and not a date.
   A filing on 1 January 2030 against a refusal is in time.
   Asserted.
   Shown by: `bgg4-tests-time-limit.l4` lines 127 to 154 (11).
18. The rules on suspension and restoration of time limits are outside the sources (the brief places them in chapter 2), so the days a rule outside the text leaves out of the count are an input and the last day moves by them (fork F10): with 16 days left out the last day from 1 March is 16 April.
   A filing before the notification gives NOTHING, because the period has not started.
   Asserted.
   Shown by: `bgg4-tests-time-limit.l4` lines 77 to 122 (28).
19. Art 100(6) is shown repealed in this text ("6 …", footnote 9, repealed by the Civil Procedure Code with effect from 1 January 2011), and so is the second sentence of Art 111(3) ("…", footnote 15).
   Each is a labelled stub that calls nothing and is called by nothing, and each has a coverage row `repealed or blank in this text`.
   Not asserted: there is nothing to assert about a repealed paragraph.
20. The text states a time limit and no consequence of missing it, for the appellant (Art 100, 101), the lower instance (Art 102(2)), the Court (Art 107(3), (4)) and the parties (Art 112(2)).
   Each duty is also a regulative rule with `LEST BREACH`, which here means only that the period was missed (fork F13), and each is run with a `#TRACE` on the last day (FULFILLED) and the day after it (BREACHED); Art 107(4) takes the length of the month in days and is traced for a month of 31 days; the permission of Art 112(2) is described under finding 33.
   Traces are printed, not asserted (see "What the stable binary does not accept").
   Shown by: `bgg4-tests-procedure.l4` lines 177 to 189 (6); `bgg4-tests-time-limit.l4` lines 159 to 185 (11).
21. Art 102(3), "in der Regel" no further exchange of submissions, answers JUST FALSE where the person says there is no exception and NOTHING where the person says there is one, because the text names no exception (fork F14).
   Art 102(1) (the Court serves the appeal "soweit erforderlich") and Art 102(2) (the lower instance sends the files within the Court's time limit) are duties of officials; Art 102(1) is NOTHING where the gate fails (fork F27).
   Asserted.
   Shown by: `bgg4-tests-procedure.l4` lines 12 to 21 (8).
22. Art 103(1) says the appeal "in der Regel" has no suspensive effect, and Art 103(2) gives it suspensive effect "im Umfang der Begehren" in four cases: a civil appeal against a judgment that creates, changes or ends a legal relationship (Gestaltungsurteil), a criminal appeal against an unconditional custodial sentence or a measure depriving of liberty (not extending to the decision on civil claims), international legal assistance in criminal matters against a final order or one that allows information or objects or assets to be handed over, and international administrative assistance in tax matters.
   Each limb answers JUST FALSE where its own "wenn" fails (reading (a), fork F15) and NOTHING outside the matter it names.
   Art 103(3) lets the instructing judge order otherwise, and the composite `Art 103 the appeal has suspensive effect` takes what the judge ordered as an input; with no order and no limb of paragraph 2 holding, the composite answers JUST FALSE from paragraph 1, taking the exceptions of paragraphs 2 and 3 as the only ones (fork F31); a power whose gate fails is NOTHING (fork F17).
   Asserted.
   Shown by: `bgg4-tests-procedure.l4` lines 26 to 70 (30).
23. Art 104 lets the instructing judge order provisional measures "um den bestehenden Zustand zu erhalten oder bedrohte Interessen einstweilen sicherzustellen"; a power whose gate fails answers NOTHING (fork F17).
   Asserted.
   Shown by: `bgg4-tests-procedure.l4` lines 75 to 77 (3).
24. Art 105 has three paragraphs on the facts: the Court bases its judgment on the facts the lower instance found (105(1)); it may correct or supplement them of its own motion if they are obviously wrong or rest on a violation of law under Art 95 (105(2), a power, NOTHING where its gate fails); and it is not bound by them in military and accident insurance money benefits (105(3), JUST FALSE for "bound").
   The composite answers JUST FALSE where paragraph 3 applies, NOTHING while the gate of paragraph 2's power holds, and otherwise JUST TRUE where the lower instance found the facts (fork F18).
   Asserted.
   Shown by: `bgg4-tests-procedure.l4` lines 82 to 95 (11).
25. Art 106(2) lets the Court examine the violation of fundamental rights and of cantonal and intercantonal law "nur insofern" as a complaint was raised and reasoned: without one it is JUST FALSE.
   Art 106(1), "Das Bundesgericht wendet das Recht von Amtes wegen an", is JUST TRUE for other law and NOTHING for those three kinds of rule, because paragraph 2 limits them and paragraph 1 does not say no to them (fork F19).
   Asserted.
   Shown by: `bgg4-tests-procedure.l4` lines 100 to 113 (12).
26. Art 107(1), "darf nicht über die Begehren der Parteien hinausgehen", is a flat negative with no condition of its own, so the question whether the Court may go beyond the claims is JUST FALSE and asks for no fact (fork F33).
   Art 107(2) names three outcomes of an upheld appeal (the Court decides the matter itself, remits to the lower instance, or remits to the first instance) and does not close the list, so another outcome is NOTHING (fork F5).
   Asserted.
   Shown by: `bgg4-tests-procedure.l4` lines 118 to 124 (6).
27. Art 107(3) gives the Court 15 days "seit Abschluss eines allfälligen Schriftenwechsels" to give a decision not to enter in international legal assistance in criminal matters and administrative assistance in tax matters, and frees it from that period in extradition proceedings where the person has no final decision on an asylum application; in an extradition appeal where the exception is not made out the Court is held to the 15 days (fork F34).
   From the close of the exchange on 10 March 2026 the last day is 25 March; a decision on 25 March is in time and one on 26 March is not; with no exchange the answer is NOTHING (fork F20).
   Art 107(4) gives one month from the appeal being brought to decide an appeal against a Federal Patent Court decision on a licence: from 15 March the last day is 15 April; where the month has no such day (31 January) the answer is NOTHING (fork F21).
   Asserted.
   Shown by: `bgg4-tests-procedure.l4` lines 126 to 169 (27).
28. Art 108(1) lets the president of the division decide alone in the simplified procedure on non-entry for three kinds of appeal (obviously inadmissible, obviously without sufficient reasoning under Art 42(2), querulous or abusive); Art 108(2) lets the president entrust another judge; Art 108(3) confines the reasons to a short statement of the ground.
   A power whose gate fails answers NOTHING (fork F17).
   Asserted.
   Shown by: `bgg4-tests-simplified.l4` lines 10 to 29 (15).
29. Art 109(1) has a bench of three decide on non-entry where no legal question of fundamental importance arises or the case is not particularly important, "wenn die Beschwerde nur unter einer dieser Bedingungen zulässig ist (Art. 74 und 83–85)"; the "oder" between the two negations is read as neither condition being present (fork F22).
   The text itself points to chapter 3 here, and `bgg4-seams` derives which condition the appeal depends on from chapter 3's Art 74(1) and (2), Art 84(1), 84a and 85(1), (2), and not from the conditions of Art 83 (forks F26 and F32).
   Art 109(1) second sentence says "Artikel 58 Absatz 1 Buchstabe b findet keine Anwendung": where the first sentence's case holds, `Art 109(1) Art 58(1)(b) is applicable to the decision` is JUST FALSE (a flat negative), and what Art 58(1)(b) provides is outside the sources.
   Art 109(2) and (3) give the bench of three, by unanimity, the decision on an obviously unfounded or obviously well-founded appeal, with summary reasons that may refer to the challenged decision.
   Asserted.
   Shown by: `bgg4-tests-seams.l4` lines 105 to 161 (40); `bgg4-tests-simplified.l4` lines 34 to 66 (28).
30. Art 110 makes the cantons ensure free review of the facts and application of the law of its own motion "Soweit die Kantone nach diesem Gesetz als letzte kantonale Instanz ein Gericht einzusetzen haben".
   Chapter 3 says where they must: Art 75(2) (civil), Art 80(2) (criminal) and Art 86(2) (public law, except where Art 86(3) lets a canton use another authority for a decision of predominantly political character, which is NOTHING here).
   A duty not done answers NOTHING (fork F27); the same duty is also a regulative rule, run with a `#TRACE`.
   Asserted.
   Shown by: `bgg4-tests-cantonal.l4` lines 12 to 15 (4); `bgg4-tests-seams.l4` lines 61 to 71 (10).
31. Art 111(1) lets "wer zur Beschwerde an das Bundesgericht berechtigt ist" take part as a party before all cantonal lower instances.
   Chapter 3 says who is entitled (Art 76(1), 81(1), 89(1)); only a JUST TRUE from chapter 3 counts as entitled, and a chapter 3 NOTHING is never turned into a no (a kind of appeal other than civil, criminal and public-law gives NOTHING).
   Art 111(2) (a federal authority's power to use the cantonal remedies) and Art 111(3) (the immediate lower instance must be able to examine at least the complaints of Art 95 to 98) are encoded for what they decide; the second sentence of Art 111(3) is repealed.
   Asserted.
   Shown by: `bgg4-tests-cantonal.l4` lines 20 to 31 (10); `bgg4-tests-seams.l4` lines 45 to 56 (8).
32. Art 112(1) requires a decision that can be appealed to be notified to the parties in writing with four contents: the claims, reasoning, evidence and declarations of the parties so far as they do not appear in the files; the governing reasons of fact and law; the operative part; and a notice of legal remedies including the value in dispute "soweit dieses Gesetz eine Streitwertgrenze vorsieht".
   A decision short of a requirement is JUST FALSE (paragraph 3 calls it one "der den Anforderungen von Absatz 1 nicht genügt", fork F23).
   Whether the Act provides a value limit is asked of chapter 3's Art 74(1) and Art 85(1), called with a value of 0 francs, and where chapter 3 does not settle it the answer stands only if it is the same read both ways (fork F30).
   Asserted.
   Shown by: `bgg4-tests-cantonal.l4` lines 36 to 67 (27); `bgg4-tests-seams.l4` lines 76 to 95 (15).
33. Art 112(2) lets an authority notify "in der Regel zeitnah und ohne Begründung" where federal or cantonal law so provides, gives the parties 30 days to demand the complete version, and bars enforcement until the 30 days lapse unused or the complete version is notified.
   From a notification on 1 March 2026 the last day to demand is 31 March: a demand on 31 March is in time and one on 1 April is not.
   The bar is encoded as "the bar on enforcing the decision still applies" (JUST TRUE until it is lifted, JUST FALSE once it is); JUST FALSE does not say the decision may be enforced (fork F25).
   Asserted for the decision functions; the regulative rule for the demand is run with `#TRACE` at day 30 and day 31 and both print FULFILLED, because a MAY's window is not enforced on the stable binary (see "What the stable binary does not accept").
   Shown by: `bgg4-tests-cantonal.l4` lines 69 to 99 (21).
34. Art 112(3) lets the Court remit a decision that falls short of paragraph 1 to the cantonal authority for improvement, or quash it (a power; NOTHING where its gate fails, fork F17).
   Art 112(4) has the cantonal authorities notify federal authorities entitled to appeal of the decisions the Federal Council determines; the Federal Council's determination is an input.
   Asserted.
   Shown by: `bgg4-tests-cantonal.l4` lines 101 to 106 (5).
35. Chapter 3's Art 77(2) says that Art 48(3), Art 90 to 98, Art 103(2), Art 105(2), Art 106(1) and, so far as it lets the Court decide the matter itself, Art 107(2), "sind in diesen Fällen nicht anwendbar" (the appeals against arbitral awards of Art 77(1)).
   For such an appeal the chapter 4 answers of those provisions are NOTHING, never JUST FALSE: "does not apply" is not "the complaint is barred", and what governs instead is outside the sources (fork F29).
   Art 99 is not named in Art 77(2), so it stays applicable.
   Art 48(3) is outside the sources and has no chapter 4 function.
   Asserted, and every seat question that Art 77(2) reaches takes the extra input "is your appeal against an arbitral award".
   Shown by: `bgg4-tests-seams.l4` lines 15 to 39 (13).
36. The value in dispute ("Streitwert") appears in the chapter 4 text once, in Art 112(1)(d) as a content of the notice of remedies (line 146 of the text file); the chapter 4 text has no rule for working it out.
   Chapter 3's notes say that how the value is worked out "is in chapter 4"; the text of chapter 4 does not hold it, so chapter 4 does not supply it, the value stays a number the person states in chapter 3's Art 74(1) and Art 85(1), and the brief places the rules on the value in dispute in chapter 2, which is outside the sources and was not checked.
   Not asserted: this is a fact about the text, which `mknotes` checks by counting the lines of the file that contain "Streitwert".
37. The chapter 3 functions have no time input and none of them calls a chapter 4 function (chapter 3 is read-only, and `mknotes` checks that no `bgg3-*.l4` file mentions `bgg4`).
   A person who asks "may I appeal this decision at all, and by when?" gets the combination from the three record functions in `bgg4-seams`, one per kind of appeal, which return one answer per section and no combined verdict (E1 option C, fork F28).
   Asserted.
   Shown by: `bgg4-tests-seams.l4` lines 166 to 214 (36).
38. A cantonal enactment (Art 101) is not an "Entscheid" of Art 90 to 93, so `Art 90 to 94 the act can be appealed` is NOTHING for an enactment and the record's time limit for it is the 30 days from publication.
   Asserted.
   Shown by: `bgg4-tests-seams.l4` lines 166 to 169 (4); `bgg4-tests-time-limit.l4` lines 133 to 134 (2).

## What the text does not answer

Asked as inputs, and a question that needs the missing rule is answered `NOTHING`; none is taken from memory.

- The rules on how time limits run, are suspended and are restored (chapter 2): the days left out of the count are an input; the text of chapter 4 does not mention Saturdays, Sundays or holidays, and says nothing on whether the day of notification counts.
- The value in dispute: chapter 4 does not work it out.
- The conditions of chapter 3's Art 83 (f)(1), (m), (w), (x), (z) and (zbis), which Art 109(1) also names ("Art. 74 und 83–85"): they are not derived and the seat question has no input for them, so an appeal that turns on one of them is answered NOTHING (fork F26).
- The value limit of chapter 3 (Art 74(1), Art 85(1)) in the three records of "may I appeal this decision at all, and by when?": a record has five fields (chapter 3 says the appeal lies against the decision, chapter 3 says I am entitled to appeal, chapter 4 says the act can be appealed, chapter 4 says the appeal is in time, chapter 4 says the time limit) and none for the value limit, which belongs to chapter 3's own row.
- What follows if a period is missed: the text states none (fork F13); chapter 4 does not say that an appeal filed late is inadmissible, only the period.
- What a missed period of the Court or the lower instance (Art 102(2), 107(3), 107(4)) means for the person.
- What governs an appeal against an arbitral award where Art 77(2) makes a provision inapplicable.
- What "in der Regel" leaves open in Art 102(3), 103(1) and 112(2): no exception is named.
- Which federal and cantonal laws let a decision be notified promptly and without reasons (Art 112(2)), and which decisions the Federal Council has determined federal authorities are to be notified of (Art 112(4)).
- Whether a cantonal enactment can be challenged by an appeal in the form of Art 90 to 93: those articles speak of "Entscheide" only, so Art 101 is the only provision of chapter 4 that speaks of an enactment.
- The text file is a script-made rendering and not the official text.

## What the stable binary does not accept

Observed on 1.6.110 and 1.6.109 during this encoding, and sorted by how the failure shows: loud (an error the reader sees) first, then silent (a wrong answer with exit code 0), which is where the words are spent.

Loud:

- A regulative rule (`PARTY ... MUST ...`) cannot be compared in an `#ASSERT`: `` #ASSERT `the duty` EQUALS `the duty` `` gives `eval/unsupported-equality` ("assertion could not be evaluated"), observed on 1.6.110 with `` `Art 100(1) the appellant's duty to file the appeal within 30 days` ``.
  So each duty and permission is run with `#TRACE` and the same condition is encoded as a decision function that is asserted; the traces are printed in "What check.sh prints" and are not asserted.
- `#ASSERT REFUSED e` where `e` produces a value fails with `eval/assertion-failed`, "expected a refusal, but the expression produced a value"; no construct that produces a refusal exists on the stable binary, so this encoding uses none.
- A genitive as a function argument, `` `f` r's g ``, is a type error on 1.6.110 (`check/not-a-function`, "which is not a function", and `check/type-mismatch`); it has to be written `` `f` (r's g) ``.
  Chapter 3's notes give a different code (`parse/unexpected-genitive`) for what looks like the same mistake; this encoding observed the code above and did not run chapter 3's file.

Silent:

- **`NOT a OR b` parses as `NOT (a OR b)`, and `NOT a AND b` as `NOT (a AND b)`**, on both 1.6.110 and 1.6.109, with no diagnostic: probed with `a` and `b` both TRUE (`NOT a OR b` gave FALSE, `(NOT a) OR b` gave TRUE) and both FALSE (`NOT a AND b` gave TRUE).
  It surfaced here as two failing cantonal assertions for Art 111(1) and was fixed to `(NOT x) OR y`; every `NOT` in the modules is now parenthesised, and no other template contained the pattern.
- **A `MAY ... WITHIN n` is accepted but its window is not enforced in a trace**: the parties' permission to demand the complete version within 30 days (Art 112(2)) prints FULFILLED for a demand at day 30 and also at day 31.
  The decision functions carry the window (`Art 112(2) the demand for the complete version is in time` is JUST TRUE on day 30 and JUST FALSE on day 31); the trace does not.
- **`check.sh` compares counts and not `#TRACE` outcomes**, so a difference in what a trace prints between the two builds does not turn it red.
  The 24 trace outcomes of the test files were compared by hand between 1.6.110 and 1.6.109 (`traces.sh` in this folder diffs every Evaluation block) and are identical in every test file and in the case file.
- A trace of a `MUST ... WITHIN n` with no event prints the residual obligation, not a verdict (`PARTY Appellant MUST ... WITHIN 30 HENCE FULFILLED LEST BREACH BY ...`), which reads like a result and is not one.
- The brief lists further constructs the stable binary rejects (`REFUSE`, `BECAUSE` outside `LEST BREACH`, a `YMD` of one's own); this encoding uses none of them.

## What the traces don't tell you

**The silent one: the trace of the Art 112(2) permission reads FULFILLED for a late demand.**
`bgg4-tests-cantonal.l4` runs `` `Art 112(2) the parties' permission to demand the complete version within 30 days` `` as a `#TRACE` with the demand at day 30 and again at day 31, and both print `FULFILLED` (observed on 1.6.110 and 1.6.109).
A reader who reads only the trace would take day 31 as an in-time demand.
It is not one: the text gives the parties 30 days ("innert 30 Tagen"), and the encoding says so in the plain assertions, not in the trace.
The trace is not the evidence for the window.
Those assertions are in `bgg4-tests-cantonal.l4`, lines 72 to 81: `Art 112(2) the last day to demand the complete version` (day 30 after the notification, plus the days a period does not run, which are an input) and `Art 112(2) the demand for the complete version is in time`, which is `JUST TRUE` for a demand on the last day, `JUST FALSE` the day after, and `NOTHING` where there was no decision without reasons or the demand predates the notification.
It is the only regulative `MAY` in the chapter 4 modules (a search of `bgg4-*.l4` for a `MAY` that is not in a comment finds `bgg4-cantonal.l4` line 246 and no other).
This section states what was observed.
It does not say why the permission's window is not enforced in a trace; that is not established here.

**What the other traces do show.**
The periods that are duties (Art 100 to 101, Art 102(2), Art 107(3) and (4)) do breach on the day after their last day, and are fulfilled on the last day, in the traces printed under "What check.sh prints".
A `MUST ... WITHIN n` with no event prints the residual obligation, not a verdict (see "What the stable binary does not accept").
**`check.sh` does not read traces at all**: it counts assertions, so a trace that changes between builds or between edits does not turn it red.
The 24 trace outcomes were compared by hand between 1.6.110 and 1.6.109 and are identical.

## Marginal readings for a lawyer

Every branch below rests on a reading the 2026-10-29 rule marks for a lawyer.
Reading (a): a failed "if" counts as the text's no, within the provision that holds it, and flat negatives count as the text saying no (ruled as N2 option A, so the flat negatives are listed for completeness).
Reading (b): a bar or grant limited by its own wording does not give a no when the case falls outside the limit; that is the reading every `NOTHING-kind (limited by its own wording)` branch rests on, and the modules carry 85 of them (`grep -o "NOTHING-kind (limited by its own wording)" bgg4-*.l4` over the layer-1 modules counts them).

Branches resting on reading (a), a failed "if" answered `JUST FALSE` (the other reading answers `NOTHING`):

- `bgg4-appealable.l4:41`, `Art 91(a) the appeal is admissible against the decision that deals with only some of the claims`
- `bgg4-appealable.l4:67`, `Art 91 the appeal is admissible against the partial decision`
- `bgg4-appealable.l4:104`, `Art 93(1)(a) the appeal is admissible because the decision may cause irreparable harm`
- `bgg4-appealable.l4:115`, `Art 93(1)(b) the appeal is admissible because allowing it would immediately bring about a final decision`
- `bgg4-appealable.l4:134`, `Art 93(1) the appeal is admissible against the other preliminary or interlocutory decision`
- `bgg4-appealable.l4:168`, `Art 93(3) the preliminary or interlocutory decision can be challenged by the appeal against the final decision`
- `bgg4-appealable.l4:226`, `Art 90 to 93 the appeal is admissible against the decision`
- `bgg4-grounds.l4:105`, `Art 96(b) the complaint that foreign law was applied wrongly can be raised`
- `bgg4-procedure.l4:86`, `Art 103(2)(a) the appeal has suspensive effect in civil matters`
- `bgg4-procedure.l4:100`, `Art 103(2)(b) the appeal has suspensive effect in criminal matters`
- `bgg4-procedure.l4:113`, `Art 103(2)(c) the appeal has suspensive effect in international legal assistance in criminal matters`
- `bgg4-procedure.l4:150`, `Art 103(2) the appeal has suspensive effect to the extent of the claims`
- `bgg4-procedure.l4:190`, `Art 103 the appeal has suspensive effect`

Branches resting on a flat negative counted as the text's no (ruling N2 option A; the other reading answers `NOTHING`):

- `bgg4-appealable.l4:91`, `Art 92(2) the decision can be challenged later`
- `bgg4-appealable.l4:156`, `Art 93(2) the appeal is admissible against the preliminary or interlocutory decision in the field`
- `bgg4-appealable.l4:224`, `Art 90 to 93 the appeal is admissible against the decision`
- `bgg4-grounds.l4:118`, `Art 96 the complaint about foreign law can be raised`
- `bgg4-new-submissions.l4:29`, `Art 99(2) the new claim is admissible`
- `bgg4-procedure.l4:63`, `Art 102(3) a further exchange of submissions takes place`
- `bgg4-procedure.l4:74`, `Art 103(1) the appeal has suspensive effect`
- `bgg4-procedure.l4:98`, `Art 103(2)(b) the appeal has suspensive effect in criminal matters`
- `bgg4-procedure.l4:186`, `Art 103 the appeal has suspensive effect`
- `bgg4-procedure.l4:232`, `Art 105(3) the Court is bound by the finding of the facts`
- `bgg4-procedure.l4:246`, `Art 105 the Court is bound by the facts found by the lower instance`
- `bgg4-procedure.l4:272`, `Art 106(2) the Court examines the violation`
- `bgg4-procedure.l4:294`, `Art 107(1) the Court is permitted to go beyond the claims of the parties`
- `bgg4-procedure.l4:334`, `Art 107(3) the Court is bound by the period of 15 days`
- `bgg4-simplified.l4:110`, `Art 109(1) Art 58(1)(b) is applicable to the decision`

Branches that answer JUST FALSE for a bare "must" not done, where the text itself calls a decision short of the requirement one "der den Anforderungen von Absatz 1 nicht genügt" (decided case by case, fork F23; the other reading answers `NOTHING`):

- `bgg4-cantonal.l4:115`, `Art 112(1) the decision is notified to the parties in writing`
- `bgg4-cantonal.l4:128`, `Art 112(1)(a) the decision contains the claims, reasoning, evidence and procedural declarations of the parties`
- `bgg4-cantonal.l4:140`, `Art 112(1)(b) the decision contains the governing reasons of fact and law`
- `bgg4-cantonal.l4:152`, `Art 112(1)(c) the decision contains the operative part`
- `bgg4-cantonal.l4:166`, `Art 112(1)(d) the decision contains a notice of legal remedies including the value in dispute where this Act provides a value limit`
- `bgg4-cantonal.l4:193`, `Art 112(1) the decision meets the requirements of paragraph 1`

Branches whose no rests on a period the text fixes in its own words, or on an "until" bar (ruled 2026-11-05, periods ruling (a) and rule (d); listed so the ruling can be seen applied, not marginal):

- `bgg4-cantonal.l4:238`, `Art 112(2) the demand for the complete version is in time`
- `bgg4-cantonal.l4:265`, `Art 112(2) the bar on enforcing the decision still applies`
- `bgg4-cantonal.l4:266`, `Art 112(2) the bar on enforcing the decision still applies`
- `bgg4-procedure.l4:42`, `Art 102(2) the lower instance has sent the files within the time limit`
- `bgg4-procedure.l4:352`, `Art 107(3) the decision not to enter is given within 15 days`
- `bgg4-procedure.l4:388`, `Art 107(4) the Court decides within one month`
- `bgg4-time-limit.l4:274`, `Art 100(1) to (5) the appeal against a decision is in time`
- `bgg4-time-limit.l4:298`, `Art 101 the appeal against an enactment is in time`

Branches whose no is the text's own closing of the list with "nur" (not marginal):

- `bgg4-grounds.l4:133`, `Art 97(1) the complaint about the finding of the facts can be raised`
- `bgg4-grounds.l4:171`, `Art 98 the complaint can be raised against the decision on provisional measures`
- `bgg4-new-submissions.l4:21`, `Art 99(1) the new fact or new evidence may be put forward`

In all 45 FALSE-kind branches are listed (the modules carry 45 FALSE-kind comments); the line numbers are those of the deposited files.

## Rulings applied

Each ruling below is recorded word for word, copied by `mknotes` from the brief of this run, because this row carries the `NOTHING-kind` tags those rulings govern.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

- **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The ruling sets three limits:

Where each ruling shows in this row: E1 option C in the seams record and E1 option B by hand only in `Art 90 to 93 the appeal is admissible against the decision` (fork F4); N2 option A in the flat-negative branches above; the periods ruling in every period and in the days counted; the "until" bar in Art 112(2) third sentence (fork F25); the case-by-case ruling in forks F4, F5, F8, F9, F10, F11, F12, F13, F14, F16, F18, F19, F20, F21, F22, F26, F27, F30 and F31; the grant-or-power ruling in forks F17 and F24.

## What check.sh prints

Run as `L4=<l4 1.6.110> L4_MAIN=<l4 1.6.109> ./check.sh` in this folder, with the target `main`.
The two version lines:

```
l4 --version -> 1.6.110 (main, e51181d, 2026-11-11)
l4 --version (main build) -> 1.6.109 (main, 4c887e0, 2026-11-04)
```

There are no baseline numbers it replaced: this is a new encoding, and the six `bgg3-*` modules count 0 assertions each, as before.
The comparison with the second stable build is of counts; traces were compared by hand (above).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
bgg3-civil.l4                                  0         0       0        0         0 |      0         0       0        0  same
bgg3-criminal.l4                               0         0       0        0         0 |      0         0       0        0  same
bgg3-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
bgg3-public-courts.l4                          0         0       0        0         0 |      0         0       0        0  same
bgg3-public-limits.l4                          0         0       0        0         0 |      0         0       0        0  same
bgg3-public-scope.l4                           0         0       0        0         0 |      0         0       0        0  same
bgg4-appealable.l4                             0         0       0        0         0 |      0         0       0        0  same
bgg4-cantonal.l4                               0         0       0        0         0 |      0         0       0        0  same
bgg4-cases-seat.l4                             0       180       0        0         0 |      0       180       0        0  same
bgg4-grounds.l4                                0         0       0        0         0 |      0         0       0        0  same
bgg4-new-submissions.l4                        0         0       0        0         0 |      0         0       0        0  same
bgg4-nouns.l4                                  0         0       0        0         0 |      0         0       0        0  same
bgg4-procedure.l4                              0         0       0        0         0 |      0         0       0        0  same
bgg4-seams.l4                                  0         0       0        0         0 |      0         0       0        0  same
bgg4-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
bgg4-simplified.l4                             0         0       0        0         0 |      0         0       0        0  same
bgg4-tests-appealable.l4                       0        57       0        0         0 |      0        57       0        0  same
bgg4-tests-cantonal.l4                         0        67       0        0         0 |      0        67       0        0  same
bgg4-tests-grounds.l4                          0        43       0        0         0 |      0        43       0        0  same
bgg4-tests-new-submissions.l4                  0         6       0        0         0 |      0         6       0        0  same
bgg4-tests-procedure.l4                        0        97       0        0         0 |      0        97       0        0  same
bgg4-tests-seams.l4                            0       122       0        0         0 |      0       122       0        0  same
bgg4-tests-simplified.l4                       0        43       0        0         0 |      0        43       0        0  same
bgg4-tests-time-limit.l4                       0        86       0        0         0 |      0        86       0        0  same
bgg4-time-limit.l4                             0         0       0        0         0 |      0         0       0        0  same
TOTAL (25 modules)                             0       701       0        0           |      0       701       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Also run in this folder:

```
python3 -I srcrefs.py check --refs <text file> bgg4-*.l4
srcrefs check: 314 src: lines, 148 runs, 207 locators, 0 problems
python3 -I srcrefs.py check --strict --refs <text file> bgg4-*.l4
srcrefs check: 314 src: lines, 148 runs, 207 locators, 0 problems
python3 -I quotecheck.py <text file>,<chapter 3 text file> bgg4-*.l4
quotecheck: 297 fragments found in the text, 0 German-looking fragments NOT found, 29 English fragments ignored
python3 -I coverage.py
text lines: 166, non-blank: 134, rows: 122; operative rows: 89; heading rows: 31
dispositions: encoded: 17, fork: 70, inert: 33, repealed or blank: 2 ; inert by reason: {1: 33, 2: 0, 3: 0}
layer-1 functions: 134 (regulative rules: 14); forks: 34; seat questions: 46; seat cases: 180
functions tested by an assertion or trace that names them: 131; only exercised through a caller: 1; labelled repealed stubs (no outcome, nothing calls them): 2
problems: 0
```

The trace outcomes (one line per `#TRACE`: file, line, rule, input, clock, event, outcome), printed by `tracetable.py` in this folder and not asserted:

```
bgg4-tests-cantonal.l4 | 111 | Art 110 the cantons' duty to ensure the review by a judicial authority | AT 0 WITH | 0 | ensure that the court or a previously competent judicial authority freely reviews the facts and applies the law of its own motion at 5 | FULFILLED
bgg4-tests-cantonal.l4 | 113 | Art 111(1) the cantons' duty to let a person entitled to appeal take part as a party | AT 0 WITH | 0 | let a person entitled to appeal take part as a party before all cantonal lower instances at 5 | FULFILLED
bgg4-tests-cantonal.l4 | 115 | Art 111(3) the cantons' duty to let the immediate lower instance examine the complaints under Art 95 to 98 | AT 0 WITH | 0 | let the immediate lower instance examine at least the complaints under Art 95 to 98 at 5 | FULFILLED
bgg4-tests-cantonal.l4 | 118 | Art 112(1) the cantonal authority's duty to notify the decision to the parties in writing | AT 0 WITH | 0 | notify the decision to the parties in writing at 2 | FULFILLED
bgg4-tests-cantonal.l4 | 121 | Art 112(2) the parties' permission to demand the complete version within 30 days | AT 0 WITH | 0 | demand the complete version of the decision at 30 | FULFILLED
bgg4-tests-cantonal.l4 | 123 | Art 112(2) the parties' permission to demand the complete version within 30 days | AT 0 WITH | 0 | demand the complete version of the decision at 31 | FULFILLED
bgg4-tests-procedure.l4 | 174 | Art 102(1) the Court's duty to serve the appeal and set a time limit | AT 0 WITH | 0 | serve the appeal and set a time limit for observations at 3 | FULFILLED
bgg4-tests-procedure.l4 | 177 | Art 102(2) the lower instance's duty to send the files within the time limit | 10 | 0 | send the files to the Federal Supreme Court at 10 | FULFILLED
bgg4-tests-procedure.l4 | 179 | Art 102(2) the lower instance's duty to send the files within the time limit | 10 | 0 | send the files to the Federal Supreme Court at 11 | DEONTIC BREACHED: BREACH BY `Lower instance` BECAUSE "the files were not sent within the time limit the Court 
bgg4-tests-procedure.l4 | 182 | Art 107(3) the Court's duty to give the decision not to enter within 15 days | AT 0 WITH | 0 | give the decision not to enter on the appeal at 15 | FULFILLED
bgg4-tests-procedure.l4 | 184 | Art 107(3) the Court's duty to give the decision not to enter within 15 days | AT 0 WITH | 0 | give the decision not to enter on the appeal at 16 | DEONTIC BREACHED: BREACH BY `Federal Supreme Court` BECAUSE "the decision not to enter was not given within 15
bgg4-tests-procedure.l4 | 187 | Art 107(4) the Court's duty to decide within one month | 31 | 0 | decide on the appeal against the Federal Patent Court decision on a licence at 31 | FULFILLED
bgg4-tests-procedure.l4 | 189 | Art 107(4) the Court's duty to decide within one month | 31 | 0 | decide on the appeal against the Federal Patent Court decision on a licence at 32 | DEONTIC BREACHED: BREACH BY `Federal Supreme Court` BECAUSE "the Court did not decide within one month after t
bgg4-tests-time-limit.l4 | 159 | Art 100(1) the appellant's duty to file the appeal within 30 days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 30 | FULFILLED
bgg4-tests-time-limit.l4 | 162 | Art 100(1) the appellant's duty to file the appeal within 30 days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 31 | DEONTIC BREACHED: BREACH BY Appellant BECAUSE "the appeal was not filed within 30 days after the complete vers
bgg4-tests-time-limit.l4 | 165 | Art 100(1) the appellant's duty to file the appeal within 30 days | AT 0 WITH | 0 | no event | PARTY Appellant MUST `file the appeal with the Federal Supreme Court` WITHIN 30 HENCE FULFILLED LEST BREACH BY
bgg4-tests-time-limit.l4 | 168 | Art 100(2) the appellant's duty to file the appeal within ten days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 10 | FULFILLED
bgg4-tests-time-limit.l4 | 170 | Art 100(2) the appellant's duty to file the appeal within ten days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 11 | DEONTIC BREACHED: BREACH BY Appellant BECAUSE "the appeal was not filed within ten days after the complete ver
bgg4-tests-time-limit.l4 | 173 | Art 100(3) the appellant's duty to file the appeal within five days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 5 | FULFILLED
bgg4-tests-time-limit.l4 | 175 | Art 100(3) the appellant's duty to file the appeal within five days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 6 | DEONTIC BREACHED: BREACH BY Appellant BECAUSE "the appeal was not filed within five days after the complete ve
bgg4-tests-time-limit.l4 | 178 | Art 100(4) the appellant's duty to file the appeal within three days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 3 | FULFILLED
bgg4-tests-time-limit.l4 | 180 | Art 100(4) the appellant's duty to file the appeal within three days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 4 | DEONTIC BREACHED: BREACH BY Appellant BECAUSE "the appeal was not filed within three days after the complete v
bgg4-tests-time-limit.l4 | 183 | Art 101 the appellant's duty to file the appeal against an enactment within 30 days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 30 | FULFILLED
bgg4-tests-time-limit.l4 | 185 | Art 101 the appellant's duty to file the appeal against an enactment within 30 days | AT 0 WITH | 0 | file the appeal with the Federal Supreme Court at 31 | DEONTIC BREACHED: BREACH BY Appellant BECAUSE "the appeal was not filed within 30 days after the publication o
```

## What would need doing before the encoding is worth relying on

- A Swiss lawyer should read every fork in the register and every branch under "Marginal readings for a lawyer" against the official text.
- The text file must be compared with the official publication; this encoding says nothing about whether the consolidated version is the authoritative one.
- The rules in chapter 2 (how time limits run, are suspended and are restored; the value in dispute; the parties) and the statutes named under "What the text does not answer" must be encoded or supplied as inputs before an answer from this chapter is an answer about whether and by when an appeal lies.
- Chapter 3's functions do not call chapter 4: a maintainer who can change chapter 3 could pass the time-limit and appealability answers into them, and the value in dispute, which chapter 3's notes say chapter 4 works out, is not in chapter 4.
- The day count (the day after notification is day 1), the shorter period for bill-of-exchange enforcement, the start of an intercantonal period and the month rule of Art 107(4) are forks a lawyer should confirm (F9, F11, F12, F21).
- The seat questions with many inputs (the three record questions have more than thirty) would do better as a series of short questions by group, which needs new questions in layer 2 and no change in layer 1.
- The open-textured inputs need guidance for a lay user that this chapter does not give.
- A regulative rule cannot be asserted on the stable binary and a `MAY` window is not enforced in a trace; when the language fixes either, the traces become assertions.
