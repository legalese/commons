# NOTES (sgg): Companies Act 1967, Part 11 Divisions 1 and 2, ss 365 to 386, lines 23608-25371

## Edition encoded

The Companies Act 1967 (Singapore), 2020 Revised Edition, Singapore Statutes Online (SSO) informal consolidation, "version in force from 6/5/2026 to 20/10/2026", retrieved 2026-10-09, carrying the amendments up to Act 24 of 2025.
A later consolidation may exist and was not read.
The encoding is of that text only: `inputs/CoA1967.txt` lines 23608 to 25371, and nothing else.
`CoA1967.txt` is a rendering of the Act (the SSO PDF turned into plain text), not the official text; nothing here is verified against the official text.
Line numbers everywhere in these notes are of that file as it is.
Division 1 of Part 11 is shown repealed ("Repealed by Act 8 of 2003"); Division 2 (foreign companies), ss 365 to 386, is encoded.

| file | what it holds |
| --- | --- |
| `sgg-scope.l4`, `sgg-tests-scope.l4` | ss 365 to 367: which foreign companies Division 2 applies to; "authorised representative" and "carrying on business"; the activities that are not carrying on business; the power to hold immovable property; the shared types `s 365 party` and `s 365 role` |
| `sgg-lodging.l4`, `sgg-tests-lodging.l4` | ss 368 to 371: the documents to lodge; service; inspection; the duty of directors and authorised representatives to give information; refusal to register; the registered office and the authorised representatives; the 3 January 2016 transitions |
| `sgg-returns.l4`, `sgg-tests-returns.l4` | ss 372 to 374: the return when documents change; the financial statements and their audit; the relief the Registrar and the Minister may give; the offences; the return on the keeping of registers |
| `sgg-identity.l4`, `sgg-tests-identity.l4` | ss 375 and 376: the name, the place of formation, the notice of limited liability and the unique entity number on its documents; service on the foreign company |
| `sgg-cessation.l4`, `sgg-tests-cessation.l4` | ss 377 to 377D: ceasing to do business, liquidation and dissolution, striking off, administrative restoration, the effect of restoration |
| `sgg-names.l4`, `sgg-tests-names.l4` | s 378: names the Registrar must refuse or may register, the names a foreign company may use, directions to change a name, reservation of a name |
| `sgg-registers.l4`, `sgg-tests-registers.l4` | ss 379 to 386: the register of members and its index, the evidence the register and a certificate give, bearer shares, regulations, the general penalty |
| `sgg-seat.l4`, `sgg-cases-seat.l4` | the seat layer: one "Under section N, ..." question per decision function, with cases |

Where PLAN.md and the brief differ, the brief governs; the places they differ that this part met are listed at the end of these notes.

## Coverage (sgg)

One row per heading, section, subsection, defined term and paragraph of lines 23608 to 25371, each with exactly one disposition: `encoded`, `inert` (reasons 1 to 3 only), `fork`, or `repealed or blank in this text`.
The table was built by script (`work/mkcov.py`, not shipped) from the raw text: a row opens at each line that begins a heading, a section, a subsection, a defined term or a lettered or numbered paragraph, and runs to the line before the next row.
Page furniture and amendment marks are not rows of their own: each sits in the row of the provision it falls in.
The L4 names are read off the `@ref` locators: a row names the functions whose `@ref` range overlaps its lines.

**Audit (script output, run on the files as shipped).**
- Non-blank lines in the ranges: 1248. Each is in exactly one row: 1248 assigned, 0 unassigned, 0 in two rows.
- Rows: 329. Before the label audit the script made 333 rows; four lines that wrap a cross-reference or a list (`(2) is deemed ...`, `(4) or 370(4) ...`, `(ii) or the unaudited ...`, `(13A) unless ...`) had been opened as rows of their own, and now belong to the row they sit in.
- Every one of the 208 layer-1 functions and rules is named in at least one row (0 functions without a row, 0 rows `UNMATCHED`).
- Dispositions: encoded 222, fork 68, inert 29 (all reason 1: headings), repealed or blank in this text 10; no row is inert for reason 2 or 3.
- A row is `fork` when a function that encodes it carries a fork id; a paragraph row takes only the fork ids of functions whose `@ref` is about as wide as the paragraph. The id points into the fork register below.
- Section 384 is encoded, not left inert: it says what regulations may do to a foreign company, and the existence of the regulations is an input named for the fact (`regulations made under section 411 ...`). The regulations themselves are not in the sources.

