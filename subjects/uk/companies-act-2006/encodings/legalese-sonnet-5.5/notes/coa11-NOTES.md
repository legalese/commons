# NOTES: Companies Act 2006 (United Kingdom), part coa11: Part 16 (Audit), Chapter 1 (Requirement for audited accounts) and Chapter 2 (Appointment of auditors), ss 475 to 494A, raw lines 6543-6969

Written by the part agent `coa11` (Sonnet 5.5) for run `dst-coa11`, on the keel agent's shared core (`coa-core.l4`, `coa-definitions.l4`, read-only copies).
Target: the stable `l4` (main): 1.6.110 (main, e51181d, 2026-11-11), cross-checked by 1.6.109 (main, 4c887e0, 2026-11-04).
Nothing in this file or in the modules is "verified against the official text".

## Source and what "verified" means here

The source is `ukpga-2006-46.txt`, a plain-text rendering of the Act from legislation.gov.uk (Open Government Licence v3.0) made by a converter script; it is not the official text.
Every quote line in the `.l4` files is copied from it by `srcrefs.py quote`, and `python3 -I srcrefs.py check --refs` and `--strict` print 0 problems on all ten `coa11-*.l4` files (472 quote lines, 167 runs, 167 locators).
That proves the quotations match the rendering and the citations lie inside the quoted lines; it does not prove that an encoding means what the text says, and it does not prove the rendering matches the official text.
The rendering prints some amended provisions twice and shows omitted words as "..." (findings 1 and 2); the encoding follows the words as shown and says where that matters.

Where `inputs/PLAN.md` and the brief differ, the brief governs.
The one difference found: PLAN.md section 4.1 says a part cannot import the keel's definitions module and takes the keel's answers as inputs; the brief says layer 1 imports `coa-core.l4` and `coa-definitions.l4`.
The modules import `coa-core` (for `Party`, `Penalty`, `Fine limit`, `Form of document`) and take every keel answer as an input named for its section, as PLAN.md 4.1 says, which is compatible with both; `coa-definitions` is not imported because no rule here calls it.

## Seat

