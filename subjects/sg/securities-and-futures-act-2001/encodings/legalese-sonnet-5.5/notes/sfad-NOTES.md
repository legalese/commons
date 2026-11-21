# NOTES (sfad): Securities and Futures Act 2001 (Singapore), Part 13 Division 1 Subdivisions (3), (4) and (5)

Status, 2026-11-19: layer 1 (seven modules and their tests) and layer 2 (the seat and its cases) are written and checked with the stable builds named under "What check.sh prints" below.
Every statement of a count in this file was read from a run on 2026-11-19 (the commands are named where they matter); none is carried from an earlier session.
Where PLAN.md and the brief differ, the brief governs; the one place they differ for this part is noted under "Seams (sfad)".

## Edition encoded

The Securities and Futures Act 2001 (Singapore), 2020 Revised Edition, as rendered by Singapore Statutes Online as an informal consolidation "version in force from 29/6/2026 to 20/10/2026", file `inputs/SFA2001.txt`.
It is a rendering of a PDF, not the official text; the amendment marks it shows were read as the text of the day.
This part encodes lines 41833-45043: Part 13 Division 1 Subdivision (3) (debentures, ss 261 to 271), Subdivision (4) (exemptions, ss 272 to 282) and Subdivision (5) (general, s 282AA).
`inputs/NAIVE-EVIDENCE/` is not among the inputs of this run (the folder is absent from INPUTS_DIR), so there is no comparison with an earlier pass and no section for one.

Files: layer 1 `sfad-debentures.l4`, `sfad-nocons-small-private.l4`, `sfad-circumstances.l4`, `sfad-investor-exemptions.l4`, `sfad-ois-intl-gov-atm.l4`, `sfad-directions.l4`, `sfad-exemption-summary.l4`; their tests `sfad-tests-*.l4`; layer 2 `sfad-seat.l4` and `sfad-cases-seat.l4`; `PROGRESS.md`.
No file needed `NEEDS-CORE.md`: the core types used are `Penalty` and the keel's period functions, and every type and constructor this part declares begins with its section label.

## Coverage (sfad)

