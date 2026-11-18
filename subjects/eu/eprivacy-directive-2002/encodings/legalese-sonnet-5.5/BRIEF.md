# Encoding brief: the ePrivacy Directive (Directive 2002/58/EC), consolidated version of 19.12.2009, whole, in L4 (stable)

You are producing a full L4 encoding of the ePrivacy Directive (Directive 2002/58/EC), consolidated version of 19.12.2009 (Directive 2002/58/EC of the European Parliament and of the Council of 12 July 2002 concerning the processing of personal data and the protection of privacy in the electronic communications sector, as amended by Directive 2006/24/EC and Directive 2009/136/EC; the Publications Office consolidated version of 19.12.2009) from the English-language text deposited in `INPUTS_DIR`.
This brief is the whole specification. Read it fully before opening any source.
You are the ONLY encoder: no ontology agent, no fleet, no integrator, no independent test author, no subagents. You do all of it in one context and check your own work with the diagnostics.

## What you are building: two layers

**Layer 1: the law, objectively.** The whole text, as isomorphic and tested L4 modules that follow the text's own structure (one module per Part or natural group, a nouns module first if you need one). It is written from the text alone and takes nobody's point of view: a reader holding the text beside a module checks it line by line, and every rule carries a source citation.

**Layer 2: one thin seat layer over it.** Commons requires every Act to be asked about from the position of the individual to whom the law is applied (the "seat"), because the Legalese website turns such a layer into a question form.
Here the seats are (the first is the individual, and is required):
- `epd-seat.l4` / `epd-cases-seat.l4`: **an individual who uses or subscribes to a publicly available electronic communications service (a telephone, mobile, internet or messaging service), or who receives unsolicited marketing messages, or whose device a website or app stores information on, asking on facts they can state what the Directive gives them (confidentiality of their communications, how their traffic and location data are handled, itemised bills, calling-line identification, call forwarding, directories, consent and objection to marketing and to cookies) and what they can do if it is not respected.**
- `epd-seat-provider.l4` / `epd-cases-seat-provider.l4`: **a provider of a publicly available electronic communications service or of a public communications network, asking on facts it can state what the Directive requires of it (security and breach notification, confidentiality, erasure or anonymisation and consented use of traffic and location data, billing and itemisation, calling-line identification and its restriction, call forwarding, directories, and what it may be penalised for).**
- `epd-seat-sender.l4` / `epd-cases-seat-sender.l4`: **a person or business that sends electronic communications for direct marketing (by automated calling systems, fax, e-mail or the like), or that stores information or gains access to information in another person's terminal equipment (for example with cookies), asking on facts it can state whether it needs the recipient's consent, whether an exception applies, what it must give and keep, what is forbidden outright (concealing the sender's identity), and what it can be made to answer for.**
Each seat layer is its own pair of files (a seat module and a cases module). It IMPORTs the layer-1 modules and calls their rules; it never restates a rule, and no layer-1 module changes to suit it.
Each question has `@export` and `@desc`, takes plain inputs (one per fact the person can state, each `@desc` worded as that person would be asked), and the questions are grouped under `§` headings in the text's natural order.
Read `inputs/ENCODING-GUIDE.md` sections 2, 3, 4, 5 and 9 and `inputs/COMMONS-CLAUDE.md` before you write any L4. `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4` is a finished seat layer for a different Act and shows the shape (it imports modules you cannot see; copy its shape, not its content).
Questions are phrased as the person asks them ("Must I ...?", "Am I entitled to ...?"). Provisions that address only an official are encoded in layer 1 for what they decide, and in layer 2 only for what they mean to the person. There is never a seat for an official.

## What "whole" means (the maintainer's ruling of 2026-10-22, applied to this Act)

Every provision of the text, that is every section, subsection, paragraph, schedule, table row and defined term, has a row in the coverage table, and each row has exactly one disposition:
- `encoded`: a rule, definition or table in layer-1 L4, with a test, citing the provision with `@ref`.
- `inert`: allowed ONLY for the three reasons below.
- `fork`: the text can be read two or more ways with different outcomes. The row points at the fork-register entry (every reading, and the text that licenses each) and at the rule that encodes the chosen reading, or at the explicit "not covered" value when the text does not choose.
- `repealed or blank in this text`: say what the text shows.

There is no `out-of-scope` row and no `deferred` row.

The three reasons for `inert`, and no others:
1. Not operative: the title, long title, enacting words, headings, the date of enactment, a purpose or objects clause that creates no rule.
2. Machinery (Guide section 4): boards and offices and their staffing, the Act's own commencement, short title and extent, regulation-making and rule-making powers, savings and transitional provisions that affect no one now, amendments of other Acts.
3. Text shown repealed or blank.

These are NOT reasons. Earlier passes used them and they no longer stand:
- "addresses an official": encode what it means for the individual: what may be done to them, what they must be given, and by when (Guide section 2).
- "an interpretive canon" or "open-textured": encode the rule, and take the open-textured judgment as a plain input.
- "refers to another Act or instrument that is not among the sources": encode the provision as stated and ask the borrowed fact or term as an input (Guide section 4).
- "no input from which an answer would differ": a rule with one answer is still a rule; encode it and test it.
- "the earlier brief said it need not be coded": superseded by this brief.

A definition is encoded: a defined-term table or function that returns the term's meaning as the Act states it (the members it names, what it includes or excludes, what it points at), with a test for each entry.
Rules of reading (the singular includes the plural; a reference to an Act includes amendments; and so on) are encoded as functions over a small typed representation of what the rule operates on, as an existing module of this family does, with tests on both sides of each limb.



## About this row

- **The text**: `eu-eprivacy-2002-58-consolidated-20091219.txt`, 5,291 words with its header: Articles 1 to 21 of the Directive. It is the Publications Office consolidated version of 19.12.2009 (a documentation tool, not the authentic text). The lines `▼B`, `▼M1`, `▼M2` (with INSERTED, REPLACED, DELETED) mark which instrument each block comes from: `▼B` the Directive of 2002, `▼M1` Directive 2006/24/EC, `▼M2` Directive 2009/136/EC. **The text after a marker is the text in force**; a block marked DELETED has no text. Recitals are not part of the file.
- **Whole means every Article, every paragraph and every list item**, including the provisions that bind only Member States or the Commission (Articles 14 to 21: technical features and standardisation, committee procedure, application of certain provisions of Directive 95/46/EC, implementation and enforcement, transitional arrangements, transposition, review, repeal, entry into force, addressees): the coverage table has a row for each, and each is encoded or `inert` under one of the three reasons.
- **A directive binds Member States, not people.** The text says "Member States shall ensure that ...": encode it as what the Directive requires the national law to give or impose on the person in the seat ("the Directive requires that I can ..."), and say in NOTES that this row answers what the Directive requires, not what any one Member State's transposing law says or whether a provision has direct effect. Where the text speaks of a provider ("the provider must ..."), the duty is the provider's. This is the whole directive, not only the marketing rules.
- **Article 13 (unsolicited communications) is to be fully encoded, on two seats.** Each of its paragraphs 1 to 6, and every limb and list item inside them, has coverage rows and is encoded; each is asked from the sender's seat (`sender`) and from the recipient's seat (the individual). Write mirror cases: the same message and the same facts asked from the sender's seat and from the recipient's seat, with answers that agree. Where the text gives a power to a court or a competent national authority (Article 13(6), Article 15a(2) and (3)), ask it in the person's own terms, as the Guide requires: the sender asks "may I be ordered to stop, or penalised?", the individual asks "what must the Member State's law let me do about this message?". A question that a person's seat cannot answer is a fork-register entry, not a dropped provision.
- **Three seats**, in this order: the individual, the provider, the sender. All three are required.
- **Cross-references to texts not among your sources**: Article 2 defines by reference to Directive 95/46/EC and Directive 2002/21/EC; `consent` "corresponds to the data subject's consent in Directive 95/46/EC". Neither is in your sources: take every borrowed definition as an input the person states (a fact, a yes/no), and make a fork-register entry that the consolidated text of 2009 still names them. One fact is outside the text and the lead states it: the Publications Office's own data lists Directive (EU) 2018/1972 as repealing Directive 2002/21/EC. Whether the Directive's terms now read as the terms of 2018/1972 is NOT decided here: record it as a fork, answer `NOTHING` where it matters, and do not import the later instrument. Regulation (EU) 2016/679 (the GDPR) is not among your sources and its scope is not decided in this row: where Articles 1(2), 2, 15 and 15a mention Directive 95/46/EC, do not encode the later regulation.
- **Article 15(1a)** was added by `▼M1` (Directive 2006/24/EC, data retention). The text of the Directive is encoded as the file states it. The lead notes, from outside your sources and unchecked against your text, that a Court of Justice judgment of 8 April 2014 (Joined Cases C-293/12 and C-594/12) declared Directive 2006/24/EC invalid; the file says nothing of it. Encode Article 15(1a) as printed, and record under the fork register, flagged `from outside the sources, stated by the lead`, that its reference may no longer have effect. Do not leave the paragraph out.
- **Time**: the Directive is encoded as in force in the consolidated version of 19.12.2009. Article 17's transposition dates and Article 16's transitional rule are the text's own: encode them and test both sides, as for any dated rule.
- **Amounts, periods and thresholds the text leaves to the Member States** (penalties, the length of time before traffic data are erased, the form of consent) are INPUTS or `NOTHING`; do not use a number from memory.
- **Naming**: a function's name carries the provision in this form: `Art 13(2) the soft opt-in applies`.

- **Seats.** This row has 3 seats, listed in the section above; the individual comes first and is required.
- Each seat has its own two files; the seats keep their own names (two seat modules must never define the same name). Questions are phrased as that person asks them. Where the Act gives the two seats the same relation from opposite sides, write MIRROR cases: the same facts asked from both seats, with answers that agree (Guide section 3).
- Never a seat for an official or the government: not the regulator, the court, the department, the police or a minister (Guide section 2). What a court, authority or Member State must or may do is encoded for what it means to the person in the seat, in the person's own terms ("may I be ordered ...?", "what must I be given ...?").

## What FALSE and NOTHING mean in your answers (the rule of 2026-10-29; assumed, not ruled by a lawyer)

This rule is in force for every row the family has filed since 2026-10-29. Follow it exactly, and flag, do not decide, the two readings marked "for a lawyer".
- A decision function answers `JUST FALSE` (a `BOOLEAN` that is `MAYBE`-wrapped), or a constructor whose meaning is "the text says no" (for example `Not entitled`, `Not barred`, `Not obliged`; choose your own descriptive names), **only** where the text itself says no to the case in its own words: a definition that says "means"; a condition the text introduces with "if", "only if", "as long as" or "unless" (and their plain variants: "so long as", "while", "until", "except", "save", "provided that"); a list the text closes with "only" or "nothing but"; a flat negative ("does not", "shall not", "may not", "is not entitled").
- Everywhere else the function answers `NOTHING` (a `MAYBE` result) or a named "... not covered" constructor: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points to a power, regulation, rate or authority outside your sources, or limits a grant or prohibition in its own wording ("without", "against the will of", "when", a stated period, a named complement) and the case falls outside the limit.
- Every branch that answers a "no" carries a comment `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`, and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)` where <why> is one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- The function's name carries the section it implements, in this form: `s 47(2) the instrument is valid`, `s 4(2)(a) the claimant has reached the qualifying age`, `sch 3 para 2 the amount is reduced` (the Act's own numbering; parentheses inside a backtick name are fine on the stable binary, checked). Not `is the instrument valid`, not `may I ...`: the name must not claim more than the section says. A caller must never turn `NOTHING` into `FALSE`.
- **For a lawyer, not for you to decide:** (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not. Take these readings as the status quo, and list every branch that rests on one under a heading `## Marginal readings for a lawyer` in `NOTES.md`, with the other reading stated.
- Put a short section `### Reading a result: FALSE and NOTHING` in `NOTES.md` saying this in your own subject's terms: what a "no" is in this row, and what "not covered" is.
- `REFUSE` does not exist on the stable binary: "not covered" is `NOTHING` or a constructor, asserted.

