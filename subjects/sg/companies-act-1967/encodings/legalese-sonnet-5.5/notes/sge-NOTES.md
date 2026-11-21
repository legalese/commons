# NOTES: Companies Act 1967 (Singapore), Part 10A, Transfer of Registration, ss 355 to 364A (agent `sge`)

## Edition encoded

This encodes the Companies Act 1967, 2020 Revised Edition, as the Singapore Statutes Online informal consolidation "version in force from 6/5/2026 to 20/10/2026", retrieved 2026-10-09, carrying the amendments up to Act 24 of 2025.
A later consolidation may exist and was not read.
The encoding is of that text only, lines 23148 to 23607 of `inputs/CoA1967.txt`, which is a PDF turned into plain text.
It is a rendering for study, not the official text, and nothing here is "verified against the official text".
Nothing here is endorsed, checked or associated with the Singapore Government or the Attorney-General's Chambers.
Line numbers in this file are lines of `CoA1967.txt` as it is.

## What the Part does, in one paragraph

Part 10A lets a body corporate incorporated outside Singapore (a "foreign corporate entity") be registered as a company limited by shares by transfer, keeping its identity.
It reserves a name (s 357), applies (s 358), is registered, with a notice of transfer and a certificate (s 359), or is refused (s 360), becomes a company from the date in the notice (s 361), must show within 60 days that it has been deregistered abroad or risk revocation (ss 359(6), 362), must register its pre-existing charges within 30 days (s 363), and must have share and debenture certificates ready within 60 days (s 364).
s 364A hands the detail to regulations.

## Seat

The seat is an individual who is, or is about to become, a director, company secretary or member of a company, or who deals with one.
Here that is the director of the foreign corporate entity that wants to be registered in Singapore (before registration), and a director, secretary or member of the company it becomes (after registration), or a person who deals with that company: a holder of shares, debentures or a share warrant, or a person interested in a charge.
Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.
There is no seat for the Registrar, the Minister or the Court: their powers appear in the seat layer only as what they mean to the person asking (for example "may the Registrar require me as applicant to furnish further information").
The seat layer is `sge-seat.l4` (68 questions, each with `@export` and `@desc`, each named "Under section N, ...") and `sge-cases-seat.l4` (161 assertions).

## Files

All files are in this folder and have ASCII names beginning `sge-`.

| layer | file | what it holds |
| --- | --- | --- |
| 1 | `sge-p10a-355-356.l4`, `sge-tests-355-356.l4` | scope (s 355) and the five definitions of s 356 |
| 1 | `sge-p10a-357-358.l4`, `sge-tests-357-358.l4` | name reservation (s 357), application and its contents (s 358) |
| 1 | `sge-p10a-359.l4`, `sge-tests-359.l4` | registration, conditions, notice, certificate, evidence, deregistration abroad, extension, waiver, appeal |
| 1 | `sge-p10a-360.l4`, `sge-tests-360.l4` | when registration must be refused, and the appeal |
| 1 | `sge-p10a-361.l4`, `sge-tests-361.l4` | effect of registration |
| 1 | `sge-p10a-362.l4`, `sge-tests-362.l4` | revocation |
| 1 | `sge-p10a-363.l4`, `sge-tests-363.l4` | pre-existing charges |
| 1 | `sge-p10a-364.l4`, `sge-tests-364.l4` | certificates, share warrants, the Court's order |
| 2 | `sge-seat.l4`, `sge-cases-seat.l4` | the seat questions and their cases |
| - | `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md` | this file, the working log, the one core item |

The keel's `sg-*.l4` files and `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` are the supplied read-only copies and were not changed.
Layer-1 quotation lines (`-- src:N | text`) were produced by `srcrefs.py quote`, not typed, and `srcrefs.py check --refs` and `--strict` report 0 problems on every `sge-` file.

## Coverage (sge)

One row per unit of lines 23148 to 23607: the Part heading, each section with its marginal heading, each subsection, paragraph and sub-paragraph, each defined term, and the closing words of a subsection where they carry a rule of their own.
Page furniture and amendment marks such as `[15/2017]` belong to the row they sit in and are not rows.
A section's marginal heading sits on the line above its number, and belongs to the section's first row.
Dispositions: `encoded` (a rule, definition or table in layer 1 with a test and an `@ref`), `fork` (an encoded row whose reading is a recorded choice, pointing at the fork register entry and at the rule), `inert` (with its reason number).
Where a lead-in has no rule of its own the row says which functions carry it.
The seat column counts the seat questions (`sge-seat.l4`, listed under "Seat layer") that ask the row's provision.
A "-" there means no question asks that row on its own: the row is asked through its section's question (a paragraph or a lead-in), or it is a definition, a power or a heading that no fact a person can state decides.