| lines | unit | disposition | L4 name, fork ids, or what the text shows |
| --- | --- | --- | --- |
| 23608-23609 | Part 11 heading | inert, reason 1 | heading (not operative) |
| 23610 | Division 1 | repealed or blank in this text | the text shows `[Repealed by Act 8 of 2003]` |
| 23612-23613 | Division 2 heading and s 365 heading | inert, reason 1 | heading (not operative) |
| 23615 | s 365 | encoded | `s 365 this Division applies to the foreign company` |
| 23616-23620 | s 365(a) | encoded | `s 365 this Division applies to the foreign company` |
| 23622-23625 | s 365(b) | encoded | `s 365 this Division applies to the foreign company` |
| 23627 | s 366 heading | inert, reason 1 | heading (not operative) |
| 23629 | s 366(1) | encoded | `s 366(1) "authorised representative" the person is an authorised representative of the fo...` |
| 23631-23632 | s 366(1) “authorised representative” | encoded | `s 366(1) "authorised representative" the person is an authorised representative of the fo...` |
| 23634-23637 | s 366(1) “authorised representative” (a) | encoded | `s 366(1) "authorised representative" the person is an authorised representative of the fo...` |
| 23639-23641 | s 366(1) “authorised representative” (b) | encoded | `s 366(1) "authorised representative" the person is an authorised representative of the fo...` |
| 23643 | s 366(1) “carrying on business” | encoded | `s 366(1) "carrying on business" the activity is within carrying on business` |
| 23645-23649 | s 366(1) “carrying on business” (a) | encoded | `s 366(1) "carrying on business" the activity is within carrying on business` |
| 23651-23654 | s 366(1) “carrying on business” (b) | encoded | `s 366(1) "carrying on business" the activity is within carrying on business`, `s 366(1) "carrying on business" the activity is kept out of carrying on business only bec...` |
| 23656-23658 | s 366(2) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23660-23663 | s 366(2)(a) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23665-23666 | s 366(2)(b) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23668-23671 | s 366(2)(c) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23673 | s 366(2)(d) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23675-23676 | s 366(2)(e) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23678-23679 | s 366(2)(f) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23681-23682 | s 366(2)(g) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23684-23686 | s 366(2)(h) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23688 | s 366(2)(i) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23690-23691 | s 366(2)(j) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23693-23698 | s 366(2)(k) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23700-23703 | s 366(2)(l) | encoded | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reas...` |
| 23705 | s 367 heading | inert, reason 1 | heading (not operative) |
| 23707-23711 | s 367 | encoded | `s 367 the foreign company has power to hold immovable property in Singapore` |
| 23713-23714 | s 368 heading | inert, reason 1 | heading (not operative) |
| 23716-23721 | s 368(1) | encoded | `s 368(1) the foreign company has lodged what the subsection requires`, `s 368(1) the foreign company lodged the documents before it began`, `s 368(1) the foreign company must lodge the documents before it establishes a place of bu...` |
| 23723-23725 | s 368(1)(a) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23727-23729 | s 368(1)(b) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23731-23737 | s 368(1)(c) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23739-23745 | s 368(1)(d) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23747-23756 | s 368(1)(e) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23758-23762 | s 368(1)(f) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23764-23772 | s 368(1)(g) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23774-23775 | s 368(1)(h) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23777-23784 | s 368(1)(h)(i) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23786-23787 | s 368(1)(h)(ii) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23789-23790 | s 368(1)(h)(iii) | encoded | `s 368(1) the foreign company has lodged what the subsection requires` |
| 23792-23802 | s 368(1)(i) | fork | `s 368(1) the foreign company has lodged what the subsection requires`, `s 368(1) the Registrar must register the foreign company under this Division`; fork F-D1 |
| 23804-23812 | s 368(2) | encoded | `s 368(2) the document is sufficiently served on the director or authorised representative` |
| 23814-23819 | s 368(3) | fork | `s 368(3) what the subsection requires to be available for inspection is available`; fork F-B1 |
| 23821-23823 | s 368(3)(a) | encoded | `s 368(3) what the subsection requires to be available for inspection is available` |
| 23825-23832 | s 368(3)(b) | encoded | `s 368(3) what the subsection requires to be available for inspection is available` |
| 23834-23841 | s 368(4) | encoded | `s 368(4) subsection (1) applies to the foreign company as if it began on 29 December 1967` |
| 23843-23844 | s 368A heading | inert, reason 1 | heading (not operative) |
| 23846-23852 | s 368A(1) | encoded | `s 368A(1) the director must give the foreign company the information it needs to comply w...`, `s 368A(1) the director gave the information not later than 14 days after the initial appo...`, `s 368A(1) a director must give the foreign company the information within 14 days after t...` |
| 23854 | s 368A(2) | encoded | `s 368A(2)(a) the authorised representative must give the foreign company the information...`, `s 368A(2) an authorised representative must give the foreign company the information with...` |
| 23856-23860 | s 368A(2)(a) | encoded | `s 368A(2)(a) the authorised representative must give the foreign company the information...`, `s 368A(2)(a) the authorised representative gave the information not later than 14 days af...`, `s 368A(2) an authorised representative must give the foreign company the information with...` |
| 23862-23869 | s 368A(2)(b) | encoded | `s 368A(2)(a) the authorised representative must give the foreign company the information...`, `s 368A(2)(b) the authorised representative gave the information not later than 14 days af...` |
| 23871-23879 | s 368A(3) | fork | `s 368A(3) the director or authorised representative must give the foreign company the inf...`; fork F-D1 |
| 23881-23886 | s 368A(4) | encoded | `s 368A(4) the information was furnished not later than 14 days after receipt of the writt...`, `s 368A(4) the director or authorised representative must furnish the information within 1...` |
| 23888-23893 | s 368A(5) | fork | `s 368A(5) the penalty for a director or authorised representative`, `s 368A(5) the offence and its penalty`; fork F-S1 |
| 23895-23897 | s 368B heading | inert, reason 1 | heading (not operative) |
| 23899-23900 | s 368B(1) | encoded | `s 368B(1)(a) the lodged name and particulars are treated as those of the foreign company'...` |
| 23902-23910 | s 368B(1)(a) | encoded | `s 368B(1)(a) the lodged name and particulars are treated as those of the foreign company'...` |
| 23912-23926 | s 368B(1)(b) | encoded | `s 368B(1)(b) the lodged name and particulars of the agents are treated as those of the fo...` |
| 23928 | s 368B(2) | encoded | `s 368B(2)(a) the address lodged for a director is treated as the director's residential a...` |
| 23930-23933 | s 368B(2)(a) | encoded | `s 368B(2)(a) the address lodged for a director is treated as the director's residential a...` |
| 23935-23943 | s 368B(2)(b) | encoded | `s 368B(2)(b) the address lodged for an agent is treated as the agent's residential addres...` |
| 23945-23946 | s 369 heading | inert, reason 1 | heading (not operative) |
| 23948-23956 | s 369(1) | fork | `s 369(1) the Registrar must refuse to register the foreign company`; fork F-D1 |
| 23958-23960 | s 369(2) | fork | `s 369(2) the foreign company may appeal to the Minister`, `s 369(2) the Minister's decision on the appeal is final`; fork F-P1 |
| 23962-23963 | s 370 heading | inert, reason 1 | heading (not operative) |
| 23965-23975 | s 370(1) | encoded | `s 370(1) the registered office meets the subsection on the business day`, `s 370(1) the foreign company must have a registered office in Singapore open and accessib...` |
| 23977-23978 | s 370(2) | fork | `s 370(2)(a) the person continues to be the authorised representative of the foreign compa...`, `s 370(2)(b) the person is answerable for the acts, matters and things the foreign company...`, `s 370(2)(c) the person is personally liable to the penalties imposed on the foreign compa...`; fork F-U2 |
| 23980-23981 | s 370(2)(a) | encoded | `s 370(2)(a) the person continues to be the authorised representative of the foreign compa...`, `s 370(2)(b) the person is answerable for the acts, matters and things the foreign company...`, `s 370(2)(c) the person is personally liable to the penalties imposed on the foreign compa...` |
| 23983-23985 | s 370(2)(b) | encoded | `s 370(2)(a) the person continues to be the authorised representative of the foreign compa...`, `s 370(2)(b) the person is answerable for the acts, matters and things the foreign company...`, `s 370(2)(c) the person is personally liable to the penalties imposed on the foreign compa...` |
| 23987-23992 | s 370(2)(c) | encoded | `s 370(2)(a) the person continues to be the authorised representative of the foreign compa...`, `s 370(2)(c) the person is personally liable to the penalties imposed on the foreign compa...` |
| 23994-23998 | s 370(3) | encoded | `s 370(3) the person may lodge a notice that the authorised representative has ceased or w...` |
| 24000-24005 | s 370(4) | encoded | `s 370(4) the foreign company has lodged the notice and the consent statement for the new...`, `s 370(4) the foreign company must lodge the notice and the consent statement for the new...` |
| 24007-24020 | s 370(5) | encoded | `s 370(5) the day the authorised representative ceases to be an authorised representative` |
| 24022-24024 | s 370(6) | fork | `s 370(6)(a) the foreign company must appoint another authorised representative`; fork F-D1 |
| 24026-24027 | s 370(6)(a) | encoded | `s 370(6)(a) the foreign company must appoint another authorised representative` |
| 24029-24034 | s 370(6)(b) | fork | `s 370(6)(a) the foreign company must appoint another authorised representative`, `s 370(6)(b) the day the sole authorised representative ceases to be an authorised represe...`; fork F-D1 |
| 24036-24040 | s 370(7) | encoded | `s 370(7) the foreign company appointed another authorised representative within 21 days a...`, `s 370(7) the foreign company must appoint another authorised representative within 21 day...` |
| 24042-24043 | s 370A heading | inert, reason 1 | heading (not operative) |
| 24045-24051 | s 370A(1) | encoded | `s 370A(1) the alternate address is taken to be the individual's contact address` |
| 24053-24059 | s 370A(2) | encoded | `s 370A(2) the residential address is taken to be the individual's contact address` |
| 24061-24063 | s 370A(3) | encoded | `s 370A(3) the contact address is deemed to be a particular lodged with the Registrar unde...` |
| 24065-24073 | s 370A(4) | fork | `s 370A(5) the notice or information must provide the information required under section 3...`; fork F-D1 |
| 24075-24080 | s 370A(5) | fork | `s 370A(5) the notice or information must provide the information required under section 3...`; fork F-D1 |
| 24082-24086 | s 370A(6) | fork | `s 370A(6) "commencement date" the commencement date`; fork F-I1 |
| 24088 | s 371 heading | inert, reason 1 | heading (not operative) |
| 24090-24093 | s 371(1) | encoded | `s 371(1) the notice is prima facie evidence of the particular in all courts` |
| 24095-24099 | s 371(2) | fork | `s 371(2) the Registrar must issue the foreign company a certificate confirming the partic...`, `s 371(2) the certificate is prima facie evidence of the particular in all courts`; fork F-D1 |
| 24101 | s 372 heading | inert, reason 1 | heading (not operative) |
| 24103 | s 372(1) | fork | `s 372(1) the change is one the subsection names`; fork F-O2 |
| 24105-24107 | s 372(1)(a) | encoded | `s 372(1) the change is one the subsection names` |
| 24109 | s 372(1)(b) | encoded | `s 372(1) the change is one the subsection names` |
| 24111-24112 | s 372(1)(c) | encoded | `s 372(1) the change is one the subsection names` |
| 24114-24121 | s 372(1)(ca) | encoded | `s 372(1) the change is one the subsection names` |
| 24123-24126 | s 372(1)(d) | encoded | `s 372(1) the change is one the subsection names` |
| 24128-24129 | s 372(1)(e) | encoded | `s 372(1) the change is one the subsection names` |
| 24131 | s 372(1)(f) | encoded | `s 372(1) the change is one the subsection names` |
| 24133-24134 | s 372(1)(g) | encoded | `s 372(1) the change is one the subsection names` |
| 24136-24144 | s 372(1)(h) | encoded | `s 372(1) the change is one the subsection names`, `s 372(1) the particulars of the change were lodged within the time`, `s 372(1) the foreign company must lodge particulars of the change within 30 days or the f...` |
| 24146-24151 | s 372(1A) | encoded | `s 372(1A) the notice of the new residential address was lodged within 30 days after the c...`, `s 372(1A) a director or authorised representative must lodge a notice of the new resident...` |
| 24153-24160 | s 372(1B) | encoded | `s 372(1B) the person is taken to have informed the Registrar of the change of residential...` |
| 24162-24170 | s 372(1C) | fork | `s 372(1C) the penalty if default is made`, `s 372(1C) the offence and its penalty`; fork F-S1 |
| 24172 | s 372(2) | repealed or blank in this text | the text shows `[Deleted by Act 36 of 2014]` |
| 24174 | s 372(3) | repealed or blank in this text | the text shows `[Deleted by Act 36 of 2014]` |
| 24176-24184 | s 372(4) | fork | `s 372(4) the foreign company must lodge a copy of the order with the Registrar`, `s 372(4) the copy of the order was lodged within the time`, `s 372(4) the foreign company must lodge a copy of the order within 30 days`; fork F-D1 |
| 24186 | s 373 heading | inert, reason 1 | heading (not operative) |
| 24188-24196 | s 373(1) | encoded | `s 373(1) the foreign company has lodged what the subsection requires` |
| 24198 | s 373(2) | encoded | `s 373(2) the financial statements the subsection means` |
| 24200-24206 | s 373(2)(a) | encoded | `s 373(2) the financial statements the subsection means` |
| 24208 | s 373(2)(b) | encoded | `s 373(2) the financial statements the subsection means` |
| 24210-24213 | s 373(2)(b)(i) | encoded | `s 373(2) the financial statements the subsection means` |
| 24215-24226 | s 373(2)(b)(ii) | encoded | `s 373(2) the financial statements the subsection means` |
| 24228-24233 | s 373(2)(b)(iii) | encoded | `s 373(2) the financial statements the subsection means` |
| 24235-24236 | s 373(3) | encoded | `s 373(3) the last day for lodging the financial statements`, `s 373(3) the financial statements were lodged within the time` |
| 24238-24242 | s 373(3)(a) | encoded | `s 373(3) the last day for lodging the financial statements`, `s 373(3) the financial statements were lodged within the time` |
| 24244-24250 | s 373(3)(b) | encoded | `s 373(3) the last day for lodging the financial statements`, `s 373(3) the financial statements were lodged within the time` |
| 24252-24255 | s 373(4) | encoded | `s 373(4) the Registrar may require the foreign company by written notice to lodge further...` |
| 24257-24258 | s 373(4)(a) | encoded | `s 373(4) the Registrar may require the foreign company by written notice to lodge further...` |
| 24260-24265 | s 373(4)(b) | encoded | `s 373(4) the Registrar may require the foreign company by written notice to lodge further...` |
| 24267 | s 373(5) | encoded | `s 373(5) subsection (4) does not authorise the Registrar to require the particulars or do...` |
| 24269-24272 | s 373(5)(a) | encoded | `s 373(5) subsection (4) does not authorise the Registrar to require the particulars or do...` |
| 24274-24279 | s 373(5)(b) | encoded | `s 373(5) subsection (4) does not authorise the Registrar to require the particulars or do...` |
| 24281-24284 | s 373(6) | encoded | `s 373(6) the foreign company has complied with the requirements in the notice`, `s 373(6) the foreign company must comply with the requirements in the Registrar's notice...` |
| 24286-24289 | s 373(7) | encoded | `s 373(7) the foreign company has lodged what the subsection requires in addition`, `s 373(7) the foreign company must lodge the audited statement, the audited profit and los...` |
| 24291-24293 | s 373(7)(a) | encoded | `s 373(7) the foreign company has lodged what the subsection requires in addition` |
| 24295-24300 | s 373(7)(b) | encoded | `s 373(7) the foreign company has lodged what the subsection requires in addition` |
| 24302-24308 | s 373(7)(c) | encoded | `s 373(7) the foreign company has lodged what the subsection requires in addition` |
| 24310-24318 | s 373(7A) | encoded | `s 373(7A) the foreign company has ensured that the profit and loss account complies and g...` |
| 24320-24333 | s 373(8) | fork | `s 373(8) the foreign company is entitled to make the apportionments and add the notes and...`; fork F-E1 |
| 24335-24337 | s 373(9) | encoded | `s 373(9) the foreign company may lodge unaudited documents in lieu of subsection (7)` |
| 24339-24340 | s 373(9)(a) | encoded | `s 373(9) the foreign company may lodge unaudited documents in lieu of subsection (7)` |
| 24342-24345 | s 373(9)(b) | encoded | `s 373(9) the foreign company may lodge unaudited documents in lieu of subsection (7)` |
| 24347-24352 | s 373(10) | fork | `s 373(10) the Registrar may extend the period for the requirement`; fork F-S3 |
| 24354-24360 | s 373(11) | encoded | `s 373(11) the statement and profit and loss account are deemed to have been duly audited` |
| 24362-24365 | s 373(12) | fork | `s 373(12) the Registrar may waive the requirement to lodge the documents referred to in s...`; fork F-S3 |
| 24367-24369 | s 373(12)(a) | encoded | `s 373(12) the Registrar may waive the requirement to lodge the documents referred to in s...` |
| 24371-24372 | s 373(12)(b) | encoded | `s 373(12) the Registrar may waive the requirement to lodge the documents referred to in s...` |
| 24374-24378 | s 373(12)(c) | encoded | `s 373(12) the Registrar may waive the requirement to lodge the documents referred to in s...` |
| 24380-24384 | s 373(12)(d) | encoded | `s 373(12) the Registrar may waive the requirement to lodge the documents referred to in s...` |
| 24386-24387 | s 373(13) | fork | `s 373(13) the Registrar may make the order on the application`; fork F-S3 |
| 24389-24394 | s 373(13)(a) | encoded | `s 373(13) the Registrar may make the order on the application` |
| 24396-24402 | s 373(13)(b) | encoded | `s 373(13) the Registrar may make the order on the application` |
| 24404-24411 | s 373(13A) | fork | `s 373(13A) the Registrar may make the order relieving the foreign company from the requir...`; fork F-S3 |
| 24413-24421 | s 373(14) | encoded | `s 373(14) the Registrar may make the order unconditionally or subject to conditions` |
| 24423-24435 | s 373(15) | encoded | `s 373(15) the Registrar is barred from making an order under subsection (13) or (13A)` |
| 24437-24443 | s 373(16) | encoded | `s 373(16) the order may be limited to a specific period and may be revoked or suspended f...` |
| 24445-24447 | s 373(17) | encoded | `s 373(17)(a) the other accounting standards apply to the foreign company in place of the...`, `s 373(17)(b) the foreign company is exempt from the requirements of subsection (7) or (7A...` |
| 24449-24451 | s 373(17)(a) | encoded | `s 373(17)(a) the other accounting standards apply to the foreign company in place of the...`, `s 373(17)(b) the foreign company is exempt from the requirements of subsection (7) or (7A...` |
| 24453-24461 | s 373(17)(b) | encoded | `s 373(17)(a) the other accounting standards apply to the foreign company in place of the...`, `s 373(17)(b) the foreign company is exempt from the requirements of subsection (7) or (7A...` |
| 24463-24464 | s 373(18) | fork | `s 373(18) the penalty if the element is met`, `s 373(18) the offence and its penalty`; fork F-S1 |
| 24466 | s 373(18)(a) | encoded | `s 373(18) the penalty if the element is met`, `s 373(18) the offence and its penalty` |
| 24468-24479 | s 373(18)(b) | fork | `s 373(18) the penalty if the element is met`, `s 373(18) the offence and its penalty`; fork F-S1 |
| 24481-24485 | s 373(18A) | fork | `s 373(18A) the penalty if the element is met`, `s 373(18A) the offence and its penalty`; fork F-S1 |
| 24487-24488 | s 373(18A)(a) | encoded | `s 373(18A) the penalty if the element is met`, `s 373(18A) the offence and its penalty` |
| 24490-24494 | s 373(18A)(b) | encoded | `s 373(18A) the penalty if the element is met`, `s 373(18A) the offence and its penalty` |
| 24496 | s 373(18A)(b)(i) | encoded | `s 373(18A) the penalty if the element is met`, `s 373(18A) the offence and its penalty` |
| 24498-24506 | s 373(18A)(b)(ii) | encoded | `s 373(18A) the penalty if the element is met`, `s 373(18A) the offence and its penalty` |
| 24508 | s 373(19) | encoded | `s 373(19)(a) the foreign company is dormant in Singapore during the period` |
| 24510-24513 | s 373(19)(a) | encoded | `s 373(19)(a) the foreign company is dormant in Singapore during the period` |
| 24515-24520 | s 373(19)(b) | encoded | `s 373(19)(b) the transaction is an accounting transaction` |
| 24522 | s 374 heading | inert, reason 1 | heading (not operative) |
| 24524-24525 | s 374 | encoded | `s 374 the foreign company has lodged the return with its lodgment`, `s 374 the foreign company must lodge the return when it lodges its financial statements` |
| 24527-24528 | s 374(a) | encoded | `s 374 the foreign company has lodged the return with its lodgment`, `s 374 the foreign company must lodge the return when it lodges its financial statements` |
| 24530-24539 | s 374(b) | encoded | `s 374 the foreign company has lodged the return with its lodgment`, `s 374 the foreign company must lodge the return when it lodges its financial statements` |
| 24541-24542 | s 374(c) | encoded | `s 374 the foreign company has lodged the return with its lodgment`, `s 374 the foreign company must lodge the return when it lodges its financial statements` |
| 24544-24545 | s 374(d) | encoded | `s 374 the foreign company has lodged the return with its lodgment`, `s 374 the foreign company must lodge the return when it lodges its financial statements` |
| 24547-24550 | s 374(e) | encoded | `s 374 the foreign company has lodged the return with its lodgment`, `s 374 the foreign company must lodge the return when it lodges its financial statements` |
| 24552-24553 | s 375 heading | inert, reason 1 | heading (not operative) |
| 24555 | s 375(1) | encoded | `s 375(1)(b) the document states the name and the place of formation in legible romanised...`, `s 375(1)(b) the foreign company must cause its name and place of formation to be stated i...` |
| 24557 | s 375(1)(a) | repealed or blank in this text | the text shows `[Deleted by Act 36 of 2014]` |
| 24559-24562 | s 375(1)(b) | encoded | `s 375(1)(b) the document states the name and the place of formation in legible romanised...`, `s 375(1)(b) the foreign company must cause its name and place of formation to be stated i...` |
| 24564-24566 | s 375(1)(c) | encoded | `s 375(1)(c) the foreign company must cause notice that the liability of its members is li...` |
| 24568-24571 | s 375(1)(c)(i) | fork | `s 375(1)(c) the foreign company must cause notice that the liability of its members is li...`, `s 375(1)(c)(i) the document states notice that the liability of the members is limited in...`; fork F-D1 |
| 24573-24577 | s 375(1)(c)(ii) | encoded | `s 375(1)(c) the foreign company must cause notice that the liability of its members is li...`, `s 375(1)(c)(ii) the foreign company must exhibit the notice outside its registered office...` |
| 24579-24591 | s 375(2) | encoded | `s 375(2) the section relating to the statement of the name is deemed not to have been com...` |
| 24593-24598 | s 375(3) | encoded | `s 375(3) the document shows the unique entity number in a legible form`, `s 375(3) the foreign company must cause its unique entity number to appear in a legible f...` |
| 24600-24604 | s 375(4) | encoded | `s 375(4) the foreign company must comply with subsection (3) on the day asked` |
| 24606 | s 376 heading | inert, reason 1 | heading (not operative) |
| 24608-24609 | s 376 | encoded | `s 376 the document is sufficiently served on the foreign company` |
| 24611-24612 | s 376(a) | encoded | `s 376 the document is sufficiently served on the foreign company` |
| 24614-24618 | s 376(b) | encoded | `s 376 the document is sufficiently served on the foreign company` |
| 24620-24625 | s 376(c) | encoded | `s 376 the document is sufficiently served on the foreign company` |
| 24627 | s 377 heading | inert, reason 1 | heading (not operative) |
| 24629-24633 | s 377(1) | fork | `s 377(1) the foreign company must lodge with the Registrar notice that it has ceased`, `s 377(1) the notice was lodged within 7 days after the foreign company ceased`, `s 377(1) the foreign company must lodge the notice within 7 days after it ceases`; fork F-D1, F-P1 |
| 24635-24644 | s 377(1A) | encoded | `s 377(1A) the obligation of the foreign company to lodge the document with the Registrar...` |
| 24646-24651 | s 377(1B) | fork | `s 377(1B) the Registrar must record in the register that the company has ceased to have a...`, `s 377(1B) the Registrar must record in the register that the company has ceased to carry...`; fork F-D1 |
| 24653-24656 | s 377(2) | fork | `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the liq...`; fork F-D1 |
| 24658-24659 | s 377(2)(a) | fork | `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the liq...`, `s 377(2) the notice was lodged within the time the subsection allows`, `s 377(2)(a) an authorised representative must lodge notice of the liquidation or the diss...`; fork F-P1, F-T1 |
| 24661-24667 | s 377(2)(b) | fork | `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the liq...`, `s 377(2) the notice was lodged within the time the subsection allows`, `s 377(2)(b) an authorised representative must lodge notice of the liquidation or the diss...`, `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the app...` and 1 more; fork F-D1, F-P1, F-T1, F-T2 |
| 24669 | s 377(3) | repealed or blank in this text | the text shows `[Deleted by Act 40 of 2018]` |
| 24671 | s 377(4) | repealed or blank in this text | the text shows `[Deleted by Act 40 of 2018]` |
| 24673 | s 377(4A) | repealed or blank in this text | the text shows `[Deleted by Act 40 of 2018]` |
| 24675-24679 | s 377(5) | fork | `s 377(5) the Registrar must record in the register that the foreign company has been diss...`; fork F-D1 |
| 24681 | s 377(6) | repealed or blank in this text | the text shows `[Deleted by Act 36 of 2014]` |
| 24683 | s 377(7) | repealed or blank in this text | the text shows `[Deleted by Act 40 of 2018]` |
| 24685-24694 | s 377(8) | fork | `s 377(8) the Registrar must strike the name of the foreign company off the register`; fork F-D1 |
| 24696-24697 | s 377(9) | encoded | `s 377(9)(b) the company has failed to appoint an authorised representative within 6 month...`, `s 377(9) the Registrar may strike the name of the foreign company off the register` |
| 24699-24701 | s 377(9)(a) | encoded | `s 377(9)(b) the company has failed to appoint an authorised representative within 6 month...`, `s 377(9) the Registrar may strike the name of the foreign company off the register` |
| 24703-24707 | s 377(9)(b) | encoded | `s 377(9)(b) the company has failed to appoint an authorised representative within 6 month...`, `s 377(9) the Registrar may strike the name of the foreign company off the register` |
| 24709-24712 | s 377(10) | fork | `s 377(10)(a) the company has failed to respond or appoint another authorised representati...`, `s 377(10) the Registrar may strike the name of the foreign company off the register on th...`; fork F-S3 |
| 24714-24719 | s 377(10)(a) | encoded | `s 377(10)(a) the company has failed to respond or appoint another authorised representati...`, `s 377(10) the Registrar may strike the name of the foreign company off the register on th...` |
| 24721-24728 | s 377(10)(b) | encoded | `s 377(10)(a) the company has failed to respond or appoint another authorised representati...`, `s 377(10)(b) the foreign company has failed to give instructions within 12 months after t...`, `s 377(10) the Registrar may strike the name of the foreign company off the register on th...` |
| 24730-24735 | s 377(11) | encoded | `s 377(11) the Registrar may have regard to the circumstances prescribed` |
| 24737-24745 | s 377(12) | encoded | `s 377(12) the provisions of this Act relating to the striking off of a defunct company ap...` |
| 24747-24751 | s 377(13) | fork | `s 377(13) the person may appeal to the Minister`, `s 377(13) the Minister's decision on the appeal is final`; fork F-P1 |
| 24753-24754 | s 377A heading | inert, reason 1 | heading (not operative) |
| 24756-24761 | s 377A(1) | encoded | `s 377A(1) the person may apply to the Registrar to restore the name of the foreign compan...` |
| 24763-24768 | s 377A(2) | fork | `s 377A(2) the application is not valid`; fork F-P1 |
| 24770-24771 | s 377B heading | inert, reason 1 | heading (not operative) |
| 24773-24776 | s 377B(1) | fork | `s 377B(1) the Registrar must give notice to the applicant of the decision`; fork F-D1 |
| 24778-24783 | s 377B(2) | encoded | `s 377B(2) the restoration date` |
| 24785 | s 377B(3) | fork | `s 377B(3)(a) the Registrar must enter in the register a note of the restoration date`; fork F-D1 |
| 24787 | s 377B(3)(a) | fork | `s 377B(3)(a) the Registrar must enter in the register a note of the restoration date`; fork F-D1 |
| 24789-24792 | s 377B(3)(b) | fork | `s 377B(3)(a) the Registrar must enter in the register a note of the restoration date`, `s 377B(3)(b) the Registrar must cause notice of the restoration to be published in the Ga...`; fork F-D1 |
| 24794 | s 377B(4) | encoded | `s 377B(4) the notice states everything the subsection requires` |
| 24796-24801 | s 377B(4)(a) | encoded | `s 377B(4) the notice states everything the subsection requires` |
| 24803-24804 | s 377B(4)(b) | encoded | `s 377B(4) the notice states everything the subsection requires` |
| 24806-24808 | s 377B(4)(c) | encoded | `s 377B(4) the notice states everything the subsection requires` |
| 24810-24815 | s 377B(5) | encoded | `s 377B(5) the person may appeal to the Court` |
| 24817 | s 377B(6) | encoded | `s 377B(6)(a) the Court may confirm the Registrar's decision` |
| 24819 | s 377B(6)(a) | encoded | `s 377B(6)(a) the Court may confirm the Registrar's decision` |
| 24821-24825 | s 377B(6)(b) | encoded | `s 377B(6)(a) the Court may confirm the Registrar's decision`, `s 377B(6)(b) the Court may restore the name of the foreign company to the register and gi...` |
| 24827-24828 | s 377C heading | inert, reason 1 | heading (not operative) |
| 24830-24835 | s 377C(1) | encoded | `s 377C(2) the mistake is a mistake of the Registrar within subsection (1)`, `s 377C(1) the Registrar may on his or her own initiative restore the name of the foreign...` |
| 24837-24843 | s 377C(2) | encoded | `s 377C(2) the mistake is a mistake of the Registrar within subsection (1)` |
| 24845-24853 | s 377C(3) | encoded | `s 377C(3) the Registrar may restore the name of the foreign company by publishing the not...`, `s 377C(3) the day the restoration takes effect` |
| 24855 | s 377D heading | inert, reason 1 | heading (not operative) |
| 24857-24863 | s 377D(1) | encoded | `s 377D(1) the foreign company is regarded as having continued its registration as if its...` |
| 24865-24869 | s 377D(2) | encoded | `s 377D(2) the person is not liable to a penalty under section 373(18) for the financial y...` |
| 24871-24872 | s 377D(2)(a) | encoded | `s 377D(2) the person is not liable to a penalty under section 373(18) for the financial y...` |
| 24874-24877 | s 377D(2)(b) | encoded | `s 377D(2) the person is not liable to a penalty under section 373(18) for the financial y...` |
| 24879-24884 | s 377D(3) | fork | `s 377D(3) the Court may give directions and make orders as seem just for placing the fore...`; fork F-S3 |
| 24886-24890 | s 377D(4) | fork | `s 377D(4) the application to the Court for the directions or orders may be made`; fork F-P1 |
| 24892 | s 378 heading | inert, reason 1 | heading (not operative) |
| 24894-24898 | s 378(1) | fork | `s 378(1) the Registrar must refuse to register the foreign company under the name`, `s 378 a period of at least the number of units has passed after the date`; fork F-D1, F-U1 |
| 24900-24903 | s 378(1)(a) | encoded | `s 378(1) the Registrar must refuse to register the foreign company under the name`, `s 378 a period of at least the number of units has passed after the date` |
| 24905-24907 | s 378(1)(b) | encoded | `s 378(1) the Registrar must refuse to register the foreign company under the name`, `s 378 a period of at least the number of units has passed after the date` |
| 24909-24914 | s 378(1)(c) | encoded | `s 378(1) the Registrar must refuse to register the foreign company under the name`, `s 378 a period of at least the number of units has passed after the date` |
| 24916-24919 | s 378(1)(d) | encoded | `s 378(1) the Registrar must refuse to register the foreign company under the name`, `s 378 a period of at least the number of units has passed after the date` |
| 24921-24923 | s 378(2) | fork | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name`; fork F-D1, F-P3 |
| 24925-24926 | s 378(2)(a) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24928-24932 | s 378(2)(a)(i) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24934-24937 | s 378(2)(a)(ii) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24939-24944 | s 378(2)(b) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24946-24953 | s 378(2)(c) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24955-24956 | s 378(2)(d) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24958-24963 | s 378(2)(d)(i) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24965-24970 | s 378(2)(d)(ii) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24972-24973 | s 378(2)(e) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24975-24979 | s 378(2)(e)(i) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24981-24985 | s 378(2)(e)(ii) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24987 | s 378(2)(f) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24989-24995 | s 378(2)(f)(i) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 24997-25005 | s 378(2)(f)(ii) | encoded | `s 378(2) the years that must have passed after the date of dissolution, cancellation or c...`, `s 378(2) the Registrar must refuse to register the foreign company under the name` |
| 25007-25008 | s 378(3) | fork | `s 378(3) the Registrar may register the foreign company under the name`; fork F-L1 |
| 25010-25011 | s 378(3)(a) | encoded | `s 378(3) the Registrar may register the foreign company under the name` |
| 25013-25017 | s 378(3)(a)(i) | encoded | `s 378(3) the Registrar may register the foreign company under the name` |
| 25019-25022 | s 378(3)(a)(ii) | encoded | `s 378(3) the Registrar may register the foreign company under the name` |
| 25024-25031 | s 378(3)(b) | encoded | `s 378(3) the Registrar may register the foreign company under the name` |
| 25033-25034 | s 378(4) | encoded | `s 378(4) the foreign company is barred from using the name in Singapore` |
| 25036-25037 | s 378(4)(a) | encoded | `s 378(4) the foreign company is barred from using the name in Singapore` |
| 25039-25047 | s 378(4)(b) | encoded | `s 378(4) the foreign company is barred from using the name in Singapore` |
| 25049-25052 | s 378(5) | fork | `s 378(5) the Registrar may direct the foreign company to change its name`; fork F-S3 |
| 25054-25055 | s 378(5)(a) | encoded | `s 378(5) the Registrar may direct the foreign company to change its name` |
| 25057-25059 | s 378(5)(b) | encoded | `s 378(5) the Registrar may direct the foreign company to change its name` |
| 25061-25070 | s 378(5)(c) | fork | `s 378(5) the Registrar may direct the foreign company to change its name`, `s 378(5) the foreign company must comply with the direction`, `s 378(5) the foreign company complied with the direction within the time allowed`, `s 378(5) the foreign company must change its name within 6 weeks after the date of the di...` and 1 more; fork F-D1, F-P1 |
| 25072-25076 | s 378(6) | encoded | `s 378(6) the person may apply to the Registrar to give a direction to the foreign company` |
| 25078-25085 | s 378(7) | fork | `s 378(7) the penalty if the element is met`, `s 378(7) the offence and its penalty`; fork F-O1, F-S1 |
| 25087-25090 | s 378(8) | encoded | `s 378(8) the name is a registered business name` |
| 25092-25097 | s 378(9) | fork | `s 378(9)(a) the foreign company may appeal to the Minister against the Registrar's decisi...`; fork F-P1 |
| 25099-25101 | s 378(9)(a) | encoded | `s 378(9)(a) the foreign company may appeal to the Minister against the Registrar's decisi...` |
| 25103-25109 | s 378(9)(b) | fork | `s 378(9)(a) the foreign company may appeal to the Minister against the Registrar's decisi...`, `s 378(9)(b) the applicant may appeal to the Minister against the Registrar's refusal to g...`; fork F-P1 |
| 25111-25114 | s 378(10) | fork | `s 378(10) the Minister must cause the direction to be published in the Gazette`; fork F-D1 |
| 25116-25121 | s 378(11) | encoded | `s 378(11) the person may apply to the Registrar for the reservation of the name` |
| 25123-25127 | s 378(12) | encoded | `s 378(12) the foreign company must not be registered by the name` |
| 25129-25130 | s 378(13) | encoded | `s 378(13) the Registrar may approve the application` |
| 25132 | s 378(13)(a) | encoded | `s 378(13) the Registrar may approve the application` |
| 25134-25138 | s 378(13)(b) | encoded | `s 378(13) the Registrar may approve the application` |
| 25140-25141 | s 378(14) | fork | `s 378(14) the Registrar must refuse to approve the application to reserve the name`; fork F-D1 |
| 25143-25145 | s 378(14)(a) | fork | `s 378(14) the Registrar must refuse to approve the application to reserve the name`; fork F-D1 |
| 25147-25153 | s 378(14)(b) | fork | `s 378(14) the Registrar must refuse to approve the application to reserve the name`; fork F-D1 |
| 25155-25158 | s 378(15) | fork | `s 378(15) the Registrar must reserve the proposed name`; fork F-D1 |
| 25160-25164 | s 378(15)(a) | encoded | `s 378(15) the Registrar must reserve the proposed name`, `s 378(15) the last day of the reservation` |
| 25166-25170 | s 378(15)(b) | encoded | `s 378(15) the Registrar must reserve the proposed name`, `s 378(15) the last day of the reservation` |
| 25172 | s 378(16) | fork | `s 378(16) the person may appeal to the Minister`; fork F-P1 |
| 25174-25175 | s 378(16)(a) | fork | `s 378(16) the person may appeal to the Minister`; fork F-P1 |
| 25177-25183 | s 378(16)(b) | fork | `s 378(16) the person may appeal to the Minister`, `s 378(16) the Minister's decision on the appeal is final`; fork F-P1 |
| 25185-25189 | s 378(17) | encoded | `s 378(17) the reservation of the name entitles the foreign company to be registered by th...` |
| 25191 | s 379 heading | inert, reason 1 | heading (not operative) |
| 25193-25194 | s 379(1) | fork | `s 379(1) the foreign company must keep a register of its members and lodge the notice wit...`, `s 379(1) the act was done within 30 days after the foreign company was registered`; fork F-D1, F-P1 |
| 25196-25197 | s 379(1)(a) | fork | `s 379(1) the foreign company must keep a register of its members and lodge the notice wit...`, `s 379(1)(a) the register of members is kept at a place the paragraph allows`, `s 379(1) the act was done within 30 days after the foreign company was registered`, `s 379(1)(a) the foreign company must keep a register of its members within 30 days after...`; fork F-D1, F-P1 |
| 25199-25205 | s 379(1)(b) | fork | `s 379(1) the foreign company must keep a register of its members and lodge the notice wit...`, `s 379(1) the act was done within 30 days after the foreign company was registered`, `s 379(1)(b) the foreign company must lodge a notice of the address of the register within...`; fork F-D1, F-P1 |
| 25207-25208 | s 379(2) | fork | `s 379(2) the foreign company must keep a register of its members and lodge the notice wit...`, `s 379(2) the act was done within 60 days after 31 March 2017`; fork F-D1, F-P1 |
| 25210-25211 | s 379(2)(a) | fork | `s 379(2) the foreign company must keep a register of its members and lodge the notice wit...`, `s 379(2)(a) the foreign company must keep a register of its members within 60 days after...`; fork F-D1 |
| 25213-25216 | s 379(2)(b) | fork | `s 379(2) the foreign company must keep a register of its members and lodge the notice wit...`, `s 379(2)(b) the foreign company must lodge a notice of the address of the register within...`; fork F-D1 |
| 25218-25223 | s 379(3) | fork | `s 379(3) the foreign company must lodge a notice of the change with the Registrar`, `s 379(3) the notice of the change was lodged within 30 days after the change`, `s 379(3) the foreign company must lodge a notice of the change of address within 30 days...`; fork F-D1, F-P1 |
| 25225-25226 | s 380 heading | inert, reason 1 | heading (not operative) |
| 25228-25229 | s 380(1) | encoded | `s 380(1) the register of members contains the particulars the subsection requires` |
| 25231-25232 | s 380(1)(a) | encoded | `s 380(1) the register of members contains the particulars the subsection requires` |
| 25234-25235 | s 380(1)(b) | encoded | `s 380(1) the register of members contains the particulars the subsection requires` |
| 25237-25238 | s 380(1)(c) | encoded | `s 380(1) the register of members contains the particulars the subsection requires` |
| 25240 | s 380(1)(d) | encoded | `s 380(1) the register of members contains the particulars the subsection requires` |
| 25242-25247 | s 380(1)(d)(i) | encoded | `s 380(1) the register of members contains the particulars the subsection requires` |
| 25249-25255 | s 380(1)(d)(ii) | encoded | `s 380(1) the register of members contains the particulars the subsection requires` |
| 25257-25259 | s 380(1)(e) | encoded | `s 380(1) the register of members contains the particulars the subsection requires` |
| 25261-25263 | s 380(2) | fork | `s 380(2) the foreign company must keep an index of the names of its members`; fork F-D1 |
| 25265-25266 | s 380(2)(a) | encoded | `s 380(2) the foreign company must keep an index of the names of its members`, `s 380(2)(a) the foreign company must keep an index in convenient form of the names of its...` |
| 25268-25270 | s 380(2)(b) | fork | `s 380(2) the foreign company must keep an index of the names of its members`, `s 380(2)(b) the index was altered within 14 days after the alteration of the register`, `s 380(2)(b) the foreign company must make the necessary alteration in the index within 14...`; fork F-P1 |
| 25272-25275 | s 380(2)(c) | encoded | `s 380(2) the foreign company must keep an index of the names of its members`, `s 380(2)(c) the index is kept where paragraph (c) requires`, `s 380(2)(c) the foreign company must keep the index at the same place as the register of...` |
| 25277-25281 | s 380(3) | encoded | `s 380(3) the index contains what the subsection requires` |
| 25283-25288 | s 380(4) | fork | `s 380(4) the foreign company must update the register of members to reflect the change`, `s 380(4) the register was updated within 30 days after the change`, `s 380(4) the foreign company must update the register of members within 30 days after the...`; fork F-D1, F-P1 |
| 25290 | s 381 heading | inert, reason 1 | heading (not operative) |
| 25292-25296 | s 381 | encoded | `s 381 the register is prima facie evidence of the matter` |
| 25298 | s 382 heading | inert, reason 1 | heading (not operative) |
| 25300-25313 | s 382 | encoded | `s 382 the certificate is prima facie evidence of the title of the member to the shares an...` |
| 25315-25316 | s 383 heading | inert, reason 1 | heading (not operative) |
| 25318-25322 | s 383(1) | encoded | `s 383(1) the disposition is void` |
| 25324-25329 | s 383(2) | encoded | `s 383(2) the civil proceedings may not be brought or maintained` |
| 25331 | s 384 heading | inert, reason 1 | heading (not operative) |
| 25333 | s 384 | encoded | `s 384(a)(i) the provision of Division 7 of Part 4 relating to the transfer of shares appl...`, `s 384(a)(ii) the provision of Division 4 of Part 5 relating to the register of members ap...`, `s 384(b) the foreign company is exempt from the provision of this Division` |
| 25335 | s 384(a) | encoded | `s 384(a)(i) the provision of Division 7 of Part 4 relating to the transfer of shares appl...`, `s 384(a)(ii) the provision of Division 4 of Part 5 relating to the register of members ap...`, `s 384(b) the foreign company is exempt from the provision of this Division` |
| 25337-25339 | s 384(a)(i) | encoded | `s 384(a)(i) the provision of Division 7 of Part 4 relating to the transfer of shares appl...`, `s 384(a)(ii) the provision of Division 4 of Part 5 relating to the register of members ap...`, `s 384(b) the foreign company is exempt from the provision of this Division` |
| 25341-25343 | s 384(a)(ii) | encoded | `s 384(a)(i) the provision of Division 7 of Part 4 relating to the transfer of shares appl...`, `s 384(a)(ii) the provision of Division 4 of Part 5 relating to the register of members ap...`, `s 384(b) the foreign company is exempt from the provision of this Division` |
| 25345-25346 | s 384(a) [the second paragraph lettered so] | encoded | `s 384(a)(i) the provision of Division 7 of Part 4 relating to the transfer of shares appl...`, `s 384(a)(ii) the provision of Division 4 of Part 5 relating to the register of members ap...`, `s 384(b) the foreign company is exempt from the provision of this Division` |
| 25348-25351 | s 384(b) | encoded | `s 384(a)(i) the provision of Division 7 of Part 4 relating to the transfer of shares appl...`, `s 384(a)(ii) the provision of Division 4 of Part 5 relating to the register of members ap...`, `s 384(b) the foreign company is exempt from the provision of this Division` |
| 25353 | s 385 | repealed or blank in this text | the text shows `[Repealed by Act 15 of 2017]` |
| 25355 | s 386 heading | inert, reason 1 | heading (not operative) |
| 25357-25370 | s 386 | fork | `s 386 a penalty or punishment is expressly mentioned in the provision`, `s 386 the penalty if the element is met`, `s 386 the offence and its penalty`; fork F-O1, F-S1 |