## Rules, duties and decision functions

The text says who is entitled to what, who must do what by when, and what follows. Encode it the way it reads, provision by provision, choosing the form closest to the words:
- a **decision function** (a typed `DECIDE`) where the provision fixes a sum, a rate, a rank, an entitlement, a condition for a lawful act, a period, or a list of who is covered;
- a **regulative rule** (`PARTY ... MUST / MAY / SHANT ... WITHIN ... HENCE ... LEST ...`, see `writing-l4-rules/references/regulative.md`) where a provision imposes a duty, permission or prohibition on a named party, with its time limit and consequence if the text gives them.
Both are tested. A regulative rule is run (`#TRACE` / `#EVAL`) and you assert what you can assert on the stable binary; if some regulative construct cannot be asserted on it, say so under "What the stable binary does not accept" and also encode the same duty as a decision function over the facts.
Do not invent an actor, a deadline, a remedy or a consequence the text does not state: where it does not say who decides, by when, or what follows, say so in the fork register and return a "not covered" value.
Amounts, rates and thresholds the text leaves to regulations, orders or a Minister are INPUTS (a number the person states), asked with an `@desc`; never a number from memory.
Dates are `Date day month year`; a period measured in days, weeks, months or years is a function with a test on both sides of its end.

## Rights and duties come in pairs (Hohfeld)