One row per provision cited by an `@ref` in a layer-1 module (a section, subsection, paragraph or defined term, at the finest level the text states a rule), in text order, plus the rows for the headings and the repealed text.
A row is `encoded` when the provision is a rule, definition or table in layer-1 L4 with a test; `fork` when a fork-register entry (below) concerns it and the row names the entry; `inert 1` for a heading; `repealed` for text the rendering shows repealed or deleted.
No row is `inert 2` or `inert 3`, and there is no `out-of-scope` or `deferred` row.
Every encoded function has at least one assertion in a tests file or in `sfad-cases-seat.l4` (checked by script: the function's name occurs in one of them).
The line check, by script over lines 41833-45043: rows(cites): 244; text lines: 2072; in a locator: 2029; in no locator: 43; classified inert/repealed: 29; GAPS: 0.
Every line in no locator is a heading, a Subdivision heading or text shown repealed; none is left over (the script prints GAP for any other).

| Provision | Source lines | Disposition | L4 name(s) | Fork ids | Seat question |
| --- | --- | --- | --- | --- | --- |
| (Subdivision (3) — Debentures Preliminary provisions) | 41833-41835 | inert 1 (a heading) | - | - | |
| s 261(1) | 41837-41838 | fork | `s 261(1) this Subdivision applies to the offer` | s261-1 |  |
| s 261(1A) | 41840-41841 | fork | `s 261(1A) sections 268, 269 and 270 do not apply to the borrowing entity` | s261-1A |  |
| s 261(1B) | 41843-41849 | encoded | `s 261(1B) the entity is a prescribed entity` |  |  |
| s 261(1C) | 41851-41864 | fork | `s 261(1C)(a) the Authority may impose a condition or restriction on the entity`; `s 261(1C)(b) the Authority may vary or revoke the condition or restriction`; `s 261(1C) the prescribed entity must comply with the condition or restriction`; `s 261(1C) the duty of a prescribed entity to comply with a condition or restrict...` | s261-1Ca, s261-1Cb, s261-1C |  |
| s 261(1D) | 41866-41871 | fork | `s 261(1D) the person is guilty of an offence`; `s 261(1D) the penalty for the offence` | s261-1D | yes |
| ((2) [Deleted by Act 1 of 2005]) | 41873-41873 | repealed (the text shows it repealed) | - | - | |
| s 261(3) | 41875-41877 | fork | `s 261(3) the corporation is related to the other corporation for this Subdivisio...` | s261-3 |  |
| (Offer of asset‑backed securities) | 41879-41879 | inert 1 (a heading) | - | - | |
| s 262(1) | 41881-41886 | encoded | `s 262(1) the asset-backed securities are issued by a special purpose vehicle or ...` |  |  |
| s 262(2) | 41888-41890 | fork | `s 262(2) the person is exempt from section 262` | s262-2 |  |
| s 262(3) "asset-backed securities" | 41892-41895 | encoded | `s 262(3) the securities are asset-backed securities` |  |  |
| s 262(3) | 41894-41895 | fork | `s 262(3) the securities are asset-backed securities as section 262(3) defines th...` | sum-S5 | yes |
| s 262(3) "securitisation transaction" | 41897-41912 | encoded | `s 262(3) the arrangement is a securitisation transaction` |  |  |
| s 262(3) "special purpose vehicle" | 41914-41923 | encoded | `s 262(3) the body is a special purpose vehicle` |  |  |
| (263. [Repealed by Act 16 of 2003] 264. [Repealed by Act 16 o) | 41925-41929 | inert 1 (a heading); repealed (the text shows it repealed) | - | - | |
| s 265(1) | 41931-41962 | fork | `s 265(1) the court may order the security for the debentures to be enforceable` | s265-1 |  |
| s 265(2) | 41964-41967 | encoded | `s 265(2) section 265(1) does not affect the power` |  |  |
| (Requirement for trustees) | 41969-41969 | inert 1 (a heading) | - | - | |
| s 265A(1) | 41971-41974 | fork | `s 265A(1) the borrowing entity must appoint a trustee for the holders of debentu...`; `s 265A(1) the duty to appoint a trustee for the holders of debentures` | s265A-1 | yes |
| s 265A(2) | 41978-42029 | fork | `s 265A(2) the borrowing entity has ensured that the appointed trustee meets the ...` | s265A-2 |  |
| s 265A(3) | 42033-42060 | encoded | `s 265A(3) the borrowing entity has considered the matters before being satisfied` |  |  |
| s 265A(4) | 42064-42068 | fork | `s 265A(4) the person is guilty of an offence`; `s 265A(4) the penalty for the offence` | s265A-4 | yes |
| s 265A(5) | 42072-42077 | encoded | `s 265A(5) the debentures are asset-backed securities or structured notes` |  |  |
| (Duties of trustees) | 42081-42081 | inert 1 (a heading) | - | - | |
| s 266(1) | 42083-42100 | encoded | `s 266(1) the trustee for the holders of debentures has done what paragraphs (a) ...` |  |  |
| s 266(2) | 42107-42113 | fork | `s 266(2) the trustee may apply to the Authority for an order` | s266-2 |  |
| s 266(3)(a) | 42115-42125 | fork | `s 266(3)(a) the Authority may impose restrictions on the activities of the borro...` | s266-3a |  |
| s 266(3)(b) | 42127-42129 | fork | `s 266(3)(b) the Authority must direct the trustee to apply to the court`; `s 266(3)(b) the trustee must apply to the court as directed`; `s 266(3)(b) the duty of the trustee to apply to the court as directed` | s266-3b |  |
| s 266(4) | 42131-42145 | fork | `s 266(4) the trustee may apply to the court for an order under subsection (5)`; `s 266(4) the trustee must apply to the court for an order under subsection (5)`; `s 266(4) the duty of the trustee to apply to the court on the request of the bor...` | s266-4a, s266-4b |  |
| s 266(5) | 42147-42178 | fork | `s 266(5) the court may make the order`; `s 266(5) the court has done what it must in making the order` | s266-5 |  |
| s 266(6) | 42180-42181 | encoded | `s 266(6) the court may vary or rescind the order` |  |  |
| s 266(7) | 42183-42187 | encoded | `s 266(7) the trustee has had the regard the subsection requires` |  |  |
| s 266(8) | 42189-42193 | fork | `s 266(8) the trustee may rely on the certificate, report or statement` | s266-8 |  |
| (Powers of trustee to apply to court for directions, etc.) | 42198-42198 | inert 1 (a heading) | - | - | |
| s 267(1) | 42200-42207 | fork | `s 267(1) the trustee for the holders of debentures may apply to the court` | s267-1 |  |
| s 267(2) | 42209-42218 | encoded | `s 267(2) the court may give directions or accede to the application` |  |  |
| s 267(2)(b) | 42214-42218 | fork | `s 267(2)(b) the court may accede to the application on terms or make another ord...` | s267-2b |  |
| s 267(3) | 42220-42224 | encoded | `s 267(3) the court may order a meeting of the holders of debentures to be called` |  |  |
| s 267(4) | 42226-42228 | encoded | `s 267(4) the meeting is held and conducted as the subsection requires` |  |  |
| (Right of Authority, approved exchange and holders of debentu) | 42230-42231 | inert 1 (a heading) | - | - | |
| s 267A | 42233-42240 | fork | `s 267A the person may apply to the court for an order compelling the trustee to ...`; `s 267A the court may make the order or dismiss the application` | s267A-1 |  |
| (Obligations of borrowing entity 268.—(1) [Deleted by Act 34 ) | 42247-42253 | inert 1 (a heading); repealed (the text shows it repealed) | - | - | |
| s 268(4) | 42255-42259 | fork | `s 268(4) the entity must provide the trustee with particulars of the charge` | s268-4 |  |
| s 268(4)(a) | 42261-42264 | fork | `s 268(4)(a) the particulars of the charge are provided in time`; `s 268(4)(a) the duty to provide the trustee with particulars of the charge withi...` | s268-4a |  |
| s 268(4)(b) | 42266-42269 | encoded | `s 268(4)(b) the particulars of the amounts advanced are provided in time`; `s 268(4)(b) the duty to provide the trustee with particulars of the amounts adva...` |  |  |
| s 268(5) | 42271-42274 | encoded | `s 268(5) it is sufficient to provide particulars of the net amount every 3 month...` |  |  |
| s 268(6) | 42276-42278 | encoded | `s 268(6) the directors or equivalent persons must cause the accounts to be made ...` |  |  |
| s 268(6)(a) | 42280-42283 | encoded | `s 268(6)(a) the half-year accounts are made out and lodged in time`; `s 268(6)(a) the duty to lodge the half-year accounts with the trustee within 3 m...` |  | yes |
| s 268(6)(b) | 42285-42288 | encoded | `s 268(6)(b) the annual accounts are made out and lodged in time`; `s 268(6)(b) the duty to lodge the annual accounts with the trustee within 5 mont...` |  | yes |
| s 268(6A) | 42295-42298 | encoded | `s 268(6A) the person has used the due care the subsection requires` |  |  |
| s 268(7) | 42302-42306 | fork | `s 268(7) the person is guilty of an offence`; `s 268(7) the penalty for the offence` | s268-7 | yes |
| s 268(7A) | 42308-42311 | fork | `s 268(7A) the person is guilty of an offence`; `s 268(7A) the penalty for the offence` | s268-7A |  |
| s 268(8) | 42315-42320 | encoded | `s 268(8) the account and balance sheet are treated as financial statements for t...` |  |  |
| s 268(9) | 42326-42331 | fork | `s 268(9) the trustee must lodge notice of that fact with the Authority`; `s 268(9) the duty of the trustee to lodge notice with the Authority` | s268-9, s268-9i |  |
| s 268(10)(a) | 42335-42340 | encoded | `s 268(10)(a) the half-year accounts need not be audited` |  |  |
| s 268(10)(b) | 42345-42352 | fork | `s 268(10)(b) the annual accounts need not be audited, or the audit may be limite...` | s268-10b |  |
| s 268(11) | 42356-42363 | fork | `s 268(11) the directors or equivalent persons must lodge a copy of the notice wi...`; `s 268(11) the copy of the notice is lodged at the time the accounts are lodged`; `s 268(11) the duty to lodge a copy of the trustee's notice with the Authority at...` | s268-11, s268-11t |  |
| s 268(12) | 42365-42372 | fork | `s 268(12) the accounts may be based on the directors' estimate of the stock in t...` | s268-12 |  |
| s 268(13) | 42374-42379 | encoded | `s 268(13) the estimation is made on the basis the subsection requires` |  |  |
| (Additional obligations of borrowing entity, where debentures) | 42381-42382 | inert 1 (a heading) | - | - | |
| s 268A(1) | 42384-42397 | fork | `s 268A(1) the borrowing entity must prepare and make available a semi-annual rep...`; `s 268A(1) the last day of the period of 6 months covered by a semi-annual report`; `s 268A(1) the duty to prepare and make available a semi-annual report` | s268A-1 |  |
| s 268A(2) | 42401-42404 | encoded | `s 268A(2) the semi-annual report is lodged with the trustee in time`; `s 268A(2) the duty to lodge the semi-annual report with the trustee within 2 mon...` |  | yes |
| s 268A(3) | 42408-42411 | fork | `s 268A(3) the trustee must lodge notice of that fact with the Authority`; `s 268A(3) the duty of the trustee to lodge notice with the Authority` | s268A-3, s268A-3i |  |
| s 268A(4) | 42415-42422 | fork | `s 268A(4) the borrowing entity must disclose the information to the holders of u...`; `s 268A(4) the borrowing entity has disclosed the information as the subsection r...`; `s 268A(4) the duty to disclose information materially affecting the unlisted deb...` | s268A-4, s268A-4i |  |
| s 268A(5) | 42426-42430 | fork | `s 268A(5) the person is guilty of an offence`; `s 268A(5) the penalty for the offence` | s268A-5 |  |
| s 268A(6) | 42434-42438 | fork | `s 268A(6) the borrowing entity must make bid or redemption prices available and ...` | s268A-6 |  |
| s 268A(6)(a) | 42438-42447 | encoded | `s 268A(6)(a) the longest number of days allowed between times bid or redemption ...`; `s 268A(6)(a) the bid or redemption prices are made available often enough` |  |  |
| s 268A(6)(b) | 42449-42453 | encoded | `s 268A(6)(b) the indicative bid prices are clearly stated to be indicative` |  |  |
| s 268A(6)(c) | 42455-42456 | encoded | `s 268A(6)(c) the bid or redemption prices are determined in an independent and f...` |  |  |
| s 268A(7) | 42460-42466 | encoded | `s 268A(7) the accounts are made available to the holders on the day of lodgment`; `s 268A(7) the duty to make the accounts available to the holders on the day of l...` |  |  |
| s 268A(8) | 42470-42474 | fork | `s 268A(8) the person is guilty of an offence`; `s 268A(8) the penalty for the offence` | s268A-8 |  |
| s 268A(9) | 42478-42481 | encoded | `s 268A(9) the person has used the due care the subsection requires` |  |  |
| s 268A(10) | 42485-42488 | fork | `s 268A(10) the person is guilty of an offence`; `s 268A(10) the penalty for the offence` | s268A-10 |  |
| (Obligation of guarantor entity to provide information) | 42495-42495 | inert 1 (a heading) | - | - | |
| s 269(1) | 42497-42503 | fork | `s 269(1) the borrowing entity may require the guarantor entity to provide the in...` | s269-1 |  |
| s 269(2) | 42505-42508 | fork | `s 269(2) the guarantor entity must provide the borrowing entity with the informa...`; `s 269(2) the date specified in the notice is not earlier than 14 days after the ...`; `s 269(2) the information is provided before the date specified in the notice`; `s 269(2) the duty of the guarantor entity to provide the information before the ...` | s269-2, s269-2t | yes |
| s 269(3) | 42510-42516 | fork | `s 269(3) the person is guilty of an offence`; `s 269(3) the penalty for the offence` | s269-3 | yes |
| (Loans and deposits to be immediately repayable on certain ev) | 42518-42519 | inert 1 (a heading) | - | - | |
| s 270(1) | 42521-42527 | fork | `s 270(1) the borrowing entity must make reports to the trustee on the progress o...`; `s 270(1) the duty to make reports to the trustee on progress` | s270-1 |  |
| s 270(2) | 42529-42531 | encoded | `s 270(2) the progress report is included in the report required under section 26...` |  |  |
| s 270(3) | 42533-42548 | fork | `s 270(3) the trustee may give written notice requiring the borrowing entity to r...`; `s 270(3) the trustee must give written notice requiring the borrowing entity to ...`; `s 270(3) the copy of the notice is lodged with the Authority in time`; `s 270(3) the duty of the trustee to lodge a copy of the notice within one month` | s270-3 | yes |
| s 270(4) | 42550-42564 | fork | `s 270(4) the trustee must not give notice under subsection (3)`; `s 270(4) the bar on the trustee giving notice` | s270-4 |  |
| s 270(5) | 42566-42593 | fork | `s 270(5) the borrowing entity is liable to repay the moneys`; `s 270(5) the duty of the borrowing entity to repay the moneys on demand` | s270-5a, s270-5i | yes |
| s 270(6) | 42595-42601 | encoded | `s 270(6) the purpose in the notice is treated as the purpose specified in the pr...` |  |  |
| (Liability of trustees for debenture holders) | 42603-42603 | inert 1 (a heading) | - | - | |
| s 271(1) | 42605-42611 | fork | `s 271(1) the provision is void` | s271-1 | yes |
| s 271(2) | 42613-42632 | encoded | `s 271(2) subsection (1) does not invalidate the release or the provision` |  |  |
| s 271(3) | 42634-42642 | encoded | `s 271(3) subsection (1) does not operate against the provision or the trustee's ...` |  |  |
| Subdivision (4) | 42644-42644 | fork | `Subdivision (4) the offer qualifies for an exemption under Subdivision (4) of Di...` | sum-S4 |  |
| (Issue or transfer of securities or securities‑based derivati) | 42646-42647 | inert 1 (a heading) | - | - | |
| s 272(1) | 42649-42653 | fork | `s 272(1) the offer is exempt from Subdivisions (1A), (2) and (3) of this Divisio...` | s272-1 | yes |
| s 272(2) | 42659-42672 | fork | `s 272(2) the offer of securities-based derivatives contracts is exempt from Subd...` | s272-2 | yes |
| (Small offers) | 42681-42681 | inert 1 (a heading) | - | - | |
| s 272A(1) | 42683-42686 | fork | `s 272A(1) the offer is exempt from Subdivisions (1A), (2) and (3) of this Divisi...` | s272A-1 |  |
| s 272A(1)(a) | 42688-42695 | fork | `s 272A(1)(a) the total amount raised within the period of 12 months does not exc...` | s272A-1a | yes |
| s 272A(1)(b) | 42697-42698 | encoded | `s 272A(1)(b) the person making each offer gives the statement and the notificati...` |  |  |
| s 272A(1)(b)(i) | 42697-42723 | encoded | `s 272A(1)(b)(i) the statement in writing is given as the paragraph requires` |  |  |
| s 272A(1)(b)(ii) | 42728-42748 | fork | `s 272A(1)(b)(ii) the notification in writing is given as the paragraph requires` | s272A-1bii |  |
| s 272A(1)(c) | 42750-42752 | encoded | `s 272A(1)(c) none of the offers is accompanied by an advertisement` |  | yes |
| s 272A(1)(d) | 42754-42784 | fork | `s 272A(1)(d) the expense is one the exemption allows`; `s 272A(1)(d) the selling or promotional expenses are ones the exemption allows` | s272A-1d |  |
| s 272A(1)(e) | 42786-42796 | encoded | `s 272A(1)(e) no prospectus is registered, or the registered prospectus has expir...` |  |  |
| s 272A(2) | 42802-42808 | fork | `s 272A(2) the statement and notification are treated as given` | s272A-2 |  |
| s 272A(3) | 42810-42811 | encoded | `s 272A(3) the offer is a personal offer of securities or securities-based deriva...` |  |  |
| s 272A(3)(a) | 42813-42814 | encoded | `s 272A(3)(a) the offer may be accepted only by the person to whom it is made` |  |  |
| s 272A(3)(b) | 42816-42827 | fork | `s 272A(3)(b) the offer is made to a person who is likely to be interested in tha...` | s272A-3b |  |
| s 272A(3)(b)(iii) | 42829-42852 | encoded | `s 272A(3)(b)(iii) the person has previously indicated that the person is interes...` |  |  |
| s 272A(3)(b)(iii)(F) | 42854-42886 | encoded | `s 272A(3)(b)(iii)(F) the person to whom the indication was made is a foreign reg...` |  |  |
| s 272A(4) | 42890-42907 | encoded | `s 272A(4) the amount raised by an offer` |  |  |
| s 272A(5) | 42911-42928 | fork | `s 272A(5) the amounts raised by earlier offers that must be included` | s272A-5 |  |
| s 272A(6) | 42932-42934 | encoded | `s 272A(6) the offer is a closely related offer` |  |  |
| s 272A(7) | 42936-42939 | encoded | `s 272A(7) the offer is treated as made by that other person` |  |  |
| s 272A(8) | 42943-42950 | fork | `s 272A(8) Subdivisions (2) and (3) of this Division apply to the offer that resu...` | s272A-8 |  |
| s 272A(8)(a) | 42952-42953 | encoded | `s 272A(8)(a) the subsequent offer is made in reliance on another exemption of th...` |  |  |
| s 272A(8)(b) | 42955-42958 | fork | `s 272A(8)(b) the subsequent offer is made in reliance on subsection (1) and at l...` | s272A-8b |  |
| s 272A(8)(c) | 42960-42960 | encoded | `s 272A(8)(c) the subsequent offer is one that meets sub-paragraphs (i) to (v)` |  |  |
| s 272A(8)(c)(i) | 42960-42963 | encoded | `s 272A(8)(c)(i) the subsequent offer may be accepted only by the person to whom ...` |  |  |
| s 272A(8)(c)(ii) | 42968-42977 | encoded | `s 272A(8)(c)(ii) the subsequent offer is made to a person likely to be intereste...` |  |  |
| s 272A(8)(c)(ii)(C) | 42979-43037 | encoded | `s 272A(8)(c)(ii)(C) the person has previously indicated that the person is inter...` |  |  |
| s 272A(8)(c)(iii) | 43039-43108 | encoded | `s 272A(8)(c)(iii) the statement and notification are given` |  |  |
| s 272A(8)(c)(iv) | 43110-43112 | encoded | `s 272A(8)(c)(iv) the subsequent offer is not accompanied by an advertisement` |  |  |
| s 272A(8)(c)(v) | 43114-43144 | encoded | `s 272A(8)(c)(v) no selling or promotional expenses are paid or incurred other th...` |  |  |
| s 272A(9) | 43148-43150 | encoded | `s 272A(9) the statement and notification in subsection (8)(c)(iii) are treated a...` |  |  |
| s 272A(10) | 43152-43195 | fork | `s 272A(10) the communication is an advertisement` | s272A-10 |  |
| s 272A(11) | 43199-43208 | fork | `s 272A(11) the matter is included in the affairs of the person making the offer,...` | s272A-11 |  |
| (Private placement) | 43215-43215 | inert 1 (a heading) | - | - | |
| s 272B(1) | 43217-43220 | fork | `s 272B(1) the offers are exempt from Subdivisions (1A), (2) and (3) of this Divi...` | s272B-1 |  |
| s 272B(1)(a) | 43222-43223 | encoded | `s 272B(1)(a) the offers are made to no more than the applicable number of person...` |  | yes |
| s 272B(1)(b) | 43225-43227 | encoded | `s 272B(1)(b) none of the offers is accompanied by an advertisement` |  |  |
| s 272B(1)(c) | 43229-43252 | encoded | `s 272B(1)(c) no selling or promotional expenses are paid or incurred other than ...` |  |  |
| s 272B(1)(d) | 43254-43274 | encoded | `s 272B(1)(d) no prospectus is registered, or the registered prospectus has expir...` |  |  |
| s 272B(2) | 43280-43281 | encoded | `s 272B(2) the applicable number of persons` |  |  |
| s 272B(3) | 43283-43299 | fork | `s 272B(3) the number of persons to whom earlier offers were made that must be in...` | s272B-3 |  |
| s 272B(4) | 43303-43305 | encoded | `s 272B(4) the offer is a closely related offer` |  |  |
| s 272B(5) | 43310-43375 | fork | `s 272B(5) the number of persons the offer to the offeree counts as` | s272B-5 |  |
| s 272B(5)(e) | 43338-43340 | encoded | `s 272B(5)(e) the offers are treated as made by that other person` |  |  |
| s 272B(5)(f) | 43342-43349 | encoded | `s 272B(5)(f) only the second-mentioned person is counted` |  |  |
| s 272B(5)(g) | 43354-43375 | encoded | `s 272B(5)(g) both persons are counted` |  |  |
| s 272B(6) | 43379-43380 | encoded | `s 272B(6) the communication is an advertisement for subsection (1)(b)` |  |  |
| (Offer made under certain circumstances) | 43382-43382 | inert 1 (a heading) | - | - | |
| s 273(1) | 43384-43386 | fork | `s 273(1) the offer is exempt from Subdivisions (2) and (3) of this Division (oth...` | s273-1 |  |
| s 273(1)(a) | 43388-43389 | encoded | `s 273(1)(a) the offer is made in connection with a take-over offer in compliance...` |  | yes |
| s 273(1)(b) | 43391-43410 | encoded | `s 273(1)(b) the offer is made in connection with an acquisition offer for the sh...` |  |  |
| s 273(1)(c) | 43412-43425 | encoded | `s 273(1)(c) the offer is made in connection with a compromise or arrangement of ...` |  |  |
| s 273(1)(ca) | 43427-43441 | encoded | `s 273(1)(ca) the offer is made in connection with an acquisition offer for the s...` |  |  |
| s 273(1)(cb) | 43443-43455 | encoded | `s 273(1)(cb) the offer is made in connection with a compromise or arrangement of...` |  |  |
| s 273(1)(cc) | 43457-43459 | encoded | `s 273(1)(cc) the offer is an offer to enter into an underwriting agreement` |  |  |
| s 273(1)(cd) | 43461-43484 | fork | `s 273(1)(cd) the offer is an offer of securities of an unlisted entity, or a non...` | s273-1cd |  |
| s 273(1)(cda) | 43488-43515 | encoded | `s 273(1)(cda) the offer is an offer of SDRs whose underlying securities are of a...` |  |  |
| s 273(1)(ce) | 43519-43530 | encoded | `s 273(1)(ce) the offer of shares or debentures is made to existing holders where...` |  | yes |
| s 273(1)(cf) | 43534-43536 | encoded | `s 273(1)(cf) the offer of debentures is made to an existing holder of listed deb...` |  |  |
| s 273(1)(cg) | 43538-43557 | encoded | `s 273(1)(cg) the offer of units of shares or debentures is made to existing hold...` |  |  |
| s 273(1)(ch) | 43561-43565 | encoded | `s 273(1)(ch) the offer of units of debentures is made to an existing holder of l...` |  |  |
| s 273(1)(ci) | 43567-43570 | encoded | `s 273(1)(ci) the offer is made in the circumstances specified under section 178 ...` |  |  |
| s 273(1)(cj) | 43572-43593 | encoded | `s 273(1)(cj) the offer of units in a listed business trust is made to existing h...` |  |  |
| s 273(1)(ck) | 43597-43626 | encoded | `s 273(1)(ck) the offer of derivatives of units in a listed business trust is mad...` |  |  |
| s 273(1)(cl) | 43630-43663 | encoded | `s 273(1)(cl) the offer of units or derivatives of units is made to existing hold...` |  |  |
| s 273(1)(cm) | 43669-43697 | encoded | `s 273(1)(cm) the offer of SDRs with units in a business trust is made to existin...` |  |  |
| s 273(1)(d) | 43701-43709 | encoded | `s 273(1)(d) the offer is an offer of previously issued shares or debentures list...` |  |  |
| s 273(1)(da) | 43711-43720 | encoded | `s 273(1)(da) the offer is an offer of previously issued units in a business trus...` |  |  |
| s 273(1)(e) | 43722-43732 | encoded | `s 273(1)(e) the offer is an offer of previously issued securities-based derivati...` |  |  |
| s 273(1)(ea) | 43734-43743 | encoded | `s 273(1)(ea) the offer is an offer of previously issued SDRs listed and traded o...` |  |  |
| s 273(1)(f) | 43747-43766 | encoded | `s 273(1)(f) the offer is an offer of securities-based derivatives contracts dete...` |  |  |
| s 273(1)(g) | 43768-43793 | encoded | `s 273(1)(g) the offer is an offer of cash-settled securities-based derivatives c...` |  |  |
| s 273(1)(h) | 43795-43817 | encoded | `s 273(1)(h) the offer is an offer of securities-based derivatives contracts sett...` |  |  |
| s 273(1)(i) | 43819-43826 | encoded | `s 273(1)(i) the offer is made by an entity to a qualifying person` |  |  |
| s 273(1)(ia) | 43830-43835 | encoded | `s 273(1)(ia) the offer is an offer of SDRs made or treated as made by an entity ...` |  |  |
| s 273(1)(j) | 43839-43846 | encoded | `s 273(1)(j) the offer is made by a trustee-manager of a business trust to a qual...` |  |  |
| s 273(1)(k) | 43855-43861 | encoded | `s 273(1)(k) the offer is an offer of SDRs made or treated as made by a trustee-m...` |  |  |
| s 273(1AA) | 43865-43868 | fork | `s 273(1AA) the securities of the entity are treated as listed for quotation on t...` | s273-1AA |  |
| s 273(1AB) | 43872-43875 | encoded | `s 273(1AB) the shares of the entity are treated as listed for quotation on the a...` |  |  |
| s 273(1AC) | 43879-43883 | encoded | `s 273(1AC) the units in the business trust are treated as listed for quotation o...` |  |  |
| s 273(1A) | 43887-43943 | fork | `s 273(1A) the offer is excluded from paragraphs (d), (da), (e), (ea) and (h) of ...` | s273-1A |  |
| s 273(1AAA) | 43949-43959 | encoded | `s 273(1AAA) the issuer is treated as having borrowed the securities being offere...` |  |  |
| s 273(1B) | 43966-43968 | fork | `s 273(1B) Subdivision (1A) of this Division does not apply to the offer` | s273-1B |  |
| s 273(2) | 43972-43998 | encoded | `s 273(2) no selling or promotional expenses are paid or incurred other than thos...` |  |  |
| ((3) [Deleted by Act 1 of 2005]) | 44004-44004 | repealed (the text shows it repealed) | - | - | |
| s 273(4)(a) | 44006-44024 | encoded | `s 273(4)(a) the person is a qualifying person in relation to the entity` |  |  |
| s 273(4)(b) | 44026-44038 | encoded | `s 273(4)(b) the person is a qualifying person in relation to the business trust` |  |  |
| s 273(5) | 44044-44057 | fork | `s 273(5) the offer is within the period of 6 months from the date of the Authori...` | s273-5 | yes |
| s 273(6) | 44063-44065 | fork | `s 273(6) the Authority may impose conditions or restrictions on the offer` | s273-6 |  |
| s 273(7) | 44070-44070 | encoded | `s 273(7) the declaration made under subsection (5) is final` |  |  |
| s 273(8) | 44072-44077 | fork | `s 273(8) the person is guilty of an offence`; `s 273(8) the penalty for the offence` | s273-8 |  |
| s 273(8A) | 44079-44106 | encoded | `s 273(8A) the person must not advertise or publish what the subsection bars`; `s 273(8A) the bar on advertising or publishing` |  | yes |
| s 273(8B) | 44110-44117 | fork | `s 273(8B) the person is guilty of an offence`; `s 273(8B) the penalty for the offence` | s273-8B | yes |
| s 273(9) | 44124-44131 | encoded | `s 273(9) the corporation is an unlisted corporation` |  |  |
| s 273(10) | 44135-44136 | encoded | `s 273(10) the corporation is a corporation for paragraphs (ca) and (cb)` |  |  |
| (Offer made to institutional investors) | 44138-44138 | inert 1 (a heading) | - | - | |
| s 274 | 44140-44143 | fork | `s 274 the offer is exempt from Subdivisions (1A), (2) and (3) of this Division (...` | s274-1 | yes |
| (Offer made to accredited investors and certain other persons) | 44149-44149 | inert 1 (a heading) | - | - | |
| s 275(1) | 44151-44155 | fork | `s 275(1) the offer is exempt from Subdivisions (1A), (2) and (3) of this Divisio...` | s275-1 | yes |
| s 275(1)(a) | 44157-44158 | encoded | `s 275(1)(a) the offer is not accompanied by an advertisement` |  |  |
| s 275(1)(b) | 44160-44186 | encoded | `s 275(1)(b) no selling or promotional expenses are paid or incurred other than t...` |  |  |
| s 275(1)(c) | 44188-44204 | encoded | `s 275(1)(c) no prospectus is registered, or the registered prospectus has expire...` |  |  |
| s 275(1A) | 44210-44215 | fork | `s 275(1A) the offer is exempt from Subdivisions (1A), (2) and (3) of this Divisi...` | s275-1A |  |
| s 275(1A)(a) | 44220-44226 | encoded | `s 275(1A)(a) the offer is on terms that the securities or contracts may only be ...` |  |  |
| s 275(1A)(b) | 44228-44229 | encoded | `s 275(1A)(b) the offer is not accompanied by an advertisement` |  |  |
| s 275(1A)(c) | 44231-44254 | encoded | `s 275(1A)(c) no selling or promotional expenses are paid or incurred other than ...` |  |  |
| s 275(1A)(d) | 44256-44275 | encoded | `s 275(1A)(d) no prospectus is registered, or the registered prospectus has expir...` |  |  |
| s 275(2) advertisement | 44281-44311 | encoded | `s 275(2) the communication is an advertisement` |  |  |
| s 275(2) information memorandum | 44316-44336 | encoded | `s 275(2) the document is an information memorandum` |  |  |
| s 275(2) relevant person | 44338-44358 | encoded | `s 275(2) the person is a relevant person` |  |  |
| s 275(2A) | 44365-44375 | fork | `s 275(2A) the matter is included in the affairs of the person making the offer, ...` | s275-2A |  |
| s 275(3) | 44379-44388 | encoded | `s 275(3) the person is treated as an exempt person` |  |  |
| s 275(4) | 44392-44393 | encoded | `s 275(4) the amount that applies in place of $200,000` |  |  |
| (Offer of securities acquired pursuant to section 274 or 275) | 44395-44395 | inert 1 (a heading) | - | - | |
| s 276(1) | 44397-44416 | fork | `s 276(1) Subdivisions (1A), (2) and (3) of this Division apply to the offer resu...` | s276-1 | yes |
| s 276(1A) | 44424-44437 | encoded | `s 276(1A) the sale of the converted securities is a sale for subsection (1)` |  |  |
| s 276(2) | 44441-44453 | encoded | `s 276(2) Subdivisions (1A), (2) and (3) of this Division do not apply to the off...` |  |  |
| s 276(3) | 44459-44485 | fork | `s 276(3) the transfer of the securities or contracts of the investment-holding c...` | s276-3 |  |
| s 276(4) | 44486-44518 | fork | `s 276(4) the transfer of the beneficiaries' rights and interest in the trust is ...` | s276-4 |  |
| s 276(5) | 44522-44524 | encoded | `s 276(5) the person is a beneficiary for subsection (4)` |  |  |
| s 276(6) | 44526-44531 | fork | `s 276(6) an offer to sell may be made in reliance on section 273(1)(d), (da), (e...` | s276-6 |  |
| s 276(7) | 44537-44584 | fork | `s 276(7) subsections (1), (3) and (4) do not apply to the securities or contract...` | s276-7 |  |
| (Offer made using offer information statement) | 44588-44588 | inert 1 (a heading) | - | - | |
| s 277(1) | 44590-44596 | fork | `s 277(1) the offer is exempt from Subdivisions (2) and (3) of this Division (oth...` | s277-1, s277-1-257 | yes |
| s 277(1)(a) | 44598-44598 | fork | `s 277(1)(a) the securities or contracts are of a kind the paragraph names` | s277-1a |  |
| s 277(1)(a)(i) | 44598-44605 | encoded | `s 277(1)(a)(i) the securities or contracts are units or derivatives of units in ...` |  |  |
| s 277(1)(a)(ia) | 44609-44617 | encoded | `s 277(1)(a)(ia) the securities are SDRs of a listed business trust` |  |  |
| s 277(1)(a)(ii) | 44621-44624 | encoded | `s 277(1)(a)(ii) the securities or contracts are issued by a corporation whose sh...` |  |  |
| s 277(1)(a)(iii) | 44630-44634 | encoded | `s 277(1)(a)(iii) the securities are SDRs of a listed corporation` |  |  |
| s 277(1)(aa) | 44638-44641 | fork | `s 277(1)(aa) the issuer of the units is the issuer of the shares or debentures` | s277-1aa |  |
| s 277(1)(ab) | 44645-44647 | fork | `s 277(1)(ab) the issuer of the derivatives is the issuer of the units in the bus...` | s277-1ab |  |
| s 277(1)(b) | 44651-44654 | encoded | `s 277(1)(b) an offer information statement complying with the prescribed require...` |  |  |
| s 277(1)(c) | 44656-44661 | encoded | `s 277(1)(c) the offer is made in or accompanied by the statement, or all the con...` |  |  |
| s 277(1AA) | 44667-44675 | fork | `s 277(1AA) the units in the business trust or the shares of the corporation are ...` | s277-1AA |  |
| s 277(1A) | 44679-44682 | fork | `s 277(1A) the offer is made within the period of 6 months from the date the offe...` | s277-1A | yes |
| s 277(1AB) | 44686-44703 | fork | `s 277(1AB) the Authority may declare that the provision of an offer information ...` | s277-1AB |  |
| s 277(1AC) | 44707-44711 | fork | `s 277(1AC) the offer is exempt from Subdivisions (2) and (3) of this Division (o...` | s277-1AC |  |
| s 277(1AC)(a) | 44713-44727 | encoded | `s 277(1AC)(a) the offer information statement meets the three requirements of pa...` |  |  |
| s 277(1AC)(b) | 44729-44735 | encoded | `s 277(1AC)(b) the offer is made in or accompanied by the statement, or all the c...` |  |  |
| s 277(1AD) | 44739-44742 | fork | `s 277(1AD) the Authority may provide that the offer may only be made subject to ...` | s277-1AD |  |
| s 277(1B) | 44746-44769 | fork | `s 277(1B) all the conditions are satisfied` | s277-1B |  |
| s 277(2) | 44776-44779 | fork | `s 277(2) the Authority may modify the prescribed form and content of the offer i...` | s277-2 |  |
| s 277(3) | 44781-44783 | encoded | `s 277(3) sections 249, 249A, 253, 254 and 255 apply to the offer information sta...` |  |  |
| s 277(4)(a) | 44787-44791 | encoded | `s 277(4)(a) the reference to the registration of the prospectus is to be read as...` |  |  |
| s 277(4)(b) | 44793-44796 | encoded | `s 277(4)(b) the reference to information required in a prospectus is to be read ...` |  |  |
| s 277(4)(c) | 44798-44802 | encoded | `s 277(4)(c) the reference to the person making the offer is to be read as a refe...` |  |  |
| s 277(5) | 44806-44809 | fork | `s 277(5) the written consent of the expert is lodged with the Authority at the s...` | s277-5 | yes |
| s 277(6) | 44811-44815 | fork | `s 277(6) the written consent of the issue manager or underwriter is lodged with ...` | s277-6 |  |
| s 277(7) | 44817-44828 | encoded | `s 277(7) the person must not advertise or publish what the subsection bars`; `s 277(7) the bar on advertising or publishing` |  | yes |
| s 277(8) | 44834-44841 | fork | `s 277(8) the person is guilty of an offence`; `s 277(8) the penalty for the offence` | s277-8 | yes |
| (Offer in respect of international debentures) | 44845-44845 | inert 1 (a heading) | - | - | |
| s 278(1) | 44847-44850 | fork | `s 278(1) the offer is exempt from Subdivisions (2) and (3) of this Division (oth...` | s278-1 | yes |
| s 278(1)(a) | 44852-44861 | fork | `s 278(1)(a) the offer is made by a licensee or an exempt person to the investors...` | s278-1a |  |
| s 278(1)(b) | 44863-44863 | encoded | `s 278(1)(b) the offer complies with the conditions specified in subsection (2)` |  |  |
| s 278(2) | 44867-44867 | encoded | `s 278(2) the offer complies with the conditions specified in this subsection` |  |  |
| s 278(2)(a) | 44867-44876 | fork | `s 278(2)(a) the debentures are denominated in a foreign currency and each has a ...` | s278-2a |  |
| s 278(2)(b) | 44878-44881 | encoded | `s 278(2)(b) the shares of the issuing corporation, or of a guarantor, are listed...` |  |  |
| s 278(3) | 44883-44884 | fork | `s 278(3) the Authority may add to, vary or amend the conditions specified in sub...` | s278-3 |  |
| (Offer of debentures made by Government or international fina) | 44886-44887 | inert 1 (a heading) | - | - | |
| s 279 | 44889-44897 | fork | `s 279 the offer is exempt from Subdivisions (2) and (3) of this Division` | s279 | yes |
| (Making offer using automated teller machine or electronic me) | 44899-44900 | inert 1 (a heading) | - | - | |
| s 280(1) | 44902-44915 | fork | `s 280(1) the offer is an offer referred to in section 280`; `s 280(1) the person making the offer is exempted from the requirement of a prosp...` | s280-1 | yes |
| s 280(2) | 44919-44927 | fork | `s 280(2) a prospectus or profile statement complying with the other requirements...` | s280-2 |  |
| s 280(3) | 44929-44943 | encoded | `s 280(3) the machine or the electronic means gives the indications that subsecti...` |  |  |
| (Information relating to certain offers) | 44947-44947 | inert 1 (a heading) | - | - | |
| s 280A | 44949-44953 | fork | `s 280A the Authority may require a person or class of persons to provide informa...` | s280A |  |
| (Revocation of exemption) | 44957-44957 | inert 1 (a heading) | - | - | |
| s 281(1) | 44959-44964 | fork | `s 281(1) the Authority may revoke an exemption under this Subdivision` | s281-1 |  |
| s 281(2) | 44966-44975 | fork | `s 281(2) the Authority may revoke the exemption without giving the person affect...`; `s 281(2) the person may apply to the Authority for the revocation to be reviewed`; `s 281(2) the revocation remains in effect` | s281-2, s281-2e | yes |
| s 281(3) | 44977-44978 | encoded | `s 281(3) the revocation is final and no appeal lies from it` |  |  |
| (Transactions under exempted offers subject to Division 2 of ) | 44980-44981 | inert 1 (a heading) | - | - | |
| s 282 | 44983-44988 | fork | `s 282 nothing in this Part limits or diminishes the liability` | s282 | yes |
| (Subdivision (5) — General Power of Authority to issue direct) | 44990-44992 | inert 1 (a heading) | - | - | |
| s 282AA(1) | 44994-44997 | fork | `s 282AA(1) the Authority may issue the direction` | s282AA-1 |  |
| s 282AA(1)(a) | 44999-45002 | encoded | `s 282AA(1)(a) the direction is to a person making an offer of securities, on mat...` |  |  |
| s 282AA(1)(b) | 45004-45007 | encoded | `s 282AA(1)(b) the direction is to a borrowing entity, on matters in connection w...` |  |  |
| s 282AA(1)(c) | 45009-45009 | encoded | `s 282AA(1)(c) the direction is to a trustee appointed under section 265A(1)` |  |  |
| s 282AA(2) | 45013-45014 | fork | `s 282AA(2) the person given the notice must comply with every direction containe...`; `s 282AA(2) the duty to comply with every direction contained in the notice` | s282AA-2 | yes |
| s 282AA(3) | 45021-45022 | encoded | `s 282AA(3) the direction need not be published in the Gazette` |  |  |
| s 282AA(4) | 45026-45031 | fork | `s 282AA(4) the person is guilty of an offence`; `s 282AA(4) the penalty for the offence` | s282AA-4 | yes |
| s 282AA(5) | 45035-45040 | fork | `s 282AA(5) the person incurs no criminal or civil liability for the thing done o...` | s282AA-5 | yes |

## Fork register (sfad)

Every ambiguity or choice the encoding took, one entry per fork line in the modules, in module order (the same text stands as a `-- FORK` comment under the function it concerns).
Each entry gives the reading taken, the other reading, and the text or ruling that licenses the choice.
A tag such as `[the "In short" sentence ...]` is the Guide's ruling, quoted from `inputs/ENCODING-GUIDE.md` with its line number.
"No ruling covers it: assumed, not ruled" marks a choice the Guide does not reach.
There are 120 entries.

### Subdivision (3): debentures, ss 261 to 271 (sfad-debentures.l4)

- **s261-1** (s 261(1); `s 261(1) this Subdivision applies to the offer`)
  took JUST FALSE where the "where" gate fails.
  other reading NOTHING (a scope limit with no "only").
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"]; the other reading is [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"].
- **s261-1A** (s 261(1A); `s 261(1A) sections 268, 269 and 270 do not apply to the borrowing entity`)
  took JUST FALSE where the "if" gate (prescribed entity) fails.
  other reading NOTHING ("if A then B" does not itself say "if not A then not B").
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] (a condition introduced with "if") and the rule of 2026-10-29 (a).
- **s261-1Ca** (s 261(1C)(a); `s 261(1C)(a) the Authority may impose a condition or restriction on the entity`)
  took NOTHING where the entity is not (known to be) a prescribed entity.
  other reading JUST FALSE (the Authority may not).
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"]: a function named for a power whose gate failed.
- **s261-1Cb** (s 261(1C)(b); `s 261(1C)(b) the Authority may vary or revoke the condition or restriction`)
  took NOTHING where no condition has been imposed.
  other reading JUST FALSE.
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s261-1C** (s 261(1C); `s 261(1C) the prescribed entity must comply with the condition or restriction`)
  took JUST FALSE where the condition was never imposed or has been revoked (a duty whose own gate is unmet).
  other reading NOTHING (the class of conditions is limited by its own wording).
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] (a duty) and [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a duty whose "if" or "where" is unmet).
- **s261-1D** (s 261(1D); `s 261(1D) the person is guilty of an offence`)
  took JUST FALSE where the contravention element is unmet (this provision's own question: no contravention, no offence under it).
  other reading NOTHING (the text does not say a person who has not contravened is not guilty of any offence).
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] ("the provision's own question") and the brief's split site (i).
- **s261-3** (s 261(3); `s 261(3) the corporation is related to the other corporation for this Subdivision`)
  took JUST FALSE where the "if" gate fails.
  other reading NOTHING (an "if" definition does not say "only if").
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("if") and the rule of 2026-10-29 (a).
- **s262-2** (s 262(2); `s 262(2) the person is exempt from section 262`)
  took NOTHING where no exemption has been granted or a condition is unmet (a grant by the Authority).
  other reading JUST FALSE.
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s265-1** (s 265(1); `s 265(1) the court may order the security for the debentures to be enforceable`)
  took NOTHING where a condition of the "if ... the court is satisfied" gate is unmet.
  other reading JUST FALSE (the court may not).
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"]; "not more than 60%" is read as AT MOST 60% of the principal sum.
- **s265A-1** (s 265A(1); `s 265A(1) the borrowing entity must appoint a trustee for the holders of debentures for the entire tenure`)
  took JUST FALSE where the "where" gate fails.
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] and [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] (a duty); no deadline is stated, so the rule has no breach path.
- **s265A-2** (s 265A(2); `s 265A(2) the borrowing entity has ensured that the appointed trustee meets the requirements`)
  took JUST FALSE where the appointed trustee is none of the listed persons, or is not independent, or misses a prescribed requirement (the duty's own question).
  other reading NOTHING (the list ends with a prescribed catch-all, so it is not closed by "only").
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] (a duty or the provision's own question).
- **s265A-4** (s 265A(4); `s 265A(4) the person is guilty of an offence`)
  took JUST FALSE where none of the three contraventions is shown (this provision's own question).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s266-2** (s 266(2); `s 266(2) the trustee may apply to the Authority for an order`)
  took JUST FALSE where the "where" gate fails.
  other reading NOTHING (a grant limited by its own wording).
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] (a "where ..." condition: when it fails the answer is JUST FALSE) against [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] (a grant limited in its own wording); [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] says list it and do not change it.
- **s266-3a** (s 266(3)(a); `s 266(3)(a) the Authority may impose restrictions on the activities of the borrowing entity`)
  took NOTHING where the application, the opportunity to make representations or the written order is missing.
  other reading JUST FALSE.
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s266-3b** (s 266(3)(b); `s 266(3)(b) the trustee must apply to the court as directed`)
  took JUST FALSE where there is no direction (a duty whose gate "accordingly" is unmet).
  other reading NOTHING.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a duty whose "if" or "where" is unmet) and [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] (a duty).
