# Independent reader: triage of the ePrivacy Directive row

An independent reader, who had only the consolidated text and then the layer-1 and seat modules (no tests, notes or plans), wrote 295 scenarios (285 before it opened any module) and asserted 277 of them in `epd-tests-independent.l4`: 21 for the individual seat, 16 for the provider seat and 14 for the sender seat.
On the first run 260 were satisfied and 17 failed, 0 refused; on every failure the encoding answered `NOTHING` where the reader expected `JUST TRUE` or `JUST FALSE`.
The 17 are accounted for below; the file now passes (277 satisfied, 0 failed, 0 refused), and each restated line carries a `RECONCILED` comment giving the reader's expectation and the reading behind it.
Lines the encoder later changed are marked in their comments.

**Three were real findings, repaired by the encoder after the reader returned; the reader's expectations stand unchanged and now pass.**
Art 13(3): when no consent was given and the recipient has said they do not wish to receive the call, both national options prohibit it, so the text decides the case whichever option national law chose, but the first version answered `NOTHING` because the option was unstated (scenarios 177 and 291, through layer 1, the individual seat and the sender seat).
Art 16(2): a "may" function whose "Where" gate failed answered `NOTHING`, against the encoder's own F11 for the other "may" functions (scenario 228).

**Four were my prompt's defect, not the encoder's (scenarios 50, 86, 263 and 292, restated to `NOTHING`).**
Each is a "may" function whose "if" gate failed (Art 4(3) fourth subparagraph, Art 6(3)).
The reader's prompt carried a worked example, "a person may appeal if the decision was made after 1 January", expected `JUST FALSE`, which contradicts the Guide's ruling on functions named for a grant or a power (2026-11-12), limit 1: such a function answers `NOTHING` unless the text closes the gate with "only".
The reader noticed that the encoding cited a ruling it had not been shown (fork F13).

**Two were the reader's own mistakes (scenarios 176 and 280): "not allowed ... without the consent" with consent falls outside the prohibition's own words and answers `NOTHING`.**

**Eight were `AMBIGUOUS`: readings the Guide leaves open, labelled "assumed, not ruled" and listed for a lawyer (scenarios 17, 46, 47, 61, 78, 79, 80 and 203).**
They are an "except" read as re-including, a "shall not be required if" with its "if" unmet, "without the consent" and "without prejudice to" read like "unless", and a purpose list inside a "when" condition.
A ninth, added after the encoder's repair of Art 16(2): the first limb of its "Where" clause (a subscriber to a fixed or mobile voice telephony service) is read by the reader as a scope limit (`NOTHING`) and by the encoder as a failed "Where" (`JUST FALSE`, fork F11).

**A seat-polarity defect came from the reader's side note, and the encoder audited for it.**
The two seat questions "Is my provider excused from telling me about the breach..." and "Am I excused from notifying the subscriber..." answered `JUST FALSE` when the provider is excused, because they called the layer-1 function "notification is required".
The encoder swapped the two definite answers in both (excused is now `JUST TRUE`) and audited all 158 seat questions: 8 mismatches in all (3 swapped, including "May I record communications ..." in Art 5(2); 5 reworded to the layer-1 polarity with no answer changed), listed in the "Seat polarity audit" section of `NOTES.md`.
Two reader assertions that had followed the old polarity are restated to `JUST TRUE`, with a comment, and one seat call is renamed to the reworded question.
This audit is the encoder's own comparison, not an independent reader's.

**24 gaps (scenarios that cannot be asked of the encoding) are not repaired.**
Most are provisions the encoder declared inert legislative machinery (reason 2): Art 4(5), 14a(1) to (3), 15a(4) second subparagraph, 17, 18, 19 first subparagraph and 20, including the dates in Art 17(1), 18 and 20, although the equally dated Art 15a(1) deadline is encoded.
The rest: whether an act is valid consent under Directive 95/46/EC (an input; the Directive points outside the sources); no composite function for Art 4(3) second and third subparagraphs, or for Art 5(3) ("may this cookie be stored or read"); no "duty met" function for Art 6(1), 6(3) second sentence and 7(2); and no input for a charge on the call-rejection feature (Art 8(3)) or on inclusion in a directory (Art 12(2)).
These are known limits of this row.

**A later seat-polarity pass changed one of the reader's lines and re-worded seven seat questions.**
After the reader returned, a second independent reader checked every seat question's wording against what `JUST TRUE` and `JUST FALSE` mean in the function it calls, without the encoder's audit table.
It found no inverted answer, so the encoder's eight fixes stand, and it flagged one question that asks "what" and answers a bare `TRUE` (Art 13(3), individual seat) and five "may the authority ..." questions whose layer-1 function says what a Member State must give a body.
The encoder re-worded those six as yes/no questions ("Must national law make ... not allowed", "Does the Directive require my Member State to give the authority the power to ...") and, on the lead's instruction, a seventh that calls the same Art 15a(2) function; no answer changed.
Two of the reader's assertions called the re-worded Art 13(3) question by its old name; they are renamed in the file, with a comment, and their expected values are unchanged.