Hohfeld's correlatives: the person's right (a claim) is the other party's duty; the person's privilege (a liberty) is the other party's no-right; the person's power is the other party's liability, that is, being subject to that power (not an obligation); the person's immunity is the other party's disability.
In layer 1, state each rule once, as a relation between two parties, and name it neutrally; never write the same relation twice, once from each side.
In `NOTES.md` keep a section `## Jural relations`: a table with one row per provision that creates a relation, giving the party holding the right, privilege, power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section, and the L4 rule that encodes it. A provision that creates no such relation (a definition, a counting rule) is listed once as `none`. Most provisions of this text DO create a relation (a person against the authority or court that acts on them, a director against the company, one party against another), so this section is long; it must cover the whole of your range.

## The subject and the sources

- **the ePrivacy Directive (Directive 2002/58/EC), consolidated version of 19.12.2009**, Directive 2002/58/EC of the European Parliament and of the Council of 12 July 2002 concerning the processing of personal data and the protection of privacy in the electronic communications sector, as amended by Directive 2006/24/EC and Directive 2009/136/EC; the Publications Office consolidated version of 19.12.2009.
- Source file(s) in `INPUTS_DIR`: `eu-eprivacy-2002-58-consolidated-20091219.txt`.
- `inputs/SOURCES.md` records where each came from, its version, its URL and its hashes. **Read it.**
- Each text is a plain-text rendering made by a converter script; it is not the official text. Say so in `NOTES.md` and in your `SOURCE-LICENSE.md`, and do not claim anything is "verified against the official text".
- `inputs/STUB-SOURCE-LICENSE.md` is the subject-level licence note written when the text was deposited. Your `SOURCE-LICENSE.md` points at it and does not repeat it.
- Encode only from these files. Quote the text mechanically (copy it, or script it as long as the script reads the file); never reconstruct wording from memory.
- Defaults ruled for Commons (Guide section 4): the Act alone, plus instruments that set its numbers or dates if among your inputs, otherwise make the number an input and say so; the actors the text names; a judgment the text hands to someone else becomes a conditional input and is never guessed; the Act's own definitions are worked out from facts, borrowed terms are asked as facts; one case is the text's natural unit; the Act's own words, each with a plain gloss in a comment.
- Build the coverage table from the text itself with a script, one row per section, subsection, schedule paragraph, defined term and table row, and check that every non-blank line of the text falls in some row.

