# NOTES (sgm): Companies Act 1967 (Singapore), part sgm

Part agent `sgm` of the wave-2 encoding of the Companies Act 1967 into L4, for the stable binary (1.6.110, with 1.6.109 as the second build).
Everything below is about my ranges only: the lines of `inputs/CoA1967.txt` 17093-17848, 22627-23147, 28877-28896 and 29311-30828.
Nothing outside those lines is encoded here; a provision of another part that these ranges need is an input fact named for the fact and its section.

## Edition encoded (sgm)

- Companies Act 1967, 2020 Revised Edition (Singapore Statutes Online informal consolidation, version in force from 6/5/2026 to 20/10/2026).
  The header of `inputs/CoA1967.txt` says the revised edition "incorporates all amendments up to and including 1 December 2021"; the brief says the consolidation carries amendments up to Act 24 of 2025.
  `inputs/CoA1967.meta.json` records `retrieved_date` 2026-10-09 and `in_force` "Current version as at 09 Oct 2026".
- **The text is a rendering and not the official text.**
  `inputs/CoA1967.txt` is a plain-text rendering of an SSO page; it keeps page furniture, amendment marks and some mislabelled closing words (findings 4 and 1).
  Every quotation in the `.l4` files is a verbatim slice of that rendering, checked by `srcrefs.py` (0 problems with `--refs` and `--strict`); none is from memory and none is claimed to match the Act as printed by the Law Revision Commission.
- **The brief governs where PLAN.md differs.**
  The brief says so itself, and this part followed it.
  The one difference I met in my own row: PLAN.md section 6 (my row) lists the seams I give as ss 196, 197 and 198, while its table A also carries s 190 ("principal register"); I give all four (see Seams).
- Ranges and contents: Part 5 Divisions 4, 4A and 5 (ss 189A to 198), Part 10 (the repealed Divisions 1 to 3, 5 and 6; Division 4 Subdivision (5), ss 344 to 344H), the Seventh to Eleventh Schedules (repealed), the Fourteenth to Sixteenth Schedules (Part 11A: companies and foreign companies excluded, and the meaning of significant control and significant interest), and the Legislative History, Abbreviations and Comparative Table (inert).

## Files (sgm)

All in `encodings/legalese-sonnet-5.5/`, ASCII names beginning `sgm-`:

| file | what | provisions |
| --- | --- | --- |
| `sgm-part5-div4.l4` | layer 1 | ss 189A to 196: the register and index of members of a public company |
| `sgm-part5-div4a.l4` | layer 1 | ss 196A to 196E: the electronic register kept by the Registrar |
| `sgm-part5-div5.l4` | layer 1 | ss 197, 198: the annual return and the financial year (and the seams s 197(1), s 198) |
| `sgm-part10.l4` | layer 1 | ss 344 to 344H: striking off and restoring a company's name |
| `sgm-schedules.l4` | layer 1 | Fourteenth, Fifteenth and Sixteenth Schedules |
| `sgm-tests-*.l4` (5 files) | tests of layer 1 | expected values written from the text, `-- EXPECT` above every `#TRACE` |
| `sgm-seat.l4` | layer 2 | 218 questions in 5 sections, every one `@export` with `@desc` |
| `sgm-cases-seat.l4` | cases of layer 2 | taken from the layer-1 tests with the facts a person in the seat would state |
| `NOTES.md`, `PROGRESS.md` | notes | |

277 layer-1 declarations, each with its `-- src:` quotation and its `@ref` locator (277 `@ref` locators and 1587 quotation lines in the five layer-1 files).

## Coverage (sgm)

One row per unit of the text of my ranges: every section, subsection, paragraph, schedule paragraph and heading, and each repealed or blank block.
The rows were built from the text by script (`work/coverage_data.py`), and `work/covcheck.py` checked that every non-blank line of my ranges falls in some row.
A line that is page furniture (the running heads and page numbers of the rendering) or an amendment mark alone on its line is not text of a provision and has no row of its own.

**Audit.**
Text units counted by an independent script over the text of my ranges (lines that open a section, subsection, paragraph, sub-paragraph or schedule paragraph, by the shape of the label): 356 marker lines; marker lines outside every row: 0; rows that contain at least one marker line: 345.
The other rows are headings, chapeaux, closing words, repealed blocks and the Legislative History, which carry no marker.
Rows in the table: 424.
Non-blank lines in my ranges: 1886; covered by a row: 1834; the other 52 are page furniture or amendment marks; uncovered lines of provision text: 0.
Rows in the table before the audit and after: 424 and 424 (`covcheck.py` printed 424 rows on both of its runs against the complete table; the covered-line count moved from 1833 to 1834 between the two runs and the final count is 1834 with 0 uncovered lines of provision text).
One disposition changed on review: s 197(3) is inert, reason 2 (machinery), see finding 6.