| lines | provision | disposition | L4 name(s) and module | tests | seat question | fork |
| --- | --- | --- | --- | --- | --- | --- |
| 23148-23151 | Part 10A heading and title ("PART 10A", "TRANSFER OF REGISTRATION") | inert, reason 1 (not operative) | (none)  not operative: a Part heading | none | - | - |
| 23152-23158 | s 355 (with its marginal heading) | fork | `s 355 this Part applies to the body` in `sge-p10a-355-356.l4` | `sge-tests-355-356.l4` | 1 | F-355 |
| 23159-23162 | s 356 opening words ("In this Part, unless the context otherwise requires") | encoded | `s 356 the definition in this section governs the word where it is used` in `sge-p10a-355-356.l4` | `sge-tests-355-356.l4` | - | - |
| 23163-23168 | s 356 "date of registration" | encoded | `s 356 "date of registration" the date of registration of the foreign corporate entity` in `sge-p10a-355-356.l4` | `sge-tests-355-356.l4` | 1 | - |
| 23169-23171 | s 356 "foreign corporate entity" | encoded | `s 356 "foreign corporate entity" the body is a foreign corporate entity` in `sge-p10a-355-356.l4` | `sge-tests-355-356.l4` | 1 | - |
| 23172-23174 | s 356 "notice of transfer of registration" | encoded | `s 356 "notice of transfer of registration" the notice is the notice of transfer of registration` in `sge-p10a-355-356.l4` | `sge-tests-355-356.l4` | - | - |
| 23175-23179 | s 356 "place of incorporation" | encoded | `s 356 "place of incorporation" the place of incorporation of the foreign corporate entity` in `sge-p10a-355-356.l4` | `sge-tests-355-356.l4` | 1 | - |
| 23180-23182 | s 356 "registration" | encoded | `s 356 "registration" the act is registration of the foreign corporate entity` in `sge-p10a-355-356.l4` | `sge-tests-355-356.l4` | - | - |
| 23183-23187 | s 356 "register" and "registered" (construed accordingly) | encoded | `s 356 "register" and "registered" the foreign corporate entity is registered` in `sge-p10a-355-356.l4` | `sge-tests-355-356.l4` | 1 | - |
| 23188-23198 | s 357(1) (with the marginal heading of s 357) | fork | `s 357(1) the foreign corporate entity must apply to reserve the name of the intended company`; `s 357(1) a foreign corporate entity that intends to be registered must apply to reserve the name of the intended company` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | 1 | F-357-1 |
| 23199-23204 | s 357(2) | encoded | `s 357(2) section 27 applies to and in respect of the application` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | 1 | - |
| 23205-23211 | s 357(3) | fork | `s 357(3) the subsection bars the registration of the foreign corporate entity under section 359(1)` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | 1 | F-357-3 |
| 23212-23218 | s 358(1) (with the marginal heading of s 358) | fork | `s 358(1) the foreign corporate entity may apply to the Registrar to be registered as a company limited by shares`; `s 358(1) a foreign corporate entity may apply to the Registrar to be registered` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | 1 | F-358-1 |
| 23219-23220 | s 358(2) lead-in | encoded | `s 358(2) the application meets the requirements of the subsection`; `s 358(2) application` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | 1 | - |
| 23221-23223 | s 358(2)(a) | encoded | `s 358(2)(a) the application is made in the form and manner, and contains the particulars, that are prescribed` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | - | - |
| 23224-23225 | s 358(2)(b) lead-in | encoded | `s 358(2)(b) the application is accompanied as the paragraph requires` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | 1 | - |
| 23226-23230 | s 358(2)(b)(i) | fork | `s 358(2)(b)(i) a certified copy of the instrument constituting or defining the entity's constitution in its place of incorporation accompanies the application` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | - | F-358-2 |
| 23231-23233 | s 358(2)(b)(ii) | encoded | `s 358(2)(b)(ii) the constitution by which the entity proposes to be registered accompanies the application` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | - | - |
| 23234-23235 | s 358(2)(b)(iii) | encoded | `s 358(2)(b)(iii) such other documents as may be prescribed accompany the application` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | - | - |
| 23236-23239 | s 358(2)(b)(iv) | encoded | `s 358(2)(b)(iv) the prescribed fee accompanies the application` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | - | - |
| 23240-23245 | s 358(3) | fork | `s 358(3) the Registrar may require the applicant to furnish further information or documents` in `sge-p10a-357-358.l4` | `sge-tests-357-358.l4` | 1 | F-358-3 |
| 23246-23258 | s 359(1) (with the marginal heading of s 359) | fork | `s 359(1) the Registrar may register the foreign corporate entity as a company limited by shares` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 1 | F-359-1, F-359-8 |
| 23259-23263 | s 359(2) | encoded | `s 359(2) the registration is subject to the condition` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 1 | - |
| 23264-23268 | s 359(3) lead-in | encoded | `s 359(3) the notice of transfer of registration is as the subsection requires`; `s 359(3) upon registration the Registrar must issue a notice of transfer of registration` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 1 | - |
| 23269-23270 | s 359(3)(a) | encoded | `s 359(3)(a) the notice states that the company is registered by way of transfer of registration` in `sge-p10a-359.l4` | `sge-tests-359.l4` | - | - |
| 23271-23272 | s 359(3)(b) | encoded | `s 359(3)(b) the notice states that the company is a company limited by shares` in `sge-p10a-359.l4` | `sge-tests-359.l4` | - | - |
| 23273-23276 | s 359(3)(c) | fork | `s 359(3)(c) the notice states that the company is a private company where that applies` in `sge-p10a-359.l4` | `sge-tests-359.l4` | - | F-359-2 |
| 23277-23281 | s 359(4) | fork | `s 359(4) the Registrar is required to issue a certificate of confirmation of registration`; `s 359(4) the Registrar must issue a certificate of confirmation of registration upon the application of the company` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 1 | F-359-3 |
| 23282-23285 | s 359(5) lead-in (a notice or a certificate "is conclusive evidence") | encoded | `s 359(5)(a) the document is conclusive evidence that the foreign corporate entity is registered under section 359`; `s 359(5)(b) the date of the company's registration that the document conclusively shows` in `sge-p10a-359.l4` the lead-in is carried by the two functions of (a) and (b), whose inputs say whether the document is a notice or a certificate | `sge-tests-359.l4` | - | - |
| 23286-23288 | s 359(5)(a) | encoded | `s 359(5)(a) the document is conclusive evidence that the foreign corporate entity is registered under section 359` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 1 | - |
| 23289-23292 | s 359(5)(b) | encoded | `s 359(5)(b) the date of the company's registration that the document conclusively shows` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 1 | - |
| 23293-23301 | s 359(6) | fork | `s 359(6) the last day for submitting the document evidencing deregistration`; `s 359(6) the day is within the time allowed for submitting the document`; `s 359(6) the foreign corporate entity has complied with the duty to submit the document evidencing deregistration`; `s 359(6) the foreign corporate entity registered under this section must submit the document evidencing deregistration` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 2 | F-359-4 |
| 23302-23311 | s 359(7) | fork | `s 359(7) the Registrar may extend the 60-day period` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 1 | F-359-5 |
| 23312-23317 | s 359(8) | fork | `s 359(8) the Registrar may waive or modify the condition` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 1 | F-359-6 |
| 23318-23319 | s 359(9) lead-in, with the closing words (23329-23331: "may within 30 days ... appeal to the Minister whose decision is final") | fork | `s 359(9) the person aggrieved may appeal to the Minister`; `s 359(9) the Minister's decision on the appeal is final`; `s 359(9) a person aggrieved may appeal to the Minister within 30 days` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 2 | F-359-7 |
| 23320-23322 | s 359(9)(a) | encoded | `s 359(9)(a) the refusal of the Registrar to register a foreign corporate entity under subsection (1)` in `sge-p10a-359.l4` | `sge-tests-359.l4` | - | - |
| 23323-23325 | s 359(9)(b) | encoded | `s 359(9)(b) a condition of registration imposed by the Registrar under subsection (2)` in `sge-p10a-359.l4` | `sge-tests-359.l4` | - | - |
| 23326-23328 | s 359(9)(c) | encoded | `s 359(9)(c) the modification of a condition by the Registrar under subsection (8)` in `sge-p10a-359.l4` | `sge-tests-359.l4` | - | - |
| 23329-23334 | s 359(9) closing words | encoded | `s 359(9) the person aggrieved may appeal to the Minister`; `s 359(9) a person aggrieved may appeal to the Minister within 30 days` in `sge-p10a-359.l4` | `sge-tests-359.l4` | 2 | - |
| 23335-23343 | s 360(1) (with the marginal heading of s 360) | fork | `s 360(1) the Registrar must refuse to register the foreign corporate entity`; `s 360(1) the Registrar must refuse to register a foreign corporate entity if not satisfied that the requirements have been met` in `sge-p10a-360.l4` | `sge-tests-360.l4` | 1 | F-360-1 |
| 23344-23346 | s 360(2) lead-in | fork | `s 360(2) the Registrar must refuse to register the foreign corporate entity on a ground in the subsection`; `s 360(2) the Registrar must refuse to register a foreign corporate entity if satisfied of a ground in the subsection` in `sge-p10a-360.l4` | `sge-tests-360.l4` | 1 | F-360-2 |
| 23347-23350 | s 360(2)(a) | encoded | `s 360(2)(a) the Registrar is satisfied that the intended company is likely to be used for a purpose that the paragraph names` in `sge-p10a-360.l4` | `sge-tests-360.l4` | - | - |
| 23351-23355 | s 360(2)(b) | encoded | `s 360(2)(b) the Registrar is satisfied that it would be contrary to national security or interest for the intended company to be registered` in `sge-p10a-360.l4` | `sge-tests-360.l4` | - | - |
| 23356-23364 | s 360(3) | fork | `s 360(3) the person aggrieved may appeal to the Minister`; `s 360(3) the Minister's decision on the appeal is final`; `s 360(3) a person aggrieved may appeal to the Minister within 30 days` in `sge-p10a-360.l4` | `sge-tests-360.l4` | 2 | F-360-3 |
| 23365-23369 | s 361(1) lead-in (with the marginal heading of s 361) | encoded | `s 361(1)(a) the provision of the Act applies to the foreign corporate entity` in `sge-p10a-361.l4` the lead-in ("Starting on the date of registration specified in the notice of transfer of registration") is the date gate in the functions of (a) and (b) | `sge-tests-361.l4` | - | - |
| 23370-23375 | s 361(1)(a) | encoded | `s 361(1)(a) the foreign corporate entity is a company as defined in section 4(1)`; `s 361(1)(a) how a provision of the Act applies to the foreign corporate entity` in `sge-p10a-361.l4` | `sge-tests-361.l4` | 2 | - |
| 23376-23382 | s 361(1)(b) | fork | `s 361(1)(b) the foreign corporate entity has ceased to be registered as a foreign company under Division 2 of Part 11` in `sge-p10a-361.l4` | `sge-tests-361.l4` | 1 | F-361-1 |
| 23383-23385 | s 361(2) lead-in | encoded | `s 361(2)(a) the registration of the foreign corporate entity creates a new legal entity` in `sge-p10a-361.l4` the lead-in ("To avoid doubt, the registration ... does not —") is the flat negative in each of (a) to (d) | `sge-tests-361.l4` | - | - |
| 23386-23387 | s 361(2)(a) | encoded | `s 361(2)(a) the registration of the foreign corporate entity creates a new legal entity` in `sge-p10a-361.l4` | `sge-tests-361.l4` | 1 | - |
| 23388-23391 | s 361(2)(b) | encoded | `s 361(2)(b) the registration of the foreign corporate entity prejudices or affects the thing` in `sge-p10a-361.l4` | `sge-tests-361.l4` | 1 | - |
| 23392-23394 | s 361(2)(c) | encoded | `s 361(2)(c) the registration of the foreign corporate entity affects the thing` in `sge-p10a-361.l4` | `sge-tests-361.l4` | 1 | - |
| 23395-23397 | s 361(2)(d) | encoded | `s 361(2)(d) the registration of the foreign corporate entity renders defective legal proceedings by or against the foreign corporate entity` in `sge-p10a-361.l4` | `sge-tests-361.l4` | 1 | - |
| 23398-23404 | s 361(2) closing words (legal proceedings may be continued or commenced) | fork | `s 361(2) the legal proceedings may be continued or commenced by or against the company after the registration` in `sge-p10a-361.l4` | `sge-tests-361.l4` | 1 | F-361-2 |
| 23405-23414 | s 362(1) (with the marginal heading of s 362) | fork | `s 362(1) the Registrar may by order revoke the registration of the company` in `sge-p10a-362.l4` | `sge-tests-362.l4` | 1 | F-362-1 |
| 23415-23416 | s 362(2) lead-in | encoded | `s 362(2) the Registrar has done what the subsection requires before making an order of revocation`; `s 362(2) before making an order of revocation the Registrar must give notice and consider representations` in `sge-p10a-362.l4` | `sge-tests-362.l4` | 1 | - |
| 23417-23419 | s 362(2)(a) | encoded | `s 362(2)(a) the Registrar has given the company written notice of the intention to revoke the registration` in `sge-p10a-362.l4` | `sge-tests-362.l4` | - | - |
| 23420-23423 | s 362(2)(b) | encoded | `s 362(2)(b) the notice specifies a period of at least 30 days for written representations`; `s 362(2)(b) the company may make written representations within the period the notice specifies` in `sge-p10a-362.l4` | `sge-tests-362.l4` | - | - |
| 23424-23429 | s 362(2)(c) | fork | `s 362(2)(c) the Registrar has considered the company's written representations` in `sge-p10a-362.l4` | `sge-tests-362.l4` | - | F-362-2 |
| 23430-23436 | s 362(3) | fork | `s 362(3) the Registrar may order that the registration of the company be revoked` in `sge-p10a-362.l4` | `sge-tests-362.l4` | 1 | F-362-3, F-362-4 |
| 23437-23438 | s 362(4) lead-in | encoded | `s 362(4) the Registrar has published and served the notice of the order of revocation`; `s 362(4) the Registrar must publish the notice of the order of revocation and serve a copy on the company` in `sge-p10a-362.l4` | `sge-tests-362.l4` | 1 | - |
| 23439-23441 | s 362(4)(a) | encoded | `s 362(4)(a) the Registrar has caused a notice of the order of revocation to be published in the Gazette` in `sge-p10a-362.l4` | `sge-tests-362.l4` | - | - |
| 23442-23446 | s 362(4)(b) | encoded | `s 362(4)(b) the Registrar has served a copy of the notice of the order of revocation on the company` in `sge-p10a-362.l4` | `sge-tests-362.l4` | - | - |
| 23447-23453 | s 362(5) | fork | `s 362(5) the order of revocation has taken effect`; `s 362(5) the company has ceased to be a company as defined in section 4(1)`; `s 362(5) the provisions of this Act have ceased to apply to the company` in `sge-p10a-362.l4` | `sge-tests-362.l4` | 3 | F-362-5 |
| 23454-23457 | s 362(6) | encoded | `s 362(6) the order of revocation is final` in `sge-p10a-362.l4` | `sge-tests-362.l4` | 1 | - |
| 23458-23463 | s 362(7) | encoded | `s 362(7) the liability of the person continues despite the order of revocation` in `sge-p10a-362.l4` | `sge-tests-362.l4` | 1 | - |
| 23464-23465 | s 362(8) lead-in | encoded | `s 362(8) section 362 prejudices the enforcement of the right or claim` in `sge-p10a-362.l4` | `sge-tests-362.l4` | 1 | - |
| 23466-23471 | s 362(8)(a) | encoded | `s 362(8)(a) the enforcement by a person of a right or claim against the company` in `sge-p10a-362.l4` | `sge-tests-362.l4` | - | - |
| 23472-23476 | s 362(8)(b) | encoded | `s 362(8)(b) the enforcement by the company of a right or claim against a person` in `sge-p10a-362.l4` | `sge-tests-362.l4` | - | - |
| 23477-23489 | s 363(1) (with the marginal heading of s 363) | fork | `s 363(1) a statement of the charge must be lodged with the Registrar`; `s 363(1) the last day for lodging the statement of the charge`; `s 363(1) the statement of the charge has been lodged as the subsection requires`; `s 363(1) the company must lodge a statement of a pre-existing charge within 30 days after the date of registration` in `sge-p10a-363.l4` | `sge-tests-363.l4` | 3 | F-363-1, F-363-2 |
| 23490-23495 | s 363(2) | fork | `s 363(2) the person may lodge the documents and particulars required to be lodged` in `sge-p10a-363.l4` | `sge-tests-363.l4` | 1 | F-363-3 |
| 23496-23502 | s 363(3) | fork | `s 363(3) the person is entitled to recover the fees from the company`; `s 363(3) the amount of fees the person is entitled to recover from the company` in `sge-p10a-363.l4` | `sge-tests-363.l4` | 2 | F-363-4 |
| 23503-23509 | s 363(4) | fork | `s 363(4) the person is guilty of an offence`; `s 363(4) the most the person may be sentenced to on conviction` in `sge-p10a-363.l4` | `sge-tests-363.l4` | 2 | F-363-5 |
| 23510-23515 | s 363(5) | encoded | `s 363(5) the failure to comply with section 363(1) affects the continuity of status, operation or effect of the thing of the charge` in `sge-p10a-363.l4` | `sge-tests-363.l4` | 1 | - |
| 23516-23517 | s 363(6) lead-in | fork | `s 363(6) the Court may order that the time for registration be extended or that the omission or mis-statement be rectified` in `sge-p10a-363.l4` | `sge-tests-363.l4` | 2 | F-363-7 |
| 23518-23528 | s 363(6)(a) | encoded | `s 363(6) the Court may order that the time for registration be extended or that the omission or mis-statement be rectified` in `sge-p10a-363.l4` encoded as the first two grounds of the s 363(6) function | `sge-tests-363.l4` | - | - |
| 23529-23530 | s 363(6)(b) | encoded | `s 363(6) the Court may order that the time for registration be extended or that the omission or mis-statement be rectified` in `sge-p10a-363.l4` encoded as the third ground of the s 363(6) function | `sge-tests-363.l4` | - | - |
| 23531-23539 | s 363(6) closing words (the application, the terms and conditions, the order) | fork | `s 363(6) the Court may impose the term or condition on its order` in `sge-p10a-363.l4` | `sge-tests-363.l4` | 2 | F-363-6 |
| 23540-23545 | s 363(7) | encoded | `s 363(7) the section applies to the charge as if it were a charge to which Division 8 of Part 4 applied` in `sge-p10a-363.l4` | `sge-tests-363.l4` | 1 | - |
| 23546-23555 | s 364(1) (with the marginal heading of s 364) | fork | `s 364(1) the company must complete and have ready for delivery appropriate certificates in respect of the person`; `s 364(1) the last day for completing and having ready for delivery the certificates`; `s 364(1) the company has completed and has ready for delivery the certificates within 60 days after the date of registration`; `s 364(1) the company must complete and have ready for delivery the certificates within 60 days after the date of registration` in `sge-p10a-364.l4` | `sge-tests-364.l4` | 3 | F-364-1 |
| 23556-23562 | s 364(2) | fork | `s 364(2) the prior certificate has ceased to be operative`; `s 364(2) the prior certificate has ceased to have any validity for the purposes of this Act` in `sge-p10a-364.l4` | `sge-tests-364.l4` | 2 | F-364-2 |
| 23563-23570 | s 364(3) | fork | `s 364(3) the share warrant is void` in `sge-p10a-364.l4` | `sge-tests-364.l4` | 1 | F-364-3 |
| 23571-23587 | s 364(4) | fork | `s 364(4) the company has failed to make good the default within 10 days after the service of the notice`; `s 364(4) the Court may make an order directing the company and any officer of the company to make good the default`; `s 364(4) the order may direct the person to make good the default`; `s 364(4) the order may provide that the costs of and incidental to the application are to be borne by the person`; `s 364(4) the company must make good the default within the time the order specifies`; `s 364(4) the officer must make good the default within the time the order specifies` in `sge-p10a-364.l4` | `sge-tests-364.l4` | 4 | F-364-4, F-364-5, F-364-6 |
| 23588-23593 | s 364A lead-in (with the marginal heading of s 364A) | inert, reason 2 (machinery) | (none)  machinery: the Minister's power to make regulations under section 411; what the regulations may do is taken as an input where a rule needs it (seams, NOTES.md) | none | - | - |
| 23594-23597 | s 364A(a) | inert, reason 2 (machinery) | (none)  machinery: regulation-making power; the minimum and other requirements are the input `the Registrar is satisfied that the minimum requirements prescribed for registration have been met` of s 360(1) | none | - | - |
| 23598-23601 | s 364A(b) | inert, reason 2 (machinery) | (none)  machinery: regulation-making power to waive a requirement of the Part; not asked as a question, because no fact the person can state decides it | none | - | - |
| 23602-23607 | s 364A(c) | inert, reason 2 (machinery) | (none)  machinery: regulation-making power to adapt, modify or exclude provisions; its effect enters as the input `the regulations specify an adaptation, exception or modification of the provision for the entity` of s 361(1)(a) | none | - | - |