## Fork register (sgg)

One line per site where the text can be read two ways with different outcomes: the provision, the function, the answer taken, the other reading, and the text that licenses the answer.
The ids are labels local to this part and each stands for one reading: **D** a gate that is not met; **P** the counting of a period; **S** the two split sites the brief asks to be recorded one by one; **E**, **I**, **O**, **T**, **L**, **U**, **B** single readings.
(The keel's own register uses the ids P1 to P9 for its counting conventions, in `sg-periods.l4`; this part's F-P1 and F-P3 cite them and are not the same list.)
Every answer is assumed, not ruled, unless the line says it follows a Guide ruling; a human reviewer may overrule any of them.

**The Guide's rulings, word for word** (`inputs/ENCODING-GUIDE.md`, section 5, each copied by script from the line named, so a change in the Guide shows here as a failed build of these notes):

> **Guide line 86.** In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
>
> **Guide line 87.** Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
>
> **Guide line 92.** - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
>
> **Guide line 93.** - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
>
> **Guide line 94.** - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
>
> **Guide line 95.** - **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.
>
> **Guide line 96.** - **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The ruling sets three limits:
>
> **Guide line 97.** 1. answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed;
>
> **Guide line 98.** 2. keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question;
>
> **Guide line 99.** 3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it).
>

