# Transport Accident Regulations 2017 (Vic): baseline encoding for the individual the Regulations are applied to

Unofficial. Copyright (c) State of Victoria; Victorian Legislation, published by the Office of the Chief
Parliamentary Counsel with the authority of the Government Printer. Encoded from a plain-text conversion of the
register's Word file; only the authorised version is evidence (Interpretation of Legislation Act 1984 s 64).
Not for public use as advice.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
It is the first encoding of these Regulations; nothing beside it was changed. The subject's indexing records of October 2026 are kept as they were.
No REFUSE, no BECAUSE except `LEST BREACH ... BECAUSE`. A question the encoding cannot answer returns `NOTHING`, and tests assert it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.

The Regulations only fill in what the Transport Accident Act 1986 leaves to them, so each question is encoded with the provision of the Act it completes. The Act has its own encoding (`../../../transport-accident-act-1986/encodings/baseline-2026-11/`), but the stable `l4` cannot IMPORT across subjects, so the provisions of the Act needed here are restated narrowly in `tar-core.l4`, each with its section and the line of the Act's deposited text: s 3(1) "severe injury"; s 60(3), (4), (5); ss 49(4), 50(4), 51(5); s 64(1), (3); s 86 (as it bears on the contract).

Three modules:

- **`tar-core.l4`**, seat-neutral: the date arithmetic (built-in date functions only, no daydate, no `YMD`), the restated provisions of the Act, and the Regulations' rules, each quoted with its line. Two duties with deadlines are regulative rules (`DEONTIC`): the statement of earnings in Form 1 (ss 49(4), 50(4), 51(5) with r 7) and the report in Form 2 (s 64(1), (3) with r 8(1)).
- **`tar-seat.l4`**, the individual's seat: 13 questions, each with `@export` and a `@desc` on every input, under `§§` headings in the order of the Regulations, situations marked. It builds the core's records from plain answers and restates no rule. No exported question takes a `DEONTIC` or `EVENT` input.
- **`tar-cases.l4`**, the cases: every exported question with its edges, and both regulative rules by `EVALTRACE`.

Victoria has no requirement ledger, so no ledger line is closed or raised.

## Edition

