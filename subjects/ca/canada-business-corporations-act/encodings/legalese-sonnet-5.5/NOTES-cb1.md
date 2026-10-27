# NOTES -- the Canada Business Corporations Act (R.S.C. 1985, c. C-44), piece cb1

Written by the piece agent cb1 (Sonnet 5.5) on 2026-10-22.
This is the report for piece cb1: the title and section 1, the rest of Part I (application: s 3 and s 4), Part II (incorporation), Part III (capacity and powers), Part IV (registered office and records), Part V (corporate finance) and Part VI (sale of constrained shares).
The ranges are lines 1-12 and 115-693 of `R.S.C.-1985-c.-C-44.txt`.
`src:N` in this folder means line N of that text file.

**What the text is.**
The text is a plain-text rendering, made by a converter script, of the Department of Justice Canada consolidation current to 2026-09-30 (last amended 2026-03-26), English version only.
It is not the official text and it is not marked up.
The French version is equally authoritative and was not read.
Nothing here is verified against the official text, and no claim is made that it is.
Contains information licensed under the Open Government Licence - Canada.

**What the files are.**
Layer 1 is the law, objectively: nine modules named `cb1-*.l4` that follow the Act's own structure, plus `cb1-nouns.l4` for the few nouns two modules share.
Layer 2 is one thin seat layer, `cb1-seat.l4` (the questions) and `cb1-cases-seat.l4` (worked cases, at least one for each question).
`cb1-tests-*.l4` test layer 1 module by module, with expected values written from the text.
Every file imports only `prelude`, the keel's `cbca-core*.l4` modules, and other `cb1-` modules; no file imports another piece's module.

**Target and binary.**
The target is `main`; the binary is the stable build `l4` 1.6.98 (`1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44ad...263e`), run with `JL4_LIBRARY_PATH` unset.
Nothing is written that the dialects page says `main` rejects; the section "What the stable binary does not accept" says what I met.

**Dates.**
My ranges hold no date of enactment, assent, or commencement.
Lines 1-12 are the converter's note, the title, the chapter citation (R.S.C., 1985, c. C-44) and the short-title section.
The text gives the consolidation currency date (2026-09-30), which dates the text and not the Act, so it is not carried as a value.
Two provisions turn on "the day on which this [sub]section comes into force" without giving the day: s 10(1.1) (the day the subsection came into force) and s 29.1(2) (the coming into force of the section).
Each is taken as a plain BOOLEAN input (the corporate name, or the certificate, was as the subsection says "immediately before" or "before" that day) and the day itself is not guessed.

**Conventions followed.**
The keel's naming conventions (KEEL-NOTES.md, "Naming conventions") are followed: a rule is named `<what it decides> within s N`, a fraction is written with `%`, money is a NUMBER of dollars, a case the text does not answer is a `MAYBE` with `NOTHING` or a named constructor.

## Seat

**The seat is a person who incorporates, directs or holds shares in a corporation under the Canada Business Corporations Act:** an incorporator, a director or officer, or a shareholder (including a minority shareholder), asking what the Act lets them do, what it requires of them, what they may require of the corporation, and what can be done to them.
That is the seat the brief rules for this Act (Commons ruling of 2026-10-18: the individual to whom the law is applied, never the regulator, the court or the Director).
Why this seat for Parts I to VI: they are the Parts a founder meets first (s 5 to s 14: who may incorporate, the articles, the certificate, the name, a contract signed before the corporation exists), and then the Parts a director and a shareholder live under (s 19 to s 23: the registered office, the records, what a shareholder may examine and be given, the register of individuals with significant control; s 24 to s 45: shares, stated capital, buying shares back, dividends, shareholder immunity; s 46 and s 47: a sale of constrained shares).

**Other parties.**
The corporation is the party most duties fall on, and a director or officer answers for it (s 21.4, s 32(4)).
The seat asks those duties from the person who must see to them: "Must my corporation ...?", "Have we ...?".
No seat is written for the Director appointed under s 260, the court, the Minister, the Governor in Council, the Financial Transactions and Reports Analysis Centre of Canada or an investigative body.
Their powers and duties (s 8, s 11, s 12, s 13, s 21.21(3), s 21.301 to s 21.303, s 21.31, s 21.32) are encoded in layer 1 for what they decide, and appear in layer 2 only as what the person is owed or exposed to (for example the certificate of incorporation the incorporators are owed, or whether the Director may refuse it).