---

The reader's own triage follows, unchanged.

# Triage: ePrivacy Directive 2002/58/EC, consolidated 19.12.2009 (independent test pass)

File: `enc/tests-independent.l4` (277 assertions: 260 satisfied, 17 failed, 0 refused; 24 gaps listed as comments at lines 299-322 of that file).
Binary: `l4-main-110`, `JL4_LIBRARY_PATH` unset, read from the diagnostics (`eval/assertion-failed` x17, `eval/assertion-passed` x260; two deliberate control assertions failed as they should in a scratch probe).
Format: scenario | assertion line | provision | my expected | the encoding answered | VERDICT | why.
On every FAILED line the encoding answered NOTHING (read from `#EVAL` of the same expression), none answered the opposite polarity.

## Failed assertions

17 | line 36 | Art 2(d) second sentence | JUST TRUE | NOTHING | AMBIGUOUS | a broadcast-service stream relatable to one identifiable subscriber: "except to the extent" re-includes it (reading A) vs the sentence only lifts the exclusion and the first sentence decides (reading B, the encoding's)
46 | line 64 | Art 4(3) third subparagraph (function "notification is required") | JUST TRUE | NOTHING | AMBIGUOUS | protection not demonstrated to the authority, so the exemption is unmet: reading A, "shall not be required if" is silent when unmet and the second subparagraph requires it, so NOTHING from this function (the encoding's); reading B, the unmet "if" makes "required" JUST TRUE; the seat question "Is my provider excused ..." then answers NOTHING for a plain "no"
47 | line 65 | Art 4(3) third subparagraph | JUST TRUE | NOTHING | AMBIGUOUS | protection not applied to the data concerned: same two readings as 46
50 | line 68 | Art 4(3) fourth subparagraph | JUST FALSE | NOTHING | ENCODER | provider already notified: "may require ... if the provider has not already notified" is a "may ... if" whose "if" is unmet, which is worked example 1 of the convention (JUST FALSE); the encoding cites a "grant and power ruling" (FORK F13) that is not among the convention paragraphs given to me, so the lead should check that ruling
61 | line 78 | Art 5(1) second sentence | JUST FALSE | NOTHING | AMBIGUOUS | third party taps with the consent of the users: "without the consent" read like "unless" (A) vs a limit on the prohibition in its own wording (B, the encoding's)
78 | line 95 | Art 6(1) | JUST FALSE | NOTHING | AMBIGUOUS | no longer needed but within the bill-challenge period: "without prejudice to paragraphs 2, 3 and 5 and Article 15(1)" read like "except" (A) vs it only preserves the other provisions (B, the encoding's); the one boolean bundles 2, 3, 5 and 15(1)
79 | line 96 | Art 6(1) | JUST FALSE | NOTHING | AMBIGUOUS | consent-based value added service: same two readings as 78
80 | line 97 | Art 6(1) | JUST FALSE | NOTHING | AMBIGUOUS | retention under Article 15(1): same two readings as 78
86 | line 102 | Art 6(3) first sentence | JUST FALSE | NOTHING | ENCODER | consent given only after processing began: "may process ... if ... prior consent" is a "may ... if" whose "if" is unmet (worked example 1: JUST FALSE); the encoding returns NOTHING under the same "grant and power ruling" (FORK F13) as scenario 50
176 | line 189 | Art 13(3) (whole-Article function) | JUST TRUE | NOTHING | SCENARIO | live call with the recipient's consent: the prohibition is "not allowed ... without the consent", so with consent the case falls outside the prohibition's own words and the convention gives NOTHING; my JUST TRUE treated consent as a positive grant. (The encoding is asymmetric with Art 13(1), where consent gives JUST TRUE, but that is because 13(1) is worded "may be allowed only in respect of ... prior consent".)
177 | line 190 | Art 13(3) (whole-Article function) | JUST FALSE | NOTHING | ENCODER | live call, no consent, the recipient does not wish to receive it, national option unstated: option A (consent) catches it and option B (people who do not wish) catches it, so the text answers whichever option national law chose; the encoding tests `national legislation has not been stated` first and stops at NOTHING
203 | line 217 | Art 15(1) first sentence | JUST FALSE | NOTHING | AMBIGUOUS | restriction for commercial convenience (a purpose not in the list): the purposes sit inside the "when ... to safeguard ..." condition so a failed "when" is JUST FALSE (A, rulings (b) and (c)) vs the list is not closed with "only" (B, the encoding's)
228 | line 240 | Art 16(2) | JUST FALSE | NOTHING | ENCODER | entry included in breach of Directive 95/46/EC: the clause opens "Where ... in conformity with ..." and ruling (b) says a failed "where" is JUST FALSE; the encoding answers NOTHING for the three limbs of this "where" but JUST FALSE for every other failed "where" (Art 8(1), 8(2), 9(2), 14(2), 14(3))
263 | line 265 | Art 6(3), provider seat ("May I process traffic data for marketing or value added services") | JUST FALSE | NOTHING | ENCODER | subscriber consented only after I started: same as 86
280 | line 281 | Art 13(3), sender seat ("May I send this marketing message to this recipient") | JUST TRUE | NOTHING | SCENARIO | live human salesperson, recipient consented: same as 176
291 | line 292 | Art 13(3), individual seat ("What must national law do about an unsolicited marketing call ...") | JUST TRUE (must stop) | NOTHING | ENCODER | no consent and I have said I do not wish to receive such calls: same as 177
292 | line 293 | Art 4(3), provider seat ("May the authority require me to notify the subscriber or individual") | JUST FALSE | NOTHING | ENCODER | I have already notified the subscriber: same as 50

## Refused assertions

None (no `assertion refused` diagnostics).

## Gaps (scenarios the encoding cannot be asked; the file line is the GAP comment in the tests file)

30 | line 299 | Art 2(f) | whether an act is valid consent under Directive 95/46/EC | GAP | the encoding takes validity as a plain input of the Art 2(f) function and no other function judges it (the Directive points outside the sources, so NOTHING would be the right answer to ask)
46-47 composite | line 300 | Art 4(3) second and third subparagraphs | "is the subscriber notification required on these facts" | GAP | only the two pieces exist (second subparagraph: must notify; third: exemption); no function composes them
59 | line 301 | Art 4(5) | Commission power to adopt technical implementing measures after consulting ENISA, the Art 29 Working Party and the EDPS | GAP | not encoded (declared inert machinery)
72-75 composite | line 302 | Art 5(3) | "may this cookie be stored or read" for the unexempt, unconsented cases | GAP | only the consent-condition function and the exemption function exist; scenarios 72 to 75 were asserted as the exemption piece (NOTHING) only
81 | line 303 | Art 6(1) | the alternative "made anonymous instead of erased" meets the duty | GAP | no boolean "duty met" function for 6(1); only a regulative rule with one act "erase the traffic data or make it anonymous"
90 | line 304 | Art 6(3) second sentence | provider gives no possibility to withdraw | GAP | the function takes only whether consent was given, so non-compliance cannot be asked
99 | line 305 | Art 7(2) | Member State applied national provisions reconciling itemised bills with privacy | GAP | only "does the duty bind" exists, no compliance function
110 | line 306 | Art 8(3) | provider charges a fee for the call-rejection feature (silent: NOTHING) | GAP | no charge input on the 8(3) functions
145 | line 307 | Art 12(2) | charge for being included in the directory (silent: NOTHING) | GAP | no input for a charge on inclusion
200 | line 308 | Art 14a(1) | Commission assisted by the Communications Committee | GAP | not encoded (declared inert machinery)
220 | line 309 | Art 15a(4) second subparagraph | regulatory authority gave the Commission a summary in good time | GAP | not encoded (declared inert machinery)
221 | line 310 | Art 15a(4) second subparagraph | authority adopted the measure without giving the summary | GAP | not encoded (declared inert machinery)
229 | line 311 | Art 17(1) | transposed on 30 October 2003: in time? (YES) | GAP | not encoded (declared inert machinery), although the equally dated Art 15a(1) deadline of 25 May 2011 is encoded
230 | line 312 | Art 17(1) | transposed on 31 October 2003: in time? (NO, "Before 31 October 2003") | GAP | not encoded
231 | line 313 | Art 17(1) | transposed on 1 November 2003: in time? (NO) | GAP | not encoded
232 | line 314 | Art 18 | report on 31 October 2006 (YES) | GAP | not encoded (declared inert machinery)
233 | line 315 | Art 18 | report on 1 November 2006 (NO) | GAP | not encoded
234 | line 316 | Art 18 | report on 30 October 2006 (YES) | GAP | not encoded
235 | line 317 | Art 19 first subparagraph | Directive 97/66/EC repealed on 30 October 2003? (NO) | GAP | not encoded (declared inert machinery)
236 | line 318 | Art 19 first subparagraph | repealed on 31 October 2003? (YES) | GAP | not encoded
237 | line 319 | Art 19 first subparagraph | repealed on 1 November 2003? (YES) | GAP | not encoded
239 | line 320 | Art 20 | in force on 31 July 2002 (publication day, OJ L 201 31.7.2002)? (YES) | GAP | not encoded (declared inert machinery)
240 | line 321 | Art 20 | in force on 30 July 2002? (NO) | GAP | not encoded
270 | line 322 | Art 8(3), provider seat | provider charges a fee for the call-rejection feature (silent: NOTHING) | GAP | the provider-seat question takes only offers and simple means

## Observations (not counted as findings)

- The seat questions "Is my provider excused from telling me about the breach ..." (individual seat) and "Am I excused from notifying the subscriber ..." (provider seat) answer JUST FALSE when the provider IS excused; the seat comment says so, but a reader taking the title at face value reads the answer backwards, and the exit code is 0 either way.
- Where the Art 13(3) national option is unstated, every Art 13(3) answer is NOTHING even in the two cases (scenarios 177, 291) the text decides under both options.
