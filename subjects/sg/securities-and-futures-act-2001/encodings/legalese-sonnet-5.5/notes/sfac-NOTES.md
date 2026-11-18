# NOTES: the Securities and Futures Act 2001 (Singapore), Part 13, Division 1, Subdivisions (1) and (2), ss 239 to 260 (sfac)

Every sentence below that states a count was produced by a script run on the files in this folder (`work/assemble.py` reads them and writes this file; `work/cov.py`, `work/units.py`, `work/tags.py`, `work/verify.py`, `work/traces.py` and the scratch generators are not part of the deposit), or is marked as an observation of one run.

## Edition encoded

The Securities and Futures Act 2001, 2020 Revised Edition, in the Singapore Statutes Online (SSO) informal consolidation "version in force from 29/6/2026 to 20/10/2026", retrieved 2026-10-09 (`inputs/SOURCES.md` has its hashes), carrying the amendments its amendment marks show.
That file is a plain-text rendering of a PDF: it is **not the official text**, and nothing here is verified against the official text.
A later consolidation may exist and was not read; the encoding is of that text only.
Line numbers (`src:N`) are lines of that file as it is.
This part's ranges are lines 37499 to 37947 (Part 13, Division 1, Subdivision (1), ss 239 to 239B) and lines 38374 to 41832 (Subdivision (2), ss 240 to 260); lines 37948 to 38373 and the lines after 41832 belong to other parts.
Amendment marks (`[4/2017]`, `[Act 12 of 2026 wef 29/06/2026]`) and page furniture are not quoted and are not rules; they sit in the row of the unit they fall in.
The text is quoted only where it is encoded, mechanically (`srcrefs.py` checks every quote line and every `@ref` locator).
Nothing in this folder says or suggests that the Singapore Government or the Attorney-General's Chambers endorses, checks or is associated with this work.

Where this part's brief and `inputs/PLAN.md` differ, the brief governs, and the differences taken are these.
`inputs/PLAN.md` section 8 lists a section `## Compared with the earlier pass`; the brief asks for it only if `inputs/NAIVE-EVIDENCE/` is present, and that folder is not in this sandbox, so there is no such section.
`inputs/PLAN.md` section 4.3 types the seam inputs S4 and S5 as `BOOLEAN`; they are `MAYBE BOOLEAN` here, so that a `NOTHING` from the part that answers is never read as a no (the brief: "a caller must never turn `NOTHING` into `FALSE`"); the input names are the plan's, word for word (see Seams).
The brief's split-site and marginal-reading rules (the lines marked `-- SPLIT-SITE (i)`, `-- SPLIT-SITE (ii)`, `-- MARGINAL-READING (a)`, `-- GRANT-RULING (1)`) are applied as the brief gives them.

## Coverage (sfac)

One row per section, subsection, defined term, paragraph, sub-paragraph and sub-sub-paragraph of lines 37499 to 37947 and 38374 to 41832: 808 rows, of which 616 `encoded`, 147 `fork`, 39 `inert` (34 of reason 1, 5 of reason 2, 0 of reason 3) and 6 `repealed or blank in this text`.
Check by script (`work/cov.py`): all 2587 non-blank lines of the two ranges fall in exactly one row (0 in no row, 0 in more than one), and no row is left without a declaration or an inert or repealed range; the `Lines` column gives each row's inclusive range (blank lines, page furniture and amendment marks inside a range belong to its row).
The rows come from the text: `work/units.py` splits the lines of the two ranges at the markers the text itself carries (a section number, `(1)`, `(a)`, `(i)`, `(A)`, a defined term in curly quotes, a marginal heading) and counts 808 text units; the code is then read for which function covers each unit (its `@ref` locators and the lines it quotes), so that a unit that is not named by an `@ref` of its own is shown as covered by the function it sits in.
Audit counts: the first table was built from the `@ref` labels alone and had 367 rows, with 8 non-blank lines in no row (found by the line check; five locators were short of the text and were corrected: the second line of s 242(5)(a), the lead-in of s 243(8), the lead-in of s 253(5)(a), the lead-in "then" of s 259(1)(c), and s 247(1), which a script had hidden behind the next locator); 327 distinct `@ref` labels remain now (observation of this run), 808 text units were counted, and the table after the audit has 808 rows, one per unit.
Where the text numbers two paragraphs alike, the second row says "(second one numbered alike)" and the text's own numbering is kept (finding 3).
A row names the L4 functions that encode it (all in the module shown; tests are in the module of the same name with `-tests`, the regulative duties in `sfac-duties.l4` and `sfac-tests-duties.l4`, and the seat in `sfac-seat.l4` and `sfac-cases-seat.l4`); where a unit is covered inside the function of the unit above it, the row says so and names that unit.