**How the questions are written.**
Each question has `@export` (the question, with the provision in brackets) and `@desc` on every input (worded as the person is asked).
Inputs are plain facts: yes or no, a number, a date, a choice from a list.
The questions are grouped under `§` headings in the Act's order.
Where a group only arises in a situation the person may not be in (an investigative body's request, a sale of constrained shares, a court application), the heading's comment says so.

**What the seat layer is made of.**
`cb1-seat.l4` holds 217 questions in 12 `§§` groups, in the Act's order: whether the Act applies (4); incorporating, s 5 to s 9 (9); the corporation's name, s 10 to s 13 (23); a contract made before the corporation exists, s 14 (4); what the corporation can do, s 15 to s 18 (8); registered office, records and who may see them, s 19 to s 21 (27); individuals with significant control, s 21.1 to s 21.4 (29); form of records and the corporate seal, s 22 and s 23 (6); shares, stated capital, series, pre-emptive rights and options, s 24 to s 29.1 (35); the corporation holding or buying its own shares, s 30 to s 37 (25); reducing stated capital, adjusting it, dividends and shareholder liability, s 38 to s 45 (32); constrained shares sold by the corporation, s 46 and s 47 (15).
`cb1-cases-seat.l4` holds 688 worked cases, grouped the same way, each with a comment naming the provision and the reason from the text.
Every question has at least one case.
Of the 19 questions whose answer is a `MAYBE`, 18 have a case whose expected answer is `NOTHING` (the text does not answer); the nineteenth, the imprisonment term of s 21.4(5), has no input that makes it `NOTHING`, because both modes of prosecution name a term.

**How a question calls layer 1.**
No question restates a rule: each one calls a layer-1 rule and passes it plain inputs.
Where a layer-1 rule takes a record, the question builds the record in a `WHERE` from plain inputs; the one shared record is `Facts for a solvency test in Part V` (seven fields), built for s 34(2), s 35(3), s 36(2), s 38(3) and s 42.
A field that the rule being called does not read is given a fixed placeholder (`0` or `FALSE`) with a comment saying so in the seat file, and every field a rule does read is asked.
Where a layer-1 rule takes the outcome of another rule, the question composes the two: the s 10(3) use question composes the may-set-out rule; the s 14 question derives "bound at the outset" and "adopted" (the contract is written, was made for the corporation, and the corporation did not yet exist) from its inputs; the s 28 "may issue without first offering" question derives "within the exceptions" from the rule that says whether a pre-emptive right arises.
Where the Act turns on a ruling the person cannot make for themselves (that s 31 lets the subsidiary keep the shares, s 30(2); that the two years of s 39(8) have run with the corporation still holding the shares, s 32(1)), the question takes it as a plain yes-or-no input and says so in its `@desc`.
Where a rule needs a date the Act does not define (the "business day" of s 21(5)), the person is asked for the date.
A `MAYBE` input is built from a flag and a value (`IF flag THEN JUST value ELSE NOTHING`).
An input that stands for a provision outside my ranges, for the regulations, or for another Act carries a comment line `-- out of range: ...` above it, as the same facts do in layer 1; the comment says which section and piece (or which source) the fact comes from.

**What is not asked.**
Of the 236 layer-1 rules written with `MEANS`, sixteen are not named by a seat question; I list them below.
The 13 named time limits (written with `DECIDE`, for example `the fifteen-day limit of s 19(4)`) are not named by a question either, but each is read by a rule that a question calls.
Nine take no input at all and state a fixed fact: the purposes of the Act (s 4) and the maximum punishment on summary conviction for the offences in s 20(6), s 21(10), s 21.1(6), s 21.21(4), s 21.31(5), s 22(3), s 32(3) and s 32(4).
A question with no inputs would be a constant, so none is asked (assumed, not ruled); the s 21.4(5) penalty, which depends on how the person is prosecuted, is asked.
Two are helpers that the name rules of s 10(1) call (the list of corporate words and abbreviations, and the full-form/abbreviation correspondence).
Five state duties of an official and not of the person in the seat: what the Director must keep or produce (s 21.21(3)) and what an investigative body must keep, report and answer for (s 21.32(1), (2), (3)).
No question asks what the Director, the court, the Minister or an investigative body decides in their own right; where such a power matters to the person it is asked as "can the Director ...?" or "what will the Director do ...?", from the side of the person who is exposed to it.

## Jural relations

Hohfeld's correlatives: a claim (right) is matched by a duty; a privilege (liberty) by a no-right; a power by a liability (being subject to the power); an immunity by a disability.
Each relation is encoded once, as a rule named for what it decides between the two parties; the seat layer asks it from the side of the person in the seat.
`none` means the provision creates no relation (a definition, a counting rule, a statement of purpose, or machinery).

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | relation | L4 rule |
| --- | --- | --- | --- | --- |
| s 3(4) | not named in the text | a corporation | duty (not to carry on the business) | `the corporation is prohibited from carrying on the business within s 3(4)` |
| s 3(5) | not named in the text | a corporation | duty (not to carry on, unless expressly authorized) | `the corporation is prohibited from carrying on a degree-granting educational institution within s 3(5)` |
| s 5(1) | individuals or bodies corporate who sign | the Director, who must then issue under s 8(1) | power / liability | `the signers may incorporate a corporation within s 5(1)` |
| s 5(2) | an individual of 18 or more, not incapable, not bankrupt | an individual who fails one of the three | power / disability | `the individual may incorporate a corporation within s 5(2)` |
| s 6(1) | not named in the text | the incorporators, who must set out each matter | duty | `the articles of incorporation are complete within s 6(1)` |
| s 6(2) | the incorporators | none stated | privilege / no-right | `the articles may set out the provision within s 6(2)` |
| s 6(3) | the shareholders, in a higher requirement set by the articles or an agreement | the corporation | immunity / disability (the Act's lower number cannot override) | `the fraction of the votes needed to effect the action within s 6(3)` |
| s 6(4) | the shareholders, against an articles requirement above s 109's number | the corporation, whose articles cannot say so | immunity / disability | `an articles requirement for the removal of a director is permitted within s 6(4)` |
| s 7 | not named in the text | an incorporator | duty | `the incorporator has complied with the duty to send the articles and documents within s 7` |
| s 8(1) | the incorporators | the Director | claim / duty (to issue the certificate) | `what the Director must or may do on receiving articles of incorporation within s 8` |
| s 8(2) | the Director | the incorporators | privilege / no-right (to refuse on a notice of non-compliance) | `what the Director must or may do on receiving articles of incorporation within s 8` |
| s 10(1) | not named in the text | a corporation | duty (to carry the word in its name) | `the corporate name carries a required word within s 10(1)` |
| s 10(1) | a corporation | none stated | privilege / no-right (full or abbreviated form) | `the corporation may use and be legally designated by the form within s 10(1)` |
| s 10(1.1) | a corporation within the saving | none stated | privilege / no-right; immunity from s 10(1) | `the corporation must carry a required word in its name within s 10(1), s 10(1.1) and s 10(2)` |
| s 10(2) | the Director | a body corporate continued under the Act | power / liability (to be exempted) | an input of `the corporation must carry a required word in its name within s 10(1), s 10(1.1) and s 10(2)` |
| s 10(3), (4) | a corporation | none stated | privilege / no-right (to use the form) | `the form of name may be set out in the articles within s 10(3)`, `the corporation may use and be legally designated by the name outside Canada within s 10(4)` |
| s 10(5) | not named in the text | a corporation | duty (to set out its name) | `the corporation has complied with the duty to set out its name within s 10(5)` |
| s 10(6) | a corporation | none stated | privilege / no-right | `the corporation may carry on business under or identify itself by the other name within s 10(6)` |
| s 11(1) | the Director | the person who requests the reservation | privilege / no-right (may reserve) | `the Director may reserve the name within s 11(1)` |
| s 11(2) | the incorporators or the corporation, on request | the Director | claim / duty (to assign a designating number name) | `the Director must assign a designating number name within s 11(2)` |
| s 12(1) | not named in the text | a corporation | duty (not to have a prohibited name) | `the name is prohibited within s 12(1)` |
| s 12(2), (4), (4.1) | the Director | a corporation | power / liability (to be directed to change its name) | `the Director may direct the corporation to change its name within s 12(2)` and its siblings |
| s 12(5) | the Director | a corporation that has not followed a directive | power / liability (to have its name revoked) | `the Director may revoke the corporation's name and assign a name within s 12(5)` |
| s 13(1) | not named in the text | the Director | duty (to issue a certificate of amendment and give notice) | `the Director must issue a certificate of amendment and give notice of the new name within s 13(1)` |
| s 14(1) | the other party to the contract | a person who contracts for a corporation not yet in existence | claim / duty (personally bound); the person also has a claim to the benefits | `the person is personally bound by and entitled to the benefits of the contract within s 14` |
| s 14(2) | a corporation (adopting) | the other party to the contract | power / liability | `the corporation has adopted the contract within s 14(2)` |
| s 14(2)(a) | the other party to the contract | the corporation, once it has adopted | claim / duty | `the corporation is bound by and entitled to the benefits of the contract as if it had been a party from the date of the contract within s 14(2)(a)` |
| s 14(3) | a party to the contract | the other party and the person who contracted; the court (to make the order) | power / liability | `a party may apply to a court for an order within s 14(3)` |
| s 14(4) | a person who contracted for the not yet existing corporation | the other party | immunity / disability (the other party cannot hold the person bound) | `the person is exempt from the contract within s 14(4)` |
| s 15(1), (2), (3) | a corporation | none stated | privilege / no-right (and power: capacity to act) | `the corporation has the right, power or privilege of a natural person within s 15(1)` and its siblings |
| s 16(1) | the corporation and its directors | none stated | immunity / disability (no by-law is needed) | `the corporation or its directors have the power within s 16(1)` |
| s 16(2) | not named in the text | a corporation | duty (not to do what the articles restrict) | `the corporation is forbidden to carry on the business or exercise the power within s 16(2)` |
| s 16(3) | a corporation, and the other party to an act or transfer | none stated | immunity / disability (the act is not invalid by reason only) | `the act of the corporation is invalid within s 16(3)` |
| s 17 | any person | none stated | immunity / disability (no constructive notice) | `the person is affected by or deemed to have notice of the contents of the document within s 17` |
| s 18(1), (2) | a person dealing with the corporation or who acquired rights from it | the corporation and a guarantor of its obligation | immunity / disability (they cannot assert the six matters) | `the assertion is barred against the person within s 18` |
| s 19(1), (2), (4) | not named in the text | a corporation | duty (a registered office; notices to the Director) | `the corporation has the registered office that s 19(1) requires`, and the siblings |
| s 19(3) | the directors | none stated | privilege / no-right (to change the address within the province) | `the directors may change the place and address of the registered office within s 19(3)` |
| s 19(4) | not named in the text | the Director | duty (to file the notice) | `the Director must file the notice of change of address within s 19(4)` |
| s 20(1), (2), (2.1), (4), (5) | not named in the text | a corporation | duty (to prepare, maintain, retain and place records) | the rules named in the coverage table |
| s 20(5.1) | a corporation | none stated | privilege / no-right (to keep records outside Canada) | `the corporation may keep the records at a place outside Canada within s 20(5.1)` |
| s 20(4) | the directors | a corporation | claim / duty (the records are open to the directors at all reasonable times) | `the records of subsection 20(2) are kept as s 20(4) requires` |
| s 20(6), s 21(10), s 22(3) | not named in the text (an offence against the Crown) | a corporation (s 20(6)); a person (s 21(10), s 22(3)) | liability to prosecution | the offence rules |
| s 21(1) | shareholders, creditors, their personal representatives, the Director; any other person if the corporation is distributing | the corporation | claim / duty (access, free or on a fee) | `the access the person has to the corporate records within s 21(1) and s 21(1.1)` |
| s 21(1.1) | a person described in subsection 21(1) | the corporation and its agent or mandatary | claim / duty (access to the securities register after an affidavit) | the same rule |
| s 21(2) | a shareholder | the corporation | claim / duty (one copy, no charge) | `the shareholder is entitled to one copy ... within s 21(2)` |
| s 21(3), (4), (6) | the person who requires the list | the corporation or its agent or mandatary | power / liability | `the person may require the corporation to provide a basic list within s 21(3)` and its siblings |
| s 21(5) | the person who required the supplemental list | the corporation | claim / duty (to provide it by the due day) | `the day the supplemental list is due within s 21(5)` |
| s 21(9) | not named in the text | any person who obtains a list or information | duty (use only for the three purposes) | `the use of the list or information is permitted within s 21(9)` |
| s 22(1) | a corporation | none stated | privilege / no-right (any listed form) | `the form of the record is permitted within s 22(1)` |
| s 22(2) | not named in the text | a corporation, its agents or mandataries | duty (reasonable precautions) | `the corporation or its agents or mandataries have taken the precautions s 22(2) requires` |
| s 23(1) | a corporation | none stated | privilege / no-right (may adopt and change a seal) | `the corporation may adopt, and may change, a corporate seal within s 23(1)` |
| s 23(2) | a person holding a document executed or signed for the corporation | none stated | immunity / disability (not invalid merely for want of a seal) | `the document is invalid within s 23(2)` |
| s 21.1(1), (2), (3), (5) | not named in the text (the individuals with significant control have an interest but no claim is stated) | a corporation to which s 21.1 applies | duty (keep the register, take steps, record, dispose) | `the register contains what s 21.1(1) requires`, `the corporation has taken the steps s 21.1(2) requires`, `the corporation recorded the information in time within s 21.1(3)`, `the last day to dispose of the personal information within s 21.1(5)` |
| s 21.1(4) | the corporation, which has asked | a shareholder | claim / duty (reply accurately, completely, as soon as feasible) | `the shareholder has complied with the duty to reply within s 21.1(4)` |
| s 21.1(7) | a corporation that is a reporting issuer, listed, or in a prescribed class | none stated | immunity / disability (s 21.1 does not apply) | `section 21.1 applies to the corporation within s 21.1(7)` |
| s 21.2, s 21.21(1), (2), s 21.3(1) | the Director | a corporation to which s 21.1 applies | claim / duty (prescribed steps; annual and event information; disclosure on request) | the rules named in the coverage table |
| s 21.21(3) | the Director | none stated | immunity (no duty to keep or produce after six years) | `the Director is required to keep or produce the information on the day within s 21.21(3)` |
| s 21.301, s 21.302 | the Director | the recipient and the corporation | privilege / no-right (may provide the information) | `the Director may provide the information received under section 21.21 to the recipient within s 21.301 and s 21.302` |
| s 21.303(1), (2) | the public | the Director | claim / duty (to make the item available) | `the Director must make the item available to the public within s 21.303` |
| s 21.303(3) | the Director | an individual with significant control, or the corporation, who applies | power / liability (to withhold) | `the Director may choose not to make the information available to the public within s 21.303(3)` |
| s 21.31(1) | an investigative body | a corporation to which s 21.1 applies | claim / duty (copy or specified information) | `the corporation must provide the copy of its register or disclose the specified information within s 21.31(1)` |
| s 21.31(3) | none (a limit) | an investigative body | disability (may make a request only with reasonable grounds) | `the investigative body may make the request within s 21.31(3)` |
| s 21.32(1), (2) | the Director (for the report) | an investigative body | duty (keep a record; report within 90 days) | `the investigative body has kept the record s 21.32(1) requires`, `the investigative body's report has the contents s 21.32(2) requires` |
| s 21.1(6), s 21.21(4), s 21.31(5), s 21.4 | not named in the text (an offence against the Crown) | a corporation (21.1(6), 21.21(4), 21.31(5)); a director or officer, or a shareholder (21.4) | liability to prosecution | the offence rules |
| s 24(1), (2) | not named in the text | a corporation | duty (shares in registered form and without nominal or par value) | `the share is as s 24(1) requires within s 24(1) and s 24(2)` |
| s 24(3) | the holders of the only class | the corporation | claim / duty (equal rights, including to vote, to dividends declared and to the remaining property) | `the holders of the only class have the right within s 24(3)` |
| s 24(4) | not named in the text | the articles | duty (set out the rights; attach the three rights to at least one class) | `the articles meet the requirements for classes of shares within s 24(4)` |
| s 25(1) | the directors | none stated | privilege / no-right and power (to determine the issue) | `the directors may determine the times, persons and consideration of an issue of shares within s 25(1)` |
| s 25(2) | the holders of issued shares | the corporation and its creditors | immunity / disability (non-assessable) | `the holder is liable in respect of the share to the corporation or its creditors within s 25(2)` |
| s 25(3) | not named in the text | a corporation | duty (no issue until fully paid) | `the share may be issued for the consideration within s 25(3)` |
| s 25(4) | the directors | none stated | privilege / no-right | `the directors may take the item into account in determining the fair equivalent within s 25(4)` |
| s 26(1), (2), (4), (8), (10) | not named in the text | a corporation | duty (maintain accounts; add the full amount, no more; add paid amounts; reduce only as the Act provides) | the stated capital rules |
| s 26(3), (6) | a corporation | none stated | privilege / no-right (may add less than the full amount; may add other amounts) | `the corporation may add less than the full consideration within s 26(3)`, `the corporation may add the amount to a stated capital account within s 26(6)` |
| s 26(5) | the shareholders (by special resolution) | the corporation | disability (an addition needs their approval) | `the addition must be approved by special resolution within s 26(5)` |
| s 26(11) | an open-end mutual fund | none stated | immunity / disability (the stated capital provisions do not apply) | `the stated capital provisions of this Act apply to the corporation within s 26(11)` |
| s 27(1) | the articles | none stated | power (to authorize a class in series) | `the articles may authorize the issue of a class of shares in series in that way within s 27(1)` |
| s 27(2) | the holders of each series of a class | the corporation | claim / duty (rateable participation) | `the amount this series receives within s 27(2)` |
| s 27(3) | the holders of another outstanding series of the same class | the articles | disability (no priority may be conferred) | `the rights attached to the series are permitted within s 27(3)` |
| s 27(4), (5) | the directors have the duty (s 27(4)); the directors have the claim (s 27(5)) | the directors; the Director | duty / claim | `the directors have complied with the duty to send articles of amendment before the issue within s 27(4)`, `the Director must issue a certificate of amendment within s 27(5)` |
| s 28(1) | the shareholders of a class, if the articles so provide | the corporation | claim / duty (first offer, pro rata) | `shareholders of the class have a pre-emptive right in respect of the shares within s 28(1) and s 28(2)` |
| s 28(2) | the corporation | the shareholders | immunity / disability (no pre-emptive right in three cases) | the same rule |
| s 29(1) | a corporation | none stated | privilege / no-right (may issue); duty (to set out the conditions) | `the corporation has set out the conditions as s 29(1) requires` |
| s 29(2) | a corporation | none stated | privilege / no-right (transferable or not; separable or not) | `the instrument may be made transferable or non-transferable within s 29(2)` |
| s 29(3) | not named in the text (the holders of the privileges, options and rights have the interest) | a corporation | duty (reserve authorized shares) | `the corporation has reserved sufficient authorized shares within s 29(3)` |
| s 29.1(1) | not named in the text | a corporation | duty (not to issue in bearer form) | `the corporation is forbidden to issue the document within s 29.1(1)` |
| s 29.1(2) | a holder of a bearer document issued before the section came into force | the corporation | claim / duty (to exchange it for a registered one) | `the corporation must issue a registered document in exchange within s 29.1(2)` |
| s 30(1), (2) | not named in the text | a corporation | duty (not to hold its own shares; not to permit a subsidiary to acquire; to cause a subsidiary to dispose within five years) | `the corporation may hold shares in itself or in its holding body corporate within s 30(1)(a)`, `the last day for the subsidiary to dispose of the shares within s 30(2)` |
| s 31(1) to (4) | a corporation | none stated | privilege / no-right (the exceptions) | the s 31 rules |
| s 31(5), (6) | not named in the text | a corporation | duty (prescribed conditions); liability to the prescribed consequences | `the conditions subsequent of s 31(5) are satisfied`, `the prescribed consequences apply to the acquisition and issuance within s 31(6)` |
| s 32(1) | a corporation | none stated | privilege / no-right (to hold shares for Canadian ownership) | `section 32(1) permits the corporation to hold the shares` |
| s 32(2) | not named in the text | a corporation | duty (not to transfer unless satisfied) | `the corporation may transfer the shares held under subsection 32(1) within s 32(2)` |
| s 32(3), (4) | not named in the text (an offence against the Crown) | a corporation; a director who knowingly authorized, permitted or acquiesced | liability to prosecution | the offence rules |
| s 32(6) | the person who receives a transfer | none stated | immunity / disability (the transfer is not void, voidable or null solely because it contravenes s 32(2)) | `the transfer of shares is void, voidable or null within s 32(6)` |
| s 33(1), (2) | not named in the text | a corporation; its subsidiary body corporate | duty (not to vote, or permit to be voted, its own shares unless the conditions are met) | `the shares may be voted or permitted to be voted within s 33(1)`, `the subsidiary may vote or be permitted to vote the shares within s 33(2)` |
| s 34(1), s 35(1), (2), s 36(1) | a corporation | none stated | privilege / no-right (to purchase, acquire or redeem its shares) | the rules named in the coverage table |
| s 34(2), s 35(3), s 36(2) | not named in the text (creditors have the interest) | a corporation | duty (no payment where reasonable grounds for believing a shortfall) | `the corporation is forbidden to make the payment to acquire its shares within s 34(2)` and its siblings |
| s 37 | a corporation | a shareholder who surrenders a share | privilege / no-right (accepting a gift); duty (no extinguishing a liability except under s 38) | `the corporation may accept the share within s 37`, `the corporation may extinguish or reduce the liability within s 37` |
| s 38(1) | a corporation | none stated | power (by special resolution) | `the corporation may reduce its stated capital within s 38(1)` |
| s 38(3) | creditors (the interest is theirs) | a corporation | duty (no reduction where reasonable grounds for believing a shortfall) | `the corporation is forbidden to reduce its stated capital within s 38(3)` |
| s 38(4) | a creditor of the corporation | a shareholder or other recipient | power / liability (to apply to a court for an order) | `the creditor is entitled to apply to a court for the order within s 38(4)` |
| s 38(5) | a shareholder or recipient sued out of time | a creditor | immunity / disability (no action after two years) | `the action to enforce a liability imposed by section 38 is in time within s 38(5)` |
| s 39(1) to (4), (6) | not named in the text | a corporation | duty (adjust the stated capital account; cancel the shares) | the s 39 rules |
| s 39(7), (8), (9), (11), (12) | a corporation, a holder of debt obligations | none stated | immunity / disability (deemed not to have acquired; not redeemed by reason only of repayment); privilege (to reissue) | the s 39 rules |
| s 40(1) | the other party to a contract to buy shares | a corporation | claim / duty (to fulfil), displaced where enforcement would breach s 34 to 36 | `the corporation must fulfil its obligations under the contract to buy shares within s 40(1)` |
| s 40(2) | the other party | the corporation; creditors and holders of prior classes (subordinated to them) | claim / duty (to be paid when lawfully able); ranking in a liquidation | `the other party is entitled to be paid within s 40(2)`, `the claimant ranks in priority to the person in a liquidation within s 40(2)` |
| s 41 | the directors | none stated | power (to authorize a commission) | `the directors may authorize the corporation to pay the commission within s 41` |
| s 42 | creditors (the interest is theirs) | a corporation | duty (no dividend where reasonable grounds for believing a shortfall) | `the corporation is forbidden to declare or pay a dividend within s 42` |
| s 43(1) | a corporation | none stated | privilege / no-right (to pay a dividend in shares, money or property) | `the corporation may pay the dividend in that form within s 43(1)` |
| s 43(2) | not named in the text | a corporation | duty (to add the declared amount to the stated capital account) | `the amount to add to the stated capital account for the class or series issued within s 43(2)` |
| s 45(1) | the shareholders | the corporation's creditors and others | immunity / disability (no liability as shareholders, except under five subsections) | `section 45(1) shields the shareholder from the liability within s 45(1)` |
| s 45(2) | a corporation (with the articles' provision) | a shareholder, whose share is subject to the lien | privilege / no-right; liability (the share is subject to the lien) | `the articles may provide that the corporation has a lien or hypothec on the share within s 45(2)` |
| s 45(3) | a corporation | a shareholder | power / liability (to enforce the lien in accordance with its by-laws) | `the corporation may enforce the lien or hypothec within s 45(3)` |
| s 46(1) | a corporation with constraints on its shares | the owner of shares held contrary to the constraints | power / liability (to have the shares sold) | `the corporation may sell the constrained shares as if it were their owner within s 46(1)` |
| s 46(2) | the holders of the shares in the constrained class or series taken as a whole | the directors | claim / duty (select in good faith, without unfair prejudice or disregard) | `the directors have complied with the duty in selecting the shares for sale within s 46(2)` |
| s 46(3) | the person who would otherwise be the registered owner | the corporation | claim / duty (to receive the net proceeds); the owner before the sale is divested (liability) | `the person is entitled to receive only the net proceeds of the sale within s 46(3)` |
| s 47(1), (2) | the person entitled under s 46(3) | the corporation (as trustee) | claim / duty (a trust fund, invested as prescribed) | `the proceeds constitute a trust fund in the hands of the corporation within s 47(1)` |
| s 47(3), (4) | the corporation, the trust company | the person entitled | power / liability (to transfer the fund); immunity (discharge on a receipt) | `the corporation may transfer the trust fund and its administration to the transferee within s 47(3)` |
| s 47(5) | Her Majesty in right of Canada | the person entitled, who has not claimed the fund in ten years | power / liability (vesting) | `the fund has vested in Her Majesty in right of Canada on the day within s 47(5)` |

### The seat's side of each relation

Layer 1 encodes each relation once.
The seat layer (`cb1-seat.l4`) asks it from the side of the person in the seat (an incorporator, a director or officer, a shareholder), so the same relation appears as a right the person holds, a duty the person must see to, or an exposure.
One row per `§§` group; "other side" is the party on the other end of the relation.

| group of questions | what the person in the seat holds or bears | other side | relation | layer-1 rules the questions call |
| --- | --- | --- | --- | --- |
| Whether the Act applies (s 3) | a status: whether the Act applies to the corporation; the corporation's duty not to carry on a barred business (s 3(4)) or a degree-granting institution (s 3(5)) | the corporation, which is under the duty | status; duty / no-right | the s 3 rules |
| Incorporating (s 5 to s 9) | the incorporators' power to incorporate (s 5(1), s 5(2)) and their duty to send the documents (s 7); the power to put the s 6 provisions in the articles | the Director, who is liable to issue or refuse the certificate (s 8); the person who fails a s 5(2) condition, who is under a disability | power / liability; power / disability; duty | the s 5 to s 9 rules |
| The corporation's name (s 10 to s 13) | the corporation's privilege to use and be designated by a form of its name (s 10(3), (4), (6)) and its duty to set the name out on documents (s 10(5)); the corporation's exposure to the Director's powers to reserve a name (s 11(1)), to give a number name (s 11(2)), to direct a change (s 12(2), (4), (4.1)) and to revoke and assign (s 12(5)) | the Director | privilege / no-right; duty; power / liability | the s 10 to s 13 rules |
| A contract made before the corporation exists (s 14) | the person's liability on the contract (s 14(1)) and immunity if the contract exempts them (s 14(4)); the corporation's power to adopt (s 14(2)); a party's power to apply to a court (s 14(3)) | the other party to the contract; the corporation; the court | liability / power; immunity / disability; power / liability | the s 14 rules |
| What the corporation can do (s 15 to s 18) | the corporation's privileges (the capacity of a natural person, s 15; carrying on business throughout Canada, s 15(2)); its disability where the articles restrict it (s 16(2)); the person's immunity from the effect of a filed document (s 17) and from the corporation's assertion of a defect (s 18) | the person dealing with the corporation | privilege / no-right; disability; immunity / disability | the s 15 to s 18 rules |
| Registered office, records and who may see them (s 19 to s 21) | the corporation's duties to have the office and keep the records (s 19, s 20); the shareholder's and creditor's claims to examine records, to a free copy of the articles and by-laws, and to the lists (s 21(1) to (6)); the person's duty to give an affidavit (s 21(7), (8)) and not to use the information outside s 21(9) | the corporation; the person who receives the information | claim / duty; duty / no-right; liability to prosecution | the s 19 to s 21 rules |
| Individuals with significant control (s 21.1 to s 21.4) | the corporation's duties to keep the register, keep it current and send the Director the information (s 21.1, s 21.2, s 21.21); a shareholder's duty to answer the corporation's request (s 21.1(4)); the Director's power to pass the information on or publish it (s 21.301 to s 21.303) and the power of the individual, or of the corporation, to apply to have it withheld, and the Director's discretion to grant that (s 21.303(3)); an investigative body's claim to the register (s 21.31); the director's, officer's and shareholder's liability to prosecution (s 21.4) | the Director; an investigative body; the individual with significant control | duty / claim; power / liability; claim / duty | the s 21.1 to s 21.4 rules |
| Form of records and the corporate seal (s 22, s 23) | the corporation's privilege to keep records in a permitted form (s 22(1)), its duty to take precautions (s 22(2)); its privilege to adopt a seal (s 23(1)); the person's immunity from invalidity for want of a seal (s 23(2)) | none stated | privilege / no-right; duty; immunity | the s 22 and s 23 rules |
| Shares, stated capital, series, pre-emptive rights and options (s 24 to s 29.1) | the shareholder's claims to vote, to dividends and to the remaining property on a single class (s 24(3)); the shareholder's immunity from further liability on issued shares (s 25(2)); the directors' power to issue shares (s 25(1)); a series' claim to rateable payment (s 27(2)); the shareholder's pre-emptive claim (s 28(1)); the holder's claim to exchange a bearer document (s 29.1(2)) | the corporation; the other series and classes | claim / duty; immunity / disability; power / liability | the s 24 to s 29.1 rules |
| The corporation holding or buying its own shares (s 30 to s 37) | the corporation's disability to hold, or to let a subsidiary hold, its own shares and its duty to see that a subsidiary disposes of them (s 30); its privileges in s 31 and s 32(1); the director's liability for the offence in s 32(4); the corporation's privileges to buy, redeem and accept a gift (s 34 to s 37), subject to the creditors' interest in the solvency tests | the subsidiary; creditors; the directors | disability / duty; privilege / no-right; liability | the s 30 to s 37 rules |
| Reducing stated capital, adjusting it, dividends and shareholder liability (s 38 to s 45) | the corporation's power to reduce stated capital by special resolution (s 38(1)) and its disability where the s 38(3) tests fail; the creditor's power to apply to a court against a shareholder (s 38(4)) and the shareholder's immunity after two years (s 38(5)); the claimant's claim to be paid under a contract to sell shares and its ranking (s 40); the directors' power to authorize a commission (s 41); the dividend limits (s 42, s 43); the shareholder's immunity as shareholder (s 45(1)); the lien (s 45(2), (3)) | creditors; the corporation; the shareholder | power / liability; claim / duty; immunity / disability | the s 38 to s 45 rules |
| Constrained shares sold by the corporation (s 46, s 47) | the corporation's power to sell constrained shares (s 46(1)) and the owner's divestment (s 46(3)); the directors' duty in selecting the shares (s 46(2)); the claim to the net proceeds (s 46(3)); the trust fund held for the person entitled (s 47(1)) and the corporation's discharge (s 47(3), (4)); the Crown's vesting of an unclaimed fund (s 47(5)) | the owner; the corporation as trustee; the Crown | power / liability; claim / duty; liability | the s 46 and s 47 rules |


## Coverage table


| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Title block: converter note on the text's status | src:1-3 | inert | - | Lines 1-3 are the converter's own note on the text (it is an unofficial plain-text reproduction, from the Justice Canada consolidation current to 2026-09-30, English only). It is not a provision of the Act; it states no rule and carries no date of enactment or commencement. Pure citation or title. |
| Title block: the Act's title, its chapter citation and long title | src:5-7 | inert | - | Lines 5-7 give the title (Canada Business Corporations Act), the chapter citation (R.S.C., 1985, c. C-44) and the long title (An Act respecting Canadian business corporations). A pure title and citation: it states no rule, and holds no date of enactment, assent or commencement, so no dated value is carried (see NOTES.md, "Dates"). |
| Heading: Short Title | src:9 | inert | - | A heading (a label for the one section under it); it states no rule and carries no condition. |
| s 1 | src:10-11 | inert | - | "This Act may be cited as the Canada Business Corporations Act." It names the Act and decides nothing for any person: a pure citation. The marginal note "Short title" (src:10) is covered by this row. |
| Heading: Application | src:115 | inert | - | A heading (a label for s 3); it states no rule and carries no condition. |
| s 3(1) | src:116-117 | encoded | `cb1-part1-application.l4` `this Act applies to the body corporate within s 3(1)` | Calls the keel's `corporation within s 2(1)`, which is the same three facts: incorporated or continued under this Act, and not discontinued. |
| s 3(2) | src:118 | repealed or blank in this text | - | `(2) [Repealed, 1991, c. 45, s. 551]` (src:118). |
| s 3(3) | src:119-124 | encoded | `cb1-part1-application.l4` `the law is excluded from applying to a corporation within s 3(3)`; `Law that s 3(3) may exclude from applying to a corporation` | Paragraphs (a.1), (b) and (c); paragraph (a) is repealed (own row below). Whether a Special Act provision is inconsistent with this Act is a plain input: the Act hands the judgement to the person asking. |
| s 3(3)(a) | src:121 | repealed or blank in this text | - | `(a) [Repealed, 2009, c. 23, s. 344]` (src:121). |
| s 3(4) | src:125-130 | encoded | `cb1-part1-application.l4` `the corporation is prohibited from carrying on the business within s 3(4)`; `Business a corporation may not carry on under s 3(4)` | The four businesses of paragraphs (a) to (c), paragraph (a.1) included; the four statutes are not among the sources, so which business a person carries on is asked as a fact. |
| s 3(5) | src:131-132 | encoded | `cb1-part1-application.l4` `the corporation is prohibited from carrying on a degree-granting educational institution within s 3(5)` | Forbidden "unless expressly authorized" by a federal or provincial agent with the power by law to confer degree-granting authority. |
| Heading: Purposes of Act | src:134 | inert | - | A heading (a label for s 4); it states no rule and carries no condition. |
| s 4 | src:135-136 | encoded | `cb1-part1-application.l4` `the purposes of this Act within s 4`; `Purpose of the Act (s 4)` | A purpose clause. It states no obligation and decides nothing for a person, so it is carried as data (the three purposes, quotable) with no seat question. |
| Heading: PART II Incorporation | src:138 | inert | - | A heading (a label for Part II); it states no rule and carries no condition. |
| s 5(1) | src:139-140 | encoded | `cb1-part2-incorporation.l4` `the signers may incorporate a corporation within s 5(1)` | One or more individuals or bodies corporate; a signer who is neither is not counted (fork cb1-F1). |
| s 5(2) | src:141-145 | encoded | `cb1-part2-incorporation.l4` `the individual may incorporate a corporation within s 5(2)` | The text joins (a) to (c) with "or"; read as cumulative (fork cb1-F3). Calls the keel's `incapable within s 2(1)`. |
| s 6(1) | src:146-155 | encoded | `cb1-part2-incorporation.l4` `Articles of incorporation as delivered (s 6(1))`; `the articles of incorporation are complete within s 6(1)` | One field per matter paragraphs (a) to (f) require, and one per condition that makes a requirement bite. |
| s 6(2) | src:156-157 | encoded | `cb1-part2-incorporation.l4` `the articles may set out the provision within s 6(2)` | A permission to put by-law matters in the articles. |
| s 6(3) | src:158-159 | encoded | `cb1-part2-incorporation.l4` `the fraction of the votes needed to effect the action within s 6(3)` | Greater of the Act's number, the articles' and a unanimous shareholder agreement's, subject to s 6(4); fork cb1-F2. |
| s 6(4) | src:160-161 | encoded | `cb1-part2-incorporation.l4` `an articles requirement for the removal of a director is permitted within s 6(4)` | Compared against the fraction s 109 requires (an input; out of range, piece cb2). |
| s 7 | src:162-163 | encoded | `cb1-part2-incorporation.l4` `the incorporator has complied with the duty to send the articles and documents within s 7` | The notice of registered office (s 19(2)) and the notice of directors (s 106) are inputs. |
| s 8(1) | src:164-165 | encoded | `cb1-part2-incorporation.l4` `what the Director must or may do on receiving articles of incorporation within s 8`; `Outcome of sending articles of incorporation under s 8` | "Shall issue" is the Director's duty; "in accordance with section 262" is out of range (piece cb5). |
| s 8(2) | src:166-167 | encoded | `cb1-part2-incorporation.l4` `what the Director must or may do on receiving articles of incorporation within s 8` | "May refuse": the Act leaves the choice to the Director, so the outcome says the Director may either issue or refuse. |
| s 9 | src:168-169 | encoded | `cb1-part2-incorporation.l4` `the corporation has come into existence by the day within s 9` | From the date shown in the certificate, that day included. |
| s 10(1) | src:170-171 | encoded | `cb1-part2-incorporation.l4` `the corporate words and abbreviations that s 10(1) lists`; `the corporate name carries a required word within s 10(1)`; `the corporation may use and be legally designated by the form within s 10(1)` | Eleven strings; the pairing of full and abbreviated forms is a reading (fork cb1-F4). |
| s 10(1.1) | src:172-173 | encoded | `cb1-part2-incorporation.l4` `the corporation must carry a required word in its name within s 10(1), s 10(1.1) and s 10(2)`; `the corporation may use and be legally designated by the expression or abbreviation within s 10(1.1)` | The day subsection (1.1) came into force is not in the text, so whether the name included the expression on that day is an input. |
| s 10(2) | src:174-175 | encoded | `cb1-part2-incorporation.l4` `the corporation must carry a required word in its name within s 10(1), s 10(1.1) and s 10(2)` | The Director's exemption of a continued body corporate is an input (the Director's choice). |
| s 10(3) | src:176-177 | encoded | `cb1-part2-incorporation.l4` `the form of name may be set out in the articles within s 10(3)`; `the corporation may use and be legally designated by the form within s 10(3)`; `Form of corporate name set out in the articles (s 10(3))` | The prescribed criteria for a combined form are not among the sources: an input. |
| s 10(4) | src:178-179 | encoded | `cb1-part2-incorporation.l4` `the corporation may use and be legally designated by the name outside Canada within s 10(4)` | Subject to s 12(1). |
| s 10(5) | src:180-181 | encoded | `cb1-part2-incorporation.l4` `the corporation must set out its name in legible characters on the document within s 10(5)`; `the corporation has complied with the duty to set out its name within s 10(5)`; `Kind of document under s 10(5)` | Four kinds of document. |
| s 10(6) | src:182-183 | encoded | `cb1-part2-incorporation.l4` `the corporation may carry on business under or identify itself by the other name within s 10(6)` | Subject to s 10(5) (which is a separate duty, encoded above) and s 12(1). |
| s 11(1) | src:184-185 | encoded | `cb1-part2-incorporation.l4` `the Director may reserve the name within s 11(1)`; `the last day the name stays reserved within s 11(1)` | "For a prescribed period": the period is an input of type `Time limit`. |
| s 11(2) | src:186-187 | encoded | `cb1-part2-incorporation.l4` `the Director must assign a designating number name within s 11(2)`; `the name is a designating number name within s 11(2)` | "Shall assign" on request by the incorporators or the corporation. |
| s 12(1) | src:188-189 | encoded | `cb1-part2-incorporation.l4` `the name is prohibited within s 12(1)` | The regulations are not among the sources: both facts are inputs. This one rule is the fact that s 10(3), (4) and (6) are subject to, and the duty "shall not". |
| s 12(2) | src:190-191 | encoded | `cb1-part2-incorporation.l4` `the Director may direct the corporation to change its name within s 12(2)` | "In accordance with section 173" is out of range (piece cb4). |
| s 12(3) | src:192 | repealed or blank in this text | - | `(3) [Repealed, 1994, c. 24, s. 7]` (src:192). |
| s 12(4) | src:193-194 | encoded | `cb1-part2-incorporation.l4` `the Director may direct the corporation to change a designating number name within s 12(4)` | Power of the Director. |
| s 12(4.1) | src:195-196 | encoded | `cb1-part2-incorporation.l4` `the Director may direct the corporation to change its name because an undertaking was not honoured within s 12(4.1)` | The period "specified in subsection (5)" is the prescribed period, which is not in the sources: whether the undertaking was honoured within it is an input (finding in NOTES). |
| s 12(5) | src:197-198 | encoded | `cb1-part2-incorporation.l4` `the Director may revoke the corporation's name and assign a name within s 12(5)`; `the last day for the corporation to follow the directive within s 12(5)`; `the name of the corporation within s 12(5)` | The prescribed period is an input of type `Time limit`. |
| s 13(1) | src:199-200 | encoded | `cb1-part2-incorporation.l4` `the Director must issue a certificate of amendment and give notice of the new name within s 13(1)` | Duty of the Director. |
| s 13(2) | src:201-202 | encoded | `cb1-part2-incorporation.l4` `the articles are amended by the certificate of amendment by the day within s 13(2)` | From the date shown in the certificate. |
| s 14(1) | src:203-204 | encoded | `cb1-part2-incorporation.l4` `the person is personally bound by the pre-incorporation contract at the outset within s 14(1)` | "Subject to this section": the outcome after (2) to (4) is the rule `the person is personally bound by and entitled to the benefits of the contract within s 14`. |
| s 14(2) | src:205-208 | encoded | `cb1-part2-incorporation.l4` `the corporation has adopted the contract within s 14(2)`; `the corporation is bound by and entitled to the benefits of the contract as if it had been a party from the date of the contract within s 14(2)(a)`; `the person is personally bound by and entitled to the benefits of the contract within s 14` | Paragraph (a) is the corporation's side; paragraph (b), with (3) and (4), the person's. Whether the time was reasonable is an input (a court's judgement). |
| s 14(3) | src:209-210 | encoded | `cb1-part2-incorporation.l4` `a party may apply to a court for an order within s 14(3)`; `the court may make an order about the obligations of the person within s 14(3)` | "May make any order it thinks fit" is the court's discretion: the rule says whether the court may, never what it will order. |
| s 14(4) | src:211-212 | encoded | `cb1-part2-incorporation.l4` `the person is exempt from the contract within s 14(4)` | Expressly so provided in the written contract. |
| Heading: PART III Capacity and Powers | src:214 | inert | - | A heading (a label for Part III); it states no rule and carries no condition. |
| s 15(1) | src:215-216 | encoded | `cb1-part3-capacity.l4` `the corporation has the right, power or privilege of a natural person within s 15(1)` | "Subject to this Act": a provision of this Act that takes a right away is an input. |
| s 15(2) | src:217-218 | encoded | `cb1-part3-capacity.l4` `the corporation may carry on business throughout Canada within s 15(2)` | A privilege of the corporation; not made "subject to" anything. |
| s 15(3) | src:219-220 | encoded | `cb1-part3-capacity.l4` `the corporation has the capacity to act in the jurisdiction outside Canada within s 15(3)` | "To the extent that the laws of such jurisdiction permit": that is the input. |
| s 16(1) | src:221-222 | encoded | `cb1-part3-capacity.l4` `the corporation or its directors have the power within s 16(1)` | No by-law is necessary; the tests assert that passing one changes nothing. |
| s 16(2) | src:223-224 | encoded | `cb1-part3-capacity.l4` `the corporation is forbidden to carry on the business or exercise the power within s 16(2)` | Two limbs: a restriction in the articles, and a manner contrary to the articles. |
| s 16(3) | src:225-226 | encoded | `cb1-part3-capacity.l4` `the act of the corporation is invalid within s 16(3)` | "By reason only": the act is invalid only on some other ground. |
| s 17 | src:227-228 | encoded | `cb1-part3-capacity.l4` `the person is affected by or deemed to have notice of the contents of the document within s 17` | Filing and availability for inspection, by themselves, give no notice. |
| s 18(1) | src:229-236 | encoded | `cb1-part3-capacity.l4` `the assertion is barred against the person within s 18`; `Assertion barred by s 18(1)` | Six assertions (a) to (f); paragraph (f) refers to s 189(3), out of range (piece cb4). |
| s 18(2) | src:237-238 | encoded | `cb1-part3-capacity.l4` `the assertion is barred against the person within s 18` | The exception for a person who has, or ought to have, knowledge by virtue of their relationship to the corporation. |
| Heading: PART IV Registered Office and Records | src:240 | inert | - | A heading (a label for Part IV); it states no rule and carries no condition. |
| s 19(1) | src:241-242 | encoded | `cb1-part4-records.l4` `the corporation has the registered office that s 19(1) requires` | "At all times" is not modelled as a period: the rule asks about the day in question. |
| s 19(2) | src:243-244 | encoded | `cb1-part4-records.l4` `the corporation has complied with the duty to send a notice of registered office within s 19(2)` | The form is the Director's to fix: not modelled. |
| s 19(3) | src:245-246 | encoded | `cb1-part4-records.l4` `the directors may change the place and address of the registered office within s 19(3)` | Within the province specified in the articles. |
| s 19(4) | src:247-248 | encoded | `cb1-part4-records.l4` `the last day to send the notice of change of address within s 19(4)`; `the notice of change of address was sent in time within s 19(4)`; `the Director must file the notice of change of address within s 19(4)` | Fifteen days; counted by the keel's convention (F1). |
| s 20(1) | src:249-254 | encoded | `cb1-part4-records.l4` `Corporate records kept under s 20(1)`; `the corporation keeps all the records s 20(1) lists`; `the corporate records are kept at a permitted place within s 20(1) and s 20(5.1)` | Four kinds of record; the place is the registered office or another place in Canada designated by the directors. |
| s 20(2) | src:255-256 | encoded | `cb1-part4-records.l4` `Directors and accounting records kept under s 20(2)`; `the corporation keeps all the records s 20(2) lists` | Accounting records, and minutes of directors and committees. |
| s 20(2.1) | src:257-258 | encoded | `cb1-part4-records.l4` `the last day the corporation must retain the accounting records within s 20(2.1)` | Six years after the end of the financial year; the later of that and any longer period another Act provides. |
| s 20(3) | src:259-260 | encoded | `cb1-part4-records.l4` `the record counts as a record for paragraph 20(1)(b) and subsection 20(2) within s 20(3)` | Records of a continued body corporate. |
| s 20(4) | src:261-262 | encoded | `cb1-part4-records.l4` `the records of subsection 20(2) are kept as s 20(4) requires` | The place need not be in Canada. |
| s 20(5) | src:263-264 | encoded | `cb1-part4-records.l4` `the corporation has complied with the duty to keep quarterly accounting records in Canada within s 20(5)` | Subsection (5.1) applies "despite" it. |
| s 20(5.1) | src:265-268 | encoded | `cb1-part4-records.l4` `the corporation may keep the records at a place outside Canada within s 20(5.1)` | "Subject to the Income Tax Act, the Excise Tax Act, the Customs Act and any other Act administered by the Minister of National Revenue": one input. |
| s 20(6) | src:269-270 | encoded | `cb1-part4-records.l4` `the corporation is guilty of an offence within s 20(6)`; `the most a court may impose on summary conviction within s 20(6)` | A fine not exceeding $5,000; no imprisonment. |
| s 21(1) | src:271-272 | encoded | `cb1-part4-records.l4` `the access the person has to the corporate records within s 21(1) and s 21(1.1)`; `Person seeking to examine the corporate records (s 21)`; `Access to the corporate records under s 21(1) and s 21(1.1)` | Free for shareholders, creditors, their personal representatives and the Director; on a reasonable fee for any other person if the corporation is distributing. |
| s 21(1.1) | src:273-274 | encoded | `cb1-part4-records.l4` `the access the person has to the corporate records within s 21(1) and s 21(1.1)` | The securities register of a distributing corporation: affidavit first. |
| s 21(2) | src:275-276 | encoded | `cb1-part4-records.l4` `the shareholder is entitled to one copy of the articles, by-laws and any unanimous shareholder agreement, without charge, within s 21(2)` | A claim of the shareholder. |
| s 21(3) | src:277-278 | encoded | `cb1-part4-records.l4` `the person may require the corporation to provide a basic list within s 21(3)`; `the last day to provide the basic list within s 21(3)`; `the earliest date the basic list may be made up to within s 21(3)`; `the corporation has provided the basic list as s 21(3) requires` | Ten days after receipt; made up to a date not more than ten days before receipt. |
| s 21(4) | src:279-280 | encoded | `cb1-part4-records.l4` `the person may require supplemental lists within s 21(4)` | On a statement in the affidavit and payment of a reasonable fee. |
| s 21(5) | src:281-284 | encoded | `cb1-part4-records.l4` `the day the supplemental list is due within s 21(5)` | "Business day" is not defined in the sources and no holiday calendar is among them: the business day after is an input (finding in NOTES). |
| s 21(6) | src:285-286 | encoded | `cb1-part4-records.l4` `the person may also require the list to include the known holders of options within s 21(6)` | A power of the person who requires a list. |
| s 21(7) | src:287-291 | encoded | `cb1-part4-records.l4` `Affidavit under s 21(7)`; `the affidavit has the contents s 21(7) and s 21(8) require` | The three statements; paragraph (b) applies only where the applicant is a body corporate. |
| s 21(8) | src:292-293 | encoded | `cb1-part4-records.l4` `the affidavit has the contents s 21(7) and s 21(8) require` | Where the applicant is a body corporate, a director or officer makes the affidavit. |
| s 21(9) | src:294-298 | encoded | `cb1-part4-records.l4` `the use of the list or information is permitted within s 21(9)`; `Use of a shareholder list or securities register information (s 21(9))` | Three permitted uses. |
| s 21(10) | src:299-300 | encoded | `cb1-part4-records.l4` `the person is guilty of an offence within s 21(10)`; `the most a court may impose on summary conviction within s 21(10)` | $5,000 or six months or both. |
| s 21.1(1) | src:301-312 | encoded | `cb1-part4-isc-register.l4` `Register of individuals with significant control as kept (s 21.1(1))`; `the register contains what s 21.1(1) requires` | One field per item (a)(i) to (f), the place, and the two conditions: an address for service provided, and other prescribed information existing. |
| s 21.1(2) | src:313-317 | encoded | `cb1-part4-isc-register.l4` `the corporation has taken the steps s 21.1(2) requires` | Three occasions: once a financial year, on the Director's request, at times the regulations provide. |
| s 21.1(3) | src:318-319 | encoded | `cb1-part4-isc-register.l4` `the last day to record the information in the register within s 21.1(3)`; `the corporation recorded the information in time within s 21.1(3)` | Fifteen days; the keel's counting (F1). |
| s 21.1(4) | src:320-321 | encoded | `cb1-part4-isc-register.l4` `the shareholder has complied with the duty to reply within s 21.1(4)` | A duty of the shareholder; "as soon as feasible" is a fact asked, not a number of days. |
| s 21.1(5) | src:322-323 | encoded | `cb1-part4-isc-register.l4` `the last day to dispose of the personal information within s 21.1(5)` | A MAYBE DATE: NOTHING if the individual has not ceased, or another Act provides a longer period. |
| s 21.1(6) | src:324-325 | encoded | `cb1-part4-isc-register.l4` `the corporation is guilty of an offence within s 21.1(6)`; `the most a court may impose on summary conviction within s 21.1(6)` | A fine not exceeding $100,000. |
| s 21.1(7) | src:326-330 | encoded | `cb1-part4-isc-register.l4` `section 21.1 applies to the corporation within s 21.1(7)` | Three limbs; this rule is "a corporation to which section 21.1 applies" in the sections below. |
| s 21.2 | src:331-332 | encoded | `cb1-part4-isc-register.l4` `the corporation has complied with the duty to take prescribed steps within s 21.2` | The steps are prescribed (not among the sources): whether they were taken is an input. |
| s 21.21(1) | src:333-336 | encoded | `cb1-part4-isc-register.l4` `the corporation has sent the annual information within s 21.21(1)(a)`; `the last day to send the recorded information to the Director within s 21.21(1)(b)`; `the corporation has sent the recorded information in time within s 21.21(1)(b)` | Paragraph (a): annually, in the form and within the period the Director fixes. Paragraph (b): fifteen days after the day it is recorded. |
| s 21.21(2) | src:337-338 | encoded | `cb1-part4-isc-register.l4` `the duty to send information to the Director has arisen within s 21.21(2)`; `the corporation has complied with the duty to send information on a certificate within s 21.21(2)` | On or after the date shown on a certificate under s 8, s 185(4) or s 187(4) (out of range, pieces cb1 and cb4). |
| s 21.21(3) | src:339-340 | encoded | `cb1-part4-isc-register.l4` `the Director is required to keep or produce the information on the day within s 21.21(3)` | Six years from the day the Director receives it. |
| s 21.21(4) | src:341-342 | encoded | `cb1-part4-isc-register.l4` `the corporation is guilty of an offence within s 21.21(4)`; `the most a court may impose on summary conviction within s 21.21(4)` | A fine not exceeding $100,000. |
| s 21.3(1) | src:343-344 | encoded | `cb1-part4-isc-register.l4` `the corporation must disclose the information in its register to the Director within s 21.3(1)` | "On request"; no time is stated. |
| s 21.3(2) | src:345 | repealed or blank in this text | - | `(2) [Repealed, 2023, c. 29, s. 3]` (src:345). |
| s 21.3(3) | src:346 | repealed or blank in this text | - | `(3) [Repealed, 2023, c. 29, s. 3]` (src:346). |
| s 21.3(4) | src:347 | repealed or blank in this text | - | `(4) [Repealed, 2023, c. 29, s. 3]` (src:347). |
| s 21.3(5) | src:348 | repealed or blank in this text | - | `(5) [Repealed, 2023, c. 29, s. 3]` (src:348). |
| s 21.3(6) | src:349 | repealed or blank in this text | - | `(6) [Repealed, 2023, c. 29, s. 3]` (src:349). |
| s 21.301 | src:350-351 | encoded | `cb1-part4-isc-register.l4` `the Director may provide the information received under section 21.21 to the recipient within s 21.301 and s 21.302`; `Recipient of information from the Director (s 21.301, s 21.302)` | A power of the Director; the rule says whether the Director may, never whether the Director will. |
| s 21.302 | src:352-353 | encoded | `cb1-part4-isc-register.l4` `the Director may provide the information received under section 21.21 to the recipient within s 21.301 and s 21.302` | The same rule as s 21.301, with the provincial recipients. |
| s 21.303(1) | src:354-360 | encoded | `cb1-part4-isc-register.l4` `the Director must make the item available to the public within s 21.303`; `Item of information about an individual with significant control (s 21.303(1))` | Paragraphs (a) to (e); paragraphs (b) and (c) turn on whether an address for service has been provided. |
| s 21.303(2) | src:361-362 | encoded | `cb1-part4-isc-register.l4` `the Director must make the item available to the public within s 21.303` | An individual under 18, or to whom prescribed circumstances apply. |
| s 21.303(3) | src:363-369 | encoded | `cb1-part4-isc-register.l4` `the Director may choose not to make the information available to the public within s 21.303(3)` | "May choose": a power of the Director, on application and on one of four grounds. |
| s 21.31(1) | src:370-373 | encoded | `cb1-part4-isc-register.l4` `the corporation must provide the copy of its register or disclose the specified information within s 21.31(1)` | "As soon as feasible" and "in the manner specified" are not modelled as numbers; the duty arises on a request served or deemed received (fork cb1-F5 on subsection (3)). |
| s 21.31(2) | src:374-378 | encoded | `cb1-part4-isc-register.l4` `the body is an investigative body for the purpose of s 21.31 within s 21.31(2)`; `Investigative body (s 21.31(2))` | Paragraphs (a) to (c). |
| s 21.31(3) | src:379-386 | encoded | `cb1-part4-isc-register.l4` `the investigative body may make the request within s 21.31(3)` | A limit on the body's power to make a request; see fork cb1-F5. |
| s 21.31(4) | src:387-388 | encoded | `cb1-part4-isc-register.l4` `the day the request is served or deemed received within s 21.31(4)` | A MAYBE DATE: served if left at the registered office; deemed received on mail delivery unless reasonable grounds for believing it did not arrive. |
| s 21.31(5) | src:389-390 | encoded | `cb1-part4-isc-register.l4` `the corporation is guilty of an offence within s 21.31(5)`; `the most a court may impose on summary conviction within s 21.31(5)` | A fine not exceeding $100,000. |
| s 21.31(6) | src:391-392 | inert | - | "The Governor in Council may, by order, amend the schedule by adding or deleting a reference to an offence." Machinery: a power of the Governor in Council to amend the schedule to which s 21.31(3) refers; it binds no corporation, director or shareholder, and the schedule is not among the sources. |
| s 21.32(1) | src:393-401 | encoded | `cb1-part4-isc-register.l4` `Record kept by an investigative body of a request (s 21.32(1))`; `the investigative body has kept the record s 21.32(1) requires` | Paragraphs (a) to (g). |
| s 21.32(2) | src:402-403 | encoded | `cb1-part4-isc-register.l4` `the last day for the investigative body to report to the Director within s 21.32(2)`; `the investigative body's report has the contents s 21.32(2) requires` | Ninety days after 31 December of the year of the request; the RCMP and the CRA add the count per province. |
| s 21.32(3) | src:404-405 | encoded | `cb1-part4-isc-register.l4` `section 251 applies to the contravention within s 21.32(3)` | A MAYBE BOOLEAN: JUST FALSE for a contravention of (1) or (2); NOTHING for any other, because s 251 (out of range, piece cb5) governs those. |
| s 21.4(1) | src:406-407 | encoded | `cb1-part4-isc-register.l4` `the director or officer commits an offence within s 21.4(1)` | "Whether or not the corporation has been prosecuted or convicted": the tests assert that it changes nothing. |
| s 21.4(2) | src:408-409 | encoded | `cb1-part4-isc-register.l4` `the director or officer commits an offence within s 21.4(2)` | Recording false or misleading information in the register. |
| s 21.4(3) | src:410-411 | encoded | `cb1-part4-isc-register.l4` `the director or officer commits an offence within s 21.4(3)` | Providing false or misleading information in relation to the register. |
| s 21.4(4) | src:412-413 | encoded | `cb1-part4-isc-register.l4` `the shareholder commits an offence within s 21.4(4)` | A shareholder who knowingly contravenes s 21.1(4). |
| s 21.4(5) | src:414-417 | encoded | `cb1-part4-isc-register.l4` `the most a court may impose within s 21.4(5)`; `Mode of prosecution (s 21.4(5))` | Summary conviction: $200,000 or two years or both. Indictment: $1,000,000 or five years or both. |
| s 22(1) | src:418-419 | encoded | `cb1-part4-records.l4` `the form of the record is permitted within s 22(1)`; `Form of a register or other record (s 22(1))` | The capability condition attaches to the data processing or storage device form. |
| s 22(2) | src:420-425 | encoded | `cb1-part4-records.l4` `the corporation or its agents or mandataries have taken the precautions s 22(2) requires` | Three precautions. |
| s 22(3) | src:426-427 | encoded | `cb1-part4-records.l4` `the person is guilty of an offence within s 22(3)`; `the most a court may impose on summary conviction within s 22(3)` | $5,000 or six months or both. |
| s 23(1) | src:428-429 | encoded | `cb1-part4-records.l4` `the corporation may adopt, and may change, a corporate seal within s 23(1)`; `the corporation must adopt a corporate seal within s 23(1)` | "May, but need not." |
| s 23(2) | src:430-431 | encoded | `cb1-part4-records.l4` `the document is invalid within s 23(2)` | "Merely because a corporate seal is not affixed": the other ground decides. |
| Heading: PART V Corporate Finance | src:433 | inert | - | A heading (a label for Part V); it states no rule and carries no condition. |
| s 24(1) | src:434-435 | encoded | `cb1-part5-shares.l4` `the share is as s 24(1) requires within s 24(1) and s 24(2)` | Registered form, and without nominal or par value. |
| s 24(2) | src:436-437 | encoded | `cb1-part5-shares.l4` `the share is as s 24(1) requires within s 24(1) and s 24(2)` | A pre-continuation share with a par value is deemed to be without one, for subsection (1). |
| s 24(3) | src:438-442 | encoded | `cb1-part5-shares.l4` `the holders of the only class have the right within s 24(3)`; `Right of a holder of shares (s 24(3))`; `the rights of the holders of the only class are as s 24(3) requires` | A MAYBE BOOLEAN: NOTHING where the subsection does not speak (more than one class, or a right it does not list). |
| s 24(4) | src:443-446 | encoded | `cb1-part5-shares.l4` `the articles meet the requirements for classes of shares within s 24(4)` | The three rights need only be on at least one class each; they need not all be on one class. |
| s 25(1) | src:447-448 | encoded | `cb1-part5-shares.l4` `the directors may determine the times, persons and consideration of an issue of shares within s 25(1)` | A power of the directors; what they decide is theirs. |
| s 25(2) | src:449-450 | encoded | `cb1-part5-shares.l4` `the holder is liable in respect of the share to the corporation or its creditors within s 25(2)` | JUST FALSE for an issued share. |
| s 25(3) | src:451-452 | encoded | `cb1-part5-shares.l4` `the share may be issued for the consideration within s 25(3)`; `Kind of consideration for a share (s 25(3))` | Fully paid, in money or in property or past services not less in value than the fair equivalent. |
| s 25(4) | src:453-454 | encoded | `cb1-part5-shares.l4` `the directors may take the item into account in determining the fair equivalent within s 25(4)`; `Item the directors may take into account (s 25(4))` | A MAYBE BOOLEAN: NOTHING for an item the subsection does not mention. |
| s 25(5) | src:455-456 | encoded | `cb1-part5-shares.l4` `the thing is property for the purposes of s 25 within s 25(5)` | A promissory note or promise to pay by the person to whom a share is issued, or by a person not at arm's length with them, is not property. |
| s 26(1) | src:457-458 | encoded | `cb1-part5-shares.l4` `the corporation has complied with the duty to maintain stated capital accounts within s 26(1)` | One account for each class and series. |
| s 26(2) | src:459-460 | encoded | `cb1-part5-shares.l4` `the amount added to the stated capital account is permitted within s 26(2), s 26(3) and s 26(4)` | The full amount of the consideration. |
| s 26(3) | src:461-467 | encoded | `cb1-part5-shares.l4` `the corporation may add less than the full consideration within s 26(3)`; `Exchange in which shares are issued (s 26(3))` | Paragraphs (a)(i), (ii), (iii) and (b). Out of range: s 182(1) and s 192(1)(b) or (c) (piece cb4) are named in an exchange's label only. |
| s 26(4) | src:468-469 | encoded | `cb1-part5-shares.l4` `the amount added to the stated capital account is permitted within s 26(2), s 26(3) and s 26(4)` | Never more than the consideration received. |
| s 26(5) | src:470-474 | encoded | `cb1-part5-shares.l4` `the addition must be approved by special resolution within s 26(5)`; `the addition has the approval s 26(5) requires` | Calls the keel's `special resolution within s 2(1)`. The reference to s 39(5) is in range (convertible shares). |
| s 26(6) | src:475-476 | encoded | `cb1-part5-shares.l4` `the corporation may add the amount to a stated capital account within s 26(6)`; `Amount a corporation proposes to add to a stated capital account (s 26(6))` | A MAYBE BOOLEAN: NOTHING for an amount the subsection does not mention. |
| s 26(7) | src:477-478 | encoded | `cb1-part5-shares.l4` `subsection 26(2) applies to the consideration within s 26(7)` | Transitional, for a continued body corporate. |
| s 26(8) | src:479-480 | encoded | `cb1-part5-shares.l4` `the corporation must add the amount to the stated capital account for the class or series within s 26(8)` | Transitional, for a continued body corporate. |
| s 26(9) | src:481-482 | encoded | `cb1-part5-shares.l4` `the stated capital of the body corporate for the purposes of s 34(2), s 38, s 42 and paragraph 185(2)(a) within s 26(9)` | "Deemed to include": read as a floor (fork cb1-F6). |
| s 26(10) | src:483-484 | encoded | `cb1-part5-shares.l4` `the corporation may reduce its stated capital or a stated capital account within s 26(10)` | Only in a manner provided in the Act. |
| s 26(11) | src:485-486 | encoded | `cb1-part5-shares.l4` `the stated capital provisions of this Act apply to the corporation within s 26(11)` | An open-end mutual fund is outside them. |
| s 26(12) | src:487-488 | encoded | `cb1-part5-shares.l4` `the corporation is an open-end mutual fund within s 26(12)` | Three facts. |
| s 27(1) | src:489-492 | encoded | `cb1-part5-shares.l4` `the articles may authorize the issue of a class of shares in series in that way within s 27(1)`; `Way of fixing the terms of a series (s 27(1))` | Paragraphs (a) and (b); "either or both". |
| s 27(2) | src:493-494 | encoded | `cb1-part5-shares.l4` `the amount this series receives within s 27(2)` | A MAYBE NUMBER: pro rata to the amounts owing, never more than owed; NOTHING where nothing is owed to any series. |
| s 27(3) | src:495-496 | encoded | `cb1-part5-shares.l4` `the rights attached to the series are permitted within s 27(3)` | No priority over another outstanding series of the same class. |
| s 27(4) | src:497-498 | encoded | `cb1-part5-shares.l4` `the directors have complied with the duty to send articles of amendment before the issue within s 27(4)` | "Before the issue": the day of sending is strictly earlier than the day of issue. The form is the Director's to fix. |
| s 27(5) | src:499-500 | encoded | `cb1-part5-shares.l4` `the Director must issue a certificate of amendment within s 27(5)` | "In accordance with section 262" is out of range (piece cb5). |
| s 27(6) | src:501-502 | encoded | `cb1-part5-shares.l4` `the articles are amended by the certificate of amendment by the day within s 27(6)` | From the date shown, that day included. |
| s 28(1) | src:503-504 | encoded | `cb1-part5-shares.l4` `shareholders of the class have a pre-emptive right in respect of the shares within s 28(1) and s 28(2)`; `the number of the offered shares the shareholder has a pre-emptive right to acquire within s 28(1)`; `the shares of the class may be issued within s 28(1)` | Only if the articles so provide; in proportion to holdings. |
| s 28(2) | src:505-509 | encoded | `cb1-part5-shares.l4` `shareholders of the class have a pre-emptive right in respect of the shares within s 28(1) and s 28(2)`; `Issue of shares (s 28(2))` | Three exceptions: non-money consideration, share dividend, exercise of conversion privileges, options or rights. |
| s 29(1) | src:510-513 | encoded | `cb1-part5-shares.l4` `the corporation has set out the conditions as s 29(1) requires` | In the certificates, warrants or other evidences, or in the certificates for the securities they attach to. |
| s 29(2) | src:514-515 | encoded | `cb1-part5-shares.l4` `the instrument may be made transferable or non-transferable within s 29(2)`; `the instrument may be made separable or inseparable from the securities to which it is attached within s 29(2)`; `Instrument under s 29(2)` | Separable or inseparable is said of options and rights only: NOTHING for a conversion privilege. |
| s 29(3) | src:516-517 | encoded | `cb1-part5-shares.l4` `the corporation has reserved sufficient authorized shares within s 29(3)` | Only if the articles limit the number of authorized shares. |
| s 29.1(1) | src:518-519 | encoded | `cb1-part5-shares.l4` `the corporation is forbidden to issue the document within s 29.1(1)` | Bearer form; "despite section 29". |
| s 29.1(2) | src:520-521 | encoded | `cb1-part5-shares.l4` `the corporation must issue a registered document in exchange within s 29.1(2)` | The day section 29.1 came into force is not in the text: whether the document was issued before it is a plain fact. |
| s 30(1) | src:522-525 | encoded | `cb1-part5-own-shares.l4` `the corporation may hold shares in itself or in its holding body corporate within s 30(1)(a)`; `the corporation may permit a subsidiary body corporate to acquire shares of the corporation within s 30(1)(b)` | Subject to subsection (2) and sections 31 to 36: the holding or acquisition is permitted where one of the exceptions in s 31 or s 32 applies. The keel defines "holding body corporate" (s 2(4)) and "subsidiary" (s 2(5)). |
| s 30(2) | src:526-529 | encoded | `cb1-part5-own-shares.l4` `the last day for the subsidiary to dispose of the shares within s 30(2)` | Five years from the later of the two dates (fork cb1-F8); NOTHING where s 31 permits the holding. |
| s 31(1) | src:530-531 | encoded | `cb1-part5-own-shares.l4` `section 31(1) permits the corporation to hold the shares` | A personal representative, unless a beneficial interest. |
| s 31(2) | src:532-533 | encoded | `cb1-part5-own-shares.l4` `section 31(2) permits the corporation to hold the shares` | Security in the ordinary course of a business that includes lending. |
| s 31(3) | src:534-537 | encoded | `cb1-part5-own-shares.l4` `section 31(3) permits the corporation to permit the subsidiary to acquire the shares` | Paragraphs (a) and (b). |
| s 31(4) | src:538-539 | encoded | `cb1-part5-own-shares.l4` `section 31(4) permits the corporation to permit the subsidiary to acquire the shares` | The prescribed conditions precedent are an input. |
| s 31(5) | src:540-541 | encoded | `cb1-part5-own-shares.l4` `the conditions subsequent of s 31(5) are satisfied` | The prescribed conditions subsequent are an input. |
| s 31(6) | src:542-548 | encoded | `cb1-part5-own-shares.l4` `the prescribed consequences apply to the acquisition and issuance within s 31(6)` | The consequences are prescribed: the rule says whether they apply. |
| s 32(1) | src:549-552 | encoded | `cb1-part5-own-shares.l4` `section 32(1) permits the corporation to hold the shares` | Subject to s 39(8) (in this piece, in the next module): an input here. |
| s 32(2) | src:553-554 | encoded | `cb1-part5-own-shares.l4` `the corporation may transfer the shares held under subsection 32(1) within s 32(2)` | The corporation's satisfaction on reasonable grounds is an input. |
| s 32(3) | src:555-556 | encoded | `cb1-part5-own-shares.l4` `the corporation is guilty of an offence within s 32(3)`; `the most a court may impose on a corporation on summary conviction within s 32(3)` | A fine not exceeding $5,000. |
| s 32(4) | src:557-558 | encoded | `cb1-part5-own-shares.l4` `the director is a party to and guilty of the offence within s 32(4)`; `the most a court may impose on a director on summary conviction within s 32(4)` | $5,000 or six months or both; whether or not the corporation has been prosecuted or convicted. |
| s 32(5) | src:559-560 | encoded | `cb1-part5-own-shares.l4` `the transfer is treated as an issue of shares within s 32(5)` | A deeming rule; the sections applied (s 25(1), (3), (4), (5), s 115(3)(c), s 118(1)) are named only. |
| s 32(6) | src:561-562 | encoded | `cb1-part5-own-shares.l4` `the transfer of shares is void, voidable or null within s 32(6)` | "Solely because": the other ground decides. |
| s 33(1) | src:563-566 | encoded | `cb1-part5-own-shares.l4` `the shares may be voted or permitted to be voted within s 33(1)` | Personal representative capacity and compliance with s 153 (out of range, piece cb3). |
| s 33(2) | src:567-568 | encoded | `cb1-part5-own-shares.l4` `the subsidiary may vote or be permitted to vote the shares within s 33(2)` | The subsidiary must satisfy subsection (1). |
| s 34(1) | src:569-570 | encoded | `cb1-part5-own-shares.l4` `the corporation may purchase or otherwise acquire shares issued by it within s 34(1)` | Subject to subsection (2) and the articles. |
| s 34(2) | src:571-574 | encoded | `cb1-part5-own-shares.l4` `the corporation is forbidden to make the payment to acquire its shares within s 34(2)` | Two limbs, over the shared solvency record (fork cb1-F7 on "reasonable grounds"). |
| s 35(1) | src:575-579 | encoded | `cb1-part5-own-shares.l4` `the corporation may purchase or acquire shares issued by it for the purpose within s 35(1) and s 35(2)`; `Purpose of an acquisition of the corporation's own shares (s 35)` | Paragraphs (a) to (c), subject to subsection (3) and the articles. |
| s 35(2) | src:580-583 | encoded | `cb1-part5-own-shares.l4` `the corporation may purchase or acquire shares issued by it for the purpose within s 35(1) and s 35(2)` | Paragraphs (a) and (b); the subsection is subject to neither the articles nor subsection (3). |
| s 35(3) | src:584-589 | encoded | `cb1-part5-own-shares.l4` `the corporation is forbidden to make the payment to acquire its shares under s 35(1) within s 35(3)` | The limb on assets has no stated capital term, and adds the amount owed to holders to be paid before. |
| s 36(1) | src:590-591 | encoded | `cb1-part5-own-shares.l4` `the corporation may purchase or redeem the shares at the price within s 36(1)` | Redeemable shares, at a price not above the redemption price. |
| s 36(2) | src:592-597 | encoded | `cb1-part5-own-shares.l4` `the corporation is forbidden to make the payment to purchase or redeem redeemable shares within s 36(2)` | The limb on assets adds the amount owed to holders to be paid rateably with or before. |
| s 37 | src:598-599 | encoded | `cb1-part5-own-shares.l4` `the corporation may accept the share within s 37`; `the corporation may extinguish or reduce the liability within s 37` | Accepting a gift; no extinguishing or reducing a liability on the share except as s 38 allows. |
| s 38(1) | src:600-604 | encoded | `cb1-part5-capital-dividends.l4` `the corporation may reduce its stated capital within s 38(1)`; `Purpose of a reduction of stated capital (s 38(1))`; `the distribution is within the limit of s 38(1)(b)` | By special resolution (the keel's `special resolution within s 2(1)`), subject to subsection (3). Paragraph (b) limits a distribution to the stated capital of the class or series. |
| s 38(2) | src:605-606 | encoded | `cb1-part5-capital-dividends.l4` `the special resolution has the contents s 38(2) requires` | The stated capital account or accounts to be reduced. |
| s 38(3) | src:607-610 | encoded | `cb1-part5-capital-dividends.l4` `the corporation is forbidden to reduce its stated capital within s 38(3)` | Two limbs; no stated capital term; the purpose of paragraph (1)(c) is outside the limit (fork cb1-F7 on "reasonable grounds"). |
| s 38(4) | src:611-614 | encoded | `cb1-part5-capital-dividends.l4` `the creditor is entitled to apply to a court for the order within s 38(4)`; `Order a creditor may seek under s 38(4)` | A creditor's right to apply; the court's order is the court's. |
| s 38(5) | src:615-616 | encoded | `cb1-part5-capital-dividends.l4` `the last day to commence an action to enforce a liability imposed by section 38 within s 38(5)`; `the action to enforce a liability imposed by section 38 is in time within s 38(5)` | Two years from the date of the act complained of. |
| s 38(6) | src:617 | repealed or blank in this text | - | `(6) [Repealed, 2001, c. 14, s. 23]` (src:617). |
| s 39(1) | src:618-619 | encoded | `cb1-part5-capital-dividends.l4` `the amount to deduct from the stated capital account on an acquisition within s 39(1)` | A MAYBE NUMBER: NOTHING where no shares were issued. The list "section 34, 35, 36, 45 or 190 or paragraph 241(3)(f)" is copied as the text has it. |
| s 39(2) | src:620-621 | encoded | `cb1-part5-capital-dividends.l4` `the balance of the stated capital account after the payment within s 39(2)` | A payment under paragraph 241(3)(g) (out of range, piece cb4). |
| s 39(3) | src:622-623 | encoded | `cb1-part5-capital-dividends.l4` `the corporation must adjust its stated capital accounts in accordance with the special resolution within s 39(3)` | A duty that follows a special resolution under s 38(2). |
| s 39(4) | src:624-627 | encoded | `cb1-part5-capital-dividends.l4` `the amount to deduct on a conversion or change within s 39(4)(a)`; `the amount to add on a conversion or change within s 39(4)(b)` | A MAYBE NUMBER: NOTHING where no shares were issued. |
| s 39(5) | src:628-629 | encoded | `cb1-part5-capital-dividends.l4` `the corporation has two classes of convertible shares referred to in s 39(5)`; `the stated capital attributable to a share in either class within s 39(5)` | "Subject to its articles": NOTHING where the articles provide otherwise. The first rule is what s 26(5) refers to. |
| s 39(6) | src:630-631 | encoded | `cb1-part5-capital-dividends.l4` `what becomes of the acquired shares within s 39(6)`; `What becomes of shares a corporation has acquired (s 39(6))` | Cancelled, or, if the articles limit the authorized shares, may be restored. |
| s 39(7) | src:632-633 | encoded | `cb1-part5-capital-dividends.l4` `the corporation is deemed not to have purchased, redeemed or otherwise acquired the shares for the purposes of s 39 within s 39(7)` | Shares held as permitted by s 31(1) and (2). |
| s 39(8) | src:634-638 | encoded | `cb1-part5-capital-dividends.l4` `the day the shares are deemed to have been acquired within s 39(8)` | A MAYBE DATE: two years from the day the shares (or the shares from which they were converted) were acquired, if still held then. |
| s 39(9) | src:639-640 | encoded | `cb1-part5-capital-dividends.l4` `the shares become issued shares of the class or series into which they were converted or changed within s 39(9)` | A deeming rule. |
| s 39(10) | src:641-642 | encoded | `cb1-part5-capital-dividends.l4` `the number of unissued shares of the first class after the change within s 39(10)` | A MAYBE NUMBER: NOTHING where the articles do not limit the authorized shares, or otherwise provide. |
| s 39(11) | src:643-644 | encoded | `cb1-part5-capital-dividends.l4` `the debt obligations are redeemed within s 39(11)` | "By reason only": the other ground decides. |
| s 39(12) | src:645-646 | encoded | `cb1-part5-capital-dividends.l4` `the corporation may reissue, pledge or hypothecate the acquired debt obligations within s 39(12)`; `the acquisition and reissue, pledge or hypothecation is a cancellation of the debt obligations within s 39(12)` | Subject to any applicable trust indenture or other agreement; the reissue is not a cancellation. |
| s 40(1) | src:647-648 | encoded | `cb1-part5-capital-dividends.l4` `the corporation must fulfil its obligations under the contract to buy shares within s 40(1)` | Unless the corporation can prove that enforcement would breach s 34, 35 or 36. |
| s 40(2) | src:649-650 | encoded | `cb1-part5-capital-dividends.l4` `the claimant ranks in priority to the person in a liquidation within s 40(2)`; `Person ranked against the claimant in a liquidation (s 40(2))`; `the other party is entitled to be paid within s 40(2)` | A MAYBE BOOLEAN for the ranking: NOTHING for anyone the subsection does not name. |
| s 41 | src:651-652 | encoded | `cb1-part5-capital-dividends.l4` `the directors may authorize the corporation to pay the commission within s 41` | A power of the directors. |
| s 42 | src:653-656 | encoded | `cb1-part5-capital-dividends.l4` `the corporation is forbidden to declare or pay a dividend within s 42` | Two limbs, with the stated capital term nil for an open-end mutual fund (fork cb1-F9; fork cb1-F7 on "reasonable grounds"). |
| s 43(1) | src:657-658 | encoded | `cb1-part5-capital-dividends.l4` `the corporation may pay the dividend in that form within s 43(1)`; `Form of a dividend (s 43(1))` | s 42 is read to reach a share dividend too (fork cb1-F10). |
| s 43(2) | src:659-660 | encoded | `cb1-part5-capital-dividends.l4` `the amount to add to the stated capital account for the class or series issued within s 43(2)` | A MAYBE NUMBER: NOTHING when no shares are issued in payment. |
| s 44 | src:661 | repealed or blank in this text | - | `44 [Repealed, 2001, c. 14, s. 26]` (src:661). |
| s 45(1) | src:662-663 | encoded | `cb1-part5-capital-dividends.l4` `section 45(1) shields the shareholder from the liability within s 45(1)`; `Basis on which a shareholder is said to be liable for the corporation's liability, act or default (s 45(1))` | The exceptions are in s 38(4), 118(4) or (5), 146(5) and 226(4) or (5) (the last three out of range). |
| s 45(2) | src:664-665 | encoded | `cb1-part5-capital-dividends.l4` `the articles may provide that the corporation has a lien or hypothec on the share within s 45(2)` | Subject to s 49(8) (out of range, piece cb2): an input. |
| s 45(3) | src:666-667 | encoded | `cb1-part5-capital-dividends.l4` `the corporation may enforce the lien or hypothec within s 45(3)` | In accordance with its by-laws. |
| Heading: PART VI Sale of Constrained Shares | src:669 | inert | - | A heading (a label for Part VI); it states no rule and carries no condition. |
| s 46(1) | src:670-674 | encoded | `cb1-part6-constrained-shares.l4` `the corporation may sell the constrained shares as if it were their owner within s 46(1)`; `Purpose of a sale of constrained shares (s 46(1))` | A power of the corporation; the conditions, the notice and the manner of the directors' determination are prescribed (inputs). |
| s 46(2) | src:675-676 | encoded | `cb1-part6-constrained-shares.l4` `the directors have complied with the duty in selecting the shares for sale within s 46(2)` | Good faith; not unfairly prejudicial; not unfairly disregarding. |
| s 46(3) | src:677-678 | encoded | `cb1-part6-constrained-shares.l4` `the owner immediately before the sale is divested of their interest or right in the shares within s 46(3)`; `what the person who would otherwise be the registered owner receives within s 46(3)`; `the person is entitled to receive only the net proceeds of the sale within s 46(3)` | Divestment; the net proceeds with income, less taxes and costs. The reference to s 51 is out of range (piece cb2). |
| s 46(4) | src:679-680 | encoded | `cb1-part6-constrained-shares.l4` `subsections 51(4) to (6) apply to the person as if the proceeds were a security and the person were a registered holder or owner within s 46(4)` | A deeming rule; s 51(4) to (6) are out of range (piece cb2). |
| s 47(1) | src:681-682 | encoded | `cb1-part6-constrained-shares.l4` `the proceeds constitute a trust fund in the hands of the corporation within s 47(1)`; `the trust fund has been invested as s 47(1) requires` | The manner of investing is prescribed (an input). |
| s 47(2) | src:683-684 | encoded | `cb1-part6-constrained-shares.l4` `the corporation may deduct the costs from the trust fund and any income earned thereon within s 47(2)` | Reasonable costs of administration. |
| s 47(3) | src:685-686 | encoded | `cb1-part6-constrained-shares.l4` `the corporation may transfer the trust fund and its administration to the transferee within s 47(3)`; `the corporation is discharged of all further liability in respect of the trust fund within s 47(3)` | A trust company in Canada registered under the laws of Canada or a province. |
| s 47(4) | src:687-688 | encoded | `cb1-part6-constrained-shares.l4` `the receipt is a complete discharge of the corporation and of any trust company within s 47(4)` | A receipt signed by a person entitled under s 46(3). |
| s 47(5) | src:689-690 | encoded | `cb1-part6-constrained-shares.l4` `the last day the fund can be claimed before it vests in the Crown within s 47(5)`; `the fund has vested in Her Majesty in right of Canada on the day within s 47(5)` | Ten years after the date of the sale, counted by the keel's convention (F1). |
| s 47(6) | src:691-692 | encoded | `cb1-part6-constrained-shares.l4` `sections 3 to 5 of the Escheats Act apply to the fund within s 47(6)` | A deeming rule; the Escheats Act is not among the sources. |

## Fork register

Every ambiguity I met in the range: the readings I saw, the one I took, and the text that licenses each.
None is resolved by a court or the regulator that I know of; none is settled by anything in the sources.
Where I looked: every subsection of s 3 to s 47 was read twice, and each place where the text says "or" between conditions, "may" or "shall", "subject to", "notwithstanding", a time limit, "reasonable grounds", or refers to a provision outside my ranges was checked for a second reading.

### F1. How days are counted in a time limit (the keel's fork)

The Act's own text does not say how a day is counted ("within 15 days after"): the Interpretation Act is not among the sources.
Readings: the start day is day 0 and the last day is included, or the start day is day 1, or the last day is excluded.
Taken: the keel's convention, the start day is day 0 and the last day is included (`the last day of ... counted from ...` in `cbca-core.l4`).
Where it bites in this range: s 11(1), s 12(5) (rules with a prescribed period), s 19, s 21, s 21.1 and every other time limit below.
Licence: none in the text; the keel's comment records it as F1.

### cb1-F1. Who may sign under s 5(1)

"One or more individuals or bodies corporate may incorporate a corporation by signing articles of incorporation" (src:140).
Readings: (1) only individuals and bodies corporate count as signers, so a signing partnership or trust is not addressed and is not counted; (2) any person who signs counts.
Taken: (1).
The rule takes two counts (individuals and bodies corporate) and asks whether their sum is one or more; a signer of another kind is simply not in either count.
Licence: the subsection names exactly two kinds of signer.

### cb1-F2. Does s 6(4) limit a unanimous shareholder agreement?

Section 6(3) lets "the articles or a unanimous shareholder agreement" require a greater number of votes; "subject to subsection (4)" (src:159).
Subsection (4) says "The articles may not require a greater number of votes of shareholders to remove a director than the number required by section 109" (src:161); it names the articles and not an agreement.
Readings: (1) s 6(4) caps only the articles, so an agreement may require more to remove a director; (2) s 6(4) caps both.
Taken: (1), because (4) names only the articles and (3) names the agreement separately.
Licence: src:159 and src:161.

### cb1-F3. The three conditions of s 5(2) are cumulative

"An individual may incorporate a corporation only if that individual (a) is not less than 18 years of age; (b) is not incapable; or (c) does not have the status of bankrupt" (src:142-145).
Readings: (1) the three are all required (the "or" joins the last of a list of conditions each a necessary one); (2) any one suffices, so a 17-year-old who is not incapable and not bankrupt qualifies.
Taken: (1): under (2) paragraph (a) would never exclude anyone who met (b) or (c), and "only if" signals a necessary condition.
Licence: "only if" at src:142.

### cb1-F4. Which abbreviation corresponds to which full form in s 10(1)

The text lists six full forms ("Limited", "Limitée", "Incorporated", "Incorporée", "Corporation", "Société par actions de régime fédéral") and five abbreviations ("Ltd.", "Ltée", "Inc.", "Corp.", "S.A.R.F.") (src:171).
Readings: (1) "Inc." corresponds to both "Incorporated" and "Incorporée"; (2) "Inc." corresponds to "Incorporated" only, and "Incorporée" has none.
Taken: (1), the one that leaves no full form without an abbreviation.
Licence: src:171 (the order of the two lists).

### cb1-F5. Does s 21.31(3) condition the corporation's duty under s 21.31(1)?

Subsection (1): "On request by an investigative body referred to in subsection (2), a corporation to which section 21.1 applies shall, as soon as feasible ... provide ... or disclose" (src:371).
Subsection (3): "An investigative body may make a request only if it has reasonable grounds to suspect ..." (src:380).
Readings: (1) the duty arises on any request by a body listed in (2), and (3) limits what the body may do (it is the body's power that is limited, and the corporation is not asked to test it); (2) the duty arises only on a request that meets (3), so a corporation may decline one that does not.
Taken: (1): the words of (1) turn on the body and the request, and (3) is addressed to the body ("may make a request only if"). Under (1) a corporation that doubts the grounds still has to comply, and the offence in (5) lies for contravening (1) "without reasonable cause".
Licence: src:371 and src:380.

### cb1-F6. What "deemed to include" means in s 26(9)

"For the purposes of subsection 34(2), sections 38 and 42, and paragraph 185(2)(a), when a body corporate is continued under this Act its stated capital is deemed to include the amount that would have been included in stated capital if the body corporate had been incorporated under this Act" (src:482).
Readings: (1) the stated capital for those purposes is at least that amount: it is the larger of what the accounts show and what would have been included; (2) the amount is added to what the accounts show; (3) the stated capital for those purposes is exactly that amount, whatever the accounts show.
Taken: (1): "include" speaks of a floor, and adding (2) would count the same consideration twice for a body corporate whose accounts already carry it.
Licence: src:482.

### cb1-F7. What "reasonable grounds for believing" is in the solvency tests (s 34(2), s 35(3), s 36(2), s 38(3), s 42)

Each test forbids a step "if there are reasonable grounds for believing" (a) that the corporation is or would after the step be unable to pay its liabilities as they become due, or (b) that the realizable value of its assets after the step would be less than a sum.
Readings: (1) the corporation's honest and reasonable estimate of the figures is the ground: where those figures show the shortfall, there are reasonable grounds, and where they show none, there are not; (2) reasonable grounds can exist for believing a shortfall although the best-estimate figures show none (for example, material uncertainty in the estimate).
Taken: (1) for limb (b), which is arithmetic over the figures; limb (a) is a plain yes or no that the person assessing the corporation supplies, because "unable to pay as they become due" is a judgement the Act hands to that person.
Licence: src:572-574, 585-589, 593-597, 608-610 and 654-656 (the text names "reasonable grounds for believing" and no method).

### cb1-F8. Which date starts the five years in s 30(2)

"... within five years from the date (a) the body corporate became a subsidiary of the corporation; or (b) the corporation was continued under this Act" (src:527-529).
Readings: (1) from the later of the two dates when both have happened; (2) from the earlier; (3) from (a) in every case, and from (b) only where the body corporate was already a subsidiary.
Taken: (1): the prohibition first bites on the later event (before it, either the body corporate was not a subsidiary or the corporation was not under this Act), and the time to dispose should not run before the holding was forbidden. A corporation that was never continued has only (a).
Licence: src:527-529.

### cb1-F9. Does s 26(11) take the stated capital term out of the dividend and purchase tests for an open-end mutual fund?

Section 26(11): "Subsections (1) to (10) and any other provisions of this Act relating to stated capital do not apply to an open-end mutual fund" (src:486).
Sections 34(2)(b) and 42(b) compare the assets with "the aggregate of its liabilities and stated capital of all classes" (src:574, 656).
Readings: (1) those two limbs are provisions "relating to stated capital", so for an open-end mutual fund the stated capital term is nil and the limb compares assets with liabilities; (2) they are not, and the test applies to an open-end mutual fund as written, with whatever stated capital it has.
Taken: (1): the limb's only reason for mentioning stated capital is that the corporation keeps stated capital accounts, which s 26(11) says an open-end mutual fund does not.
Licence: src:486, 574 and 656.

### cb1-F10. Does s 42 reach a dividend paid by issuing shares?

"A corporation may pay a dividend by issuing fully paid shares of the corporation and, subject to section 42, a corporation may pay a dividend in money or property" (src:658). Section 42 says "A corporation shall not declare or pay a dividend if ..." (src:654).
Readings: (1) section 42 forbids every dividend, including one paid in shares, and "subject to section 42" in s 43(1) only repeats that for money and property; (2) the words "subject to section 42" attach to money and property alone, so a dividend in shares is not caught by s 42.
Taken: (1): s 42 speaks of "a dividend" without limit, and a permission to choose the form of payment is not a release from the prohibition.
Licence: src:654 and 658.

### cb1-F11. A longer retention period under another Act: s 20(2.1) and s 21.1(5)

Both subsections are "subject to any other Act of Parliament and to any Act of the legislature of a province that provides for a longer retention period" (src:258, src:323).
Readings: (1) the other Act's period replaces the Act's own period and is counted from the same starting point, so the last day is the later of the two; (2) once another Act applies, this Act names no day at all.
Taken: (1) for s 20(2.1), where the period is six years counted from the end of the financial year: the person supplies the other Act's period, and the rule counts it from the same day and keeps the later day.
Taken: (2) for s 21.1(5), where the day is one year after the sixth anniversary of the day the individual ceased: s 21.1(5) names no starting point for the other Act's period, so the rule takes only whether another Act provides a longer period, and returns `NOTHING` when it does.
The two readings differ because the two provisions give different starting points to build on; a reader who prefers one reading for both can make the change in two rules.
Licence: src:258 and src:323.

## Cross-references out of my ranges

Every reference to a provision outside my ranges that is taken as a plain input is named for the fact and carries the comment `-- out of range: section N (piece X)` (or the source in place of the section and piece, for the regulations and other Acts) on the line that declares the input.
A reference that is only named in a label, or not modelled, has no input and so no comment; the table says which.
The table has 65 rows. Thirteen of them (piece "this piece") link two of my own modules, and are kept because each is an input the seat passes in or a rule-to-rule link a reader will look for; the other 52 point out of my ranges.
Pieces: cb2 = ss 48-125; cb3 = ss 126-172.1; cb4 = ss 173-228; cb5 = ss 229-268 and the Schedule; keel = s 2 and s 2.1.

| your provision | the provision it depends on | its piece | the input you made |
| --- | --- | --- | --- |
| s 3(3)(c) | section 87 of the Canada Transportation Act (definition of "Special Act") | outside the Act | `the provision of the Special Act is inconsistent with this Act` |
| s 3(4) | the Cooperative Credit Associations Act, the Insurance Companies Act and the Trust and Loan Companies Act (the text names them for the businesses of an association, a company or society, and a company; "a bank" is named without an Act) | outside the Act | the businesses in `Business a corporation may not carry on under s 3(4)` |
| s 6(1)(e) | s 107(a) | cb2 | `paragraph 107(a) allows a minimum and maximum number of directors` |
| s 6(4) | s 109 | cb2 | `the fraction of the votes of shareholders that section 109 requires to remove a director` |
| s 7 | s 19 (the notice of registered office, s 19(2)) | this piece | `the incorporator sent the notice of registered office that section 19 requires`: the notice is a thing sent, so it is a fact, not a computed value |
| s 7 | s 106 | cb2 | `the incorporator sent the notice of directors that section 106 requires` |
| s 8(1) | s 262 (the form of the certificate) | cb5 | not made an input: the rule says the Director must issue, and the form is no part of whether |
| s 8(2) | s 19(2) and s 106(1) (the notices) | this piece and cb2 | `a notice required under subsection 19(2) or 106(1) indicates that the corporation, if it came into existence, would not be in compliance with this Act` |
| s 10(1.1) | the day s 10(1.1) came into force | not in the text | `the name immediately before the day subsection 10(1.1) came into force included "Société commerciale canadienne" or "S.C.C." other than only in a figurative or descriptive sense` |
| s 10(3), (4), (6), s 11(1), s 12(1) to (5) | the regulations ("prescribed", "prohibited by the regulations") | not among the sources | `the combined form meets the prescribed criteria`, `the prescribed period of reservation`, `the name is prohibited by the regulations`, `the name meets the prescribed requirements`, `the prescribed period for following the directive` |
| s 12(2), (4), (4.1) | s 173 (change of name) | cb4 | not made an input: the rules say the Director may direct, and the procedure is s 173's |
| s 12(5) | s 173 | cb4 | `the name has since been changed in accordance with section 173` |
| s 15(1), s 15(2) | "subject to this Act" | the Act as a whole | `a provision of this Act takes the right, power or privilege away from the corporation` |
| s 18(1)(b) | s 106 and s 113 (notices to the Director of directors) | cb2 | not made an input: the notices are only named in the text of an assertion |
| s 18(1)(c) | s 19 (notice of registered office) | this piece | not made an input: only named in the text of an assertion |
| s 18(1)(f) | s 189(3) (sale, lease or exchange of property) | cb4 | not made an input: only named in the text of an assertion |
| s 19(2) | the form the Director fixes | not among the sources | not modelled |
| s 20(1)(c) | s 106 and s 113 | cb2 | `copies of all notices required by section 106 or 113` (a field of the record) |
| s 20(1)(d) | s 50 (securities register) | cb2 | `a securities register that complies with section 50` (a field of the record) |
| s 20(2.1) | other Acts of Parliament and provincial Acts that provide a longer retention period | outside the Act | `the longer retention period that another Act of Parliament or a provincial Act provides, if there is one` (a `MAYBE` time limit) |
| s 21.1(5) | the same | outside the Act | `another Act provides for a longer retention period` (yes or no; the rule then gives no day, fork cb1-F11) |
| s 20(5.1) | the Income Tax Act, the Excise Tax Act, the Customs Act and other Acts administered by the Minister of National Revenue | outside the Act | `an Act administered by the Minister of National Revenue requires the records to be kept in Canada` |
| s 21(1.1), s 21(3) | s 21(7) (the affidavit) | this piece | `the person has made a request accompanied by an affidavit referred to in subsection 21(7)`, `the person has sent the corporation or its agent or mandatary the affidavit referred to in subsection 21(7)`: the affidavit's own content is the rule `the affidavit has the contents s 21(7) and s 21(8) require` |
| s 21(1), s 21(3) | "distributing corporation" (s 2(1), the keel) | keel | `the corporation is a distributing corporation` |
| s 21(5) | "business day" (not defined in the text) | not in the sources | `the business day following the day to which the supplemental list relates` |
| s 21.1(1), s 21.1(2) | "individual with significant control" (s 2.1) | keel | `it contains the name and date of birth of each individual with significant control` and the other fields of the register record: who is such an individual is not computed here |
| s 21.1(1)(e), s 21.1(2)(c), s 21.1(7)(c), s 21.2, s 21.32(1)(g), s 21.303(1)(e), (2), (3)(b)(iii) | the regulations ("prescribed") | not among the sources | `there is other prescribed information`, `a time is provided for in the regulations`, `the corporation is a member of a prescribed class`, `the corporation took the prescribed steps`, `prescribed circumstances apply to the individual` |
| s 21.1(5) | s 2(1) of the Personal Information Protection and Electronic Documents Act (personal information) | outside the Act | not modelled: the rule disposes of "that individual's personal information"; which items count is that Act's |
| s 21.1(7)(a), (b) | a provincial securities Act; s 248(1) of the Income Tax Act (designated stock exchange) | outside the Act | `the corporation is a reporting issuer or an émetteur assujetti under an Act of the legislature of a province relating to the regulation of securities`, `any of the securities of the corporation are listed and posted for trading on a designated stock exchange, as defined in subsection 248(1) of the Income Tax Act` |
| s 21.21(2) | s 8 (this piece), s 185(4) and s 187(4) (certificates) | this piece and cb4 | `the date shown on a certificate referred to in section 8 or subsection 185(4) or 187(4)` |
| s 21.303(3)(b)(ii) | s 27(8) of the Conflict of Interest Act or a similar provincial provision | outside the Act | `the Director is satisfied that the information is to be kept confidential under subsection 27(8) of the Conflict of Interest Act or a similar provision of an Act of the legislature of a province` |
| s 21.31(3), s 21.32(1) | "the schedule" (offences) | cb5 | not modelled: the rule asks whether the body has reasonable grounds to suspect an offence referred to in the schedule |
| s 21.31(4) | s 19 (the last notice of registered office) | this piece | not modelled: the registered office is the place where the request is left or sent |
| s 21.32(3) | s 251 | cb5 | not made an input: the rule answers JUST FALSE for a contravention of (1) or (2) and NOTHING for any other |
| s 25(1) | s 28 (this piece) | this piece | `section 28 restricts the determination because shareholders have a pre-emptive right`: the answer of s 28's rule is passed in by the seat |
| s 25(5), s 26(3) | "does not deal at arm's length" within the meaning of the Income Tax Act | outside the Act | `it is made by a person to whom a share is issued, or by a person who does not deal at arm's length with a person to whom a share is issued`, and the arm's-length labels in the exchange enumeration |
| s 26(3)(b) | s 182(1), s 192(1)(b) and (c) | cb4 | named in the label of the exchange only; not modelled |
| s 26(5) | s 39(5) (convertible shares) | this piece | `all the issued and outstanding shares are shares of not more than two classes of convertible shares referred to in subsection 39(5)`: the answer of the s 39(5) rule is passed in by the seat |
| s 26(5) | "special resolution" (s 2(1)) | keel | `special resolution within s 2(1)` is called on a `Vote tally` |
| s 26(9) | s 34(2), s 38, s 42 (this piece) and s 185(2)(a) | this piece and cb4 | named in the rule's name; the rule computes the stated capital to be used there |
| s 26(12), s 26(11) | "distributing corporation" (s 2(1)) | keel | `the corporation is a distributing corporation` |
| s 27(4) | the form the Director fixes | not among the sources | not modelled |
| s 27(5) | s 262 | cb5 | not made an input: the rule says the Director must issue, and the form is no part of whether |
| s 29.1(2) | the day s 29.1 came into force | not in the text | `the document was issued before the coming into force of section 29.1` |
| s 30(1), s 31, s 33 | "holding body corporate" (s 2(4)), "subsidiary body corporate" (s 2(5)), "personal representative", "beneficial interest" (s 2(1)) | keel | plain facts about the body in question, named for the fact (for example `the corporation, the holding body corporate or a subsidiary of either of them has a beneficial interest in the shares`) |
| s 31(4) to (6) | the regulations (prescribed conditions and consequences) | not among the sources | `the conditions prescribed for the purposes of subsection 31(4) were met before the acquisition took place` and its siblings |
| s 32(1) | "prescribed law of Canada or a province", "affiliates or associates" (s 2(1), s 2(2)) | outside the Act and keel | `the purpose is to assist the corporation or any of its affiliates or associates to qualify under a prescribed law of Canada or a province to receive licences, permits, grants, payments or other benefits by reason of attaining or maintaining a specified level of Canadian ownership or control` |
| s 32(1) | s 39(8) | this piece | `subsection 39(8) forbids the corporation to hold them`: the answer of the s 39(8) rule is passed in by the seat |
| s 32(5) | s 25(1), (3), (4), (5) (this piece), s 115(3)(c), s 118(1) | this piece and cb2 | named in the rule's name only: the rule says whether the transfer is treated as an issue |
| s 33(1) | s 153 | cb3 | `it has complied with section 153` |
| s 35(2) | s 190 (dissent) and s 241 (oppression order) | cb4 | named in the label of the purpose only |
| s 37 | s 38 | this piece | `it does so in accordance with section 38`: the answer of the s 38 rule is passed in by the seat |
| s 38(1) | "special resolution" (s 2(1)) | keel | `special resolution within s 2(1)` is called on a `Vote tally` |
| s 38(4), s 45(1) | s 118(4) and (5), s 146(5), s 226(4) and (5) | cb2, cb3, cb4 | named in the label of the basis only (`Basis on which a shareholder is said to be liable ... (s 45(1))`) |
| s 39(1), (2), (4), (9) | s 190, s 241(3)(f) and (g), s 173, s 191, s 241 | cb4 | named in input labels only: the rules compute from the figures |
| s 39(7) | s 31(1) and (2) | this piece | `the corporation holds the shares in itself as permitted by subsection 31(1) or (2)`: the answer of the s 31 rules is passed in by the seat |
| s 39(8) | s 32(1)(a) and (b) | this piece | `the shares are held as permitted by paragraph 32(1)(a), or are shares into which such shares were converted and are held under paragraph 32(1)(b)` |
| s 40(1) | s 34, 35, 36 | this piece | `the corporation can prove that enforcement of the contract would put it in breach of section 34, 35 or 36`: the answer of those rules is passed in by the seat |
| s 43(1) | s 42 | this piece | `section 42 forbids the dividend`: the answer of the s 42 rule is passed in by the seat |
| s 45(2) | s 49(8) | cb2 | `subsection 49(8) forbids it` |
| s 26(11) | the stated capital provisions that an open-end mutual fund is out of | this piece | the fact `the corporation is an open-end mutual fund` in the solvency record, used by s 34(2) and s 42 (fork cb1-F9) |
| s 46(1) | "prescribed law", the prescribed conditions and notice, the prescribed manner of the directors' determination | not among the sources | `the prescribed conditions are met and the prescribed notice has been given`, `the shares are owned, or the directors have determined in the prescribed manner that they may be owned, contrary to the constraints` |
| s 46(3), s 46(4) | s 51 (registered holder; subsections (4) to (6)) | cb2 | `the person satisfies the corporation that, but for the sale, they could properly be treated as the registered owner or registered holder of the shares under section 51` |
| s 47(1) | the manner of investing "as may be prescribed" | not among the sources | `the fund is invested in the manner that may be prescribed` |
| s 47(6) | sections 3 to 5 of the Escheats Act | outside the Act | not modelled: the rule says whether they apply |

## Needs from the core

Nothing in the keel was missing for my range: every rule and type I needed from it was there, and nothing was changed or copied.
What I call from `cbca-core.l4` is `Time limit`, `Vote tally`, `the last day of ... counted from ...`, `the earliest day allowed by ...`, `done within the time limit` and the `YMD` date shim; from `cbca-core-definitions.l4` I call `corporation within s 2(1)`, `incapable within s 2(1)` and `special resolution within s 2(1)`.
Where a seat question needs a special resolution (s 26(5), s 38(1)), it asks for the votes for and against and for whether every shareholder signed, builds a `Vote tally` from them, and passes it to `special resolution within s 2(1)`.

Three local types are declared in `cb1-nouns.l4`, each named with the range it serves so that a later piece's name cannot clash; the lead may decide whether to promote any of them to the core:

| type | what it is | why another piece may want it |
| --- | --- | --- |
| `Maximum punishment for an offence in Parts I to VI` | a fine in dollars and `MAYBE` an imprisonment term in months | offence provisions in other Parts may state the same two figures (I did not read them); the type carries `NOTHING` for "no imprisonment named", which is the Act's answer and not a gap |
| `Place where corporate records are kept (Part IV)` | four places: the registered office, another place in Canada designated by the directors, a place in Canada the directors have not designated, a place outside Canada | other Parts that mention the registered office or a place designated by the directors (I did not read them) |
| `Facts for a solvency test in Part V` | seven facts that s 34(2), s 35(3), s 36(2), s 38(3) and s 42 each read in part | s 45(1) names s 118(4) and (5) and s 226(4) and (5), which are in other pieces' ranges; I did not read them and do not know whether they use the same facts |

One local enumeration, `Mode of prosecution (s 21.4(5))`, serves a single question (summary conviction against indictment) and is declared in `cb1-part4-isc-register.l4`; it would be reusable by any piece that has the same two modes.

Not needed, but noted: the Act says "reasonable grounds for believing" in s 34(2), s 35(3), s 36(2), s 38(3) and s 42, and "reasonable cause" in every offence.
I take the first as a plain yes-or-no input (cb1-F7) and the second as a plain yes-or-no input too.
A keel convention for both would make the pieces agree; I did not build one.

## What the text turns out to say

Numbered findings. Each ends "Asserted." where a case in `cb1-tests-*.l4` or `cb1-cases-seat.l4` asserts it.

1. **Section 5(2) does not say what it means.** It joins its three conditions with "or" and also says "only if", and read as alternatives it excludes no one that paragraph (a) is meant to exclude. The rule reads them as cumulative (fork cb1-F3). Asserted (`cb1-tests-part2.l4`: age 17 fails; incapable fails; bankrupt fails).
2. **A unanimous shareholder agreement may demand more votes than the articles may, to remove a director.** Section 6(4) names the articles alone (fork cb1-F2). Asserted.
3. **A shareholder needs a higher vote only if the document asks for more.** Section 6(3) speaks of "a greater number"; a lower number in the articles does not lower the Act's. Asserted.
4. **Section 8(2) leaves the refusal to the Director.** The rule says the Director "may either issue or refuse" once a notice indicates non-compliance, and says "must issue" otherwise. Asserted.
5. **Section 14(2)(b) is not the whole story of the person's liability.** It ends the person's liability on adoption "except as provided in subsection (3)", and (3) is "subject to subsection (4)". A court order under (3) can bind the person again after adoption; a contract term under (4) shuts that out. Asserted.
6. **Section 12(4.1) points to the wrong subsection for its period.** It lets the Director direct a change of name "unless the undertaking is honoured within the period specified in subsection (5)", but subsection (5) specifies no period itself; it says "the prescribed period" for a different purpose. The rule takes the fact (honoured in time or not) as an input.
7. **Section 10(1.1) cannot be evaluated from the text.** It saves a name that included "S.C.C." "immediately before the day on which this subsection comes into force", a day the text does not give. The fact is an input.
8. **Section 10(1) lists six full forms and five abbreviations** (fork cb1-F4).
9. **Section 9 and s 13(2) both start on "the date shown" in a document.** That date is an input; the rule includes that day. Asserted.
10. **Section 16(3) is not a rule that every act is valid.** An act "contrary to its articles or this Act" is not invalid "by reason only" of that; it can still be invalid on another ground. The rule takes that other ground as the deciding fact. Section 23(2) and s 17 have the same shape. Asserted.
11. **Section 21(5) rests on "business day", which the text does not define.** The CBCA text in the sources has no definition of "business day" and no calendar of holidays, so the rule takes the next business day as a date supplied by the person asking. Asserted for both branches.
12. **Section 21(1) and s 21(1.1) put the securities register on a different footing from the other records in a distributing corporation.** Everyone who may examine the other records free of charge, or on a fee, must first send an affidavit for the securities register; and the extract is on a reasonable fee even for a shareholder. Asserted.
13. **Section 20(4) does not require the directors' records to be kept in Canada.** It speaks of "such other place as the directors think fit"; s 20(5) separately requires a quarterly set of accounting records in Canada when the accounting records are kept abroad. Asserted.
14. **Section 20(5.1) overrides s 20(5) as well as s 20(1)** ("Despite subsections (1) and (5)"), so a corporation that meets (5.1)'s conditions need not keep a quarterly set in Canada. Asserted.
15. **Section 21.4(1) is complete without a prosecution of the corporation.** The text says the director or officer commits the offence "whether or not the corporation has been prosecuted or convicted"; the rule takes the corporation's contravention as the fact and ignores whether it has been prosecuted. Asserted.
16. **A request for the register may be made only on grounds (s 21.31(3)), but the duty to comply runs from the request itself (s 21.31(1)).** Fork cb1-F5. Asserted.
17. **Section 21.303(1)(b) and (c) are mutually exclusive.** The address for service is published if it has been provided to the corporation; the residential address only if it has not. Asserted.
18. **Section 21.32(2) says "after the end the calendar year"** (a typographical slip in the text). The rule counts from 31 December of the year in which the request was made. Asserted.
19. **Section 21.21(1) says "information determined by the Director"; what that is, and the form and period, are the Director's to fix.** They are inputs, not rules.
20. **Section 21.3 has only subsection (1) in force in this text**; subsections (2) to (6) are repealed.
21. **Section 26(2) makes the full consideration the rule, and s 26(3) the only place a smaller amount may go in.** The rule that validates an amount refuses anything less than the consideration unless the exchange is one of the listed kinds, and refuses anything more in every case (s 26(4)). Asserted.
22. **Section 26(5) refers to s 39(5), a subsection of the same Part.** The rule takes the answer of the s 39(5) test as an input (see the cross-references). Asserted.
23. **Section 26(11) takes an open-end mutual fund out of subsections (1) to (10) and out of "any other provisions of this Act relating to stated capital".** Which of s 34 to s 42 count as relating to stated capital is for the reader of s 26(11) to say; the solvency record in `cb1-nouns.l4` carries the open-end mutual fund fact so that those sections can use it. Not asserted.
24. **Section 29(2) speaks of "separable or inseparable" for options and rights only**, not for conversion privileges. The rule answers NOTHING for a conversion privilege. Asserted.
25. **Section 28(1) fixes the price and terms of the first offer: they are those on which the shares "are to be offered to others".** The rule asks whether the shares were first offered to the class on that price and those terms, as one fact. Asserted.
26. **Section 27(2) is silent where nothing is owing.** The rule returns NOTHING where no series has a claim. Asserted.
27. **Section 35(2) is subject to neither the articles nor s 35(3).** Paragraphs (1)(a) to (c) are "subject to subsection (3) and to its articles", but (2)(a) and (b) (dissenting shareholder; court order) say neither. A corporation may acquire shares for those two purposes whatever its articles say and whatever its solvency. Asserted.
28. **Section 35(3)'s asset test has no stated capital term, but s 34(2)'s does.** The same figures can be forbidden by s 34(2) and allowed under s 35(3). Asserted.
29. **Section 36(2) adds a different amount from s 35(3).** Section 35(3) adds the amount owed to holders to be paid before the holders of the shares being acquired; s 36(2) adds the amount owed to holders to be paid rateably with or before. They are different fields of the shared record. Asserted.
30. **Section 32(4) makes the director guilty "whether or not the corporation has been prosecuted or convicted"**, and punishes the director with a fine or six months, though the corporation can only be fined. Asserted.
31. **The prescribed conditions and consequences of s 31(4) to (6) are in regulations that are not among the sources.** Whether they were met is an input.
32. **Section 38(3) has no stated capital term, but s 34(2) and s 42 do.** A reduction of stated capital is tested against the liabilities only; a dividend or a purchase against the liabilities and the stated capital. Asserted.
33. **Section 38(3) does not limit a reduction made to declare stated capital not represented by realizable assets (paragraph (1)(c)).** That purpose is outside the limit whatever the figures. Asserted.
34. **Section 39(5) is "for the purposes of subsection (4)" and "subject to its articles".** The per-share capital is the aggregate over both classes' shares, and the articles can displace it. Asserted.
35. **Section 39(1) lists "section 34, 35, 36, 45 or 190".** Section 45 in this text is the shareholder immunity and lien section, and its three subsections (src:663-667) do not provide for a purchase, redemption or other acquisition of shares by the corporation; the list is copied as the text has it and no reading is taken.
36. **Section 45(1) shields a shareholder "as shareholder" and names five subsections as the exceptions.** Three of them are out of range. Asserted for the five.
37. **Section 40(2) ranks the claimant behind creditors and prior classes and ahead of other shareholders.** A person the subsection does not name is NOTHING. Asserted.
38. **Section 46(3) leaves the net proceeds with income "from the beginning of the month next following the date of the receipt by the corporation of the proceeds" and less "any taxes on the proceeds and any costs of administration of a trust fund".** The rule takes the income, taxes and costs as figures, and does not compute the income. Asserted for the arithmetic.
39. **Section 47(5) vests an unclaimed fund in the Crown after ten years from the date of the sale.** Whether the last day is included follows the keel's counting convention (F1). Asserted.
40. **Section 16(1) removes the need for a by-law; it confers no power.** Whether the corporation or its directors have a power depends on whether something else (this Act, the articles) confers it, and passing a by-law changes nothing either way. A power that only a by-law would confer is not made a power by the subsection. Asserted.
41. **Once another Act provides a longer retention period, s 21.1(5) names no day for disposing of the personal information** (fork cb1-F11); s 20(2.1) counts the longer period from the end of the financial year. Asserted.
42. **Section 24(3) says the equal rights of the holders of a single class "include" the rights to vote, to dividends and to the remaining property.** Whether such a holder has any other right the subsection does not say, so the answer is `NOTHING`. Asserted.
43. **Section 25(4) names two things the directors may take into account in valuing property or past services.** Whether they may take any other thing into account it does not say, so the answer is `NOTHING`. Asserted.
44. **Section 21.31(4) deems a mailed request received "at the time it would be delivered in the ordinary course of mail", unless there are reasonable grounds for believing the corporation did not receive it at that time or at all.** Where there are such grounds the subsection gives no day, so the answer is `NOTHING`. Asserted.
45. **Section 39(10) increases the number of unissued shares of the first class "unless the articles otherwise provide".** Where they do, the Act gives no figure, so the answer is `NOTHING`. Asserted.

## What the stable binary does not accept

The target is `main`, the stable build 1.6.98, run with `JL4_LIBRARY_PATH` unset.
Everything I met while writing is below; each was reproduced on this binary on 2026-10-22 with a one-file probe (removed afterwards), except where it says otherwise.

| what I wrote | what the binary said | what I did instead |
| --- | --- | --- |
| `length (LIST 1, 2, 3)` | `I could not find a definition for the identifier length` | I did not need a list length: the rule for s 5(1) takes the number of individual signers and the number of body corporate signers as two `NUMBER` inputs |
| `r WITH a IS 3`, an update of one field of a record that already exists | `You are trying to apply r (predefined) of type R (which is not a function) to (named) arguments here.` The same error appeared when I first tried it on a test record, `complete articles`, in `cb1-tests-part2.l4` | a new record is built with every field written out (`R WITH a IS 1, b IS 2` is accepted, as a constructor); `cb1-tests-part2.l4` builds each variant of the articles in full, generated by `gen_articles_tests.py` |
| `d BEFORE (YMD 2026 1 1)`, a comparison of two dates | when it first came up in the s 21(5) rule: `I could not find a definition for the identifier BEFORE`, together with `You are trying to apply ... (DATE) to 2 arguments here`; a bare probe today gave a type error instead (a DATE where the rule says `BOOLEAN`) | `AT MOST` and `AT LEAST`, which compare dates, as the keel does in `cbca-core.l4` |

Words the dialects page says `main` rejects (`REFUSE`, `BECAUSE`, `TYPICALLY`, the regulative `MUST`, `PARTY` and `HENCE`, `ASSUME`, `EVERY`, `EACH`, `SET OF`, `NOTIFY`, and the others it lists) do not occur in the code of any `cb1-` file: I checked the files outside comments and outside backticked names with `grep`.
I did not test each of them against the binary; the claim that they are rejected is the dialects page's.

Every `cb1-` file also passes `l4 check` with no warning of the kinds `build.sh` greps for (`Unknown annotation`, `is at the end of the file`, `follows code on its line`, `Warning`): the loop printed nothing for all 25 files on 2026-10-22.

## What check.sh prints

Run on 2026-10-22 as `L4=<the stable 1.6.98 binary> L4_TARGET=unstable ./check.sh` in the deposit folder, with `JL4_LIBRARY_PATH` unset; the exit code was 0.
The brief says to set `L4_TARGET=unstable` because the binary is already the stable one; the script's one line on stderr says it skipped the comparison with a second binary.
Standard error:

```
check.sh: the target is unstable, so the main check was skipped.
```

Standard output, unedited:

```
module                                    errors satisfied  failed  refused  expected
cb1-cases-seat.l4                              0       688       0        0         0
cb1-nouns.l4                                   0         0       0        0         0
cb1-part1-application.l4                       0         0       0        0         0
cb1-part2-incorporation.l4                     0         0       0        0         0
cb1-part3-capacity.l4                          0         0       0        0         0
cb1-part4-isc-register.l4                      0         0       0        0         0
cb1-part4-records.l4                           0         0       0        0         0
cb1-part5-capital-dividends.l4                 0         0       0        0         0
cb1-part5-own-shares.l4                        0         0       0        0         0
cb1-part5-shares.l4                            0         0       0        0         0
cb1-part6-constrained-shares.l4                0         0       0        0         0
cb1-seat.l4                                    0         0       0        0         0
cb1-tests-part1.l4                             0        21       0        0         0
cb1-tests-part2.l4                             0       151       0        0         0
cb1-tests-part3.l4                             0        30       0        0         0
cb1-tests-part4-isc-register.l4                0       144       0        0         0
cb1-tests-part4-records.l4                     0       120       0        0         0
cb1-tests-part5-capital-dividends.l4           0        89       0        0         0
cb1-tests-part5-own-shares.l4                  0       102       0        0         0
cb1-tests-part5-shares.l4                      0       131       0        0         0
cb1-tests-part6-constrained-shares.l4          0        40       0        0         0
cbca-core-control.l4                           0         0       0        0         0
cbca-core-definitions.l4                       0         0       0        0         0
cbca-core-isc.l4                               0         0       0        0         0
cbca-core.l4                                   0         0       0        0         0
TOTAL (25 modules)                             0      1516       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

The 1,516 satisfied assertions are every `#ASSERT` in the 21 `cb1-` files (`grep -c '^#ASSERT'` over them also gives 1,516), so none is skipped and none is hidden.
Of them 688 are in the seat's worked cases and 828 in the nine test files; the `cbca-core*` files carry none.
`python3 -I srcrefs.py check --refs R.S.C.-1985-c.-C-44.txt cb1-*.l4` printed: `srcrefs check: 602 src: lines, 290 runs, 326 locators, 0 problems`.
`l4 check` on each `cb1-` file, filtered for `Unknown annotation`, `is at the end of the file`, `follows code on its line` and `Warning`, printed nothing.
No assertion is expected to fail, so the `expected` column is 0 throughout and the `expected_failed` function in `check.sh` names no module.

## Before this is worth relying on

What `check.sh` reports is that the files parse, type-check, and agree with the expected values I wrote; it does not report that the encoding is right.

1. **Read the official text.**
   The source is an unofficial plain-text rendering of the Justice Canada consolidation current to 2026-09-30.
   The `src:` quotes are copied from it mechanically (`srcrefs.py` reports 0 problems), so they show what I read, not what the Act says.
   The French version is equally authoritative and was not read.
2. **A lawyer must rule on the forks.**
   The register lists twelve (the keel's F1 and my cb1-F1 to cb1-F11).
   Each is a place where the text can be read two ways; the reading I took is stated with the text that licenses it, and each can be changed in one or two rules.
   The ones that change an answer a person would notice are cb1-F3 (s 5(2) cumulative), cb1-F6 (s 26(9) a floor, not an addition), cb1-F7 (the estimates are the "reasonable grounds"), cb1-F9 and cb1-F10 (the open-end mutual fund and the share dividend in the solvency tests), and cb1-F11.
3. **The regulations are not here.**
   Every "prescribed" or "regulations" fact is a plain input.
   The prescribed steps, times and conditions of s 21.1(1)(e), s 21.1(2)(c), s 21.2, s 31(4) to (6), s 46(1) and the rest are therefore not checked; the Act's regulations would have to be read and encoded.
4. **The cross-references are plain inputs and nothing joins them.**
   The register lists 65.
   The provisions they point to are in the ranges of the other pieces (for example s 49(8), s 51, s 106, s 109, s 113, s 118(4) and (5), s 146(5), s 153, s 173, s 185, s 187, s 189(3), s 190, s 191, s 226(4) and (5), s 241 and s 262) and in other Acts; I did not import another piece's module, so a person asking about one of them gets the answer to the part this piece can see.
5. **The tests and cases have the same author as the rules.**
   I wrote every expected value by hand from the text, and the dates in the seat's worked cases were checked by arithmetic done outside the encoding; but the same reader wrote the rules, the tests and the cases, so a misreading shared by all three would pass.
   A second reader should read the 45 findings and the 217 questions against the Act, not rerun the check.
6. **The seat has not been tried with a person.**
   The wording of the 217 questions has not been read by a non-lawyer.
   I ran `l4 batch` on six of the questions with JSON input (a date, a string, a choice, a number, a prosecution mode, a choice of name form) and each answered; I did not run the other 211 that way.
   The solvency questions fix the fields their rule does not read at a placeholder (0 or `FALSE`); if a later change makes a rule read them, the seat must ask for them.
7. **Some answers are `NOTHING` on purpose.**
   Where the text is silent the rule says so (`NOTHING` or a named case) and does not guess; those places include findings 41 to 45, and a reader who expected a yes or no there should read the finding.
