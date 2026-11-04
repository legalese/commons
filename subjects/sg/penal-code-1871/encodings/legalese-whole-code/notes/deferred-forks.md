# deferred forks - the completion pass of 2026-11-04

Every ambiguity met while encoding `pc-body-a-deferred.l4`, `pc-body-b-deferred.l4`, `pc-body-b-deferred-images.l4` and `pc-general-moved.l4`: the readings, the one taken, why, and the text that licenses each.
Written by one Sonnet 5.5 agent.
The text is the converter's plain-text rendering of Singapore Statutes Online ("Current version as at 09 Sep 2026"), not the official text; a line number is a line of `registers/source-bundle/PC1871.txt`.
None of these has been put to a lawyer.
The ones that change what a result says are also listed in NOTES.md under "Marginal readings for a lawyer".

How to read a result: `JUST TRUE` and `JUST FALSE` are answers the text gives in its own words; `NOTHING` is "the text does not say".
A caller must never turn `NOTHING` into `FALSE` (NOTES.md, "Reading a result: FALSE and NOTHING").

## Body-a (`pc-body-a-deferred.l4`)

### DEF-A1. Infanticide: is "would have amounted to murder" an element? (s 310, s 311; lines 7181-7187)

**Text.** A woman who by an intentional act or omission causes the death of her child below 12 months, with the balance of her mind disturbed by reason of not having fully recovered from giving birth or by the effect of lactation, "shall, notwithstanding that the circumstances were such that but for this section the offence would have amounted to murder, be guilty of the offence of infanticide".
**Readings.** (a) the killing being murder but for the section is a condition, so the ladder also asks whether the facts make out murder; (b) "notwithstanding" removes a bar and adds nothing: the ladder asks for the woman, the intentional act or omission, the child below 12 months, and the disturbance.
**Taken.** (b). The words say the section applies even where the offence would otherwise be murder; they do not say it applies only then.
**Consequence.** A woman whose act would not have been murder at all (no intention to kill, say) is still within s 310 on these facts if she meant the act. Under (a) she would not be.

### DEF-A2. Two punishments for sustained abuse (s 304B(1)(a), (b); lines 6859-6907)

**Text.** The two limbs of subsection (1) each carry a punishment; the text does not say when the court gives which.
**Readings.** (a) two offences, one per limb; (b) one offence whose record carries both punishments.
**Taken.** (b), as `s 304(a)` does with its (i) and (ii): one record, the charge states the words of both.
**Consequence.** The charge states the words of both limbs.

### DEF-A3. Which alternative of s 304C(1)(d)? (s 304C(2); lines 6985-6995)

**Text.** Subsection (2): the prosecution need not prove which of the two alternatives of (1)(d) applies.
**Taken.** The ladder is the OR of the two, which is exactly "need not prove which". Both tested together.

### DEF-A4. Does s 304C(3) answer the whole offence or only the second alternative? (lines 6985-6995)

**Text.** "A is not guilty of an offence under this section if A could not have been expected in A's circumstances to take any such step."
**Readings.** (a) a flat negative for the whole offence; (b) it answers only the second alternative of (1)(d) (failure to take steps), where "any such step" has its antecedent.
**Taken.** (a): the ladder asks `NOT` of the leaf `A could not have been expected in A's circumstances to take any such step` for the whole offence, whichever alternative of (1)(d) is relied on, and a FALSE-kind comment on that branch quotes the words.
**Consequence.** On (b), an accused charged on the first alternative (his own act) could not use the bar. Marginal reading (a) in NOTES.md: a flat negative counts as the text's no.

### DEF-A5. Is the definition of an "unlawful" act closed? (s 304C(5)(c), lines 6974-6987; s 335A(3), lines 7570-7585)

**Text.** An "unlawful" act, other than an act by A, "is one that constitutes an offence ... or would constitute such an offence but for being the act of a person entitled to rely on" a listed defence.
**Readings.** (a) closed: any other act is not "unlawful" here; (b) open: the description is one way to be unlawful.
**Taken.** (a), because "is one that" defines and no "includes" is used. The branch is `OTHERWISE JUST FALSE` with the words quoted.
**Consequence.** A caller with an act that is wrongful but neither an offence nor excused by one of the listed defences gets `FALSE`, not `NOTHING`. Marginal reading (a).

### DEF-A6. "Group" (s 308A(3); line 7145)