| Provision | Lines | Disposition | Module | L4 name(s) or reason |
| --- | --- | --- | --- | --- |
| heading: PART 13 | src:37499-37500 | inert (reason 1) | sfac-239 | Part 13, Division 1 and Subdivision (1) headings: not operative. |
| heading: OFFERS OF INVESTMENTS | src:37501-37502 | inert (reason 1) | sfac-239 | Part 13, Division 1 and Subdivision (1) headings: not operative. |
| heading: Division 1 — Securities and Securities-based Derivatives Contracts | src:37503-37506 | inert (reason 1) | sfac-239 | Part 13, Division 1 and Subdivision (1) headings: not operative. |
| heading: Subdivision (1) — Interpretation | src:37507-37508 | inert (reason 1) | sfac-239 | Part 13, Division 1 and Subdivision (1) headings: not operative. |
| s 239 marginal heading | src:37509-37510 | inert (reason 1) | sfac-239 | Part 13, Division 1 and Subdivision (1) headings: not operative. |
| s 239(1) | src:37511-37512 | inert (reason 1) | sfac-239 | s 239(1) chapeau "In this Division": introduces the definitions below, each encoded as its own function; creates no rule of its own. |
| s 239(1) "borrowing entity" | src:37513-37517 | encoded | sfac-239 | `s 239(1) "borrowing entity" the body is a borrowing entity` |
| s 239(1) "control" | src:37518-37521 | encoded | sfac-239 | `s 239(1) "control" the person has control of the entity` |
| s 239(1) "control" (a) | src:37522-37525 | encoded | sfac-239 | in the function(s) of s 239(1) "control" |
| s 239(1) "control" (b) | src:37526-37539 | encoded | sfac-239 | in the function(s) of s 239(1) "control" |
| s 239(1) "dealing in capital markets products" | src:37540-37544 | encoded | sfac-239 | `s 239(1) "dealing in capital markets products" the activity is dealing in securities or securities-based derivatives contracts` |
| s 239(1) "dealing in capital markets products" (a) | src:37545-37546 | encoded | sfac-239 | in the function(s) of s 239(1) "dealing in capital markets products" |
| s 239(1) "dealing in capital markets products" (b) | src:37547-37554 | encoded | sfac-239 | in the function(s) of s 239(1) "dealing in capital markets products" |
| s 239(1) "debenture issuance programme" | src:37555-37561 | encoded | sfac-239 | `s 239(1) "debenture issuance programme" the arrangement is a debenture issuance programme` |
| s 239(1) "expert" | src:37562-37564 | encoded | sfac-239 | `s 239(1) "expert" the person is an expert` |
| s 239(1) "guarantor entity" | src:37565-37570 | encoded | sfac-239 | `s 239(1) "guarantor entity" the body is a guarantor entity of the borrowing entity` |
| s 239(1) "immediate family" | src:37571-37575 | encoded | sfac-239 | `s 239(1) "immediate family" the person is in the immediate family of the individual` |
| s 239(1) "issuer" | src:37576-37577 | encoded | sfac-239 | `s 239(1) "issuer" the person is the issuer in relation to the offer` |
| s 239(1) "issuer" (a) | src:37578-37586 | encoded | sfac-239 | in the function(s) of s 239(1) "issuer" |
| s 239(1) "issuer" (b) | src:37587-37590 | encoded | sfac-239 | in the function(s) of s 239(1) "issuer" |
| s 239(1) "issuer" (c) | src:37591-37595 | encoded | sfac-239 | in the function(s) of s 239(1) "issuer" |
| s 239(1) "minimum subscription" | src:37596-37604 | encoded | sfac-239 | `s 239(1) "minimum subscription" the amount of the minimum subscription` |
| s 239(1) "preliminary document" | src:37605-37612 | encoded | sfac-239 | `s 239(1) "preliminary document" the document is a preliminary document` |
| s 239(1) "product highlights sheet" | src:37613-37615 | encoded | sfac-239 | `s 239(1) "product highlights sheet" the document is a product highlights sheet` |
| s 239(1) "profile statement" | src:37616-37618 | encoded | sfac-239 | `s 239(1) "profile statement" the document is a profile statement` |
| s 239(1) "promoter" | src:37619-37625 | encoded | sfac-239 | `s 239(1) "promoter" the person is a promoter in relation to the prospectus` |
| s 239(1) "prospectus" | src:37626-37635 | encoded | sfac-239 | `s 239(1) "prospectus" the document is a prospectus` |
| s 239(1) "prospectus" (a) | src:37636-37637 | encoded | sfac-239 | in the function(s) of s 239(1) "prospectus" |
| s 239(1) "prospectus" (b) | src:37638-37641 | encoded | sfac-239 | in the function(s) of s 239(1) "prospectus" |
| s 239(1) "prospectus" (c) | src:37642-37643 | encoded | sfac-239 | in the function(s) of s 239(1) "prospectus" |
| s 239(1) "recognised securities exchange" | src:37644-37648 | encoded | sfac-239 | `s 239(1) "recognised securities exchange" the corporation is a recognised securities exchange` |
| s 239(1) "related party" | src:37649-37650 | encoded | sfac-239 | `s 239(1) "related party" (a) the person is a related party of the entity` |
| s 239(1) "related party" (a) | src:37651-37652 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" |
| s 239(1) "related party" (a)(i) | src:37653-37654 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (a) |
| s 239(1) "related party" (a)(ii) | src:37655-37657 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (a) |
| s 239(1) "related party" (a)(iii) | src:37658-37659 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (a) |
| s 239(1) "related party" (a)(iv) | src:37660-37661 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (a) |
| s 239(1) "related party" (a)(v) | src:37662-37663 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (a) |
| s 239(1) "related party" (a)(vi) | src:37664-37666 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (a) |
| s 239(1) "related party" (a)(vii) | src:37667-37669 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (a) |
| s 239(1) "related party" (b) | src:37670-37671 | encoded | sfac-239 | `s 239(1) "related party" (b) the person is a related party of the individual` |
| s 239(1) "related party" (b)(i) | src:37672-37673 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (b) |
| s 239(1) "related party" (b)(ii) | src:37674-37677 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (b) |
| s 239(1)(b)(ii)(A) | src:37678-37679 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (b)(ii) |
| s 239(1)(b)(ii)(B) | src:37680-37685 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (b)(ii) |
| s 239(1) "related party" (b)(ii) (second one numbered alike) | src:37686-37687 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (b) |
| s 239(1) "related party" (b)(iii) | src:37688-37693 | encoded | sfac-239 | in the function(s) of s 239(1) "related party" (b) |
| s 239(1) "replacement document" | src:37694-37697 | encoded | sfac-239 | `s 239(1) "replacement document" the document is a replacement document` |
| s 239(1) "statutory meeting" | src:37698-37700 | encoded | sfac-239 | `s 239(1) "statutory meeting" the meeting is a statutory meeting` |
| s 239(1) "supplementary document" | src:37701-37704 | encoded | sfac-239 | `s 239(1) "supplementary document" the document is a supplementary document` |
| s 239(1) "trust deed" | src:37705-37707 | encoded | sfac-239 | `s 239(1) "trust deed" the document is a trust deed` |
| s 239(1) "trust property" | src:37708-37710 | encoded | sfac-239 | `s 239(1) "trust property" the property is trust property` |
| s 239(1) "underlying entity" | src:37711-37714 | encoded | sfac-239 | `s 239(1) "underlying entity" the body is the underlying entity of the offer` |
| s 239(1) "unit" | src:37715-37721 | encoded | sfac-239 | `s 239(1) "unit" the thing is a unit of a share or debenture` |
| s 239(2) | src:37722-37726 | encoded | sfac-239 | `s 239(2) the statement is deemed to be included in the prospectus or profile statement` |
| s 239(3) | src:37727-37728 | encoded | sfac-239 | `s 239(3)(a) the invitation is deemed to be an offer of debentures of the entity` |
| s 239(3)(a) | src:37729-37735 | encoded | sfac-239 | in the function(s) of s 239(3) |
| s 239(3)(b) | src:37736-37742 | encoded | sfac-239 | `s 239(3)(b) the document is deemed to be a debenture` |
| s 239(3A) | src:37743-37744 | encoded | sfac-239 | `s 239(3A)(a) the invitation by the prescribed entity is not an offer of debentures`, `s 239(3) and (3A) the invitation to deposit or lend is an offer of debentures` |
| s 239(3A)(a) | src:37745-37748 | encoded | sfac-239 | `s 239(3A)(a) the invitation by the prescribed entity is not an offer of debentures` |
| s 239(3A)(b) | src:37749-37751 | encoded | sfac-239 | `s 239(3A)(b) the document issued by the prescribed entity is not a debenture` |
| s 239(3A)(b)(i) | src:37752-37753 | encoded | sfac-239 | in the function(s) of s 239(3A)(b) |
| s 239(3A)(b)(ii) | src:37754-37758 | encoded | sfac-239 | in the function(s) of s 239(3A)(b) |
| s 239(4) | src:37759-37760 | encoded | sfac-239 | `s 239(4) "deposit" the thing is a deposit` |
| s 239(4) "deposit" | src:37761-37763 | encoded | sfac-239 | in the function(s) of s 239(4) |
| s 239(4) "prescribed entity" | src:37764-37765 | encoded | sfac-239 | `s 239(4) "prescribed entity" the body is a prescribed entity` |
| s 239(4) "prescribed entity" (a) | src:37766-37767 | encoded | sfac-239 | in the function(s) of s 239(4) "prescribed entity" |
| s 239(4) "prescribed entity" (b) | src:37768-37772 | encoded | sfac-239 | in the function(s) of s 239(4) "prescribed entity" |
| s 239(4A) | src:37773-37778 | encoded | sfac-239 | `s 239(4A) the instrument is within the references to a debenture in this Division` |
| s 239(5) | src:37779-37780 | encoded | sfac-239 | `s 239(5) the prescribed entity must comply with the condition or restriction` |
| s 239(5)(a) | src:37781-37786 | encoded | sfac-239 | in the function(s) of s 239(5) |
| s 239(5)(b) | src:37787-37793 | encoded | sfac-239 | in the function(s) of s 239(5) |
| s 239(5A) | src:37794-37800 | fork | sfac-239 | `s 239(5A) the person is guilty of an offence`, `s 239(5A) the penalty for the offence`, `s 239(5A) the prescribed entity shall not contravene a condition or restriction` (fork F1 in NOTES.md) |
| s 239(6) | src:37801-37804 | encoded | sfac-239 | `s 239(6) the person makes an offer of securities or securities-based derivatives contracts` |
| s 239(6)(a) | src:37805-37812 | encoded | sfac-239 | in the function(s) of s 239(6) |
| s 239(6)(b) | src:37813-37822 | encoded | sfac-239 | in the function(s) of s 239(6) |
| s 239(7) | src:37823-37825 | encoded | sfac-239 | `s 239(7) the disposal is a sale for the purposes of subsection (6)` |
| s 239(8) | src:37826-37833 | encoded | sfac-239 | `s 239(8) this Division applies to the offer`, `s 239A(1) and (2), s 239(8) and Subdivision (4): this Subdivision applies to the offer` |
| s 239AA marginal heading | src:37834-37835 | inert (reason 1) | sfac-239 | heading "Offers of sponsored depositary receipts". |
| s 239AA(1) | src:37836-37837 | inert (reason 1) | sfac-239 | s 239AA(1) chapeau "In this Division": introduces the two definitions below. |
| s 239AA(1) "depositary" | src:37838-37841 | encoded | sfac-239 | `s 239AA(1) "depositary" the person is the depositary in relation to the offer of SDRs` |
| s 239AA(1) "SDR" | src:37842-37844 | encoded | sfac-239 | `s 239AA(1) "SDR" the instrument is an SDR or sponsored depositary receipt` |
| s 239AA(1) "SDR" (a) | src:37845-37848 | encoded | sfac-239 | in the function(s) of s 239AA(1) "SDR" |
| s 239AA(1) "SDR" (b) | src:37849-37850 | encoded | sfac-239 | in the function(s) of s 239AA(1) "SDR" |
| s 239AA(1) "SDR" (b)(i) | src:37851-37854 | encoded | sfac-239 | in the function(s) of s 239AA(1) "SDR" (b) |
| s 239AA(1) "SDR" (b)(ii) | src:37855-37858 | encoded | sfac-239 | in the function(s) of s 239AA(1) "SDR" (b) |
| s 239AA(1) "SDR" (c) | src:37859-37866 | encoded | sfac-239 | in the function(s) of s 239AA(1) "SDR" |
| s 239AA(2) | src:37867-37868 | fork | sfac-239 | `s 239AA(2) the offer of SDRs is within the references to an offer of securities` (fork F2 in NOTES.md) |
| s 239AA(2)(a) | src:37869-37870 | encoded | sfac-239 | in the function(s) of s 239AA(2) |
| s 239AA(2)(b) | src:37871-37873 | encoded | sfac-239 | in the function(s) of s 239AA(2) |
| s 239AA(2)(c) | src:37874-37876 | encoded | sfac-239 | in the function(s) of s 239AA(2) |
| s 239AA(3) | src:37877-37882 | encoded | sfac-239 | `s 239AA(3)(a) the person is treated as the issuer of the SDRs being offered` |
| s 239AA(3)(a) | src:37883-37885 | encoded | sfac-239 | in the function(s) of s 239AA(3) |
| s 239AA(3)(b) | src:37886-37888 | encoded | sfac-239 | `s 239AA(3)(b) the person is treated as the person who makes the offer of the SDRs` |
| s 239AA(3)(c) | src:37889-37894 | encoded | sfac-239 | `s 239AA(3)(c) the person has the rights and duties under this Act of the issuer and of the person making the offer` |
| s 239AA(3)(c)(i) | src:37895-37896 | encoded | sfac-239 | in the function(s) of s 239AA(3)(c) |
| s 239AA(3)(c)(ii) | src:37897-37898 | encoded | sfac-239 | in the function(s) of s 239AA(3)(c) |
| s 239AA(4) | src:37899-37902 | encoded | sfac-239 | `s 239AA(4) the person is the issuer of the SDRs, section 239AA(3) prevailing over section 239` |
| s 239A marginal heading | src:37903-37904 | inert (reason 1) | sfac-239 | heading "Authority may disapply this Division to certain offers". |
| s 239A(1) | src:37905-37907 | encoded | sfac-239 | `s 239A(1) the Authority's declaration disapplies this Division to the offer` |
| s 239A(1)(a) | src:37908-37911 | encoded | sfac-239 | `s 239A(1) the Authority's declaration disapplies this Division to the offer`, `s 239A(1) and (2), s 239(8) and Subdivision (4): this Subdivision applies to the offer` |
| s 239A(1)(b) | src:37912-37919 | encoded | sfac-239 | `s 239A(1) the Authority's declaration disapplies this Division to the offer`, `s 239A(1) and (2), s 239(8) and Subdivision (4): this Subdivision applies to the offer` |
| s 239A(2) | src:37920-37923 | encoded | sfac-239 | `s 239A(2) this Division does not apply to the offer of units or derivatives of units in a business trust` |
| s 239A(2)(a) | src:37924-37930 | encoded | sfac-239 | in the function(s) of s 239A(2) |
| s 239A(2)(b) | src:37931-37936 | encoded | sfac-239 | in the function(s) of s 239A(2) |
| s 239B marginal heading | src:37937-37938 | inert (reason 2) | sfac-239 | s 239B (heading and text): the Authority's power to modify or adapt the provisions of this Division by regulations for prescribed offers; a regulation-making power, the effect of any regulation on an offer is not in this text. |
| s 239B | src:37939-37947 | inert (reason 2) | sfac-239 | s 239B (heading and text): the Authority's power to modify or adapt the provisions of this Division by regulations for prescribed offers; a regulation-making power, the effect of any regulation on an offer is not in this text. |
| heading: Subdivision (2) — Prospectus requirements | src:38374-38375 | inert (reason 1) | sfac-240 | Subdivision (2) heading and the marginal heading of s 240: not operative. |
| s 240 marginal heading | src:38376-38378 | inert (reason 1) | sfac-240 | Subdivision (2) heading and the marginal heading of s 240: not operative. |
| s 240(1) | src:38379-38381 | fork | sfac-240 | `s 240(1) the person must not make the offer`, `s 240(1) the person shall not make the offer without a registered prospectus` (fork F4 in NOTES.md); lines 38379-38379 of it are inert (reason 1) |
| s 240(1)(a) | src:38382-38384 | encoded | sfac-240 | in the function(s) of s 240(1) |
| s 240(1)(a)(i) | src:38385-38386 | encoded | sfac-240 | in the function(s) of s 240(1)(a) |
| s 240(1)(a)(ii) | src:38387-38390 | encoded | sfac-240 | in the function(s) of s 240(1)(a) |
| s 240(1)(a)(iii) | src:38391-38395 | encoded | sfac-240 | in the function(s) of s 240(1)(a) |
| s 240(1)(b) | src:38396-38400 | encoded | sfac-240 | in the function(s) of s 240(1) |
| s 240(2) | src:38401-38403 | encoded | sfac-240 | `s 240(2) the person is deemed to have lodged a prospectus with the Authority` |
| s 240(3) | src:38404-38407 | encoded | sfac-240 | `s 240(3) the preliminary document contains all the information it must contain` |
| s 240(4) | src:38408-38412 | fork | sfac-240 | `s 240(4) the offer may be made in or accompanied by a profile statement instead of a prospectus` (fork F5 in NOTES.md) |
| s 240(4)(a) | src:38413-38416 | encoded | sfac-240 | in the function(s) of s 240(4) |
| s 240(4)(b) | src:38417-38421 | encoded | sfac-240 | in the function(s) of s 240(4) |
| s 240(4)(c) | src:38422-38424 | encoded | sfac-240 | in the function(s) of s 240(4) |
| s 240(4)(d) | src:38425-38428 | encoded | sfac-240 | in the function(s) of s 240(4) |
| s 240(4)(e) | src:38429-38433 | encoded | sfac-240 | in the function(s) of s 240(4) |
| s 240(4A) | src:38434-38436 | encoded | sfac-240 | `s 240(4A) the copy lodged with the Authority has been signed as required` |
| s 240(4A)(a) | src:38437-38438 | encoded | sfac-240 | in the function(s) of s 240(4A) |
| s 240(4A)(a)(i) | src:38439-38448 | encoded | sfac-240 | in the function(s) of s 240(4A)(a) |
| s 240(4A)(a)(ii) | src:38449-38452 | encoded | sfac-240 | in the function(s) of s 240(4A)(a) |
| s 240(4A)(b) | src:38453-38455 | encoded | sfac-240 | in the function(s) of s 240(4A) |
| s 240(4A)(b)(i) | src:38456-38458 | encoded | sfac-240 | in the function(s) of s 240(4A)(b) |
| s 240(4A)(b)(i)(A) | src:38459-38460 | encoded | sfac-240 | in the function(s) of s 240(4A)(b)(i) |
| s 240(4A)(b)(i)(B) | src:38461-38468 | encoded | sfac-240 | in the function(s) of s 240(4A)(b)(i) |
| s 240(4A)(b)(ii) | src:38469-38471 | encoded | sfac-240 | in the function(s) of s 240(4A)(b) |
| s 240(4A)(c) | src:38472-38474 | encoded | sfac-240 | in the function(s) of s 240(4A) |
| s 240(4A)(c)(i) | src:38475-38477 | encoded | sfac-240 | in the function(s) of s 240(4A)(c) |
| s 240(4A)(c)(i)(A) | src:38478-38480 | encoded | sfac-240 | in the function(s) of s 240(4A)(c)(i) |
| s 240(4A)(c)(i)(B) | src:38481-38491 | encoded | sfac-240 | in the function(s) of s 240(4A)(c)(i) |
| s 240(4A)(c)(ii) | src:38492-38495 | encoded | sfac-240 | in the function(s) of s 240(4A)(c) |
| s 240(4A)(d) | src:38496-38498 | encoded | sfac-240 | in the function(s) of s 240(4A) |
| s 240(4A)(d)(i) | src:38499-38501 | encoded | sfac-240 | in the function(s) of s 240(4A)(d) |
| s 240(4A)(d)(i)(A) | src:38502-38505 | encoded | sfac-240 | in the function(s) of s 240(4A)(d)(i) |
| s 240(4A)(d)(i)(B) | src:38506-38513 | encoded | sfac-240 | in the function(s) of s 240(4A)(d)(i) |
| s 240(4A)(d)(ii) | src:38514-38518 | encoded | sfac-240 | in the function(s) of s 240(4A)(d) |
| s 240(4B) | src:38519-38522 | encoded | sfac-240 | `s 240(4B) the requirement for signature by a director or equivalent person is satisfied` |
| s 240(4B)(a) | src:38523-38524 | encoded | sfac-240 | in the function(s) of s 240(4B) |
| s 240(4B)(b) | src:38525-38527 | encoded | sfac-240 | in the function(s) of s 240(4B) |
| s 240(4C) | src:38528-38532 | encoded | sfac-240 | `s 240(4C) the requirement for signature by a proposed director or equivalent person is satisfied` |
| s 240(4C)(a) | src:38533-38534 | encoded | sfac-240 | in the function(s) of s 240(4C) |
| s 240(4C)(b) | src:38535-38540 | encoded | sfac-240 | in the function(s) of s 240(4C) |
| s 240(5) | src:38541-38546 | encoded | sfac-240 | `s 240(5) the person must not make the offer`, `s 240(5) the person shall not make an offer in respect of an entity or business trust not formed` |
| s 240(6) | src:38547-38548 | repealed or blank in this text | sfac-240 | s 240(6): "[Deleted by Act 1 of 2005]". |
| s 240(7) | src:38549-38555 | fork | sfac-240 | `s 240(7) the person is guilty of an offence`, `s 240(7) the penalty for the offence` (fork F6 in NOTES.md) |
| s 240(8) | src:38556-38559 | fork | sfac-240 | `s 240(8) the Authority may register the prospectus or profile statement on the day` (fork F9 in NOTES.md) |
| s 240(8)(a) | src:38560-38562 | encoded | sfac-240 | in the function(s) of s 240(8) |
| s 240(8)(b) | src:38563-38567 | encoded | sfac-240 | in the function(s) of s 240(8) |
| s 240(8)(b)(i) | src:38568-38569 | encoded | sfac-240 | in the function(s) of s 240(8)(b) |
| s 240(8)(b)(ii) | src:38570-38572 | encoded | sfac-240 | in the function(s) of s 240(8)(b) |
| s 240(8)(c) | src:38573-38579 | encoded | sfac-240 | in the function(s) of s 240(8) |
| s 240(8)(c)(i) | src:38580-38581 | encoded | sfac-240 | in the function(s) of s 240(8)(c) |
| s 240(8)(c)(ii) | src:38582-38584 | encoded | sfac-240 | in the function(s) of s 240(8)(c) |
| s 240(8)(d) | src:38585-38595 | encoded | sfac-240 | in the function(s) of s 240(8) |
| s 240(8A) | src:38596-38605 | fork | sfac-240 | `s 240(8A) the Authority may proceed with the registration on the date` (fork F7 in NOTES.md) |
| s 240(8B) | src:38606-38611 | inert (reason 2) | sfac-240 | s 240(8B): the Authority may prescribe the same or different periods and days for different offers; a rule-making power, the period it prescribes is an input of s 240(8) and s 240(8A). |
| s 240(9) | src:38612-38620 | encoded | sfac-240 | `s 240(9) the Authority must not register the prospectus` |
| s 240(9A) | src:38621-38628 | encoded | sfac-240 | `s 240(9A) the person may lodge an amendment on the day` |
| s 240(10) | src:38629-38630 | encoded | sfac-240 | `s 240(10) and (11) the date taken as the date of lodgment for the purposes of subsection (8)` |
| s 240(10)(a) | src:38631-38635 | encoded | sfac-240 | in the function(s) of s 240(10) |
| s 240(10)(b) | src:38636-38644 | encoded | sfac-240 | in the function(s) of s 240(10) |
| s 240(11) | src:38645-38650 | encoded | sfac-240 | `s 240(10) and (11) the date taken as the date of lodgment for the purposes of subsection (8)` |
| s 240(11A) | src:38651-38654 | encoded | sfac-240 | `s 240(11A) the amendment is treated as part of the original prospectus or profile statement` |
| s 240(12) | src:38655-38656 | encoded | sfac-240 | `s 240(12) the person making the offer must provide the Authority with a copy in the form or medium required`, `s 240(12) the person making the offer must provide the Authority with a copy for publication` |
| s 240(12)(a) | src:38657-38659 | encoded | sfac-240 | in the function(s) of s 240(12) |
| s 240(12)(b) | src:38660-38667 | encoded | sfac-240 | in the function(s) of s 240(12) |
| s 240(13) | src:38668-38669 | encoded | sfac-240 | `s 240(13) the Authority must refuse to register the prospectus` |
| s 240(13)(a) | src:38670-38672 | encoded | sfac-240 | in the function(s) of s 240(13) |
| s 240(13)(b) | src:38673-38676 | encoded | sfac-240 | in the function(s) of s 240(13) |
| s 240(13)(c) | src:38677-38679 | encoded | sfac-240 | in the function(s) of s 240(13) |
| s 240(13)(d) | src:38680-38682 | encoded | sfac-240 | in the function(s) of s 240(13) |
| s 240(13)(e) | src:38683-38690 | encoded | sfac-240 | in the function(s) of s 240(13) |
| s 240(13)(ea) | src:38691-38695 | encoded | sfac-240 | in the function(s) of s 240(13) |
| s 240(13)(eb) | src:38696-38700 | encoded | sfac-240 | in the function(s) of s 240(13) |
| s 240(13)(f) | src:38701-38703 | encoded | sfac-240 | in the function(s) of s 240(13) |
| s 240(14) | src:38704-38705 | encoded | sfac-240 | `s 240(14) the Authority must refuse to register the profile statement` |
| s 240(14)(a) | src:38706-38708 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(14)(b) | src:38709-38713 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(14)(c) | src:38714-38717 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(14)(ca) | src:38718-38722 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(14)(cb) | src:38723-38727 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(14)(cc) | src:38728-38732 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(14)(d) | src:38733-38738 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(14)(e) | src:38739-38740 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(14)(f) | src:38741-38743 | encoded | sfac-240 | in the function(s) of s 240(14) |
| s 240(15) | src:38744-38751 | encoded | sfac-240 | `s 240(15) the Authority must give the person making the offer an opportunity to be heard before refusing` |
| s 240(15)(a) | src:38752-38757 | encoded | sfac-240 | in the function(s) of s 240(15) |
| s 240(15)(b) | src:38758-38761 | encoded | sfac-240 | in the function(s) of s 240(15) |
| s 240(15)(c) | src:38762-38771 | encoded | sfac-240 | in the function(s) of s 240(15) |
| s 240(16) | src:38772-38777 | fork | sfac-240 | `s 240(16) the person making an offer may appeal to the Minister`, `s 240(16) the Minister's decision on the appeal is final` (fork F9 in NOTES.md) |
| s 240(17) | src:38778-38779 | fork | sfac-240 | `s 240(17) the person is guilty of an offence`, `s 240(17) the penalty for the offence`, `s 240(17) the person shall not accept an application or allot before registration` (fork F8 in NOTES.md) |
| s 240(17)(a) | src:38780-38786 | encoded | sfac-240 | in the function(s) of s 240(17) |
| s 240(17)(b) | src:38787-38797 | encoded | sfac-240 | in the function(s) of s 240(17) |
| s 240(17)(c) | src:38798-38800 | encoded | sfac-240 | in the function(s) of s 240(17) |
| s 240(17)(d) | src:38801-38804 | encoded | sfac-240 | in the function(s) of s 240(17) |
| s 240(17)(e) | src:38805-38815 | encoded | sfac-240 | in the function(s) of s 240(17) |
| s 240(18) | src:38816-38817 | encoded | sfac-240 | `s 240(18) this section yields to section 240A for the offer` |
| s 240(19) | src:38818-38822 | encoded | sfac-240 | `s 240(19) the information is a statement for the purposes of subsections (13)(a) and (14)(a)` |
| s 240(20) | src:38823-38826 | inert (reason 2) | sfac-240 | s 240(20): regulations made under this section may make a contravention an offence with penalties up to a fine of $50,000; a regulation-making power. |
| s 240AA marginal heading | src:38827-38828 | inert (reason 1) | sfac-240 | s 240AA marginal heading: not operative. |
| s 240AA(1) | src:38829-38838 | fork | sfac-240aa | `s 240AA(1) the person must not make the offer`, `s 240AA(1) the person shall not make the offer without a product highlights sheet` (fork F10 in NOTES.md) |
| s 240AA(1)(a) | src:38839-38841 | encoded | sfac-240aa | in the function(s) of s 240AA(1) |
| s 240AA(1)(b) | src:38842-38845 | encoded | sfac-240aa | in the function(s) of s 240AA(1) |
| s 240AA(2) | src:38846-38854 | fork | sfac-240aa | `s 240AA(2) the person must not publish or disseminate the document`, `s 240AA(2) the person shall not publish or disseminate the document` (fork F11 in NOTES.md) |
| s 240AA(2)(a) | src:38855-38857 | encoded | sfac-240aa | in the function(s) of s 240AA(2) |
| s 240AA(2)(b) | src:38858-38860 | encoded | sfac-240aa | in the function(s) of s 240AA(2) |
| s 240AA(2)(c) | src:38861-38865 | encoded | sfac-240aa | in the function(s) of s 240AA(2) |
| s 240AA(3) | src:38866-38867 | encoded | sfac-240aa | `s 240AA(3) the Authority may publish the document for public information` |
| s 240AA(3)(a) | src:38868-38870 | encoded | sfac-240aa | in the function(s) of s 240AA(3) |
| s 240AA(3)(b) | src:38871-38875 | encoded | sfac-240aa | in the function(s) of s 240AA(3) |
| s 240AA(4) | src:38876-38887 | fork | sfac-240aa | `s 240AA(4) the person is guilty of an offence`, `s 240AA(4) the penalty for the offence` (fork F12 in NOTES.md) |
| s 240AA(5) | src:38888-38889 | inert (reason 1) | sfac-240aa | s 240AA(5) opening words "In this section": the definitions are each encoded in their own function. |
| s 240AA(5) "asset-backed securities" | src:38890-38892 | encoded | sfac-240aa | `s 240AA(5) "asset-backed securities" the securities are asset-backed securities` |
| s 240AA(5) "relevant securities or securities-based derivatives contracts" | src:38893-38895 | encoded | sfac-240aa | `s 240AA(5) "relevant securities or securities-based derivatives contracts" the securities or contracts are relevant` |
| s 240AA(5) "relevant securities or securities-based derivatives contracts" (a) | src:38896-38897 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "relevant securities or securities-based derivatives contracts" |
| s 240AA(5) "relevant securities or securities-based derivatives contracts" (b) | src:38898-38899 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "relevant securities or securities-based derivatives contracts" |
| s 240AA(5) "relevant securities or securities-based derivatives contracts" (c) | src:38900-38903 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "relevant securities or securities-based derivatives contracts" |
| s 240AA(5) "single purpose vehicle" | src:38904-38907 | encoded | sfac-240aa | `s 240AA(5) "single purpose vehicle" the body is a single purpose vehicle` |
| s 240AA(5) "single purpose vehicle" (a) | src:38908-38912 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "single purpose vehicle" |
| s 240AA(5) "single purpose vehicle" (b) | src:38913-38914 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "single purpose vehicle" |
| s 240AA(5) "specified financial institution" | src:38915-38916 | encoded | sfac-240aa | `s 240AA(5) "specified financial institution" the body is a specified financial institution` |
| s 240AA(5) "specified financial institution" (a) | src:38917-38918 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "specified financial institution" |
| s 240AA(5) "specified financial institution" (b) | src:38919-38923 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "specified financial institution" |
| s 240AA(5) "structured notes" | src:38924-38926 | fork | sfac-240aa | `s 240AA(5) "structured notes" the debentures or units of debentures are structured notes` (fork F13 in NOTES.md) |
| s 240AA(5) "structured notes" (a) | src:38927-38928 | fork | sfac-240aa | `s 240AA(5) "structured notes" (a) the debentures are issued in relation to a transaction and by a specified financial institution` (fork F21 in NOTES.md) |
| s 240AA(5) "structured notes" (a)(i) | src:38929-38930 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (a) |
| s 240AA(5)(a)(i)(A) | src:38931-38932 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (a)(i) |
| s 240AA(5)(a)(i)(B) | src:38933-38939 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (a)(i) |
| s 240AA(5) "structured notes" (a)(ii) | src:38940-38941 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (a) |
| s 240AA(5) "structured notes" (b) | src:38942-38943 | encoded | sfac-240aa | `s 240AA(5) "structured notes" (b) the debentures carry a payment or delivery term` |
| s 240AA(5) "structured notes" (b)(i) | src:38944-38946 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (b) |
| s 240AA(5) "structured notes" (b)(ii) | src:38947-38950 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (b) |
| s 240AA(5) "structured notes" (b)(iii) | src:38951-38957 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (b) |
| s 240AA(5) "structured notes" (b)(iv) | src:38958-38960 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (b) |
| s 240AA(5) "structured notes" (b) (second one numbered alike) | src:38961-38963 | encoded | sfac-240aa | `s 240AA(5) "structured notes" in accordance with a formula based on one or more of the variables` |
| s 240AA(5) "structured notes" (b)(v) | src:38964-38970 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (b) (second one numbered alike) |
| s 240AA(5) "structured notes" (b)(vi) | src:38971-38973 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (b) (second one numbered alike) |
| s 240AA(5) "structured notes" (b)(vii) | src:38974-38976 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (b) (second one numbered alike) |
| s 240AA(5) "structured notes" (b)(viii) | src:38977-38980 | encoded | sfac-240aa | in the function(s) of s 240AA(5) "structured notes" (b) (second one numbered alike) |
| s 240AA(5) "synthetic securitisation transaction" | src:38981-38991 | encoded | sfac-240aa | `s 240AA(5) "synthetic securitisation transaction" the arrangement is a synthetic securitisation transaction` |
| s 240AB marginal heading | src:38992-38993 | inert (reason 1) | sfac-240aa | s 240AB marginal heading: not operative. |
| s 240AB(1) | src:38994-39000 | encoded | sfac-240aa | `s 240AB(1) and (2) the person is exempt from the requirements in section 240AA` |
| s 240AB(2) | src:39001-39007 | encoded | sfac-240aa | `s 240AB(1) and (2) the person is exempt from the requirements in section 240AA` |
| s 240AB(3) | src:39008-39012 | encoded | sfac-240aa | `s 240AB(3) the condition or restriction is in force` |
| s 240AB(4) | src:39013-39017 | encoded | sfac-240aa | `s 240AB(4) it is necessary to publish the exemption in the Gazette` |
| s 240AB(5) | src:39018-39026 | fork | sfac-240aa | `s 240AB(5) the person is guilty of an offence`, `s 240AB(5) the penalty for the offence`, `s 240AB(5) the person shall not contravene a condition or restriction` (fork F14 in NOTES.md) |
| s 240A marginal heading | src:39027-39028 | inert (reason 1) | sfac-240aa | s 240A marginal heading: not operative. |
| s 240A(1) | src:39029-39032 | encoded | sfac-240aa | `s 240A(1) the prospectus comprises what it must comprise` |
| s 240A(1)(a) | src:39033-39035 | encoded | sfac-240aa | in the function(s) of s 240A(1) |
| s 240A(1)(b) | src:39036-39040 | encoded | sfac-240aa | in the function(s) of s 240A(1) |
| s 240A(2) | src:39041-39044 | encoded | sfac-240aa | `s 240A(2) the profile statement comprises what it must comprise` |
| s 240A(2)(a) | src:39045-39048 | encoded | sfac-240aa | in the function(s) of s 240A(2) |
| s 240A(2)(b) | src:39049-39050 | encoded | sfac-240aa | in the function(s) of s 240A(2) |
| s 240A(3) | src:39051-39058 | encoded | sfac-240aa | `s 240A(3) the requirements of section 240(1)(a)(ii) and (iii) are satisfied for the offer` |
| s 240A(4) | src:39059-39066 | encoded | sfac-240aa | `s 240A(4) the requirements of section 240(4)(b) and (c) are satisfied for the offer` |
| s 240A(5) | src:39067-39072 | encoded | sfac-240aa | `s 240A(5) the base prospectus or base profile statement is treated as lodged with and registered by the Authority for the offer` |
| s 240A(6) | src:39073-39078 | encoded | sfac-240aa | `s 240A(6) a reference to a prospectus is read as a reference to both the base prospectus and the pricing statement` |
| s 240A(7) | src:39079-39088 | encoded | sfac-240aa | `s 240A(7) a reference to a profile statement is read as a reference to both the base profile statement and the pricing statement` |
| s 240A(8) | src:39089-39092 | inert (reason 2) | sfac-240aa | s 240A(8): the Authority may by regulations prescribe how the provisions of this Subdivision apply to an offer referred to in subsection (1) or (2); a regulation-making power, whatever it prescribes is not in this text. |
| s 240A(9) | src:39093-39095 | fork | sfac-240aa | `s 240A(9) the Authority may register the pricing statement on the day` (fork F15 in NOTES.md) |
| s 241 marginal heading | src:39096-39097 | inert (reason 1) | sfac-241 | s 241 marginal heading: not operative. |
| s 241(1) | src:39098-39102 | fork | sfac-241 | `s 241(1) the person making the offer may lodge a supplementary or replacement document` (fork F16 in NOTES.md) |
| s 241(1)(a) | src:39103-39105 | encoded | sfac-241 | in the function(s) of s 241(1) |
| s 241(1)(b) | src:39106-39111 | encoded | sfac-241 | in the function(s) of s 241(1) |
| s 241(1)(c) | src:39112-39113 | encoded | sfac-241 | in the function(s) of s 241(1) |
| s 241(1)(c)(i) | src:39114-39116 | encoded | sfac-241 | in the function(s) of s 241(1)(c) |
| s 241(1)(c)(ii) | src:39117-39118 | encoded | sfac-241 | in the function(s) of s 241(1)(c) |
| s 241(1)(c)(ii)(A) | src:39119-39120 | encoded | sfac-241 | in the function(s) of s 241(1)(c)(ii) |
| s 241(1)(c)(ii)(B) | src:39121-39123 | encoded | sfac-241 | in the function(s) of s 241(1)(c)(ii) |
| s 241(1)(c)(ii) (second one numbered alike) | src:39124-39138 | encoded | sfac-241 | in the function(s) of s 241(1)(c) |
| s 241(1A) | src:39139-39147 | fork | sfac-241 | `s 241(1A) the person making the offer may lodge a supplementary or replacement document for a base prospectus or base profile statement` (fork F17 in NOTES.md) |
| s 241(1B) | src:39148-39150 | encoded | sfac-241 | `s 241(1B) subsections (7) to (16) apply to the document` |
| s 241(1C) | src:39151-39153 | encoded | sfac-241 | `s 241(1C) the offer is not treated as subsisting` |
| s 241(1C)(a) | src:39154-39157 | encoded | sfac-241 | in the function(s) of s 241(1C) |
| s 241(1C)(b) | src:39158-39161 | encoded | sfac-241 | in the function(s) of s 241(1C) |
| s 241(1C)(b)(i) | src:39162-39165 | encoded | sfac-241 | in the function(s) of s 241(1C)(b) |
| s 241(1C)(b)(ii) | src:39166-39169 | encoded | sfac-241 | in the function(s) of s 241(1C)(b) |
| s 241(1C)(b)(ii)(A) | src:39170-39174 | encoded | sfac-241 | in the function(s) of s 241(1C)(b)(ii) |
| s 241(1C)(b)(ii)(B) | src:39175-39182 | encoded | sfac-241 | in the function(s) of s 241(1C)(b)(ii) |
| s 241(2) | src:39183-39185 | encoded | sfac-241 | `s 241(2) the supplementary document begins as it must` |
| s 241(2)(a) | src:39186-39188 | encoded | sfac-241 | in the function(s) of s 241(2) |
| s 241(2)(b) | src:39189-39191 | encoded | sfac-241 | in the function(s) of s 241(2) |
| s 241(2)(c) | src:39192-39194 | encoded | sfac-241 | in the function(s) of s 241(2) |
| s 241(2)(d) | src:39195-39198 | encoded | sfac-241 | in the function(s) of s 241(2) |
| s 241(3) | src:39199-39200 | encoded | sfac-241 | `s 241(3) the replacement document begins as it must` |
| s 241(3)(a) | src:39201-39203 | encoded | sfac-241 | in the function(s) of s 241(3) |
| s 241(3)(b) | src:39204-39206 | encoded | sfac-241 | in the function(s) of s 241(3) |
| s 241(4) | src:39207-39210 | encoded | sfac-241 | `s 241(4) the document is dated with the date on which it is lodged` |
| s 241(5) | src:39211-39212 | encoded | sfac-241 | `s 241(5) the person making the offer has taken the reasonable steps` |
| s 241(5)(a) | src:39213-39216 | encoded | sfac-241 | in the function(s) of s 241(5) |
| s 241(5)(b) | src:39217-39219 | encoded | sfac-241 | in the function(s) of s 241(5) |
| s 241(6) | src:39220-39222 | encoded | sfac-241 | `s 241(6)(a) the prospectus in relation to the offer is taken to be the original prospectus with the supplementary prospectus and any previous one` |
| s 241(6)(a) | src:39223-39231 | encoded | sfac-241 | in the function(s) of s 241(6) |
| s 241(6)(b) | src:39232-39237 | encoded | sfac-241 | `s 241(6)(b) the profile statement in relation to the offer is taken to be the original profile statement with the supplementary profile statement and any previous one` |
| s 241(6A) | src:39238-39239 | repealed or blank in this text | sfac-241 | s 241(6A): "[Deleted by Act 1 of 2005]". |
| s 241(6B) | src:39240-39242 | encoded | sfac-241 | `s 241(6B)(a) the prospectus in relation to the offer is taken to be the replacement prospectus` |
| s 241(6B)(a) | src:39243-39246 | encoded | sfac-241 | in the function(s) of s 241(6B) |
| s 241(6B)(b) | src:39247-39250 | encoded | sfac-241 | `s 241(6B)(b) the profile statement in relation to the offer is taken to be the replacement profile statement` |
| s 241(7) | src:39251-39255 | encoded | sfac-241 | `s 241(7) the offer has been kept open for at least 14 days after the lodgment` |
| s 241(8) | src:39256-39260 | encoded | sfac-241 | `s 241(8)(a) the person making the offer is bound by paragraph (a)`, `s 241(8)(b) the person making the offer is bound by paragraph (b)` |
| s 241(8)(a) | src:39261-39264 | encoded | sfac-241 | `s 241(8)(a) the person making the offer is bound by paragraph (a)`, `s 241(8)(a) the person making the offer has met one of the routes` |
| s 241(8)(a)(i) | src:39265-39266 | encoded | sfac-241 | `s 241(8)(a)(i) the person making the offer has given written notice with an option to withdraw their applications and made the document available` |
| s 241(8)(a)(i)(A) | src:39267-39280 | encoded | sfac-241 | in the function(s) of s 241(8)(a)(i) |
| s 241(8)(a)(i)(B) | src:39281-39289 | encoded | sfac-241 | in the function(s) of s 241(8)(a)(i) |
| s 241(8)(a)(ii) | src:39290-39296 | encoded | sfac-241 | `s 241(8)(a)(ii) the person making the offer has given the document with an option to withdraw their applications` |
| s 241(8)(a)(iii) | src:39297-39298 | encoded | sfac-241 | `s 241(8)(a)(iii) the person making the offer has treated the applications as withdrawn and cancelled and paid all moneys` |
| s 241(8)(a)(iii)(A) | src:39299-39303 | encoded | sfac-241 | `s 241(8)(a)(iii)(A) the applications are deemed to have been withdrawn and cancelled` |
| s 241(8)(a)(iii)(B) | src:39304-39310 | encoded | sfac-241 | in the function(s) of s 241(8)(a)(iii) |
| s 241(8)(b) | src:39311-39314 | encoded | sfac-241 | `s 241(8)(b) the person making the offer is bound by paragraph (b)`, `s 241(8)(b) the person making the offer has met one of the routes` |
| s 241(8)(b)(i) | src:39315-39316 | encoded | sfac-241 | `s 241(8)(b)(i) the person making the offer has given written notice with an option to return those securities or securities-based derivatives contracts and made the document available` |
| s 241(8)(b)(i)(A) | src:39317-39332 | encoded | sfac-241 | in the function(s) of s 241(8)(b)(i) |
| s 241(8)(b)(i)(B) | src:39333-39341 | encoded | sfac-241 | in the function(s) of s 241(8)(b)(i) |
| s 241(8)(b)(ii) | src:39342-39350 | encoded | sfac-241 | `s 241(8)(b)(ii) the person making the offer has given the document with an option to return those securities or securities-based derivatives contracts` |
| s 241(8)(b)(iii) | src:39351-39352 | encoded | sfac-241 | `s 241(8)(b)(iii) the person making the offer has treated the issue as void and paid all moneys` |
| s 241(8)(b)(iii)(A) | src:39353-39356 | encoded | sfac-241 | `s 241(8)(b)(iii)(A) the issue is deemed void` |
| s 241(8)(b)(iii)(B) | src:39357-39364 | encoded | sfac-241 | in the function(s) of s 241(8)(b)(iii) |
| s 241(9) | src:39365-39370 | encoded | sfac-241 | `s 241(9) the provision has effect despite sections 76 and 76A and Division 3A of Part 4 of the Companies Act 1967` |
| s 241(10) | src:39371-39381 | encoded | sfac-241, sfac-duties | `s 241(10) the applicant has notified the person making the offer within 14 days`, `s 241(10) the person making the offer has paid the applicant within 7 days from the receipt of the notification`, `s 241(10) the person making the offer must pay the applicant within 7 days from the receipt of the notification` |
| s 241(11) | src:39382-39397 | encoded | sfac-241, sfac-duties | `s 241(11) the applicant has notified the person making the offer and returned the documents within 14 days`, `s 241(11) the person making the offer has paid the applicant within 7 days from the receipt of the notification and documents`, `s 241(11) the issue of the securities or contracts is deemed to be void`, `s 241(11) the person making the offer must pay the applicant within 7 days from the receipt of the notification and documents` |
| s 241(12) | src:39398-39402 | encoded | sfac-241 | `s 241(12)(a) the person making the offer is bound by paragraph (a)`, `s 241(12)(b) the person making the offer is bound by paragraph (b)` |
| s 241(12)(a) | src:39403-39406 | encoded | sfac-241 | `s 241(12)(a) the person making the offer is bound by paragraph (a)`, `s 241(12)(a) the person making the offer has met one of the routes` |
| s 241(12)(a)(i) | src:39407-39408 | encoded | sfac-241 | `s 241(12)(a)(i) the person making the offer has given written notice with an option to withdraw their applications and made the document available` |
| s 241(12)(a)(i)(A) | src:39409-39422 | encoded | sfac-241 | in the function(s) of s 241(12)(a)(i) |
| s 241(12)(a)(i)(B) | src:39423-39431 | encoded | sfac-241 | in the function(s) of s 241(12)(a)(i) |
| s 241(12)(a)(ii) | src:39432-39438 | encoded | sfac-241 | `s 241(12)(a)(ii) the person making the offer has given the document with an option to withdraw their applications` |
| s 241(12)(a)(iii) | src:39439-39440 | encoded | sfac-241 | `s 241(12)(a)(iii) the person making the offer has treated the applications as withdrawn and cancelled and paid all moneys` |
| s 241(12)(a)(iii)(A) | src:39441-39445 | encoded | sfac-241 | `s 241(12)(a)(iii)(A) the applications are deemed to have been withdrawn and cancelled` |
| s 241(12)(a)(iii)(B) | src:39446-39452 | encoded | sfac-241 | in the function(s) of s 241(12)(a)(iii) |
| s 241(12)(b) | src:39453-39456 | encoded | sfac-241 | `s 241(12)(b) the person making the offer is bound by paragraph (b)`, `s 241(12)(b) the person making the offer has met one of the routes` |
| s 241(12)(b)(i) | src:39457-39458 | encoded | sfac-241 | `s 241(12)(b)(i) the person making the offer has given written notice with an option to return those securities or securities-based derivatives contracts and made the document available` |
| s 241(12)(b)(i)(A) | src:39459-39474 | encoded | sfac-241 | in the function(s) of s 241(12)(b)(i) |
| s 241(12)(b)(i)(B) | src:39475-39483 | encoded | sfac-241 | in the function(s) of s 241(12)(b)(i) |
| s 241(12)(b)(ii) | src:39484-39492 | encoded | sfac-241 | `s 241(12)(b)(ii) the person making the offer has given the document with an option to return those securities or securities-based derivatives contracts` |
| s 241(12)(b)(iii) | src:39493-39496 | encoded | sfac-241 | `s 241(12)(b)(iii) the person making the offer has treated the sale as void and paid all moneys`, `s 241(12)(b)(iii) the sale is deemed void` |
| s 241(12)(b)(iii)(A) | src:39497-39502 | encoded | sfac-241 | `s 241(12)(b)(iii) the person making the offer has treated the sale as void and paid all moneys` |
| s 241(12)(b)(iii)(AA) | src:39503-39516 | encoded | sfac-241 | `s 241(12)(b)(iii) the person making the offer has treated the sale as void and paid all moneys` |
| s 241(12)(b)(iii)(AB) | src:39517-39525 | encoded | sfac-241 | `s 241(12)(b)(iii) the person making the offer has treated the sale as void and paid all moneys` |
| s 241(12)(b)(iii)(B) | src:39526-39534 | encoded | sfac-241 | `s 241(12)(b)(iii) the person making the offer has treated the sale as void and paid all moneys` |
| s 241(13) | src:39535-39545 | encoded | sfac-241, sfac-duties | `s 241(13) the applicant has notified the person making the offer within 14 days`, `s 241(13) the person making the offer has paid the applicant within 7 days of the receipt of the notification`, `s 241(13) the person making the offer must pay the applicant within 7 days of the receipt of the notification` |
| s 241(14) | src:39546-39564 | encoded | sfac-241, sfac-duties | `s 241(14) the applicant has notified the person making the offer and returned the documents within 14 days`, `s 241(14) the person making the offer has paid the applicant within 7 days from the receipt of the notification and documents`, `s 241(14) the sale of the securities or contracts is deemed to be void`, `s 241(14) the person making the offer must pay the applicant within 7 days from the receipt of the notification and documents` |
| s 241(15) | src:39565-39570 | fork | sfac-241 | `s 241(15) the person is guilty of an offence`, `s 241(15) the penalty for the offence` (fork F19 in NOTES.md) |
| s 241(16) | src:39571-39576 | fork | sfac-241 | `s 241(16) the person is guilty of an offence`, `s 241(16) the penalty for the offence` (fork F20 in NOTES.md) |
| s 241(17) | src:39577-39580 | encoded | sfac-241 | `s 241(17) the information presented is a statement for the purposes of subsection (1)(a)` |
| s 242 marginal heading | src:39581-39582 | inert (reason 1) | sfac-242 | s 242 marginal heading: not operative. |
| s 242(1) | src:39583-39584 | fork | sfac-242 | `s 242(1) the Authority may serve a stop order on the person making the offer for the prospectus` (fork F22 in NOTES.md) |
| s 242(1)(a) | src:39585-39587 | encoded | sfac-242 | in the function(s) of s 242(1) |
| s 242(1)(b) | src:39588-39591 | encoded | sfac-242 | in the function(s) of s 242(1) |
| s 242(1)(c) | src:39592-39594 | encoded | sfac-242 | in the function(s) of s 242(1) |
| s 242(1)(d) | src:39595-39609 | encoded | sfac-242 | `s 242(1) the Authority may serve a stop order on the person making the offer for the prospectus`, `s 242(11) the person making the offer shall not allot, issue or sell contrary to the order` |
| s 242(2) | src:39610-39611 | fork | sfac-242 | `s 242(2) the Authority may serve a stop order on the person making the offer for the profile statement` (fork F22 in NOTES.md) |
| s 242(2)(a) | src:39612-39614 | encoded | sfac-242 | in the function(s) of s 242(2) |
| s 242(2)(b) | src:39615-39618 | encoded | sfac-242 | in the function(s) of s 242(2) |
| s 242(2)(c) | src:39619-39621 | encoded | sfac-242 | in the function(s) of s 242(2) |
| s 242(2)(d) | src:39622-39632 | encoded | sfac-242 | in the function(s) of s 242(2) |
| s 242(3) | src:39633-39640 | fork | sfac-242 | `s 242(3) the Authority must not serve a stop order` (fork F23 in NOTES.md) |
| s 242(4) | src:39641-39646 | encoded | sfac-242 | `s 242(4) the Authority must give the person making the offer an opportunity to be heard` |
| s 242(4)(a) | src:39647-39655 | encoded | sfac-242 | in the function(s) of s 242(4) |
| s 242(4)(aa) | src:39656-39659 | encoded | sfac-242 | in the function(s) of s 242(4) |
| s 242(4)(b) | src:39660-39663 | encoded | sfac-242 | in the function(s) of s 242(4) |
| s 242(4)(b)(i) | src:39664-39667 | encoded | sfac-242 | in the function(s) of s 242(4)(b) |
| s 242(4)(b)(ii) | src:39668-39670 | encoded | sfac-242 | in the function(s) of s 242(4)(b) |
| s 242(4)(b)(iii) | src:39671-39674 | encoded | sfac-242 | in the function(s) of s 242(4)(b) |
| s 242(5) | src:39675-39679 | encoded | sfac-242 | `s 242(5)(a) the person making the offer is bound by paragraph (a)` |
| s 242(5)(a) | src:39680-39682 | encoded | sfac-242 | in the function(s) of s 242(5) |
| s 242(5)(a)(i) | src:39683-39685 | encoded | sfac-242 | `s 242(5)(a)(i) the applications are deemed to have been withdrawn and cancelled` |
| s 242(5)(a)(ii) | src:39686-39691 | encoded | sfac-242, sfac-duties | `s 242(5)(a)(ii) the person making the offer has paid the applicants within 14 days from the date of the stop order`, `s 242(5)(a)(ii) the person making the offer must pay the applicants within 14 days from the date of the stop order (applications)` |
| s 242(5)(b) | src:39692-39694 | encoded | sfac-242 | `s 242(5)(b) the person making the offer is bound by paragraph (b)` |
| s 242(5)(b)(i) | src:39695-39697 | encoded | sfac-242 | `s 242(5)(b)(i) the issue of the securities or contracts is deemed to be void` |
| s 242(5)(b)(ii) | src:39698-39708 | encoded | sfac-242, sfac-duties | `s 242(5)(b)(ii) the person making the offer has paid the applicants within 14 days from the date of the stop order`, `s 242(5)(b)(ii) the person making the offer must pay the applicants within 14 days from the date of the stop order (issue)` |
| s 242(6) | src:39709-39711 | encoded | sfac-242 | `s 242(6) the provision has effect despite sections 76 and 76A and Division 3A of Part 4 of the Companies Act 1967` |
| s 242(7) | src:39712-39715 | encoded | sfac-242 | `s 242(7)(a) the person making the offer is bound by paragraph (a)` |
| s 242(7)(a) | src:39716-39718 | encoded | sfac-242 | in the function(s) of s 242(7) |
| s 242(7)(a)(i) | src:39719-39721 | encoded | sfac-242 | `s 242(7)(a)(i) the applications are deemed to have been withdrawn and cancelled` |
| s 242(7)(a)(ii) | src:39722-39727 | encoded | sfac-242, sfac-duties | `s 242(7)(a)(ii) the person making the offer has paid the applicants within 14 days from the date of the stop order`, `s 242(7)(a)(ii) the person making the offer must pay the applicants within 14 days from the date of the stop order (sale)` |
| s 242(7)(b) | src:39728-39732 | encoded | sfac-242 | `s 242(7)(b) the person making the offer is bound by paragraph (b)`, `s 242(7)(b) the sale is deemed to be void` |
| s 242(7)(b)(i) | src:39733-39736 | encoded | sfac-242 | `s 242(7)(b)(i) the person making the offer has informed the applicants and paid them, where title documents were issued` |
| s 242(7)(b)(i)(A) | src:39737-39741 | encoded | sfac-242 | in the function(s) of s 242(7)(b)(i) |
| s 242(7)(b)(i)(B) | src:39742-39750 | encoded | sfac-242 | in the function(s) of s 242(7)(b)(i) |
| s 242(7)(b)(ii) | src:39751-39758 | encoded | sfac-242, sfac-duties | `s 242(7)(b)(ii) the person making the offer has paid the applicants within 7 days, where no title documents were issued`, `s 242(7)(b)(ii) the person making the offer must pay the applicants within 7 days from the date of the stop order where no title documents were issued` |
| s 242(8) | src:39759-39768 | fork | sfac-242 | `s 242(8) the Authority may serve an interim stop order without giving an opportunity to be heard` (fork F22 in NOTES.md) |
| s 242(9) | src:39769-39771 | fork | sfac-242 | `s 242(9) the interim stop order is in force` (fork F24 in NOTES.md) |
| s 242(9)(a) | src:39772-39773 | encoded | sfac-242 | in the function(s) of s 242(9) |
| s 242(9)(a)(i) | src:39774-39775 | encoded | sfac-242 | in the function(s) of s 242(9)(a) |
| s 242(9)(a)(ii) | src:39776-39778 | encoded | sfac-242 | in the function(s) of s 242(9)(a) |
| s 242(9)(a) (second one numbered alike) | src:39779-39781 | encoded | sfac-242 | in the function(s) of s 242(9) |
| s 242(9)(b) | src:39782-39784 | encoded | sfac-242 | in the function(s) of s 242(9) |
| s 242(10) | src:39785-39787 | encoded | sfac-242 | `s 242(10) subsections (5) and (7) apply` |
| s 242(11) | src:39788-39795 | fork | sfac-242 | `s 242(11) the person is guilty of an offence`, `s 242(11) the penalty for the offence` (fork F25 in NOTES.md) |
| s 242(12) | src:39796-39805 | fork | sfac-242 | `s 242(12) the person is guilty of an offence`, `s 242(12) the penalty for the offence` (fork F26 in NOTES.md) |
| s 242(13) | src:39806-39810 | encoded | sfac-242 | `s 242(13) the information presented is a statement for the purposes of subsections (1)(a) and (2)(a)` |
| s 243 marginal heading | src:39811-39812 | inert (reason 1) | sfac-243 | s 243 marginal heading: not operative. |
| s 243(1) | src:39813-39815 | encoded | sfac-243 | `s 243(1) the prospectus contains what it must contain` |
| s 243(1)(a) | src:39816-39819 | encoded | sfac-243 | in the function(s) of s 243(1) |
| s 243(1)(b) | src:39820-39823 | encoded | sfac-243 | in the function(s) of s 243(1) |
| s 243(2) | src:39824-39826 | encoded | sfac-243 | `s 243(2) the item of information must be contained in the prospectus` |
| s 243(2)(a) | src:39827-39830 | encoded | sfac-243 | in the function(s) of s 243(2) |
| s 243(2)(b) | src:39831-39833 | encoded | sfac-243 | in the function(s) of s 243(2) |
| s 243(2)(b)(i) | src:39834-39835 | encoded | sfac-243 | in the function(s) of s 243(2)(b) |
| s 243(2)(b)(ii) | src:39836-39838 | encoded | sfac-243 | in the function(s) of s 243(2)(b) |
| s 243(3) | src:39839-39840 | encoded | sfac-243 | `s 243(3)(a) the rights and liabilities attaching to the securities or contracts are a matter the information must relate to` |
| s 243(3)(a) | src:39841-39843 | encoded | sfac-243 | in the function(s) of s 243(3) |
| s 243(3)(b) | src:39844-39852 | encoded | sfac-243 | `s 243(3)(b) the issuer's assets and liabilities, profits and losses, financial position and performance, and prospects are a matter the information must relate to` |
| s 243(3)(c) | src:39853-39854 | encoded | sfac-243 | `s 243(3)(c) the underlying entity's assets and liabilities, profits and losses, financial position and performance, and prospects are a matter the information must relate to` |
| s 243(3)(c)(i) | src:39855-39856 | encoded | sfac-243 | in the function(s) of s 243(3)(c) |
| s 243(3)(c)(ii) | src:39857-39859 | encoded | sfac-243 | in the function(s) of s 243(3)(c) |
| s 243(3)(c)(iii) | src:39860-39862 | encoded | sfac-243 | in the function(s) of s 243(3)(c) |
| s 243(3)(c) (second one numbered alike) | src:39863-39865 | encoded | sfac-243 | `s 243(3)(c) the underlying entity's assets and liabilities, profits and losses, financial position and performance, and prospects are a matter the information must relate to` |
| s 243(3)(d) | src:39866-39868 | encoded | sfac-243 | `s 243(3)(d) the capacity of the person or entity to issue or deliver the units, or to meet its obligations, is a matter the information must relate to` |
| s 243(3)(d)(i) | src:39869-39873 | encoded | sfac-243 | in the function(s) of s 243(3)(d) |
| s 243(3)(d)(ii) | src:39874-39878 | encoded | sfac-243 | in the function(s) of s 243(3)(d) |
| s 243(3)(d)(ii)(A) | src:39879-39880 | encoded | sfac-243 | in the function(s) of s 243(3)(d)(ii) |
| s 243(3)(d)(ii)(B) | src:39881-39883 | encoded | sfac-243 | in the function(s) of s 243(3)(d)(ii) |
| s 243(3)(d)(ii)(C) | src:39884-39886 | encoded | sfac-243 | in the function(s) of s 243(3)(d)(ii) |
| s 243(3)(d) (second one numbered alike) | src:39887-39890 | encoded | sfac-243 | `s 243(3)(d) the capacity of the person or entity to issue or deliver the units, or to meet its obligations, is a matter the information must relate to` |
| s 243(3)(e) | src:39891-39894 | encoded | sfac-243 | `s 243(3)(e) the business trust's and the trustee-manager's assets and liabilities, profits and losses, financial position and performance, and the prospects of the business trust, are a matter the information must relate to` |
| s 243(3)(e)(i) | src:39895-39900 | encoded | sfac-243 | in the function(s) of s 243(3)(e) |
| s 243(3)(e)(ii) | src:39901-39903 | encoded | sfac-243 | in the function(s) of s 243(3)(e) |
| s 243(3)(e)(ii)(A) | src:39904-39905 | encoded | sfac-243 | in the function(s) of s 243(3)(e)(ii) |
| s 243(3)(e)(ii)(B) | src:39906-39908 | encoded | sfac-243 | in the function(s) of s 243(3)(e)(ii) |
| s 243(3)(e)(ii)(C) | src:39909-39911 | encoded | sfac-243 | in the function(s) of s 243(3)(e)(ii) |
| s 243(3)(e) (second one numbered alike) | src:39912-39915 | encoded | sfac-243 | `s 243(3)(e) the business trust's and the trustee-manager's assets and liabilities, profits and losses, financial position and performance, and the prospects of the business trust, are a matter the information must relate to` |
| s 243(3)(f) | src:39916-39920 | encoded | sfac-243 | `s 243(3)(f) the assets and liabilities, profits and losses, financial position and performance, and prospects of the issuing entity are a matter the information must relate to` |
| s 243(3)(f)(i) | src:39921-39922 | encoded | sfac-243 | in the function(s) of s 243(3)(f) |
| s 243(3)(f)(ii) | src:39923-39924 | encoded | sfac-243 | in the function(s) of s 243(3)(f) |
| s 243(3)(f)(ii)(A) | src:39925-39926 | encoded | sfac-243 | in the function(s) of s 243(3)(f)(ii) |
| s 243(3)(f)(ii)(B) | src:39927-39929 | encoded | sfac-243 | in the function(s) of s 243(3)(f)(ii) |
| s 243(3)(f)(ii)(C) | src:39930-39932 | encoded | sfac-243 | in the function(s) of s 243(3)(f)(ii) |
| s 243(3)(f) (second one numbered alike) | src:39933-39935 | encoded | sfac-243 | `s 243(3)(f) the assets and liabilities, profits and losses, financial position and performance, and prospects of the issuing entity are a matter the information must relate to` |
| s 243(3)(g) | src:39936-39939 | encoded | sfac-243 | `s 243(3)(g) the capacity of the person or entity to issue or deliver the units or derivatives of units, or to meet its obligations, is a matter the information must relate to` |
| s 243(3)(g)(i) | src:39940-39944 | encoded | sfac-243 | in the function(s) of s 243(3)(g) |
| s 243(3)(g)(ii) | src:39945-39954 | encoded | sfac-243 | in the function(s) of s 243(3)(g) |
| s 243(3)(g)(ii)(A) | src:39955-39956 | encoded | sfac-243 | in the function(s) of s 243(3)(g)(ii) |
| s 243(3)(g)(ii)(B) | src:39957-39959 | encoded | sfac-243 | in the function(s) of s 243(3)(g)(ii) |
| s 243(3)(g)(ii)(C) | src:39960-39962 | encoded | sfac-243 | in the function(s) of s 243(3)(g)(ii) |
| s 243(3)(g) (second one numbered alike) | src:39963-39969 | encoded | sfac-243 | `s 243(3)(g) the capacity of the person or entity to issue or deliver the units or derivatives of units, or to meet its obligations, is a matter the information must relate to` |
| s 243(4) | src:39970-39972 | encoded | sfac-243 | `s 243(4) regard has been had to the matters` |
| s 243(4)(a) | src:39973-39975 | encoded | sfac-243 | in the function(s) of s 243(4) |
| s 243(4)(b) | src:39976-39978 | encoded | sfac-243 | in the function(s) of s 243(4) |
| s 243(4)(c) | src:39979-39983 | encoded | sfac-243 | in the function(s) of s 243(4) |
| s 243(4A) | src:39984-39991 | encoded | sfac-243 | `s 243(4A) the information may be incorporated in the prospectus by reference to the reference document` |
| s 243(4B) | src:39992-39996 | encoded | sfac-243 | `s 243(4B) the information is part of the prospectus` |
| s 243(5) | src:39997-39999 | encoded | sfac-243 | `s 243(5) the person's knowledge is relevant` |
| s 243(5)(a) | src:40000-40004 | encoded | sfac-243 | in the function(s) of s 243(5) |
| s 243(5)(b) | src:40005-40007 | encoded | sfac-243 | in the function(s) of s 243(5) |
| s 243(5)(c) | src:40008-40009 | encoded | sfac-243 | in the function(s) of s 243(5) |
| s 243(5)(d) | src:40010-40012 | encoded | sfac-243 | in the function(s) of s 243(5) |
| s 243(5)(da) | src:40013-40015 | encoded | sfac-243 | in the function(s) of s 243(5) |
| s 243(5)(e) | src:40016-40019 | encoded | sfac-243 | in the function(s) of s 243(5) |
| s 243(5)(f) | src:40020-40022 | encoded | sfac-243 | in the function(s) of s 243(5) |
| s 243(5)(f)(i) | src:40023-40024 | encoded | sfac-243 | in the function(s) of s 243(5)(f) |
| s 243(5)(f)(ii) | src:40025-40027 | encoded | sfac-243 | in the function(s) of s 243(5)(f) |
| s 243(5)(g) | src:40028-40031 | encoded | sfac-243 | in the function(s) of s 243(5) |
| s 243(6) | src:40032-40039 | encoded | sfac-243 | `s 243(6) the condition is void` |
| s 243(7) | src:40040-40042 | encoded | sfac-243 | `s 243(7) this section affects the liability` |
| s 243(8) | src:40043-40054 | encoded | sfac-243 | `s 243(8) "assets and liabilities, profits and losses, financial position and performance" the figures are those of the business trust` |
| s 243(8) "prospects" | src:40055-40061 | encoded | sfac-243 | `s 243(8) "prospects" the prospects are those of the business trust` |
| s 244 | src:40062-40063 | repealed or blank in this text | sfac-243 | s 244: "[Repealed by Act 16 of 2003]". |
| s 245 marginal heading | src:40064-40066 | inert (reason 1) | sfac-243 | s 245 marginal heading: not operative. |
| s 245(1) | src:40067-40070 | fork | sfac-243 | `s 245(1) the entity must not accept or retain the subscriptions`, `s 245(1) the entity shall not accept or retain over-subscriptions` (fork F27 in NOTES.md) |
| s 245(1)(a) | src:40071-40073 | encoded | sfac-243 | in the function(s) of s 245(1) |
| s 245(1)(b) | src:40074-40078 | encoded | sfac-243 | in the function(s) of s 245(1) |
| s 245(2) | src:40079-40083 | encoded | sfac-243 | `s 245(2)(a) the entity must not make, authorise or permit the statement of asset-backing`, `s 245(2)(a) the entity shall not make, authorise or permit a statement of asset-backing` |
| s 245(2)(a) | src:40084-40090 | fork | sfac-243 | in the function(s) of s 245(2) (fork F28 in NOTES.md) |
| s 245(2)(b) | src:40091-40095 | encoded | sfac-243 | `s 245(2)(b) the prospectus contains the statement of total assets and total liabilities` |
| s 245(3) | src:40096-40105 | fork | sfac-243 | `s 245(3) the person is guilty of an offence`, `s 245(3) the penalty for the offence` (fork F29 in NOTES.md) |
| s 246 marginal heading | src:40106-40107 | inert (reason 1) | sfac-243 | s 246 marginal heading: not operative. |
| s 246(1) | src:40108-40110 | encoded | sfac-243 | `s 246(1) the profile statement contains what it must contain` |
| s 246(1)(a) | src:40111-40112 | encoded | sfac-243 | in the function(s) of s 246(1) |
| s 246(1)(a)(i) | src:40113-40114 | encoded | sfac-243 | in the function(s) of s 246(1)(a) |
| s 246(1)(ia) | src:40115-40118 | encoded | sfac-243 | in the function(s) of s 246(1) |
| s 246(1)(ib) | src:40119-40124 | encoded | sfac-243 | in the function(s) of s 246(1) |
| s 246(1)(ib)(ii) | src:40125-40127 | encoded | sfac-243 | in the function(s) of s 246(1)(ib) |
| s 246(1)(ib)(iii) | src:40128-40130 | encoded | sfac-243 | in the function(s) of s 246(1)(ib) |
| s 246(1)(ib)(iv) | src:40131-40133 | encoded | sfac-243 | in the function(s) of s 246(1)(ib) |
| s 246(1)(ib)(v) | src:40134-40138 | encoded | sfac-243 | in the function(s) of s 246(1)(ib) |
| s 246(1)(b) | src:40139-40142 | encoded | sfac-243 | in the function(s) of s 246(1) |
| s 246(1)(c) | src:40143-40152 | encoded | sfac-243 | in the function(s) of s 246(1) |
| s 246(2) | src:40153-40154 | fork | sfac-243 | `s 246(2) the profile statement contains something it must not contain` (fork F30 in NOTES.md) |
| s 246(2)(a) | src:40155-40157 | encoded | sfac-243 | in the function(s) of s 246(2) |
| s 246(2)(b) | src:40158-40160 | encoded | sfac-243 | in the function(s) of s 246(2) |
| s 246(2)(c) | src:40161-40163 | encoded | sfac-243 | in the function(s) of s 246(2) |
| s 246(3) | src:40164-40167 | encoded | sfac-243 | `s 246(3) the information presented is a statement for the purposes of subsection (2)(a)` |
| s 247 marginal heading | src:40168-40170 | inert (reason 1) | sfac-243 | s 247 marginal heading: not operative. |
| s 247(1) | src:40171-40175 | encoded | sfac-243 | `s 247(1) and (3) the person or document is exempt from the requirement of form or content` |
| s 247(2) | src:40176-40178 | encoded | sfac-243 | `s 247(2) the Authority is barred from granting the exemption under subsection (1)` |
| s 247(2)(a) | src:40179-40182 | encoded | sfac-243 | in the function(s) of s 247(2) |
| s 247(2)(b) | src:40183-40186 | encoded | sfac-243 | in the function(s) of s 247(2) |
| s 247(3) | src:40187-40192 | encoded | sfac-243 | `s 247(1) and (3) the person or document is exempt from the requirement of form or content` |
| s 247(4) | src:40193-40194 | repealed or blank in this text | sfac-243 | s 247(4): "[Deleted by Act 16 of 2003]". |
| s 247(5) | src:40195-40205 | fork | sfac-243 | `s 247(5) the person is guilty of an offence`, `s 247(5) the penalty for the offence`, `s 247(5) the person shall not contravene a condition or restriction` (fork F31 in NOTES.md) |
| s 248 marginal heading | src:40206-40209 | inert (reason 1) | sfac-243 | s 248 marginal heading: not operative. |
| s 248(1) | src:40210-40212 | encoded | sfac-243 | `s 248(1) this section applies to the entity` |
| s 248(2) | src:40213-40219 | fork | sfac-243 | `s 248(2) the Authority may exempt the entity from the requirements` (fork F32 in NOTES.md) |
| s 248(3) | src:40220-40224 | encoded | sfac-243 | `s 248(3) the requirement as to signing by directors resident in Singapore is met` |
| s 248(4) | src:40225-40229 | fork | sfac-243 | `s 248(4) the Authority may permit a duly authorised agent to sign` (fork F32 in NOTES.md) |
| s 248(5) | src:40230-40233 | fork | sfac-243 | `s 248(5) the Authority may grant the exemption applied for` (fork F32 in NOTES.md) |
| s 248(6) | src:40234-40239 | encoded | sfac-243 | `s 248(6) the document is deemed to be a prospectus or profile statement for the purposes of this Division`, `s 248(6) a copy of the document must be registered by the Authority` |
| s 249 marginal heading | src:40240-40242 | inert (reason 1) | sfac-249 | s 249 marginal heading: not operative. |
| s 249(1) | src:40243-40252 | encoded | sfac-249 | `s 249(1) the prospectus or profile statement must not be issued`, `s 249(1) the person shall not issue the prospectus or profile statement` |
| s 249(1)(a) | src:40253-40258 | encoded | sfac-249 | in the function(s) of s 249(1) |
| s 249(1)(b) | src:40259-40264 | encoded | sfac-249 | in the function(s) of s 249(1) |
| s 249(1A) | src:40265-40271 | encoded | sfac-249, sfac-duties | `s 249(1A) the person making the offer has deposited the copies of the consents`, `s 249(1A) the person making the offer must deposit the copies of the consents within 7 days after the registration` |
| s 249(1B) | src:40272-40281 | encoded | sfac-249 | `s 249(1B) the issuer has kept the copies and made them available` |
| s 249(2) | src:40282-40290 | fork | sfac-249 | `s 249(2) the person is guilty of an offence`, `s 249(2) the penalty for the offence` (fork F33 in NOTES.md) |
| s 249(3) | src:40291-40299 | encoded | sfac-249 | `s 249(3) the person or document is exempt from the section` |
| s 249(4) | src:40300-40306 | fork | sfac-249 | `s 249(4) the person is guilty of an offence`, `s 249(4) the penalty for the offence`, `s 249(4) the person shall not contravene a condition or restriction` (fork F34 in NOTES.md) |
| s 249A marginal heading | src:40307-40309 | inert (reason 1) | sfac-249 | s 249A marginal heading: not operative. |
| s 249A(1) | src:40310-40315 | encoded | sfac-249 | `s 249A(1) the prospectus or profile statement must not be issued`, `s 249A(1) the person shall not issue the prospectus or profile statement` |
| s 249A(1)(a) | src:40316-40321 | encoded | sfac-249 | in the function(s) of s 249A(1) |
| s 249A(1)(b) | src:40322-40327 | encoded | sfac-249 | in the function(s) of s 249A(1) |
| s 249A(2) | src:40328-40333 | encoded | sfac-249 | `s 249A(2) the prospectus or profile statement must not be issued`, `s 249A(2) the person shall not issue the prospectus or profile statement` |
| s 249A(2)(a) | src:40334-40342 | encoded | sfac-249 | in the function(s) of s 249A(2) |
| s 249A(2)(b) | src:40343-40348 | encoded | sfac-249 | in the function(s) of s 249A(2) |
| s 249A(3) | src:40349-40357 | fork | sfac-249 | `s 249A(3) the person is guilty of an offence`, `s 249A(3) the penalty for the offence` (fork F35 in NOTES.md) |
| s 249A(4) | src:40358-40364 | encoded | sfac-249, sfac-duties | `s 249A(4) the person making the offer has deposited the copies of the consents`, `s 249A(4) the person making the offer must deposit the copies of the consents within 7 days after the registration (issue manager or underwriter)` |
| s 249A(5) | src:40365-40374 | encoded | sfac-249 | `s 249A(5) the issuer has kept the copies and made them available` |
| s 250 marginal heading | src:40375-40376 | inert (reason 1) | sfac-249 | s 250 marginal heading: not operative. |
| s 250(1) | src:40377-40384 | fork | sfac-249 | `s 250(1) the person must not make the offer or allot, issue or sell on the basis of the prospectus`, `s 250(1) the person shall not make the offer or allot, issue or sell after the period` (fork F36 in NOTES.md) |
| s 250(2) | src:40385-40395 | fork | sfac-249 | `s 250(2) the officer or promoter must not authorise or permit the offer, allotment, issue or sale`, `s 250(2) the officer or promoter shall not authorise or permit the offer, allotment, issue or sale after the period` (fork F36 in NOTES.md) |
| s 250(2)(a) | src:40396-40398 | encoded | sfac-249 | in the function(s) of s 250(2) |
| s 250(2)(b) | src:40399-40406 | encoded | sfac-249 | in the function(s) of s 250(2) |
| s 250(3) | src:40407-40408 | encoded | sfac-249 | `s 250(3) the last day of the period` |
| s 250(3)(a) | src:40409-40415 | encoded | sfac-249 | in the function(s) of s 250(3) |
| s 250(3)(b) | src:40416-40421 | encoded | sfac-249 | in the function(s) of s 250(3) |
| s 250(4) | src:40422-40430 | fork | sfac-249 | `s 250(4) the person is guilty of an offence`, `s 250(4) the penalty for the offence` (fork F37 in NOTES.md) |
| s 250(5) | src:40431-40439 | encoded | sfac-249 | `s 250(5) the allotment, issue or sale is void or voidable by reason only of the contravention` |
| s 251 marginal heading | src:40440-40441 | inert (reason 1) | sfac-249 | s 251 marginal heading: not operative. |
| s 251(1) | src:40442-40445 | fork | sfac-249 | `s 251(1) the person must not advertise the offer or publish the statement`, `s 251(1) the person shall not advertise the offer or publish the statement` (fork F38 in NOTES.md) |
| s 251(1)(a) | src:40446-40447 | encoded | sfac-249 | in the function(s) of s 251(1) |
| s 251(1)(b) | src:40448-40449 | encoded | sfac-249 | in the function(s) of s 251(1) |
| s 251(1)(b)(i) | src:40450-40452 | encoded | sfac-249 | in the function(s) of s 251(1)(b) |
| s 251(1)(b)(ii) | src:40453-40460 | encoded | sfac-249 | `s 251(1) the person must not advertise the offer or publish the statement`, `s 251(1) the person shall not advertise the offer or publish the statement`, `s 251 the advertisement or publication is authorised by this section` |
| s 251(2) | src:40461-40462 | fork | sfac-249 | `s 251(2) regard has been had to the three matters` (fork F41 in NOTES.md) |
| s 251(2)(a) | src:40463-40465 | encoded | sfac-249 | in the function(s) of s 251(2) |
| s 251(2)(b) | src:40466-40471 | encoded | sfac-249 | in the function(s) of s 251(2) |
| s 251(2)(c) | src:40472-40473 | encoded | sfac-249 | `s 251(2)(c) the statement forms part of the normal advertising` |
| s 251(2)(c)(i) | src:40474-40478 | encoded | sfac-249 | `s 251(2) regard has been had to the three matters`, `s 251(2)(c) the statement forms part of the normal advertising` |
| s 251(2)(c)(ii) | src:40479-40485 | encoded | sfac-249 | `s 251(2) regard has been had to the three matters`, `s 251(2)(c) the statement forms part of the normal advertising` |
| s 251(2)(d) | src:40486-40491 | encoded | sfac-249 | in the function(s) of s 251(2) |
| s 251(2)(e) | src:40492-40497 | encoded | sfac-249 | in the function(s) of s 251(2) |
| s 251(3) | src:40498-40502 | fork | sfac-249 | `s 251(3) the person may disseminate the preliminary document without contravening subsection (1)` (fork F39 in NOTES.md) |
| s 251(3)(a) | src:40503-40504 | encoded | sfac-249 | in the function(s) of s 251(3) |
| s 251(3)(a)(i) | src:40505-40516 | encoded | sfac-249 | in the function(s) of s 251(3)(a) |
| s 251(3)(a)(ii) | src:40517-40518 | repealed or blank in this text | sfac-249 | s 251(3)(a)(ii): "[Deleted by Act 12 of 2026 wef 29/06/2026]". |
| s 251(3)(a)(iii) | src:40519-40524 | encoded | sfac-249 | in the function(s) of s 251(3)(a) |
| s 251(3)(b) | src:40525-40531 | encoded | sfac-249 | in the function(s) of s 251(3) |
| s 251(3)(c) | src:40532-40543 | encoded | sfac-249 | in the function(s) of s 251(3) |
| s 251(4) | src:40544-40546 | encoded | sfac-249 | `s 251(4)(a) the person does not contravene subsection (1) by presenting the material` |
| s 251(4)(a) | src:40547-40551 | fork | sfac-249 | in the function(s) of s 251(4) (fork F39 in NOTES.md) |
| s 251(4)(a)(i) | src:40552-40556 | encoded | sfac-249 | in the function(s) of s 251(4)(a) |
| s 251(4)(a)(ii) | src:40557-40563 | encoded | sfac-249 | in the function(s) of s 251(4)(a) |
| s 251(4)(a)(iii) | src:40564-40567 | encoded | sfac-249 | in the function(s) of s 251(4)(a) |
| s 251(4)(a)(iv) | src:40568-40575 | encoded | sfac-249 | in the function(s) of s 251(4)(a) |
| s 251(4)(b) | src:40576-40593 | fork | sfac-249 | `s 251(4)(b) the person does not contravene subsection (1) by presenting the material to equip those persons` (fork F39 in NOTES.md) |
| s 251(4)(b)(i) | src:40594-40597 | encoded | sfac-249 | `s 251(4)(b) the person equipped is one of the eight persons listed` |
| s 251(4)(b)(ii) | src:40598-40599 | encoded | sfac-249 | `s 251(4)(b) the person equipped is one of the eight persons listed` |
| s 251(4)(b)(iii) | src:40600-40603 | encoded | sfac-249 | `s 251(4)(b) the person equipped is one of the eight persons listed` |
| s 251(4)(b)(iv) | src:40604-40605 | encoded | sfac-249 | `s 251(4)(b) the person equipped is one of the eight persons listed` |
| s 251(4)(b)(v) | src:40606-40609 | encoded | sfac-249 | `s 251(4)(b) the person equipped is one of the eight persons listed` |
| s 251(4)(b)(vi) | src:40610-40611 | encoded | sfac-249 | `s 251(4)(b) the person equipped is one of the eight persons listed` |
| s 251(4)(b)(vii) | src:40612-40615 | encoded | sfac-249 | `s 251(4)(b) the person equipped is one of the eight persons listed` |
| s 251(4)(b)(viii) | src:40616-40619 | encoded | sfac-249 | `s 251(4)(b) the person equipped is one of the eight persons listed` |
| s 251(5) | src:40620-40622 | encoded | sfac-249 | `s 251(5)(a) the person may disseminate the registered prospectus or profile statement` |
| s 251(5)(a) | src:40623-40625 | fork | sfac-249 | in the function(s) of s 251(5) (fork F40 in NOTES.md) |
| s 251(5)(b) | src:40626-40633 | fork | sfac-249 | `s 251(5)(b) the person may disseminate the product highlights sheet` (fork F40 in NOTES.md) |
| s 251(6) | src:40634-40640 | fork | sfac-249 | `s 251(6) the advertisement or publication does not contravene subsection (1) before registration` (fork F39 in NOTES.md) |
| s 251(6)(a) | src:40641-40642 | encoded | sfac-249 | `s 251(6)(a) the statement identifies what paragraph (a) requires` |
| s 251(6)(a)(i) | src:40643-40649 | encoded | sfac-249 | `s 251(6)(a) the statement identifies what paragraph (a) requires`, `s 251(6) the advertisement or publication does not contravene subsection (1) before registration` |
| s 251(6)(a)(ii) | src:40650-40654 | encoded | sfac-249 | `s 251(6)(a) the statement identifies what paragraph (a) requires`, `s 251(6) the advertisement or publication does not contravene subsection (1) before registration` |
| s 251(6)(b) | src:40655-40657 | encoded | sfac-249 | in the function(s) of s 251(6) |
| s 251(6)(c) | src:40658-40662 | encoded | sfac-249 | in the function(s) of s 251(6) |
| s 251(6)(d) | src:40663-40667 | encoded | sfac-249 | in the function(s) of s 251(6) |
| s 251(7) | src:40668-40672 | encoded | sfac-249 | `s 251(7) the advertisement or publication satisfies subsection (6)` |
| s 251(8) | src:40673-40676 | fork | sfac-249 | `s 251(8) the advertisement or publication does not contravene subsection (1) after registration` (fork F39 in NOTES.md) |
| s 251(8)(a) | src:40677-40682 | encoded | sfac-249 | in the function(s) of s 251(8) |
| s 251(8)(b) | src:40683-40691 | encoded | sfac-249 | in the function(s) of s 251(8) |
| s 251(8)(c) | src:40692-40694 | encoded | sfac-249 | in the function(s) of s 251(8) |
| s 251(8)(d) | src:40695-40699 | encoded | sfac-249 | in the function(s) of s 251(8) |
| s 251(9) | src:40700-40702 | fork | sfac-249 | `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` (fork F40 in NOTES.md) |
| s 251(9)(a) | src:40703-40707 | fork | sfac-249 | `s 251(9)(a) the advertisement or publication is a required disclosure, notice or report` (fork F40 in NOTES.md) |
| s 251(9)(b) | src:40708-40715 | fork | sfac-249 | `s 251(9)(b) the advertisement or publication is a notice or report of a general meeting` (fork F40 in NOTES.md) |
| s 251(9)(c) | src:40716-40721 | fork | sfac-249 | `s 251(9)(c) the advertisement or publication is a report about the issuer, the business trust or the underlying entity` (fork F40 in NOTES.md) |
| s 251(9)(c)(i) | src:40722-40729 | encoded | sfac-249 | `s 251(9)(c) the advertisement or publication is a report about the issuer, the business trust or the underlying entity`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(c)(ii) | src:40730-40735 | encoded | sfac-249 | `s 251(9)(c) the advertisement or publication is a report about the issuer, the business trust or the underlying entity`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(d) | src:40736-40741 | fork | sfac-249 | `s 251(9)(d) the advertisement or publication is a statement that the prospectus or profile statement has been lodged` (fork F40 in NOTES.md) |
| s 251(9)(e) | src:40742-40747 | fork | sfac-249 | `s 251(9)(e) the advertisement or publication is a news report or a genuine comment` (fork F40 in NOTES.md) |
| s 251(9)(e)(i) | src:40748-40751 | encoded | sfac-249 | `s 251(9)(e) the advertisement or publication is a news report or a genuine comment`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(e)(ii) | src:40752-40754 | encoded | sfac-249 | `s 251(9)(e) the advertisement or publication is a news report or a genuine comment`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(e)(iii) | src:40755-40758 | encoded | sfac-249 | `s 251(9)(e) the advertisement or publication is a news report or a genuine comment`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(e)(iv) | src:40759-40760 | encoded | sfac-249 | `s 251(9)(e) the advertisement or publication is a news report or a genuine comment`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(e)(v) | src:40761-40762 | encoded | sfac-249 | `s 251(9)(e) the advertisement or publication is a news report or a genuine comment`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(f) | src:40763-40766 | fork | sfac-249 | `s 251(9)(f) the person is one of the four persons paragraph (f) names`, `s 251(9)(f) the advertisement or publication is a report by a person other than the four` (fork F40 in NOTES.md) |
| s 251(9)(f)(i) | src:40767-40772 | encoded | sfac-249 | `s 251(9)(f) the person is one of the four persons paragraph (f) names`, `s 251(9)(f) the advertisement or publication is a report by a person other than the four`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(f)(ii) | src:40773-40782 | encoded | sfac-249 | `s 251(9)(f) the person is one of the four persons paragraph (f) names`, `s 251(9)(f) the advertisement or publication is a report by a person other than the four`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(f)(iii) | src:40783-40786 | encoded | sfac-249 | `s 251(9)(f) the person is one of the four persons paragraph (f) names`, `s 251(9)(f) the advertisement or publication is a report by a person other than the four`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(f)(iv) | src:40787-40790 | encoded | sfac-249 | `s 251(9)(f) the person is one of the four persons paragraph (f) names`, `s 251(9)(f) the advertisement or publication is a report by a person other than the four`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(g) | src:40791-40794 | fork | sfac-249 | `s 251(9)(g) the advertisement or publication is of a description the Authority has prescribed` (fork F40 in NOTES.md) |
| s 251(9)(h) | src:40795-40801 | fork | sfac-249 | `s 251(9)(h) the advertisement or publication corrects or clarifies an earlier report or publication` (fork F40 in NOTES.md) |
| s 251(9)(i) | src:40802-40804 | encoded | sfac-249 | `s 251(9)(h) the advertisement or publication corrects or clarifies an earlier report or publication`, `s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight` |
| s 251(9)(i)(ii) | src:40805-40811 | encoded | sfac-249 | in the function(s) of s 251(9)(i) |
| s 251(9)(h) (second one numbered alike) | src:40812-40817 | fork | sfac-249 | `s 251(9)(h) the advertisement or publication corrects or clarifies an earlier report or publication` (fork F40 in NOTES.md) |
| s 251(10) | src:40818-40819 | fork | sfac-249 | `s 251(10) the person does not contravene subsection (1) by publishing in the ordinary course of business` (fork F40 in NOTES.md) |
| s 251(10)(a) | src:40820-40822 | encoded | sfac-249 | in the function(s) of s 251(10) |
| s 251(10)(a)(i) | src:40823-40824 | encoded | sfac-249 | in the function(s) of s 251(10)(a) |
| s 251(10)(a)(ii) | src:40825-40830 | encoded | sfac-249 | in the function(s) of s 251(10)(a) |
| s 251(10)(b) | src:40831-40834 | encoded | sfac-249 | in the function(s) of s 251(10) |
| s 251(11) | src:40835-40838 | fork | sfac-249 | `s 251(11) subsection (9)(e) and (f) apply to the advertisement or statement` (fork F40 in NOTES.md) |
| s 251(12) | src:40839-40840 | fork | sfac-249 | `s 251(12) the person is guilty of an offence`, `s 251(12) the penalty for the offence` (fork F38 in NOTES.md) |
| s 251(12)(a) | src:40841-40842 | encoded | sfac-249 | in the function(s) of s 251(12) |
| s 251(12)(b) | src:40843-40854 | encoded | sfac-249 | in the function(s) of s 251(12) |
| s 251(13) | src:40855-40857 | encoded | sfac-249 | `s 251(13) this section affects a liability under another law` |
| s 251(14) | src:40858-40861 | encoded | sfac-249 | `s 251(14) the person is exempt from this section` |
| s 251(15) | src:40862-40868 | fork | sfac-249 | `s 251(15) the person is guilty of an offence`, `s 251(15) the penalty for the offence`, `s 251(15) the person shall not contravene a condition or restriction` (fork F34 in NOTES.md) |
| s 251(16) | src:40869-40872 | encoded | sfac-249 | `s 251(16) the person publishes a statement for the purposes of this section` |
| s 251(17) | src:40873-40879 | encoded | sfac-249 | `s 251(17) the item is a statement for the purposes of subsections (1) and (2)` |
| s 251(18) | src:40880-40882 | fork | sfac-249 | `s 251(18) the matter is within the affairs of the entity or the business trust` (fork F42 in NOTES.md) |
| s 251(18)(a) | src:40883-40885 | encoded | sfac-249 | in the function(s) of s 251(18) |
| s 251(18)(b) | src:40886-40890 | encoded | sfac-249 | in the function(s) of s 251(18) |
| s 251(18A) | src:40891-40892 | fork | sfac-249 | `s 251(18A) the term "exempt financial adviser" or "financial advisory service" is met` (fork F42 in NOTES.md) |
| s 251(18A) "exempt financial adviser" | src:40893-40896 | encoded | sfac-249 | in the function(s) of s 251(18A) |
| s 251(18A) "representative" | src:40897-40898 | fork | sfac-249 | `s 251(18A) "representative" the person is a representative` (fork F42 in NOTES.md) |
| s 251(18A) "representative" (a) | src:40899-40903 | encoded | sfac-249 | `s 251(18A) the term "exempt financial adviser" or "financial advisory service" is met`, `s 251(18A) "representative" the person is a representative` |
| s 251(18A) "representative" (b) | src:40904-40910 | encoded | sfac-249 | `s 251(18A) the term "exempt financial adviser" or "financial advisory service" is met`, `s 251(18A) "representative" the person is a representative` |
| s 251(19) | src:40911-40913 | fork | sfac-249 | `s 251(19) the matter is within the affairs of the issuer, underlying entity or business trust` (fork F42 in NOTES.md) |
| s 251(19)(a) | src:40914-40917 | encoded | sfac-249 | in the function(s) of s 251(19) |
| s 251(19)(b) | src:40918-40922 | encoded | sfac-249 | in the function(s) of s 251(19) |
| s 252 marginal heading | src:40923-40925 | inert (reason 1) | sfac-249 | s 252 marginal heading: not operative. |
| s 252(1) | src:40926-40936 | fork | sfac-249 | `s 252(1) the person has notified the person making the offer` (fork F18 in NOTES.md) |
| s 252(1)(a) | src:40937-40939 | encoded | sfac-249 | in the function(s) of s 252(1) |
| s 252(1)(b) | src:40940-40945 | encoded | sfac-249 | in the function(s) of s 252(1) |
| s 252(1)(c) | src:40946-40947 | encoded | sfac-249 | in the function(s) of s 252(1) |
| s 252(1)(c)(i) | src:40948-40950 | encoded | sfac-249 | in the function(s) of s 252(1)(c) |
| s 252(1)(c)(ii) | src:40951-40962 | encoded | sfac-249 | in the function(s) of s 252(1)(c) |
| s 252(2) | src:40963-40966 | fork | sfac-249 | `s 252(2) the person is guilty of an offence`, `s 252(2) the penalty for the offence` (fork F43 in NOTES.md) |
| s 252(3) | src:40967-40970 | encoded | sfac-249 | `s 252(3) the item is a statement for the purposes of subsection (1)(a)` |
| s 253 marginal heading | src:40971-40972 | inert (reason 1) | sfac-253 | s 253 marginal heading: not operative. |
| s 253(1) | src:40973-40981 | fork | sfac-253 | `s 253(1) the false or misleading statement or omission is present` (fork F44 in NOTES.md) |
| s 253(1)(a) | src:40982-40983 | encoded | sfac-253 | in the function(s) of s 253(1) |
| s 253(1)(a)(i) | src:40984-40985 | encoded | sfac-253 | in the function(s) of s 253(1)(a) |
| s 253(1)(a)(ii) | src:40986-40988 | encoded | sfac-253 | in the function(s) of s 253(1)(a) |
| s 253(1)(b) | src:40989-40994 | encoded | sfac-253 | in the function(s) of s 253(1) |
| s 253(1)(c) | src:40995-40996 | encoded | sfac-253 | in the function(s) of s 253(1) |
| s 253(1)(c)(i) | src:40997-40999 | encoded | sfac-253 | in the function(s) of s 253(1)(c) |
| s 253(1)(c)(ii) | src:41000-41017 | encoded | sfac-253 | `s 253(1) the false or misleading statement or omission is present`, `s 253(1) the person is guilty of an offence`, `s 253(1) the penalty for the offence` |
| s 253(2) | src:41018-41023 | fork | sfac-253 | `s 253(2) a false or misleading statement about a future matter is taken to have been made` (fork F45 in NOTES.md) |
| s 253(3) | src:41024-41032 | fork | sfac-253 | `s 253(3) the person does not contravene subsection (1)` (fork F46 in NOTES.md) |
| s 253(4) | src:41033-41034 | fork | sfac-253 | `s 253(4) the person is one of the persons guilty of the offence` (fork F48 in NOTES.md) |
| s 253(4)(a) | src:41035-41036 | encoded | sfac-253 | in the function(s) of s 253(4) |
| s 253(4)(b) | src:41037-41038 | fork | sfac-253 | `s 253(4)(b) the person is a director or proposed director of the entity making the offer` (fork F47 in NOTES.md) |
| s 253(4)(b)(i) | src:41039-41040 | encoded | sfac-253 | in the function(s) of s 253(4)(b) |
| s 253(4)(b)(ii) | src:41041-41045 | encoded | sfac-253 | in the function(s) of s 253(4)(b) |
| s 253(4)(c) | src:41046-41050 | fork | sfac-253 | `s 253(4)(c) the person is the issuer or a director or proposed director of the issuer` (fork F47 in NOTES.md) |
| s 253(4)(c)(i) | src:41051-41052 | encoded | sfac-253 | in the function(s) of s 253(4)(c) |
| s 253(4)(c)(ii) | src:41053-41054 | encoded | sfac-253 | in the function(s) of s 253(4)(c) |
| s 253(4)(c)(iii) | src:41055-41059 | encoded | sfac-253 | in the function(s) of s 253(4)(c) |
| s 253(4)(d) | src:41060-41064 | fork | sfac-253 | `s 253(4)(d) the issue manager is one of the persons guilty` (fork F47 in NOTES.md) |
| s 253(4)(d)(i) | src:41065-41068 | encoded | sfac-253 | in the function(s) of s 253(4)(d) |
| s 253(4)(d)(ii) | src:41069-41077 | encoded | sfac-253 | in the function(s) of s 253(4)(d) |
| s 253(4)(d)(iii) | src:41078-41081 | encoded | sfac-253 | in the function(s) of s 253(4)(d) |
| s 253(4)(e) | src:41082-41086 | fork | sfac-253 | `s 253(4)(e) the underwriter is one of the persons guilty` (fork F47 in NOTES.md) |
| s 253(4)(e)(i) | src:41087-41090 | encoded | sfac-253 | in the function(s) of s 253(4)(e) |
| s 253(4)(e)(ii) | src:41091-41096 | encoded | sfac-253 | in the function(s) of s 253(4)(e) |
| s 253(4)(e)(iii) | src:41097-41100 | encoded | sfac-253 | in the function(s) of s 253(4)(e) |
| s 253(4)(f) | src:41101-41103 | fork | sfac-253 | `s 253(4)(f) the person named as having made a statement is one of the persons guilty` (fork F47 in NOTES.md) |
| s 253(4)(f)(i) | src:41104-41106 | encoded | sfac-253 | in the function(s) of s 253(4)(f) |
| s 253(4)(f)(ii) | src:41107-41112 | encoded | sfac-253 | in the function(s) of s 253(4)(f) |
| s 253(4)(f) (second one numbered alike) | src:41113-41115 | fork | sfac-253 | `s 253(4)(f) the person named as having made a statement is one of the persons guilty` (fork F47 in NOTES.md) |
| s 253(4)(g) | src:41116-41128 | fork | sfac-253 | `s 253(4)(g) any other person is one of the persons guilty` (fork F47 in NOTES.md) |
| s 253(5) | src:41129-41130 | encoded | sfac-253 | `s 253(5)(a) the action is remedial action` |
| s 253(5)(a) | src:41131-41132 | fork | sfac-253 | in the function(s) of s 253(5) (fork F50 in NOTES.md) |
| s 253(5)(a)(i) | src:41133-41137 | encoded | sfac-253 | in the function(s) of s 253(5)(a) |
| s 253(5)(a)(ii) | src:41138-41140 | encoded | sfac-253 | in the function(s) of s 253(5)(a) |
| s 253(5)(b) | src:41141-41150 | fork | sfac-253 | `s 253(5)(b) the person is reckless` (fork F50 in NOTES.md) |
| s 253(5)(b)(i) | src:41151-41153 | encoded | sfac-253 | in the function(s) of s 253(5)(b) |
| s 253(5)(b)(ii) | src:41154-41157 | encoded | sfac-253 | in the function(s) of s 253(5)(b) |
| s 253(6) | src:41158-41161 | encoded | sfac-253 | `s 253(6) the item is a statement for the purposes of this section` |
| s 254 marginal heading | src:41162-41163 | inert (reason 1) | sfac-253 | s 254 marginal heading: not operative. |
| s 254(1) | src:41164-41172 | fork | sfac-253 | `s 254(1) the false or misleading statement or omission is present` (fork F44 in NOTES.md) |
| s 254(1)(a) | src:41173-41174 | encoded | sfac-253 | in the function(s) of s 254(1) |
| s 254(1)(a)(i) | src:41175-41176 | encoded | sfac-253 | in the function(s) of s 254(1)(a) |
| s 254(1)(a)(ii) | src:41177-41179 | encoded | sfac-253 | in the function(s) of s 254(1)(a) |
| s 254(1)(b) | src:41180-41185 | encoded | sfac-253 | in the function(s) of s 254(1) |
| s 254(1)(c) | src:41186-41187 | encoded | sfac-253 | in the function(s) of s 254(1) |
| s 254(1)(c)(i) | src:41188-41190 | encoded | sfac-253 | in the function(s) of s 254(1)(c) |
| s 254(1)(c)(ii) | src:41191-41205 | encoded | sfac-253 | `s 254(1) the false or misleading statement or omission is present`, `s 254(1) the person is liable to compensate the claimant` |
| s 254(2) | src:41206-41211 | fork | sfac-253 | `s 254(2) a false or misleading statement about a future matter is taken to have been made` (fork F45 in NOTES.md) |
| s 254(3) | src:41212-41213 | fork | sfac-253 | `s 254(3) the person is one of the persons liable` (fork F48 in NOTES.md) |
| s 254(3)(a) | src:41214-41215 | encoded | sfac-253 | in the function(s) of s 254(3) |
| s 254(3)(b) | src:41216-41217 | fork | sfac-253 | `s 254(3)(b) the person is a director or proposed director of the entity making the offer` (fork F47 in NOTES.md) |
| s 254(3)(b)(i) | src:41218-41222 | encoded | sfac-253 | in the function(s) of s 254(3)(b) |
| s 254(3)(b)(ii) | src:41223-41227 | encoded | sfac-253 | in the function(s) of s 254(3)(b) |
| s 254(3)(c) | src:41228-41232 | fork | sfac-253 | `s 254(3)(c) the person is the issuer or a director or proposed director of the issuer` (fork F47 in NOTES.md) |
| s 254(3)(c)(i) | src:41233-41234 | encoded | sfac-253 | in the function(s) of s 254(3)(c) |
| s 254(3)(c)(ii) | src:41235-41236 | encoded | sfac-253 | in the function(s) of s 254(3)(c) |
| s 254(3)(c)(iii) | src:41237-41241 | encoded | sfac-253 | in the function(s) of s 254(3)(c) |
| s 254(3)(d) | src:41242-41246 | fork | sfac-253 | `s 254(3)(d) the issue manager is one of the persons liable` (fork F47 in NOTES.md) |
| s 254(3)(da) | src:41247-41251 | fork | sfac-253 | `s 254(3)(da) the underwriter is one of the persons liable` (fork F47 in NOTES.md) |
| s 254(3)(e) | src:41252-41254 | fork | sfac-253 | `s 254(3)(e) the person named as having made a statement is one of the persons liable` (fork F47 in NOTES.md) |
| s 254(3)(e)(i) | src:41255-41257 | encoded | sfac-253 | in the function(s) of s 254(3)(e) |
| s 254(3)(e)(ii) | src:41258-41260 | encoded | sfac-253 | in the function(s) of s 254(3)(e) |
| s 254(3)(e) (second one numbered alike) | src:41261-41262 | fork | sfac-253 | `s 254(3)(e) the person named as having made a statement is one of the persons liable` (fork F47 in NOTES.md) |
| s 254(3)(f) | src:41263-41274 | fork | sfac-253 | `s 254(3)(f) any other person is one of the persons liable` (fork F47 in NOTES.md) |
| s 254(4) | src:41275-41282 | fork | sfac-253 | `s 254(4) the person is taken to have acquired in reliance on both the profile statement and the prospectus` (fork F45 in NOTES.md) |
| s 254(4A) | src:41283-41286 | encoded | sfac-253 | `s 254(4A) the item is a statement for the purposes of this section` |
| s 254(5) | src:41287-41289 | fork | sfac-253 | `s 254(5) the action may not be commenced` (fork F52 in NOTES.md) |
| s 254(6) | src:41290-41292 | encoded | sfac-253 | `s 254(6) this section affects a liability under another law` |
| s 255 marginal heading | src:41293-41294 | inert (reason 1) | sfac-253 | s 255 marginal heading: not operative. |
| s 255(1) | src:41295-41300 | fork | sfac-253 | `s 255(1) this section gives a defence for the false or misleading statement`, `s 255 the person has a defence` (fork F53 in NOTES.md) |
| s 255(1)(a) | src:41301-41303 | encoded | sfac-253 | `s 255(1) this section gives a defence for the false or misleading statement` |
| s 255(1)(b) | src:41304-41306 | encoded | sfac-253 | `s 255(1) this section gives a defence for the false or misleading statement` |
| s 255(2) | src:41307-41312 | fork | sfac-253 | `s 255(2) this section gives a defence for the omission` (fork F53 in NOTES.md) |
| s 255(2)(a) | src:41313-41318 | encoded | sfac-253 | in the function(s) of s 255(2) |
| s 255(2)(b) | src:41319-41322 | encoded | sfac-253 | in the function(s) of s 255(2) |
| s 255(3) | src:41323-41327 | fork | sfac-253 | `s 255(3) this section gives a defence for reasonable reliance on information` (fork F53 in NOTES.md) |
| s 255(3)(a) | src:41328-41329 | encoded | sfac-253 | in the function(s) of s 255(3) |
| s 255(3)(a)(i) | src:41330-41331 | encoded | sfac-253 | in the function(s) of s 255(3)(a) |
| s 255(3)(a)(ii) | src:41332-41333 | encoded | sfac-253 | in the function(s) of s 255(3)(a) |
| s 255(3)(a) (second one numbered alike) | src:41334-41335 | encoded | sfac-253 | in the function(s) of s 255(3) |
| s 255(3)(b) | src:41336-41338 | encoded | sfac-253 | in the function(s) of s 255(3) |
| s 255(4) | src:41339-41343 | fork | sfac-253 | `s 255(4) the person is an agent of the entity or individual` (fork F53 in NOTES.md) |
| s 255(5) | src:41344-41346 | fork | sfac-253 | `s 255(5) this section gives a defence for publicly withdrawing consent` (fork F53 in NOTES.md) |
| s 255(5)(a) | src:41347-41349 | encoded | sfac-253 | in the function(s) of s 255(5) |
| s 255(5)(b) | src:41350-41352 | encoded | sfac-253 | in the function(s) of s 255(5) |
| s 255(5)(c) | src:41353-41361 | encoded | sfac-253 | in the function(s) of s 255(5) |
| s 255(6) | src:41362-41370 | fork | sfac-253 | `s 255(6) this section gives a defence for not being aware of a new circumstance` (fork F53 in NOTES.md) |
| s 255(7) | src:41371-41374 | encoded | sfac-253 | `s 255(7) the item is a statement for the purposes of this section` |
| s 256 | src:41375-41376 | repealed or blank in this text | sfac-253 | s 256: "[Repealed by Act 1 of 2005]". |
| s 257 marginal heading | src:41377-41379 | inert (reason 1) | sfac-257 | s 257 marginal heading: not operative. |
| s 257(1) | src:41380-41381 | fork | sfac-257 | `s 257(1) subsection (2) applies` (fork F54 in NOTES.md) |
| s 257(1)(a) | src:41382-41387 | encoded | sfac-257 | in the function(s) of s 257(1) |
| s 257(1)(b) | src:41388-41393 | encoded | sfac-257 | in the function(s) of s 257(1) |
| s 257(2) | src:41394-41401 | fork | sfac-257 | `s 257(2) the document is deemed to be a prospectus issued by the entity`, `s 257(2) the entity is deemed to be the person making the offer`, `s 257(2) the persons accepting the subsequent offer are deemed subscribers`, `s 257(2) the deeming affects the liability of the persons making the subsequent offer` (fork F55 in NOTES.md) |
| s 257(2)(a) | src:41402-41404 | encoded | sfac-257 | in the function(s) of s 257(2) |
| s 257(2)(b) | src:41405-41417 | encoded | sfac-257 | in the function(s) of s 257(2) |
| s 257(3) | src:41418-41423 | fork | sfac-257 | `s 257(3) it is sufficient evidence that the allotment was made with a view to subsequent sale` (fork F56 in NOTES.md) |
| s 257(3)(a) | src:41424-41428 | encoded | sfac-257 | in the function(s) of s 257(3) |
| s 257(3)(b) | src:41429-41435 | encoded | sfac-257 | in the function(s) of s 257(3) |
| s 257(4) | src:41436-41440 | fork | sfac-257 | `s 257(4) the person making the subsequent offer is treated as a person named in the prospectus as a director` (fork F55 in NOTES.md) |
| s 257(5) | src:41441-41443 | fork | sfac-257 | `s 257(5) the document states what it must state` (fork F18 in NOTES.md) |
| s 257(5)(a) | src:41444-41447 | encoded | sfac-257 | in the function(s) of s 257(5) |
| s 257(5)(b) | src:41448-41453 | encoded | sfac-257 | in the function(s) of s 257(5) |
| s 258 marginal heading | src:41454-41456 | inert (reason 1) | sfac-257 | s 258 marginal heading: not operative. |
| s 258(1) | src:41457-41473 | fork | sfac-257 | `s 258(1) the person making the offer holds the moneys on trust in a separate bank account` (fork F18 in NOTES.md) |
| s 258(2) | src:41474-41477 | fork | sfac-257 | `s 258(2) the bank has an obligation or duty to enquire into the application of the moneys` (fork F57 in NOTES.md) |
| s 258(3) | src:41478-41484 | fork | sfac-257 | `s 258(3) the person is guilty of an offence`, `s 258(3) the penalty for the offence` (fork F58 in NOTES.md) |
| s 259 marginal heading | src:41485-41488 | inert (reason 1) | sfac-257 | s 259 marginal heading: not operative. |
| s 259(1) | src:41489-41493 | fork | sfac-257 | `s 259(1) the permission was not applied for or not granted in time` (fork F59 in NOTES.md) |
| s 259(1)(a) | src:41494-41497 | fork | sfac-257 | `s 259(1)(a) the permission was not applied for in time` (fork F59 in NOTES.md) |
| s 259(1)(b) | src:41498-41505 | fork | sfac-257 | `s 259(1)(b) the permission was not granted in time` (fork F59 in NOTES.md) |
| s 259(1)(c) | src:41506-41513 | fork | sfac-257 | `s 259(1)(c) the allotment is void` (fork F60 in NOTES.md) |
| s 259(1)(d) | src:41514-41525 | fork | sfac-257 | `s 259(1)(d) the person is guilty of an offence`, `s 259(1)(d) the penalty for the offence` (fork F61 in NOTES.md) |
| s 259(2) | src:41526-41533 | fork | sfac-257 | `s 259(2) the person making the offer has repaid the moneys` (fork F18 in NOTES.md) |
| s 259(2)(a) | src:41534-41537 | fork | sfac-257 | `s 259(2)(a) the person making the offer is liable to repay with interest at 10% per annum` (fork F62 in NOTES.md) |
| s 259(2)(b) | src:41538-41543 | fork | sfac-257 | `s 259(2)(b) the director is jointly and severally liable to repay with interest at 10% per annum` (fork F62 in NOTES.md) |
| s 259(3) | src:41544-41546 | fork | sfac-257 | `s 259(3) the Authority may exempt the allotment`, `s 259(3) the Authority has given notice of the exemption in the Gazette` (fork F63, F18 in NOTES.md) |
| s 259(3)(a) | src:41547-41549 | encoded | sfac-257 | in the function(s) of s 259(3) |
| s 259(3)(b) | src:41550-41564 | encoded | sfac-257 | in the function(s) of s 259(3) |
| s 259(4) | src:41565-41569 | fork | sfac-257 | `s 259(4) this section gives the director a defence` (fork F53 in NOTES.md) |
| s 259(5) | src:41570-41575 | encoded | sfac-257 | `s 259(5) the condition is void` |
| s 259(6) | src:41576-41578 | fork | sfac-257 | `s 259(6)(a) the underwriter is treated as having applied pursuant to the prospectus` (fork F64 in NOTES.md) |
| s 259(6)(a) | src:41579-41583 | encoded | sfac-257 | in the function(s) of s 259(6) |
| s 259(6)(b) | src:41584-41590 | fork | sfac-257 | `s 259(6)(b) a reference to sale is read for a reference to allotment` (fork F64 in NOTES.md) |
| s 259(7) | src:41591-41594 | fork | sfac-257 | `s 259(7) the moneys are kept in a separate bank account` (fork F18 in NOTES.md) |
| s 259(8) | src:41595-41601 | fork | sfac-257 | `s 259(8) the person is guilty of an offence`, `s 259(8) the penalty for the offence` (fork F58 in NOTES.md) |
| s 259(9) | src:41602-41615 | fork | sfac-257 | `s 259(9) permission is deemed to have been granted` (fork F65 in NOTES.md) |
| s 259(10) | src:41616-41622 | fork | sfac-257 | `s 259(10) the director is guilty of an offence`, `s 259(10) the penalty for the offence` (fork F66 in NOTES.md) |
| s 259(11) | src:41623-41626 | fork | sfac-257 | `s 259(11) the person must not issue the prospectus`, `s 259(11) the person shall not issue the prospectus` (fork F67 in NOTES.md) |
| s 259(11)(a) | src:41627-41631 | encoded | sfac-257 | in the function(s) of s 259(11) |
| s 259(11)(b) | src:41632-41638 | encoded | sfac-257 | in the function(s) of s 259(11) |
| s 259(11)(b)(i) | src:41639-41643 | encoded | sfac-257 | in the function(s) of s 259(11)(b) |
| s 259(11)(b)(ii) | src:41644-41648 | encoded | sfac-257 | in the function(s) of s 259(11)(b) |
| s 259(12) | src:41649-41658 | fork | sfac-257 | `s 259(12) the person is guilty of an offence`, `s 259(12) the penalty for the offence` (fork F58 in NOTES.md) |
| s 259(13) | src:41659-41670 | fork | sfac-257 | `s 259(13) the prospectus is deemed to imply that application has been or will be made for permission` (fork F68 in NOTES.md) |
| s 260 marginal heading | src:41671-41672 | inert (reason 1) | sfac-257 | s 260 marginal heading: not operative. |
| s 260(1) | src:41673-41676 | fork | sfac-257 | `s 260(1) the person must not make the allotment`, `s 260(1) the person shall not make the allotment` (fork F69 in NOTES.md) |
| s 260(1)(a) | src:41677-41678 | encoded | sfac-257 | in the function(s) of s 260(1) |
| s 260(1)(b) | src:41679-41685 | encoded | sfac-257 | in the function(s) of s 260(1) |
| s 260(1A) | src:41686-41694 | fork | sfac-257 | `s 260(1A) the sum payable on application is treated as received` (fork F69 in NOTES.md) |
| s 260(2) | src:41695-41696 | fork | sfac-257 | `s 260(2) the minimum subscription is calculated as it must be` (fork F70 in NOTES.md) |
| s 260(2)(a) | src:41697-41701 | encoded | sfac-257 | in the function(s) of s 260(2) |
| s 260(2)(b) | src:41702-41709 | encoded | sfac-257 | in the function(s) of s 260(2) |
| s 260(3) | src:41710-41717 | fork | sfac-257 | `s 260(3) the amount payable on application is not less than 5% of the price` (fork F70 in NOTES.md) |
| s 260(4) | src:41718-41725 | fork | sfac-257 | `s 260(4) the moneys have been repaid` (fork F18 in NOTES.md) |
| s 260(5) | src:41726-41734 | fork | sfac-257 | `s 260(5) the director is jointly and severally liable to repay with interest at 10% per annum` (fork F62 in NOTES.md) |
| s 260(6) | src:41735-41740 | fork | sfac-257 | `s 260(6) this section gives the director a defence` (fork F53 in NOTES.md) |
| s 260(7) | src:41741-41745 | fork | sfac-257 | `s 260(7) the applicant has exercised the option to avoid the allotment in time` (fork F71 in NOTES.md) |
| s 260(7)(a) | src:41746-41747 | encoded | sfac-257 | in the function(s) of s 260(7) |
| s 260(7)(a)(i) | src:41748-41750 | encoded | sfac-257 | in the function(s) of s 260(7)(a) |
| s 260(7)(a)(ii) | src:41751-41758 | encoded | sfac-257 | in the function(s) of s 260(7)(a) |
| s 260(7)(b) | src:41759-41764 | encoded | sfac-257 | in the function(s) of s 260(7) |
| s 260(7A) | src:41765-41769 | fork | sfac-257 | `s 260(7A) the allotment is voidable although the company or business trust is being wound up` (fork F71 in NOTES.md) |
| s 260(7B) | src:41770-41773 | fork | sfac-257 | `s 260(7B) the trustee-manager is guilty of an offence` (fork F72 in NOTES.md) |
| s 260(7B)(a) | src:41774-41779 | fork | sfac-257 | `s 260(7B)(a) the trustee-manager must pay into the trust property the loss, damages or costs` (fork F72 in NOTES.md) |
| s 260(7B)(b) | src:41780-41785 | fork | sfac-257 | `s 260(7B)(b) the trustee-manager must compensate the allottee` (fork F72 in NOTES.md) |
| s 260(7C) | src:41786-41791 | fork | sfac-257 | `s 260(7C) the director of the trustee-manager is guilty of an offence` (fork F72 in NOTES.md) |
| s 260(7C)(a) | src:41792-41797 | fork | sfac-257 | `s 260(7C)(a) the director must pay into the trust property the loss, damages or costs` (fork F72 in NOTES.md) |
| s 260(7C)(b) | src:41798-41803 | fork | sfac-257 | `s 260(7C)(b) the director must compensate the allottee` (fork F72 in NOTES.md) |
| s 260(7D) | src:41804-41812 | fork | sfac-257 | `s 260(7D) the director of the company is guilty of an offence` (fork F72 in NOTES.md) |
| s 260(7D)(a) | src:41813-41816 | fork | sfac-257 | `s 260(7D)(a) the director must compensate the company` (fork F72 in NOTES.md) |
| s 260(7D)(b) | src:41817-41822 | fork | sfac-257 | `s 260(7D)(b) the director must compensate the allottee` (fork F72 in NOTES.md) |
| s 260(8) | src:41823-41826 | fork | sfac-257 | `s 260(8) the proceedings may not be commenced` (fork F73 in NOTES.md) |
| s 260(9) | src:41827-41832 | encoded | sfac-257 | `s 260(9) the condition is void` |