The seat (assumed, not ruled): an individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows (liability, offences, penalties) if it is not done.
There is no seat for an official: the powers of the Secretary of State, the Scottish Ministers and the competent authority appear only as what they mean for the company or its officers (for example `Under section 486(2), must my private company give the Secretary of State notice ...`).
The seat layer is `coa11-seat.l4` (67 `@export` questions, each named "Under section N, ..." and grouped under `§` headings in the text's order) with its cases in `coa11-cases-seat.l4` (227 assertions).
The seat questions are listed, with the layer-1 rule each calls, in the table "Seat questions" below, together with the audit of direction required by the brief.

## What is encoded and what is not

Everything in raw lines 6543 to 6969 has a row in the coverage table.
Encoded in layer 1 (four modules along the text's own cuts): ss 475 to 484 (`coa11-part16-ch1.l4`), ss 485 to 488 with 485A, 485B, 485C and 486A (`coa11-part16-ch2-private.l4`), ss 489 to 491 with 489A, 489B, 489C and 490A (`coa11-part16-ch2-public.l4`), ss 492, 494ZA and 494A (`coa11-part16-ch2-general.l4`).
Inert under reason 2 (machinery): s 483(4), s 484, s 493 and s 494 (powers to make orders and regulations, and the procedure for them).
Shown blank in the text: 477(2), (3) and (4)(b); 479(2) and (5)(c) to (e); 479C(2)(c); 487(1A) to (1E) and 487A; 491(1A) to (1E) and 491A; the three lines of "..." in 494A.
Not encoded because the text points outside the sources: the content of the Audit Regulation (Article 16), Directive 2003/71/EC, the Financial Services and Markets Act 2000, the Government Resources and Accounts Act 2000 and the other Acts and instruments cited; each is a plain input.

## Coverage (coa11)

One row per unit of the text of raw lines 6543-6969: heading, cross-heading, section, subsection, paragraph, sub-paragraph, closing words, table row and defined term, built by `work/units.py` reading the raw file.
Audit: 427 non-blank lines in the range, all 427 covered by exactly one row, none uncovered; the first run of the units script found 401 rows, and reading the continuation lines it had folded into their neighbours (a section's lead-in, the closing words of a provision, the second "(2)" of s 475) added 13 more, so the table went from 401 rows to 414.
Dispositions (exactly one per row): encoded 299, fork 7, inert reason 1 48, inert reason 2 37, repealed or blank in this text 23; total 414.
The L4 names are given by their section label (the full names are in the index at the end of this file); `ch1`, `private`, `public` and `general` name the module.
A "fork" column entry points to the fork register; a row whose disposition is `fork` is one where the text itself can be read two ways with different outcomes.

| unit | raw lines | disposition | L4 name(s) / reason | forks |
| --- | --- | --- | --- | --- |
| heading: Part 16 — Audit | 6543 | inert (reason 1: not operative) | a heading (not operative) |  |
| heading: Chapter 1 — Requirement for audited accounts | 6544 | inert (reason 1: not operative) | a heading (not operative) |  |
| heading: Requirement for audited accounts | 6545 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 475 | 6546 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 475(1) | 6547 | encoded | `s 475 exemption`; `s 475(1)` (ch1) | F3, F25 |
| s 475(1)(a) | 6548-6552 | encoded | `s 475 exemption`; `s 475(1)` (ch1) | F3, F25 |
| s 475(1)(b) | 6553 | encoded | `s 475 exemption`; `s 475(1)` (ch1) | F3, F25 |
| s 475(2) | 6554 | fork | `s 475(2) (first printed version)` (ch1) -- the first of two printed versions of s 475(2) | F2 |
| s 475(2) [printed again, copy 2] | 6555 | fork | `s 475(2) (second printed version)` (ch1) -- the second of two printed versions of s 475(2) | F2 |
| s 475(2)(a) | 6556 | fork | `s 475(2) (second printed version)` (ch1) -- a limb of the second printed version of s 475(2) | F2 |
| s 475(2)(b) | 6557 | fork | `s 475(2) (second printed version)` (ch1) -- a limb of the second printed version of s 475(2) | F2 |
| s 475(3) | 6558 | encoded | `s 475(3)` (ch1); `s 475(2) to (4)` | F3, F5 |
| s 475(3)(a) | 6559 | encoded | `s 475(3)` (ch1); `s 475(2) to (4)` | F3, F5 |
| s 475(3)(b) | 6560 | encoded | `s 475(3)` (ch1); `s 475(2) to (4)` | F3, F5 |
| s 475(4) | 6561 | encoded | `s 475(4)` (ch1); `s 475(2) to (4)` | F4, F5 |
| s 476 | 6562 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 476(1) | 6563 | encoded | `s 476(1)` (ch1) | F7 |
| s 476(2) | 6564 | encoded | `s 476(2)` (ch1) | F4, F7 |
| s 476(2)(a) | 6565 | encoded | `s 476(2)` (ch1) | F4, F7 |
| s 476(2)(b) | 6566 | encoded | `s 476(2)` (ch1) | F4, F7 |
| s 476(3) | 6567 | encoded | `s 476(3) the last day ...`, `s 476(3) the notice is given in time` (ch1) | F6, F7 |
| heading: Exemption from audit: small companies | 6568 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 477 | 6569 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 477(1) | 6570 | encoded | `s 477(1)` (ch1) | F1 |
| s 477(2) | 6571 | repealed or blank in this text | shown as dots in the text |  |
| s 477(3) | 6572 | repealed or blank in this text | shown as dots in the text |  |
| s 477(4) | 6573 | encoded | the section 382 input of `s 477(1)` -- smallness is "determined in accordance with section 382(1) to (6)": an input, a seam (coa8) | F1 |
| s 477(4)(a) | 6574 | encoded | the section 382 input of `s 477(1)` -- smallness is "determined in accordance with section 382(1) to (6)": an input, a seam (coa8) | F1 |
| s 477(4)(b) | 6575 | repealed or blank in this text | shown as dots in the text |  |
| s 477(5) | 6576-6580 | encoded | `s 477(5)` (ch1), calling `s 475(2) to (4)` | F5 |
| s 478 | 6581 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 478 lead-in | 6582 | encoded | `s 478` (ch1) | F8 |
| s 478(a) | 6583 | encoded | `s 478` (ch1) | F8 |
| s 478(b) | 6584 | encoded | `s 478` (ch1) | F8 |
| s 478(b)(i) | 6585 | encoded | `s 478` (ch1) | F8 |
| s 478(b)(ii) | 6586 | encoded | `s 478` (ch1) | F8 |
| s 478(b)(iii) | 6587 | encoded | `s 478` (ch1) | F8 |
| s 478(c) | 6588 | encoded | `s 478` (ch1) | F8 |
| s 479 | 6589 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 479(1) | 6590 | encoded | `s 479(1)` (ch1) | F3 |
| s 479(1)(a) | 6591 | encoded | `s 479(1)` (ch1) | F3 |
| s 479(1)(a)(i) | 6592 | encoded | `s 479(1)` (ch1) | F3 |
| s 479(1)(a)(ii) | 6593 | encoded | `s 479(1)` (ch1) | F3 |
| s 479(1)(b) | 6594 | encoded | `s 479(1)` (ch1) | F3 |
| s 479(2) | 6595 | repealed or blank in this text | shown as dots in the text |  |
| s 479(3) | 6596 | encoded | `s 479(3) subsection (3) applies ...` (ch1) | F10 |
| s 479(4) | 6597 | encoded | `s 479(4)(a)`, `s 479(4) the two undertakings are associated`, `s 479(4)(b)` (ch1) | F9 |
| s 479(4)(a) | 6598 | encoded | `s 479(4)(a)`, `s 479(4) the two undertakings are associated`, `s 479(4)(b)` (ch1) | F9 |
| s 479(4)(b) | 6599 | encoded | `s 479(4)(a)`, `s 479(4) the two undertakings are associated`, `s 479(4)(b)` (ch1) | F9 |
| s 479(4) closing words (associated undertakings) | 6600 | encoded | `s 479(4)(a)`, `s 479(4) the two undertakings are associated`, `s 479(4)(b)` (ch1) -- closing words of the provision above | F9 |
| s 479(5) | 6601 | encoded | the section 383 and section 384(2) and (3) inputs of `s 479(1)` -- seams (coa8): "whether a group qualifies as small", "ineligible group" |  |
| s 479(5)(a) | 6602 | encoded | the section 383 and section 384(2) and (3) inputs of `s 479(1)` -- seams (coa8): "whether a group qualifies as small", "ineligible group" |  |
| s 479(5)(b) | 6603 | encoded | the section 383 and section 384(2) and (3) inputs of `s 479(1)` -- seams (coa8): "whether a group qualifies as small", "ineligible group" |  |
| s 479(5)(c) | 6604 | repealed or blank in this text | shown as dots in the text |  |
| s 479(5)(d) | 6605 | repealed or blank in this text | shown as dots in the text |  |
| s 479(5)(e) | 6606 | repealed or blank in this text | shown as dots in the text |  |
| s 479(6) | 6607 | encoded | `s 479(6)` (ch1) |  |
| heading: Exemption from audit: qualifying subsidiaries | 6608 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 479A | 6609 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 479A(1) | 6610 | encoded | `s 479A(1)` (ch1) | F1 |
| s 479A(1)(a) | 6611 | encoded | `s 479A(1)` (ch1) | F1 |
| s 479A(1)(b) | 6612 | encoded | `s 479A(1)` (ch1) | F1 |
| s 479A(2) | 6613 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(a) | 6614 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(b) | 6615 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(c) | 6616 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(c)(i) | 6617 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(c)(ii) | 6618 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(d) | 6619 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(e) | 6620 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(e)(i) | 6621 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(e)(ii) | 6622 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(e)(iii) | 6623 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(e)(iv) | 6624 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(2)(e)(v) | 6625 | encoded | `s 479A(2)`, `s 479A(2)(e) ...` and the record `s 479A(2)(e) documents delivered to the registrar` (ch1) | F1, F4 |
| s 479A(3) | 6626-6628 | encoded | `s 479A(3)` (ch1), calling `s 475(2) to (4)` | F5 |
| s 479B | 6629 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 479B lead-in | 6630 | encoded | `s 479B` (ch1) | F8 |
| s 479B(a) | 6631 | encoded | `s 479B` (ch1) | F8 |
| s 479B(b) | 6632 | encoded | `s 479B` (ch1) | F8 |
| s 479B(b)(i) | 6633 | encoded | `s 479B` (ch1) | F8 |
| s 479B(b)(ii) | 6634 | encoded | `s 479B` (ch1) | F8 |
| s 479B(b)(iii) | 6635 | encoded | `s 479B` (ch1) | F8 |
| s 479B(c) | 6636 | encoded | `s 479B` (ch1) | F8 |
| s 479C | 6637 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 479C(1) | 6638 | encoded | `s 479C(1)` (ch1) | F11 |
| s 479C(2) | 6639 | encoded | `s 479C(2)` (ch1) | F4 |
| s 479C(2)(a) | 6640 | encoded | `s 479C(2)` (ch1) | F4 |
| s 479C(2)(b) | 6641 | encoded | `s 479C(2)` (ch1) | F4 |
| s 479C(2)(c) | 6642 | repealed or blank in this text | shown as dots in the text |  |
| s 479C(2)(d) | 6643 | encoded | `s 479C(2)` (ch1) | F4 |
| s 479C(2)(e) | 6644 | encoded | `s 479C(2)` (ch1) | F4 |
| s 479C(2)(f) | 6645 | encoded | `s 479C(2)` (ch1) | F4 |
| s 479C(3) | 6646 | encoded | `s 479C(3)(a)`, `s 479C(3)(b)` (ch1) |  |
| s 479C(3)(a) | 6647 | encoded | `s 479C(3)(a)`, `s 479C(3)(b)` (ch1) |  |
| s 479C(3)(b) | 6648 | encoded | `s 479C(3)(a)`, `s 479C(3)(b)` (ch1) |  |
| heading: Exemption from audit: dormant companies | 6649 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 480 | 6650 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 480(1) | 6651 | encoded | `s 480(1)` (ch1) | F1 |
| s 480(1)(a) | 6652 | encoded | `s 480(1)` (ch1) | F1 |
| s 480(1)(b) | 6653 | encoded | `s 480(1)` (ch1) | F1 |
| s 480(2) | 6654 | encoded | `s 480(2)` (ch1) |  |
| s 480(2)(a) | 6655 | encoded | `s 480(2)` (ch1) |  |
| s 480(2)(a)(i) | 6656 | encoded | `s 480(2)` (ch1) |  |
| s 480(2)(a)(ii) | 6657 | encoded | `s 480(2)` (ch1) |  |
| s 480(2)(b) | 6658 | encoded | `s 480(2)` (ch1) |  |
| s 480(3) | 6659-6662 | encoded | `s 480(3)` (ch1), calling `s 475(2) to (4)` | F5 |
| s 481 | 6663 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 481 lead-in | 6664 | encoded | `s 481` (ch1) | F8 |
| s 481(za) | 6665 | encoded | `s 481` (ch1) | F8 |
| s 481(a) | 6666 | encoded | `s 481` (ch1) | F8 |
| s 481(b) | 6667 | encoded | `s 481` (ch1) | F8 |
| heading: Companies subject to public sector audit | 6668 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 482 | 6669 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 482(1) | 6670 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(1)(a) | 6671 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(1)(ab) | 6672 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(1)(ab)(i) | 6673 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(1)(ab)(ii) | 6674 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(1)(b) | 6675 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(1)(b)(i) | 6676 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(1)(b)(ii) | 6677 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(1)(c) | 6678 | encoded | `s 482(1) route of public sector audit` (type), `s 482(1)` (ch1) | F1 |
| s 482(2) | 6679 | encoded | `s 482(1)` (the group limb) (ch1) |  |
| s 482(3) | 6680 | encoded | the "non-profit-making" input of `s 482(1)` -- borrowed: Article 54 of the Treaty on the Functioning of the European Union; an input |  |
| s 482(4) | 6681 | encoded | `s 482(4)` (ch1), calling `s 475(2) to (4)` | F5 |
| s 483 | 6682 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 483(1) | 6683 | encoded | `s 483(1)` (ch1) | F16 |
| s 483(2) | 6684 | encoded | `s 483(1)` (ch1) | F16 |
| s 483(2)(a) | 6685 | encoded | `s 483(1)` (ch1) | F16 |
| s 483(2)(b) | 6686 | encoded | `s 483(1)` (ch1) | F16 |
| s 483(3) | 6687 | encoded | `s 483(3)` (ch1) | F12 |
| s 483(3)(a) | 6688 | encoded | `s 483(3)` (ch1) | F12 |
| s 483(3)(b) | 6689 | encoded | `s 483(3)` (ch1) | F12 |
| s 483(4) | 6690 | inert (reason 2: machinery) | the scope of an order-making power (machinery) |  |
| s 483(5) | 6691 | encoded | `s 483(5)` (ch1) | F3 |
| heading: General power of amendment by regulations | 6692 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 484 | 6693 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 484(1) | 6694 | inert (reason 2: machinery) | a regulation-making power and the procedure for regulations (machinery) |  |
| s 484(2) | 6695 | inert (reason 2: machinery) | a regulation-making power and the procedure for regulations (machinery) |  |
| s 484(3) | 6696 | inert (reason 2: machinery) | a regulation-making power and the procedure for regulations (machinery) |  |
| s 484(4) | 6697 | inert (reason 2: machinery) | a regulation-making power and the procedure for regulations (machinery) |  |
| heading: Chapter 2 — Appointment of auditors | 6698 | inert (reason 1: not operative) | a heading (not operative) |  |
| heading: Private companies | 6699 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 485 | 6700 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 485(1) | 6701 | encoded | `s 485(1)` (private) | F3 |
| s 485(2) | 6702 | encoded | `s 485(2) period for appointing auditors` (type), `s 485(2) the period for appointing auditors`, `s 485(2) the last day of the 28 days beginning with`, `s 485(2) the appointment is made before the end ...` (private) | F6, F27 |
| s 485(2)(a) | 6703 | encoded | `s 485(2) period for appointing auditors` (type), `s 485(2) the period for appointing auditors`, `s 485(2) the last day of the 28 days beginning with`, `s 485(2) the appointment is made before the end ...` (private) | F6, F27 |
| s 485(2)(b) | 6704 | encoded | `s 485(2) period for appointing auditors` (type), `s 485(2) the period for appointing auditors`, `s 485(2) the last day of the 28 days beginning with`, `s 485(2) the appointment is made before the end ...` (private) | F6, F27 |
| s 485(2) closing words (the period for appointing auditors) | 6705 | encoded | `s 485(2) period for appointing auditors` (type), `s 485(2) the period for appointing auditors`, `s 485(2) the last day of the 28 days beginning with`, `s 485(2) the appointment is made before the end ...` (private) -- closing words of the provision above | F6, F27 |
| s 485(3) | 6706 | encoded | `s 485(3)` (private) | F13 |
| s 485(3)(a) | 6707 | encoded | `s 485(3)` (private) | F13 |
| s 485(3)(b) | 6708 | encoded | `s 485(3)` (private) | F13 |
| s 485(3)(c) | 6709 | encoded | `s 485(3)` (private) | F13 |
| s 485(4) | 6710 | encoded | `s 485(4)` (private) | F13 |
| s 485(4)(a) | 6711 | encoded | `s 485(4)` (private) | F13 |
| s 485(4)(b) | 6712 | encoded | `s 485(4)` (private) | F13 |
| s 485(4)(c) | 6713 | encoded | `s 485(4)` (private) | F13 |
| s 485(5) | 6714 | encoded | `s 485(5)` (private) | F24 |
| s 485(5)(a) | 6715 | encoded | `s 485(5)` (private) | F24 |
| s 485(5)(b) | 6716 | encoded | `s 485(5)` (private) | F24 |
| s 485(5) closing words (deemed re-appointment) | 6717 | encoded | `s 485(5)` (private) -- closing words of the provision above | F24 |
| s 485A | 6718 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 485A(1) | 6719 | encoded | `s 485A(1)` (private) | F14 |
| s 485A(1)(a) | 6720 | encoded | `s 485A(1)` (private) | F14 |
| s 485A(1)(b) | 6721 | encoded | `s 485A(1)` (private) | F14 |
| s 485A(2) | 6722 | encoded | `s 485A(1)` (private) | F14 |
| s 485A(3) | 6723 | encoded | `s 485A(3)(a)`, `s 485A(3)(b)` (regulative rules), `s 485A(3)` (decision) (private) | F4 |
| s 485A(3)(a) | 6724 | encoded | `s 485A(3)(a)`, `s 485A(3)(b)` (regulative rules), `s 485A(3)` (decision) (private) | F4 |
| s 485A(3)(b) | 6725 | encoded | `s 485A(3)(a)`, `s 485A(3)(b)` (regulative rules), `s 485A(3)` (decision) (private) | F4 |
| s 485A(4) | 6726 | encoded | `s 485A(4)` (private) | F3 |
| s 485A(5) | 6727 | encoded | `s 485A(5)` (private) | F4 |
| s 485A(5)(a) | 6728 | encoded | `s 485A(5)` (private) | F4 |
| s 485A(5)(b) | 6729 | encoded | `s 485A(5)` (private) | F4 |
| s 485A(5)(c) | 6730 | encoded | `s 485A(5)` (private) | F4 |
| s 485A(5)(c)(i) | 6731 | encoded | `s 485A(5)` (private) | F4 |
| s 485A(5)(c)(ii) | 6732 | encoded | `s 485A(5)` (private) | F4 |
| s 485A(6) | 6733 | encoded | `s 485A(6)` (private) | F4 |
| s 485A(6)(a) | 6734 | encoded | `s 485A(6)` (private) | F4 |
| s 485A(6)(b) | 6735 | encoded | `s 485A(6)` (private) | F4 |
| s 485A(6)(b)(i) | 6736 | encoded | `s 485A(6)` (private) | F4 |
| s 485A(6)(b)(ii) | 6737 | encoded | `s 485A(6)` (private) | F4 |
| s 485A(7) | 6738 | encoded | limbs of `s 485A(4)` and `s 485A(5)` (private) | F3 |
| s 485B | 6739 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 485B(1) | 6740 | encoded | `s 485B(1)` (private) | F14 |
| s 485B(1)(a) | 6741 | encoded | `s 485B(1)` (private) | F14 |
| s 485B(1)(b) | 6742 | encoded | `s 485B(1)` (private) | F14 |
| s 485B(2) | 6743 | encoded | `s 485B(1)` (private) | F14 |
| s 485B(3) | 6744 | encoded | `s 485B(3)` (rule and decision) (private) | F4 |
| s 485B(4) | 6745 | encoded | `s 485B(4)` (two functions) (private) | F3, F4 |
| s 485B(5) | 6746 | encoded | `s 485B(4)` (two functions) (private) | F3, F4 |
| s 485C | 6747 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 485C(1) | 6748 | encoded | `s 485C(1)`, `s 485C(2)` and the four-year functions (private) | F6, F15 |
| s 485C(2) | 6749 | encoded | `s 485C(1)`, `s 485C(2)` and the four-year functions (private) | F6, F15 |
| s 485C(3) | 6750 | encoded | `s 485C(1)`, `s 485C(2)` and the four-year functions (private) | F6, F15 |
| s 486 | 6751 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 486(1) | 6752 | encoded | `s 486(1)` (private) | F16 |
| s 486(2) | 6753 | encoded | `s 486(2)` (three: duty, regulative rule, timing) (private) | F4, F6 |
| s 486(3) | 6754 | encoded | `s 486(3)(a)`, `s 486(3)(b)` (private) |  |
| s 486(3)(a) | 6755 | encoded | `s 486(3)(a)`, `s 486(3)(b)` (private) |  |
| s 486(3)(b) | 6756 | encoded | `s 486(3)(a)`, `s 486(3)(b)` (private) |  |
| s 486(4) | 6757 | encoded | `s 486(4)` (penalty and two amounts) (private) |  |
| s 486A | 6758 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 486A(1) | 6759 | encoded | `s 486A(1)` (private) | F16 |
| s 486A(1)(a) | 6760 | encoded | `s 486A(1)` (private) | F16 |
| s 486A(1)(b) | 6761 | encoded | `s 486A(1)` (private) | F16 |
| s 486A(1) closing words (Secretary of State may appoint) | 6762 | encoded | `s 486A(1)` (private) -- closing words of the provision above | F16 |
| s 486A(2) | 6763 | encoded | `s 486A(2)` (private) |  |
| s 486A(3) | 6764 | encoded | `s 486A(3)` (private) | F4 |
| s 486A(4) | 6765 | encoded | `s 486A(4)` (regulative rule and timing) (private) | F6 |
| s 486A(5) | 6766 | encoded | `s 486A(5)(a)`, `s 486A(5)(b)` (private) |  |
| s 486A(5)(a) | 6767 | encoded | `s 486A(5)(a)`, `s 486A(5)(b)` (private) |  |
| s 486A(5)(b) | 6768 | encoded | `s 486A(5)(a)`, `s 486A(5)(b)` (private) |  |
| s 486A(6) | 6769 | encoded | `s 486A(6)` (penalty and two amounts) (private) |  |
| s 487 | 6770 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 487(1) | 6771 | encoded | `s 487(1)(a)`, `s 487(1)(b)` (private) | F6 |
| s 487(1)(a) | 6772 | encoded | `s 487(1)(a)`, `s 487(1)(b)` (private) | F6 |
| s 487(1)(b) | 6773 | encoded | `s 487(1)(a)`, `s 487(1)(b)` (private) | F6 |
| s 487(1A) | 6774 | repealed or blank in this text | shown as dots in the text |  |
| s 487(1B) | 6775 | repealed or blank in this text | shown as dots in the text |  |
| s 487(1C) | 6776 | repealed or blank in this text | shown as dots in the text |  |
| s 487(1D) | 6777 | repealed or blank in this text | shown as dots in the text |  |
| s 487(1E) | 6778 | repealed or blank in this text | shown as dots in the text |  |
| s 487(2) | 6779 | encoded | `s 487(2)` (private) | F3, F17 |
| s 487(2)(a) | 6780 | encoded | `s 487(2)` (private) | F3, F17 |
| s 487(2)(b) | 6781 | encoded | `s 487(2)` (private) | F3, F17 |
| s 487(2)(c) | 6782 | encoded | `s 487(2)` (private) | F3, F17 |
| s 487(2)(d) | 6783 | encoded | `s 487(2)` (private) | F3, F17 |
| s 487(2)(e) | 6784 | encoded | `s 487(2)` (private) | F3, F17 |
| s 487(2)(f) | 6785 | encoded | `s 487(2)` (private) | F3, F17 |
| s 487(3) | 6786 | encoded | `s 487(3)` (private) |  |
| s 487(4) | 6787 | encoded | `s 487(4)` (private) |  |
| s 487A | 6788 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 487A body (blank) | 6789 | repealed or blank in this text | a body of dots |  |
| s 488 | 6790 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 488(1) | 6791 | encoded | `s 488(1)` (private) |  |
| s 488(2) | 6792 | encoded | `s 488(2)` (private) | F18 |
| s 488(3) | 6793 | encoded | `s 488(3)` (private) | F4, F6 |
| s 488(3)(a) | 6794 | encoded | `s 488(3)` (private) | F4, F6 |
| s 488(3)(b) | 6795 | encoded | `s 488(3)` (private) | F4, F6 |
| s 488(3)(c) | 6796 | encoded | `s 488(3)` (private) | F4, F6 |
| heading: Public companies | 6797 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 489 | 6798 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 489(1) | 6799 | encoded | `s 489(1)` (public) | F3 |
| s 489(2) | 6800 | encoded | `s 489(2)` (public) | F6, F19, F27 |
| s 489(3) | 6801 | encoded | `s 489(3)` (public) | F13 |
| s 489(3)(a) | 6802 | encoded | `s 489(3)` (public) | F13 |
| s 489(3)(b) | 6803 | encoded | `s 489(3)` (public) | F13 |
| s 489(3)(c) | 6804 | encoded | `s 489(3)` (public) | F13 |
| s 489(4) | 6805 | encoded | `s 489(4)` (public) | F13 |
| s 489(4)(a) | 6806 | encoded | `s 489(4)` (public) | F13 |
| s 489(4)(b) | 6807 | encoded | `s 489(4)` (public) | F13 |
| s 489(4)(c) | 6808 | encoded | `s 489(4)` (public) | F13 |
| s 489(5) | 6809 | encoded | `s 489(5)` (public) | F24 |
| s 489(5)(a) | 6810 | encoded | `s 489(5)` (public) | F24 |
| s 489(5)(b) | 6811 | encoded | `s 489(5)` (public) | F24 |
| s 489A | 6812 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 489A(1) | 6813 | encoded | `s 489A(1)` (public) | F14 |
| s 489A(1)(a) | 6814 | encoded | `s 489A(1)` (public) | F14 |
| s 489A(1)(b) | 6815 | encoded | `s 489A(1)` (public) | F14 |
| s 489A(2) | 6816 | encoded | `s 489A(1)` (public) | F14 |
| s 489A(3) | 6817 | encoded | `s 489A(3)(a)`, `s 489A(3)(b)` (regulative rules), `s 489A(3)` (decision) (public) | F4 |
| s 489A(3)(a) | 6818 | encoded | `s 489A(3)(a)`, `s 489A(3)(b)` (regulative rules), `s 489A(3)` (decision) (public) | F4 |
| s 489A(3)(b) | 6819 | encoded | `s 489A(3)(a)`, `s 489A(3)(b)` (regulative rules), `s 489A(3)` (decision) (public) | F4 |
| s 489A(4) | 6820 | encoded | `s 489A(4)` (public) | F3 |
| s 489A(4)(a) | 6821 | encoded | `s 489A(4)` (public) | F3 |
| s 489A(4)(b) | 6822 | encoded | `s 489A(4)` (public) | F3 |
| s 489A(5) | 6823 | encoded | `s 489A(5)` (public) | F4 |
| s 489A(5)(a) | 6824 | encoded | `s 489A(5)` (public) | F4 |
| s 489A(5)(b) | 6825 | encoded | `s 489A(5)` (public) | F4 |
| s 489A(5)(c) | 6826 | encoded | `s 489A(5)` (public) | F4 |
| s 489A(5)(c)(i) | 6827 | encoded | `s 489A(5)` (public) | F4 |
| s 489A(5)(c)(ii) | 6828 | encoded | `s 489A(5)` (public) | F4 |
| s 489A(6) | 6829 | encoded | `s 489A(6)` (public) | F4 |
| s 489A(6)(a) | 6830 | encoded | `s 489A(6)` (public) | F4 |
| s 489A(6)(b) | 6831 | encoded | `s 489A(6)` (public) | F4 |
| s 489A(6)(b)(i) | 6832 | encoded | `s 489A(6)` (public) | F4 |
| s 489A(6)(b)(ii) | 6833 | encoded | `s 489A(6)` (public) | F4 |
| s 489A(7) | 6834 | encoded | limbs of `s 489A(4)` and `s 489A(5)` (public) | F3 |
| s 489B | 6835 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 489B(1) | 6836 | encoded | `s 489B(1)` (public) | F14 |
| s 489B(1)(a) | 6837 | encoded | `s 489B(1)` (public) | F14 |
| s 489B(1)(b) | 6838 | encoded | `s 489B(1)` (public) | F14 |
| s 489B(2) | 6839 | encoded | `s 489B(1)` (public) | F14 |
| s 489B(3) | 6840 | encoded | `s 489B(3)` (rule and decision) (public) | F4 |
| s 489B(4) | 6841 | encoded | `s 489B(4)` (two functions) (public) | F3, F4 |
| s 489B(4)(a) | 6842 | encoded | `s 489B(4)` (two functions) (public) | F3, F4 |
| s 489B(4)(b) | 6843 | encoded | `s 489B(4)` (two functions) (public) | F3, F4 |
| s 489B(5) | 6844 | encoded | `s 489B(4)` (two functions) (public) | F3, F4 |
| s 489C | 6845 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 489C(1) | 6846 | encoded | `s 489C(1)`, `s 489C(2)` and the four-year functions (public) | F6, F15 |
| s 489C(2) | 6847 | encoded | `s 489C(1)`, `s 489C(2)` and the four-year functions (public) | F6, F15 |
| s 489C(3) | 6848 | encoded | `s 489C(1)`, `s 489C(2)` and the four-year functions (public) | F6, F15 |
| s 490 | 6849 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 490(1) | 6850 | encoded | `s 490(1)` (public) | F16 |
| s 490(2) | 6851 | encoded | `s 490(2)` (three: duty, regulative rule, timing) (public) | F4, F6 |
| s 490(3) | 6852 | encoded | `s 490(3)(a)`, `s 490(3)(b)` (public) |  |
| s 490(3)(a) | 6853 | encoded | `s 490(3)(a)`, `s 490(3)(b)` (public) |  |
| s 490(3)(b) | 6854 | encoded | `s 490(3)(a)`, `s 490(3)(b)` (public) |  |
| s 490(4) | 6855 | encoded | `s 490(4)` (penalty and two amounts) (public) |  |
| s 490A | 6856 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 490A(1) | 6857 | encoded | `s 490A(1)` (public) | F16 |
| s 490A(1)(a) | 6858 | encoded | `s 490A(1)` (public) | F16 |
| s 490A(1)(b) | 6859 | encoded | `s 490A(1)` (public) | F16 |
| s 490A(1) closing words (Secretary of State may appoint) | 6860 | encoded | `s 490A(1)` (public) -- closing words of the provision above | F16 |
| s 490A(2) | 6861 | encoded | `s 490A(2)` (public) |  |
| s 490A(3) | 6862 | encoded | `s 490A(3)` (public) | F4 |
| s 490A(4) | 6863 | encoded | `s 490A(4)` (regulative rule and timing) (public) | F6 |
| s 490A(5) | 6864 | encoded | `s 490A(5)(a)`, `s 490A(5)(b)` (public) |  |
| s 490A(5)(a) | 6865 | encoded | `s 490A(5)(a)`, `s 490A(5)(b)` (public) |  |
| s 490A(5)(b) | 6866 | encoded | `s 490A(5)(a)`, `s 490A(5)(b)` (public) |  |
| s 490A(6) | 6867 | encoded | `s 490A(6)` (penalty and two amounts) (public) |  |
| s 491 | 6868 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 491(1) | 6869 | encoded | `s 491(1)(a)`, `s 491(1)(b)` (public) | F19 |
| s 491(1)(a) | 6870 | encoded | `s 491(1)(a)`, `s 491(1)(b)` (public) | F19 |
| s 491(1)(b) | 6871 | encoded | `s 491(1)(a)`, `s 491(1)(b)` (public) | F19 |
| s 491(1A) | 6872 | repealed or blank in this text | shown as dots in the text |  |
| s 491(1B) | 6873 | repealed or blank in this text | shown as dots in the text |  |
| s 491(1C) | 6874 | repealed or blank in this text | shown as dots in the text |  |
| s 491(1D) | 6875 | repealed or blank in this text | shown as dots in the text |  |
| s 491(1E) | 6876 | repealed or blank in this text | shown as dots in the text |  |
| s 491(2) | 6877 | encoded | `s 491(2)` (public) |  |
| s 491A | 6878 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 491A body (blank) | 6879 | repealed or blank in this text | a body of dots |  |
| heading: General provisions | 6880 | inert (reason 1: not operative) | a heading (not operative) |  |
| s 492 | 6881 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 492(1) | 6882 | encoded | `s 492 way the auditor was appointed`, `s 492 who fixes the remuneration` (types), `s 492(1) to (3)` (general) |  |
| s 492(2) | 6883 | encoded | `s 492 way the auditor was appointed`, `s 492 who fixes the remuneration` (types), `s 492(1) to (3)` (general) |  |
| s 492(3) | 6884 | encoded | `s 492 way the auditor was appointed`, `s 492 who fixes the remuneration` (types), `s 492(1) to (3)` (general) |  |
| s 492(4) | 6885 | encoded | `s 492(4)` (general) |  |
| s 492(5) | 6886 | encoded | `s 492(5)` (general) |  |
| s 493 | 6887 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 493(1) | 6888 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(1) closing words (generality of the power) | 6889 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2) | 6890 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2)(a) | 6891 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2)(a)(i) | 6892 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2)(a)(ii) | 6893 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2)(b) | 6894 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2)(c) | 6895 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2)(c)(i) | 6896 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2)(c)(ii) | 6897 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(2)(c)(iii) | 6898 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(3) | 6899 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 493(4) | 6900 | inert (reason 2: machinery) | a regulation-making power about the disclosure of the terms of an auditor's appointment, and the procedure for the regulations (machinery) |  |
| s 494 | 6901 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 494(1) | 6902 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(1)(a) | 6903 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(1)(b) | 6904 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(1) closing words (generality of the power) | 6905 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(2) | 6906 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(2)(a) | 6907 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(2)(b) | 6908 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(2)(c) | 6909 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(3) | 6910 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(3)(a) | 6911 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(3)(b) | 6912 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(3)(c) | 6913 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(3)(d) | 6914 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(4) | 6915 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(4)(a) | 6916 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(4)(b) | 6917 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(4)(c) | 6918 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(5) | 6919 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494(6) | 6920 | inert (reason 2: machinery) | a regulation-making power about the disclosure of services and remuneration, and the procedure for the regulations (machinery) |  |
| s 494ZA | 6921 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 494ZA(1) | 6922 | encoded | `s 494ZA financial year` (type), `s 494ZA(1)` and its helpers (general) | F20 |
| s 494ZA(1)(a) | 6923 | encoded | `s 494ZA financial year` (type), `s 494ZA(1)` and its helpers (general) | F20 |
| s 494ZA(1)(b) | 6924 | encoded | `s 494ZA financial year` (type), `s 494ZA(1)` and its helpers (general) | F20 |
| s 494ZA(1) Table header | 6925 | encoded | `s 494ZA(1)` (general) -- the Table | F20 |
| s 494ZA(1) Table row 1 | 6926 | encoded | `s 494ZA(1)` (general) -- the Table | F20 |
| s 494ZA(1) Table row 2 | 6927 | encoded | `s 494ZA(1)` (general) -- the Table | F20 |
| s 494ZA(1) Table row 3 | 6928 | fork | `s 494ZA(1)` row 3 (general) -- three sub-cases in one raw line (6928); the readings of "the last financial year for which the auditor was appointed following a qualifying selection procedure" differ | F20 |
| s 494ZA(1) Table row 4 | 6929 | encoded | `s 494ZA(1)` (general) -- the Table | F20 |
| s 494ZA(2) | 6930 | encoded | `s 494ZA(2)` (two functions) (general) | F22, F23 |
| s 494ZA(3) | 6931 | encoded | `s 494ZA(3)` (general) |  |
| s 494ZA(4) | 6932 | fork | `s 494ZA(4)(a)` (general) -- "the necessary modifications" are not spelled out | F23 |
| s 494ZA(4)(a) | 6933 | fork | `s 494ZA(4)(a)` (general) -- "the necessary modifications" are not spelled out | F23 |
| s 494ZA(4)(b) | 6934 | encoded | `s 494ZA(4)(a)`, `s 494ZA(4)(b)` (general) | F4, F23 |
| s 494ZA(5) | 6935 | encoded | `s 494ZA(5) compliance of the selection procedure` (type), `s 494ZA(5)` (general) |  |
| s 494ZA(5)(a) | 6936 | encoded | `s 494ZA(5) compliance of the selection procedure` (type), `s 494ZA(5)` (general) |  |
| s 494ZA(5)(a)(i) | 6937 | encoded | `s 494ZA(5) compliance of the selection procedure` (type), `s 494ZA(5)` (general) |  |
| s 494ZA(5)(a)(ii) | 6938 | encoded | `s 494ZA(5) compliance of the selection procedure` (type), `s 494ZA(5)` (general) |  |
| s 494ZA(5)(a)(iii) | 6939 | encoded | `s 494ZA(5) compliance of the selection procedure` (type), `s 494ZA(5)` (general) |  |
| s 494ZA(5)(a)(iv) | 6940 | encoded | `s 494ZA(5) compliance of the selection procedure` (type), `s 494ZA(5)` (general) |  |
| s 494ZA(5)(b) | 6941 | encoded | `s 494ZA(5) compliance of the selection procedure` (type), `s 494ZA(5)` (general) |  |
| s 494A | 6942 | inert (reason 1: not operative) | the section number and title (a heading) |  |
| s 494A lead-in | 6943 | inert (reason 1: not operative) | "In this Chapter—": the lead-in to the definitions (not operative) |  |
| s 494A "audit committee" | 6944 | encoded | `s 494A "audit committee"` (general) | F21 |
| s 494A "audit committee"(a) | 6945 | encoded | `s 494A "audit committee"` (general) | F21 |
| s 494A "audit committee"(a)(i) | 6946 | encoded | `s 494A "audit committee"` (general) | F21 |
| s 494A "audit committee"(a)(ii) | 6947 | encoded | `s 494A "audit committee"` (general) | F21 |
| s 494A "audit committee"(a) closing words (as they have effect on IP completion day) | 6948 | encoded | `s 494A "audit committee"` (general) -- the words that close paragraph (a) | F21 |
| s 494A "audit committee"(b) | 6949 | encoded | `s 494A "audit committee"` (general) | F21 |
| s 494A omitted words (...) | 6950 | repealed or blank in this text | the text shows only "..." (omitted words) | F21 |
| s 494A "Auditor General" | 6951 | encoded | `s 494A "Auditor General"` (general) |  |
| s 494A "Auditor General"(a) | 6952 | encoded | `s 494A "Auditor General"` (general) |  |
| s 494A "Auditor General"(b) | 6953 | encoded | `s 494A "Auditor General"` (general) |  |
| s 494A "Auditor General"(c) | 6954 | encoded | `s 494A "Auditor General"` (general) |  |
| s 494A "Auditor General"(d) | 6955 | encoded | `s 494A "Auditor General"` (general) |  |
| s 494A "issuer" | 6956 | encoded | `s 494A "issuer"` (general): the borrowed answer is an input |  |
| s 494A "network" | 6957 | encoded | `s 494A "network"` (general) |  |
| s 494A "network"(a) | 6958 | encoded | `s 494A "network"` (general) |  |
| s 494A "network"(b) | 6959 | encoded | `s 494A "network"` (general) |  |
| s 494A "network"(c) | 6960 | encoded | `s 494A "network"` (general) |  |
| s 494A "network"(d) | 6961 | encoded | `s 494A "network"` (general) |  |
| s 494A "network"(e) | 6962 | encoded | `s 494A "network"` (general) |  |
| s 494A "network"(f) | 6963 | encoded | `s 494A "network"` (general) |  |
| s 494A "public interest entity" | 6964 | encoded | `s 494A "public interest entity"` (general) | F21 |
| s 494A "public interest entity"(a) | 6965 | encoded | `s 494A "public interest entity"` (general) | F21 |
| s 494A "public interest entity"(b) | 6966 | encoded | `s 494A "public interest entity"` (general) | F21 |
| s 494A "public interest entity"(c) | 6967 | encoded | `s 494A "public interest entity"` (general) | F21 |
| s 494A omitted words (...) [printed again, copy 2] | 6968 | repealed or blank in this text | the text shows only "..." (omitted words) | F21 |
| s 494A omitted words (...) [printed again, copy 3] | 6969 | repealed or blank in this text | the text shows only "..." (omitted words) | F21 |