- **s266-4a** (s 266(4); `s 266(4) the trustee may apply to the court for an order under subsection (5)`)
  took JUST FALSE where neither (a) nor (b) holds.
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] against [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"]; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"]. Paragraph (b) speaks of an order "under subsection (2)"; subsection (2) itself says the trustee may apply "for an order under this subsection", while subsection (3) is where the Authority "by written order" imposes restrictions; the input is worded as the text words it (an order of the Authority on the application), and the numbering is recorded as finding F-266.
- **s266-4b** (s 266(4); `s 266(4) the trustee must apply to the court for an order under subsection (5)`)
  took JUST FALSE where there is no request (a duty whose "where" gate is unmet).
  other reading NOTHING.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] and [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"].
- **s266-5** (s 266(5); `s 266(5) the court may make the order`)
  took JUST FALSE where there is no application ("where" gate) and NOTHING where the opportunity to be heard or the listed kind is missing.
  other reading NOTHING for the first and JUST FALSE for the second.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] against [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] for the first; [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"] for the second; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"].
- **s266-8** (s 266(8); `s 266(8) the trustee may rely on the certificate, report or statement`)
  took NOTHING where the "if" gate fails.
  other reading JUST FALSE.
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s267-1** (s 267(1); `s 267(1) the trustee for the holders of debentures may apply to the court`)
  took NOTHING where the application is for neither purpose.
  other reading JUST FALSE (a list closed by "or").
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s267-2b** (s 267(2)(b); `s 267(2)(b) the court may accede to the application on terms or make another order`)
  took NOTHING where the court is not satisfied.
  other reading JUST FALSE.
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s267A-1** (s 267A; `s 267A the person may apply to the court for an order compelling the trustee to perform the trustee's duties`)
  took NOTHING for anyone else (the text opens with "Without affecting any other right").
  other reading JUST FALSE.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] (a list not closed) and [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s268-4** (s 268(4); `s 268(4) the entity must provide the trustee with particulars of the charge`)
  took JUST FALSE where there is no trustee or the entity is neither the borrowing entity nor a guarantor (a duty whose "where" gate fails).
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] and [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] (a duty).
- **s268-4a** (s 268(4)(a); `s 268(4)(a) the particulars of the charge are provided in time`)
  took JUST FALSE outside the 21 days or not in writing (a period fixed in the text's own words).
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"]. The keel's convention P2 reads "within N days after" as a window that opens the day after the event; for a duty this encoding counts an act on or before the last day as in time ("not later than the end of"), so an early act is not late.
- **s268-7** (s 268(7); `s 268(7) the person is guilty of an offence`)
  took JUST FALSE where the person does not fail to comply (this provision's own question).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s268-7A** (s 268(7A); `s 268(7A) the person is guilty of an offence`)
  took JUST FALSE where the person does not contravene subsection (6A).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s268-9** (s 268(9); `s 268(9) the trustee must lodge notice of that fact with the Authority`)
  took JUST FALSE where the "where" gate fails.
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] and [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"]. "Immediately" has no stated measure, so the rule has no breach path.
- **s268-10b** (s 268(10)(b); `s 268(10)(b) the annual accounts need not be audited, or the audit may be limited`)
  took NOTHING where there is no written consent (a relief limited by an "if", and what then applies is the Companies Act 1967).
  other reading JUST FALSE (the audit is then required).
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"] (a relief is read like a grant) against [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("if").
- **s268-11** (s 268(11); `s 268(11) the directors or equivalent persons must lodge a copy of the notice with the Authority`)
  took JUST FALSE where there is no consent (a duty whose "where" gate fails).
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] and [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line].
- **s268-11t** (s 268(11); `s 268(11) the copy of the notice is lodged at the time the accounts are lodged`)
  took "at the time when" to mean the same day (the clock here counts days).
  other reading a same-moment test finer than a day.
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"].
- **s268-12** (s 268(12); `s 268(12) the accounts may be based on the directors' estimate of the stock in trade`)
  took JUST FALSE once the "unless" is met (the trustee requires otherwise in writing).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] ("may ... unless": the text closes the gate itself) and [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (an "unless" once it is met).
- **s268A-1** (s 268A(1); `s 268A(1) the borrowing entity must prepare and make available a semi-annual report`)
  took JUST FALSE where the debentures are listed or the tenure is under 12 months (the "if" gate of a duty).
  other reading NOTHING.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("if") and [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"]. The form and content of the report are "such other requirements as the Authority may prescribe", outside the sources.
- **s268A-3** (s 268A(3); `s 268A(3) the trustee must lodge notice of that fact with the Authority`)
  took JUST FALSE where the "where" gate fails.
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] and [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"]. "Immediately" has no stated measure, so the rule has no breach path.
- **s268A-4** (s 268A(4); `s 268A(4) the borrowing entity must disclose the information to the holders of unlisted debentures`)
  took NOTHING for information that affects neither (a scope limit with no "only").
  other reading JUST FALSE.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"].
- **s268A-5** (s 268A(5); `s 268A(5) the person is guilty of an offence`)
  took JUST FALSE where none of the contraventions is shown.
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s268A-6** (s 268A(6); `s 268A(6) the borrowing entity must make bid or redemption prices available and meet paragraphs (a) to (c)`)
  took JUST FALSE where the "where" gate fails.
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] and [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"].
- **s268A-8** (s 268A(8); `s 268A(8) the person is guilty of an offence`)
  took JUST FALSE where neither contravention is shown.
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s268A-10** (s 268A(10); `s 268A(10) the person is guilty of an offence`)
  took JUST FALSE where the person does not contravene subsection (9).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s269-1** (s 269(1); `s 269(1) the borrowing entity may require the guarantor entity to provide the information`)
  took NOTHING where a limb of the power is missing.
  other reading JUST FALSE.
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s269-2** (s 269(2); `s 269(2) the guarantor entity must provide the borrowing entity with the information`)
  took JUST FALSE where no notice under subsection (1) has been given (the duty is of "the information required under subsection (1)").
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] (a duty) and [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line].
- **s269-2t** (s 269(2); `s 269(2) the information is provided before the date specified in the notice`)
  took "before such date" to exclude the specified date itself, so the last day to provide is the day before it.
  other reading the specified date is itself in time.
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"].
- **s269-3** (s 269(3); `s 269(3) the person is guilty of an offence`)
  took JUST FALSE where the entity has not failed, or the person is neither the entity nor an officer in default.
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s270-1** (s 270(1); `s 270(1) the borrowing entity must make reports to the trustee on the progress of the purpose or project`)
  took JUST FALSE where a "where" gate fails.
  other reading NOTHING.
  licence [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] and [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"]. "From time to time" states no period, so the rule has no breach path.
- **s270-3** (s 270(3); `s 270(3) the trustee may give written notice requiring the borrowing entity to repay the moneys`)
  took JUST FALSE where the "when" gate fails.
  other reading NOTHING (a grant limited by its own wording).
  licence [the delegated-definitions ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 94): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling"] ("when" counts as "where" under rule (b) of the periods ruling) against [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"]; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"].
- **s270-4** (s 270(4); `s 270(4) the trustee must not give notice under subsection (3)`)
  took JUST FALSE where the trustee is satisfied of none of (a) to (c) (a bar whose "if" gate is unmet: the bar does not apply).
  other reading NOTHING (a prohibition limited by its own wording, case outside the limit).
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] (a bar) against [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"].
- **s270-5a** (s 270(5); `s 270(5) the borrowing entity is liable to repay the moneys`)
  took JUST FALSE once the "unless" is met (paragraph (a), or paragraph (b) with no demand in time).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] ("unless") and [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (an "unless" once it is met).
- **s270-5b** (s 270(5); the same function, "Upon receipt ... of a notice")
  took JUST FALSE where there is no notice or no moneys owing ("upon" counts as "where").
  other reading NOTHING.
  licence [the delegated-definitions ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 94): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling"] against [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"]; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] does not apply because the function is named for a liability, not a power.
