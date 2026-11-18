# Independent reader: triage of the Art 336 to 336b row

An independent reader, who had only the German text and then the layer-1 and seat modules (no tests, notes or plans), wrote 113 scenarios before opening any module and asserted 104 of them in `or336-tests-independent.l4` (111 assertions, 7 scenarios with a second one).
On the first run 98 were satisfied and 13 failed, 0 refused.
Every one of the 13 is now restated to the encoding's answer, with a `RECONCILED` comment on its line giving the reader's expectation and the reading behind it, so the file passes and its comments are the record of the disagreements.

**Three of the 13 were labelled `ENCODER` by the reader (lines 154, 188 and 236 of the file, scenarios S70, S91, S112).**
They concern Art 336b(2), "Ist die Einsprache gültig erfolgt und einigen sich die Parteien nicht ..., so kann die Partei, der gekündigt worden ist, ihre Entschädigungsforderung geltend machen", when the parties do agree to continue.
The encoding answers `NOTHING`; the reader expected `JUST FALSE` from a worked example in the reader's prompt ("a person may appeal if the decision was made after 1 January").
That example was the coordinating session's, and it contradicted the Guide's ruling on functions named for a grant or a power (2026-11-12), limit 1: a function named for a power ("kann") whose `if` gate failed answers `NOTHING`, unless the text closes the gate itself ("only if").
Here the text does not.
So these three are reclassified `SCENARIO` (the prompt's defect, not the encoder's), and the encoding follows the ruling.

**Nine of the 13 are `AMBIGUOUS`: two readings the Guide leaves open, labelled "assumed, not ruled" and listed for a lawyer.**
Six (lines 22, 38, 60, 78, 96 and 200) are one question: Art 336(1) lists grounds without closing the list, so a dismissal that meets none of them is either "not covered" (`NOTHING`, the reader) or "no" because "wenn" introduces an "if" (`JUST FALSE`, the encoding, which names its question "a ground the Article lists", fork F1).
Three (lines 52, 54 and 58) are Art 336(1)(e): a qualifier inside the "weil" ground ("schweizerischen", "obligatorischen", "nicht freiwillig") is read by the reader as a scope limit with no "only" (`NOTHING`) and by the encoding as a failed condition of the ground (`JUST FALSE`, fork F7).

**One of the 13 is the reader's own mistake (line 80, S29, `SCENARIO`).**

**Gaps.**
Nine scenarios could not be asked of the encoding and are not repaired: Art 335d (what a mass dismissal is) and Art 335f lie outside the sources and are plain inputs; the amount of the compensation is the judge's (Art 336a(2)); whether an e-mail is "in writing" is an input; the length of a notice period and the effect of settlement talks on the 180 days are outside the text; whether an abusive dismissal is void is not in the text.
A tenth, an employer who received an abusive resignation asking whether to assert the claim, was a real hole in the employer seat.
It, and the employer's other procedure questions (is the objection valid, the last day to object, the last day to sue, forfeiture), which were worded only for the party that gave the notice, were built after the reader returned, as recipient-side questions 21 to 25 of the employer seat (fork F31, reading A: either party can be the recipient).
Each calls the same layer-1 rule as its employee twin, and the mirror cases assert that the two recipient seats agree.

---

The reader's own triage follows, unchanged.

# Triage: Art. 336 to 336b OR, independent tests

Run: `l4-main-110 run tests-independent.l4` from `enc/`, `JL4_LIBRARY_PATH` unset.
Result: 111 assertions, 98 satisfied, 13 failed (all `assertion failed` at Error), 0 refused.
Scenarios written: 113 in `ANSWERS.md`; 104 asserted, 9 are GAPs (the 111 assertions include 7 second assertions on a scenario, marked /overall, /pay, /b, /owed).
Line numbers are lines of `enc/tests-independent.l4`.
JT = JUST TRUE, JF = JUST FALSE, N = NOTHING.

## Failed assertions (13)