## Fork register (coa11)

Each entry gives the provision, the function, the reading taken, the other reading, and the text that licenses each.
Sites the 2026-11-05 ruling leaves to the encoder's judgment ("unless" met, a bare "must" not done, "listed in Schedule N", a duty whose "if" or "where" is unmet, "(other than X)", a missing ledger event) carry one entry here for the human reviewer to overrule.

- **F1** (s 477(1), s 479A(1) and (2), s 480(1), s 482(1); `s 477(1) the company is exempt ...`, `s 479A(1)`, `s 479A(2)`, `s 480(1)`, `s 482(1)`, the combiner `s 475(2) to (4)`): Taken: an exemption answers JUST TRUE when its conditions hold and JUST FALSE ("this section gives no exemption on these facts") when they do not, by analogy with the 2026-11-05 ruling (b) on defences ("this section gives no defence on these facts", never "no defence at all"); s 475(1) is written "unless the company ... is exempt from audit under section 477, 479A or 480", so a company in none of the exemptions must get a definite answer ("must be audited"). Other reading: the exemptions are grants ("is exempt", "is entitled") and the brief's grant rule gives NOTHING when the gate fails; then s 475(1) answers NOTHING for every company that is not exempt, which makes "must my accounts be audited" unanswerable for the ordinary case.
- **F2** (s 475(2), printed twice (raw lines 6554 and 6555-6557); `s 475(2) (first printed version) ...`, `s 475(2) (second printed version) ...`): Taken: both printed versions are encoded as separate functions and the seat answers only where they agree (`coa11 seat section 475(2) bar`); the first version asks for "a statement by the directors to that effect" (taken as a statement confirming that the company qualifies), the second for a statement "(a) identifying the exemption in question, and (b) confirming that the company qualifies for the exemption". Other readings: the second version alone is in force (it is the more detailed, and "to that effect" in the first is then what the second spells out), or the first alone is. The text as rendered shows no mark of which is in force, so a statement that confirms the company qualifies but does not identify the exemption answers NOTHING in the seat.
- **F3** ("unless" met: s 475(2), s 475(3), s 479(1)(a), s 483(5), s 485(1), s 485A(4), s 485B(4), s 487(2), s 489(1), s 489A(4), s 489B(4)): Taken: once the "unless" is met the bar or the duty does not apply and the function answers JUST FALSE with the quoted "unless" words in its FALSE-kind comment (a bar function: "not barred"; a duty function: "no duty"). Other reading: NOTHING, because "A is barred unless B" says what happens if B is not met and does not itself say that the bar lifts when B is met.
- **F4** (a bare "must" not done: s 475(4), s 476(2), s 479C(2), s 485A(3), (5), (6), s 485B(3), (4), s 486(2) and s 486A(3) (the "where" gates), s 488(3), s 494ZA(4)(b), and the mirror sections for public companies): Taken: a required content or step that is missing answers JUST FALSE, with the quoted "must" words in the comment. Other reading: NOTHING, because "must" imposes a duty and does not say that a non-compliant notice or recommendation has no effect; where the text names the consequence (s 475(2) and (3): "not entitled ... unless") the JUST FALSE is the text's own.
- **F5** (the four combiners `s 477(5)`, `s 479A(3)`, `s 480(3)`, `s 482(4)` and their helper `s 475(2) to (4) the exemption is in force once the restrictions on it are taken together`): Taken: "This section has effect subject to ..." is read as: the exemption is in force (JUST TRUE) only if its own conditions hold, no bar applies, the directors' statements are on the balance sheet, and (s 475(4)) the statement appears above the signature required by section 414 (a misplaced statement is not "the statement required"); a members' notice under s 476 defeats it; any one of these failing answers JUST FALSE; an unknown input leaves NOTHING. Other reading: JUST TRUE for "entitled" is more than the text says ("is exempt" and "has effect subject to" do not say "is entitled"), and s 475(4) is a separate duty with no stated effect on entitlement; then the combiners answer NOTHING when no restriction applies, or ignore the placement.
- **F6** (counting periods: "the period of 28 days beginning with" (s 485(2)); "within one week of" (ss 486(2), 486A(4), 490(2), 490A(4)); "not later than one month before the end of that year" (s 476(3)); "the period of 4 years beginning with the day after" (ss 485C(1), 489C(1)); "before the end of the accounting reference period" (s 488(3)(c)); "before the end of the accounts meeting" (s 489(2))): Taken: the 28 days run from the first day to the first day plus 27; one week is the day itself to the day plus 7, both ends inclusive; one month before the end of a year is `add months` of minus 1 (31 March gives 28 or 29 February: capped at the end of a shorter month); the 4 years run to the day before the fourth anniversary of the day after; a notice received on the last day of the accounting reference period counts; an appointment made on the day the accounts meeting ends counts (the time of day is not modelled). Other readings: the 28th day, the 8th day, the strictly earlier day (an event "before the end" of a period is before its last day), a month counted as 30 days, an appointment on the day the meeting ends being after its end.
- **F7** (s 476(1), (2), (3); `s 476(1)`, `s 476(2)`, `s 476(3)`): Taken: a notice not given by 10% of the capital, or of a class, or (no share capital) of the members, or given outside the financial year or too late, answers JUST FALSE ("must be given by", "may not be given before ... and must be given not later than one month before the end of that year"); a company that would not otherwise be entitled to an exemption answers NOTHING (the grant is "the members of a company that would otherwise be entitled"). Other reading: NOTHING for a defective notice (the text says how a notice must be given and does not say it has no effect otherwise), and JUST FALSE for a company not otherwise entitled.
- **F8** (s 478, s 479B, s 481; `s 478`, `s 479B`, `s 481`): Taken: bar polarity: JUST TRUE if any listed kind holds at some time in the year; JUST FALSE ("this section does not bar it") when every listed kind is JUST FALSE; NOTHING when a borrowed term (traded company, e-money issuer, MiFID investment firm, UCITS management company: section 474(1)) is not known and no listed kind holds. Each limb is "at some time within the financial year". Other reading: a prohibition limited by its own wording ("if it was at any time within the financial year ... a public company") answers NOTHING outside the limit.
- **F9** (s 479(4); `s 479(4) the two undertakings are associated`, `s 479(4)(b)`): Taken: "undertakings are associated if one is a subsidiary undertaking of the other or both are subsidiary undertakings of a third undertaking" is the definition of the term (an "if" read as closed): JUST FALSE when neither holds. Other reading: NOTHING ("if" does not say "only if").
- **F10** (s 479(3); `s 479(3) subsection (3) applies: the company is not excluded by subsection (1)`): Taken: the function answers whether the "if" of subsection (3) is met (the name is "subsection (3) applies"), so a company that was not both a subsidiary undertaking and dormant throughout answers JUST FALSE (a failed "if" counts as the text's no, clause by clause, within the provision that holds it); s 479(1)(b) takes this answer. The seat cases showed that a function answering only JUST TRUE or NOTHING could not feed s 479(1)(b). Other reading: NOTHING for a company outside the carve-out ("A company is not excluded by subsection (1) if ..." is a grant that says nothing of other companies); s 479(1) would then answer NOTHING whenever the group is not small.
- **F11** (s 479C(1); `s 479C(1) a guarantee is given by the parent undertaking`): Taken: "A guarantee is given ... when the directors ... deliver to the registrar a statement ..." counts "when" as "where" (ruling of 2026-11-05 (c)): JUST FALSE until both limbs hold. Other reading: NOTHING.
- **F12** (s 483(3); `s 483(3)`): Taken: "Those accounts are— (a) ..., (b) ..." closes with no "only": a case in neither answers NOTHING (list not closed). Other reading: JUST FALSE (a list that defines the term).
- **F13** (s 485(3), s 485(4), s 489(3), s 489(4); the "may appoint" functions): Taken: the directors' and members' powers to appoint are grants that name their occasions ("(a) at any time before ..., (b) ..., (c) ..."): outside the named occasions the answer is NOTHING, and a resolution that is not an ordinary resolution also answers NOTHING. Other reading: JUST FALSE (the occasions are the only ones).
- **F14** (s 485A(1), s 485B(1), s 489A(1), s 489B(1); the "section applies" functions): Taken: "This section applies to the appointment ... of a private company— (a) which is also a public interest entity; and (b) which has an audit committee" is a scope limit with no "only" (ruling of 2026-11-05 (c)): outside the scope the answer is NOTHING; an Auditor General answers JUST FALSE (a flat negative). Other reading: JUST FALSE for a company outside the scope ("does not apply").
- **F15** (s 485C(1) and (2), s 489C(1) and (2); `s 485C(1)`, `s 485C(2)`, `s 489C(1)`, `s 489C(2)`): Taken: the functions are named as bars; a year that begins outside the 4 years, a company that is not a public interest entity, or a person who was not auditor for every year of the maximum engagement period answers JUST FALSE ("the bar does not catch it"); an Auditor General answers JUST FALSE (s 485C(3)). Other reading: NOTHING outside the stated period or class (a prohibition limited by its own wording, the brief's grant-and-prohibition rule).
- **F16** (s 483(1), s 486(1), s 486A(1), s 490(1), s 490A(1); the Secretary of State's and the Scottish Ministers' powers): Taken: a power given on stated facts ("If a private company fails to appoint ..., the Secretary of State may appoint") answers NOTHING when the facts are not there; s 483(1) answers JUST FALSE where it appears to the Ministers that neither (2)(a) nor (2)(b) holds ("only if it appears"). Other reading: JUST FALSE ("the Secretary of State may not appoint") on a failed gate; that reads a grant as its own prohibition.
- **F17** (s 487(2); `s 487(2) the auditor in office is deemed to be re-appointed`): Taken: a deeming rule whose "Where" fails, or whose "unless" exceptions (a) to (f) are met, answers JUST FALSE ("is not deemed"). Other reading: NOTHING (the deeming is a grant of a status limited by its own wording).
- **F18** (s 488(2); `s 488(2) the requisite percentage`): Taken: "5%, or such lower percentage as is specified for this purpose in the company's articles": an articles percentage that is not lower than 5% is not "such lower percentage", so 5% stays. Other reading: the articles' figure governs whatever it is.
- **F19** (s 489(2), s 491(1)(b); `s 489(2)`, `s 491(1)(b)`): Taken: the accounts meeting is modelled by the day it ends (s 489(2), an input from section 437) and by a yes or no "has the meeting concluded" (s 491(1)(b)). Other reading: a date and time of day, so that a same-day appointment can be before or after the end of the meeting.
- **F20** (s 494ZA(1), the Table (raw line 6928 holds three sub-cases of row 3 in one line); `s 494ZA(1) the last financial year of the maximum engagement period` and its helpers): Taken: the company's financial years are supplied as a list in date order whose first element is the first year of the maximum engagement period; an answer is NOTHING until the list reaches a year beginning on or after each cut-off the Table uses; the last qualifying year for sub-case (ii) is the last such year beginning before 17 June 2016, and for sub-case (iii) and row 4 the last such year in the list. Read with "the last financial year for which the auditor was appointed following a qualifying selection procedure" meaning the last year in the list for sub-case (iii) and row 4 but the last year before 17 June 2016 for the trigger of sub-case (ii), so that paragraph (b) of sub-case (ii) ("unless the auditor is appointed following a qualifying selection procedure for the first financial year ... on or after 17 June 2016") can operate. Other reading: the same last year for both, in which case (ii)(b) can never apply (a year flagged for 2017 would make the ten years from it end after 17 June 2016); finding 7. The seat question also assumes each financial year begins on the same day of every calendar year.
- **F21** (s 494A, the omitted words after "audit committee" (raw line 6950) and after paragraph (c) of "public interest entity" (raw lines 6968 and 6969); `s 494A "audit committee"`, `s 494A "public interest entity"`): Taken: the "..." marks words omitted from the consolidated text (repealed or omitted by amendment), so the definitions that "mean" a closed list answer JUST FALSE for a case outside it. Other reading: NOTHING, because the omitted words may have held further limbs.
- **F22** (s 494ZA(2) and (3); `s 494ZA(2) the maximum engagement period may be extended by the period`, `s 494ZA(3)`): Taken: an extension of more than 2 years ("no more than 2 years"), one without the competent authority's approval ("with the approval of the competent authority"), or one whose approval the authority could not give (it is not satisfied that exceptional circumstances exist: "only if it is satisfied", s 494ZA(3)) answers JUST FALSE; a first year before 17 June 2003 answers NOTHING ("Where ... begins on or after 17 June 2003"). Other reading: NOTHING for a failed approval.
- **F23** (s 494ZA(2) and (4)(a); `s 494ZA(2) the last day of the maximum engagement period as extended`, `s 494ZA(4)(a)`): Taken: the extension moves the end of the period later by the approved number of years (`add years`, capped at the end of a shorter month); "the second column of the Table has effect with the necessary modifications" answers NOTHING because the modifications are not spelled out. Other reading: the Table's second column is recomputed with the extended end date; the text does not say how.
- **F24** (s 485(5), s 489(5); `s 485(5)`, `s 489(5)`): Taken: "may only be appointed— (a) in accordance with this section, or (b) in accordance with section 486 or 486A": a route outside the two answers JUST FALSE (closed with "only"); JUST TRUE on a listed route says only that this subsection does not bar it; a deemed re-appointment answers NOTHING ("without prejudice"). Other reading: JUST TRUE for a listed route reads a limit as a grant; or JUST FALSE for a deemed re-appointment.
- **F25** (the seat question on s 475(1)): Taken: the question takes the answer of each exemption question (yes, no, not sure) as an input, because s 475(1) is itself written in terms of those exemptions ("unless the company is exempt under ...") and a single question with the union of their facts would have about 80 inputs. Other reading: one question with every fact of the four exemptions.
- **F26** (the brief against PLAN.md (see "Source" above)): Taken: the brief governs; the modules import `coa-core` only and take keel answers as inputs. Other reading: import `coa-definitions` and call its functions (the brief's wording); not done because the part cannot import another part and the keel's functions are only seams here.
- **F27** (s 485(2), s 489(2) "(other than the company's first financial year)"; `s 485(2) the appointment is made before the end of the period for appointing auditors`): Taken: the company's first financial year answers NOTHING (the "(other than X)" site of the 2026-11-05 ruling). Other reading: JUST FALSE, because the carve-out removes the first year from the rule and the section then says nothing of it; NOTHING is the same words as "not covered".
- **F28** (name-test sweep of 2026-11-12, group (ii) "entitled": `s 477(5) the company is entitled to the exemption conferred by section 477`, and its seat question `Under section 477, is my company entitled to the small companies exemption from audit for the year`): Taken: not flipped, so it keeps JUST FALSE where the exemption's own condition or a restriction on it fails (forks F1, F5). An "entitled"-named function states a claim, not a power, and the Guide's line on grants does not settle it; whether it goes with the grants (NOTHING) is ASSUMED, NOT RULED, a question for the maintainer or a lawyer, not one to settle by sweep. Other reading: NOTHING on a failed condition.
- **F29** (name-test sweep of 2026-11-12, group (ii) "entitled": `s 479A(3) the company is entitled to the exemption conferred by section 479A`, and its seat question `Under section 479A, is my company entitled to the subsidiary companies exemption from the audit of its individual accounts for the year`): Taken: not flipped, so it keeps JUST FALSE where the exemption's own condition or a restriction on it fails (forks F1, F5). An "entitled"-named function states a claim, not a power, and the Guide's line on grants does not settle it; whether it goes with the grants (NOTHING) is ASSUMED, NOT RULED, a question for the maintainer or a lawyer, not one to settle by sweep. Other reading: NOTHING on a failed condition.
- **F30** (name-test sweep of 2026-11-12, group (ii) "entitled": `s 480(3) the company is entitled to the exemption conferred by section 480`, and its seat question `Under section 480, is my company entitled to the dormant companies exemption from audit for the year`): Taken: not flipped, so it keeps JUST FALSE where the exemption's own condition or a restriction on it fails (forks F1, F5). An "entitled"-named function states a claim, not a power, and the Guide's line on grants does not settle it; whether it goes with the grants (NOTHING) is ASSUMED, NOT RULED, a question for the maintainer or a lawyer, not one to settle by sweep. Other reading: NOTHING on a failed condition.
- **F31** (name-test sweep of 2026-11-12, group (ii) "entitled": `s 482(4) the company is entitled to the exemption conferred by section 482`, and its seat question `Under section 482, is my company entitled to the exemption from audit for non-profit-making companies subject to public sector audit for the year`): Taken: not flipped, so it keeps JUST FALSE where the exemption's own condition or a restriction on it fails (forks F1, F5). An "entitled"-named function states a claim, not a power, and the Guide's line on grants does not settle it; whether it goes with the grants (NOTHING) is ASSUMED, NOT RULED, a question for the maintainer or a lawyer, not one to settle by sweep. Other reading: NOTHING on a failed condition.
- **F32** (name-test sweep of 2026-11-12, group (i) "may" with a where/when/upon-kind gate: `s 494ZA(2) the maximum engagement period may be extended by the period`, and its seat question `Under section 494ZA(2), may the maximum engagement period of my company's auditor be extended by the period I have in mind`): Taken: not flipped. The extension is a grant ("may be extended") and its answer is JUST FALSE for an extension without the competent authority's approval ("with the approval of the competent authority"), a condition of the same kind as "on payment" or "on such an application"; the sweep ASSUMES, NOT RULES, that such equivalents go with the listed group, and ruling (b) of the Guide's "Periods, where and scope limits" paragraph (JUST FALSE) points the other way from its line on grants, so this is a question for the maintainer or a lawyer, not one to settle by sweep. The branch for an extension of more than 2 years stays JUST FALSE as a cap in the text's own words ("no more than 2 years"), and the "Where ... begins on or after 17 June 2003" gate already answers NOTHING (fork F22). Other reading: NOTHING for a failed approval (fork F22 records the same reading for the approval branch).

### The rulings of 2026-11-04 and 2026-11-05, recorded word for word

Copied from the brief (which copies section 2 of `docs/design-question-false-or-nothing.md` and `inputs/ENCODING-GUIDE.md` section 5); each is the rule that this row's `NOTHING-kind` tags rest on.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

### Name-test sweep of 2026-11-12

The sweep (`instructions/name-test-sweep.md`) reads every function whose name contains "may", "permitted", "power", "entitled" or "authorised".
A case-insensitive search of every top-level name in the four layer-1 modules finds 21; none contains "permitted", "authorised" or "lawful".
Result: no function is named for a grant or a power and answers JUST FALSE because an "IF" gate failed, so none was flipped and no layer-1 `.l4` file changed.
The counts below are layer-1 functions.
The 14 seat questions with the same words in their names (8 "may", 4 "entitled", 2 "power") each return the answer of the layer-1 function they call, unchanged, so each follows the row of that function; the four "entitled" ones and the 494ZA(2) one are named in the rows F28 to F32 of the fork register.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 0 | 6 | 1 | 4 |

- **Flipped to NOTHING:** none.
- **Kept JUST FALSE** (6):
  - `s 476(1) the members may by notice require the company to obtain an audit ...`: the text closes the gate in its own words ("The notice may not be given before the financial year to which it relates and must be given not later than one month before the end of that year", subsection (3); "The notice must be given by" members representing 10%, subsection (2)); the other reading, NOTHING for a defective notice, is fork F7.
  - `s 483(1) the Scottish Ministers may by order provide ...`: the text closes the gate itself ("may be made in relation to a company only if it appears to the Scottish Ministers").
  - `s 483(5) the order may not yet be made`: a bar ("shall not be made unless"), and its JUST FALSE is the case where the unless is met.
  - `s 486(2) the company must give the Secretary of State notice that his power has become exercisable` and `s 490(2) ...`: duties, not grants; the word "power" is the Secretary of State's, and a duty whose "where" gate fails answers JUST FALSE by the ruling of 2026-11-05 (b).
  - `s 494ZA(3) the competent authority may give its approval`: the text closes the gate itself ("only if it is satisfied that exceptional circumstances exist").
- **Listed: "may" with a where/when/upon-kind gate that answers JUST FALSE** (1): `s 494ZA(2) the maximum engagement period may be extended by the period` (F32).
  Its JUST FALSE for an extension without approval rests on "with the approval of the competent authority", which is of the kind of "on payment" and "on such an application"; ASSUMED, NOT RULED that it goes with this group.
  Its branch for an extension of more than 2 years stays JUST FALSE as a cap in the text's own words ("no more than 2 years"), and its "Where ... begins on or after 17 June 2003" gate already answers NOTHING.
  Nine other functions named for a grant or a power already answer NOTHING when their gate fails, so they need no row here: `s 479C(3)(b)`, `s 485(3)`, `s 485(4)`, `s 486(1)`, `s 486A(1)`, `s 489(3)`, `s 489(4)`, `s 490(1)` and `s 490A(1)`.
  Forks F13 and F16 record the other reading for the last eight of those; `s 479C(3)(b)` takes the same Guide line and has no fork row of its own.
- **Listed: "entitled"** (4, one row each in the fork register above): `s 477(5)` (F28), `s 479A(3)` (F29), `s 480(3)` (F30), `s 482(4)` (F31).
- `s 476(3) the last day on which the notice may be given` is the 21st name; it returns a date, so it answers neither JUST FALSE nor NOTHING.
- The 21 names are accounted for: 6 kept + 1 listed (may) + 4 listed (entitled) + 9 already NOTHING + 1 date function = 21.
- **Outside the sweep: named "it is lawful":** 0.

### Reading a result: FALSE and NOTHING (coa11)

The rule of 2026-10-29 (assumed, not ruled by a lawyer) as it reads in Part 16.
- `JUST TRUE`: the text says the case is within what the function's name asks: the company must have its accounts audited, the exemption is in force, the member may appoint, the person is barred, the notice was given in time, the offence is committed.
- `JUST FALSE` ("a no"): the text says no in its own words: a "means" definition ("“network” means ..."), a condition introduced with "if", "only if", "unless" or "where" that is not met ("is exempt ... if", "may be given by the competent authority only if it is satisfied" (s 494ZA(3)), "Where subsection (2) of section 485 applies ..."), a period the text fixes in its own words ("within one week", "not later than one month before the end of that year"), or a flat negative ("is not entitled", "may not be appointed", "does not apply", "does not invalidate"). Each such branch carries `-- FALSE-kind (the text says no in its own words): "..."`. In this Part the polarity of the name decides what the no means: for a bar it means "the bar does not catch this case", for an exemption "this section gives no exemption on these facts", for a duty "no duty arises".
- `NOTHING` ("not covered"): the text does not decide: it lists without closing the list (s 483(3)), says "includes" (s 492(4)), leaves a term undefined ("the necessary modifications", s 494ZA(4)(a)), points outside the sources (Article 16 of the Audit Regulation, the Financial Services and Markets Act 2000, sections 382 to 384 and 474, which are other parts' ranges), is silent, or limits a grant or prohibition in its own wording and the case falls outside the limit ("the members of a company that would otherwise be entitled", "the company's first financial year"). Each such branch carries `-- NOTHING-kind (<why>)`, <why> being one of silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- A caller must never turn `NOTHING` into `FALSE`. The seat and the combiners keep NOTHING as NOTHING; where a seat input is a "yes, no, not sure" answer (s 475(1)), "not sure" becomes NOTHING.
- `REFUSE` is not used: "not covered" is `NOTHING` or a named constructor, and is asserted in the tests.

## Marginal readings for a lawyer (coa11)

The two readings the brief marks "for a lawyer": (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (and flat negatives count as the text saying no); (b) a prohibition or grant limited by its own wording does not (the case outside the limit answers NOTHING). Every branch below rests on one of them; the other reading is stated.

| function | branch | rests on | the other reading |
| --- | --- | --- | --- |
| `s 477(1)`, `s 479A(1)`, `s 479A(2)`, `s 480(1)`, `s 480(2)`, `s 482(1)` | JUST FALSE when the conditions of the exemption fail | (a), by analogy with ruling 2026-11-05 (b) (F1) | NOTHING (a grant limited by its own wording) |
| `s 475(2)`, `s 475(3)`, `s 479(1)`, `s 483(5)`, `s 485A(4)`, `s 485B(4)`, `s 487(2)`, `s 489A(4)`, `s 489B(4)` | JUST FALSE when the "unless" is met | (a) (F3) | NOTHING |
| `s 475(4)`, `s 476(2)`, `s 476(3)`, `s 479C(2)`, `s 485A(5)`, `s 485A(6)`, `s 485B(4)`, `s 488(3)`, `s 494ZA(4)(b)` | JUST FALSE where a "must" is not done | (a): the 2026-11-05 case-by-case ruling (F4) | NOTHING |
| `s 478`, `s 479B`, `s 481`, `s 485C(1)`, `s 485C(2)`, `s 489C(1)`, `s 489C(2)`, `s 479(1)` | JUST FALSE when the bar does not catch the case | (a): "is not entitled ... if" (F8, F15) | NOTHING (a prohibition limited by its own wording) |
| `s 479(3)`, `s 479(4)` | JUST FALSE when the "if" of the definition or carve-out is not met | (a) (F9, F10) | NOTHING |
| `s 476(1)` | NOTHING for a company not otherwise entitled; JUST FALSE for a notice defective in form or time | (b) and (a) (F7) | JUST FALSE and NOTHING respectively |
| `s 483(1)`, `s 486(1)`, `s 486A(1)`, `s 490(1)`, `s 490A(1)`, `s 485(3)`, `s 485(4)`, `s 489(3)`, `s 489(4)` | NOTHING outside the stated facts or occasions | (b) (F13, F16) | JUST FALSE |
| `s 485A(1)`, `s 485B(1)`, `s 489A(1)`, `s 489B(1)` | NOTHING for a company outside the stated scope | (b), and ruling 2026-11-05 (c) (F14) | JUST FALSE |
| `s 486(2)` (duty), `s 486A(3)`, `s 487(2)`, `s 490(2)`, `s 490A(3)` | JUST FALSE where the "Where" gate is not met | ruling 2026-11-05 (b) (F4, F17) | NOTHING |
| `s 486(2)` (timing), `s 486A(4)` (timing), `s 487(1)(b)`, `s 490(2)` (timing), `s 490A(4)` (timing), `s 491(1)(b)`, `s 485(2)`, `s 489(2)` | JUST FALSE outside the period the text fixes | ruling 2026-11-05 (a) (F6) | NOTHING |
| `s 486(3)(a)`, `s 486(3)(b)`, `s 486A(5)(a)`, `s 486A(5)(b)`, `s 490(3)`, `s 490A(5)` | JUST FALSE when the company has not failed to give the notice, or the officer is not in default | (a): "If a company fails ..., an offence is committed by" and flat limbs | NOTHING |
| `s 486A(2)`, `s 487(3)`, `s 487(4)`, `s 490A(2)`, `s 491(2)` | JUST FALSE for the matter the flat negative names; NOTHING for any other | (a) for the flat negative, (b) for the rest | JUST FALSE for the rest |
| `s 487(1)(a)`, `s 491(1)(a)` | JUST TRUE before the previous auditors cease, JUST FALSE after | ruling 2026-11-05 (d) (the "until" bar) | none: the ruling covers it |
| `s 488(1)` | JUST FALSE when the members' notices fall below the requisite percentage | (a) ("is not deemed to be re-appointed if ... at least") | NOTHING |
| `s 492(1) to (3)`, `s 492(4)`, `s 492(5)` | a "not covered" constructor or NOTHING outside the named ways of appointment, expenses, benefits in kind | (b) and "includes" (list not closed) | JUST FALSE |
| `s 494ZA(2)`, `s 494ZA(3)` | JUST FALSE for an extension over 2 years, without approval, or without exceptional circumstances; NOTHING before 17 June 2003 | (a) "no more than 2 years" and "with the approval of the competent authority" (s 494ZA(2)) and "only if it is satisfied" (s 494ZA(3)); (b) "Where ... begins on or after 17 June 2003" (F22; the approval branch of s 494ZA(2) is also listed in F32) | NOTHING for a failed approval |
| `s 494A "audit committee"`, `"Auditor General"`, `"network"`, `"public interest entity"` | JUST FALSE for a case outside the closed "means" list | "means" (the text says no in its own words); F21 on the omitted words | NOTHING |
| `s 475(1)` | JUST FALSE when an exemption applies; JUST TRUE when none does | (a): "unless the company ... is exempt" (F1, F3) | NOTHING |

## Jural relations (coa11)

Hohfeld's correlatives, stated once per provision as a relation between two parties and named neutrally.
Where the text names no counterparty the cell says "none named" and the relation is still stated for the party the text does name.
A definition or a counting rule creates no relation: listed once as `none`.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| Part 16 and Chapter headings, cross-headings, section numbers and titles | none | none | (inert) |
| s 475(1) accounts must be audited | none named (members, creditors, the registrar) | the company: duty to have its annual accounts audited unless exempt | `s 475(1)` (ch1) |
| s 475(2), (3) no exemption without the directors' statements | none named | the company: disability (it cannot claim the exemption) until the statements are on the balance sheet | `s 475(2) ...`, `s 475(3)` (ch1) |
| s 475(4) where the statement must appear | none named | the directors: duty to place the statement above the section 414 signature | `s 475(4)` (ch1) |
| s 476 members' notice requiring an audit | members holding 10% (power) | the company: liability to be required to obtain an audit | `s 476(1)`, `s 476(2)`, `s 476(3)` (ch1) |
| s 477(1), (5) small companies exemption | a small company: immunity from the audit requirement | whoever could require an audit under Part 16: disability (none named) | `s 477(1)`, `s 477(5)` (ch1) |
| s 477(4)(a) smallness determined under section 382 | none | none | input of `s 477(1)` |
| s 478, s 479(1), s 479B, s 481 companies excluded | none named | the excluded company: disability (no exemption) | `s 478`, `s 479(1)`, `s 479B`, `s 481` (ch1) |
| s 479(3), (4), (5), (6) carve-out, group, associated undertakings | none | none (definitions and a carve-out of the bar of s 479(1)) | `s 479(3)`, `s 479(4)(a)`, `s 479(4)`, `s 479(4)(b)`, `s 479(6)` (ch1) |
| s 479A(1), (2), (3) subsidiary companies exemption | the subsidiary company: immunity from the audit of its individual accounts | whoever could require that audit: disability (none named) | `s 479A(1)`, `s 479A(2)`, `s 479A(3)` (ch1) |
| s 479A(2)(e) delivery to the registrar | the registrar: claim | the directors of the company: duty to deliver five documents on or before the filing date | `s 479A(2)(e) ...` (ch1) |
| s 479C(1), (2) the parent undertaking's statement | the subsidiary (condition of its exemption) | the parent undertaking and the directors: duty to deliver an authenticated statement with the listed particulars | `s 479C(1)`, `s 479C(2)` (ch1) |
| s 479C(3) effect of the guarantee | any person to whom the subsidiary is liable: claim | the parent undertaking: duty to meet the outstanding liabilities until satisfied | `s 479C(3)(a)`, `s 479C(3)(b)` (ch1) |
| s 480 dormant companies exemption | a dormant company: immunity from the audit requirement | whoever could require an audit: disability (none named) | `s 480(1)`, `s 480(2)`, `s 480(3)` (ch1) |
| s 482 public sector audit | a non-profit-making company audited by a public sector auditor: immunity | whoever could require an audit under Part 16: disability (none named) | `s 482(1)`, `s 482(4)` (ch1) |
| s 483(1), (2), (5) order of the Scottish Ministers | the Scottish Ministers: power | a company with its registered office in Scotland: liability to have its accounts audited by the Auditor General for Scotland | `s 483(1)`, `s 483(5)` (ch1) |
| s 483(3), (4); s 484; ss 493, 494 | none | none (definition; machinery) | `s 483(3)` (ch1); the rest inert |
| s 485(1) an auditor must be appointed | none named | the company: duty to appoint for each financial year | `s 485(1)` (private) |
| s 485(2) period for appointing auditors | none named | the company: duty to appoint before the end of the period | `s 485(2) ...` (private) |
| s 485(3) the directors may appoint | the directors: power | the company: liability to an appointment by the directors | `s 485(3)` (private) |
| s 485(4) the members may appoint | the members: power (by ordinary resolution) | the company: liability to an appointment by the members | `s 485(4)` (private) |
| s 485(5) only the routes the section allows | the company: immunity from any other appointment | whoever would appoint otherwise: disability | `s 485(5)` (private) |
| s 485A(3) the audit committee recommends, the directors propose | the directors (claim to the recommendation); none named for the proposal | the audit committee: duty to recommend; the directors: duty to propose | `s 485A(3)(a)`, `s 485A(3)(b)`, `s 485A(3)` (private) |
| s 485A(4), (5), (6), (7) | none named | the audit committee: duty to select by procedure and to give the recommendation its content; the directors: duty on the content of the proposal | `s 485A(4)`, `s 485A(5)`, `s 485A(6)` (private) |
| s 485B(3), (4), (5) | none named | the directors: duty to propose and to carry out a selection procedure | `s 485B(3)`, `s 485B(4)` (private) |
| s 485C(1), (2), (3) restriction on appointment | a person who has been auditor for the whole maximum engagement period, and a member of the same network: none (they bear the disability) | the company: disability (it cannot validly appoint them for a year beginning within the four years) | `s 485C(1)`, `s 485C(2)` (private) |
| s 486(1) default power | the Secretary of State: power | a private company that fails to appoint: liability to an appointment | `s 486(1)` (private) |
| s 486(2) notice to the Secretary of State | the Secretary of State: claim to the notice | the company: duty to give it within one week | `s 486(2)` (private; three functions) |
| s 486(3), (4) offence and penalty | the prosecuting authority: power (none named) | the company and every officer in default: liability to a fine | `s 486(3)(a)`, `s 486(3)(b)`, `s 486(4)` (private) |
| s 486A(1) power on a defective appointment | the Secretary of State: power | the company: liability to the replacement of its auditor | `s 486A(1)` (private) |
| s 486A(2) reports stay valid | the company (and those who rely on the report): immunity from invalidity | none named: disability | `s 486A(2)` (private) |
| s 486A(3) second audit | the Secretary of State: power under ss 1248 and 1249 | the company: liability | `s 486A(3)` (private) |
| s 486A(4)-(6) notice, offence, penalty | the Secretary of State (claim to the notice); the prosecuting authority | the company, and every officer in default | `s 486A(4)` (rule and timing), `s 486A(5)(a)`, `s 486A(5)(b)`, `s 486A(6)` (private) |
| s 487(1) term of office | none | none (a rule about when an appointment takes effect and ends) | `s 487(1)(a)`, `s 487(1)(b)` (private) |
| s 487(2) deemed re-appointment | the auditor in office: privilege to continue | the company: no-right to treat the office as ended | `s 487(2)` (private) |
| s 487(3) removal and resignation saved | none | none (a saving) | `s 487(3)` (private) |
| s 487(4) no compensation for the lost opportunity | the company: immunity | the auditor: disability (cannot recover for the loss) | `s 487(4)` (private) |
| s 488 members prevent deemed re-appointment | the members (5% or the articles' lower figure): power by notice | the auditor: liability not to be deemed re-appointed | `s 488(1)`, `s 488(2)`, `s 488(3)` (private) |
| s 489(1) to (5) appointing the auditor of a public company | as s 485(1) to (5), with the accounts meeting for the period for appointing auditors: none named (s 489(1), (2)); the directors (power, s 489(3)); the members (power, s 489(4)) | the company: duty to appoint; liability to appointment by the directors or the members | `s 489(1)`, `s 489(2)`, `s 489(3)`, `s 489(4)`, `s 489(5)` (public) |
| s 489A, s 489B, s 489C (public interest entities) | as ss 485A, 485B, 485C (the directors; none named; a person who has been auditor and a member of the same network bear the disability) | the audit committee and the directors: duties on the recommendation, the proposal and the selection procedure; the company: disability under s 489C | `s 489A(1)` to `s 489C(2)` (public) |
| s 490, s 490A default power, notice, offence, penalty | the Secretary of State: power and claim to the notice; the prosecuting authority: power (none named) | the public company: liability to an appointment and duty to give notice within one week; the company and every officer in default: liability to a fine | `s 490(1)` to `s 490(4)`, `s 490A(1)` to `s 490A(6)` (public) |
| s 491 term of office of a public company's auditor | none | none (a rule about when an appointment takes effect and ends; there is no deemed re-appointment and no counterpart of s 488) | `s 491(1)(a)`, `s 491(1)(b)`, `s 491(2)` (public) |
| s 492 who fixes the remuneration | none named (the auditor is affected) | the members (by ordinary resolution), the directors, or the Secretary of State: duty to fix it | `s 492(1) to (3)` (general) |
| s 492(4), (5) remuneration includes expenses; benefits in kind | none | none (definitions) | `s 492(4)`, `s 492(5)` (general) |
| s 494ZA(1) maximum engagement period | the company and the audit market: none named | the auditor: disability (cannot continue after the period) | `s 494ZA(1)` (general) |
| s 494ZA(2), (3), (4) extension | the competent authority: power to approve an extension (only if exceptional circumstances) | the auditor and the company: liability to the longer period; duty to appoint after a qualifying selection procedure at the end | `s 494ZA(2)`, `s 494ZA(3)`, `s 494ZA(4)(b)` (general) |
| s 494ZA(5), s 494A definitions | none | none (definitions) | `s 494ZA(5)`, `s 494A "..."` (general) |

## Seams (coa11)

Each seam is an input named for the section that answers it (PLAN.md section 4); the lead wires the answering part's function at the merge.

| input (as the modules name it) | answering section (part) | where taken | type |
| --- | --- | --- | --- |
| `s 382 the company qualifies as a small company in relation to the financial year` | s 382 (coa8) | `s 477(1)` | MAYBE BOOLEAN |
| `s 383 the group qualifies as a small group in relation to the financial year` | s 383 (coa8) | `s 479(1)` | MAYBE BOOLEAN |
| `s 384(2) and (3) the group was at some time in the year an ineligible group` | s 384 (coa8) | `s 479(1)` | MAYBE BOOLEAN |
| `s 381 the company is entitled to prepare accounts in accordance with the small companies regime ...` | ss 381 to 384 (coa8) | `s 480(2)` | MAYBE BOOLEAN |
| `s 474(1) was at some time within the financial year a traded company`; `s 474 ... an e-money issuer`, `... a MiFID investment firm`, `... a UCITS management company` | s 474(1) (coa10) | `s 479B`, `s 481`, `s 478` | MAYBE BOOLEAN |
| "UK-adopted international accounting standards (within the meaning given by section 474(1))" | s 474(1) (coa10) | `s 479A(2)` | BOOLEAN (a fact the person can state) |
| `s 423 the day on which copies ... are sent out`; `s 424 the end of the time allowed for sending out copies ...` | ss 423, 424 (coa9) | `s 485(2)` | MAYBE DATE; DATE |
| `s 437 the day the accounts meeting ... ends` | s 437 (coa9) | `s 489(2)` | DATE |
| `s 282 the resolution is an ordinary resolution` | s 282 (coa7) | `s 485(4)`, `s 489(4)` | MAYBE BOOLEAN |
| `s 1121 the officer is in default` | s 1121 (coa24) | `s 486(3)(b)`, `s 486A(5)(b)`, `s 490(3)(b)`, `s 490A(5)(b)` | MAYBE BOOLEAN |
| `s 1173(1) the company is a parent company`; `s 1162 the company is a subsidiary undertaking` | s 1173(1), s 1162 (keel) | `s 479(4)(a)` | MAYBE BOOLEAN |
| "public company (section 4(2))", "private company (section 4(1))" | s 4 (keel) | `s 478`, `s 485(1)`, `s 489(1)`, `s 485A(1)` and the mirror sections | BOOLEAN suffices |
| "authorised insurance company (section 1165(2))", "banking company (section 1164(2))", "insurance market activity (section 1165)" | ss 1164, 1165 (keel) | `s 478`, `s 479B`, `s 481` | BOOLEAN suffices |
| "dormant" (`s 1169(1) the company has been dormant ...`) | s 1169 (keel) | `s 480(1)`, `s 479(3)` | MAYBE BOOLEAN |
| "signature required by section 414" | s 414 (coa8) | `s 475(4)` (a plain fact: the statement is above that signature) | BOOLEAN |
| ss 1248 and 1249 (Secretary of State's power to require a second audit) | ss 1248, 1249 (coa27) | `s 486A(3)`, `s 490A(3)` (they say the sections "apply as if"; the function answers whether that deeming operates) | JUST TRUE / JUST FALSE |
| `s 494A "public interest entity"`, `s 494A "audit committee"` | this part (s 494A) | `s 485A(1)`, `s 485B(1)`, `s 489A(1)`, `s 489B(1)`, `s 494ZA(5)` | MAYBE BOOLEAN |

Seams the plan lists that are false positives of its script (they are not cross-references to another part): s 478 and s 479B cite `section 117(1)` of the Trade Union and Labour Relations (Consolidation) Act 1992 (not s 117 of this Act, coa3) and the Pension Schemes Acts (not "Part 1" of this Act, keel); ss 482 and 483 cite `section 21` of the Public Finance and Accountability (Scotland) Act 2000 (not s 21 of this Act, coa1).
Answers this part gives to others: PLAN.md section 6 lists "period for appointing auditors, in relation to a private company | section 485(2)": `s 485(2) the period for appointing auditors` returns the record `s 485(2) period for appointing auditors` (first day and last day); the public-company counterpart is the accounts meeting (s 489(2)). `s 494A "public interest entity"`, `"audit committee"`, `"network"`, `"Auditor General"` and `s 494ZA(1) the last financial year of the maximum engagement period` are the other answers other parts may ask for (the Act's own index, Schedule 8, names ss 494A and 494ZA).
The inputs of ss 478, 479B, 481, 485(1), 485A(1), 489(1) and the mirror sections that the plan would name `s 4(2) the company is a public company`, `s 1164(2) ...` and `s 1165(2) ...` are spelled "... (section 4(2))" and "was at some time within the financial year ..." because the asking section quantifies over the whole financial year ("at any time within the financial year in question"), so each is not the keel's point-in-time answer: the lead cannot wire them one to one to the keel's functions, and a caller must combine the keel's answer over the year (the company was a public company, an authorised insurance company, a banking company, ... at some time in it).
The helper names `coa11 seat ...` and `coa11 test ...` begin with the part id and not a section label because they are not provisions (the seat's yes/no/not-sure type and its input builders, and the tests' fixtures); the part id keeps them unique across the 30 parts.
A seam seen only from the plan: s 539 (cited by s 484, which is inert) and ss 1248 and 1249 (cited by ss 486A(3) and 490A(3)) are not taken as inputs because the function that cites them does not need their answers.

## What the text turns out to say (findings)

1. **s 475(2) is printed twice** (raw lines 6554 and 6555-6557) with different words ("to that effect" against "(a) identifying the exemption in question, and (b) confirming that the company qualifies for the exemption"), with no mark of which is in force. Both are encoded (fork F2); the seat answers only where they agree.
2. **The text shows omitted words as "..."**: in s 485A(3)(b) and (4), s 486(1), s 489A(3)(b) and (4), s 490(1), after the definition of "audit committee" (raw line 6950) and after paragraph (c) of "public interest entity" (raw lines 6968, 6969), and shows repealed provisions as ". . . ." (477(2), (3), (4)(b); 479(2), (5)(c)-(e); 479C(2)(c); 487(1A)-(1E); 487A; 491(1A)-(1E); 491A). The encoding follows the words as shown.
3. **s 489B(4)(a) prints "Directive 2003/71/EU"** where the neighbouring provisions print "Directive 2003/71/EC". The function and the seat input keep each as printed.
4. **s 479C(2)(b) says "(if any)"**: a parent undertaking with no registered number need not give one; encoded and tested on both sides (`s 479C(2)`).
5. **s 475(3) is narrower than s 475(2)**: subsection (2) speaks of "any such exemption" (the four of subsection (1), including section 482) and subsection (3) of "any of the provisions mentioned in subsection (1)(a)" (sections 477, 479A and 480 only), so s 475(3) answers NOTHING for section 482.
6. **s 477(1) exempts from "the audit of accounts" and s 479A(1) only from "the audit of individual accounts"**: section 479A says nothing of the audit of group accounts; encoded as the text has it.
7. **The Table in s 494ZA(1), sub-case (ii)(b), cannot operate if "the last financial year ... for which the auditor was appointed following a qualifying selection procedure" is the last such year of all**: a qualifying procedure for the first year after 17 June 2016 would itself be that last year, and the ten years from it would end after 17 June 2016, so the case (ii) would not arise. The encoding reads the trigger of (ii) as the last such year before 17 June 2016 (fork F20).
8. **Raw line 6928 holds three sub-cases of row 3 of the Table in one line** (the converter joined them); the units script counts it as one raw line with three sub-cases in one row, and the encoding handles them in `s 494ZA(1) the Table applied to the first financial year`.
9. **s 483(3)(b) refers back to "an order under this section"** and s 482(1)(b)(ii) to "an order under section 483": s 483(2)(b) and (3)(b) let an order be made in relation to a company funded from a body whose accounts are audited under an order under the same section; encoded as given.
10. **A test expectation corrected on re-reading the text.** In `coa11-tests-ch1.l4` I first wrote NOTHING for `s 479(1)` with the group status unknown and limb (a) met; reading the text again ("unless (a) the group qualifies as small and was not ineligible"), the bar is lifted whether or not the company is a group company, so the answer is JUST FALSE, which is what the code gave. The expectation was wrong, not the code; the corrected assertion and a new one for the case where (a) is not met are in the file.
11. **A wiring defect found by the seat cases.** `s 479(3)` first answered only JUST TRUE or NOTHING, so `s 479(1)` could never answer JUST TRUE ("barred") for a group company that failed limb (a); the seat case for s 477 with a group company showed it. Fixed by renaming and re-typing (`s 479(3) subsection (3) applies: ...` answers JUST FALSE when its "if" is not met; fork F10) and updating `coa11-tests-ch1.l4`.
12. **The deadlines of s 485A(3) and s 485B(3) are fixed only by the day of the appointment** ("Before an appointment to which this section applies is made"): the regulative rules take the number of days to the appointment as an input and are traced on both sides of it; the text gives no sequence between the audit committee's recommendation and the directors' proposal, so they are two independent rules.

## What the stable binary does not accept, and what it does

The binary governs (1.6.110, main, e51181d; the same counts on 1.6.109).
Measured here on 2026-11-13 with one-line probe files: `length`, `head` and `last` are not defined in the prelude (`I could not find a definition for the identifier`), so the modules write their own recursion over `LIST` (`s 494ZA the last one of the years`, `s 494ZA the first financial year ...`); `min` and `minimum` are defined twice (a NUMBER and a MAYBE NUMBER overload: "multiple definitions"), so the later-of and earlier-of comparisons are written out; `filter`, `any`, `all` and `elem` exist and are used; `add months` with a negative count and `add years` cap at the end of a shorter month (31 March less one month is 28 February).
`#TRACE` with `WITHIN n`, `HENCE FULFILLED` and `LEST BREACH BY ... BECAUSE "..."` runs and prints `FULFILLED` or `DEONTIC BREACHED: BREACH BY ... BECAUSE ...`; `(WAITUNTIL n)` advances the clock.
A DEONTIC value cannot be compared in an `#ASSERT` (the brief and `dialects.md` say so; not re-measured), so no trace is asserted: each trace's expected outcome is written beside it in the test file and was read off the printed result by hand (of the 22 traces in `coa11-tests-ch2-private.l4` and `coa11-tests-ch2-public.l4`, 10 print FULFILLED and 12 print BREACH, each as written beside it), and the same duties are encoded as decision functions with assertions (`s 485A(3)`, `s 485B(3)`, `s 486(2)`, `s 486A(4)`, `s 490(2)`, `s 490A(4)`).
`check.sh` does not see a different trace outcome, so the 22 trace results of the two test files were compared by running each file with 1.6.110 and with 1.6.109 and diffing the results: identical (11 and 11).
Not used because the stable binary does not have them (per the brief): `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` outside `LEST BREACH`, `TYPICALLY` on a field, opaque `DECLARE`, section `GIVEN`, sets, `YMD`. The modules use `Date day month year`, `NOTHING` and `MAYBE` only.
Every `NOT` is parenthesised (`NOT a AND b` reads as `NOT (a AND b)`; not re-measured).

## What `check.sh` printed

Run as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` (target `main`: every module is also run with 1.6.109 and the counts compared). `expected_failed` is empty: no assertion is meant to fail.
The baseline it replaced: the folder as supplied held two modules, `coa-core.l4` and `coa-definitions.l4`, with 0 assertions between them (the keel's own tests, `coa-definitions-tests.l4`, are not in this sandbox).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa11-cases-seat.l4                            0       212       0        0         0 |      0       212       0        0  same
coa11-part16-ch1.l4                            0         0       0        0         0 |      0         0       0        0  same
coa11-part16-ch2-general.l4                    0         0       0        0         0 |      0         0       0        0  same
coa11-part16-ch2-private.l4                    0         0       0        0         0 |      0         0       0        0  same
coa11-part16-ch2-public.l4                     0         0       0        0         0 |      0         0       0        0  same
coa11-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa11-tests-ch1.l4                             0       239       0        0         0 |      0       239       0        0  same
coa11-tests-ch2-general.l4                     0        99       0        0         0 |      0        99       0        0  same
coa11-tests-ch2-private.l4                     0       180       0        0         0 |      0       180       0        0  same
coa11-tests-ch2-public.l4                      0       139       0        0         0 |      0       139       0        0  same
TOTAL (12 modules)                             0       869       0        0           |      0       869       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## Seat questions (the audit of direction required by the brief)

First pass (the brief's audit): every seat question was read against the layer-1 function its body calls for direction; none differed in direction.
Second pass (2026-11-12, requested by the lead): each of the 62 questions was read, name, `@export` text and input `@desc`s, against the BODY of the layer-1 function its `DECIDE` calls, not against that function's title.
28 of the 62 were retitled and 34 stand. By kind (a question can show two kinds, so the lines sum to more than 28):
- direction or modality, 1: `Under section 476(3)` named a last day on which the notice "may" be given, where the text says it "must be given not later than one month before the end of that year".
- a premise or consequence carried in the name, 6: `Under section 479(1)` ("because it was a group company"), `482` ("because its accounts are subject to public sector audit"), `485C(2)` and `489C(2)` ("because they belong to the same network"), `486(3)(b)` and `490(3)(b)` ("by the company's failure to give the notice"); the function takes each as an input or tests it.
- a status stated as a given where the function tests it, 10: "my private company" in `485(1)`, `485A(4)`, `485B(4)`, `485C(1)`, `485C(2)` and "my public company" in `489(1)`, `489A(4)`, `489B(4)`, `489C(1)`, `489C(2)`.
  Each of these functions takes "my company is a private (public) company" as an input, directly or through the applicability of section 485A, 485B, 489A or 489B, and tests it.
  The names now read "my company ..., if it is a private (public) company" for 485(1), 489(1), 485C and 489C, and "if section 485A (485B, 489A, 489B) applies to the appointment" for the four selection-procedure questions.
- a name that asks more or less than the limb the body answers, 11: `476` (the members generally, where the body tests the notice given), `479A` (the exemption is from the audit of individual accounts), `479C(2)`, `479C(3)(a)`, `483(1) and (2)` (not subsection (5)), `485A(5)`, `485A(6)`, `489A(5)`, `489A(6)` ("the requirements" without saying of which subsection), `491(1)(b)` (the name asked whether the auditor "has ceased to hold office" for any reason; the body tests only the end of the term at the accounts meeting next following the appointment) and `494ZA(1)` (the last day of the last financial year, before any extension).
- an actor or tense the text does not have, 4: `485(1)` and `489(1)` (the text is "An auditor or auditors of a private company must be appointed", with no actor; the old name had the company appoint), `485(2)` and `489(2)` ("was made" for a day that may be planned).
Each retitled question has its new name in its `@export` text and in its `DECIDE` name; the input `@desc`s are unchanged, since they ask the same facts.
The cases are generated by question, so `coa11-cases-seat.l4` carries the new names: 100 of its 227 assertions are restated in place with `-- RECONCILED 2026-11-12: was <the original assertion text>; ...`, and no expected value changed.
Negating an answer was not used as a fix anywhere.

Third change (2026-11-13): a gap found by an independent reader of the seat layer.
The seat questions on 485(3) and 489(3) ("may the directors ... appoint an auditor") answer NOTHING for an appointment outside every route the section lists, while the layer-1 rules `s 485(5)` and `s 489(5)` ("may only be appointed") answer JUST FALSE there, and no seat question asked those rules.
5 questions were added, so the seat layer has 67 (62 before):
- Under section 483(5), is an order under section 483(1) barred until a draft of it has been laid before, and approved by resolution of, the Scottish Parliament?
- Under section 485(5), is the appointment of an auditor of my private company made in accordance with a route the subsection allows (section 485, 486 or 486A)?
- Under section 487(1)(b), has the auditor of my private company ceased to hold office at the end of the next period for appointing auditors?
- Under section 489(5), is the appointment of an auditor of my public company made in accordance with a route the subsection allows (section 489, 490 or 490A)?
- Under section 494ZA(3), may the competent authority give its approval to an extension of the maximum engagement period of my company's auditor?
The two on subsection (5) are titled to what the rule answers: `JUST TRUE` for an appointment made by a listed route, `JUST FALSE` outside every route, and (private company only) `NOTHING` for a deemed re-appointment under section 487 ("without prejudice").
They are not titled "may the directors appoint outside the routes the section lists", because the rule's `JUST TRUE` is the listed route, and that title would read it as "yes, outside".
Every layer-1 rule whose source text says "only", "unless", "shall not", "may not", "must not" or "cannot" now has a seat question, alone or inside a wider one:
- a question of its own: 475(1), 475(2), 475(3), 476(3), 479(1), 485(1), 485(5), 485A(4), 485B(4), 485C(1), 485C(2), 487(1)(b), 487(2), 489(1), 489(5), 489A(4), 489B(4), 489C(1), 489C(2), 491(1)(b), 494ZA(1), 494ZA(3);
- answered inside a wider question: 482(2) and 483(2) (the questions on 482 and on 483(1) and (2));
- added in this change because they had none of their own: 485(5), 489(5), 483(5) ("shall not be made unless", the contrapositive of the "only if" of 483(2)), 494ZA(3) (reachable before only inside the question on 494ZA(2)) and 487(1)(b) ("unless re-appointed"; its public-company sibling 491(1)(b) already had one).
The check was a search of the quoted source lines of the four layer-1 modules for those words; it is a check of this list, not a proof that no other rule has the wording.

| seat question | layer-1 rule called |
| --- | --- |
| Under section 475(1), must my company's annual accounts for the year be audited | `s 475(1) the company's annual accounts for the financial year must be audited in accordance with Part 16` |
| Under section 475(2), is my company barred from an audit exemption for want of the directors' statement on the balance sheet | `coa11 seat section 475(2) bar` |
| Under section 475(3), is my company barred from an audit exemption for want of the directors' statements about the members' right and the directors' responsibilities | `s 475(3) the company is barred from the exemption for want of the directors' statements` |
| Under section 475(4), does the directors' statement appear on my company's balance sheet above the signature required by section 414 | `s 475(4) the statement appears on the balance sheet above the signature required by section 414` |
| Under section 476, may the members who give this notice require my company to obtain an audit of its accounts for the year | `s 476(1) the members may by notice require the company to obtain an audit of its accounts for the financial year` |
| Under section 476(3), what is the latest day by which the members of my company must give notice requiring an audit | `s 476(3) the last day on which the notice may be given` |
| Under section 477, is my company entitled to the small companies exemption from audit for the year | `s 477(5) the company is entitled to the exemption conferred by section 477` |
| Under section 478, is my company barred from the small companies exemption by the kind of company it is | `s 478 the company is barred from the small companies exemption` |
| Under section 479(1), is my company barred from the small companies exemption by the rule on group companies | `s 479(1) the company is barred from the small companies exemption as a group company` |
| Under section 479A, is my company entitled to the subsidiary companies exemption from the audit of its individual accounts for the year | `s 479A(3) the company is entitled to the exemption conferred by section 479A` |
| Under section 479B, is my company barred from the subsidiary companies exemption by the kind of company it is | `s 479B the company is barred from the subsidiary companies audit exemption` |
| Under section 479C(2), does the parent undertaking's statement meet the requirements of section 479C(2) (authentication and the listed particulars) | `s 479C(2) the statement meets the requirements` |
| Under section 479C(3)(a), does the parent undertaking's guarantee cover this liability of the subsidiary company | `s 479C(3)(a) the parent undertaking guarantees the liability` |
| Under section 480, is my company entitled to the dormant companies exemption from audit for the year | `s 480(3) the company is entitled to the exemption conferred by section 480` |
| Under section 481, is my company barred from the dormant companies exemption by the kind of company it is | `s 481 the company is barred from the dormant companies exemption` |
| Under section 482, is my company entitled to the exemption from audit for non-profit-making companies subject to public sector audit for the year | `s 482(4) the company is entitled to the exemption conferred by section 482` |
| Under section 483(1) and (2), is my company one in relation to which the Scottish Ministers may make an order providing for its accounts to be audited by the Auditor General for Scotland | `s 483(1) the Scottish Ministers may by order provide for the company's accounts to be audited by the Auditor General for Scotland` |
| Under section 483(5), is an order under section 483(1) barred until a draft of it has been laid before, and approved by resolution of, the Scottish Parliament | `s 483(5) the order may not yet be made` |
| Under section 485(1), must an auditor be appointed for my company for the financial year, if it is a private company | `s 485(1) an auditor or auditors of the private company must be appointed for the financial year` |
| Under section 485(2), what is the last day of my private company's period for appointing auditors | `s 485(2) the period for appointing auditors` (its last day) |
| Under section 485(2), is my private company's appointment of an auditor made before the end of the period for appointing auditors | `s 485(2) the appointment is made before the end of the period for appointing auditors` |
| Under section 485(3), may the directors of my private company appoint an auditor | `s 485(3) the directors may appoint an auditor or auditors of the company` |
| Under section 485(4), may the members of my private company appoint an auditor by ordinary resolution | `s 485(4) the members may appoint an auditor or auditors of the company by ordinary resolution` |
| Under section 485(5), is the appointment of an auditor of my private company made in accordance with a route the subsection allows (section 485, 486 or 486A) | `s 485(5) the appointment is made in accordance with a route the section allows` |
| Under section 485A(4), if section 485A applies to the appointment, must the audit committee or directors of my company carry out a selection procedure | `s 485A(4) the audit committee or the directors must carry out a selection procedure in accordance with Article 16(3) of the Audit Regulation` |
| Under section 485A(5), does the audit committee's recommendation meet the requirements of section 485A(5) | `s 485A(5) the audit committee's recommendation meets the requirements` |
| Under section 485A(6), does the directors' proposal meet the requirements of section 485A(6) | `s 485A(6) the directors' proposal meets the requirements` |
| Under section 485B(4), if section 485B applies to the appointment, must the directors of my company carry out a selection procedure | `s 485B(4) the directors must carry out a selection procedure in accordance with Article 16(3) of the Audit Regulation` |
| Under section 485C(1), is a person barred from appointment as auditor of my company for the financial year, if it is a private company that is a public interest entity | `s 485C(1) the person is barred from appointment as auditor of the company for the financial year` |
| Under section 485C(2), is a person barred from appointment as auditor of my company for the financial year under the network rule of section 485C(2), if it is a private company that is a public interest entity | `s 485C(2) the person is barred as a member of the same network as the auditor mentioned in subsection (1)` |
| Under section 486(2), must my private company give the Secretary of State notice that his power to appoint an auditor has become exercisable | `s 486(2) the company must give the Secretary of State notice that his power has become exercisable` |
| Under section 486(2), did my private company give that notice within one week of the end of the period for appointing auditors | `s 486(2) the company gave the notice within one week of the end of the period for appointing auditors` |
| Under section 486(3)(b), does an officer of my private company commit an offence under section 486 | `s 486(3)(b) the officer commits an offence` |
| Under section 486(4), what is the most the company or an officer can be fined on summary conviction for that offence, in pounds | `s 486(4) the most the person can be fined on summary conviction, in pounds` |
| Under section 486(4), what is the most the company or an officer can be fined for each day of continued contravention, in pounds | `s 486(4) the most the person can be fined for each day of continued contravention, in pounds` |
| Under section 486A(4), did my private company give the Secretary of State notice within one week of becoming aware of the breach | `s 486A(4) the company gave the notice within one week of becoming aware of the breach` |
| Under section 487(1)(b), has the auditor of my private company ceased to hold office at the end of the next period for appointing auditors | `s 487(1)(b) the auditor or auditors have ceased to hold office` |
| Under section 487(2), is the auditor of my private company deemed to be re-appointed | `s 487(2) the auditor in office is deemed to be re-appointed` |
| Under section 488(1), is the deemed re-appointment of the auditor of my private company prevented by the members' notices | `s 488(1) the deemed re-appointment is prevented by the members` |
| Under section 488(3), is the members' notice to my private company a valid notice under section 488 | `s 488(3) the notice is a notice under section 488` |
| Under section 489(1), must an auditor be appointed for my company for the financial year, if it is a public company | `s 489(1) an auditor or auditors of the public company must be appointed for the financial year` |
| Under section 489(2), is my public company's appointment of an auditor made before the end of the accounts meeting at which the previous year's accounts and reports are laid | `s 489(2) the appointment is made before the end of the accounts meeting` |
| Under section 489(3), may the directors of my public company appoint an auditor | `s 489(3) the directors may appoint an auditor or auditors of the company` |
| Under section 489(4), may the members of my public company appoint an auditor by ordinary resolution | `s 489(4) the members may appoint an auditor or auditors of the company by ordinary resolution` |
| Under section 489(5), is the appointment of an auditor of my public company made in accordance with a route the subsection allows (section 489, 490 or 490A) | `s 489(5) the appointment is made in accordance with a route the section allows` |
| Under section 489A(4), if section 489A applies to the appointment, must the audit committee or directors of my company carry out a selection procedure | `s 489A(4) the audit committee or the directors must carry out a selection procedure in accordance with Article 16(3) of the Audit Regulation` |
| Under section 489A(5), does the audit committee's recommendation meet the requirements of section 489A(5) | `s 489A(5) the audit committee's recommendation meets the requirements` |
| Under section 489A(6), does the directors' proposal meet the requirements of section 489A(6) | `s 489A(6) the directors' proposal meets the requirements` |
| Under section 489B(4), if section 489B applies to the appointment, must the directors of my company carry out a selection procedure | `s 489B(4) the directors must carry out a selection procedure in accordance with Article 16(3) of the Audit Regulation` |
| Under section 489C(1), is a person barred from appointment as auditor of my company for the financial year, if it is a public company that is a public interest entity | `s 489C(1) the person is barred from appointment as auditor of the company for the financial year` |
| Under section 489C(2), is a person barred from appointment as auditor of my company for the financial year under the network rule of section 489C(2), if it is a public company that is a public interest entity | `s 489C(2) the person is barred as a member of the same network as the auditor mentioned in subsection (1)` |
| Under section 490(2), must my public company give the Secretary of State notice that his power to appoint an auditor has become exercisable | `s 490(2) the company must give the Secretary of State notice that his power has become exercisable` |
| Under section 490(2), did my public company give that notice within one week of the end of the accounts meeting | `s 490(2) the company gave the notice within one week of the end of the accounts meeting` |
| Under section 490(3)(b), does an officer of my public company commit an offence under section 490 | `s 490(3)(b) the officer commits an offence` |
| Under section 490(4), what is the most the company or an officer can be fined on summary conviction for that offence, in pounds | `s 490(4) the most the person can be fined on summary conviction, in pounds` |
| Under section 490(4), what is the most the company or an officer can be fined for each day of continued contravention, in pounds | `s 490(4) the most the person can be fined for each day of continued contravention, in pounds` |
| Under section 490A(4), did my public company give the Secretary of State notice within one week of becoming aware of the breach | `s 490A(4) the company gave the notice within one week of becoming aware of the breach` |
| Under section 491(1)(b), has the auditor of my public company ceased to hold office at the conclusion of the accounts meeting next following their appointment | `s 491(1)(b) the auditor or auditors have ceased to hold office` |
| Under section 492, who must fix the remuneration of my company's auditor | `s 492(1) to (3) who must fix the auditor's remuneration` |
| Under section 492(4), is a sum paid in respect of expenses part of the auditor's remuneration | `s 492(4) the sum is part of the auditor's remuneration` |
| Under section 494ZA(1), what is the last day of the last financial year of the maximum engagement period of my company's auditor, before any extension | `s 494ZA(1) the last financial year of the maximum engagement period` |
| Under section 494ZA(2), may the maximum engagement period of my company's auditor be extended by the period I have in mind | `s 494ZA(2) the maximum engagement period may be extended by the period` |
| Under section 494ZA(3), may the competent authority give its approval to an extension of the maximum engagement period of my company's auditor | `s 494ZA(3) the competent authority may give its approval` |
| Under section 494A, is my company a public interest entity | `s 494A "public interest entity" the entity is a public interest entity` |
| Under section 494A, is this body an audit committee | `s 494A "audit committee" the body is an audit committee` |
| Under section 494A, do these persons form a network | `s 494A "network" the association is a network` |
| Under section 494A, is this person an Auditor General | `s 494A "Auditor General" the person is an Auditor General` |

## Open questions for a domain expert

1. Which printed version of s 475(2) is in force (fork F2, finding 1)?
2. Is a company in none of the exemptions "not exempt" (JUST FALSE) or "not covered" (NOTHING) under s 477, 479A, 480 and 482 (fork F1)?
3. Does a misplaced balance sheet statement (s 475(4)) defeat the exemption, or is s 475(4) a separate duty (fork F5)?
4. How is the "last financial year for which the auditor was appointed following a qualifying selection procedure" read in s 494ZA(1), sub-case (ii) against sub-case (iii) (fork F20, finding 7)?
5. What are "the necessary modifications" of s 494ZA(4)(a) (fork F23)?
6. Do the omitted words after "audit committee" and "public interest entity" in s 494A leave the definitions closed (fork F21)?

## Peeked

No existing encoding of any Act, no directory under `runs/` other than `dst-coa11/`, no `memory/`, `projects/` memory file, `state/` or `tmp` of `<local tool>` was read.
Two things worth declaring: (1) the harness saved the output of my own `sed -n 6543,6969p` command (the Act's text for my range, which was too large to print inline) to a file under `<local tool>`, and I read that file with the Read tool; it holds only the raw text of lines 6543-6969, not a note, a memory or an encoding. (2) I read the language library `jl4-core/libraries/daydate.l4` of the l4-ide checkout to learn the names of the date functions (`add months`, `add years`, `Day`, `Date`); it is a library of the language, not an encoding of an Act.

## Index of the layer-1 names

Full names of every top-level function and type of the four layer-1 modules that begins with a section label (constructors and fields are declared beside their type).

**coa11-part16-ch1.l4** (41 names)

- `s 475 exemption`
- `s 475(1) the company's annual accounts for the financial year must be audited in accordance with Part 16`
- `s 475(2) (first printed version) the company is barred from the exemption for want of the directors' statement`
- `s 475(2) (second printed version) the company is barred from the exemption for want of the directors' statement`
- `s 475(3) the company is barred from the exemption for want of the directors' statements`
- `s 475(4) the statement appears on the balance sheet above the signature required by section 414`
- `s 475(2) to (4) the exemption is in force once the restrictions on it are taken together`
- `s 476(2) the notice is given by enough members`
- `s 476(3) the last day on which the notice may be given`
- `s 476(3) the notice is given in time`
- `s 476(1) the members may by notice require the company to obtain an audit of its accounts for the financial year`
- `s 477(1) the company is exempt from audit under section 477`
- `s 477(5) the company is entitled to the exemption conferred by section 477`
- `s 478 the company is barred from the small companies exemption`
- `s 479(4)(a) the company is a group company`
- `s 479(4) the two undertakings are associated`
- `s 479(4)(b) the undertaking belongs to the group of the group company`
- `s 479(6) the body is treated as a company for the purposes of section 479(5)`
- `s 479(3) subsection (3) applies: the company is not excluded by subsection (1)`
- `s 479(1) the company is barred from the small companies exemption as a group company`
- `s 479A(1) the company is within the subsidiary companies audit exemption`
- `s 479A(2)(e) documents delivered to the registrar`
- `s 479A(2)(e) one document was delivered on or before the date the directors file the accounts`
- `s 479A(2)(e) the five documents were delivered on or before the date the directors file the accounts`
- `s 479A(2) the conditions of the exemption are complied with`
- `s 479A(3) the company is entitled to the exemption conferred by section 479A`
- `s 479B the company is barred from the subsidiary companies audit exemption`
- `s 479C(1) a guarantee is given by the parent undertaking`
- `s 479C(2) the statement meets the requirements`
- `s 479C(3)(a) the parent undertaking guarantees the liability`
- `s 479C(3)(b) the person may enforce the guarantee against the parent undertaking`
- `s 480(2) the conditions for the dormant companies exemption are met`
- `s 480(1) the company is exempt from audit under section 480`
- `s 480(3) the company is entitled to the exemption conferred by section 480`
- `s 481 the company is barred from the dormant companies exemption`
- `s 482(1) route of public sector audit`
- `s 482(1) the requirements of Part 16 as to audit of accounts do not apply to the company`
- `s 482(4) the company is entitled to the exemption conferred by section 482`
- `s 483(1) the Scottish Ministers may by order provide for the company's accounts to be audited by the Auditor General for Scotland`
- `s 483(3) the accounts are accounts falling within paragraph (a) or (b) of subsection (3)`
- `s 483(5) the order may not yet be made`

**coa11-part16-ch2-private.l4** (57 names)

- `s 485(1) an auditor or auditors of the private company must be appointed for the financial year`
- `s 485(2) period for appointing auditors`
- `s 485(2) the period for appointing auditors`
- `s 485(2) the last day of the 28 days beginning with`
- `s 485(2) the appointment is made before the end of the period for appointing auditors`
- `s 485(3) the directors may appoint an auditor or auditors of the company`
- `s 485(4) the members may appoint an auditor or auditors of the company by ordinary resolution`
- `s 485(5) the appointment is made in accordance with a route the section allows`
- `s 485A(1) the section applies to the appointment`
- `s 485A party`
- `s 485A act`
- `s 485A(3)(a) the audit committee must make a recommendation to the directors before the appointment is made`
- `s 485A(3)(b) the directors must propose an auditor or auditors for appointment before the appointment is made`
- `s 485A(3) the audit committee recommended and the directors proposed before the appointment was made`
- `s 485A(4) the audit committee or the directors must carry out a selection procedure in accordance with Article 16(3) of the Audit Regulation`
- `s 485A(5) the audit committee's recommendation meets the requirements`
- `s 485A(6) the directors' proposal meets the requirements`
- `s 485B(1) the section applies to the appointment`
- `s 485B party`
- `s 485B act`
- `s 485B(3) the directors must propose an auditor or auditors for appointment before the appointment is made`
- `s 485B(3) the directors proposed an auditor or auditors before the appointment was made`
- `s 485B(4) the directors must carry out a selection procedure in accordance with Article 16(3) of the Audit Regulation`
- `s 485B(4) the proposed auditor or auditors are drawn from the selection procedure`
- `s 485C(1) the first day of the period of 4 years`
- `s 485C(1) the last day of the period of 4 years`
- `s 485C(1) the person is barred from appointment as auditor of the company for the financial year`
- `s 485C(2) the person is barred as a member of the same network as the auditor mentioned in subsection (1)`
- `s 486(1) the Secretary of State may appoint one or more persons to fill the vacancy`
- `s 486(2) the company must give the Secretary of State notice that his power has become exercisable`
- `s 486 act`
- `s 486(2) the company must give notice to the Secretary of State within one week of the end of the period for appointing auditors`
- `s 486(2) the company gave the notice within one week of the end of the period for appointing auditors`
- `s 486(3)(a) the company commits an offence`
- `s 486(3)(b) the officer commits an offence`
- `s 486(4) the penalty for an offence under section 486`
- `s 486(4) the most the person can be fined on summary conviction, in pounds`
- `s 486(4) the most the person can be fined for each day of continued contravention, in pounds`
- `s 486A(1) the Secretary of State may appoint another auditor or auditors in place of the auditor or auditors appointed`
- `s 486A(2) the breach invalidates the report`
- `s 486A(3) sections 1248 and 1249 apply as if the auditor was not an appropriate person for the period during which the audit was conducted`
- `s 486A act`
- `s 486A(4) the company must give notice to the Secretary of State within one week of becoming aware of the breach`
- `s 486A(4) the company gave the notice within one week of becoming aware of the breach`
- `s 486A(5)(a) the company commits an offence`
- `s 486A(5)(b) the officer commits an offence`
- `s 486A(6) the penalty for an offence under section 486A`
- `s 486A(6) the most the person can be fined on summary conviction, in pounds`
- `s 486A(6) the most the person can be fined for each day of continued contravention, in pounds`
- `s 487(1)(a) the auditor or auditors cannot yet take office`
- `s 487(1)(b) the auditor or auditors have ceased to hold office`
- `s 487(2) the auditor in office is deemed to be re-appointed`
- `s 487(3) the deemed re-appointment prejudices the provision`
- `s 487(4) the loss is taken into account in ascertaining the compensation or damages payable to the auditor`
- `s 488(2) the requisite percentage`
- `s 488(3) the notice is a notice under section 488`
- `s 488(1) the deemed re-appointment is prevented by the members`

**coa11-part16-ch2-public.l4** (49 names)

- `s 489(1) an auditor or auditors of the public company must be appointed for the financial year`
- `s 489(2) the appointment is made before the end of the accounts meeting`
- `s 489(3) the directors may appoint an auditor or auditors of the company`
- `s 489(4) the members may appoint an auditor or auditors of the company by ordinary resolution`
- `s 489(5) the appointment is made in accordance with a route the section allows`
- `s 489A(1) the section applies to the appointment`
- `s 489A party`
- `s 489A act`
- `s 489A(3)(a) the audit committee must make a recommendation to the directors before the appointment is made`
- `s 489A(3)(b) the directors must propose an auditor or auditors for appointment before the appointment is made`
- `s 489A(3) the audit committee recommended and the directors proposed before the appointment was made`
- `s 489A(4) the audit committee or the directors must carry out a selection procedure in accordance with Article 16(3) of the Audit Regulation`
- `s 489A(5) the audit committee's recommendation meets the requirements`
- `s 489A(6) the directors' proposal meets the requirements`
- `s 489B(1) the section applies to the appointment`
- `s 489B party`
- `s 489B act`
- `s 489B(3) the directors must propose an auditor or auditors for appointment before the appointment is made`
- `s 489B(3) the directors proposed an auditor or auditors before the appointment was made`
- `s 489B(4) the directors must carry out a selection procedure in accordance with Article 16(3) of the Audit Regulation`
- `s 489B(4) the proposed auditor or auditors are drawn from the selection procedure`
- `s 489C(1) the first day of the period of 4 years`
- `s 489C(1) the last day of the period of 4 years`
- `s 489C(1) the person is barred from appointment as auditor of the company for the financial year`
- `s 489C(2) the person is barred as a member of the same network as the auditor mentioned in subsection (1)`
- `s 490(1) the Secretary of State may appoint one or more persons to fill the vacancy`
- `s 490(2) the company must give the Secretary of State notice that his power has become exercisable`
- `s 490 act`
- `s 490(2) the company must give notice to the Secretary of State within one week of the end of the accounts meeting`
- `s 490(2) the company gave the notice within one week of the end of the accounts meeting`
- `s 490(3)(a) the company commits an offence`
- `s 490(3)(b) the officer commits an offence`
- `s 490(4) the penalty for an offence under section 490`
- `s 490(4) the most the person can be fined on summary conviction, in pounds`
- `s 490(4) the most the person can be fined for each day of continued contravention, in pounds`
- `s 490A(1) the Secretary of State may appoint another auditor or auditors in place of the auditor or auditors appointed`
- `s 490A(2) the breach invalidates the report`
- `s 490A(3) sections 1248 and 1249 apply as if the auditor was not an appropriate person for the period during which the audit was conducted`
- `s 490A act`
- `s 490A(4) the company must give notice to the Secretary of State within one week of becoming aware of the breach`
- `s 490A(4) the company gave the notice within one week of becoming aware of the breach`
- `s 490A(5)(a) the company commits an offence`
- `s 490A(5)(b) the officer commits an offence`
- `s 490A(6) the penalty for an offence under section 490A`
- `s 490A(6) the most the person can be fined on summary conviction, in pounds`
- `s 490A(6) the most the person can be fined for each day of continued contravention, in pounds`
- `s 491(1)(a) the auditor or auditors cannot yet take office`
- `s 491(1)(b) the auditor or auditors have ceased to hold office`
- `s 491(2) the term of office rule prejudices the provision`

**coa11-part16-ch2-general.l4** (26 names)

- `s 492 way the auditor was appointed`
- `s 492 who fixes the remuneration`
- `s 492(1) to (3) who must fix the auditor's remuneration`
- `s 492(4) the sum is part of the auditor's remuneration`
- `s 492(5) the section applies to the benefit as to a payment of money`
- `s 494ZA financial year`
- `s 494ZA the last financial year of the company to begin before the day`
- `s 494ZA the last financial year of the company to begin within the period of years beginning with the day`
- `s 494ZA the last one of the years`
- `s 494ZA the first financial year of the company to begin on or after the day`
- `s 494ZA the later of the two years`
- `s 494ZA the earlier of the two years`
- `s 494ZA(1) the last financial year of the maximum engagement period`
- `s 494ZA(1) the Table applied to the first financial year`
- `s 494ZA(2) the maximum engagement period may be extended by the period`
- `s 494ZA(2) the last day of the maximum engagement period as extended`
- `s 494ZA(3) the competent authority may give its approval`
- `s 494ZA(4)(a) the second column of the Table has effect with the necessary modifications`
- `s 494ZA(4)(b) the appointment meets the requirement of a qualifying selection procedure`
- `s 494ZA(5) compliance of the selection procedure`
- `s 494ZA(5) the selection procedure is a qualifying selection procedure`
- `s 494A "audit committee" the body is an audit committee`
- `s 494A "Auditor General" the person is an Auditor General`
- `s 494A "issuer" the person is an issuer`
- `s 494A "network" the association is a network`
- `s 494A "public interest entity" the entity is a public interest entity`