## Fork register (sge)

Every site where the text can be read two ways with different outcomes.
"Answer taken" is what the encoding returns; "other reading" is the one it did not take.
Rulings cited are in `inputs/ENCODING-GUIDE.md` section 5 (the periods ruling of 2026-11-05 items (a), (b), (c); the delegated-definitions ruling of 2026-11-05 item (c), which counts "when", "upon" and "whenever" as "where"; the case-by-case ruling of 2026-11-05; the grant ruling of 2026-11-12 and its three limits; N2 of 2026-11-04).
The quoted ruling words are the Guide's: (c) "a scope limit with no 'only' ... outside the scope the answer is `NOTHING`"; (b) "a 'where ...' condition: when it fails the answer is `JUST FALSE`"; (a) "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"; grant limit 1: answer `NOTHING` "only for a function named for a grant or a power ... whose `if` gate failed".

| id | provision and function | answer taken | other reading | what licenses the answer |
| --- | --- | --- | --- | --- |
| F-355 | s 355, `s 355 this Part applies to the body` | `JUST TRUE` for a foreign corporate entity that intends to be registered; `NOTHING` for any other body | `JUST FALSE` for any other body | periods ruling (c): "This Part applies to a foreign corporate entity which intends to be registered" is a scope limit with no "only" |
| F-357-1 | s 357(1), `s 357(1) the foreign corporate entity must apply to reserve the name of the intended company` and its rule | `JUST TRUE` for an entity that intends to be registered, `NOTHING` otherwise; the rule is a bare "must" with no time and no consequence | `JUST FALSE` for an entity with no such intention | periods ruling (c): the relative clause names the class that is bound |
| F-357-3 | s 357(3), `s 357(3) the subsection bars the registration of the foreign corporate entity under section 359(1)` | `JUST TRUE` (bars) when the name is not reserved; `JUST FALSE` (does not bar) when it is, because the "unless" is met | `NOTHING` when the name is reserved, the bar being lifted and nothing said; either way JUST FALSE is NOT a grant to register: s 359(1) and s 360 decide that | the text's own "unless"; case-by-case ruling of 2026-11-05 ("an 'unless' or 'except' once it is met") |
| F-358-1 | s 358(1), `s 358(1) the foreign corporate entity may apply to the Registrar to be registered as a company limited by shares` | `NOTHING` for a body that is not a foreign corporate entity | `JUST FALSE` | grant ruling of 2026-11-12, limit 1 |
| F-358-2 | s 358(2)(b)(i), the certified copy "(if any)" | `JUST TRUE` where the entity has no such instrument (no copy is owed) | `JUST FALSE` (a certified copy is missing); or `NOTHING` | the words "(if any)" in the text |
| F-358-3 | s 358(3), `s 358(3) the Registrar may require the applicant to furnish further information or documents` | `NOTHING` for a person who is not an applicant | `JUST FALSE` | grant ruling, limit 1 |
| F-359-1 | s 359(1), the Registrar "may, if the Registrar thinks fit, register" | `NOTHING` when the Registrar does not think fit; `JUST FALSE` where s 360 requires refusal ("Subject to section 360") | `JUST FALSE` where the Registrar does not think fit | grant ruling, limit 1, for the "if" gate; the text's own "Subject to section 360" for the bar |
| F-359-8 | s 359(1), "upon compliance by the foreign corporate entity with section 358" | `JUST FALSE` when s 358 has not been complied with | `NOTHING` | periods ruling (b), and the delegated-definitions ruling (c) ("upon" counts as "where"); a "may" with a "where/upon" gate is listed for a lawyer under grant limit 3 (split site (ii)) |
| F-359-2 | s 359(3)(c), "where applicable, a private company" | `NOTHING` for a company that is not private (the text does not say when a transferred company is private); `JUST TRUE` or `JUST FALSE` by what the notice states for one that is | `JUST FALSE` for a company that is not private (ruling (b): "where" fails); or `JUST TRUE` | undefined term: s 4(1) "private company" (line 1622) has no limb for a company registered by transfer (finding 4) |
| F-359-3 | s 359(4), a certificate "must be issued by the Registrar upon the application of the company" | `JUST FALSE` before the company applies; `NOTHING` for an entity not yet registered | `NOTHING` before the application | "upon" counts as "where": ruling (b), (c); the duty is the Registrar's |
| F-359-4 | s 359(6), "or such further period as may be extended under subsection (7)" | the extension is given as the last day of the extended period, because the text does not say how an extension is expressed | a number of further days | the text is silent on the form of the extension |
| F-359-5 | s 359(7), "The Registrar may, on the application of the foreign corporate entity ..., extend" | `JUST FALSE` when no application has been made; `NOTHING` for an entity not registered | `NOTHING` when no application | "on the application of" is the short form of "upon the application of": ruling (b), (c); split site (ii) |
| F-359-6 | s 359(8), the Registrar "may ... waive or modify" a condition | `NOTHING` for a condition not imposed under s 359(2) | `JUST FALSE` | grant ruling, limit 1 |
| F-359-7 | s 359(9), "Any person aggrieved by (a), (b) or (c) ... may within 30 days ... appeal to the Minister whose decision is final" | `JUST TRUE` within the 30 days; `JUST FALSE` after them; `NOTHING` for a person not aggrieved or a decision not named | `JUST FALSE` for the last two | periods ruling (a) for the stated period; grant limit 1 for the class |
| F-360-1 | s 360(1), the Registrar "must refuse ... if the Registrar is not satisfied" | `JUST FALSE` when the Registrar is satisfied on both counts (the duty to refuse does not arise) | `NOTHING` | reading (a) of the rule of 2026-10-29 (a failed "if" counts as the text's no); a marginal reading for a lawyer |
| F-360-2 | s 360(2), refuse "if the Registrar is satisfied that (a) or (b)" | `JUST FALSE` when neither ground is made out | `NOTHING` | the same reading (a) |
| F-360-3 | s 360(3), appeal against a decision "under subsection (1) or (2)" | as F-359-7: `JUST FALSE` out of time; `NOTHING` for a person not aggrieved or another decision | `JUST FALSE` for those | periods ruling (a); grant limit 1 |
| F-361-1 | s 361(1)(b), "if the foreign corporate entity was registered as a foreign company under Division 2 of Part 11 immediately before that date, ceases to be so registered" | `JUST FALSE` when it was not so registered, or before the date | `NOTHING` | reading (a) of the rule of 2026-10-29; marginal reading for a lawyer |
| F-361-2 | s 361(2), the closing words: proceedings "that could have been continued or commenced ... may be continued or commenced" | `NOTHING` for proceedings that could not have been | `JUST FALSE` | grant ruling, limit 1 |
| F-362-1 | s 362(1), the Registrar "may by order revoke the registration of a company if the company fails to comply with section 359(6)" | `NOTHING` when the company has not failed | `JUST FALSE` | grant ruling, limit 1 |
| F-362-2 | s 362(2)(c), "consider the company's written representations (if any)" | `JUST TRUE` when none was received in time | `NOTHING` | the words "(if any)" |
| F-362-3 | s 362(3), "the time mentioned in the notice" | counted from the day the notice is given; the order may be made on a day after the last day of the period | counted from the day after, or from receipt | the text does not say when the time starts |
| F-362-4 | s 362(3), "At the expiration of the time" and "unless cause to the contrary is previously shown" | `JUST FALSE` when the time has not expired and `JUST FALSE` when cause was shown | `NOTHING` for each | periods ruling (b), (c) for the time; the text's own "unless" for the cause; split site (ii) |
| F-362-5 | s 362(5), "Upon publication of the notice ... in the Gazette" (three effects) | `JUST FALSE` before publication, `JUST TRUE` from the day of publication | `NOTHING` before | "upon" counts as "where": ruling (b), (c) |
| F-363-1 | s 363(1), "If, before the registration ..., there are any charges which would have been required to be registered under Division 8 of Part 4" | `JUST FALSE` when the charge did not exist before, or would not have needed registering | `NOTHING` | reading (a) of the rule of 2026-10-29; marginal reading for a lawyer |
| F-363-2 | s 363(1), who must lodge | the company: the text says "there must be lodged" and names no actor, while subsection (4) puts the default on the company and its officers in default | no party named | s 363(4) and the heading "Duty of company to register pre-existing charges" |
| F-363-3 | s 363(2), "may be lodged by the company concerned or by any person interested" | `NOTHING` for anyone else | `JUST FALSE` | grant ruling, limit 1 |
| F-363-4 | s 363(3), "Where registration ... is effected by some person other than the company concerned, that person is entitled to recover" | `JUST FALSE` when the registration was not effected by another person; `NOTHING` for the amount | `NOTHING` | periods ruling (b) for the "Where"; an "entitled"-named function, left as the Guide's rulings give it and listed for a lawyer (grant limit 3) |
| F-363-5 | s 363(4), "If default is made ..., the company and every officer of the company who is in default shall each be guilty of an offence" | `JUST FALSE` when an element is unmet (the provision's own question); the sentence function answers `NOTHING` for a person not guilty | `NOTHING` for the guilt function | split site (i); N2 (a flat negative counts as no); the "if" is read as the text's no, reading (a) |
| F-363-6 | s 363(6), "on such terms and conditions as seem to the Court just and expedient (including ...)" | `NOTHING` for a term that is neither the one named nor one that seems just and expedient to the Court | `JUST FALSE` | grant ruling, limit 1 |
| F-363-7 | s 363(6), "The Court, on being satisfied ..., may on the application of the company or any person interested ... order" | `JUST FALSE` when the Court is not satisfied of any ground, or when neither the company nor a person interested has applied | `NOTHING` for each | periods ruling (b), (c) ("on being satisfied", "on the application of" read as "upon"); split site (ii) |
| F-364-1 | s 364(1), the persons covered | `NOTHING` for a person who was not a registered holder of existing shares or debentures at the date of registration | `JUST FALSE` | periods ruling (c) |
| F-364-2 | s 364(2), "Upon the delivery of the certificates" | `JUST FALSE` before delivery; `NOTHING` for a certificate for shares or debentures whose new certificates are not in question | `NOTHING` before delivery | "upon" counts as "where": ruling (b), (c) |
| F-364-3 | s 364(3), a bearer share warrant issued before the date of registration "is void" | `JUST TRUE` for such a warrant; `NOTHING` for any other document | `JUST FALSE` for any other document | periods ruling (c): a flat statement about a named class, no "only" |
| F-364-4 | s 364(4), "If any company on which a notice has been served ... fails to make good the default within 10 days ..., the Court may, on the application of the person entitled ..., make an order" | `JUST FALSE` when there is no failure, and `JUST FALSE` when the person entitled has not applied; the failure itself is `NOTHING` while the 10 days still run | `NOTHING` for each gate | ruling (b), (c); split site (ii); the text does not say who serves the notice (an input) |
| F-364-5 | s 364(4), the order directs "the company and any officer of the company" | `JUST TRUE` for the company and for any officer (in default or not); `NOTHING` for any other person | `JUST FALSE` for any other person | grant ruling, limit 1 |
| F-364-6 | s 364(4), costs "borne by the company or by any officer of the company in default" | "in default" is read as qualifying the officer: `JUST TRUE` for the company and an officer in default; `NOTHING` for an officer not in default | "in default" qualifies both, so the company is within the costs only if in default | the grammar of the phrase; marginal reading for a lawyer |

### Rulings relied on, word for word

Copied from the brief (the text of `inputs/ENCODING-GUIDE.md` section 5), so that a reviewer sees the wording each fork line above relies on.
Only the rulings this part uses are copied: E1 (per-section answers), N2 (flat negatives), the periods ruling, the delegated-definitions ruling (item (c), "upon" counts as "where"), the case-by-case ruling, and the grant ruling with its three limits.

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

## Jural relations (sge)

One row per provision of the range that creates a relation, and `none` for a provision that creates none.
"Holder" is the party with the right (claim), privilege (liberty), power or immunity; "bearer" is the party with the correlative duty, no-right, liability or disability.
Where the text names no one to whom a duty is owed, the row says so rather than invent one.

| provision | holder | bearer | kind | L4 rule |
| --- | --- | --- | --- | --- |
| Part 10A heading | none | none | not operative | - |
| s 355 | none | none | scope | `s 355 this Part applies to the body` |
| s 356 (opening words, five definitions) | none | none | definitions | the six `s 356` functions |
| s 357(1) | no one named (the Registrar receives the application) | the foreign corporate entity that intends to be registered (duty to apply to reserve the name) | claim / duty | `s 357(1) a foreign corporate entity that intends to be registered must apply to reserve the name of the intended company` |
| s 357(2) | none | none | applies s 27 | `s 357(2) section 27 applies ...` |
| s 357(3) | the foreign corporate entity (no claim to registration without a reserved name, a no-right of the entity) | the Registrar (disability: may not register without a reserved name) | disability / no-right | `s 357(3) the subsection bars ...` |
| s 358(1) | the foreign corporate entity (liberty to apply) | the Registrar (no-right to stop an application) | privilege / no-right | `s 358(1) a foreign corporate entity may apply to the Registrar to be registered` |
| s 358(2) | none | none | content requirements of the application | the `s 358(2)` functions |
| s 358(3) | the Registrar (power to require more) | the applicant (liability to furnish it) | power / liability | `s 358(3) the Registrar may require ...` |
| s 359(1) | the Registrar (power to register, subject to s 360) | the foreign corporate entity (liability to be registered) | power / liability | `s 359(1) the Registrar may register ...` |
| s 359(2) | the Registrar (power to impose a condition) | the registered company (liability to the condition) | power / liability | `s 359(2) the registration is subject to the condition` |
| s 359(3) | the company (claim to a notice in the form with the three statements) | the Registrar (duty to issue it) | claim / duty | `s 359(3) upon registration the Registrar must issue a notice of transfer of registration` |
| s 359(4) | the company (claim to a certificate of confirmation, upon its application) | the Registrar (duty to issue it) | claim / duty | `s 359(4) the Registrar must issue a certificate of confirmation of registration upon the application of the company` |
| s 359(5) | the company (immunity: the notice or certificate is conclusive) | any person (disability to prove otherwise) | immunity / disability | `s 359(5)(a)`, `s 359(5)(b)` |
| s 359(6) | the Registrar (claim to the evidence of deregistration abroad) | the registered company (duty to submit it within the time) | claim / duty | `s 359(6) the foreign corporate entity registered under this section must submit ...` |
| s 359(7) | the Registrar (power to extend); the entity (liberty to apply) | the entity (liability to the Registrar's decision) | power / liability | `s 359(7) the Registrar may extend the 60-day period` |
| s 359(8) | the Registrar (power to waive or modify) | the company (liability to the change) | power / liability | `s 359(8) the Registrar may waive or modify the condition` |
| s 359(9) | the person aggrieved (power to appeal to the Minister within 30 days); the Minister's decision is final | the Minister (liability to the appeal); the person (disability to appeal further) | power / liability; immunity / disability | `s 359(9) the person aggrieved may appeal to the Minister`, `... decision ... is final`, the rule |
| s 360(1), (2) | no one named (the duty is the Registrar's; the applicant is under the liability of being refused) | the Registrar (duty to refuse) | duty, no named claimant | `s 360(1) ...`, `s 360(2) ...` |
| s 360(3) | the person aggrieved (power to appeal) | the Minister (liability); the person (disability to appeal further) | power / liability; immunity / disability | `s 360(3) ...` |
| s 361(1) | none | none | a status rule (deeming; ceasing to be a registered foreign company) | `s 361(1)(a) ...`, `s 361(1)(b) ...` |
| s 361(2) | the entity and those dealing with it (immunity from a loss of identity, property, rights, obligations or sound proceedings by reason of registration) | any person (disability to treat the registration as a change) | immunity / disability | `s 361(2)(a)` to `(d)`, `s 361(2) the legal proceedings may be continued ...` |
| s 362(1) | the Registrar (power to revoke on failure under s 359(6)) | the company (liability to revocation) | power / liability | `s 362(1) ...` |
| s 362(2) | the company (claim to written notice, at least 30 days, and consideration of its representations); the company (liberty to make representations) | the Registrar (duty); no one (no-right to refuse to receive them) | claim / duty; privilege / no-right | `s 362(2) ...`, `s 362(2)(b) the company may make written representations ...` |
| s 362(3) | the Registrar (power to order, at the expiration of the time, unless cause is shown) | the company (liability to the order) | power / liability | `s 362(3) ...` |
| s 362(4) | the company (claim to publication and service of the notice) | the Registrar (duty) | claim / duty | `s 362(4) ...` |
| s 362(5) | none | none | effect (takes effect on publication) | `s 362(5) ...` (three functions) |
| s 362(6) | the Registrar (immunity: the order is final) | the company (disability to contest it) | immunity / disability | `s 362(6) the order of revocation is final` |
| s 362(7) | whoever holds the claim in respect of the company (not named) | every officer and member (duty: the liability continues) | claim / duty | `s 362(7) ...` |
| s 362(8) | the holder of a right or claim (immunity: s 362 does not prejudice its enforcement) | any person (disability) | immunity / disability | `s 362(8) ...` |
| s 363(1) | the Registrar (claim to the statement); persons interested in the charge | the company (duty to lodge within 30 days) | claim / duty | `s 363(1) the company must lodge ...` |
| s 363(2) | the company and any person interested (liberty to lodge) | no one (no-right) | privilege / no-right | `s 363(2) ...` |
| s 363(3) | the person who effected the registration (claim for the fees) | the company (duty to repay) | claim / duty | `s 363(3) ...` |
| s 363(4) | the State (power to prosecute; not named in the text) | the company and every officer in default (liability to a fine up to $1,000 and a default penalty) | power / liability | `s 363(4) ...` (two functions) |
| s 363(5) | the holders of security, right, priority or obligation of the charge (immunity from a failure to lodge) | any person (disability to treat the failure as an effect) | immunity / disability | `s 363(5) ...` |
| s 363(6) | the company or a person interested (liberty to apply); the Court (power to order) | whoever the order binds (liability to the order and its terms) | power / liability | `s 363(6) ...` (two functions) |
| s 363(7) | none | none | applies ss 134, 135, 136, 138 | `s 363(7) ...` |
| s 364(1) | each person registered as a holder of existing shares or debentures (claim to appropriate certificates) | the company (duty, within 60 days) | claim / duty | `s 364(1) ...` (four functions) |
| s 364(2) | none | none | effect (prior certificates cease) | `s 364(2) ...` (two functions) |
| s 364(3) | none | none | voidness of a class of bearer warrant | `s 364(3) the share warrant is void` |
| s 364(4) | the person entitled to have the certificates or debentures delivered (liberty to apply); the Court (power to order) | the company and any officer (liability to the order, costs on the company or an officer in default) | power / liability | `s 364(4) ...` (six functions) |
| s 364A | the Minister (power to make regulations) | those the regulations bind | power / liability | none (inert, reason 2) |

## Marginal readings for a lawyer (sge)

The rule of 2026-10-29 leaves two readings to a lawyer: (a) a failed "if" counts as the text's no, within the provision that holds the "if"; flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
Every branch of this encoding that rests on one of them is listed, with the other reading.

Branches resting on reading (a), where a failed "if" or an unmet element answers `JUST FALSE` (the other reading is `NOTHING` in each):
- F-360-1 and F-360-2, s 360(1) and (2): the duty to refuse does not arise when the Registrar is satisfied on both counts, or of no ground.
- F-361-1, s 361(1)(b): the entity ceases to be a registered foreign company only if it was registered immediately before the date.
- F-363-1, s 363(1): a statement is required only for a charge that existed before registration and would have needed registering under Division 8 of Part 4.
- F-363-5, s 363(4): guilt requires default and the person to be the company or an officer in default.
- The flat negatives of s 361(2)(a) to (d) and s 362(8)(a) and (b) ("does not", "Nothing in this section prejudices") answer `JUST FALSE` under N2; the other reading is that they are statements of effect that decide nothing for a case outside them.
- The "means" definitions of s 356 answer `JUST FALSE` outside the definition; that is the text's own word, not a marginal reading.

Branches resting on reading (b), where a grant or prohibition limited by its own wording answers `NOTHING` when the case falls outside the limit (the other reading is `JUST FALSE` in each):
- F-355 (scope of the Part), F-357-1 (the class bound to reserve a name), F-358-1, F-358-3, F-359-1 (the "if the Registrar thinks fit"), F-359-6, F-359-7 and F-360-3 (the person aggrieved), F-361-2, F-362-1, F-363-3, F-363-6, F-364-1, F-364-3, F-364-5.

Branches the grant ruling of 2026-11-12 (limit 3) lists for a lawyer, left as the Guide's rulings give them:
- "may" functions whose gate is "where", "when" or "upon" (five, all `JUST FALSE`): F-359-8 (s 359(1), "upon compliance"), F-359-5 (s 359(7), "on the application of"), F-362-4 (s 362(3), "at the expiration of the time", "unless"), F-363-7 (s 363(6), "on being satisfied", "on the application of"), F-364-4 (s 364(4), "If ... fails", "on the application of").
- "entitled"-named functions (one): F-363-4, s 363(3), `JUST FALSE` when the "Where" is not met.

Other marginal readings:
- F-364-6: "in default" qualifies the officer, not the company, in the costs words of s 364(4).
- F-359-4 and F-362-3: how an extension is expressed, and when the time of a notice starts; the text is silent and the encoding takes an input or a day.
- F-363-2: the company is the party who must lodge.
- The period counts of ss 359(6), 359(9), 360(3), 363(1), 364(1) and 364(4): "within N days after" excludes day 0 (the keel's `period:` function P2), and a thing done on day 0 itself is not asserted either way in the tests.
- F-359-2: whether a company registered by transfer is a private company (an undefined term, answered `NOTHING`).
- F-358-2 and F-362-2: the words "(if any)" are read as "nothing is owed where there is none".
- F-357-3 and F-362-4: an "unless" that is met is read as the text's no, under the case-by-case ruling of 2026-11-05.

### Reading a result: FALSE and NOTHING (sge)

In this Part, `JUST TRUE` is the text's yes: the Registrar may register, the notice is as required, the company must lodge, the warrant is void.
`JUST FALSE` is the text's no in its own words: a "means" definition outside its terms (s 356), a flat negative ("does not create a new legal entity", "does not prejudice"), an "unless" that is met (s 357(3), s 362(3)), a stated period that has run (30 or 60 days, 10 days, the 30 days to appeal), an "if", "where" or "upon" gate that failed on a bar, a duty or the provision's own question.
`NOTHING` is "the text does not say": a scope limit with no "only" (a body that is not a foreign corporate entity), a grant limited by its own wording (a person who is not an applicant, an officer not named), a term left undefined ("where applicable, a private company"), and a period that has not yet run on a question that is neither met nor missed.
A caller never turns `NOTHING` into `FALSE`.
A `JUST FALSE` on a bar never reads as a grant: `s 357(3)` answering `JUST FALSE` does not say the entity may be registered.
Every branch that answers a no carries `-- FALSE-kind (the text says no in its own words): "..."`, and every "not covered" branch carries `-- NOTHING-kind (why)`, with one of the six reasons the brief allows.

## Seams (sge)

PLAN.md section 4 lists for this part: takes the s 4(1) functions named; "Transfer of registration brings a foreign corporate entity within 'company' by regulation: take that as the input the function asks."
A part cannot import another part, so each fact another provision decides is an input named for the fact and the section it comes from.

| seam | where used | taken as | seen |
| --- | --- | --- | --- |
| s 4(1) "company" (keel function `s 4(1) "company" the body is a company`) | `s 361(1)(a) the foreign corporate entity is a company as defined in section 4(1)`: from the date of registration the entity is deemed one; before it, the keel's answer with both limbs FALSE (the entity is not incorporated under this Act or a corresponding earlier law) | called (the keel's function) | text, lines 23367 to 23375; PLAN section 6 |
| s 4(1) "company", ceasing | `s 362(5) the company has ceased to be a company as defined in section 4(1)` | NOT a call of the keel: the subsection states an effect from the day of publication, so it is encoded as that effect | text, lines 23447 to 23450 |
| s 4(1) "certified" | `s 358(2)(b)(i)`: the copy is certified | called (the keel's function) | text, lines 23224 to 23229 |
| `period:` functions of `sg-periods` | every period in the Part: 30 days (appeal, charges), 60 days (certificates, evidence of deregistration), 10 days (notice served), 30 days (minimum notice) | called | by design |
| s 27 (names of companies; later wave) | `s 357(2)`, `s 357(3)`: whether a name "has been reserved under section 27, as applied by section 357(2)" | input `the name the entity is to be registered under has been reserved` (seat) / `the name that the foreign corporate entity is proposed to be registered under has been reserved under section 27, as applied by section 357(2)` (layer 1) | text; XREFS; line 4678 of s 27 also cites s 357(2) |
| ss 134, 135, 136, 138 and Division 8 of Part 4 (charges; later wave) | `s 363(1)`, `s 363(7)` | inputs for the fact (`the charge would have been required to be registered under Division 8 of Part 4 ...`); the four sections are a choice, with "another section" for the rest | text |
| s 408(1) and (3) (default penalty, "officer who is in default"; later wave) | `s 363(4)` | input `the person is an officer of the company who is in default, as section 408(3) defines that phrase`; the default penalty's amount is s 408(1)'s and is not stated in the Part; the definition was read at line 28139 for the wording only | text; line 28139 |
| Division 2 of Part 11 (foreign companies; the `sgg` part) | `s 361(1)(b)` | input `the foreign corporate entity was registered as a foreign company under Division 2 of Part 11 immediately before the date of registration` | text; XREFS (the heading of s 365 is at line 23615) |
| regulations under s 411 (not a source) | the form, manner, particulars, other documents and fee of s 358(2); the minimum requirements of s 360(1); the adaptation of s 361(1)(a) | inputs named for the fact (the prescribed thing was done; the Registrar is satisfied the minimum requirements are met; the regulations specify an adaptation) | text; s 364A |
| s 4(1) "private company" (keel) | `s 359(3)(c)` | NOT called: the keel's three limbs (lines 1622 to 1631) have none for a company registered by transfer; the fact is an input | finding 4 |

Seams the plan lacks:
- The core `Party` has no constructor for a foreign corporate entity that is not yet a company, so the rules of ss 357 and 358 use a small type of this module (`s 357 party`); see NEEDS-CORE.md.
- Section 357(3) is a bar that sits outside s 359(1), whose own words say only "Subject to section 360"; each section answers for itself (E1, option C), and the seat's s 359(1) question says so in a comment.

Seams given (sections of this part that others cite): `s 355` is cited by s 2, "Division into Parts" (line 1067, as "sections 355-364A"), and `s 357(2)` by s 27 (line 4678).
They are cited by number and ask nothing of this part's functions.

## Split sites (sge)

(i) An unmet element of an offence or contravention: `JUST FALSE` or `NOTHING`?
One site: s 363(4), `s 363(4) the person is guilty of an offence`.
The answer taken is `JUST FALSE` when default has not been made, or the person is neither the company nor an officer in default, because the function is the provision's own question ("shall each be guilty of an offence") and flat negatives count as no (N2); the other reading is `NOTHING`.
Fork line: F-363-5.
The companion function `s 363(4) the most the person may be sentenced to on conviction` answers `NOTHING` for a person not guilty (silent: the subsection states a penalty only for the person it makes guilty).
Count: 1 site, 1 answer `JUST FALSE`.

(ii) A "may" gated by "where", "when", "upon", "on application" or the like: `JUST FALSE` or `NOTHING`?
Five sites, all taken as `JUST FALSE`, by the periods ruling of 2026-11-05 item (b) and the ruling of the same day that "when", "upon" and "whenever" count as "where"; the other reading is `NOTHING` by the grant ruling's line, which the Guide leaves for a lawyer (grant limit 3).
- s 359(1), "upon compliance by the foreign corporate entity with section 358": F-359-8.
- s 359(7), "on the application of the foreign corporate entity": F-359-5.
- s 362(3), "At the expiration of the time ..." and "unless cause to the contrary is previously shown": F-362-4.
- s 363(6), "on being satisfied" and "on the application of": F-363-7.
- s 364(4), "If ... fails to make good the default within 10 days" and "on the application of the person entitled": F-364-4.

Not split sites, but near them: s 359(1)'s "if the Registrar thinks fit" is an "if" gate on a grant and answers `NOTHING` (grant limit 1, F-359-1); s 362(1)'s "if the company fails to comply" the same (F-362-1); the two "upon" gates on duties (s 359(4), F-359-3, and s 364(2), F-364-2) and the "Where" of s 363(3) (F-363-4) answer `JUST FALSE` under ruling (b), (c); s 363(3) is the one "entitled"-named function.

## Rules with no breach path (sge)

A `MUST` with no time limit and no consequence cannot be shown breached: a late action still reads `FULFILLED`, and a different action leaves the obligation open (`RESIDUAL`).
These seven rules are regulative rules of the Registrar or of an entity whose text states neither a time nor a consequence; each has a trace that reaches `FULFILLED` and one that stays `RESIDUAL`, on both builds:
- s 357(1), `s 357(1) a foreign corporate entity that intends to be registered must apply to reserve the name of the intended company` (no time, no consequence).
- s 359(3), `s 359(3) upon registration the Registrar must issue a notice of transfer of registration`.
- s 359(4), `s 359(4) the Registrar must issue a certificate of confirmation of registration upon the application of the company`.
- s 360(1), `s 360(1) the Registrar must refuse to register a foreign corporate entity if not satisfied that the requirements have been met`.
- s 360(2), `s 360(2) the Registrar must refuse to register a foreign corporate entity if satisfied of a ground in the subsection`.
- s 362(2), `s 362(2) before making an order of revocation the Registrar must give notice and consider representations`.
- s 362(4), `s 362(4) the Registrar must publish the notice of the order of revocation and serve a copy on the company`.

The rules with a stated time and a consequence reach `BREACH`: s 359(6) (60 days, or the extended period), s 363(1) (30 days), s 364(1) (60 days), s 364(4) (the time the order specifies; company and officer).
The four permissions (`MAY`: s 358(1), s 359(9), s 360(3), s 362(2)(b)) carry no `LEST`, because a `MAY` with a `LEST` reads differently on the two stable builds and cannot be breached anyway; after the stated period the permission lapses and the rule reads `FULFILLED`.
36 traces run, each with an `-- EXPECT` comment; each was read against the printed outcome on both builds by `work/traces.sh` (not shipped), because `check.sh` does not compare traces.


## Findings: what the text turns out to say

1. **The Part provides for a transfer in only.**
   Nothing in ss 355 to 364A (lines 23148 to 23607, the whole of this range) provides for a transfer of registration out of Singapore.
   A search of the range for "transfer", "outside Singapore", "deregist" and "domicile" finds only the words of the transfer in: the definitions of s 356, the notice of transfer of registration of s 359(3), and the entity's duty under s 359(6) to show that it has been deregistered in its place of incorporation (the one other hit, at line 23565, is the transfer of shares by delivery of a warrant, which is not a transfer of registration).
   This encoding has not looked beyond its ranges, so it says nothing about any other provision.
   The nearest headings in other ranges, named without being encoded, are Part 11, Division 2 (foreign companies, from s 365 at line 23615) and s 344F (restoring a company deregistered by mistake, line 23058).
   No provision is invented for an outward route.
2. **Two clocks.**
   Section 359(6) counts its 60 days from "the issue of the notice of transfer of registration" (lines 23293 to 23296).
   Sections 363(1) and 364(1) count 30 and 60 days from "the date of registration of the company", which s 356 defines as the date "specified in the notice" (lines 23163 to 23167).
   The text does not say that the two dates are the same, so the functions take them as two dates.
3. **Section 359(1) is "Subject to section 360" only.**
   The bar of s 357(3) (no registration unless the name has been reserved) is a separate sentence, and the Registrar's power in s 359(1) is also "upon compliance by the foreign corporate entity with section 358", which does not mention s 357.
   Each section answers for itself in this encoding (ruling E1, option C); a caller who wants "may the Registrar register" asks s 359(1) and s 357(3) both, and the seat's s 359(1) question says so in a comment.
4. **"Where applicable, a private company" has no definition to apply.**
   s 4(1) "private company" (lines 1622 to 1631) has three limbs: a company that was a private company before 29 December 1967, one incorporated as private under s 18, and one converted under s 31(1).
   None is a company registered by transfer, so s 359(3)(c) is answered `NOTHING` for a company the caller says is not private, and the fact "the company is a private company" is an input (F-359-2).
5. **Only one offence in the Part.**
   The only offence and penalty in the range is s 363(4): a fine not exceeding $1,000 and also a default penalty, on the company and every officer in default (lines 23503 to 23506).
   Section 364 states none; its sanction is the Court's order in subsection (4).
   Section 362 states none; its sanction is revocation.
   The amount of the default penalty is s 408(1)'s, not the Part's.
6. **Most of the Registrar's duties have no time limit.**
   ss 359(3), 359(4), 360(1), 360(2), 362(2) and 362(4) say "must" and name no period; see "Rules with no breach path".
   The persons with time limits are the entity (60 days, s 359(6)), the company (30 days, s 363(1); 60 days, s 364(1)) and the person aggrieved (30 days, ss 359(9), 360(3)).
7. **s 363(1) names no actor.**
   "there must be lodged with the Registrar"; the heading and subsection (4) put the duty on the company (F-363-2).
8. **s 362(3) names no start for its period.**
   "At the expiration of the time mentioned in the notice" is the period the Registrar's notice specifies under s 362(2)(b), which must be at least 30 days; the text does not say from when it runs (F-362-3).
9. **The bearer warrant is void, but the Part is silent on what its holder gets.**
   Section 364(3) makes void a share warrant to bearer issued by the foreign corporate entity before the date of registration.
   Section 364(1) speaks of "persons registered as holders of existing shares or debentures".
   The Part says nothing of what the holder of a voided warrant is owed.
10. **The effect of registration is stated mostly by negatives.**
    Section 361(2) says the registration "does not" create a new legal entity, prejudice or affect the identity or continuity of the body corporate, affect its property, rights or obligations, or render defective any legal proceedings.
    Under N2 each is `JUST FALSE`, and the closing words say that proceedings that could have been continued or commenced before registration may be after it.
11. **Section 364A is a power to make regulations, and the Part leans on it.**
    The "prescribed" form, manner, particulars, documents, fee and minimum requirements, and any waiver or adaptation, are in regulations that were not among the sources, so each is an input.

## What the stable binary does not accept

The binary governs where a skill describes a construct it rejects.
Loud failures (an error that teaches):
- Two consecutive `GIVEN` lines are a parse error (`unexpected GIVEN`); every function has one `GIVEN` block.
- `WAIT UNTIL` is spelled `WAITUNTIL`.
- A `NOT` is parenthesised, and every `#ASSERT` is on one line.

Silent differences (a wrong answer with no error), and how this encoding avoids them:
- A `MAY` with a `LEST` reads differently on the two stable builds, so no `MAY` rule here carries a `LEST`.
- `check.sh` compares counts and does not see a different `#TRACE` outcome; the 36 traces were compared by hand on both builds (`work/traces.sh`, not shipped), and agree.
- `REFUSE`, `YMD`, `TYPICALLY` on a record field, sets and `EVERY` are not used.

`l4 batch` finds the `@export` questions of `sge-seat.l4` and evaluates them on a row of inputs (checked on the s 355 question; the answer for a body corporate incorporated abroad that intends to register was `true`).

## Seat layer: the questions and the direction check

68 questions in nine groups, in the text's order, 161 assertions in `sge-cases-seat.l4` (every question has at least one case, and most also assert a `NOTHING` or a `JUST FALSE` case).
Every question asks yes or no (or a date, a number, a place or a choice) in the direction its name says.
The check: for each question the name's verb and subject were compared with the layer-1 function it calls, and with what `JUST TRUE` would mean.
Two titles were changed by that check: "how much may I recover" became "how much in fees am I entitled to recover" (the function is the entitlement of s 363(3)), and a garbled verb in the s 364(1) deadline question was repaired.
No question is titled as a permission while calling a bar: the one bar, s 357(3), is titled as the bar ("does the section bar registration"), and the "must" questions (ss 357(1), 360(1), 360(2), 364(1)) call the functions that say the duty arises.
The groups that arise only in a situation the person may not be in are marked in the heading itself: refusal (s 360) and revocation (s 362).


### The questions

| # | question | layer-1 function called | cases |
| --- | --- | --- | --- |
| 1 | Under section 355, does Part 10A of the Companies Act apply to the body I act for? | `s 355 this Part applies to the body` | 3 |
| 2 | Under section 356, is the body I act for a foreign corporate entity? | `s 356 "foreign corporate entity" the body is a foreign corporate entity` | 2 |
| 3 | Under section 356, what is the date of registration of the foreign corporate entity? | `s 356 "date of registration" the date of registration of the foreign corporate entity` | 2 |
| 4 | Under section 356, what is the place of incorporation of the foreign corporate entity? | `s 356 "place of incorporation" the place of incorporation of the foreign corporate entity` | 2 |
| 5 | Under section 356, is the foreign corporate entity registered? | `s 356 "register" and "registered" the foreign corporate entity is registered` | 3 |
| 6 | Under section 357(1), must the foreign corporate entity I act for apply to reserve the name of the intended company? | `s 357(1) the foreign corporate entity must apply to reserve the name of the intended company` | 3 |
| 7 | Under section 357(2), does section 27 apply to and in respect of my application to reserve the name? | `s 357(2) section 27 applies to and in respect of the application` | 2 |
| 8 | Under section 357(3), does the section bar registration of the foreign corporate entity under section 359(1)? | `s 357(3) the subsection bars the registration of the foreign corporate entity under section 359(1)` | 2 |
| 9 | Under section 358(1), may the foreign corporate entity I act for apply to the Registrar to be registered as a company limited by shares? | `s 358(1) the foreign corporate entity may apply to the Registrar to be registered as a company limited by shares` | 2 |
| 10 | Under section 358(2), does the application meet the requirements of the subsection? | `s 358(2) the application meets the requirements of the subsection` | 3 |
| 11 | Under section 358(2)(b), is the application accompanied as the paragraph requires? | `s 358(2)(b) the application is accompanied as the paragraph requires` | 2 |
| 12 | Under section 358(3), may the Registrar require me as applicant to furnish further information or documents? | `s 358(3) the Registrar may require the applicant to furnish further information or documents` | 2 |
| 13 | Under section 359(1), may the Registrar register the foreign corporate entity as a company limited by shares? | `s 359(1) the Registrar may register the foreign corporate entity as a company limited by shares` | 3 |
| 14 | Under section 359(2), is the registration subject to the condition the Registrar imposed? | `s 359(2) the registration is subject to the condition` | 2 |
| 15 | Under section 359(3), is the notice of transfer of registration as the subsection requires? | `s 359(3) the notice of transfer of registration is as the subsection requires` | 3 |
| 16 | Under section 359(4), is the Registrar required to issue a certificate of confirmation of registration? | `s 359(4) the Registrar is required to issue a certificate of confirmation of registration` | 3 |
| 17 | Under section 359(5), is the document conclusive evidence that the foreign corporate entity is registered under section 359? | `s 359(5)(a) the document is conclusive evidence that the foreign corporate entity is registered under section 359` | 3 |
| 18 | Under section 359(5), what date of the company's registration does the document conclusively show? | `s 359(5)(b) the date of the company's registration that the document conclusively shows` | 2 |
| 19 | Under section 359(6), what is the last day for submitting the document evidencing deregistration? | `s 359(6) the last day for submitting the document evidencing deregistration` | 2 |
| 20 | Under section 359(6), has the foreign corporate entity complied with the duty to submit the document evidencing deregistration? | `s 359(6) the foreign corporate entity has complied with the duty to submit the document evidencing deregistration` | 3 |
| 21 | Under section 359(7), may the Registrar extend the 60-day period? | `s 359(7) the Registrar may extend the 60-day period` | 3 |
| 22 | Under section 359(8), may the Registrar waive or modify the condition? | `s 359(8) the Registrar may waive or modify the condition` | 2 |
| 23 | Under section 359(9), may I appeal to the Minister against the decision? | `s 359(9) the person aggrieved may appeal to the Minister` | 3 |
| 24 | Under section 359(9), is the Minister's decision on my appeal final? | `s 359(9) the Minister's decision on the appeal is final` | 2 |
| 25 | Under section 360(1), must the Registrar refuse to register the foreign corporate entity? | `s 360(1) the Registrar must refuse to register the foreign corporate entity` | 2 |
| 26 | Under section 360(2), must the Registrar refuse to register the foreign corporate entity on a ground in the subsection? | `s 360(2) the Registrar must refuse to register the foreign corporate entity on a ground in the subsection` | 2 |
| 27 | Under section 360(3), may I appeal to the Minister against the Registrar's refusal? | `s 360(3) the person aggrieved may appeal to the Minister` | 3 |
| 28 | Under section 360(3), is the Minister's decision on my appeal final? | `s 360(3) the Minister's decision on the appeal is final` | 2 |
| 29 | Under section 361(1)(a), is the foreign corporate entity a company as defined in section 4(1)? | `s 361(1)(a) the foreign corporate entity is a company as defined in section 4(1)` | 2 |
| 30 | Under section 361(1)(a), how does a provision of the Act apply to the foreign corporate entity? | `s 361(1)(a) the provision of the Act applies to the foreign corporate entity` | 4 |
| 31 | Under section 361(1)(b), has the foreign corporate entity ceased to be registered as a foreign company under Division 2 of Part 11? | `s 361(1)(b) the foreign corporate entity has ceased to be registered as a foreign company under Division 2 of Part 11` | 2 |
| 32 | Under section 361(2)(a), does the registration of the foreign corporate entity create a new legal entity? | `s 361(2)(a) the registration of the foreign corporate entity creates a new legal entity` | 2 |
| 33 | Under section 361(2)(b), does the registration of the foreign corporate entity prejudice or affect its identity or its continuity as a body corporate? | `s 361(2)(b) the registration of the foreign corporate entity prejudices or affects the thing` | 2 |
| 34 | Under section 361(2)(c), does the registration of the foreign corporate entity affect its property, rights or obligations? | `s 361(2)(c) the registration of the foreign corporate entity affects the thing` | 2 |
| 35 | Under section 361(2)(d), does the registration of the foreign corporate entity render defective legal proceedings by or against it? | `s 361(2)(d) the registration of the foreign corporate entity renders defective legal proceedings by or against the foreign corporate entity` | 2 |
| 36 | Under section 361(2), may legal proceedings be continued or commenced by or against the company after the registration? | `s 361(2) the legal proceedings may be continued or commenced by or against the company after the registration` | 2 |
| 37 | Under section 362(1), may the Registrar by order revoke the registration of the company? | `s 362(1) the Registrar may by order revoke the registration of the company` | 2 |
| 38 | Under section 362(2), has the Registrar done what the subsection requires before making an order of revocation? | `s 362(2) the Registrar has done what the subsection requires before making an order of revocation` | 3 |
| 39 | Under section 362(3), may the Registrar order that the registration of the company be revoked? | `s 362(3) the Registrar may order that the registration of the company be revoked` | 3 |
| 40 | Under section 362(4), has the Registrar published and served the notice of the order of revocation? | `s 362(4) the Registrar has published and served the notice of the order of revocation` | 2 |
| 41 | Under section 362(5), has the order of revocation taken effect? | `s 362(5) the order of revocation has taken effect` | 2 |
| 42 | Under section 362(5), has the company ceased to be a company as defined in section 4(1)? | `s 362(5) the company has ceased to be a company as defined in section 4(1)` | 2 |
| 43 | Under section 362(5), have the provisions of the Act ceased to apply to the company? | `s 362(5) the provisions of this Act have ceased to apply to the company` | 2 |
| 44 | Under section 362(6), is the order of revocation final? | `s 362(6) the order of revocation is final` | 2 |
| 45 | Under section 362(7), does my liability continue despite the order of revocation? | `s 362(7) the liability of the person continues despite the order of revocation` | 3 |
| 46 | Under section 362(8), does section 362 prejudice the enforcement of the right or claim? | `s 362(8) section 362 prejudices the enforcement of the right or claim` | 2 |
| 47 | Under section 363(1), must a statement of the charge be lodged with the Registrar? | `s 363(1) a statement of the charge must be lodged with the Registrar` | 2 |
| 48 | Under section 363(1), what is the last day for lodging the statement of the charge? | `s 363(1) the last day for lodging the statement of the charge` | 1 |
| 49 | Under section 363(1), has the statement of the charge been lodged as the subsection requires? | `s 363(1) the statement of the charge has been lodged as the subsection requires` | 3 |
| 50 | Under section 363(2), may I lodge the documents and particulars required to be lodged? | `s 363(2) the person may lodge the documents and particulars required to be lodged` | 2 |
| 51 | Under section 363(3), am I entitled to recover the fees from the company? | `s 363(3) the person is entitled to recover the fees from the company` | 2 |
| 52 | Under section 363(3), how much in fees am I entitled to recover from the company? | `s 363(3) the amount of fees the person is entitled to recover from the company` | 2 |
| 53 | Under section 363(4), is the person I ask about guilty of an offence? | `s 363(4) the person is guilty of an offence` | 3 |
| 54 | Under section 363(4), what is the most the person I ask about may be sentenced to on conviction? | `s 363(4) the most the person may be sentenced to on conviction` | 2 |
| 55 | Under section 363(5), does a failure to comply with section 363(1) affect the continuity of status, operation or effect of the charge? | `s 363(5) the failure to comply with section 363(1) affects the continuity of status, operation or effect of the thing of the charge` | 2 |
| 56 | Under section 363(6), may the Court order that the time for registration be extended or that the omission or mis-statement be rectified? | `s 363(6) the Court may order that the time for registration be extended or that the omission or mis-statement be rectified` | 3 |
| 57 | Under section 363(6), may the Court impose the term or condition on its order? | `s 363(6) the Court may impose the term or condition on its order` | 2 |
| 58 | Under section 363(7), does the section apply to the charge as if it were a charge to which Division 8 of Part 4 applied? | `s 363(7) the section applies to the charge as if it were a charge to which Division 8 of Part 4 applied` | 3 |
| 59 | Under section 364(1), must the company complete and have ready for delivery appropriate certificates in respect of me? | `s 364(1) the company must complete and have ready for delivery appropriate certificates in respect of the person` | 2 |
| 60 | Under section 364(1), what is the last day for the company to complete and have ready the certificates? | `s 364(1) the last day for completing and having ready for delivery the certificates` | 1 |
| 61 | Under section 364(1), has the company completed the certificates, and does it have them ready for delivery, within 60 days after the date of registration? | `s 364(1) the company has completed and has ready for delivery the certificates within 60 days after the date of registration` | 3 |
| 62 | Under section 364(2), has my prior certificate ceased to be operative? | `s 364(2) the prior certificate has ceased to be operative` | 3 |
| 63 | Under section 364(2), has my prior certificate ceased to have any validity for the purposes of the Act? | `s 364(2) the prior certificate has ceased to have any validity for the purposes of this Act` | 2 |
| 64 | Under section 364(3), is the share warrant void? | `s 364(3) the share warrant is void` | 2 |
| 65 | Under section 364(4), has the company failed to make good the default within 10 days after the service of the notice? | `s 364(4) the company has failed to make good the default within 10 days after the service of the notice` | 3 |
| 66 | Under section 364(4), may the Court make an order directing the company and any officer of the company to make good the default? | `s 364(4) the Court may make an order directing the company and any officer of the company to make good the default` | 3 |
| 67 | Under section 364(4), may the order direct the person I ask about to make good the default? | `s 364(4) the order may direct the person to make good the default` | 3 |
| 68 | Under section 364(4), may the order provide that the costs are to be borne by the person I ask about? | `s 364(4) the order may provide that the costs of and incidental to the application are to be borne by the person` | 3 |

## What the text does not answer

- What the prescribed form, manner, particulars, other documents, fee and minimum requirements of ss 358 and 360 are (regulations; inputs).
- When a company registered by transfer is a private company (s 359(3)(c)).
- From when the time of a notice runs under s 362(3), and how an extension under s 359(7) is expressed.
- Who must lodge the statement of a charge under s 363(1) (taken as the company).
- The amount of a default penalty, and who is "an officer who is in default" (s 408, outside this range; asked as an input).
- Any time limit for the Registrar's duties in ss 359(3), 359(4), 360, 362(2) and 362(4), and any consequence if the Registrar does not act.
- What the holder of a bearer share warrant made void by s 364(3) is owed.
- Whether and how a registration may be transferred out of Singapore (finding 1; this encoding has not looked beyond its ranges).

## Inert rows

Five rows, none a rule the person could be asked about:
- Row 1, "Part 10A" and "TRANSFER OF REGISTRATION" (lines 23148 to 23151): reason 1 (not operative, a Part heading).
- Rows for s 364A: its lead-in and paragraphs (a), (b) and (c) (lines 23588 to 23607): reason 2 (machinery, the Minister's power to make regulations under s 411).
  What the regulations may do enters the layer-1 functions as inputs (the minimum requirements of s 360(1), the adaptation of s 361(1)(a)); the waiver of paragraph (b) has no function, because no fact a person can state decides it.

## Audit counts

The coverage table was built from the text with a script (`work/coverage.py`, not shipped), and every non-blank line of lines 23148 to 23607 (310 lines) falls in exactly one row.
An independent scan of the same lines for labelled units (a section number, a `(1)` subsection, a `(a)` or `(i)` paragraph, a defined term opening with a quotation mark) found 81 unit lines; every one is a row start or the number line of a row that starts at its marginal heading.
The five rows that are not labelled units are the Part heading, the closing words of s 359(9), s 361(2) and s 363(6), and the "register" and "registered" clause of s 356.
Rows before the audit script: 86 (written by hand from the labels).
Rows after: 86 (the script found no uncovered line and no unit start outside a row).
Dispositions: 49 `encoded`, 32 `fork`, 5 `inert` (1 of reason 1, 4 of reason 2), 0 `repealed or blank in this text`.
(A `fork` row is an encoded row with an entry in the fork register; each points at the entry and at the rule.)

## Compared with the earlier pass

Not applicable: there is no `inputs/NAIVE-EVIDENCE/` folder in this sandbox.

## What check.sh prints

Run on 1.6.110 (`l4-main-110`, sha256 `9c7656f7...016c7`, matching the brief) with 1.6.109 as the second stable build, in this folder:

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
sge-cases-seat.l4                              0       161       0        0         0 |      0       161       0        0  same
sge-p10a-355-356.l4                            0         0       0        0         0 |      0         0       0        0  same
sge-p10a-357-358.l4                            0         0       0        0         0 |      0         0       0        0  same
sge-p10a-359.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-360.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-361.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-362.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-363.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-p10a-364.l4                                0         0       0        0         0 |      0         0       0        0  same
sge-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sge-tests-355-356.l4                           0        28       0        0         0 |      0        28       0        0  same
sge-tests-357-358.l4                           0        38       0        0         0 |      0        38       0        0  same
sge-tests-359.l4                               0        64       0        0         0 |      0        64       0        0  same
sge-tests-360.l4                               0        20       0        0         0 |      0        20       0        0  same
sge-tests-361.l4                               0        26       0        0         0 |      0        26       0        0  same
sge-tests-362.l4                               0        49       0        0         0 |      0        49       0        0  same
sge-tests-363.l4                               0        45       0        0         0 |      0        45       0        0  same
sge-tests-364.l4                               0        37       0        0         0 |      0        37       0        0  same
TOTAL (26 modules)                             0       468       0        0           |      0       468       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline it replaced: the eight keel modules alone, each with 0 errors and 0 assertions, 8 modules in all.
After this encoding: 26 modules, 468 assertions satisfied (307 in the eight layer-1 test files and 161 in the seat cases), 0 failed, 0 refused, 0 errors, every module "same" on the main build.
The `srcrefs.py check --refs` and `--strict` gates report 0 problems on every `sge-` file.
A mutation check ran on each of the eight layer-1 modules (a period changed by one day, a comparison loosened, or a conjunction changed to a disjunction): each mutation made at least one assertion fail on 1.6.110, and the files were restored byte for byte.
Three expected values of the seat cases were also flipped on a copy (a yes, a not-covered and a date): three assertions failed, so the seat harness can fail.

## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its fork-line comment, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

No site of this part changed under it (2026S1bC): the functions of this part that stay Boolean after the protocol split already answered as the ruling reads, and its protocol-shaped functions keep limit 3 of the grant ruling until they are re-encoded.