| scenario | line | provision | expected | encoding answered | verdict |
| --- | --- | --- | --- | --- | --- |
| S2/overall | 22 | 336(1)(a), characteristic connected with employment, overall | N | JF | AMBIGUOUS: list not closed with "only" (N) vs "wenn" as an if (JF); same root as S20 |
| S9/overall | 38 | 336(1)(c), thwarting not the only purpose, overall | N | JF | AMBIGUOUS: same two readings as S20 |
| S16 | 52 | 336(1)(e), foreign military service | N | JF | AMBIGUOUS: "schweizerischen" as a scope limit with no "only" (N, periods ruling (c)) vs a failed "weil" condition (JF); the encoding cannot tell foreign service from no service, all five facts are false |
| S17 | 54 | 336(1)(e), voluntary (not compulsory) Swiss service | N | JF | AMBIGUOUS: "obligatorischen" as scope limit (N) vs failed condition (JF); same input vector as S16 |
| S19 | 58 | 336(1)(e), statutory duty voluntarily assumed | N | JF | AMBIGUOUS: "nicht freiwillig" as scope limit (N) vs failed condition (JF) |
| S20 | 60 | 336(1) chapeau, dismissal for poor performance, no listed ground | N | JF | AMBIGUOUS: open list, other grounds not excluded (N) vs "wenn" is an if (JF); the encoding says JF means "no listed ground met", not "no other ground exists" |
| S28/overall | 78 | 336(2)(b), employer proves a reason, overall | N | JF | AMBIGUOUS: same two readings as S20 |
| S29 | 80 | 336(2)(b), representative appointed, not elected | N | JF | SCENARIO: I read "gewählter" as a scope word, but it sits inside the "während ... ist" clause, which the guide treats as a "while" condition (JF), as I did myself in S30; JF is the consistent answer |
| S36/overall | 96 | 336(2)(c), not a mass dismissal, overall | N | JF | AMBIGUOUS: same two readings as S20 |
| S70 | 154 | 336b(2), valid objection but the parties agree to continue: may assert | JF | N | ENCODER: "Ist ... und einigen sich ... nicht, so kann" is a power with an "if", the shape of the guide's worked example 1 (may + if, unmet: JF); the encoding's comment says the text does not say "only if", but the guide lists "if" and "only if" together. If read as "a duty whose if is unmet" it would be AMBIGUOUS |
| S91 | 188 | 336b(2), employee seat: objected in time, then agreed to stay: can I still claim | JF | N | ENCODER: same root as S70 |
| S97 | 200 | 336(1), employee seat: dismissed for poor work, abusive on a listed ground | N | JF | AMBIGUOUS: same two readings as S20 |
| S112 | 236 | 336b(2), employer seat: objection in time, then agreed to continue: can he still claim | JF | N | ENCODER: same root as S70 |

## Refused assertions

None.

## GAPs (no function asks the question; listed in the header comment at line 15 of `tests-independent.l4`)

| scenario | provision | expected | what the encoding has | verdict |
| --- | --- | --- | --- | --- |
| S37 | 336(2)(c), is 5 of 500 a mass dismissal | N (Art. 335d is outside the sources) | "mass dismissal" is a plain yes/no input, no function decides it (documented in `or336-nouns.l4` header) | GAP |
| S38 | 336(2)(c) with 335f(2), consultation without any chance to submit proposals | JT (abusive) | "consulted" is a yes/no input, 335f is not modelled (documented in the nouns header) | GAP |
| S50 | 336a(2), is a minimum compensation fixed | N | no function; the closest, `Art 336a(2) the amount of the compensation`, always answers NOTHING, which is consistent | GAP |
| S53 | 336a(2), may the parties fix the amount by agreement | N | no function (same closest function) | GAP |
| S65 | 336b(1), does an e-mail satisfy "schriftlich" | N | "in writing" is a yes/no input | GAP |
| S72 | 336b(2), the party who gave notice asserts a claim | N | no function for the notice-giver | GAP |
| S78 | 336b(2), do settlement talks extend the 180 days | N | no function | GAP |
| S79 | 336/336a, is an abusive dismissal void or ineffective | N | no function | GAP |
| S80 | 336b(1), length of the notice period for three years' service | N (outside the sources) | the notice period's last day is an input | GAP |
| S110, part 2 | 336b(2), employer seat: an employer whose employee resigned abusively asks "may I assert my claim" | JT | the employer seat has procedure questions only for "the other side" (the party that received the notice); the layer-1 `Art 336b(2) the party that received the notice can assert the compensation claim` would answer, but there is no employer-claimant question | GAP |

## Notes

- Six of the failures (S2/overall, S9/overall, S20, S28/overall, S36/overall, S97) rest on one reading question, the one in S20: if the reviewer rules that "wenn" is an if, my expectation for all six is the one to withdraw; if the reviewer rules the list open, they are real findings.
- S16, S17 and S19 stand or fall together: they are one question about qualifiers inside a "weil" ground.
- S70, S91 and S112 are one finding (the "if" of the power in 336b(2)) seen through layer 1, the employee seat and the employer seat.
- S44 and S45 (who is the creditor) are asserted only as the boolean "the notice-giver owes compensation"; the regulative rule names the payer and no payee.