- **s271-1** (s 271(1); `s 271(1) the provision is void`)
  took NOTHING where the provision is outside the limit "insofar as ... where the trustee fails to show the degree of care" and no carve-out applies.
  other reading JUST FALSE.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("limits a grant or prohibition in its own wording ... and the case falls outside the limit"). The carve-outs of (2) and (3) are flat negatives ("does not invalidate"), so they give JUST FALSE.
- **s268-9i** (s 268(9); `s 268(9) the duty of the trustee to lodge notice with the Authority`)
  took "immediately" as a promptness standard with no number of days or hours the clock can count, so the rule has no WITHIN and no breach path.
  other reading WITHIN 0 (the same day), under which a trace one day late reaches BREACH.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a bare "must" not done, decided on the text's own words).
- **s268A-3i** (s 268A(3); `s 268A(3) the duty of the trustee to lodge notice with the Authority`)
  took "immediately" as a promptness standard with no number of days or hours the clock can count, so the rule has no WITHIN and no breach path.
  other reading WITHIN 0 (the same day), under which a trace one day late reaches BREACH.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a bare "must" not done, decided on the text's own words).
- **s268A-4i** (s 268A(4); `s 268A(4) the duty to disclose information materially affecting the unlisted debentures`)
  took "immediately" as a promptness standard with no number of days or hours the clock can count, so the rule has no WITHIN and no breach path.
  other reading WITHIN 0 (the same day), under which a trace one day late reaches BREACH.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a bare "must" not done, decided on the text's own words).
- **s270-5i** (s 270(5); `s 270(5) the duty of the borrowing entity to repay the moneys on demand`)
  took "on demand in writing ... must immediately repay" as a promptness standard with no number of days or hours the clock can count, so the rule has no WITHIN and no breach path.
  other reading WITHIN 0 (the same day), under which a trace one day late reaches BREACH.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a bare "must" not done, decided on the text's own words).

### ss 272, 272A and 272B: no consideration, small offers, private placement (sfad-nocons-small-private.l4)

- **s272-1** (s 272(1); `s 272(1) the offer is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)`)
  took JUST FALSE where consideration is or will be given (a condition introduced with "if") and NOTHING where the offer is not an offer of shares, debentures or business-trust units (the section speaks only of those).
  other reading NOTHING for the first (an "if" condition does not itself say "if not then not") and JUST FALSE for the second.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] for the first and [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] for the second; the first is also under "Marginal readings for a lawyer".
- **s272-2** (s 272(2); `s 272(2) the offer of securities-based derivatives contracts is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)`)
  took JUST FALSE where either paragraph (a) or paragraph (b) is not met (both are conditions of an "if" joined by "and") and NOTHING where the offer is not of the kind named.
  other reading NOTHING for the first.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] and [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"]; under "Marginal readings for a lawyer".
- **s272A-10** (s 272A(10); `s 272A(10) the communication is an advertisement`)
  took the definition as closed ("means"), so a communication outside paragraphs (a) to (c) is JUST FALSE, and one inside an exclusion (d), (e) or (f) is JUST FALSE.
  other reading none: "means" closes the term (the delegated-definitions ruling distinguishes a bare list; this is a definition that says "means").
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("a means definition"). Paragraph (d) is read as both of its sub-paragraphs (i) and (ii) joined by "and", given as one input.
- **s272A-11** (s 272A(11); `s 272A(11) the matter is included in the affairs of the person making the offer, the issuer, the underlying entity or the business trust`)
  took "includes" as an extension, so a matter that is neither within section 2(2) nor prescribed answers NOTHING, never JUST FALSE.
  other reading JUST FALSE.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("says includes" answers NOTHING).
- **s272A-1d** (s 272A(1)(d); `s 272A(1)(d) the selling or promotional expenses are ones the exemption allows`)
  took the expenses one by one: every expense must be an administrative or professional one, or a commission or fee for services rendered by a person named in (i), (ii) or (iii).
  other reading the persons named qualify all expenses of a total, not each.
  licence the text's own "no ... expenses ... other than those".
- **s272A-3b** (s 272A(3)(b); `s 272A(3)(b) the offer is made to a person who is likely to be interested in that offer`)
  took the likelihood as a judgment the person states, answered JUST TRUE only when it rests on at least one of the three matters (i), (ii), (iii), and NOTHING when the person is likely to be interested but none of the three is shown.
  other reading JUST TRUE on the judgment alone, or JUST FALSE when none of the three holds.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("having regard to" is not "only"); under "Marginal readings for a lawyer".
- **s272A-2** (s 272A(2); `s 272A(2) the statement and notification are treated as given`)
  took NOTHING where the deeming condition is not met (the deeming is an aid; the person may still have given the statement and notification by other means, which paragraph (1)(b) asks as its own facts).
  other reading JUST FALSE ("if" condition).
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] against [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"]: the provision grants a deeming, so a failed gate is not read as a bar.
- **s272A-1a** (s 272A(1)(a); `s 272A(1)(a) the total amount raised within the period of 12 months does not exceed the limit`)
  took "within any period of 12 months" as a window the caller names: the function answers for one window, and the exemption holds only if it holds for every window (the caller asks once for each window).
  other reading a single trailing window ending on the offer date.
  licence the text's own "any period of 12 months". The "$5 million (or its equivalent in a foreign currency)" is read as the same limit in whichever currency the total is stated: the caller states the total in one currency.
- **s272A-1bii** (s 272A(1)(b)(ii); `s 272A(1)(b)(ii) the notification in writing is given as the paragraph requires`)
  took the notification as one that names all three ways (A), (B) and (C) of a lawful later sale, as the text words it.
  other reading a notification that names fewer of them still states the restriction.
  licence the text's own wording of the notification (the sub-paragraphs are joined by "or" inside the notification, so each names a case the notification must tell the buyer of).
- **s272A-1** (s 272A(1); `s 272A(1) the offer is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)`)
  took NOTHING where the offer is not a personal offer (a scope limit with no "only"), JUST FALSE where a paragraph (a) to (e) fails (conditions of an "if"), JUST TRUE only when all hold.
  other reading NOTHING for a failed paragraph ("if A then B" does not say "if not A then not B") and JUST FALSE for a non-personal offer.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] for the first, [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] for the second; the second is under "Marginal readings for a lawyer". Section 257 and the Subdivisions (1A), (2) and (3) are another part's; this function answers only "is the offer exempt from them".
- **s272A-5** (s 272A(5); `s 272A(5) the amounts raised by earlier offers that must be included`)
  took the two limbs (a) and (b) as alternatives joined by "or", each counted only "within that period in reliance on the exemption under subsection (1) or section 302B(1)", and the period as 12 months beginning on the first day asked about.
  other reading an earlier offer counts whether or not it relied on the exemption.
  licence the text's own "if any, within that period in reliance on the exemption". The function adds amounts; it never answers JUST FALSE.
- **s272A-8b** (s 272A(8)(b); `s 272A(8)(b) the subsequent offer is made in reliance on subsection (1) and at least 6 months have elapsed`)
  took "at least 6 months have elapsed from the date acquired" as: the offer is made after the last day of the period of 6 months that follows the day of acquisition (convention P1 of the keel: the day of the event is not counted, so 6 months from 1 January end on 1 July and the first day after is 2 July).
  other reading the offer is in time on the corresponding date itself (1 July).
  licence the keel's P1 and P10; "elapsed" is read as the whole period having run.
- **s272A-8** (s 272A(8); `s 272A(8) Subdivisions (2) and (3) of this Division apply to the offer that resulted in the sale`)
  took JUST FALSE once an "unless" exception (a), (b) or (c) is met, JUST TRUE when the three exceptions are all unmet, and NOTHING where the securities were not acquired under subsection (1) or were not sold on.
  other reading NOTHING once an exception is met (the question the text leaves is whether the sale needs a prospectus, which the other Subdivisions answer).
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (an "unless" once it is met) and [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] for the scope; under "Marginal readings for a lawyer".
- **s272B-5** (s 272B(5); `s 272B(5) the number of persons the offer to the offeree counts as`)
  took each paragraph as a case the caller names; (a), (c), (d) and (f) count as one person (the single person, the joint owners as a single person, the other person on whose behalf, only the second-mentioned person), (b) counts the equity owners, partners, members or beneficiaries, and (g) counts both persons.
  other reading for (d): the person acting on behalf is itself counted too.
  licence the text's own words: "treated as an offer to a single person", "treated as an offer made to that other person", "only the second‑mentioned person is counted", "both persons are counted".
- **s272B-3** (s 272B(3); `s 272B(3) the number of persons to whom earlier offers were made that must be included`)
  took (a) as an earlier offer by the first person of securities issued by the same entity in reliance on section 272B, and (b) as a closely related offer by that person or another in reliance on section 272B or section 302C, each within the period of 12 months beginning on the first day asked about.
  other reading none the text supports; the period is the caller's window, as in section 272A(1)(a).
  licence the text's own words. The function adds numbers; it never answers JUST FALSE.
- **s272B-1** (s 272B(1); `s 272B(1) the offers are exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)`)
  took JUST FALSE where a paragraph (a) to (d) fails (conditions of an "if").
  other reading NOTHING ("if A then B" does not say "if not A then not B").
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"]; under "Marginal readings for a lawyer".

### s 273: offers made under certain circumstances (sfad-circumstances.l4)

- **s273-1AA** (s 273(1)(cd) and (cda); `s 273(1AA) the securities of the entity are treated as listed for quotation on the approved exchange`)
  took NOTHING where neither the securities nor the SDRs are listed (a deeming that extends "listed"; it does not say the securities are not listed otherwise).
  other reading JUST FALSE.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("includes" and an extension answer NOTHING); the listing question itself is asked as the first input, so a caller who says the securities are not listed and the SDRs are not either gets NOTHING here and JUST FALSE from the paragraph.
- **s273-1cd** (s 273(1)(cd); `s 273(1)(cd) the offer is an offer of securities of an unlisted entity, or a non-primary listing, to existing members, debenture holders or SDR holders`)
  took "formed or constituted in Singapore or otherwise" in sub-paragraph (i) as any entity, wherever formed, whose securities are not listed, and sub-paragraph (ii) as an entity not formed in Singapore whose securities are listed on a non-primary listing.
  other reading (i) limited to entities formed in Singapore or elsewhere by some other test.
  licence the text's own words; "whether or not the offer is renounceable" is not a condition and adds no input.
- **s273-1A** (s 273(1A); `s 273(1A) the offer is excluded from paragraphs (d), (da), (e), (ea) and (h) of subsection (1)`)
  took JUST FALSE where a limb (a), (b) or (c) is unmet: the exclusion's "if" is not met, which says nothing about whether the offer comes within the paragraph (that is the paragraph's own function).
  other reading NOTHING.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("if") and [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line]; under "Marginal readings for a lawyer". Limb (c) is read as applying only to an offer of securities-based derivatives contracts ("in the case of").
- **s273-1B** (s 273(1B); `s 273(1B) Subdivision (1A) of this Division does not apply to the offer`)
  took NOTHING where the offer is not of a kind described (the flat negative "does not apply" is limited to those kinds, so outside them the text is silent).
  other reading JUST FALSE.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] (a scope limit with no "only").
- **s273-5** (s 273(5); `s 273(5) the offer is within the period of 6 months from the date of the Authority's declaration`)
  took the 6 months as beginning with the day of the declaration (keel P10) and JUST FALSE outside the period (a period the text fixes in its own words), NOTHING where no declaration is shown.
  other reading the offer on the day of the declaration is outside the period.
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"] and [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"].
- **s273-6** (s 273(6); `s 273(6) the Authority may impose conditions or restrictions on the offer`)
  took JUST FALSE where the Authority is not making a declaration: "on making" is a gate of the "where", "when", "upon" kind, which the delegated-definitions ruling's item (c) counts as "where", and the periods ruling's item (b) answers JUST FALSE for a failed "where".
  other reading NOTHING (a function named for a power whose gate failed, limit 1 of the grant ruling).
  licence [the delegated-definitions ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 94): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling"] and [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"]; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] says to list a "may" function with such a gate and not to change it, and this is the split site (ii) of the brief.
- **s273-8** (s 273(8); `s 273(8) the person is guilty of an offence`)
  took JUST FALSE where the contravention element is unmet (this provision's own question).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s273-8B** (s 273(8B); `s 273(8B) the person is guilty of an offence`)
  took JUST FALSE where neither element is shown (this provision's own question).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s273-1** (s 273(1); `s 273(1) the offer is exempt from Subdivisions (2) and (3) of this Division (other than section 257)`)
  took JUST FALSE where every paragraph the caller lists is answered and none holds (the "if" list is the text's only route, apart from the Authority's declaration in subsection (5), which has its own function).
  other reading NOTHING ("if A then B" does not say "if not A then not B"); and an empty list answers JUST FALSE, as no paragraph holds.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"]; under "Marginal readings for a lawyer". "Subject to subsection (5)" is read as the Authority's declaration being another route, not a limit on this one.

### ss 274, 275 and 276: investors and resale (sfad-investor-exemptions.l4)

- **s274-1** (s 274; `s 274 the offer is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)`)
  took NOTHING where the offer is not made to an institutional investor (the section grants an exemption to offers made to them and has no "if" and no "only").
  other reading JUST FALSE.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] (a scope limit with no "only").
- **s275-2A** (s 275(2A); `s 275(2A) the matter is included in the affairs of the person making the offer, the issuer, the underlying entity, the trustee-manager or the business trust`)
  took "includes" as an extension: NOTHING for a matter that is neither within section 2(2) nor prescribed.
  other reading JUST FALSE.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("says includes" answers NOTHING).
- **s275-1** (s 275(1); `s 275(1) the offer is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)`)
  took NOTHING where the offer is not made to a relevant person (the "where" names the scope of the exemption, with no "only") and JUST FALSE where a paragraph (a), (b) or (c) fails (conditions of an "if").
  other reading JUST FALSE for a non-relevant person and NOTHING for a failed paragraph.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] for the first and [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] for the second; the second is under "Marginal readings for a lawyer".