**Text.** "In subsection (1), 'group' has the meaning given by section 2(1) of the Organised Crime Act 2015."
**Taken.** That Act is not in the sources, so whether there is a group is an input, and its `@desc` says where the meaning comes from.
**Consequence.** None for the Code's own words; the investigator answers a question the sources do not.

### DEF-A7. The Explanation to s 314 (line 7240)

**Text.** "It is not essential to this offence that the offender should know that the act is likely to cause death."
**Taken.** The record carries the knowledge as a leaf the ladder ignores; the Explanation is tested on both sides (knowledge true, knowledge false: same result).

### DEF-A8. "Quick unborn child" (s 316; lines 7265-7270)

**Text.** The Code does not define "quick".
**Taken.** One input (`the accused by such act causes the death of a quick unborn child`), with the Illustration to s 316 tested. No age or stage is guessed.

## Body-b (`pc-body-b-deferred.l4`, `pc-body-b-deferred-images.l4`)

### DEF-B1. The presumption in the Explanations to ss 372 and 373 (lines 8080-8083, 8094-8097)

**Text.** A person who disposes of (or obtains) a female below 21 to a prostitute or brothel-keeper "shall, until the contrary is proved, be presumed" to have intended prostitution.
**Readings.** (a) the presumption is an element; (b) it is a rebuttable presumption of intent, applying when the stated facts are shown and no more.
**Taken.** (b): the ladder reads the intent and the knowledge as the caller states them, and a function of its own (`s 372 Explanation the intent that she shall be used for prostitution`; likewise for s 373) returns the constructor `presumed, until the contrary is proved, ...` when the Explanation's two facts are shown and `not covered by this Explanation` otherwise.
**Consequence.** Outside the Explanation's facts the answer is "not covered", not "no intent": the Explanation does not say the intent is absent. Marginal reading (b).

### DEF-B2. Selling or buying abroad: the act "that would, if done in Singapore, constitute an offence under section 376B" (s 376C(1); lines 8387-8407)

**Taken.** A nested `Commercial Sex Facts` for the same act, which the caller supplies. The punishment is borrowed from s 376B(1) or (2), whichever the nested facts make out, and the charge states the words of the one borrowed.
**Consequence.** The caller fills two records for one act.

### DEF-B3. Sexual communication: replies and place of origin (s 376EB(2); s 376EC(2); lines 8635-8644)