## Writing L4 that the stable binary accepts (from the Commons guide, section 5, verbatim)

- **No `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`** (except `LEST BREACH … BECAUSE`, which is accepted). For a case outside the encoding, return an explicit "not covered" value, either a constructor or `NOTHING`, and assert it.
- **Parenthesise every `NOT`.** `NOT a AND b` parses as `NOT (a AND b)`.
- **Keep each `#ASSERT` on one line.** A continuation line is rejected.
- **Bracket arithmetic that crosses a line break.** `x DIVIDED BY w` at the end of a line, followed by `TIMES 100` on the next, divides by `w × 100`. Chained `MINUS` is left-associative.
- **`IMPORT` finds only modules in the importing file's own folder** (and the libraries). One encoding cannot import another from a different subject, and a file in a `cases/` subfolder cannot reach the modules above it. A name defined in two imported modules cannot be used at all. Cross-encoding links go in `docs/au-baseline-links.md` style registers, not code, until the language allows them.
- **Dates: write `Date day month year`, and never define a `YMD` of your own.** `Date` (from `IMPORT daydate`) is in every build. Unstable builds have had a year-first `YMD` in daydate since 29 July 2026, and it is proposed for the stable line (legalese/l4-ide#768, not landed); a file that imports daydate and also defines `YMD` then fails with "There are multiple definitions for the identifier YMD", and so does every file that imports it. Earlier encodings followed this guide's old advice to add a `YMD` shim; on 29 October 2026 the shim was renamed `YearMonthDay` in the 50 files that define it and the 809 others that call it, so that the collision no longer stops them (checked on 29 October 2026 over those files and every file that imports them: no file that checked before fails after, on stable 1.6.98, on unstable-20261028-5e95b5a, or with the daydate of #768). Keep `YearMonthDay` where an encoding already uses it, and do not start a new encoding with it. `Date` and the shim roll an impossible date forward (`Date 29 2 2023` is 1 March 2023); daydate's `YMD` refuses it. When a stable `l4` ships `YMD`, the shims are to be deleted and `YearMonthDay` renamed back. **Smaller gaps:** `WAIT UNTIL` is spelled `WAITUNTIL`. `TYPICALLY` on a record field is not accepted.
- **`@export` and `@desc` on every question** in a seat or baseline. Legalese Cloud publishes those, and the website's Interact form asks them.
- **Expected values are hand-written from the text,** never copied from the encoding's own output.
- **Checks before committing:** `l4 run` on every file shows no `DiagnosticSeverity_Error` or `_Warning`, and every case file has assertions written equal to assertions satisfied. A test that fails on purpose is allowed only where NOTES.md records it as a finding, as the HVAC worked example does.

### Rulings on negatives and legal effects (ruled 2026-11-04)

These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.
The rule of 2026-10-29 for what `JUST FALSE` and `NOTHING` mean is the convention the rows written since then follow (applied in legalese/commons#30 and #37); it was assumed, not ruled as a whole, and the rulings below settle parts of it.
In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.
- **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The ruling sets three limits:
  1. answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed;
  2. keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question;
  3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it).
  The ruling and the counts it produced are recorded in `subjects/uk/companies-act-2006/encodings/legalese-sonnet-5.5/NOTES.md`, section "The grant and power name test".
- **Lists:** write a list of strings as a vertical `LIST` block, one string per line, not with `•` bullets (those are a parse error on the stable binary).

Your binary is the stable build, so anything it rejects is not available to you. Where the skills describe a construct the stable binary rejects, the binary governs; say so in `NOTES.md` under the finding "What the stable binary does not accept".
## Deliverables, all under your `DEPOSIT` directory (given in your task)

```
DEPOSIT/
  encodings/legalese-sonnet-5.5/
    epd-*.l4            layer 1: every module of the law (flat folder: IMPORT finds only modules beside it)
    epd-seat.l4                layer 2: the individual seat's questions
    epd-cases-seat.l4          layer 2: worked cases, one per question at least
    epd-seat-provider.l4       layer 2: the provider seat's questions
    epd-cases-seat-provider.l4 layer 2: worked cases, one per question at least
    epd-seat-sender.l4         layer 2: the sender seat's questions
    epd-cases-seat-sender.l4   layer 2: worked cases, one per question at least
    tests, check.sh, srcrefs.py, NOTES.md, PROGRESS.md, encoding.json, SOURCE-LICENSE.md, BRIEF.md (a copy of this brief)
```

All `.l4` files sit directly in that folder (no subfolders), have ASCII filenames beginning with `epd-`, and never define the same name as another module imported with it.
You do not write `subject.json`, `README.md` or `source/`: the subject already exists and is not yours to change.
`encoding.json` and `SOURCE-LICENSE.md` follow `references/canon-deposit.md` of the `encoding-a-subject` skill: status `draft`, `not_reviewed` saying no domain expert has read it against the text, `"seat": "<the seat in one line>"`, the scope and the edition encoded, the checks run, and the `l4_bin` path with its sha256.
The encoding's name is `legalese-sonnet-5.5`; the method is a single Sonnet 5.5 agent working alone from this brief.
`NOTES.md` carries: a `## Seat` section naming the seat and why; the `## Jural relations` table; what is encoded and what is not; the coverage table; a **fork register** (every ambiguity, the readings you saw, the one you took, the text that licenses each); numbered findings ("What the text turns out to say"), each ending "Asserted." where a case asserts it; what the binary does not accept; what `check.sh` prints; what would need doing before the encoding is worth relying on.

## Your context will be compacted: make the disk your memory

This run may exceed your context window, and the harness will then compact your context into a summary. So write as you go, not at the end:
- Keep `NOTES.md`'s coverage table and fork register on disk, and update them after each section you finish.
- Keep `PROGRESS.md`: sections done, in progress, next, decisions taken (with the section that licenses each), and the files you have written.
- After any compaction, re-read `PROGRESS.md`, `NOTES.md` and the text, not your summary of them.

## Tests

Expected values come from the text, never from your code, and are written beside the assertion.
Decide each expected answer by reading the section, write it down, then run. A failing assertion is a finding: never edit an expected value to match what the code computed.
Cover at least: every branch of each rule you encode; the boundary values on each side of every threshold; every question in the seat layer (if the row has one), with the facts a real person in the seat would state; and a case outside the encoding (an explicit "not covered" value, asserted).
If you keep some expectations meant to fail, put them in their own file, count them, record them in `NOTES.md` as a finding, and list them in `check.sh`'s `expected_failed`.
Every case file ends with assertions written equal to assertions satisfied.

## Rules that matter

- **Follow the two skills.** Read before writing any L4: `<scratchpad>/skills/encoding-a-subject/SKILL.md` (steps 1 to 7, 9 and 11; there is no step 8 here, and you do not deposit into a repository) and `<scratchpad>/skills/writing-l4-rules/SKILL.md`, then its `references/drafting-patterns.md`, all of `references/source-patterns/`, and `references/dialects.md`.
- **Encode isomorphically.** Cite the section on every rule with `@ref`; follow `encoding-a-subject/references/source-locators.md` for quoting and run `python3 -I srcrefs.py check --refs <the raw text file> <your .l4 files>`; it must report 0 problems.
- **Where the source does not answer,** return an explicit "not covered" value (a constructor or `NOTHING`) and assert it. Never `FALSE`, never `0`, never a plausible default.
- **Read the DIAGNOSTICS, not the exit code.** `l4 run` exits 0 when an `#ASSERT` fails. Report the numbers `check.sh` prints.
- **Every file runs clean:** `l4 run` shows no `DiagnosticSeverity_Error` or `_Warning` on any file except a registered, deliberately failing one.
- **No sleep-polls and no waiting loops**: run each command in the foreground.
- **Do not git add, commit or push anything.** Write files only under `DEPOSIT`.

## Toolchain

The binary is `L4_BIN` (given in your task; version 1.6.110 (main, e51181d, 2026-11-11), sha256 `9c7656f74151383da2c7344ad53269a8754bd874af8eb513180d61dc145016c7`). Leave `JL4_LIBRARY_PATH` UNSET: the standard library is compiled into the binary and always matches it.
`L4_BIN check FILE` typechecks; `L4_BIN run FILE` also evaluates every `#EVAL` and `#ASSERT`. Run the binary by its absolute path.
Run the check as `L4=<L4_BIN> L4_MAIN=<scratchpad>/bin/l4-main-109 ./check.sh` (the default target `main`: it runs every module with a second stable build as well and goes red when the two read it differently).

## Independence

Do not read any existing encoding of any Act: nothing under `<local path>`, `<local worktrees>` or `canon`, no directory under `<scratchpad>/runs` other than your own `dst-epd/`, and nothing under `<local tool>` (no `memory/`, no `projects/`, no `state/`, no `tmp`).
The one exception is `inputs/EXAMPLE-sg-employment-act-seat/`, which is yours to read.
The answers must come from the text alone. Do not use WebFetch, WebSearch, curl or any other way to reach the web, and do not look for any other formalisation, encoding, program or model of this text in any language or tool: a published one may exist, and yours must be made from the text, the two skills and the Guide alone. You may read `INPUTS_DIR`, the two skills and their references, and the Commons guide copies in `inputs/`.
Your context may contain an index of someone's notes that mentions other encodings; do not follow it. If you open a forbidden file by accident, stop reading it and say so under `peeked`.

## Final report (your last message; the report is your final response, not a file)

Return: (1) the list of files you wrote or changed; (2) exactly what `check.sh` printed, and the baseline numbers it replaced; (3) the coverage table summary (counts per disposition) and the audit counts (text units counted, rows in the table before and after); (4) the forks you took, one line each with the reading chosen; (5) every row you moved out of `inert` and every row you left `inert` with its reason number (1, 2 or 3); (6) any failing or refused assertion and what it means; (7) what the text does not answer; (8) `peeked`: nothing, or what you opened by accident.
Subagents cannot write report-named files such as `FINDINGS.md`; `NOTES.md`, `PROGRESS.md` and `.l4` files are fine.