Every row left `inert`, with its reason (1 not operative, 2 machinery, 3 text shown repealed or blank): see the rows above with `inert` in the third column; the 34 rows of reason 1 are the headings of the Part, Division and Subdivisions, the marginal headings, and the opening words of s 239(1), s 239AA(1), s 240(1) and s 240AA(5) that introduce definitions or limbs each encoded on its own; the 5 rows of reason 2 are s 239B (the Authority's power to modify this Division by regulations), s 240(8B) (the Authority's power to prescribe periods), s 240(20) (regulations under s 240 may make a contravention an offence), s 240A(8) (the Authority's power to prescribe how this Subdivision applies to an offer under a debenture issuance programme) and the marginal heading of s 239B.

## Fork register (sfac)

Each entry: the provision, the function, the answer taken, the other reading and the text that licenses each.
Every fork is also marked `-- FORK F<n>` in the code, above the function that carries it; the numbers F1 to F74 skip F3 (never used).
F9, F18, F40 and F53 are conventions that cover many functions (the counting of "within N days from", the duty functions, the safe harbours, the delegated defences): they are marked on the functions named in them and apply to every function of the same kind.

### F1 s 239(5A) `s 239(5A) the person is guilty of an offence` (split site (i); uses `sfac-239.l4`)
Text: "Any person who contravenes any condition or restriction imposed under subsection (5) shall be guilty of an offence".
Read: JUST TRUE when the person contravenes a condition; otherwise NOTHING.
The text defines the offence by the relative clause "who contravenes"; it does not say that a person who does not contravene is not guilty, so the unmet element is "limited by its own wording" (the "In short" line of Guide section 5: "limits a grant or prohibition in its own wording ... and the case falls outside the limit").
Other reading: JUST FALSE for a person who does not contravene (the offence is defined by "who contravenes", so anyone else is outside it).
Flip: the line marked `-- SPLIT-SITE (i)` in the function.

### F2 s 239AA(2) `s 239AA(2) the offer of SDRs is within the references to an offer of securities` (uses the keel's `s 2(1) "securities"`)
Text: "an offer of SDRs that are securities by virtue of paragraph (a), (b) or (c) of the definition of "securities" in section 2(1), and not excluded by virtue of paragraph (g) of that definition".
Read: the keel function is called with the limbs for paragraphs (a), (b), (c) and with FALSE for the exclusions (d), (e), (f) (a unit of a collective investment scheme, a bill of exchange, a certificate of deposit), and the prescribed exclusion (g) is tested first, because the text names only (g) as the exclusion.
Other reading: pass the real facts for (d), (e), (f), so that an SDR that is also a bill of exchange is not securities even though it satisfies (a), (b) or (c).
Both readings agree on every SDR that is not a unit of a collective investment scheme, a bill of exchange or a certificate of deposit.

### F4 s 240(1) `s 240(1) the person must not make the offer` (split site (i))
Text: "A person must not make an offer of securities or securities-based derivatives contracts unless the offer —".
Read: NOTHING when the person makes no offer: the bar is limited by its own wording to a person who makes an offer.
"unless" is a closed gate: JUST FALSE once the offer meets every limb of (a) and (b), or the profile statement route of s 240(4) answers JUST TRUE (any other answer of s 240(4), NOTHING included, is read as the route not being shown open, so the bar still bites), or another provision says this Subdivision does not apply.
Other reading: JUST FALSE for a person who makes no offer (a flat negative "must not" that does not bite on them).
Flip: the line marked `-- SPLIT-SITE (i)`.

### F5 s 240(4) `s 240(4) the offer may be made in or accompanied by a profile statement instead of a prospectus` (the grant ruling of 2026-11-12, limit (1))
Text: "Despite subsection (1), an offer ... may be made in or accompanied by an extract from, or an abridged version of, a prospectus (called in this section a profile statement), instead of a prospectus, if — (a) ... (e)".
Read: a function named for a permission ("may be made") whose "if" gate failed answers NOTHING.
Guide section 5, the grant ruling: "A function named for a grant or a power ... that answers JUST FALSE because an if gate failed reads as 'may not': a grant turned into a bar."
Other reading: JUST FALSE ("if" is a condition the text introduces, so a failed "if" is the text's no, clause by clause).
The caller s 240(1) treats only JUST TRUE as opening the route, so the two readings give the same answer to the bar.
Flip: the line marked `-- GRANT-RULING (1)`.

### F6 s 240(7) `s 240(7) the person is guilty of an offence` (split site (i))
Text: "Any person who contravenes subsection (1) or (5) shall be guilty of an offence".
Read: JUST TRUE when s 240(1) or s 240(5) answers JUST TRUE for the person; NOTHING when both answer JUST FALSE ("who contravenes" is the offence's own wording and the text does not say that anyone else is not guilty); NOTHING when an answer was not worked out.
Other reading: JUST FALSE when both answer JUST FALSE.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F7 s 240(8A) `s 240(8A) the Authority may proceed with the registration on the date` (split site (ii))
Text: "Where, after a notice of an opportunity to be heard has been given under subsection (8)(a), (b)(ii) or (c)(ii), the Authority decides not to refuse registration ..., the Authority may proceed with the registration on such date as it considers appropriate, except that that date must not be earlier than such day from the date of lodgment ... as the Authority may prescribe".
Read: JUST FALSE when the "Where" gate fails: the periods ruling of 2026-11-05, rule (b): "a 'where ...' condition: when it fails the answer is JUST FALSE"; and the grant ruling's limit (3) says to keep that answer and list the site for a lawyer ("a 'may' function whose gate is 'where', 'when' or 'upon' (ruling (b) ... says JUST FALSE, and the 'In short' line on grants points the other way)").
Other reading: NOTHING (a function named for a power whose gate failed).
Flip: the line marked `-- SPLIT-SITE (ii)`.

### F8 s 240(17) `s 240(17) the person is guilty of an offence` (split site (i), two sites)
Text: "If — (a) a prospectus or profile statement is issued ... before it has been registered ...; or (b) an application ... is accepted ... before a prospectus ... has been registered ..., the person making the offer and every person who is knowingly a party to — ... shall be guilty of an offence".
Read: (1) neither trigger occurs: JUST FALSE, because the text opens with "If" (the rule of 2026-10-29: "a condition the text introduces with 'if'"; a failed "if" counts as the text's no, reading (a) of the lawyer's question).
(2) a trigger occurs but the person is neither the person making the offer nor knowingly a party: NOTHING, because the text names the persons liable and says nothing of anyone else ("limited by its own wording").
Other reading: (1) NOTHING (the "If" only says when the offence arises); (2) JUST FALSE.
Flip: the two lines marked `-- SPLIT-SITE (i)`.

### F9 ss 240(8), 240(16) and every "within N days from" deadline in ss 241 and 242: counting "within" a period after an event
Text: s 240(8) "on any day within the period prescribed by the Authority from the date of lodgment"; s 240(16) "within 30 days after the person is notified".
Read: `period: the date is not later than the end of a period after` (keel), so that an act on the day of the event itself is in time and the last day is the event's day plus N (keel P1).
Other reading: `period: the date is within a period after` (keel P2), under which the window opens the day after the event and an act on the day itself is outside it.
s 240(8)'s "on any day within the period prescribed by the Authority" is a period the text fixes in its own words, so the periods ruling of 2026-11-05, rule (a), answers JUST FALSE outside it; it is not a split site (ii).
Reason: an appeal lodged the day the refusal is notified, or a registration on the day of lodgment, is not meant to be out of time.
The same reading counts the 2-day, 7-day and 14-day deadlines of s 241 and the 14-day and 7-day deadlines of s 242: an act on the day of lodgment, or of the stop order, itself is in time; the business-day deadline of s 241(8) and (12) counts the second business day after lodgment as the last (the keel's P8).

### F10 s 240AA(1) `s 240AA(1) the person must not make the offer` (split site (i), three sites)
Text: "A person must not make an offer of any relevant securities or securities-based derivatives contracts, being an offer that is made in or accompanied by a prospectus or profile statement that complies with section 240, unless the prospectus or profile statement is accompanied by a product highlights sheet".
Read: NOTHING when the person makes no offer, when the securities are not relevant securities (the s 240AA(5) function answers JUST FALSE), and when the offer is not made in or with a prospectus or profile statement that complies with section 240.
Each of the three is an element the bar is limited to by its own wording: the "In short" line of Guide section 5 (`inputs/ENCODING-GUIDE.md:87`) gives NOTHING where the text "limits a grant or prohibition in its own wording and the case falls outside the limit".
"unless" is a closed gate: JUST FALSE once the sheet is there, complies and is lodged, or the person is exempt under s 240AB (only an exemption answered JUST TRUE counts), or the Subdivision does not apply.
Other reading: JUST FALSE at each of the three sites (a flat "must not" that does not bite on a person outside it).
Flip: the three lines marked `-- SPLIT-SITE (i)`.

### F11 s 240AA(2) `s 240AA(2) the person must not publish or disseminate the document` (split site (i), three sites, and one failed "if")
Text: "A person must not publish or disseminate, whether in Singapore or elsewhere, any document relating to any offer or intended offer of any relevant securities ..., being an offer that is, or an intended offer that will be, made in or accompanied by a prospectus or profile statement that complies with section 240, if the document resembles or may otherwise be confused with a product highlights sheet, unless the person is required to do so".
Read: NOTHING when the person publishes nothing, when the securities are not relevant securities, and when the document does not relate to an offer or intended offer made in or with a prospectus or profile statement that complies with section 240 (`inputs/ENCODING-GUIDE.md:87`, "limits a grant or prohibition in its own wording and the case falls outside the limit").
JUST FALSE when the document does not resemble a product highlights sheet: the text introduces the resemblance with "if" (`inputs/ENCODING-GUIDE.md:86`, "a condition the text introduces with \"if\""), the reading (a) of the brief's lawyer question, so the line is also marked `-- MARGINAL-READING (a)`.
"unless the person is required to do so" under (a), (b) or (c) is a closed gate: JUST FALSE.
Other reading: JUST FALSE at the three limits; NOTHING at the "if" (the "if" then only says which documents the bar is about, not that others are free to be published).
Flip: the four lines marked `-- SPLIT-SITE (i)`.

### F12 s 240AA(4) `s 240AA(4) the person is guilty of an offence` (split site (i))
Text: "Any person who contravenes subsection (1) or (2) shall be guilty of an offence".
Read: JUST TRUE when s 240AA(1) or s 240AA(2) answers JUST TRUE for the person; NOTHING when both answer JUST FALSE ("who contravenes" is the offence's own wording and the text does not say that anyone else is not guilty: `inputs/ENCODING-GUIDE.md:87`); NOTHING when an answer was not worked out.
Other reading: JUST FALSE when both answer JUST FALSE.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F13 s 240AA(5) `s 240AA(5) "structured notes" the debentures or units of debentures are structured notes` (an ambiguity of the rendering, not a split site)
Text: after paragraph (b)(iv) the rendering prints a second line labelled "(b)": "in accordance with a formula based on one or more of the following:", then four variables numbered (v) to (viii).
Read: the "(b)" label there is a rendering artefact and the words are the tail of paragraph (b): the payment or delivery in (b)(i) to (iv) must be "in accordance with a formula based on one or more of" the four variables.
So a debenture is structured notes only if (a), (b) and the formula tail are all met; the combiner takes the three answers and a debenture or unit of debentures.
Other reading 1: a second paragraph (b) that is an alternative to the first, so that a payment term OR a formula suffices (a disjunction, in place of the conjunction taken).
Other reading 2: the tail qualifies only (b)(iv).
Flip: the third branch of the combiner (the conjunction of the three answers) and the second branch (the JUST FALSE when any limb is JUST FALSE).
(b)(iv), "2 or more of sub-paragraphs (i), (ii) and (iii) apply", adds nothing to the "or" of (i), (ii) and (iii); it is computed anyway, so the text is followed.

### F14 s 240AB(5) `s 240AB(5) the person is guilty of an offence` (split site (i))
Text: "Any person who contravenes any condition or restriction imposed under subsection (1), (2) or (3) shall be guilty of an offence".
Read: JUST TRUE when the person contravenes a condition or restriction; otherwise NOTHING, because the text defines the offence by the relative clause "who contravenes" and does not say that anyone else is not guilty (`inputs/ENCODING-GUIDE.md:87`, "limits a grant or prohibition in its own wording and the case falls outside the limit").
Other reading: JUST FALSE for a person who does not contravene.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F15 s 240A(9) `s 240A(9) the Authority may register the pricing statement on the day` (split site (ii); and the day of lodgment)
Text: "a pricing statement may be registered by the Authority at any time after its lodgment with the Authority".
Read: JUST FALSE on a day before the date of lodgment: a "may" gated by a time, which the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md:93`, "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"), reaches by analogy; the grant line (`inputs/ENCODING-GUIDE.md:99`) lists "a \"may\" function whose gate is \"where\", \"when\" or \"upon\"" for a lawyer.
Other reading: NOTHING on a day before lodgment (a function named for a power whose gate failed).
Date granularity: a registration on the day of lodgment, later in the day, is "at a time after its lodgment", so the day counts (AT LEAST the date of lodgment), as in s 240(8) (F9).
Other reading of the day: only a later day counts (the keel's P2: the day of the event is not counted).
Flip: the line marked `-- SPLIT-SITE (ii)`; the comparison `AT LEAST` in the condition.

### F21 s 240AA(5) `s 240AA(5) "structured notes" (a) the debentures are issued in relation to a transaction and by a specified financial institution` (the raw text's "or")
Text (the rendering, lines 38927 to 38940): "(a) which is issued — (i) in relation to — (A) a synthetic securitisation transaction; or (B) such other arrangement or transaction as the Authority may prescribe by regulations made under section 341; or (ii) by a specified financial institution; and (b) for which —".
Read: the three alternatives are joined by "or", as printed: debentures are within paragraph (a) if they are issued in relation to a synthetic securitisation transaction, or in relation to a prescribed arrangement, or by a specified financial institution.
Other reading: "(i) ... and (ii) ..." (both needed: a transaction of the kind in (A) or (B) AND an issuer that is a specified financial institution), which is how the sub-paragraph numbering (i) and (ii) reads.
Effect: under the other reading a note issued by a specified financial institution that is not tied to a synthetic securitisation transaction or a prescribed arrangement is not a structured note.
Flip: the first two branches of the function (JUST TRUE on any one of the three; JUST FALSE only when all three are shown absent).

### F16 s 241(1) `s 241(1) the person making the offer may lodge a supplementary or replacement document` (the grant ruling of 2026-11-12, limit (1))
Text: "If, after a prospectus or profile statement is registered but before the close of the offer ... the person making that offer becomes aware of — (a) ...; (b) ...; or (c) ..., and that is materially adverse from the point of view of an investor, the person may lodge a supplementary or replacement prospectus ... with the Authority".
Read: NOTHING when the gate fails (a function named for a power; `inputs/ENCODING-GUIDE.md:99`, limit 1: "answer `NOTHING` ... only for a function named for a grant or a power ... whose `if` gate failed").
Other reading: JUST FALSE ("If" is a condition the text introduces, `inputs/ENCODING-GUIDE.md:86`).
The rendering prints paragraph (c)(ii) twice, once as the introduction of (A) and (B) ("would have been required by") and again as "(ii) if it had arisen before the prospectus or the profile statement ... was lodged"; the second is read as the tail of the first, and the function has one input for it.
Flip: the line marked `-- GRANT-RULING (1)`.

### F17 s 241(1A) `s 241(1A) the person making the offer may lodge a supplementary or replacement document for a base prospectus or base profile statement` (grant ruling, and a proviso)
Text: "If, after a base prospectus ... is registered but before the expiration of 24 months from the registration ..., the person making that offer intends to update any information ..., the person may lodge a supplementary or replacement document with the Authority, provided that no offer to which the base prospectus or base profile statement relates is subsisting at the time of the lodgment."
Read: NOTHING when the "If" gate fails (grant ruling, limit (1)); JUST FALSE when an offer is subsisting, because "provided that" closes the grant itself (limit (2), "keep `JUST FALSE` where the text closes the gate itself").
"Before the expiration of 24 months from the registration" is counted as not later than the last day of 24 months after the registration (the keel's P1 and P2; the day the period ends is in time).
Other reading: NOTHING for the proviso too (a limit on a grant, not a closed gate); and strictly before the last day.
Flip: the second branch; the date comparison.

### F18 s 241 duties whose "if", "where" or scope clause is unmet (the Guide's six site-by-site questions, `inputs/ENCODING-GUIDE.md:95`: "a duty whose \"if\" or \"where\" is unmet")
Sites (each answers NOTHING, "limited by its own wording", when the clause is unmet; the other reading at every site is JUST FALSE):
- s 241(2) `s 241(2) the supplementary document begins as it must`: "At the beginning of a supplementary document" (scope: a supplementary document).
- s 241(3) `s 241(3) the replacement document begins as it must`: "At the beginning of a replacement document" (scope).
- s 241(4) `s 241(4) the document is dated with the date on which it is lodged`: "The supplementary document and the replacement document" (scope).
- s 241(5) `s 241(5) the person making the offer has taken the reasonable steps`: "of any supplementary or replacement document under subsection (1) or (1A)" (scope: a lodgment).
- s 241(7) `s 241(7) the offer has been kept open for at least 14 days after the lodgment`: "If a supplementary document or replacement document is lodged" (an "If" on a duty).
- s 241(10), (11), (13), (14) the four applicant functions: "An applicant who wishes to exercise the applicant's option" (a relative clause, a scope limit with no "only": periods ruling, rule (c), NOTHING).
Count: 9 sites.
Two groups the Guide settles and that are listed here for the maintainer (no change made): the paragraphs of s 241(8) and (12) that begin "where" answer JUST FALSE as "the person is bound by the paragraph" (periods ruling, rule (b), 4 sites); the four payment functions of s 241(10), (11), (13), (14) ("upon which that person must", "upon" counts as "where", `inputs/ENCODING-GUIDE.md:94`) answer JUST FALSE when the applicant has not notified the person, so that JUST FALSE there means "not paid, or nothing was due".

### F19 s 241(15) `s 241(15) the person is guilty of an offence` (split site (i))
Text: "Any person who contravenes subsection (8) or (12) shall be guilty of an offence".
Read: JUST TRUE when for one of the four paragraphs the person is bound (JUST TRUE) and has not met it (JUST FALSE); NOTHING when for each paragraph the person is not bound or has met it ("who contravenes" is the offence's own wording, `inputs/ENCODING-GUIDE.md:87`); NOTHING when an answer was not worked out.
Other reading: JUST FALSE when no paragraph is contravened.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F20 s 241(16) `s 241(16) the person is guilty of an offence` (split site (i))
Text: "Any person who contravenes any other provision of this section shall be guilty of an offence".
Read: JUST TRUE when the list of answers of the duty functions holds a JUST FALSE; otherwise NOTHING (`inputs/ENCODING-GUIDE.md:87`).
The list holds the answers for subsections (2), (3), (4), (5), (7), (10), (11), (13), (14); subsection (1), (1A), (1B), (1C), (6), (6B), (9), (17) state powers, deemings and readings and have no duty to contravene.
Other reading: JUST FALSE when the list holds no JUST FALSE.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F22 s 242(1), (2) and (8) the Authority's powers (the grant ruling of 2026-11-12, limit (1))
Functions: `s 242(1) the Authority may serve a stop order on the person making the offer for the prospectus`, `s 242(2) ... for the profile statement`, `s 242(8) the Authority may serve an interim stop order without giving an opportunity to be heard`.
Text: "If a prospectus has been registered and — (a) ...; (b) ...; (c) ...; or (d) ..., the Authority may by a written order (called in this section a stop order) served on the person making the offer"; "If the Authority is of the opinion that any delay ... the Authority may, without giving an opportunity to be heard, serve an interim stop order".
Read: NOTHING when the "if" gate fails, for each of the three (`inputs/ENCODING-GUIDE.md:99`, limit 1: "answer `NOTHING` ... only for a function named for a grant or a power ... whose `if` gate failed").
Other reading: JUST FALSE at each (`inputs/ENCODING-GUIDE.md:86`, a condition the text introduces with "if").
The opinions of the Authority are inputs.
Flip: the lines marked `-- GRANT-RULING (1)` (3 sites).

### F23 s 242(3) `s 242(3) the Authority must not serve a stop order` (split site (i), and a failed "if")
Text: "Despite subsections (1) and (2), the Authority must not serve a stop order if any of the securities or securities-based derivatives contracts to which the prospectus or profile statement relates has been issued or sold, and listed for quotation on an approved exchange and trading in them has commenced."
Read: JUST TRUE when all three facts hold; JUST FALSE otherwise: the "if" is the bar's own condition (`inputs/ENCODING-GUIDE.md:86`, "a condition the text introduces with \"if\""), the reading (a); so the line is also marked `-- MARGINAL-READING (a)`.
Other reading: NOTHING otherwise (the bar is limited by its own wording and the text does not say that the Authority may serve in any other case: `inputs/ENCODING-GUIDE.md:87`).
Flip: the line marked `-- SPLIT-SITE (i)`.

### F24 s 242(9) `s 242(9) the interim stop order is in force` (an ambiguity of the rendering, and a count)
Text: "(a) in a case where — (i) it is served during a hearing under subsection (4); or (ii) a hearing under subsection (4) is commenced while it is in force, (a) until the Authority makes an order under subsection (1) or (2); and (b) in any other case, for a period of 14 days from the day on which the interim stop order is served."
The rendering prints the label "(a)" twice (once for the case, once for "until"); the first is read as the case and the second as the first limb of the case's duration.
Read: in the hearing case the order is in force until the Authority makes an order (JUST TRUE before, JUST FALSE after: the Guide's ruling (d) on "until" bars, `inputs/ENCODING-GUIDE.md:94`); in any other case for 14 days beginning with the day it is served (the keel's P10: "for a period of 14 days from the day" counts the day of service as day 1, so the last day is the 14th day counted from it).
Other reading for the count: the keel's P1 (the day of service is not counted, so the last day is service plus 14).
Other reading for the structure: the "(a)" and "(b)" are two cases and the hearing case has no end date.
Flip: the last branch (`period: the last day of a period beginning with`, in place of `period: the last day of a period after`).

### F25 s 242(11) `s 242(11) the person is guilty of an offence` (split site (i))
Text: "Any person who fails to comply with a stop order served under subsection (1) or (2) or an interim stop order served under subsection (8) shall be guilty of an offence".
Read: JUST TRUE when the person fails to comply with either; otherwise NOTHING ("who fails" is the offence's own wording: `inputs/ENCODING-GUIDE.md:87`).
Other reading: JUST FALSE for a person who complies.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F26 s 242(12) `s 242(12) the person is guilty of an offence` (split site (i))
Text: "Any person who contravenes subsection (5) or (7) shall be guilty of an offence".
Read: JUST TRUE when for one of paragraphs (5)(a), (5)(b), (7)(a), (7)(b) the person is bound (JUST TRUE) and has not paid or informed as it requires (JUST FALSE); NOTHING when no paragraph is contravened (`inputs/ENCODING-GUIDE.md:87`); NOTHING when an answer was not worked out.
Other reading: JUST FALSE when no paragraph is contravened.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F18 (addendum) s 242 sites of the same kind
- s 242(4) `s 242(4) the Authority must give the person making the offer an opportunity to be heard`: "under subsection (1) or (2)" (scope: a stop order to be served) answers NOTHING outside it.
- s 242(7)(b)(i) and (ii): "if documents purporting to evidence title ... have been issued" and "if no such documents have been issued" each answer NOTHING when its "if" is unmet.
- s 245(2)(b) `s 245(2)(b) the prospectus contains the statement of total assets and total liabilities`: "where an entity specifies in a prospectus ... that it reserves the right" (a "where" on a duty to contain).
- s 243(4) `s 243(4) regard has been had to the matters`: "In deciding what information must be included under subsection (1)(a)" (scope).
- s 246(1) and (2), s 243(1), s 243(2), s 243(8): the scope "A profile statement for an offer", "A prospectus for an offer", "in relation to a business trust" answers NOTHING outside it (six sites of scope limits, rule (c)).
Count of F18 sites with s 241 and s 242: 12 + 2 (s 245(2)(b), s 243(4)) = 14 duties whose "if", "where" or scope is unmet, and six scope sites in ss 243 and 246.
The paragraphs of s 242(5) and (7) that begin "where" answer JUST FALSE as "the person is bound by the paragraph" (rule (b)): 4 gates.

### F27 s 245(1) `s 245(1) the entity must not accept or retain the subscriptions` (split site (i))
Text: "An entity must not accept or retain subscriptions to a debenture issue in excess of the amount of the issue as disclosed in the prospectus unless the entity has specified in the prospectus (a) ... and (b) ... not more than 25% in excess of the amount of the issue".
Read: NOTHING when the body is not an entity or accepts no excess (the bar is limited by its own wording, `inputs/ENCODING-GUIDE.md:87`); JUST FALSE when the prospectus reserves the right and states a limit not above 25% of the amount of the issue ("unless" closes the gate, `inputs/ENCODING-GUIDE.md:86`); JUST TRUE otherwise.
"not more than 25% in excess of the amount of the issue" is read as: the limit (the sum of over-subscriptions that may be kept) is at most 25% of the amount of the issue.
Other reading: JUST FALSE for a body that accepts no excess.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F28 s 245(2)(a) `s 245(2)(a) the entity must not make, authorise or permit the statement of asset-backing` (split site (i), a "where" gate, an "other than", and a pointer outside the text)
Text: "Subject to regulations made by the Authority for the purposes of this subsection, where an entity specifies in a prospectus ... that it reserves the right to accept or retain over-subscriptions — (a) the entity must not make, authorise or permit any statement of or reference as to the asset-backing ... other than a statement or reference to the total tangible assets and the total liabilities of the entity and of its guarantor entities".
Read: NOTHING when regulations for the subsection apply (the text points outside itself); JUST FALSE when the "where" gate fails (the periods ruling of 2026-11-05, rule (b)); NOTHING when no statement of asset-backing is made (the bar is limited by its own wording, `inputs/ENCODING-GUIDE.md:87`); JUST FALSE when the statement is only the permitted kind ("other than", one of the Guide's six site-by-site questions, `inputs/ENCODING-GUIDE.md:95`: "\"(other than X)\""); JUST TRUE otherwise.
Other reading: JUST FALSE for a body that makes no statement; "other than" read as NOTHING.
Flip: the lines marked `-- SPLIT-SITE (i)`.

### F29 s 245(3) `s 245(3) the person is guilty of an offence` (split site (i))
Text: "Every entity or other person that contravenes subsection (1) or (2) shall be guilty of an offence".
Read: JUST TRUE when (1) answers JUST TRUE, or (2)(a) answers JUST TRUE, or (2)(b) answers JUST FALSE (the prospectus lacks the statement); NOTHING otherwise (`inputs/ENCODING-GUIDE.md:87`: "who contravenes" is the offence's own wording).
Other reading: JUST FALSE when none is contravened.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F30 s 246(2) `s 246(2) the profile statement contains something it must not contain` (split site (i))
Text: "A profile statement must not contain — (a) any statement that is false or misleading ...; (b) any material information that is not contained in the prospectus; and (c) any material information that differs in any material particular from that set out in the prospectus."
Read: JUST TRUE when the profile statement contains any of the three; NOTHING when it contains none (`inputs/ENCODING-GUIDE.md:87`, "limits a grant or prohibition in its own wording").
Other reading: JUST FALSE when it contains none.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F31 s 247(5) `s 247(5) the person is guilty of an offence` (split site (i))
Text: "Any person who contravenes any of the conditions or restrictions imposed under subsection (1) or (3) shall be guilty of an offence".
Read: JUST TRUE when the person contravenes; otherwise NOTHING (`inputs/ENCODING-GUIDE.md:87`).
Other reading: JUST FALSE for a person who does not contravene.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F32 s 248(2), (4) and (5) the Authority's powers (the grant ruling of 2026-11-12, limit (1); and "so long as")
Functions: `s 248(2) the Authority may exempt the entity from the requirements` ("if it considers those requirements unduly burdensome"), `s 248(4) the Authority may permit a duly authorised agent to sign` ("In the event that no director ... is resident in Singapore"), `s 248(5) the Authority may grant the exemption applied for` ("if satisfied").
Read: NOTHING when the "if" or "in the event" gate fails (`inputs/ENCODING-GUIDE.md:99`, limit 1).
Read at s 248(4): "so long as such authorisation is supported by a resolution of the board" closes the grant itself: JUST FALSE when there is no resolution (limit 2, "keep `JUST FALSE` where the text closes the gate itself", and `inputs/ENCODING-GUIDE.md:86`, "as long as").
Other reading: JUST FALSE at the "if" sites; NOTHING at the "so long as".
Flip: the lines marked `-- GRANT-RULING (1)` (3 sites).

### F33 s 249(2) `s 249(2) the person is guilty of an offence` (split site (i), a failed "If" and a person limit)
Text: "If any prospectus or profile statement is issued in contravention of subsection (1), the person making the offer and every person who is knowingly a party to the issue thereof shall be guilty of an offence".
Read: JUST FALSE when nothing is issued, or the bar of subsection (1) is answered JUST FALSE (the text introduces the case with "If", `inputs/ENCODING-GUIDE.md:86`; reading (a) of the lawyer's question, marked `-- MARGINAL-READING (a)`); NOTHING when the bar's answer was not worked out; JUST TRUE for the person making the offer and for a person knowingly a party; NOTHING for any other person (the text names the persons liable and says nothing of anyone else, `inputs/ENCODING-GUIDE.md:87`).
Other reading: JUST FALSE for any other person; NOTHING at the "If".
Flip: the two lines marked `-- SPLIT-SITE (i)`.

### F34 s 249(4) and s 251(15) the offences of contravening a condition (split site (i), two sites)
Text: "Any person who contravenes any of the conditions or restrictions imposed under subsection (3) [or (14)] shall be guilty of an offence".
Read: JUST TRUE when the person contravenes; NOTHING otherwise (`inputs/ENCODING-GUIDE.md:87`).
No imprisonment is stated, so the penalty function says 0 months and "both" FALSE.
Other reading: JUST FALSE for a person who does not contravene.
Flip: the lines marked `-- SPLIT-SITE (i)` at s 249(4) and s 251(15).

### F35 s 249A(3) `s 249A(3) the person is guilty of an offence` (split site (i), a failed "If" and a person limit)
The same reading as F33, for a prospectus issued in contravention of subsection (1) or (2) of s 249A.
JUST FALSE needs both answers JUST FALSE (or nothing issued); an answer not worked out gives NOTHING.
Flip: the two lines marked `-- SPLIT-SITE (i)`.

### F36 s 250(1) and (2) the bars on using an expired prospectus (split site (i), a "where" gate, and the period)
Text: "(1) A person must not make an offer ..., or allot, issue or sell any securities ..., on the basis of a prospectus or profile statement after the expiration of the period referred to in subsection (3)." "(2) In a case where an entity makes an offer ... an officer or equivalent person or a promoter ... must not authorise or permit — (a) the offer ...; or (b) the allotment, issue or sale ... on the basis of a prospectus or profile statement after the expiration of the period".
Read: NOTHING when the person does none of the acts the bar names (`inputs/ENCODING-GUIDE.md:87`); JUST FALSE within the period ("a period the text fixes in its own words", `inputs/ENCODING-GUIDE.md:93`, rule (a)); at s 250(2) JUST FALSE when the "In a case where" gate fails (rule (b)); JUST TRUE after the period.
The last day of the period is the date of registration plus 24 months (a debenture issuance programme, with the base prospectus) or 6 months (any other case), by the keel's months; "after the expiration" means later than that last day, so a sale on it is within the period.
Other reading: JUST FALSE for a person who does none of the acts; NOTHING for a day outside the period.
Flip: the lines marked `-- SPLIT-SITE (i)` (2 sites).

### F37 s 250(4) `s 250(4) the person is guilty of an offence` (split site (i), a failed "If")
Text: "If default is made in complying with subsection (1) or (2), the person and, in the case of an entity or a proposed entity, every officer or equivalent person or promoter of the entity or proposed entity shall be guilty of an offence".
Read: JUST TRUE when (1) or (2) is breached, or the person is an officer or promoter of an entity in default; JUST FALSE when both are answered JUST FALSE (the text opens with "If", `inputs/ENCODING-GUIDE.md:86`, reading (a), marked `-- MARGINAL-READING (a)`); NOTHING when an answer was not worked out.
Other reading: NOTHING at the "If".
Flip: the line marked `-- SPLIT-SITE (i)`.

### F38 s 251(1) and (12) the bar on advertising and its offence (split site (i), three sites, and one failed "If")
Text: "If a prospectus is required for an offer or intended offer ..., a person must not — (a) advertise the offer or intended offer; or (b) publish a statement that — (i) directly or indirectly refers to the offer ...; or (ii) is reasonably likely to induce persons to subscribe for or purchase the securities ..., unless the advertisement or publication is authorised by this section."
Read: JUST FALSE when no prospectus is required (the text introduces the bar with "If", `inputs/ENCODING-GUIDE.md:86`, reading (a), marked `-- MARGINAL-READING (a)`); NOTHING when the person does none of the three acts (`inputs/ENCODING-GUIDE.md:87`); JUST FALSE once the act is authorised by the section or the person is exempt under subsection (14) ("unless" closes the gate, and only an answer JUST TRUE counts); JUST TRUE otherwise.
At s 251(12): JUST TRUE for a person who contravenes subsection (1) or who knowingly authorises or permits the publication; NOTHING for any other.
Other reading: JUST FALSE at the NOTHING sites.
Flip: the lines marked `-- SPLIT-SITE (i)` (3 sites).

### F39 s 251(3), (4)(a), (4)(b), (6), (8) the windows "before" and "after" registration (split site (ii), five sites)
Text: "a person may, before a prospectus or profile statement is registered by the Authority, disseminate a preliminary document ...", "a person does not contravene subsection (1) — (a) by presenting, before a prospectus or profile statement is registered ...", "Before a prospectus or profile statement is registered, an advertisement or publication does not contravene subsection (1) if it contains only the following", "After a prospectus or profile statement is registered with the Authority, an advertisement or a publication does not contravene subsection (1) if —".
Read: outside the window the route answers JUST FALSE, the "when" of a "may" read as a "where" (the periods ruling, rule (b), `inputs/ENCODING-GUIDE.md:93`, with "when" counted as "where", `inputs/ENCODING-GUIDE.md:94`).
The Guide asks that a "may" function gated by "where", "when" or "upon" be listed here for the maintainer, with a count, and that its ruling stay as it is (`inputs/ENCODING-GUIDE.md:99`, item 3).
s 251(3) is a literal "may"; the other four are "does not contravene" routes and are counted with it for the same reason.
Other reading: NOTHING outside the window ("the 'In short' line on grants points the other way").
Count: 5 sites.
Flip: the lines marked `-- SPLIT-SITE (ii)`.

### F40 s 251(5) to (11) and "authorised by this section": the safe harbours and their combiner
Read: each route that says a person "may" disseminate or "does not contravene subsection (1) if" answers JUST TRUE when its conditions are met and NOTHING when its plain "if" is unmet (the grant ruling of 2026-11-12, `inputs/ENCODING-GUIDE.md:99`, limit 1: a function named for a power whose "if" gate fails answers NOTHING).
A scope limit with no "only" (a lodged document, a registered prospectus, a report published by one of the named persons) gives NOTHING (`inputs/ENCODING-GUIDE.md:93`, rule (c)).
The persons list of s 251(4)(b) and the "sole purpose" are closed ("the following", "sole"): JUST FALSE.
Subsection (11) answers JUST FALSE for paragraphs (9)(e) and (f) when consideration is given ("does not apply ... if"); otherwise it says nothing (NOTHING).
"authorised by this section" is not defined; the combiner reads it as any one of the nine routes of subsections (3) to (10) answered JUST TRUE, and otherwise answers NOTHING (an undefined term).
Subsection (3)'s "Despite subsection (6)" changes no answer: the two routes are separate functions and the combiner takes either.
Other reading: JUST FALSE at the unmet plain "if" of each route; JUST FALSE from the combiner when every route is answered JUST FALSE.
Flip: the lines marked `-- GRANT-RULING (1)` (1 site, s 251(3)) and the NOTHING branches of the routes.

### F41 s 251(2) `s 251(2) regard has been had to the three matters`
Text: "In determining whether a statement — (a) indirectly refers to an offer ...; or (b) is reasonably likely to induce persons ..., regard must be had to whether the statement — (c) forms part of the normal advertising ...; (d) communicates information that materially deals with the affairs of the entity or the business trust; and (e) is likely to encourage investment decisions".
Read: a duty on whoever determines, with the gate "In determining" (NOTHING when no determination is made, `inputs/ENCODING-GUIDE.md:95`, "a duty whose \"if\" or \"where\" is unmet"); JUST TRUE when regard is had to all three; JUST FALSE otherwise ("a bare \"must\" not done", same line).
The text does not say how the three matters weigh, so no function gives a verdict on the statement from them.
Other reading: NOTHING when regard is not had to all three.
Flip: the line `OTHERWISE JUST FALSE` of that function.

### F42 s 251(18), (18A) and (19) meanings that include, close or point outside
s 251(18) and (19): for a corporation the affairs "include" the matters in section 2(2), so a matter outside them is NOTHING (`inputs/ENCODING-GUIDE.md:87`, "includes"); "in any other case, is a reference to such matters as the Authority may prescribe" closes the meaning, so a matter the Authority has not prescribed is JUST FALSE (`inputs/ENCODING-GUIDE.md:86`, a flat meaning).
s 251(18A): "exempt financial adviser", "financial advisory service" and the second limb of "representative" take their meanings from section 2(1) of the Financial Advisers Act 2001, which this text does not contain: NOTHING when the meaning is not shown ("points outside the sources").
Other reading: NOTHING at the closed meaning ("is a reference to" read as saying only what the reference covers).
Flip: the two lines marked `-- FALSE-kind` at s 251(18) and (19).

### F43 s 252(2) `s 252(2) the person is guilty of an offence` (split site (i))
Text: "Any person who contravenes subsection (1) shall be guilty of an offence and shall be liable on conviction to a fine not exceeding $50,000."
Read: JUST TRUE when s 252(1) is answered JUST FALSE (the duty arose and the notice was not given as soon as practicable); NOTHING otherwise (`inputs/ENCODING-GUIDE.md:87`).
s 252(1) has no regulative rule: "as soon as practicable" carries no number of days, so no trace can reach a breach by the clock; the function states whether the notice was given as soon as practicable, as a fact the person gives.
Other reading: JUST FALSE for a person who does not contravene.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F44 s 253(1) and s 254(1) the "Where" block of facts
Text: "Where an offer of securities or securities-based derivatives contracts is made in or accompanied by a prospectus or profile statement, or, in the case of an offer referred to in section 280, where a prospectus or profile statement is prepared and issued in relation to the offer, and — (a) a false or misleading statement is contained in ...; (b) there is an omission ...; or (c) there is an omission to state a new circumstance that ...".
Read: the whole block is one "Where": JUST TRUE when the offer is made and one of (a), (b), (c) holds ((c) needs both (i) and (ii)); JUST FALSE otherwise (the periods ruling, rule (b), `inputs/ENCODING-GUIDE.md:93`).
Other reading: NOTHING when (a), (b) and (c) are all unmet (the block as the facts of the case, not a gate).
Flip: the two FALSE-kind lines of `s 253(1) the false or misleading statement or omission is present` and `s 254(1) ...`.

### F45 s 253(2), s 254(2), s 254(4) deemings
Text: "a false or misleading statement about a future matter ... is taken to have been made if a person made the statement without having reasonable grounds" (s 254(2): "makes"); "A person who acquires ... as a result of an offer that was made in or accompanied by a profile statement is taken to have acquired ... in reliance on both".
Read: JUST TRUE when the deeming's conditions are met; NOTHING when they are not, because a deeming "if" only says when the deeming happens (`inputs/ENCODING-GUIDE.md:87`).
Other reading: JUST FALSE when the condition is unmet.
Flip: the three NOTHING-kind lines (s 253(2), s 254(2), s 254(4)).

### F46 s 253(3) `s 253(3) the person does not contravene subsection (1)`
Text: "A person does not contravene subsection (1) if the false or misleading statement, or the omission ..., is not materially adverse from the point of view of the investor."
Read: JUST TRUE when it is not materially adverse; NOTHING otherwise (a safe harbour: its plain "if" says when the person is safe and says nothing of when the person is not).
The offence function takes this answer, and only JUST TRUE counts.
Other reading: JUST FALSE when it is materially adverse.
Flip: the NOTHING-kind line.

### F47 s 253(4) and s 254(3) the persons guilty or liable
Text: "The persons guilty of the offence are — (a) ... (g)" and "The persons liable are — (a) ... (f)".
Read: one function per paragraph; a paragraph that begins "where" answers JUST FALSE when the "where" fails (rule (b)); a paragraph limited by "but only in respect of the inclusion of" answers JUST FALSE for a charge that is not for the inclusion (a list the text closes with "only", `inputs/ENCODING-GUIDE.md:86`); otherwise NOTHING when the person is none of the kind the paragraph names.
The combiner answers JUST TRUE when any paragraph is JUST TRUE and otherwise NOTHING: the list "are" is not closed with "only" (`inputs/ENCODING-GUIDE.md:87`, "lists without closing the list").
"controlled by" and "related party" (s 253(4)(c), s 254(3)(c)) are keel concepts: the seat computes them, layer 1 takes one BOOLEAN.
At s 253(4)(d), (e) the "if" before (i), (ii), (iii) is a plain "if" that closes nothing: NOTHING when none of the three is met.
Other reading: JUST FALSE from the combiner when no paragraph holds.
Flip: the `list not closed` line of each combiner (2 sites) and the `only` lines (4 sites: s 253(4)(f), (g), s 254(3)(e), (f)).

### F48 the combiners of s 253(4) and s 254(3): see F47.

### F49 s 253(1) `s 253(1) the person is guilty of an offence` (split site (i))
Text: "the persons referred to in subsection (4) shall be guilty of an offence even if such persons, unless otherwise specified, were not involved in the making of the false or misleading statement or the omission".
Read: JUST FALSE when the facts are answered JUST FALSE, when subsection (3) holds, or when a defence of section 255 is proved (only JUST TRUE counts for (3) and the defence); JUST TRUE when the facts and the person are both JUST TRUE; NOTHING for any other person (the text names the persons of subsection (4) and says nothing of anyone else, `inputs/ENCODING-GUIDE.md:87`).
Other reading: JUST FALSE for any other person.
Flip: the line marked `-- SPLIT-SITE (i)`.

### F50 s 253(5) `remedial action includes`, and "reckless"
s 253(5)(a): an "includes" list: JUST TRUE when one of the two is done, NOTHING otherwise (`inputs/ENCODING-GUIDE.md:87`).
s 253(5)(b): "a person is reckless ... if, having been put upon inquiry ..., the person fails to — (i) make all inquiries as are reasonable ...; and (ii) take such remedial action ... if such action is warranted by the outcome of the inquiries".
Read: JUST TRUE when put on inquiry and the person made no reasonable inquiries, or inquired, action was warranted and none was taken (a failure at either step); NOTHING otherwise (a plain "if" definition).
Other reading: only a person who fails at both steps is reckless.
Flip: the formula of `s 253(5)(b) the person is reckless`.

### F51 s 254(1) `s 254(1) the person is liable to compensate the claimant` (a jural relation)
Read: JUST TRUE when the facts hold, the person is one of subsection (3), the claimant suffers loss or damage as a result, and no section 255 defence is proved; JUST FALSE when the facts fail or a defence is proved; NOTHING when no loss is shown or the person is not shown to be one of subsection (3).
The claimant's claim-right and the person's duty to compensate are one relation (NOTES, "Jural relations").
Other reading: JUST FALSE when no loss is shown.

### F52 s 254(5) and s 260(8) the limitation periods
Text: "No action under subsection (1) may be commenced after the expiration of 6 years from the date on which the cause of action arose" and "No proceedings for the recovery of any compensation under subsection (7) may be commenced after the expiration of 2 years from the date of the allotment".
Read: a period fixed in the text's own words: JUST FALSE inside it (the action may be commenced), JUST TRUE after it (the bar bites): rule (a), `inputs/ENCODING-GUIDE.md:93`, as at s 250(1).
The last day is the event's date plus 6 years (2 years), by the keel's years; a proceeding on the last day is in time.
Other reading: NOTHING inside the period (the text says only that the action may not be commenced after it).
Flip: the JUST FALSE line of each of the two functions.

### F53 s 255 and the other defences: delegated defences
Text: "... is not liable ... if the person proves that the person — (a) made all inquiries ...; and (b) after doing so, believed on reasonable grounds ...", and the same shape at s 255(2), (3), (5), (6), s 259(4), s 260(6).
Read (`inputs/ENCODING-GUIDE.md:94`, (b)): JUST TRUE when the person proves what the paragraph asks; JUST FALSE when not, worded "this section gives no defence on these facts"; NOTHING when the person or the ground is outside the paragraph's scope ("only because of", the kind of person: a scope limit with no "only", rule (c)).
`s 255 the person has a defence` answers JUST TRUE if any paragraph does, JUST FALSE if every paragraph answers JUST FALSE ("this section gives no defence on these facts", never "no defence at all"), and NOTHING otherwise.
s 255(4) ("a person is not the agent of an entity or individual merely because ...") is a flat negative: JUST FALSE when the person merely performs the professional or advisory function.
Other reading: JUST FALSE for a person outside the scope.
Count: 8 sites in s 255, s 259(4), s 260(6).

### F54 s 257(1) `s 257(1) subsection (2) applies`
Text: "Subsection (2) applies where — (a) an entity allots or agrees to allot ... with a view to ... being subsequently offered for sale to another person; and (b) such offer ... does not qualify for an exemption under Subdivision (4) of this Division (other than section 280)".
Read: JUST FALSE when (a) fails (a "where", rule (b)) or the exemption is JUST TRUE; JUST TRUE when (a) holds and the exemption is JUST FALSE; NOTHING when the exemption's answer was not worked out.
The exemption of Subdivision (4) belongs to another part of the Act and is an input (a seam).
Other reading: NOTHING at the "where".

### F55 s 257(2), (4) the deemings
Read: JUST TRUE when subsection (1) holds and the document is the one by which the subsequent offer is made; JUST FALSE when (1) is JUST FALSE ("applies where"); NOTHING otherwise (`inputs/ENCODING-GUIDE.md:87`).
The saving "but without affecting the liability (if any) of the persons making the subsequent offer" is a flat negative: JUST FALSE for that liability, NOTHING for any other.
Count: 5 sites.

### F56 s 257(3) `s 257(3) it is sufficient evidence`
Text: "unless the contrary is proved, it is sufficient evidence that an allotment ... was made with a view to ... being subsequently offered for sale if it is shown — (a) that an offer ... was made within 6 months after the allotment ...; or (b) that at the date when the offer was made the whole consideration ... had not been so received".
Read: JUST FALSE when the contrary is proved ("unless"); JUST TRUE when (a) or (b) is shown; NOTHING otherwise (two ways are named and no more).
Other reading: JUST FALSE when neither way is shown.

### F57 s 258(2) `s 258(2) the bank has an obligation or duty to enquire`
Text: "There is no obligation or duty on any bank ... to enquire into or see to the proper application of those moneys, so long as the bank acts in good faith."
Read: JUST FALSE while the bank acts in good faith; NOTHING when it does not (the text says no duty "so long as" and does not say there is a duty otherwise).
Other reading: JUST TRUE when the bank does not act in good faith.

### F58 the offences of contravening a duty or bar in ss 258, 259 (split site (i), 4 sites)
s 258(3), s 259(8), s 259(12), s 259(1)(d): "Any person who contravenes subsection (1) [(7), (11)]" shall be guilty of an offence.
Read: JUST TRUE when the duty function answers JUST FALSE (or the bar answers JUST TRUE); NOTHING otherwise (`inputs/ENCODING-GUIDE.md:87`).
Other reading: JUST FALSE for a person who does not contravene.
Flip: the lines marked `-- SPLIT-SITE (i)`.

### F59 s 259(1) the trigger, the 3 days and the 6 weeks
Text: "(a) the permission is not applied for in the form required ... within 3 days from the date of the issue of the prospectus; or (b) the permission is not granted before the expiration of 6 weeks from the date of the issue ... or such longer period not exceeding 12 weeks as is, within those 6 weeks, notified to the applicant".
Read: "within 3 days from" counts the day of issue as in time (F9), so the last day is the issue date plus 3 days; the 6 weeks, or the notified longer period of 7 to 12 weeks, end on the issue date plus that many weeks; a notified period outside 7 to 12 weeks is not one the text allows and 6 weeks stands.
A failed "Where" (no statement or implication of an application to list) answers JUST FALSE (rule (b)); an application made in time, or permission granted in time, answers JUST FALSE as a failed "if" (`-- MARGINAL-READING (a)`).
Other reading: NOTHING at the failed "if"; a notified period beyond 12 weeks capped at 12.

### F60 s 259(1)(c) `s 259(1)(c) the allotment is void`
Text: "any allotment whenever made of securities ... made on an application pursuant to the prospectus is, subject to subsection (3), void".
Read: JUST TRUE when the trigger holds and the allotment was made on an application pursuant to the prospectus; JUST FALSE when the trigger is JUST FALSE or the Authority has exempted the allotment under subsection (3) (only JUST TRUE counts); NOTHING for an allotment not made on such an application.

### F61 s 259(1)(d) `s 259(1)(d) the person is guilty of an offence` (split site (i))
Text: "any person who continues to allot such securities ... after the period specified in paragraph (a) or (b), shall be guilty of an offence".
Read: JUST TRUE when the trigger holds and the person continues to allot after the period; NOTHING for an allotment not after the period (SPLIT-SITE (i)).
The "period specified in paragraph (a) or (b)" is an input: the last day of the period that was missed.

### F62 s 259(2)(a), (b) and s 260(5) the 14 days and the 5 months before interest runs
Text: "if any such moneys is not repaid within 14 days after the person making the offer so becomes liable to repay them, then (a) ... liable to repay those moneys with interest at the rate of 10% per annum from the expiration of such 14 days" and "If any money mentioned in subsection (4) is not repaid within 5 months after the issue of the prospectus, the directors ... are jointly and severally liable to repay that money with interest".
Read: repaid in time: JUST FALSE as a failed "if" (`-- MARGINAL-READING (a)`, `inputs/ENCODING-GUIDE.md:86`); not repaid in time: JUST TRUE; a director for whom the defence is JUST TRUE: JUST FALSE.
Other reading: NOTHING for money repaid in time.
Flip: the lines marked `-- MARGINAL-READING (a)` at s 259(1)(a), s 259(1)(b), s 259(2)(a) and s 260(5).

### F63 s 259(3) `s 259(3) the Authority may exempt the allotment` (split site (ii), a "may" gated by "Where")
Text: "Where in relation to any securities ... (a) permission is not applied for ...; or (b) permission is not granted ..., the Authority may, on the application of the issuer made before any of the securities ... is purported to be allotted, exempt the allotment".
Read: JUST FALSE when neither (a) nor (b) holds (rule (b), and the Guide's item 3 at `inputs/ENCODING-GUIDE.md:99`: listed for the maintainer); NOTHING when no application was made before any allotment (the grant ruling, limit 1); JUST TRUE otherwise.
Count: 1 site.
Other reading: NOTHING at the "Where".
The notice duty ("the Authority must give notice of such exemption in the Gazette") is a duty gated by the exemption having been given (F18).

### F64 s 259(6) the extensions
Text: "this section has effect (a) in relation to any securities ... agreed to be taken by a person underwriting an offer ... as if the person had applied therefor pursuant to the prospectus; and (b) in relation to a prospectus offering securities ... for sale as if a reference to sale were substituted for a reference to allotment".
Read: JUST TRUE when the securities are so agreed to be taken (the prospectus so offers); NOTHING otherwise (limited by its own wording).

### F65 s 259(9) `s 259(9) permission is deemed to have been granted`
Read: JUST FALSE when the exchange has not granted permission subject to compliance within the time ("Where"); JUST TRUE when the directors have given the written undertaking; NOTHING when they have not.

### F66 s 259(10) `s 259(10) the director is guilty of an offence` (split site (i), a failed "If")
Text: "If any such undertaking referred to in subsection (9) is not complied with, each director or equivalent person who is in default shall be guilty of an offence".
Read: JUST FALSE when the undertaking is complied with (`-- MARGINAL-READING (a)`); JUST TRUE for a director in default; NOTHING for any other person.
Flip: the two lines marked `-- SPLIT-SITE (i)`.

### F67 s 259(11) `s 259(11) the person must not issue the prospectus` (split site (i), two sites)
Read: NOTHING when no prospectus inviting subscriptions of an entity is issued; JUST TRUE for a false or misleading statement that permission was granted, or for a statement about permission or listing outside both exceptions; JUST FALSE when the statement is within an exception ("unless", a closed gate); NOTHING when the prospectus has no such statement.
Other reading: JUST FALSE at the two NOTHING sites.

### F68 s 259(13) `s 259(13) the prospectus is deemed to imply that application has been or will be made`
Read: JUST TRUE when the prospectus contains the statement and no contrary intention appears; JUST FALSE when the contrary intention appears ("unless", a closed gate); NOTHING when it has no such statement.

### F69 s 260(1) and (1A) the bar on allotment and the cheque rule
Text: "A person must not make an allotment of any securities ... unless — (a) the minimum subscription has been subscribed; and (b) the sum payable on application ... has been received", and "if a cheque ... has been received ..., the sum is treated as not having been received ... until the cheque is paid by the bank".
Read: NOTHING when the person makes no allotment of such securities (SPLIT-SITE (i)); JUST FALSE when (a) holds and (1A) says the sum is received (only JUST TRUE counts); JUST TRUE otherwise.
(1A): JUST FALSE for a sum received only by an unpaid cheque; JUST TRUE for cash or a paid cheque; NOTHING when no sum is shown.
Other reading: JUST FALSE for a person who makes no allotment.

### F70 s 260(2), (3) the calculation and the 5%
Read: a "must" not done is JUST FALSE (`inputs/ENCODING-GUIDE.md:95`, "a bare \"must\" not done"); s 260(3): the amount payable at least one twentieth of the price is JUST TRUE, below it JUST FALSE.

### F71 s 260(7) and (7A) the option to avoid
Text: "voidable at the option of the applicant, which option may be exercised by written notice served ... within one month after the holding of the statutory meeting of the company; or ... within one month after the date of the allotment".
Read: the option is a power with a window the text fixes in its own words: JUST FALSE outside it (rule (a)); the window runs from the statutory meeting when the company must hold one and the allotment was made before it, and from the allotment otherwise; one month by the keel's months, last day included.
Other reading: NOTHING outside the window.

### F72 s 260(7B), (7C), (7D) offences with no stated penalty, and the money liabilities
Read: JUST TRUE for the trustee-manager that contravenes, and for a director who knowingly contravenes or permits or authorises it; NOTHING otherwise (SPLIT-SITE (i), 3 sites).
The liabilities "(a) to pay into the trust property ...; (b) to compensate the allottee" are JUST TRUE for a person of the right kind where the loss is shown, and NOTHING otherwise.
No penalty function: the text says only "in addition to the penalty or punishment for the offence".

### F73 s 260(8) reads "compensation under subsection (7)"
Subsection (7) provides no compensation; subsections (7B), (7C) and (7D) do. The function reads (8) as covering the compensation of (7B) to (7D).
Other reading: (8) applies to nothing (no proceedings are "under subsection (7)").

### F74 the time-limited duties of ss 241, 242, 249 and 249A written as rules (`sfac-duties.l4`)
Text: the person making the offer "must, within 7 days from the receipt of such notification, pay to the applicant all moneys paid by the applicant" (s 241(10), (11), (13), (14)); "within 14 days from the date of the stop order, pay to the applicants" (s 242(5)(a)(ii), (5)(b)(ii), (7)(a)(ii)) or "within 7 days" where no title documents were issued (s 242(7)(b)(ii)); "within 7 days after the registration" the copies of the consents are to be deposited (s 249(1A), s 249A(4)).
Read: each is a `PARTY ... MUST ... WITHIN n` rule over an action, so that a trace can reach `BREACH` when the time runs out; the same duty is also the decision function of the same provision (`s N the person making the offer has paid ...`), which answers `JUST TRUE` done in time, `JUST FALSE` not done or late, `NOTHING` where the duty is not shown to arise (F18).
The rule's clock starts at AT 0 of the trace, which the caller sets to the day the time runs from (the receipt of the notification, the stop order, the registration), and an act on day n is in time (F9).
The text states a time limit and no consequence of its own for these duties; the rule's `LEST BREACH` says so and invents none (the consequences are the offences of other subsections, which are their own rules).
Other reading: no rule (the duty only as a decision function), under which no trace could show the duty breached; or `WITHIN n` counted from the day after the event (the keel's P2), under which an act on day n is late by none and an act on day n + 1 is in time.
Flip: the `WITHIN` number of each rule, and the comparison in the paired decision function (`AT MOST`) together.

### The grant and power name test (the Guide's ruling of 2026-11-12, `inputs/ENCODING-GUIDE.md:99`)

Limit (1): a function named for a grant or a power ("may", "is permitted to", "has power to") whose "if" gate failed answers `NOTHING`, with one fork line each.
The lines marked `-- GRANT-RULING (1)` are these 11 sites (found by `work/tags.py`):

- s 240(4) the offer may be made in or accompanied by a profile statement instead of a prospectus, `sfac-240.l4:143`
- s 241(1) the person making the offer may lodge a supplementary or replacement document, `sfac-241.l4:61`
- s 241(1A) the person making the offer may lodge a supplementary or replacement document for a base prospectus or base profile statement, `sfac-241.l4:84`
- s 242(1) the Authority may serve a stop order on the person making the offer for the prospectus, `sfac-242.l4:51`
- s 242(2) the Authority may serve a stop order on the person making the offer for the profile statement, `sfac-242.l4:81`
- s 242(8) the Authority may serve an interim stop order without giving an opportunity to be heard, `sfac-242.l4:378`
- s 248(2) the Authority may exempt the entity from the requirements, `sfac-243.l4:726`
- s 248(4) the Authority may permit a duly authorised agent to sign, `sfac-243.l4:761`
- s 248(5) the Authority may grant the exemption applied for, `sfac-243.l4:778`
- s 251(3) the person may disseminate the preliminary document without contravening subsection (1), `sfac-249.l4:670`
- s 259(3) the Authority may exempt the allotment, `sfac-257.l4:534`

Limit (3): a "may" function whose gate is "where", "when" or "upon" is not changed and is listed for the maintainer or a lawyer; the lines marked `-- SPLIT-SITE (ii)` are these 8 sites, answered `JUST FALSE` (the periods ruling, rule (b)); each has a fork line (see Split sites):

- s 240(8A) the Authority may proceed with the registration on the date, `sfac-240.l4:409`
- s 240A(9) the Authority may register the pricing statement on the day, `sfac-240aa.l4:628`
- s 251(3) the person may disseminate the preliminary document without contravening subsection (1), `sfac-249.l4:667`
- s 251(4)(a) the person does not contravene subsection (1) by presenting the material, `sfac-249.l4:713`
- s 251(4)(b) the person does not contravene subsection (1) by presenting the material to equip those persons, `sfac-249.l4:779`
- s 251(6) the advertisement or publication does not contravene subsection (1) before registration, `sfac-249.l4:901`
- s 251(8) the advertisement or publication does not contravene subsection (1) after registration, `sfac-249.l4:937`
- s 259(3) the Authority may exempt the allotment, `sfac-257.l4:531`

An "entitled"-named function: 0 (no function of this part is named for an entitlement).

The Guide's six site-by-site questions (`inputs/ENCODING-GUIDE.md:95`: "an \"unless\" or \"except\" once it is met; a bare \"must\" not done; \"listed in Schedule N\"; a duty whose \"if\" or \"where\" is unmet; \"(other than X)\"; a missing event in the state ledger") arise here as follows; the fork entries were found by searching the register for the words, and each fork line is the one entry named:

- "unless" or "except" once met: F4, F10, F11, F27, F38, F49, F56, F67, F68, F69 (the bars and the offences state their closed gate).
- a bare "must" not done, and a duty whose "if" or "where" is unmet: F18 (s 241), F41, F70; the "must" duties of ss 241, 242, 249 and 249A with a time limit are `JUST FALSE` when not done in time and are also written as rules (`sfac-duties.l4`).
- "listed in Schedule N": none in this part (no unit of the two ranges refers to a Schedule: `grep -c "Schedule" ` over the ranges is the check).
- "(other than X)": F28 (s 245(2)(a), "other than"), F54 (s 257, "other than section 280").
- a missing event in the state ledger: none (this part has no ledger).

## Jural relations (sfac)

Hohfeld's correlatives: a right (claim) is the other party's duty; a privilege (liberty) is the other party's no-right; a power is the other party's liability; an immunity is the other party's disability.
Each rule is stated once, as a relation between two parties, from the side of the holder.
Where the text makes a contravention an offence and names no claimant, the holder is "the State (no claimant is named)" and the correlative is a liability to the penalty; no party is invented.
The rows give the provisions that create a relation; the provisions that create none are listed once under the table.

| Provision | Holds the right, privilege, power or immunity | Bears the correlative | Kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 239(5) | the Authority (it imposes conditions or restrictions on a prescribed entity) | the prescribed entity | claim-right / duty to comply | `s 239(5) the prescribed entity must comply with the condition or restriction`, `s 239(5A) the prescribed entity shall not contravene a condition or restriction` |
| s 239(5A) | the State (the text makes the contravention an offence; no claimant is named) | the person who contravenes | power to punish / liability to the penalty | `s 239(5A) the person is guilty of an offence`, `s 239(5A) the penalty for the offence` |
| s 239A(1), (2) | the Authority (its Gazette order); the person making the offer of units in a business trust (the exclusion of (2)) | the persons making offers the order or the exclusion reaches (they are freed of this Division) | power (the order) / liability; immunity (the exclusion) / disability | `s 239A(1) the Authority's declaration disapplies this Division to the offer`, `s 239A(2) this Division does not apply to the offer of units or derivatives of units in a business trust` |
| s 240(1) | none named in the text | the person making the offer | duty not to offer without a registered prospectus / claim-right of the State, enforced by s 240(7) | `s 240(1) the person must not make the offer`, `s 240(1) the person shall not make the offer without a registered prospectus` |
| s 240(4) | the person making the offer (it may use a profile statement) | none named (no one may demand the full prospectus) | privilege / no-right | `s 240(4) the offer may be made in or accompanied by a profile statement instead of a prospectus` |
| s 240(5) | none named in the text | the person making an offer in respect of an entity or business trust not formed | duty / claim-right | `s 240(5) the person must not make the offer`, `s 240(5) the person shall not make an offer in respect of an entity or business trust not formed` |
| s 240(7), (17) | the State (offences; no claimant is named) | the person who contravenes | power to punish / liability to the penalty | `s 240(7) the person is guilty of an offence`, `s 240(17) the person is guilty of an offence` |
| s 240(8), (8A), (9) | the Authority (it registers, or must not) | the person making the offer | power to register / liability to registration or to a refusal | `s 240(8) the Authority may register the prospectus or profile statement on the day`, `s 240(8A) the Authority may proceed with the registration on the date`, `s 240(9) the Authority must not register the prospectus` |
| s 240(9A) | the person making the offer (it may lodge an amendment before registration) | the Authority | privilege / no-right | `s 240(9A) the person may lodge an amendment on the day` |
| s 240(12) | the Authority (it is to be given a copy) | the person making the offer | claim-right / duty to provide the copy | `s 240(12) the person making the offer must provide the Authority with a copy for publication` |
| s 240(13), (14), (15) | the person making the offer (an opportunity to be heard before a refusal) | the Authority | claim-right / duty to give the opportunity (and to refuse in the cases listed) | `s 240(15) the Authority must give the person making the offer an opportunity to be heard before refusing`, `s 240(13) the Authority must refuse to register the prospectus`, `s 240(14) the Authority must refuse to register the profile statement` |
| s 240(16) | the person making the offer (an appeal to the Minister within 30 days) | the Minister, whose decision is final | power / liability; the finality is a disability of the person to appeal further | `s 240(16) the person making an offer may appeal to the Minister`, `s 240(16) the Minister's decision on the appeal is final` |
| s 240AA(1), (2), (4) | none named in the text | the person making the offer; the person publishing or disseminating | duty / claim-right of the State; offence (4) as above | `s 240AA(1) the person shall not make the offer without a product highlights sheet`, `s 240AA(2) the person shall not publish or disseminate the document`, `s 240AA(4) the person is guilty of an offence` |
| s 240AA(3) | the Authority (it may publish a lodged product highlights sheet) | the person who lodged it | power / liability | `s 240AA(3) the Authority may publish the document for public information` |
| s 240AB(1) to (5) | the person exempted (an immunity from s 240AA); the Authority (the power to exempt and to set conditions) | the Authority (a disability to require the sheet); the exempted person (liability to the conditions) | immunity / disability; power / liability | `s 240AB(1) and (2) the person is exempt from the requirements in section 240AA`, `s 240AB(5) the person shall not contravene a condition or restriction`, `s 240AB(5) the person is guilty of an offence` |
| s 240A(9) | the Authority (it may register the pricing statement after its lodgment) | the person making the offer | power / liability | `s 240A(9) the Authority may register the pricing statement on the day` |
| s 241(1), (1A) | the person making the offer (it may lodge a supplementary or replacement document) | the Authority; the applicants (they take the option of (8)) | privilege / no-right; the lodgment triggers the options below | `s 241(1) the person making the offer may lodge a supplementary or replacement document`, `s 241(1A) the person making the offer may lodge a supplementary or replacement document for a base prospectus or base profile statement` |
| s 241(5) | potential investors (to be informed of the lodgment) | the person making the offer | claim-right / duty to take reasonable steps | `s 241(5) the person making the offer has taken the reasonable steps` |
| s 241(8), (12) | the applicant (the option to withdraw the application, or to return the securities) | the person making the offer | power / liability; and claim-right of the applicant to all moneys paid / duty to repay | `s 241(8)(a) the person making the offer is bound by paragraph (a)`, `s 241(8)(b) the person making the offer is bound by paragraph (b)`, `s 241(12)(a) the person making the offer is bound by paragraph (a)`, `s 241(12)(b) the person making the offer is bound by paragraph (b)` |
| s 241(10), (11), (13), (14) | the applicant (repayment within 7 days of the notification) | the person making the offer | claim-right / duty to pay | `s 241(10) the person making the offer has paid the applicant within 7 days from the receipt of the notification`, `s 241(11) the person making the offer has paid the applicant within 7 days from the receipt of the notification and documents`, `s 241(13) the person making the offer has paid the applicant within 7 days of the receipt of the notification`, `s 241(14) the person making the offer has paid the applicant within 7 days from the receipt of the notification and documents`, `s 241(10) the person making the offer must pay the applicant within 7 days from the receipt of the notification`, `s 241(11) the person making the offer must pay the applicant within 7 days from the receipt of the notification and documents`, `s 241(13) the person making the offer must pay the applicant within 7 days of the receipt of the notification`, `s 241(14) the person making the offer must pay the applicant within 7 days from the receipt of the notification and documents` |
| s 241(15), (16) | the State (offences; no claimant is named) | the person who contravenes | power to punish / liability to the penalty | `s 241(15) the person is guilty of an offence`, `s 241(16) the person is guilty of an offence` |
| s 242(1), (2), (8) | the Authority (it may serve a stop order, or an interim one) | the person making the offer | power / liability | `s 242(1) the Authority may serve a stop order on the person making the offer for the prospectus`, `s 242(2) the Authority may serve a stop order on the person making the offer for the profile statement`, `s 242(8) the Authority may serve an interim stop order without giving an opportunity to be heard` |
| s 242(3), (4) | the person making the offer (an opportunity to be heard before the stop order) | the Authority | claim-right / duty to give the opportunity | `s 242(4) the Authority must give the person making the offer an opportunity to be heard`, `s 242(3) the Authority must not serve a stop order` |
| s 242(5), (7) | the applicants (repayment of all moneys within 14 days, or 7 where no title documents were issued) | the person making the offer | claim-right / duty to pay | `s 242(5)(a)(ii) the person making the offer has paid the applicants within 14 days from the date of the stop order`, `s 242(7)(a)(ii) the person making the offer has paid the applicants within 14 days from the date of the stop order`, `s 242(7)(b)(ii) the person making the offer has paid the applicants within 7 days, where no title documents were issued`, `s 242(5)(a)(ii) the person making the offer must pay the applicants within 14 days from the date of the stop order (applications)`, `s 242(5)(b)(ii) the person making the offer must pay the applicants within 14 days from the date of the stop order (issue)`, `s 242(7)(a)(ii) the person making the offer must pay the applicants within 14 days from the date of the stop order (sale)`, `s 242(7)(b)(ii) the person making the offer must pay the applicants within 7 days from the date of the stop order where no title documents were issued` |
| s 242(11), (12) | the State (offences; no claimant is named) | the person who allots, issues or sells contrary to the order, and the person who contravenes (12) | duty / claim-right of the State (11); liability to the penalty (11), (12) | `s 242(11) the person making the offer shall not allot, issue or sell contrary to the order`, `s 242(11) the person is guilty of an offence`, `s 242(12) the person is guilty of an offence` |
| s 243(1) | none named in the text | the person making the offer (the prospectus must contain the information) | duty (no claimant named; s 253 and s 254 give the remedies) | `s 243(1) the prospectus contains what it must contain` |
| s 243(6) | the applicant | any person who relies on a condition that waives compliance | immunity / disability (the condition is void) | `s 243(6) the condition is void` |
| s 245(1), (2), (3) | none named in the text | the entity that accepts or retains over-subscriptions, or makes a statement of asset-backing | duty / claim-right of the State; offence (3) as above | `s 245(1) the entity shall not accept or retain over-subscriptions`, `s 245(2)(a) the entity shall not make, authorise or permit a statement of asset-backing`, `s 245(3) the person is guilty of an offence` |
| s 246(2) | none named in the text | the person making the offer (the profile statement must not contain what the text bars) | duty (no claimant named) | `s 246(2) the profile statement contains something it must not contain` |
| s 247(1), (3) | the Authority (it may exempt a person, a class or a document from a requirement of form or content) | the person or class exempted (liability to the conditions; (5) is the offence) | power / liability; immunity of the exempted person | `s 247(1) and (3) the person or document is exempt from the requirement of form or content`, `s 247(5) the person shall not contravene a condition or restriction`, `s 247(5) the person is guilty of an offence` |
| s 248(2), (4), (5) | the Authority (it may exempt a governmental or international entity, permit an agent to sign, grant the exemption applied for) | the entity | power / liability | `s 248(2) the Authority may exempt the entity from the requirements`, `s 248(4) the Authority may permit a duly authorised agent to sign`, `s 248(5) the Authority may grant the exemption applied for` |
| s 249(1), (1A), (2), (4) | the expert (no statement of the expert may be issued without written consent); the Authority (copies of the consents are to be deposited, and it may exempt under (3)) | the person who issues the prospectus; the person making the offer | claim-right / duty (consent; deposit within 7 days); power of consent | `s 249(1) the person shall not issue the prospectus or profile statement`, `s 249(1A) the person making the offer has deposited the copies of the consents`, `s 249(2) the person is guilty of an offence`, `s 249(4) the person shall not contravene a condition or restriction`, `s 249(1A) the person making the offer must deposit the copies of the consents within 7 days after the registration`, `s 249(3) the person or document is exempt from the section` |
| s 249A(1) to (4) | the issue manager and the underwriter (no one may name them in the prospectus without consent) | the person who issues the prospectus | claim-right / duty (consent); offence (3) as above | `s 249A(1) the person shall not issue the prospectus or profile statement`, `s 249A(2) the person shall not issue the prospectus or profile statement`, `s 249A(3) the person is guilty of an offence`, `s 249A(4) the person making the offer has deposited the copies of the consents`, `s 249A(4) the person making the offer must deposit the copies of the consents within 7 days after the registration (issue manager or underwriter)` |
| s 250(1), (2), (4) | none named in the text | the person who offers, allots, issues or sells on an expired prospectus; the officer or promoter who authorises or permits it | duty / claim-right of the State; offence (4) as above | `s 250(1) the person shall not make the offer or allot, issue or sell after the period`, `s 250(2) the officer or promoter shall not authorise or permit the offer, allotment, issue or sale after the period`, `s 250(4) the person is guilty of an offence` |
| s 250(5) | the allottee or buyer (the allotment, issue or sale is not void or voidable by reason only of the contravention) | any person who would avoid it | immunity / disability | `s 250(5) the allotment, issue or sale is void or voidable by reason only of the contravention` |
| s 251(1), (12), (15) | none named in the text | the person who advertises or publishes a statement before registration or after the period; offences (12), (15) as above | duty / claim-right of the State; liability to the penalty | `s 251(1) the person shall not advertise the offer or publish the statement`, `s 251(12) the person is guilty of an offence`, `s 251(15) the person shall not contravene a condition or restriction`, `s 251(15) the person is guilty of an offence` |
| s 251(3) to (11) | the person who disseminates within a safe harbour | none named (the bar of s 251(1) does not reach the case) | privilege / no-right | `s 251(3) the person may disseminate the preliminary document without contravening subsection (1)`, `s 251(5)(a) the person may disseminate the registered prospectus or profile statement`, `s 251(5)(b) the person may disseminate the product highlights sheet`, `s 251 the advertisement or publication is authorised by this section` |
| s 251(14) | the person the Authority exempts | none named | immunity / disability (and the Authority's power to exempt) | `s 251(14) the person is exempt from this section` |
| s 252(1), (2) | the person making the offer (to be informed of a deficiency) | a person liable on the prospectus or profile statement | claim-right / duty to notify as soon as practicable; offence (2) as above | `s 252(1) the person has notified the person making the offer`, `s 252(2) the person is guilty of an offence` |
| s 253(1), (4) | the State (the offence; no claimant is named) | the persons s 253(4) lists | power to punish / liability to the penalty | `s 253(1) the person is guilty of an offence`, `s 253(4) the person is one of the persons guilty of the offence` |
| s 253(3) | the person who proves no material adverseness | the State | immunity / disability | `s 253(3) the person does not contravene subsection (1)` |
| s 254(1), (3) | the claimant who acquired the securities or contracts and suffered loss or damage | the persons s 254(3) lists | claim-right / duty to compensate | `s 254(1) the person is liable to compensate the claimant`, `s 254(3) the person is one of the persons liable` |
| s 254(5) | the persons liable (6 years from the date the cause of action arose) | the claimant (the power to sue lapses) | immunity / disability | `s 254(5) the action may not be commenced` |
| s 255 | the person who proves a defence | the claimant and the State | immunity / disability (the defence of s 255(1) to (6)) | `s 255 the person has a defence`, `s 255(1) this section gives a defence for the false or misleading statement`, `s 255(3) this section gives a defence for reasonable reliance on information` |
| s 257(2), (4) | the persons who accept the subsequent offer (they are treated as subscribers) | the entity (treated as the person making the offer); the person making the subsequent offer (treated as a named director) | claim-right / duty; liability | `s 257(2) the entity is deemed to be the person making the offer`, `s 257(2) the persons accepting the subsequent offer are deemed subscribers`, `s 257(4) the person making the subsequent offer is treated as a person named in the prospectus as a director` |
| s 258(1), (2), (3) | the applicant (the moneys are held on trust in a separate account until allotment); the bank (no duty to enquire) | the person making the offer (trustee); the applicants and anyone claiming under the trust (the bank's no-right) | claim-right / duty (trust); privilege / no-right (the bank); offence (3) as above | `s 258(1) the person making the offer holds the moneys on trust in a separate bank account`, `s 258(2) the bank has an obligation or duty to enquire into the application of the moneys`, `s 258(3) the person is guilty of an offence` |
| s 259(1)(c), (d) | the applicant (the allotment is void); the State (offence) | the person who allots (the allotment is void; offence (d)) | immunity / disability; liability to the penalty | `s 259(1)(c) the allotment is void`, `s 259(1)(d) the person is guilty of an offence` |
| s 259(2), (4), (7), (8) | the applicants (immediate repayment without interest; interest at 10% after 14 days) | the person making the offer; each director who does not show the s 259(4) defence | claim-right / duty to repay; joint and several liability | `s 259(2) the person making the offer has repaid the moneys`, `s 259(2)(a) the person making the offer is liable to repay with interest at 10% per annum`, `s 259(2)(b) the director is jointly and severally liable to repay with interest at 10% per annum`, `s 259(4) this section gives the director a defence`, `s 259(8) the person is guilty of an offence` |
| s 259(3) | the Authority (it may exempt an allotment, with notice in the Gazette) | the person making the offer and the applicants | power / liability | `s 259(3) the Authority may exempt the allotment`, `s 259(3) the Authority has given notice of the exemption in the Gazette` |
| s 259(10), (11), (12) | none named in the text | the director who contravenes (10); the person who issues the prospectus without the statement (11); offence (12) | duty / claim-right of the State; liability to the penalty | `s 259(10) the director is guilty of an offence`, `s 259(11) the person shall not issue the prospectus`, `s 259(12) the person is guilty of an offence` |
| s 259(5), s 260(9) | the applicant | any person who relies on a condition that waives compliance with the section | immunity / disability (the condition is void) | `s 259(5) the condition is void`, `s 260(9) the condition is void` |
| s 260(1), (1A) | none named in the text | the person who allots before the minimum subscription is received | duty / claim-right of the State | `s 260(1) the person shall not make the allotment` |
| s 260(4), (5), (6) | the applicants (repayment of the moneys; interest at 10% per annum once 5 months have passed) | the company or business trust; each director who does not show the s 260(6) defence | claim-right / duty to repay; joint and several liability | `s 260(4) the moneys have been repaid`, `s 260(5) the director is jointly and severally liable to repay with interest at 10% per annum`, `s 260(6) this section gives the director a defence` |
| s 260(7), (7A) | the applicant (the option to avoid the allotment, by written notice served within the time s 260(7) gives) | the company or the trustee-manager (liability to the avoidance) | power / liability | `s 260(7) the applicant has exercised the option to avoid the allotment in time`, `s 260(7A) the allotment is voidable although the company or business trust is being wound up` |
| s 260(7B) to (7D) | the business trust (to be paid into the trust property); the company (to be compensated); the allottee (to be compensated) | the trustee-manager (7B); a director of the trustee-manager (7C); a director of the company (7D) | claim-right / duty to pay or compensate; offence with no stated penalty | `s 260(7B)(a) the trustee-manager must pay into the trust property the loss, damages or costs`, `s 260(7B)(b) the trustee-manager must compensate the allottee`, `s 260(7C)(a) the director must pay into the trust property the loss, damages or costs`, `s 260(7C)(b) the director must compensate the allottee`, `s 260(7D)(a) the director must compensate the company`, `s 260(7D)(b) the director must compensate the allottee` |
| s 260(8) | the persons liable (2 years from the date of the allotment) | the claimant (the power to sue lapses) | immunity / disability | `s 260(8) the proceedings may not be commenced` |

Provisions that create no such relation (none): the definitions of s 239(1), (4), s 239AA(1), s 240AA(5), s 243(8) and s 251(18), (18A); the deeming and counting rules of s 239(2), (3), (3A), (4A), (6), (7), (8), s 239AA(2), (3), (4), s 240(2), (3), (4A) to (4C), (10), (11), (11A), (18), (19), s 240A(1) to (7), s 241(1B), (1C), (2) to (4), (6), (7), (9), (17), s 242(6), (9), (10), (13), s 243(2) to (5), (7), s 244 (repealed), s 246(1), (3), s 248(1), (3), (6), s 249(1B), s 249A(5), s 251(2), (13), (16) to (19), s 252(3), s 253(2), (5), (6), s 254(2), (4), (4A), (6), s 255(7), s 256 (repealed), s 257(1), (3), (5), s 259(6), (9), (13), s 260(2), (3); and the regulation-making provisions s 239B, s 240(8B), (20) and s 240A(8), which are inert (machinery).

## Marginal readings for a lawyer (sfac)

The brief's two readings "for a lawyer, not for you to decide": (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (and flat negatives count as the text saying no); (b) a prohibition or grant limited by its own wording does not (the answer is `NOTHING`).
Every branch below rests on one of them; the other reading is a one-branch change (swap `JUST FALSE` and `NOTHING` on the named branch).
The branches are listed by script from the code: reading (a) from the `-- MARGINAL-READING (a)` comments (21 branches), reading (b) from the `-- NOTHING-kind (limited by its own wording)` comments (208 branches).

### Reading (a): a failed "if" answers `JUST FALSE`; the other reading answers `NOTHING`

| Function | File:line of the branch |
| --- | --- |
| s 239(2) the statement is deemed to be included in the prospectus or profile statement | sfac-239.l4:483 |
| s 240(4B) the requirement for signature by a director or equivalent person is satisfied | sfac-240.l4:258 |
| s 240(4C) the requirement for signature by a proposed director or equivalent person is satisfied | sfac-240.l4:275 |
| s 240(13) the Authority must refuse to register the prospectus | sfac-240.l4:568 |
| s 240(14) the Authority must refuse to register the profile statement | sfac-240.l4:613 |
| s 240(17) the person is guilty of an offence | sfac-240.l4:729 |
| s 240AA(2) the person must not publish or disseminate the document | sfac-240aa.l4:114 |
| s 240A(3) the requirements of section 240(1)(a)(ii) and (iii) are satisfied for the offer | sfac-240aa.l4:534 |
| s 240A(4) the requirements of section 240(4)(b) and (c) are satisfied for the offer | sfac-240aa.l4:558 |
| s 240A(5) the base prospectus or base profile statement is treated as lodged with and registered by the Authority for the offer | sfac-240aa.l4:574 |
| s 241(1C) the offer is not treated as subsisting | sfac-241.l4:134 |
| s 242(3) the Authority must not serve a stop order | sfac-242.l4:99 |
| s 249(2) the person is guilty of an offence | sfac-249.l4:149 |
| s 249A(3) the person is guilty of an offence | sfac-249.l4:312 |
| s 250(4) the person is guilty of an offence | sfac-249.l4:492 |
| s 251(1) the person must not advertise the offer or publish the statement | sfac-249.l4:540 |
| s 259(1)(a) the permission was not applied for in time | sfac-257.l4:309 |
| s 259(1)(b) the permission was not granted in time | sfac-257.l4:339 |
| s 259(2)(a) the person making the offer is liable to repay with interest at 10% per annum | sfac-257.l4:463 |
| s 259(10) the director is guilty of an offence | sfac-257.l4:672 |
| s 260(5) the director is jointly and severally liable to repay with interest at 10% per annum | sfac-257.l4:932 |

Not marginal, though a condition is involved: a "where", "when" or "upon" gate is decided by the periods ruling of 2026-11-05, rule (b) (`JUST FALSE`); a defence that is not proved is decided by the delegated-defence ruling of 2026-11-05 (the defences of s 255(1) to (6), s 259(4) and s 260(6): "this section gives no defence on these facts"); a period fixed in the text's own words is decided by rule (a); a branch under "means" rests on "means"; a branch under "unless", "only if", "so long as", "provided that" or "except" rests on the closed gate; a branch under a flat negative ("does not", "must not", "shall not", "need not") rests on the flat-negative reading of the Guide's N2 ruling (2026-11-04).
The "may" sites whose gate is "where", "when" or "upon" (Split sites (ii)) are listed for a lawyer under the fork register above and below.

### Reading (b): a rule limited by its own wording answers `NOTHING` outside its limit; the other reading answers `JUST FALSE`

| Function | File:line(s) of the branches |
| --- | --- |
| s 239(1) "issuer" the person is the issuer in relation to the offer | sfac-239.l4:195 |
| s 239(5A) the person is guilty of an offence | sfac-239.l4:651 |
| s 239AA(3)(a) the person is treated as the issuer of the SDRs being offered | sfac-239.l4:816 |
| s 239AA(3)(b) the person is treated as the person who makes the offer of the SDRs | sfac-239.l4:834 |
| s 239AA(3)(c) the person has the rights and duties under this Act of the issuer and of the person making the offer | sfac-239.l4:856 |
| s 240(1) the person must not make the offer | sfac-240.l4:55 |
| s 240(3) the preliminary document contains all the information it must contain | sfac-240.l4:103 |
| s 240(4) the offer may be made in or accompanied by a profile statement instead of a prospectus | sfac-240.l4:143 |
| s 240(4A) the copy lodged with the Authority has been signed as required | sfac-240.l4:241 |
| s 240(5) the person must not make the offer | sfac-240.l4:293 |
| s 240(7) the person is guilty of an offence | sfac-240.l4:331 |
| s 240(9) the Authority must not register the prospectus | sfac-240.l4:431 |
| s 240(12) the person making the offer must provide the Authority with a copy in the form or medium required | sfac-240.l4:519 |
| s 240(15) the Authority must give the person making the offer an opportunity to be heard before refusing | sfac-240.l4:650 |
| s 240(16) the person making an offer may appeal to the Minister | sfac-240.l4:671 |
| s 240(16) the Minister's decision on the appeal is final | sfac-240.l4:683 |
| s 240(17) the person is guilty of an offence | sfac-240.l4:734 |
| s 240AA(1) the person must not make the offer | sfac-240aa.l4:49, sfac-240aa.l4:51, sfac-240aa.l4:53 |
| s 240AA(2) the person must not publish or disseminate the document | sfac-240aa.l4:108, sfac-240aa.l4:110, sfac-240aa.l4:112 |
| s 240AA(3) the Authority may publish the document for public information | sfac-240aa.l4:152 |
| s 240AA(4) the person is guilty of an offence | sfac-240aa.l4:172 |
| s 240AB(1) and (2) the person is exempt from the requirements in section 240AA | sfac-240aa.l4:402 |
| s 240AB(3) the condition or restriction is in force | sfac-240aa.l4:415 |
| s 240AB(4) it is necessary to publish the exemption in the Gazette | sfac-240aa.l4:430 |
| s 240AB(5) the person is guilty of an offence | sfac-240aa.l4:447 |
| s 240A(1) the prospectus comprises what it must comprise | sfac-240aa.l4:485 |
| s 240A(2) the profile statement comprises what it must comprise | sfac-240aa.l4:507 |
| s 240A(3) the requirements of section 240(1)(a)(ii) and (iii) are satisfied for the offer | sfac-240aa.l4:531 |
| s 240A(4) the requirements of section 240(4)(b) and (c) are satisfied for the offer | sfac-240aa.l4:555 |
| s 240A(6) a reference to a prospectus is read as a reference to both the base prospectus and the pricing statement | sfac-240aa.l4:591 |
| s 240A(7) a reference to a profile statement is read as a reference to both the base profile statement and the pricing statement | sfac-240aa.l4:611 |
| s 241(1) the person making the offer may lodge a supplementary or replacement document | sfac-241.l4:61 |
| s 241(1A) the person making the offer may lodge a supplementary or replacement document for a base prospectus or base profile statement | sfac-241.l4:84 |
| s 241(1B) subsections (7) to (16) apply to the document | sfac-241.l4:99 |
| s 241(2) the supplementary document begins as it must | sfac-241.l4:161 |
| s 241(3) the replacement document begins as it must | sfac-241.l4:181 |
| s 241(4) the document is dated with the date on which it is lodged | sfac-241.l4:199 |
| s 241(5) the person making the offer has taken the reasonable steps | sfac-241.l4:220 |
| s 241(7) the offer has been kept open for at least 14 days after the lodgment | sfac-241.l4:300 |
| s 241(8)(a)(iii)(A) the applications are deemed to have been withdrawn and cancelled | sfac-241.l4:407 |
| s 241(8)(b)(iii)(A) the issue is deemed void | sfac-241.l4:529 |
| s 241(9) the provision has effect despite sections 76 and 76A and Division 3A of Part 4 of the Companies Act 1967 | sfac-241.l4:558 |
| s 241(10) the applicant has notified the person making the offer within 14 days | sfac-241.l4:579 |
| s 241(11) the applicant has notified the person making the offer and returned the documents within 14 days | sfac-241.l4:622 |
| s 241(11) the issue of the securities or contracts is deemed to be void | sfac-241.l4:647 |
| s 241(12)(a)(iii)(A) the applications are deemed to have been withdrawn and cancelled | sfac-241.l4:751 |
| s 241(12)(b)(iii) the sale is deemed void | sfac-241.l4:899 |
| s 241(13) the applicant has notified the person making the offer within 14 days | sfac-241.l4:937 |
| s 241(14) the applicant has notified the person making the offer and returned the documents within 14 days | sfac-241.l4:979 |
| s 241(14) the sale of the securities or contracts is deemed to be void | sfac-241.l4:1004 |
| s 241(15) the person is guilty of an offence | sfac-241.l4:1031 |
| s 241(16) the person is guilty of an offence | sfac-241.l4:1053 |
| s 242(1) the Authority may serve a stop order on the person making the offer for the prospectus | sfac-242.l4:51 |
| s 242(2) the Authority may serve a stop order on the person making the offer for the profile statement | sfac-242.l4:81 |
| s 242(4) the Authority must give the person making the offer an opportunity to be heard | sfac-242.l4:135 |
| s 242(6) the provision has effect despite sections 76 and 76A and Division 3A of Part 4 of the Companies Act 1967 | sfac-242.l4:237 |
| s 242(7)(b)(i) the person making the offer has informed the applicants and paid them, where title documents were issued | sfac-242.l4:335 |
| s 242(7)(b)(ii) the person making the offer has paid the applicants within 7 days, where no title documents were issued | sfac-242.l4:355 |
| s 242(8) the Authority may serve an interim stop order without giving an opportunity to be heard | sfac-242.l4:378 |
| s 242(9) the interim stop order is in force | sfac-242.l4:403 |
| s 242(10) subsections (5) and (7) apply | sfac-242.l4:420 |
| s 242(11) the person is guilty of an offence | sfac-242.l4:441 |
| s 242(12) the person is guilty of an offence | sfac-242.l4:491 |
| s 243(1) the prospectus contains what it must contain | sfac-243.l4:45 |
| s 243(2) the item of information must be contained in the prospectus | sfac-243.l4:71 |
| s 243(3)(b) the issuer's assets and liabilities, profits and losses, financial position and performance, and prospects are a matter the information must relate to | sfac-243.l4:104 |
| s 243(3)(c) the underlying entity's assets and liabilities, profits and losses, financial position and performance, and prospects are a matter the information must relate to | sfac-243.l4:122 |
| s 243(3)(d) the capacity of the person or entity to issue or deliver the units, or to meet its obligations, is a matter the information must relate to | sfac-243.l4:152 |
| s 243(3)(e) the business trust's and the trustee-manager's assets and liabilities, profits and losses, financial position and performance, and the prospects of the business trust, are a matter the information must relate to | sfac-243.l4:179 |
| s 243(3)(f) the assets and liabilities, profits and losses, financial position and performance, and prospects of the issuing entity are a matter the information must relate to | sfac-243.l4:204 |
| s 243(3)(g) the capacity of the person or entity to issue or deliver the units or derivatives of units, or to meet its obligations, is a matter the information must relate to | sfac-243.l4:237 |
| s 243(4) regard has been had to the matters | sfac-243.l4:260 |
| s 243(4A) the information may be incorporated in the prospectus by reference to the reference document | sfac-243.l4:279 |
| s 243(4B) the information is part of the prospectus | sfac-243.l4:291 |
| s 243(6) the condition is void | sfac-243.l4:345 |
| s 243(7) this section affects the liability | sfac-243.l4:357 |
| s 243(8) "assets and liabilities, profits and losses, financial position and performance" the figures are those of the business trust | sfac-243.l4:375 |
| s 243(8) "prospects" the prospects are those of the business trust | sfac-243.l4:392 |
| s 245(1) the entity must not accept or retain the subscriptions | sfac-243.l4:422 |
| s 245(2)(a) the entity must not make, authorise or permit the statement of asset-backing | sfac-243.l4:466 |
| s 245(2)(b) the prospectus contains the statement of total assets and total liabilities | sfac-243.l4:497 |
| s 245(3) the person is guilty of an offence | sfac-243.l4:520 |
| s 246(1) the profile statement contains what it must contain | sfac-243.l4:578 |
| s 246(2) the profile statement contains something it must not contain | sfac-243.l4:602, sfac-243.l4:605 |
| s 247(1) and (3) the person or document is exempt from the requirement of form or content | sfac-243.l4:641 |
| s 247(5) the person is guilty of an offence | sfac-243.l4:677 |
| s 248(2) the Authority may exempt the entity from the requirements | sfac-243.l4:726 |
| s 248(3) the requirement as to signing by directors resident in Singapore is met | sfac-243.l4:742 |
| s 248(4) the Authority may permit a duly authorised agent to sign | sfac-243.l4:761 |
| s 248(5) the Authority may grant the exemption applied for | sfac-243.l4:778 |
| s 248(6) the document is deemed to be a prospectus or profile statement for the purposes of this Division | sfac-243.l4:793 |
| s 248(6) a copy of the document must be registered by the Authority | sfac-243.l4:802 |
| s 249(1A) the person making the offer has deposited the copies of the consents | sfac-249.l4:102 |
| s 249(1B) the issuer has kept the copies and made them available | sfac-249.l4:125 |
| s 249(2) the person is guilty of an offence | sfac-249.l4:154 |
| s 249(3) the person or document is exempt from the section | sfac-249.l4:172 |
| s 249(4) the person is guilty of an offence | sfac-249.l4:188 |
| s 249A(3) the person is guilty of an offence | sfac-249.l4:317 |
| s 249A(4) the person making the offer has deposited the copies of the consents | sfac-249.l4:342 |
| s 249A(5) the issuer has kept the copies and made them available | sfac-249.l4:365 |
| s 250(1) the person must not make the offer or allot, issue or sell on the basis of the prospectus | sfac-249.l4:408 |
| s 250(2) the officer or promoter must not authorise or permit the offer, allotment, issue or sale | sfac-249.l4:453 |
| s 250(5) the allotment, issue or sale is void or voidable by reason only of the contravention | sfac-249.l4:511 |
| s 251(1) the person must not advertise the offer or publish the statement | sfac-249.l4:542 |
| s 251(2) regard has been had to the three matters | sfac-249.l4:595 |
| s 251(3) the person may disseminate the preliminary document without contravening subsection (1) | sfac-249.l4:665, sfac-249.l4:670 |
| s 251(4)(a) the person does not contravene subsection (1) by presenting the material | sfac-249.l4:711, sfac-249.l4:716 |
| s 251(4)(b) the person does not contravene subsection (1) by presenting the material to equip those persons | sfac-249.l4:777 |
| s 251(5)(a) the person may disseminate the registered prospectus or profile statement | sfac-249.l4:805 |
| s 251(5)(b) the person may disseminate the product highlights sheet | sfac-249.l4:823 |
| s 251(6) the advertisement or publication does not contravene subsection (1) before registration | sfac-249.l4:906 |
| s 251(8) the advertisement or publication does not contravene subsection (1) after registration | sfac-249.l4:940 |
| s 251(9)(a) the advertisement or publication is a required disclosure, notice or report | sfac-249.l4:955 |
| s 251(9)(b) the advertisement or publication is a notice or report of a general meeting | sfac-249.l4:972 |
| s 251(9)(c) the advertisement or publication is a report about the issuer, the business trust or the underlying entity | sfac-249.l4:998 |
| s 251(9)(d) the advertisement or publication is a statement that the prospectus or profile statement has been lodged | sfac-249.l4:1013 |
| s 251(11) subsection (9)(e) and (f) apply to the advertisement or statement | sfac-249.l4:1060 |
| s 251(9)(e) the advertisement or publication is a news report or a genuine comment | sfac-249.l4:1091 |
| s 251(9)(f) the advertisement or publication is a report by a person other than the four | sfac-249.l4:1126 |
| s 251(9)(h) the advertisement or publication corrects or clarifies an earlier report or publication | sfac-249.l4:1169 |
| s 251(9) the advertisement or publication does not contravene subsection (1) by being one of the eight | sfac-249.l4:1274 |
| s 251(10) the person does not contravene subsection (1) by publishing in the ordinary course of business | sfac-249.l4:1295 |
| s 251(12) the person is guilty of an offence | sfac-249.l4:1337 |
| s 251(13) this section affects a liability under another law | sfac-249.l4:1354 |
| s 251(14) the person is exempt from this section | sfac-249.l4:1367 |
| s 251(15) the person is guilty of an offence | sfac-249.l4:1384 |
| s 252(1) the person has notified the person making the offer | sfac-249.l4:1563, sfac-249.l4:1565 |
| s 252(2) the person is guilty of an offence | sfac-249.l4:1582 |
| s 253(2) a false or misleading statement about a future matter is taken to have been made | sfac-253.l4:79 |
| s 253(3) the person does not contravene subsection (1) | sfac-253.l4:94 |
| s 253(4)(b) the person is a director or proposed director of the entity making the offer | sfac-253.l4:117 |
| s 253(4)(c) the person is the issuer or a director or proposed director of the issuer | sfac-253.l4:143 |
| s 253(4)(d) the issue manager is one of the persons guilty | sfac-253.l4:171 |
| s 253(4)(e) the underwriter is one of the persons guilty | sfac-253.l4:199 |
| s 253(4)(f) the person named as having made a statement is one of the persons guilty | sfac-253.l4:227 |
| s 253(4)(g) any other person is one of the persons guilty | sfac-253.l4:247 |
| s 253(1) the person is guilty of an offence | sfac-253.l4:293 |
| s 253(5)(b) the person is reckless | sfac-253.l4:346 |
| s 254(2) a false or misleading statement about a future matter is taken to have been made | sfac-253.l4:418 |
| s 254(3)(b) the person is a director or proposed director of the entity making the offer | sfac-253.l4:441 |
| s 254(3)(c) the person is the issuer or a director or proposed director of the issuer | sfac-253.l4:467 |
| s 254(3)(d) the issue manager is one of the persons liable | sfac-253.l4:481 |
| s 254(3)(da) the underwriter is one of the persons liable | sfac-253.l4:495 |
| s 254(3)(e) the person named as having made a statement is one of the persons liable | sfac-253.l4:516 |
| s 254(3)(f) any other person is one of the persons liable | sfac-253.l4:535 |
| s 254(1) the person is liable to compensate the claimant | sfac-253.l4:579, sfac-253.l4:580 |
| s 254(4) the person is taken to have acquired in reliance on both the profile statement and the prospectus | sfac-253.l4:596 |
| s 254(6) this section affects a liability under another law | sfac-253.l4:635 |
| s 255(1) this section gives a defence for the false or misleading statement | sfac-253.l4:660 |
| s 255(2) this section gives a defence for the omission | sfac-253.l4:686 |
| s 255(3) this section gives a defence for reasonable reliance on information | sfac-253.l4:715 |
| s 255(4) the person is an agent of the entity or individual | sfac-253.l4:732 |
| s 255(5) this section gives a defence for publicly withdrawing consent | sfac-253.l4:757 |
| s 255(6) this section gives a defence for not being aware of a new circumstance | sfac-253.l4:775 |
| s 257(2) the document is deemed to be a prospectus issued by the entity | sfac-257.l4:77 |
| s 257(2) the entity is deemed to be the person making the offer | sfac-257.l4:106 |
| s 257(2) the persons accepting the subsequent offer are deemed subscribers | sfac-257.l4:135 |
| s 257(2) the deeming affects the liability of the persons making the subsequent offer | sfac-257.l4:145 |
| s 257(3) it is sufficient evidence that the allotment was made with a view to subsequent sale | sfac-257.l4:175 |
| s 257(4) the person making the subsequent offer is treated as a person named in the prospectus as a director | sfac-257.l4:193 |
| s 257(5) the document states what it must state | sfac-257.l4:213 |
| s 258(1) the person making the offer holds the moneys on trust in a separate bank account | sfac-257.l4:243 |
| s 258(2) the bank has an obligation or duty to enquire into the application of the moneys | sfac-257.l4:259 |
| s 258(3) the person is guilty of an offence | sfac-257.l4:275 |
| s 259(1)(c) the allotment is void | sfac-257.l4:376 |
| s 259(1)(d) the person is guilty of an offence | sfac-257.l4:404 |
| s 259(2) the person making the offer has repaid the moneys | sfac-257.l4:430, sfac-257.l4:432 |
| s 259(4) this section gives the director a defence | sfac-257.l4:481 |
| s 259(2)(b) the director is jointly and severally liable to repay with interest at 10% per annum | sfac-257.l4:507 |
| s 259(3) the Authority may exempt the allotment | sfac-257.l4:534 |
| s 259(3) the Authority has given notice of the exemption in the Gazette | sfac-257.l4:545 |
| s 259(5) the condition is void | sfac-257.l4:560 |
| s 259(6)(a) the underwriter is treated as having applied pursuant to the prospectus | sfac-257.l4:580 |
| s 259(6)(b) a reference to sale is read for a reference to allotment | sfac-257.l4:594 |
| s 259(7) the moneys are kept in a separate bank account | sfac-257.l4:610 |
| s 259(8) the person is guilty of an offence | sfac-257.l4:629 |
| s 259(9) permission is deemed to have been granted | sfac-257.l4:655 |
| s 259(10) the director is guilty of an offence | sfac-257.l4:675 |
| s 259(11) the person must not issue the prospectus | sfac-257.l4:714, sfac-257.l4:721 |
| s 259(12) the person is guilty of an offence | sfac-257.l4:750 |
| s 259(13) the prospectus is deemed to imply that application has been or will be made for permission | sfac-257.l4:775 |
| s 260(1) the person must not make the allotment | sfac-257.l4:824 |
| s 260(4) the moneys have been repaid | sfac-257.l4:890 |
| s 260(6) this section gives the director a defence | sfac-257.l4:907 |
| s 260(5) the director is jointly and severally liable to repay with interest at 10% per annum | sfac-257.l4:930 |
| s 260(7) the applicant has exercised the option to avoid the allotment in time | sfac-257.l4:966 |
| s 260(7A) the allotment is voidable although the company or business trust is being wound up | sfac-257.l4:982 |
| s 260(7B) the trustee-manager is guilty of an offence | sfac-257.l4:1004 |
| s 260(7B)(a) the trustee-manager must pay into the trust property the loss, damages or costs | sfac-257.l4:1015 |
| s 260(7B)(b) the trustee-manager must compensate the allottee | sfac-257.l4:1026 |
| s 260(7C) the director of the trustee-manager is guilty of an offence | sfac-257.l4:1050 |
| s 260(7C)(a) the director must pay into the trust property the loss, damages or costs | sfac-257.l4:1061 |
| s 260(7C)(b) the director must compensate the allottee | sfac-257.l4:1072 |
| s 260(7D) the director of the company is guilty of an offence | sfac-257.l4:1093 |
| s 260(7D)(a) the director must compensate the company | sfac-257.l4:1104 |
| s 260(7D)(b) the director must compensate the allottee | sfac-257.l4:1115 |
| s 260(9) the condition is void | sfac-257.l4:1142 |

### Reading a result: FALSE and NOTHING (sfac)

This is how to read an answer from this part, in the terms of the offers regime.
A function answers `JUST TRUE` when the facts put to it fit the rule, definition, deeming or limb it encodes: the person must not make the offer without a registered prospectus, the document is a prospectus, the allotment is void.
It answers `JUST FALSE` ("a no") only where the text itself says no to the case in its own words: a definition that says "means" and no limb fits; an express exclusion ("does not apply", "need not be given", "may not be commenced after"); a condition the text introduces with "unless", "only if", "so long as", "provided that" or "except"; a period the text fixes in its own words ("within 14 days from", "6 months from the date of registration"), where the act falls outside it; a "where" or "when" or "upon" gate that is not met (the periods ruling of 2026-11-05, rule (b)); a defence that is not proved ("this section gives no defence on these facts", the delegated-defence ruling of 2026-11-05); and a failed "if", which is the marginal reading (a) below.
It answers `NOTHING` ("the text does not say") where the text lists without closing the list ("includes"), leaves a word undefined ("authorised by this section", "such matters as the Authority may prescribe"), is silent, hands the answer to a power or to another Act or Part that is not among the sources (a regulation under section 341, section 262(3), Subdivision (4) of this Division), or limits a prohibition, a grant or an offence in its own wording and the case falls outside the limit ("A person who contravenes ... shall be guilty of an offence" says nothing of a person who does not contravene; "a director of the entity making the offer" says nothing of anyone else).
A caller must never turn `NOTHING` into `FALSE`.
In this part the combining functions take the answers of the functions below them as `MAYBE BOOLEAN` inputs, so that a limb the caller could not answer stays `NOTHING`; for an exemption or an open route (the profile statement route of s 240(4), the exemption of s 240AB, a safe harbour of s 251) only `JUST TRUE` counts as the route being shown, and `JUST FALSE` and `NOTHING` both leave the bar in place; for the gate that disapplies the Subdivision (`this Subdivision applies to the offer`) `JUST FALSE` ends the bar and `NOTHING` gives `NOTHING`.
For an offence, `JUST TRUE` is "guilty on these facts", `JUST FALSE` is "an element the text states is shown absent" or "the text itself says no", and `NOTHING` is "the text names who is guilty and says nothing of this person" (the split sites (i) below).
For a duty (a time limit, a payment), `JUST TRUE` is "done in time", `JUST FALSE` is "not done, or done late", and `NOTHING` is "the duty is not shown to arise on these facts" (fork F18).
The seat (`sfac-seat.l4`) puts the same three answers to a person in the person's words: `JUST TRUE` is yes, `JUST FALSE` is no in the text's own words, `NOTHING` is "the text does not say".

## Seams (sfac)

A seam is a provision in one part whose answer another part's provision needs; the dependent part takes the answer as an input, named for the fact and the section it comes from (`inputs/PLAN.md` section 4).
Every seam below was confirmed by reading the text at the cited line, not from the plan alone.
S1 and S2 are the keel's (sfaa answers them); S3 to S8 are the plan's seams for this part; S9 is one the plan lacks.

| id | asking provision | answering provision | input (name word for word as `inputs/PLAN.md` section 4.3 gives it; type as taken here) | function(s) in this part |
| --- | --- | --- | --- | --- |
| S3 | sfac s 253(1) and s 254(1) ("in the case of an offer referred to in section 280", text at src:40975 and src:41166) | sfad s 280 | `the offer is an offer referred to in section 280` (BOOLEAN), with the separate fact `a prospectus or profile statement is prepared and issued in relation to the offer` (BOOLEAN), which the text also requires | `s 253(1) the false or misleading statement or omission is present`, `s 254(1) the false or misleading statement or omission is present` |
| S4 | sfac s 257(1)(b) ("does not qualify for an exemption under Subdivision (4) of this Division (other than section 280)", src:41389) | sfad Subdivision (4), ss 272 to 282 | `the offer qualifies for an exemption under Subdivision (4) of Division 1 of Part 13, other than section 280` (MAYBE BOOLEAN here, BOOLEAN in the plan: only `JUST TRUE` counts as the exemption being shown) | `s 257(1) subsection (2) applies` |
| S5 | sfac s 240AA(5) ("asset-backed securities" "has the meaning given by section 262(3)", src:38891) | sfad s 262(3) | `the securities are asset-backed securities as section 262(3) defines them` (MAYBE BOOLEAN here, BOOLEAN in the plan: the answer of section 262(3) is passed through as it is, so a `JUST FALSE` from a "means" definition stays a no and a `NOTHING` stays not covered) | `s 240AA(5) "asset-backed securities" the securities are asset-backed securities` |
| S6 | sfad s 265A ("structured notes" "has the meaning given by section 240AA(5)") | sfac s 240AA(5) | answered here: `s 240AA(5) "structured notes" the debentures or units of debentures are structured notes`, with its limbs (F13, F21) | `s 240AA(5) "structured notes" the debentures or units of debentures are structured notes` |
| S7 | sfad s 273 (an offer of SDRs "made or treated under section 239AA as made by" an entity or a trustee-manager) | sfac s 239AA | answered here: `s 239AA(3)(a) the person is treated as the issuer of the SDRs being offered`, `s 239AA(3)(b) the person is treated as the person who makes the offer of the SDRs`, `s 239AA(4) the person is the issuer of the SDRs, section 239AA(3) prevailing over section 239`; the "qualifying person" half of the plan's input is sfad's | the three functions named |
| S8 | sfad ss 272A, 272B and 275 ("the prospectus has expired pursuant to section 250") | sfac s 250 | answered here by the date: `s 250(3) the last day of the period` (a prospectus has expired under section 250 on any later day); sfac's own bar is `s 250(1) the person must not make the offer or allot, issue or sell on the basis of the prospectus` | `s 250(3) the last day of the period` |
| S9 | the bars on making an offer or publishing (s 240(1), (5), (17), s 240AA(1) and (2)): the Subdivision does not apply to an offer that Subdivision (4) exempts, the Authority has disapplied it, or s 239(8) leaves outside it (the plan lists sfad ss 272 to 275's "Subdivisions (1A), (2) and (3) ... do not apply" as needing no input) | sfad Subdivision (4), the Authority's order of s 239A(1), and s 239A(2) | found here, not in the plan: `the offer is exempted from Subdivision (2) by a provision of Subdivision (4)` (MAYBE BOOLEAN), taken by `s 239A(1) and (2), s 239(8) and Subdivision (4): this Subdivision applies to the offer`, whose answer is the input `this Subdivision applies to the offer` of those five functions (`JUST FALSE` ends the bar, `NOTHING` gives `NOTHING`); the other functions of ss 241 to 260 do not take it, so a caller whose offer is exempted from Subdivision (2) must ask that function first and ask no other question of this part (a gap, recorded under What the text does not answer) | `s 239A(1) and (2), s 239(8) and Subdivision (4): this Subdivision applies to the offer` |

Other inputs that point outside this part and are not seams of the plan: the Authority's prescriptions under section 341 and its orders, notices and exemptions are inputs named `the Authority has prescribed ...` / `... by regulations made under section 341`; the Business Trusts Act 2004, the Companies Act 1967, the Banking Act 1970 and the Financial Advisers Act 2001 terms are inputs named for the fact and the Act (for example `the property is trust property within section 2 of the Business Trusts Act 2004`).
The keel's functions are called, not asked, wherever the text uses a term of section 2(1) (`s 2(1) "director" the person is a director` in `Under section 253(1), ...`, and section 2(2) in `s 251(18) the matter is within the affairs of the entity or the business trust`).
The merged seat layer is for the lead: this part's seat asks `the date asked` and `I am a director of the corporation` under the plan's names (section 7.1 and 7.2), and one input of its own per fact the keel's seat does not ask.

## Split sites (sfac)

The two questions the brief leaves to each encoder, recorded site by site and counted here.
A search for `SPLIT-SITE` over this folder finds the branches below and the mentions in this file; the count is by tagged branch (a function with two tagged branches has two sites).

- (i), an unmet element of an offence or a contravention: **51 sites**, in 40 functions.
- (ii), a "may" gated by "where", "when", "upon", "on application", "with the consent of" and the like: **8 sites**, in 8 functions, all answered `JUST FALSE` (periods ruling, rule (b)); the other reading is `NOTHING`.

### Sites of (i)

| # | Function | File:line | Answer taken | Fork line |
| --- | --- | --- | --- | --- |
| i-1 | s 239(5A) the person is guilty of an offence | sfac-239.l4:651 | `NOTHING` | F1 |
| i-2 | s 240(1) the person must not make the offer | sfac-240.l4:55 | `NOTHING` | F4 |
| i-3 | s 240(5) the person must not make the offer | sfac-240.l4:293 | `NOTHING` | F6 |
| i-4 | s 240(7) the person is guilty of an offence | sfac-240.l4:331 | `NOTHING` | F6 |
| i-5 | s 240(17) the person is guilty of an offence | sfac-240.l4:729 | `JUST FALSE` | F8 |
| i-6 | s 240(17) the person is guilty of an offence | sfac-240.l4:734 | `NOTHING` | F8 |
| i-7 | s 240AA(1) the person must not make the offer | sfac-240aa.l4:49 | `NOTHING` | F10 |
| i-8 | s 240AA(1) the person must not make the offer | sfac-240aa.l4:51 | `NOTHING` | F10 |
| i-9 | s 240AA(1) the person must not make the offer | sfac-240aa.l4:53 | `NOTHING` | F10 |
| i-10 | s 240AA(2) the person must not publish or disseminate the document | sfac-240aa.l4:108 | `NOTHING` | F11 |
| i-11 | s 240AA(2) the person must not publish or disseminate the document | sfac-240aa.l4:110 | `NOTHING` | F11 |
| i-12 | s 240AA(2) the person must not publish or disseminate the document | sfac-240aa.l4:112 | `NOTHING` | F11 |
| i-13 | s 240AA(2) the person must not publish or disseminate the document | sfac-240aa.l4:114 | `JUST FALSE` | F11 |
| i-14 | s 240AA(4) the person is guilty of an offence | sfac-240aa.l4:172 | `NOTHING` | F12 |
| i-15 | s 240AB(5) the person is guilty of an offence | sfac-240aa.l4:447 | `NOTHING` | F14 |
| i-16 | s 241(15) the person is guilty of an offence | sfac-241.l4:1031 | `NOTHING` | F19 |
| i-17 | s 241(16) the person is guilty of an offence | sfac-241.l4:1053 | `NOTHING` | F20 |
| i-18 | s 242(3) the Authority must not serve a stop order | sfac-242.l4:99 | `JUST FALSE` | F23 |
| i-19 | s 242(11) the person is guilty of an offence | sfac-242.l4:441 | `NOTHING` | F25 |
| i-20 | s 242(12) the person is guilty of an offence | sfac-242.l4:491 | `NOTHING` | F26 |
| i-21 | s 245(1) the entity must not accept or retain the subscriptions | sfac-243.l4:422 | `NOTHING` | F27 |
| i-22 | s 245(2)(a) the entity must not make, authorise or permit the statement of asset-backing | sfac-243.l4:466 | `NOTHING` | F28 |
| i-23 | s 245(3) the person is guilty of an offence | sfac-243.l4:520 | `NOTHING` | F29 |
| i-24 | s 246(2) the profile statement contains something it must not contain | sfac-243.l4:605 | `NOTHING` | F30 |
| i-25 | s 247(5) the person is guilty of an offence | sfac-243.l4:677 | `NOTHING` | F31 |
| i-26 | s 249(2) the person is guilty of an offence | sfac-249.l4:149 | `JUST FALSE` | F33 |
| i-27 | s 249(2) the person is guilty of an offence | sfac-249.l4:154 | `NOTHING` | F33 |
| i-28 | s 249(4) the person is guilty of an offence | sfac-249.l4:188 | `NOTHING` | F34 |
| i-29 | s 249A(3) the person is guilty of an offence | sfac-249.l4:312 | `JUST FALSE` | F35 |
| i-30 | s 249A(3) the person is guilty of an offence | sfac-249.l4:317 | `NOTHING` | F35 |
| i-31 | s 250(1) the person must not make the offer or allot, issue or sell on the basis of the prospectus | sfac-249.l4:408 | `NOTHING` | F36 |
| i-32 | s 250(2) the officer or promoter must not authorise or permit the offer, allotment, issue or sale | sfac-249.l4:453 | `NOTHING` | F36 |
| i-33 | s 250(4) the person is guilty of an offence | sfac-249.l4:492 | `JUST FALSE` | F37 |
| i-34 | s 251(1) the person must not advertise the offer or publish the statement | sfac-249.l4:540 | `JUST FALSE` | F38 |
| i-35 | s 251(1) the person must not advertise the offer or publish the statement | sfac-249.l4:542 | `NOTHING` | F38 |
| i-36 | s 251(12) the person is guilty of an offence | sfac-249.l4:1337 | `NOTHING` | F38 |
| i-37 | s 251(15) the person is guilty of an offence | sfac-249.l4:1384 | `NOTHING` | F34 |
| i-38 | s 252(2) the person is guilty of an offence | sfac-249.l4:1582 | `NOTHING` | F43 |
| i-39 | s 253(1) the person is guilty of an offence | sfac-253.l4:293 | `NOTHING` | F49 |
| i-40 | s 258(3) the person is guilty of an offence | sfac-257.l4:275 | `NOTHING` | F58 |
| i-41 | s 259(1)(d) the person is guilty of an offence | sfac-257.l4:404 | `NOTHING` | F61 |
| i-42 | s 259(8) the person is guilty of an offence | sfac-257.l4:629 | `NOTHING` | F58 |
| i-43 | s 259(10) the director is guilty of an offence | sfac-257.l4:672 | `JUST FALSE` | F66 |
| i-44 | s 259(10) the director is guilty of an offence | sfac-257.l4:675 | `NOTHING` | F66 |
| i-45 | s 259(11) the person must not issue the prospectus | sfac-257.l4:714 | `NOTHING` | F67 |
| i-46 | s 259(11) the person must not issue the prospectus | sfac-257.l4:721 | `NOTHING` | F67 |
| i-47 | s 259(12) the person is guilty of an offence | sfac-257.l4:750 | `NOTHING` | F58 |
| i-48 | s 260(1) the person must not make the allotment | sfac-257.l4:824 | `NOTHING` | F69 |
| i-49 | s 260(7B) the trustee-manager is guilty of an offence | sfac-257.l4:1004 | `NOTHING` | F72 |
| i-50 | s 260(7C) the director of the trustee-manager is guilty of an offence | sfac-257.l4:1050 | `NOTHING` | F72 |
| i-51 | s 260(7D) the director of the company is guilty of an offence | sfac-257.l4:1093 | `NOTHING` | F72 |

### Sites of (ii)

| # | Function | File:line | Answer taken | Fork line |
| --- | --- | --- | --- | --- |
| ii-1 | s 240(8A) the Authority may proceed with the registration on the date | sfac-240.l4:409 | `JUST FALSE` | F7 |
| ii-2 | s 240A(9) the Authority may register the pricing statement on the day | sfac-240aa.l4:628 | `JUST FALSE` | F15 |
| ii-3 | s 251(3) the person may disseminate the preliminary document without contravening subsection (1) | sfac-249.l4:667 | `JUST FALSE` | F39 |
| ii-4 | s 251(4)(a) the person does not contravene subsection (1) by presenting the material | sfac-249.l4:713 | `JUST FALSE` | F39 |
| ii-5 | s 251(4)(b) the person does not contravene subsection (1) by presenting the material to equip those persons | sfac-249.l4:779 | `JUST FALSE` | F39 |
| ii-6 | s 251(6) the advertisement or publication does not contravene subsection (1) before registration | sfac-249.l4:901 | `JUST FALSE` | F39 |
| ii-7 | s 251(8) the advertisement or publication does not contravene subsection (1) after registration | sfac-249.l4:937 | `JUST FALSE` | F39 |
| ii-8 | s 259(3) the Authority may exempt the allotment | sfac-257.l4:531 | `JUST FALSE` | F63 |

Each fork line gives the answer taken, the other reading, and the line of `inputs/ENCODING-GUIDE.md` section 5 or the dated ruling it relies on (the "In short" line on lines 86 and 87, the periods ruling on line 93, the delegated-defence ruling on line 94, the site-by-site rule on line 95, the grant ruling on line 99), quoted in the appendix below.
Test on both readings' inputs, by script (`work/assemble.py`): for each of the 59 sites, the test files (`sfac-tests-*.l4`) assert the function with the answer taken and with at least one other answer; sites for which that is not so: 0.
The sites of (i) that answer `JUST FALSE` rest on the text opening an offence with "If" or "Where" (reading (a)) and are also listed in the reading (a) table; the sites that answer `NOTHING` rest on the offence being defined by a relative clause ("A person who contravenes ... shall be guilty") or by a named person and say nothing of anyone else (reading (b), listed in its table).

## Rules with no breach path (sfac)

A regulative rule here is a `PARTY ... SHANT ...` bar or a `PARTY ... MUST ... WITHIN n` duty, and each has a `#TRACE` that reaches `BREACH` (the counts are under "What `check.sh` prints" below), except the one rule below that has no time limit and no consequence the text states:

- **s 240(12)**, `s 240(12) the person making the offer must provide the Authority with a copy for publication`: a `MUST` with no time limit and no consequence of its own, so its traces end in `FULFILLED` (done) or `RESIDUAL` (still open) and never `BREACH`.

These duties are encoded as decision functions over the facts and have no regulative rule, because the text gives no number of days to count, or states a status and not an event; none can be shown breached by a trace, and nothing is invented to make one:

- **s 241(5)**: "must take reasonable steps" to inform potential investors; no time limit.
- **s 241(7)**: the offer is kept open "for at least 14 days after the lodgment": a minimum period of a state, not a deadline for an act.
- **s 243(1), (2), s 245(2)(b), s 246(1), s 257(5)**: what a prospectus, a profile statement or a document "must contain" or "must state": a status of a document, with no time limit.
- **s 252(1)**: a person liable must notify the person making the offer "as soon as practicable", which is not a number; the consequence is the offence of s 252(2), a bar of its own.
- **s 258(1)**: the moneys are held on trust in a separate bank account "until allotment": a continuing status, no act to be done by a day.
- **s 259(2) and s 260(4)**: "immediately repay without interest": "immediately" is not a number; the money consequences that follow a stated number of days (14 days, 5 months) are the joint and several liabilities of s 259(2)(b) and s 260(5), which are liabilities and not duties with a clock of their own.
- **s 260(7B), (7C), (7D)**: the duties to pay into the trust property and to compensate have no time limit (only the limitation of s 260(8)) and no penalty is stated for the offences (finding 4).

## What the text turns out to say (numbered findings)

Each finding was checked against the text or the generated files when written (the check is named).

1. **6 units of the two ranges are shown deleted or repealed**: s 240(6), s 241(6A), s 244, s 247(4), s 251(3)(a)(ii), s 256. The newest is s 251(3)(a)(ii), "[Deleted by Act 12 of 2026 wef 29/06/2026]". Check: `grep -n "Repealed\|Deleted"` over the lines of the two ranges prints exactly these lines; the rows are the `repealed or blank in this text` rows above.
2. **`inputs/HEADINGS.md` is wrong for the two repealed sections**: it lists s 244 with an empty title and s 256 with a line of s 255(7) as its title, because neither repealed section has a marginal heading of its own. Check: `grep -n "s 244\|s 256" inputs/HEADINGS.md`.
3. **The rendering numbers 13 units alike** (for example s 243(3) prints (c) to (g) twice, s 242(9) prints "(a)" twice, s 240AA(5) "structured notes" prints "(b)" twice, s 239(1) "related party" (b) prints "(ii)" twice). The labels keep the text's numbering and the second one is marked in the coverage table; the readings are F13, F21, F24. Check: the rows of the coverage table whose first column ends "(second one numbered alike)" (`work/units.py`).
4. **The offences of s 260(7B), (7C) and (7D) state no penalty.** Each says the person "shall be guilty of an offence and shall be liable, in addition to the penalty or punishment for the offence" to pay or compensate, and none gives a fine or a term (F72, src:41770 to 41812). So there is no penalty function for them. Every other offence of the two ranges states one: 24 penalty functions, over 6 combinations of fine, term and daily fine (below).
5. **s 260(8) refers to "compensation under subsection (7)"**, and subsection (7) gives the applicant an option to avoid the allotment, not compensation; the compensation is in (7B) to (7D). The function reads (8) as covering the compensation of (7B) to (7D) (F73).
6. **s 253(1) and s 254(1) open with the same "Where" block** of facts: the first five lines after the section number are identical in the two sections (a `diff` of src:40973 to 40977 against src:41164 to 41168, with the section numbers removed, prints nothing). Each section has its own function over the same inputs (F44).
7. **s 250(3) gives two periods**: 24 months from the registration of the base prospectus for debentures or units of debentures issued under a debenture issuance programme, and 6 months from registration in any other case (src:40407 to 40418); `s 250(3) the last day of the period` takes the first case as a fact.
8. **s 240AA(5) "structured notes"**: after paragraph (b)(iv) the rendering prints a second "(b)" and four more variables numbered (v) to (viii); and paragraph (a) joins "(i) in relation to (A) ...; or (B) ...; or (ii) by a specified financial institution" with "or", though the numbering reads like "and" (F13, F21). Both readings are in the register with the branch to flip.
9. **The penalties of the offences, by script** (read from the `Penalty OF` lines of the layer-1 files; 24 penalty functions): $150,000 fine, or imprisonment up to 24 months, or both, further fine $15,000 for each day (5 offences: s 240(17), s 240(7), s 242(11), s 253(1), s 259(1)(d)); $100,000 fine, no imprisonment stated, further fine $10,000 for each day (2 offences: s 241(15), s 242(12)); $50,000 fine, or imprisonment up to 24 months, or both, further fine $5,000 for each day (1 offence: s 258(3)); $50,000 fine, or imprisonment up to 12 months, or both, further fine $5,000 for each day (7 offences: s 240AA(4), s 249(2), s 249A(3), s 250(4), s 251(12), s 259(12), s 259(8)); $50,000 fine, no imprisonment stated, further fine $5,000 for each day (8 offences: s 239(5A), s 240AB(5), s 241(16), s 245(3), s 247(5), s 249(4), s 251(15), s 259(10)); $50,000 fine, no imprisonment stated, further fine none stated for each day (1 offence: s 252(2)). The heaviest is $150,000 or 24 months, and no offence of the range has a higher penalty.
10. **s 239(8) is a date gate**: "This Division applies only in relation to offers ... made on or after 1 July 2002" (src:37826 to 37827); for any offer made today it is met, and `s 239(8) this Division applies to the offer` takes the date of the offer as a fact.
11. **A defence is a proof, and the delegated rulings decide the answer when it is not shown**: s 255(1) to (6), s 259(4) and s 260(6) each turn on "if the person proves" (or "if he or she proves", "if the director proves"); the answer on facts that do not prove the defence is `JUST FALSE` worded "this section gives no defence on these facts" (the ruling of 2026-11-05), not "the person is guilty".
12. **The seat is built so that a caller cannot turn `NOTHING` into `FALSE`**: the seat questions pass the answers of other questions as `MAYBE BOOLEAN` and turn a person's plain "no" to an exemption or a route into `NOTHING`, never into `JUST FALSE` (`work/verify.py` (h) and `sfac-cases-seat.l4`).

## The seat (sfac)

The seat is an issuer, an offeror or a director of either, asking whether a prospectus is required and what it must contain (`sfac-seat.l4`, 21 questions, each `@export` ending in `?`, every input with an `@desc`, in the text order of the sections; `sfac-cases-seat.l4` has the cases).
A question is "Under section N, ..." in the person's words; it never restates a rule: it calls the layer-1 function and the keel's function for a keel term (`s 2(1) "director" the person is a director` for "I am a director of the corporation").
There is no seat for an official.
No question's name and body differ in direction or subject (checked by reading each name against the function it calls: `JUST TRUE` is yes in every one).
The facts that the keel's seat does not ask and this part's seat does are named as `inputs/PLAN.md` sections 7.1 and 7.2 fix them (`the date asked`, `I am a director of the corporation`).
For a question whose function takes the answers of other functions, the person's plain "no" to an exemption or a route is passed as `NOTHING` (never `JUST FALSE`), so that a bar is never lifted by an answer the text did not give.
In the s 253(1) question, `the entity is also the issuer` and the proposed-director fact of s 253(4)(b) are passed as `FALSE`: they matter only when the person is not a director of the entity making the offer, and the seat asks the person as a director (finding of the seat, recorded here).

## What the text does not answer

Each is a place where the text stops, and where this part answers `NOTHING`, takes an input, or states the reading it took in the fork register.

- **The penalty for the offences of s 260(7B), (7C) and (7D)**: each says the person "shall be guilty of an offence and shall be liable, in addition to the penalty or punishment for the offence" to pay or compensate, and none states a penalty (F72); there is no penalty function for them.
- **s 260(8)**: "compensation under subsection (7)": subsection (7) gives no compensation; (7B) to (7D) do (F73).
- **"authorised by this section" (s 251)**: undefined; the combining function answers `JUST TRUE` through a listed safe harbour and `NOTHING` otherwise (F40).
- **How the three matters of s 251(2) are weighed**: "regard must be had to" says what is looked at and not how it is weighed; the function asks whether regard was had (F41).
- **The periods, days and conditions the Authority or the regulations prescribe** (the period of s 240(8), the conditions of s 243(4A), the other sums and variables of s 240AA(5)): inputs, not numbers from memory.
- **A longer period notified under s 259(1)(b) that is outside 7 to 12 weeks**: the text says "not exceeding 12 weeks"; a period of 6 weeks or less leaves the 6 weeks, and one above 12 is not one the text allows, so 6 weeks stands (F59).
- **Section 262(3)** (asset-backed securities), **section 280**, **Subdivision (4)** (the exemptions) and **section 341**: other parts' or later waves' provisions, taken as inputs (Seams).
- **Whether the exemption of s 240AB(1) and (2) lapses on a breach of its conditions**: the text makes a breach an offence (s 240AB(5)) and does not say the exemption lapses; the exemption function does not look at the conditions.
- **"Immediately" and "as soon as practicable"** (s 252(1), s 259(2), s 260(4)): no number of days.
- **Which provisions of Subdivision (2) an exemption under Subdivision (4) reaches**: sfad's ss 272 to 275 say that Subdivisions (1A), (2) and (3) "(other than section 257) do not apply" to an offer; this part takes that as the input of five functions (S9) and the other rules of ss 241 to 260 do not take it, so for an exempted offer the caller must ask `s 239A(1) and (2), s 239(8) and Subdivision (4): this Subdivision applies to the offer` first.

## What the stable binary does not accept

Found on 1.6.110 (the writing build) and 1.6.109 (the second build), by running the files:

- `AFTER` is not an operator on either build (an error in `sfac-257.l4` when a deadline was first written with it); `NOT (x AT MOST y)` is how "after" is written throughout.
- There is no `REFUSE` and no `#ASSERT REFUSED`; "not covered" is `NOTHING`, asserted with `EQUALS NOTHING`.
- `BECAUSE` is accepted only in `LEST BREACH BY p BECAUSE "..."`; every other reason is a `--` comment, and every `NOT` is parenthesised (`verify.py` (d) finds 0 that are not).
- An `#ASSERT` is on one line (`verify.py` (e): 0 continuation lines).
- A name defined in two imported modules cannot be used: every top-level name of this part begins with its section label, so that the merged seat layer can import all parts.
- A regulative bar is written `PARTY p SHANT `action` HENCE FULFILLED LEST BREACH BY p BECAUSE "..."` over `DECLARE `s NNN action` IS ONE OF ...`; a trace is `#TRACE rule args AT 0 WITH PARTY (...) DOES `action` AT n`, and the outcome of every trace is compared on both builds by `work/traces.py` (the numbers of traces and their `-- EXPECT` words are under "What `check.sh` prints" below).
- `check.sh` does not see a different `#TRACE` outcome between the two builds; `work/traces.py` does, and found none.

## Appendix: the Guide's own words for the split sites

Lines of `inputs/ENCODING-GUIDE.md`, copied by script (`work/assemble.py`), that the fork lines of the split sites rely on:

Line 86:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

Line 87:

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

Line 93:

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

Line 94:

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

Line 95:

> - **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Line 99:

>   3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it).

## What `check.sh` prints

Run from this folder as `L4=<l4 1.6.110> L4_MAIN=<l4 1.6.109> ./check.sh` on 2026-11-19, after the last regeneration of the modules.
Exit code 0.
Every module compiles with no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning`, every assertion is satisfied on both builds, and the four counts of each module are the same on both.
The 12 `sfa-*.l4` modules are the keel's and were already in the folder (their tests are not in this deposit); the other rows are this part's.
Output, verbatim:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sfa-application.l4                             0         0       0        0         0 |      0         0       0        0  same
sfa-associates.l4                              0         0       0        0         0 |      0         0       0        0  same
sfa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-benchmarks.l4                  0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-markets.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-persons.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-products.l4                    0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-rest.l4                        0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-schemes.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-interests.l4                               0         0       0        0         0 |      0         0       0        0  same
sfa-investors.l4                               0         0       0        0         0 |      0         0       0        0  same
sfa-periods.l4                                 0         0       0        0         0 |      0         0       0        0  same
sfac-239.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-240.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-240aa.l4                                  0         0       0        0         0 |      0         0       0        0  same
sfac-241.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-242.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-243.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-249.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-253.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-257.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfac-cases-seat.l4                             0        75       0        0         0 |      0        75       0        0  same
sfac-duties.l4                                 0         0       0        0         0 |      0         0       0        0  same
sfac-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sfac-tests-239.l4                              0       184       0        0         0 |      0       184       0        0  same
sfac-tests-240.l4                              0       152       0        0         0 |      0       152       0        0  same
sfac-tests-240aa.l4                            0       159       0        0         0 |      0       159       0        0  same
sfac-tests-241.l4                              0       210       0        0         0 |      0       210       0        0  same
sfac-tests-242.l4                              0        90       0        0         0 |      0        90       0        0  same
sfac-tests-243.l4                              0       136       0        0         0 |      0       136       0        0  same
sfac-tests-249.l4                              0       296       0        0         0 |      0       296       0        0  same
sfac-tests-253.l4                              0       168       0        0         0 |      0       168       0        0  same
sfac-tests-257.l4                              0       213       0        0         0 |      0       213       0        0  same
sfac-tests-duties.l4                           0         0       0        0         0 |      0         0       0        0  same
TOTAL (34 modules)                             0      1683       0        0           |      0      1683       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline it replaced: the keel's own run (`inputs/KEEL-NOTES.md`, "What `check.sh` prints") was `TOTAL (26 modules) 0 1069 0 0`, with its tests and seat; the folder this part was given held only the 12 keel modules (no assertions), so the run before this part's first file counted 12 modules and 0 assertions.
Now: 34 modules, 1683 assertions satisfied (this part: 22 modules and 1683 assertions of its own, the 12 keel modules adding none).

`work/traces.py` (outcome of every `#TRACE` on both builds against its `-- EXPECT` word, which `check.sh` does not see):

```
traces: 77, mismatches: 0
```

77 traces, 77 with outcome equal to the `-- EXPECT` word on 1.6.110 and 1.6.109 (31 BREACH, 25 FULFILLED, 21 RESIDUAL).

`srcrefs.py` over the layer-1 modules (`python3 -I srcrefs.py check --refs ../../../inputs/SFA2001.txt sfac-*.l4`, then the same with `--strict`):

```
srcrefs check: 2827 src: lines, 338 runs, 406 locators, 0 problems
srcrefs check: 2827 src: lines, 338 runs, 406 locators, 0 problems
```

`work/verify.py`, which checks what `check.sh` does not, on the final run:

```
(a) non-blank lines 2587 of the two ranges, each in exactly one row: YES; rows 808; rows by disposition: {'inert': 39, 'encoded': 616, 'fork': 147, 'repealed or blank in this text': 6}; units (rows) with no declaration and no inert range: 0
(b) top-level names (functions, types, constructors): 445; not beginning with a provision label: 0
(c) quotes checked: 581 segments, 0 problems; branches answering JUST FALSE or NOTHING: 560, untagged: 0
(d) unbracketed NOT in code: 0
(e) #ASSERT continuation lines: 0
(f) forbidden words in code (REFUSE, REFUSED, BECAUSE outside LEST BREACH, a YMD of my own, WAIT UNTIL, AFTER as an operator): 0
(g) files with an emoji: 0
(h) seat questions: 21, not ending in "?": 0
    seat inputs: 89, without @desc: 0
```