**Text.** (a) "whether B replied is immaterial"; (b) where the communication originated is immaterial "provided that either A or B was in Singapore".
**Taken.** (a): the leaf is carried and ignored, tested both ways. (b): "provided that" is a condition, so a communication with neither in Singapore is not within the subsection (the text's own "provided that").

### DEF-B4. The spouse bar in s 376ED(4) (lines 8741-8742)

**Text.** "No person shall be guilty of an offence under this section against B if B is his or her spouse with the consent of that spouse."
**Readings.** (a) bars both offences, (1) activity and (2) image; (b) bars (1) only.
**Taken.** (a): the text says "an offence under this section", and the module's comment says subsection (4) is read as covering both.
**Consequence.** Marginal reading (a): a flat negative counts as the text's no.

### DEF-B5. s 376F(2) "subject to subsection (3)" (lines 8800-8846)

**Taken.** The offence under (2) is the one whose touching involved no penetration of the kind (3) describes; the offence under (3) is the one that did. The two charges are framed separately.

### DEF-B6. s 376G(4): the penetration "which would constitute an offence under section 375(1)(a), 375(1A)(a), 376(2) or 376AA(1)" (lines 8850-8905)

**Taken.** A nested `Sexual Penetration Facts` for the same act, which the caller supplies, as for DEF-B2.
**Also.** Subsection (6) ("a person below 18 years of age who is a victim of an offence under section 376AA is not guilty of an offence under this section in respect of the same acts") is read as a flat negative for the whole offence. Marginal reading (a).

### DEF-B7. s 377BO is six limbs, not one offence (lines 9837-9903)

**Text.** Subsections (1), (2), (3), (5), (6) and (7) each extend the offences "under section 377BG, 377BH or 377BL(2) or (3), as the case may be" to acts done outside Singapore; (4) only makes (5) and (6) turn on the exploitative relationship.
**Taken.** The underlying offence is a nested record for the same act, and the charge is framed under the underlying section read with the limb of 377BO. Where the facts make out more than one underlying offence, the charge is framed under the first in the order the text names them: 377BG, 377BH, 377BL(2), 377BL(3).
**Consequence.** A caller who wants a different order frames the charge by hand.

## Provisions moved out of `inert` (`pc-general-moved.l4`)

### DEF-M1. s 2: "and not otherwise" (lines 1240-1244)

**Taken.** The liability under the Code (`JUST TRUE`) and the "not otherwise" (`JUST FALSE` for liability under any other law) are two functions, the second a flat negative. Where the person is not guilty within Singapore, both are `NOTHING`: ss 3 to 4B extend the Code, and s 2 does not speak. Marginal reading (a).

### DEF-M2. ss 73(3), 74(3), 74A(4), 74B(4), 74C(4), 74D(4): "where no imprisonment is prescribed or where twice the maximum term ... does not exceed 5 years" (e.g. lines 2154-2160)

**Text.** A Magistrate's Court "has jurisdiction to try the offences in subsection (1), where no imprisonment is prescribed or where twice the maximum term of imprisonment prescribed for the offence does not exceed 5 years, and has power to impose the full punishment provided under that subsection".
**Taken.** One helper reads the offence's own `Punishment` record: no imprisonment prescribed (and no imprisonment for life) is `JUST TRUE`; twice the stated maximum at most 60 months is `JUST TRUE`; anything else is `NOTHING`, because the grant is limited by its own wording and does not say that a Magistrate's Court lacks jurisdiction elsewhere. The "where" is read as limiting the power to impose as well as the jurisdiction to try; the result is the same either way, since the power follows the jurisdiction. The District Court's grant is unconditional given the offence is in scope. Marginal reading (b).
**Literal reading of death alone.** An offence punished with death only prescribes no imprisonment, so the helper says `JUST TRUE`; the scope of the sections excludes such offences, which is the caller's input, not this helper's.
**Not decided.** Which offences are "in scope" of each section is an input (`the offence is one specified in subsection (2)` and its siblings); this pass does not list them.

### DEF-M3. s 53 Explanation: "caning shall be with a rattan" (line 2112)

**Taken.** `JUST TRUE` for a rattan, `NOTHING` for another instrument: the Explanation says what caning is done with, not in its own words that another instrument is not caning. Marginal reading (b); the other reading is `JUST FALSE`.

### DEF-M4. s 33(1), s 44A, s 45 to s 48, s 50, s 12, s 17, s 29A, s 51, s 86(3): "denotes", "includes", "deemed to include"

**Taken.** A definition that says "includes" or "denotes" is not closed: a case outside it is `NOTHING`. A definition that says "means" (s 42) is closed. s 49's "it is to be understood that the year or the month is to be reckoned according to the Gregorian calendar" and s 29B's "has the same meaning as in the Electronic Transactions Act 2010" are read as closed (`JUST FALSE` for another calendar, or for what that Act does not call an electronic record), each with the words quoted.

### DEF-M5. s 6A: the order of the limbs

**Taken.** An offence in neither the Code nor any other written law is `NOTHING` before the exceptions are asked; then the "dishonestly"/"fraudulently" exception and the "unless that written law expressly provides" proviso are each `JUST FALSE`; otherwise `JUST TRUE`.

### DEF-M6. The Electronic Transactions Act 2010 and the Criminal Procedure Code 2010 are not in the sources

**Taken.** s 29B's meaning, and s 3's "liable by law to be tried", are inputs. Nothing is guessed about either Act.

### DEF-M7. The scope of the jurisdiction subsections is an input, not wired to `pc-general-part.l4` (ss 73(3), 74(3), 74A(4), 74B(4), 74C(4), 74D(4))

**Text.** Each subsection gives jurisdiction over "the offences in subsection (1)" (s 73) or "any offence specified in subsection (2)" (s 74), and so on.
**Readings.** (a) take the scope from the existing `enhanced penalty under s N` predicate over the section's `... Facts` record in `pc-general-part.l4`; (b) take it as a BOOLEAN input of its own.
**Taken.** (b). For s 73, `enhanced penalty under s 73` also folds in subsection (2) ("This section does not apply where the offender proves ..."); for s 74 it also folds in the aggravation of subsection (4); the jurisdiction subsections mention neither.
For ss 74A to 74D this pass did not make the same comparison.
**Consequence.** A caller who holds the existing records must answer the scope question from the same leaves by hand; nothing ties the two together or tests them together.