- **s275-1A** (s 275(1A); `s 275(1A) the offer is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)`)
  took NOTHING where the person does not acquire as principal (the scope of the exemption, with no "only") and JUST FALSE where a paragraph (a) to (d) fails.
  other reading as for section 275(1).
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] and [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"]; under "Marginal readings for a lawyer".
- **s276-7** (s 276(7); `s 276(7) subsections (1), (3) and (4) do not apply to the securities or contracts acquired`)
  took NOTHING where the securities are not of the kinds (a) or (b) (the flat "do not apply" is limited to those cases).
  other reading JUST FALSE.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"]. The text's paragraphs (a) and (b) are alternatives for a corporation's securities and a business trust's units: the first two inputs ask which of them the securities are, and the other two inputs are the same for both.
- **s276-1** (s 276(1); `s 276(1) Subdivisions (1A), (2) and (3) of this Division apply to the offer resulting in the sale`)
  took JUST FALSE where the sale is outside the 6 months (a period the text fixes in its own words), where subsection (7) applies, or where the buyer is one of the three excepted persons ("other than"); took NOTHING where the securities were not acquired under section 274 or 275 or were not sold; took the 6 months as ending on the day 6 months after the day of acquisition (the keel's P1 and P4).
  other reading NOTHING outside the 6 months (the text does not say the Subdivisions do not apply then).
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"] and the delegated-definitions ruling's item (c) ("when" counts as "where"); under "Marginal readings for a lawyer". The opening "Despite sections 272A, 272B, 273(1)(d) ... 277, 278 and 279" is the reason the answer is JUST TRUE even when another exemption would otherwise cover the offer: the caller does not state those exemptions here.
- **s276-3** (s 276(3); `s 276(3) the transfer of the securities or contracts of the investment-holding corporation is barred`)
  took the bar as a decision function (JUST TRUE: the transfer is barred) because the text names no party who "must not" transfer; JUST FALSE once an "unless" exception (c), (d) or (e) is met or after the 6 months, NOTHING where the corporation is not of the kind described.
  other reading NOTHING once an exception is met.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (an "unless" once met) and [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"]; no regulative rule is written for it (no party is named): listed under "Rules with no breach path (sfad)".
- **s276-4** (s 276(4); `s 276(4) the transfer of the beneficiaries' rights and interest in the trust is barred`)
  took the bar as a decision function (no party is named), JUST FALSE once an "unless" exception holds or after the 6 months, NOTHING outside the trusts described.
  other reading NOTHING once an exception holds.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] and [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"]; the $200,000 of paragraph (c)(ii) is not subject to the Authority's order under section 275(4), which speaks only of subsection (1A)(a); the caller states whether the offer's terms met $200,000.
- **s276-6** (s 276(6); `s 276(6) an offer to sell may be made in reliance on section 273(1)(d), (da), (e) or (ea)`)
  took JUST FALSE before the 6 months have elapsed: the gate "after 6 months have elapsed" is a period the text fixes in its own words (the periods ruling's item (a)).
  other reading NOTHING (a grant limited by its own wording, the "In short" sentence and limit 1 of the grant ruling).
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"]; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] says to list a "may" function gated in this way and not to change it: this is the split site (ii) of the brief. The section is a "to avoid doubt" clarification.

### ss 277 to 282: offer information statement, international debentures, Government, machines, information, revocation, liability (sfad-ois-intl-gov-atm.l4)

- **s277-1AA** (s 277(1)(a); `s 277(1AA) the units in the business trust or the shares of the corporation are treated as being listed for quotation on an approved exchange`)
  took NOTHING where neither the units or shares nor the SDRs are listed (a deeming that extends "listed"; it does not say they are not listed otherwise).
  other reading JUST FALSE.
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("includes" and an extension answer NOTHING); the listing question itself is the first input, so a caller who says neither is listed gets NOTHING here and JUST FALSE from the paragraph.
- **s277-1a** (s 277(1)(a); `s 277(1)(a) the securities or contracts are of a kind the paragraph names`)
  took the four sub-paragraphs as alternatives (the rendering ends (i) and (ia) with a semicolon and a comma, (ii) with "; or" and (iii) with a semicolon, and no "and" joins them).
  other reading all four must hold (which no offer can satisfy, since (i) and (ii) exclude each other).
  licence the text's own words: "(ii) ... (other than those mentioned in sub-paragraph (i) and SDRs) ... ; or".
- **s277-1aa** (s 277(1)(aa); `s 277(1)(aa) the issuer of the units is the issuer of the shares or debentures`)
  took JUST TRUE where the securities are not units of shares or of debentures (a condition that begins "if the securities ... are units" has nothing to fail when its own antecedent is unmet).
  other reading NOTHING (the paragraph is silent about other securities).
  licence no ruling covers a conditional condition: assumed, not ruled.
- **s277-1ab** (s 277(1)(ab); `s 277(1)(ab) the issuer of the derivatives is the issuer of the units in the business trust`)
  took JUST TRUE where the securities are not derivatives of units in a business trust (a condition that begins "if" has nothing to fail when its own antecedent is unmet).
  other reading NOTHING (the paragraph is silent about other securities).
  licence no ruling covers a conditional condition: assumed, not ruled.
- **s277-1B** (s 277(1B)(b); `s 277(1B) all the conditions are satisfied`)
  took the second "(b)" in the rendering ("(b) before enabling the prospective subscriber or buyer to submit any application ...") as the end of paragraph (b), which the text's own sentence runs on to: the two indications of (b)(i) and (b)(ii) are given "before enabling" the application.
  other reading a separate fourth condition, which changes nothing for the answer (it is asked as its own input either way).
  licence the text's own words: "(ii) that the prospective subscriber or buyer should read the offer information statement before submitting an application, (b) before enabling the prospective subscriber or buyer to submit any application".
- **s277-1A** (s 277(1A); `s 277(1A) the offer is made within the period of 6 months from the date the offer information statement is lodged`)
  took the 6 months as beginning with the day of lodgment (keel P10, "beginning with") and JUST FALSE outside the period, because "only applies" closes the gate in the text's own words; NOTHING where no statement has been lodged (there is no date to count from).
  other reading the period starts the day after lodgment (keel P1, "from").
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"] (a period the text fixes in its own words) and [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("only").
- **s277-1** (s 277(1); `s 277(1) the offer is exempt from Subdivisions (2) and (3) of this Division (other than section 257)`)
  took NOTHING for securities or contracts the Authority has prescribed as outside the exemption (the content of the prescription is in regulations, outside the text; "not being such ... as may be prescribed" is a scope limit with no "only") and JUST FALSE where a condition fails or the six months of subsection (1A) have run.
  other reading JUST FALSE for the prescribed securities.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] for the prescribed securities, [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("if", "only") for the conditions.
- **s277-1-257** (s 277(1); `s 277(1) the offer is exempt from Subdivisions (2) and (3) of this Division (other than section 257)`)
  took "(other than section 257)" as not touched by this function: no rule about section 257, which is Subdivision (2)'s and another part's, is encoded here, so the answer says only that Subdivisions (2) and (3) do not apply, leaving section 257 for the caller to apply.
  other reading a flag for the caller that section 257 still applies.
  licence the case-by-case ruling ([the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line], "(other than X)" is one of the six questions decided site by site) and PLAN.md section 4.3 (sfad does not encode a rule about section 257).
- **s277-1AB** (s 277(1AB); `s 277(1AB) the Authority may declare that the provision of an offer information statement in lieu of a prospectus would not be prejudicial to investors`)
  took JUST FALSE where the subsidiary condition, the guarantee or the application is missing: the text opens "In relation to an offer of securities — (a) where ...; and (b) where ..." and then "on the application of the subsidiary or the listed entity", gates of the "where" and "on" kind, which the delegated-definitions ruling's item (c) counts as "where" and the periods ruling's item (b) answers JUST FALSE.
  other reading NOTHING (a function named for a power whose gate failed, limit 1 of the grant ruling).
  licence [the delegated-definitions ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 94): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling"] and [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"]; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] says to list a "may" function with such a gate and not to change it: this is a split site (ii) of the brief. "On the application" is not named by the Guide itself: read by analogy with "upon" and listed under the marginal readings.
- **s277-1AC** (s 277(1AC); `s 277(1AC) the offer is exempt from Subdivisions (2) and (3) of this Division (other than section 257) for 6 months from the declaration`)
  took the 6 months as beginning with the day of the declaration ("starting on the date of the declaration": keel P10), JUST FALSE outside the period (a period the text fixes in its own words) and where a condition fails ("if all of the following conditions are satisfied"), and NOTHING where no declaration has been made (the subsection speaks only of the case where the Authority makes one).
  other reading JUST FALSE where no declaration has been made (a "where" condition, the periods ruling's item (b)).
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"], [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] for the conditions, and [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] for the missing declaration. The "(other than section 257)" is left to the caller as at s 277(1) (fork s277-1-257).
- **s277-1AD** (s 277(1AD); `s 277(1AD) the Authority may provide that the offer may only be made subject to conditions or restrictions`)
  took JUST FALSE where the Authority is not making a declaration: "on making" is a gate of the "where", "when", "upon" kind, which the delegated-definitions ruling's item (c) counts as "where", and the periods ruling's item (b) answers JUST FALSE for a failed "where" (the same words and the same answer as section 273(6)).
  other reading NOTHING (a function named for a power whose gate failed, limit 1 of the grant ruling).
  licence [the delegated-definitions ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 94): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling"] and [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"]; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] says to list a "may" function with such a gate and not to change it: this is a split site (ii) of the brief.
- **s277-2** (s 277(2); `s 277(2) the Authority may modify the prescribed form and content of the offer information statement`)
  took JUST FALSE where no person interested has applied: "on the application of any person interested" is a gate of the "upon" kind (the delegated-definitions ruling's item (c) counts "upon" as "where").
  other reading NOTHING (a function named for a power whose gate failed, limit 1 of the grant ruling).
  licence [the delegated-definitions ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 94): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling"] and [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"]; [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] says to list such a "may" function and not to change it: this is a split site (ii) of the brief. "On the application" is not named by the Guide itself: read by analogy with "upon" and listed under the marginal readings. The conditions or restrictions "as the Authority may determine" are the Authority's, outside the text.
- **s277-5** (s 277(5); `s 277(5) the written consent of the expert is lodged with the Authority at the same time as the lodgment of the statement`)
  took "at the same time" as the same day (the text counts no unit finer than a day and this encoding takes dates) and NOTHING where no consent is required (the question is whether the duty was met; the "Where" gate, if unmet, leaves no duty to meet).
  other reading JUST FALSE where no consent is required, or the same instant rather than the same day.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a duty whose "where" is unmet, decided site by site) and the text's own words. No party is named (the text says only that the consent "must be lodged"), so there is no regulative rule here: the duty is listed under "Rules with no breach path".
- **s277-6** (s 277(6); `s 277(6) the written consent of the issue manager or underwriter is lodged with the Authority at the same time as the lodgment of the statement`)
  took the same readings as section 277(5): the same day, and NOTHING where no consent is required.
  other reading JUST FALSE where no consent is required, or the same instant rather than the same day.
  licence [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a duty whose "where" is unmet, decided site by site) and the text's own words. No party is named, so there is no regulative rule here: the duty is listed under "Rules with no breach path".
- **s277-8** (s 277(8); `s 277(8) the person is guilty of an offence`)
  took JUST FALSE where neither element is shown (this provision's own question).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s278-1a** (s 278(1)(a); `s 278(1)(a) the offer is made by a licensee or an exempt person to the investors the Authority has specified`)
  took "being persons or bodies that appear to the Authority to have sufficient expertise to understand any risk involved" as the Authority's reason for specifying the investors, not a second condition the caller must show (the specification by order in the Gazette is the fact asked).
  other reading a separate condition that the investors appear to the Authority to have sufficient expertise.
  licence the text's own words: "such institutional, professional or business investors as the Authority may, by order in the Gazette, specify, being persons or bodies that appear to the Authority".
- **s278-2a** (s 278(2)(a); `s 278(2)(a) the debentures are denominated in a foreign currency and each has a face value of at least US$5,000`)
  took "each debenture, or each unit of debenture, has a face value of at least US$5,000 or its equivalent" as a test on the lowest face value in the offer, in United States dollars or the equivalent (the conversion is the caller's).
  other reading a test on the face value of each debenture one by one, which gives the same answer.
  licence the text's own words. The figure US$5,000 is the text's own; the Authority may vary it by order under section 278(3), which is outside the text (a caller who knows of a varied figure applies it themselves).
- **s278-1** (s 278(1); `s 278(1) the offer is exempt from Subdivisions (2) and (3) of this Division (other than section 257)`)
  took NOTHING where the offer is not by a body incorporated outside Singapore or is not of debentures (a scope limit with no "only") and JUST FALSE where paragraph (a) or (b) fails (a "where" condition on the exemption, which is not a "may").
  other reading JUST FALSE for the scope too.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] for the scope, [the periods ruling of 2026-11-05, item (b) (`inputs/ENCODING-GUIDE.md` line 93): "a "where ..." condition: when it fails the answer is `JUST FALSE`"] for the "where" paragraphs. "(other than section 257)" is left to the caller as at section 277(1) (fork s277-1-257).
- **s278-3** (s 278(3); `s 278(3) the Authority may add to, vary or amend the conditions specified in subsection (2)`)
  took NOTHING where the Authority does not act by order in the Gazette (the text limits the power to that manner and does not say what the Authority may do otherwise).
  other reading JUST FALSE.
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"]; "by order in the Gazette" is a manner, not a gate of the "where", "when" or "upon" kind, so this is not a split site.
- **s279** (s 279; `s 279 the offer is exempt from Subdivisions (2) and (3) of this Division`)
  took NOTHING where the offer is not made or guaranteed by the Government or such an institution (a scope limit with no "only", and the list of persons is not closed with "only").
  other reading JUST FALSE.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"]. Unlike sections 277 and 278 this section does not say "(other than section 257)": it names Subdivisions (2) and (3) only, and the function says so.
- **s280-1** (s 280(1); `s 280(1) the person making the offer is exempted from the requirement of a prospectus or profile statement`)
  took JUST FALSE where the prescribed requirements are not complied with: "Subject to ... such requirements as the Authority may prescribe" is read as the text's own condition, a plain variant of "if".
  other reading NOTHING ("subject to" is not one of the words the "In short" sentence lists, and the requirements are outside the text).
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] ("plain variants" of "if"). The requirement exempted from, section 240(1)(a) and (4), is Subdivision (2)'s and another part's; the function does not call it (PLAN.md section 4.3).
- **s280-2** (s 280(2); `s 280(2) a prospectus or profile statement complying with the other requirements has been prepared and issued for the offer`)
  took the function as the compliance question (JUST TRUE where it has been prepared and issued, JUST FALSE where it has not) and NOTHING for an offer that is not one referred to in subsection (1).
  other reading the function answers "is a prospectus still required" (always JUST TRUE for such an offer).
  licence the text's own words ("must still be prepared and issued") and [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line]. No party is named and no time is given, so there is no regulative rule here: the duty is listed under "Rules with no breach path".