**The readings:**

| id | the reading | answer taken | the other reading | what licenses it |
| --- | --- | --- | --- | --- |
| F-D1 | a duty, a bar or the provision's own question whose gate ("if", "where", "when", "upon", "on receipt", "except", "unless", "until", a date the text names, or the Registrar's opinion) is not met | JUST FALSE: the gate is the text's own word, so a case outside it is the text's no | NOTHING: "if A then B" does not itself say "if not A then not B" | Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except")"; Guide line 95: "a duty whose "if" or "where" is unmet"; Guide line 98: "and for a bar, a duty or the provision's own question" |
| F-P1 | "within N days (weeks, months, years) after X", for a duty or a right to act | in time on every day up to and including the last day, so an act on X itself or before X is in time (`period: the date is not later than the end of a period after`) | the window opens the day after X, so an act on X itself is not "within" it (`period: the date is within a period after`) | Guide line 93: "a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`"; sg-periods.l4, convention P2: the Act is silent on how a period is counted |
| F-P3 | "a period of at least N years (months) has passed after the date" | passed from the day after the last day of the period: the day asked is later than `period: the last day of a period after` (the same reading as "after the expiration of", s 375(4)) | passed on the last day of the period itself | sg-periods.l4, conventions P1 and P4: the Act counts nothing itself |
| F-S1 | an unmet element of an offence (split site (i)) | JUST FALSE: the offence section is the provision's own question, and the element ("If default is made", "who knowingly and wilfully authorises or permits") is in its own words | NOTHING: an unmet element is only the absence of one ground for the offence | Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; Guide line 98: "and for a bar, a duty or the provision's own question" |
| F-S3 | a "may" gated by "where", "when", "upon", "on application" (split site (ii)) | JUST FALSE when the gate fails (the periods ruling, item (b), with "upon" counted as "where" by item (c) of the delegated-definitions ruling) | NOTHING (the grant ruling: the "In short" line on grants points the other way) | Guide line 93: "a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; Guide line 99: "do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon"" |
| F-E1 | an "entitled"-named function (s 373(8)) | JUST TRUE when the purpose is s 373(7A) and the act is one the subsection names; NOTHING otherwise | JUST FALSE otherwise (an entitlement is a claim, not a power) | Guide line 99: "an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it)" |
| F-I1 | a date the section leaves to another Act (s 370A(6): the commencement of section 47 of the ACRA (Registry and Regulatory Enhancements) Act 2024) | a supplied fact: the date is an input and the function returns it | a date read from memory of that Act (not done: it is not among the sources) | the text itself; the Guide has no line for it |
| F-O1 | a director of the foreign company under an offence that names "every officer of the company who is in default" (ss 378(7) and 386) | a director is an officer: `s 4(1) "officer" what the person is` has the constructor `a director of the corporation` | a director is not an officer for these sections: NOTHING for a director, because only officers and authorised representatives are named | the text itself; the Guide has no line for it |
| F-O2 | s 372(1)(ca): particulars of a director or authorised representative "other than the director's or authorised representative's residential address" | JUST FALSE for a change of the residential address (the text's own "other than"; subsection (1A) deals with it) | NOTHING (the exclusion says only that paragraph (ca) does not reach the address) | Guide line 95: ""(other than X)"" |
| F-T1 | the "further time as the Registrar in special circumstances allows" of s 377(2)(b) | the allowance is a last day the Registrar fixed, whether it is added to the 14 days or replaces them; the function takes that last day as an input | the allowance is a length of time counted from the end of the 14 days, which the function would have to compute | the text itself; the Guide has no line for it |
| F-T2 | the notice of the appointment of a liquidator in s 377(2) ("and, when a liquidator is appointed, notice of such appointment") | the time limits (a) and (b) govern the notice of the liquidation or dissolution; the notice of the appointment has no limit of its own, so its rule has no breach path | the 14 days (or the further time) also govern the notice of the appointment | the text itself; the Guide has no line for it |
| F-L1 | the "and" between s 378(3)(a)(i) and (a)(ii) | two cases, each with its own period (3 months after a notice of cessation; 6 years after a striking off) | one name that must have both histories, needing both periods | the text itself; the Guide has no line for it |
| F-U1 | the words "or as provided in subsection (2)" in s 378(1) | an input, `subsection (2) provides that the Registrar is not to refuse`, taken as the text has it | read "(2)" as "(3)", which is where the exception to subsection (1) is ("Despite subsection (1), the Registrar may ... register") | the text itself; the Guide has no line for it |
| F-U2 | s 370(2)(c): "An authorised representative, until he or she ceases to be such in accordance with subsection (5) ... shall be personally liable to all penalties imposed on the company" | JUST FALSE once the person has ceased to be an authorised representative (the "until" is the text's own limit) | NOTHING: the text does not say who bears a penalty for a contravention made while the person was the representative and the notice has since taken effect | Guide line 86: "(and plain variants such as "while", "until" and "except")" |
| F-B1 | s 368(3): "The following must be made available for inspection at the registered office of the foreign company" | the text names no bearer of the duty, so no regulative rule is derived; the decision function answers whether the documents are available (JUST FALSE if not) | the foreign company is the bearer (it keeps the registered office), and a regulative rule is derived | the text itself; the Guide has no line for it |

**The sites, one line each** (text order within each id):

| id | provision | function | answer taken | the other reading | the words relied on |
| --- | --- | --- | --- | --- | --- |
| F-D1 | s 368(1) | `s 368(1) the Registrar must register the foreign company under this Division` | JUST FALSE | NOTHING | "and on payment of the appropriate fees ..., the Registrar must register the foreign company under this Division by registration of the documents" |
| F-D1 | s 368A(3) | `s 368A(3) the director or authorised representative must give the foreign company the information o...` | JUST FALSE | NOTHING | "a director or an authorised representative must, subject to subsection (4), if requested by the foreign company, give the company any information referred to in section 368(1)(d) or (e) for the purpose of enabling the company to... |
| F-D1 | s 369(1) | `s 369(1) the Registrar must refuse to register the foreign company` | JUST FALSE | NOTHING | "the Registrar must refuse to register a company under this Division if the Registrar is satisfied that the foreign company is being used or is likely to be used for an unlawful purpose ... or it would be contrary to the national... |
| F-D1 | s 370(6)(a) | `s 370(6)(a) the foreign company must appoint another authorised representative` | JUST FALSE | NOTHING | "Where the authorised representative in respect of whom the notice under subsection (3) has been lodged is the sole authorised representative of a foreign company — (a) the foreign company must appoint another authorised represen... |
| F-D1 | s 370A(5) | `s 370A(5) the notice or information must provide the information required under section 368 as in f...` | JUST FALSE | NOTHING | "Where the notice or information mentioned in subsection (4) is lodged or given on or after the commencement date, the notice or information must provide the information required under section 368 as in force when the notice or i... |
| F-D1 | s 371(2) | `s 371(2) the Registrar must issue the foreign company a certificate confirming the particulars` | JUST FALSE | NOTHING | "Upon the application of the foreign company that has been duly registered and payment of the prescribed fee, the Registrar must issue to the foreign company a certificate" |
| F-D1 | s 372(4) | `s 372(4) the foreign company must lodge a copy of the order with the Registrar` | JUST FALSE | NOTHING | "If any order is made by a court under any law in force in the country in which a foreign company is incorporated which corresponds to section 210 of this Act or section 71 of the Insolvency, Restructuring and Dissolution Act 201... |
| F-D1 | s 375(1)(c) | `s 375(1)(c) the foreign company must cause notice that the liability of its members is limited to b...` | JUST FALSE | NOTHING | "if the liability of its members is limited" |
| F-D1 | s 377(1) | `s 377(1) the foreign company must lodge with the Registrar notice that it has ceased` | JUST FALSE | NOTHING | "If a foreign company ceases to have a place of business in Singapore or to carry on business in Singapore, it must ... lodge with the Registrar notice of that fact" |
| F-D1 | s 377(1B) | `s 377(1B) the Registrar must record in the register that the company has ceased to have a place of...` | JUST FALSE | NOTHING | "The Registrar must as soon as practicable after the lodgment of the notice mentioned in subsection (1) record in the register that the company has ceased to have a place of business in Singapore ..., as the case may be" |
| F-D1 | s 377(1B) | `s 377(1B) the Registrar must record in the register that the company has ceased to carry on busines...` | JUST FALSE | NOTHING | "record in the register that the company has ... ceased to carry on business in Singapore, as the case may be" |
| F-D1 | s 377(2) | `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the liquidation o...` | JUST FALSE | NOTHING | "If a foreign company goes into liquidation or is dissolved in its place of incorporation or origin, each person who immediately before the commencement of the liquidation proceedings was an authorised representative must ... lod... |
| F-D1 | s 377(2) | `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the appointment o...` | JUST FALSE | NOTHING | "each person who immediately before the commencement of the liquidation proceedings was an authorised representative must ... lodge or cause to be lodged with the Registrar ... when a liquidator is appointed, notice of such appoi... |
| F-D1 | s 377(5) | `s 377(5) the Registrar must record in the register that the foreign company has been dissolved` | JUST FALSE | NOTHING | "On receipt of a notice from an authorised representative that the foreign company has been dissolved, the Registrar must record in the register that the foreign company has been dissolved" |
| F-D1 | s 377(8) | `s 377(8) the Registrar must strike the name of the foreign company off the register` | JUST FALSE | NOTHING | "The Registrar must strike the name of a foreign company off the register if the Registrar is satisfied that ..." |
| F-D1 | s 377B(1) | `s 377B(1) the Registrar must give notice to the applicant of the decision` | JUST FALSE | NOTHING | "The Registrar must give notice to the applicant of the decision on an application under section 377A" |
| F-D1 | s 377B(3)(a) | `s 377B(3)(a) the Registrar must enter in the register a note of the restoration date` | JUST FALSE | NOTHING | "The Registrar must — (a) enter in the register a note of the restoration date" |
| F-D1 | s 377B(3)(b) | `s 377B(3)(b) the Registrar must cause notice of the restoration to be published in the Gazette and...` | JUST FALSE | NOTHING | "The Registrar must — ... (b) cause notice of the restoration to be published in the Gazette and on the Authority's website" |
| F-D1 | s 378(1) | `s 378(1) the Registrar must refuse to register the foreign company under the name` | JUST FALSE | NOTHING | "Except with the consent of the Minister or as provided in subsection (2), the Registrar must refuse" |
| F-D1 | s 378(2) | `s 378(2) the Registrar must refuse to register the foreign company under the name` | JUST FALSE | NOTHING | "the Registrar must, on or after 3 January 2016, except with the consent of the Minister, refuse to register a foreign company under a name, if — (a) it is identical to the name of a company that was dissolved — (i) unless ... a... |
| F-D1 | s 378(5) | `s 378(5) the foreign company must comply with the direction` | JUST FALSE | NOTHING | "the company must comply with the direction ..., unless the direction is annulled by the Minister" |
| F-D1 | s 378(10) | `s 378(10) the Minister must cause the direction to be published in the Gazette` | JUST FALSE | NOTHING | "The Minister must cause a direction given by the Minister under subsection (1)(d) to be published in the Gazette" |
| F-D1 | s 378(14) | `s 378(14) the Registrar must refuse to approve the application to reserve the name` | JUST FALSE | NOTHING | "The Registrar must refuse to approve an application to reserve a name under subsection (11) if the Registrar is satisfied that —" |
| F-D1 | s 378(15) | `s 378(15) the Registrar must reserve the proposed name` | JUST FALSE | NOTHING | "Where an application for a reservation of a name is made under subsection (11), the Registrar must reserve the proposed name" |
| F-D1 | s 379(1) | `s 379(1) the foreign company must keep a register of its members and lodge the notice within 30 day...` | JUST FALSE | NOTHING | "A foreign company registered under this Division on or after 31 March 2017 must, within 30 days after it is registered —" |
| F-D1 | s 379(2) | `s 379(2) the foreign company must keep a register of its members and lodge the notice within 60 day...` | JUST FALSE | NOTHING | "A foreign company registered under this Division before 31 March 2017 must, within 60 days after that date —" |
| F-D1 | s 379(3) | `s 379(3) the foreign company must lodge a notice of the change with the Registrar` | JUST FALSE | NOTHING | "If there is any change in the address at which the register of members ... is kept, the foreign company must, within 30 days after the change, lodge a notice of the change with the Registrar" |
| F-D1 | s 380(2) | `s 380(2) the foreign company must keep an index of the names of its members` | JUST FALSE | NOTHING | "Every foreign company having more than 50 members must, unless the register of members is in such a form as to constitute in itself an index —" |
| F-D1 | s 380(4) | `s 380(4) the foreign company must update the register of members to reflect the change` | JUST FALSE | NOTHING | "If there is any change in the particulars mentioned in subsection (1) contained in the register of members of a foreign company, the foreign company must, within 30 days after the change, update the register" |
| F-P1 | s 368A(1) | `s 368A(1) the director gave the information not later than 14 days after the initial appointment` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "as soon as practicable but not later than 14 days after his or her initial appointment" |
| F-P1 | s 368A(2)(a) | `s 368A(2)(a) the authorised representative gave the information not later than 14 days after the in...` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "as soon as practicable but not later than 14 days after his or her initial appointment" |
| F-P1 | s 368A(2)(b) | `s 368A(2)(b) the authorised representative gave the information not later than 14 days after the ch...` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "as soon as practicable but not later than 14 days after any change in his or her particulars" |
| F-P1 | s 368A(4) | `s 368A(4) the information was furnished not later than 14 days after receipt of the written request` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "must furnish the information to the foreign company as soon as practicable but not later than 14 days after receipt of a written request" |
| F-P1 | s 369(2) | `s 369(2) the foreign company may appeal to the Minister` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "may, within 30 days of the date of the decision, appeal to the Minister" |
| F-P1 | s 370(7) | `s 370(7) the foreign company appointed another authorised representative within 21 days after the d...` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "the company must, within 21 days after the death of the authorised representative, appoint another authorised representative" |
| F-P1 | s 372(1) | `s 372(1) the particulars of the change were lodged within the time` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "the foreign company must, within 30 days or within such further period as the Registrar in special circumstances allows after the change or alteration, lodge with the Registrar particulars of the change or alteration and such do... |
| F-P1 | s 372(1A) | `s 372(1A) the notice of the new residential address was lodged within 30 days after the change` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "must lodge with the Registrar a notice of the director's or authorised representative's new residential address within 30 days after the date of change" |
| F-P1 | s 372(4) | `s 372(4) the copy of the order was lodged within the time` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "the company must, within 30 days or within such further period as the Registrar in special circumstances allows after the order was made, lodge with the Registrar a copy of that order" |
| F-P1 | s 377(1) | `s 377(1) the notice was lodged within 7 days after the foreign company ceased` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "it must, within 7 days after so ceasing, lodge with the Registrar notice of that fact" |
| F-P1 | s 377(2) | `s 377(2) the notice was lodged within the time the subsection allows` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "(a) within 14 days after the commencement of the liquidation or the dissolution; or (b) within such further time as the Registrar in special circumstances allows" |
| F-P1 | s 377(13) | `s 377(13) the person may appeal to the Minister` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "may, within 30 days after the date of the decision, appeal to the Minister" |
| F-P1 | s 377A(2) | `s 377A(2) the application is not valid` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "is not valid unless the application is received by the Registrar within 6 years" |
| F-P1 | s 377D(4) | `s 377D(4) the application to the Court for the directions or orders may be made` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "may be made any time within 3 years after the date of restoration" |
| F-P1 | s 378(5) | `s 378(5) the foreign company complied with the direction within the time allowed` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "within 6 weeks after the date of the direction or such longer period as the Registrar may allow" |
| F-P1 | s 378(9)(a) | `s 378(9)(a) the foreign company may appeal to the Minister against the Registrar's decision under s...` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "within 30 days after the decision" |
| F-P1 | s 378(9)(b) | `s 378(9)(b) the applicant may appeal to the Minister against the Registrar's refusal to give a dire...` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "within 30 days after being informed of the refusal" |
| F-P1 | s 378(16) | `s 378(16) the person may appeal to the Minister` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "may, within 30 days after being informed of the Registrar's decision, appeal to the Minister" |
| F-P1 | s 379(1) | `s 379(1) the act was done within 30 days after the foreign company was registered` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "must, within 30 days after it is registered" |
| F-P1 | s 379(2) | `s 379(2) the act was done within 60 days after 31 March 2017` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "must, within 60 days after that date" |
| F-P1 | s 379(3) | `s 379(3) the notice of the change was lodged within 30 days after the change` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "must, within 30 days after the change, lodge a notice of the change with the Registrar" |
| F-P1 | s 380(2)(b) | `s 380(2)(b) the index was altered within 14 days after the alteration of the register` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "within 14 days after the date on which any alteration is made in the register of members, make any necessary alteration in the index" |
| F-P1 | s 380(4) | `s 380(4) the register was updated within 30 days after the change` | not later than the last day (an early act is in time); JUST FALSE after it | a window that opens the day after the event; an act on the event day is out | "must, within 30 days after the change, update the register of members to reflect the change" |
| F-P3 | s 378 | `s 378 a period of at least the number of units has passed after the date` | later than the last day of the period | on or after the last day of the period | "a period of at least N years has passed after the date": counted as passed from the day after the last day of the period (the same reading as "after the expiration of", s 375(4); fork F-P3). |
| F-P3 | s 378(2) | `s 378(2) the Registrar must refuse to register the foreign company under the name` | later than the last day of the period | on or after the last day of the period | "the Registrar must, on or after 3 January 2016, except with the consent of the Minister, refuse to register a foreign company under a name, if — (a) it is identical to the name of a company that was dissolved — (i) unless ... a... |
| F-S1 | s 368A(5) | `s 368A(5) the penalty for a director or authorised representative` | JUST FALSE | NOTHING | "A director or an authorised representative who is bound to comply with a requirement under this section and fails to do so shall be guilty of an offence" |
| F-S1 | s 372(1C) | `s 372(1C) the penalty if default is made` | JUST FALSE | NOTHING | "If default is made by any director or authorised representative of a foreign company in complying with subsection (1A), he or she shall be guilty of an offence" |
| F-S1 | s 373(18) | `s 373(18) the penalty if the element is met` | JUST FALSE | NOTHING | "If default is made by a foreign company in complying with this section, other than subsection (7A) — (a) the company; and (b) every director or equivalent person, and every authorised representative of the company, who knowingly... |
| F-S1 | s 373(18A) | `s 373(18A) the penalty if the element is met` | JUST FALSE | NOTHING | "If default is made by a foreign company in complying with subsection (7A) — (a) the company shall be guilty of an offence ...; and (b) every director or equivalent person, and every authorised representative, of the company, who... |
| F-S1 | s 378(7) | `s 378(7) the penalty if the element is met` | JUST FALSE | NOTHING | "If the foreign company fails to comply with subsection (4), the company and every officer of the company who is in default and every authorised representative of the company who knowingly and wilfully authorises or permits the d... |
| F-S1 | s 386 | `s 386 the penalty if the element is met` | JUST FALSE | NOTHING | "If default is made by any foreign company in complying with any provision of this Division, other than a provision in which a penalty or punishment is expressly mentioned, the company and every officer of the company who is in d... |
| F-S3 | s 373(10) | `s 373(10) the Registrar may extend the period for the requirement` | JUST FALSE | NOTHING | "The Registrar may, on application by a foreign company and payment of the prescribed application fee, extend the period" |
| F-S3 | s 373(12) | `s 373(12) the Registrar may waive the requirement to lodge the documents referred to in subsection...` | JUST FALSE | NOTHING | "The Registrar may, upon the written application of a foreign company, waive the requirement" |
| F-S3 | s 373(13) | `s 373(13) the Registrar may make the order on the application` | JUST FALSE | NOTHING | "The Registrar may, upon the application of a foreign company, make an order" |
| F-S3 | s 373(13A) | `s 373(13A) the Registrar may make the order relieving the foreign company from the requirement` | JUST FALSE | NOTHING | "The Registrar may, upon the application of a foreign company, make an order relieving the foreign company from any requirement relating to audit or the form and content of the documents referred to in subsection (7) or (7A)" |
| F-S3 | s 377(10) | `s 377(10) the Registrar may strike the name of the foreign company off the register on the applicat...` | JUST FALSE | NOTHING | "The Registrar may strike the name of a foreign company off the register upon the application of the sole authorised representative of the foreign company in the prescribed form" |
| F-S3 | s 377D(3) | `s 377D(3) the Court may give directions and make orders as seem just for placing the foreign compan...` | JUST FALSE | NOTHING | "On the application by any person, the Court may give directions and make orders" |
| F-S3 | s 378(5) | `s 378(5) the Registrar may direct the foreign company to change its name` | JUST FALSE | NOTHING | "where the Registrar is satisfied that a foreign company has been registered ... by a name — (a) ...; (b) ...; or (c) ..., the Registrar may direct the foreign company to change its name" |
| F-E1 | s 373(8) | `s 373(8) the foreign company is entitled to make the apportionments and add the notes and explanati...` | NOTHING outside the purpose and the acts named | JUST FALSE outside them | (8) "entitled to make such apportionments of expenses ... and to add such notes and explanations as in its opinion are necessary or desirable": an entitlement (fork F-E1). |
| F-I1 | s 370A(6) | `s 370A(6) "commencement date" the commencement date` | an input | a remembered date | That Act is not among the sources and the section's own text does not give the date, so it is a supplied fact: fork F-I1. |
| F-O1 | s 378(7) | `s 378(7) the offence and its penalty` | a director is an officer | a director is not named | WHEN `s 365 role: a director of the foreign company, or an equivalent person` THEN `s 378(7) the penalty if the element is met` (`the foreign company fails to comply with subsection (4)` AND `the officer is in default`)   -- s 4(... |
| F-O1 | s 386 | `s 386 the offence and its penalty` | a director is an officer | a director is not named | WHEN `s 365 role: a director of the foreign company, or an equivalent person` THEN `s 386 the penalty if the element is met` (`default is made by the foreign company in complying with a provision of this Division` AND (NOT `the p... |
| F-O2 | s 372(1) | `s 372(1) the change is one the subsection names` | JUST FALSE | NOTHING | "(ca) the particulars of any director or authorised representative of the foreign company which are lodged with the Registrar under section 368(1), other than the director's or authorised representative's residential address" |
| F-T1 | s 377(2) | `s 377(2) the notice was lodged within the time the subsection allows` | an input: the last day allowed | a length counted from the 14 days | "(a) within 14 days after the commencement of the liquidation or the dissolution; or (b) within such further time as the Registrar in special circumstances allows" |
| F-T2 | s 377(2) | `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the appointment o...` | no time limit; no breach path | the 14 days govern it too | "each person who immediately before the commencement of the liquidation proceedings was an authorised representative must ... lodge or cause to be lodged with the Registrar ... when a liquidator is appointed, notice of such appoi... |
| F-L1 | s 378(3) | `s 378(3) the Registrar may register the foreign company under the name` | two cases | one name with both histories | The "and" between (a)(i) and (a)(ii) is read as joining two cases, each with its own period, not one name that must have both histories (fork F-L1). |
| F-U1 | s 378(1) | `s 378(1) the Registrar must refuse to register the foreign company under the name` | an input | read as subsection (3) | "Except with the consent of the Minister or as provided in subsection (2), the Registrar must refuse" |
| F-U2 | s 370(2)(c) | `s 370(2)(c) the person is personally liable to the penalties imposed on the foreign company for a c...` | JUST FALSE after ceasing | NOTHING | "An authorised representative, until he or she ceases to be such in accordance with subsection (5) — ... (c) shall be personally liable to all penalties imposed on the company for any contravention" |
| F-B1 | s 368(3) | `s 368(3) what the subsection requires to be available for inspection is available` | no bearer, no rule | the foreign company is the bearer | "The following must be made available for inspection at the registered office of the foreign company during the hours in which the registered office of the company is accessible to the public: (a) a copy of the memorandum of appo... |

Sites per id: F-D1 29, F-P1 23, F-P3 2, F-S1 6, F-S3 7, F-E1 1, F-I1 1, F-O1 2, F-O2 1, F-T1 1, F-T2 1, F-L1 1, F-U1 1, F-U2 1, F-B1 1. Total 78.
(Counted by script, one per id and function. The F-P1 sites are the 23 decision functions whose body calls `period: the date is not later than the end of a period after`; the comment tags in the source undercount them. The 22 regulative rules with a `WITHIN` count the same way: `WITHIN n` is "not later than day n". 8 further functions call `period: the last day of a period after` for a limit that is not a window to act in, under the keel conventions P1 and P4, and are not sites of F-P1: `s 370(5) the day the authorised representative ceases to be...`; `s 373(3) the last day for lodging the financial statements`; `s 375(4) the foreign company must comply with subsection (3...`; `s 377(9)(b) the company has failed to appoint an authorised...`; `s 377(10)(a) the company has failed to respond or appoint a...`; `s 377(10)(b) the foreign company has failed to give instruc...`; `s 378 a period of at least the number of units has passed a...`; `s 378(15) the last day of the reservation`.)

## Jural relations (sgg)

One row per provision (or group of subsections that create one relation) that creates a right, privilege, power or immunity, with the correlative; the provisions that create none are listed after the table.
**Assumed, not ruled; a lawyer should confirm it.** The Hohfeld kinds were assigned by hand from the text's own verbs ("must", "may", "is not liable", "is void", "is entitled", "no ... may"); the text names the bearer of a duty or liability far more often than the holder of the correlative claim, so a holder marked "not named in the text" is not guessed at, and a holder given as "the Registrar" is the person the duty is directed to rather than a named claimant.
Provisions addressed only to an official (the Registrar, the Minister, the Court) are asked in the seat only for what they mean to the person; there is no seat for an official.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | kind |
| --- | --- | --- | --- |
| s 367 | the foreign company registered under this Division | anyone who would deny it the power to hold immovable property in Singapore | power ("has power to hold", subject to written law) |
| s 368(1) (lodging) | the Registrar | the foreign company (lodge the documents before it establishes a place of business or begins to carry on business) | claim / duty |
| s 368(1) (registering) | the foreign company that has lodged and paid the fees | the Registrar (must register it under this Division) | claim / duty |
| s 368(3) | not named in the text | not named in the text (fork F-B1): the documents must be available for inspection at the registered office | duty with no named bearer or holder |
| s 368A(1) to (4) | the foreign company (the information is given to it) | a director, or an authorised representative (give the information within 14 days, or on request) | claim / duty |
| s 368A(5) | not named in the text (whoever prosecutes, and the court) | the director or authorised representative who is bound and fails to comply (a fine, and a default penalty) | power / liability |
| s 369(1) | not named in the text | the Registrar (must refuse to register on the grounds named) | duty with no named holder |
| s 369(2) | the foreign company aggrieved by the decision (appeal to the Minister within 30 days) | the Minister (decides; the decision is final) | power / liability, and disability to go further |
| s 370(1) | not named in the text (those who address communications to the registered office, and the public) | the foreign company (a registered office, open for at least 5 hours between 9 a.m. and 5 p.m. each business day) | claim / duty |
| s 370(2)(b) | not named in the text | the authorised representative (answerable for the things the foreign company must do) until he or she ceases to be one | claim / duty |
| s 370(2)(c) | not named in the text | the authorised representative (personally liable to the company's penalties) until he or she ceases to be one, unless he or she satisfies the court that he or she should not be (fork F-U2) | liability, with a defence (privilege) |
| s 370(3) | the foreign company, or its authorised representative (lodge a notice of cessation) | the Registrar (receives it) | power / liability |
| s 370(4) | the Registrar | the foreign company (lodge the notice and the consent statement on the appointment of a new authorised representative) | claim / duty |
| s 370(6)(a), (7) | the Registrar | the foreign company (appoint another authorised representative; within 21 days after the death of the sole one) | claim / duty |
| s 371(1), (2) (issuing) | the foreign company (on its registration; on its application and payment of the fee) | the Registrar (must issue the notice; must issue the certificate) | claim / duty |
| s 372(1) | the Registrar | the foreign company (lodge particulars of a change within 30 days or the further period allowed) | claim / duty |
| s 372(1A) | the Registrar | a director, or an authorised representative (lodge a notice of a new residential address within 30 days) | claim / duty |
| s 372(1C) | not named in the text (whoever prosecutes, and the court) | the director or authorised representative in default (a fine, and a default penalty) | power / liability |
| s 372(4) | the Registrar | the foreign company (lodge a copy of the foreign court order within 30 days or the further period allowed) | claim / duty |
| s 373(1), (3), (7), (7A) | the Registrar | the foreign company (lodge the financial statements, and the audited documents, within the time in subsection (3); ensure the profit and loss account complies) | claim / duty |
| s 373(4) | the Registrar (may require further statements and annexed documents by written notice) | the foreign company | power / liability |
| s 373(5) | the foreign company (not to be required to give what a public company would not) | the Registrar (no power to require it) | immunity / disability |
| s 373(6) | the Registrar | the foreign company (comply with the notice under subsection (4)) | claim / duty |
| s 373(8) | the foreign company (entitled to make apportionments and add notes for the purpose of subsection (7A); fork F-E1) | the Registrar and anyone who would object | privilege / no-right |
| s 373(9) | a foreign company that is dormant in Singapore (may lodge unaudited documents in lieu of subsection (7)) | the Registrar | privilege / no-right |
| s 373(10), (12), (13), (13A), (14), (16) | the Registrar (extend the period; waive; make an order; add conditions; limit, revoke or suspend) | the foreign company | power / liability |
| s 373(15) | not named in the text | the Registrar (must not make an order under subsection (13) or (13A) unless of the opinion the text names) | disability (a limit on a power) |
| s 373(17) | the Minister (by order in the Gazette: substitute accounting standards; exempt a class) | foreign companies of the class | power / liability; for (b), immunity / disability of the Registrar |
| s 373(18), (18A) | not named in the text (whoever prosecutes, and the court) | the foreign company, and every director or equivalent person and every authorised representative who knowingly and wilfully authorises or permits the default (a fine; for (18A)(b)(ii) also imprisonment) | power / liability |
| s 374 | the Registrar | the foreign company (lodge the return on the keeping of registers when it lodges its financial statements) | claim / duty |
| s 375(1)(b), (c), (3) | not named in the text (those who read its documents) | the foreign company (state its name and place of formation; give the notice of limited liability; show the unique entity number) | claim / duty |
| s 375(4) | a foreign company incorporated before 3 January 2016 (need comply with subsection (3) only after 12 months from that date) | anyone who would require compliance sooner | immunity / disability (a transitional release) |
| s 377(1) | the Registrar | the foreign company (lodge notice of ceasing within 7 days) | claim / duty |
| s 377(1A) | the foreign company (from the day it lodges the notice) | the Registrar (no claim to later documents, but still to those that ought to have been lodged before) | immunity / disability |
| s 377(1B), (5) | the foreign company | the Registrar (must record the ceasing; must record the dissolution on receiving the notice) | claim / duty |
| s 377(2) | the Registrar | each person who was an authorised representative immediately before the liquidation (lodge notice within 14 days or the further time; notice of the liquidator's appointment: forks F-T1, F-T2) | claim / duty |
| s 377(8) | not named in the text | the Registrar (must strike the name off if satisfied of the grounds) | duty with no named holder |
| s 377(9), (10), (11) | the Registrar (may strike off; may have regard to the prescribed circumstances) | the foreign company | power / liability |
| s 377(13) | the person aggrieved by a decision under subsection (8), (9) or (10) (appeal to the Minister within 30 days) | the Minister (decides; the decision is final) | power / liability, and disability to go further |
| s 377A(1) | a director or member of a foreign company struck off under s 377(9) or (10) (apply for restoration) | the Registrar (receives and decides) | power / liability |
| s 377A(2) | the Registrar | the applicant (an application out of time is not valid) | immunity / disability |
| s 377B(1), (3) | the applicant (notice of the decision); the public (the Gazette and website notice) | the Registrar | claim / duty |
| s 377B(5) | the applicant, or any other person aggrieved by a refusal to restore (appeal to the Court) | the Court | power / liability |
| s 377B(6), s 377D(3) | the Court (may confirm; may restore; may give directions and make orders on the application of any person) | the foreign company and all other persons | power / liability |
| s 377C(1), (3) | the Registrar (may restore on his or her own initiative if satisfied of a mistake of the Registrar) | the foreign company | power / liability |
| s 377D(2) | the foreign company, its directors or equivalent persons, and its authorised representatives (not liable to a penalty under s 373(18) for the financial year the text names) | the Registrar and the court | immunity / disability |
| s 377D(4) | anyone applying to the Court for directions or orders (within 3 years after the restoration) | the Court (receives and decides it) | power / liability, limited in time |
| s 378(1), (2), (14) | not named in the text | the Registrar (must refuse the name on the grounds the text names, or refuse to approve a reservation) | duty with no named holder |
| s 378(3) | the Registrar (may register a foreign company under a name identical to an earlier name, on the conditions in the paragraphs) | anyone who would object | power / liability |
| s 378(4), (12) | not named in the text | the foreign company (must not use any other name in Singapore; must not be registered by a name not reserved) | claim / duty |
| s 378(5) (direction) | the Registrar (may direct the foreign company to change its name) | the foreign company | power / liability |
| s 378(5) (complying) | the Registrar | the foreign company (must comply within 6 weeks, or the longer period the Registrar allows, unless the direction is annulled by the Minister) | claim / duty |
| s 378(6), (11) | any person (apply for a direction; apply for the reservation of a name) | the Registrar (receives and decides) | power / liability |
| s 378(7) | not named in the text (whoever prosecutes, and the court) | the company, every officer in default, and every authorised representative who knowingly and wilfully authorises or permits the default (a fine of up to $2,000, and a default penalty) | power / liability |
| s 378(9), (16) | the foreign company (against a direction); the applicant (against a refusal to direct); a person aggrieved by a refusal to approve or to extend (appeal to the Minister within 30 days) | the Minister (decides; the decision is final under (16)) | power / liability |
| s 378(13) | the Registrar (may approve an application to reserve a name only if satisfied of the two conditions) | the applicant | power / liability, closed by "only if" |
| s 378(15) | the applicant | the Registrar (must reserve the proposed name for the period the text gives) | claim / duty |
| s 378(17) | no one: a reservation "does not in itself entitle" the foreign company to the name | no one | a disclaimer of a claim |
| s 379(1) to (3) | not named in the text (the Registrar receives the lodgments) | the foreign company (keep a register of members; lodge notice of its address; lodge notice of a change) | claim / duty |
| s 380(1), (2), (3), (4) | not named in the text | the foreign company (the contents of the register; an index where there are more than 50 members; update the register within 30 days) | claim / duty |
| s 383(1) | not named in the text (the person who would take the share or warrant) | the foreign company registered under this Division (the disposition is void) | disability |
| s 383(2) | not named in the text | any claimant (no civil proceedings may be brought or maintained) | immunity / disability |
| s 384(a), (b) | the maker of regulations under s 411 (may apply provisions of the Act to a foreign company; may exempt it) | the foreign company | power / liability; for (b), immunity / disability |
| s 386 | not named in the text (whoever prosecutes, and the court) | the foreign company, every officer in default, and every authorised representative who knowingly and wilfully authorises or permits the default (a fine of up to $1,000, and a default penalty) | power / liability |

Provisions that create no right, privilege, power or immunity (definitions, deemings, counting and evidence rules, transitional deemings, tests with no party): s 365; s 366(1); s 366(2); s 368(2); s 368(4); s 368B; s 370(2)(a); s 370(5); s 370(6)(b); s 370A; s 371 (the evidence rules); s 372(1B); s 373(2); s 373(11); s 373(19); s 375(1)(c)(i); s 375(2); s 376; s 377(12); s 377B(2), (4); s 377C(2); s 377D(1); s 378(8); s 381; s 382; s 384(a)(i), (ii) as definitions of what the regulations may cover; s 386 (the carve-out in the penalty section: `a penalty or punishment is expressly mentioned in the provision`).

## Marginal readings for a lawyer (sgg)

Status-quo reading (a): a failed "if" (or "where", "when", "upon", "on receipt", "except", "unless", "until", or the Registrar's opinion) counts as the text's no, within the provision that holds the gate.
The other reading of (a): the function answers `NOTHING` where its gate fails, because "if A then B" does not itself say "if not A then not B".
Status-quo reading (b): a prohibition or grant limited by its own wording ("includes", a named list without "only", a named date or person) does not say no outside the limit: the function answers `NOTHING`.
The other reading of (b): the function answers `JUST FALSE` outside the limit.
Both are taken as the status quo and are not decided here: a lawyer decides.

Reading (a) is the answer in 55 functions; reading (b) is the answer in 73 functions. Each branch is tagged in the source with `FALSE-kind` or `NOTHING-kind`.
A site that fits none of the Guide's lines would be listed here and say so in its fork line; none of this part's does, and the 7 `F-S3` sites are listed below because the Guide itself says to list them (line 99).

| provision | function | rests on |
| --- | --- | --- |
| s 365 | `s 365 this Division applies to the foreign company` | (b) |
| s 366(2) | `s 366(2) the foreign company is not regarded as carrying on business in Singapore by reason only of the activity` | (b) |
| s 367 | `s 367 the foreign company has power to hold immovable property in Singapore` | (b) |
| s 368(1) | `s 368(1) the Registrar must register the foreign company under this Division` | (a) and (b) |
| s 368(2) | `s 368(2) the document is sufficiently served on the director or authorised representative` | (a) and (b) |
| s 368(4) | `s 368(4) subsection (1) applies to the foreign company as if it began on 29 December 1967` | (b) |
| s 368A(3) | `s 368A(3) the director or authorised representative must give the foreign company the information on request` | (a) |
| s 368A(5) | `s 368A(5) the penalty for a director or authorised representative` | (a) |
| s 368A(5) | `s 368A(5) the offence and its penalty` | (b) |
| s 368B(1)(a) | `s 368B(1)(a) the lodged name and particulars are treated as those of the foreign company's directors` | (a) |
| s 368B(1)(b) | `s 368B(1)(b) the lodged name and particulars of the agents are treated as those of the foreign company's authorised rep...` | (a) |
| s 368B(2)(a) | `s 368B(2)(a) the address lodged for a director is treated as the director's residential address` | (b) |
| s 368B(2)(b) | `s 368B(2)(b) the address lodged for an agent is treated as the agent's residential address as authorised representative` | (b) |
| s 369(1) | `s 369(1) the Registrar must refuse to register the foreign company` | (a) |
| s 369(2) | `s 369(2) the foreign company may appeal to the Minister` | (b) |
| s 369(2) | `s 369(2) the Minister's decision on the appeal is final` | (b) |
| s 370(2)(a) | `s 370(2)(a) the person continues to be the authorised representative of the foreign company` | (a) |
| s 370(2)(b) | `s 370(2)(b) the person is answerable for the acts, matters and things the foreign company must do under this Act` | (a) |
| s 370(2)(c) | `s 370(2)(c) the person is personally liable to the penalties imposed on the foreign company for a contravention of this...` | (a) |
| s 370(3) | `s 370(3) the person may lodge a notice that the authorised representative has ceased or will cease` | (b) |
| s 370(4) | `s 370(4) the foreign company has lodged the notice and the consent statement for the new authorised representative` | (b) |
| s 370(5) | `s 370(5) the day the authorised representative ceases to be an authorised representative` | (b) |
| s 370(6)(a) | `s 370(6)(a) the foreign company must appoint another authorised representative` | (a) |
| s 370(6)(b) | `s 370(6)(b) the day the sole authorised representative ceases to be an authorised representative` | (b) |
| s 370A(1) | `s 370A(1) the alternate address is taken to be the individual's contact address` | (a) |
| s 370A(2) | `s 370A(2) the residential address is taken to be the individual's contact address` | (a) |
| s 370A(3) | `s 370A(3) the contact address is deemed to be a particular lodged with the Registrar under section 368(1) for section 3...` | (b) |
| s 370A(5) | `s 370A(5) the notice or information must provide the information required under section 368 as in force when it is lodg...` | (a) |
| s 371(1) | `s 371(1) the notice is prima facie evidence of the particular in all courts` | (b) |
| s 371(2) | `s 371(2) the Registrar must issue the foreign company a certificate confirming the particulars` | (a) |
| s 371(2) | `s 371(2) the certificate is prima facie evidence of the particular in all courts` | (b) |
| s 372(1) | `s 372(1) the change is one the subsection names` | (a) |
| s 372(1B) | `s 372(1B) the person is taken to have informed the Registrar of the change of residential address` | (a) |
| s 372(1C) | `s 372(1C) the penalty if default is made` | (a) |
| s 372(1C) | `s 372(1C) the offence and its penalty` | (b) |
| s 372(4) | `s 372(4) the foreign company must lodge a copy of the order with the Registrar` | (a) |
| s 373(4) | `s 373(4) the Registrar may require the foreign company by written notice to lodge further statements and annex documents` | (b) |
| s 373(5) | `s 373(5) subsection (4) does not authorise the Registrar to require the particulars or documents` | (b) |
| s 373(6) | `s 373(6) the foreign company has complied with the requirements in the notice` | (b) |
| s 373(7A) | `s 373(7A) the foreign company has ensured that the profit and loss account complies and gives a true and fair view` | (b) |
| s 373(8) | `s 373(8) the foreign company is entitled to make the apportionments and add the notes and explanations` | (b) |
| s 373(9) | `s 373(9) the foreign company may lodge unaudited documents in lieu of subsection (7)` | (b) |
| s 373(10) | `s 373(10) the Registrar may extend the period for the requirement` | (a) and (b) |
| s 373(11) | `s 373(11) the statement and profit and loss account are deemed to have been duly audited` | (a) |
| s 373(12) | `s 373(12) the Registrar may waive the requirement to lodge the documents referred to in subsection (7)` | (a) and (b) |
| s 373(13) | `s 373(13) the Registrar may make the order on the application` | (a) and (b) |
| s 373(13A) | `s 373(13A) the Registrar may make the order relieving the foreign company from the requirement` | (a) and (b) |
| s 373(14) | `s 373(14) the Registrar may make the order unconditionally or subject to conditions` | (b) |
| s 373(15) | `s 373(15) the Registrar is barred from making an order under subsection (13) or (13A)` | (b) |
| s 373(16) | `s 373(16) the order may be limited to a specific period and may be revoked or suspended from time to time` | (b) |
| s 373(18) | `s 373(18) the penalty if the element is met` | (a) |
| s 373(18) | `s 373(18) the offence and its penalty` | (b) |
| s 373(18A) | `s 373(18A) the penalty if the element is met` | (a) |
| s 373(18A) | `s 373(18A) the offence and its penalty` | (b) |
| s 374 | `s 374 the foreign company has lodged the return with its lodgment` | (b) |
| s 375(1)(b) | `s 375(1)(b) the document states the name and the place of formation in legible romanised letters` | (b) |
| s 375(1)(c) | `s 375(1)(c) the foreign company must cause notice that the liability of its members is limited to be given` | (a) |
| s 375(1)(c)(i) | `s 375(1)(c)(i) the document states notice that the liability of the members is limited in legible characters` | (b) |
| s 375(2) | `s 375(2) the section relating to the statement of the name is deemed not to have been complied with` | (b) |
| s 375(3) | `s 375(3) the document shows the unique entity number in a legible form` | (b) |
| s 375(4) | `s 375(4) the foreign company must comply with subsection (3) on the day asked` | (b) |
| s 376 | `s 376 the document is sufficiently served on the foreign company` | (a) and (b) |
| s 377(1) | `s 377(1) the foreign company must lodge with the Registrar notice that it has ceased` | (a) |
| s 377(1B) | `s 377(1B) the Registrar must record in the register that the company has ceased to have a place of business in Singapore` | (a) |
| s 377(1B) | `s 377(1B) the Registrar must record in the register that the company has ceased to carry on business in Singapore` | (a) |
| s 377(2) | `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the liquidation or the dissolution` | (a) |
| s 377(2) | `s 377(2) the person must lodge or cause to be lodged with the Registrar notice of the appointment of a liquidator` | (a) |
| s 377(5) | `s 377(5) the Registrar must record in the register that the foreign company has been dissolved` | (a) |
| s 377(8) | `s 377(8) the Registrar must strike the name of the foreign company off the register` | (a) |
| s 377(9) | `s 377(9) the Registrar may strike the name of the foreign company off the register` | (b) |
| s 377(10) | `s 377(10) the Registrar may strike the name of the foreign company off the register on the application of the sole auth...` | (a) and (b) |
| s 377(11) | `s 377(11) the Registrar may have regard to the circumstances prescribed` | (b) |
| s 377(13) | `s 377(13) the person may appeal to the Minister` | (b) |
| s 377(13) | `s 377(13) the Minister's decision on the appeal is final` | (b) |
| s 377A(1) | `s 377A(1) the person may apply to the Registrar to restore the name of the foreign company to the register` | (b) |
| s 377A(2) | `s 377A(2) the application is not valid` | (b) |
| s 377B(1) | `s 377B(1) the Registrar must give notice to the applicant of the decision` | (a) |
| s 377B(2) | `s 377B(2) the restoration date` | (b) |
| s 377B(3)(a) | `s 377B(3)(a) the Registrar must enter in the register a note of the restoration date` | (a) |
| s 377B(3)(b) | `s 377B(3)(b) the Registrar must cause notice of the restoration to be published in the Gazette and on the Authority's w...` | (a) |
| s 377B(5) | `s 377B(5) the person may appeal to the Court` | (b) |
| s 377B(6)(a) | `s 377B(6)(a) the Court may confirm the Registrar's decision` | (b) |
| s 377B(6)(b) | `s 377B(6)(b) the Court may restore the name of the foreign company to the register and give the directions and make the...` | (b) |
| s 377C(1) | `s 377C(1) the Registrar may on his or her own initiative restore the name of the foreign company to the register` | (b) |
| s 377C(3) | `s 377C(3) the Registrar may restore the name of the foreign company by publishing the notice` | (b) |
| s 377C(3) | `s 377C(3) the day the restoration takes effect` | (b) |
| s 377D(1) | `s 377D(1) the foreign company is regarded as having continued its registration as if its name had not been struck off t...` | (a) |
| s 377D(2) | `s 377D(2) the person is not liable to a penalty under section 373(18) for the financial year` | (b) |
| s 377D(3) | `s 377D(3) the Court may give directions and make orders as seem just for placing the foreign company and all other pers...` | (a) |
| s 378(1) | `s 378(1) the Registrar must refuse to register the foreign company under the name` | (a) and (b) |
| s 378(2) | `s 378(2) the Registrar must refuse to register the foreign company under the name` | (a) |
| s 378(3) | `s 378(3) the Registrar may register the foreign company under the name` | (b) |
| s 378(4) | `s 378(4) the foreign company is barred from using the name in Singapore` | (b) |
| s 378(5) | `s 378(5) the Registrar may direct the foreign company to change its name` | (a) |
| s 378(5) | `s 378(5) the foreign company must comply with the direction` | (a) |
| s 378(6) | `s 378(6) the person may apply to the Registrar to give a direction to the foreign company` | (b) |
| s 378(7) | `s 378(7) the penalty if the element is met` | (a) |
| s 378(7) | `s 378(7) the offence and its penalty` | (b) |
| s 378(9)(a) | `s 378(9)(a) the foreign company may appeal to the Minister against the Registrar's decision under subsection (5)` | (b) |
| s 378(9)(b) | `s 378(9)(b) the applicant may appeal to the Minister against the Registrar's refusal to give a direction under subsecti...` | (b) |
| s 378(10) | `s 378(10) the Minister must cause the direction to be published in the Gazette` | (a) |
| s 378(11) | `s 378(11) the person may apply to the Registrar for the reservation of the name` | (b) |
| s 378(12) | `s 378(12) the foreign company must not be registered by the name` | (b) |
| s 378(14) | `s 378(14) the Registrar must refuse to approve the application to reserve the name` | (a) |
| s 378(15) | `s 378(15) the Registrar must reserve the proposed name` | (a) |
| s 378(15) | `s 378(15) the last day of the reservation` | (b) |
| s 378(16) | `s 378(16) the person may appeal to the Minister` | (b) |
| s 378(16) | `s 378(16) the Minister's decision on the appeal is final` | (b) |
| s 379(1) | `s 379(1) the foreign company must keep a register of its members and lodge the notice within 30 days after it is regist...` | (a) |
| s 379(2) | `s 379(2) the foreign company must keep a register of its members and lodge the notice within 60 days after 31 March 2017` | (a) |
| s 379(3) | `s 379(3) the foreign company must lodge a notice of the change with the Registrar` | (a) |
| s 380(2) | `s 380(2) the foreign company must keep an index of the names of its members` | (a) |
| s 380(4) | `s 380(4) the foreign company must update the register of members to reflect the change` | (a) |
| s 381 | `s 381 the register is prima facie evidence of the matter` | (b) |
| s 382 | `s 382 the certificate is prima facie evidence of the title of the member to the shares and the registration of the shar...` | (b) |
| s 383(1) | `s 383(1) the disposition is void` | (b) |
| s 383(2) | `s 383(2) the civil proceedings may not be brought or maintained` | (b) |
| s 386 | `s 386 the penalty if the element is met` | (a) |
| s 386 | `s 386 the offence and its penalty` | (b) |

Also for a lawyer, not a branch of either reading:
- s 375(1)(c): the text names four endings of the name that make the notice unnecessary: the words "Limited" and "Berhad" and the abbreviations "Ltd." and "Bhd." A name ending "Ltd" with no full stop is not one of the four, so the function treats the notice as still due. The other reading treats "Ltd" as the abbreviation.
- s 378(15)(a): "such further period of 60 days as the Registrar may, on application made in good faith, extend" is read as one further period of 60 days. The other reading lets the Registrar extend more than once.
- s 378(1)(b) and (c): "identical" is the Registrar's opinion and is a plain input; the text gives no test of when two names are identical.

### Reading a result: FALSE and NOTHING (sgg)

This part follows the rule of 2026-10-29 as the Guide states it (line 86, quoted word for word in the fork register), in a foreign company's terms.
- `JUST TRUE` is the section's own test met: the Division applies to the company, the notice must be lodged, the document is sufficiently served, the Registrar must refuse the name.
- `JUST FALSE` is the text saying no in its own words: a "means" or "deemed" test the facts do not meet; a duty whose own "if", "where", "unless" or "until" the facts do not satisfy (s 377(1): the company has not ceased to have a place of business, so the duty to lodge the notice is not on it); a period the text fixes ("within 7 days after so ceasing") when the act is outside it; a flat negative ("is not liable", "may not"); a grant the text closes with "only if" (s 378(13)).
- `NOTHING` is "the text does not say": a list the text does not close (s 366(2) names twelve activities and does not say "only", so a thirteenth is not covered); a grant limited by its own wording whose gate is not met (s 377(9): two grounds for striking off are named without "only if", so a third ground gets no answer); a scope limit with no "only" (s 383(1) is limited to a disposition "in Singapore"); a matter the text hands to regulations, an Act or an authority that is not among the sources (s 384; the Minister's orders under s 373(17); the Business Names Registration Act 2014).
- A caller must never turn `NOTHING` into `FALSE`. For a foreign company, "not covered" does not mean "not required": it means this Division, in this text, says nothing on those facts.
- A bar answers in the bar's direction: `JUST TRUE` means "barred" (s 378(4), s 378(12), s 377A(2), s 383(2)); a bar whose own "unless" is met, or that the facts fall outside, answers `NOTHING` or `JUST FALSE` as the function states, and is never read as a grant.
- A function whose name is a duty ("must ...") answers `JUST FALSE` for "no such duty on these facts", never for "the duty was complied with": compliance is a separate function (`has lodged`, `was lodged within`).

## Seams (sgg)

**Taken from the keel** (PLAN.md section 4 and the sgg row of section 6; each is a call to a keel function, checked in the keel module):
- `s 4(1) "foreign company" the body is a foreign company`, over the `s 4(1) body` record, called by `s 365 this Division applies to the foreign company`. The seat question for s 365 builds the record from ten plain yes/no inputs about the body, and asks three more about the company's place of business and intention (13 inputs).
- `s 4(1) "related corporation" the other corporation is a related corporation of the corporation`, called in s 373(12)(d) with the shared input `the other corporation is deemed to be related to the corporation by virtue of section 6` (BOOLEAN). This is the plan's seam row "sgg line 24382".
- The `period:` functions of `sg-periods.l4` for every counted period (7, 14, 21, 30 and 60 days, 6 weeks, 3 and 6 months, 12 months, 1, 2, 3 and 6 years); no part of this encoding does its own date arithmetic outside the helper `s 378 a period of at least the number of units has passed after the date`, which calls them.
- The core constants `the day 3 January 2016` and `the day 29 December 1967` (`sg-core.l4`).

**Seams the plan lacks (found here):**
- PLAN.md's sgg row (section 6) names neither `s 4(1) "banking corporation" the body is a banking corporation` nor `s 4(1) "accounting entity" the person is an accounting entity`. Both are keel functions in `sg-definitions.l4`, and this part calls them: the first in s 375(1)(c)(ii), the second in s 373(11).
- The plan names `s 4(1) "corporation"`, `"director"`, `"officer"`, `"chief executive officer"`, `"residential address"`, `"Court"`, `"Registrar"` and `"company"` as names to expect. This part calls none of them: the roles are the part's own `s 365 role` (see `NEEDS-CORE.md`), and a director is treated as an officer by fork F-O1 without calling the keel function.
- The plan's seam table has no row for the two citations XREFS lists with another part as owner: s 207 (line 24358, owner sgc2) and s 210 (line 24178, owner sgd). They are taken as supplied facts: `the report complies, insofar as is practicable, with section 207` (s 373(11)) and `a court has made an order under a law in force in the country in which the foreign company is incorporated which corresponds to section 210 of this Act or section 71 of the Insolvency, Restructuring and Dissolution Act 2018` (s 372(4)).
- Citations of sections a later wave encodes (XREFS: ss 27, 344, 344A, 386AF, 386AKA, 386ALA, 411) are supplied facts or constructors, each named for the fact: the s 27(12B) reserved names inside the Registrar's-opinion input of s 378(1)(c); ss 344 and 344A as constructors `s 378(2)(a)(ii)` and `s 378(2)(f)(ii)`; the three returns of s 374 as three yes/no inputs; the regulations of s 384 as three yes/no inputs.
- XREFS lists three cites that are not of this Act: line 25041 (s 8), line 24942 (s 22) and line 24960 (s 39) are "section 8", "section 22" and "section 39" of the Business Names Registration Act 2014 and the Limited Liability Partnerships Act 2005, named in s 378(4)(b), (2)(b) and (2)(d)(i). They are not seams.
- The Business Names Registration Act 2014, the Limited Liability Partnerships Act 2005, the Limited Partnerships Act 2008, the VCC Act, the Insolvency, Restructuring and Dissolution Act 2018, the National Registration Act 1965 and the ACRA (Registry and Regulatory Enhancements) Act 2024 are not among the sources. Each appears as a constructor or a yes/no input named for the fact (for example `the earlier holder of the name`, the report under section 10 of the National Registration Act 1965, and the commencement date of section 47 of the 2024 Act: fork F-I1). Nothing from those Acts is read from memory.
- The Minister's orders (s 373(17)), the prescribed forms, particulars and fees, and the "circumstances as may be prescribed" (s 377(11)) are inputs named for the fact.
- The core `Party` has no foreign company, authorised representative or equivalent-person constructor, so this part declares `s 365 party` and `s 365 role` (see `NEEDS-CORE.md`).

## Split sites (sgg)

The two questions the brief leaves to this part, recorded site by site; nothing is harmonised with any other part.
Each line below is the fork line of its site: the provision, the function, the answer taken and the other reading, followed by the Guide line relied on, quoted word for word.

**(i) An unmet element of an offence or a contravention: 6 sites, every one answered `JUST FALSE`.**
The Guide lines relied on are line 86 ("a condition the text introduces with "if", "only if", "as long as" or "unless"") and line 98, limit 2 of the grant ruling ("and for a bar, a duty or the provision's own question"): the offence section is the provision's own question, and the element the facts do not meet is in its own words ("If default is made ...", "who knowingly and wilfully authorises or permits ...").
The other reading is `NOTHING`: an unmet element is only the absence of one ground. It would rest on line 87 ("limits a grant or prohibition in its own wording and the case falls outside the limit"), which these sections do not invoke: none of the six offence sections limits itself in its wording.

| provision | function | answer taken | the other reading | Guide line relied on | fork line |
| --- | --- | --- | --- | --- | --- |
| s 368A(5) | `s 368A(5) the penalty for a director or authorised representative` | JUST FALSE | NOTHING | line 86 and line 98 (limit 2) | F-S1: "A director or an authorised representative who is bound to comply with a requirement under this section and fails to do so shall be guilty of an offence" |
| s 372(1C) | `s 372(1C) the penalty if default is made` | JUST FALSE | NOTHING | line 86 and line 98 (limit 2) | F-S1: "If default is made by any director or authorised representative of a foreign company in complying with subsection (1A), he or she shall be guilty of an offence" |
| s 373(18) | `s 373(18) the penalty if the element is met` | JUST FALSE | NOTHING | line 86 and line 98 (limit 2) | F-S1: "If default is made by a foreign company in complying with this section, other than subsection (7A) — (a) the company; and (b) every director or equivalent person, and every authorised representative... |
| s 373(18A) | `s 373(18A) the penalty if the element is met` | JUST FALSE | NOTHING | line 86 and line 98 (limit 2) | F-S1: "If default is made by a foreign company in complying with subsection (7A) — (a) the company shall be guilty of an offence ...; and (b) every director or equivalent person, and every authorised repre... |
| s 378(7) | `s 378(7) the penalty if the element is met` | JUST FALSE | NOTHING | line 86 and line 98 (limit 2) | F-S1: "If the foreign company fails to comply with subsection (4), the company and every officer of the company who is in default and every authorised representative of the company who knowingly and wilful... |
| s 386 | `s 386 the penalty if the element is met` | JUST FALSE | NOTHING | line 86 and line 98 (limit 2) | F-S1: "If default is made by any foreign company in complying with any provision of this Division, other than a provision in which a penalty or punishment is expressly mentioned, the company and every offi... |

**(ii) A "may" gated by "where", "when", "upon" or "on application": 7 sites, every one answered `JUST FALSE`.**
The Guide lines relied on are line 93, item (b) of the periods ruling of 2026-11-05 ("a "where ..." condition: when it fails the answer is `JUST FALSE`") and line 94, item (c) (""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above").
The other reading is `NOTHING`, the grant rule of 2026-11-12: line 87 says a function answers `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit", and line 97 (limit 1) says to "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed".
Line 99 (limit 3) says to "do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon"" and not to change the answer, so each of the 7 sites below answers by the periods ruling and is listed in the fork register and in the marginal readings.
A "may" gated by "if" alone is not a split site; it answers `NOTHING` under limit 1 (for example s 373(4), s 373(9), s 377(9), s 377C(1), s 378(3)).
No "may" in these ranges is gated by "with the consent of"; the consent of the Minister in s 378(1) and (2) is an exception to a duty (`must refuse`), not a gate on a "may".

| provision | function | answer taken | the other reading | Guide line relied on | fork line |
| --- | --- | --- | --- | --- | --- |
| s 373(10) | `s 373(10) the Registrar may extend the period for the requirement` | JUST FALSE | NOTHING | line 93 item (b); line 94 item (c); line 99 limit 3 | F-S3: "The Registrar may, on application by a foreign company and payment of the prescribed application fee, extend the period" |
| s 373(12) | `s 373(12) the Registrar may waive the requirement to lodge the documents referred to in subsection...` | JUST FALSE | NOTHING | line 93 item (b); line 94 item (c); line 99 limit 3 | F-S3: "The Registrar may, upon the written application of a foreign company, waive the requirement" |
| s 373(13) | `s 373(13) the Registrar may make the order on the application` | JUST FALSE | NOTHING | line 93 item (b); line 94 item (c); line 99 limit 3 | F-S3: "The Registrar may, upon the application of a foreign company, make an order" |
| s 373(13A) | `s 373(13A) the Registrar may make the order relieving the foreign company from the requirement` | JUST FALSE | NOTHING | line 93 item (b); line 94 item (c); line 99 limit 3 | F-S3: "The Registrar may, upon the application of a foreign company, make an order relieving the foreign company from any requirement relating to audit or the form and content of the documents referred to... |
| s 377(10) | `s 377(10) the Registrar may strike the name of the foreign company off the register on the applicat...` | JUST FALSE | NOTHING | line 93 item (b); line 94 item (c); line 99 limit 3 | F-S3: "The Registrar may strike the name of a foreign company off the register upon the application of the sole authorised representative of the foreign company in the prescribed form" |
| s 377D(3) | `s 377D(3) the Court may give directions and make orders as seem just for placing the foreign compan...` | JUST FALSE | NOTHING | line 93 item (b); line 94 item (c); line 99 limit 3 | F-S3: "On the application by any person, the Court may give directions and make orders" |
| s 378(5) | `s 378(5) the Registrar may direct the foreign company to change its name` | JUST FALSE | NOTHING | line 93 item (b); line 94 item (c); line 99 limit 3 | F-S3: "where the Registrar is satisfied that a foreign company has been registered ... by a name — (a) ...; (b) ...; or (c) ..., the Registrar may direct the foreign company to change its name" |

## Rules with no breach path (sgg)

A regulative `MUST` with no time limit and no stated consequence cannot be shown breached: with no event the obligation stays `RESIDUAL`, and a late act still reads `FULFILLED`.
No deadline and no consequence is invented for any of them.
The rules listed are those whose source has no `WITHIN`, found by script.

| provision | rule | why there is no breach path |
| --- | --- | --- |
| s 370(1) | `s 370(1) the foreign company must have a registered office in Singapore open and accessible to the public` | the text gives this duty no time limit and no consequence |
| s 370(4) | `s 370(4) the foreign company must lodge the notice and the consent statement for the new authorised representative` | the text gives this duty no time limit and no consequence |
| s 370(6)(a) | `s 370(6)(a) the foreign company must appoint another authorised representative` | the text gives this duty no time limit and no consequence |
| s 374 | `s 374 the foreign company must lodge the return when it lodges its financial statements` | the text gives this duty no time limit and no consequence |
| s 375(1)(b) | `s 375(1)(b) the foreign company must cause its name and place of formation to be stated in legible romanised letters` | the text gives this duty no time limit and no consequence |
| s 375(1)(c) | `s 375(1)(c) the foreign company must cause notice that the liability of its members is limited to be given` | the text gives this duty no time limit and no consequence |
| s 375(3) | `s 375(3) the foreign company must cause its unique entity number to appear in a legible form on its business letters an...` | the text gives this duty no time limit and no consequence |
| s 377(2) | `s 377(2) an authorised representative must lodge notice of the appointment of a liquidator when one is appointed` | the text gives the notice of the appointment of a liquidator no time limit of its own (fork F-T2) |
| s 380(2)(a) | `s 380(2)(a) the foreign company must keep an index in convenient form of the names of its members` | the text gives this duty no time limit and no consequence |
| s 380(2)(c) | `s 380(2)(c) the foreign company must keep the index at the same place as the register of members` | the text gives this duty no time limit and no consequence |

10 of the 32 regulative rules have no breach path; the other 22 have a `WITHIN` and a trace that reaches `BREACH` (the act done one day late, or not done), with its `-- EXPECT` comment checked on both stable builds.
The penalty provisions (ss 368A(5), 372(1C), 373(18), 373(18A), 378(7), 386) are decision functions over the facts that return, each as `MAYBE`, whether the offence applies, the maximum fine, the maximum term and whether a default penalty also applies, with the amounts copied from the text; only s 373(18A)(b)(ii) states a term of imprisonment (3 years).

## What the text turns out to say (findings, sgg)

1. Division 2 applies to a foreign company "which" (a) establishes a place of business or carries on business in Singapore, or (b) intends to establish a place of business or carry on business in Singapore (s 365, lines 23615-23622). A body that is not a foreign company within s 4(1) is not covered, and the text gives no answer for it: the function answers `NOTHING`.
2. s 366(1) "carrying on business" has two limbs. (a) "includes" administering, managing or dealing with property in Singapore as an agent, legal personal representative or trustee: the list is open, so an activity outside it gets `NOTHING`. (b) "does not exclude activities carried on without a view to any profit" is a flat negative: the absence of a profit motive is no ground for exclusion (`JUST FALSE` to "kept out only because it is carried on without profit"), but the text does not say such an activity is carrying on business.
3. s 366(2) lists twelve activities that are not carrying on business "for the reason only" that the company does them, and does not say the list is closed, so an activity outside the twelve gets `NOTHING`. Paragraph (h) is limited by its own words: an isolated transaction "completed within a period of 31 days, but not being one of a number of similar transactions repeated from time to time"; the function answers `JUST TRUE` for such a transaction and `NOTHING` for one that took longer or is one of a series. Paragraphs (k) and (l) point outside the text (the Monetary Authority's licensing; what the Minister prescribes).
4. Six provisions turn on 3 January 2016 (ss 366(1), 368B, 375(4), 378(2), 378(3) and 378(9)); ss 379(1) and (2) turn on 31 March 2017; s 368(4) on 29 December 1967. Section 370A(6) leaves its date to another Act (the commencement of section 47 of the ACRA (Registry and Regulatory Enhancements) Act 2024), which is not among the sources: the date is an input (fork F-I1).
5. s 378(1) excepts the Registrar's duty to refuse a name "with the consent of the Minister or as provided in subsection (2)". Subsection (2) adds refusals ("In addition to subsection (1), the Registrar must ... refuse") and excepts nothing from (1); the exception to (1) is in subsection (3) ("Despite subsection (1), the Registrar may ... register"). The function takes "as provided in subsection (2)" as an input and does not read it as (3) (fork F-U1).
6. s 378(3)(a) joins (i) a foreign company that gave notice of cessation under s 377(1) (3 months) and (ii) a foreign company whose name was struck off under s 377(8), (9) or (10) (6 years) with "and". It is read as two cases (fork F-L1); read as one name with both histories, a name would need both periods.
7. s 377(2) gives each person who was an authorised representative (a) 14 days after the commencement of the liquidation or the dissolution, "or" (b) "such further time as the Registrar in special circumstances allows", to lodge notice of that fact "and, when a liquidator is appointed, notice of such appointment". The further time is taken as a last day the Registrar fixed (fork F-T1), and the notice of the appointment has no time limit of its own (fork F-T2), so its rule is listed under the rules with no breach path.
8. s 377(1A) ends the obligation to lodge "any document (not being a document that ought to have been lodged before that day)" starting on the day the notice of cessation was lodged. A document that ought to have been lodged before that day stays due, and before that day, or with no notice lodged, the cessation has not begun; the function answers `JUST FALSE` on each of those three footings, each in the text's own words.
9. Restoration reaches only a name struck off under s 377(9) or (10): ss 377A(1) and 377C(1) name those two subsections and not s 377(8). A name struck off under s 377(8) (a company used for an unlawful purpose) is outside both sections, and the text says nothing of restoring it: `NOTHING`. An application under s 377A must be received within 6 years of the striking off (s 377A(2)), and an application to the Court for directions within 3 years of the restoration (s 377D(4)).
10. s 377D(2) relieves the foreign company, its directors or equivalent persons, and its authorised representatives from "a penalty under section 373(18)" for a financial year whose filing period ended after the striking off and before the restoration. It names s 373(18) and not s 373(18A) (the offence of failing to comply with s 373(7A)); the function is about s 373(18) only and answers `NOTHING` for any other role or year.
11. The offence sections name different people. Sections 373(18) and (18A) name "every director or equivalent person, and every authorised representative ... who knowingly and wilfully authorises or permits the default"; ss 378(7) and 386 name "every officer of the company who is in default and every authorised representative of the company who knowingly and wilfully authorises or permits the default"; ss 368A(5) and 372(1C) name a director or authorised representative. A director is an officer by s 4(1) (fork F-O1), so a director answers under the officer limb of ss 378(7) and 386.
12. s 373(7A) requires a foreign company that lodges a duly audited profit and loss account to ensure "insofar as is practicable" that it complies with the Accounting Standards and gives "a true and fair view" of the profit or loss of its operations in Singapore. Both are judgments the text leaves to the company, so they are inputs. s 373(8) says the company "is entitled" to make apportionments and add notes "for the purpose of subsection (7A)": an entitlement, listed as fork F-E1.
13. s 374 requires a return "containing prescribed information" about three registers (of controllers, s 386AF; of nominee directors, s 386AKA; of nominee shareholders, s 386ALA), lodged "at the time when making a lodgment" of the financial statements or of the other document the Registrar allows instead (s 373(13)(b)). Those sections belong to a later wave, so each return is a yes/no input.
14. s 379(1) and (2) are one duty on two dates: a foreign company registered on or after 31 March 2017 has 30 days after it is registered; one registered before has 60 days after 31 March 2017. A company registered on 31 March 2017 itself falls under (1).
15. s 380(2) requires an index only of "every foreign company having more than 50 members" whose register is not itself an index: 50 members need no index, 51 do.
16. s 383(1) makes void a disposition of a bearer share or share warrant "in Singapore" by a foreign company registered under this Division; a disposition outside Singapore is not void by these words (`NOTHING`). s 383(2) has no "in Singapore": it bars civil proceedings "in any court for or in respect of" such a share or warrant allotted, issued, sold or disposed by such a company.
17. s 384 has two paragraphs lettered (a) in this text: (a)(i) and (a)(ii) provide for the application of Division 7 of Part 4 (transfer of shares) and Division 4 of Part 5 (register of members); the second (a) says "subject to such adaptations, modifications or additions as may be prescribed"; (b) lets the regulations exempt a foreign company or a class from any provision of this Division. The coverage table labels the second one "[the second paragraph lettered so]".
18. Deleted or repealed in this text: s 375(1)(a) (deleted, while (b) and (c) keep their letters), s 372(2) and (3), s 377(3), (4), (4A), (6) and (7), and s 385 are shown deleted or repealed; Division 1 of Part 11 is shown "Repealed by Act 8 of 2003".
19. s 386 applies to a default "in complying with any provision of this Division, other than a provision in which a penalty or punishment is expressly mentioned". The provisions that mention one are ss 368A(5), 372(1C), 373(18), 373(18A) and 378(7); `s 386 provision of this Division` lists them with a sixth constructor for any other provision, and `s 386 a penalty or punishment is expressly mentioned in the provision` answers `JUST TRUE` for the five.
20. s 370(2) makes an authorised representative answerable and "personally liable to all penalties imposed on the company" until he or she ceases to be one "in accordance with subsection (5)", unless he or she "satisfies the court hearing the matter that he or she should be not so liable". The text does not say who bears a penalty for a contravention made while the person was the representative and the notice has since taken effect (fork F-U2).
21. s 368(3) says what "must be made available for inspection at the registered office" and names no bearer, so no regulative rule is derived (fork F-B1). s 372(1)(ca) covers a change in the particulars of a director or authorised representative "other than ... residential address", which s 372(1A) deals with separately (fork F-O2).
22. s 378(2) lists paragraphs (a) to (f) under the lead-in "if —". Paragraphs (a) to (d) end in ";" and the only "or" before the last paragraph stands at the end of (e)(ii), so the text joins the paragraphs by an "or" in the middle of (e). They are read as alternatives (the type `s 378(2) earlier holder of the name` is a choice among them), as the lead-in and the "or" before (f) make plain; each of (a), (d), (e) and (f) has its own sub-cases (i) and (ii), joined by "or".
23. s 378(13) allows the Registrar to approve an application to reserve a name "only if" two conditions hold, so the function answers `JUST FALSE` when they do not; s 378(12) bars registering a name unless it has been reserved under subsection (15); s 378(17) says a reservation "does not in itself entitle" the company to the name.

## What the stable binary does not accept (sgg)

Each item was met on `l4-main-110` (1.6.110) and read the same on `l4-main-109`, or is a property of both that the brief or the plan states; none is a defect of the text.
- There is no `BEFORE` keyword. "Before X" for a duty is written `WITHIN n`, with n an input counted from the start of the trace (`s 368(1)`: the number of days before the company begins).
- `WAITUNTIL` is one word.
- `NOT a OR b` parses as `NOT (a OR b)`, and `NOT a AND b` as `NOT (a AND b)`. Every `NOT` in these modules is bracketed, `((NOT a) OR b)`; one unbracketed `NOT` in s 377B(4) made an assertion fail before it was found, and the same fix went into s 378(2) and (3).
- `JUST (call args)` needs the brackets round the call.
- A `#ASSERT` stays on one line (a trailing `-- comment` is accepted).
- A `MUST` with no `WITHIN` stays `RESIDUAL`, and a late act on it still reads `FULFILLED`: such a rule cannot be shown breached (the section above).
- `Date day month year`: the keel does not define `YMD`, and this part does not either.
- `l4 run` exits 0 when an `#ASSERT` fails (the keel's note, section "What the stable binary does not accept"): the counts `check.sh` prints are what was read, not the exit code.

## What check.sh prints (sgg)

Run from the deposit folder as `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` (target `main`: every module runs with 1.6.110 and with 1.6.109, and the counts must match):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sg-auditors.l4                                 0         0       0        0         0 |      0         0       0        0  same
sg-core.l4                                     0         0       0        0         0 |      0         0       0        0  same
sg-definitions.l4                              0         0       0        0         0 |      0         0       0        0  same
sg-groups.l4                                   0         0       0        0         0 |      0         0       0        0  same
sg-interests.l4                                0         0       0        0         0 |      0         0       0        0  same
sg-interpretation.l4                           0         0       0        0         0 |      0         0       0        0  same
sg-periods.l4                                  0         0       0        0         0 |      0         0       0        0  same
sg-solvency.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgg-cases-seat.l4                              0       375       0        0         0 |      0       375       0        0  same
sgg-cessation.l4                               0         0       0        0         0 |      0         0       0        0  same
sgg-identity.l4                                0         0       0        0         0 |      0         0       0        0  same
sgg-lodging.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgg-names.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgg-registers.l4                               0         0       0        0         0 |      0         0       0        0  same
sgg-returns.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgg-scope.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgg-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgg-tests-cessation.l4                         0       125       0        0         0 |      0       125       0        0  same
sgg-tests-identity.l4                          0        37       0        0         0 |      0        37       0        0  same
sgg-tests-lodging.l4                           0       127       0        0         0 |      0       127       0        0  same
sgg-tests-names.l4                             0       118       0        0         0 |      0       118       0        0  same
sgg-tests-registers.l4                         0        79       0        0         0 |      0        79       0        0  same
sgg-tests-returns.l4                           0       132       0        0         0 |      0       132       0        0  same
sgg-tests-scope.l4                             0        38       0        0         0 |      0        38       0        0  same
TOTAL (24 modules)                             0      1031       0        0           |      0      1031       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The script exited with status 0.
**Baseline it replaced.** The keel's own run (`inputs/KEEL-NOTES.md`, section "What `check.sh` prints"): 17 modules, 974 assertions satisfied, 0 failed, 0 refused, the same four counts on both builds, exit status 0.
**This run:** 24 modules, 1031 assertions satisfied, 0 failed, 0 refused, the same four counts on both builds, exit status 0.
What the move from 974 to 1031 is made of, read from the table above and not from the direction of the number: the 8 keel modules in this folder (`sg-auditors.l4` to `sg-solvency.l4`) each show 0 assertions, because the keel's own test, seat and case files, which carry its 974, are not in this sandbox. The 1031 are all this part's: 656 in the seven `sgg-tests-*.l4` files (38, 127, 132, 37, 125, 118 and 79) and 375 in `sgg-cases-seat.l4`. The two totals are therefore not one count with 57 added to it, and no row of this part replaces a baseline row.

The other gates, run on the files as shipped:

```
$ python3 -I srcrefs.py check --strict RAW sgg-<module>.l4   (and the same with --refs)
sgg-scope.l4   --strict: srcrefs check: 59 src: lines, 5 runs, 6 locators, 0 problems
sgg-scope.l4   --refs:   srcrefs check: 59 src: lines, 5 runs, 6 locators, 0 problems
sgg-lodging.l4 --strict: srcrefs check: 251 src: lines, 29 runs, 48 locators, 0 problems
sgg-lodging.l4 --refs:   srcrefs check: 251 src: lines, 29 runs, 48 locators, 0 problems
sgg-returns.l4 --strict: srcrefs check: 251 src: lines, 29 runs, 42 locators, 0 problems
sgg-returns.l4 --refs:   srcrefs check: 251 src: lines, 29 runs, 42 locators, 0 problems
sgg-identity.l4 --strict: srcrefs check: 44 src: lines, 6 runs, 11 locators, 0 problems
sgg-identity.l4 --refs:   srcrefs check: 44 src: lines, 6 runs, 11 locators, 0 problems
sgg-cessation.l4 --strict: srcrefs check: 140 src: lines, 25 runs, 41 locators, 0 problems
sgg-cessation.l4 --refs:   srcrefs check: 140 src: lines, 25 runs, 41 locators, 0 problems
sgg-names.l4   --strict: srcrefs check: 187 src: lines, 17 runs, 26 locators, 0 problems
sgg-names.l4   --refs:   srcrefs check: 187 src: lines, 17 runs, 26 locators, 0 problems
sgg-registers.l4 --strict: srcrefs check: 100 src: lines, 13 runs, 33 locators, 0 problems
sgg-registers.l4 --refs:   srcrefs check: 100 src: lines, 13 runs, 33 locators, 0 problems

$ python3 work/traces.py sgg-tests-<module>.l4   (every -- EXPECT against l4-main-110 and l4-main-109)
sgg-tests-scope.l4   traces checked: 0, mismatches: 0
sgg-tests-lodging.l4 traces checked: 20, mismatches: 0
sgg-tests-returns.l4 traces checked: 16, mismatches: 0
sgg-tests-identity.l4 traces checked: 6, mismatches: 0
sgg-tests-cessation.l4 traces checked: 11, mismatches: 0
sgg-tests-names.l4   traces checked: 6, mismatches: 0
sgg-tests-registers.l4 traces checked: 20, mismatches: 0

$ python3 work/mkcov.py   (the coverage audit)
non-blank lines: 1248 rows: 329 unassigned: 0
Counter({'encoded': 222, 'fork': 68, 'inert': 29, 'repealed or blank in this text': 10})
```

## Where PLAN.md and the brief differ (sgg)

- The brief asks `NOTES.md` to open with `## Edition encoded`, to carry `## Seams (sgg)`, and, only if the part has `inputs/NAIVE-EVIDENCE/`, `## Compared with the earlier pass`. PLAN.md section 8, which lists the sections of a part's NOTES, names none of the three. The brief governs: this file has the first two, and there is no `inputs/NAIVE-EVIDENCE/` in this sandbox, so it has no third.
- PLAN.md section 8 names, for the split-site fork lines, Guide line 93, line 87, lines 96 to 99 and line 92; the brief gives line 93 and the grant rule as examples and asks for the Guide's own words. This part quotes lines 86, 87, 93, 94, 97, 98 and 99 in the split-site section and prints lines 86, 87 and 92 to 99 of the Guide word for word in the fork register, so every line either document names is there.

## Status of this file

The coverage, fork-site, jural-relation, marginal-reading and no-breach-path tables, and the Guide quotations, were generated by script (`work/mkcov.py`, `work/mknotes.py`, not shipped) from the raw text, the `@ref` locators and the layer-1 sources, and the prose and findings were then checked line by line against the raw text and the functions they describe.
The readings in them are the encoder's, not a lawyer's.

## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its fork-line comment, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

No site of this part changed under it (2026S1bC): the functions of this part that stay Boolean after the protocol split already answered as the ruling reads, and its protocol-shaped functions keep limit 3 of the grant ruling until they are re-encoded.