**Transport Accident Regulations 2017**, S.R. No. 40/2017, **Version No. 002, incorporating amendments as at 23 October 2018** (the register's current version when read on 2026-11-07), deposited at `../../registers/source-bundle/transport-accident-regulations-2017.txt` (sha256 of the text in the `.meta.json`). The owner saved the Word file by hand on 2026-11-07 from the version page; `subjects/au/vic/README.md` and the `.meta.json` record the deposit. Line numbers in the modules are lines of that text.
The one amendment is S.R. No. 177/2018 (made and in operation 23 October 2018), which substituted r 11. The r 11 it replaced is not deposited.
The endnotes (which are not part of the Regulations) say they "will sunset ... on 6 June 2027" under s 5 of the Subordinate Legislation Act 1994 (not deposited).
For the provisions restated: **Transport Accident Act 1986**, Version No. 159, as at 1 November 2026, deposited at `../../../transport-accident-act-1986/registers/source-bundle/transport-accident-act-1986.txt`.
The conversion has not been checked against the authorised PDF, which was not saved.

## Checks

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `tar-core.l4` | 0 | 0 | 0 | 0 |
| `tar-seat.l4` | 0 | 0 | 0 | 0 |
| `tar-cases.l4` | 0 | 0 | 102 | 102 |

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (2026-11-07). A copy of the case file with one expected value changed was run first, to confirm that a failure is reported (101 satisfied, 1 failed); it was not kept.
Every expected value was worked by hand from the deposited text. The edges asserted include: burns of 50% and 51% (where r 5(1)(b) meets s 3(1)(a)), and 0%; a field of 10, 10.5 and 11 degrees; an acuity of exactly 6/60 (0.1), 0.099 and 3/60, in one eye and in both; two of the three kinds of task and all three; the order of routes when more than one applies; $50 000 and $50 001 for a home, $10 000 and $10 001 for a vehicle; 22 and 23 October 2018, 5 and 6 June 2027; the anniversary, the day before it, the last day and the day after for the statement of earnings, with 29 February and 31 December first payments; the 28 days for a report across a leap February and the turn of the year; each age edge of s 64(3) (14 and 15 for driver and owner).

## Seat

**The individual the Regulations are applied to** (`tar-seat.l4`), in four situations, each a `§§` group:

- **the person injured in a transport accident**: *Is my injury a severe injury, and by which part of the definition? Is my loss of sight "permanent blindness"? If my home or vehicle must be modified, what is the most the Commission can pay without an agreement, and must I enter one before it pays this amount?*
- **the person receiving weekly payments for loss of earning capacity** (ss 49-51): *Which form, by what day, and is my statement of earnings in time?*
- **the driver, owner or owner's parent or guardian asked by the Commission to report an accident** (s 64): *Am I the one who must report, on which form, and by what day?*
- **the owner of a trailer insured with the Commission, or a person in charge of it** (s 86): *Is my contract in the prescribed form? Does it cover me for this liability? What is the most the Commission is liable for where another contract also covers the owner?*

The Transport Accident Commission gets no seat. Form 3 (the report of a train or tram operator or manager, s 64(2)) is answered only as a form in "Which form must I use"; operators get no seat of their own.

**The 2026-10-18 defaults.**

- **The Act alone, with the instruments that set its numbers.** Here the instrument is the one that sets the Act's numbers; the provisions of the Act it completes are restated narrowly (see Method).
- **The actors the text names.** Followed: the person with the injury, the person receiving weekly payments, the driver, the owner, the parent or guardian of the owner, the owner of a trailer, the person in charge of it, the Commission.
- **A judgment handed to someone else answered conditionally.** Followed. Severe disfigurement, severe difficulties in performing tasks, whether a combination of visual defects gives the same loss, the loss of the use of a limb, and the Commission's rateable proportion are inputs.
- **Definitions worked out, borrowed terms asked.** Worked out: "severe injury" (s 3(1) with r 5(1)), "permanent blindness" (r 5(2)), the s 64(3) reporter, the commencement day of r 10(2) (6 June 2017, from the endnotes). Asked: "significant acquired brain injury", "paraplegia", "quadriplegia", "amputation of a limb", "brachial plexus injury", "full-thickness burns", "recreation vehicle", corrected visual acuity on the Snellen scale (asked as the fraction's value, 6/60 = 0.1).
- **One case.** One injury; one payment; one statement for one anniversary; one notice; one liability under one contract.
- **The text's own terms with a plain gloss.** Followed; the brachial plexus gets a gloss in its `@desc`.
- **Operative provisions in; machinery out.** rr 1-4 and 6 (objectives, authority, revocation, definitions, form numbering) are machinery and are reflected only in the forms function.

## Scope

**In:** r 5(1), (2) with Act s 3(1); r 7 with Act ss 49(4), 50(4), 51(5) and Form 1 (the particulars it asks for are a core list and are named in the forms question); r 8(1), (2) with Act s 64(1)-(3) and Forms 2 and 3 (as forms); r 9 and Form 4 cll 2, 3 with Act s 86; r 10 (transitional); r 11 with Act s 60(3)-(5). That is the whole of the Regulations' operative text.

**Out, and why:** rr 1-4, 6 (machinery); the content of Forms 2 and 3 (blank forms; nothing turns on a field); Form 4 cl 1 (definitions, used in the questions' wording); Form 4 cl 2(2)(a) "subject to Part 5 of the Transport Accident Act 1986" (Part 5 is s 86, whose own limits, s 86(2)(c) and (3), are not restated; cl 3(1)(a) carries the workers' compensation exclusion); Act s 60(4A), (4B), (6) (the Commission's factors and the agreement's contents); Act ss 65, 66 (the $50 penalty, named in the report rule's breach reason; the Act's encoding has them as a rule).

## Negatives and legal effects

This row follows the corpus convention in `docs/ENCODING-GUIDE.md` section 5, "Rulings on negatives and legal effects" (2026-11-04 and 2026-11-05): a function answers `JUST FALSE` only where the text itself says no to the case in its own words, and `NOTHING` elsewhere. Questions that can only be answered yes or no by the text are typed `BOOLEAN`. In this row:

- **No (`FALSE` or `JUST FALSE`):** "severe injury" and "permanent blindness" (each a "means" definition, the first closed by the Regulations' list); the statement of earnings and the report outside their periods; s 64's designation of who reports; r 10 (a contract neither in Form 4 nor carried over); the agreement question when the payment does not exceed the amount (fork line 5); Form 4 outside the period of cl 2(2)(b) and under each exclusion of cl 3(1) ("does not indemnify").
- **`NOTHING`:** the modification amounts outside 23 October 2018 to 5 June 2027 (the replaced r 11 is not deposited, and the sunset points outside the sources); Form 4 for a case outside the grant of cl 2(1) (not the owner or a person in charge; not a death or injury from the trailer's use in Australia).

**Fork lines** (case-by-case decisions under the ruling of 2026-11-05, for the reviewer to overrule):

1. r 5(2), `r 5(2) -- is permanent blindness`: the "means" definition has no element of permanence, so a measurement meeting (a), (b) or (c) is enough. Other reading: "permanent" in the defined term adds that the loss must be lasting.
2. r 5(1)(b), `r 5(1)(b) -- burns that are a severe injury`: burns that "comprise of full-thickness burns ... to the head, neck, arms or lower legs" read as burns that include full-thickness burns there. Other reading: all of the burns must be full-thickness (and, for (i), all at those sites).
3. r 5(1)(b)(ii), the same function: "severe difficulties in performing mobility, communication and self-care tasks" read as difficulties with all three. Other reading: with any of them.
4. Act s 60(5) with r 11, `s 60(5), r 11 -- the most without an agreement`: "a payment or contribution ... which exceeds" is read one payment at a time. Other reading: the payments for one modification (or all of them) are added together.
5. Act s 60(5), `s 60(5), r 11 -- an agreement is needed for the payment`: a payment that does not exceed the amount gets `JUST FALSE` (s 60(5) asks no agreement). Other reading: `NOTHING`, as the "unless" is unmet and the text is silent.
6. Act ss 49(4), 50(4), 51(5), `ss 49(4), 50(4), 51(5) -- the statement is given within the two months`: a statement given before the anniversary is not given "within two months after" it. Other reading: an early statement is in time.
7. Act s 64(1)(a), (b), (3)(a), (b), `s 64(1), (3) -- I am the one who must report on a notice`: with no one injured or killed (or entitled), the duty does not reach the person (`FALSE`). Other reading: `NOTHING`, the case being outside the section.
8. r 11 and the endnotes, `r 11 -- the deposited version applies on`: the Regulations are read as in force to 5 June 2027 and not on the sunset day, 6 June 2027. Other reading: in force on 6 June 2027.
9. Form 4 cl 3(1)(c), `Form 4 cl 2, 3(1) -- the contract indemnifies against the liability`: the exclusion is read in its own words, so the input asks whether the trailer was registered "in Victoria under the Interstate Road Transport Act 1985 of the Commonwealth" (finding 4). Other reading: registration in Victoria under any law.

## What the Regulations turn out to say

1. **r 11 is headed a "limit", but s 60(5) makes it a threshold.** The heading reads "Prescribed limit for home modification payment by the Commission", but s 60(5) does not cap the payment: it bars a payment over the amount "unless the person enters into an agreement with the Commission" about ownership and maintenance. Above $50 000 the Commission can still pay, with the agreement. Asserted ($50 001 needs the agreement).
2. **Only the home got the higher amount.** r 11 prescribes $50 000 "for the purposes of section 60(4)". Nothing is prescribed for s 60(3), so a vehicle modification or contribution over $10 000 still needs the agreement. Neither amount is indexed: $10 000 is not in the s 61(2) list (Act line 2092), and the prescribed amount is not an amount "referred to in this Division". Asserted ($20 000: an agreement for a vehicle, none for a home).
3. **Burns meet at 50% with no gap.** s 3(1)(a) takes "burns to more than 50% of the body"; r 5(1)(b) takes burns "to not more than 50%" with severe disfigurement and full-thickness burns at the listed sites or with severe difficulties. At exactly 50% only r 5(1)(b) can apply. Asserted (50% with nothing more: not severe; 51%: severe).
4. **The trailer contract excludes every period in which the trailer is not registered "in Victoria under the Interstate Road Transport Act 1985 of the Commonwealth".** Read literally, a trailer registered only under the Road Safety Act 1986 (Vic) is never covered, while s 86(2)(a) keeps the contract in force "for the period for which the registration of the trailer remains in force". The clause may be a relic of the federal interstate registration scheme; whether that Commonwealth Act is still in force was not checked (it is not deposited). The question asks the clause's own words (fork line 9). Asserted.
5. **The rateable proportion has no method.** Form 4 cl 3(2) limits the Commission to "its rateable proportion" where another contract covers the owner for the same liability, but gives no way to work it out, and the contract states no limit of cover from which a proportion could be drawn. It is an input. Asserted (a half, a third).
6. **The rateable proportion is triggered only by cover of the owner.** Another contract covering the person in charge of the trailer (not the owner) does not bring cl 3(2) into play, though cl 2(1)(b) indemnifies that person too.
7. **Permanent blindness need not be permanent.** r 5(2) defines the term by measurement alone (fork line 1). Asserted on the definition's terms.
8. **The Regulations do not set everything the Act leaves to them.** Version 002 prescribes nothing for the s 47(4) periodic payments ("calculated in accordance with the regulations"), s 46A(6) (psychiatric impairment, "subject to any regulations"), or s 60(7)(e) (further things the Commission is not liable for, "specified by the regulations"). The Act's encoding listed these Regulations as wanted for some of them; they do not supply them.
9. **The Regulations sunset on 6 June 2027** (endnotes), so r 5's further severe injuries, the forms and the $50 000 lapse then unless remade or extended. Asserted as `NOTHING` from that day (fork line 8).
10. **Form 3 names an "MTA officer"**, a name of a former Victorian transport authority. Not encoded; noted for the reviewer.

## Before relying on it

- Check the conversion against the authorised PDF.
- Deposit the r 11 that S.R. No. 177/2018 replaced, and the Transport Accident Regulations 2007 r 10 form, to answer before 23 October 2018.
- After 6 June 2027, deposit the remade Regulations, if any.
- An independent test pass, and a lawyer's review of the fork lines and findings, especially finding 4.

## Read with

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here, not in code.

- **Transport Accident Act 1986** (`../../../transport-accident-act-1986/encodings/baseline-2026-11/`), the parent Act. Its `Severe injury head` has a head `an injury specified by the regulations`, asked as a fact; the questions here answer it. Its s 64 and ss 49(4), 50(4), 51(5) rules say "the prescribed form"; r 8(1) and r 7 make that Form 2 and Form 1. Its s 54A safety net question takes a severe injury as an input.