- **s280A** (s 280A; `s 280A the Authority may require a person or class of persons to provide information about an offer made in reliance on an exemption`)
  took NOTHING where the information is about another kind of offer or the Authority does not act by regulations (the text limits the power to that subject and that manner).
  other reading JUST FALSE.
  licence [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"]; neither limit is a gate of the "where", "when" or "upon" kind, so this is not a split site. Which persons and what information the regulations name is outside the text.
- **s281-1** (s 281(1); `s 281(1) the Authority may revoke an exemption under this Subdivision`)
  took JUST FALSE where the Authority has formed neither view: the gate "Where the Authority considers ..." fails, and the S1b ruling (Guide line 101, 2026S1bC) answers JUST FALSE for a failed gate on a public body's power, which this is.
  other reading NOTHING (the gate is the Authority's own opinion, a standard for exercising its power, not a fact the caller can show to be absent, and the text does not say what the Authority may do when it holds neither view; the text says "Where", and the periods ruling's item (b) says a failed "where" condition answers JUST FALSE, which is the reading taken).
  licence [the S1b ruling of 2026-11-21 (`docs/ENCODING-GUIDE.md` line 101, 2026S1bC): "A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes"], which replaces the grant ruling's limit 3 for this site; the other reading rests on the grant ruling's limit 1 ([the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"]: NOTHING for a power whose gate failed; the "In short" sentence: "limits a grant or prohibition in its own wording and the case falls outside the limit"); [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] says to list a "may" function whose gate is "where" and not to change it (replaced for this site by the S1b ruling): this is a split site (ii) of the brief, answered as at section 282AA(1) and as at sections 277(1AB), (1AD) and (2). Listed under the marginal readings.
- **s281-2** (s 281(2); `s 281(2) the person may apply to the Authority for the revocation to be reviewed`)
  took the 14 days as running from the day of the revocation (keel P1: the day of the revocation is not counted as day 1, so the last day is the 14th day after it) with an application on the day of the revocation itself in time (the keel's "not later than the end of a period after", not its "within a period after" window, which opens the day after, P2: the text says "within 14 days of", and a person who applies on the day of the revocation is evidently within 14 days of it), and JUST FALSE outside it, because "within 14 days" is a period the text fixes in its own words; NOTHING where nothing has been revoked.
  other reading the keel's P2 window, which opens the day after the revocation, so that an application on the day of the revocation is out of time.
  licence [the periods ruling of 2026-11-05, item (a) (`inputs/ENCODING-GUIDE.md` line 93): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"] (a period the text fixes in its own words). "Within 14 days" is a period, not a gate of the "where", "when" or "upon" kind, so this is not a split site.
- **s281-2e** (s 281(2); `s 281(2) the revocation remains in effect`)
  took the revocation as remaining in effect whether or not the person has applied for a review (the text says it "remains in effect unless it is withdrawn by the Authority", and does not make the application a ground for it to lapse).
  other reading an application for review suspends the revocation.
  licence the text's own words ("unless").
- **s282** (s 282; `s 282 nothing in this Part limits or diminishes the liability`)
  took the declaration as a rule that preserves a liability (JUST TRUE where both facts are shown) and NOTHING otherwise: it declares what this Part does not do and is silent on every other transaction.
  other reading an inert row (a declaration "to avoid doubt" that adds no rule).
  licence [the "In short" sentence (`inputs/ENCODING-GUIDE.md` line 86): "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not")" and, for `NOTHING`, "limits a grant or prohibition in its own wording and the case falls outside the limit"] (silent). Whether an offence is a "relevant offence" is for Part 12 and the Companies Act 1967, outside this text.

### s 282AA: directions (sfad-directions.l4)

- **s282AA-1** (s 282AA(1); `s 282AA(1) the Authority may issue the direction`)
  took JUST FALSE where the Authority does not think the direction necessary or expedient, or does not give it by written notice: the gate "where it thinks it necessary or expedient" fails, and the S1b ruling (Guide line 101, 2026S1bC) answers JUST FALSE for a failed gate on a public body's power, which this is.
  other reading NOTHING (the gate is the Authority's own opinion, a standard for exercising its power, not a fact the caller can show to be absent, and the text does not say what the Authority may do when it holds no such view; the text says "where", and the periods ruling's item (b) says a failed "where" condition answers JUST FALSE, which is the reading taken).
  licence [the S1b ruling of 2026-11-21 (`docs/ENCODING-GUIDE.md` line 101, 2026S1bC): "A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes"], which replaces the grant ruling's limit 3 for this site; the other reading rests on the grant ruling's limit 1 ([the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"]: NOTHING for a power whose gate failed; the "In short" sentence: "limits a grant or prohibition in its own wording and the case falls outside the limit"); [the grant ruling of 2026-11-12, limit 3 (`inputs/ENCODING-GUIDE.md` line 99): "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon" ... and an "entitled"-named function"] says to list a "may" function whose gate is "where" and not to change it (replaced for this site by the S1b ruling): this is a split site (ii) of the brief, answered as at section 281(1) and as at sections 277(1AB), (1AD) and (2). Listed under the marginal readings.
- **s282AA-1p** (s 282AA(1)(a), (b) and (c); the three paragraph functions)
  took NOTHING for a recipient outside the paragraph (the paragraphs name the persons to whom the Authority may issue directions and do not say it may not direct anyone else).
  other reading JUST FALSE.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] (a scope limit with no "only") and [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].
- **s282AA-2** (s 282AA(2); `s 282AA(2) the person given the notice must comply with every direction contained in it`)
  took JUST FALSE for a person to whom no notice is given (the duty is the person's own question, and it is a duty).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] (keep JUST FALSE "for a bar, a duty or the provision's own question") and [the case-by-case ruling of 2026-11-05T10:25:24Z (`inputs/ENCODING-GUIDE.md` line 95): "a duty whose "if" or "where" is unmet ... decided site by site, at encoding time, on the text's own words", each site with one fork line] (a duty whose "if" is unmet). The regulative rule below has no time limit: "must comply" gives none, so no trace reaches BREACH (listed under "Rules with no breach path").
- **s282AA-4** (s 282AA(4); `s 282AA(4) the person is guilty of an offence`)
  took JUST FALSE where the contravention element is unmet (this provision's own question).
  other reading NOTHING.
  licence [the grant ruling of 2026-11-12, limit 2 (`inputs/ENCODING-GUIDE.md` line 98): "keep `JUST FALSE` where the text closes the gate itself ... and for a bar, a duty or the provision's own question"] and the brief's split site (i).
- **s282AA-5** (s 282AA(5); `s 282AA(5) the person incurs no criminal or civil liability for the thing done or omitted`)
  took NOTHING where an element is missing (the trustee, the connection with a direction, reasonable care, good faith): the immunity is limited in its own wording and the text does not say that a trustee who lacked care or good faith is liable.
  other reading JUST FALSE.
  licence [the periods ruling of 2026-11-05, item (c) (`inputs/ENCODING-GUIDE.md` line 93): "a scope limit with no "only" ...: outside the scope the answer is `NOTHING`"] (a scope limit with no "only") and [the grant ruling of 2026-11-12, limit 1 (`inputs/ENCODING-GUIDE.md` line 97): answer `NOTHING` "only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"].

### the answers to seams S4 and S5 (sfad-exemption-summary.l4)

- **sum-S4** (Subdivision (4); `Subdivision (4) the offer qualifies for an exemption under Subdivision (4) of Division 1 of Part 13, other than section 280`)
  took the offer as qualifying when at least one exemption of the Subdivision (other than section 280) is shown to hold (its function answers JUST TRUE) and has not been revoked under section 281; FALSE where none is shown, including where an answer is NOTHING (PLAN.md section 4.1 types the seam input as BOOLEAN, so the third value cannot cross it).
  other reading a revoked exemption still "qualifies" until the review of section 281(2) ends; or a three-valued seam in which NOTHING stays NOTHING.
  licence the seam's type in PLAN.md and the text of section 281(1) ("revoke any exemption under this Subdivision"), which makes a revoked exemption no longer an exemption the offer can rely on. Section 280 is left out, as the question names it ("other than section 280").
- **sum-S5** (s 262(3); `s 262(3) the securities are asset-backed securities as section 262(3) defines them`)
  took the securities as asset-backed securities only where section 262(3)'s own function answers JUST TRUE; FALSE where it answers JUST FALSE or NOTHING (PLAN.md section 4.1 types the seam input as BOOLEAN).
  other reading a three-valued seam in which NOTHING stays NOTHING.
  licence the seam's type in PLAN.md.

## Jural relations (sfad)

One row per provision or group that creates, changes or removes a position between parties; a provision that only counts, defines or deems has a row with no parties.
The Hohfeld kinds are the table's; the L4 names are the functions or rules that carry each row.

| Provision | First party: position | Second party: position | Kind | L4 |
| --- | --- | --- | --- | --- |
| s 261(1) | none (scope of the Subdivision) | none | - | `s 261(1) this Subdivision applies to the offer` |
| s 261(1A), (1B) | the prescribed entity: immunity from ss 268, 269, 270 | the holders of its debentures and the trustee: disability (cannot demand what those sections give) | immunity / disability | `s 261(1A) sections 268, 269 and 270 do not apply to the borrowing entity`; `s 261(1B) the entity is a prescribed entity` |
| s 261(1C)(a), (b) | the Authority: power to impose, vary, revoke conditions | the prescribed entity: liability | power / liability | `s 261(1C)(a) the Authority may impose a condition or restriction on the entity`; `s 261(1C)(b) the Authority may vary or revoke the condition or restriction` |
| s 261(1C) (the entity "must comply") | the Authority: claim | the prescribed entity: duty | claim / duty | `s 261(1C) the prescribed entity must comply with the condition or restriction`; rule `s 261(1C) the duty of a prescribed entity to comply with a condition or restriction` |
| s 261(1D) | the State (prosecutor): power to prosecute (the text names no prosecutor) | the person who contravenes: liability to the stated fine | power / liability | `s 261(1D) the person is guilty of an offence`; `s 261(1D) the penalty for the offence` |
| s 261(2) | none (text shows `[Deleted by Act 1 of 2005]`) | none | - | repealed row |
| s 261(3) | none (a definition by cross-reference) | none | - | `s 261(3) the corporation is related to the other corporation for this Subdivision` |
| s 262(1) | none (a rule of when an offer of asset-backed securities is made) | none | - | `s 262(1) the asset-backed securities are issued by a special purpose vehicle or the trustee of one` |
| s 262(2) | the person (or class) the Authority exempts: immunity from section 262 | the Authority: disability to enforce section 262 against the person while the conditions are met | immunity / disability | `s 262(2) the person is exempt from section 262` |
| s 262(3) | none (definitions) | none | - | `s 262(3) the body is a special purpose vehicle`; `s 262(3) the arrangement is a securitisation transaction`; `s 262(3) the securities are asset-backed securities` |
| s 265(1) | the holders of irredeemable debentures, through the trustee (or a holder where there is no trustee): power to apply; the court: power to order | the borrowing entity: liability to the order | power / liability | `s 265(1) the court may order the security for the debentures to be enforceable` |
| s 265(2) | the trustee or holders under the terms of the debentures: preserved power | the borrowing entity: liability | power / liability | `s 265(2) section 265(1) does not affect the power` |
| s 265A(1) | the holders of debentures: claim that a trustee be appointed | the borrowing entity: duty | claim / duty | `s 265A(1) the borrowing entity must appoint a trustee for the holders of debentures for the entire tenure`; rule `s 265A(1) the duty to appoint a trustee for the holders of debentures` |
| s 265A(2), (3), (5) | the holders of debentures: claim that the trustee is a qualified, independent person | the borrowing entity: duty to ensure and to consider | claim / duty | `s 265A(2) the borrowing entity has ensured that the appointed trustee meets the requirements`; `s 265A(3) the borrowing entity has considered the matters before being satisfied`; `s 265A(5) the debentures are asset-backed securities or structured notes` |
| s 265A(4) | the State: power to prosecute | the person who contravenes (1), (2) or (3): liability | power / liability | `s 265A(4) the person is guilty of an offence`; `s 265A(4) the penalty for the offence` |
| s 266(1) | the holders of the debentures: claim | the trustee: duty of diligence, vigilance and the paragraphs (a) to (d) | claim / duty | `s 266(1) the trustee for the holders of debentures has done what paragraphs (a) to (d) require` |
| s 266(2) | the trustee: power to apply to the Authority | the borrowing entity: liability | power / liability | `s 266(2) the trustee may apply to the Authority for an order` |
| s 266(3)(a) | the Authority: power to impose restrictions | the borrowing entity: liability (it has a claim to be heard first) | power / liability | `s 266(3)(a) the Authority may impose restrictions on the activities of the borrowing entity` |
| s 266(3)(b) | the borrowing entity: claim that the Authority direct the trustee; the Authority: power to direct | the Authority: duty to direct on the entity's requirement; the trustee: duty to apply as directed | claim / duty; power / liability | `s 266(3)(b) the Authority must direct the trustee to apply to the court`; `s 266(3)(b) the trustee must apply to the court as directed`; rule `s 266(3)(b) the duty of the trustee to apply to the court as directed` |
| s 266(4) | the trustee: power to apply to the court; the borrowing entity: claim that the trustee apply on its request | the trustee: duty to apply on the request; the borrowing entity: liability to the application | power / liability; claim / duty | `s 266(4) the trustee may apply to the court for an order under subsection (5)`; `s 266(4) the trustee must apply to the court for an order under subsection (5)`; rule `s 266(4) the duty of the trustee to apply to the court on the request of the borrowing entity` |
| s 266(5) | the court: power to order; the borrowing entity: claim to be heard | the borrowing entity: liability; the court: duty to have regard to the rights of all creditors | power / liability; claim / duty | `s 266(5) the court may make the order`; `s 266(5) the court has done what it must in making the order` |
| s 266(6) | the court: power to vary or rescind | the parties to the order: liability | power / liability | `s 266(6) the court may vary or rescind the order` |
| s 266(7) | the holders: claim | the trustee: duty to have regard to the security or to the position as unsecured creditors | claim / duty | `s 266(7) the trustee has had the regard the subsection requires` |
| s 266(8) | the trustee: privilege to rely on a competent person's certificate | the holders and the borrowing entity: no-right to complain of that reliance | privilege / no-right | `s 266(8) the trustee may rely on the certificate, report or statement` |
| s 267(1), (2), (3), (4) | the trustee: power to apply to the court; the court: power to give directions, order a meeting | the borrowing entity and the holders: liability | power / liability | `s 267(1) the trustee for the holders of debentures may apply to the court`; `s 267(2) the court may give directions or accede to the application`; `s 267(2)(b) the court may accede to the application on terms or make another order`; `s 267(3) the court may order a meeting of the holders of debentures to be called`; `s 267(4) the meeting is held and conducted as the subsection requires` |
| s 267A | a holder, the Authority or an approved exchange: power to apply; the court: power to order | the trustee: liability to be compelled | power / liability | `s 267A the person may apply to the court for an order compelling the trustee to perform the trustee's duties`; `s 267A the court may make the order or dismiss the application` |
| s 268(4) | the trustee: claim to particulars of the charge | the borrowing entity and each guarantor entity: duty, with 21 days (charge) or 7 days (advances) | claim / duty | `s 268(4) the entity must provide the trustee with particulars of the charge`; `s 268(4)(a) the particulars of the charge are provided in time`; `s 268(4)(b) the particulars of the amounts advanced are provided in time`; rules `s 268(4)(a) the duty to provide the trustee with particulars of the charge within 21 days` and `s 268(4)(b) the duty to provide the trustee with particulars of the amounts advanced within 7 days` |
| s 268(5) | the borrowing entity or guarantor: privilege to give net-amount particulars every 3 months | the trustee: no-right to more frequent particulars | privilege / no-right | `s 268(5) it is sufficient to provide particulars of the net amount every 3 months` |
| s 268(6) | the trustee: claim to the accounts | the directors or equivalent persons: duty, within 3 months of the first 6 months and 5 months of the financial year | claim / duty | `s 268(6) the directors or equivalent persons must cause the accounts to be made out and lodged with the trustee`; `s 268(6)(a) the half-year accounts are made out and lodged in time`; `s 268(6)(b) the annual accounts are made out and lodged in time`; rules `s 268(6)(a) ...`, `s 268(6)(b) ...` |
| s 268(6A) | the trustee and holders: claim | the person who provides information: duty of due care | claim / duty | `s 268(6A) the person has used the due care the subsection requires` |
| s 268(7), (7A) | the State: power to prosecute | the person who fails to comply with (6), or contravenes (6A): liability | power / liability | `s 268(7) the person is guilty of an offence`, `s 268(7) the penalty for the offence`, `s 268(7A) the person is guilty of an offence`, `s 268(7A) the penalty for the offence` |
| s 268(8) | none (a deeming rule) | none | - | `s 268(8) the account and balance sheet are treated as financial statements for the Companies Act 1967 sections` |
| s 268(9) | the Authority: claim to notice | the trustee: duty to lodge notice immediately | claim / duty | `s 268(9) the trustee must lodge notice of that fact with the Authority`; rule `s 268(9) the duty of the trustee to lodge notice with the Authority` |
| s 268(10) | the borrowing entity: privilege not to audit (half-year always; annual with the trustee's consent) | the trustee and holders: no-right to an audit | privilege / no-right | `s 268(10)(a) the half-year accounts need not be audited`; `s 268(10)(b) the annual accounts need not be audited, or the audit may be limited` |
| s 268(11) | the Authority: claim to a copy of the trustee's consent | the directors or equivalent persons: duty, at the time the accounts are lodged | claim / duty | `s 268(11) the directors or equivalent persons must lodge a copy of the notice with the Authority`; `s 268(11) the copy of the notice is lodged at the time the accounts are lodged`; rule `s 268(11) the duty to lodge a copy of the trustee's notice with the Authority at the time the accounts are lodged` |
| s 268(12), (13) | the directors or equivalent persons: privilege to estimate the stock in trade | the trustee: no-right unless it requires otherwise in writing | privilege / no-right; power / liability (the trustee's written requirement) | `s 268(12) the accounts may be based on the directors' estimate of the stock in trade`; `s 268(13) the estimation is made on the basis the subsection requires` |
| s 268A(1), (2) | the holders of unlisted debentures and the trustee: claim to a semi-annual report | the borrowing entity: duty to prepare, make available and lodge it within 2 months of the end of each period of 6 months | claim / duty | `s 268A(1) the borrowing entity must prepare and make available a semi-annual report`; `s 268A(1) the last day of the period of 6 months covered by a semi-annual report`; `s 268A(2) the semi-annual report is lodged with the trustee in time`; rules `s 268A(1) the duty to prepare and make available a semi-annual report`, `s 268A(2) the duty to lodge the semi-annual report with the trustee within 2 months` |
| s 268A(3) | the Authority: claim to notice | the trustee: duty to lodge notice | claim / duty | `s 268A(3) the trustee must lodge notice of that fact with the Authority`; rule `s 268A(3) the duty of the trustee to lodge notice with the Authority` |
| s 268A(4) | the holders of unlisted debentures: claim to disclosure of material information | the borrowing entity: duty to disclose immediately | claim / duty | `s 268A(4) the borrowing entity must disclose the information to the holders of unlisted debentures`; `s 268A(4) the borrowing entity has disclosed the information as the subsection requires`; rule `s 268A(4) the duty to disclose information materially affecting the unlisted debentures` |
| s 268A(5), (8), (10) | the State: power to prosecute | the person who contravenes: liability | power / liability | `s 268A(5) ...`, `s 268A(8) ...`, `s 268A(10) ...` (offence and penalty functions of each) |
| s 268A(6) | the holders of redeemable unlisted debentures: claim to bid or redemption prices | the borrowing entity: duty (frequency, indicative marking, independence and fairness) | claim / duty | `s 268A(6) the borrowing entity must make bid or redemption prices available and meet paragraphs (a) to (c)`; `s 268A(6)(a) ...` (two functions), `s 268A(6)(b) ...`, `s 268A(6)(c) ...` |
| s 268A(7) | the holders: claim to the accounts on the day of lodgment | the borrowing entity: duty | claim / duty | `s 268A(7) the accounts are made available to the holders on the day of lodgment`; rule `s 268A(7) the duty to make the accounts available to the holders on the day of lodgment` |
| s 268A(9) | the trustee and holders: claim | the person who provides information: duty of due care | claim / duty | `s 268A(9) the person has used the due care the subsection requires` |
| s 269(1) | the borrowing entity: power to require information by written notice | the guarantor entity: liability | power / liability | `s 269(1) the borrowing entity may require the guarantor entity to provide the information` |
| s 269(2) | the borrowing entity: claim to the information | the guarantor entity: duty to provide it before the date specified, which must be at least 14 days after the notice | claim / duty | `s 269(2) the guarantor entity must provide the borrowing entity with the information`; `s 269(2) the date specified in the notice is not earlier than 14 days after the notice is given`; `s 269(2) the information is provided before the date specified in the notice`; rule `s 269(2) the duty of the guarantor entity to provide the information before the specified date` |
| s 269(3) | the State: power to prosecute | the guarantor entity and its officers in default: liability | power / liability | `s 269(3) the person is guilty of an offence`; `s 269(3) the penalty for the offence` |
| s 270(1), (2) | the trustee and holders: claim to progress reports | the borrowing entity: duty | claim / duty | `s 270(1) the borrowing entity must make reports to the trustee on the progress of the purpose or project`; `s 270(2) the progress report is included in the report required under section 268(1)`; rule `s 270(1) the duty to make reports to the trustee on progress` |
| s 270(3) | the trustee: power to give notice requiring repayment; the holders: claim that it do so where necessary | the borrowing entity: liability; the trustee: duty to lodge a copy with the Authority within one month | power / liability; claim / duty | `s 270(3) the trustee may give written notice requiring the borrowing entity to repay the moneys`; `s 270(3) the trustee must give written notice requiring the borrowing entity to repay the moneys`; `s 270(3) the copy of the notice is lodged with the Authority in time`; rule `s 270(3) the duty of the trustee to lodge a copy of the notice within one month` |
| s 270(4) | the borrowing entity: immunity from the notice where the trustee is satisfied of (a), (b) or (c) | the trustee: disability (shall not give the notice) | immunity / disability | `s 270(4) the trustee must not give notice under subsection (3)`; rule `s 270(4) the bar on the trustee giving notice` |
| s 270(5) | the person owed the moneys: claim to repayment on demand | the borrowing entity: duty | claim / duty | `s 270(5) the borrowing entity is liable to repay the moneys`; rule `s 270(5) the duty of the borrowing entity to repay the moneys on demand` |
| s 270(6) | none (a deeming rule for the purpose in the notice) | none | - | `s 270(6) the purpose in the notice is treated as the purpose specified in the prospectus` |
| s 271(1) | the holders: immunity from exoneration clauses | the trustee: disability (cannot be exempted from the duty of care) | immunity / disability | `s 271(1) the provision is void` |
| s 271(2), (3) | the trustee: privilege (the saved release or provision) | the holders: no-right to challenge the saved release or provision | privilege / no-right | `s 271(2) subsection (1) does not invalidate the release or the provision`; `s 271(3) subsection (1) does not operate against the provision or the trustee's exemption` |
| s 272(1), (2) | the offeror: immunity from Subdivisions (1A), (2) and (3) of this Division (other than section 257) where no consideration is given | the Authority and the holders: disability to require a prospectus | immunity / disability | `s 272(1) the offer is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)`; `s 272(2) the offer of securities-based derivatives contracts is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)` |
| s 272A(1) to (3) | the offeror: immunity (a small, personal offer of at most $5 million in 12 months, with a statement and notification, no advertisement, limited expenses and no registered prospectus) | the Authority and the holders: disability | immunity / disability | `s 272A(1) the offer is exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)` and its limbs |
| s 272A(4) to (7), (9) to (11) | none (rules of counting, deeming and definition) | none | - | `s 272A(4) the amount raised by an offer`; `s 272A(5) the total amount raised within the period of 12 months`; `s 272A(10) the communication is an advertisement` and the others |
| s 272A(8) | the person who sells what was acquired under the small-offers exemption: liability to Subdivisions (2) and (3) unless a paragraph is met | the Authority and buyers: claim | liability / claim | `s 272A(8) Subdivisions (2) and (3) of this Division apply to the offer that resulted in the sale` |
| s 272B | the offeror: immunity (private placement to no more than 50 persons in 12 months, with no advertisement, limited expenses and no registered prospectus) | the Authority and the holders: disability | immunity / disability | `s 272B(1) the offers are exempt from Subdivisions (1A), (2) and (3) of this Division (other than section 257)` and its limbs |
| s 273(1) and (2) to (4), (9), (10) | the offeror: immunity under whichever of paragraphs (a) to (k) the offer comes within | the Authority and the holders: disability | immunity / disability | `s 273(1) the offer is exempt from Subdivisions (2) and (3) of this Division (other than section 257)` and the paragraph functions |
| s 273(5), (7) | the offeror: immunity for 6 months from the Authority's declaration; the Authority: power to declare | the holders: disability; the person affected: no-right to challenge (the declaration is final) | immunity / disability; power / no-right | `s 273(5) the offer is within the period of 6 months from the date of the Authority's declaration`; `s 273(7) the declaration made under subsection (5) is final` |
| s 273(6) | the Authority: power to impose conditions on making the declaration | the offeror: liability | power / liability | `s 273(6) the Authority may impose conditions or restrictions on the offer` |
| s 273(8), (8B) | the State: power to prosecute | the person who contravenes a condition, or (8A), or knowingly permits a prohibited advertisement: liability | power / liability | `s 273(8) the person is guilty of an offence`; `s 273(8B) the person is guilty of an offence` |
| s 273(8A) | the public and the Authority: claim that nothing is advertised or published outside the prescribed requirements | the person: duty not to (a bar, `SHANT`) | claim / duty | `s 273(8A) the person must not advertise or publish what the subsection bars`; rule `s 273(8A) the bar on advertising or publishing` |
| s 274, 275(1), (1A), (3) | the offeror: immunity (offer to an institutional investor, to a relevant person, or at not less than $200,000 each) | the Authority and the holders: disability | immunity / disability | `s 274 the offer is exempt ...`; `s 275(1) the offer is exempt ...`; `s 275(1A) the offer is exempt ...`; `s 275(3) the person is treated as an exempt person` |
| s 275(2), (2A), (4) | none (definitions and the amount the Authority may substitute) | none | - | `s 275(2) the person is a relevant person`; `s 275(2) the document is an information memorandum` and the others |
| s 276(1), (2) | the person who sells within 6 months: liability to Subdivisions (1A), (2) and (3); the buyer, where the sale is to an institutional investor or a relevant person: immunity | the Authority: claim | liability / claim; immunity / disability | `s 276(1) Subdivisions (1A), (2) and (3) of this Division apply to the offer resulting in the sale`; `s 276(2) Subdivisions (1A), (2) and (3) of this Division do not apply to the offer resulting in the sale` |
| s 276(3), (4) | the Authority and the market: claim that an investment-holding corporation's securities, or the beneficiaries' rights in an investment trust, are not transferred within 6 months except as the subsections allow | the corporation, trustee or beneficiary: duty not to transfer (a bar, no party named) | claim / duty | `s 276(3) the transfer of the securities or contracts of the investment-holding corporation is barred`; `s 276(4) the transfer of the beneficiaries' rights and interest in the trust is barred` |
| s 276(5), (6), (7), (1A) | none (definitions and rules of reading) | none | - | `s 276(5) the person is a beneficiary for subsection (4)`; `s 276(6) an offer to sell may be made in reliance on section 273(1)(d), (da), (e) or (ea)` |
| s 277(1), (1A), (1AC) | the offeror: immunity (an offer made using an offer information statement lodged with the Authority, within 6 months) | the Authority and the holders: disability | immunity / disability | `s 277(1) the offer is exempt ...`; `s 277(1A) the offer is made within the period of 6 months from the date the offer information statement is lodged`; `s 277(1AC) the offer is exempt ...` |
| s 277(1AB), (1AD), (2) | the Authority: power to declare, to impose conditions and restrictions, and to modify the prescribed form and content | the subsidiary, the listed entity and the person applying: liability | power / liability | `s 277(1AB) the Authority may declare ...`; `s 277(1AD) the Authority may provide ...`; `s 277(2) the Authority may modify ...` |
| s 277(3), (4) | none (rules of application and reading) | none | - | `s 277(3) sections 249, 249A, 253, 254 and 255 apply ...`; `s 277(4)(a)`, `(b)`, `(c)` |
| s 277(5), (6) | the Authority: claim that the expert's, issue manager's or underwriter's written consent is lodged with the statement | the person who must lodge it: duty (no party named) | claim / duty | `s 277(5) the written consent of the expert is lodged ...`; `s 277(6) ...` |
| s 277(7) | the public and the Authority: claim that nothing is advertised or published outside the prescribed requirements | the person: duty not to (a bar, `SHANT`) | claim / duty | `s 277(7) the person must not advertise or publish what the subsection bars`; rule `s 277(7) the bar on advertising or publishing` |
| s 277(8) | the State: power to prosecute | the person who contravenes (7) or knowingly permits a prohibited advertisement: liability | power / liability | `s 277(8) the person is guilty of an offence`; `s 277(8) the penalty for the offence` |
| s 278(1), (2) | the offeror: immunity (international debentures, to specified investors, with the conditions of (2)) | the Authority and the holders: disability | immunity / disability | `s 278(1) the offer is exempt ...` and its limbs |
| s 278(3) | the Authority: power to add to, vary or amend the conditions by order in the Gazette | offerors: liability | power / liability | `s 278(3) the Authority may add to, vary or amend the conditions specified in subsection (2)` |
| s 279 | the offeror: immunity (an offer of debentures made or guaranteed by the Government or an international financial institution) | the Authority and the holders: disability | immunity / disability | `s 279 the offer is exempt from Subdivisions (2) and (3) of this Division` |
| s 280(1), (3) | the person making the offer by machine or prescribed electronic means: immunity from the prospectus or profile statement requirement of section 240 | the Authority and the holders: disability, until the indications of (3) are given | immunity / disability | `s 280(1) the person making the offer is exempted ...`; `s 280(3) the machine or the electronic means gives the indications that subsection (1) needs` |
| s 280(2) | the Authority and the holders: claim that a complying prospectus or profile statement is still prepared and issued | the person making the offer: duty (no party named, no time) | claim / duty | `s 280(2) a prospectus or profile statement complying with the other requirements has been prepared and issued for the offer` |
| s 280A | the Authority: power to require information by regulations | the person or class of persons: liability | power / liability | `s 280A the Authority may require a person or class of persons ...` |
| s 281(1) | the Authority: power to revoke an exemption | the person relying on it: liability | power / liability | `s 281(1) the Authority may revoke an exemption under this Subdivision` |
| s 281(2) | the Authority: power to revoke without a hearing; the person: power to apply for review within 14 days | the person: no-right to be heard first; the Authority: liability to review | power / no-right; power / liability | `s 281(2) the Authority may revoke the exemption without giving the person affected an opportunity to be heard`; `s 281(2) the person may apply to the Authority for the revocation to be reviewed`; `s 281(2) the revocation remains in effect` |
| s 281(3) | the Authority: immunity from appeal | the person: disability to appeal | immunity / disability | `s 281(3) the revocation is final and no appeal lies from it` |
| s 282 | any person's liability under Division 2 of Part 12 of the Companies Act 1967 and Part 12: preserved | the offeror: no immunity from it | (declaratory) | `s 282 nothing in this Part limits or diminishes the liability` |
| s 282AA(1) | the Authority: power to issue directions (to an offeror, a borrowing entity, a trustee) | the recipient: liability | power / liability | `s 282AA(1) the Authority may issue the direction` and its paragraphs |
| s 282AA(2) | the Authority: claim that every direction is complied with | the person given the notice: duty (no time limit) | claim / duty | `s 282AA(2) the person given the notice must comply with every direction contained in it`; rule `s 282AA(2) the duty to comply with every direction contained in the notice` |
| s 282AA(3) | the Authority: privilege not to publish in the Gazette | none | privilege | `s 282AA(3) the direction need not be published in the Gazette` |
| s 282AA(4) | the State: power to prosecute | the person who contravenes a direction: liability | power / liability | `s 282AA(4) the person is guilty of an offence`; `s 282AA(4) the penalty for the offence` |
| s 282AA(5) | the trustee and the person acting for it: immunity from criminal and civil liability for what was done with reasonable care and in good faith | whoever would sue or prosecute: disability | immunity / disability | `s 282AA(5) the person incurs no criminal or civil liability for the thing done or omitted` |
| Subdivision (4) as a whole (seam S4) | none | none | - | `Subdivision (4) the offer qualifies for an exemption under Subdivision (4) of Division 1 of Part 13, other than section 280` |

## Marginal readings for a lawyer (sfad)

The readings below are the ones a lawyer might reasonably overrule; each is a one-branch change (the comment `-- SPLIT-SITE` or the fork line names the branch).

1. The twelve "may" functions gated by "where", "when", "upon", "on application" or "on making" (split sites (ii), table below): ten answer JUST FALSE (the periods ruling's item (b), with the delegated-definitions ruling's item (c)), and two, ss 281(1) and 282AA(1), answer JUST FALSE by the S1b ruling (Guide line 101, 2026S1bC), because each is a failed gate on a public body's power; the gate is the Authority's own opinion, which the other reading, NOTHING, would rely on.
   The Guide says "on application" is not among the words it names; it was read by analogy with "upon" at ss 277(1AB), 277(2) and 266(2).
   The Guide's grant ruling points the other way (NOTHING) and says to list, not to change, these functions (limit 3); the S1b ruling replaces limit 3 for ss 281(1) and 282AA(1) only, so for the other ten the question stays as listed.
2. "Immediately" at ss 268(9), 268A(3), 268A(4) and 270(5) was read as a promptness standard with no measure, so the four rules have no `WITHIN` and no breach path (forks s268-9i, s268A-3i, s268A-4i, s270-5i).
3. Ss 277(5), 277(6) and 280(2) are duties with no named party; they are decision functions that answer whether the duty was met (JUST TRUE met, JUST FALSE not met, NOTHING where the duty does not arise), and "at the same time" is read as the same day (forks s277-5, s277-6, s280-2).
4. Section 281(2) "within 14 days of the revocation" lets an application on the day of the revocation itself be in time, which the keel's "within a period after" window (P2) would not (fork s281-2).
5. The vacuous conditions at s 277(1)(aa) and (ab) answer JUST TRUE where their antecedent is unmet (forks s277-1aa, s277-1ab); no ruling covers a conditional condition.
6. Section 280(1) "Subject to subsection (3) and such requirements as the Authority may prescribe" is read as the text's own condition (JUST FALSE where unmet), a plain variant of "if" (fork s280-1).
7. The seams S4 and S5 are BOOLEAN as PLAN.md types them, so the third value does not cross them (a NOTHING answer becomes FALSE: forks sum-S4, sum-S5).
8. "(other than section 257)" is left to the caller at every exemption that carries it (fork s277-1-257 and its fellows): no rule about section 257 is encoded here, because section 257 is another part's.
9. Section 277(1AC) answers NOTHING where no declaration has been made (a scope), although "Where the Authority makes a declaration" is a "where" (fork s277-1AC).
10. Section 278(1)(a) "being persons or bodies that appear to the Authority to have sufficient expertise" is read as the Authority's reason for specifying the investors, not a second condition the caller shows (fork s278-1a).
11. Section 266(4)(b) refers to "an order made by the Authority under subsection (2)" (finding 2 below).

### Reading a result: FALSE and NOTHING (sfad)

A function answers `JUST TRUE` where the text says yes, `JUST FALSE` only where the text says no in its own words, and `NOTHING` everywhere else; each branch carries a comment `-- FALSE-kind (the text says no in its own words): "<quote>"` (two, at ss 281(1) and 282AA(1), carry `-- FALSE-kind (a public body's power, a failed gate; S1b ruling 2026S1bC)` instead) or `-- NOTHING-kind (<reason>)`.
The reasons used are `silent` (46 branches), `limited by its own wording` (83), `points outside the text` (6), `list not closed` (2: `s 267A the person may apply to the court for an order compelling the trustee to perform the trustee's duties` and `s 272A(3)(b) the offer is made to a person who is likely to be interested in that offer`) and `includes` (2: `s 276(1A) the sale of the converted securities is a sale for subsection (1)` and `s 276(5) the person is a beneficiary for subsection (4)`); `undefined term` does not occur in this part's branches (counts by `grep -ho "NOTHING-kind ([^)]*)" sfad-*.l4`, read on 2026-11-19, before the two sites at ss 281(1) and 282AA(1) were turned to `JUST FALSE` by the S1b ruling; they are now `FALSE-kind (a public body's power, a failed gate; S1b ruling 2026S1bC)` and no longer counted under `limited by its own wording`).
A function named for a grant or a power answers NOTHING, not JUST FALSE, when an "if" gate fails, with one fork line each (the grant ruling, limit 1), except at the "where", "when" and "upon" gates listed as split sites (ii), where the periods ruling's item (b) is followed and the other reading is flagged (limit 3), and except that the S1b ruling (Guide line 101, 2026S1bC) answers JUST FALSE at ss 281(1) and 282AA(1), which replaces limit 3 for those two.
A bar, a duty and the provision's own question keep JUST FALSE (limit 2).
A BOOLEAN result (the seams S3, S4 and S5) has no third value.

The rulings this part relies on, word for word from `inputs/ENCODING-GUIDE.md` (line numbers are the file's):

- Line 86: In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
- Line 87: Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
- Line 93: **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- Line 94: **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- Line 95: **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.
- Lines 96 to 100: - **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The ruling sets three limits: 1. answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed; 2. keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question; 3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it). The ruling and the counts it produced are recorded in `subjects/uk/companies-act-2006/encodings/legalese-sonnet-5.5/NOTES.md`, section "The grant and power name test".

## Seams (sfad)

The brief governs where it differs from PLAN.md; for this part the one difference is that the Guide's two-question rule for split sites is recorded below, which PLAN.md does not mention.

| Seam | Direction | Provision | Name of the input or function | Module |
| --- | --- | --- | --- | --- |
| S3 | sfad answers (sfac asks) | s 280 | `s 280(1) the offer is an offer referred to in section 280` (BOOLEAN) | sfad-ois-intl-gov-atm.l4 |
| S4 | sfad answers | Subdivision (4), ss 272 to 282 | `Subdivision (4) the offer qualifies for an exemption under Subdivision (4) of Division 1 of Part 13, other than section 280` (BOOLEAN; it takes a list of the sections' answers) | sfad-exemption-summary.l4 |
| S5 | sfad answers | s 262(3) | `s 262(3) the securities are asset-backed securities as section 262(3) defines them` (BOOLEAN) | sfad-exemption-summary.l4 |
| S6 | sfad asks (sfac answers) | s 265A(5) | input `the notes are structured notes as section 240AA(5) defines them` (BOOLEAN) | sfad-debentures.l4 |
| S7 | sfad asks | s 273(1)(i) and (j), (k) | inputs `the offer is an offer of SDRs made, or treated under section 239AA as made, by the entity to a qualifying person` and `... by a trustee-manager of a business trust to a qualifying person` (BOOLEAN each; PLAN.md spells "sponsored depositary receipts" where the inputs say "SDRs", with the same meaning) | sfad-circumstances.l4 |
| S8 | sfad asks | ss 272A(1)(e), 272B(1)(d), 275(1)(c), 275(1A)(d) | input `the prospectus has expired under section 250` (BOOLEAN) | sfad-nocons-small-private.l4, sfad-investor-exemptions.l4 |

The keel's answers are taken as inputs of type MAYBE BOOLEAN and named for the fact: `the person to whom the offer is made is an institutional investor` (s 274, the keel's `s 4A(1)` function), `the person is an accredited investor` (s 275(2)), `the matter is within section 2(2) as the keel answers it` (ss 272A(11), 275(2A)) and the similar inputs; each `@desc` names the keel function whose answer to pass.
Layer 2 calls the layer-1 functions only: the seat's own imports are the prelude, `daydate` and the six layer-1 modules that carry rules (the `IMPORT` lines of `sfad-seat.l4`, read on 2026-11-19), and it imports no keel module directly.
Seams found that the plan lacks: none.
`(other than section 257)` and the sections 240(1)(a) and 240(4) that s 280 exempts from are sfac's: the exemptions answer that the Subdivisions "do not apply" and leave section 257 and the requirement itself to the caller (PLAN.md section 4.3).

## Split sites (sfad)

The brief's two open questions, answered site by site on the text's own words, with the comment `-- SPLIT-SITE (i)` or `(ii)` on the branch line that answers the site and a fork line that names the Guide's ruling it relies on.
Counts (read from the modules by script): 12 sites of (i), all answered JUST FALSE; 12 sites of (ii), all answered JUST FALSE (ss 281(1) and 282AA(1) by the S1b ruling, 2026S1bC).
Every site has a test on the inputs of the branch that answers it and on the inputs of the other branch (the other reading differs only in the one branch).

(i) An unmet element of an offence or a contravention (the reading taken: JUST FALSE, because each function is the offence's own question; the other reading is NOTHING; ruling relied on: the grant ruling's limit 2, "for a bar, a duty or the provision's own question").

| Provision (function) | Module | Answer taken | Fork id(s) |
| --- | --- | --- | --- |
| `s 261(1D) the person is guilty of an offence` | sfad-debentures.l4:121 | JUST FALSE | s261-1D |
| `s 265A(4) the person is guilty of an offence` | sfad-debentures.l4:442 | JUST FALSE | s265A-4 |
| `s 268(7) the person is guilty of an offence` | sfad-debentures.l4:925 | JUST FALSE | s268-7 |
| `s 268(7A) the person is guilty of an offence` | sfad-debentures.l4:945 | JUST FALSE | s268-7A |
| `s 268A(5) the person is guilty of an offence` | sfad-debentures.l4:1189 | JUST FALSE | s268A-5 |
| `s 268A(8) the person is guilty of an offence` | sfad-debentures.l4:1300 | JUST FALSE | s268A-8 |
| `s 268A(10) the person is guilty of an offence` | sfad-debentures.l4:1337 | JUST FALSE | s268A-10 |
| `s 269(3) the person is guilty of an offence` | sfad-debentures.l4:1419 | JUST FALSE | s269-3 |
| `s 273(8) the person is guilty of an offence` | sfad-circumstances.l4:992 | JUST FALSE | s273-8 |
| `s 273(8B) the person is guilty of an offence` | sfad-circumstances.l4:1046 | JUST FALSE | s273-8B |
| `s 277(8) the person is guilty of an offence` | sfad-ois-intl-gov-atm.l4:542 | JUST FALSE | s277-8 |
| `s 282AA(4) the person is guilty of an offence` | sfad-directions.l4:118 | JUST FALSE | s282AA-4 |

(ii) A "may" gated by "where", "when", "upon", "on application" and the like (the readings: JUST FALSE under the periods ruling's item (b) read with the delegated-definitions ruling's item (c); NOTHING under the grant ruling's limit 1; ss 281(1) and 282AA(1) are answered by the S1b ruling, 2026S1bC; the choice for each site and the words that decided it are in its fork line).

| Provision (function) | Module | Answer taken | Fork id(s) |
| --- | --- | --- | --- |
| `s 266(2) the trustee may apply to the Authority for an order` | sfad-debentures.l4:497 | JUST FALSE | s266-2 |
| `s 266(4) the trustee may apply to the court for an order under subsection (5)` | sfad-debentures.l4:567 | JUST FALSE | s266-4a |
| `s 266(5) the court may make the order` | sfad-debentures.l4:616 | JUST FALSE | s266-5 |
| `s 270(3) the trustee may give written notice requiring the borrowing entity to repay the moneys` | sfad-debentures.l4:1480 | JUST FALSE | s270-3 |
| `s 270(5) the borrowing entity is liable to repay the moneys` | sfad-debentures.l4:1566 | JUST FALSE | s270-5a |
| `s 273(6) the Authority may impose conditions or restrictions on the offer` | sfad-circumstances.l4:966 | JUST FALSE | s273-6 |
| `s 276(6) an offer to sell may be made in reliance on section 273(1)(d), (da), (e) or (ea)` | sfad-investor-exemptions.l4:649 | JUST FALSE | s276-6 |
| `s 277(1AB) the Authority may declare that the provision of an offer information statement in lieu of a prospectus would not be prejudicial to investors` | sfad-ois-intl-gov-atm.l4:303 | JUST FALSE | s277-1AB |
| `s 277(1AD) the Authority may provide that the offer may only be made subject to conditions or restrictions` | sfad-ois-intl-gov-atm.l4:383 | JUST FALSE | s277-1AD |
| `s 277(2) the Authority may modify the prescribed form and content of the offer information statement` | sfad-ois-intl-gov-atm.l4:399 | JUST FALSE | s277-2 |
| `s 281(1) the Authority may revoke an exemption under this Subdivision` | sfad-ois-intl-gov-atm.l4:817 | JUST FALSE | s281-1 |
| `s 282AA(1) the Authority may issue the direction` | sfad-directions.l4:73 | JUST FALSE | s282AA-1 |

## Rules with no breach path (sfad)

A regulative rule with no `WITHIN` is never in BREACH by lateness: a trace in which the party never acts stays RESIDUAL.
Rules that have no time limit, no named party or no stated consequence are listed here with the words that say so; each has a decision function that answers the same question.
The rules that reach BREACH in a trace are the three bars `s 270(4) the bar on the trustee giving notice`, `s 273(8A) the bar on advertising or publishing` and `s 277(7) the bar on advertising or publishing` (each a `SHANT` whose act is a BREACH), and the nine dated duties of Subdivision (3) that carry a `WITHIN`: ss 268(4)(a), 268(4)(b), 268(6)(a), 268(6)(b), 268(11), 268A(2), 268A(7), 269(2) and 270(3) (BREACH when the day is passed); each is traced in the tests, and the traces were read on 2026-11-19.

| Provision | Rule or function | Why there is no breach path |
| --- | --- | --- |
| s 261(1C) | `s 261(1C) the duty of a prescribed entity to comply with a condition or restriction` | "must comply with every such condition or restriction": no time limit and no stated consequence in this provision (the offence is s 261(1D), a separate rule) |
| s 265A(1) | `s 265A(1) the duty to appoint a trustee for the holders of debentures` | "must appoint a trustee ... for the entire tenure": no time limit; the consequence is s 265A(4), a separate offence rule |
| s 266(3)(b) | `s 266(3)(b) the duty of the trustee to apply to the court as directed` | "and the trustee must apply accordingly": no time limit |
| s 266(4) | `s 266(4) the duty of the trustee to apply to the court on the request of the borrowing entity` | "must apply to the court": no time limit |
| s 268(9) | `s 268(9) the duty of the trustee to lodge notice with the Authority` | "immediately": a promptness standard with no measure (fork s268-9i) |
| s 268A(1) | `s 268A(1) the duty to prepare and make available a semi-annual report` | "must ... prepare and make available": the time limit is in s 268A(2), a separate rule that does have a breach path |
| s 268A(3) | `s 268A(3) the duty of the trustee to lodge notice with the Authority` | "immediately" (fork s268A-3i) |
| s 268A(4) | `s 268A(4) the duty to disclose information materially affecting the unlisted debentures` | "immediately" (fork s268A-4i) |
| s 270(1) | `s 270(1) the duty to make reports to the trustee on progress` | "from time to time": no period fixed |
| s 270(5) | `s 270(5) the duty of the borrowing entity to repay the moneys on demand` | "on demand ... must immediately repay" (fork s270-5i) |
| s 277(5) | `s 277(5) the written consent of the expert is lodged with the Authority at the same time as the lodgment of the statement` | "must be lodged ... at the same time": no party is named, so there is no regulative rule; the decision function answers whether the duty was met |
| s 277(6) | `s 277(6) the written consent of the issue manager or underwriter is lodged with the Authority at the same time as the lodgment of the statement` | the same |
| s 280(2) | `s 280(2) a prospectus or profile statement complying with the other requirements has been prepared and issued for the offer` | "must still be prepared and issued": no party and no time limit |
| s 282AA(2) | `s 282AA(2) the duty to comply with every direction contained in the notice` (a rule) | "must comply with every direction": no time limit in the text, so a trace in which the person never complies stays RESIDUAL; the consequence is the separate offence of section 282AA(4) |
| s 276(3), (4) | `s 276(3) the transfer of the securities or contracts of the investment-holding corporation is barred`; `s 276(4) the transfer of the beneficiaries' rights and interest in the trust is barred` | bars with no party named ("shall not be transferred"): decision functions only, no regulative rule |

## What the text turns out to say (numbered findings)

1. The rendering repeats a label for the words that finish a paragraph after its sub-paragraphs: at section 273(1)(b) a second "(b) where such offer is in compliance with the laws, codes and other requirements ..." (line 43407) follows sub-paragraphs (i) and (ii), and at section 277(1B) a second "(b) before enabling the prospective subscriber or buyer to submit any application ..." (line 44764) follows sub-paragraphs (i) and (ii). Both are read as the end of the first (b), not a new paragraph (fork s277-1B and the comment at s 273(1)(b)).
2. Section 266(4)(b) speaks of "an order made by the Authority under subsection (2)", while subsection (2) says the trustee may apply "for an order under this subsection" and subsection (3) is where the Authority, "on such application", acts "by written order". The encoding names the input for the text's own words (`the borrowing entity has contravened an order made by the Authority under subsection (2)`), so a caller states one fact whichever way the numbering is read.
3. Section 268A(1) counts "the period of 6 months beginning on the date of issuance of the debentures and each subsequent period of 6 months", so each period begins the day after the previous one ends. The encoding therefore computes the end of the nth period recursively (`s 268A(1) the last day of the period of 6 months covered by a semi-annual report`): for debentures issued on 1 January 2025 the first three periods end on 30 June 2025, 31 December 2025 and 30 June 2026 (tested).
4. The time limits of ss 268, 268A, 269 and 270 are written in days, weeks, months or "not later than" a date; the regulative rules take the number of days between the event and the last day the text allows (counted by `sfa-periods` in the tests) as an input, so that the rule's clock is in days and the month arithmetic stays in one place.
5. Twelve sentences say that Subdivisions (2) and (3), or (1A), (2) and (3), "do not apply" to an offer, and each adds "(other than section 257)": ss 272(1) and (2), 272A(1), 272B(1), 273(1) and (5), 274, 275(1) and (1A), 277(1) and (1AC), and 278(1). The other "do not apply" sentences of the range carry no such words, and each says something different: s 273(1B) names only Subdivision (1A); s 276(2) and s 279 exempt from Subdivisions (2) and (3) (or (1A), (2) and (3)) with no carve-out; s 261(1A) is about sections 268, 269 and 270; s 276(7) and s 280(3) are about other provisions (counted by script over lines 41833-45043 on 2026-11-19, which listed 18 such sentences and read the three lines around each for "257"). The functions follow the text: ss 273(1B), 276(2) and 279 name what they say without the carve-out.
6. Section 277(1)(a) lists four kinds of securities; the rendering ends (i) with a semicolon, (ia) with a comma, (ii) with "; or" and (iii) with a semicolon, so only one "or" joins four alternatives. The encoding takes them as alternatives (fork s277-1a).
7. Section 277(1B)(b) and section 280(3) require the same two indications (how the person can obtain a copy; that the person should read it before submitting an application), the first for the offer information statement and the second for a prospectus or profile statement; and section 280(1) is both "Subject to subsection (3)" and, in (3), "does not apply unless", so the exemption is gated twice by the same words.
8. Section 281(2) says an application for review may be made "within 14 days of the revocation"; the keel's convention (P2) for "within N days after X" opens the window the day after X. The encoding lets an application on the day of the revocation itself be in time (fork s281-2).
9. Section 282AA(2) ("must comply with every direction") gives no time limit, and neither do sections 277(5) and (6) ("at the same time as the lodgment", no party named) and 280(2) ("must still be prepared and issued", no party named); their rules or decision functions have no breach by lateness (see "Rules with no breach path").
10. Provisions shown repealed or deleted in this rendering: section 261(2) ("[Deleted by Act 1 of 2005]"), sections 263 and 264 ("[Repealed by Act 16 of 2003]"), section 268(1) to (3) ("[Deleted by Act 34 of 2012]") and section 273(3) ("[Deleted by Act 1 of 2005]"); each has a row in the coverage table.
11. Sections 277(1)(c)(ii) and 277(1AC)(b)(ii) both point to the conditions of subsection (1B), and subsection (1B) names both ("The conditions mentioned in subsections (1)(c)(ii) and (1AC)(b)(ii) are"), so one function answers both and each paragraph takes its answer.
12. Section 276(3) and (4) say the securities or the beneficiaries' rights "must not be transferred" within 6 months unless one of the listed cases holds, and name no party, so they are decision functions (the bar's own question) with no regulative rule.
13. Section 273(8A) and section 277(7) bar advertising and publishing "unless the advertisement or publication complies with such requirements as the Authority may prescribe"; the requirements are outside the text, so the caller says whether they are met, and a bar with no end date stays standing (a trace with no act is RESIDUAL; with the act, BREACH).
14. The seat layer asks section 277(1) only for an offer of securities issued by a listed corporation (sub-paragraph (a)(ii)), and asks sections 272A(1), 272B(1) and 273(1) by their limbs, because the whole conjunction needs thirty or more facts a person can state (see the header of `sfad-seat.l4`).

## What the stable binary does not accept

The stable builds (1.6.110 and 1.6.109) read every file of this part without an error or a warning.
The plan and the brief name constructs the stable binary does not accept or reads differently; this part's files were written to those limits and both builds read them cleanly.
Two of the limits were checked mechanically on 2026-11-19: `grep -n "REFUSE\|TYPICALLY\|SET OF" sfad-*.l4` prints no match, and `BECAUSE` occurs only after `LEST BREACH`.
The others (every `NOT` parenthesised, each `#ASSERT` on one line, no section-level `GIVEN`, no sets) are followed by construction and were not separately grepped.

Two behaviours of the binary shaped the design and are worth knowing:

- A regulative rule whose party and act carry no fields (as here) is traced with `PARTY p DOES act AT n`; a rule with no `WITHIN`, and a `SHANT` with no end date, stays RESIDUAL in a trace with no act, which the tests assert (`-- EXPECT RESIDUAL`).
- `l4 run` exits 0 when an `#ASSERT` fails, so the numbers in "What check.sh prints" are the evidence, not the exit status.

## What check.sh prints

Run on 2026-11-19 from the deposit folder as `L4=<bin>/l4-main-110 L4_MAIN=<bin>/l4-main-109 ./check.sh` (target `main`, so every module is run with both builds and the counts compared):

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
sfad-cases-seat.l4                             0       134       0        0         0 |      0       134       0        0  same
sfad-circumstances.l4                          0         0       0        0         0 |      0         0       0        0  same
sfad-debentures.l4                             0         0       0        0         0 |      0         0       0        0  same
sfad-directions.l4                             0         0       0        0         0 |      0         0       0        0  same
sfad-exemption-summary.l4                      0         0       0        0         0 |      0         0       0        0  same
sfad-investor-exemptions.l4                    0         0       0        0         0 |      0         0       0        0  same
sfad-nocons-small-private.l4                   0         0       0        0         0 |      0         0       0        0  same
sfad-ois-intl-gov-atm.l4                       0         0       0        0         0 |      0         0       0        0  same
sfad-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sfad-tests-circumstances.l4                    0       175       0        0         0 |      0       175       0        0  same
sfad-tests-debentures.l4                       0       302       0        0         0 |      0       302       0        0  same
sfad-tests-directions.l4                       0        29       0        0         0 |      0        29       0        0  same
sfad-tests-exemption-summary.l4                0        12       0        0         0 |      0        12       0        0  same
sfad-tests-investor-exemptions.l4              0       121       0        0         0 |      0       121       0        0  same
sfad-tests-nocons-small-private.l4             0       193       0        0         0 |      0       193       0        0  same
sfad-tests-ois-intl-gov-atm.l4                 0       179       0        0         0 |      0       179       0        0  same
TOTAL (28 modules)                             0      1145       0        0           |      0      1145       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

Sites of this part changed under it (2026S1bC), both from `NOTHING` to `JUST FALSE` for the failed gate of a public body's power: s 282AA(1), `s 282AA(1) the Authority may issue the direction` (fork s282AA-1, `sfad-directions.l4:73`; the other branch, where no paragraph holds, stays `NOTHING`); and s 281(1), `s 281(1) the Authority may revoke an exemption under this Subdivision` (fork s281-1, `sfad-ois-intl-gov-atm.l4:817`). The other ten sites of kind (ii) keep `JUST FALSE`.