**Counts per disposition** (`encoded` is a rule with a test; `fork` is an encoded row whose declaration cites a fork id other than the keel's period convention F-P2, so a different reading is on record in the fork register; "inert" carries the reason number):

| disposition | rows |
| --- | --- |
| encoded | 95 |
| fork (encoded, reading chosen) | 133 |
| inert, reason 1 (not operative) | 143 |
| inert, reason 2 (machinery) | 1 |
| inert, reason 3 (repealed or blank, as inert) | 0 |
| repealed or blank in this text | 52 |
| total | 424 |

How to read the "L4 name" column: for an encoded or fork row it lists the declarations (up to three; the rest are counted) whose `@ref` locator overlaps the row's lines; it is computed from the code by `work/mk_notes.py`, not typed.
For every other row it says what the text shows.
There is no `out-of-scope` row and no `deferred` row.
Definitions that the text introduces as tables or lists (the Sixteenth Schedule's paragraphs) are encoded as functions with a test on each limb; the headings of divisions, schedules and sub-headings are reason 1.


| unit | lines | disposition | L4 name, or what the text shows | forks |
| --- | --- | --- | --- | --- |
| Part 5 Div 4 heading | 17093-17095 | inert, reason 1 (not operative) | heading: Division 4 -- Register of members kept by public company |  |
| s 189A(1) | 17097-17102 | encoded | `s 189A(1) this Division applies to the company` |  |
| s 189A(2) | 17104-17108 | encoded | `s 189A(2) the register is the register of this Division` |  |
| s 190(1) chapeau | 17110-17113 | encoded | `s 190(1) the company must keep a register of its members`; `s 190(1) the register has every entry the subsection requires`; `s 190(1) the register is the register of members of the company kept pursuant to section 190` (+1 more) |  |
| s 190(1)(a) | 17115-17121 | encoded | `s 190(1)(a) the register enters the names and addresses and, for a company having a share capital, the stat...`; `s 190(1) the register has every entry the subsection requires` |  |
| s 190(1)(b) | 17123-17124 | encoded | `s 190(1)(b) the register enters the date at which the name of each person was entered as a member`; `s 190(1) the register has every entry the subsection requires` |  |
| s 190(1)(c) | 17126-17127 | encoded | `s 190(1)(c) the register enters the date at which a person who ceased to be a member during the previous 7 ...`; `s 190(1) the register has every entry the subsection requires` |  |
| s 190(1)(d) | 17129-17133 | encoded | `s 190(1)(d) the register enters the date and size of every allotment, for a company having a share capital`; `s 190(1) the register has every entry the subsection requires` |  |
| s 190(2) | 17135-17146 | fork (encoded, reading chosen) | `s 190(2) the company must alter the register to show stock instead of shares`; `s 190(2) the register has been altered as the subsection requires` | F-W1 |
| s 190(2A) chapeau | 17148-17149 | fork (encoded, reading chosen) | `s 190(2A)(a) the requirements of subsections (1)(a), (b) and (c) and (2) must be complied with` | F-W1 |
| s 190(2A)(a) | 17151-17154 | fork (encoded, reading chosen) | `s 190(2A)(a) the requirements of subsections (1)(a), (b) and (c) and (2) must be complied with` | F-W1 |
| s 190(2A)(b) | 17156-17159 | fork (encoded, reading chosen) | `s 190(2A)(b) the share or stock is disregarded for the purposes of subsections (1)(a) and (2)` | F-W2 |
| s 190(3) | 17161-17168 | fork (encoded, reading chosen) | `s 190(3) the public company may keep the names and particulars of former members separately`; `s 190(3) the company need not supply the names and particulars of former members` | F-U1 |
| s 190(4) | 17170-17171 | encoded | `s 190(4) the register is prima facie evidence of the matter` |  |
| s 190(5) | 17173-17182 | fork (encoded, reading chosen) | `s 190(5) the public company must keep an index of the names of its members`; `s 190(5) the last day for making the necessary alteration in the index`; `s 190(5) the index was altered within 14 days after the alteration of the register` (+2 more) | F-S1 |
| s 190(6) | 17184-17186 | fork (encoded, reading chosen) | `s 190(6) the index has the indication the subsection requires` | F-B1 |
| s 190(7) | 17188-17197 | fork (encoded, reading chosen) | `s 190(7) the public company is guilty of an offence`; `s 190(7) the officer of the company is guilty of an offence`; `s 190(7) the most the officer of the company may be sentenced to on conviction` (+1 more) | F-O1 |
| s 191(1) chapeau | 17199-17202 | encoded | `s 191(1) the place where the register and index are kept is one the subsection allows` |  |
| s 191(1)(a) | 17204-17206 | fork (encoded, reading chosen) | `s 191(1)(a) the register and index may be kept at that other office`; `s 191(1) the place where the register and index are kept is one the subsection allows` | F-G1 |
| s 191(1)(b) | 17208-17213 | fork (encoded, reading chosen) | `s 191(1)(b) the register and index may be kept at the office of that other person`; `s 191(1) the place where the register and index are kept is one the subsection allows` | F-G1 |
| s 191(2) | 17215-17222 | fork (encoded, reading chosen) | `s 191(2) the public company must lodge notice with the Registrar`; `s 191(2) the last day for lodging the notice`; `s 191(2) the notice was lodged within 14 days` (+1 more) | F-E1 |
| s 191(3) | 17224-17229 | fork (encoded, reading chosen) | `s 191(3) the public company is guilty of an offence`; `s 191(3) the officer of the company is guilty of an offence`; `s 191(3) the most the public company or an officer in default may be sentenced to on conviction` | F-O1 |
| s 192(1) | 17231-17237 | fork (encoded, reading chosen) | `s 192(1) the public company may close the register of members or a class of members for the periods` | F-G2 |
| s 192(2) | 17239-17243 | fork (encoded, reading chosen) | `s 192(2) the register and index must be open to the person's inspection`; `s 192(2) the charge the company requires for an inspection is one the subsection allows`; `s 192(2) a public company must open the register and index to inspection` | F-C1 |
| s 192(3) | 17248-17259 | fork (encoded, reading chosen) | `s 192(3) the person may request a copy of the part of the register`; `s 192(3) the sum required in advance for a page is one the subsection allows`; `s 192(3) the amount payable in advance for the copy, in dollars` (+4 more) | F-C1, F-R1 |
| s 192(4) | 17261-17267 | fork (encoded, reading chosen) | `s 192(4) the public company is guilty of an offence`; `s 192(4) the officer of the company is guilty of an offence`; `s 192(4) the most the public company or an officer in default may be sentenced to on conviction` | F-O1 |
| s 193 | 17269-17281 | fork (encoded, reading chosen) | `s 193 the other person is liable to the same penalties as an officer of the company in default`; `s 193 the power of the Court under section 399 extends to orders against that other person and that person'...`; `s 193 the most the other person may be sentenced to on conviction` | F-G6, F-W1 |
| s 194(1) chapeau and closing words | 17283-17286, 17297-17303 | fork (encoded, reading chosen) | `s 194(1)(a) the name of a person is without sufficient cause entered in or omitted from the register`; `s 194(1)(b) default is made or unnecessary delay takes place in entering the fact of a person having ceased...`; `s 194(1) the person may apply to the Court for rectification of the register` (+1 more) | F-G1 |
| s 194(1)(a) | 17287-17288 | fork (encoded, reading chosen) | `s 194(1)(a) the name of a person is without sufficient cause entered in or omitted from the register`; `s 194(1)(b) default is made or unnecessary delay takes place in entering the fact of a person having ceased...`; `s 194(1) the person may apply to the Court for rectification of the register` | F-G1 |
| s 194(1)(b) | 17290-17292 | fork (encoded, reading chosen) | `s 194(1)(b) default is made or unnecessary delay takes place in entering the fact of a person having ceased...`; `s 194(1) the person may apply to the Court for rectification of the register` | F-G1 |
| s 194(2) chapeau | 17305-17306 | fork (encoded, reading chosen) | `s 194(2) the Court may decide the question on the application` | F-G6 |
| s 194(2)(a) | 17308-17313 | fork (encoded, reading chosen) | `s 194(2) the Court may decide the question on the application` | F-G6 |
| s 194(2)(b) | 17315-17318 | fork (encoded, reading chosen) | `s 194(2) the Court may decide the question on the application` | F-G6 |
| s 194(3) | 17320-17321 | fork (encoded, reading chosen) | `s 194(3) the Court's order must direct a notice of the rectification to be lodged` | F-W1 |
| s 194(4) | 17323-17325 | fork (encoded, reading chosen) | `s 194(4) the Court is barred from entertaining the application` | F-B2 |
| s 195(1) | 17327-17338 | encoded | `s 195(1) the trustee, executor or administrator may become registered as the holder of the share`; `s 195(1) the person is subject in respect of the share to the same liabilities and no more than the decease...` |  |
| s 195(2) | 17340-17353 | fork (encoded, reading chosen) | `s 195(2) the trustee, executor or administrator may become registered as the holder of the share`; `s 195(2) the person is subject in respect of the share to the same liabilities and no more than the decease...` | F-G3 |
| s 195(3) | 17355-17360 | fork (encoded, reading chosen) | `s 195(3) the shares must be marked in the register as held in respect of the trust` | F-B1, F-W1 |
| s 195(4) | 17362-17369 | fork (encoded, reading chosen) | `s 195(4) the entry or receipt of the notice is barred`; `s 195(4) no liabilities are affected by what was done`; `s 195(4) the company is not affected by notice of any trust by anything so done` | F-U1 |
| s 196(1) | 17371-17377 | encoded | `s 196(1) the public company may cause a branch register of members to be kept in the place`; `s 196(1) the branch register is deemed to be part of the company's register of members`; `s 196(1) the register is a branch register of members of the company kept pursuant to section 196` |  |
| s 196(2) | 17379-17385 | fork (encoded, reading chosen) | `s 196(2) the public company must lodge notice with the Registrar`; `s 196(2) the last day for lodging the notice`; `s 196(2) the notice was lodged within 14 days` (+1 more) | F-E1 |
| s 196(3) | 17387-17388 | fork (encoded, reading chosen) | `s 196(3) the branch register is kept as the subsection requires` | F-B1 |
| s 196(4) | 17390-17401 | encoded | `s 196(4) the public company has transmitted a copy of the entry as the subsection requires`; `s 196(4) the public company has caused a duplicate of the branch register to be kept as the subsection requ...`; `s 196(4) the duplicate is deemed to be part of the principal register` (+2 more) |  |
| s 196(5) | 17403-17407 | fork (encoded, reading chosen) | `s 196(5) the shares in the branch register are distinguished from the shares in the principal register`; `s 196(5) the transaction is barred from being registered in any other register` | F-B1, F-P3 |
| s 196(6) | 17409-17414 | fork (encoded, reading chosen) | `s 196(6) the public company may discontinue the branch register`; `s 196(6) the entries in the discontinued branch register must be transferred`; `s 196(6) the place the entries are transferred to is one the subsection allows` | F-W1 |
| s 196(7) | 17416-17419 | encoded | `s 196(7) this section applies to the public company` |  |
| s 196(8) | 17421-17429 | encoded | `s 196(8) the provisions of this Act relating to inspection, place of keeping and rectification apply to the...` |  |
| s 196(9) | 17431-17438 | fork (encoded, reading chosen) | `s 196(9) the public company is guilty of an offence`; `s 196(9) the officer of the company is guilty of an offence`; `s 196(9) the person who arranged to make up the principal register is guilty of an offence` (+1 more) | F-O1 |
| Part 5 Div 4A heading | 17443 | inert, reason 1 (not operative) | heading: Division 4A -- Electronic register of members kept by Registrar |  |
| s 196A(1) | 17445-17452 | fork (encoded, reading chosen) | `s 196A(1) the Registrar must keep an electronic register of members of the company`; `s 196A(1) the Registrar must keep an electronic register of members of every private company` | F-P5 |
| s 196A(2) chapeau and (a) | 17454-17458 | encoded | `s 196A(2) the electronic register contains what the subsection requires` |  |
| s 196A(2)(a)(i) | 17460 | encoded | `s 196A(2)(a)(i) the register contains the names of the members`; `s 196A(2) the electronic register contains what the subsection requires` |  |
| s 196A(2)(a)(ii) | 17462-17466 | encoded | `s 196A(2)(a)(ii) the register contains the addresses the paragraph requires of the member`; `s 196A(2) the electronic register contains what the subsection requires` |  |
| s 196A(2)(a)(iii) chapeau | 17468 | encoded | `s 196A(2)(a)(iii)(A) the register contains the statement of the shares and of the amount paid, for a compan...`; `s 196A(2)(a)(iii)(B) the register contains the date and size of every allotment, for a company having a sha...`; `s 196A(2) the electronic register contains what the subsection requires` |  |
| s 196A(2)(a)(iii)(A) | 17469-17472 | encoded | `s 196A(2)(a)(iii)(A) the register contains the statement of the shares and of the amount paid, for a compan...`; `s 196A(2)(a)(iii)(B) the register contains the date and size of every allotment, for a company having a sha...`; `s 196A(2) the electronic register contains what the subsection requires` |  |
| s 196A(2)(a)(iii)(B) | 17474-17477 | encoded | `s 196A(2)(a)(iii)(B) the register contains the date and size of every allotment, for a company having a sha...`; `s 196A(2) the electronic register contains what the subsection requires` |  |
| s 196A(2)(a)(iv) | 17479-17480 | encoded | `s 196A(2)(a)(iv) the register contains the date on which the name of each person was entered as a member`; `s 196A(2) the electronic register contains what the subsection requires` |  |
| s 196A(2)(a)(v) | 17482-17484 | fork (encoded, reading chosen) | `s 196A(2)(a)(v) the person ceased to be a member during the previous 7 years`; `s 196A(2)(a)(v) the register must contain the date on which the person ceased to be a member`; `s 196A(2) the electronic register contains what the subsection requires` | F-P5, F-P6 |
| s 196A(2)(b) | 17486-17490 | encoded | `s 196A(2)(b) the register shows the changes to the information that occur on or after 3 January 2016`; `s 196A(2) the electronic register contains what the subsection requires` |  |
| s 196A(3) | 17495-17501 | fork (encoded, reading chosen) | `s 196A(3) the electronic register must show stock instead of shares` | F-W1 |
| s 196A(4) | 17503-17510 | fork (encoded, reading chosen) | `s 196A(4) particulars of the change must be given to the Registrar` | F-B1, F-W1 |
| s 196A(5) | 17512-17518 | encoded | `s 196A(5) the Registrar must update the electronic register of members in accordance with the change`; `s 196A(5) the Registrar must update the electronic register of members` |  |
| s 196A(6) | 17520-17525 | encoded | `s 196A(6) the entry is prima facie evidence of the truth of the matter` |  |
| s 196B(1) chapeau | 17527-17533 | encoded | `s 196B(1) the private company must lodge the information with the Registrar`; `s 196B(1) the last day for lodging the information`; `s 196B(1) the information was lodged by the last day` (+1 more) |  |
| s 196B(1)(a) | 17535 | encoded | `s 196B(1)(a) the date 6 months after 3 January 2016`; `s 196B(1) the last day for lodging the information`; `s 196B(1) the information was lodged by the last day` (+1 more) |  |
| s 196B(1)(b) | 17537-17541 | encoded | `s 196B(1) the last day for lodging the information`; `s 196B(1) the information was lodged by the last day`; `s 196B(1) a private company must lodge the information by the earlier of the two dates` |  |
| s 196B(2) | 17546-17554 | fork (encoded, reading chosen) | `s 196B(2) the Registrar may enter the corresponding information from the old register of members` | F-G1 |
| s 196B(3) | 17556-17560 | fork (encoded, reading chosen) | `s 196B(3) the Registrar may extend the time for furnishing the information` | F-G1 |
| s 196C(1) | 17562-17570 | encoded | `s 196C(1) section 194 applies in respect of the electronic register of members` |  |
| s 196C(2) chapeau | 17572-17574 | encoded | `s 196C(2) section 195 applies in respect of the electronic register of members, with the modifications` |  |
| s 196C(2)(a) | 17576-17578 | encoded | `s 196C(2)(a) the reference is read as a reference to the electronic register of the private company` |  |
| s 196C(2)(b) | 17580 | encoded | `s 196C(2)(b) the reference is omitted` |  |
| s 196C(2)(c) | 17582-17588 | fork (encoded, reading chosen) | `s 196C(2)(c) the company must notify the Registrar of the trustee's request`; `s 196C(2)(c) the last day for notifying the Registrar`; `s 196C(2)(c) the Registrar was notified within 14 days after the request` (+1 more) | F-E1 |
| s 196D(1) chapeau | 17593-17597 | encoded | `s 196D(1) the private company must keep its old registers`; `s 196D(1)(a) a private company must not stop keeping the branch register within 7 years after 3 January 2016`; `s 196D(1)(b) a private company must not stop keeping its register of members within 7 years after the last ...` |  |
| s 196D(1)(a) | 17599-17601 | fork (encoded, reading chosen) | `s 196D(1)(a) the last day of the period for keeping the branch register`; `s 196D(1)(a) the private company must continue to keep the branch register`; `s 196D(1)(a) a private company must not stop keeping the branch register within 7 years after 3 January 2016` (+1 more) | F-P5, F-P2 |
| s 196D(1)(b) | 17603-17608 | fork (encoded, reading chosen) | `s 196D(1)(b) the last day of the period for keeping the register of members`; `s 196D(1)(b) the private company must continue to keep its register of members`; `s 196D(1)(b) a private company must not stop keeping its register of members within 7 years after the last ...` | F-P5, F-P2 |
| s 196D(2) | 17610-17616 | encoded | `s 196D(2) the private company is not required to update the old register for the change` |  |
| s 196D(3) chapeau | 17618-17620 | fork (encoded, reading chosen) | `s 196D(3)(a) the old sections continue to apply to the old registers`; `s 196D(3)(b) the non-compliance may be dealt with and punished as if the old sections were in force` | F-P5 |
| s 196D(3)(a) | 17622-17626 | fork (encoded, reading chosen) | `s 196D(3)(a) the old sections continue to apply to the old registers`; `s 196D(3)(b) the non-compliance may be dealt with and punished as if the old sections were in force` | F-P5 |
| s 196D(3)(b) | 17628-17633 | fork (encoded, reading chosen) | `s 196D(3)(b) the non-compliance may be dealt with and punished as if the old sections were in force` | F-P5 |
| s 196E chapeau | 17638-17643 | fork (encoded, reading chosen) | `s 196E(a) the address in the electronic register is kept as the residential address of the member`; `s 196E(a) the address in the electronic register is also kept as the contact address of the member` | F-P5 |
| s 196E(a) | 17645-17650 | fork (encoded, reading chosen) | `s 196E(a) the address in the electronic register is kept as the residential address of the member`; `s 196E(a) the address in the electronic register is also kept as the contact address of the member` | F-P5 |
| s 196E(b) | 17652-17657 | fork (encoded, reading chosen) | `s 196E(b) the contact address is made available for public access under section 12(2)(d) as the address of ...` | F-P5 |
| Part 5 Div 5 heading | 17659 | inert, reason 1 (not operative) | heading: Division 5 -- Annual return |  |
| s 197(1) chapeau | 17661-17665 | fork (encoded, reading chosen) | `s 197(1) the number of months after the end of the financial year within which the company must lodge its r...`; `s 197(1) the last day for lodging the return`; `s 197(1) the return was lodged after the annual general meeting and within the time the subsection allows` (+2 more) | F-P5, F-P7 |
| s 197(1)(a) | 17667-17668 | fork (encoded, reading chosen) | `s 197(1)(a) the months after the end of the financial year within which a listed company must lodge its return`; `s 197(1) the number of months after the end of the financial year within which the company must lodge its r...`; `s 197(1) the last day for lodging the return` (+3 more) | F-P5, F-P7 |
| s 197(1)(b) | 17670-17673 | fork (encoded, reading chosen) | `s 197(1)(b) the months after the end of the financial year within which any other company must lodge its re...`; `s 197(1) the number of months after the end of the financial year within which the company must lodge its r...`; `s 197(1) the last day for lodging the return` (+3 more) | F-P5, F-P7 |
| s 197(1A) chapeau | 17675-17677 | fork (encoded, reading chosen) | `s 197(1A) the company is one mentioned in subsection (1A)`; `s 197(1) the number of months after the end of the financial year within which the company must lodge its r...`; `s 197(1) the last day for lodging the return` (+3 more) | F-P5, F-P7 |
| s 197(1A)(a) | 17679-17680 | fork (encoded, reading chosen) | `s 197(1A)(a) the months after the end of the financial year within which a listed company must lodge its re...`; `s 197(1) the number of months after the end of the financial year within which the company must lodge its r...`; `s 197(1) the last day for lodging the return` (+2 more) | F-P5, F-P7 |
| s 197(1A)(b) | 17682-17685 | fork (encoded, reading chosen) | `s 197(1A)(b) the months after the end of the financial year within which any other company must lodge its r...`; `s 197(1) the number of months after the end of the financial year within which the company must lodge its r...`; `s 197(1) the last day for lodging the return` (+2 more) | F-P5, F-P7 |
| s 197(1B) chapeau | 17690-17692 | fork (encoded, reading chosen) | `s 197(1) the last day for lodging the return`; `s 197(1) the return was lodged after the annual general meeting and within the time the subsection allows`; `s 197(1) a company must lodge a return with the Registrar within the time the subsection gives` (+1 more) | F-G4, F-P5, F-P7 |
| s 197(1B)(a) | 17694 | fork (encoded, reading chosen) | `s 197(1) the last day for lodging the return`; `s 197(1) the return was lodged after the annual general meeting and within the time the subsection allows`; `s 197(1) a company must lodge a return with the Registrar within the time the subsection gives` (+1 more) | F-G4, F-P5, F-P7 |
| s 197(1B)(b) | 17696-17698 | fork (encoded, reading chosen) | `s 197(1) the last day for lodging the return`; `s 197(1) the return was lodged after the annual general meeting and within the time the subsection allows`; `s 197(1) a company must lodge a return with the Registrar within the time the subsection gives` (+1 more) | F-G4, F-P5, F-P7 |
| s 197(2) chapeau, (a), (b), (c) and closing words | 17700-17710 | encoded | `s 197(2) the return is in the form, has the contents and is accompanied by the documents that the subsectio...` |  |
| s 197(3) | 17712-17716 | inert, reason 2 (machinery) | machinery: a power for the regulations to vary the particulars and documents by class of company (the Act's own rule is s 197(2), encoded) |  |
| s 197(4) | 17718-17724 | fork (encoded, reading chosen) | `s 197(4) the private company must lodge a notice of the date on which the annual general meeting was held`; `s 197(4) the last day for lodging the notice`; `s 197(4) the notice was lodged within 14 days` (+1 more) | F-W1 |
| s 197(5) | 17726 | repealed or blank in this text | (5) [Deleted by Act 15 of 2017] |  |
| s 197(6) | 17728-17735 | fork (encoded, reading chosen) | `s 197(6) the company is guilty of an offence`; `s 197(6) the officer of the company is guilty of an offence`; `s 197(6) the most the company or an officer in default may be sentenced to on conviction` | F-O1 |
| s 198(1) chapeau | 17737-17740 | fork (encoded, reading chosen) | `s 198 the day 31 August 2018`; `s 198(1) the company is incorporated on or after 31 August 2018`; `s 198(1)(a) the period is the first financial year of the company` (+1 more) | F-D1, F-W1 |
| s 198(1)(a) | 17742-17749 | fork (encoded, reading chosen) | `s 198(1)(a) the last day of the company's first financial year`; `s 198(1)(a) the period is the first financial year of the company`; `s 198 the period is a financial year of the company as section 198 determines` | F-D1 |
| s 198(1)(b) | 17751-17756 | fork (encoded, reading chosen) | `s 198(1)(b) the last day of a subsequent financial year`; `s 198(1)(b) the period is a subsequent financial year of the company`; `s 198 the period is a financial year of the company as section 198 determines` | F-D1 |
| s 198(2) | 17758-17762 | fork (encoded, reading chosen) | `s 198(2) the period is longer than 18 months`; `s 198(2) the first financial year is no longer than the subsection allows`; `s 198 the period is a financial year of the company as section 198 determines` | F-B1 |
| s 198(3) chapeau | 17764 | fork (encoded, reading chosen) | `s 198(3) the company was incorporated before 31 August 2018`; `s 198 the period is a financial year of the company as section 198 determines` | F-W1 |
| s 198(3)(a) chapeau | 17766-17767 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(3)(a) the last day of the company's first financial year ending on or after 31 August 2018`; `s 198(3)(a) the period is the company's first financial year ending on or after 31 August 2018` (+1 more) | F-D1 |
| s 198(3)(a)(i) | 17769-17775 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(3)(a)(i) the last day of the first financial year ending on or after 31 August 2018, where a return o...`; `s 198(3)(a) the last day of the company's first financial year ending on or after 31 August 2018` (+2 more) | F-D1 |
| s 198(3)(a)(ii) | 17777-17781 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(3)(a)(ii) the last day of the first financial year ending on or after 31 August 2018, where none had ...`; `s 198(3)(a) the last day of the company's first financial year ending on or after 31 August 2018` (+2 more) | F-D1 |
| s 198(3)(b) | 17783-17788 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(3)(b) the period is a subsequent financial year of the company`; `s 198 the period is a financial year of the company as section 198 determines` | F-D1 |
| s 198(4) | 17790-17795 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(4) the company may by notice specify a new date as the last day of its financial year` | F-G1 |
| s 198(5) chapeau | 17800-17801 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(5) the notice is lodged less than 5 years after the end of an earlier financial year`; `s 198(5) the Registrar's approval must be obtained for the notice` | F-W1 |
| s 198(5)(a) | 17803 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(5) the notice is lodged less than 5 years after the end of an earlier financial year`; `s 198(5) the Registrar's approval must be obtained for the notice` | F-W1 |
| s 198(5)(b) | 17805-17810 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(5) the notice is lodged less than 5 years after the end of an earlier financial year`; `s 198(5) the Registrar's approval must be obtained for the notice` | F-W1 |
| s 198(6) chapeau | 17812-17813 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(6) the notice cannot specify the new date as the last day of the financial year` | F-B2 |
| s 198(6)(a) | 17815-17817 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(6) the notice cannot specify the new date as the last day of the financial year` | F-B2 |
| s 198(6)(b) | 17819-17821 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(6) the notice cannot specify the new date as the last day of the financial year` | F-B2 |
| s 198(6)(c) | 17823-17830 | fork (encoded, reading chosen) | `s 198(3)(a) the first anniversary on or after 31 August 2018`; `s 198(6) the notice cannot specify the new date as the last day of the financial year` | F-B2 |
| s 198(7) chapeau | 17832 | encoded | `s 198(3)(a) the first anniversary on or after 31 August 2018` |  |
| s 198(7)(a) | 17834-17839 | encoded | `s 198(3)(a) the first anniversary on or after 31 August 2018` |  |
| s 198(7)(b) | 17841-17845 | encoded | `s 198(3)(a) the first anniversary on or after 31 August 2018` |  |
| Part 10 heading | 22627-22630 | inert, reason 1 (not operative) | heading: PART 10 DISSOLUTION |  |
| Part 10 Division 1 heading | 22632 | repealed or blank in this text | Division 1 -- [Repealed by Act 40 of 2018] |  |
| ss 247 to 252 | 22633 | repealed or blank in this text | 247. to 252. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 2 heading | 22635 | repealed or blank in this text | Division 2 -- [Repealed by Act 40 of 2018] |  |
| Part 10 Division 2 Subdivision (1) heading | 22636 | repealed or blank in this text | Subdivision (1) -- [Repealed by Act 40 of 2018] |  |
| ss 253 to 262 | 22637 | repealed or blank in this text | 253. to 262. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 2 Subdivision (2) heading | 22639 | repealed or blank in this text | Subdivision (2) -- [Repealed by Act 40 of 2018] |  |
| ss 263 to 276 | 22640 | repealed or blank in this text | 263. to 276. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 2 Subdivision (3) heading | 22642 | repealed or blank in this text | Subdivision (3) -- [Repealed by Act 40 of 2018] |  |
| s 277 | 22643 | repealed or blank in this text | 277. [Repealed by Act 40 of 2018] |  |
| s 278 | 22644 | repealed or blank in this text | 278. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 2 Subdivision (4) heading | 22649 | repealed or blank in this text | Subdivision (4) -- [Repealed by Act 40 of 2018] |  |
| ss 279 to 289 | 22651 | repealed or blank in this text | 279. to 289. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 3 heading | 22653 | repealed or blank in this text | Division 3 -- [Repealed by Act 40 of 2018] |  |
| Part 10 Division 3 Subdivision (1) heading | 22654 | repealed or blank in this text | Subdivision (1) -- [Repealed by Act 40 of 2018] |  |
| s 290 | 22655 | repealed or blank in this text | 290. [Repealed by Act 40 of 2018] |  |
| s 291 | 22656 | repealed or blank in this text | 291. [Repealed by Act 40 of 2018] |  |
| s 292 | 22657 | repealed or blank in this text | 292. [Repealed by Act 40 of 2018] |  |
| s 293 | 22658 | repealed or blank in this text | 293. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 3 Subdivision (2) heading | 22660 | repealed or blank in this text | Subdivision (2) -- [Repealed by Act 40 of 2018] |  |
| s 294 | 22661 | repealed or blank in this text | 294. [Repealed by Act 40 of 2018] |  |
| s 295 | 22662 | repealed or blank in this text | 295. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 3 Subdivision (3) heading | 22664 | repealed or blank in this text | Subdivision (3) -- [Repealed by Act 40 of 2018] |  |
| s 296 | 22665 | repealed or blank in this text | 296. [Repealed by Act 40 of 2018] |  |
| s 297 | 22666 | repealed or blank in this text | 297. [Repealed by Act 40 of 2018] |  |
| s 298 | 22667 | repealed or blank in this text | 298. [Repealed by Act 40 of 2018] |  |
| s 299 | 22668 | repealed or blank in this text | 299. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 3 Subdivision (4) heading | 22670 | repealed or blank in this text | Subdivision (4) -- [Repealed by Act 40 of 2018] |  |
| ss 300 to 312 | 22671 | repealed or blank in this text | 300. to 312. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 4 heading | 22673-22674 | inert, reason 1 (not operative) | heading: Division 4 -- Provisions applicable to every mode of winding up |  |
| Part 10 Division 4 Subdivision (1) heading | 22676 | repealed or blank in this text | Subdivision (1) -- [Repealed by Act 40 of 2018] |  |
| ss 313 to 326 | 22678 | repealed or blank in this text | 313. to 326. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 4 Subdivision (2) heading | 22680 | repealed or blank in this text | Subdivision (2) -- [Repealed by Act 40 of 2018] |  |
| s 327 | 22681 | repealed or blank in this text | 327. [Repealed by Act 40 of 2018] |  |
| s 328 | 22686 | repealed or blank in this text | 328. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 4 Subdivision (3) heading | 22688 | repealed or blank in this text | Subdivision (3) -- [Repealed by Act 40 of 2018] |  |
| ss 329 to 335 | 22689 | repealed or blank in this text | 329. to 335. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 4 Subdivision (4) heading | 22691 | repealed or blank in this text | Subdivision (4) -- [Repealed by Act 40 of 2018] |  |
| ss 336 to 342 | 22692 | repealed or blank in this text | 336. to 342. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 4 Subdivision (5) heading | 22694 | inert, reason 1 (not operative) | heading: Subdivision (5) -- Dissolution |  |
| s 343 | 22696 | repealed or blank in this text | 343. [Repealed by Act 40 of 2018] |  |
| s 344(1) | 22698-22708 | fork (encoded, reading chosen) | `s 344(1) the Registrar may send the company and its directors, secretaries and members a letter`; `s 344(1) the last day for an answer showing cause to the contrary`; `s 344(1) the answer was received within 30 days after the date of the letter` | F-G5 |
| s 344(1A) | 22710-22715 | encoded | `s 344(1A) the Registrar may have regard to the circumstance in determining whether the company is not carry...` |  |
| s 344(2) | 22717-22726 | fork (encoded, reading chosen) | `s 344(2) the Registrar may publish the notice that the name of the company will be struck off`; `s 344(2) the last day of the 60 days after the date of the notice` | F-U1 |
| s 344(3) chapeau | 22728-22729 | fork (encoded, reading chosen) | `s 344(3) the Registrar may publish in the Gazette and send the notice to the same effect as the notice unde...` | F-G1 |
| s 344(3)(a) | 22734 | fork (encoded, reading chosen) | `s 344(3) the Registrar may publish in the Gazette and send the notice to the same effect as the notice unde...` | F-G1 |
| s 344(3)(b) | 22736-22738 | fork (encoded, reading chosen) | `s 344(3) the Registrar may publish in the Gazette and send the notice to the same effect as the notice unde...` | F-G1 |
| s 344(3)(c) | 22740-22744 | fork (encoded, reading chosen) | `s 344(3) the Registrar may publish in the Gazette and send the notice to the same effect as the notice unde...` | F-G1 |
| s 344(3) closing words | 22746-22750 | fork (encoded, reading chosen) | `s 344(3) the Registrar may publish in the Gazette and send the notice to the same effect as the notice unde...` | F-G1 |
| s 344(4) chapeau | 22752-22756 | fork (encoded, reading chosen) | `s 344(4) the Registrar may strike the name of the company off the register`; `s 344(4) the Registrar must publish notice of the striking off in the Gazette`; `s 344(4) the Registrar must publish notice of the striking off in the Gazette (rule)` (+3 more) | F-E1, F-P5, F-U1 |
| s 344(4)(a) | 22758-22760 | encoded | `s 344(4)(a) the liability of the officer or member continues and may be enforced as if the company had not ...`; `s 344(4)(b) the Court may wind up the company the name of which has been struck off the register` |  |
| s 344(4)(b) | 22762-22764 | encoded | `s 344(4)(b) the Court may wind up the company the name of which has been struck off the register` |  |
| s 344(5) | 22766-22784 | fork (encoded, reading chosen) | `s 344(5) the Court may order the name of the company to be restored to the register`; `s 344(5) the company is deemed to have continued in existence as if its name had not been struck off` | F-G5, F-P5 |
| s 344(6) | 22786-22796 | fork (encoded, reading chosen) | `s 344(6) the notice may be addressed to the liquidator at the liquidator's last known place of business`; `s 344(6) the letter or notice may be addressed to the company at its registered office`; `s 344(6) the letter or notice may be addressed to the company in the care of some officer of the company` (+1 more) | F-G1 |
| s 344(7) chapeau | 22798 | encoded | `s 344(7)(a) the Registrar must ensure that the particulars are sent to the Inland Revenue Authority of Sing...`; `s 344(7)(a) the Registrar must send the particulars to the Inland Revenue Authority of Singapore and the Ce...`; `s 344(7)(b) the Registrar must ensure that the substance of the notice is also published on the Authority's...` (+1 more) |  |
| s 344(7)(a) | 22800-22810 | encoded | `s 344(7)(a) the Registrar must ensure that the particulars are sent to the Inland Revenue Authority of Sing...`; `s 344(7)(a) the Registrar must send the particulars to the Inland Revenue Authority of Singapore and the Ce...`; `s 344(7)(b) the Registrar must ensure that the substance of the notice is also published on the Authority's...` (+1 more) |  |
| s 344(7)(b) | 22812-22816 | encoded | `s 344(7)(b) the Registrar must ensure that the substance of the notice is also published on the Authority's...`; `s 344(7)(b) the Registrar must publish the substance of the notices on the Authority's website (rule)` |  |
| s 344A(1) | 22818-22824 | fork (encoded, reading chosen) | `s 344A(1) the Registrar may strike the company's name off the register on the application of the company` | F-G5 |
| s 344A(2) | 22826-22829 | encoded | `s 344A(2) the application is made on the company's behalf as the subsection requires` |  |
| s 344A(3) | 22834-22844 | fork (encoded, reading chosen) | `s 344A(3) the Registrar must send the company and its directors, secretaries and members a letter informing...`; `s 344A(3) the Registrar must send the letter informing the company, its directors, secretaries and members ...`; `s 344A(3) the last day for an answer showing cause to the contrary` | F-W1 |
| s 344A(4) chapeau | 22846-22848 | encoded | `s 344A(4) the Registrar is barred from striking the company's name off the register under this section`; `s 344A(4) the last day of the 60 days after the publication of the notice` |  |
| s 344A(4)(a) | 22850-22851 | encoded | `s 344A(4) the Registrar is barred from striking the company's name off the register under this section`; `s 344A(4) the last day of the 60 days after the publication of the notice` |  |
| s 344A(4)(b) | 22853-22856 | encoded | `s 344A(4) the Registrar is barred from striking the company's name off the register under this section`; `s 344A(4) the last day of the 60 days after the publication of the notice` |  |
| s 344A(5) | 22858-22864 | fork (encoded, reading chosen) | `s 344A(5) the Registrar must strike off the name of the company from the register and publish a notice in t...`; `s 344A(5) the Registrar must strike off the name of the company from the register and publish a notice in t...` | F-W1 |
| s 344A(6) | 22866-22869 | encoded | `s 344A(6) the company is dissolved` |  |
| s 344A(7) chapeau | 22871 | encoded | `s 344A(7)(a) the liability of the officer or member continues and may be enforced as if the company had not...`; `s 344A(7)(b) the Court may wind up the company the name of which has been struck off the register` |  |
| s 344A(7)(a) | 22873-22875 | encoded | `s 344A(7)(a) the liability of the officer or member continues and may be enforced as if the company had not...`; `s 344A(7)(b) the Court may wind up the company the name of which has been struck off the register` |  |
| s 344A(7)(b) | 22877-22881 | encoded | `s 344A(7)(b) the Court may wind up the company the name of which has been struck off the register` |  |
| s 344A(8) chapeau | 22886 | encoded | `s 344A(8)(a) the Registrar must ensure that the particulars of the company and of the application are sent ...`; `s 344A(8)(a) the Registrar must send the particulars of the company and of the application to the Inland Re...`; `s 344A(8)(b) the Registrar must ensure that the substance of the notice is also published on the Authority'...` (+1 more) |  |
| s 344A(8)(a) | 22888-22897 | encoded | `s 344A(8)(a) the Registrar must ensure that the particulars of the company and of the application are sent ...`; `s 344A(8)(a) the Registrar must send the particulars of the company and of the application to the Inland Re...`; `s 344A(8)(b) the Registrar must ensure that the substance of the notice is also published on the Authority'...` (+1 more) |  |
| s 344A(8)(b) | 22899-22903 | encoded | `s 344A(8)(b) the Registrar must ensure that the substance of the notice is also published on the Authority'...`; `s 344A(8)(b) the Registrar must publish the substance of the notices on the Authority's website (rule)` |  |
| s 344A(9) | 22905-22908 | encoded | `s 344A(9) the Registrar may send the notice to the company in that manner` |  |
| s 344B(1) | 22910-22917 | fork (encoded, reading chosen) | `s 344B(1) the applicant may withdraw the application to strike the company's name off the register` | F-G1, F-P5 |
| s 344B(2) chapeau | 22919-22920 | fork (encoded, reading chosen) | `s 344B(2)(a) the Registrar must send the company by ordinary post a notice that the application has been wi...`; `s 344B(2)(b) the Registrar must publish a notice on the Authority's website that the application has been w...`; `s 344B(2)(a) the Registrar must send the company a notice that the application has been withdrawn (rule)` (+1 more) | F-W1 |
| s 344B(2)(a) | 22922-22924 | fork (encoded, reading chosen) | `s 344B(2)(a) the Registrar must send the company by ordinary post a notice that the application has been wi...`; `s 344B(2)(b) the Registrar must publish a notice on the Authority's website that the application has been w...`; `s 344B(2)(a) the Registrar must send the company a notice that the application has been withdrawn (rule)` (+1 more) | F-W1 |
| s 344B(2)(b) | 22925-22930 | fork (encoded, reading chosen) | `s 344B(2)(b) the Registrar must publish a notice on the Authority's website that the application has been w...`; `s 344B(2)(b) the Registrar must publish a notice on the Authority's website that the application has been w...` | F-W1 |
| s 344C(1) | 22932-22948 | fork (encoded, reading chosen) | `s 344C(1) any person may deliver an objection to the striking off of the name of the company` | F-G1, F-G5, F-P5 |
| s 344C(2) | 22950-22954 | encoded | `s 344C(2) the objection is given as the subsection requires` |  |
| s 344C(3) chapeau | 22956-22958 | fork (encoded, reading chosen) | `s 344C(3)(a) the Registrar must give the applicant or applicants notice of the objection`; `s 344C(3)(b) the Registrar must take into account the considerations prescribed in deciding whether to allo...`; `s 344C(3)(a) the Registrar must give the applicant or applicants notice of the objection (rule)` (+1 more) | F-W1 |
| s 344C(3)(a) | 22960-22962 | fork (encoded, reading chosen) | `s 344C(3)(a) the Registrar must give the applicant or applicants notice of the objection`; `s 344C(3)(b) the Registrar must take into account the considerations prescribed in deciding whether to allo...`; `s 344C(3)(a) the Registrar must give the applicant or applicants notice of the objection (rule)` (+1 more) | F-W1 |
| s 344C(3)(b) | 22964-22967 | fork (encoded, reading chosen) | `s 344C(3)(b) the Registrar must take into account the considerations prescribed in deciding whether to allo...`; `s 344C(3)(b) the Registrar must take into account the prescribed considerations (rule)` | F-W1 |
| s 344D(1) | 22969-22978 | fork (encoded, reading chosen) | `s 344D(1) an application may be made to the Registrar to restore the name of the company to the register` | F-G1 |
| s 344D(2) | 22980-22983 | encoded | `s 344D(2) the application may be made whether or not the company has in consequence been dissolved` |  |
| s 344D(3) | 22985-22988 | encoded | `s 344D(3) the person may make the application` |  |
| s 344D(4) | 22993-22997 | fork (encoded, reading chosen) | `s 344D(4) the application is valid as to time` | F-P5 |
| s 344E(1) | 22999-23005 | fork (encoded, reading chosen) | `s 344E(1) the Registrar must give the applicant notice of the decision`; `s 344E(1) the Registrar must give the applicant notice of the decision (rule)` | F-E1 |
| s 344E(2) chapeau | 23007-23008 | fork (encoded, reading chosen) | `s 344E(2)(a) the restoration has taken effect`; `s 344E(2)(b)(i) the Registrar must enter in the register a note of the date on which the restoration takes ...`; `s 344E(2)(b)(ii) the Registrar must cause notice of the restoration to be published in the Gazette and on t...` (+2 more) | F-P5, F-W1 |
| s 344E(2)(a) | 23010-23011 | fork (encoded, reading chosen) | `s 344E(2)(a) the restoration has taken effect`; `s 344E(2)(b)(i) the Registrar must enter in the register a note of the date on which the restoration takes ...`; `s 344E(2)(b)(ii) the Registrar must cause notice of the restoration to be published in the Gazette and on t...` (+2 more) | F-P5, F-W1 |
| s 344E(2)(b) chapeau | 23013 | fork (encoded, reading chosen) | `s 344E(2)(b)(i) the Registrar must enter in the register a note of the date on which the restoration takes ...`; `s 344E(2)(b)(ii) the Registrar must cause notice of the restoration to be published in the Gazette and on t...`; `s 344E(2)(b)(i) the Registrar must enter in the register a note of the date of the restoration (rule)` (+1 more) | F-W1 |
| s 344E(2)(b)(i) | 23015-23016 | fork (encoded, reading chosen) | `s 344E(2)(b)(i) the Registrar must enter in the register a note of the date on which the restoration takes ...`; `s 344E(2)(b)(ii) the Registrar must cause notice of the restoration to be published in the Gazette and on t...`; `s 344E(2)(b)(i) the Registrar must enter in the register a note of the date of the restoration (rule)` (+1 more) | F-W1 |
| s 344E(2)(b)(ii) | 23018-23021 | fork (encoded, reading chosen) | `s 344E(2)(b)(ii) the Registrar must cause notice of the restoration to be published in the Gazette and on t...`; `s 344E(2)(b)(ii) the Registrar must cause notice of the restoration to be published (rule)` | F-W1 |
| s 344E(3) chapeau | 23023 | encoded | `s 344E(3) the notice states what the subsection requires` |  |
| s 344E(3)(a) | 23025-23027 | encoded | `s 344E(3) the notice states what the subsection requires` |  |
| s 344E(3)(b) | 23029 | encoded | `s 344E(3) the notice states what the subsection requires` |  |
| s 344E(3)(c) | 23031-23034 | encoded | `s 344E(3) the notice states what the subsection requires` |  |
| s 344E(4) | 23036-23041 | fork (encoded, reading chosen) | `s 344E(4) the person may appeal to the Court` | F-G1 |
| s 344E(5) chapeau | 23043 | fork (encoded, reading chosen) | `s 344E(5)(a) the Court may confirm the Registrar's decision`; `s 344E(5)(b) the Court may restore the name of the company to the register and give directions and make orders` | F-G5 |
| s 344E(5)(a) | 23045 | fork (encoded, reading chosen) | `s 344E(5)(a) the Court may confirm the Registrar's decision`; `s 344E(5)(b) the Court may restore the name of the company to the register and give directions and make orders` | F-G5 |
| s 344E(5)(b) | 23050-23054 | fork (encoded, reading chosen) | `s 344E(5)(b) the Court may restore the name of the company to the register and give directions and make orders` | F-G5 |
| s 344F(1) | 23056-23064 | fork (encoded, reading chosen) | `s 344F(1) the Registrar may on his or her own initiative restore the name of the company to the register` | F-G1 |
| s 344F(2) | 23066-23072 | encoded | `s 344F(2) the mistake is a mistake of the Registrar` |  |
| s 344F(3) | 23074-23079 | fork (encoded, reading chosen) | `s 344F(3) the restoration has taken effect` | F-P5 |
| s 344G(1) | 23081-23088 | encoded | `s 344G(1) the company is regarded as having continued in existence as if its name had not been struck off t...` |  |
| s 344G(2) chapeau | 23090-23092 | encoded | `s 344G(2) the company and its directors are not liable to a penalty under section 204 for the financial year` |  |
| s 344G(2)(a) | 23094 | encoded | `s 344G(2) the company and its directors are not liable to a penalty under section 204 for the financial year` |  |
| s 344G(2)(b) | 23096-23099 | encoded | `s 344G(2) the company and its directors are not liable to a penalty under section 204 for the financial year` |  |
| s 344G(3) | 23104-23110 | fork (encoded, reading chosen) | `s 344G(3) the Court may give directions and make orders for placing the company and all other persons in th...` | F-G5 |
| s 344G(4) | 23112-23116 | fork (encoded, reading chosen) | `s 344G(4) the application to the Court is made in time` | F-P5 |
| s 344H(1) | 23118-23127 | fork (encoded, reading chosen) | `s 344H(1) the person must ensure that all the books and papers of the company are retained`; `s 344H(1) an officer must not fail to retain the books and papers within 5 years after the dissolution` | F-P5, F-W1 |
| s 344H(2) | 23129-23133 | fork (encoded, reading chosen) | `s 344H(2) the officer of the company is guilty of an offence`; `s 344H(2) the most the officer may be sentenced to on conviction` | F-O1 |
| ss 345 to 349 | 23135 | repealed or blank in this text | 345. to 349. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 5 heading | 23137 | repealed or blank in this text | Division 5 -- [Repealed by Act 40 of 2018] |  |
| ss 350 to 354 | 23138 | repealed or blank in this text | 350. to 354. [Repealed by Act 40 of 2018] |  |
| Part 10 Division 6 heading | 23140 | repealed or blank in this text | Division 6 -- [Repealed by Act 40 of 2018] |  |
| s 354A | 23141 | repealed or blank in this text | 354A. [Repealed by Act 40 of 2018] |  |
| s 354B | 23142 | repealed or blank in this text | 354B. [Repealed by Act 40 of 2018] |  |
| s 354C | 23143 | repealed or blank in this text | 354C. [Repealed by Act 40 of 2018] |  |
| Seventh Schedule | 28877-28879 | repealed or blank in this text | SEVENTH SCHEDULE [Repealed by S 236/2002] |  |
| Eighth Schedule | 28881-28883 | repealed or blank in this text | EIGHTH SCHEDULE [Repealed by Act 36 of 2014] |  |
| Ninth Schedule | 28885-28887 | repealed or blank in this text | NINTH SCHEDULE [Repealed by Act 12 of 2002] |  |
| Tenth Schedule | 28889-28891 | repealed or blank in this text | TENTH SCHEDULE [Repealed by Act 40 of 2018] |  |
| Eleventh Schedule | 28893-28895 | repealed or blank in this text | ELEVENTH SCHEDULE [Repealed by Act 40 of 2018] |  |
| Fourteenth Schedule heading | 29311-29316 | inert, reason 1 (not operative) | heading: FOURTEENTH SCHEDULE, the sections it is made for, and its title |  |
| sch 14 para 1 chapeau | 29318-29319 | fork (encoded, reading chosen) | `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(a) | 29321-29322 | fork (encoded, reading chosen) | `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(b) | 29324 | fork (encoded, reading chosen) | `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(c) | 29326 | fork (encoded, reading chosen) | `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(d) | 29328-29329 | fork (encoded, reading chosen) | `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(e) | 29331-29332 | fork (encoded, reading chosen) | `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(f) chapeau | 29334-29335 | fork (encoded, reading chosen) | `sch 14 para 1(f) the company is within paragraph 1(f)`; `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(f)(i) | 29337 | fork (encoded, reading chosen) | `sch 14 para 1(f) the company is within paragraph 1(f)`; `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(f)(ii) | 29339-29340 | fork (encoded, reading chosen) | `sch 14 para 1(f) the company is within paragraph 1(f)`; `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 1(f) closing words | 29342-29345 | fork (encoded, reading chosen) | `sch 14 para 1(f) the company is within paragraph 1(f)`; `sch 14 para 1 Part 11A does not apply to the company` | F-U1 |
| sch 14 para 2 chapeau | 29352 | encoded | `sch 14 para 2 the person is a Singapore financial institution`; `sch 14 para 2(a) the financial institution is within paragraph (a)` |  |
| sch 14 para 2(a) chapeau | 29354-29357 | encoded | `sch 14 para 2 the person is a Singapore financial institution`; `sch 14 para 2(a) the financial institution is within paragraph (a)` |  |
| sch 14 para 2(a)(i) | 29358 | repealed or blank in this text | (i) [Deleted by Act 2 of 2019] |  |
| sch 14 para 2(a)(ii) | 29360-29368 | encoded | `sch 14 para 2 the person is a Singapore financial institution`; `sch 14 para 2(a) the financial institution is within paragraph (a)` |  |
| sch 14 para 2(b) | 29370-29372 | encoded | `sch 14 para 2 the person is a Singapore financial institution` |  |
| sch 14 para 2(c) | 29374-29381 | encoded | `sch 14 para 2 the person is a Singapore financial institution` |  |
| Fifteenth Schedule heading | 29383-29389 | inert, reason 1 (not operative) | heading: FIFTEENTH SCHEDULE, the sections it is made for, and its title |  |
| sch 15 para 1 chapeau | 29391-29392 | fork (encoded, reading chosen) | `sch 15 para 1 Part 11A does not apply to the foreign company` | F-U1 |
| sch 15 para 1(a) | 29394 | fork (encoded, reading chosen) | `sch 15 para 1 Part 11A does not apply to the foreign company` | F-U1 |
| sch 15 para 1(b) | 29396-29397 | fork (encoded, reading chosen) | `sch 15 para 1 Part 11A does not apply to the foreign company` | F-U1 |
| sch 15 para 1(c) chapeau | 29399-29400 | fork (encoded, reading chosen) | `sch 15 para 1(c) the foreign company is within paragraph 1(c)`; `sch 15 para 1 Part 11A does not apply to the foreign company` | F-U1 |
| sch 15 para 1(c)(i) | 29402 | fork (encoded, reading chosen) | `sch 15 para 1(c) the foreign company is within paragraph 1(c)`; `sch 15 para 1 Part 11A does not apply to the foreign company` | F-U1 |
| sch 15 para 1(c)(ii) | 29409-29410 | fork (encoded, reading chosen) | `sch 15 para 1(c) the foreign company is within paragraph 1(c)`; `sch 15 para 1 Part 11A does not apply to the foreign company` | F-U1 |
| sch 15 para 1(c) closing words | 29412-29415 | fork (encoded, reading chosen) | `sch 15 para 1(c) the foreign company is within paragraph 1(c)`; `sch 15 para 1 Part 11A does not apply to the foreign company` | F-U1 |
| sch 15 para 1(d) | 29417-29422 | fork (encoded, reading chosen) | `sch 15 para 1(d) the foreign company is within paragraph 1(d)`; `sch 15 para 1 Part 11A does not apply to the foreign company` | F-U1 |
| sch 15 para 2 | 29424-29429 | encoded | `sch 15 para 2 the foreign company is a Singapore financial institution` |  |
| Sixteenth Schedule heading | 29431-29436 | inert, reason 1 (not operative) | heading: SIXTEENTH SCHEDULE, the sections it is made for, and its title |  |
| sch 16 heading Definition of significant control | 29438 | inert, reason 1 (not operative) | heading: Definition of significant control |  |
| sch 16 para 1 chapeau | 29440-29441 | encoded | `sch 16 para 1 the person has significant control over the company or foreign company` |  |
| sch 16 para 1(a) | 29443-29446 | encoded | `sch 16 para 1(a) the person has significant control by the right to appoint or remove the directors`; `sch 16 para 1 the person has significant control over the company or foreign company` |  |
| sch 16 para 1(b) | 29448-29450 | encoded | `sch 16 para 1(b) the person has significant control by holding more than 25% of the rights to vote`; `sch 16 para 1 the person has significant control over the company or foreign company` |  |
| sch 16 para 1(c) | 29452-29453 | encoded | `sch 16 para 1 the person has significant control over the company or foreign company` |  |
| sch 16 heading Definition of significant interest | 29455 | inert, reason 1 (not operative) | heading: Definition of significant interest |  |
| sch 16 para 2(1) chapeau | 29457-29458 | encoded | `sch 16 para 2(1) the person has a significant interest in the company or foreign company having a share cap...` |  |
| sch 16 para 2(1)(a) | 29460-29463 | encoded | `sch 16 para 2(1) the person has a significant interest in the company or foreign company having a share cap...` |  |
| sch 16 para 2(1)(b) chapeau | 29468 | encoded | `sch 16 para 2(1) the person has a significant interest in the company or foreign company having a share cap...` |  |
| sch 16 para 2(1)(b)(i) | 29470-29472 | encoded | `sch 16 para 2(1) the person has a significant interest in the company or foreign company having a share cap...` |  |
| sch 16 para 2(1)(b)(ii) | 29474-29476 | encoded | `sch 16 para 2(1) the person has a significant interest in the company or foreign company having a share cap...` |  |
| sch 16 para 2(2) | 29478-29479 | encoded | `sch 16 para 2(2) the share is a voting share for sub-paragraph (1)(b)` |  |
| sch 16 para 3 | 29481-29485 | encoded | `sch 16 para 3 the person has a significant interest in the company or foreign company that does not have a ...` |  |
| sch 16 heading Supplementary provisions | 29487 | inert, reason 1 (not operative) | heading: Supplementary provisions |  |
| sch 16 para 4(1) | 29489-29491 | encoded | `sch 16 para 4(1) the subsection of section 7 applies in determining whether the person has an interest in a...` |  |
| sch 16 para 4(2) | 29493-29495 | encoded | `sch 16 para 4(2) each of the persons is considered as having an interest in the share, or as holding the right` |  |
| sch 16 para 4(3) | 29497-29500 | encoded | `sch 16 para 4(3) each of them is treated as having an interest in the combined shares of both of them`; `sch 16 para 4(3) the percentage of the shares in which the person is treated as having an interest` |  |
| sch 16 para 4(4) | 29502-29504 | encoded | `sch 16 para 4(4) each of them is treated as holding the combined rights of both of them`; `sch 16 para 4(4) the percentage of the rights the person is treated as holding` |  |
| sch 16 para 4(5) | 29506-29507 | encoded | `sch 16 para 4(5) the share or right is considered as held by the person for whom it is held as nominee`; `sch 16 para 4(5) the share or right is considered as held by the nominee` |  |
| sch 16 para 4(6) chapeau | 29509 | encoded | `sch 16 para 4(6)(a) the arrangement is a joint arrangement`; `sch 16 para 4(6)(b) the thing counts as an arrangement` |  |
| sch 16 para 4(6)(a) | 29511-29514 | encoded | `sch 16 para 4(6)(a) the arrangement is a joint arrangement`; `sch 16 para 4(6)(b) the thing counts as an arrangement` |  |
| sch 16 para 4(6)(b) chapeau | 29521 | encoded | `sch 16 para 4(6)(b) the thing counts as an arrangement` |  |
| sch 16 para 4(6)(b)(i) | 29523-29524 | encoded | `sch 16 para 4(6)(b) the thing counts as an arrangement` |  |
| sch 16 para 4(6)(b)(ii) | 29526 | encoded | `sch 16 para 4(6)(b) the thing counts as an arrangement` |  |
| sch 16 para 4(6)(b) closing words | 29528-29532 | encoded | `sch 16 para 4(6)(b) the thing counts as an arrangement` |  |
| Legislative History heading and note | 29534-29539 | inert, reason 1 (not operative) | heading and the note that the Legislative History "is not part of the Act" |  |
| Legislative History entry 1 | 29541-29558 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 2 | 29559-29562 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 3 | 29563-29573 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 4 | 29574-29587 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 5 | 29588-29598 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 6 | 29599-29605 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 7 | 29606-29616 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 8 | 29617-29620 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 9 | 29621-29625 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 10 | 29626-29630 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 11 | 29631-29651 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 12 | 29652-29656 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 13 | 29657-29660 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 14 | 29661-29672 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 15 | 29673-29677 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 16 | 29678-29682 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 17 | 29683-29703 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 18 | 29704-29708 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 19 | 29709-29713 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 20 | 29714-29718 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 21 | 29719-29723 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 22 | 29724-29728 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 23 | 29729-29732 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 24 | 29733-29737 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 25 | 29738-29742 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 26 | 29743-29763 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 27 | 29764-29768 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 28 | 29769-29773 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 29 | 29774-29778 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 30 | 29779-29796 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 31 | 29797-29820 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 32 | 29821-29825 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 33 | 29826-29837 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 34 | 29838-29842 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 35 | 29843-29861 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 36 | 29862-29875 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 37 | 29876-29880 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 38 | 29881-29885 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 39 | 29886-29896 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 40 | 29897-29907 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 41 | 29908-29919 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 42 | 29920-29934 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 43 | 29935-29939 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 44 | 29940-29950 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 45 | 29951-29955 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 46 | 29956-29960 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 47 | 29961-29972 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 48 | 29973-29994 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 49 | 29995-29999 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 50 | 30000-30004 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 51 | 30005-30009 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 52 | 30010-30014 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 53 | 30015-30027 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 54 | 30028-30033 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 55 | 30034-30038 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 56 | 30039-30046 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 57 | 30047-30052 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 58 | 30053-30063 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 59 | 30064-30074 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 60 | 30075-30079 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 61 | 30080-30093 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 62 | 30094-30108 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 63 | 30109-30120 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 64 | 30121-30125 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 65 | 30126-30130 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 66 | 30131-30141 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 67 | 30142-30146 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 68 | 30147-30161 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 69 | 30162-30173 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 70 | 30174-30186 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 71 | 30187-30197 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 72 | 30198-30202 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 73 | 30203-30207 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 74 | 30208-30215 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 75 | 30216-30226 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 76 | 30227-30238 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 77 | 30239-30249 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 78 | 30250-30253 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 79 | 30254-30268 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 80 | 30269-30279 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 81 | 30280-30291 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 82 | 30292-30296 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 83 | 30297-30301 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 84 | 30302-30313 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 85 | 30314-30328 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 86 | 30329-30340 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 87 | 30341-30352 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 88 | 30353-30364 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 89 | 30365-30379 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 90 | 30380-30391 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 91 | 30392-30403 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 92 | 30404-30408 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 93 | 30409-30422 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 94 | 30423-30438 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 95 | 30439-30449 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 96 | 30450-30460 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 97 | 30461-30465 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 98 | 30466-30470 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 99 | 30471-30481 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 100 | 30482-30496 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 101 | 30497-30501 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 102 | 30502-30506 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 103 | 30507-30519 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 104 | 30520-30529 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 105 | 30530-30540 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 106 | 30541-30553 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 107 | 30554-30563 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 108 | 30564-30573 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 109 | 30574-30584 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 110 | 30585-30594 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 111 | 30595-30607 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 112 | 30608-30617 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 113 | 30618-30627 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 114 | 30628-30637 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 115 | 30638-30641 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 116 | 30642-30651 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 117 | 30652-30670 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 118 | 30671-30680 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 119 | 30681-30685 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 120 | 30686-30696 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 121 | 30697-30707 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 122 | 30708-30717 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 123 | 30718-30731 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 124 | 30732-30741 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 125 | 30742-30752 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 126 | 30753-30763 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Legislative History entry 127 | 30764-30773 | inert, reason 1 (not operative) | a row of the table of amending laws (not operative) |  |
| Abbreviations | 30777-30792 | inert, reason 1 (not operative) | the list of abbreviations used in the Legislative History |  |
| Comparative Table heading and note | 30795-30799 | inert, reason 1 (not operative) | heading and the note that the table helps readers locate corresponding provisions of the last Revised Edition |  |
| Comparative Table body | 30800-30828 | inert, reason 1 (not operative) | table rows pairing 2020 Ed. provisions with 2006 Ed. provisions (not operative) |  |

## Fork register (sgm)

Every ambiguity, the readings I saw, the one I took, and the text that licenses each.
Source of each entry: `work/notes/forks.md`, written as the modules were written.
The last line under each id is computed from the code: it counts the declarations whose own comment block names the id.
The register line gives the provisions in full; the computed count can be lower than the list there when a site is covered by a shared comment above it.
F-P2 is the keel's period convention (P2) applied; the others are forks of this part.

**Grant-ruling register.**
The grant ruling of 2026-11-12 (limit 3) says a "may" function gated by where, when or upon is listed for the maintainer and is not changed: its answer is as periods ruling (b) and delegated-definitions ruling (c) give, which is JUST FALSE.
This part has 9 such sites, all `JUST FALSE`: s 197(1B) (the "upon an application" or "in respect of any prescribed class" gate; F-G4), s 193 (the "Where" gate; F-G6), s 194(2) ("On any application"; F-G6), s 344(1) ("Where the Registrar has reasonable cause"; F-G5), s 344A(1) ("on the application"; F-G5), s 344C(1) ("Where a notice is given"; F-G5), s 344E(5)(a) and (b) ("On an appeal"; F-G5), s 344G(3) ("On the application"; F-G5).
I did not decide any of them on my own beyond following those two rulings; if the maintainer rules the other way each is one `ELSE` branch (they carry `-- FALSE-kind (split site (ii) ...)` comments).
The "may" sites whose `if` gate failed (s 344(5) "if satisfied", s 344A(1) prescribed grounds, s 197(1B) "special reasons", s 195(2) consent) answer NOTHING under limit 1.


### F-P2
- Provisions: every "within N days after X" duty (ss 190(5), 191(2), 192(3), 196(2), 196C(2)(c), 197(4))
- Functions: the `... lodged/altered/sent within` functions and the regulative rules
- Answer taken: the day of the act is in time if it is on or before the last day (X plus N), an act on X itself included: `period: the date is not later than the end of a period after`
- Other reading: the keel's window function `period: the date is within a period after` (P2) treats an act on the day of the event as outside the window
- Text that licenses each: the text names a closing edge only ("within 14 days after the date on which any alteration is made"); the periods ruling (a) of 2026-11-05 ("outside the period the answer is JUST FALSE") applies to the closing edge
- Declarations whose comment block names F-P2: 2 (`s 196D(1)(a) the private company must continue to keep the branch register`; `s 196D(1)(b) the private company must continue to keep its register of members`)

### F-W1
- Provisions: ss 190(2), 190(2A)(a), 193, 194(3), 195(3), 196(6), 196A(3), 196A(4), 197(4), 198(1), 198(3), 198(5), 344A(3), 344A(5), 344B(2), 344C(3), 344E(2)(b), 344H(1)
- Functions: the duty functions gated by "where", "when", "at the request of", "thereupon"
- Answer taken: JUST FALSE when the gate is unmet
- Other reading: NOTHING (the text does not say the duty is absent)
- Text that licenses each: Guide section 5, periods ruling of 2026-11-05, item (b) "a 'where ...' condition: when it fails the answer is `JUST FALSE`", and the 2026-11-05 delegated-definitions ruling item (c) "'when', 'upon' and 'whenever' count as 'where'"; these are duties, not grants, so the grant ruling does not turn them to NOTHING
- Declarations whose comment block names F-W1: 21 (`s 190(2) the company must alter the register to show stock instead of shares`; `s 190(2A)(a) the requirements of subsections (1)(a), (b) and (c) and (2) must...`; `s 193 the other person is liable to the same penalties as an officer of the c...`; `s 194(3) the Court's order must direct a notice of the rectification to be lo...`; `s 195(3) the shares must be marked in the register as held in respect of the ...`; `s 196(6) the entries in the discontinued branch register must be transferred`, ...)

### F-W2
- Provisions: s 190(2A)(b)
- Functions: `... is disregarded for the purposes of subsections (1)(a) and (2)`
- Answer taken: NOTHING for a share or stock not cancelled
- Other reading: JUST FALSE
- Text that licenses each: "any share or stock which is so cancelled is to be disregarded": a relative clause naming the cancelled share only; periods ruling (c) "a scope limit with no 'only' ... NOTHING"
- Declarations whose comment block names F-W2: 1 (`s 190(2A)(b) the share or stock is disregarded for the purposes of subsection...`)

### F-U1
- Provisions: s 190(3) (need not supply), s 195(4) (marking under (3)), s 344(2), s 344(4)
- Functions: the functions with an "unless" or "Subject to" exception met
- Answer taken: JUST FALSE
- Other reading: NOTHING
- Text that licenses each: "need not be supplied ... unless the person specifically requests" and "Subject to this section, no notice of any trust ... may be entered": an exception stated by the text is a no to the main rule on the excepted facts (the maintainer, 2026-11-05: an "unless" or "except" once it is met is decided site by site)
- Declarations whose comment block names F-U1: 6 (`s 190(3) the company need not supply the names and particulars of former members`; `s 195(4) the entry or receipt of the notice is barred`; `s 344(2) the Registrar may publish the notice that the name of the company wi...`; `s 344(4) the Registrar may strike the name of the company off the register`; `sch 14 para 1 Part 11A does not apply to the company`; `sch 15 para 1 Part 11A does not apply to the foreign company`)

### F-S1
- Provisions: s 190(5)
- Functions: `the public company must keep an index of the names of its members`
- Answer taken: NOTHING for a company with 50 members or fewer
- Other reading: JUST FALSE
- Text that licenses each: "Every public company having more than 50 members must": a scope limit with no "only"; periods ruling (c) "outside the scope the answer is NOTHING"
- Declarations whose comment block names F-S1: 1 (`s 190(5) the public company must keep an index of the names of its members`)

### F-B1
- Provisions: ss 190(6), 195(3), 196(3), 196(5) first limb, 196A(4), 198(2)
- Functions: the duty functions
- Answer taken: decision function only, no regulative rule
- Other reading: a regulative rule for the company
- Text that licenses each: the text says "The index must ...", "Shares ... must be marked", "A branch register must be kept", "the shares ... must be distinguished" and names no bearer; the brief says not to invent an actor
- Declarations whose comment block names F-B1: 6 (`s 190(6) the index has the indication the subsection requires`; `s 195(3) the shares must be marked in the register as held in respect of the ...`; `s 196(3) the branch register is kept as the subsection requires`; `s 196(5) the shares in the branch register are distinguished from the shares ...`; `s 196A(4) particulars of the change must be given to the Registrar`; `s 198(2) the first financial year is no longer than the subsection allows`)

### F-O1
- Provisions: ss 190(7), 191(3), 192(4), 196(9), 197(6), 344H(2) offence functions
- Functions: the "is guilty of an offence" functions
- Answer taken: JUST FALSE when the "If default is made" is unmet, or an officer is not in default (split site (i))
- Other reading: NOTHING
- Text that licenses each: Guide section 5, rule of 2026-10-29 as summarised under "Rulings on negatives and legal effects": "a condition the text introduces with 'if' ... JUST FALSE"; the other reading is that the section is silent on the innocence of anyone it does not make guilty
- Declarations whose comment block names F-O1: 12 (`s 190(7) the public company is guilty of an offence`; `s 190(7) the officer of the company is guilty of an offence`; `s 191(3) the public company is guilty of an offence`; `s 191(3) the officer of the company is guilty of an offence`; `s 192(4) the public company is guilty of an offence`; `s 192(4) the officer of the company is guilty of an offence`, ...)

### F-G1
- Provisions: ss 191(1)(a), 191(1)(b), 194(1), 195(1), 196(1), 196B(2), 196B(3), 196D(3)(b) (limb outside the listed sections), 198(4), 344(3), 344(6), 344B(1), 344C(1) (ground limb), 344D(1), 344E(4), 344F(1) and every function named for a grant ("may ...") whose "if"/scope gate failed
- Functions: the grant functions
- Answer taken: NOTHING
- Other reading: JUST FALSE
- Text that licenses each: grant ruling of 2026-11-12, limit 1, quoted in Guide section 5: "answer `NOTHING` ... only for a function named for a grant or a power ('may', 'is permitted to', 'has power to') whose `if` gate failed"
- Declarations whose comment block names F-G1: 14 (`s 191(1)(a) the register and index may be kept at that other office`; `s 191(1)(b) the register and index may be kept at the office of that other pe...`; `s 194(1) the person may apply to the Court for rectification of the register`; `s 196B(2) the Registrar may enter the corresponding information from the old ...`; `s 196B(3) the Registrar may extend the time for furnishing the information`; `s 198(4) the company may by notice specify a new date as the last day of its ...`, ...)

### F-G2
- Provisions: s 192(1)
- Functions: `the public company may close the register ... for the periods`
- Answer taken: NOTHING for more than 30 days in the aggregate
- Other reading: JUST FALSE
- Text that licenses each: "may close ... for one or more periods not exceeding 30 days in the aggregate": a grant limited by its own wording, the case outside the limit; Guide "In short": "limits a grant or prohibition in its own wording ... NOTHING"
- Declarations whose comment block names F-G2: 1 (`s 192(1) the public company may close the register of members or a class of m...`)

### F-G3
- Provisions: s 195(2)
- Functions: `the trustee ... may become registered as the holder of the share`
- Answer taken: NOTHING without the consent of the company and of the registered holder (split site (ii))
- Other reading: JUST FALSE
- Text that licenses each: "may with the consent of the company and of the registered holder": the grant rule (Guide section 5, 2026-11-12 ruling, limit 1) and its limit 3 (a "may" gated by "where", "when", "upon" is listed for the maintainer, not changed); periods ruling (b) is for "where"
- Declarations whose comment block names F-G3: 1 (`s 195(2) the trustee, executor or administrator may become registered as the ...`)

### F-E1
- Provisions: ss 191(2), 196(2), 196C(2)(c), 344(4) (publish), 344E(1)
- Functions: `the public company must lodge notice with the Registrar`
- Answer taken: NOTHING when none of the triggering events occurred
- Other reading: JUST FALSE
- Text that licenses each: the duty arises "after the register and index ... are first kept at a place other than the registered office" and "after any change"; silent without the event; periods ruling (c) (a scope limit without "only")
- Declarations whose comment block names F-E1: 5 (`s 191(2) the public company must lodge notice with the Registrar`; `s 196(2) the public company must lodge notice with the Registrar`; `s 196C(2)(c) the company must notify the Registrar of the trustee's request`; `s 344(4) the Registrar must publish notice of the striking off in the Gazette`; `s 344E(1) the Registrar must give the applicant notice of the decision`)

### F-C1
- Provisions: ss 192(2), 192(3)
- Functions: the charge functions
- Answer taken: JUST FALSE for a charge above the stated cap ($1 for a non-member's inspection, $1 per page, nothing for a member)
- Other reading: NOTHING
- Text that licenses each: "without charge", "on payment ... of $1 or such less sum as the public company requires": the text states the price in its own words
- Declarations whose comment block names F-C1: 2 (`s 192(2) the charge the company requires for an inspection is one the subsect...`; `s 192(3) the sum required in advance for a page is one the subsection allows`)

### F-R1
- Provisions: s 192(3)
- Functions: `the last day for sending the copy`
- Answer taken: "such further period as the Registrar considers reasonable" is read as further days added to the 21 days, supplied by the person (0 if none)
- Other reading: the Registrar's period replaces the 21 days
- Text that licenses each: "within a period of 21 days or within such further period as the Registrar considers reasonable in the circumstances commencing on the day next after the day on which the request is received"
- Declarations whose comment block names F-R1: 1 (`s 192(3) the last day for sending the copy`)

### F-B2
- Provisions: ss 194(4), 198(6)
- Functions: `the Court is barred from entertaining the application`
- Answer taken: NOTHING where the entry is 30 years old or less
- Other reading: JUST FALSE
- Text that licenses each: a bar limited by its own wording ("more than 30 years before the date of the application"); Guide "In short": "limits a grant or prohibition in its own wording ... NOTHING"
- Declarations whose comment block names F-B2: 2 (`s 194(4) the Court is barred from entertaining the application`; `s 198(6) the notice cannot specify the new date as the last day of the financ...`)

### F-P3
- Provisions: s 196(5)
- Functions: `the transaction is barred from being registered in any other register`
- Answer taken: JUST FALSE once the registration in the branch register has ended; NOTHING for a transaction not about branch-register shares
- Other reading: NOTHING for both
- Text that licenses each: "during the continuance of that registration": a period the text fixes in its own words, periods ruling (a)
- Declarations whose comment block names F-P3: 1 (`s 196(5) the transaction is barred from being registered in any other register`)

### F-P4
- Provisions: s 194(4), s 198 (any year-step from 29 February)
- Functions: the 30-year step
- Answer taken: the 30th anniversary of 29 February is 28 February in a year with no 29 February (period convention P4)
- Other reading: 1 March
- Text that licenses each: the Act says nothing for s 194(4); s 198(7) says 28 February for its own two cases
- Declarations whose comment block names F-P4: 0

### F-P5
- Provisions: ss 196A(1), 196A(2)(a)(v), 196D(1)(a), 196D(1)(b), 196D(3)(a), 196D(3)(b), 196E(a), 196E(b), 197(1), 344(4), 344(5), 344B(1), 344C(1), 344D(4), 344E(2)(a), 344F(3), 344G(4), 344H(1)
- Functions: the duty functions each tied to a period or date the text names ("On and after 3 January 2016", "during the previous 7 years", "for a period of 7 years after", "Until the expiry of the period", "As from the date of commencement")
- Answer taken: JUST FALSE outside the period (before 3 January 2016, or more than 7 years back, or after the 7 years)
- Other reading: NOTHING
- Text that licenses each: periods ruling of 2026-11-05, item (a), quoted in Guide section 5: "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"
- Declarations whose comment block names F-P5: 18 (`s 196A(1) the Registrar must keep an electronic register of members of the co...`; `s 196A(2)(a)(v) the register must contain the date on which the person ceased...`; `s 196D(1)(a) the private company must continue to keep the branch register`; `s 196D(1)(b) the private company must continue to keep its register of members`; `s 196D(3)(b) the non-compliance may be dealt with and punished as if the old ...`; `s 196E(a) the address in the electronic register is kept as the residential a...`, ...)

### F-P6
- Provisions: s 196A(2)(a)(v)
- Functions: `the person ceased to be a member during the previous 7 years`
- Answer taken: the window of the keel's P6 (`period: the date is within a period before`): from the date 7 years before the date asked up to the day before it, so a person who ceases on the date asked is not yet "previous"
- Other reading: the window including the date asked
- Text that licenses each: "any person who ceased to be a member during the previous 7 years": the Act says nothing about the edge; the keel's P6 is the one convention for "within N units before X"
- Declarations whose comment block names F-P6: 1 (`s 196A(2)(a)(v) the person ceased to be a member during the previous 7 years`)

### F-P7
- Provisions: s 197(1)
- Functions: `the return was lodged after the annual general meeting and within the time the subsection allows`
- Answer taken: a return lodged on the day of the annual general meeting counts as "after its annual general meeting"
- Other reading: only a later day counts
- Text that licenses each: "must lodge a return with the Registrar after its annual general meeting": the Act does not say whether the day of the meeting is "after" it; the return is of the meeting's results, so a return lodged later the same day follows the meeting
- Declarations whose comment block names F-P7: 1 (`s 197(1) the return was lodged after the annual general meeting and within th...`)

### F-G4
- Provisions: s 197(1B)
- Functions: `the Registrar may extend the period within which the company must lodge its return`
- Answer taken: NOTHING when the Registrar thinks there are no special reasons (an "if" gate); JUST FALSE when there are special reasons but neither "upon an application by the company" nor "in respect of any prescribed class" holds (a "upon" gate) (split site (ii))
- Other reading: NOTHING for both gates; or JUST FALSE for both
- Text that licenses each: "The Registrar may, if the Registrar thinks there are special reasons to do so, extend ... (a) upon an application by the company; or (b) in respect of any prescribed class of companies": the grant rule (Guide section 5, 2026-11-12 ruling, limit 1: `NOTHING` for a function named for a grant whose "if" gate failed) for the "if"; periods ruling (b) with the delegated-definitions ruling (c) ("'when', 'upon' and 'whenever' count as 'where'") for the "upon", left as the guide's rulings give it under limit 3 of the grant rule
- Declarations whose comment block names F-G4: 1 (`s 197(1B) the Registrar may extend the period within which the company must l...`)

### F-D1
- Provisions: ss 198(1)(a), 198(1)(b), 198(3)(a), 198(3)(b)
- Functions: the "the period is ... financial year" functions
- Answer taken: JUST FALSE for a period that is not the one the text describes (it "starts on ... and ends on", "is the anniversary of")
- Other reading: NOTHING
- Text that licenses each: the text states which periods are the financial years (a closed statement, like "means"); the keel's "financial year" function hands the question to s 198 (delegated-definitions ruling of 2026-11-05, item (a): when no head holds, `JUST FALSE`)
- Declarations whose comment block names F-D1: 4 (`s 198(1)(a) the period is the first financial year of the company`; `s 198(1)(b) the period is a subsequent financial year of the company`; `s 198(3)(a) the period is the company's first financial year ending on or aft...`; `s 198(3)(b) the period is a subsequent financial year of the company`)

### F-G5
- Provisions: ss 344(1), 344(5), 344A(1), 344C(1), 344E(5)(a), 344E(5)(b), 344G(3)
- Functions: the "may" functions gated by "Where", "on the application", "On an appeal", "On the application" or "on an application made within 6 years"
- Answer taken: JUST FALSE when the "Where" or "upon" gate fails (ss 344(1), 344C(1), 344A(1) without an application, 344E(5), 344G(3)); JUST FALSE outside the 6 years of s 344(5); NOTHING within the 6 years when the "if satisfied" gate fails, and NOTHING at s 344A(1) when the prescribed grounds or conditions are unmet (split site (ii))
- Other reading: NOTHING for the "Where" and "upon" sites
- Text that licenses each: periods ruling of 2026-11-05, item (b), Guide section 5: "a "where ..." condition: when it fails the answer is `JUST FALSE`", with the delegated-definitions ruling item (c): "'when', 'upon' and 'whenever' count as 'where'"; the grant rule (2026-11-12 ruling) limit 3 lists a "may" gated by "where", "when" or "upon" for the maintainer and does not change it, and limit 1 gives `NOTHING` for an "if" gate; item (a) of the periods ruling ("a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`") for the 6 years
- Declarations whose comment block names F-G5: 7 (`s 344(1) the Registrar may send the company and its directors, secretaries an...`; `s 344(5) the Court may order the name of the company to be restored to the re...`; `s 344A(1) the Registrar may strike the company's name off the register on the...`; `s 344C(1) any person may deliver an objection to the striking off of the name...`; `s 344E(5)(a) the Court may confirm the Registrar's decision`; `s 344E(5)(b) the Court may restore the name of the company to the register an...`, ...)

### F-G6
- Provisions: ss 193 (Court power), 194(2)
- Functions: `s 193 the power of the Court under section 399 extends to orders against that other person ...`; `s 194(2) the Court may decide the question on the application`
- Answer taken: JUST FALSE when the "Where" gate (s 193) or the "On any application" gate (s 194(2)) fails (split site (ii))
- Other reading: NOTHING
- Text that licenses each: periods ruling of 2026-11-05, item (b), Guide section 5: "a "where ..." condition: when it fails the answer is `JUST FALSE`", with the delegated-definitions ruling item (c): "'when', 'upon' and 'whenever' count as 'where'"; the grant rule's limit 3 lists the site for the maintainer and does not change it
- Declarations whose comment block names F-G6: 2 (`s 193 the power of the Court under section 399 extends to orders against that...`; `s 194(2) the Court may decide the question on the application`)


## Jural relations (sgm)

A Hohfeld table of the provisions of my ranges.
The Act mostly states a duty without naming who holds the matching claim; where it does not, the claim-right column says so and the sanction (an offence) is shown instead.
A row for an official (the Registrar, the Court) is in layer 1 only; the seat asks what each means for the person.
Provisions not listed (the interpretive definitions, the evidential rules of ss 190(4) and 196A(6), the Schedules' definitions) create no jural relation of their own.

| provision | position | holder | counter-party | content |
| --- | --- | --- | --- | --- |
| s 190(1) | duty | public company | none named (sanction: s 190(7)) | keep a register of its members with the entries the subsection lists; no deadline |
| s 190(2), (2A) | duty | public company | none named | alter the register to show stock; keep the register after a buy-back as the subsections say |
| s 190(3) | privilege | public company | none named | keep the names and particulars of former members separately; need not supply them unless specifically requested |
| s 190(5) | duty | public company having more than 50 members | none named | keep an index; alter it within 14 days after altering the register |
| s 190(7), 191(3), 192(4), 196(9), 197(6), 344H(2) | liability | the company and each officer in default (s 196(9) also the person who arranged to make up the principal register) | none named | a fine, and a default penalty where the section says so; `Penalty` record |
| s 191(1) | privilege | public company | none | keep the register and index at another office in Singapore or at the office of the person who makes them up |
| s 191(2) | duty | public company | Registrar (receives the notice) | lodge notice of the place, or of a change, within 14 days |
| s 192(1) | privilege | public company | none | close the register for periods not exceeding 30 days in the aggregate in a calendar year |
| s 192(2) | duty / claim-right | public company / any member (free of charge) and any other person (on payment of $1 or less) | | open the register and index to inspection |
| s 192(3) | claim-right / duty | any person who applies and pays in advance (not more than $1 a page) / public company | | a copy of the register or of the part asked for; the company must send it within 21 days (and any further period the Registrar allows) |
| s 193 | liability; power | the person who keeps the register for the company; the Court | | the same penalties as an officer in default; the Court's power under s 399 reaches that person and its officers and employees |
| s 194(1) | power; liability | person aggrieved, any member or the public company; the company | the Court | apply for rectification of the register; the company may be ordered to pay damages |
| s 194(2) | power | the Court | the parties | decide questions of title and any question necessary for rectification |
| s 194(4) | disability | the Court | applicant | no application about an entry more than 30 years old may be entertained |
| s 195(1), (2) | power; immunity | trustee, executor or administrator | company | become registered as holder of the deceased's share (with the consents in (2)); subject only to the liabilities the deceased had |
| s 195(3) | duty (bearer not named) | none named | | mark the shares in the register as held in respect of the trust, at the trustee's request |
| s 195(4) | disability; immunity | the company and anyone entering a notice of trust | | no notice of a trust may be entered or received; the company is not affected by notice of a trust |
| s 196(1) | privilege | public company | none | cause a branch register of members to be kept in a place outside Singapore (a public company having a share capital) |
| s 196(2), (4) | duty | public company | Registrar (notice) | lodge notice of the branch register office within 14 days; transmit a copy of every entry; keep a duplicate |
| s 196(6) | privilege; duty | public company | | discontinue a branch register; transfer its entries |
| s 196A(1), (5) | duty | Registrar (no seat) | private company and its members | keep and update the electronic register of members |
| s 196A(4) | duty (bearer not named) | none named | Registrar | give particulars of a change that another section requires or authorises to be lodged |
| s 196B(1), (3) | duty; power | private company; Registrar | | lodge the information by the earlier of the two dates; the Registrar may extend the time |
| s 196C(2)(c) | duty | private company | Registrar | notify the trustee's request within 14 days |
| s 196D(1) | duty (negative: SHANT) | private company | none named | not stop keeping the branch register and the register of members for 7 years |
| s 196D(2) | privilege | private company | none | need not update the old register for a change |
| s 197(1), (1A) | duty | company | Registrar | lodge the annual return after its annual general meeting and within 5, 6, 7 or 8 months after its financial year |
| s 197(1B) | power; liability | Registrar; company | | extend the period on application or for a prescribed class |
| s 197(4) | duty | private company | Registrar | lodge notice of the date of the annual general meeting within 14 days |
| s 198(4) | power; liability | company; Registrar (approval under (5)) | | specify a new last day of the financial year by notice |
| s 198(6) | disability | company | | the notice cannot specify a date once the periods in (6) have expired |
| s 344(1) to (4) | power; liability | Registrar; company, its directors, secretaries and members | | send the letter, publish the notice, strike off; the company is dissolved; liability of officers and members continues (s 344(4)(a)) |
| s 344(5) | power | person aggrieved; the Court | | within 6 years apply to restore the name; the Court may order it |
| s 344A, 344B | power | company (by all its directors or a majority); Registrar; applicant | | apply to strike off; the applicant may withdraw |
| s 344C | power | any person | Registrar | object to the striking off |
| s 344D, 344E, 344F | power | former director or former member; Registrar; the Court | | apply to restore the name; appeal to the Court; the Registrar may restore on the Registrar's own initiative after a mistake |
| s 344G(2) | immunity | company and its directors | | not liable to a penalty under s 204 for a financial year whose filing period ended after the dissolution or striking off and before the restoration |
| s 344H(1) | duty (negative: SHANT) | officer | none named | not fail to retain the books and papers for 5 years after the dissolution |
| Schedules 14 and 15 | immunity | the companies and foreign companies the paragraphs name | | Part 11A (registers of controllers) does not apply to them |
| Schedule 16 | none (definitions) | | | when a person has significant control or a significant interest |


## Marginal readings for a lawyer (sgm)

The points where a lawyer reading the encoding should look twice.
Each is a place where the text does not decide the point and I took a reading; the fork register gives the other reading and the licence.

1. **Grants gated by where, when or upon answer JUST FALSE (9 sites; F-G4, F-G5, F-G6).**
   Two rulings pull in opposite directions here: the grant ruling (a "may" whose `if` gate fails answers NOTHING) and the periods ruling item (b) with delegated-definitions item (c) (a "where", "when" or "upon" gate that fails answers JUST FALSE).
   I followed the grant ruling's own limit 3, which leaves the "where/upon" sites as (b) and (c) give; the sites are listed under Split sites and in the fork register.
2. **The consent of s 195(2) answers NOTHING (F-G3).**
   "may with the consent of the company and of the registered holder": no consent is neither a prohibition nor a grant in the text, so the answer is NOTHING, not JUST FALSE.
3. **A period the text fixes: JUST FALSE outside it (F-P5).**
   s 196A(1) and (2)(a)(v), s 196D, s 196E, s 197(1), s 344(4), (5), s 344B(1), s 344C(1), s 344D(4), s 344E(2)(a), s 344F(3), s 344G(4) and s 344H(1) all carry a period in the text's own words, and each answers JUST FALSE for a date outside it.
4. **"Within N days after" counts the day of the event out and the last day in (F-P2).**
   An act on the day of the event itself is in time (the keel's `period: the date is not later than the end of a period after`), not "within" a window that opens the next day.
5. **The previous 7 years of s 196A(2)(a)(v) (F-P6).**
   A person who ceases to be a member on the date asked is not yet one who ceased "during the previous 7 years".
6. **A return lodged on the day of the annual general meeting is "after" it (F-P7).**
   The text does not say; a return of the meeting's results is lodged after the meeting, so a same-day return follows it.
7. **The further period of s 192(3) is added to the 21 days (F-R1).**
   "such further period as the Registrar considers reasonable": the person supplies the number of further days (0 if none).
8. **An application to restore a name made before the dissolution is valid (finding 3).**
   s 344D(2) lets an application be made whether or not the company has been dissolved, and s 344D(4) sets an upper limit; I read the 6 years as an upper limit only.
9. **A company that keeps a branch register abroad lodges its return under s 197(1A), and that return is not "the annual return" of s 4(1) (finding 5).**
   The keel's definition of "annual return" cites only s 197(1); the seam I give (`s 197(1) the return is the return required to be lodged under section 197(1)`) answers JUST FALSE for a (1A) company, on the text's own words.
10. **The financial year of s 198: a period that is not one the text describes is JUST FALSE (F-D1).**
    s 198 states which periods are financial years; the keel's "financial year" hands the question to it, and the delegated-definitions ruling item (a) gives JUST FALSE when no head holds.
11. **s 197(3) is machinery (inert, reason 2).**
    "may differ according to the class or description of company prescribed": the content of the return by class is taken through `the return contains the particulars and information prescribed` (a plain input), so nothing of s 197(2) is lost; if a maintainer reads s 197(3) as a rule, the row becomes encoded and the input becomes a function of the class.
12. **The 30-year step of s 194(4) from 29 February is 28 February (F-P4).**
    The Act says nothing for s 194(4); s 198(7) says 28 February for its own two cases, and the keel's P4 gives the same.

### Reading a result: FALSE and NOTHING (sgm)

A question that asks "is", "must", "may" or "does" answers JUST TRUE for yes.
**JUST FALSE** is the text's no, in its own words: a "means" definition (`s 197(1) the return is the return required ...` for a (1A) company), an "if" or "where" condition that fails, a period the text fixes, a flat negative, an exception stated by the text once met ("unless"), or a list closed with "only" (s 344D(3): "may only be made by a former director or former member").
**NOTHING** means the text does not say: a scope limit with no "only" (s 190(5) "having more than 50 members": a company with 50 or fewer is outside the section and the answer is NOTHING), a grant limited by its own wording (s 192(1) "not exceeding 30 days in the aggregate"), a power whose "if satisfied" gate failed (s 344(5)), the case where the text is silent, or the consent of s 195(2).
In the layer-1 code every `JUST FALSE` branch carries `-- FALSE-kind (...)` and every `NOTHING` branch `-- NOTHING-kind (...)`: 128 and 104 of them, 0 without (checked by script when this file was generated).
In the seat the same answers come out unchanged: the seat question calls the layer-1 function and returns its value (the exceptions are listed under The seat), so a person who sees NOTHING is being told the Act does not answer on those facts, and a person who sees JUST FALSE is being told the Act says no.
The seat's question names ask in the direction the body answers: a question about a bar is titled as the bar ("Under section 194(4), is the Court barred from entertaining my application ..."), never as the opposite ("may the Court entertain ...").
Audit of directions: every question was listed against the layer-1 function it calls (the list is in the scratch folder, not shipped); a script compared the polarity words (may, must, barred, cannot, need not, not required, not affected) of the two names, and the only differences were the dates and amounts ("by what day must ...", "what is the most ... can be fined"), which carry no polarity.
One rewording came out of that audit: s 196D(1)(b) now asks "until what day must my private company keep its register of members" because the function answers the last day of a period, not a deadline.


## Seams (sgm)

**Seams I give** (PLAN.md table A; each is a layer-1 function named for the fact, with a seat question beside it):

| section | function | inputs |
| --- | --- | --- |
| s 190 | `s 190(1) the register is the register of members of the company kept pursuant to section 190` | `the company is a public company`, `the register is the register of members of the company` |
| s 196 | `s 196(1) the register is a branch register of members of the company kept pursuant to section 196` | `the company is a public company`, `the company has a share capital`, `the register is kept in a place outside Singapore as a branch register of members of the company` |
| s 197 | `s 197(1) the return is the return required to be lodged under section 197(1)` | `the company has a share capital`, `the company keeps a branch register in a place outside Singapore`, `the return is lodged with the Registrar after the annual general meeting of the company` (see finding 5) |
| s 198 | `s 198 the period is a financial year of the company as section 198 determines` | 10 inputs (the dates and the notice facts of s 198) |

PLAN.md section 6 (my row) lists only ss 196, 197 and 198; table A has s 190 as well; I give all four.

**Seams I take** (a provision of another part, asked as a plain fact named for the fact and its section):

- `the company is a public company`, `the company is a private company` (s 4(1)), under the exact names and `@desc` of PLAN section 7.
  I take them as the shared plain inputs and do not call the keel's `s 4(1) "public company"` function, which would ask `the body is a company` and `the company is a private company` first; assumed, not ruled: the result is the same fact and the seat then asks it once.
  `sg-definitions` is therefore not imported by this part (`sg-core` and `sg-periods` are).
- `the company is a listed company` (s 4(1) "listed company"), `the company has a share capital`.
- `the private company is required under section 175A(4) to hold an annual general meeting ...` (sgl), and the three expiry facts of s 198(6): `the notice is lodged after the expiry of the period under section 175`, `... under section 197` and `... under section 203` (sgl, sgc1).
- s 76H and s 76K(1) (buy-back and cancellation, s 190(2A)), s 63(3) (deemed allotment, s 196A(2)), s 21(4B) and (6C) (treasury shares), s 19(1)(b) (the first financial year as furnished), s 12(2)(d) (public access to the contact address, s 196E(b)).
- s 204 (penalty for late financial statements, s 344G(2)), s 399 (the Court's power, s 193), s 386AA(1A) (Part 11A applies despite the Schedules).
- The regulations and the matters "prescribed" (forms, particulars, grounds, conditions, circumstances) are plain inputs, never guessed.
- The date of commencement of section 43 of the ACRA (Registry and Regulatory Enhancements) Act 2024 (s 196E) is an input date.

**A seam the plan lacks.**
The keel's seam for "annual return" is one BOOLEAN (`the return is the return required to be lodged under section 197(1)`); the text has a second return, under s 197(1A), which is not "the annual return" of s 4(1) on its words (finding 5).


## Split sites (sgm)

Two kinds of site where the guide's rulings pull two ways; each is counted, listed with the function that holds it, and carries a fork line.
Every site is tagged in the code with `split site (i)` or `split site (ii)` in its `-- FALSE-kind (...)` or `-- NOTHING-kind (...)` comment, so a grep finds it.


### Split site (i): an unmet element of an offence (12 sites)

- `s 190(7) the public company is guilty of an offence` (sgm-part5-div4.l4:335), fork F-O1
- `s 190(7) the officer of the company is guilty of an offence` (sgm-part5-div4.l4:348), fork F-O1
- `s 191(3) the public company is guilty of an offence` (sgm-part5-div4.l4:550), fork F-O1
- `s 191(3) the officer of the company is guilty of an offence` (sgm-part5-div4.l4:563), fork F-O1
- `s 192(4) the public company is guilty of an offence` (sgm-part5-div4.l4:756), fork F-O1
- `s 192(4) the officer of the company is guilty of an offence` (sgm-part5-div4.l4:770), fork F-O1
- `s 196(9) the public company is guilty of an offence` (sgm-part5-div4.l4:1377), fork F-O1
- `s 196(9) the officer of the company is guilty of an offence` (sgm-part5-div4.l4:1392), fork F-O1
- `s 196(9) the person who arranged to make up the principal register is guilty of an offence` (sgm-part5-div4.l4:1408), fork F-O1
- `s 197(6) the company is guilty of an offence` (sgm-part5-div5.l4:288), fork F-O1
- `s 197(6) the officer of the company is guilty of an offence` (sgm-part5-div5.l4:301), fork F-O1
- `s 344H(2) the officer of the company is guilty of an offence` (sgm-part10.l4:1193), fork F-O1

### Split site (ii): a "may" gated by where, when, upon, on application or with the consent of (10 sites tagged in the code, plus s 344(5))

- `s 193 the power of the Court under section 399 extends to orders against that other person and that person's officers and employees` (sgm-part5-div4.l4:823)
- `s 194(2) the Court may decide the question on the application` (sgm-part5-div4.l4:931)
- `s 195(2) the trustee, executor or administrator may become registered as the holder of the share` (sgm-part5-div4.l4:1007)
- `s 197(1B) the Registrar may extend the period within which the company must lodge its return` (sgm-part5-div5.l4:203)
- `s 344(1) the Registrar may send the company and its directors, secretaries and members a letter` (sgm-part10.l4:50)
- `s 344A(1) the Registrar may strike the company's name off the register on the application of the company` (sgm-part10.l4:429)
- `s 344C(1) any person may deliver an objection to the striking off of the name of the company` (sgm-part10.l4:754)
- `s 344E(5)(a) the Court may confirm the Registrar's decision` (sgm-part10.l4:1021)
- `s 344E(5)(b) the Court may restore the name of the company to the register and give directions and make orders` (sgm-part10.l4:1033)
- `s 344G(3) the Court may give directions and make orders for placing the company and all other persons in the same position` (sgm-part10.l4:1128)

The fork lines for these sites quote the Guide section 5 line each one relies on:

- Split site (i) (fork F-O1): Guide section 5, rule of 2026-10-29, as summarised under "Rulings on negatives and legal effects": "a condition the text introduces with 'if' ... JUST FALSE".
  The other reading is that the section is silent on the innocence of anyone it does not make guilty (NOTHING).
- Split site (ii), a "may" whose gate is where, when, upon or on application (forks F-G4, F-G5, F-G6): periods ruling of 2026-11-05, item (b), Guide section 5: "a "where ..." condition: when it fails the answer is `JUST FALSE`", with the delegated-definitions ruling item (c): "'when', 'upon' and 'whenever' count as 'where'"; the grant ruling of 2026-11-12, limit 3, lists the site for the maintainer and does not change it.
- Split site (ii), a "may" gated by the consent of someone (fork F-G3, s 195(2)): the grant ruling of 2026-11-12, limit 1, quoted in Guide section 5: "answer `NOTHING` ... only for a function named for a grant or a power ('may', 'is permitted to', 'has power to') whose `if` gate failed", and its limit 3.
- Split site (ii) at s 344(5), a power on application within 6 years whose "if satisfied" gate failed (fork F-G5): outside the 6 years JUST FALSE (periods ruling item (a)); within them NOTHING (grant ruling, limit 1).
  This site carries the fork id in its comment but not the `split site (ii)` tag on the branch line; it is counted here by hand.

Counts: 12 sites of kind (i); 10 tagged sites of kind (ii), plus s 344(5) counted by hand (so 11 in all).
Of the sites of kind (ii), 9 answer JUST FALSE for an unmet where/upon gate (the grant-ruling register under the fork register), 1 answers NOTHING for an unmet consent (s 195(2)), and s 344(5) answers JUST FALSE outside its period and NOTHING when "if satisfied" fails.


## Rules with no breach path (sgm)

A `MUST` or `SHANT` with no deadline cannot reach BREACH in a `#TRACE`: the obligation stays a RESIDUAL until it is done, and the text names no moment at which it lapses.
These are the 21 regulative rules of this part with no breach path (of 32 in all); each has a `#TRACE` showing FULFILLED and one showing the RESIDUAL, and no `#TRACE` can show BREACH.
The Registrar's duties of Part 10 and ss 196A(1), (5) are here because the text gives no time for them; they are encoded in layer 1 for what they decide, and the seat asks them only as what they mean to the person ("must the Registrar update the electronic register of my company"), never from the Registrar's side.
The other 11 rules carry a deadline in the text (a number of days, or a period such as the 7 years of s 196D(1), or the 5 years of s 344H(1)), and each has a `#TRACE` that reaches BREACH on both stable builds, with `-- EXPECT BREACH` above it.


- `s 190(1) a public company must keep a register of its members` (sgm-part5-div4.l4): traces FULFILLED, RESIDUAL
- `s 190(5) a public company having more than 50 members must keep an index of the names of the members` (sgm-part5-div4.l4): traces FULFILLED, RESIDUAL
- `s 192(2) a public company must open the register and index to inspection` (sgm-part5-div4.l4): traces FULFILLED, RESIDUAL
- `s 196(4) a public company must transmit a copy of every entry in its branch register` (sgm-part5-div4.l4): traces FULFILLED, RESIDUAL
- `s 196(4) a public company must cause a duplicate of its branch register to be kept` (sgm-part5-div4.l4): traces FULFILLED, RESIDUAL
- `s 196A(1) the Registrar must keep an electronic register of members of every private company` (sgm-part5-div4a.l4): traces FULFILLED, RESIDUAL
- `s 196A(5) the Registrar must update the electronic register of members` (sgm-part5-div4a.l4): traces FULFILLED, RESIDUAL
- `s 344(4) the Registrar must publish notice of the striking off in the Gazette (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344(7)(a) the Registrar must send the particulars to the Inland Revenue Authority of Singapore and the Central Provident Fund Board (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344(7)(b) the Registrar must publish the substance of the notices on the Authority's website (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344A(3) the Registrar must send the letter informing the company, its directors, secretaries and members of the application (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344A(5) the Registrar must strike off the name of the company from the register and publish a notice in the Gazette (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344A(8)(a) the Registrar must send the particulars of the company and of the application to the Inland Revenue Authority of Singapore and the Central Provident Fund Board (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344A(8)(b) the Registrar must publish the substance of the notices on the Authority's website (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344B(2)(a) the Registrar must send the company a notice that the application has been withdrawn (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344B(2)(b) the Registrar must publish a notice on the Authority's website that the application has been withdrawn (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344C(3)(a) the Registrar must give the applicant or applicants notice of the objection (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344C(3)(b) the Registrar must take into account the prescribed considerations (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344E(1) the Registrar must give the applicant notice of the decision (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344E(2)(b)(i) the Registrar must enter in the register a note of the date of the restoration (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL
- `s 344E(2)(b)(ii) the Registrar must cause notice of the restoration to be published (rule)` (sgm-part10.l4): traces FULFILLED, RESIDUAL

The 11 regulative rules that do reach BREACH in a `#TRACE` (each with a deadline):

- `s 190(5) a public company must alter the index within 14 days after an alteration of the register`
- `s 191(2) a public company must lodge notice with the Registrar within 14 days`
- `s 192(3) a public company must send the requested copy within 21 days`
- `s 196(2) a public company must lodge notice with the Registrar within 14 days`
- `s 196B(1) a private company must lodge the information by the earlier of the two dates`
- `s 196C(2)(c) a private company must notify the Registrar of the trustee's request within 14 days`
- `s 196D(1)(a) a private company must not stop keeping the branch register within 7 years after 3 January 2016`
- `s 196D(1)(b) a private company must not stop keeping its register of members within 7 years after the last member ceased`
- `s 197(1) a company must lodge a return with the Registrar within the time the subsection gives`
- `s 197(4) a private company must lodge a notice of the date of the annual general meeting within 14 days`
- `s 344H(1) an officer must not fail to retain the books and papers within 5 years after the dissolution`

## Numbered findings: what the text turns out to say (sgm)

1. **s 194(3), "so lodged", has no antecedent in this rendering.**
   "The Court when making an order for rectification of the register must by its order direct a notice of the rectification to be so lodged."
   Nothing earlier in s 194 mentions lodging anything.
   Encoded as the Court's direction that a notice of the rectification be lodged (`s 194(3) the Court's order must direct a notice of the rectification to be lodged`); the Registrar as the recipient is not in the sentence and is not assumed.
2. **s 196C(2)(a) says "under section 194" in a paragraph that modifies section 195.**
   "(a) a reference to a register under section 194 refers to the electronic register of members of the private company in question".
   Subsection (1), which modifies s 194, has the same phrase.
   The paragraph is followed as printed; the seat asks which reference in s 195 is being read (a choice of three) and the layer-1 function answers on it.
3. **s 344D(2) and (4) leave the case of an application made before the dissolution open.**
   Subsection (2): an application "may be made whether or not the company has in consequence been dissolved".
   Subsection (4): not valid "unless the application is received by the Registrar within 6 years after the date on which the company is dissolved".
   Read literally, an application received before the date of dissolution is not "within 6 years after" it.
   Read with (2), the 6 years are an upper limit.
   Encoded as an upper limit only (`s 344D(4) the application is valid as to time` is JUST TRUE for a date on or before the 6th anniversary of the dissolution, and so for an earlier date); a test on each side.
4. **The rendering prints the closing words of three lists with a second label.**
   Fourteenth Schedule para 1(f) ("(f) imposed through stock exchange rules, law or other enforceable means"), Fifteenth Schedule para 1(c) (the same words, labelled "(c)") and Sixteenth Schedule para 4(6)(b) (the closing words about "at least some degree of stability", labelled "(b)").
   In each the closing words belong to the paragraph above them (the label is repeated by the rendering); they are encoded as the closing words of (f), (c) and (b) respectively, and the quotations show the repeated label as printed.
5. **s 4(1) "annual return" cites s 197(1) only, and a company within s 197(1A) lodges its return under (1A).**
   s 4(1): "annual return" means the return required to be lodged under section 197(1); s 197(1) is for "every company, other than a company mentioned in subsection (1A)".
   On the words, the return of a company that has a share capital and keeps a branch register outside Singapore is not "the annual return" of s 4(1).
   The seam `s 197(1) the return is the return required to be lodged under section 197(1)` answers JUST FALSE for such a company ("means" with a closed list); if the maintainer prefers the reading that the (1A) return is also an annual return, the seam becomes JUST TRUE for both and the keel's definition is the place to change.
6. **s 197(3) is machinery.**
   "The particulars to be contained in, and the documents that are to accompany, the return mentioned in subsection (1) may differ according to the class or description of company prescribed."
   It gives the regulations a power to vary what s 197(2) requires by class, so it is inert, reason 2 (regulation-making power); s 197(2) takes what is prescribed as plain inputs (`the return is in the form prescribed`, `the return contains the particulars and information prescribed`, `the return is accompanied by the documents prescribed`).
7. **No assertion fails or is refused.**
   There are no expected failures: the `expected` column of `check.sh` is 0 for every module, and the run is green on both builds.


## What the stable binary does not accept (sgm)

Each line below was measured on the stable binary 1.6.110 (`l4 run`) on 2026-11-18 with a four-line probe file, not read from a document.
Sorted by how the failure shows up.

**Loud (an error diagnostic; check.sh counts it):**

- `REFUSE`: `parse/unexpected-end-of-input`.
  A case outside the encoding is an explicit `NOTHING` (or an "other" constructor) that a test asserts.
- Pattern-matching on a date, `WHEN Date a b c THEN ...`: `check/unknown-identifier`.
  `Date` is a function (`Date 1 3 2026`), not a constructor; read the parts with `DATE_DAY`, `DATE_MONTH` and `DATE_YEAR`, or step the date with the keel's `period:` functions.
- A name that `daydate` already defines (`year of` is one), defined again in a module: `check/ambiguous-identifier`, reported at the use.
  Every top-level name of this part begins with its provision label, which avoids it.
- A continuation line under an `#ASSERT` (the second line starting `AND`): `parse/unexpected-AND`.
  One assertion per line.

**Silent (exit status 0, no diagnostic; only a test or a reading of the code finds them):**

- `NOT a AND b` parses as `NOT (a AND b)`.
  With `a` TRUE and `b` FALSE it evaluates to TRUE; `(NOT a) AND b` is FALSE.
  Every `NOT` in this part is parenthesised.
- A `GIVEN` parameter the body never uses is accepted without a warning.
  `l4 run` does not tell you; three were found by reading the code and removed.
- `l4 run` exits 0 when an `#ASSERT` fails or refuses (the header of `check.sh` says so, and says that no exit code says which assertion failed): the numbers come from `check.sh`, not from the exit status.
- A different `#TRACE` outcome on the two stable builds changes no assertion count and is therefore invisible to `check.sh` (its header says so); each `#TRACE` here has an `-- EXPECT` word above it and `work/tc.sh` ran the file on both builds and compared: no mismatch.


## What check.sh prints (sgm)

Run as `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` in `encodings/legalese-sonnet-5.5/`, target `main` (every module is run on both stable builds and the four counts are compared), exit status 0; it also printed nothing on stderr.
Read as diagnostics, not as the exit code: 20 modules, 0 errors, 1415 assertions satisfied, 0 failed, 0 refused, the same on both builds.
Assertions written equal assertions satisfied in each test file (written: 235, 122, 136, 188, 95, 639; satisfied: the same, read from the `satisfied` column below).
No file shows a `DiagnosticSeverity_Error` or `_Warning` on either build.

**Baseline it replaced.**
The keel alone (`sg-*.l4`, 8 modules, as supplied), run through the same `check.sh` and the same two builds: `TOTAL (8 modules)  0 errors, 0 satisfied, 0 failed, 0 refused`, the same on main.
With this part: `TOTAL (20 modules)` below (the 8 keel modules still print 0; the 12 modules of this part print their own counts).


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
sgm-cases-seat.l4                              0       639       0        0         0 |      0       639       0        0  same
sgm-part10.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgm-part5-div4.l4                              0         0       0        0         0 |      0         0       0        0  same
sgm-part5-div4a.l4                             0         0       0        0         0 |      0         0       0        0  same
sgm-part5-div5.l4                              0         0       0        0         0 |      0         0       0        0  same
sgm-schedules.l4                               0         0       0        0         0 |      0         0       0        0  same
sgm-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgm-tests-part10.l4                            0       188       0        0         0 |      0       188       0        0  same
sgm-tests-part5-div4.l4                        0       235       0        0         0 |      0       235       0        0  same
sgm-tests-part5-div4a.l4                       0       122       0        0         0 |      0       122       0        0  same
sgm-tests-part5-div5.l4                        0       136       0        0         0 |      0       136       0        0  same
sgm-tests-schedules.l4                         0        95       0        0         0 |      0        95       0        0  same
TOTAL (20 modules)                             0      1415       0        0           |      0      1415       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## Tests (sgm)

| file | assertions written | #TRACE |
| --- | --- | --- |
| sgm-tests-part5-div4.l4 | 235 | 22 |
| sgm-tests-part5-div4a.l4 | 122 | 18 |
| sgm-tests-part5-div5.l4 | 136 | 11 |
| sgm-tests-part10.l4 | 188 | 31 |
| sgm-tests-schedules.l4 | 95 | 0 |
| sgm-cases-seat.l4 | 639 | 0 |
| total | 1415 | 82 |

The expected outcome of every `#TRACE` is written above it (`-- EXPECT FULFILLED`, `BREACH` or `RESIDUAL`): 18 BREACH, 36 FULFILLED, 28 RESIDUAL. `work/tc.sh` compared each on both stable builds (1.6.110 and 1.6.109): no mismatch.


## The seat (sgm)

The seat is an individual who is, or is about to become, a director, the company secretary or a member of a company or a foreign company, or who deals with one.
Every question is named "Under section N, ..." (or "Under schedule N paragraph M, ...") in the direction its body answers, is `@export`ed, and has an `@desc` on every input worded as the person would be asked.
Questions are grouped under `§` headings in the text's order (one per Division of Part 5, one for Part 10 Division 4 Subdivision (5), one for the Schedules) and `§§` headings by section.
There is never a seat for the Registrar, the Court or the Minister: their duties and powers appear as what they mean to the person ("must the Registrar update the electronic register", "may the Court order my company's name to be restored"), asked on facts the person can state.
The seat calls the layer-1 function and returns its value, and never restates a rule.
The exceptions, all wiring and no rule: the two questions that take a layer-1 record build it from the yes/no facts inside the question (s 190(1), 7 facts; s 196A(2), 8 facts); s 198(4) calls the layer-1 functions of s 198(5) and (6) in a `WHERE` and passes their answers to s 198(4); the penalty questions return the highest fine in dollars from the layer-1 `Penalty` (a `MAYBE NUMBER`); and the enumerated inputs of layer 1 are renamed in the person's voice (for example `where my company's register and index are kept`), each with a plain `@desc`.
The shared inputs of PLAN section 7 are used under their exact name and `@desc`: `the date asked`, `the company is a private company` and `the company is a public company`.
An input named for a fact has the same name, type and `@desc` in every question that asks it (the generator refuses to emit a file otherwise).
The cases (`sgm-cases-seat.l4`) are the layer-1 tests re-asked through the seat question with the same facts, so their expected values are the ones written from the text; for each question every outcome that its layer-1 tests have (a yes, the text's no, a NOTHING) is in the cases (checked by script), and the three special questions have hand-written cases.


| section | questions |
| --- | --- |
| Part 5 Division 4: the register and index of members of a public company (sections 189A to 196) | 76 |
| Part 5 Division 4A: the electronic register of members kept by the Registrar (sections 196A to 196E) | 30 |
| Part 5 Division 5: the annual return and the financial year (sections 197 and 198) | 26 |
| Part 10 Division 4 Subdivision (5): striking off and restoring a company's name (sections 344 to 344H) | 62 |
| The Fourteenth, Fifteenth and Sixteenth Schedules: Part 11A (registers of controllers) | 24 |
| total | 218 |

## What the text does not answer (sgm)

- Who prosecutes, or who may enforce a duty: ss 190 to 192, 196, 197 and 344H state offences and no prosecutor; the Hohfeld table records "none named".
- Who bears the duties the text states without a bearer (ss 190(6), 195(3), 196(3), 196(5) first limb, 196A(4), 198(2); fork F-B1): decision functions only, no regulative rule.
- Everything the text hands to the regulations: the form and contents of the return (s 197(2)), the prescribed grounds and conditions of s 344A(1) and s 344D(1), the prescribed circumstance of s 344(1A), the prescribed considerations of s 344C(3)(b), the prescribed class of s 197(1B)(b).
  Each is a plain input, never guessed.
- Whether the day of an act is "after" the day of the event it follows (F-P2, F-P7) and whether "the previous 7 years" includes the date asked (F-P6): one reading taken each, the other on record.
- What s 344D(4) means for an application received before the dissolution (finding 3).
- Whether a company within s 197(1A) lodges "the annual return" of s 4(1) (finding 5).
- The 30-year step of s 194(4) from 29 February (F-P4).

## NEEDS-CORE (sgm)

None.
This part needed no type or constructor the core lacks, so there is no `NEEDS-CORE.md`.
The local constants (`s 198 the day 31 August 2018`) and the recursive anniversary helper of s 198(3)(a) are this part's own declarations under its own prefix, not requests.

## Progress

`PROGRESS.md` in this folder records the sections done, the decisions taken and the files written.
The generators (`work/gen.py`, `work/mk_notes.py`, `work/mk_seat.py`, `work/mk_tests_*.py`) and the checks (`work/covcheck.py`, `work/tc.sh`) are in `DEPOSIT/../work/`, which is not shipped.
